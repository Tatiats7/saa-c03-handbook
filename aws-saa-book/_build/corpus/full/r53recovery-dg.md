# Amazon Application Recovery Controller (ARC) Developer Guide

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
+ [What is ARC?](#what-is-route53-recovery)
+ [Amazon Application Recovery Controller (ARC) readiness check availability change](#arc-readiness-availability-change)
+ [Compare multi-AZ and multi-Region recovery capabilities in ARC](#compare-capabilities)
+ [Use zonal shift and zonal autoshift to recover applications in ARC](#multi-az)
   + [Zonal shift in ARC](#arc-zonal-shift)
      + [How a zonal shift works](#arc-zonal-shift.how-it-works)
      + [AWS Region availability for zonal shift](#introduction-regions-zonal)
      + [Zonal shift components](#introduction-components-zonal)
      + [Data and control planes for zonal shift](#data-and-control-planes-zonal-shift)
      + [Pricing for zonal shift in ARC](#introduction-pricing-zonal-shift)
      + [Best practices for zonal shifts in ARC](#route53-arc-best-practices.zonal-shifts)
      + [Zonal shift API operations](#actions.zonalshift)
      + [Examples of using the AWS CLI with zonal shift](#getting-started-cli-zonalshift)
      + [Supported resources](#arc-zonal-shift.resource-types)
         + [Amazon EC2 Auto Scaling groups](#arc-zonal-shift.resource-types.ec2-auto-scaling-groups)
         + [Amazon Elastic Kubernetes Service](#arc-zonal-shift.resource-types.eks)
         + [Application Load Balancers](#arc-zonal-shift.resource-types.app-load-balancers)
         + [Network Load Balancers](#arc-zonal-shift.resource-types.network-load-balancers)
      + [Starting, updating, or canceling a zonal shift](#arc-zonal-shift.start-cancel)
      + [Logging and monitoring for zonal shift in Amazon Application Recovery Controller (ARC)](#monitoring-zonal-shift)
         + [Logging zonal shift API calls using AWS CloudTrail](#cloudtrail-zonal-shift)
      + [Identity and Access Management for zonal shift in ARC](#security-iam-zonalshift)
         + [How zonal shift works with IAM](#security_iam_service-with-iam-zs)
         + [IAM and permissions for zonal shift](#security_iam_service-with-iam-zonal-shift)
         + [Identity-based policy examples for zonal shift in ARC](#security_iam_id-based-policy-examples-zonal)
   + [Zonal autoshift in ARC](#arc-zonal-autoshift)
      + [How zonal autoshift and practice runs work](#arc-zonal-autoshift.how-it-works)
         + [About zonal autoshift](#arc-zonal-autoshift.how-it-works.about)
         + [When AWS starts and stops autoshifts](#arc-zonal-autoshift.how-it-works.start-stop-auto)
         + [When ARC schedules, starts, and ends practice runs](#arc-zonal-autoshift.how-it-works.scheduled-practice-runs)
         + [Capacity checks for practice runs](#arc-zonal-autoshift.how-it-works.capacity-check)
         + [Notification for practice runs and autoshifts](#arc-zonal-autoshift.how-it-works.notifications)
         + [Precedence for zonal shifts](#arc-zonal-autoshift.how-it-works.precedence)
         + [Stopping an active autoshift or practice run for a resource](#arc-zonal-autoshift.how-it-works.stop-shift)
         + [How traffic is shifted away](#arc-zonal-autoshift.how-it-works.how-traffic-shifted)
         + [Alarms for practice runs](#arc-zonal-autoshift.how-it-works.alarms)
         + [Blocked windows and allowed windows (in UTC)](#arc-zonal-autoshift.how-it-works.blocked-windows)
      + [AWS Region availability for zonal autoshift](#introduction-region-zonal-autoshift)
      + [Zonal autoshift components](#introduction-components-zonal-autoshift)
      + [Data and control planes for zonal autoshift](#data-and-control-planes-zonal-autoshift)
      + [Pricing for zonal autoshift in ARC](#introduction-pricing-zonal-autoshift)
      + [Best practices when you configure zonal autoshift](#arc-zonal-autoshift.considerations)
      + [Zonal autoshift API operations](#actions.zonalautoshift)
      + [Examples of using the AWS CLI with zonal autoshift](#getting-started-cli-zonal-autoshift)
         + [Create a practice run configuration](#getting-started-cli-update-zonal_autoshift.create-practice-run)
         + [Enable or disable autoshifts](#getting-started-cli-zonal-autoshift.update-autoshift)
         + [Start an on-demand practice run](#getting-started-cli-zonal-autoshift.start-practice-run)
         + [Cancel an in-progress practice run](#getting-started-cli-zonal-autoshift.cancel-practice-run)
         + [Cancel an in-progress autoshift](#getting-started-cli-zonal-autoshift.cancel-autoshift)
         + [Edit a practice run configuration](#getting-started-cli-zonal_autoshift.edit-practice-run-config)
         + [Delete a practice run configuration](#getting-started-cli-zonal-autoshift.delete-practice-run-config)
      + [Enabling and working with zonal autoshift](#arc-zonal-autoshift.start-cancel)
         + [Configuring, editing, or deleting a practice run configuration](#arc-zonal-autoshift.edit-delete-practice-run)
         + [Canceling a zonal autoshift](#arc-zonal-autoshift.canceling-an-autoshift)
         + [Starting a practice run zonal shift](#arc-zonal-autoshift.start-practice-run)
         + [Canceling a practice run zonal shift](#arc-zonal-autoshift.cancel-practice-run)
         + [Enabling or disabling autoshift observer notification](#arc-zonal-autoshift.enable-autoshift-observer)
      + [Testing zonal autoshift with AWS FIS](#testing-zonal-autoshift-fis)
      + [Logging and monitoring for zonal autoshift in Amazon Application Recovery Controller (ARC)](#monitoring-zonal-autoshift)
         + [Logging zonal autoshift API calls using AWS CloudTrail](#cloudtrail-zonal-autoshift)
         + [Using zonal autoshift with Amazon EventBridge](#eventbridge-zonal-autoshift)
      + [Identity and Access Management for zonal autoshift in ARC](#security-iam-zonalautoshift)
         + [How zonal autoshift in ARC works with IAM](#security_iam_service-with-iam-zonalautoshift)
         + [Identity-based policy examples for zonal autoshift in ARC](#security_iam_id-based-policy-examples-zonalautoshift)
         + [Using the service-linked role for zonal autoshift in ARC](#using-service-linked-roles-zonal-autoshift)
         + [AWS managed policies for zonal autoshift in ARC](#security-iam-awsmanpol-zonal-autoshift)
      + [Quotas for zonal autoshift](#quotas.zonal-autoshift)
+ [Use routing control to recover multi-Region applications in ARC](#multi-region)
   + [Routing control in ARC](#routing-control)
      + [About routing control](#routing-control.about)
      + [AWS Region availability for routing control](#introduction-regions-routing)
      + [Routing control components](#introduction-components-routing)
      + [Data and control planes for routing control](#data-and-control-planes)
      + [Tagging for routing control in Amazon Application Recovery Controller (ARC)](#introduction-tagging-routing-control)
      + [Pricing for routing control in ARC](#introduction-pricing-routing-control)
      + [Getting started with multi-Region recovery in Amazon Application Recovery Controller (ARC)](#getting-started)
      + [Best practices for routing control in ARC](#route53-arc-best-practices.regional)
      + [Routing control API operations](#actions.routing-control)
         + [Using this service with an AWS SDK](#sdk-general-information-section)
      + [Examples of using ARC routing control API operations with the AWS CLI](#getting-started-cli-routing)
         + [Set up routing control components](#getting-started-cli-routing-config)
         + [List and update routing controls and states with the AWS CLI](#getting-started-cli-routing.control-state)
      + [Working with routing control components in ARC](#routing-control.working-with)
         + [Creating routing control components in ARC](#routing-control.create)
            + [Creating a cluster in ARC](#routing-control.create-cluster)
            + [Creating a routing control in ARC](#routing-control.create-control)
            + [Creating a routing control health check in ARC](#routing-control.create-health-check)
            + [Creating a control panel in ARC](#routing-control.create-control-panel)
         + [Viewing and updating routing control states in ARC](#routing-control.update)
            + [Getting and updating routing control states using the ARC API (recommended)](#routing-control.update.api)
            + [Getting and updating routing control states in the AWS Management Console](#routing-control.update.console)
         + [Creating safety rules for routing control](#routing-control.safety-rules)
            + [Creating a safety rule on the console](#routing-control.create-safety-rule)
            + [Editing or deleting a safety rule on the console](#routing-control.edit-delete-safety-rule)
            + [Overriding safety rules to reroute traffic](#routing-control.override-safety-rule)
         + [Support cross-account for clusters in ARC](#routing-control.failover-different-accounts)
      + [Logging and monitoring for routing control in Amazon Application Recovery Controller (ARC)](#monitoring-routing)
         + [Logging ARC API calls using AWS CloudTrail](#cloudtrail-routing)
      + [Identity and Access Management for routing control in ARC](#security-iam-routing)
         + [How routing control in Amazon Application Recovery Controller (ARC) works with IAM](#security_iam_service-with-iam-routing)
         + [Identity-based policy examples for routing control in ARC](#security_iam_id-based-policy-examples-routing)
         + [AWS managed policies for routing control in Amazon Application Recovery Controller (ARC)](#security-iam-awsmanpol-routing)
      + [Quotas for routing control](#routing-control.quotas)
   + [Readiness check in ARC](#recovery-readiness)
      + [What is readiness check in Amazon Application Recovery Controller (ARC)?](#readiness-what-is)
         + [How readiness rules determine readiness status](#recovery-readiness.rules)
         + [How readiness checks, resource sets, and readiness scopes work together](#recovery-readiness.recovery-groups.readiness-scope)
         + [DNS target resource readiness checks: Auditing resiliency readiness](#recovery-readiness.readiness-checks.architectural)
         + [Readiness checks and disaster recovery scenarios](#recovery-readiness.disaster)
      + [AWS Region availability for readiness check](#introduction-regions-readiness)
      + [Readiness check components](#introduction-components-readiness)
      + [Data and control planes for readiness check](#data-and-control-planes-readiness)
      + [Tagging for readiness check in Amazon Application Recovery Controller (ARC)](#introduction-tagging-readiness)
      + [Pricing for readiness check in ARC](#introduction-pricing-readiness)
      + [Best practices for readiness check in ARC](#route53-arc-best-practices.readiness)
      + [Readiness check API operations](#actions.readiness)
      + [Examples of using ARC readiness check API operations with the AWS CLI](#getting-started-cli-readiness)
      + [Working with recovery groups and readiness checks](#recovery-readiness.recovery-groups-and-readiness-checks)
         + [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups)
         + [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set)
      + [Monitoring readiness status in ARC](#recovery-readiness.status)
      + [Getting architecture recommendations in ARC](#recovery-readiness.evaluate-arch)
      + [Creating cross-account authorizations in ARC](#recovery-readiness.cross-account)
      + [Readiness rules, resource types, and ARNS](#recovery-readiness.rules-and-resource-types)
         + [Readiness rules descriptions in ARC](#recovery-readiness.rules-resources)
         + [Resource types and ARN formats in ARC](#recovery-readiness.resource-types-arns)
      + [Logging and monitoring for readiness check in Amazon Application Recovery Controller (ARC)](#monitoring-readiness)
         + [Using Amazon CloudWatch with readiness check in ARC](#cloudwatch-readiness)
         + [Logging readiness check API calls using AWS CloudTrail](#cloudtrail-readiness)
         + [Using readiness check in ARC with Amazon EventBridge](#eventbridge-readiness)
      + [Identity and Access Management for readiness check in ARC](#security-iam-readiness)
         + [How readiness check in Amazon Application Recovery Controller (ARC) works with IAM](#security_iam_service-with-iam-readiness)
         + [Identity-based policy examples for readiness check in ARC](#security_iam_id-based-policy-examples-readiness)
         + [Using service-linked role for readiness check in ARC](#using-service-linked-roles-readiness)
         + [AWS managed policies for readiness check in ARC](#security-iam-awsmanpol-readiness)
      + [Quotas for readiness check](#recovery-readiness.quotas)
   + [Region switch in ARC](#region-switch)
      + [About Region switch](#region-switch-plans)
         + [AWS Regions](#aws-regions-rs)
         + [Region switch components](#components-rs)
         + [Reliability of Region switch as a recovery platform](#data-and-control-planes-rs)
         + [Tagging for ARC Region switch;](#tagging.region-switch)
         + [Pricing for Region switch in ARC](#pricing-rs)
      + [Best practices for Region switch in ARC](#best-practices.region-switch)
      + [Tutorial: Create an active/passive Region switch plan](#tutorial-region-switch)
      + [Tutorial: Configure plan execution report autogeneration](#tutorial-report-generation)
      + [Tutorial: Execute an RDS post-recovery workflow](#tutorial-post-recovery)
      + [Region switch API operations](#actions.region-switch)
      + [Working with Region switch](#working-with-rs)
         + [Plan evaluation for Region switch plans](#working-with-rs-plan-evaluation)
         + [Working with service quota checks](#working-with-rs-service-quota-checks)
         + [Create a Region switch plan](#working-with-rs-create-plan)
         + [Create Region switch plan workflows](#working-with-rs-workflows)
         + [Add execution blocks](#working-with-rs-execution-blocks)
            + [ARC Region switch plan execution block](#region-switch-plan-block)
            + [Amazon EC2 Auto Scaling group execution block](#ec2-auto-scaling-block)
            + [Amazon EKS resource scaling execution block](#eks-resource-scaling-block)
            + [Amazon ECS service scaling execution block](#ecs-service-scaling-block)
            + [ARC routing control execution block](#arc-routing-controls-block)
            + [Amazon Aurora Global Database execution block](#aurora-global-database-block)
            + [Amazon DocumentDB Global Cluster execution block](#documentdb-global-cluster-block)
            + [Aurora Provisioned Scaling execution block](#aurora-provisioned-scaling-block)
            + [Aurora Serverless Scaling execution block](#aurora-serverless-scaling-block)
            + [Amazon Neptune Global Cluster execution block](#neptune-global-database-block)
            + [Amazon RDS Promote Read Replica execution block](#rds-promote-read-replica-block)
            + [Amazon RDS Create Cross-Region Replica execution block](#rds-create-cross-region-replica-block)
            + [Amazon RDS Switchover Read Replica execution block](#rds-switchover-read-replica-block)
            + [Manual approval execution block](#manual-approval-block)
            + [Custom action Lambda execution block](#custom-action-lambda-block)
            + [Amazon Route 53 health check execution block](#route53-health-check-block)
            + [Lambda event source mapping execution block](#lambda-event-source-mapping-block)
         + [Create child plans](#working-with-rs-child-plan)
         + [Create a trigger for a Region switch plan](#working-with-rs-triggers)
         + [Execute a Region switch plan to recover an application](#plan-execution-rs)
      + [Region switch dashboards](#region-switch.dashboarding-and-reports)
      + [Cross-account support in Region switch](#cross-account-resources-rs)
         + [Support sharing plans across accounts for ARC Region switch](#resource-sharing.region-switch)
      + [Identity and Access Management for Region switch in ARC](#security-iam-region-switch)
         + [How Region switch in ARC works with IAM](#security_iam_service-with-iam-region-switch)
         + [Identity-based policy examples for Region switch in ARC](#security_iam_id-based-policy-examples-region-switch)
            + [Plan execution role trust policy](#security_iam_region_switch_trust_policy)
            + [Full access permissions](#security_iam_region_switch_full_access)
            + [Read-only permissions](#security_iam_region_switch_read_only)
            + [Execution block permissions](#security_iam_region_switch_execution_blocks)
               + [EC2 Auto Scaling execution block sample policy](#security_iam_region_switch_ec2_autoscaling)
               + [Amazon EKS resource scaling execution block sample policy](#security_iam_region_switch_eks)
               + [Amazon ECS service scaling execution block sample policy](#security_iam_region_switch_ecs)
               + [ARC routing controls execution block sample policy](#security_iam_region_switch_arc_routing)
               + [Aurora Global Database execution block sample policy](#security_iam_region_switch_aurora)
               + [Amazon DocumentDB Global Cluster execution block sample policy](#security_iam_region_switch_documentdb)
               + [Amazon Neptune Global Cluster execution block sample policy](#security_iam_region_switch_neptune)
               + [Amazon RDS execution block sample policy](#security_iam_region_switch_rds)
               + [Aurora provisioned scaling execution block sample policy](#security_iam_region_switch_aurora_provisioned_scaling)
               + [Aurora serverless scaling execution block sample policy](#security_iam_region_switch_aurora_serverless_scaling)
               + [Amazon RDS Switchover Read Replica execution block sample policy](#security_iam_region_switch_rds_switchover_read_replica)
               + [Manual approval execution block sample policy](#security_iam_region_switch_manual_approval)
               + [Custom action Lambda execution block sample policy](#security_iam_region_switch_lambda)
               + [Route 53 health check execution block sample policy](#security_iam_region_switch_route53)
               + [Lambda event source mapping execution block sample policy](#security_iam_region_switch_lambda_esm)
               + [Region switch plan execution block sample policy](#security_iam_region_switch_plan_execution)
            + [CloudWatch alarms for application health permissions](#security_iam_region_switch_cloudwatch)
            + [Automatic plan execution reports permissions](#security_iam_region_switch_reports)
            + [Cross-account resource permissions](#security_iam_region_switch_cross_account)
            + [Complete plan execution role permissions](#security_iam_region_switch_complete_policy)
      + [Logging and monitoring for Region switch in ARC](#logging-and-monitoring-rs)
         + [Logging Region switch API calls using AWS CloudTrail](#cloudtrail-region-switch)
         + [Using Region switch in ARC with Amazon EventBridge](#eventbridge-region-switch)
      + [Quotas for Region switch](#quotas.region-switch)
+ [Code examples for Application Recovery Controller using AWS SDKs](#service_code_examples)
   + [Basic examples for Application Recovery Controller using AWS SDKs](#service_code_examples_basics)
      + [Actions for Application Recovery Controller using AWS SDKs](#service_code_examples_actions)
         + [Use GetRoutingControlState with an AWS SDK](#example_route53-recovery-cluster_GetRoutingControlState_section)
         + [Use UpdateRoutingControlState with an AWS SDK](#example_route53-recovery-cluster_UpdateRoutingControlState_section)
+ [Security in Amazon Application Recovery Controller](#security)
   + [Data protection in Amazon Application Recovery Controller](#data-protection)
   + [Identity and Access Management for Amazon Application Recovery Controller (ARC)](#security-iam)
      + [How Amazon Application Recovery Controller (ARC) capabilities work with IAM](#security_iam_service-with-iam)
      + [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](#security_iam_id-based-policy-examples)
      + [AWS managed policies for Amazon Application Recovery Controller (ARC)](#security-iam-awsmanpol)
      + [Troubleshooting Amazon Application Recovery Controller (ARC) identity and access](#security_iam_troubleshoot)
      + [Access Amazon Application Recovery Controller (ARC) zonal shift using an interface endpoint (AWS PrivateLink)](#vpc-interface-endpoints)
   + [Logging and monitoring in ARC](#logging-and-monitoring)
   + [Compliance validation for Amazon Application Recovery Controller](#r53-recovery-controller-compliance)
   + [Resilience in Amazon Application Recovery Controller](#disaster-recovery-resiliency)
   + [Infrastructure security in Amazon Application Recovery Controller](#infrastructure-security)
+ [Document history for the Amazon Application Recovery Controller (ARC) Developer Guide](#doc-history)

-----



# What is ARC?
<a name="what-is-route53-recovery"></a>

Amazon Application Recovery Controller (ARC) helps you prepare for and complete faster recovery for applications running on the AWS Global Cloud Infrastructure.

ARC provides the following capabilities:
+ *Multi-Availability Zone (AZ) recovery*, including zonal shift and zonal autoshift, which enable you to recover from single AZ impairments by temporarily shifting traffic from an impaired AZ to a healthy AZ.
+ *Multi-Region recovery*, which includes routing control and Region switch for Regional application recovery, and readiness check for application monitoring.

## Multi-Availability Zone recovery
<a name="what-is-route53-recovery.az"></a>

*Zonal shift*

You can use ARC zonal shift to quickly isolate and recover from single Availability Zone (AZ) impairments. Zonal shift temporarily shifts traffic for a supported resource away from an impaired AZ to healthy AZs in the same AWS Region. Starting a zonal shift helps your application recover quickly, for example, from a developer's bad code deployment or from an AWS impairment in a single AZ. Shifting traffic away from the impaired AZ reduces the impact for clients who are using your application in the impaired AZ.

You can start a zonal shift for any supported resource in your account in an AWS Region. Zonal shifts are manual and temporary. When you start a zonal shift, you must specify an (extendable) expiration of up to three days. To enable zonal shift for supported resources, refer to [Supported resources](#arc-zonal-shift.resource-types).

*Zonal autoshift*

ARC zonal autoshift authorizes AWS to shift traffic away from an impaired AZ for supported resources, on your behalf, to healthy AZs in the same AWS Region. AWS starts a zonal autoshift when internal telemetry indicates that there is an impairment in one AZ in an AWS Region that could potentially impact customers. The internal telemetry incorporates metrics from multiple sources, including the AWS network, and the Amazon EC2 and Elastic Load Balancing services.

Zonal autoshifts are temporary. AWS ends a zonal autoshift when the internal telemetry indicators show that there is no longer an issue or potential issue.

To learn more about these capabilities, see the following chapters:
+ [Zonal shift in ARC](#arc-zonal-shift)
+ [Zonal autoshift in ARC](#arc-zonal-autoshift)

## Multi-Region recovery
<a name="what-is-route53-recovery.region"></a>

*Region switch*

Region switch in ARC provides a centralized, automated, and observable solution for multi-Region application recovery. Region switch helps you to plan and coordinate recovery for your applications across AWS Regions, to help ensure business continuity and reduce operational overhead. 

You can use Region switch to orchestrate large-scale, complex recovery tasks for your application resources, across multiple AWS account. If an AWS Region becomes impaired, the plans that you create by using Region switch can fail over or switch your resources to another Region, so that your application can continue to operate, in a healthy AWS Region.

*Routing control*

ARC's extremely reliable routing controls enable multi-Region recovery so that your applications can failover Domain Name System DNS traffic across AWS Regions.

If your application is designed to operate out of multiple AWS Regions, you can use ARC *routing control* to failover between Regions. Routing control enables you to failover traffic from an impaired AWS Region to a healthy AWS Region, so that you can ensure that your application maintains availability. Routing control includes safety rules, which help protect you from unintended outcomes by imposing guardrails that you define. For example, you can impose a safety rule that only one of your application replicas, active or standby, is enabled and in use. 

*Readiness check *

ARC readiness check continually monitors AWS resource quotas, capacity, and network routing policies, and can notify you about changes that may affect your ability to failover to a replica application and recover from Region impairment. Continual readiness checks ensure that you can maintain your multi-Region applications in a state that is scaled and configured to handle failover traffic. Readiness check is useful when you first configure ARC, and during normal application operation. Readiness check is not intended to be used in the critical path for failover during an event.

To learn more about these capabilities, see the following chapters:
+ [Region switch in ARC](#region-switch)
+ [Routing control in ARC](#routing-control)
+ [Readiness check in ARC](#recovery-readiness)

# Amazon Application Recovery Controller (ARC) readiness check availability change
<a name="arc-readiness-availability-change"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal.

After careful consideration, we decided to close the readiness check feature in Amazon Application Recovery Controller (ARC) to new customers. Existing customers can continue to use the service as normal.

ARC readiness check is a feature that enables you to monitor the readiness of your resources for disaster recovery. ARC continues to be available, but the readiness check feature is no longer open to new customers.

**Note**  
ARC and ARC Region switch continue to be fully supported. Only the readiness check feature is affected by this change. There are no changes to Region switch, routing controls, zonal shift, and zonal autoshift.

## Migration options
<a name="arc-readiness-availability-change.migration"></a>

For capabilities similar to readiness check, we recommend onboarding your multi-Region application to ARC Region switch.

ARC Region switch is a fully managed service that provides complete multi-Region recovery orchestration. It includes a capability called plan evaluation, which regularly monitors the state of your Region switch plan to ensure readiness for execution.

To get started with ARC Region switch, see [Region switch in ARC](#region-switch).

# Compare multi-AZ and multi-Region recovery capabilities in ARC
<a name="compare-capabilities"></a>

Zonal shift, zonal autoshift, routing control, and Region switch in Amazon Application Recovery Controller (ARC) can all achieve rapid recovery and help you to ensure resilience for your AWS applications. These features are highly available, and help support recovery in scenarios when your application is experiencing increased latency or reduced availability. These features also help recover applications quickly by shifting traffic away from isolated impairments, which limits the impact and time lost from impairments.

Routing control and Region switch are focused on AWS applications that are in multiple AWS Regions (multi-Region), while zonal shift and zonal autoshift only support shifting traffic for supported resources with multi-AZ applications. 

The information in the following table includes some of the key features of the ARC resilience capabilities. These descriptions can help you better understand how a specific option might be the best choice for your application's needs.


| Routing control | Region switch | Zonal shift | Zonal autoshift | 
| --- | --- | --- | --- | 
| **Regional**<br />Reroutes traffic from one AWS Region to another (primarily) | **Regional**<br />Reroutes traffic from one AWS Region to another (primarily) | **Zonal**<br />Shifts traffic away from an Availability Zone<br />Traffic goes to other Availability Zones in the Region, not to a specific target | **Zonal**<br />Shifts traffic away from an Availability Zone<br />Traffic goes to other Availability Zones in the Region, not to a specific target | 
| **Requires setup**<br />Requires configuration and setup | **Requires setup**<br />Requires configuration and setup | **May require setup**<br />Requires opt-in for some supported resources<br />For more information, refer to [Supported resources](#arc-zonal-shift.resource-types) | **Requires setup**<br />Must be enabled for a supported resource<br />For more information, refer to [Supported resources](#arc-zonal-shift.resource-types) | 
| **Customer-initiated**<br />Customer determines when to re-route traffic | **Customer-initiated**<br />Customer determines when to re-route traffic | **Customer-initiated**<br />Customer determines when to start a zonal shift | **AWS-initiated**<br />AWS shifts application traffic away from an AZ on your behalf | 
| **Fee-based**<br />Requires separate charges for routing control | **Fee-based**<br />Requires separate charges for Region switch plans | **Included with services (no additional charge)**<br />Creating zonal shifts to move traffic away from AZs is included for supported resources | **Included with services (no additional charge)**<br />Starting autoshifts to move traffic away from AZs on your behalf is included for supported resources | 
| **Does not expire**<br />Traffic can be rerouted to a replica indefinitely | **Does not expire**<br />Application can be shifted to a replica indefinitely | **Temporary**<br />All zonal shifts must be set to expire | **Temporary**<br />AWS starts and ends autoshifts | 

To learn more about each of these features, see the following chapters:
+ [Zonal shift in ARC](#arc-zonal-shift)
+ [Zonal autoshift in ARC](#arc-zonal-shift)
+ [Routing control in ARC](#routing-control)
+ [Region switch in ARC](#region-switch)

# Use zonal shift and zonal autoshift to recover applications in ARC
<a name="multi-az"></a>

This section explains how to use capabilities in Amazon Application Recovery Controller (ARC) to reliably recover your AWS resource from an issue in an impaired Availability Zone (AZ). Zonal shift and zonal autoshift temporarily shift the traffic for a supported resource away from an impaired AZ, which reduces time to recovery for your applications. 

The primary difference between zonal shift and zonal autoshift is that one is a manual traffic shift that you control, and the other shifts traffic away from an impairment automatically on your behalf.
+ With zonal shift, you manually shift traffic for a supported resource in an AWS Region away from an Availability Zone.
+ With zonal autoshift, the traffic for a supported resource is automatically shifted away from an impaired AZ and rerouted to healthy AZs in the same AWS Region.

The following topics describe the zonal shift and zonal autoshift capabilities, and how to use them.

**Topics**
+ [Zonal shift in ARC](#arc-zonal-shift)
+ [Zonal autoshift in ARC](#arc-zonal-autoshift)

## Zonal shift in ARC
<a name="arc-zonal-shift"></a>

Amazon Application Recovery Controller (ARC) *zonal shift* allows you to shift traffic for a supported resource away from an impaired Availability Zone (AZ) in an AWS Region to healthy AZs in the same Region. Shifting your resource's traffic away from an impaired AZ reduces the duration and severity of impact caused by power outages, or hardware or software issues in an AZ, and helps to mitigate issues and quickly recover your application. You might choose to shift traffic, for example, because a bad deployment is causing latency issues, or because the Availability Zone is impaired. 

You must opt-in resources in order to use zonal shift. For more information, refer to [Supported resources](#arc-zonal-shift.resource-types). 

Before you start a zonal shift, you must prescale your application and ensure that you have sufficient capacity to shift traffic away from an Availability Zone. After prescaling, you can choose the Availability Zone to shift away from and the resource to shift traffic away for, and then start the zonal shift. You can cancel the shift at any time to have traffic begin returning to the original Availability Zone. For more information, see [Best practices for zonal shifts in ARC](#route53-arc-best-practices.zonal-shifts) 

All zonal shifts are temporary mitigations. You set an initial expiration when you start a zonal shift, from one minute up to three days (72 hours), which you can extend, if you need to continue the traffic shift. 

In specific scenarios, zonal shift does not shift traffic away from the AZ. For more information, see [Supported resources](#arc-zonal-shift.resource-types). 

### How a zonal shift works
<a name="arc-zonal-shift.how-it-works"></a>

When you start a zonal shift for a supported resource, traffic for the resource is moved away from the Availability Zone (AZ) that you've specified. ARC's supported resources provide integrations that mark the specified AZ as unhealthy, which results in a traffic shifting away from the impaired AZ. 

**Traffic begins to shift** - When you start a zonal shift in ARC, you might not see traffic move out of the Availability Zone immediately. It can take a short time for existing, in-progress connections in the Availability Zone to complete, depending on client behavior and connection reuse. DNS settings and other factors including existing connections can complete in just a few minutes, but they may take longer. For more information, see [Ensuring that traffic shifts finish quickly](#arc-zonal-shift.existing-connections).

**Traffic shift ends** - When a zonal shift expires or you cancel it, ARC takes steps to stop shifting traffic and reverses the process for starting a traffic shift. Now, the recovered AZ is recognized as available for the resource and traffic resumes flowing to the AZ.

You must set all zonal shifts to expire when you start the shifts. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time. You can also cancel a zonal shift before it expires, if you're ready to restore traffic to the Availability Zone.

**When traffic does not shift away** - In specific scenarios, a zonal shift does not shift traffic from the Availability Zone. For example, say you start a zonal shift for a load balancer when the load balancer target groups in the AZs don't have any instances, or if all of the instances are unhealthy. In this scenario, the load balancer is in a fail open state and starting a zonal shift does not shift away traffic.

Before you start a zonal shift for a resource, make sure that all the conditions for a successful zonal shift are met. AWS resources handle zonal shifts differently. For more information about zonal shift support, see [Supported resources](#arc-zonal-shift.resource-types).

### AWS Region availability for zonal shift
<a name="introduction-regions-zonal"></a>

For detailed information about Regional support and service endpoints for Amazon Application Recovery Controller (ARC), see [Amazon Application Recovery Controller (ARC) endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/r53arc.html) in the *Amazon Web Services General Reference*.

Zonal shift and zonal autoshift are currently available in the AWS Regions listed here. Zonal shift and zonal autoshift also available in the China Regions, that is, China (Beijing) Region and China (Ningxia) Region. Resources that use Amazon Application Recovery Controller (ARC) may have additional considerations. For more information, refer to [Supported resources](#arc-zonal-shift.resource-types).


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  arc-zonal-shift.us-east-2.amazonaws.com <br /> arc-zonal-shift-fips.us-east-2.api.aws <br /> arc-zonal-shift.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  arc-zonal-shift.us-east-1.amazonaws.com <br /> arc-zonal-shift-fips.us-east-1.api.aws <br /> arc-zonal-shift.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  arc-zonal-shift.us-west-1.amazonaws.com <br /> arc-zonal-shift-fips.us-west-1.api.aws <br /> arc-zonal-shift.us-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  arc-zonal-shift.us-west-2.amazonaws.com <br /> arc-zonal-shift-fips.us-west-2.api.aws <br /> arc-zonal-shift.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  arc-zonal-shift.af-south-1.amazonaws.com <br /> arc-zonal-shift.af-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  arc-zonal-shift.ap-east-1.amazonaws.com <br /> arc-zonal-shift.ap-east-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  arc-zonal-shift.ap-south-2.amazonaws.com <br /> arc-zonal-shift.ap-south-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  arc-zonal-shift.ap-southeast-3.amazonaws.com <br /> arc-zonal-shift.ap-southeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  arc-zonal-shift.ap-southeast-5.amazonaws.com <br /> arc-zonal-shift.ap-southeast-5.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  arc-zonal-shift.ap-southeast-4.amazonaws.com <br /> arc-zonal-shift.ap-southeast-4.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  arc-zonal-shift.ap-south-1.amazonaws.com <br /> arc-zonal-shift.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  arc-zonal-shift.ap-southeast-6.amazonaws.com <br /> arc-zonal-shift.ap-southeast-6.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  arc-zonal-shift.ap-northeast-3.amazonaws.com <br /> arc-zonal-shift.ap-northeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  arc-zonal-shift.ap-northeast-2.amazonaws.com <br /> arc-zonal-shift.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  arc-zonal-shift.ap-southeast-1.amazonaws.com <br /> arc-zonal-shift.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  arc-zonal-shift.ap-southeast-2.amazonaws.com <br /> arc-zonal-shift.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  arc-zonal-shift.ap-east-2.amazonaws.com <br /> arc-zonal-shift.ap-east-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  arc-zonal-shift.ap-southeast-7.amazonaws.com <br /> arc-zonal-shift.ap-southeast-7.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  arc-zonal-shift.ap-northeast-1.amazonaws.com <br /> arc-zonal-shift.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  arc-zonal-shift.ca-central-1.amazonaws.com <br /> arc-zonal-shift-fips.ca-central-1.api.aws <br /> arc-zonal-shift.ca-central-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| Canada West (Calgary) | ca-west-1 |  arc-zonal-shift.ca-west-1.amazonaws.com <br /> arc-zonal-shift-fips.ca-west-1.api.aws <br /> arc-zonal-shift.ca-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  arc-zonal-shift.eu-central-1.amazonaws.com <br /> arc-zonal-shift.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  arc-zonal-shift.eu-west-1.amazonaws.com <br /> arc-zonal-shift.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  arc-zonal-shift.eu-west-2.amazonaws.com <br /> arc-zonal-shift.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Milan) | eu-south-1 |  arc-zonal-shift.eu-south-1.amazonaws.com <br /> arc-zonal-shift.eu-south-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  arc-zonal-shift.eu-west-3.amazonaws.com <br /> arc-zonal-shift.eu-west-3.api.aws  | HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  arc-zonal-shift.eu-south-2.amazonaws.com <br /> arc-zonal-shift.eu-south-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Stockholm) | eu-north-1 |  arc-zonal-shift.eu-north-1.amazonaws.com <br /> arc-zonal-shift.eu-north-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Zurich) | eu-central-2 |  arc-zonal-shift.eu-central-2.amazonaws.com <br /> arc-zonal-shift.eu-central-2.api.aws  | HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  arc-zonal-shift.il-central-1.amazonaws.com <br /> arc-zonal-shift.il-central-1.api.aws  | HTTPS<br />HTTPS | 
| Mexico (Central) | mx-central-1 |  arc-zonal-shift.mx-central-1.amazonaws.com <br /> arc-zonal-shift.mx-central-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (Bahrain) | me-south-1 |  arc-zonal-shift.me-south-1.amazonaws.com <br /> arc-zonal-shift.me-south-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (UAE) | me-central-1 |  arc-zonal-shift.me-central-1.amazonaws.com <br /> arc-zonal-shift.me-central-1.api.aws  | HTTPS<br />HTTPS | 
| South America (São Paulo) | sa-east-1 |  arc-zonal-shift.sa-east-1.amazonaws.com <br /> arc-zonal-shift.sa-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  arc-zonal-shift.us-gov-east-1.amazonaws.com <br /> arc-zonal-shift-fips.us-gov-east-1.api.aws <br /> arc-zonal-shift.us-gov-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  arc-zonal-shift.us-gov-west-1.amazonaws.com <br /> arc-zonal-shift-fips.us-gov-west-1.api.aws <br /> arc-zonal-shift.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 

### Zonal shift components
<a name="introduction-components-zonal"></a>

The following diagram illustrates an example of a zonal shift shifting traffic away from an Availability Zone in an AWS Region. Checks that are built into zonal shift prevent you from starting another zonal shift for a resource when it already has an active shift.

![Diagram of a zonal shift with three Availability Zones](https://docs.aws.amazon.com/r53recovery/latest/dg/images/ZonalShiftDiagramRev2023.png)


The following are components of the zonal shift capability in ARC.

**Zonal shift**  
You start a zonal shift for a managed resource in your AWS account to temporarily move traffic away from an Availability Zone in an AWS Region, to healthy AZs in the Region, to quickly recover from an issue in one AZ. For more information on supported resources for zonal shift, refer to [Supported resources](#arc-zonal-shift.resource-types).

**Built-in safety checks**  
Checks that are built into ARC prevent more than one traffic shift for a resource from being in effect at a time. That is, only one customer-initiated zonal shift, practice run, or autoshift for the resource can be actively shifting traffic away from an Availability Zone. For example, if you start a zonal shift for a resource when it is currently shifted away with autoshift, your zonal shift takes precedence. For more information, see [Zonal autoshift in ARC](#arc-zonal-autoshift) and [Outcomes for practice runs](#ZAShiftPrecedence).

**Resource identifier**  
The identifier for a resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.  
For a zonal shift, you can only choose resources in your account for an AWS service that is supported by ARC. For more information on supported resources for zonal shift, refer to [Supported resources](#arc-zonal-shift.resource-types).

**Managed resource**  
Some AWS resources must manually opt-in to zonal shift, and others are automatically enabled. For more information on supported resources for zonal shift, refer to [Supported resources](#arc-zonal-shift.resource-types).

**Resource name**  
The name of a resource in ARC that you can specify for a zonal shift.

**Status (zonal shift status)**  
A status for a zonal shift. The `Status` for a zonal shift can have one of the following values:  
+ **ACTIVE**: The zonal shift is started and active.
+ **EXPIRED**: The zonal shift has expired (the expiry time was exceeded).
+ **CANCELED**: The zonal shift was canceled.

**Applied status**  
An applied status indicates whether a shift is in effect for a resource. The shift that has the status `APPLIED` determines the Availability Zone where application traffic has been shifted away for a resource, and when that shift ends.

**Shift type**  
Defines the zonal shift type. The `shiftType` can have the following values:  
+ **ZONAL\_SHIFT**
+ **ZONAL\_AUTOSHIFT**
+ **PRACTICE\_RUN**
+ **FIS\_EXPERIMENT**

**Expiry time (expiration time)**  
The expiry time (expiration time) for a zonal shift. Zonal shifts are temporary. For a zonal shift, you can initially set a zonal shift to be active for up to three days (72 hours).  
When you start a zonal shift, you specify how long you want it to be active, which ARC converts to an expiry time (expiration time). You can cancel a zonal shift, for example, if you're ready to restore traffic to the Availability Zone. Or you can extend a customer-initiated zonal shift by updating it to specify another length of time to expire in.  
You can cancel zonal shift practice runs that are part of zonal autoshift.

### Data and control planes for zonal shift
<a name="data-and-control-planes-zonal-shift"></a>

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that you make sure that the mechanisms that you depend on during failover are highly available, so that you can use them when you need them in a disaster scenario. Typically, you should use data plane functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind, it's important to understand how the functionality of a service is divided between control planes and data planes, and when you can rely on an expectation of extreme reliability with a service's data plane.

As with most AWS services, the functionality for the zonal shift capability is supported by control planes and data planes. While both of these are built to be reliable, a control plane is optimized for data consistency, while a data plane is optimized for availability. A data plane is designed for resilience so that it can maintain availability even during disruptive events, when a control plane might become unavailable.

In general, a *control plane* enables you to do basic management functions, such as create, update, and delete resources in the service. A *data plane* provides a service's core functionality.

For more information about data planes, control planes, and how AWS builds services to meet high availability targets, see the [Static stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) in the Amazon Builders' Library.

### Pricing for zonal shift in ARC
<a name="introduction-pricing-zonal-shift"></a>

For zonal shift, you can start a zonal shift for supported resources, to recover your application from an issue in an Availability Zone. There is no additional charge for using zonal shift.

For detailed pricing information for ARC and pricing examples, see [ARC Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

### Best practices for zonal shifts in ARC
<a name="route53-arc-best-practices.zonal-shifts"></a>

We recommend the following best practices for using zonal shifts for multi-AZ recovery in ARC. 

**Topics**
+ [Capacity planning and pre-scaling](#ZSBestPracticeCapacityPrescaling)
+ [Limit the time that clients stay connected to your endpoints](#arc-zonal-shift.existing-connections)
+ [Test starting zonal shifts, in advance](#ZSBestPracticeTestShifting)
+ [Ensure that all Availability Zones are healthy and taking traffic](#ZSBestPracticeEnsureHealthyAZs)
+ [Use data plane API operations for disaster recovery](#ZSBestPracticeUseDataPlane)
+ [Move traffic with a zonal shift only temporarily](#ZSBestPracticeMoveTrafficTemp)

**Capacity planning and pre-scaling**  
Ensure that you have planned for, and either pre-scaled or can auto-scale, sufficient capacity to accommodate the extra load imposed on Availability Zones when you start a zonal shift. With a recovery-oriented architecture, a typical recommendation is to pre-scale compute capacity to include enough headroom to serve your peak traffic when one of your (typically) three replicas is offline.  
When you start a zonal shift for a supported resource and traffic is shifted away from an AZ, the capacity that your application was using to service requests is removed. You must ensure that you have planned for a shift of traffic away from an AZ and can continue to service requests in the remaining AZs. 

**Limit the time that clients stay connected to your endpoints**  
When Amazon Application Recovery Controller (ARC) shifts traffic away from an impairment, for example, by using zonal shift or zonal autoshift, the mechanism that ARC uses to move your application traffic is a DNS update. A DNS update causes all new connections to be directed away from the impaired location.  
However, clients with pre-existing open connections might continue to make requests against the impaired location until the clients reconnect. To ensure a quick recovery, we recommend that you limit the amount of time clients stay connected to your endpoints. 

**Test starting zonal shifts, in advance**  
Regularly test moving traffic away from Availability Zones for your application by starting zonal shifts. Plan for and execute starting zonal shifts, preferably in both test and production environments, as part of regular failover testing for recovering your applications in the event of a disaster. Regular testing is a critical part of ensuring that you're ready for and have the confidence to mitigate issues when an operational event occurs.

**Ensure that all Availability Zones are healthy and taking traffic**  
Zonal shifts work by marking a resource, that is, an application replica, as unhealthy in an Availability Zone. This means that it's critical to ensure that the resources in your applications are generally healthy and actively taking traffic in the Availability Zones in a Region. We recommend that you have dashboards to track this, including, for example, Elastic Load Balancing metrics for unhealthy targets and bytesProcessed per Availability Zone.   
Consider monitoring the health of your resources from a second, adjacent Region. Advantages of this approach are that it can be more representative of your end users' experience, and it also reduces the risk of both your application and your monitoring being impacted by the same disaster at the same time.

**Use data plane API operations for disaster recovery**  
For starting a zonal shift when you need to recover an application quickly, with few dependencies, we recommend using the AWS Command Line Interface or API with zonal shift actions, with pre-stored credentials, if possible. You can also start zonal shifts in the AWS Management Console, for ease of use. But when fast, reliable recovery is critical, data plane operations are a better choice. For more information, see [ Zonal Shift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

**Move traffic with a zonal shift only temporarily**  
A zonal shift moves traffic away from an Availability Zone on a temporary basis, to mitigate an impairment. You should restore the resource for the application to service as soon as you've taken action to correct a problem. This ensures that your overall application is restored to its original fully redundant, resilient state.

### Zonal shift API operations
<a name="actions.zonalshift"></a>

The following table lists ARC API operations that you can use using zonal shift, which moves traffic away from an Availability Zone for multi-AZ applications. The table also includes links to relevant documentation.

For examples of how to use common zonal shift API operations with the AWS Command Line Interface, see [Examples of using the AWS CLI with zonal shift](#getting-started-cli-zonalshift).


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Start a zonal shift | See [Starting a zonal shift](#arc-zonal-shift.start) | See [StartZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartZonalShift.html) | 
| Update a zonal shift | See [Updating or canceling a zonal shift](#arc-zonal-shift.update-cancel) | See [UpdateZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalShift.html) | 
| List zonal shifts | See [Zonal shift in ARC](#arc-zonal-shift) | See [ListZonalShifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListZonalShifts.html) | 
| List managed resources | See [Supported resources](#arc-zonal-shift.resource-types) | See [ListManagedResources](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html) | 
| Get managed resource | See [Supported resources](#arc-zonal-shift.resource-types) | See [GetManagedResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetManagedResource.html) | 
| Cancel a zonal shift | See [Updating or canceling a zonal shift](#arc-zonal-shift.update-cancel) | See [CancelZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelZonalShift.html) | 

### Examples of using the AWS CLI with zonal shift
<a name="getting-started-cli-zonalshift"></a>

This section provides application examples of using zonal shift, using the AWS Command Line Interface to work with the zonal shift capability in Amazon Application Recovery Controller (ARC) using API operations. The examples are intended to help you develop a basic understanding of how to work with zonal shift using the CLI.

Zonal shift in ARC enables you to temporarily move traffic for supported resources away from an Availability Zone so that your application can continue to operate normally with other Availabilty Zones in an AWS Region.

All zonal shifts are temporary and must be set initially to expire within three days. However, you can update a zonal shift later to set a new expiration.

For more information about using the AWS CLI, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/arc-zonal-shift/index.html). For a list of zonal shift API actions and links to more information, see [Zonal shift API operations](#actions.zonalshift).

#### Start zonal shift
<a name="getting-started-cli-zonalshift.start-zonal-shift"></a>

You can start a zonal shift with the CLI by using the `start-zonal-shift` command.

```
aws arc-zonal-shift start-zonal-shift \
       --resource-identifier arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05 \
       --away-from use1-az1 \
       --expires-in 10m \
       --comment "Shifting traffic away from use1-az1"
```

```
{
    "awayFrom": "use1-az1",
    "comment": "Shifting traffic away from use1-az1",
    "expiryTime": "2024-12-17T21:37:26-08:00",
    "resourceIdentifier": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
    "startTime": "2024-12-17T21:27:26-08:00",
    "status": "ACTIVE",
    "zonalShiftId": "9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38"
}
```

#### Get managed resource
<a name="getting-started-cli-zonalshift.get-managed-resource"></a>

You can get information about a managed resource with the CLI by using the `get-managed-resource` command.

```
aws arc-zonal-shift get-managed-resource \
       --resource-identifier arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05
```

```
{
    "appliedWeights": {
        "use1-az1": 0.0,
        "use1-az2": 1.0,
        "use1-az6": 1.0
    },
    "arn": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
    "autoshifts": [],
    "name": "Testing",
    "zonalAutoshiftStatus": "DISABLED",
    "zonalShifts": [
        {
            "appliedStatus": "APPLIED",
            "awayFrom": "use1-az1",
            "comment": "Shifting traffic away from use1-az1",
            "expiryTime": "2024-12-17T21:37:26-08:00",
            "resourceIdentifier": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
            "startTime": "2024-12-17T21:27:26-08:00",
            "zonalShiftId": "9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38"
            "shiftType": "MANUAL"
        }
    ]
}
```

#### List managed resources
<a name="getting-started-cli-zonalshift.list-managed-resource"></a>

You can list the managed resources in your account with the CLI by using the `list-managed-resources` command.

```
aws arc-zonal-shift list-managed-resources 
```

```
{
    "items": [
        {
            "appliedWeights": {
                "use1-az1": 0.0,
                "use1-az2": 1.0,
                "use1-az6": 1.0
            },
            "arn": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
            "autoshifts": [],
            "availabilityZones": [
                "use1-az1",
                "use1-az2",
                "use1-az6"
            ],
            "name": "Testing",
            "practiceRunStatus": "DISABLED",
            "zonalAutoshiftStatus": "DISABLED",
            "zonalShifts": [
                {
                    "appliedStatus": "APPLIED",
                    "awayFrom": "use1-az1",
                    "comment": "Shifting traffic away from use1-az1",
                    "expiryTime": "2024-12-17T21:37:26-08:00",
                    "resourceIdentifier": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
                    "startTime": "2024-12-17T21:27:26-08:00",
                    "zonalShiftId": "9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38"
                }
            ]
        }
    ]
}
```

#### List zonal shifts
<a name="getting-started-cli-zonalshift.list-zonal-shifts"></a>

You can list the zonal shifts in your account with the CLI by using the `list-zonal-shifts` command.

```
aws arc-zonal-shift list-zonal-shifts 
```

```
{
    "items": [
        {
            "awayFrom": "use1-az1",
            "comment": "Shifting traffic away from use1-az1",
            "expiryTime": "2024-12-17T21:37:26-08:00",
            "resourceIdentifier": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
            "startTime": "2024-12-17T21:27:26-08:00",
            "status": "ACTIVE",
            "zonalShiftId": "9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38"
        }
    ]
}
```

#### Update zonal shift
<a name="getting-started-cli-zonalshift.update-zonal-shift"></a>

You can update a zonal shift with the CLI by using the `update-zonal-shift` command.

```
aws arc-zonal-shift update-zonal-shift \  
       --zonal-shift-id 9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38 \
       --expires-in 1h \
       --comment "Still shifting traffic away from use1-az1"
```

```
{
    "awayFrom": "use1-az1",
    "comment": "Still shifting traffic away from use1-az1",
    "expiryTime": "2024-12-17T22:29:38-08:00",
    "resourceIdentifier": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
    "startTime": "2024-12-17T21:27:26-08:00",
    "status": "ACTIVE",
    "zonalShiftId": "9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38"
}
```

#### Cancel zonal shift
<a name="getting-started-cli-zonalshift.cancel-zonal-shift"></a>

You can cancel a zonal shift with the CLI by using the `cancel-zonal-shift` command.

```
aws arc-zonal-shift cancel-zonal-shift \
       --zonal-shift-id 9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38
```

```
{
    "awayFrom": "use1-az1",
    "comment": "Still shifting traffic away from use1-az1",
    "expiryTime": "2024-12-17T22:29:38-08:00",
    "resourceIdentifier": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
    "startTime": "2024-12-17T21:27:26-08:00",
    "status": "CANCELED",
    "zonalShiftId": "9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38"
}
```

### Supported resources
<a name="arc-zonal-shift.resource-types"></a>

Amazon Application Recovery Controller (ARC) currently supports enabling the following resources for zonal shift and zonal autoshift:
+ [Amazon EC2 Auto Scaling groups](#arc-zonal-shift.resource-types.ec2-auto-scaling-groups)
+ [Amazon Elastic Kubernetes Service](#arc-zonal-shift.resource-types.eks)
+ [Application Load Balancers](#arc-zonal-shift.resource-types.app-load-balancers) with cross-zone load balancing enabled or disabled
+ [Network Load Balancers](#arc-zonal-shift.resource-types.network-load-balancers) with cross-zone load balancing enabled or disabled

For specific requirements for Network Load Balancers and Application Load Balancers, see the additional topics in this section.

Review the following conditions for working with zonal shifts, zonal autoshift, and resources in ARC:
+ A resource must be active and fully provisioned to shift traffic for it. Before you start a zonal shift for a resource, check to make sure that it's a managed resource in ARC. For example, view the list of managed resources in the AWS Management Console, or use the `get-managed-resource` operation with the resource's identifier.
+ To start a zonal shift with a resource, it must be deployed in the Availability Zone and AWS Region where you start the shift. Make sure that you start a zonal shift in the same Region that the AZ you want to shift away from is in, and that the resource that you're shifting traffic for is in the same AZ and Region as well. 
+ Ensure that you have the correct IAM permissions to use zonal shift with a resource. For more information, see [IAM and permissions for zonal shift](#security_iam_service-with-iam-zonal-shift).
+ When a Network Load Balancer or Application Load Balancer is in a fail open state, a zonal shift will have no effect. This is expected behavior because zonal shift cannot force an AZ to be unhealthy and then shift traffic to the other AZs in a Region when a load balancer is failing open. For more information, see [Using Route 53 DNS failover for your load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#r53-dns-failover) in the *Network Load Balancers User Guide* and [Using Route 53 DNS failover for your load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#r53-dns-failover) in the *Application Load Balancers User Guide*.
+ If multiple load balancers are forwarding traffic to the same targets, a zonal shift on a cross-zone enabled load balancer drops target capacity for all load balancers, even if their traffic is not shifted by a zonal shift.

#### Amazon EC2 Auto Scaling groups
<a name="arc-zonal-shift.resource-types.ec2-auto-scaling-groups"></a>

An Amazon EC2 Auto Scaling group contains a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. An Auto Scaling group also lets you use Amazon EC2 Auto Scaling features such as health check replacements and scaling policies. Both maintaining the number of instances in an Auto Scaling group and automatic scaling are the core functionality of the Amazon EC2 Auto Scaling service.

##### Using zonal shift for Auto Scaling groups
<a name="using-asg-zs"></a>

To enable zonal shift, use one of the following methods.

------
#### [ Console ]

**To enable zonal shift on a new group (console)**

1. Follow the instructions in [Create an Auto Scaling group using a launch template](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template) and complete each step in the procedure, up to step 10.

1. On the **Integrate with other services** page, for **ARC zonal shift**, select the checkbox to enable zonal shift.

1. For **Health check behavior**, choose Ignore unhealthy or Replace unhealthy. If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift.

1. Continue with the steps in [Create an Auto Scaling group using a launch template](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template).

------
#### [ AWS CLI ]

**To enable zonal shift on a new group (AWS CLI)**  
Add the `--availability-zone-impairment-policy` parameter to the [create-auto-scaling-group](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/create-auto-scaling-group.html) command.

The `--availability-zone-impairment-policy` parameter has two options:
+ **ZonalShiftEnabled** – If set to `true`, Auto Scaling registers the Auto Scaling group with ARC zonal shift and you can [start, update, or cancel a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html) on the ARC console. If set to `false`, Auto Scaling deregisters the Auto Scaling group from ARC zonal shift. You must already have zonal shift enabled to set to `false`.
+ **ImpairedZoneHealthCheckBehavior** – If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift.

The following example enables zonal shift on a new Auto Scaling group named `{{my-asg}}`.

```
aws autoscaling create-auto-scaling-group \
  --launch-template LaunchTemplateName={{my-launch-template}},Version='{{1}}' \
  --auto-scaling-group-name {{my-asg}} \
  --min-size {{1}} \
  --max-size {{10}} \
  --desired-capacity {{5}} \
  --availability-zones {{us-east-1a}} {{us-east-1b}} {{us-east-1c}} \
  --availability-zone-impairment-policy '{
      "ZonalShiftEnabled": {{true}},
      "ImpairedZoneHealthCheckBehavior": {{IgnoreUnhealthy}}       
    }'
```

------

------
#### [ Console ]

**To enable zonal shift on an existing group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the checkbox next to the Auto Scaling group.

   A split pane opens up in the bottom of the page. 

1. On the **Integrations** tab, under **ARC zonal shift**, choose **Edit**.

1. Select the checkbox to enable zonal shift.

1. For **Health check behavior**, choose **Ignore unhealthy** or **Replace unhealthy**. 
   + If health check behavior is set to ignore unhealthy, unhealthy instances are *not* replaced in the Availability Zone with the active zonal shift.
   + If health check behavior is set to replace unhealthy, unhealthy instances are replaced in the Availability Zone with the active zonal shift.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To enable zonal shift on an existing group (AWS CLI)**  
Add the `--availability-zone-impairment-policy` parameter to the [update-auto-scaling-group](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/update-auto-scaling-group.html) command.

The `--availability-zone-impairment-policy` parameter has two options:
+ **ZonalShiftEnabled** – If set to `TRUE`, Auto Scaling registers the Auto Scaling group with ARC zonal shift and you can [start, update, or cancel a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html) on the ARC console. If set to `FALSE`, Auto Scaling deregisters the Auto Scaling group from ARC zonal shift. You must already have zonal shift enabled to set it to `FALSE`.
+ **ImpairedZoneHealthCheckBehavior** – If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift.

The following example enables zonal shift on the specified Auto Scaling group.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --availability-zone-impairment-policy '{
      "ZonalShiftEnabled": {{true}},
      "ImpairedZoneHealthCheckBehavior": {{IgnoreUnhealthy}}       
    }'
```

------

To start a zonal shift, see [Starting, updating, or canceling a zonal shift](#arc-zonal-shift.start-cancel).

##### How zonal shift works for Auto Scaling groups
<a name="how-it-works-asg-zs"></a>

Suppose you have an Auto Scaling group with the following Availability Zones: 
+ `us-east-1a`
+ `us-east-1b`
+ `us-east-1c`

You notice failures in `us-east-1a` and start a zonal shift. The following behaviors occur when a zonal shift is started in `us-east-1a`.
+ **Scaling out** – Auto Scaling launches all new capacity requests in the healthy Availability Zones (`us-east-1b` and `us-east-1c`).
+ **Dynamic scaling** – Auto Scaling blocks scaling policies from decreasing desired capacity. Auto Scaling does not block scaling policies from increasing desired capacity.
+ **Instance refresh** – Auto Scaling extends the timeout for any instance refresh process that is delayed during an active zonal shift.


<table>
<tbody>
</tbody>
</table>


##### Best practices for using zonal shift
<a name="best-practices-asg-zs"></a>

To maintain high availability for your applications when using zonal shift, we recommend the following best practices.
+ Monitor EventBridge notifications to determine when there is an ongoing availability zone impairment event. For more information, see [Automating Amazon EC2 Auto Scaling with EventBridge](https://docs.aws.amazon.com/autoscaling/ec2/userguide/automating-ec2-auto-scaling-with-eventbridge.html).
+ Use scaling policies with appropriate thresholds to make sure that you have enough capacity to tolerate the loss of an availability zone.
+ Set an instance maintenance policy with a minimum healthy percentage of 100. With this setting, Auto Scaling waits for a new instance to be ready to use before terminating an unhealthy instance.

For prescaled customers, we also recommend the following:
+ Select **Ignore unhealthy** as the health check behavior for the impaired availability zone because you don't need to replace the unhealthy instance during the impairment event.
+ Use zonal autoshift in ARC for your Auto Scaling groups. The zonal autoshift capability in Amazon Application Recovery Controller (ARC) allows AWS to shift traffic for a resource away from an availability zone when AWS detects an impairment in an availability zone. For more information, see [Zonal autoshift in ARC](#arc-zonal-autoshift).

For customers with cross-zone disabled load balancers, we also recommend:
+ Use **balanced only** for your availability zone distribution.
+ If you are using zonal shift on both your Auto Scaling group and your load balancers, make sure to cancel the zonal shift on your Auto Scaling group first. Then, wait until the capacity is balanced across all availability zones. before you cancel the zonal shift on the load balancer.
+ Because of the possibility of imbalanced capacity when you enable zonal shift and you use a cross-zone disabled load balancer, Auto Scaling has an extra validation. If you are following the best practices, you can acknowledge this possibility by selecting the checkbox in the AWS Management Console or using the `skip-zonal-shift-validation` flag in `CreateAutoScalingGroup`, `UpdateAutoScalingGroup`, or `AttachTrafficSources`.

#### Amazon Elastic Kubernetes Service
<a name="arc-zonal-shift.resource-types.eks"></a>

Amazon EKS provides features that enable you to make your applications more resilient to events such as the degraded health or the impairment of an Availability Zone. When you run your workloads in an Amazon EKS cluster, you can further improve fault tolerance and application recovery by using zonal shift or zonal autoshift. For more information, see [Learn about ARC Zonal Shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the *Amazon Elastic Kubernetes Service User Guide*.

##### Using zonal shift with Amazon Elastic Kubernetes Service
<a name="using-eks-zs"></a>

To enable zonal shift, use one of the following methods. For more information, see [Learn about ARC zonal shift](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift-enable.html#zone-shift-enable-steps) in the *Amazon Elastic Kubernetes Service User Guide*.

------
#### [ Console ]

**To enable zonal shift on a new Amazon EKS cluster (Console)**

1. Find the name and Region of the Amazon EKS cluster that you want to register with ARC.

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. Select your cluster.

1. On the **Cluster info** page, select the **Overview** tab.

1. Under **Zonal shift**, choose **Manage**.

1. For **EKS Zonal Shift**, choose **Enable** or **Disable**.

------
#### [ AWS CLI ]

**To enable zonal shift on a new Amazon EKS cluster (AWS CLI)**
+ Enter the following command:

  ```
  aws eks create-cluster --name {{my-eks-cluster}} --role-arn {{my-role-arn-to-create-cluster}} --resources-vpc-config subnetIds=string,string,securityGroupIds=string,string,endpointPublicAccess=boolean,endpointPrivateAccess=boolean,publicAccessCidrs=string,string --zonal-shift-config enabled=true
  ```

**To enable zonal shift on an existing Amazon EKS cluster (AWS CLI)**
+ Enter the following command:

  ```
  aws eks update-cluster-config --name {{my-eks-cluster}} --zonal-shift-config enabled=true
  ```

------

You can start a zonal shift for an Amazon EKS cluster, or you can allow AWS to do it for you, by enabling zonal autoshift. After your Amazon EKS cluster zonal shift enabled with ARC, you can start a zonal shift or enable zonal autoshift using the ARC Console, the AWS CLI, or the zonal shift and zonal autoshift APIs. 

For more information on starting a zonal shift, see [Starting, updating, or canceling a zonal shift](#arc-zonal-shift.start-cancel).

For more information on enabling Amazon EKS with zonal shift, see [Learn about ARC Zonal Shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the *Amazon Elastic Kubernetes Service User Guide*. 

##### How zonal shift works for Amazon Elastic Kubernetes Service
<a name="how-it-works-eks-zs"></a>

During an Amazon EKS zonal shift, the following automatically takes place for all Amazon EKS clusters:
+ All the nodes in the impacted AZ are cordoned. This prevents the Kubernetes Scheduler from scheduling new Pods onto the nodes in the unhealthy AZ.
+ If you’re using [Managed Node Groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html), [Availability Zone rebalancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#AutoScalingBehavior.InstanceUsage) is suspended, and your Auto Scaling group is updated to ensure that new Amazon EKS data plane nodes are only launched in healthy AZs.
+ The nodes in the unhealthy AZ are not terminated and the Pods are not evicted from these nodes. This is to ensure that when a zonal shift expires or is canceled, your traffic can be safely returned to the AZ that still has full capacity.
+ The EndpointSlice controller finds all the Pod endpoints in the impaired AZ and removes them from the relevant EndpointSlices. This ensures that only Pod endpoints in healthy AZs are targeted to receive network traffic. When a zonal shift is canceled or expires, the EndpointSlice controller updates the EndpointSlices to include the endpoints in the restored AZ.

If you are using EKS Auto Mode or self-managed Karpenter, the Karpenter controller also does the following during a zonal shift:
+ Stops provisioning new capacity in the impaired AZ by marking all compute offerings in that zone as unavailable.
+ Stops voluntary disruption (consolidation and drift) on nodes in the impaired AZ.
+ Prevents launch attempts for pods with strict scheduling requirements (such as EBS volume affinity) that require the impaired AZ.
+ Resumes normal behavior when the zonal shift is canceled or expires.

For more information about Amazon EKS zonal shift, see the [AWS Containers blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-amazon-application-recovery-controller/) on the AWS website.

#### Application Load Balancers
<a name="arc-zonal-shift.resource-types.app-load-balancers"></a>

##### Using zonal shift for Application Load Balancers
<a name="using-alb-zs"></a>

To use Application Load Balancers with zonal shift, you must enable ARC zonal shift integration in the Application Load Balancer attributes. Application Load Balancer supports zonal shift with cross-zone enabled or cross-zone disabled configurations.

Before you enable the ARC integration and start using zonal shift, review the following information:
+ You can start a zonal shift for a specific load balancer only for a single Availability Zone. You can't start a zonal shift for multiple Availability Zones.
+ AWS proactively removes zonal load balancer IP addresses from DNS when multiple infrastructure issues impact services. Always check current Availability Zone capacity before you start a zonal shift.
+ Zonal shift won't work for single-AZ target groups.
+ When an Application Load Balancer is a target of a Network Load Balancer, always start the zonal shift from the Network Load Balancer. If you start a zonal shift from the Application Load Balancer, the Network Load Balancer doesn't recognize the shift and continues to send traffic to the Application Load Balancer.

You can start a zonal shift for a load balancer in the Elastic Load Balancing console (in most AWS Regions) or in the ARC console.

------
#### [ Console ]

**To enable zonal shift on a load balancer (Console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the **Navigation** page, under **Load balancing**, choose **Load balancers**.

1. Select the Application Load Balancer name.

1. On the **Attributes** tab, **Edit**.

1. Under **Availability Zone routing configuration**, for >ARC zonal shift integration, choose **Enable**.

1. Choose **Save**.

------
#### [ AWS CLI ]

**To enable zonal shift on a load balancer (AWS CLI)**
+ Enter the following command:

  ```
  aws elbv2 modify-load-balancer-attributes --load-balancer-arn {{my-alb-arn}} --attributes Key=zonal_shift.config.enabled,Value=true
  ```

------

For more information on starting a zonal shift, see [Starting, updating, or canceling a zonal shift](#arc-zonal-shift.start-cancel).

You can use the `keepalive` option to configure how long connections continue. For more information, see [ HTTP client keepalive duration](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#http-client-keep-alive-duration) in the Application Load Balancer User Guide. By default, Application Load Balancers set the HTTP client keepalive duration value to 3600 seconds, or 1 hour. We suggest that you lower the value to be inline with your recovery time goal for your application, for example, 300 seconds. When you choose an HTTP client keepalive duration time, consider that this value is a trade off between reconnecting more frequently in general, which can affect latency, and more quickly moving all clients away from an impaired AZ or Region.

##### How zonal shift works for Application Load Balancers
<a name="how-it-works-alb-zs"></a>

When a zonal shift is started on an Application Load Balancer with cross-zone load balancing enabled, all traffic to targets is blocked in the Availability Zone that is impacted, and the zonal shift removes the zonal IP address from DNS.

For more information, see [Integrations for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-integrations.html#zonal-shift) in the *Application Load Balancer User Guide*.

#### Network Load Balancers
<a name="arc-zonal-shift.resource-types.network-load-balancers"></a>

##### Using zonal shift for Network Load Balancers
<a name="using-nlb-zs"></a>

To use Network Load Balancers with zonal shift, you must enable ARC zonal shift integration in the Network Load Balancer attributes. Network Load Balancer supports zonal shift with cross-zone enabled or cross-zone disabled configurations. 

You can choose which resources to opt-in to use zonal shift and zonal autoshift, and when you would like to fail away from an impaired Availability Zone. Both internet-facing and internal Network Load Balancers are supported. 

To enable zonal shift for your cross-zone enabled Network Load Balancer, all target groups attached to the load balancer must have cross-zone load balancing enabled, or set to `use_load_balancer_configuration`. For more information on target group cross-zone load balancing, see [Cross-zone load balancing for target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/edit-target-group-attributes.html#target-group-cross-zone).

You can start a zonal shift for a Network Load Balancer by using the AWS CLI, the AWS Management Console, or the Elastic Load Balancing widget. When an Application Load Balancer is the target of a Network Load Balancer, you must start the zonal shift from the Network Load Balancer. If you start the zonal shift from the Application Load Balancer, the Network Load Balancer will not stop sending traffic to the Application Load Balancer and its targets.

------
#### [ Console ]

**To enable zonal shift on a load balancer (Console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the **Navigation** page, under **Load balancing**, choose **Load balancers**.

1. Select the Network Load Balancer name.

1. On the **Attributes** tab, choose **Edit**.

1. Under **Availability Zone routing configuration**, for **ARC zonal shift integration**, choose **Enable**.

1. Choose **Save**.

------
#### [ AWS CLI ]

**To enable zonal shift on a load balancer (AWS CLI)**
+ Enter the following command:

  ```
  aws elbv2 modify-load-balancer-attributes --load-balancer-arn {{my-nlb-arn}} --attributes Key=zonal_shift.config.enabled,Value=true
  ```

------

For more information about starting a zonal shift, see [Starting, updating, or canceling a zonal shift](#arc-zonal-shift.start-cancel).

##### How zonal shift works for Network Load Balancers
<a name="howt-it-works-nlb-zs"></a>

ARC creates a health check failure for the registered Network Load Balancer so that the Network Load Balancer node in the impaired AZ is removed from the DNS when you start a zonal shift. The Network Load Balancer disables the targets in the impacted zone so that they stop receiving traffic, and Elastic Load Balancing treats these targets as disabled targets for zonal shift. Targets in the disabled state continue receiving health checks. When the targets are healthy and the zonal shift expires (or is canceled), routing to targets in the previously impaired zone resumes.

During zonal shift on Network Load Balancers with cross-zone load balancing enabled, the zonal load balancer IP addresses are removed from DNS. Existing connections to targets in the impaired Availability Zone persist until they organically close, while new connections are no longer routed to targets in the impaired Availability Zone.

 For more information see [Zonal Shift for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/zonal-shift.html) in the *Network Load Balancer User Guide*. 

### Starting, updating, or canceling a zonal shift
<a name="arc-zonal-shift.start-cancel"></a>

This section provides procedures for working with zonal shifts, including starting a zonal shift and canceling a zonal shift.

#### Starting a zonal shift
<a name="arc-zonal-shift.start"></a>

The steps in this section explain how to start a customer-initiated zonal shift on the Amazon Application Recovery Controller (ARC) console. To work with zonal shift programmatically, see the [ Zonal Shift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

In addition to starting a zonal shift in ARC, you can also start a zonal shift for a load balancer in the Elastic Load Balancing console (in supported Regions). For more information, see [Zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/zonal-shift.html) in the Elastic Load Balancing User Guide.

#### To start a zonal shift


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Under **Multi-AZ**, choose **Zonal shift**.

1. On the **Zonal shift** page, choose **Start zonal shift**.

1. Select the Availability Zone that you want to shift traffic away from.

1. Select a supported resource from the **Resources** table to shift traffic away for.

1. For **Set zonal shift expiration**, choose or enter an expiration for the zonal shift. A zonal shift can set to be active initially for 1 minute or up to three days (72 hours). 

   All zonal shifts are temporary. You must set an expiration, but you can update active shifts later to set a new expiration period of up to three days. 

1. Enter a comment. You can update the zonal shift later to edit the comment, if you like.

1. Select the checkbox to acknowledge that starting a zonal shift will reduce available capacity for your application by shifting traffic away from the Availability Zone.

1. Choose **Start**.

#### Updating or canceling a zonal shift
<a name="arc-zonal-shift.update-cancel"></a>

The steps in this section explain how to update a zonal shift that you initiate, or cancel a zonal shift, on the Amazon Application Recovery Controller (ARC) console. To work with zonal shift programmatically, see the [ Zonal Shift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift. You can cancel a zonal shift any time before it expires.

You can cancel zonal shifts that you initiate, or zonal shifts that AWS starts for a resource for a practice run for zonal autoshift. To learn more about practice shifts in zonal autoshift, see [How zonal autoshift and practice runs work](#arc-zonal-autoshift.how-it-works).

#### To update a zonal shift


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Under **Multi-AZ**, choose **Zonal shift**.

1. Select a zonal shift that you want to update, and then choose **Update zonal shift**.

1. For **Set zonal shift expiration**, optionally select or enter an expiration.

1. For **Comment**, optionally edit the existing comment or enter a new comment.

1. Choose **Update**.

#### To cancel a zonal shift


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Under **Multi-AZ**, choose **Zonal shift**.

1. Select a zonal shift that you want to cancel, and then choose **Cancel zonal shift**.

1. On the confirmation modal dialog, choose **Confirm**.

### Logging and monitoring for zonal shift in Amazon Application Recovery Controller (ARC)
<a name="monitoring-zonal-shift"></a>

You can use AWS CloudTrail for monitoring zonal shift in Amazon Application Recovery Controller (ARC), to analyze patterns and help troubleshoot issues.

**Topics**
+ [Logging zonal shift API calls using AWS CloudTrail](#cloudtrail-zonal-shift)

#### Logging zonal shift API calls using AWS CloudTrail
<a name="cloudtrail-zonal-shift"></a>

Zonal shift for ARC is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in ARC. CloudTrail captures all API calls for zonal shift as events. The calls captured include calls from the ARC console and code calls to the ARC API operations for zonal shift. 

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for zonal shift. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**.

Using the information collected by CloudTrail, you can determine the request that was made to ARC for zonal shift, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

##### Zonal shift information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in ARC for zonal shift, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for zonal shift in ARC, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services, to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All ARC actions are logged by CloudTrail and are documented in the [Routing Control API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/routing-control/latest/APIReference/). For example, calls to the `StartZonalShift` and `ListManagedResources` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

##### Viewing ARC events in event history
<a name="amazon-arc-events-in-cloudtrail-event-history"></a>

CloudTrail lets you view recent events in **Event history**. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*.

##### Understanding zonal shift log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `ListManagedResources` action for zonal shift.

```
{
      "eventVersion": "1.08",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/admin",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "AROA33L3W36EXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/admin",
            "accountId": "111122223333",
            "userName": "EXAMPLENAME"
          },
          "webIdFederationData": {},
          "attributes": {
            "creationDate": "2022-11-14T16:01:51Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2022-11-14T16:14:41Z",
      "eventSource": "arc-zonal-shift.amazonaws.com",
      "eventName": "ListManagedResources",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.50",
      "userAgent": "Boto3/1.17.101 Python/3.8.10 Linux/4.14.231-180.360.amzn2.x86_64 exec-env/AWS_Lambda_python3.8 Botocore/1.20.102",      
      "requestParameters": null,
      "responseElements": null,
      "requestID": "VGXG4ZUE7UZTVCMTJGIAF_EXAMPLE",
      "eventID": "4b5c42df-1174-46c8-be99-d67_EXAMPLE",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333"
      "eventCategory": "Management"
      }
    }
```

The following example shows a CloudTrail log entry that demonstrates the `StartZonalShift` action with a conflict exception for zonal shift.

```
{
      "eventVersion": "1.08",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/admin",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "AROA33L3W36EXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/admin",
            "accountId": "111122223333",
            "userName": "EXAMPLENAME"
          },
          "webIdFederationData": {},
          "attributes": {
            "creationDate": "2022-11-14T16:01:51Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2022-11-14T16:10:38Z",
      "eventSource": "arc-zonal-shift.amazonaws.com",
      "eventName": "StartZonalShift",
     "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.50",
      "userAgent": "Boto3/1.17.101 Python/3.8.10 Linux/4.14.231-180.360.amzn2.x86_64 exec-env/AWS_Lambda_python3.8 Botocore/1.20.102",
      "errorCode": "ConflictException",
      "errorMessage": "There's already an active zonal shift for that resource identifier: 'arn:aws:testservice:us-west-2:077059137270:testResource/456apples'. Active zonal shift: 'bac23b74-176e-c073-de8f-484ca508910f'",
      "requestParameters": {
        "resourceIdentifier": "arn:aws:testservice:us-west-2:077059137270:testResource/456apples",
        "awayFrom": "usw2-az1",
        "expiresIn": "2m",
        "comment": "HIDDEN_FOR_SECURITY_REASONS"
      },
      "responseElements": null,
      "requestID": "OP4OYXZ54HUPMIPGWH_EXAMPLE",
      "eventID": "0bca6660-e999-43a5-9008-EXAMPLE",
      "readOnly": false,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333"
      "eventCategory": "Management"
      }
    }
```

### Identity and Access Management for zonal shift in ARC
<a name="security-iam-zonalshift"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use ARC resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [How zonal shift works with IAM](#security_iam_service-with-iam-zs)
+ [Permissions for zonal shift](#security_iam_service-with-iam-zonal-shift)
+ [Identity-based policy examples](#security_iam_id-based-policy-examples-zonal)

#### How zonal shift works with IAM
<a name="security_iam_service-with-iam-zs"></a>

Before you use IAM to manage access to zonal shift in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with zonal shift.


**IAM features you can use with zonal shift**  

| IAM feature | Zonal shift support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Partial | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes | 

To get a high-level, overall view of how AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Identity-based policies for ARC
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To view examples of ARC identity-based policies, see [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](#security_iam_id-based-policy-examples).

##### Resource-based policies within ARC
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

##### Policy actions for zonal shift
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of ARC actions for zonal shift, see [ Actions defined by Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in ARC for zonal shift use the following prefixes before the action:

```
arc-zonal-shift
```

To specify multiple actions in a single statement, separate them with commas. For example, the following:

```
"Action": [
      "arc-zonal-shift:{{action1}}",
      "arc-zonal-shift:{{action2}}"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "arc-zonal-shift:Describe*"
```

To view examples of ARC identity-based policies for zonal shift, see [Identity-based policy examples for zonal shift in ARC](#security_iam_id-based-policy-examples-zonal).

##### Policy resources for zonal shift
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of resource types and their ARNs, and the actions that you can specify with the ARN of each resource, see the following topic in the *Service Authorization Reference*:
+ [ Actions defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions)

To see the actions and resources that you can use with a condition key, see the following topic in the *Service Authorization Reference*:
+ [ Condition keys defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-policy-keys)

To view examples of ARC identity-based policies for zonal shift, see [Identity-based policy examples for zonal shift in ARC](#security_iam_id-based-policy-examples-zonal).

##### Policy condition keys for zonal shift
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of zonal shift condition keys, see the following topic in the *Service Authorization Reference*:
+ [ Condition keys defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-policy-keys)

To see the actions and resources that you can use with a condition key, see the following topics in the *Service Authorization Reference*:
+ [ Actions defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions)
+ [ Resource types defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html#amazonroute53applicationrecoverycontroller-zonalshift-resources-for-iam-policies)

To view examples of ARC identity-based policies for zonal shift, see [Identity-based policy examples for zonal shift in ARC](#security_iam_id-based-policy-examples-zonal).

##### Access control lists (ACLs) in ARC
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

##### Attribute-based access control (ABAC) with ARC
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

ARC includes the following partial support for ABAC: 
+ Zonal shift supports ABAC for managed resources that are registered in ARC for zonal shift. For more information about ABAC for Network Load Balancer and Application Load Balancer managed resources, see [ ABAC with Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags) in the Elastic Load Balancing User Guide.

##### Using temporary credentials with ARC
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Cross-service principal permissions for ARC
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

When you use an IAM entity (user or role) to perform actions in AWS, you are considered a principal. Policies grant permissions to a principal. When you use some services, you might perform an action that then triggers another action in a different service. In this case, you must have permissions to perform both actions.

To see whether an action requires additional dependent actions in a policy, see the following topic in the *Service Authorization Reference*:
+ [ Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html)

##### Service roles for ARC
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

##### Service-linked roles for ARC
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

Zonal shift does not use service-linked roles. 

#### IAM and permissions for zonal shift
<a name="security_iam_service-with-iam-zonal-shift"></a>

This section provides additional information about how permissions work for the zonal shift feature in Amazon Application Recovery Controller (ARC), especially if you work with the feature from another AWS service, such as Elastic Load Balancing. To learn about how ARC features works with IAM and permissions in general, review the information in the overview topic, [Identity and Access Management for zonal shift in ARC](#security-iam-zonalshift).

Zonal shift supports Application Load Balancers, Network Load Balancers, Amazon EC2 Auto Scaling groups, and Amazon EKS. You can use IAM condition keys to scope an IAM permission policy to these resources. The following is an example policy using a condition key with multiple resources of different types:

```
{
    "Condition": {
        "StringLike": {
            "arc-zonal-shift:ResourceIdentifier": [
                "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/*",
                "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/*",
                "arn:aws:eks:us-east-1:123456789012:cluster/*"
            ]
        }
    },
    "Action": [
        "arc-zonal-shift:StartZonalShift"
    ],
    "Resource": "*",
    "Effect": "Allow"
}
```

For more information, see [Supported resources](#arc-zonal-shift.resource-types).

In addition to the permissions outlined in the IAM overview topic, the following applies to zonal shift for IAM and permissions:
+ Make sure that you have the required permissions for working with zonal shift in ARC. For more information, see [zonal shift console access](#security_iam_id-based-policy-examples-console-zonal) and [zonal shift operations access](#security_iam_id-based-policy-examples-api-zonal).
+ You do not need to add additional Elastic Load Balancing permissions with IAM to work with zonal shifts for managed load balancer resources in your account in ARC.
+ An AWS managed policy that provides full access for Elastic Load Balancing includes permissions for working with zonal shifts. If you use AWS managed policies for Elastic Load Balancing access, you do not need additional permissions in IAM for zonal shift to start zonal shifts for load balancers or work with in the Elastic Load Balancing console. For more information, see [AWS managed policies for Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/managed-policies.html). 

#### Identity-based policy examples for zonal shift in ARC
<a name="security_iam_id-based-policy-examples-zonal"></a>

By default, users and roles don't have permission to create or modify ARC resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by ARC, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices-zonal)
+ [Example: Zonal shift console access](#security_iam_id-based-policy-examples-console-zonal)
+ [Example: Zonal shift API actions](#security_iam_id-based-policy-examples-api-zonal)

##### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices-zonal"></a>

Identity-based policies determine whether someone can create, access, or delete ARC resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

##### Example: Zonal shift console access
<a name="security_iam_id-based-policy-examples-console-zonal"></a>

To access the Amazon Application Recovery Controller (ARC) console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the ARC resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To give users full access to use zonal shift in the AWS Management Console, attach a policy like the following to the user:

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
                   "arc-zonal-shift:ListManagedResources",
                   "arc-zonal-shift:GetManagedResource",
                   "arc-zonal-shift:ListZonalShifts",
                   "arc-zonal-shift:StartZonalShift",
                   "arc-zonal-shift:UpdateZonalShift",
                   "arc-zonal-shift:CancelZonalShift"
             ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeAvailabilityZones",
            "Resource": "*"
        }
    ]
}
```

------

##### Example: Zonal shift API actions
<a name="security_iam_id-based-policy-examples-api-zonal"></a>

The zonal shift API temporarily moves traffic away from an Availability Zone to recover an application.

To ensure that a user can use zonal shift API actions, attach a policy that corresponds to the API operations that the user needs to work with, such as the following:

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
                   "arc-zonal-shift:ListManagedResources",
                   "arc-zonal-shift:GetManagedResource",
                   "arc-zonal-shift:ListZonalShifts",
                   "arc-zonal-shift:StartZonalShift",
                   "arc-zonal-shift:UpdateZonalShift",
                   "arc-zonal-shift:CancelZonalShift"
             ],
            "Resource": "*"
        }
    ]
}
```

------

## Zonal autoshift in ARC
<a name="arc-zonal-autoshift"></a>

With zonal autoshift, you authorize AWS to shift away resource traffic for an application from an Availability Zone (AZ) during events, on your behalf, to help reduce time to recovery. AWS starts an autoshift when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers. When AWS starts an autoshift, application traffic to resources that you've configured for zonal autoshift starts shifting away from the Availability Zone.

Be aware that ARC does not inspect the health of individual resources. AWS starts an autoshift when AWS telemetry detects that there is an Availability Zone impairment that could potentially impact customers. In some cases, traffic might be shifted away for resources that are not experiencing impact.

With zonal autoshift, you also authorize AWS to shift away resource traffic for an application from an Availability Zone, on your behalf, for regular practice runs. Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application. Practice runs regularly test that your application can operate normally without one Availability Zone by starting zonal shifts that shift traffic for a resource away from an Availability Zone. Practice runs take place weekly, and provide an outcome—such as `SUCCEEDED` or `FAILED`—to help you understand if the application operates as expected.

**Important**  
Before you configure practice runs or enable zonal autoshift, we strongly recommend that you pre-scale your application resource capacity in all Availability Zones in the Region where your application resources are deployed. You should not rely on scaling on demand when an autoshift or practice run starts. Zonal autoshift, including practice runs, works independently, and does not wait for auto scaling actions to complete. Relying on auto scaling, instead of pre-scaling, can result in it taking longer for your application to recover.  
If you use auto scaling to handle regular cycles of traffic, we strongly recommend that you configure the minimum capacity of your auto scaling to continue operating normally with the loss of an Availability Zone. 

If you plan to enable zonal autoshift or configure practice runs, after you pre-scale your application resource capacity, test that your application can operate normally without one Availability Zone. To test this, start a zonal shift to move traffic for a resource away from an Availability Zone.

After you enable zonal autoshift, we recommend that you verify, by starting and evaluating an on-demand practice run zonal shift, that your application can continue operating normally with traffic shifted away from an Availability Zone. Then, the regular practice runs that ARC performs help you to confirm, on an ongoing basis, that you have enough capacity for an autoshift.

To ensure that your tests with zonal shift are effective, it's important to validate that traffic drains as expected from the AZ you shift away from. For example, both Application Load Balancers and Network Load Balancers provide per AZ metrics in Amazon CloudWatch that you can use to monitor this. Depending on how long a service and clients reuse connections, traffic might continue to the AZ that you have shifted away from for longer than you expect. To learn more, see [Limit the time that clients stay connected to your endpoints](#ZAConsiderationsCurrentConnections).

You can enable zonal autoshift, for a supported resource, in the ARC console. Or, in the Amazon EC2 console, you have the option to enable zonal autoshift for a specific load balancer resource. To learn more about enabling zonal autoshift with Elastic Load Balancing, see [Zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/zonal-shift.html) in the Elastic Load Balancing User Guide.

Autoshifts and practice run zonal shifts are temporary. With autoshifts, when the affected Availability Zone recovers, AWS stops shifting traffic for resources away from the Availability Zone. Application traffic for customers returns to all Availability Zones in the Region. With a practice run, traffic is shifted away from an Availability Zone for a single resource for about 30 minutes, and then shifted back to all Availability Zones in the Region.

You can configure Amazon EventBridge notifications to alert you about autoshifts and practice runs. For more information, see [Using zonal autoshift with Amazon EventBridge](#eventbridge-zonal-autoshift).

### How zonal autoshift and practice runs work
<a name="arc-zonal-autoshift.how-it-works"></a>

The zonal autoshift capability in Amazon Application Recovery Controller (ARC) allows AWS to shift traffic for a resource away from an Availability Zone, on your behalf, when AWS determines that there's an impairment that could potentially affect customers in the Availability Zone. Zonal autoshift is designed for a resource that is pre-scaled in all Availability Zones in an AWS Region, so that an application can operate normally with the loss of one Availability Zone.

With zonal autoshift, you are required to configure practice runs, where ARC regularly shifts traffic for the resource away from one Availability Zone. ARC schedules practice runs about weekly for each resource that has a practice run configuration associated with it. Practice runs for each resource are scheduled independently.

For each practice run, ARC records an outcome. If a practice run is interrupted by a blocking condition, the practice run outcome is not marked as successful. For more information about practice run outcomes, see [Outcomes for practice runs](#ZAConsiderationsPracticeRunOutcomes). 

You can configure Amazon EventBridge notifications to send you information about autoshifts and practice runs. For more information, see [Using zonal autoshift with Amazon EventBridge](#eventbridge-zonal-autoshift).

**Topics**
+ [About zonal autoshift](#arc-zonal-autoshift.how-it-works.about)
+ [When AWS starts and stops autoshifts](#arc-zonal-autoshift.how-it-works.start-stop-auto)
+ [When ARC schedules, starts, and ends practice runs](#arc-zonal-autoshift.how-it-works.scheduled-practice-runs)
+ [Capacity checks for practice runs](#arc-zonal-autoshift.how-it-works.capacity-check)
+ [Notification for practice runs and autoshifts](#arc-zonal-autoshift.how-it-works.notifications)
+ [Precedence for zonal shifts](#arc-zonal-autoshift.how-it-works.precedence)
+ [Stopping an active autoshift or practice run](#arc-zonal-autoshift.how-it-works.stop-shift)
+ [How traffic is shifted away](#arc-zonal-autoshift.how-it-works.how-traffic-shifted)
+ [Alarms for practice runs](#arc-zonal-autoshift.how-it-works.alarms)
+ [Blocked windows and allowed windows (in UTC)](#arc-zonal-autoshift.how-it-works.blocked-windows)

#### About zonal autoshift
<a name="arc-zonal-autoshift.how-it-works.about"></a>

Zonal autoshift is a capability where AWS shifts application resource traffic away from an Availability Zone, on your behalf. AWS starts an autoshift when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers. The internal telemetry incorporates metrics from several sources, including the AWS network, and the Amazon EC2 and Elastic Load Balancing services. 

You must manually enable zonal autoshift for supported AWS resources. 

When you deploy and run AWS applications on load balancers in multiple (typically three) AZs in a Region, and you pre-scale to support static stability, AWS can quickly recover customer applications in an AZ by shifting traffic away with an autoshift. By shifting away resource traffic to other AZs in the Region, AWS can reduce the duration and severity of potential impact caused by power outages, hardware or software issues in an AZ, or other impairments.

The resources supported by ARC provide integrations that mark the specified AZ as unhealthy, which results in traffic being shifted away from the impaired AZ. 

When you enable zonal autoshift for a resource, you must also configure a practice run for the resource. AWS performs practice runs about weekly, for 30 minutes, to help you make sure that you have enough capacity to run your application without one of the Availability Zones in the Region.

As with zonal shift, there are a few specific scenarios where zonal autoshift does not shift traffic away from the AZ. For example, if the load balancer target groups in the AZs don't have any instances, or if all of the instances are unhealthy, then the load balancer is in a fail open state and you can't shift away one of the AZs.

To learn more about zonal autoshift, see [Zonal autoshift in ARC](#arc-zonal-autoshift).

#### When AWS starts and stops autoshifts
<a name="arc-zonal-autoshift.how-it-works.start-stop-auto"></a>

When you enable zonal autoshift for a resource, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.

To achieve this, zonal autoshift uses AWS telemetry to detect, as early as possible, that there is an Availability Zone impairment that could potentially impact customers. When AWS starts an autoshift, traffic to configured resources immediately starts shifting away from the impaired Availability Zone that could potentially impact customers.

Zonal autoshift is a capability designed for customers who have pre-scaled their application resources for all Availability Zones in an AWS Region. You should not rely on scaling on demand when an autoshift or practice run starts.

AWS ends an autoshift when it determines that the Availability Zone has recovered.

#### When ARC schedules, starts, and ends practice runs
<a name="arc-zonal-autoshift.how-it-works.scheduled-practice-runs"></a>

ARC schedules a practice run for a resource weekly, for about 30 minutes. ARC schedules, starts, and manages practice runs for each resource independently. ARC does not batch together practice runs for resources in the same account. You can also start on-demand practice runs yourself, to help verify that your setup is safe for a zonal autoshift event.

When a practice run continues for the expected duration, without interruption, it is marked with an outcome of `SUCCESSFUL`. There are several other possible outcomes: `FAILED`, `INTERRUPTED`, `CAPACITY_CHECK_FAILED` and `PENDING`. Outcome values and descriptions are included in the [Outcomes for practice runs](#ZAConsiderationsPracticeRunOutcomes) section.

There are some scenarios when ARC interrupts a practice run and ends it. For example, if an autoshift starts during a practice run, ARC interrupts the practice run and ends it. As another example, say that the resource has an adverse response to a practice run and causes an alarm that you've specified to monitor the practice run to go into an `ALARM` state. In this scenario, ARC also interrupts the practice run and ends it.

In addition, there are several scenarios when ARC does not start a schedule practice run for a resource.

In response to interrupted and blocked practice runs for a resource, ARC does the following:
+ If a practice run for a resource is interrupted while it's in progress, ARC considers the weekly practice run to be over, and schedules a new practice run for the resource for the next week. The weekly practice outcome is `INTERRUPTED` in this scenario, not `FAILED`. The practice run outcome set to `FAILED` only when the outcome alarm that monitors the practice run goes into an `ALARM` state during the practice run. 
+ If there is a blocking constraint when a practice run for a resource is scheduled to be started, ARC does not start the practice run. ARC continues regular monitoring, to determine if there are still one or more blocking constraints. When there aren't any blocking constraints, ARC starts the practice run for the resource.

The following are examples of blocking constraints that stop ARC from starting, or continuing, a practice run for a resource:
+ ARC does not start or continue practice runs when there is an AWS Fault Injection Service experiment in progress. If an AWS FIS event is active when ARC has scheduled a practice run to start, ARC does not start the practice run. ARC monitors throughout practice runs for blocking constraints, including an AWS FIS event. If an AWS FIS event starts while a practice run is active, ARC ends the practice run and doesn't attempt to start another one until the next regularly scheduled practice run for the resource.
+ If there is a current AWS event in a Region, ARC does not start practice runs for resources, and ends active practice runs, in the Region.

When the practice run finishes without being interrupted, ARC schedules the next practice run in a week, as usual. If a practice run isn't started because of a blocking constraint, such as a AWS FIS experiment or a blocked time window that you've specified, ARC continues to attempt to start a practice run until the practice run can be started.

#### Capacity checks for practice runs
<a name="arc-zonal-autoshift.how-it-works.capacity-check"></a>

When a practice run starts, to temporarily move traffic away from an Availability Zone, ARC runs a check to verify that you have enough capacity in other Availability Zones to safely move traffic away from the AZ. If there isn't sufficient capacity available, the traffic shift for the practice run is not started and the practice run ends. 

In addition, ARC runs a capacity check for load balancer resources when a zonal autoshift completes, before ARC ends the traffic shift started by the autoshift. If the capacity check fails when the autoshift ends, traffic is not shifted back to the Availability Zone that it was moved away from.

Checks for balanced capacity are only completed for load balancers and Auto Scaling groups.

For a load balancer resource, capacity checks validate that healthy hosts associated with the load balancer are distributed across Availability Zones. Specifically, capacity checks make sure that the number of healthy hosts across all Availability Zones where the resource is registered are balanced. For capacity checks, balanced means that the healthy capacity for each Availability Zone is in parity with the other zones, within a small variance.

Note that capacity checks are not applied to load balancers with target groups of type Lambda nor to load balancers with target groups of type Application Load Balancer, because those targets are not configured zonally.

Capacity checks are also completed for Auto Scaling groups. For an Auto Scaling group, capacity checks validate that the total healthy zonal capacity of an Auto Scaling group–that is, the number of total healthy hosts across all the Availability Zones–meet the desired capacity set for that Auto Scaling group. 

**When a capacity check fails**

When a capacity check finds that available capacity isn't balanced for a resource, the outcome for the practice run is `CAPACITY_CHECK_FAILED`. To learn more about why a capacity check has failed, see the comment field for the `ZonalShiftSummary`. To find the comment field for your practice run zonal shift, do the following:

1. Using the AWS CLI, list the zonal shifts for the resource that you specified in the practice run using the [ListZonalShifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListZonalShifts.html) API operation. 

   FOr example, to return the zonal shifts, you can run a command similar to the following:

   ```
   aws arc-zonal-shift start-practice-run 
       --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}"
   ```

1. Review the array of `ZonalShiftSummary` objects returned to find the zonal shift for the practice run that failed due to capacity checks.

1. For the applicable zonal shift, review the information in the `Comment` field.

#### Notification for practice runs and autoshifts
<a name="arc-zonal-autoshift.how-it-works.notifications"></a>

You can choose to be notified about practice runs and autoshifts for your resource by setting up Amazon EventBridge notifications. You can set up EventBridge notifications even when you haven't enabled zonal autoshift for any resources, known as *autoshift observer notification*. With autoshift observer notification, you are notified about all autoshifts that ARC starts when an Availability Zone is potentially impaired. Note that you must configure this option in each AWS Region that you want to receive notifications about. 

To see the steps for enabling autoshift observer notification, see [Enabling or disabling autoshift observer notification](#arc-zonal-autoshift.enable-autoshift-observer). To learn more about notification options and how to configure them in EventBridge, see [Using zonal autoshift with Amazon EventBridge](#eventbridge-zonal-autoshift).

#### Precedence for zonal shifts
<a name="arc-zonal-autoshift.how-it-works.precedence"></a>

There can be no more than one applied zonal shift at a given time. That is, only one practice run zonal shift, customer-initiated zonal shift, autoshift, or AWS FIS experiment for the resource. When a second zonal shift is started, ARC follows a precedence to determine which zonal shift type is in effect for a resource. 

The general principle for precedence is that zonal shifts that you start as a customer take precedence over other shift types. However, be aware that a currently-running AWS-initiated practice run prevents you from starting an on-demand practice run.

To illustrate precedence in ARC, the following is how precedence works for example scenarios:


| Zonal shift type applied | Zonal shift type initiated | Result | 
| --- | --- | --- | 
| AWS FIS experiment | Practice run | The practice run will fail to start, as the AWS FIS experiment takes precedence.  | 
| AWS FIS experiment | Manual zonal shift | The AWS FIS experiment will be canceled, and the manual zonal shift will be applied.  | 
| AWS FIS experiment | Zonal autoshift | The AWS FIS experiment will be canceled, and the zonal autoshift will be applied.  | 
| AWS FIS experiment | AWS FIS experiment | The initiated AWS FIS experiment will fail to start because there is an existing experiment running that triggered the AWS FIS autoshift action. | 
| Practice run | Manual zonal shift | The practice run will be canceled and the outcome set to INTERRUPTED, and the zonal shift will be applied. | 
| Practice run | AWS FIS experiment | The practice run will be canceled and the outcome set to INTERRUPTED, and the AWS FIS experiment will be applied. | 
| Practice run | Zonal autoshift | The practice run will be canceled and the outcome set to INTERRUPTED, and the zonal autoshift will be applied. | 
| Manual zonal shift | Practice run | The practice run will fail to start. | 
| Manual zonal shift | AWS FIS experiment | The AWS FIS experiment will fail to start, or fail if it's already in progress. | 
| Manual zonal shift | Zonal autoshift | The zonal autoshift will be ACTIVE but not APPLIED on the resource. The manual zonal shift takes precedence. | 
| Zonal autoshift  | AWS FIS experiment | The AWS FIS experiment will fail to start, or will fail if it's in progress. | 
| Zonal autoshift  | Manual zonal shift | The zonal autoshift will be ACTIVE but not APPLIED on the resource. The manual zonal shift takes precedence. | 
| Zonal autoshift  | Practice run | The practice run will fail to start, as the zonal autoshift takes precedence. | 

The traffic shift that is currently in effect for the resource has an applied zonal shift status set to `APPLIED`. Only one shift is set to `APPLIED` at any time. Other shifts that are in progress are set to `NOT_APPLIED`, but remain with `ACTIVE` status.

#### Stopping an active autoshift or practice run for a resource
<a name="arc-zonal-autoshift.how-it-works.stop-shift"></a>

To stop an in-progress autoshift for a resource you must cancel the zonal shift.

Regular practice runs still take place for the resource, on the same schedule. If you want to stop practice runs in addition to disabling autoshifts, you must delete the practice run configuration associated with the resource.

When you delete a practice run configuration, AWS stops performing practice runs that shift traffic for the resource away from an Availability Zone each week. In addition, because zonal autoshift requires practice runs, when you delete a practice run configuration using the ARC console, this action also disables zonal autoshift for the resource. However, note that if you use the zonal autoshift API to delete a practice run, you must first disable zonal autoshift for the resource.

For more information, see [Canceling a zonal autoshift](#arc-zonal-autoshift.canceling-an-autoshift) and [Enabling and working with zonal autoshift](#arc-zonal-autoshift.start-cancel).

#### How traffic is shifted away
<a name="arc-zonal-autoshift.how-it-works.how-traffic-shifted"></a>

For autoshifts and for practice run zonal shifts, traffic is shifted away from an Availability Zone using the same mechanism that ARC uses for customer-initiated zonal shifts. An unhealthy health check results in Amazon Route 53 withdrawing the corresponding IP addresses for the resource from DNS, so that traffic is redirected from the Availability Zone. New connections are now routed to other Availability Zones in the AWS Region instead.

With an autoshift, when an Availability Zone recovers and AWS decides to end the autoshift, ARC reverses the health check process, requesting the Route 53 health checks to be reverted. Then, the original zonal IP addresses are restored and, if the health checks continue to be healthy, the Availability Zone is included in the application's routing again.

It's important to be aware that autoshifts are not based on health checks that monitor the underlying health of load balancers or applications. ARC uses health checks to move traffic away from Availability Zones, by requesting health checks to be set to unhealthy, and then restores health checks to normal again when it ends an autoshift or zonal shift. 

#### Alarms for practice runs
<a name="arc-zonal-autoshift.how-it-works.alarms"></a>

You can specify two types of CloudWatch alarms for practice runs in zonal autoshift: outcome alarms and blocking alarms. 

**Outcome alarms (required)**  
 For the first type of alarm, the *outcome alarm*, at least one alarm is required to be specified. You should configure outcome alarms to monitor the health of your application when traffic is shifted away from an Availability Zone during each 30-minute practice run.  
For a practice run to be effective, specify as outcome alarms at least one CloudWatch alarm that meets both of the following criteria:  
The alarm monitors metrics for the resource, or for your application  
AND  
The alarm responds with an `ALARM` state when your application is adversely affected by the loss of one Availability Zone.  
For more information, see the **Alarms that you specify for practice runs** section in [Best practices when you configure zonal autoshift](#arc-zonal-autoshift.considerations).  
Outcome alarms also provide information for the *practice run outcome* that ARC reports for each practice run. If an outcome alarm enters an `ALARM` state, ARC ends the practice run and returns a practice run outcome of `FAILED`. If the practice run completes the 30 minute test period and none of the outcome alarms that you've specified enters an `ALARM` state, the outcome returned is `SUCCEEDED`. A list of all outcome values, with descriptions, is provided in the [Outcomes for practice runs](#ZAConsiderationsPracticeRunOutcomes) section.

**Blocking alarms (optional)**  
Optionally, you can specify a second type of alarm, the *blocking alarm*. Blocking alarms block practice runs from starting, or continuing, when one or more of the alarms is in an `ALARM` state. Blocking alarms block practice run traffic shifts from being started—and stop any practice runs in progress—when at least one of the alarms is in an `ALARM` state.   
For example, in a large architecture with multiple microservices, when one microservice is experiencing a problem, you typically want to stop all other changes in the application environment, which would including blocking practice runs. You can add a blocking alarm in ARC to accomplish this.

#### Blocked windows and allowed windows (in UTC)
<a name="arc-zonal-autoshift.how-it-works.blocked-windows"></a>

You have the option to *block* or *allow* practice runs for specific calendar dates, or for specific time windows, that is, days and times, specified in UTC. 

For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for `2024-05-01`.

Or, say you run business report summaries three days a week. For this scenario, you could set the following recurring days and times as blocked windows, for example, in UTC: `MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30`.

Alternatively, you might decide that Wednesdays and Fridays from noon to 5:00 are the best times for ARC to start practice runs, to test your setup. For this scenario, you could set the following recurring days and times as allowed windows, for example, in UTC: `WED-12:00-17:00 FRI-12:00-17:00`.

### AWS Region availability for zonal autoshift
<a name="introduction-region-zonal-autoshift"></a>

Zonal shift and zonal autoshift are currently available in the commercial AWS Regions, as well as the China Regions, that is, China (Beijing) Region and China (Ningxia) Region. 

Resources that use Amazon Application Recovery Controller (ARC) can include additional considerations. For more information, see [Supported resources](#arc-zonal-shift.resource-types).

For a list of Regions and detailed information about Regional support and service endpoints for ARC, see [Amazon Application Recovery Controller (ARC) endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/r53arc.html) in the *Amazon Web Services General Reference*.

### Zonal autoshift components
<a name="introduction-components-zonal-autoshift"></a>

The following diagram illustrates an example of an autoshift shifting traffic away from an Availability Zone. AWS starts an autoshift when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers. 

![Diagram of an autoshift with three Availability Zones](https://docs.aws.amazon.com/r53recovery/latest/dg/images/ZonalAutoshiftDiagram.png)


The following are components of the zonal autoshift capabilities in ARC.

**Zonal autoshifts**  
Zonal autoshift shifts traffic away for a resource, without requiring you to take any action. Zonal autoshift is a capability in ARC where AWS starts an autoshift when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers. Be aware that, in some cases, resources might be shifted away that are not experiencing impact.

**Practice runs**  
When you enable zonal autoshift for a resource, you must also configure zonal autoshift *practice runs* for the resource. AWS performs a zonal shift for practice runs about weekly, for about 30 minutes. You can also schedule practice runs on-demand.   
Practice runs make sure that your application can run normally with the loss of one Availability Zone. In a practice run, AWS shifts traffic for a resource away from one Availability Zone with a zonal shift, and then shifts traffic back when the practice run ends. 

**Practice run configurations**  
With a practice run configuration, you can define the time frames (blocked or allowed windows)for when ARC can start a practice run for a resource with zonal autoshift. You also define the CloudWatch alarms for an AWS practice run. You can edit a practice run configuration at any time, to add or change blocked or allowed windows, or to update the alarms for the practice run.  
To enable zonal autoshift, you must have a practice run configuration in place for a resource.  
You can delete a practice run, but first, you must disable zonal autoshift.

**Practice run alarms**  
When you configure practice runs, you specify CloudWatch alarms (that you first create in CloudWatch), based on your resource and application requirements. The alarms that you specify can block a practice run from starting, or can stop a practice run in progress, if your application is adversely affected by the practice run.  
If an alarm that you specify goes into an `ALARM` state, ARC ends the zonal shift for the practice run, so that traffic for the resource is no longer shifted away from the Availability Zone.  
There are two types of alarms that you specify for practice runs: *outcome* alarms, to monitor the health of your resource and application during the practice run, and *blocking* alarms, which you can configure to prevent practice runs from starting, or to stop an in-progress practice run. At least one outcome alarm is required; blocking alarms are optional.

**Practice run outcomes**  
ARC reports an outcome for each practice run. The following are the possible practice run outcomes:   
+ **PENDING:** The zonal shift for the practice run is active (in progress). There's no outcome to return yet.
+ **SUCCEEDED:** The outcome alarm did not enter an `ALARM` state during the practice run, and the practice run completed the full 30 minute test period.
+ **INTERRUPTED:** The practice run ended for a reason that was not the outcome alarm entering an `ALARM` state. A practice run can be interrupted for a variety of reasons. For example, a practice run that ends because the blocking alarm specified for the practice run entered an `ALARM` state has an outcome of `INTERRUPTED`. For more information about reasons for an `INTERRUPTED` outcome, see [Outcomes for practice runs](#ZAConsiderationsPracticeRunOutcomes).
+ **FAILED:** The outcome alarm entered an `ALARM` state during the practice run.
+ **CAPACITY\_CHECK\_FAILED:** The check for balanced capacity across Availability Zones for your load balancing and Auto Scaling group resources failed.

**Built-in safety rules**  
Safety rules built into ARC prevent more than one traffic shift for a resource from being in effect at a time. That is, only one customer-initiated zonal shift, practice run zonal shift (initiated by AWS or by a customer), or autoshift for the resource can be actively shifting traffic away from an Availability Zone. For example, if you start a zonal shift for a resource when it is currently shifted away with autoshift, your zonal shift takes precedence. For more information, see [Precedence for zonal shifts](#ZAShiftPrecedence).

**Resource identifier**  
The identifier for a resource to enable zonal autoshift for, which is the Amazon Resource Name (ARN) for the resource. You can only enable zonal autoshift for resources in your account that are in an AWS service that is supported by ARC. 

**Managed resource**  
Application Load Balancers register resources automatically with ARC for zonal autoshift. You must manually opt-in other resources for zonal autoshift.

**Resource name**  
The name of a managed resource in ARC.

**Applied status**  
An applied status indicates whether a traffic shift is in effect for a resource. When you configure zonal autoshift, a resource can have more than one active traffic shift—that is, a practice run zonal shift, customer-initiated zonal shift, or autoshift. However, only one is *applied*, that is, is in effect for the resource at a time. The shift that has the status `APPLIED` determines the Availability Zone where application traffic has been shifted away for a resource, and when that traffic shift ends.

**Shift type**  
Defines the zonal shift type. Zonal shifts can have one of the following types:  
+ **ZONAL\_SHIFT**
+ **ZONAL\_AUTOSHIFT**
+ **PRACTICE\_RUN**
+ **FIS\_EXPERIMENT**

### Data and control planes for zonal autoshift
<a name="data-and-control-planes-zonal-autoshift"></a>

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that you make sure that the mechanisms that you depend on during failover are highly available, so that you can use them when you need them in a disaster scenario. Typically, you should use data plane functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind, it's important to understand how the functionality of a service is divided between control planes and data planes, and when you can rely on an expectation of extreme reliability with a service's data plane.

In general, a *control plane* enables you to do basic management functions, such as create, update, and delete resources in the service. A *data plane* provides a service's core functionality.

For more information about data planes, control planes, and how AWS builds services to meet high availability targets, see the [Static stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) in the Amazon Builders' Library.

### Pricing for zonal autoshift in ARC
<a name="introduction-pricing-zonal-autoshift"></a>

For zonal autoshift, AWS shifts traffic away from an Availability Zone on your behalf for supported resources when AWS determines that there is a potential issue that can adversely affect customer applications. There is no additional charge for enabling zonal autoshift. 

For detailed pricing information for ARC and pricing examples, see [ARC Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

### Best practices when you configure zonal autoshift
<a name="arc-zonal-autoshift.considerations"></a>

Be aware of the following best practices and considerations when you enable zonal autoshift in Amazon Application Recovery Controller (ARC).

Zonal autoshift includes two types of traffic shifts: autoshifts and practice run zonal shifts. 
+ With an *autoshift*, AWS helps reduce your time to recovery by shifting away application resource traffic from an Availability Zone during events, on your behalf. 
+ With *practice runs*, ARC starts a zonal shift on your behalf or you start a zonal shift practice run. The AWS practice run zonal shift shifts traffic away from an Availability Zone for a resource, and back again, on a weekly cadence. Practice runs help you to make sure that you have scaled up sufficient capacity for Availability Zones in a Region for your application to tolerate the loss of one Availability Zone.

There are several best practices and considerations to keep in mind with autoshifts and practice runs. Review the following topics before you enable zonal autoshift or configure practice runs for a resource.

**Topics**
+ [Limit the time that clients stay connected to your endpoints](#ZAConsiderationsCurrentConnections)
+ [Prescale your resource capacity and test shifting traffic](#ZAConsiderationsCapacityPrescaling)
+ [Be aware of resource types and restrictions](#ZAConsiderationsResourceRequirements)
+ [Specify alarms for practice runs](#ZAConsiderationsPracticeRunAlarms)
+ [Evaluate outcomes for practice runs](#ZAConsiderationsPracticeRunOutcomes)

**Limit the time that clients stay connected to your endpoints**  
When Amazon Application Recovery Controller (ARC) shifts traffic away from an impairment, for example, by using zonal shift or zonal autoshift, the mechanism that ARC uses to move your application traffic is a DNS update. A DNS update causes all new connections to be directed away from the impaired location. However, clients with pre-existing open connections might continue to make requests against the impaired location until the clients reconnect. To ensure a quick recovery, we recommend that you limit the amount of time clients stay connected to your endpoints.   
If you use an Application Load Balancer, you can use the `keepalive` option to configure how long connections continue. We suggest that you lower the `keepalive` value to be inline with your recovery time goal for your application, for example, 300 seconds. When you choose a `keepalive` time, consider that this value is a trade off between reconnecting more frequently in general, which can affect latency, and more quickly moving all clients away from an impaired AZ or Region.  
For more information about setting the `keepalive` option for Application Load Balancer, see the [ HTTP client keepalive duration](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#http-client-keep-alive-duration) in the Application Load Balancer User Guide.

**Prescale your resource capacity and test shifting traffic**  
When AWS shifts traffic away from one Availability Zone for a zonal shift or an autoshift, it's important that the remaining Availability Zones can service the increased request rates for your resource. This pattern is known as *static stability*. For more information, see the [ Static stability using Availability Zones whitepaper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) in the Amazon Builder’s Library.  
For example, if your application requires 30 instances to serve its clients, you should provision 15 instances across three Availability Zones, for a total of 45 instances. By doing this, when AWS shifts traffic away from one Availability Zone—with an autoshift or during a practice run—AWS can still serve your application’s clients with the remaining total of 30 instances, across two Availability Zones.  
The zonal autoshift capability in ARC helps you to quickly recover from AWS events in an Availability Zone when you have an application with resources that are pre-scaled to work normally with the loss of one Availability Zone. Before you enable zonal autoshift for a resource, scale your resource capacity in all configured Availability Zones in an AWS Region. Then, start zonal shifts for the resource, to test that your application still runs normally when traffic is shifted away from an Availability Zone.   
After you test with zonal shifts, then enable zonal autoshift and configure practice runs for application resources. Run your own on-demand practice runs to help ensure that your configuration is scaled properly. Regular practice runs with zonal autoshift help you to make sure—on an ongoing basis—that your capacity is still scaled appropriately. With sufficient capacity across Availability Zones, your application can continue to serve clients, without interruption, during an autoshift.  
For more information about starting a zonal shift for a resource, see [Zonal shift in ARC](#arc-zonal-shift).

**Be aware of resource types and restrictions**  
Zonal autoshift supports shifting traffic out of an Availability Zone for all resources that are supported by zonal shift. In a few specific resource scenarios, zonal autoshift does not shift traffic from an Availability Zone for an autoshift.  
For example, if the load balancer target groups in the Availability Zones don't have any instances, or if all of the instances are unhealthy, then the load balancer is in a fail open state. If AWS starts an autoshift for a load balancer in this scenario, an autoshift does not change which Availability Zones the load balancer uses because the load balancer is already in a fail open state. This is expected behavior. Autoshift cannot cause one Availability Zone to be unhealthy and shift traffic to the other Availability Zones in an AWS Region if all Availability Zones are failing open (unhealthy).  
To see details about supported resources, including all of the requirements and exceptions to be aware of, see [Supported resources](#arc-zonal-shift.resource-types).

**Specify alarms for practice runs**  
You must configure at least one type of alarm (an outcome alarm) for practice runs with zonal autoshift. Optionally, you can also configure a second type of alarm (blocking alarms).  
When you consider the CloudWatch alarms that you configure for practice runs for your resource, keep in mind the following:  
+ You're required to configure at least one outcome alarm for a practice run configuration. For outcome alarms, we recommend that you configure CloudWatch alarms to go into an `ALARM` state when metrics for the resource, or your application, indicate that shifting traffic away from the Availability Zone adversely impacts performance. For example, you can determine a threshold for request rates for your resource, and then configure an alarm to go into an `ALARM` state when the threshold is exceeded. You are responsible for configuring appropriate alarms that cause AWS to end the practice run and return a `FAILED` outcome. 
+ We recommend that you follow the [AWS Well Architected Framework](https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_monitor_instances_post_launch_establish_kpi.html), which advises you to implement key performance indicators (KPIs) as CloudWatch alarms. If you do so, you can use these alarms to create a composite alarm to use as a safety trigger, to prevent practice runs from starting if they might cause your application to miss a KPI. When the alarm is no longer in an `ALARM` state, ARC starts practice runs the next time a practice run is scheduled for the resource.
+ For practice run blocking alarms, if you choose to configure one (or more), you might choose to track specific metrics that you use to indicate that you don't want an AWS practice run to start—for example, when an alarm indicates that there is an ongoing incident.
+ For practice run alarms, you specify the Amazon Resource Name (ARN) for each alarm, so you must first configure the alarm in Amazon CloudWatch. The CloudWatch alarms that you specify can be composite alarms, to enable you to include several metrics and checks for your application and resource that can trigger the alarm to go into an `ALARM` state. Or, you can configure separate alarms, and then specify more than one alarm of each type for your practice run configuration. For more information, see [Combining alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) in the Amazon CloudWatch User Guide.
+ Make sure that the CloudWatch alarms that you specify for practice runs are in the same Region as the resource that you're configuring a practice run for.

**Evaluate outcomes for practice runs**  
ARC reports an outcome for each practice run. After a practice run, evaluate the outcome, and determine if you need to take action. For example, you might need to scale capacity or adjust the configuration for an alarm.  
The following are the possible practice run outcomes:   
+ **SUCCEEDED:** No outcome alarms entered an `ALARM` state during the practice run, and the practice run completed the full 30 minute test period.
+ **FAILED: ** At least one outcome alarm entered an `ALARM` state during the practice run.
+ **INTERRUPTED: ** The practice run ended for a reason that was not the outcome alarm entering an `ALARM` state. A practice run can be interrupted for a variety of reasons, including the following: 
  + Practice run was ended because AWS started an autoshift in the AWS Region or there was an alarm condition in the Region.
  + Practice run was ended because the practice run configuration was deleted for the resource.
  + Practice run was ended because a customer-initiated zonal shift was started for the resource in the Availability Zone that the practice run zonal shift was shifting traffic away from.
  + Practice run was ended because a CloudWatch alarm that was specified for the practice run configuration could no longer be accessed.
  + Practice run was ended because a blocking alarm specified for the practice run entered an `ALARM` state.
  + Practice run was ended for an unknown reason.
  + Practice run was ended because a zonal autoshift with precedence was initiated. See [Precedence for zonal shifts](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html#ZAShiftPrecedence).
+ **CAPACITY\_CHECK\_FAILED:** The check for balanced capacity across Availability Zones for your load balancing and Auto Scaling group resources failed.
+ **PENDING:** The practice run is active (in progress). There's no outcome to return yet.

### Zonal autoshift API operations
<a name="actions.zonalautoshift"></a>

The following table lists ARC API operations that you can use with zonal autoshift. For examples of using zonal autoshift API operations with the AWS CLI, see .

For examples of how to use common zonal autoshift API operations with the AWS Command Line Interface, see [Examples of using the AWS CLI with zonal autoshift](#getting-started-cli-zonal-autoshift).


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Create a practice run configuration | See [Enabling or disabling zonal autoshift](#arc-zonal-autoshift.configure) | See [CreatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CreatePracticeRunConfiguration.html) | 
| Delete a practice run configuration | See [Configuring, editing, or deleting a practice run configuration](#arc-zonal-autoshift.edit-delete-practice-run) | See [DeletePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_DeletePracticeRunConfiguration.html) | 
| List autoshifts | See [Zonal autoshift in ARC](#arc-zonal-shift) | See [ListAutoshifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html) | 
| List resources for zonal autoshift | See [Supported resources](#arc-zonal-shift.resource-types) | See [ListManagedResources](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html) | 
| Get resources for zonal autoshift | See [Supported resources](#arc-zonal-shift.resource-types) | See [GetManagedResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetManagedResource.html) | 
| Edit a practice run configuration | See [Configuring, editing, or deleting a practice run configuration](#arc-zonal-autoshift.edit-delete-practice-run) | See [UpdatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdatePracticeRunConfiguration.html) | 
| Enable or disable zonal autoshift | See [Enabling or disabling zonal autoshift](#arc-zonal-autoshift.configure) | See [UpdateZonalAutoshiftConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalAutoshiftConfiguration.html) | 
| Enable or disable autoshift observer notification | See [Enabling and working with zonal autoshift](#arc-zonal-autoshift.start-cancel) | See [UpdateAutoshiftObserverNotificationStatus](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateAutoshiftObserverNotificationStatus.html) | 
| Start a practice run | See [Starting a practice run zonal shift](#arc-zonal-autoshift.start-cancel) | See [StartPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartPracticeRun.html) | 
| Cancel a practice run | See [Canceling a practice run zonal shift](#arc-zonal-autoshift.start-cancel) | See [CancelPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelPracticeRun.html) | 

### Examples of using the AWS CLI with zonal autoshift
<a name="getting-started-cli-zonal-autoshift"></a>

This section walks through simple application examples of working with zonal autoshift, using the AWS Command Line Interface to work with the zonal autoshift capability in Amazon Application Recovery Controller (ARC) using API operations. The examples are intended to help you develop a basic understanding of how to work with zonal autoshift using the CLI.

Zonal autoshift is a capability in ARC. With zonal autoshift, you authorize AWS to shift away supported application resource traffic from an Availability Zone during events, on your behalf, to help reduce your time to recovery. For more information about resources that you can use with zonal autoshift, see [Supported resources](#arc-zonal-shift.resource-types).

Zonal autoshift includes practice runs, which also shift traffic away from Availability Zones, to help verify that autoshifts are safe for your application.

For a list of zonal autoshift API actions and links to more information, see [Zonal autoshift API operations](#actions.zonalautoshift). For more information about using the AWS CLI, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/arc-zonal-shift/index.html). 

**Topics**
+ [Create a practice run configuration](#getting-started-cli-update-zonal_autoshift.create-practice-run)
+ [Enable or disable autoshifts](#getting-started-cli-zonal-autoshift.update-autoshift)
+ [Start an on-demand practice run](#getting-started-cli-zonal-autoshift.start-practice-run)
+ [Cancel an in-progress practice run](#getting-started-cli-zonal-autoshift.cancel-practice-run)
+ [Cancel an in-progress autoshift](#getting-started-cli-zonal-autoshift.cancel-autoshift)
+ [Edit a practice run configuration](#getting-started-cli-zonal_autoshift.edit-practice-run-config)
+ [Delete a practice run configuration](#getting-started-cli-zonal-autoshift.delete-practice-run-config)

#### Create a practice run configuration
<a name="getting-started-cli-update-zonal_autoshift.create-practice-run"></a>

Before you can enable zonal autoshift for a resource, you must create a practice run configuration for the resource, to choose options for the required practice runs. You create a practice run configuration for a resource with the CLI by using the `create-practice-run-configuration` command.

Note the following when you create a practice run configuration for a resource:
+ The only supported alarm type at this time is `CLOUDWATCH`.
+ You must use alarms that are in the same AWS Region that your resource is deployed in.
+ Specifying an outcome alarm is required. Specifying a blocking alarm is optional.
+ Specifying blocked or allowed dates or windows is optional.

You create a practice run configuration with the CLI by using the `create-practice-run-configuration` command.

For example, to create a practice run configuration for a resource, use a command like the following:

```
aws arc-zonal-shift create-practice-run-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}" \
      --outcome-alarms type=CLOUDWATCH,alarmIdentifier=arn:aws:cloudwatch:{{Region}}:{{111122223333}}:alarm:{{Region}}-{{MyAppHealthAlarm}} \
      --blocking-alarms type=CLOUDWATCH,alarmIdentifier=arn:aws:cloudwatch:{{Region}}:{{111122223333}}:alarm:{{Region}}-{{BlockWhenALARM}} \
      --blocked-dates 2023-12-01 --blocked-windows Mon:10:00-Mon:10:30
```

```
{
   "arn": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "name": "zonal-shift-elb"
   "zonalAutoshiftStatus": "DISABLED",
   "practiceRunConfiguration": {
       "blockingAlarms": [
                  {
               "type": "CLOUDWATCH",
               "alarmIdentifier": "arn:aws:cloudwatch:us-west-2:111122223333:alarm:us-west-2-BlockWhenALARM"
           }
       ]
       "outcomeAlarms": [
           {
               "type": "CLOUDWATCH",
               "alarmIdentifier": "arn:aws:cloudwatch:us-west-2:111122223333:alarm:us-west-2-MyAppHealthAlarm"
           }
       ],
       "blockedWindows": [
           "Mon:10:00-Mon:10:30"
       ],
       "blockedDates": [
           "2023-12-01"
       ]
}
```

#### Enable or disable autoshifts
<a name="getting-started-cli-zonal-autoshift.update-autoshift"></a>

You enable or disable autoshifts for a resource by updating the zonal autoshift status with the CLI. To change the zonal autoshift status, use the `update-zonal-autoshift-configuration` command.

For example, to enable autoshifts for a resource, use a command like the following:

```
aws arc-zonal-shift update-zonal-autoshift-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}" \
      --zonal-autoshift-status="ENABLED"
```

```
{
   "resourceIdentifier": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "zonalAutoshiftStatus": "ENABLED"
}
```

#### Start an on-demand practice run
<a name="getting-started-cli-zonal-autoshift.start-practice-run"></a>

You can start an on-demand practice run zonal shift with the CLI by using the `start-practice-run` command.

For example, to start a practice run for a resource, use a command like the following:

```
aws arc-zonal-shift start-practice-run 
    --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}" \
    "awayFrom": "usw2-az1",
```

```
{
    "awayFrom": "usw2-az1",
    "comment": "Practice run started. Shifting traffic away from Availability Zone usw2-az1.",
}
```

#### Cancel an in-progress practice run
<a name="getting-started-cli-zonal-autoshift.cancel-practice-run"></a>

You can cancel an in-progress practice run with the CLI by using the `cancel-practice-run` command.

For example, to cancel a practice run for a resource, use a command like the following:

```
aws arc-zonal-shift cancel-practice-run \
   --zonal-shift-id="="arn:aws:testservice::111122223333:ExampleALB123456890"
```

```
{
    "zonalShiftId": "2222222-3333-444-1111",
    "resourceIdentifier": "arn:aws:testservice::111122223333:ExampleALB123456890",
    "awayFrom": "usw2-az1",
    "expiryTime": 2024-11-15T10:35:42+00:00,
    "startTime": 2024-11-15T09:35:42+00:00,
    "status": "CANCELED",
    "comment": "Practice run canceled"
}
```

#### Cancel an in-progress autoshift
<a name="getting-started-cli-zonal-autoshift.cancel-autoshift"></a>

You can cancel an in-progress autoshift with the CLI by canceling the zonal autoshift for the resource. To cancel a zonal autoshift, use the `cancel-zonal-shift command`.

```
aws arc-zonal-shift cancel-zonal-shift --zonal-shift-id 9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38
```

```
{
    "awayFrom": "usw2-az1",
    "comment": "Zonal autoshift started. Shifting traffic away from Availability Zone usw2-az1.",
    "expiryTime": "2024-12-17T22:29:38-08:00",
    "resourceIdentifier": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/app/Testing/5a19403ecd42dc05",
    "startTime": "2024-12-17T21:27:26-08:00",
    "status": "CANCELED",
    "zonalShiftId": "9ac9ec1e-1df1-0755-3dc5-8cf573cd9c38"
}
```

#### Edit a practice run configuration
<a name="getting-started-cli-zonal_autoshift.edit-practice-run-config"></a>

You can edit a practice run configuration for a resource with the CLI to update different configuration options, such as changing the alarms for practice runs or updating the blocked dates or blocked windows, when ARC won't start practice runs. To edit a practice run configuration, use the `update-practice-run-configuration` command.

Note the following when you edit a practice run configuration for a resource:
+ The only supported alarm type at this time is `CLOUDWATCH`.
+ You must use alarms that are in the same AWS Region that your resource is deployed in.
+ Specifying an outcome alarm is required. Specifying a blocking alarm is optional.
+ Specifying blocked dates or blocked windows is optional.
+ The blocked dates or blocked windows that you specify replace any existing values.

For example, to edit a practice run configuration for a resource to specify a new blocked date, use a command like the following:

```
aws arc-zonal-shift update-practice-run-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}" \
      --blocked-dates 2024-03-01
```

```
{
   "arn": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "name": "zonal-shift-elb"
   "zonalAutoshiftStatus": "DISABLED",
   "practiceRunConfiguration": {
       "blockingAlarms": [
                  {
               "type": "CLOUDWATCH",
               "alarmIdentifier": "arn:aws:cloudwatch:us-west-2:111122223333:alarm:us-west-2-BlockWhenALARM"
           }
       ]
       "outcomeAlarms": [
           {
               "type": "CLOUDWATCH",
               "alarmIdentifier": "arn:aws:cloudwatch:us-west-2:111122223333:alarm:us-west-2-MyAppHealthAlarm"
           }
       ],
       "blockedWindows": [
           "Mon:10:00-Mon:10:30"
       ],
       "blockedDates": [
           "2024-03-01"
       ]
}
```

#### Delete a practice run configuration
<a name="getting-started-cli-zonal-autoshift.delete-practice-run-config"></a>

You can delete a practice run configuration for a resource, but you must first disable zonal autoshift for the resource. A resource is required to have a practice run configuration to have zonal autoshift enabled. Regular practice runs help you to make sure that your application can run normally without one Availability Zone. 

To delete a practice run configuration by using the CLI, first, disable zonal autoshift, if needed by using the `update-zonal-autoshift` command. Then, to delete the practice run configuration, use the `delete-practice-run-configuration` command.

First, disable zonal autoshift for the resource, using a command like the following:

```
aws arc-zonal-shift update-zonal-autoshift-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}" \
      --zonal-autoshift-status="DISABLED"
```

```
{
   "resourceIdentifier": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "zonalAutoshiftStatus": "DISABLED"
}
```

Then, delete the practice run configuration, using a command like the following:

```
aws arc-zonal-shift delete-practice-run-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}"
```

```
{
   "arn": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "name": "TestResource",
   "zonalAutoshiftStatus": "DISABLED"
}
```

### Enabling and working with zonal autoshift
<a name="arc-zonal-autoshift.start-cancel"></a>

This section provides procedures for working with zonal autoshifts in Amazon Application Recovery Controller (ARC). After you enable zonal autoshift, you can make changes to practice run configurations, start an on-demand practice run, cancel an in-progress shift, including practice runs, or enable autoshift observer notifications.

#### Enabling or disabling zonal autoshift
<a name="arc-zonal-autoshift.configure"></a>

The steps here explain how to enable or disable zonal autoshift on the Amazon Application Recovery Controller (ARC) console. To work with zonal autoshift programmatically, see the [ Zonal Shift and Zonal Autoshift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

When zonal autoshift is enabled, you authorize AWS to shift away application resource traffic from an Availability Zone during events, on your behalf, to help reduce your time to recovery.

#### To enable or disable zonal autoshift


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift). 

1. Under **Resource zonal autoshift configurations**, choose a resource.

1. In the **Actions** menu, choose **Enable zonal autoshift**, then follow the steps to complete the update.

If the resource doesn't have a practice run configuration, **Enable zonal autoshift** is not available. To configure a practice run configuration and enable zonal autoshift, choose ** Configure zonal autoshift**.

**Topics**
+ [Enabling or disabling zonal autoshift](#arc-zonal-autoshift.configure)
+ [Configuring, editing, or deleting a practice run configuration](#arc-zonal-autoshift.edit-delete-practice-run)
+ [Canceling a zonal autoshift](#arc-zonal-autoshift.canceling-an-autoshift)
+ [Starting a practice run zonal shift](#arc-zonal-autoshift.start-practice-run)
+ [Canceling a practice run zonal shift](#arc-zonal-autoshift.cancel-practice-run)
+ [Enabling or disabling autoshift observer notification](#arc-zonal-autoshift.enable-autoshift-observer)

#### Configuring, editing, or deleting a practice run configuration
<a name="arc-zonal-autoshift.edit-delete-practice-run"></a>

The steps in this section explain how to edit or delete a practice run configuration on the Amazon Application Recovery Controller (ARC) console. To work with zonal autoshift programmatically, including changes to practice run configurations, see the [Zonal Shift and Zonal Autoshift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

If you delete a practice run configuration in the console, zonal autoshift is disabled. Before you can delete a practice run configuration with an API operation, you must disable zonal autoshift. You can configure a practice run without enabling zonal autoshift. However, for zonal autoshift to be enabled for a resource, you are required to have a practice run configured for the resource.

#### To configure a practice run


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift). 

1. Choose **Configure zonal autoshift**.

1. Choose a resource to configure for zonal autoshift.

1. Choose to disable zonal autoshift if you don't want AWS to start an autoshift for a resource when there's an AWS event. You can continue with the wizard to configure a practice run configuration without enabling autoshifts, if you choose.

1. Choose options for practice runs for the resource. For alarms, you can do the following:
   + (Required) Specify at least one outcome alarm to monitor practice runs for this resource.
   + (Optional) Specify one or more blocking alarms for practice runs for this resource. 

   For more information, see the **Alarms that you specify for practice runs** section in [Best practices when you configure zonal autoshift](#arc-zonal-autoshift.considerations).

1. Optionally, specify blocked windows or allowed windows, to block ARC from starting practice runs or allow ARC to start practice runs for this resource. All dates and times are in UTC.

1. Select the check box to confirm that you have read the acknowledgement note.

1. Choose **Create**.

#### To edit a practice run configuration


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift). 

1. Under **Resource zonal autoshift configurations**, choose a resource.

1. In the **Actions** menu, choose **Edit practice run configuration**.

1. Make changes to the practice run configuration, to do one or more of the following:
   + For alarms, you can do the following:
     + For blocking alarms, you can add one or more alarms or delete alarms. 
     + For outcome alarms, you can add one or more alarms or delete alarms. At least one outcome alarm is required, so you can't delete all of the outcome alarms in a configuration.
   + For blocked windows and allowed windows, you can add new dates or days and times, or you can remove or update existing dates or days and times. All dates and times are in UTC.

1. Choose **Save**.

#### To delete a practice run configuration


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift). 

1. Under **Resource zonal autoshift configurations**, choose a resource.

1. In the **Actions** menu, choose **Delete practice run configuration**.

1. On the confirmation modal dialog, type `Delete`, and then choose **Delete**.

   Note that deleting a practice run configuration in the console also disables zonal autoshift for the resource. Zonal autoshift requires a practice run to be configured for the resource.

#### Canceling a zonal autoshift
<a name="arc-zonal-autoshift.canceling-an-autoshift"></a>

To stop an in-progress zonal autoshift for a resource, you must cancel the zonal autoshift.

#### To stop an in-progress zonal autoshift


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/](https://console.aws.amazon.com/route53recovery/zonalshift/home#/). 

1. Select a zonal autoshift that you want to cancel, and then choose **Cancel zonal shift**.

1. On the confirmation modal dialog, choose **Confirm**.

#### Starting a practice run zonal shift
<a name="arc-zonal-autoshift.start-practice-run"></a>

The steps in this section explain how to start an on-demand practice run zonal shift on the ARC console. To work with zonal shift and zonal autoshift programmatically, see the [ Zonal Shift and Zonal Autoshift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

You can start a practice run zonal shift after you configure zonal autoshift and create a practice run configuration.

#### To start a practice run zonal shift


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/](https://console.aws.amazon.com/route53recovery/zonalshift/home#/). 

1. Under **Zonal autoshift resources**, browse to an individual resource that has zonal autoshift configured.

1. On the **Resource overview** page, choose **Start practice run**.

1. Select an Availability Zone, and then enter a comment for your practice run. The practice run will shift traffic away from the Availability Zone that you selected.

1. Choose **Start**.

#### Canceling a practice run zonal shift
<a name="arc-zonal-autoshift.cancel-practice-run"></a>

The steps in this section explain how to cancel a zonal shift on the ARC console. To work with zonal shift and zonal autoshift programmatically, see the [ Zonal Shift and Zonal Autoshift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

You can cancel zonal shifts or practice runs that you initiate yourself. You can also cancel zonal shifts that AWS starts for a resource for a practice run for zonal autoshift.

#### To cancel a practice run zonal shift


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/](https://console.aws.amazon.com/route53recovery/zonalshift/home#/). 

1. Select a practice run zonal shift that you want to cancel, and then choose **Cancel zonal shift** or **Cancel practice run**.

1. On the confirmation modal dialog, choose **Confirm**.

#### Enabling or disabling autoshift observer notification
<a name="arc-zonal-autoshift.enable-autoshift-observer"></a>

You can configure zonal autoshift to notify you, through Amazon EventBridge, whenever AWS starts an autoshift to shift traffic away from a potentially impaired Availability Zone. You must configure this option in each AWS Region that you want to receive notifications about. You do not have to configure any specific resources with zonal autoshift to enable these separate notifications. For more information, see [Using zonal autoshift with Amazon EventBridge](#eventbridge-zonal-autoshift).

The steps in this section explain how to enable autoshift observer notification by using the Amazon Application Recovery Controller (ARC) console. To work with zonal autoshift programmatically, see the [ Zonal Shift and Zonal Autoshift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

#### To enable or disable autoshift observer notification


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/](https://console.aws.amazon.com/route53recovery/zonalshift/home#/). 

1. Under **Getting started**, choose **Enable autoshift observer notification**.

1. In the confirmation dialog box, choose **Enable observer notification**.

### Testing zonal autoshift with AWS FIS
<a name="testing-zonal-autoshift-fis"></a>

You can use AWS Fault Injection Service to set up and run experiments that help you simulate real-world conditions, such as the [AZ Availability: Power Interruption scenario](https://docs.aws.amazon.com/fis/latest/userguide/az-availability-scenario.html), that will demonstrate what happens when AWS starts a zonal autoshift on your autoshift-enabled resources during a potentially widespread AZ impairment.

The start `aws:arc:start-zonal-autoshift` recovery action allows you to demonstrate how AWS will automatically shifts traffic, for zonal autoshift enabled resources, away from a potentially impaired AZ and reroute them to healthy AZs in the same AWS Region during the execution of the AZ availability scenario.

For example, you can use the AWS FIS scenario library to simulate an AZ impairment that was caused by a power interruption. In this experiment, five minutes after the AZ power interruption begins, the recovery action `aws:arc:start-zonal-autoshift` automatically shifts resource traffic away from the specified AZ. The traffic is shifted for the remaining 25 minutes of the power interruption, to demonstrate how autoshift would be triggered when there is potentially widespread AZ impairment. When the experiment completes, the traffic shift ends and traffic begins flowing to all AZs again. This process demonstrates a complete recovery from a power event that impacts an AZ.

#### How experiments differ from zonal autoshift practice runs
<a name="zonal-shift-vs-practice"></a>

AWS FIS experiments differ from zonal autoshift practice runs in that, during practice runs, ARC shifts traffic for your resource away from one AZ as part of a normal process to ensure that your application can tolerate the loss of an AZ. However, during an AWS FIS experiment, AWS FIS demonstrates how an AZ impairment and an autoshift would be triggered for your autoshift-enabled resources on your behalf, and then cancels the autoshift when the impairment has been resolved. 

You cannot update an AWS FIS-initiated zonal shift while it is running. In addition, if you cancel a zonal shift outside of AWS FIS, the AWS FIS experiment ends. 

#### AWS FIS expiration-based safety mechanism
<a name="fis-safety-mechanism"></a>

AWS FIS manages the zonal shift using the [StartZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartZonalShift.html), [UpdateZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalShift.html), and [CancelZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelZonalShift.html) API operations, with the `expiresIn` field for these requests set to 1 minute as a safety mechanism. This enables AWS FIS to quickly roll back the zonal shift if there are unexpected events, such as network outages or system issues. In the ARC console, the expiration time field will display AWS FIS-managed, and the actual expected expiration is determined by the duration specified in the zonal shift action. For more information on practice runs, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html)

There can be no more than one applied zonal shift at a given time. That is, only one practice run zonal shift, customer-initiated zonal shift, autoshift, or AWS FIS experiment for the resource. When a second zonal shift is started, ARC follows a precedence to determine which zonal shift type is in effect for a resource. For more information on precedence for zonal shifts, see [Precedence for zonal shifts](#arc-zonal-autoshift.how-it-works.precedence).

For more information about AWS FIS recovery actions, refer to the [AWS FIS recovery action](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-recovery.html) in the *AWS Fault Injection Service User Guide*. 

### Logging and monitoring for zonal autoshift in Amazon Application Recovery Controller (ARC)
<a name="monitoring-zonal-autoshift"></a>

You can use AWS CloudTrail and Amazon EventBridge for monitoring zonal autoshift in Amazon Application Recovery Controller (ARC), to analyze patterns and help troubleshoot issues.

**Topics**
+ [Logging zonal autoshift API calls using AWS CloudTrail](#cloudtrail-zonal-autoshift)
+ [Using zonal autoshift with Amazon EventBridge](#eventbridge-zonal-autoshift)

#### Logging zonal autoshift API calls using AWS CloudTrail
<a name="cloudtrail-zonal-autoshift"></a>

Zonal autoshift for ARC is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in ARC. CloudTrail captures all API calls for zonal shift as events. The calls captured include calls from the ARC console and code calls to the ARC API operations for zonal shift. 

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for zonal shift. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**.

Using the information collected by CloudTrail, you can determine the request that was made to ARC for zonal shift, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

##### Zonal autoshift information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in ARC for zonal autoshift, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for zonal autoshift in ARC, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services, to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All ARC actions are logged by CloudTrail and are documented in the [Routing Control API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/routing-control/latest/APIReference/). For example, calls to the `StartZonalShift` and `ListManagedResources` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

##### Viewing ARC events in event history
<a name="amazon-arc-events-in-cloudtrail-event-history"></a>

CloudTrail lets you view recent events in **Event history**. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*.

##### Understanding zonal autoshift log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `ListManagedResources` action for zonal autoshift.

```
{
      "eventVersion": "1.08",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/admin",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "AROA33L3W36EXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/admin",
            "accountId": "111122223333",
            "userName": "EXAMPLENAME"
          },
          "webIdFederationData": {},
          "attributes": {
            "creationDate": "2022-11-14T16:01:51Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2022-11-14T16:14:41Z",
      "eventSource": "arc-zonal-shift.amazonaws.com",
      "eventName": "ListManagedResources",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.50",
      "userAgent": "Boto3/1.17.101 Python/3.8.10 Linux/4.14.231-180.360.amzn2.x86_64 exec-env/AWS_Lambda_python3.8 Botocore/1.20.102",      
      "requestParameters": null,
      "responseElements": null,
      "requestID": "VGXG4ZUE7UZTVCMTJGIAF_EXAMPLE",
      "eventID": "4b5c42df-1174-46c8-be99-d67_EXAMPLE",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333"
      "eventCategory": "Management"
      }
    }
```

#### Using zonal autoshift with Amazon EventBridge
<a name="eventbridge-zonal-autoshift"></a>

Using Amazon EventBridge, you can set up event-driven rules that monitor your zonal autoshift resources and initiate target actions that use other AWS services. For example, you can set a rule for sending out email notifications by signaling an Amazon SNS topic when a practice run starts for zonal autoshift.

You can create rules in Amazon EventBridge to act on zonal autoshift. An event for zonal autoshift specifies status information about practice runs or autoshifts, for example, when a practice run is started. You can configure zonal autoshift to notify you about zonal autoshift events for resources that you enable for the service.

You can also choose, in addition to or instead of other notifications, to enable autoshift observer notification, which provides a notification event whenever AWS starts an autoshift for a potentially impaired Availability Zone. Autoshift observer notification is separate from notifications that you receive when the traffic for resources that you have enabled for zonal autoshift is shifted away from an Availability Zone. You don't need to configure any resources with zonal autoshift to enable autoshift observer notification. For more information, see [Enabling and working with zonal autoshift](#arc-zonal-autoshift.start-cancel). 

To capture specific zonal autoshift events that you're interested in, define event-specific patterns that EventBridge can use to detect the events. Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for. 

Events are emitted on a best effort basis. They're delivered from ARC to EventBridge in near real-time, under normal operational circumstances. However, situations can arise that might delay or prevent delivery of an event.

For information about how EventBridge rules work with event patterns, see [Events and Event Patterns in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html). 

##### Monitor a zonal autoshift resource with EventBridge
<a name="arc-eventbridge-tasks-zonal-autoshift"></a>

With EventBridge, you can create rules that define actions to take when ARC emits events for its resources. For example, you can create a rule that sends an email message when a practice run starts for zonal autoshift. 

To type or copy and paste an event pattern into the EventBridge console, select to the option to use **Enter my own** option in the console. To help you determine event patterns that might be useful for you, this topic includes examples of both [zonal autoshift event-matching patterns ](#ZAEventBridgePatterns) and [zonal autoshift events](#ZAEventBridgeEventSamples) that you can use. 

**To create a rule for a resource event**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose the AWS Region that you want to create the rule in, that is the Region that you're interested in watching events for.

1. Choose **Create rule**.

1. Enter a **Name** for the rule, and, optionally, a description.

1. For **Event bus**, leave the default value, **default**.

1. Choose **Next**.

1. For the **Build event pattern** step, for **Event source**, leave the default value, **AWS events**.

1. Under **Sample event**, choose **Enter my own**.

1. For **Sample events**, type or copy and paste an event pattern.

##### Example zonal autoshift event patterns
<a name="arc-eventbridge-patterns-zonal-autoshift"></a>

Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for.

You can copy and paste event patterns from this section into EventBridge to create rules that you can use to monitor zonal autoshift actions and resources.

When you create event patterns for zonal autoshift events, you can specify any of the following for the `detail-type`:
+ `Autoshift In Progress`
+ `Autoshift Completed`
+ `Practice Run Started`
+ `Practice Run Succeeded`
+ `Practice Run Interrupted`
+ `Practice Run Failed`
+ `FIS Experiment Autoshift In Progress`
+ `FIS Experiment Autoshift Completed`
+ `FIS Experiment Autoshift Canceled`
+ `Manual Shift Started`
+ `Manual Shift Updated`
+ `Manual Shift Canceled`

When a practice run is interrupted, for more information about what caused the interruption, see the `additionalFailureInfo` field.

You can choose to monitor all AWS autoshifts by enabling *autoshift observer notifications*. After you enable autoshift observer notification, to receive the notifications, choose to be notified for the zonal autoshift detail type `Autoshift In Progress`. To see the steps for enabling autoshift observer notification, see [Enabling and working with zonal autoshift](#arc-zonal-autoshift.start-cancel).

For examples, see the [Example zonal autoshift events](#ZAEventBridgeEventSamples) section.
+ *Select all events from zonal autoshift where an autoshift has started.*

  Note the following:
  + If you have autoshift observer notification enabled, ARC returns all autoshift events. 
  + If you do not have autoshift observer notification enabled, ARC returns autoshift events only when a resource that you have configured for zonal autoshift is included in an autoshift.

  ```
  {
      "source": [
          "aws.arc-zonal-shift"
      ],
      "detail-type": [
          "Autoshift In Progress"
      ]
  }
  ```
+ *Select all events from zonal autoshift where a practice run has started*.

  ```
  {
      "source": [
          "aws.arc-zonal-shift"
      ],
      "detail-type": [
          "Practice Run Started"
      ]
  }
  ```
+ *Select all events from zonal autoshift where a practice run has failed*.

  ```
  {
      "source": [
          "aws.arc-zonal-shift"
      ],
      "detail-type": [
          "Practice Run Failed"
      ]
  }
  ```

##### Example zonal autoshift events
<a name="arc-eventbridge-examples-zonal-autoshift"></a>

This section includes example events for *zonal autoshift* actions.

The following is an example event for the `Autoshift In Progress` action, when 1) autoshift observer notification is *enabled* and 2) you have not configured a resource with zonal autoshift that is included in an autoshift:

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Autoshift In Progress",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":"AWS has started an autoshift for an impaired Availability Zone. This notification 
            is separate from autoshift notifications for resources, if any, that you have configured for 
            zonal autoshift. For details, see the Developer Guide."
        }
    }
}
```

The following is an example event for the `Autoshift In Progress` action, when 1) autoshift observer notification is *disabled* and 2) you have configured a resource with zonal autoshift that is included in an autoshift:

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Autoshift In Progress",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":""
        }
    }
}
```

The following is an example event for the `Practice Run Interrupted` action:

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Practice Run Interrupted",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": {
            "additionalFailureInfo": "Practice run interrupted. The blocking alarm entered ALARM state."
        },
        "metadata": {
            "awayFrom": "use1-az2"
        }
    }
}
```

The following is an example event for the `FIS Experiment Autoshift In Progress` action:

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "FIS Experiment Autoshift In Progress",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":""
        }
    }
}
```

The following is an example event for the `Manual Shift Started` action. It is emitted when the `StartZonalShift` API is called on a resource:

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Manual Shift Started",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":""
        }
    }
}
```

##### Specify a CloudWatch log group to use as a target
<a name="arc-eventbridge-cw-loggroup"></a>

When you create an EventBridge rule, you must specify the target where events that are matched to the rule are sent. For a list of available targets for EventBridge, see [Targets available in the EventBridge console](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html#eb-console-targets). One of the targets that you can add to an EventBridge rule is an Amazon CloudWatch log group. This section describes the requirements for adding CloudWatch log groups as targets, and provides a procedure for adding a log group when you create a rule.

To add a CloudWatch log group as a target, you can do one of the following:
+ Create a new log group 
+ Choose an existing log group

If you specify a new log group using the console when you create a rule, EventBridge automatically creates the log group for you. Make sure that the log group that you use as a target for the EventBridge rule starts with `/aws/events`. If you want to choose an existing log group, be aware that only log groups that start with `/aws/events` appear as options in the drop-down menu. For more information, see [Create a new log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group) in the *Amazon CloudWatch User Guide*.

If you create or use a CloudWatch log group to use as a target using CloudWatch operations outside of the console, make sure that you set permissions correctly. If you use the console to add a log group to an EventBridge rule, then the resource-based policy for the log group is updated automatically. But, if you use the AWS Command Line Interface or an AWS SDK to specify a log group, then you must update resource-based policy for the log group. The following example policy illustrates the permissions that you must define in a resource-based policy for the log group:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 

    "Statement": [
        {
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "events.amazonaws.com",
                    "delivery.logs.amazonaws.com"
                ]
            },
            "Resource": "arn:aws:logs:us-east-1:{{222222222222}}:log-group:/aws/events/*:*",
            "Sid": "TrustEventsToStoreLogEvent"
        }
    ]
}
```

------

You can't configure a resource-based policy for a log group by using the console. To add the required permissions to a resource-based policy, use the CloudWatch [PutResourcePolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html) API operation. Then, you can use the [ describe-resource-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-resource-policies.html) CLI command to check that your policy was applied correctly.

**To create a rule for a resource event and specify a CloudWatch log group target**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose the AWS Region that you want to create the rule in.

1. Choose **Create rule** and then enter any information about that rule, such as the event pattern or schedule details.

   For more information about creating EventBridge rules for ARC, see the sections earlier in this topic.

1. On the **Select target** page, choose **CloudWatch** as your target.

1. Choose a CloudWatch log group from the drop-down menu.

### Identity and Access Management for zonal autoshift in ARC
<a name="security-iam-zonalautoshift"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use ARC resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [How zonal autoshift works with IAM](#security_iam_service-with-iam-zonalautoshift)
+ [Identity-based policy examples](#security_iam_id-based-policy-examples-zonalautoshift)
+ [Service-linked role](#using-service-linked-roles-zonal-autoshift)
+ [AWS managed policies](#security-iam-awsmanpol-zonal-autoshift)

#### How zonal autoshift in ARC works with IAM
<a name="security_iam_service-with-iam-zonalautoshift"></a>

Before you use IAM to manage access to zonal autoshift in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with zonal autoshift.


**IAM features that you can use with zonal autoshift in ARC**  

| IAM feature | Zonal autoshift support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-zonalautoshift-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-zonalautoshift-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-zonalautoshift-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-zonalautoshift-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-zonalautoshift-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-zonalautoshift-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-zonalautoshift-tags) |  Partial | 
| [Temporary credentials](#security_iam_service-with-iam-zonalautoshift-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-zonalautoshift-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-zonalautoshift-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-zonalautoshift-roles-service-linked) |  Yes | 

To get a high-level, overall view of how AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Identity-based policies for ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To view examples of ARC identity-based policies, see [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](#security_iam_id-based-policy-examples).

##### Resource-based policies within ARC
<a name="security_iam_service-with-iam-zonalautoshift-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

##### Policy actions for ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of ARC actions for zonal autoshift, see [ Actions defined by Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in ARC for zonal autoshift use the following prefixes before the action:

```
arc-zonal-shift
```

To specify multiple actions in a single statement, separate them with commas. For example, the following:

```
"Action": [
      "arc-zonal-shift:{{action1}}",
      "arc-zonal-shift:{{action2}}"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "arc-zonal-shift:Describe*"
```

To view examples of ARC identity-based policies for zonal autoshift, see [Identity-based policy examples for zonal autoshift in ARC](#security_iam_id-based-policy-examples-zonalautoshift).

##### Policy resources for zonal autoshift in ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of resource types and their ARNs, and the actions that you can specify with the ARN of each resource, see the following topic in the *Service Authorization Reference*:
+ [ Actions defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions)

To see the actions and resources that you can use with a condition key, see the following topic in the *Service Authorization Reference*:
+ [ Condition keys defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-policy-keys)

To view examples of ARC identity-based policies for zonal autoshift, see [Identity-based policy examples for zonal autoshift in ARC](#security_iam_id-based-policy-examples-zonalautoshift).

##### Policy condition keys for zonal autoshift in ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of ARC condition keys for zonal autoshift, see the following topics in the *Service Authorization Reference*:
+ [ Condition keys for Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html#amazonroute53applicationrecoverycontroller-zonalshift-policy-keys)

To see the actions and resources that you can use with a condition key, see the following topics in the *Service Authorization Reference*:
+ [ Actions defined by Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions)

To view examples of ARC identity-based policies for zonal autoshift, see [Identity-based policy examples for zonal autoshift in ARC](#security_iam_id-based-policy-examples-zonalautoshift).

##### Access control lists (ACLs) in ARC
<a name="security_iam_service-with-iam-zonalautoshift-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

##### Attribute-based access control (ABAC) with ARC
<a name="security_iam_service-with-iam-zonalautoshift-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

Zonal autoshift in ARC includes the following partial support for ABAC: 
+ Zonal autoshift supports ABAC for managed resources that are registered in ARC for zonal shift. For more information about ABAC for Network Load Balancer and Application Load Balancer managed resources, see [ ABAC with Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags) in the Elastic Load Balancing User Guide.

##### Using temporary credentials with ARC
<a name="security_iam_service-with-iam-zonalautoshift-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Cross-service principal permissions for ARC
<a name="security_iam_service-with-iam-zonalautoshift-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

When you use an IAM entity (user or role) to perform actions in AWS, you are considered a principal. Policies grant permissions to a principal. When you use some services, you might perform an action that then triggers another action in a different service. In this case, you must have permissions to perform both actions.

To see whether an action requires additional dependent actions in a policy, see the following topic in the *Service Authorization Reference*:
+ [ Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html)

##### Service roles for ARC
<a name="security_iam_service-with-iam-zonalautoshift-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

##### Service-linked roles for ARC
<a name="security_iam_service-with-iam-zonalautoshift-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing ARC service-linked roles, see [Using the service-linked role for zonal autoshift in ARC](#using-service-linked-roles-zonal-autoshift).

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.

#### Identity-based policy examples for zonal autoshift in ARC
<a name="security_iam_id-based-policy-examples-zonalautoshift"></a>

By default, users and roles don't have permission to create or modify ARC resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by ARC, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices-zonal)
+ [Example: Zonal autoshift console access](#security_iam_id-based-policy-examples-console-zonalautoshift)
+ [Examples: ARC API actions](#security_iam_id-based-policy-examples-api-zonalautoshift)

##### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices-zonal"></a>

Identity-based policies determine whether someone can create, access, or delete ARC resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

##### Example: Zonal autoshift console access
<a name="security_iam_id-based-policy-examples-console-zonalautoshift"></a>

To access the Amazon Application Recovery Controller (ARC) console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the ARC resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To perform some tasks, users must have permission to create the service-linked role that is associated with zonal autoshift in ARC. To learn more, see [Using the service-linked role for zonal autoshift in ARC](#using-service-linked-roles-zonal-autoshift).

To give users full access to use zonal autoshift in the AWS Management Console, attach a policy like the following to the user:

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
                   "arc-zonal-shift:ListManagedResources",
                   "arc-zonal-shift:GetManagedResource",
                   "arc-zonal-shift:ListZonalShifts",
                   "arc-zonal-shift:StartZonalShift",
                   "arc-zonal-shift:UpdateZonalShift",
                   "arc-zonal-shift:CancelZonalShift",
                   "arc-zonal-shift:CreatePracticeRunConfiguration",
                   "arc-zonal-shift:DeletePracticeRunConfiguration",
                   "arc-zonal-shift:ListAutoshifts",
                   "arc-zonal-shift:UpdatePracticeRunConfiguration",
                   "arc-zonal-shift:UpdateZonalAutoshiftConfiguration"
             ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeAvailabilityZones",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "cloudwatch:DescribeAlarms",
            "Resource": "*"
        }
    ]
}
```

------

##### Examples: ARC API actions
<a name="security_iam_id-based-policy-examples-api-zonalautoshift"></a>

You can use a policy to ensure that a user can use ARC API actions for zonal autoshift to configure zonal autoshift so that AWS shifts away application resource traffic from an Availability Zone, on your behalf, to healthy AZs in the AWS Region, to help reduce your time to recovery during events. To provide these permissions, attach a policy that corresponds to the API operations that the user needs to work with, as described below.

To perform some tasks, users must have permissions for the service-linked role that is associated with ARC. Permissions needed to create the service-linked role are included in the following example policy. To learn more, see [Using the service-linked role for zonal autoshift in ARC](#using-service-linked-roles-zonal-autoshift).

To work with API operations for zonal autoshift, attach a policy such as the following to the user:

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
                   "arc-zonal-shift:ListManagedResources",
                   "arc-zonal-shift:GetManagedResource",
                   "arc-zonal-shift:ListZonalShifts",
                   "arc-zonal-shift:StartZonalShift",
                   "arc-zonal-shift:UpdateZonalShift",
                   "arc-zonal-shift:CancelZonalShift",
                   "arc-zonal-shift:CreatePracticeRunConfiguration",
                   "arc-zonal-shift:DeletePracticeRunConfiguration",
                   "arc-zonal-shift:ListAutoshifts",
                   "arc-zonal-shift:UpdatePracticeRunConfiguration",
                   "arc-zonal-shift:UpdateZonalAutoshiftConfiguration"
             ],
            "Resource": "*"
        },
        {
            "Effect" : "Allow",
            "Action" : [
                    "cloudwatch:DescribeAlarms",
                    "health:DescribeEvents"
            ],
            "Resource" : "*"
        },
        {
            "Effect" : "Allow",
            "Action" : [
                    "arc-zonal-shift:CancelZonalShift",
                    "arc-zonal-shift:GetManagedResource",
                    "arc-zonal-shift:StartZonalShift",
                    "arc-zonal-shift:UpdateZonalShift"
            ],
            "Resource" : "*"
        }
    ]
}
```

------

#### Using the service-linked role for zonal autoshift in ARC
<a name="using-service-linked-roles-zonal-autoshift"></a>

Zonal autoshift in Amazon Application Recovery Controller uses a AWS Identity and Access Management (IAM)[ service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to a service— in this case, ARC. The service-linked role is predefined by ARC and includes all the permissions that the service requires to call other AWS services on your behalf for specific purposes. 

A service-linked role makes setting up ARC easier because you don’t have to manually add the necessary permissions. ARC defines the permissions for the service-linked role, and unless defined otherwise, only ARC can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your ARC zonal autoshift resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-linked role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

##### Service-linked role permissions for AWSServiceRoleForZonalAutoshiftPracticeRun
<a name="slr-permissions-slr2"></a>

ARC uses the service-linked role named **AWSServiceRoleForZonalAutoshiftPracticeRun** to do the following:
+ Monitor customer-provided Amazon CloudWatch alarms and customer Health Dashboard events for practice runs
+ Manage practice runs (practice zonal shifts)

This section describes the permissions for the service-linked role, and information about creating, editing, and deleting the role.

###### Service-linked role permissions for AWSServiceRoleForZonalAutoshiftPracticeRun
<a name="slr-permissions-slr2-permissions"></a>

This service-linked role uses the managed policy `AWSZonalAutoshiftPracticeRunSLRPolicy`. 

The **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role trusts the following service to assume the role:
+ `practice-run.arc-zonal-shift.amazonaws.com`

To view the permissions for this policy, see [AWSZonalAutoshiftPracticeRunSLRPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSZonalAutoshiftPracticeRunSLRPolicy.html) in the *AWS Managed Policy Reference*.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

###### Creating the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role for ARC
<a name="create-slr2"></a>

You don't need to manually create the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role. When you create the first practice run configuration in the AWS Management Console, the AWS CLI, or an AWS SDK, ARC creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create the first practice run configuration, ARC creates the service-linked role for you again. 

###### Editing the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role for ARC
<a name="edit-slr"></a>

ARC does not allow you to edit the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role. After you create the service-linked role, you cannot change the name of the role because other entities might reference it. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

###### Deleting the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role for ARC
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for a service-linked role before you can manually delete it.

After you have disabled autoshift, then you can delete the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role. For more information about the autoshift capability, see [Zonal shift in ARC](#arc-zonal-shift). 

**Note**  
If the ARC service is using the role when you try to delete the resources, then the service role deletion might fail. If that happens, wait for a few minutes and try the again to delete the role.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForZonalAutoshiftPracticeRun service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

##### Updates to the ARC service-linked role for zonal autoshift
<a name="security-iam-awsmanpol-zonal-autoshift-updates"></a>

For updates to the AWS managed policies for the ARC service-linked roles, see the [AWS managed policies updates table](#security-iam-awsmanpol-arc-updates) for ARC. You can also subscribe to automatic RSS alerts on the ARC [Document history page](#doc-history).

#### AWS managed policies for zonal autoshift in ARC
<a name="security-iam-awsmanpol-zonal-autoshift"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

##### AWS managed policy: AWSZonalAutoshiftPracticeRunSLRPolicy
<a name="security-iam-awsmanpol-AWSZonalAutoshiftPracticeRunSLRPolicy"></a>

You can't attach `AWSZonalAutoshiftPracticeRunSLRPolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon Application Recovery Controller (ARC) to do the following for zonal autoshift:
+ Monitor customer-provided Amazon CloudWatch alarms and customer Health Dashboard events for practice runs
+ Manage practice runs (practice zonal shifts)
+ Manage balanced capacity checks for practice runs and autoshifts

For more information, see [Using the service-linked role for zonal autoshift in ARC](#using-service-linked-roles-zonal-autoshift).

##### Updates for AWS managed policies for zonal autoshift
<a name="security-iam-awsmanpol-zonal-autoshift-updates"></a>

For details about updates to AWS managed policies for zonal autoshift in ARC since this service began tracking these changes, see [Updates to AWS managed policies for Amazon Application Recovery Controller (ARC)](#security-iam-awsmanpol-arc-updates). For automatic alerts about changes to this page, subscribe to the RSS feed on the ARC [Document history page](#doc-history).

### Quotas for zonal autoshift
<a name="quotas.zonal-autoshift"></a>

Zonal autoshift in Amazon Application Recovery Controller (ARC) is subject to the following quotas.


| Entity | Quota | 
| --- | --- | 
| Number of outcome alarms per practice run configuration | 10<br />You can [ request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/arc-region-switch/quotas). | 
| Number of blocking alarms per practice run configuration | 10<br />You can [ request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/arc-region-switch/quotas). | 

# Use routing control to recover multi-Region applications in ARC
<a name="multi-region"></a>

This section explains how to use the routing control capability in Amazon Application Recovery Controller (ARC) to minimize disruption and help provide continuity for your users when you have an AWS application deployed in multiple AWS Regions. 

You can also learn about readiness check, a capability in ARC that you can use to gain insights into whether your applications and resources are prepared for recovery.

The topics in this section describe the routing control and readiness check capabilities, how to set them up, and how to use them.

**Topics**
+ [Routing control in ARC](#routing-control)
+ [Readiness check in ARC](#recovery-readiness)
+ [Region switch in ARC](#region-switch)

## Routing control in ARC
<a name="routing-control"></a>

To fail over traffic to application replicas in multiple AWS Regions, you can use routing controls in Amazon Application Recovery Controller (ARC) that are integrated with a specific kind of health check in Amazon Route 53. *Routing controls* are simple on-off switches that enable you to switch your client traffic from one Regional replica to another. The traffic rerouting is accomplished by *routing control health checks* that are set up with Amazon Route 53 DNS records. For example, DNS failover records, associated with domain names that front your application replicas in each Region. 

This section explains how routing control works, how to set up routing control components, and how to use them to reroute traffic for failover.

The routing control components in ARC are: clusters, control panels, routing controls, and routing control health checks. All routing controls are grouped on control panels. You can group them on the default control panel that ARC creates for your cluster, or create your own custom control panels. You must create a cluster before you can create a control panel or a routing control. Each cluster in ARC is a data plane of endpoints in five AWS Regions.

After you create routing controls and routing control health checks, you can create safety rules for routing control to help prevent unintentional recovery automation side effects. You can update routing control states to reroute traffic, individually or in batches, by using the AWS CLI or API actions (recommended), or by using the AWS Management Console.

This section explains how routing controls work, and how to create and use them to reroute traffic for your application.

**Important**  
To learn about preparing to use ARC to reroute traffic as part of a failover plan for your application in a disaster scenario, see [Best practices for routing control in ARC](#route53-arc-best-practices.regional).

### About routing control
<a name="routing-control.about"></a>

Routing control redirects traffic by using health checks in Amazon Route 53 that are configured with DNS records associated with the top-level resource of the cells in your recovery group, such as an Elastic Load Balancing load balancer. You can redirect traffic from one cell to another, for example, by updating a routing control state to `Off` (to stop traffic flow to one cell) and updating another routing control state to `On` (to start traffic flow to another). The process that changes the traffic flow is the Route 53 health check associated with the routing control, after ARC updates it to set it as healthy or unhealthy, based on the corresponding routing control state. 

Routing controls support failover across any AWS service that has a DNS endpoint. You can update routing control states to fail over traffic for disaster recovery, or when you detect latency drops for your application, or other issues. 

You can also configure safety rules for routing control, to make sure that rerouting traffic by using routing controls doesn't impair availability. For more information, see [Creating safety rules for routing control](#routing-control.safety-rules).

It's important to note that routing controls are not themselves health checks that monitor the underlying health of endpoints. For example, unlike a Route 53 health check, a routing control doesn't monitor response times or TCP connection times. A routing control is a simple on-off switch that controls a health check. Typically, you change the state to redirect traffic, and that state change moves the traffic to go to a particular endpoint for an entire application stack, or prevents routing to the whole application stack. For example, in a simple scenario, when you change a routing control state from `On` to `Off`, it updates a Route 53 health check, which you've associated with a DNS failover record to move the traffic off of an endpoint.

#### How to use routing control
<a name="routing-control.about-how-to"></a>

To update a routing control state, so that you can reroute traffic, you must connect to one of your cluster endpoints in ARC. If the endpoint that you try to connect to is unavailable, try changing the state with another cluster endpoint. Your process for changing routing control states should be prepared to try each endpoint in rotation, since cluster endpoints are cycled through available and unavailable states for regular maintenance and updates.

When you create routing controls, you configure your DNS records to associate routing control health checks with Route 53 DNS names that front each application replica. For example, to control traffic failovers across two load balancers, one in each of two Regions, you create two routing control health checks and associate them with two DNS records, for example, Alias records with failover routing policies, with the domain names of the respective load balancers.

You can also set up more complex traffic failover scenarios by using ARC routing control together with Route 53 health checks and DNS record sets, using DNS records with weighted routing policies. To see a detailed example, see the section on failing over user traffic in the following AWS blog post: [ Building highly resilient applications using Amazon Application Recovery Controller (ARC), Part 2: Multi-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-2-multi-region-stack/)

When you start a failover for an AWS Region using routing control, because of the steps involved with traffic flow, you might not see traffic move out of the Region immediately. It also can take a short time for existing, in-progress connections in the Region to complete, depending on client behavior and connection reuse. Depending on your DNS settings and other factors, existing connections can complete in just a few minutes, or might take longer. For more information, see [Ensuring that traffic shifts finish quickly](#arc-zonal-shift.existing-connections).

#### Benefits of routing control
<a name="routing-control.about-benefits"></a>

A routing control in ARC has several benefits over rerouting traffic with traditional health checks. For example:
+ A routing control gives you a way to fail over an entire application stack. This is in contrast to failing over individual components of a stack, as Amazon EC2 instances do, based on resource-level health checks.
+ A routing control gives you a safe, simple manual override that you can use to shift traffic to do maintenance or to recover from failures when internal monitors don't detect an issue. 
+ You can use a routing control together with safety rules to prevent common side effects that can happen with fully automated health check-based automation, such as failing over to standby infrastructure that isn't prepared for failover.

Here's an example of incorporating routing controls into your failover strategy, to improve the resilience and availability of your applications in AWS.

You can support highly available AWS applications on AWS by running multiple (typically three) redundant replicas across Regions. Then you can use Amazon Route 53 routing control to route traffic to the appropriate replica. 

For example, you can set up one application replica to be active and serve application traffic, while another is a standby replica. When your active replica has failures, you can reroute user traffic there to restore availability to your application. You should decide whether to fail away from or to a replica based on information from your monitoring and health check systems. 

If you want to enable faster recoveries, another option that you can choose for your architecture is an active-active implementation. With this approach, your replicas are active at the same time. This means that you can recover from failures by moving users away from an impaired application replica by just rerouting traffic to another active replica.

### AWS Region availability for routing control
<a name="introduction-regions-routing"></a>

For detailed information about Regional support and service endpoints for Amazon Application Recovery Controller (ARC), see [Amazon Application Recovery Controller (ARC) endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/r53arc.html) in the *Amazon Web Services General Reference*.

**Note**  
Routing control in Amazon Application Recovery Controller (ARC) is a global feature. However, you must specify the US West (Oregon) Region (specify the parameter `--region us-west-2`) in Regional ARC AWS CLI commands. That is, when you create resources such as clusters, control panels, or routing controls.

A ARC routing control is an on/off switch that changes the state of a ARC health check, which can then be associated with a DNS record that redirects traffic, for example, from a primary to a standby deployment replica.

If there's an application failure or latency issue, you can update routing control states to shift traffic from your primary replica to, for example, a standby replica. By using the highly reliable ARC data plane API operations to make routing control queries and routing control state updates, you can rely on ARC for failover during disaster recovery scenarios. For more information, see [Getting and updating routing control states using the ARC API (recommended)](#routing-control.update.api).

ARC maintains routing control states in a *cluster*, which is a set of five redundant Regional endpoints. ARC propagates routing control state changes across the cluster, which is located in an Amazon EC2 fleet, to get a quorum across five AWS Regions. After propagation, when you query ARC for a routing control state, using the API and the highly-reliable data plane, it returns the consensus view. 

You can interact with any one of the five cluster endpoints to update the state of a routing control from, for example, `Off` to `On`. Then ARC propagates the update across the five Regions of the cluster. 

Data consistency across all five cluster endpoints is achieved within 5 seconds on average, and after no more than 15 seconds maximum.

ARC offers extreme reliability with its data plane for you to manually fail over your application across cells. ARC ensures that at least three out of the five cluster endpoints are always accessible to you to perform routing control state changes. Note that each ARC cluster is single-tenant, to ensure that you're not affected by "noisy neighbors" that might slow down your access patterns.

When you make changes to routing control states, you rely on the following three criteria, which are highly unlikely to fail:
+ At least three of your five endpoints are available and take part in the quorum.
+ You have working IAM credentials and can authenticate against a working Regional cluster endpoint.
+ The Route 53 data plane is healthy (this data plane is designed to meet a 100% availability SLA).

### Routing control components
<a name="introduction-components-routing"></a>

The following diagram illustrates an example of components that support the routing control feature in ARC. The routing controls shown here (grouped into one control panel) let you manage traffic to two Availability Zones in each of two Regions. When you update routing control states, ARC changes health checks in Amazon Route 53, which redirect DNS traffic to different cells. Safety rules that you configure for routing controls help avoid fail-open scenarios and other unintentional consequences.

![Components that support routing control in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/images/GS_RecoveryControlDiagram.png)


The following are components of the routing control feature in ARC.

**Cluster**  
A cluster is a set of five redundant Regional endpoints against which you initiate API calls to update or get routing control states. A cluster includes a default control panel, and you can host multiple control panels and routing controls on one cluster.

**Routing controls**  
A routing control is a simple on/off switch, hosted on a cluster, that you use to control routing of client traffic in and out of cells. When you create a routing control, you add a ARC health check in Route 53. This enables you to reroute traffic (using the health checks, configured with DNS records for your applications) when you update the routing control state in ARC. 

**Routing control health check**  
Routing controls are integrated with health checks in Route 53. The health checks are associated with DNS records that front each application replica, for example, failover records. When you change routing control states, ARC updates the corresponding health checks, which redirect traffic—for example, to failover to your standby replica. 

**Control panel**  
A control panel groups together a set of related routing controls. You can associate multiple routing controls with one control panel, and then create safety rules for the control panel to ensure that the traffic redirection updates that you make are safe. For example, you can configure a routing control for each of your load balancers in each Availability Zone, and then group them in the same control panel. Then you can add a safety rule (an "assertion rule") that makes sure that at least one zone (represented by a routing control) is active at any one time, to avoid unintended "fail-open" scenarios.

**Default control panel**  
When you create a cluster, ARC creates a default control panel. By default, all routing controls that you create on the cluster are added to the default control panel. Or, you can create your own control panels to group related routing controls.

**Safety rule**  
Safety rules are rules that you add to routing control to ensure that recovery actions don't accidentally impair your application's availability. For example, you can create a safety rule that creates a routing control that acts as an overall "on/off" switch so that you can enable or disable a set of other routing controls. 

****Endpoint (cluster endpoint)****  
Each cluster in ARC has five Regional endpoints that you can use for setting and retrieving routing control states. Your process for accessing the endpoints should assume that ARC regularly brings the endpoints up and down for maintenance, so you should try each endpoint in succession until you connect to one. You access the endpoints to get the current state of routing controls (On or Off) and to trigger failovers for your applications by changing routing control states.

### Data and control planes for routing control
<a name="data-and-control-planes"></a>

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that you make sure that the mechanisms that you depend on during failover are highly available, so that you can use them when you need them in a disaster scenario. Typically, you should use data plane functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind, it's important to understand how the functionality of a service is divided between control planes and data planes, and when you can rely on an expectation of extreme reliability with a service's data plane.

As with most AWS services, the functionality for the routing control capability is supported by control planes and data planes. While both of these are built to be reliable, a control plane is optimized for data consistency, while a data plane is optimized for availability. A data plane is designed for resilience so that it can maintain availability even during disruptive events, when a control plane might become unavailable.

In general, a *control plane* enables you to do basic management functions, such as create, update, and delete resources in the service. A *data plane* provides a service's core functionality. Because of this, we recommend that you use data plane operations when availability is important, for example, when you need to reroute traffic to a standby replica during an outage.

For routing control, the control planes and data planes are divided as follows:
+ The control plane API for routing control is the [Recovery Control Configuration API](https://docs.aws.amazon.com/recovery-cluster/latest/api/what-is-recovery-control.html), supported in the US West (Oregon) Region (us-west-2). You use these API operations or the AWS Management Console to create or delete clusters, control panels, and routing controls, to help prepare for a disaster recovery event when you might need to reroute traffic for your application. *The routing control configuration control plane is not highly available.*
+ The routing control data plane is a dedicated cluster across five geographically-isolated AWS Regions. Each customer creates one or more clusters using the routing control control plane. The cluster hosts control panels and routing controls. Then you use the [Routing Control (Recovery Cluster) API](https://docs.aws.amazon.com/routing-control/latest/APIReference/Welcome.html) to get, list, and update routing control states when you want to reroute traffic for your application. *The routing control data plane IS highly available.*

Because the routing control data plane is highly available, we recommend that you plan to use the AWS Command Line Interface to make API calls to work with routing control states when you want to fail over to recover from an event. For more information about key considerations when you prepare for and complete a recovery operation with routing control, see [Best practices for routing control in ARC](#route53-arc-best-practices.regional).

For more information about data planes, control planes, and how AWS builds services to meet high availability targets, see the [Static stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) in the Amazon Builders' Library.

### Tagging for routing control in Amazon Application Recovery Controller (ARC)
<a name="introduction-tagging-routing-control"></a>

Tags are words or phrases (meta data) that you use to identify and organize your AWS resources. You can add multiple tags to each resource, and each tag includes a key and a value that you define. For example, the key might be environment and the value might be production. You can search and filter your resources based on the tags you add.

You can tag the following resources in routing control in ARC:
+ Clusters
+ Control panels
+ Safety rules

Tagging in ARC is available only through the API, for example, by using the AWS CLI. 

The following are examples of tagging in routing control by using the AWS CLI.

`aws route53-recovery-control-config --region us-west-2 create-cluster --cluster-name example1-cluster --tags Region=PDX,Stage=Prod`

`aws route53-recovery-control-config --region us-west-2 create-control-panel --control-panel-name example1-control-panel --cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh --tags Region=PDX,Stage=Prod`

For more information, see [TagResource](https://docs.aws.amazon.com/recovery-cluster/latest/api/tags-resourcearn.html) in the *Recovery Control Configuration API Reference Guide* for Amazon Application Recovery Controller (ARC).

### Pricing for routing control in ARC
<a name="introduction-pricing-routing-control"></a>

For routing control in ARC, you pay an hourly cost per cluster that you create. Each cluster can host multiple routing controls, which you use to trigger application failovers.

To help manage costs and improve efficiency, you can set up cross-account sharing for a cluster, to share one cluster with multiple AWS accounts. For more information, see [Support cross-account for clusters in ARC](#routing-control.failover-different-accounts).

For detailed pricing information for ARC and pricing examples, see [ARC Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

### Getting started with multi-Region recovery in Amazon Application Recovery Controller (ARC)
<a name="getting-started"></a>

To fail over your applications by using routing control in Amazon Application Recovery Controller (ARC), you must have AWS applications that are in multiple AWS Regions. To get started, first, make sure that your applications are set up in siloed replicas in each Region, so that you can fail over from one to another during an event. Then, you can create routing controls to reroute the application traffic to fail over from a primary application to a secondary, maintaining continuity for your users.

**Note**  
If you have an application that is siloed by Availability Zones, consider using zonal shift or zonal autoshift for failover recovery. No setup is required to use zonal shift or zonal autoshift to reliably recover applications from Availability Zone impairments. For more information, see [Use zonal shift and zonal autoshift to recover applications in ARC](#multi-az).

So that you can use ARC routing control to recover applications during an event, we recommend that you set up at least two applications that are replicas of each other. Each replica, or *cell*, represents an AWS Region. After you've set up your application resources to align with Regions, make sure that your application set up for successful recovery by taking the following steps.

Tip: To help simplify setup, we provide CloudFormation and HashiCorp Terraform templates that create an application with redundant replicas that fail independently of one another. To learn more and download the templates, see [Setting up an example app](#getting-started-example).

To prepare to use routing control, make sure that your application is set up to be resilient by doing the following:

1. Build independent copies of your application stack (networking and compute layer) that are replicas of each other in each Region so that you can fail over traffic from one to the other when there's an event. Make sure that you don't have any cross-Region dependencies in your application code that would cause the failure of one replica to impact the other. To successfully fail over between AWS Regions, your stack boundaries should be within a Region. 

1. Duplicate all the required stateful data for your application across the replicas. You can use AWS database services to help replicate your data. 

#### Get started with routing control for traffic failover
<a name="getting-started-routing-controls"></a>

Routing control in Amazon Application Recovery Controller (ARC) enables you to trigger failover for your traffic to fail over between redundant application copies, or replicas, that are running in separate AWS Regions. Failover is performed with DNS, using the Amazon Route 53 data plane.

After you set up your replicas in each Region, as described in the next section, you can associate each one with a routing control. First, you associate routing controls with the top-level domain names of your replicas in each Region. Then, you add a routing control health check to the routing control so that it can turn traffic flow on and off. This enables you to control traffic routing across replicas of your application. 

You can update routing control states in the AWS Management Console to fail over traffic, but we recommend that instead you use ARC actions, using the API or AWS CLI, to change them. API actions aren't dependent on the console, so they're more resilient.

For example, to fail over between Regions, from us-west-1 to us-east-1, you can use the `update-routing-control-state` API action to set the state of `us-west-1` to `Off` and `us-east-1` to `On`.

Before you create routing control components to set up failover for your application, make sure that your application is siloed into Regional replicas, so that you can fail over from one to the other. To learn more and get started siloing a new application or creating a example stack, see the next sections.

#### Setting up an example app
<a name="getting-started-example"></a>

To help you understand how routing control works, we provide an example application called `TicTacToe`. The example uses CloudFormation templates to simplify the process, as well as a downloadable CloudFormation template so that you can quickly explore setting up and using ARC yourself.

After you deploy the sample app, you can use the templates to create ARC components, and then explore using routing controls to manage traffic flow to the app. You can adapt the template and process for your own scenario and applications.

To get started with a sample application and CloudFormation templates, see the README instructions in the [ARC GitHub repo](https://github.com/aws-samples/r53-arc-iad). You can learn more about using CloudFormation templates by reading [CloudFormation concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) in the AWS CloudFormation User Guide.

### Best practices for routing control in ARC
<a name="route53-arc-best-practices.regional"></a>

We recommend the following best practices for recovery and failover preparedness for routing control in ARC.

**Topics**
+ [Keep purpose-built, long-lived AWS credentials secure and always accessible](#RCBestPracticeCredentials)
+ [Choose lower TTL values for DNS records involved in failover](#RCBestPracticeLowerTTL)
+ [Limit the time that clients stay connected to your endpoints](#RCBestPracticeCurrentConnections)
+ [Bookmark or hard code your five Regional cluster endpoints and routing control ARNs](#RCBestPracticeBookmarkEndpoints)
+ [Choose one of your endpoints at random to update your routing control states](#RCBestPracticeRandomEndpoint)
+ [Use the extremely reliable data plane API to list and update routing control states, not the console](#RCBestPracticeUseDataPlane)

**Keep purpose-built, long-lived AWS credentials secure and always accessible**  
In a disaster recovery (DR) scenario, keep system dependencies to a minimum by using a simple approach to accessing AWS and performing recovery tasks. Create [ IAM long-lived credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html) specifically for DR tasks, and keep the credentials securely in an on-premises physical safe or a virtual vault, to access when needed. With IAM, you can centrally manage security credentials, such as access keys, and permissions for access to AWS resources. For non-DR tasks, we recommend that you continue to use federated access, using AWS services such as [AWS Single Sign-On](https://aws.amazon.com/single-sign-on/).  
To perform failover tasks in ARC with the recovery cluster data plane API, you can attach a ARC IAM policy to your user. To learn more, see [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](#security_iam_id-based-policy-examples).

**Choose lower TTL values for DNS records involved in failover**  
For DNS records that you might need to change as part of your failover mechanism, especially records that are health checked, using lower TTL values is appropriate. Setting a TTL of 60 or 120 seconds is a common choice for this scenario.  
The DNS TTL (time to live) setting tells DNS resolvers how long to cache a record before requesting a new one. When you choose a TTL, you make a trade-off between latency and reliability, and responsiveness to change. With a shorter TTL on a record, DNS resolvers notice updates to the record more quickly because the TTL specifies that they must query more frequently.  
For more information, see *Choosing TTL values for DNS records* in [Best practices for Amazon Route 53 DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-dns.html). 

**Limit the time that clients stay connected to your endpoints**  
When you use routing controls to shift from one AWS Region to another, the mechanism that Amazon Application Recovery Controller (ARC) uses to move your application traffic is a DNS update. This update causes all new connections to be directed away from the impaired location.  
However, clients with pre-existing open connections might continue to make requests against the impaired location until the clients reconnect. To ensure a quick recovery, we recommend that you limit the amount of time clients stay connected to your endpoints.   
If you use an Application Load Balancer, you can use the `keepalive` option to configure how long connections continue. For more information, see [ HTTP client keepalive duration](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#http-client-keep-alive-duration) in the Application Load Balancer User Guide.  
By default, Application Load Balancers set the HTTP client keepalive duration value to 3600 seconds, or 1 hour. We suggest that you lower the value to be inline with your recovery time goal for your application, for example, 300 seconds. When you choose an HTTP client keepalive duration time, consider that this value is a trade off between reconnecting more frequently in general, which can affect latency, and more quickly moving all clients away from an impaired AZ or Region.

**Bookmark or hard code your five Regional cluster endpoints and routing control ARNs**  
We recommend that you keep a local copy of your ARC Regional cluster endpoints, in bookmarks or saved in automation code that you use to retry your endpoints. During a failure event, you might not be able to access some API operations, including ARC API operations that are not hosted on the extremely reliable data plane cluster. You can list the endpoints for your ARC clusters by using the [DescribeCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html) API operation. 

**Choose one of your endpoints at random to update your routing control states**  
Routing controls provide five Regional endpoints to ensure high availability, even when dealing with failures. To achieve their full resilience, it's important to have retry logic that can use all five endpoints as necessary. For information about using code examples with the AWS SDK, including examples for trying cluster endpoints, see [Code examples for Application Recovery Controller using AWS SDKs](#service_code_examples).

**Use the extremely reliable data plane API to list and update routing control states, not the console**  
Using the ARC data plane API, view your routing controls and states with the [ListRoutingControls](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_ListRoutingControls.html) operation and update routing control states to redirect traffic for failover with the [UpdateRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlState.html) operation. You can use the AWS CLI [(as in these examples)](#getting-started-cli-routing.control-state) or code that you write using one of the AWS SDKs. ARC offers extreme reliability with the API in the data plane to fail over traffic. We recommend using the API instead of changing routing control states in the AWS Management Console.  
Connect to one of your Regional cluster endpoints for ARC to use the data plane API. If the endpoint is unavailable, try connecting to another cluster endpoint.  
If a safety rule blocks a routing control state update, you can bypass it to make the update and fail over traffic. For more information, see [Overriding safety rules to reroute traffic](#routing-control.override-safety-rule).

**Test failover with ARC**  
Test failover regularly with ARC routing control, to fail over from your primary application stack to a secondary application stack. It's important to make sure that the ARC structures that you've added are aligned with the correct resources in your stack, and that everything works as you expect it to. You should test this after you set up ARC for your environment, and continue to test periodically, so that your failover environment is prepared, before you experience a failure situation in which you need your secondary system to be up and running quickly to avoid downtime for your users.

### Routing control API operations
<a name="actions.routing-control"></a>

This section includes tables with lists API operations that you can use for setting up and using routing control in Amazon Application Recovery Controller (ARC), with links to relevant documentation.

For examples of how to use common routing control configuration API operations with the AWS Command Line Interface, see [Examples of using ARC routing control API operations with the AWS CLI](#getting-started-cli-routing).

The following table lists ARC API operations that you can use for routing control configuration, with links to relevant documentation.


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Create a cluster | See [Creating routing control components in ARC](#routing-control.create) | See [CreateCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html) | 
| Describe a cluster | See [Creating routing control components in ARC](#routing-control.create) | See [DescribeCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html) | 
| Delete a cluster | See [Creating routing control components in ARC](#routing-control.create) | See [DeleteCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html) | 
| List clusters for an account | See [Creating routing control components in ARC](#routing-control.create) | See [ListClusters](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html) | 
| Create a routing control | See [Creating routing control components in ARC](#routing-control.create) | See [CreateRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html) | 
| Describe a routing control | See [Creating routing control components in ARC](#routing-control.create) | See [DescribeRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html) | 
| Update a routing control | See [Creating routing control components in ARC](#routing-control.create) | See [UpdateRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html) | 
| Delete a routing control | See [Creating routing control components in ARC](#routing-control.create) | See [DeleteRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html) | 
| List routing controls | See [Creating routing control components in ARC](#routing-control.create) | See [ListRoutingControls](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-routingcontrols.html) | 
| Create a control panel | See [Creating routing control components in ARC](#routing-control.create) | See [CreateControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html) | 
| Describe a control panel | See [Creating routing control components in ARC](#routing-control.create) | See [DescribeControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html) | 
| Update a control panel | See [Creating routing control components in ARC](#routing-control.create) | See [UpdateControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html) | 
| Delete a control panel | See [Creating routing control components in ARC](#routing-control.create) | See [DeleteControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html) | 
| List control panels | See [Creating routing control components in ARC](#routing-control.create) | See [ListControlPanels](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanels.html) | 
| Create a safety rule | See [Creating safety rules for routing control](#routing-control.safety-rules) | See [CreateSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html) | 
| Describe a safety rule | See [Creating safety rules for routing control](#routing-control.safety-rules) | See [DescribeSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule-safetyrulearn.html) | 
| Update a safety rule | See [Creating safety rules for routing control](#routing-control.safety-rules) | See [UpdateSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html) | 
| Delete a safety rule | See [Creating safety rules for routing control](#routing-control.safety-rules) | See [DeleteSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule-safetyrulearn.html) | 
| List safety rules | See [Creating safety rules for routing control](#routing-control.safety-rules) | See [ListSafetyRules](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-safetyrules.html) | 
| List associated Route 53 health checks | See [Creating a routing control health check in ARC](#routing-control.create-health-check) | See [ ListAssociatedRoute53HealthChecks](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn-associatedroute53healthchecks.html) | 
| List the AWS RAM resource policies for cluster sharing | See [Support cross-account for clusters in ARC](#routing-control.failover-different-accounts) | See [ GetResourcePolicy](https://docs.aws.amazon.com/recovery-cluster/latest/api/resourcepolicy-resourcearn.html) | 

The following table lists common ARC API operations that you can use for managing traffic failover with the routing control data plane, with links to relevant documentation.


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Get a routing control state | See [Getting and updating routing control states in the AWS Management Console](#routing-control.update.console) | See [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html) | 
| List routing controls | N/A | See [ListRoutingControls](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_ListRoutingControls.html) | 
| Update a routing control state | See [Getting and updating routing control states in the AWS Management Console](#routing-control.update.console) | See [UpdateRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlState.html) | 
| Update multiple routing control states | See [Getting and updating routing control states in the AWS Management Console](#routing-control.update.console) | See [UpdateRoutingControlStates](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html) | 

#### Using this service with an AWS SDK
<a name="sdk-general-information-section"></a>

AWS software development kits (SDKs) are available for many popular programming languages. Each SDK provides an API, code examples, and documentation that make it easier for developers to build applications in their preferred language.


| SDK documentation | Code examples | 
| --- | --- | 
| [AWS SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp) | [AWS SDK for C\+\+ code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp) | 
| [AWS CLI](https://docs.aws.amazon.com/cli) | [AWS CLI code examples](https://docs.aws.amazon.com/code-library/latest/ug/cli_2_code_examples.html) | 
| [AWS SDK for Go](https://docs.aws.amazon.com/sdk-for-go) | [AWS SDK for Go code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2) | 
| [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java) | [AWS SDK for Java code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2) | 
| [AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript) | [AWS SDK for JavaScript code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3) | 
| [AWS SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin) | [AWS SDK for Kotlin code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin) | 
| [AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net) | [AWS SDK for .NET code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3) | 
| [AWS SDK for PHP](https://docs.aws.amazon.com/sdk-for-php) | [AWS SDK for PHP code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php) | 
| [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell) | [AWS Tools for PowerShell code examples](https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_code_examples.html) | 
| [AWS SDK for Python v4](https://docs.aws.amazon.com/sdk-for-python) | [AWS SDK for Python v4 code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/pythonv4) | 
| [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/sdk-for-python) | [AWS SDK for Python (Boto3) code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python) | 
| [AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby) | [AWS SDK for Ruby code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby) | 
| [AWS SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust) | [AWS SDK for Rust code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1) | 
| [AWS SDK for SAP ABAP](https://docs.aws.amazon.com/sdk-for-sapabap) | [AWS SDK for SAP ABAP code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap) | 
| [AWS SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift) | [AWS SDK for Swift code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift) | 

For examples specific to this service, see [Code examples for Application Recovery Controller using AWS SDKs](#service_code_examples).

**Example availability**  
Can't find what you need? Request a code example by using the **Provide feedback** link at the bottom of this page.

### Examples of using ARC routing control API operations with the AWS CLI
<a name="getting-started-cli-routing"></a>

This section walks through simple application examples of working with routing control, using the AWS Command Line Interface to work with the routing control capability in Amazon Application Recovery Controller (ARC) using API operations. The examples are intended to help you develop a basic understanding of how to work with routing control using the CLI.

With routing control in Amazon Application Recovery Controller (ARC), you can trigger traffic failovers between redundant application copies, or replicas, that are running in separate AWS Regions or Availability Zones.

You organize routing controls into groups called control panels that are provisioned on a cluster. A ARC cluster is a Regional set of endpoints that is globally deployed. Cluster endpoints provide a highly available API that you can use to set and retrieve routing control states. For more information about the components of the routing control feature, see [Routing control components](#introduction-components-routing).

**Note**  
ARC is a global service that supports endpoints in multiple AWS Regions. However, you must specify the US West (Oregon) Region—that is, specify the parameter `--region us-west-2`— in most ARC CLI commands. For example, use the `region` parameter when you create recovery groups, control panels, and clusters.   
When you create a cluster, ARC provides you with a set of Regional endpoints. To get or update routing control states, you must specify the Regional endpoint (the AWS Region and the endpoint URL) in your CLI command.

For more information about using the AWS CLI, see the AWS CLI Command Reference. For a list of routing control API actions, see [Routing control API operations](#actions.routing-control) and [Routing control API operations](#actions.routing-control).

We'll start by creating the components you need to manage failover by using routing controls, beginning with creating a cluster.

#### Set up routing control components
<a name="getting-started-cli-routing-config"></a>

Our first step is to create a cluster. An ARC cluster is a set of five endpoints, one in each of five different AWS Regions. The ARC infrastructure supports these endpoints to work in coordination so that they guarantee high availability and sequential consistency of failover operations. 

##### 1. Create a cluster
<a name="getting-started-cli-routing.cluster"></a>

1a. Create a cluster. The `network-type` is optional, and can either be `IPV4` or `DUALSTACK`. The default is `IPV4`.

```
aws route53-recovery-control-config create-cluster --cluster-name test --network-type DUALSTACK
```

```
"Cluster": {
    "ClusterArn": "arn:aws:route53-recovery-control::123456789123:cluster/12341234-1234-1234-1234-123412341234",
    "Name": "test",
    "Status": "PENDING",
    "Owner": "123456789123",
    "NetworkType": "DUALSTACK"
}
```

When you first create a ARC resource, it has a status of `PENDING` while the cluster is created. You can check in on its progress by calling `describe-cluster`. 

1b. Describe a cluster.

```
aws route53-recovery-control-config --region us-west-2 \
				describe-cluster --cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh
```

```
"Cluster": {
    "ClusterArn": "arn:aws:route53-recovery-control::123456789123:cluster/12341234-1234-1234-1234-123412341234",
    "Name": "test",
    "Status": "DEPLOYED",
    "Owner": "123456789123",
    "NetworkType": "DUALSTACK"
}
```

When the status is DEPLOYED, ARC has successfully created the cluster with the set of endpoints for you to interact with. You can list all of your clusters by calling `list-clusters`.

1c. List your clusters.

```
aws route53-recovery-control-config --region us-west-2 list-clusters
```

```
"Cluster": {
    "ClusterArn": "arn:aws:route53-recovery-control::123456789123:cluster/12341234-1234-1234-1234-123412341234",
    "Name": "test",
    "Status": "DEPLOYED",
    "Owner": "123456789123",
    "NetworkType": "DUALSTACK"
}
```

1d. Update the network type for your clusters. Options are `IPV4` or `DUALSTACK`.

```
aws route53-recovery-control-config update-cluster \
--cluster-arn arn:aws:route53-recovery-control::123456789123:cluster/12341234-1234-1234-1234-123412341234 \
--network-type DUALSTACK
```

```
"Cluster": {
    "ClusterArn": "arn:aws:route53-recovery-control::123456789123:cluster/12341234-1234-1234-1234-123412341234",
    "Name": "test",
    "Status": "PENDING",
    "Owner": "123456789123",
   "NetworkType": "DUALSTACK"
}
```

##### 2. Create a control panel
<a name="getting-started-cli-routing.panel"></a>

A control panel is a logical grouping for organizing your ARC routing controls. When you create a cluster, ARC automatically provides a control panel for you called `DefaultControlPanel`. You can use this control panel right away.

A control panel can only exist in one cluster. If you want to move a control panel to another cluster, you must delete it and then create it in the second cluster. You can see all of the control panels in your account by calling `list-control-panels`. To see just the control panels in a specific cluster, add the `--cluster-arn` field.

2a. List control panels.

```
aws route53-recovery-control-config --region us-west-2 \
				list-control-panels --cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/eba23304-1a51-4674-ae32-b4cf06070bdd
```

```
{
    "ControlPanels": [
        {
            "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/1234567dddddd1234567dddddd1234567",
            "ClusterArn": "arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh",
            "DefaultControlPanel": true,
            "Name": "DefaultControlPanel",
            "RoutingControlCount": 0,
            "Status": "DEPLOYED"
        }
    ]
}
```

Optionally, create your own control panel by calling `create-control-panel`.

2b. Create a control panel.

```
aws route53-recovery-control-config --region us-west-2 create-control-panel \
        --control-panel-name NewControlPanel2 \
        --cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh
```

```
{
    "ControlPanel": {
        "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "ClusterArn": "arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh",
        "DefaultControlPanel": false,
        "Name": "NewControlPanel2",
        "RoutingControlCount": 0,
        "Status": "PENDING"
    }
}
```

When you first create a ARC resource, it has a status of `PENDING` while it's being created. You can check on progress by calling `describe-control-panel`.

2c. Describe a control panel.

```
aws route53-recovery-control-config --region us-west-2 describe-control-panel \
				--control-panel-arn arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456
```

```
{
    "ControlPanel": {
        "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "ClusterArn": "arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh",
        "DefaultControlPanel": true,
        "Name": "DefaultControlPanel",
        "RoutingControlCount": 0,
        "Status": "DEPLOYED"
    }
}
```

##### 3. Create a routing control
<a name="getting-started-cli-routing.control"></a>

Now that you've set up the cluster and looked at control panels, you can begin creating routing controls. When you create a routing control, you must at least specify the Amazon Resource Name (ARN) of the cluster that you want the routing control to be in. You can also specify the ARN of a control panel for the routing control. You'll also need to specify the cluster where the control panel is located. 

If you don't specify a control panel, your routing control is added to the automatically created control panel, `DefaultControlPanel`.

Create a routing control by calling `create-routing-control`.

3a. Create a routing control.

```
aws route53-recovery-control-config --region us-west-2 create-routing-control \
				--routing-control-name NewRc1 \
				--cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh
```

```
{
    "RoutingControl": {
        "ControlPanelArn": " arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "Name": "NewRc1",
        "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
        "Status": "PENDING"
    }
}
```

Routing controls follow the same creation pattern as other ARC resources, so you can track their progress by calling a describe operation. 

3b. Describe routing control.

```
aws route53-recovery-control-config --region us-west-2 describe-routing-control \
			    --routing-control-arn arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567
```

```
{
    "RoutingControl": {
        "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "Name": "NewRc1",
        "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
        "Status": "DEPLOYED"
    }
}
```

You can list the routing controls in a control panel by calling `list-routing-controls`. The control panel ARN is required.

3c. List routing controls.

```
aws route53-recovery-control-config --region us-west-2 list-routing-controls \
        --control-panel-arn arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456
```

```
{
    "RoutingControls": [
        {
            "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
            "Name": "Rc1",
            "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
            "Status": "DEPLOYED"
        },
        {
            "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
            "Name": "Rc2",
            "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/hijklmnop987654321",
            "Status": "DEPLOYED"
        }
    ]
}
```

In the following example, where we work with routing control states, we assume that you have the two routing controls listed in this section (Rc1 and Rc2). In this example, each routing control represents an Availability Zone that your application is deployed in. 

##### 4. Create safety rules
<a name="getting-started-cli-routing.safety"></a>

When you work with several routing controls at the same time, you might decide that you want some safeguards in place when you enable and disable them, to avoid unintentional consequences, like turning both routing controls off and stopping all traffic flow. To create these safeguards, you create routing control safety rules.

There are two types of safety rules: assertion rules and gating rules. To learn more about safety rules, see [Creating safety rules for routing control](#routing-control.safety-rules).

The following call provides an example of creating an assertion rule that makes sure that at least one of two routing controls is set to `On` at any given time. To create the rule, you run `create-safety-rule` with the `assertion-rule` parameter.

For detailed information about the assertion rule API operation, see [AssertionRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-assertionrule) in the Routing Control API Reference Guide for Amazon Application Recovery Controller.

4a. Create an assertion rule.

```
aws route53-recovery-control-config --region us-west-2 create-safety-rule \
        --assertion-rule '{"Name": "TestAssertionRule", 
        "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx", 
        "WaitPeriodMs": 5000, 
        "AssertedControls":
        ["arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/def123def123def" 
        "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/ghi456ghi456ghi"], 
        "RuleConfig": {"Threshold": 1, "Type": "ATLEAST", "Inverted": false}}'
```

```
{
    "Rule": {
        "ASSERTION": {
            "Arn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/safetyrule/333333444444",
            "AssertedControls": [
                "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/def123def123def" 
                "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/ghi456ghi456ghi"],
            "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx",
            "Name": "TestAssertionRule",
            "RuleConfig": {
                "Inverted": false,
                "Threshold": 1,
                "Type": "ATLEAST"
            },
            "Status": "PENDING",
            "WaitPeriodMs": 5000
        }
    }
}
```

The following call provides an example of creating a gating rule that provides an overall "on/off" or "gating" switch for a set of target routing controls in a control panel. This lets you disallow updating the target routing controls so that, for example, automation can't make unauthorized updates. In this example, the gating switch is a routing control specified by the `GatingControls` parameter and the two routing controls that are controlled or "gated" are specified by the `TargetControls` parameter.

**Note**  
Before you create the gating rule, you must create the gating routing control, which does not include DNS failover records, and the target routing controls, which you do configure with DNS failover records.

To create the rule, you run `create-safety-rule` with the `gating-rule` parameter.

For detailed information about the assertion rule API operation, see [GatingRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-gatingrule) in the Routing Control API Reference Guide for Amazon Application Recovery Controller.

4b. Create a gating rule.

```
aws route53-recovery-control-config --region us-west-2 create-safety-rule \
        --gating-rule '{"Name": "TestGatingRule", 
        "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx", 
        "WaitPeriodMs": 5000, 
        "GatingControls": ["arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/def123def123def"] 
        "TargetControls": ["arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/ghi456ghi456ghi", 
        "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/lmn789lmn789lmn"], 
        "RuleConfig": {"Threshold": 0, "Type": "OR", "Inverted": false}}'
```

```
{
    "Rule": {
        "GATING": {
            "Arn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/safetyrule/444444444444",
            "GatingControls": [
                "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/def123def123def"
            ],
            "TargetControls": [
                "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/ghi456ghi456ghi" 
                "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/lmn789lmn789lmn"
            ],
            "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx",
            "Name": "TestGatingRule",
            "RuleConfig": {
                "Inverted": false,
                "Threshold": 0,
                "Type": "OR"
            },
            "Status": "PENDING",
            "WaitPeriodMs": 5000
        }
    }
}
```

As with other routing control resources, you can describe, list, or delete safety rules after they propagate to the data plane.

After you set up one or more safety rules, you can continue to interact with the cluster, to set, or retrieve state for routing controls. If a `set-routing-control-state` operation breaks a rule that you created, you’ll receive an exception similar to the following:

`Cannot modify control state for [0123456bbbbbbb0123456bbbbbb01234560123 abcdefg1234567] due to failed rule evaluation 0123456bbbbbbb0123456bbbbbb0123456333333444444`

The first identifier is the control panel ARN concatenated with the routing control ARN. The second identifier is the control panel ARN concatenated with the safety rule ARN.

##### 5. Create health checks
<a name="getting-started-cli-routing.healthcheck"></a>

To use routing controls to fail over traffic, you create health checks in Amazon Route 53, and then associate the health checks with your DNS records. To fail over traffic, a ARC routing control sets the health check to fail, so that Route 53 reroutes the traffic. (The health check doesn't valid the health of your application; it's simply used as a method for rerouting traffic.)

As an example, let's say you have two cells (Regions or Availability Zones). You configure one as the primary cell for your application, and the other as the secondary, to fail over to. 

To set up health checks for failover, you can do the following, for example:

1. Use the ARC CLI to create a routing control for each cell.

1. Use the Route 53 CLI to create a ARC health check in Route 53 for each routing control.

1. Use the Route 53 CLI to create two failover DNS records in Route 53, and associate a health check with each one.

5a. Create a routing control for each cell.

```
aws route53-recovery-control-config --region us-west-2 create-routing-control \
        --routing-control-name RoutingControlCell1 \
        --cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh
```

```
aws route53-recovery-control-config --region us-west-2 create-routing-control \
        --routing-control-name RoutingControlCell2 \
        --cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh
```

5b. Create a health check for each routing control.

**Note**  
You create ARC health checks by using the Amazon Route 53 CLI.

```
aws route53 create-health-check --caller-reference RoutingControlCell1 \
        --health-check-config \
        Type=RECOVERY_CONTROL,RoutingControlArn=arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567
```

```
{
    "Location": "https://route53.amazonaws.com/2015-01-01/healthcheck/11111aaaa-bbbb-cccc-dddd-ffffff22222",
    "HealthCheck": {
        "Id": "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "CallerReference": "RoutingControlCell1",
        "HealthCheckConfig": {
            "Type": "RECOVERY_CONTROL",
            "Inverted": false,
            "Disabled": false,
            "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567"
        },
        "HealthCheckVersion": 1
    }
}
```

```
aws route53 create-health-check --caller-reference RoutingControlCell2 \
				--health-check-config \
				Type=RECOVERY_CONTROL,RoutingControlArn=arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567
```

```
{
    "Location": "https://route53.amazonaws.com/2015-01-01/healthcheck/11111aaaa-bbbb-cccc-dddd-ffffff22222",
    "HealthCheck": {
        "Id": "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "CallerReference": "RoutingControlCell2",
        "HealthCheckConfig": {
            "Type": "RECOVERY_CONTROL",
            "Inverted": false,
            "Disabled": false,
            "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567"
        },
        "HealthCheckVersion": 1
    }
}
```

5c. Create two failover DNS records, and associate a health check with each one.

You create failover DNS records in Route 53 using the Route 53 CLI. To create the records, follow the directions in the Amazon Route 53 AWS CLI Command Reference for the [change-resource-record-sets](https://docs.aws.amazon.com/cli/latest/reference/route53/change-resource-record-sets.html) command. In the records, specify the DNS value for each cell together with the corresponding `HealthCheckID` value that Route 53 created for the health check (see 6b).

For the primary cell:

```
{
    "Name": "myapp.yourdomain.com",
    "Type": "CNAME",
    "SetIdentifier": "primary",
    "Failover": "PRIMARY",
    "TTL": 0,
    "ResourceRecords": [
        {
            "Value": "cell1.yourdomain.com"
        }
    ],
    "HealthCheckId": "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

For the secondary cell:

```
{
    "Name": "myapp.yourdomain.com",
    "Type": "CNAME",
    "SetIdentifier": "secondary",
    "Failover": "SECONDARY",
    "TTL": 0,
    "ResourceRecords": [
        {
            "Value": "cell2.yourdomain.com"
        }
    ],
    "HealthCheckId": "yyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
}
```

Now, to fail over from your primary cell to your secondary cell, you can follow the CLI example in step 4b to update the state of `RoutingControlCell1` to `OFF` and `RoutingControlCell2` to `ON`.

#### List and update routing controls and states with the AWS CLI
<a name="getting-started-cli-routing.control-state"></a>

After you create your Amazon Application Recovery Controller (ARC) resources, such as cluster, routing controls, and control panels, you can interact with the cluster to list and update routing control states for failover.

For each cluster that you create, ARC provides you with a set of cluster endpoints, one in each of five AWS Regions. You must specify one of these Regional endpoints (the AWS Region and the endpoint URL) when you make calls to the cluster to retrieve or set routing control states to `On` or `Off`. When you use the AWS CLI, to get or update routing control states, in addition to the Regional endpoint, you must also specify the `--region` of the Regional endpoint, as shown in the examples in this section.

You can use any of the Regional cluster endpoints. We recommend that your systems rotate through the regional endpoints, and be prepared to retry with each of the available endpoints. For code samples that illustrate trying cluster endpoints in sequence, see [Actions for Application Recovery Controller using AWS SDKs](#service_code_examples_actions).

For more information about using the AWS CLI, see the AWS CLI Command Reference. For a list of routing control API actions and links to more information, see [Routing control API operations](#actions.routing-control).

**Important**  
Although you can update a routing control state on the Amazon Route 53 console, we recommend that you [update routing control states](#routing-control.update.api) by using the AWS CLI or an AWS SDK. ARC offers extreme reliability with the ARC routing control data plane for rerouting traffic and failing over across cells. For more recommendations about using ARC for failover, see [Best practices for routing control in ARC](#route53-arc-best-practices.regional).

When you create a routing control, the state is set to `Off`. This means that traffic is not routed to the target cell for that routing control. You can verify the state of the routing control by running the command `get-routing-control-state`.

To determine the Region and the endpoint to specify, run the `describe-clusters` command to view the `ClusterEndpoints`. Each `ClusterEndpoint` includes a Region and corresponding endpoint that you can use to get or update routing control states. * [DescribeCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html) is a recovery control configuration API operation. We recommend that you keep a local copy of your ARC Regional cluster endpoints, in bookmarks or hardcoded in automation code that you use to retry your endpoints.*

##### 1. List routing controls
<a name="getting-started-cli-routing.view-rc"></a>

You can view your routing controls and routing control states using the highly reliable ARC data plane endpoints.

1. List routing controls for a specific control panel. If you don't specify a control panel, `list-routing-controls` returns all the routing controls in the cluster.

```
aws route53-recovery-cluster list-routing-controls --control-panel-arn \
        arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456 \ 
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{
    "RoutingControls": [{
        "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "ControlPanelName": "ExampleControlPanel",
        "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
        "RoutingControlName": "RCOne",
        "RoutingControlState": "On"
    },
    {
        "ControlPanelArn": "arn:aws:route53-recovery-control::023759465626:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "ControlPanelName": "ExampleControlPanel",
        "RoutingControlArn": "arn:aws:route53-recovery-control::023759465626:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/zzzzxxxxyyyy123456",
        "RoutingControlName": "RCTwo",
        "RoutingControlState": "Off"
    }
]
```

##### 2. Get routing controls
<a name="getting-started-cli-routing.get-rc"></a>

2. Get a routing control state.

```
aws route53-recovery-cluster get-routing-control-state --routing-control-arn \
        arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{"RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
    "RoutingControlName": "RCOne",
    "RoutingControlState": "On"
}
```

##### 2. Update routing controls
<a name="getting-started-cli-routing.update-rc"></a>

To route traffic to the target endpoint controlled by the routing control, you update the routing control state to `On`. Update the routing control state by running the command `update-routing-control-state`. (When the request is successful, the response is empty.)

2a. Update a routing control state.

```
aws route53-recovery-cluster update-routing-control-state \
        --routing-control-arn \
        arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
        --routing-control-state On \
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{}
```

You can update several routing controls at the same time with one API call: `update-routing-control-states`. (When the request is successful, the response is empty.)

2b. Update several routing control states at once (batch updates).

```
aws route53-recovery-cluster update-routing-control-states \
        --update-routing-control-state-entries \
        '[{"RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
        "RoutingControlState": "Off"}, \
        {"RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/hijklmnop987654321",
        "RoutingControlState": "On"}]' \
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{}
```

### Working with routing control components in ARC
<a name="routing-control.working-with"></a>

**Topics**
+ [Creating routing control components in ARC](#routing-control.create)
+ [Viewing and updating routing control states in ARC](#routing-control.update)
+ [Creating safety rules for routing control](#routing-control.safety-rules)
+ [Support cross-account for clusters in ARC](#routing-control.failover-different-accounts)

#### Creating routing control components in ARC
<a name="routing-control.create"></a>

This section explains how to create a cluster, routing controls, health checks, and control panels for working with routing control in Amazon Application Recovery Controller (ARC).

Start by creating a cluster, to host your routing controls and the control panels that you use to group them. Then create routing controls and health checks so you can reroute traffic to fail over from one cell to another, so that traffic goes to your backup replica, for example.

Note that you are charged by the hour for each cluster that you create. You typically only need one cluster to host the routing controls and control panels for recovery control management for an application. In addition, you can set up resource sharing by using AWS Resource Access Manager, so that one cluster can host routing controls and other ARC resources owned by multiple AWS accounts. To learn about resource sharing in ARC, [Support cross-account for clusters in ARC](#routing-control.failover-different-accounts). For pricing information, see [Amazon Application Recovery Controller (ARC) Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

To use routing controls to fail over traffic, you create routing control health checks that you associate with Amazon Route 53 DNS records for resources in your application. As an example, let's say you have two cells, one that you've configured as the primary cell for your application, and the other that you've configured as the secondary, to fail over to. 

To set up health checks for failover, do the following:

1. Create a routing control for each cell.

1. Create a health check for each routing control.

1. Create two DNS records, for example, two DNS failover records, and associate a health check with each one.

Another scenario when you might create a routing control is when you create a safety rule that is a gating rule. In this case, you don't associate health checks and DNS records with the routing control because you will use it as a *gating routing control*. For more information, see [Creating safety rules for routing control](#routing-control.safety-rules).

The steps to create the components for routing control on the ARC console are included in these sections. To learn about using recovery control configuration API operations with ARC, see the [Routing control API operations](#actions.routing-control).

##### Creating a cluster in ARC
<a name="routing-control.create-cluster"></a>

You must create a cluster to host routing controls and control panels in ARC.

A *cluster* is a set of redundant Regional endpoints against which you can execute API calls to update or get the state of one or more routing controls. A single cluster can host a number of routing controls. 

**Important**  
Be aware that you are charged by the hour for each cluster that you create. One cluster can host a number of routing controls and control panels for recovery control management, typically enough for an application.

##### To create a cluster


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Clusters**.

1. Choose **Create**, and then enter a name for your cluster.

1. Choose **Create cluster**.

##### Creating a routing control in ARC
<a name="routing-control.create-control"></a>

Create a routing control for each cell that you want to route traffic to. For example, when you have an application with resources that you have siloed for recoverability, you might have a cell for each AWS Region, and nested cells for each Availability Zone within each Region. In this scenario, you would create a routing control for each cell and each nested cell.

When you create routing controls, keep in mind that routing control names must be unique within each control panel.

After you create routing controls to use for rerouting traffic, you associate each one with a health check, which allows you to route traffic to cells, based on the DNS records that you've associated with each one. If you're setting up a gating rule as a safety rule and creating a gating routing control, you don't add a health check to the routing control.

##### To create a routing control


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. On the **Routing control** page, choose **Create**, and then choose a **Routing control**.

1. Enter a name for your routing control, choose the cluster to add the control to, and choose to add it to an existing control panel, including using the default control panel. Or, create a new control panel.

1. If you choose to create a new control panel, choose a cluster to create the control panel on, and then enter a name for the panel.

1. Choose **Create routing control**.

1. Follow the steps to name and create the routing control.

##### Creating a routing control health check in ARC
<a name="routing-control.create-health-check"></a>

You associate a routing control health check with each routing control that you want to use for rerouting traffic. Then you configure each health check with a Amazon Route 53 DNS record, for example, a failover DNS record. Then you can reroute traffic in Amazon Application Recovery Controller (ARC) simply by updating the state of the associated routing control, to set it to `On` or `Off`.

**Note**  
You can't edit an existing routing control health check to associate it with a different routing control.

##### To create a routing control health check


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. On the **Routing control** page, choose a routing control.

1. On the **Routing control** detail page, choose a **Create health check**.

1. Enter a name for the health check, and then choose **Create**.

Next, you create Route 53 DNS records, and associate your routing control health checks with each one. For example, let's assume that you want to use two DNS failover records to associate your routing control health checks with. For ARC to correctly fail over traffic by using routing controls, start by creating the two failover records in Route 53: a primary and a secondary. For more information about configuring DNS failover records, see [ Health checking concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-health-checking).

When you create the primary failover record, the values should be something like the following:

```
			Name: myapp.yourdomain.com
			Type: CNAME
			Set Identifier: Primary
			Failover: Primary
			TTL: 0
			Resource Records:
			Value: cell1.yourdomain.com
			Health Check ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

The secondary failover record values should be something like the following:

```
			Name: myapp.yourdomain.com
			Type: CNAME
			Set Identifier: Secondary
			Failover: Secondary
			TTL: 0
			Resource Records:
			Value: cell2.yourdomain.com
			Health Check ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Now, say that you want to reroute traffic because there's a failure. To do this, you update the associated routing control states to change the primary routing control state to `OFF` and the secondary routing control state to `ON`. When you do this, the associated health checks stop traffic from going to the primary replica and route it instead to the secondary replica. For more information about failing over traffic with routing controls, see [Getting and updating routing control states using the ARC API (recommended)](#routing-control.update.api).

To see examples of the AWS CLI commands for creating routing controls and the associated health checks using ARC API operations, see [Examples of using ARC routing control API operations with the AWS CLI](#getting-started-cli-routing).

##### Creating a control panel in ARC
<a name="routing-control.create-control-panel"></a>

A control panel in Amazon Application Recovery Controller (ARC) lets you group together related routing controls. A control panel can have routing controls that represent a microservice within an application, an entire application itself, or a group of applications, depending on the scope of your failover. A benefit of grouping routing controls into a control panel is that you can use safety rules with a control panel to help safeguard traffic routing changes. 

When you create a cluster, ARC creates a default control panel. You can use the default control panel for your routing controls, or you can create one or more control panels to group your routing controls. Note that only ASCII characters are supported for control panel names.

The steps to create a control panel on the ARC console are included in this section. For information about using recovery control configuration API operations with ARC, see the [Routing control API operations](#actions.routing-control).

##### To create a control panel


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. On the **Routing control** page, choose **Create**, and then choose a **Control panel**. 

1. Choose a cluster to create the control panel on, and then enter a name for the panel.

1. Choose **Create control panel**.

#### Viewing and updating routing control states in ARC
<a name="routing-control.update"></a>

This section describes how to view and update routing control states in Amazon Application Recovery Controller (ARC). Routing controls are simple on-off switches that manage traffic flow to cells in your recovery group. Cells are typically AWS Regions, or sometimes Availability Zones, that includes your resources. When a routing control state is `On`, traffic flows to the cell that is controlled by that routing control. 

You group routing controls into control panels, which are logical failover groupings. When you open a control panel on the console, for example, you can view all of the routing controls for a grouping at once, to see where traffic is flowing.

You can update a routing control state on the ARC console or by using the ARC API. We recommend that you update routing control states by using the API. First, ARC offers extreme reliability with the API in the data plane to perform these actions. That's important when you're changing these states because routing state changes fail over across cells by rerouting application traffic. In addition, by using the API, you can try connecting to different cluster endpoints in rotation, as needed, if a cluster endpoint that you try connecting to is unavailable.

You can update one routing control state, or you can update several routing control states at once. For example, you might want to set one routing control state to `Off` to stop traffic from flowing to one cell, such as an Availability Zone where an application is experiencing increased latency. At the same time, you might want to set another routing control state to `On` to start traffic flowing to another cell or Availability Zone. In this scenario, you can update both routing control states at the same time, so traffic continues to flow.

**Topics**
+ [Getting and updating routing control states using the ARC API (recommended)](#routing-control.update.api)
+ [Getting and updating routing control states in the AWS Management Console](#routing-control.update.console)

##### Getting and updating routing control states using the ARC API (recommended)
<a name="routing-control.update.api"></a>

We recommend that you use Amazon Application Recovery Controller (ARC) API operations to get or update routing control states, by using an AWS CLI command or by using code that you have developed to use ARC API operations with one of the AWS SDKs. We recommend using API operations, with the CLI or in code, for working with routing control states, rather than using the AWS Management Console.

ARC offers extreme reliability for failing over across cells (AWS Regions) by updating routing control states using the API because routing controls are stored in a highly available cluster. ARC ensures that at least three out of the five Regional cluster endpoints are always accessible to you to make routing control state changes. To get or change a routing control state using the API, you connect to one of your Regional cluster endpoints. If the endpoint is unavailable, you can try connecting to another one of your cluster endpoints.

You can view the list of Regional cluster endpoints for your cluster in the Route 53 console, or by using an API action, [DescribeCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html). Your process for getting and changing routing control states should try each endpoint in rotation, as needed, since cluster endpoints are cycled through available and unavailable states for regular maintenance and updates. 

We provide detailed information and code examples for using ARC API operations to get and update routing control states, and work with Regional cluster endpoints. For more information, see the following :
+ For code examples that explain how to rotate through Regional cluster endpoints to get and set routing control states, see [Actions for Application Recovery Controller using AWS SDKs](#service_code_examples_actions). 
+ For information about using the AWS CLI to get and update routing control states, see [List and update routing controls and states with the AWS CLI](#getting-started-cli-routing.control-state).

##### Getting and updating routing control states in the AWS Management Console
<a name="routing-control.update.console"></a>

You can get and update routing control states in the AWS Management Console. Be aware, though, that you can't choose different Regional cluster endpoints in the console. That is, there isn't a process for choosing and rotating through cluster endpoints in the console as you can do by using the Amazon Application Recovery Controller (ARC) API. In addition, the console is not highly available while the ARC data plane offers extreme reliability. For these reasons, we recommend that you use the ARC API to get and update routing control states for production operations.

For more recommendations about using ARC for failover, see [Best practices for routing control in ARC](#route53-arc-best-practices.regional).

To view and update routing controls in the console, follow the steps in the following procedures.

##### To get routing control states


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. From the list, choose a control panel and view the routing controls.

##### To update one or multiple routing control states


1. Open the Amazon Route 53 console at [ https://console.aws.amazon.com/route53recovery/home](https://console.aws.amazon.com/route53recovery/home). 

1. Under **Application Recovery Controller**, choose **Routing control**.

1. Choose **Action**, and then choose **Change traffic routing**.

1. Update the states of one or more routing controls to be `Off` or `On`, depending on where you want traffic to flow or stop flowing for your application.

1. Enter `confirm` in the text box.

1. Choose **Update traffic routing**.

#### Creating safety rules for routing control
<a name="routing-control.safety-rules"></a>

When you work with several routing controls at the same time, you might decide that you want safeguards in place to avoid unintended consequences. For example, you might want to prevent inadvertently turning off all the routing controls for an application, which would result in a fail-open scenario. Or you might want to implement a master on-off switch to disable a set of routing controls, perhaps to prevent automation from rerouting traffic. To establish safeguards like these for routing control in ARC, you create *safety rules*. 

You configure safety rules for routing control with a combination of routing controls, rules, and other options that you specify. Each safety rule is associated with a single control panel, but a control panel can have more than one safety rule. When you create safety rules, keep in mind that safety rule names must be unique within each control panel.

**Topics**
+ [Types of safety rules](#routing-control.about-safety-rule)
+ [Creating a safety rule on the console](#routing-control.create-safety-rule)
+ [Editing or deleting a safety rule on the console](#routing-control.edit-delete-safety-rule)
+ [Overriding safety rules to reroute traffic](#routing-control.override-safety-rule)

##### Types of safety rules
<a name="routing-control.about-safety-rule"></a>

There are two types of safety rules, *assertion rules* and *gating rules*, which you can use to safeguard failover in different ways.

**Assertion rule**  
With an assertion rule, when you change one or a set of routing control states, ARC enforces that the criteria that you set when you configured the rule is met, or else the routing control states aren't changed.   
An example of when this is useful is to prevent a fail-open scenario, like a scenario where you stop traffic from going to one cell but do not start traffic flowing to another cell. To avoid this, an assertion rule makes sure that at least one routing control in a set of routing controls in a control panel is `On` at any given time. This ensures that traffic flows to at least one Region or Availability Zone for an application.   
To see an example AWS CLI command that creates an assertion rule to enforce this criteria, see *Create safety rules* in [Examples of using ARC routing control API operations with the AWS CLI](#getting-started-cli-routing).   
For detailed information about the assertion rule API operation properties, see [AssertionRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-assertionrule) in the Routing Control API Reference Guide for Amazon Application Recovery Controller.

**Gating rule**  
With a gating rule, you can enforce an overall on-off switch over a set of routing controls so that whether those routing control states can be changed is enforced based on a set of criteria that you specify in the rule. The simplest criteria is whether a single routing control that you specify as the switch is set to `ON` or `OFF`.   
To implement this, you create a *gating routing control*, to use as the overall switch, and *target routing controls*, to control traffic flow to different Regions or Availability Zones. Then, to prevent manual or automated state updates to the target routing controls that you've configured for the gating rule, you set the gating routing control state to `Off`. To allow updates, you set it to `On`.   
To see an example AWS CLI command that creates a gating rule that implements this kind of overall switch, see *Create safety rules* in [Examples of using ARC routing control API operations with the AWS CLI](#getting-started-cli-routing).   
For detailed information about the gating rule API operation properties, see [GatingRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-gatingrule) in the Routing Control API Reference Guide for Amazon Application Recovery Controller.

##### Creating a safety rule on the console
<a name="routing-control.create-safety-rule"></a>

The steps in this section explain how to create a safety rule on the ARC console. The steps are similar whether you create an assertion rule or a gating rule. The differences are noted in the procedure.

To learn about using recovery and routing control API operations with Amazon Application Recovery Controller (ARC), see [Routing control API operations](#actions.routing-control).

##### To create a safety rule


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. On the **Routing control** page, choose a control panel.

1. On the control panel details page, choose **Action**, and then choose **Add safety rule**.

1. Choose a type of rule to add: **Assertion rule** or **Gating rule**.

1. Choose a name and, optionally, change the wait period.

1. Specify the configuration options for the safety rule.
   + For an assertion rule, specify the asserted routing controls.
   + For a gating rule, specify the gating routing control and target routing controls.

   For both rules, specify the rule configuration by choosing the type and threshold, and whether the rule is inverted.
**Note**  
To learn more about specifying an assertion rule, see the information provided for [AssertionRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-assertionrule) operation in the Routing Control API Reference Guide for Amazon Application Recovery Controller. To learn more about specifying a gating rule, see the information provided for the [GatingRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-gatingrule) operation in the Routing Control API Reference Guide for Amazon Application Recovery Controller.

1. Choose **Create**.

##### Editing or deleting a safety rule on the console
<a name="routing-control.edit-delete-safety-rule"></a>

The steps in this section explain how to edit or delete a safety rule on the ARC console. You can make only limited edits to a safety rule, to change the name or update the wait period. To make other changes, delete and recreate the safety rule.

To learn about using API operations with Amazon Application Recovery Controller (ARC), see the [Routing control API operations](#actions.routing-control).

##### To delete a safety rule


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. On the **Routing control** page, choose a control panel.

1. On the control panel details page, choose a safety rule, and then choose **Delete** or **Edit**.

##### Overriding safety rules to reroute traffic
<a name="routing-control.override-safety-rule"></a>

There are scenarios when you might want to bypass the routing control safeguards that are enforced with safety rules that you've configured. For example, you might want to fail over quickly for disaster recovery, and one or more safety rules might be unexpectedly preventing you from updating a routing control state to reroute traffic. In a "break glass" scenario like this, you can override one or more safety rules to change a routing control state and fail over your application.

You can bypass safety rules when you update a routing control state (or multiple routing control states) by using the `update-routing-control-state` or `update-routing-control-states` AWS CLI command with the `safety-rules-to-override` parameter. Specify the parameter with the Amazon Resource Name (ARN) of the safety rule that you want to override, or specify a comma-separated list of ARNs to override two or more safety rules.

When a safety rule blocks a routing control state update, the error message includes the ARN of the rule that blocked the update. So you can make a note of the ARN, and then specify it in a routing control state CLI command with the safety rule override parameter.

**Note**  
Because more than one safety rule might be in place for the routing controls that you're updating, you could run the CLI command to update your routing control state with one safety rule override but get an error that another safety rule is blocking the update. Continue to add safety rule ARNs to the list of rules to override in the update command, separated by commas, until the update command completes successfully.

To learn more about using the `SafetyRulesToOverride` property with the API and SDKs, see [UpdateRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlState.html).

The following are two examples of CLI commands to override safety rules to update routing control states.

**Override one safety rule**  

```
aws route53-recovery-cluster --region us-west-2 update-routing-control-state \
				--routing-control-arn \
				arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
				--routing-control-state On \
				--safety-rules-to-override arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/safetyrule/yyyyyyy8888888 \
				--endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

**Override two safety rules**  

```
aws route53-recovery-cluster --region us-west-2 update-routing-control-state \
				--routing-control-arn \
				arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
				--routing-control-state On \
				--safety-rules-to-override "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/safetyrule/yyyyyyy8888888" \
				"arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/safetyrule/qqqqqqq7777777"
				--endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

#### Support cross-account for clusters in ARC
<a name="routing-control.failover-different-accounts"></a>

Amazon Application Recovery Controller (ARC) integrates with AWS Resource Access Manager to enable resource sharing. AWS RAM is a service that enables you to share resources with other AWS accounts or through AWS Organizations. For ARC routing control, you can share the cluster resource.

With AWS RAM, you share resources that you own by creating a *resource share*. A resource share specifies the resources to share, and the *participants* to share them with. Participants can include:
+ Specific AWS accounts inside or outside of owner's organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations

For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.

By using AWS Resource Access Manager to share cluster resources across accounts in ARC, you can use one cluster to host control panels and routing controls owned by several different AWS accounts. When you opt to share a cluster, other AWS accounts that you specify can use the cluster to host their own control panels and routing controls, allowing more control and flexibility over routing capabilities across different teams.

AWS RAM is a service that helps AWS customers to securely share resources across AWS accounts. With AWS RAM, you can share resources within an organization or organizational units (OUs) in AWS Organizations, by using IAM roles and users. AWS RAM is a centralized and controlled way to share a cluster. 

When you share a cluster, you can reduce the number of total clusters that your organization requires. With a shared cluster, you can allocate the total cost of running the cluster across different teams, to maximize the benefits of ARC with lower cost. (Creating resources that are hosted in a cluster does not have additional costs, for the owner or for participants.) Sharing clusters across accounts can also ease the process of onboarding multiple applications to ARC, especially if you have a large number of applications distributed across several accounts and operations teams.

To get started with cross-account sharing in ARC, you create a *resource share* in AWS RAM. The resource share specifies *participants* who are authorized to share the cluster that your account owns. Then, participants can create resources, such as control panels and routing controls, in the cluster, by using the AWS Management Console or by running ARC API operations using the AWS Command Line Interface or AWS SDKs.

This topic explains how to share resources that you own, and how to use resources that are shared with you.

**Topics**
+ [Prerequisites for sharing clusters](#sharing-prereqs)
+ [Sharing a cluster](#sharing-share)
+ [Unsharing a shared cluster](#sharing-unshare)
+ [Identifying a shared cluster](#sharing-identify)
+ [Responsibilities and permissions for shared clusters](#sharing-perms)
+ [Billing costs](#sharing-billing)
+ [Quotas](#sharing-quotas)

##### Prerequisites for sharing clusters
<a name="sharing-prereqs"></a>
+ To share a cluster, you must own it in your AWS account. This means that the resource must be allocated or provisioned in your account. You cannot share a cluster that has been shared with you.
+ To share a cluster with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [ Enable sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.
+ AWS RAM resource shares for global resources like clusters must be created in US East (N. Virginia) Region (us-east-1).

##### Sharing a cluster
<a name="sharing-share"></a>

When you share a cluster that you own, the participants that you specify to share the cluster can create and host their own ARC resources in the cluster.

To share a cluster, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the participants they're shared with. To share a cluster you can create a new resource share or add the resource to an existing resource share. To create a new resource share, you can use the [AWS RAM console](https://console.aws.amazon.com/ram), or use AWS RAM API operations with the AWS Command Line Interface or AWS SDKs.

If you are part of an organization in AWS Organizations and sharing within your organization is enabled, participants in your organization are automatically granted access to the shared cluster. Otherwise, participants receive an invitation to join the resource share and are granted access to the shared cluster after accepting the invitation.

You can share a cluster that you own by using the AWS RAM console, or by using AWS RAM API operations with the AWS CLI or SDKs.

**To share a cluster that you own by using the AWS RAM console**  
See [ Creating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html) in the *AWS RAM User Guide*.

**To share a cluster that you own by using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command.

**Granting permissions to share clusters**

Sharing clusters across accounts requires permissions for the IAM principal sharing the cluster via AWS RAM.

We recommend using the `AmazonRoute53RecoveryControlConfigFullAccess` managed IAM policy to ensure that your IAM principals have the required permissions to share and use shared clusters.

Sharing a cluster using a custom IAM policy requires `route53-recovery-control-config:PutResourcePolicy`, `route53-recovery-control-config:GetResourcePolicy`, and `route53-recovery-control-config:DeleteResourcePolicy` permissions for that cluster. `PutResourcePolicy` and `DeleteResourcePolicy` are permission-only IAM actions. Attempting to share a cluster through AWS RAM without having these permissions will result in an error.

For more information about the way that AWS Resource Access Manager uses IAM see [ How AWS Resource Access Manager uses IAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html) in the *AWS RAM User Guide*.

##### Unsharing a shared cluster
<a name="sharing-unshare"></a>

When you unshare a cluster, the following applies to participants and owners:
+ Current participant resources continue to exist in the unshared cluster.
+ Participants can continue to update routing control states in the unshared cluster, to manage routing for application failover.
+ Participants can no longer create new resources in the unshared cluster.
+ If participants still have resources in an unshared cluster, the owner cannot delete the shared cluster.

To unshare a shared cluster that you own, remove it from the resource share. You can do this by using the AWS RAM console or by using AWS RAM API operations with the AWS CLI or SDKs.

**To unshare a shared cluster that you own using the AWS RAM console**  
See [Updating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared cluster that you own using the AWS CLI**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

##### Identifying a shared cluster
<a name="sharing-identify"></a>

Owners and participants can identify shared clusters by viewing information in AWS RAM. They can also get information about shared resources by using the ARC console and AWS CLI.

In general, to learn more about the resources that you've shared or that have been shared with you, see the information in the AWS Resource Access Manager User Guide:
+ As an owner, you can view all resources that you are sharing with others by using AWS RAM. For more information, see [Viewing your shared resources in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-view-sr.html).
+ As a participant, you can view all resources shared with you by using AWS RAM. For more information, see [Viewing your shared resources in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-view-sr.html).

As an owner, you can determine if you're sharing a cluster by viewing information in the AWS Management Console or by using the AWS Command Line Interface with ARC API operations.

**To identify if a cluster that you own is shared by using the console**  
In the AWS Management Console, on the details page for a cluster, see the **Cluster sharing status**.

**To identify if a cluster that you own is shared by using the AWS CLI**  
Use the [ get-resource-policy](https://docs.aws.amazon.com/recovery-cluster/latest/api/resourcepolicy-resourcearn.html.html) command. If there is a resource policy for a cluster, the command returns information about the policy.

As a participant, when a cluster is shared with you, you typically must accept the share. In addition, the **Owner** field for the cluster contains the account of the cluster owner.

##### Responsibilities and permissions for shared clusters
<a name="sharing-perms"></a>

###### Permissions for owners
<a name="perms-owner"></a>

When you share a cluster that you own with other AWS accounts, participants who are permitted to use the cluster can create control panels, routing controls, and other resources in the cluster. 

As a cluster owner, you are responsible for creating, managing, and deleting clusters. You can't modify or delete resources created by participants, such as routing controls and safety rules. For example, you can't update a routing control created by a participant to change the routing control state.

However, you can view the details for routing controls that are created by participants in a cluster that you own. For example, you can view routing control states by calling a [ARC routing control API operation](#actions.routing-control), using the AWS Command Line Interface or AWS SDKs.

If you need to modify resources create by participants, they can set up a role in IAM with permission to access the resources, and add your account to the role.

###### Permissions for participants
<a name="perms-consumer"></a>

In general, participants can create and use control panels, routing controls, safety rules, and health checks that they create in a cluster that is shared with them. They can only view, modify, or delete cluster resources in the shared cluster if they own the resources. For example, participants can create and delete safety rules for control panels that they have created.

The following restrictions apply for participants:
+ Participants cannot view, modify, or delete control panels created by other accounts using a shared cluster.
+ Participants cannot view, create, or modify routing controls, including routing control states, for resources created in a shared cluster by other accounts.
+ Participants cannot create, modify, or view safety rules created by other accounts in a shared cluster.
+ Participants cannot add resources in the default control panel in a shared cluster because it belongs to the cluster owner.

As noted, participants cannot create routing controls in the default control panel for a shared cluster, because the cluster owner owns the default control panel. However, the cluster owner can create a cross-account IAM role that provides permission to access the default control panel for the cluster. Then, the owner can grant a participant permissions to assume the role, so that the participant can access the default control panel to use it however the owner has specified through the role's permissions.

##### Billing costs
<a name="sharing-billing"></a>

The owner of a cluster in ARC is billed for costs associated with the cluster. There are no additional costs, for cluster owners or for participants, for creating resources hosted in a cluster.

For detailed pricing information and examples, see [Amazon Application Recovery Controller (ARC) Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

##### Quotas
<a name="sharing-quotas"></a>

All resources created in a shared cluster—including resources created by all participants with access to the shared cluster—count toward quotas in effect for the cluster and other resources, such as routing controls. If accounts that share the cluster resource have a higher quota than the cluster owner's quotas, the cluster owner's quotas takes precedence over the quotas for the accounts that are sharing.

 To better understand how this works, see the following examples. To illustrate how quotas work with resource sharing, for these examples, let's say that the cluster owner is Owner and an account that the cluster has been shared with is Participant.

**Control panels quota**  
Quotas are enforced for Owner's total control panels per cluster.  
For example, say Owner has a quota of 50 for the number of control panels per cluster, and has 13 control panels in the cluster. Now, say that Participant has the quota set to 150. In this scenario, Participant can only create up to 37 control panels (that is, 50-13) in the shared cluster.  
In addition, if other accounts that share the cluster also create control panels, those also all count toward the cluster overall quota of 50 control panels.

**Routing control quotas**  
Routing controls have multiple quotas: a quota per control panel, a quota per cluster, and a quota per safety rule. Owner's quotas take precedence for all of these quotas.  
For example, say Owner has a quota of 300 for the number of routing controls per cluster, and already has 300 routing controls in the cluster. Now, say that Participant has this quota set to 500. In this scenario, Participant cannot create any new routing controls in the shared cluster.

**Safety rules quotas**  
Quotas are enforced for Owner's safety rules per control panel quota.  
For example, say Owner has a quota of 20 for the number of safety rules per control panel and Participant has this quota set to 80. In this scenario, because Owner's lower limit takes precedence, Participant can only create up to 20 safety rules in a control panel in the shared cluster. 

For a list of routing control quotas, see [Quotas for routing control](#routing-control.quotas).

### Logging and monitoring for routing control in Amazon Application Recovery Controller (ARC)
<a name="monitoring-routing"></a>

You can use AWS CloudTrail for monitoring routing control in Amazon Application Recovery Controller (ARC), to analyze patterns and help troubleshoot issues.

**Topics**
+ [Logging ARC API calls using AWS CloudTrail](#cloudtrail-routing)

#### Logging ARC API calls using AWS CloudTrail
<a name="cloudtrail-routing"></a>

Amazon Application Recovery Controller (ARC) is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in ARC. CloudTrail captures all API calls for ARC as events. The calls captured include calls from the ARC console and code calls to the ARC API operations. 

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for ARC. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**.

Using the information collected by CloudTrail, you can determine the request that was made to ARC, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

##### ARC information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in ARC, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for ARC, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All ARC actions are logged by CloudTrail and are documented in the [Recovery Readiness API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/recovery-readiness/latest/api/), [Recovery Control Configuration API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/recovery-cluster/latest/api/), and [Routing Control API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/routing-control/latest/APIReference/). For example, calls to the `CreateCluster`, `UpdateRoutingControlState` and `CreateRecoveryGroup` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

##### Viewing ARC events in event history
<a name="amazon-arc-events-in-cloudtrail-event-history"></a>

CloudTrail lets you view recent events in **Event history**. To view events for ARC API requests, you must choose **US West (Oregon)** in the Region selector at the top of the console. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*.

##### Understanding ARC log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `CreateCluster` action for configuring routing control.

```
{
  "eventVersion": "1.08",
   "userIdentity": {
     "type": "IAMUser",
     "principalId": "A1B2C3D4E5F6G7EXAMPLE",
     "arn": "arn:aws:iam::111122223333:user/smithj",
     "accountId": "111122223333",
     "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
     "sessionContext": {
          "sessionIssuer": {
              "type": "Role",
              "principalId": "A1B2C3D4E5F6G7EXAMPLE",
              "arn": "arn:aws:iam::111122223333:role/smithj",
              "accountId": "111122223333",
              "userName": "smithj"
          },
          "webIdFederationData": {},
          "attributes": {
              "mfaAuthenticated": "false",
              "creationDate": "2021-06-30T04:44:41Z"
          }
      }
  },
  "eventTime": "2021-06-30T04:45:46Z",
  "eventSource": "route53-recovery-control-config.amazonaws.com",
  "eventName": "CreateCluster",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "192.0.2.50",
  "userAgent": "aws-cli/2.0.0 Python/3.8.2 Darwin/19.6.0 botocore/2.0.0dev7",
  "requestParameters": {
      "ClientToken": "12345abcdef-1234-5678-abcd-12345abcdef",
      "ClusterName": "XYZCluster"
  },
  "responseElements": {
      "Cluster": {
          "Arn": "arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456",
          "ClusterArn": "arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456",
          "Name": "XYZCluster",
          "Status": "PENDING"
      }
  },
  "requestID": "6090509a-5a97-4be6-8e6a-7d73example",
  "eventID": "9cab44ef-0777-41e6-838f-f249example",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "111122223333"
}
```

The following example shows a CloudTrail log entry that demonstrates the `UpdateRoutingControlState` action for routing control.

```
{
  "eventVersion": "1.08",
   "userIdentity": {
     "type": "AssumedRole",
     "principalId": "A1B2C3D4E5F6G7EXAMPLE",
     "arn": "arn:aws:sts::111122223333:assumed-role/admin/smithj",
     "accountId": "111122223333",
     "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
     "sessionContext": {
          "sessionIssuer": {
              "type": "Role",
              "principalId": "A1B2C3D4E5F6G7EXAMPLE",
              "arn": "arn:aws:iam::111122223333:role/admin",
              "accountId": "111122223333",
              "userName": "admin"
          },
          "webIdFederationData": {},
          "attributes": {
              "mfaAuthenticated": "false",
              "creationDate": "2021-06-30T04:44:41Z"
          }
      }
  },
  "eventTime": "2021-06-30T04:45:46Z",
  "eventSource": "route53-recovery-control-config.amazonaws.com",
  "eventName": "UpdateRoutingControl",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "192.0.2.50",
  "userAgent": "aws-cli/2.0.0 Python/3.8.2 Darwin/19.6.0 botocore/2.0.0dev7",
  "requestParameters": {
      "RoutingControlName": "XYZRoutingControl3",
      "RoutingControlArn": "arn:aws:route53-recovery-control::012345678:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567"
  },
  "responseElements": {
      "RoutingControl": {
          "ControlPanelArn": "arn:aws:route53-recovery-control::012345678:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
          "Name": "XYZRoutingControl3",
          "Status": "DEPLOYED",
          "RoutingControlArn": "arn:aws:route53-recovery-control::012345678:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567"
      }
  },
  "requestID": "6090509a-5a97-4be6-8e6a-7d73example",
  "eventID": "9cab44ef-0777-41e6-838f-f249example",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "111122223333"
}
```

### Identity and Access Management for routing control in ARC
<a name="security-iam-routing"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use ARC resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [How routing control works with IAM](#security_iam_service-with-iam-routing)
+ [Identity-based policy examples](#security_iam_id-based-policy-examples-routing)
+ [AWS managed policies](#security-iam-awsmanpol-routing)

#### How routing control in Amazon Application Recovery Controller (ARC) works with IAM
<a name="security_iam_service-with-iam-routing"></a>

Before you use IAM to manage access to routing control in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with routing control.


**IAM features that you can use with routing control in Amazon Application Recovery Controller (ARC)**  

| IAM feature | Routing control support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-routing-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-routing-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-routing-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-routing-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-routing-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-routing-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-routing-tags) |  Partial | 
| [Temporary credentials](#security_iam_service-with-iam-routing-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-routing-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-routing-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-routing-roles-service-linked) |  No  | 

To get a high-level, overall view of how AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Identity-based policies for ARC
<a name="security_iam_service-with-iam-routing-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To view examples of ARC identity-based policies for routing control, see [Identity-based policy examples for routing control in ARC](#security_iam_id-based-policy-examples-routing).

##### Resource-based policies within routing control
<a name="security_iam_service-with-iam-routing-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

##### Policy actions for routing control
<a name="security_iam_service-with-iam-routing-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of ARC actions for routing control, see [ Actions defined by Amazon Route 53 Recovery Controls](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycontrols-actions-as-permissions) and [ Actions defined by Amazon Route 53 Recovery Cluster](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycluster-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in ARC for routing control use the following prefixes before the action, depending on the API that you're working with:

```
route53-recovery-control-config
route53-recovery-cluster
```

To specify multiple actions in a single statement, separate them with commas. For example, you could do the following:

```
"Action": [
      "route53-recovery-control-config:{{action1}}",
      "route53-recovery-control-config:{{action2}}"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "route53-recovery-control-config:Describe*"
```

To view examples of ARC identity-based policies for routing control, see [Identity-based policy examples for routing control in ARC](#security_iam_id-based-policy-examples-routing).

##### Policy resources for ARC
<a name="security_iam_service-with-iam-routing-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

In the *Service Authorization Reference*, you can see the following information related to ARC:

To see a list of resource types and their ARNs, and the actions that you can specify with the ARN of each resource, see the following topics in the *Service Authorization Reference*:
+ [ Actions defined by Amazon Route 53 Recovery Controls](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycontrols-actions-as-permissions)
+ [ Actions defined by Amazon Route 53 Recovery Cluster](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycluster-actions-as-permissions).

To view examples of ARC identity-based policies for routing control, see [Identity-based policy examples for routing control in ARC](#security_iam_id-based-policy-examples-routing).

##### Policy condition keys for ARC
<a name="security_iam_service-with-iam-routing-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of ARC condition keys for routing control, see the following topics in the *Service Authorization Reference*:
+ [ Condition keys for Amazon Route 53 Recovery Controls](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycontrols-policy-keys)
+ [ Condition keys for Amazon Route 53 Recovery Cluster](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycluster-policy-keys)

To see the actions and resources that you can use with a condition key, see the following topics in the *Service Authorization Reference*:
+ To see a list of resource types and their ARNs, see [ Actions defined by Amazon Route 53 Recovery Controls](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycontrols-actions-as-permissions) and [ Actions defined by Amazon Route 53 Recovery Cluster](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycluster-actions-as-permissions).
+ To see a list of the actions that you can specify with the ARN of each resource, see [ Resources defined by Amazon Route 53 Recovery Controls](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycontrols-resources-for-iam-policies) and [ Resources defined by Amazon Route 53 Recovery Cluster](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoverycluster-resources-for-iam-policies).

To view examples of ARC identity-based policies for routing control, see [Identity-based policy examples for routing control in ARC](#security_iam_id-based-policy-examples-routing)

##### Access control lists (ACLs) in ARC
<a name="security_iam_service-with-iam-routing-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

##### Attribute-based access control (ABAC) with ARC
<a name="security_iam_service-with-iam-routing-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

ARC routing control includes the following support for ABAC: 
+ Recovery Control Config supports ABAC. 
+ Recovery Cluster does not support ABAC. 

##### Using temporary credentials with ARC
<a name="security_iam_service-with-iam-routing-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Cross-service principal permissions for ARC
<a name="security_iam_service-with-iam-routing-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

When you use an IAM entity (user or role) to perform actions in AWS, you are considered a principal. Policies grant permissions to a principal. When you use some services, you might perform an action that then triggers another action in a different service. In this case, you must have permissions to perform both actions.

To see whether an action requires additional dependent actions in a policy, see the following topics in the *Service Authorization Reference*:
+ [ Amazon Route 53 Recovery Cluster](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycluster.html)
+ [ Amazon Route 53 Recovery Controls](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html)

##### Service roles for ARC
<a name="security_iam_service-with-iam-routing-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

##### Service-linked roles for ARC
<a name="security_iam_service-with-iam-routing-roles-service-linked"></a>

**Supports service-linked roles:** 

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

Routing control does not use service-linked roles. 

#### Identity-based policy examples for routing control in ARC
<a name="security_iam_id-based-policy-examples-routing"></a>

By default, users and roles don't have permission to create or modify ARC resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by ARC, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices-zonal)
+ [Example: ARC console access for routing control](#security_iam_id-based-policy-examples-console-routing)
+ [Examples: ARC API actions for routing control configuration](#security_iam_id-based-policy-examples-api-routing)

##### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices-zonal"></a>

Identity-based policies determine whether someone can create, access, or delete ARC resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

##### Example: ARC console access for routing control
<a name="security_iam_id-based-policy-examples-console-routing"></a>

To access the Amazon Application Recovery Controller (ARC) console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the ARC resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can still use the ARC console when you allow access to only specific API operations, also attach a `ReadOnly` AWS managed policy for ARC to the entities. For more information, see the ARC [ARC managed policies page](#security-iam-awsmanpol) or [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

To give users full access to use ARC routing control features through the console, attach a policy like the following to the user, to give the user full permissions to configure ARC routing control resources and operations:

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
                   "route53-recovery-cluster:GetRoutingControlState",
                   "route53-recovery-cluster:UpdateRoutingControlState",
                   "route53-recovery-cluster:UpdateRoutingControlStates",
                   "route53-recovery-control-config:CreateCluster",
                   "route53-recovery-control-config:CreateControlPanel",
                   "route53-recovery-control-config:CreateRoutingControl",
                   "route53-recovery-control-config:CreateSafetyRule",
                   "route53-recovery-control-config:DeleteCluster",
                   "route53-recovery-control-config:DeleteControlPanel",
                   "route53-recovery-control-config:DeleteRoutingControl",
                   "route53-recovery-control-config:DeleteSafetyRule",
                   "route53-recovery-control-config:DescribeCluster",
                   "route53-recovery-control-config:DescribeControlPanel",
                   "route53-recovery-control-config:DescribeSafetyRule",
                   "route53-recovery-control-config:DescribeRoutingControl",
                   "route53-recovery-control-config:ListAssociatedRoute53HealthChecks",
                   "route53-recovery-control-config:ListClusters",
                   "route53-recovery-control-config:ListControlPanels",
                   "route53-recovery-control-config:ListRoutingControls",
                   "route53-recovery-control-config:ListSafetyRules",
                   "route53-recovery-control-config:UpdateControlPanel",
                   "route53-recovery-control-config:UpdateRoutingControl",
                   "route53-recovery-control-config:UpdateSafetyRule"
             ],
            "Resource": "*"
        },
                {
            "Effect": "Allow",
            "Action": [
                   "route53:GetHealthCheck",
                   "route53:CreateHealthCheck",
                   "route53:DeleteHealthCheck",
                   "route53:ChangeTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

------

##### Examples: ARC API actions for routing control configuration
<a name="security_iam_id-based-policy-examples-api-routing"></a>

To ensure that a user can use ARC API actions to work with ARC routing control configuration, attach a policy that corresponds to the API operations that the user needs to work with, as described below.

To work with API operations for recovery control configuration, attach a policy like the following to the user:

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
                   "route53-recovery-control-config:CreateCluster",
                   "route53-recovery-control-config:CreateControlPanel",
                   "route53-recovery-control-config:CreateRoutingControl",
                   "route53-recovery-control-config:CreateSafetyRule",
                   "route53-recovery-control-config:DeleteCluster",
                   "route53-recovery-control-config:DeleteControlPanel",
                   "route53-recovery-control-config:DeleteRoutingControl",
                   "route53-recovery-control-config:DeleteSafetyRule",
                   "route53-recovery-control-config:DescribeCluster",
                   "route53-recovery-control-config:DescribeControlPanel",
                   "route53-recovery-control-config:DescribeSafetyRule",
                   "route53-recovery-control-config:DescribeRoutingControl",
                   "route53-recovery-control-config:GetResourcePolicy",
                   "route53-recovery-control-config:ListAssociatedRoute53HealthChecks",
                   "route53-recovery-control-config:ListClusters",
                   "route53-recovery-control-config:ListControlPanels",
                   "route53-recovery-control-config:ListRoutingControls",
                   "route53-recovery-control-config:ListSafetyRules",
                   "route53-recovery-control-config:ListTagsForResource",
                   "route53-recovery-control-config:UpdateControlPanel",
                   "route53-recovery-control-config:UpdateRoutingControl",
                   "route53-recovery-control-config:UpdateSafetyRule",
                   "route53-recovery-control-config:TagResource",
                   "route53-recovery-control-config:UntagResource"
            ],
            "Resource": "*"
        }
    ]
}
```

------

To perform tasks in ARC routing control with the recovery cluster data plane API, for example, updating routing control states to fail over during a disaster event, you can attach a ARC IAM policy such as the following to your IAM user.

The `AllowSafetyRuleOverride` boolean gives permission to override safety rules that you've configured as safeguards for routing controls. This permission might be required in "break glass" scenarios to bypass the safeguards in disasters or other urgent failover scenarios. For example, an operator might need to fail over quickly for disaster recovery, and one or more safety rules might unexpectedly prevent a routing control state update required to reroute traffic. This permission allows the operator to specify safety rules to override when making API calls to update routing control states. For more information, see [Overriding safety rules to reroute traffic](#routing-control.override-safety-rule).

If you want to allow an operator to use the recovery cluster data plane API but *prevent* overriding safety rules, you can attach a policy such as the following, with `AllowSafetyRuleOverrides` boolean to `false`. To allow the operator to override safety rules, set the `AllowSafetyRuleOverrides` boolean to `true`.

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
                "route53-recovery-cluster:GetRoutingControlState",
                "route53-recovery-cluster:ListRoutingControls"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "route53-recovery-cluster:UpdateRoutingControlStates",
                "route53-recovery-cluster:UpdateRoutingControlState"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "route53-recovery-cluster:AllowSafetyRulesOverrides": "false"
                }
            }
        }
    ]
}
```

------

#### AWS managed policies for routing control in Amazon Application Recovery Controller (ARC)
<a name="security-iam-awsmanpol-routing"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

##### AWS managed policy: AmazonRoute53RecoveryControlConfigFullAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryControlConfigFullAccess"></a>

You can attach `AmazonRoute53RecoveryControlConfigFullAccess` to your IAM entities. This policy grants full access to actions for working with recovery control configuration in ARC. Attach it to IAM users and other principals who need full access to recovery control configuration actions.

At your discretion, you can add access to additional Amazon Route 53 actions to enable users to create health checks for routing controls. For example, you might allow permission for one or more of the following actions: `route53:GetHealthCheck`, `route53:CreateHealthCheck`, `route53:DeleteHealthCheck`, and `route53:ChangeTagsForResource`.

To view the permissions for this policy, see [AmazonRoute53RecoveryControlConfigFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigFullAccess.html) in the *AWS Managed Policy Reference*.

##### AWS managed policy: AmazonRoute53RecoveryControlConfigReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryControlConfigReadOnlyAccess"></a>

You can attach `AmazonRoute53RecoveryControlConfigReadOnlyAccess` to your IAM entities. It's useful for users who need to view routing control and safety rule configurations. This policy grants read-only access to actions for working with recovery control configuration in ARC. These users can't create, update, or delete recovery control resources.

To view the permissions for this policy, see [AmazonRoute53RecoveryControlConfigReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

##### AWS managed policy: AmazonRoute53RecoveryClusterFullAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryClusterFullAccess"></a>

You can attach `AmazonRoute53RecoveryClusterFullAccess` to your IAM entities. This policy grants full access to actions for working with the cluster data plane in ARC. Attach it to IAM users and other principals who need full access to updating and retrieving routing control states.

To view the permissions for this policy, see [AmazonRoute53RecoveryClusterFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterFullAccess.html) in the *AWS Managed Policy Reference*.

##### AWS managed policy: AmazonRoute53RecoveryClusterReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryClusterReadOnlyAccess"></a>

You can attach `AmazonRoute53RecoveryClusterReadOnlyAccess` to your IAM entities. This policy grants read-only access to the cluster data plane in ARC. These users can retrieve routing control states but can't update them.

To view the permissions for this policy, see [AmazonRoute53RecoveryClusterReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

##### AWS managed policy: AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy
<a name="security-iam-awsmanpol-AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy"></a>

You can attach `AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy` to your IAM entities. This policy grants permissions for ARC Region switch plan execution, plan evaluation, and service quota remediation. Attach it to IAM roles used for Region switch plan execution.

**Permissions details**

This policy includes the following permissions:
+ `arc-region-switch:GetPlan` – Allows principals to retrieve configuration details for a Region switch plan.
+ `arc-region-switch:GetPlanExecution` – Allows principals to retrieve information about a specific Region switch plan execution.
+ `arc-region-switch:ListPlanExecutions` – Allows principals to list all executions of Region switch plans.
+ `iam:SimulatePrincipalPolicy` – Allows principals to simulate and evaluate what actions an IAM role can perform. This permission is scoped to IAM roles only and is used during plan evaluation to verify that necessary permissions are in place before executing a Region switch plan.
+ `cloudwatch:DescribeAlarms` – Allows principals to retrieve information about Amazon CloudWatch alarms.
+ `cloudwatch:DescribeAlarmHistory` – Allows principals to retrieve historical state changes for Amazon CloudWatch alarms.
+ `cloudwatch:GetMetricStatistics` – Allows principals to retrieve statistical data for Amazon CloudWatch metrics.
+ `servicequotas:GetServiceQuota` – Allows principals to read the current value of a service quota to detect quotas that are out of sync between the Regions used by a Region switch plan.
+ `servicequotas:GetRequestedServiceQuotaChange` – Allows principals to read the status of a submitted service quota increase request.
+ `servicequotas:RequestServiceQuotaIncrease` – Allows principals to submit a service quota increase request. This keeps service quotas in sync across the Regions used by a Region switch plan.

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy.html) in the *AWS Managed Policy Reference Guide*.

##### Updates for AWS managed policies for routing control
<a name="security-iam-awsmanpol-routing-updates"></a>

For details about updates to AWS managed policies for routing control in ARC since this service began tracking these changes, see [Updates to AWS managed policies for Amazon Application Recovery Controller (ARC)](#security-iam-awsmanpol-arc-updates). For automatic alerts about changes to this page, subscribe to the RSS feed on the ARC [Document history page](#doc-history).

### Quotas for routing control
<a name="routing-control.quotas"></a>

Routing control in Amazon Application Recovery Controller (ARC) is subject to the following quotas (formerly referred to as limits).


| Entity | Quota | 
| --- | --- | 
| Number of clusters per account | 2 | 
| Number of control panels per cluster | 50 | 
| Number of routing controls per control panel | 100 | 
| Total number of routing controls (in all control panels) per cluster | 300 | 
| Number of safety rules per control panel | 20 | 
| Number of routing controls per [UpdateRoutingControlStates](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html) operation call | 10 | 
| Number of mutating API calls to a cluster endpoint, per second | 3 | 

## Readiness check in ARC
<a name="recovery-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

With readiness check in Amazon Application Recovery Controller (ARC), you can gain insights into whether your applications and resources are prepared for recovery. After you model your AWS application in ARC and create readiness checks, the checks continually monitor information about your application, such as AWS resource quotas, capacity, and network routing policies. Then, you can choose to be notified about changes that would affect your ability to fail over to a replica of your application, to recover from an event. Readiness checks help make sure, on an ongoing basis, that you can maintain your multi-Region applications in a state that is scaled and configured to handle failover traffic.

This chapter explains how to model your application in ARC to set up the structure that enables readiness checks to work, by creating a recovery group and cells that describe your application. Then, you can follow the steps to add readiness checks and readiness scopes so that ARC can audit readiness for your application. 

After you create readiness checks, you can monitor the readiness status of your resources. Readiness checks help you to ensure that a standby application replica and its resources match your production replica on an ongoing basis, reflecting the capacity, routing policies, and other configuration details of your production application. If the replica doesn't match, you can add capacity or change a configuration so that your application replicas are aligned again.

**Important**  
Readiness checks are most useful for verifying, on an ongoing basis, that application replica configurations and runtime states are aligned. Readiness checks shouldn't be used to indicate whether your production replica is healthy, nor should you rely on readiness checks as a primary trigger for failover during a disaster event.

### Set up a resilient recovery process for your application
<a name="getting-started-readiness"></a>

To use Amazon Application Recovery Controller (ARC) with AWS applications that are in multiple AWS Regions, there are guidelines to follow to set up your applications for resilience, so that you can support recovery readiness effectively. Then, you can create readiness checks for your application and set up routing controls to reroute traffic for failover. You can also review the recommendations ARC provides to about your application's architecture that can improve resiliency.

**Note**  
If you have an application that is siloed by Availability Zones, consider using zonal shift or zonal autoshift for failover recovery. No setup is required to use zonal shift or zonal autoshift to reliably recover applications from Availability Zone impairments.  
To move traffic away from an Availability Zone for load balancer resources, start a zonal shift in the ARC console or in the Elastic Load Balancing console. Or, you can use the AWS Command Line Interface or AWS SDK with zonal shift API actions. For more information, see [Zonal shift in ARC](#arc-zonal-shift).

To learn more about getting started with resilient failover configurations, see [Getting started with multi-Region recovery in Amazon Application Recovery Controller (ARC)](#getting-started).

### What is readiness check in Amazon Application Recovery Controller (ARC)?
<a name="readiness-what-is"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

A readiness check in ARC continually (at one-minute intervals) audits for mismatches in AWS provisioned capacity, service quotas, throttle limits, and configuration and version discrepancies for the resources included in the check. Readiness checks can notify you of these differences so that you can make sure that each replica has the same configuration setup and the same runtime state. Although readiness checks ensure that your configured capacities across replicas are consistent, you should not expect them to decide on your behalf what the capacity of your replica should be. For example, you should understand your application requirements so that you size your Auto Scaling groups with enough buffer capacity in each replica to manage if another cell is unavailable.

For quotas, when ARC detects a mismatch with a readiness check, it can take steps to align the quotas for the replicas by increasing the lower quota to match the higher quota. When the quotas match, the readiness check status shows `READY`. (Note that this isn't an immediate update process, and the total time depends on the specific resource type and other factors.) 

The first step is setting up readiness checks to create a [recovery group](#recovery-readiness.recovery-groups) that represents your application. Each recovery group includes *cells* for each individual failure-containment unit or *replica* of your application. Next, you create [resource sets](#recovery-readiness.recovery-groups.readiness-scope) for each resource type in your application, and associate *readiness checks* with the resource sets. Finally, you associate the resources with *readiness scopes*, so you can get readiness status about the resources in a recovery group (your application) or individual cells (replicas, which are Regions or Availability Zones (AZs)). 

Readiness (that is, `READY` or `NOT READY`) is based on the resources that are in the scope of the readiness check and the set of rules for a resource type. There are [sets of readiness rules](#recovery-readiness.list-rules) for each resource type, which ARC checks use to audit resources for readiness. Whether a resource is `READY` or not is based on how each readiness rule is defined. All readiness rules evaluate resources, but some compare resources to each other and some look at specific information about each resource in the resource set. 

By adding readiness checks, you can monitor readiness status, in one of several ways: with EventBridge, in the AWS Management Console, or by using ARC API actions. You can also monitor readiness status of resources in different contexts, including the readiness of cells and the readiness of your application. Use the [cross-account authorization](#recovery-readiness.cross-account) feature in ARC to make it easier to set up and monitor distributed resources from a single AWS account.

#### Monitoring application replicas with readiness checks
<a name="readiness-what-is.readiness-auditing"></a>

ARC audits your application replicas by using *readiness checks* to ensure that each one has the same configuration setup and the same runtime state. A readiness check continually audits AWS resource capacity, configuration, AWS quotas, and routing policies for an application, information that you can use to help make sure that replicas are ready for failover. Readiness checks help you to ensure that your recovery environment is scaled and configured to fail over to when needed.

The following sections provide more details about how readiness check works.

##### Readiness checks and your application replicas
<a name="readiness-what-is.readiness-auditing-details"></a>

To be prepared for recovery, you must maintain sufficient spare capacity in replicas at all times, to absorb failover traffic from another Availability Zone or Region. ARC continually (once a minute) inspects your application to ensure that your provisioned capacity matches across all Availability Zones or Regions.

The capacity that ARC inspects includes, for example, Amazon EC2 instance counts, Aurora read and write capacity units, and Amazon EBS volume size. If you scale up the capacity in your primary replica for resource values but forget to also increase the corresponding values in your standby replica, ARC detects the mismatch so that you can increase the values in the standby.

**Important**  
Readiness checks are most useful for verifying, on an ongoing basis, that application replica configurations and runtime states are aligned. Readiness checks shouldn't be used to indicate whether your production replica is healthy, nor should you rely on readiness checks as a primary trigger for failover during a disaster event.

In an active-standby configuration, you should make decisions about whether to fail away from or to a cell based on your monitoring and health check systems, and consider readiness checks as a complementary service to those systems. ARC readiness checks are not highly available, so you should not depend on the checks being accessible during an outage. In addition, the resources that are checked might also not be available during a disaster event. 

You can monitor the readiness status for your application's resources in specific cells (AWS Regions or Availability Zones) or for your overall application. You can be notified when a readiness check status changes, for example, to `Not ready`, by creating rules in EventBridge. For more information, see [Using readiness check in ARC with Amazon EventBridge](#eventbridge-readiness). You can also view readiness status in the AWS Management Console, or by using API operations, such as `get-recovery-readiness`. For more information, see [Readiness check API operations](#actions.readiness).

##### How readiness check works
<a name="readiness-what-is.readiness-how-it-works"></a>

ARC audits your application replicas by using *readiness checks* to ensure that each one has the same configuration setup and the same runtime state.

To be prepared for recovery, for example, you must maintain sufficient spare capacity at all times to absorb failover traffic from another Availability Zone or Region. ARC continually (once a minute) inspects your application to ensure that your provisioned capacity matches across all Availability Zones or Regions. The capacity that ARC inspects includes, for example, Amazon EC2 instance counts, Aurora read and write capacity units, and Amazon EBS volume size. If you scale up the capacity in your primary replica for resource values but forget to also increase the corresponding values in your standby replica, ARC detects the mismatch so that you can increase the values in the standby.

**Important**  
Readiness checks are most useful for verifying, on an ongoing basis, that application replica configurations and runtime states are aligned. Readiness checks shouldn't be used to indicate whether your production replica is healthy, nor should you rely on readiness checks as a primary trigger for failover during a disaster event.

In an active-standby configuration, you should make decisions about whether to fail away from or to a cell based on your monitoring and health check systems, and consider readiness checks as a complementary service to those systems. ARC readiness checks are not highly available, so you should not depend on the checks being accessible during an outage. In addition, the resources that are checked might also not be available during a disaster event. 

You can monitor the readiness status for your application's resources in specific cells (AWS Regions or Availability Zones) or for your overall application. You can be notified when a readiness check status changes, for example, to `Not ready`, by creating rules in EventBridge. For more information, see [Using readiness check in ARC with Amazon EventBridge](#eventbridge-readiness). You can also view readiness status in the AWS Management Console, or by using API operations, such as `get-recovery-readiness`. For more information, see [Readiness check API operations](#actions.readiness).

#### How readiness rules determine readiness status
<a name="recovery-readiness.rules"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

ARC readiness checks determine readiness status based on the predefined rules for each resource type and the way those rules are defined. ARC includes one group of rules for each type of resource that it supports. For example, ARC has groups of readiness rules for Amazon Aurora clusters, Auto Scaling groups, and so on. Some readiness rules compare resources in a set to each other, and some look at specific information about each resource in the resource set. 

You can't add, edit, or remove readiness rules, or groups of rules. However, you can create an Amazon CloudWatch alarm and create a readiness check to monitor the state of the alarm. For example, you can create a custom CloudWatch alarm to monitor Amazon EKS container services, and create a readiness check to audit the readiness status of the alarm.

You can view all the readiness rules for each resource type in the AWS Management Console when you create a resource set, or you can view the readiness rules later by navigating to the details page for a resource set. You can also view readiness rules in the following section: [Readiness rules in ARC](#recovery-readiness.list-rules).

When a readiness check audits a set of resources with a set of rules, the way each rule is defined determines whether the result will be `READY` or `NOT READY` for all the resources or if the result will be different for different resources. In addition, you can view readiness status in multiple ways. For example, you can view the readiness status of a group of resources in a resource set or view a summary of readiness status for a recovery group or a cell (that is, an AWS Region or Availability Zone, depending on how you've set up your recovery group).

The wording in each rule description explains how it evaluates the resources to determine the readiness status when that rule is applied. A rule is defined to inspect *each resource* or to inspect *all resources* in a resource set to determine readiness. Specifically, the rules work as follows: 
+ The rule inspects *each resource* in the resource set to ensure a condition. 
  + If all resources succeed, all resources are set as `READY`.
  + If one resource fails, that resource is set as `NOT READY`, and the other cells remain `READY`.

  For example: **MskClusterState:** Inspects each Amazon MSK cluster to ensure that it is in an `ACTIVE` state.
+ The rule inspects *all resources* in the resource set to ensure a condition. 
  + If the condition is ensured, all resources are set as `READY`.
  + If any fails to meet the condition, all resources are set as `NOT READY`.

  For example: **VpcSubnetCount:** Inspects all VPC subnets to ensure that they have the same number of subnets.
+ Non-critical rule: The rule inspects all resources in the resource set to ensure a condition. 
  + If any fails, the readiness status is unchanged. A rule with this behavior has a note in its description. 

  For example: **ElbV2CheckAzCount:** Inspects each Network Load Balancer to ensure that it is attached to only one Availability Zone. Note: This rule does not affect readiness status.

In addition, ARC takes an extra step for quotas. If a readiness check detects a mismatch across cells for service quotas (the maximum value for resource creation and operations) for any supported resource, ARC automatically raises the quota for the resource with the lower quota. This applies only to quotas (limits). For capacity, you should add additional capacity as required for your application needs.

You can also set up an Amazon EventBridge notification for readiness checks, for example, when any readiness check status changes to `NOT READY`. Then when a configuration mismatch is detected, EventBridge sends you a notification and you can take corrective action to make sure that your application replicas are aligned and prepared for recovery. For more information, see [Using readiness check in ARC with Amazon EventBridge](#eventbridge-readiness).

#### How readiness checks, resource sets, and readiness scopes work together
<a name="recovery-readiness.recovery-groups.readiness-scope"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

Readiness checks always audit groups of resources in *resource sets*. You create resource sets (separately, or while you're creating a readiness check) to group the resources that are in the cells (Availability Zones or AWS Regions) in your ARC recovery group, so that you can define readiness checks. A resource set is typically a group of same type of resources (like Network Load Balancers) but can also be DNS target resources, for architectural readiness checks.

You typically create one resource set and readiness check for each type of resource in your application. For an architectural readiness check, you create a top level DNS target resource and a global (recovery group level) resource set for it, and then create cell level DNS target resources, for a separate resource set.

The following diagram shows an example of a recovery group with three cells (Availability Zones), each with a Network Load Balancer (NLB) and Auto Scaling group (ASG).

![A sample recovery group for ARC. It has three cells (AZs), each with one NLB and one EC2 Auto Scaling group.](https://docs.aws.amazon.com/r53recovery/latest/dg/images/Sample3AZRecoveryGroup.png)


In this scenario, you would create a resource set and readiness check for the three Network Load Balancers, and a resource set and readiness check for the three Auto Scaling groups. Now you have a readiness check for each set of resources for your recovery group, by resource type. 

By creating *readiness scopes* for resources, you can add readiness check summaries for cells or recovery groups. To specify a readiness scope for a resource, you associate the ARN of the cell or recovery group with each resource in a resource set. You can do this when you're creating a readiness check for a resource set.

For example, when you add a readiness check for a resource set for the Network Load Balancers for this recovery group, you can add readiness scopes to each NLB at the same time. In this case, you would associate the ARN of AZ 1a to the NLB in AZ 1a, the ARN of `AZ 1b` to the NLB `AZ 1b`, and the ARN of `AZ 1c` to the NLB in `AZ 1c`. When you create a readiness check for the Auto Scaling groups, you would do the same, assigning readiness scopes to each of them when you create the readiness check for the Auto Scaling group resource set.

It’s optional to associate readiness scopes when you create a readiness check, however, we strongly recommend that you set them. Readiness scopes enable ARC to show the correct `READY` or `NOT READY` readiness status for recovery group summary readiness checks and cell level summary readiness checks. Unless you set readiness scopes, ARC can't provide these summaries.

Note that when you add an application-level or a global resource, such as a DNS routing policy, you don't choose a recovery group or cell for the readiness scope. Instead, you choose **global resource (no cell)**.

#### DNS target resource readiness checks: Auditing resiliency readiness
<a name="recovery-readiness.readiness-checks.architectural"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

With DNS target resource readiness checks in ARC, you can audit the architectural and resiliency readiness of your application. This type of readiness check continually scans your application's architecture and Amazon Route 53 routing policies to audit for cross-zone and cross-Region dependencies.

A recovery-oriented application has multiple replicas that are siloed into Availability Zones or AWS Regions, so that the replicas can fail independently of one another. If your application needs adjusting to be siloed correctly, ARC will suggest changes that you can make, if needed, to update your architecture to help ensure that it's resilient and ready for failover.

ARC automatically detects the number and the scope of cells (representing replicas, or failure-containment units) in your application, and whether the cells are siloed by Availability Zone or by Region. Then, ARC identifies and provides information to you about the application resources in the cells, to determine if they are correctly siloed to zones or Regions. For example, if you have cells that are scoped to specific zones, readiness checks can monitor if your load balancers and the targets behind them are also siloed to those zones.

With this information, you can determine if there are changes that you need to make to align resources in your cells to the correct zones or Regions.

To get started, you create DNS target resources for your application, and resource sets and readiness checks for them. For more information, see [Getting architecture recommendations in ARC](#recovery-readiness.evaluate-arch).

#### Readiness checks and disaster recovery scenarios
<a name="recovery-readiness.disaster"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

ARC readiness checks give you insights into whether your applications and resources are ready for recovery by helping you make sure that your applications are scaled to handle failover traffic. Readiness check statuses should not be used as a signal to indicate that a production replica is healthy. You can, however, use readiness checks as a supplement to your application and infrastructure monitoring or health checker systems to determine whether to fail away from or to a replica.

In an urgent situation or an outage, use a combination of health checks and other information to determine that your standby is scaled up, healthy, and ready for you to fail over production traffic. For example, check to see if canaries that run against your standby cell are meeting your success criteria, in addition to verifying that readiness check statuses for the standby are `READY`.

Be aware that ARC readiness checks are hosted in a single AWS Region, US West (Oregon), and during an outage or disaster, readiness check information could become stale or the checks could become unavailable. For more information, see [Data and control planes for routing control](#data-and-control-planes).

### AWS Region availability for readiness check
<a name="introduction-regions-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

For detailed information about Regional support and service endpoints for Amazon Application Recovery Controller (ARC), see [Amazon Application Recovery Controller (ARC) endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/r53arc.html) in the *Amazon Web Services General Reference*.

**Note**  
Readiness check in Amazon Application Recovery Controller (ARC) is a global feature. However, readiness check resources are in the US West (Oregon) Region, so you must specify the US West (Oregon) Region (specify the parameter `--region us-west-2`) in Regional ARC AWS CLI commands, for example, when you create resources such as resource sets and readiness checks.

### Readiness check components
<a name="introduction-components-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

The following diagram illustrates a sample recovery group that is configured to support the readiness check feature. Resources in this example are grouped into cells (by AWS Region) and nested cells (by Availability Zones) in a recovery group. There is an overall readiness status for the recovery group (application), as well as individual readiness statuses for each cell (Region) and nested cell (Availability Zone).

![A sample recovery group for ARC. It has two cells, by Region, and within each Region, there are 2 nested cells, by Availability Zone. The first Region cell has all ready statuses and the second Region cell has a not ready status because one of its zone cells is not ready. The recovery group is overall not ready.](https://docs.aws.amazon.com/r53recovery/latest/dg/images/GS_ReacoveryReadinessDiagram.png)


The following are components of the readiness check feature in ARC.

**Cell**  
A cell defines your application's replicas or independent units of failover. It groups all the AWS resources that are necessary for your application to run independently within the replica. For example, you might have one set of resources in a primary cell and another set in a standby cell. You determine the boundary of what a cell includes, but cells typically represent an Availability Zone or a Region. You can have multiple cells (nested cells) within a cell, such as AZs within a Region. Each nested cell represents an isolated unit of failover.

**Recovery group**  
Cells are collected into a recovery group. A recovery group represents an application or group of applications that you want to check failover readiness for. It consists of two or more cells, or replicas, that match each other in terms of functionality. For example, if you have a web application that is replicated across us-east-1a and us-east-1b, where us-east-1b is your failover environment, you can represent this application in ARC as a recovery group with two cells: one in us-east-1a and one in us-east-1b. A recovery group can also include a global resource, such as a Route 53 health check.

**Resources and resource identifiers**  
When you create components for readiness checks in ARC, you specify a resource, such as an Amazon DynamoDB table, a Network Load Balancer, or a DNS target resource, by using a resource identifier. A resource identifier is either the Amazon Resource Name (ARN) for the resource or, for a DNS target resource, the identifier that ARC generates when it creates the resource. 

**DNS target resource**  
A DNS target resource is the combination of your application's domain name and other DNS information, such as the AWS resource that the domain points to. Including an AWS resource is optional but if you provide it, it must be a Route 53 resource record or a Network Load Balancer. When you provide the AWS resource, you can get more detailed architectural recommendations that can help you improve your application's recovery resiliency. You can create resource sets in ARC for DNS target resources, and then create a readiness check for the resource set so that you can get architecture recommendations for your application. The readiness check also monitors the DNS routing policy for your application, based on the readiness rules for DNS target resources.

**Resource set**  
 A resource set is a set of resources, including AWS resources or DNS target resources, that span multiple cells. For example, you might have a load balancer in us-east-1a and another one in us-east-1b. To monitor the recovery readiness of the load balancers, you can create a resource set that includes both load balancers, and then create a readiness check for the resource set. ARC will continually check the readiness of the resources in the set. You can also add a readiness scope to associate resources in a resource set with the recovery group that you create for your application.

**Readiness rule**  
Readiness rules are audits that ARC performs against a set of resources in a resource set. ARC has a set of readiness rules for each type of resource that it supports readiness checks for. Each rule includes an ID and a description that explains what ARC inspects the resources for.

**Readiness check**  
A readiness check monitors a resource set in your application, such as a set of Amazon Aurora instances, that ARC is auditing recovery readiness for. Readiness checks can include auditing, for example, capacity configurations, AWS quotas, or routing policies. For example, if you want to audit readiness for your Amazon EC2 Auto Scaling groups across two Availability Zones, you can create a readiness check for a resource set with two resource ARNs, one for each Auto Scaling group. Then, to make sure that each group is scaled equally, ARC continually monitors the instance types and the counts in the two groups.

**Readiness scope**  
A readiness scope identifies the grouping of resources that a specific readiness check encompasses. The scope of a readiness check can be a recovery group (that is, global to the whole application) or a cell (that is, a Region or Availability Zone). For a resource that is a global resource for ARC, set the readiness scope at to recovery group or global resource level. For example, a Route 53 health check is a global resource in ARC because it isn't specific to a Region or Availability Zone.

### Data and control planes for readiness check
<a name="data-and-control-planes-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that you make sure that the mechanisms that you depend on during failover are highly available, so that you can use them when you need them in a disaster scenario. Typically, you should use data plane functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind, it's important to understand how the functionality of a service is divided between control planes and data planes, and when you can rely on an expectation of extreme reliability with a service's data plane.

As with most AWS services, the functionality for the readiness check capability is supported by control planes and data planes. While both of these are built to be reliable, a control plane is optimized for data consistency, while a data plane is optimized for availability. A data plane is designed for resilience so that it can maintain availability even during disruptive events, when a control plane might become unavailable.

In general, a *control plane* enables you to do basic management functions, such as create, update, and delete resources in the service. A *data plane* provides a service's core functionality. 

For readiness check, there is a single API, the [Recovery Readiness API](https://docs.aws.amazon.com/recovery-readiness/latest/api/what-is-recovery-readiness.html), for both the control plane and data plane. Readiness checks and readiness resources are only in the US West (Oregon) Region (us-west-2). *The readiness check control plane and data plane are reliable but not highly available.*

For more information about data planes, control planes, and how AWS builds services to meet high availability targets, see the [Static stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) in the Amazon Builders' Library.

### Tagging for readiness check in Amazon Application Recovery Controller (ARC)
<a name="introduction-tagging-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

Tags are words or phrases (meta data) that you use to identify and organize your AWS resources. You can add multiple tags to each resource, and each tag includes a key and a value that you define. For example, the key might be environment and the value might be production. You can search and filter your resources based on the tags you add.

You can tag the following resources in readiness check in ARC:
+ Resource sets
+ Readiness checks

Tagging in ARC is available only through the API, for example, by using the AWS CLI. 

The following are examples of tagging in readiness check by using the AWS CLI.

`aws route53-recovery-readiness --region us-west-2 create-resource-set --resource-set-name dynamodb_resource_set --resource-set-type AWS::DynamoDB::Table --resources ReadinessScopes=arn:aws:aws-recovery-readiness::111122223333:cell/PDXCell,ResourceArn=arn:aws:dynamodb:us-west-2:111122223333:table/PDX_Table ReadinessScopes=arn:aws:aws-recovery-readiness::111122223333:cell/IADCell,ResourceArn=arn:aws:dynamodb:us-east-1:111122223333:table/IAD_Table --tags Stage=Prod`

`aws route53-recovery-readiness --region us-west-2 create-readiness-check --readiness-check-name dynamodb_readiness_check --resource-set-name dynamodb_resource_set --tags Stage=Prod`

For more information, see [TagResource](https://docs.aws.amazon.com/recovery-readiness/latest/api/tags-resource-arn.html) in the *Recovery Readiness API Reference Guide* for Amazon Application Recovery Controller (ARC).

### Pricing for readiness check in ARC
<a name="introduction-pricing-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

You pay an hourly cost per readiness check that you configure.

For detailed pricing information for ARC and pricing examples, see [ARC Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

### Best practices for readiness check in ARC
<a name="route53-arc-best-practices.readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

We recommend the following best practice for readiness check in Amazon Application Recovery Controller (ARC).

**Add notifications for readiness status changes**

Set a rule in Amazon EventBridge to send a notification whenever a readiness check status changes, for example, from `READY` to `NOT READY`. When you receive a notification, you can investigate and address the issue, to make sure that your application and resources are ready for failover when you expect them to be.

You can set EventBridge rules to send notifications for several readiness check status changes, including for your recovery group (for your application), for a cell (such as an AWS Region), or for a readiness check for a resource set.

For more information, see [Using readiness check in ARC with Amazon EventBridge](#eventbridge-readiness).

### Readiness check API operations
<a name="actions.readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

The following table lists ARC operations that you can use for recovery readiness (readiness check), with links to relevant documentation.

For examples of how to use common recovery readiness API operations with the AWS Command Line Interface, see [Examples of using ARC readiness check API operations with the AWS CLI](#getting-started-cli-readiness).


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Create a cell | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [CreateCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html) | 
| Get a cell | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [GetCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html) | 
| Delete a cell | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [DeleteCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html) | 
| Update a cell | N/A | See [UpdateCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html) | 
| List cells for an account | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [ListCells](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html) | 
| Create a recovery group | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [CreateRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html) | 
| Get a recovery group | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [GetRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html) | 
| Update a recovery group | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [UpdateRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html) | 
| Delete a recovery group | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [DeleteRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html) | 
| List recovery groups | See [Creating, updating, and deleting recovery groups in ARC](#recovery-readiness.recovery-groups) | See [ListRecoveryGroups](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html) | 
| Create a resource set | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [CreateResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html) | 
| Get a resource set | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [GetResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html) | 
| Update a resource set | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [UpdateResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html) | 
| Delete a resource set | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [DeleteResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html) | 
| List resource sets | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [ListResourceSets](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html) | 
| Create a readiness check | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [CreateReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html) | 
| Get a readiness check | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [GetReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html) | 
| Update a readiness check | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [UpdateReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html) | 
| Delete a readiness check | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [DeleteReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html) | 
| List readiness checks | See [Creating and updating readiness checks in ARC](#recovery-readiness.create-readiness-check-or-set) | See [ListReadinessChecks](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html) | 
| List readiness rules | See [Readiness rules descriptions in ARC](#recovery-readiness.rules-resources) | See [ListRules](https://docs.aws.amazon.com/recovery-readiness/latest/api/rules.html) | 
| Check status of an entire readiness check | See [Monitoring readiness status in ARC](#recovery-readiness.status) | See [GetReadinessCheckStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-status.html) | 
| Check status of a resource | See [Monitoring readiness status in ARC](#recovery-readiness.status) | See [GetReadinessCheckResourceStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-resource-resourceidentifier-status.html) | 
| Check status of a cell | See [Monitoring readiness status in ARC](#recovery-readiness.status) | See [GetCellReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/cellreadiness-cellname.html) | 
| Check status of a recovery group | See [Monitoring readiness status in ARC](#recovery-readiness.status) | See [GetRecoveryGroupReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroupreadiness-recoverygroupname.html) | 

### Examples of using ARC readiness check API operations with the AWS CLI
<a name="getting-started-cli-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

This section walks through simple application examples, using the AWS Command Line Interface to work with readiness check features in Amazon Application Recovery Controller (ARC) using API operations. The examples are intended to help you develop a basic understanding of how to work with readiness check capabilities using the CLI.

Readiness check in ARC audits for mismatches for the resources in your application replicas. To set up readiness checks for your application, you must set up—or model—your application resources in ARC *cells* that align with the replicas that you've created for your application. You then set up readiness checks that audit these replicas, to help you make sure that your standby application replica and its resources match your production replica, on an ongoing basis

Let’s look at a simple case where you have an application named Simple-Service that currently runs in the US East (N. Virginia) Region (us-east-1). You also have a standby copy of the application in the US West (Oregon) Region (us-west-2). In this example, we'll configure readiness checks to compare these two versions of the application. This lets us ensure that the standby, US West (Oregon) Region, is ready to receive traffic, if it needs to in a failover scenario.

For more information about using the AWS CLI, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/route53-recovery-readiness/index.html). For a list of readiness API actions and links to more information, see [Readiness check API operations](#actions.readiness).

*Cells* in ARC represent fault boundaries (like Availability Zones or Regions) and are collected into *recovery groups*. A recovery group represents an application that you want to check failover readiness for. For more information about the components of readiness check, see [Readiness check components](#introduction-components-readiness).

**Note**  
ARC is a global service that supports endpoints in multiple AWS Regions but you must specify the US West (Oregon) Region (that is, specify the parameter `--region us-west-2`) in most ARC CLI commands. For example, to create resources such as recovery groups or readiness checks. 

For our application example, we'll start by creating one cell for each Region where we have resources. Then we'll create a recovery group, and then complete the setup for a readiness check.

#### 1. Create cells
<a name="getting-started-cli-readiness.cell"></a>

1a. Create a us-east-1 cell.

```
aws route53-recovery-readiness --region us-west-2 create-cell \
				--cell-name east-cell
```

```
{
    "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell",
    "CellName": "east-cell",
    "Cells": [],
    "ParentReadinessScopes": [],
    "Tags": {}
}
```

1b. Create a us-west-1 cell.

```
aws route53-recovery-readiness --region us-west-2 create-cell \
				--cell-name west-cell
```

```
{
    "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell",
    "CellName": "west-cell",
    "Cells": [],
    "ParentReadinessScopes": [],
    "Tags": {}
}
```

1c. Now we have two cells. You can verify that they exist by calling the `list-cells` API.

```
aws route53-recovery-readiness --region us-west-2 list-cells
```

```
{
    "Cells": [
        {
            "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell",
            "CellName": "east-cell",
            "Cells": [],
            "ParentReadinessScopes": [],
            "Tags": {}
        },
        {
            "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell",
            "CellName": "west-cell"
            "Cells": [],
            "ParentReadinessScopes": [],
            "Tags": {}
        }
    ]
}
```

#### 2. Create a recovery group
<a name="getting-started-cli-readiness.recovery"></a>

Recovery groups are the top-level resource for recovery readiness in ARC. A recovery group represents an application as a whole. In this step, we'll create a recovery group to model an overall application, and then add the two cells that we created.

2a. Create a recovery group.

```
aws route53-recovery-readiness --region us-west-2 create-recovery-group \
				--recovery-group-name simple-service-recovery-group \
			    --cells "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"\
			    "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
```

```
{
    "Cells": [],
    "RecoveryGroupArn": "arn:aws:route53-recovery-readiness::111122223333:recovery-group/simple-service-recovery-group",
    "RecoveryGroupName": "simple-service-recovery-group",
    "Tags": {}
}
```

2b. (Optional) You can verify that your recovery group was created correctly by calling the `list-recovery-groups `API.

```
aws route53-recovery-readiness --region us-west-2 list-recovery-groups
```

```
{
    "RecoveryGroups": [
        {
            "Cells": [
                "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell",
                "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
            ],
            "RecoveryGroupArn": "arn:aws:route53-recovery-readiness::111122223333:recovery-group/simple-service-recovery-group",
            "RecoveryGroupName": "simple-service-recovery-group",
            "Tags": {}
        }
    ]
}
```

Now that we have a model for our application, let’s add the resources to be monitored. In ARC, a group of resources that you want to monitor is called a resource set. Resource sets contain resources that are all of the same type. We compare the resources in a resource set to each other to help determine a cell's readiness for failover.

#### 3. Create a resource set
<a name="getting-started-cli-readiness.resource"></a>

Let’s assume our Simple-Service application is indeed very simple and only uses DynamoDB tables. It has a DynamoDB table in us-east-1 and another one in us-west-2. A resource set also contains a readiness scope, which identifies the cell that each resource is contained in. 

3a. Create a resource set that reflects our Simple-Service application's resources.

```
aws route53-recovery-readiness --region us-west-2 create-resource-set \
				--resource-set-name ImportantInformationTables \
				--resource-set-type AWS::DynamoDB::Table \
				--resources
				ResourceArn="arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2",ReadinessScopes="arn:aws:route53-recovery-readiness::111122223333:cell/west-cell" 
				ResourceArn="arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1",ReadinessScopes="arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"
```

```
{
    "ResourceSetArn": "arn:aws:route53-recovery-readiness::111122223333:resource-set/sample-resource-set",
    "ResourceSetName": "ImportantInformationTables",
    "Resources": [
        {
            "ReadinessScopes": [
                "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
            ],
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
        },
        {
            "ReadinessScopes": [
                "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"
            ],
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1"
        }
    ],
    "Tags": {}
}
```

3b. (Optional) You can verify what's included in the resource set by calling the `list-resource-sets` API. This lists all the resource sets for an AWS account. Here you can see that we have just the one resource set that we created above.

```
aws route53-recovery-readiness --region us-west-2 list-resource-sets
```

```
{
    "ResourceSets": [
        {
            "ResourceSetArn": "arn:aws:route53-recovery-readiness::111122223333:resource-set/ImportantInformationTables",
            "ResourceSetName": "ImportantInformationTables",
            "Resources": [
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
                },
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1"
                }
            ],
            "Tags": {}
        }
    ]
}{
    "ResourceSets": [
        {
            "ResourceSetArn": "arn:aws:route53-recovery-readiness::111122223333:resource-set/ImportantInformationTables",
            "ResourceSetName": "ImportantInformationTables",
            "Resources": [
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
                },
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::&ExampleAWSAccountNo1;:cell/east-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1"
                }
            ],
            "Tags": {}
        }
    ]
}
```

Now we’ve created the cells, recovery group, and resource set to model the Simple-Service application in ARC. Next, we'll set up readiness checks to monitor the readiness of the resources for fail over.

#### 4. Create a readiness check
<a name="getting-started-cli-readiness.check"></a>

A readiness check applies a set of rules to each resource in the resource set that is attached to the check. Rules are specific to each resource type. That is, there are different rules for `AWS::DynamoDB::Table`, `AWS::EC2::Instance`, and so on. Rules check a variety of dimensions for a resource, including configuration, capacity (where available and applicable), limits (where available and applicable), and routing configurations.

**Note**  
To see the rules that are applied to a resource in a readiness check, you can use the `get-readiness-check-resource-status` API, as described in step 5. To see a list of all the readiness rules in ARC, use `list-rules` or see [Readiness rules descriptions in ARC](#recovery-readiness.rules-resources). ARC has a specific set of rules that it runs for each resource type; they're not customizable at this time. 

4a. Create a readiness check for the resource set, ImportantInformationTables.

```
aws route53-recovery-readiness --region us-west-2 create-readiness-check \
				--readiness-check-name ImportantInformationTableCheck --resource-set-name ImportantInformationTables
```

```
{
    "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::111122223333:readiness-check/ImportantInformationTableCheck",
    "ReadinessCheckName": "ImportantInformationTableCheck",
    "ResourceSet": "ImportantInformationTables",
    "Tags": {}
}
```

4b. (Optional) To verify that the readiness check was created successfully, run the `list-readiness-checks` API. This API shows all the readiness checks in an account.

```
aws route53-recovery-readiness --region us-west-2 list-readiness-checks
```

```
{
    "ReadinessChecks": [
        {
            "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::111122223333:readiness-check/ImportantInformationTableCheck",
            "ReadinessCheckName": "ImportantInformationTableCheck",
            "ResourceSet": "ImportantInformationTables",
            "Tags": {}
        }
    ]
}
```

#### 5. Monitor readiness checks
<a name="getting-started-cli-readiness.monitor"></a>

Now that we’ve modeled the application and added a readiness check, we’re ready to monitor resources. You can model the readiness of your application at four levels: the readiness check level (a group of resources), the individual resource level, the cell level (all the resources in an Availability Zone or Region), and the recovery group level (the application as a whole). Commands for getting each of these types of readiness statuses are provided below.

5a. See the status of your readiness check.

```
aws route53-recovery-readiness --region us-west-2 get-readiness-check-status\
				--readiness-check-name ImportantInformationTableCheck
```

```
{
    "Readiness": "READY",
    "Resources": [
        {
            "LastCheckedTimestamp": "2021-01-07T00:53:39Z",
            "Readiness": "READY",
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:53:39Z",
            "Readiness": "READY",
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast2"
    ]
}
```

5b. See the detailed readiness status of a single resource in a readiness check, including the status of each rule that is checked.

```
aws route53-recovery-readiness --region us-west-2 get-readiness-check-resource-status \
				--readiness-check-name ImportantInformationTableCheck \ 
				--resource-identifier "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
```

```
{"Readiness": "READY",
    "Rules": [
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoTableStatus"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoCapacity"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoPeakRcuWcu"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsPeakRcuWcu"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsConfig"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsStatus"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsCapacity"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoReplicationLatency"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoAutoScalingConfiguration"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoLimits"
        }
    ]
}
```

5c. See the overall readiness for a cell.

```
aws route53-recovery-readiness --region us-west-2 get-cell-readiness-summary \
				--cell-name west-cell
```

```
{
    "Readiness": "READY",
    "ReadinessChecks": [
        {
            "Readiness": "READY",
            "ReadinessCheckName": "ImportantTableCheck"
        }
    ]
}
```

5d. Finally, see the top-level readiness of your application, at the recovery group level.

```
aws route53-recovery-readiness --region us-west-2 get-recovery-group-readiness-summary \
				--recovery-group-name simple-service-recovery-group
```

```
{
    "Readiness": "READY",
    "ReadinessChecks": [
        {
            "Readiness": "READY",
            "ReadinessCheckName": "ImportantTableCheck"
        }
    ]
}
```

### Working with recovery groups and readiness checks
<a name="recovery-readiness.recovery-groups-and-readiness-checks"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

This section describes and provides procedures for recovery groups and readiness checks, including creating, updating, and deleting these resources.

#### Creating, updating, and deleting recovery groups in ARC
<a name="recovery-readiness.recovery-groups"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

A recovery group represents your application in Amazon Application Recovery Controller (ARC). It typically consists of two or more *cells* that are replicas of each other in terms of resources and functionality, so that you can fail over from one to the other. Each cell includes the Amazon Resource Names (ARNs) for the active resources for one AWS Region or Availability Zone. The resources might be an Elastic Load Balancing load balancer, an Auto Scaling group, or other resources. A corresponding cell representing another zone or Region has standby resources of the same type that are in your active cell – a load balancer, Auto Scaling group, and so on.

A cell represents replicas of your application. Readiness checks in ARC help you determine if your application is ready to fail over from one replica to another. However, you should make decisions about whether to fail away from or to a replica based on your monitoring and health check systems, and consider readiness checks as a complementary service to those systems. 

Readiness checks audit resources to determine their readiness based on a set of pre-defined rules for that type of resource. After you create your recovery group with the replicas, you add ARC readiness checks for the resources in your application, so ARC can help make sure that the replicas have the same setup and configuration over time. 

**Topics**
+ [Creating recovery groups](#recovery-readiness.recovery-groups.create)
+ [Updating and deleting recovery groups and cells](#recovery-readiness.recovery-groups.edit-delete)

##### Creating recovery groups
<a name="recovery-readiness.recovery-groups.create"></a>

The steps in this section explain how to create a recovery group on the ARC console. To learn about using recovery readiness API operations with Amazon Application Recovery Controller (ARC), see [Readiness check API operations](#actions.readiness).

##### To create a recovery group


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. On the **Recovery readiness** page, choose **Create**, and then choose a **Recovery group**.

1. Enter a name for your recovery group, and then choose **Next**.

1. Choose **Create cells**, and then choose **Add cell**.

1. Enter a name for the cell. For example, if you have an application replica in US West (N. California), you could add a cell named `MyApp-us-west-1`. 

1. Choose **Add cell**, and add a name for a second cell. For example, if you have a replica in US East (Ohio), you could add a cell named` MyApp-us-east-2`.

1. If you want to add nested cells (replicas in Availability Zones within Regions), choose **Action**, choose **Add nested cell**, and then enter a name.

1. When you've added all of the cells and nested cells for your application replicas, choose **Next**. 

1. Review your recovery group, and then choose **Create recovery group**.

##### Updating and deleting recovery groups and cells
<a name="recovery-readiness.recovery-groups.edit-delete"></a>

The steps in this section explain how to update and delete a recovery group, and delete a cell on the ARC console. To learn about using recovery readiness API operations with Amazon Application Recovery Controller (ARC), see [Readiness check API operations](#actions.readiness).

##### To update or delete a recovery group, or delete a cell


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. On the **Recovery readiness** page, choose a recovery group.

1. To work with a recovery group, choose **Action**, and then choose **Edit recovery group** or **Delete recovery group**.

1. When you edit a recovery group, you can add or remove cells or nested cells. 
   + To add a cell, choose **Add cell**.
   + To remove a cell, under the **Action** label next to the cell, choose **Delete cell**.

#### Creating and updating readiness checks in ARC
<a name="recovery-readiness.create-readiness-check-or-set"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

This section provides procedures for readiness checks and resource sets, including creating, updating, and deleting these resources.

##### Creating and updating a readiness check
<a name="recovery-readiness.readiness-checks.create"></a>

The steps in this section explain how to create a readiness check on the ARC console. To learn about using recovery readiness API operations with Amazon Application Recovery Controller (ARC), see [Readiness check API operations](#actions.readiness).

To update a readiness check, you can edit the resource set for the readiness check, to add or remove resources or to change the readiness scope for a resource. 

##### To create a readiness check


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. On the **Readiness** page, choose **Create**, and then choose a **Readiness check**.

1. Enter a name for your readiness check, choose the resource type that you want to check, and then choose **Next**.

1. Add a resource set for your readiness check. A resource set is a group of resources of the same type in different replicas. Choose one of the following:
   + Create a readiness check with resources in a resource set that you've already created.
   + Create a new resource set.

   If you choose to create a new resource set, enter a name for it and choose **Add**. 

1. Copy and paste Amazon Resource Names (ARNs) one by one for each resource that you want to include in the set, and then choose **Next**.
**Tip**  
For examples and more information about the ARN format that ARC expects for each resource type, see [Resource types and ARN formats in ARC](#recovery-readiness.resource-types-arns).

1. If you like, view the readiness rules that will be used when ARC checks the type of resource you included in this readiness check. Then choose **Next**.

1. (Optional) Under **Recovery group name**, choose a recovery group to associate the readiness check with and then, for each resource ARN, choose a cell (Region or Availability Zone) from the drop-down menu that the resource is in. If it's an application-level resource, like a DNS routing policy, choose **global resource (no cell)**.

   *This specifies the readiness scopes for the resources in the readiness check.*
**Important**  
Although this step is optional, readiness scopes must be added to get summary readiness information for your recovery group and cells. If you skip this step and don't associate the readiness check with your recovery group's resources by choosing readiness scopes here, ARC cannot return summary readiness information for the recovery group or cells.

1. Choose **Next**.

1. Review the information on the confirmation page, and then choose **Create readiness check**.

##### To delete a readiness check


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. Choose a readiness check, and under **Actions**, choose **Delete**.

##### Creating and editing resource sets
<a name="recovery-readiness.resource-set.create"></a>

Typically, you create a resource set as part of creating a readiness check, but you can create a resource set separately as well. You can also edit a resource set to add or remove resources. The steps in this section explain how to create or edit a resource set on the ARC console. To learn about using recovery readiness API operations with Amazon Application Recovery Controller (ARC), see [Readiness check API operations](#actions.readiness).

##### To create a resource set


1. Open the Route 53 console at [ https://console.aws.amazon.com/route53recovery/home](https://console.aws.amazon.com/route53recovery/home). 

1. Under **Application Recovery Controller**, choose **Resource sets**.

1. Choose **Create**.

1. Enter a name for the resource set, and then choose the type of resource to include in the set.

1. Choose **Add**, and then enter the Amazon Resource Name (ARN) for the resource to add to the set.

1. After you've finished adding resources, choose **Create resource set**.

##### To edit a resource set


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. Under **Resource sets**, choose **Action**, and then choose **Edit**.

1. Do one of the following:
   + To remove a resource from the set, choose **Remove**.
   + To add a resource to the set, choose **Add**, and then enter the Amazon Resource Name (ARN) for the resource.

1. You can also edit the readiness scope for the resource, to associate the resource with a different cell for the readiness check.

1. Choose **Save**.

### Monitoring readiness status in ARC
<a name="recovery-readiness.status"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

You can see readiness for your application in Amazon Application Recovery Controller (ARC) at the following levels:
+ The readiness check level for the resources in a resource set
+ The individual resource level
+ The cell (application replica) level for all the resources in an Availability Zone or AWS Region
+ The recovery group level for the application as a whole

You can be notified about readiness status changes, or you can monitor readiness status changes in the Route 53 console or by using ARC CLI commands.

#### Readiness status notification
<a name="recovery-readiness.status-alert"></a>

You can use Amazon EventBridge to set up event-driven rules to monitor ARC resources and notify you about changes in readiness status. For more information, see [Using readiness check in ARC with Amazon EventBridge](#eventbridge-readiness).

#### Monitoring readiness status in the ARC console
<a name="recovery-readiness.status-console"></a>

The following procedure describes how to monitor recovery readiness in the AWS Management Console.

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. On the **Readiness** page, under **Recovery group**, view the **Recovery group readiness status** for each recovery group (application).

   You can also view the readiness of specific cells or individual resources.

#### Monitoring readiness status by using CLI commands
<a name="recovery-readiness.status-cli"></a>

This section provides examples of AWS CLI commands to use to see the readiness status for your application and resources at different levels.

**Readiness for a resource set**  
The status of a readiness check you've created for a resource set (a group of resources).  
`aws route53-recovery-readiness --region us-west-2 get-readiness-check-status --readiness-check-name {{ReadinessCheckName}} `

**Readiness for a single resource**  
To get the status of a single resource in a readiness check, including the status of each readiness rule that is checked, specify the readiness check name and a resource ARN. For example:  
`aws route53-recovery-readiness --region us-west-2 get-readiness-check-status --readiness-check-name {{ReadinessCheckName}} --resource-arn "arn:aws:dynamodb:us-west-2:111122223333:table/{{TableName}}"`

**Readiness for a cell**  
The status of a single cell, that is, a Region or Availability Zone.  
`aws route53-recovery-readiness --region us-west-2 get-cell-readiness-summary --cell-name {{CellName}} `

**Readiness for an application**  
The status of the overall application, at the recovery group level.  
`aws route53-recovery-readiness --region us-west-2 get-recovery-group-readiness-summary --recovery-group-name {{RecoveryGroupName}} `

### Getting architecture recommendations in ARC
<a name="recovery-readiness.evaluate-arch"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

If you have an existing application, Amazon Application Recovery Controller (ARC) can evaluate the architecture of your application and routing policies to provide recommendations for modifying the design to improve your application's recovery resiliency. After you create a recovery group in ARC that represents your application, follow the steps in this section to get recommendations for your application's architecture.

We recommend that you specify a target resource for the DNS target resource for your recovery group, if you haven't specified one yet, so that we can provide more detailed recommendations. When you provide additional information, ARC can provide better recommendations for you. For example, if you enter an Amazon Route 53 resource record or a Network Load Balancer as a target resource, ARC can provide information about whether you've created the optimal number of cells for your recovery group.

Note the following for DNS target resources:
+ Specify only a Route 53 resource record or Network Load Balancer for a target resource.
+ Create only one DNS target resource for each recovery group.
+ Recommended: Create one DNS target resource for each cell.
+ Group the DNS target resources into one resource set with a readiness check.

The following procedure explains how to create DNS target resources and get architecture recommendations for your application.

### To get recommendations for updating your architecture


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. Under **Recovery group name**, choose the recovery group that represents your application.

1. On the **Recovery group details** page, on the **Action** menu, choose **Get architecture recommendations for this recovery group**.

1. If you haven't created a DNS target resource readiness check yet, create one so that ARC can provide architecture recommendations. Choose **Create a DNS target resource**.

   For more information about DNS target resources, see [Readiness check components](#introduction-components-readiness).

1. To create a resource set for a DNS target resource, you create a readiness check. Enter a name for the readiness check, and then, for the type of readiness check, choose **DNS target resource**.

1. Enter a name for the resource set.

1. Enter the attributes for your application, including the DNS name, hosted zone ARN, and record set ID.
**Tip**  
To see the format for a hosted zone ARN, see **ARN format for hosted zone** in [Resource types and ARN formats in ARC](#recovery-readiness.resource-types-arns).

   Optionally, but strongly recommended, choose **Add optional attribute** and provide a Network Load Balancer ARN or your domain's Route 53 resource record.

1. (Optional) In **Recovery group configuration**, choose a cell for your DNS target resource, to set the readiness scope.

1. Choose **Create resource set**.

1. On the **Recovery group** details page, choose **Get architecture recommendations**. ARC displays a set of recommendations on the page.

Review the list of recommendations. Then you can decide whether and how to make changes to improve your app's recovery resilience.

### Creating cross-account authorizations in ARC
<a name="recovery-readiness.cross-account"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

You might have your resources distributed across multiple AWS accounts, which can make it challenging to get a comprehensive view of your application’s health. It can also make it hard to get the information required to make quick decisions. To help streamline this for readiness check in Amazon Application Recovery Controller (ARC), you can use *cross-account authorization*. 

Cross-account authorization in ARC works with the readiness check feature. With cross-account authorization, you can use one central AWS account to monitor your resources that are located in multiple AWS accounts. In each account that has resources that you want to monitor, you authorize the central account to have access to those resources. Then the central account can create readiness checks for the resources in all the accounts and from the central account, you can monitor readiness for failover.

**Note**  
Cross-account authorization setup isn't available in the console. Instead, use ARC API operations to set up and work with cross-account authorization. To help you get started, this section provides AWS CLI command examples. 

Let’s say that an application has an account that has resources in the US West (Oregon) Region (us-west-2), and there's also an account that has resources that you'd like to monitor in the US East (N. Virginia) Region (us-east-1). ARC can allow access for you to monitor both sets of resources from one account, us-west-2, by using cross-account authorization.

For example, let's say that you have the following AWS accounts:
+ US-West account: 999999999999
+ US-East account: 111111111111

In the us-east-1 account (111111111111), we can enable cross-account authorization to allow access by the us-west-2 account (999999999999) by specifying the Amazon Resource Name (ARN) for the (root) user in the us-west-2 IAM account: `arn:aws:iam::999999999999:root`. After we create the authorization, the us-west-2 account can add resources owned by us-east-1 to resource sets and create readiness checks to run on the resource sets.

The following example illustrates setting up cross-account authorization for one account. You must enable cross-account authorization in each additional account that has AWS resources that you want to add and monitor in ARC. 

**Note**  
ARC is a global service that supports endpoints in multiple AWS Regions but you must specify the US West (Oregon) Region (that is, specify the parameter `--region us-west-2`) in most ARC CLI commands.

The following AWS CLI command shows how to set up cross-account authorization for this example:

```
aws route53-recovery-readiness --region us-west-2 --profile {{profile-in-us-east-1-account}} \
				create-cross-account-authorization --cross-account-authorization arn:aws:iam::999999999999:root
```

To disable this authorization, do the following:

```
aws route53-recovery-readiness --region us-west-2 --profile {{profile-in-us-east-1-account}} \
				delete-cross-account-authorization --cross-account-authorization arn:aws:iam::999999999999:root
```

To check in a specific account for all the accounts that you've provided cross-account authorization for, use the `list-cross-account-authorizations` command. Note that at this time, you can't check in the other direction. That is, there isn't an API operation that you can use with an account profile to list all of the accounts for which it has been granted cross-account authorization to add and monitor resources.

```
aws route53-recovery-readiness --region us-west-2 --profile {{profile-in-us-east-1-account}} \
				list-cross-account-authorizations
```

```
{
    "CrossAccountAuthorizations": [
        "arn:aws:iam::999999999999:root"
    ]
}
```

### Readiness rules, resource types, and ARNS
<a name="recovery-readiness.rules-and-resource-types"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

This section includes reference information about the readiness rules descriptions, and supported resource types and the format for Amazon Resource Names (ARNs) that you use for resource sets.

#### Readiness rules descriptions in ARC
<a name="recovery-readiness.rules-resources"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

This section lists the readiness rules descriptions for all the types of resources supported by Amazon Application Recovery Controller (ARC). To see a list of the resource types supported by ARC, see [Resource types and ARN formats in ARC](#recovery-readiness.resource-types-arns).

You can also view the readiness rules descriptions on the ARC console or by using an API operation, by doing the following:
+ To view readiness rules in the console, follow the steps in the following procedure: [View readiness rules on the console](#recovery-readiness.list-rules-console).
+ To view readiness rules by using the API, see the [ListRules](https://docs.aws.amazon.com/recovery-readiness/latest/api/rules.html) operation.

**Topics**
+ [Readiness rules in ARC](#recovery-readiness.list-rules)
+ [View readiness rules on the console](#recovery-readiness.list-rules-console)

##### Readiness rules in ARC
<a name="recovery-readiness.list-rules"></a>

This section lists the set of readiness rules for each resource type that is supported by ARC. 

As you look through the rule descriptions, you can see that most of them include the terms **Inspects all** or **Inspects each**. To understand how these terms explain how a rule works in the context of a readiness check, and other details about how ARC sets readiness status, see [How readiness rules determine readiness status](#recovery-readiness.rules).

###### Readiness rules
<a name="recovery-readiness.list-rules-all"></a>

ARC audits resources by using the following readiness rules.

**Amazon API Gateway Version 1 stages**  
+ **ApiGwV1ApiKeyCount**: Inspects all API Gateway stages to ensure that they have the same number of API Keys linked to them.
+ **ApiGwV1ApiKeySource**: Inspects all API Gateway stages to ensure that they have the same value for `API Key Source`.
+ **ApiGwV1BasePath**: Inspects all API Gateway stages to ensure that they are linked to the same base path.
+ **ApiGwV1BinaryMediaTypes**: Inspects all API Gateway stages to ensure that they support the same binary media types.
+ **ApiGwV1CacheClusterEnabled**: Inspects all API Gateway stages to ensure that either all have `Cache Cluster` enabled, or none do.
+ **ApiGwV1CacheClusterSize**: Inspects all API Gateway stages to ensure that they have the same `Cache Cluster Size`. If one has a greater value, the others are marked NOT READY.
+ **ApiGwV1CacheClusterStatus**: Inspects all API Gateway stages to ensure that the `Cache Cluster` is in the AVAILABLE state.
+ **ApiGwV1DisableExecuteApiEndpoint**: Inspects all API Gateway stages to ensure that either all have `Execute API Endpoint` disabled, or none do.
+ **ApiGwV1DomainName**: Inspects all API Gateway stages to ensure that they are linked to the same domain name.
+ **ApiGwV1EndpointConfiguration**: Inspects all API Gateway stages to ensure that they are linked to a domain with the same endpoint configuration.
+ **ApiGwV1EndpointDomainNameStatus**: Inspects all API Gateway stages to ensure that the domain name that they are linked to is in the AVAILABLE state.
+ **ApiGwV1MethodSettings**: Inspects all API Gateway stages to ensure that they have the same value for `Method Settings`.
+ **ApiGwV1MutualTlsAuthentication**: Inspects all API Gateway stages to ensure that they have the same value for `Mutual TLS Authentication`.
+ **ApiGwV1Policy**: Inspects all API Gateway stages to ensure that either all use API level policies, or none do.
+ **ApiGwV1RegionalDomainName**: Inspects all API Gateway stages to ensure that they are linked to the same Regional domain name. Note: This rule does not affect readiness status.
+ **ApiGwV1ResourceMethodConfigs**: Inspects all API Gateway stages to ensure that they have a similar resource hierarchy, including the related configurations.
+ **ApiGwV1SecurityPolicy**: Inspects all API Gateway stages to ensure that they have the same value for `Security Policy`.
+ **ApiGwV1Quotas**: Inspects all API Gateway groups to ensure that they conform to quotas (limits) that are managed by Service Quotas.
+ **ApiGwV1UsagePlans**: Inspects all API Gateway stages to ensure that they are linked to `Usage Plans` with the same configuration.

**Amazon API Gateway Version 2 stages**  
+ **ApiGwV2ApiKeySelectionExpression**: Inspects all API Gateway stages ensure that they have the same value for `API Key Selection Expression`.
+ **ApiGwV2ApiMappingSelectionExpression**: Inspects all API Gateway stages to ensure that they have the same value for `API Mapping Selection Expression`.
+ **ApiGwV2CorsConfiguration**: Inspects all API Gateway stages to ensure that they have the same CORS related configuration.
+ **ApiGwV2DomainName**: Inspects all API Gateway stages to ensure that they are linked to the same domain name.
+ **ApiGwV2DomainNameStatus**: Inspects all API Gateway stages to ensure that the domain name is in the AVAILABLE state.
+ **ApiGwV2EndpointType**: Inspects all API Gateway stages to ensure that they have the same value for `Endpoint Type`.
+ **ApiGwV2Quotas**: Inspects all API Gateway groups to ensure that they conform to quotas (limits) that are managed by Service Quotas.
+ **ApiGwV2MutualTlsAuthentication**: Inspects all API Gateway stages to ensure that they have the same value for `Mutual TLS Authentication`.
+ **ApiGwV2ProtocolType**: Inspects all API Gateway stages to ensure that they have the same value for `Protocol Type`.
+ **ApiGwV2RouteConfigs**: Inspects all API Gateway stages to ensure that they have the same hierarchy of routes with the same configuration.
+ **ApiGwV2RouteSelectionExpression**: Inspects all API Gateway stages to ensure that they have the same value for `Route Selection Expression`.
+ **ApiGwV2RouteSettings**: Inspects all API Gateway stages to ensure that they have the same value for `Default Route Settings`.
+ **ApiGwV2SecurityPolicy**: Inspects all API Gateway stages to ensure that they have the same value for `Security Policy`.
+ **ApiGwV2StageVariables**: Inspects all API Gateway stages to ensure that they all have the same `Stage Variables` as the other stages.
+ **ApiGwV2ThrottlingBurstLimit**: Inspects all API Gateway stages to ensure that they have the same value for `Throttling Burst Limit`.
+ **ApiGwV2ThrottlingRateLimit**: Inspects all API Gateway stages to ensure that they have the same value for `Throttling Rate Limit`.

**Amazon Aurora clusters**  
+ **RdsClusterStatus**: Inspects each Aurora cluster to ensure that it has a status of either `AVAILABLE` or `BACKING-UP`.
+ **RdsEngineMode**: Inspects all Aurora clusters to ensure that they have the same value for `Engine Mode`.
+ **RdsEngineVersion**: Inspects all Aurora clusters to ensure that they have the same value for `Major Version`.
+ **RdsGlobalReplicaLag**: Inspects each Aurora cluster to ensure that it has a `Global Replica Lag` of less than 30 seconds.
+ **RdsNormalizedCapacity**: Inspects all Aurora clusters to ensure that they have a normalized capacity within 15% of the maximum in the resource set.
+ **RdsInstanceType**: Inspects all Aurora clusters to ensure that they have the same instance types.
+ **RdsQuotas**: Inspects all Aurora clusters to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Auto Scaling groups**  
+ **AsgMinSizeAndMaxSize**: Inspects all Auto Scaling groups to ensure that they have the same minimum and maximum group sizes.
+ **AsgAZCount**: Inspects all Auto Scaling groups to ensure that they have the same number of Availability Zones.
+ **AsgInstanceTypes**: Inspects all Auto Scaling groups to ensure that they have the same instance types. Note: This rule does not affect readiness status.
+ **AsgInstanceSizes**: Inspects all Auto Scaling groups to ensure that they have the same instance sizes.
+ **AsgNormalizedCapacity**: Inspects all Auto Scaling groups to ensure that they have a normalized capacity within 15% of the maximum in the resource set.
+ **AsgQuotas**: Inspects all Auto Scaling groups to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**CloudWatch alarms**  
+ **CloudWatchAlarmState**: Inspects CloudWatch alarms to ensure that each is not in the `ALARM` or `INSUFFICIENT_DATA` state.

**Customer gateways**  
+ **CustomerGatewayIpAddress**: Inspects all customer gateways to ensure that they have the same IP address.
+ **CustomerGatewayState**: Inspects customer gateways to ensure that each is in the `AVAILABLE` state.
+ **CustomerGatewayVPNType**: Inspects all customer gateways to ensure that they have the same VPN type.

**DNS target resources**  
+ **DnsTargetResourceHostedZoneConfigurationRule**: Inspects all DNS target resources to ensure that they have the same Amazon Route 53 hosted zone ID and that each hosted zone is not private. Note: This rule does not affect readiness status.
+ **DnsTargetResourceRecordSetConfigurationRule**: Inspects all DNS target resources to ensure that they have the same resource record cache time to live (TTL) and that the TTLs are less than or equal to 300.
+ **DnsTargetResourceRoutingRule**: Inspects each DNS target resource associated with an alias resource record set to ensure that it routes traffic to the DNS name configured on the target resource. Note: This rule does not affect readiness status.
+ **DnsTargetResourceHealthCheckRule**: Inspects all DNS target resources to ensure that health checks are associated with their resource record sets when appropriate and not otherwise. Note: This rule does not affect readiness status.

**Amazon DynamoDB tables**  
+ **DynamoConfiguration**: Inspects all DynamoDB tables to ensure that they have the same keys, attributes, server-side encryption, and streams configurations.
+ **DynamoTableStatus**: Inspects each DynamoDB table to ensure that it has a status of ACTIVE.
+ **DynamoCapacity**: Inspects all DynamoDB tables to ensure that their provisioned read capacities and write capacities are within 20% of the maximum capacities in the resource set.
+ **DynamoPeakRcuWcu**: Inspects each DynamoDB table to ensure that it has had similar peak traffic to the other tables, to assure provisioned capacity.
+ **DynamoGsiPeakRcuWcu**: Inspects each DynamoDB table to ensure that it has had similar maximum read and write capacity to the other tables, to assure provisioned capacity.
+ **DynamoGsiConfig**: Inspects all DynamoDB tables that have global secondary indexes to ensure that the tables use the same index, key schema, and projection.
+ **DynamoGsiStatus**: Inspects all DynamoDB tables that have global secondary indexes to ensure that the global secondary indexes have an ACTIVE status.
+ **DynamoGsiCapacity**: Inspects all DynamoDB tables that have global secondary indexes to ensure that the tables have provisioned GSI read capacities and GSI write capacities within 20% of the maximum capacities in the resource set.
+ **DynamoReplicationLatency**: Inspects all DynamoDB tables that are global tables to ensure that they have the same replication latency.
+ **DynamoAutoScalingConfiguration**: Inspects all DynamoDB tables that have Auto Scaling enabled to ensure that they have the same minimum, maximum, and target read and write capacities.
+ **DynamoQuotas**: Inspects all DynamoDB tables to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Elastic Load Balancing (Classic Load Balancers)**  
+ **ElbV1CheckAzCount**: Inspects each Classic Load Balancer to ensure that it is attached to only one Availability Zone. Note: This rule does not affect readiness status.
+ **ElbV1AnyInstances**: Inspects all Classic Load Balancers to ensure that they have at least one EC2 instance.
+ **ElbV1AnyInstancesHealthy**: Inspects all Classic Load Balancers to ensure that they have at least one healthy EC2 instance.
+ **ElbV1Scheme**: Inspects all Classic Load Balancers to ensure that they have the same load balancer scheme.
+ **ElbV1HealthCheckThreshold**: Inspects all Classic Load Balancers to ensure that they have the same health check threshold value.
+ **ElbV1HealthCheckInterval**: Inspects all Classic Load Balancers to ensure that they have the same health check interval value.
+ **ElbV1CrossZoneRoutingEnabled**: Inspects all Classic Load Balancers to ensure that they have the same value for cross-zone load balancing (ENABLED or DISABLED).
+ **ElbV1AccessLogsEnabledAttribute**: Inspects all Classic Load Balancers to ensure that they have the same value for access logs (ENABLED or DISABLED).
+ **ElbV1ConnectionDrainingEnabledAttribute**: Inspects all Classic Load Balancers to ensure that they have the same value for connection draining (ENABLED or DISABLED).
+ **ElbV1ConnectionDrainingTimeoutAttribute**: Inspects all Classic Load Balancers to ensure that they have the same connection draining timeout value.
+ **ElbV1IdleTimeoutAttribute**: Inspects all Classic Load Balancers to ensure that they have the same value for idle timeout.
+ **ElbV1ProvisionedCapacityLcuCount**: Inspects all Classic Load Balancers with a provisioned LCU greater than 10 to ensure that they are within 20% of the highest provisioned LCU in the resource set.
+ **ElbV1ProvisionedCapacityStatus**: Inspects the provisioned capacity status on each Classic Load Balancer to ensure that it does not have a value of DISABLED or PENDING.

**Amazon EBS volumes**  
+ **EbsVolumeEncryption**: Inspects all EBS volumes to ensure that they have the same value for encryption (ENABLED or DISABLED).
+ **EbsVolumeEncryptionDefault**: Inspects all EBS volumes to ensure that they have the same value for encryption by default (ENABLED or DISABLED).
+ **EbsVolumeIops**: Inspects all EBS volumes to ensure that they have the same input/output operations per second (IOPS).
+ **EbsVolumeKmsKeyId**: Inspects all EBS volumes to ensure that they have the same default AWS KMS key ID.
+ **EbsVolumeMultiAttach**: Inspects all EBS volumes to ensure that they have the same value for multi-attach (ENABLED or DISABLED).
+ **EbsVolumeQuotas**: Inspects all EBS volumes to ensure that they conform to quotas (limits) that are set by Service Quotas.
+ **EbsVolumeSize**: Inspects all EBS volumes to ensure that they have the same readable size.
+ **EbsVolumeState**: Inspects all EBS volumes to ensure that they have the same volume state.
+ **EbsVolumeType**: Inspects all EBS volumes to ensure that they have the same volume type.

**AWS Lambda functions**  
+ **LambdaMemorySize**: Inspects all Lambda functions to ensure that they have the same memory size. If one has more memory, the others are marked `NOT READY`.
+ **LambdaFunctionTimeout**: Inspects all Lambda functions to ensure that they have the same timeout value. If one has a greater value, the others are marked `NOT READY`.
+ **LambdaFunctionRuntime**: Inspects all Lambda functions to ensure that they all have the same runtime.
+ **LambdaFunctionReservedConcurrentExecutions**: Inspects all Lambda functions to ensure that they all have the same value for `Reserved Concurrent Executions`. If one has a greater value, the others are marked `NOT READY`.
+ **LambdaFunctionDeadLetterConfig**: Inspects all Lambda functions to ensure that they either all have a `Dead Letter Config` defined, or that none of them do.
+ **LambdaFunctionProvisionedConcurrencyConfig**: Inspects all Lambda functions to ensure that they have the same value for `Provisioned Concurrency`.
+ **LambdaFunctionSecurityGroupCount**: Inspects all Lambda functions to ensure that they have the same value for `Security Groups`.
+ **LambdaFunctionSubnetIdCount**: Inspects all Lambda functions to ensure that they have the same value for `Subnet Ids`.
+ **LambdaFunctionEventSourceMappingMatch**: Inspects all Lambda functions to ensure that all of the chosen `Event Source Mapping `properties match between them.
+ **LambdaFunctionLimitsRule**: Inspects all Lambda functions to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Network Load Balancers and Application Load Balancers**  
+ **ElbV2CheckAzCount**: Inspects each Network Load Balancer to ensure that it is attached to only one Availability Zone. Note: This rule does not affect readiness status.
+ **ElbV2TargetGroupsCanServeTraffic**: Inspects each Network Load Balancer and Application Load Balancer to ensure that it has at least one healthy Amazon EC2 instance.
+ **ElbV2State**: Inspects each Network Load Balancer and Application Load Balancer to ensure that it is in the `ACTIVE` state.
+ **ElbV2IpAddressType**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same IP address types.
+ **ElbV2Scheme**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same scheme.
+ **ElbV2Type**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same type.
+ **ElbV2S3LogsEnabled**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for Amazon S3 server access logs (ENABLED or DISABLED).
+ **ElbV2DeletionProtection**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for deletion protection (ENABLED or DISABLED).
+ **ElbV2IdleTimeoutSeconds**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for idle time seconds.
+ **ElbV2HttpDropInvalidHeaders**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for HTTP drop invalid headers.
+ **ElbV2Http2Enabled**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for HTTP2 (ENABLED or DISABLED).
+ **ElbV2CrossZoneEnabled**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for cross-zone load balancing (ENABLED or DISABLED).
+ **ElbV2ProvisionedCapacityLcuCount**: Inspects all Network Load Balancers and Application Load Balancers with a provisioned LCU greater than 10 to ensure that they are within 20% of the highest provisioned LCU in the resource set.
+ **ElbV2ProvisionedCapacityEnabled**: Inspects all Network Load Balancers and Application Load Balancers provisioned capacity status to ensure that it does not have a value of DISABLED or PENDING.

**Amazon MSK clusters**  
+ **MskClusterClientSubnet**: Inspects each MSK cluster to ensure that it has only two or only three client subnets.
+ **MskClusterInstanceType**: Inspects all MSK clusters to ensure that they have the same Amazon EC2 instance type.
+ **MskClusterSecurityGroups**: Inspects all MSK clusters to ensure that they have the same security groups.
+ **MskClusterStorageInfo**: Inspects all MSK clusters to ensure that they have the same EBS storage volume size. If one has a greater value, the others are marked NOT READY.
+ **MskClusterACMCertificate**: Inspects all MSK clusters to ensure that they have the same list of client authorization certificate ARNs.
+ **MskClusterServerProperties**: Inspects all MSK clusters to ensure that they have the same value for `Current Broker Software Info`.
+ **MskClusterKafkaVersion**: Inspects all MSK clusters to ensure that they have the same Kafka version.
+ **MskClusterEncryptionInTransitInCluster**: Inspects all MSK clusters to ensure that they have the same value for `Encryption In Transit In Cluster`.
+ **MskClusterEncryptionInClientBroker**: Inspects all MSK clusters to ensure that they have the same value for `Encryption In Transit Client Broker`.
+ **MskClusterEnhancedMonitoring**: Inspects all MSK clusters to ensure that they have the same value for `Enhanced Monitoring`.
+ **MskClusterOpenMonitoringInJmx**: Inspects all MSK clusters to ensure that they have the same value for `Open Monitoring JMX Exporter`.
+ **MskClusterOpenMonitoringInNode**: Inspects all MSK clusters to ensure that they have the same value for `Open Monitoring Not Exporter.`
+ **MskClusterLoggingInS3**: Inspects all MSK clusters to ensure that they have the same value for `Is Logging in S3`.
+ **MskClusterLoggingInFirehose**: Inspects all MSK clusters to ensure that they have the same value for `Is Logging In Firehose`.
+ **MskClusterLoggingInCloudWatch**: Inspects all MSK clusters to ensure that they have the same value for `Is Logging Available In CloudWatch Logs`.
+ **MskClusterNumberOfBrokerNodes**: Inspects all MSK clusters to ensure they have the same value for `Number of Broker Nodes`. If one has a greater value, the others are marked NOT READY.
+ **MskClusterState**: Inspects each MSK cluster to ensure that it is in an ACTIVE state.
+ **MskClusterLimitsRule**: Inspects all Lambda functions to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon Route 53 health checks**  
+ **R53HealthCheckType**: Inspects each Route 53 health check to ensure that it is not of type CALCULATED and that all checks are of the same type.
+ **R53HealthCheckDisabled**: Inspects each Route 53 health check to ensure that it does not have a DISABLED state.
+ **R53HealthCheckStatus**: Inspects each Route 53 health check to ensure that it has a SUCCESS status.
+ **R53HealthCheckRequestInterval**: Inspects all Route 53 health checks to ensure that they all have the same value for `Request Interval`.
+ **R53HealthCheckFailureThreshold**: Inspects all Route 53 health checks to ensure that they all have the same value for `Failure Threshold.`
+ **R53HealthCheckEnableSNI**: Inspects all Route 53 health checks to ensure that they all have the same value for `Enable SNI.`
+ **R53HealthCheckSearchString**: Inspects all Route 53 health checks to ensure that they all have the same value for `Search String.`
+ **R53HealthCheckRegions**: Inspects all Route 53 health checks to ensure that they all have the same list of AWS Regions.
+ **R53HealthCheckMeasureLatency**: Inspects all Route 53 health checks to ensure that they all have the same value for `Measure Latency`.
+ **R53HealthCheckInsufficientDataHealthStatus**: Inspects all Route 53 health checks to ensure that they all have the same value for `Insufficient Data Health Status`.
+ **R53HealthCheckInverted**: Inspects all Route 53 health checks to ensure that they are all Inverted, or are all not Inverted.
+ **R53HealthCheckResourcePath**: Inspects all Route 53 health checks to ensure that they all have the same value for `Resource Path`.
+ **R53HealthCheckCloudWatchAlarm**: Inspects all Route 53 health checks to ensure that the CloudWatch alarms associated with them have the same settings and configurations.

**Amazon SNS subscriptions**  
+ **SnsSubscriptionProtocol**: Inspects all SNS subscriptions to ensure that they have the same protocol.
+ **SnsSubscriptionSqsLambdaEndpoint**: Inspects all SNS subscriptions that have Lambda or SQS endpoints to ensure that they have different endpoints.
+ **SnsSubscriptionNonAwsEndpoint**: Inspects all SNS subscriptions that have a non-AWS service endpoint type, for example, email, to ensure that the subscriptions have the same endpoint.
+ **SnsSubscriptionPendingConfirmation**: Inspects all SNS subscriptions to ensure that they have the same value for 'Pending Confirmations'.
+ **SnsSubscriptionDeliveryPolicy**: Inspects all SNS subscriptions that use HTTP/S to ensure that they have the same value for 'Effective Delivery Period'.
+ **SnsSubscriptionRawMessageDelivery**: Inspects all SNS subscriptions to ensure that they have the same value for 'Raw Message Delivery'.
+ **SnsSubscriptionFilter**: Inspects all SNS subscriptions to ensure that they have the same value for 'Filter Policy'.
+ **SnsSubscriptionRedrivePolicy**: Inspects all SNS subscriptions to ensure that they have the same value for 'Redrive Policy'.
+ **SnsSubscriptionEndpointEnabled**: Inspects all SNS subscriptions to ensure that they have the same value for 'Endpoint Enabled'.
+ **SnsSubscriptionLambdaEndpointValid**: Inspects all SNS subscriptions that have Lambda endpoints to ensure that they have valid Lambda endpoints.
+ **SnsSubscriptionSqsEndpointValidRule**: Inspects all SNS subscriptions that use SQS endpoints to ensure that they have valid SQS endpoints.
+ **SnsSubscriptionQuotas**: Inspects all SNS subscriptions to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon SNS topics**  
+ **SnsTopicDisplayName**: Inspects all SNS topics to ensure that they have the same value for `Display Name`.
+ **SnsTopicDeliveryPolicy**: Inspects all SNS topics that have HTTPS subscribers to ensure that they have the same `EffectiveDeliveryPolicy`.
+ **SnsTopicSubscription**: Inspects all SNS topics to ensure that they have the same number of subscribers for each of their protocols.
+ **SnsTopicAwsKmsKey**: Inspects all SNS topics to ensure that all of the topics or none of the topics have an AWS KMS key.
+ **SnsTopicQuotas**: Inspects all SNS topics to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon SQS queues**  
+ **SqsQueueType**: Inspects all SQS queues to ensure that they are all the same value for `Type`.
+ **SqsQueueDelaySeconds**: Inspects all SQS queues to ensure that they all have the same value for `Delay Seconds`.
+ **SqsQueueMaximumMessageSize**: Inspects all SQS queues to ensure that they all have the same value for `Maximum Message Size`.
+ **SqsQueueMessageRetentionPeriod**: Inspects all SQS queues to ensure that they all have the same value for `Message Retention Period`.
+ **SqsQueueReceiveMessageWaitTimeSeconds**: Inspects all SQS queues to ensure that they all have the same value for `Receive Message Wait Time Seconds`.
+ **SqsQueueRedrivePolicyMaxReceiveCount**: Inspects all SQS queues to ensure that they all have the same value for `Redrive Policy Max Receive Count`.
+ **SqsQueueVisibilityTimeout**: Inspects all SQS queues to ensure that they all have the same value for `Visibility Timeout`.
+ **SqsQueueContentBasedDeduplication**: Inspects all SQS queues to ensure that they all have the same value for `Content-Based Deduplication`.
+ **SqsQueueQuotas**: Inspects all SQS queues to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon VPCs**  
+ **VpcCidrBlock**: Inspects all VPCs to ensure that they all have the same value for CIDR block network size.
+ **VpcCidrBlocksSameProtocolVersion**: Inspects all VPCs that have the same CIDR blocks to ensure that they have the same value for Internet Stream Protocol version number.
+ **VpcCidrBlocksStateInAssociationSets**: Inspects all CIDR block association sets for all VPCs to ensure that they all have CIDR blocks that are in an `ASSOCIATED` state.
+ **VpcIpv6CidrBlocksStateInAssociationSets**: Inspects all CIDR block association sets for all VPCs to ensure that they all have CIDR blocks with the same number of addresses.
+ **VpcCidrBlocksInAssociationSets**: Inspects all CIDR block association sets for all VPCs to ensure that they all have the same size.
+ **VpcIpv6CidrBlocksInAssociationSets**: Inspects all IPv6 CIDR block association sets for all VPCs to ensure that they have the same size.
+ **VpcState**: Inspects each VPC to ensure that it is in an `AVAILABLE` state.
+ **VpcInstanceTenancy**: Inspects all VPCs to ensure that they all have the same value for `Instance Tenancy`.
+ **VpcIsDefault**: Inspects all VPCs to ensure that they have the same value for `Is Default.`
+ **VpcSubnetState**: Inspects each VPC subnet to ensure that it is in an AVAILABLE state.
+ **VpcSubnetAvailableIpAddressCount**: Inspects each VPC subnet to ensure that it has an available IP address count greater than zero.
+ **VpcSubnetCount**: Inspects all VPC subnets to ensure that they have the same number of subnets.
+ **VpcQuotas**: Inspects all VPC subnets to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Site-to-Site VPN connections**  
+ **VpnConnectionsRouteCount**: Inspects all VPN connections to ensure that they have at least one route, and also the same number of routes.
+ **VpnConnectionsEnableAcceleration**: Inspects all VPN connections to ensure that they have the same value for `Enable Accelerations`.
+ **VpnConnectionsStaticRoutesOnly**: Inspects all VPN connections to ensure that they have the same value for `Static Routes Only.`
+ **VpnConnectionsCategory**: Inspects all VPN connections to ensure that they have a category of `VPN`.
+ **VpnConnectionsCustomerConfiguration**: Inspects all VPN connections to ensure that they have the same value for `Customer Gateway Configuration`.
+ **VpnConnectionsCustomerGatewayId**: Inspects each VPN connection to ensure that it has a customer gateway attached.
+ **VpnConnectionsRoutesState**: Inspects all VPN connections to ensure that they are in an `AVAILABLE` state.
+ **VpnConnectionsVgwTelemetryStatus**: Inspects each VPN connection to ensure that it has a VGW status of `UP`.
+ **VpnConnectionsVgwTelemetryIpAddress**: Inspects each VPN connection to ensure that it has a different outside IP address for each VGW telemetry.
+ **VpnConnectionsTunnelOptions**: Inspects all VPN connections to ensure that they have the same tunnel options.
+ **VpnConnectionsRoutesCidr**: Inspects all VPN connections to ensure that they have the same destination CIDR blocks.
+ **VpnConnectionsInstanceType**: Inspects all VPN connections to ensure that they have the same `Instance Type`.

**Site-to-Site VPN gateways**  
+ **VpnGatewayState**: Inspects all VPN gateways to ensure that they are in an AVAILABLE state.
+ **VpnGatewayAsn**: Inspects all VPN gateways to ensure that they have the same ASN.
+ **VpnGatewayType**: Inspects all VPN gateways to ensure that they have the same type.
+ **VpnGatewayAttachment**: Inspects all VPN gateways to ensure that they have the same attachment configurations.

##### View readiness rules on the console
<a name="recovery-readiness.list-rules-console"></a>

You can view readiness rules on the AWS Management Console, listed by each resource type.

##### To view readiness rules on the console


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. Under **Resource type**, choose the resource type that you want to view the rules for.

#### Resource types and ARN formats in ARC
<a name="recovery-readiness.resource-types-arns"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

When you create a resource set in Amazon Application Recovery Controller (ARC), you specify the type of resource to include in the set and Amazon Resource Names (ARNs) for each of the resources to include. ARC expects a specific ARN format for each resource type. This section lists the resource types supported by ARC and the associated ARN formats for each one.

The specific format depends on the resource. When you provide an ARN, replace the {{italicized}} text with your resource-specific information. 

**Note**  
Be aware that the ARN format that ARC requires for resources might differ from the ARN format that a service itself requires for its resources. For example, the ARN formats that are described in the **Resource type** sections for each service in the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/reference.html) might not include the AWS account ID or other information that ARC needs to support features in the ARC service.

**AWS::ApiGateway::Stage**  
An Amazon API Gateway Version 1 stage.  
+ **ARN format: **`arn:{{partition}}:apigateway:{{region}}:{{account}}:/restapis/{{api-id}}/stages/{{stage-name}}`

  Example: `arn:aws:apigateway:us-east-1:111122223333:/restapis/123456789/stages/ExampleStage`

  For more information, see [API Gateway Amazon Resource Name (ARN) reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/arn-format-reference.html).

**AWS::ApiGatewayV2::Stage**  
An Amazon API Gateway Version 2 stage.  
+ **ARN format: **`arn:{{partition}}:apigateway:{{region}}:{{account}}:/apis/{{api-id}}/stages/{{stage-name}}`

  Example: `arn:aws:apigateway:us-east-1:111122223333:/apis/123456789/stages/ExampleStage`

  For more information, see [API Gateway Amazon Resource Name (ARN) reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/arn-format-reference.html).

**AWS::CloudWatch::Alarm**  
An Amazon CloudWatch alarm.  
+ **ARN format: **`arn:{{partition}}:cloudwatch:{{region}}:{{account}}:alarm:{{alarm-name}}`

  Example: `arn:aws:cloudwatch:us-west-2:111122223333:alarm:test-alarm-1`

  For more information, see [Resource types defined by Amazon CloudWatch](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies).

**AWS::DynamoDB::Table**  
An Amazon DynamoDB table.  
+ **ARN format: **`arn:{{partition}}:dynamodb:{{region}}:{{account}}:table/{{table-name}}`

  Example: `arn:aws:dynamodb:us-west-2:111122223333:table/BigTable`

  For more information, see [DynamoDB resources and operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-overview.html#access-control-resources).

**AWS::EC2::CustomerGateway**  
A customer gateway device.  
+ **ARN format: **`arn:{{partition}}:ec2:{{region}}:{{account}}:customer-gateway/{{CustomerGatewayId}}`

  Example: `arn:aws:ec2:us-west-2:111122223333:customer-gateway/vcg-123456789`

  For more information, see [Resource types defined by Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies).

**AWS::EC2::Volume**  
An Amazon EBS volume.  
+ **ARN format: **`arn:{{partition}}:ec2:{{region}}:{{account}}:volume/{{VolumeId}}`

  Example: `arn:aws:ec2:us-west-2:111122223333:volume/volume-of-cylinder-is-pi`

  For more information, see [API Gateway Amazon Resource Name (ARN) reference](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies).

**AWS::ElasticLoadBalancing::LoadBalancer**  
A Classic Load Balancer.  
+ **ARN format: **`arn:{{partition}}:elasticloadbalancing:{{region}}:{{account}}:loadbalancer/{{LoadBalancerName}}`

  Example: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/123456789abcbdeCLB`

  For more information, see [Elastic Load Balancing resources](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.html#elb-resources).

**AWS::ElasticLoadBalancingV2::LoadBalancer**  
A Network Load Balancer or an Application Load Balancer.  
+ **ARN format for Network Load Balancer: **`arn:{{partition}}:elasticloadbalancing:{{region}}:{{account}}:loadbalancer/net/{{LoadBalancerName}}`

  Example for Network Load Balancer: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/net/sandbox-net/123456789acbdeNLB`
+ **ARN format for Application Load Balancer: **`arn:{{partition}}:elasticloadbalancing:{{region}}:{{account}}:loadbalancer/app/{{LoadBalancerName}}`

  Example for Application Load Balancer: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/app/sandbox-alb/123456789acbdeALB`

  For more information, see [Elastic Load Balancing resources](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.html#elb-resources).

**AWS::Lambda::Function**  
An AWS Lambda function.  
+ **ARN format: **`arn:{{partition}}:lambda:{{region}}:{{account}}:function:{{FunctionName}}`

  Example: `arn:aws:lambda:us-west-2:111122223333:function:my-function`

  For more information, see [Resources and conditions for Lambda actions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html).

**AWS::MSK::Cluster**  
An Amazon MSK cluster.  
+ **ARN format: **`arn:{{partition}}:kafka:{{region}}:{{account}}:cluster/{{ClusterName}}/{{UUID}}`

  Example: `arn:aws:kafka:us-east-1:111122223333:cluster/demo-cluster-1/123456-1111-2222-3333`

  For more information, see [Resource types defined by Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedstreamingforapachekafka.html#amazonmanagedstreamingforapachekafka-resources-for-iam-policies).

**AWS::RDS::DBCluster**  
An Aurora DB cluster.  
+ **ARN format: **`arn:{{partition}}:rds:{{region}}:{{account}}:cluster:{{DbClusterInstanceName}}`

  Example: `arn:aws:rds:us-west-2:111122223333:cluster:database-1`

  For more information, see [Working with Amazon Resource Names (ARNs) in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html).

**AWS::Route53::HealthCheck**  
An Amazon Route 53 health check.  
+ **ARN format: **`arn:{{partition}}:route53:::healthcheck/{{Id}}`

  Example: `arn:aws:route53:::healthcheck/123456-1111-2222-3333`

**AWS::SQS::Queue**  
An Amazon SQS queue.  
+ **ARN format: **`arn:{{partition}}:sqs:{{region}}:{{account}}:{{QueueName}}`

  Example: `arn:aws:sqs:us-west-2:111122223333:StandardQueue`

  For more information, see [Amazon Simple Queue Service resource and operations](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html#sqs-resource-and-operations).

**AWS::SNS::Topic**  
An Amazon SNS topic.  
+ **ARN format: **`arn:{{partition}}:sns:{{region}}:{{account}}:{{TopicName}}`

  Example: `arn:aws:sns:us-west-2:111122223333:TopicName`

  For more information, see [Amazon SNS resource ARN format](https://docs.aws.amazon.com/sns/latest/dg/sns-using-identity-based-policies.html#sns-arn-format).

**AWS::SNS::Subscription**  
An Amazon SNS subscription.  
+ **ARN format: **`arn:{{partition}}:sns:{{region}}:{{account}}:{{TopicName}}:{{SubscriptionId}}`

  Example: `arn:aws:sns:us-west-2:111122223333:TopicName:123456789012345567890`

**AWS::EC2::VPC**  
A virtual private cloud (VPC).  
+ **ARN format: **`arn:{{partition}}:ec2:{{region}}:{{account}}:vpc/{{VpcId}}`

  Example: `arn:aws:ec2:us-west-2:111122223333:vpc/vpc-123456789`

  For more information, see [VPC Resources](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies).

**AWS::EC2::VPNConnection**  
A virtual private network (VPN) connection.  
+ **ARN format: **`arn:{{partition}}:ec2:{{region}}:{{account}}:vpn-connection/{{VpnConnectionId}}`

  Example: `arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-123456789`

  For more information, see [Resource types defined by Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies).

**AWS::EC2::VPNGateway**  
A virtual private network (VPN) gateway.  
+ **ARN format: **`arn:{{partition}}:ec2:{{region}}:{{account}}:vpn-gateway/{{VpnGatewayId}}`

  Example: `arn:aws:ec2:us-west-2:111122223333:vpn-gateway/vgw-123456789acbdefgh`

  For more information, see [Resource types defined by Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies).

**AWS::Route53RecoveryReadiness::DNSTargetResource**  
A DNS target resource for readiness checks includes the DNS record type, domain name, Route 53 hosted zone ARN, and Network Load Balancer ARN or Route 53 record set ID.  
+ **ARN format for hosted zone: **`arn:{{partition}}:route53::{{account}}:hostedzone/{{Id}}`

  Example for a hosted zone: `arn:aws:route53::111122223333:hostedzone/abcHostedZone`

  NOTE: You must include the account ID in hosted zone ARNs, as specified here. The account ID is required so that ARC can poll the resource. The format is intentionally different from the ARN format that Amazon Route 53 requires, described in the Route 53 service [Resource types](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53.html#amazonroute53-resources-for-iam-policies) in the *Service Authorization Reference*. 
+ **ARN format for Network Load Balancer: **`arn:{{partition}}:elasticloadbalancing:{{region}}:{{account}}:loadbalancer/net/{{LoadBalancerName}}`

  Example for Network Load Balancer: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/net/sandbox-net/123456789acbdefgh`

  For more information, see [Elastic Load Balancing resources](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.html#elb-resources).

### Logging and monitoring for readiness check in Amazon Application Recovery Controller (ARC)
<a name="monitoring-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

You can use Amazon CloudWatch, AWS CloudTrail, and Amazon EventBridge for monitoring readiness check in Amazon Application Recovery Controller (ARC), to analyze patterns and help troubleshoot issues.

**Note**  
You must view CloudWatch metrics and logs for ARC in the US West (Oregon) Region, both in the console and when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region for your command by including the following parameter: `--region us-west-2`.

**Topics**
+ [Using Amazon CloudWatch with readiness check in ARC](#cloudwatch-readiness)
+ [Logging readiness check API calls using AWS CloudTrail](#cloudtrail-readiness)
+ [Using readiness check in ARC with Amazon EventBridge](#eventbridge-readiness)

#### Using Amazon CloudWatch with readiness check in ARC
<a name="cloudwatch-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

Amazon Application Recovery Controller (ARC) publishes data points to Amazon CloudWatch for your readiness checks. CloudWatch enables you to retrieve statistics about those data points as an ordered set of time-series data, known as *metrics*. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. For example, you can monitor traffic through an AWS Region over a specified time period. Each data point has an associated time stamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such as sending a notification to an email address) if the metric goes outside what you consider an acceptable range.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [ARC metrics](#cloudwatch-metrics-recovery-readiness)
+ [Statistics for ARC metrics](#cloudwatch-metric-statistics)
+ [View CloudWatch metrics in ARC](#view-metric-data)

##### ARC metrics
<a name="cloudwatch-metrics-recovery-readiness"></a>

The `AWS/Route53RecoveryReadiness` namespace includes the following metrics.


| Metric | Description | 
| --- | --- | 
| ReadinessChecks | Represents the number of readiness checks processed by ARC. The metric can be dimensioned by its states, listed below.<br />**Unit**: `Count`.<br />**Reporting criteria**: There is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+ `READY`<br />+ `NOT_READY`<br />+ `NOT_AUTHORIZED`<br />+ `UNKNOWN` | 
| Resources | Represents the number of resources processed by ARC, which can be dimensioned by their resource identifier, as defined by the API.<br />**Unit**: `Count`.<br />**Reporting criteria**: There is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+  `ResourceSetType`: These are the resource types, filtered by the number of resources per given type evaluated by ARC <br />For example: `AWS::CloudWatch::Alarm` | 

##### Statistics for ARC metrics
<a name="cloudwatch-metric-statistics"></a>

CloudWatch provides statistics based on the metric data points published by ARC. Statistics are aggregations of metric data over a specified period of time. When you request statistics, the returned data stream is identified by the metric name and dimension. A dimension is a name/value pair that uniquely identifies a metric.

The following are examples of metric/dimension combinations that you might find useful:
+ View the number of readiness checks evaluated for readiness by ARC.
+ View the total number of resources for a given resource set type evaluated by ARC.

##### View CloudWatch metrics in ARC
<a name="view-metric-data"></a>

You can view the CloudWatch metrics for ARC using the CloudWatch console or the AWS CLI. In the console, metrics are displayed as monitoring graphs.

You must view CloudWatch metrics for ARC in the US West (Oregon) Region, both in the console or when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region for your command by including the following parameter: `--region us-west-2`. 

**To view metrics using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Select the **Route53RecoveryReadiness** namespace.

1. (Optional) To view a metric across all dimensions, type its name in the search field.

**To view metrics using the AWS CLI**  
Use the following [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) command to list the available metrics:

```
aws cloudwatch list-metrics --namespace AWS/Route53RecoveryReadiness --region us-west-2
```

**To get the statistics for a metric using the AWS CLI**  
Use the following [get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) command to get statistics for a specified metric and dimension. Note that CloudWatch treats each unique combination of dimensions as a separate metric. You can't retrieve statistics using combinations of dimensions that were not specifically published. You must specify the same dimensions that were used when the metrics were created.

The following example lists the total readiness checks evaluated, per minute, for an account in ARC.

```
aws cloudwatch get-metric-statistics --namespace AWS/Route53RecoveryReadiness \
--metric-name ReadinessChecks \
--region us-west-2 \
--statistics Sum --period 60 \
--dimensions Name=State,Value=READY \
--start-time 2021-07-03T01:00:00Z --end-time 2021-07-03T01:20:00Z
```

The following is example output from the command:

```
{
    "Label": "ReadinessChecks",
    "Datapoints": [
        {
            "Timestamp": "2021-07-08T18:00:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:04:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:01:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:02:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:03:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        }
    ]
}
```

#### Logging readiness check API calls using AWS CloudTrail
<a name="cloudtrail-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

 is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in ARC. CloudTrail captures all API calls for ARC as events. The calls captured include calls from the ARC console and code calls to the ARC API operations. 

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for ARC. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**.

Using the information collected by CloudTrail, you can determine the request that was made to ARC, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

##### ARC information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in ARC, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for ARC, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All ARC actions are logged by CloudTrail and are documented in the [Recovery Readiness API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/recovery-readiness/latest/api/), [Recovery Control Configuration API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/recovery-cluster/latest/api/), and [Routing Control API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/routing-control/latest/APIReference/). For example, calls to the `CreateCluster`, `UpdateRoutingControlState` and `CreateRecoveryGroup` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

##### Viewing ARC events in event history
<a name="amazon-arc-events-in-cloudtrail-event-history"></a>

CloudTrail lets you view recent events in **Event history**. To view events for ARC API requests, you must choose **US West (Oregon)** in the Region selector at the top of the console. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*.

##### Understanding ARC log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `CreateRecoveryGroup` action for readiness check.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/admin",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA33L3W36EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/admin",
                "accountId": "111122223333",
                "userName": "EXAMPLENAME"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-07-06T17:38:05Z"
            }
        }
    },
    "eventTime": "2021-07-06T18:08:03Z",
    "eventSource": "route53-recovery-readiness.amazonaws.com",
    "eventName": "CreateRecoveryGroup",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.50",
    "userAgent": "Boto3/1.17.101 Python/3.8.10 Linux/4.14.231-180.360.amzn2.x86_64 exec-env/AWS_Lambda_python3.8 Botocore/1.20.102",
    "requestParameters": {
        "recoveryGroupName": "MyRecoveryGroup"
    },
    "responseElements": {
        "Access-Control-Expose-Headers": "x-amzn-errortype,x-amzn-requestid,x-amzn-errormessage,x-amzn-trace-id,x-amzn-requestid,x-amz-apigw-id,date",
        "cells": [],
        "recoveryGroupName": "MyRecoveryGroup",
        "recoveryGroupArn": "arn:aws:route53-recovery-readiness::111122223333:recovery-group/MyRecoveryGroup",
        "tags": "***"
    },
    "requestID": "fd42dcf7-6446-41e9-b408-d096example",
    "eventID": "4b5c42df-1174-46c8-be99-d67aexample",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333"
}
```

#### Using readiness check in ARC with Amazon EventBridge
<a name="eventbridge-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

Using Amazon EventBridge, you can set up event-driven rules that monitor your readiness check resources in Amazon Application Recovery Controller (ARC), and then initiate target actions that use other AWS services. For example, you can set a rule for sending out email notifications by signaling an Amazon SNS topic when a readiness check status changes from **READY** to **NOT READY**.

**Note**  
ARC only publishes EventBridge events for readiness check in the US West (Oregon) (us-west-2) AWS Region. To receive EventBridge events for readiness check, create EventBridge rules in the US West (Oregon) Region.

You can create rules in Amazon EventBridge to act on the following ARC readiness check event:
+ *Readiness check readiness.* The event specifies if readiness check status changes, for example, from **READY** to **NOT READY**.

To capture specific ARC events that you're interested in, define event-specific patterns that EventBridge can use to detect the events. Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for. 

Events are emitted on a best effort basis. They're delivered from ARC to EventBridge in near real-time under normal operational circumstances. However, situations can arise that might delay or prevent delivery of an event.

For information about how EventBridge rules work with event patterns, see [Events and Event Patterns in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html). 

##### Monitor a readiness check resource with EventBridge
<a name="arc-eventbridge-tasks-readiness"></a>

With EventBridge, you can create rules that define actions to take when ARC emits events for readiness check resources. 

To type or copy and paste an event pattern into the EventBridge console, in the console, select to the option **Enter my own** option. To help you determine event patterns that might be useful for you, this topic includes [example readiness event patterns](#arc-eventbridge-examples-readiness).

**To create a rule for a resource event**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. For the AWS Region to create the rule in, choose US West (Oregon). This is the required Region for readiness events.

1. Choose **Create rule**.

1. Enter a **Name** for the rule, and, optionally, a description.

1. For **Event bus**, leave the default value, **default**.

1. Choose **Next**.

1. For the **Build event pattern** step, for **Event source**, leave the default value, **AWS events**.

1. Under **Sample event**, choose **Enter my own**.

1. For **Sample events**, type or copy and paste an event pattern. For examples, see the next section.

##### Example readiness event patterns
<a name="arc-eventbridge-examples-readiness"></a>

Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for.

You can copy and paste event patterns from this section into EventBridge to create rules that you can use to monitor ARC actions and resources.

The following event patterns provide examples that you might use in EventBridge for the readiness check capability in ARC.
+ *Select all events from ARC readiness check*.

  ```
  {
      "source": [
          "aws.route53-recovery-readiness"
      ]
  }
  ```
+ *Select only events related to cells*.

  ```
  {
      "source": [
          "aws.route53-recovery-readiness"
      ],
      "detail-type": [
          "Route 53 Application Recovery Controller cell readiness status change"
      ]
  }
  ```
+ *Select only events related to a specific cell called `MyExampleCell`*.

  ```
  {
      "source": [
          "aws.route53-recovery-readiness"
      ],
      "detail-type": [
          "Route 53 Application Recovery Controller cell readiness status change"
      ],
      "resources": [
          "arn:aws:route53-recovery-readiness::111122223333:cell/MyExampleCell"
      ]
  }
  ```
+ *Select only events when any recovery group, cell, or readiness check status becomes `NOT READY`*.

  ```
  {
     "source":[
        "aws.route53-recovery-readiness"
     ],
     "detail-type":{
        "new-state":{
           "readiness-status":[
              "NOT_READY"
           ]
        }
     }
  }
  ```
+ *Select only events when any recovery group, cell, or readiness check becomes anything except `READY`*

  ```
  {
     "source":[
        "aws.route53-recovery-readiness"
     ],
     "detail":{
        "new-state":{
           "readiness-status":[
              {
                 "anything-but":"READY"
              }
           ]
        }
     }
  }
  ```

The following is an example ARC event for a *recovery group readiness status change*:

```
{
    "version": "0",
    "account":"111122223333",
    "detail-type":"Route 53 Application Recovery Controller recovery group readiness status change",
    "source":"route53-recovery-readiness.amazonaws.com",
    "time":"2020-11-03T00:31:54Z",
    "id": "1234a678-1b23-c123-12fd3f456e78",
    "region": "us-west-2",
    "resources":[
        "arn:aws:route53-recovery-readiness::111122223333:recovery-group/BillingApp"
    ],
    "detail": {
        "recovery-group-name": "BillingApp",
        "previous-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        },
        "new-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        }
    }
}
```

The following is an example ARC event for a *cell readiness status change*:

```
{
    "version": "0",
    "account":"111122223333",
    "detail-type":"Route 53 Application Recovery Controller cell readiness status change",
    "source":"route53-recovery-readiness.amazonaws.com",
    "time":"2020-11-03T00:31:54Z",
    "id": "1234a678-1b23-c123-12fd3f456e78",
    "region": "us-west-2",
    "resources":[
        "arn:aws:route53-recovery-readiness::111122223333:cell/PDXCell"
    ],
    "detail": {
        "cell-name": "PDXCell",
        "previous-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        },
        "new-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        }
    }
}
```

The following is an example ARC event for a *readiness check status change*:

```
{
    "version": "0",
    "account":"111122223333",
    "detail-type":"Route 53 Application Recovery Controller readiness check status change",
    "source":"route53-recovery-readiness.amazonaws.com",
    "time":"2020-11-03T00:31:54Z",
    "id": "1234a678-1b23-c123-12fd3f456e78",
    "region": "us-west-2",
    "resources":[
        "arn:aws:route53-recovery-readiness::111122223333:readiness-check/UserTableReadinessCheck"
    ],
    "detail": {
    "readiness-check-name": "UserTableReadinessCheck",
        "previous-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        },
        "new-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        }
    }
}
```

##### Specify a CloudWatch log group to use as a target
<a name="arc-eventbridge-cw-loggroup"></a>

When you create an EventBridge rule, you must specify the target where events that are matched to the rule are sent. For a list of available targets for EventBridge, see [Targets available in the EventBridge console](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html#eb-console-targets). One of the targets that you can add to an EventBridge rule is an Amazon CloudWatch log group. This section describes the requirements for adding CloudWatch log groups as targets, and provides a procedure for adding a log group when you create a rule.

To add a CloudWatch log group as a target, you can do one of the following:
+ Create a new log group 
+ Choose an existing log group

If you specify a new log group using the console when you create a rule, EventBridge automatically creates the log group for you. Make sure that the log group that you use as a target for the EventBridge rule starts with `/aws/events`. If you want to choose an existing log group, be aware that only log groups that start with `/aws/events` appear as options in the drop-down menu. For more information, see [Create a new log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group) in the *Amazon CloudWatch User Guide*.

If you create or use a CloudWatch log group to use as a target using CloudWatch operations outside of the console, make sure that you set permissions correctly. If you use the console to add a log group to an EventBridge rule, then the resource-based policy for the log group is updated automatically. But, if you use the AWS Command Line Interface or an AWS SDK to specify a log group, then you must update resource-based policy for the log group. The following example policy illustrates the permissions that you must define in a resource-based policy for the log group:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 

    "Statement": [
        {
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "events.amazonaws.com",
                    "delivery.logs.amazonaws.com"
                ]
            },
            "Resource": "arn:aws:logs:us-east-1:{{222222222222}}:log-group:/aws/events/*:*",
            "Sid": "TrustEventsToStoreLogEvent"
        }
    ]
}
```

------

You can't configure a resource-based policy for a log group by using the console. To add the required permissions to a resource-based policy, use the CloudWatch [PutResourcePolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html) API operation. Then, you can use the [ describe-resource-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-resource-policies.html) CLI command to check that your policy was applied correctly.

**To create a rule for a resource event and specify a CloudWatch log group target**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose the AWS Region that you want to create the rule in.

1. Choose **Create rule** and then enter any information about that rule, such as the event pattern or schedule details.

   For more information about creating EventBridge rules for readiness, see [ Monitor a readiness check resource with EventBridge](#RCEventBridgeCreateRule).

1. On the **Select target** page, choose **CloudWatch** as your target.

1. Choose a CloudWatch log group from the drop-down menu.

### Identity and Access Management for readiness check in ARC
<a name="security-iam-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use ARC resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [How readiness check works with IAM](#security_iam_service-with-iam-readiness)
+ [Identity-based policy examples](#security_iam_id-based-policy-examples-readiness)
+ [Service-linked roles](#using-service-linked-roles-readiness)
+ [AWS managed policies](#security-iam-awsmanpol-readiness)

#### How readiness check in Amazon Application Recovery Controller (ARC) works with IAM
<a name="security_iam_service-with-iam-readiness"></a>

Before you use IAM to manage access to ARC, learn what IAM features are available to use with ARC.

Before you use IAM to manage access to readiness check in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with readiness check.


**IAM features you can use with readiness check in Amazon Application Recovery Controller (ARC)**  

| IAM feature | Readiness check support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-readiness-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-readiness-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-readiness-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-readiness-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-readiness-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-readiness-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-readiness-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-readiness-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-readiness-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-readiness-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-readiness-roles-service-linked) |  Yes | 

To get a high-level, overall view of how AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Identity-based policies for readiness check
<a name="security_iam_service-with-iam-readiness-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To view examples of ARC identity-based policies, see [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](#security_iam_id-based-policy-examples).

##### Resource-based policies within readiness check
<a name="security_iam_service-with-iam-readiness-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

##### Policy actions for readiness check
<a name="security_iam_service-with-iam-readiness-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of ARC actions for readiness check, see [ Actions defined by Amazon Route 53 Recovery Readiness](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53recoveryreadiness-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in ARC for readiness check use the following prefixes before the action:

```
route53-recovery-readiness
```

To specify multiple actions in a single statement, separate them with commas. For example, the following:

```
"Action": [
      "route53-recovery-readiness:{{action1}}",
      "route53-recovery-readiness:{{action2}}"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "route53-recovery-readiness:Describe*"
```

To view examples of ARC identity-based policies for readiness check, see [Identity-based policy examples for readiness check in ARC](#security_iam_id-based-policy-examples-readiness).

##### Policy resources for readiness check
<a name="security_iam_service-with-iam-readiness-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of ARC actions for zonal shift, see [ Actions defined by Amazon Route 53 Recovery Readiness](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoveryreadiness.html#amazonroute53recoveryreadiness-actions-as-permissions).

To view examples of ARC identity-based policies for readiness check, see [Identity-based policy examples for readiness check in ARC](#security_iam_id-based-policy-examples-readiness).

##### Policy condition keys for readiness check
<a name="security_iam_service-with-iam-readiness-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of ARC actions for readiness check, see [ Condition keys for Amazon Route 53 Recovery Readiness](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoveryreadiness.html#amazonroute53recoveryreadiness-policy-keys)

To see the actions and resources that you can use with a condition key with readiness check, see [ Actions defined by Amazon Route 53 Recovery Readiness](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoveryreadiness.html#amazonroute53recoveryreadiness-actions-as-permissions)

To view examples of ARC identity-based policies for readiness check, see [Identity-based policy examples for readiness check in ARC](#security_iam_id-based-policy-examples-readiness).

##### Access control lists (ACLs) in readiness check
<a name="security_iam_service-with-iam-readiness-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

##### Attribute-based access control (ABAC) with readiness check
<a name="security_iam_service-with-iam-readiness-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

Recovery Readiness (readiness check) supports ABAC.

##### Using temporary credentials with readiness check
<a name="security_iam_service-with-iam-readiness-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Cross-service principal permissions for readiness check
<a name="security_iam_service-with-iam-readiness-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

When you use an IAM entity (user or role) to perform actions in AWS, you are considered a principal. Policies grant permissions to a principal. When you use some services, you might perform an action that then triggers another action in a different service. In this case, you must have permissions to perform both actions.

To see whether an action in readiness check requires additional dependent actions in a policy, see [ Amazon Route 53 Recovery Readiness](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoveryreadiness.html)

##### Service roles for readiness check
<a name="security_iam_service-with-iam-readiness-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

##### Service-linked roles for readiness check
<a name="security_iam_service-with-iam-readiness-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing ARC service-linked roles, see [Using service-linked role for readiness check in ARC](#using-service-linked-roles-readiness).

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.

#### Identity-based policy examples for readiness check in ARC
<a name="security_iam_id-based-policy-examples-readiness"></a>

By default, users and roles don't have permission to create or modify ARC resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by ARC, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices-zonal)
+ [Example: Readiness check console access](#security_iam_id-based-policy-examples-console-readiness)
+ [Examples: Readiness check API actions for readiness check](#security_iam_id-based-policy-examples-api-readiness)

##### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices-zonal"></a>

Identity-based policies determine whether someone can create, access, or delete ARC resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

##### Example: Readiness check console access
<a name="security_iam_id-based-policy-examples-console-readiness"></a>

To access the Amazon Application Recovery Controller (ARC) console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the ARC resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can still use the readiness check console when you allow access to only specific API operations, also attach a `ReadOnly` AWS managed policy for readiness check to the entities. For more information, see the readiness check [Readiness check managed policies page](#security-iam-awsmanpol-readiness) or [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

To perform some tasks, users must have permission to create the service-linked role that is associated with readiness check in ARC. To learn more, see [Using service-linked role for readiness check in ARC](#using-service-linked-roles-readiness).

To give users full access to use readiness check features through the console, attach a policy like the following to the user:

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
                   "route53-recovery-readiness:CreateCell",
                   "route53-recovery-readiness:CreateCrossAccountAuthorization",
                   "route53-recovery-readiness:CreateReadinessCheck",
                   "route53-recovery-readiness:CreateRecoveryGroup",
                   "route53-recovery-readiness:CreateResourceSet",
                   "route53-recovery-readiness:DeleteCell",
                   "route53-recovery-readiness:DeleteCrossAccountAuthorization",
                   "route53-recovery-readiness:DeleteReadinessCheck",
                   "route53-recovery-readiness:DeleteRecoveryGroup",
                   "route53-recovery-readiness:DeleteResourceSet",
                   "route53-recovery-readiness:GetArchitectureRecommendations",
                   "route53-recovery-readiness:GetCell",
                   "route53-recovery-readiness:GetCellReadinessSummary",
                   "route53-recovery-readiness:GetReadinessCheck",
                   "route53-recovery-readiness:GetReadinessCheckResourceStatus",
                   "route53-recovery-readiness:GetReadinessCheckStatus", 
                   "route53-recovery-readiness:GetRecoveryGroup",
                   "route53-recovery-readiness:GetRecoveryGroupReadinessSummary",
                   "route53-recovery-readiness:GetResourceSet",
                   "route53-recovery-readiness:ListCells",
                   "route53-recovery-readiness:ListCrossAccountAuthorizations",
                   "route53-recovery-readiness:ListReadinessChecks",
                   "route53-recovery-readiness:ListRecoveryGroups",
                   "route53-recovery-readiness:ListResourceSets",
                   "route53-recovery-readiness:ListRules",
                   "route53-recovery-readiness:UpdateCell",
                   "route53-recovery-readiness:UpdateReadinessCheck",
                   "route53-recovery-readiness:UpdateRecoveryGroup",
                   "route53-recovery-readiness:UpdateResourceSet"
             ],
            "Resource": "*"
        }
    ]
}
```

------

##### Examples: Readiness check API actions for readiness check
<a name="security_iam_id-based-policy-examples-api-readiness"></a>

To ensure that a user can use ARC API actions to work with the ARC readiness check control plane – for example, to create recovery groups, resource sets, and readiness checks – attach a policy that corresponds to the API operations that the user needs to work with, as described below.

To perform some tasks, users must have permission to create the service-linked role that is associated with readiness check in ARC. To learn more, see [Using service-linked role for readiness check in ARC](#using-service-linked-roles-readiness).

To work with API operations for readiness check, attach a policy like the following to the user:

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
                   "route53-recovery-readiness:CreateCell",
                   "route53-recovery-readiness:CreateCrossAccountAuthorization",
                   "route53-recovery-readiness:CreateReadinessCheck",
                   "route53-recovery-readiness:CreateRecoveryGroup",
                   "route53-recovery-readiness:CreateResourceSet",
                   "route53-recovery-readiness:DeleteCell",
                   "route53-recovery-readiness:DeleteCrossAccountAuthorization",
                   "route53-recovery-readiness:DeleteReadinessCheck",
                   "route53-recovery-readiness:DeleteRecoveryGroup",
                   "route53-recovery-readiness:DeleteResourceSet",
                   "route53-recovery-readiness:GetArchitectureRecommendations",
                   "route53-recovery-readiness:GetCell",
                   "route53-recovery-readiness:GetCellReadinessSummary",
                   "route53-recovery-readiness:GetReadinessCheck",
                   "route53-recovery-readiness:GetReadinessCheckResourceStatus",
                   "route53-recovery-readiness:GetReadinessCheckStatus", 
                   "route53-recovery-readiness:GetRecoveryGroup",
                   "route53-recovery-readiness:GetRecoveryGroupReadinessSummary",
                   "route53-recovery-readiness:GetResourceSet",
                   "route53-recovery-readiness:ListCells",
                   "route53-recovery-readiness:ListCrossAccountAuthorizations",
                   "route53-recovery-readiness:ListReadinessChecks",
                   "route53-recovery-readiness:ListRecoveryGroups",
                   "route53-recovery-readiness:ListResourceSets",
                   "route53-recovery-readiness:ListRules",
                   "route53-recovery-readiness:ListTagsForResources",
                   "route53-recovery-readiness:UpdateCell",
                   "route53-recovery-readiness:UpdateReadinessCheck",
                   "route53-recovery-readiness:UpdateRecoveryGroup",
                   "route53-recovery-readiness:UpdateResourceSet",
                   "route53-recovery-readiness:TagResource",
                   "route53-recovery-readiness:UntagResource"
             ],
            "Resource": "*"
        }
    ]
}
```

------

#### Using service-linked role for readiness check in ARC
<a name="using-service-linked-roles-readiness"></a>

Amazon Application Recovery Controller uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to a service— in this case, ARC. Service-linked roles are predefined by ARC and include all the permissions that the service requires to call other AWS services on your behalf for specific purposes. 

Service-linked roles make setting up ARC easier because you don’t have to manually add the necessary permissions. ARC defines the permissions of its service-linked roles, and unless defined otherwise, only ARC can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your ARC resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-linked role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

ARC has the following service-linked roles, which are described in this chapter:
+ ARC uses the service-linked role named **Route53RecoveryReadinessServiceRolePolicy** to access resources and configurations to check readiness.
+ ARC uses the service-linked role named **** for autoshift practice runs, to monitor customer-provided Amazon CloudWatch alarms and customer Health Dashboard events, and to start practice runs.

##### Service-linked role permissions for Route53RecoveryReadinessServiceRolePolicy
<a name="slr-permissions"></a>

ARC uses a service-linked role named **Route53RecoveryReadinessServiceRolePolicy** to access resources and configurations to check readiness. This section describes the permissions for the service-linked role, and information about creating, editing, and deleting the role.

###### Service-linked role permissions for Route53RecoveryReadinessServiceRolePolicy
<a name="slr-permissions-slr1-permissions"></a>

This service-linked role uses the managed policy `Route53RecoveryReadinessServiceRolePolicy`. 

The **Route53RecoveryReadinessServiceRolePolicy** service-linked role trusts the following service to assume the role:
+ `route53-recovery-readiness.amazonaws.com`

To view the permissions for this policy, see [Route53RecoveryReadinessServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Route53RecoveryReadinessServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

###### Creating the **Route53RecoveryReadinessServiceRolePolicy** service-linked role for ARC
<a name="create-slr"></a>

You don't need to manually create the **Route53RecoveryReadinessServiceRolePolicy** service-linked role. When you create the first readiness check or cross account authorization in the AWS Management Console, the AWS CLI, or the AWS API, ARC creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create the first readiness check or cross account authorization, ARC creates the service-linked role for you again. 

###### Editing the **Route53RecoveryReadinessServiceRolePolicy** service-linked role for ARC
<a name="edit-slr"></a>

ARC does not allow you to edit the **Route53RecoveryReadinessServiceRolePolicy** service-linked role. After you create the service-linked role, you cannot change the name of the role because other entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

###### Deleting the **Route53RecoveryReadinessServiceRolePolicy** service-linked role for ARC
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

After you have removed your readiness checks and your cross-account authorizations, then you can delete the **Route53RecoveryReadinessServiceRolePolicy** service-linked role. For more information about readiness checks, see [Readiness check in ARC](#recovery-readiness). For more information about cross-account authorizations, see [Creating cross-account authorizations in ARC](#recovery-readiness.cross-account).

**Note**  
If the ARC service is using the role when you try to delete the resources, then the service role deletion might fail. If that happens, wait for a few minutes and try the again to delete the role.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the Route53RecoveryReadinessServiceRolePolicy service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

##### Updates to the ARC service-linked role for readiness check
<a name="security-iam-awsmanpol-readiness-updates"></a>

For updates to the AWS managed policies for the ARC service-linked roles, see the [AWS managed policies updates table](#security-iam-awsmanpol-arc-updates) for ARC. You can also subscribe to automatic RSS alerts on the ARC [Document history page](#doc-history).

#### AWS managed policies for readiness check in ARC
<a name="security-iam-awsmanpol-readiness"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

##### AWS managed policy: Route53RecoveryReadinessServiceRolePolicy
<a name="security-iam-awsmanpol-Route53RecoveryReadinessServiceRolePolicy"></a>

You can't attach `Route53RecoveryReadinessServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon Application Recovery Controller (ARC) to access AWS services and resources that are used or managed by ARC. For more information, see [Using service-linked role for readiness check in ARC](#using-service-linked-roles-readiness).

##### AWS managed policy: AmazonRoute53RecoveryReadinessFullAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryReadinessFullAccess"></a>

You can attach `AmazonRoute53RecoveryReadinessFullAccess` to your IAM entities. This policy grants full access to actions for working with recovery readiness (readiness check) in ARC. Attach it to IAM users and other principals who need full access to recovery readiness actions.

To view the permissions for this policy, see [AmazonRoute53RecoveryReadinessFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryReadinessFullAccess.html) in the *AWS Managed Policy Reference*.

##### AWS managed policy: AmazonRoute53RecoveryReadinessReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryReadinessReadOnlyAccess"></a>

You can attach `AmazonRoute53RecoveryReadinessReadOnlyAccess` to your IAM entities. This policy grants read-only access to actions for working with recovery readiness in ARC. It's useful for users who need to view readiness statuses and recovery group configurations. These users can't create, update, or delete recovery readiness resources.

To view the permissions for this policy, see [AmazonRoute53RecoveryReadinessReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryReadinessReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

##### Updates for AWS managed policies for readiness
<a name="security-iam-awsmanpol-readiness-updates"></a>

For details about updates to AWS managed policies for readiness check in ARC since this service began tracking these changes, see [Updates to AWS managed policies for Amazon Application Recovery Controller (ARC)](#security-iam-awsmanpol-arc-updates). For automatic alerts about changes to this page, subscribe to the RSS feed on the ARC [Document history page](#doc-history).

### Quotas for readiness check
<a name="recovery-readiness.quotas"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

Readiness check in Amazon Application Recovery Controller (ARC) is subject to the following quotas (formerly referred to as limits).


| Entity | Quota | 
| --- | --- | 
| Number of recovery groups per account | 5 | 
| Number of cells per account | 15 | 
| Number of nested cells per cell | 3 | 
| Number of cells per recovery group | 3 | 
| Number of resources per cell | 10 | 
| Number of resources per recovery group | 10 | 
| Number of resources per resource set | 6 | 
| Number of resource sets per account | 200 | 
| Number of readiness checks per account | 200 | 
| Number of cross-account authorizations | 100 | 

## Region switch in ARC
<a name="region-switch"></a>

You can use Region switch in ARC to orchestrate large-scale, complex recovery tasks for your application resources across AWS accounts, to help ensure business continuity and reduce operational overhead. Region switch provides a centralized and observable solution that you can perform manually, or automate by using Amazon CloudWatch alarm triggers. If an AWS Region becomes impaired, you can execute the plans that you create by using Region switch to fail over or switch your resources to another Region. This ensures that your application can continue to operate, running in a healthy AWS Region.

Region switch is built around the concept of a *plan*, which you design and configure for your specific recovery needs. Each plan includes *workflows* that are made up of steps. Each step runs one or more *execution blocks*, which Region switch runs in parallel or in sequence, to complete an application recovery. Each execution block handles a different task, such as switching over resources or managing traffic redirection for your application. For even more flexibility, you can create parent plans, by adding child plans to an overall parent plan.

Region switch includes the following:
+ Support for active/passive and active/active configurations. You can failover and failback if you have an active/passive multi-Region configurations, or shift-away and return if your application is set up as active/active in multiple Regions.
+ Cross-account support for application resources that you include in your application recovery. You can also share Region switch plans across accounts.
+ Automatic failover or switchover, by triggering plan execution based on Amazon CloudWatch alarms. Or, you can choose to execute a Region switch plan manually.
+ Full-featured dashboards that give you real-time visibility into the recovery process. 
+ A data plane in each AWS Region, so that you can execute your Region switch plan without taking a dependency on the Region that you’re deactivating. 

Region switch is fully managed by AWS. Using Region switch enables you to benefit from the resilience of a recovery platform that focuses on your application's specific requirements, instead of building and maintaining scripts, and manually gathering data about recoveries.

### About Region switch
<a name="region-switch-plans"></a>

With Region switch, you can orchestrate the specific steps to switch the AWS Region that your multi-Region application is running in. 

Region switch is built around the concept of a *plan*, which you design and configure for your specific recovery needs. Each plan includes *workflows* that are made up of steps. Each step runs one or more *execution blocks*, which Region switch runs in parallel or in sequence, to complete an application recovery. Each execution block handles a different task, such as switching over resources or managing traffic redirection for your application. For even more flexibility, you can create parent plans, by adding child plans.

Whenever you create, or update, a plan, Region switch performs a plan evaluation, to ensure that there aren't issues with IAM permissions, resource configurations, or running capacity. Region switch runs these evaluations regularly, and generates a warning for any issues that it finds.

Region switch also calculates an actual recovery time value for each plan execution, to help you evaluate if the plan is meeting your objectives. You can view recovery time and other details about plan executions in Region switch dashboards in the AWS Management Console. For more information, see [Region switch dashboards](#region-switch.dashboarding-and-reports).

To learn more about each of these areas in Region switch, see the following sections.

#### Region switch plans
<a name="region-switch-plans.plan-overview"></a>

A Region switch plan is the top-level resource in Region switch. You should scope your plan to a specific multi-Region application. A plan enables you to build *workflows* to recover your applications by running a series of Region switch *execution blocks* that activate or deactivate your application and its resources, including cross-account resources, in the AWS Region that you specify.

A plan is made up of one or more workflows, to enable you to activate or deactivate a specific AWS Region. You can configure execution blocks in a workflow to run sequentially, or you can specify that some of the blocks run in parallel.

For a plan that you configure for an active/passive multi-Region approach, you create either one workflow that can be used to activate either of your Regions, or two separate activation workflows, one for each Region. For a plan that you configure for an active/active approach, you create one workflow to activate your Regions and one workflow to deactivate your Regions.

AWS Regions are geographic locations worldwide where AWS clusters data centers. Each Region is designed to be completely isolated from the other Regions, providing fault tolerance and stability. When you use Region switch, you need to consider which Regions your application is deployed in and which Regions you want to use for recovery.

Region switch supports recovery between any two AWS Regions where the service is available. When you configure a Region switch plan, you specify the Regions that your application is deployed in and the recovery approach that you want to use: active/passive or active/active. 

For example, you might have an active/passive multi-Region approach with us-east-1 as the primary Region and us-west-2 as the standby Region. To recover your application from an operational issue that impacts the application in us-east-1, you could execute your Region switch plan to activate us-west-2. This would result in the application switching from resources in us-east-1 to resources in us-west-2.

Region switch plans run using the permissions associated with the IAM role that you specify when you create the plan.

 You can create multiple plans, one for each of your multi-Region applications, and then orchestrate recovery across these plans in your required order by creating a *parent plan*. A parent plan is a plan that uses the Region switch plan execution blocks as steps. The hierarchy of plans is limited to two levels (parent and child), but you can include multiple child plans under the same parent plan.

#### Workflows and execution blocks
<a name="execution-blocks-rs"></a>

After you create a Region switch plan, you must add one or more workflows to the plan, to define the steps you want the plan to perform for your application recovery. For each workflow, you add steps that contain execution blocks. Each execution block performs a specific recovery action, such as scaling up resources or updating routing controls to reroute traffic. Steps organize these execution blocks and control whether they run in parallel or in sequence. By creating parent plans, you can also orchestrate the order in which multiple applications recover into the Region that you're activating.

You organize execution blocks into steps within a workflow. Each step can contain one or more execution blocks that run in parallel, and you arrange steps to run sequentially in your workflow. Also, depending on the resource, you can have the option to run an execution block with graceful (planned) or ungraceful (unplanned) execution.
+ Graceful execution: A planned execution workflow. When your environment is healthy, you can use the graceful workflow to run all steps for an orderly plan execution.
+ Ungraceful execution: An unplanned execution. The ungraceful workflow mode uses only the necessary steps and actions. This mode either changes the behavior of the execution blocks in a workflow or skips specific execution blocks.
+ Post-recovery execution: A workflow that runs after a successful recovery to prepare for future regional events. Post-recovery executions can create read replicas, run custom logic via Lambda functions, add manual approval gates, and embed child plans for complex orchestration. These executions require both Regions to be healthy and run in the Region that was previously impaired.

Finally, you can also configure cross-account resources for an execution block. First, you must configure permissions, by following the guidance in [Cross-account support in Region switch](#cross-account-resources-rs). After you've set up the required IAM roles, then you can add cross-acount resources in the execution blocks in your plan workflows. To add cross-account resources, when you add a step, you specify a target IAM role that has permissions to the resource of other AWS accounts. You also must specify the external ID that you provided in the trust policy for the cross-account role. For details about creating the required IAM roles, see [Cross-account resource permissions](#security_iam_region_switch_cross_account).

To learn more about workflows, see [Create Region switch plan workflows](#working-with-rs-workflows). For details about each type of execution block, including configuration steps, how it works, and what is evaluated as part of plan evaluation, see [Add execution blocks](#working-with-rs-execution-blocks).

#### Plan evaluation
<a name="region-switch-plans.plan-evaluation"></a>

Plan evaluation is an automated process that Region switch runs when a plan is created or updated, and then every 30 minutes after that, during steady state. The evaluation process verifies several critical aspects of plan configuration and resource configurations. The evaluations include verifying IAM permissions, resource configurations, and running capacity.

If Region switch finds an issue that might prevent a successful plan execution, it generates a plan evaluation warning, which is highlighted on the plan details page in the console. You can also consume plan evaluation warnings with Amazon EventBridge, or you can view warnings by using the Region switch API. For more information about the Plan Evaluation API, see [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html) in the *Region Switch API Reference Guide* for Amazon Application Recovery Controller (ARC).

You can see details and suggested remediation for issues that plan evaluation surfaces in the **Plan evaluation** tab on the plan details page. We recommend that you also test application recovery by executing your Region switch plan, and that you don't rely solely on Region switch plan evaluation to test that your recovery plan will work as you expect it to. 

#### Service quota checks
<a name="region-switch-plans.service-quota-checks"></a>

In a multi-Region application, your standby Region often runs at reduced capacity until you need to recover into it. As demand grows in your active Region, you might raise service quotas there to keep up, but forget to request matching increases in your standby Region. This gap can cause a healthy-looking plan to fail during execution, because the standby Region can't launch enough resources to take over. To help you catch these gaps, Region switch performs service quota checks on the compute and database resources in your plan's execution blocks.

A service quota check compares the applied quota values across the accounts and Regions in a plan, and flags any quota whose value is lower in one Region than the value for the matching resource in another Region or account. This comparison is called a parity check. When Region switch finds a mismatch, it can automatically request a service quota increase to raise the lower quota to match the higher one. If Region switch can't submit the request, it surfaces a warning instead. Service quota checks are advisory and run separately from plan evaluation, so they don't delay or block plan evaluation warnings.

**Quota parity doesn't guarantee successful execution**  
A parity check confirms that your Regions have matching quota values. It doesn't guarantee that an execution won't reach a quota limit. For example, an execution can still fail if several plans run at the same time in the same account, or if you increase resource usage in a Region while you're executing a plan.

For more information about how service quota checks work, the permissions they require, and how to view service quota warnings, see [Working with service quota checks](#working-with-rs-service-quota-checks).

#### Automatic plan execution reports
<a name="region-switch-plans.plan-execution-reports"></a>

Region switch can automatically generate comprehensive PDF reports for plan executions to help you meet regulatory compliance requirements. These reports provide evidence of your disaster recovery tests and actual recovery events, including detailed execution timelines, plan configurations, and resource states.

When you configure automatic report generation for a plan, Region switch creates a PDF report after each plan execution completes and delivers it to an Amazon S3 bucket that you specify. Reports are typically available within 30 minutes of execution completion. S3 storage costs apply.

Each report includes:
+ Executive summary with service overview and report creation date
+ Plan configuration details as they existed at execution time
+ Detailed execution timeline with steps, affected resources, and statuses
+ Plan warnings that were present when the execution started
+ Amazon CloudWatch alarm states and alarm history for associated alarms
+ For parent plans, configuration and execution details of child plans
+ Glossary of terms and concepts

To enable automatic report generation, you configure a report output destination when you create or update a plan. You must also ensure that your plan's execution IAM role has the necessary permissions to write reports to your Amazon S3 bucket and access the resources needed to generate the report content. For more information about required permissions, see [Automatic plan execution reports permissions](#security_iam_region_switch_reports).

You can view the status of report generation and download completed reports from the plan execution details page in the console. If report generation encounters errors, such as insufficient permissions or misconfigured Amazon S3 buckets, Region switch provides error details to help you troubleshoot the issue.

Plan evaluation continuously validates your report configuration, including verifying that the execution role has the required IAM permissions. If Region switch detects configuration issues that would prevent successful report generation, it generates warnings that you can view on the plan details page.

#### Regional alarms and actual recovery time
<a name="region-switch-plans.plan-rto"></a>

Region switch calculates an *actual recovery time* value for each plan execution, which you can view after a plan execution. Actual recovery time is shown on the plan execution details page, so that you can compare the actual time to the recovery time objective you specified when you created the plan.

Actual recovery time is calculated as the total of the time is takes for a plan execution to complete, and any additional time that elapses before specific Amazon CloudWatch alarms that you configure return to a green state.

To support calculating an accurate actual recovery time for plan execution, you must configure Regional Amazon CloudWatch alarms for a Region switch plan that provide a signal about the health of your application in each Region. When a plan is executed, Region switch uses these application health alarms to determine when your application is healthy again. Then, Region switch calculates actual recovery time based on the time it takes for your plan to execute added to the time it takes for your application to return to healthy, based on the application health alarms that you configure. 

Before you add CloudWatch alarms to a Region switch plan, make sure that you have the correct IAM policy in place. For more information, see [CloudWatch alarms for application health permissions](#security_iam_region_switch_cloudwatch).

#### AWS Regions
<a name="aws-regions-rs"></a>

Region switch is available in all commercial AWS Regions, as well as AWS GovCloud (US) Regions.

For detailed information about Regional support and service endpoints for Amazon Application Recovery Controller (ARC), see [Amazon Application Recovery Controller (ARC) endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/arc.html) in the *Amazon Web Services General Reference*.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  arc-region-switch.us-east-2.api.aws <br /> arc-region-switch-fips.us-east-2.api.aws  | HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  arc-region-switch.us-east-1.api.aws <br /> arc-region-switch-control-plane-fips.us-east-1.api.aws <br /> arc-region-switch-fips.us-east-1.api.aws <br /> arc-region-switch-control-plane.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  arc-region-switch.us-west-1.api.aws <br /> arc-region-switch-fips.us-west-1.api.aws  | HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  arc-region-switch.us-west-2.api.aws <br /> arc-region-switch-fips.us-west-2.api.aws  | HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  arc-region-switch.af-south-1.api.aws  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  arc-region-switch.ap-east-1.api.aws  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  arc-region-switch.ap-south-2.api.aws  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  arc-region-switch.ap-southeast-3.api.aws  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  arc-region-switch.ap-southeast-5.api.aws  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  arc-region-switch.ap-southeast-4.api.aws  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  arc-region-switch.ap-south-1.api.aws  | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  arc-region-switch.ap-southeast-6.api.aws  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  arc-region-switch.ap-northeast-3.api.aws  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  arc-region-switch.ap-northeast-2.api.aws  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  arc-region-switch.ap-southeast-1.api.aws  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  arc-region-switch.ap-southeast-2.api.aws  | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  arc-region-switch.ap-east-2.api.aws  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  arc-region-switch.ap-southeast-7.api.aws  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  arc-region-switch.ap-northeast-1.api.aws  | HTTPS | 
| Canada (Central) | ca-central-1 |  arc-region-switch.ca-central-1.api.aws  | HTTPS | 
| Canada West (Calgary) | ca-west-1 |  arc-region-switch.ca-west-1.api.aws  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  arc-region-switch.eu-central-1.api.aws  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  arc-region-switch.eu-west-1.api.aws  | HTTPS | 
| Europe (London) | eu-west-2 |  arc-region-switch.eu-west-2.api.aws  | HTTPS | 
| Europe (Milan) | eu-south-1 |  arc-region-switch.eu-south-1.api.aws  | HTTPS | 
| Europe (Paris) | eu-west-3 |  arc-region-switch.eu-west-3.api.aws  | HTTPS | 
| Europe (Spain) | eu-south-2 |  arc-region-switch.eu-south-2.api.aws  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  arc-region-switch.eu-north-1.api.aws  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  arc-region-switch.eu-central-2.api.aws  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  arc-region-switch.il-central-1.api.aws  | HTTPS | 
| Mexico (Central) | mx-central-1 |  arc-region-switch.mx-central-1.api.aws  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  arc-region-switch.me-south-1.api.aws  | HTTPS | 
| Middle East (UAE) | me-central-1 |  arc-region-switch.me-central-1.api.aws  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  arc-region-switch.sa-east-1.api.aws  | HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  arc-region-switch.us-gov-east-1.api.aws <br /> arc-region-switch-fips.us-gov-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  arc-region-switch.us-gov-west-1.api.aws <br /> arc-region-switch-control-plane-fips.us-gov-west-1.api.aws <br /> arc-region-switch-fips.us-gov-west-1.api.aws <br /> arc-region-switch-control-plane.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 

#### Region switch components
<a name="components-rs"></a>

The following are components of, and concepts about, the Region switch feature in Amazon Application Recovery Controller (ARC).

**Plan**  
A plan is the fundamental recovery process for your application. You create a plan by building one or more workflows with execution blocks to be run in sequence or in parallel. Then, when there is a Regional impairment, you execute the plan to complete a recovery for your application by shifting the application to run in a healthy Region.

**Child plan**  
A child plan is a self-contained plan that can be run from within a parent plan, to coordinate more complex application recovery scenarios. You can nest Region switch plans one level.

**Workflow**  
A Region switch plan includes one or more workflows. A workflow is made up of steps that contain execution blocks, which you specify to be run in parallel or in sequence, to complete the activation or deactivation of a Region as part of a recovery plan. For a plan that you configure to have an active/passive approach, you create either one workflow that can be used to activate either of your Regions, or separate activation workflows, one for each Region. For a plan that you configure for an active/active approach, you create one workflow to activate your Regions and one workflow to deactivate your Regions. 

**Execution block**  
You add steps to your Region switch plan workflows containing an execution block. Execution blocks allow you to specify the recovery for multiple applications or resources into an activating Region. When you add a step to a workflow, you can add it in sequence with other steps, or in parallel with one or more other steps.

**Graceful and ungraceful configurations**  
You can choose to run specific execution blocks with graceful (planned) or ungraceful (unplanned) execution. When your environment is healthy, you can use the graceful workflow to run all steps for an orderly plan execution. The ungraceful workflow mode uses only the necessary steps and actions. When you run a plan in ungraceful mode, it either changes the behavior of execution blocks in a workflow or skips specific execution blocks, depending on the type of execution block.  
Specific types of execution blocks have different behavior when they run ungracefully. Details about these differences are described in the section that includes details about each type of execution block. For more information, see [Add execution blocks](#working-with-rs-execution-blocks).

**Active/active and active/passive configurations**  
There are two main approaches to creating a resilient configuration for an application across multiple Regions: active/passive and active/active. Region switch supports application recovery for both of these approaches.  
With an active/passive configuration, you deploy two replicas of your application in two different Regions, with customer traffic only going to one Region.  
With an active/active configuration, you deploy two replicas to two different Regions, but both replicas are processing work or receiving traffic.

**Plan execution**  
When a Region switch plan executes, it implements recovery for an application when a Region becomes impaired by activating a healthy Region for your application and traffic it's receiving. With an active/active configuration, you also run a plan execution to deactivate the impaired Region.

**Application health alarms**  
Application health alarms are CloudWatch alarms that you specify for a plan to indicate the health of your application in each Region. Region switch uses application health alarms to help determine the actual recovery time after you switch Regions to implement recovery.

**Triggers**  
You can use triggers in Region switch to automate application recovery. When you create a trigger, you specify one or more Amazon CloudWatch alarms and define which alarm conditions (such as "red" or "green") should initiate plan execution. When the specified conditions are met, Region switch automatically executes the plan. Triggers are distinct from application health alarms: triggers start plan execution, while application health alarms help Region switch calculate actual recovery time after a plan completes.

**Post-recovery workflow**  
A post-recovery workflow is an optional workflow that runs after a successful recovery to prepare for future regional events. These workflows require both Regions to be healthy and run in the Region that was previously impaired. Post-recovery executions reference the recovery execution ID of the most recent recovery execution.  
Post-recovery workflows support the following execution blocks:  
+ RDS Create Cross-Region Replica
+ Custom Action Lambda
+ Manual Approval
+ Region Switch Plan

**Dashboards**  
Region switch includes dashboards where you can track details about plan executions in real time. 

#### Reliability of Region switch as a recovery platform
<a name="data-and-control-planes-rs"></a>

A recovery mechanism is only useful if it works when you need it most, during an actual Regional impairment. Region switch is designed with reliability as a core principle, so that you can depend on it to orchestrate recovery even when parts of your infrastructure are unavailable. The following factors contribute to the reliability of Region switch as a recovery platform.

##### 1. Data and control plane API decoupling
<a name="reliability-data-control-planes"></a>

As with many AWS services, the functionality for Region switch is divided between a *control plane* and *data planes*. A control plane enables management functions such as creating, updating, and deleting resources. A data plane provides a service's core functionality and is optimized for availability. It is designed to maintain operations even during disruptive events when a control plane might become unavailable.

Region switch decouples these two planes so that all critical recovery capabilities are highly reliable data plane operations. Plan creation and plan updates are control plane operations located in US East (N. Virginia) (us-east-1) and AWS GovCloud (US-West) (us-gov-west-1). Recovery-critical APIs, including plan execution, update execution, pause, cancel, and retrieving open plan evaluation warnings, are all data plane operations.

The best practice is to create your Region switch recovery plan in advance of an actual recovery, and to test it regularly as part of game days and after new deployments. This way, when a real impairment occurs, your recovery depends only on the highly available data plane. For a list of data plane operations, see [Region switch API operations](#actions.region-switch).

##### 2. Plan execution from healthy Region
<a name="reliability-plan-execution-region"></a>

When executing a Region switch plan to recover your application, you execute from the Region you are activating. For active/passive architectures, this means executing from your standby Region, the one you are bringing online. For active/active architectures, where both Regions are already serving traffic, you execute from the healthy Region that will absorb the workload. In both cases, this ensures your recovery does not take a dependency on the Region that is experiencing issues. Region Switch provides an independent console in each AWS Region that calls data plane API operations for recovery tasks, so you can use the console in the target Region to execute plans for application recovery. This design ensures that recovery remains highly reliable and available regardless of the state of the impaired Region.

##### 3. Declarative recovery plans and cross-Region replication
<a name="reliability-declarative-plans"></a>

You can declare Region switch recovery plans as code using Terraform or CloudFormation. This allows you to integrate your recovery plans into the same testing and deployment rigor as your application. Changes go through code review, version control, and CI/CD pipelines, which reduces the risk of configuration drift and untested recovery paths.

Additionally, Region switch allows failover and failback workflows to live in the same plan, and automatically replicates the plan in both Regions. This means a single plan contains everything needed to recover in either direction, and both Regions always have the latest configuration. You don't need to manually synchronize plan configurations across Regions, which eliminates a class of failures where a stale or missing plan in the target Region blocks recovery.

Together, these design choices ensure that Region switch can reliably orchestrate your application recovery during a Regional impairment. For more information about how AWS builds services to meet high availability targets, see the [Static stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) in the Amazon Builders' Library.

#### Tagging for ARC Region switch;
<a name="tagging.region-switch"></a>

Tags are words or phrases (meta data) that you use to identify and organize your AWS resources. You can add multiple tags to each resource, and each tag includes a key and a value that you define. For example, the key might be environment and the value might be production. You can search and filter your resources based on the tags you add.

You can tag the following resource in Region switch in ARC:
+ Plans

Tagging in ARC is available only through the API, for example, by using the AWS CLI. 

The following are examples of tagging in Region switch by using the AWS CLI.

`aws arc-region-switch --region us-east-1 create-plan --plan-name example-plan --tags Region=IAD,Stage=Prod`

For more information, see [TagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TagResource.html) in the *Region Switch API Reference Guide* for Amazon Application Recovery Controller (ARC).

#### Pricing for Region switch in ARC
<a name="pricing-rs"></a>

You pay a fixed monthly cost per Region switch plan that you configure.

For detailed pricing information for ARC and pricing examples, see [ARC Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

### Best practices for Region switch in ARC
<a name="best-practices.region-switch"></a>

We recommend the following best practices for recovery and failover preparedness with Region switch in Amazon Application Recovery Controller (ARC).

**Topics**
+ [Keep purpose-built, long-lived AWS credentials secure and always accessible](#RSBestPracticeCredentials)
+ [Choose lower TTL values for DNS records involved in failover](#RSBestPracticeLowerTTL)
+ [Reserve required capacity for critical applications](#RSBestPracticeCapacity)
+ [Use the extremely reliable data plane API operations to list and get information about Region switch plans](#RSBestPracticeUseDataPlane)
+ [Test failover with ARC](#RSBestPracticeTestFailover)

**Keep purpose-built, long-lived AWS credentials secure and always accessible**  
In a disaster recovery (DR) scenario, keep system dependencies to a minimum by using a simple approach to accessing AWS and performing recovery tasks. Create [ IAM long-lived credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html) specifically for DR tasks, and keep the credentials securely in an on-premises physical safe or a virtual vault, to access when needed. With IAM, you can centrally manage security credentials, such as access keys, and permissions for access to AWS resources. For non-DR tasks, we recommend that you continue to use federated access, using AWS services such as [AWS Single Sign-On](https://aws.amazon.com/single-sign-on/).

**Choose lower TTL values for DNS records involved in failover**  
For DNS records that you might need to change as part of your failover mechanism, especially records that are health checked, using lower TTL values is appropriate. Setting a TTL of 60 or 120 seconds is a common choice for this scenario.  
The DNS TTL (time to live) setting tells DNS resolvers how long to cache a record before requesting a new one. When you choose a TTL, you make a trade-off between latency and reliability, and responsiveness to change. With a shorter TTL on a record, DNS resolvers notice updates to the record more quickly because the TTL specifies that they must query more frequently.  
For more information, see *Choosing TTL values for DNS records* in [Best practices for Amazon Route 53 DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-dns.html). 

**Reserve required capacity for critical applications**  
Region switch includes execution block types that help scale compute resources as part of recovery. If you use these execution blocks in a plan, Region switch does not guarantee that the desired compute capacity with be attained. If you have a critical application and need to guarantee access to capacity, we recommend that you reserve the capacity.   
There are strategies that you can follow to reserve compute capacity in a secondary Region while also limiting cost. To learn more, see [ Pilot light with reserved capacity: How to optimize DR cost using On-Demand Capacity Reservations](https://aws.amazon.com/blogs/architecture/pilot-light-with-reserved-capacity-how-to-optimize-dr-cost-using-on-demand-capacity-reservations/).

**Use the extremely reliable data plane API operations to list and get information about Region switch plans**  
Use data plane API operations to work with and execute your Region switch plan during an event. For a list of Region switch data plane operations, see [Region switch API operations](#actions.region-switch).  
The Region switch console in each Region uses data plane operations for executing Region switch plans. You can also call data plane API operations by using the AWS CLI or by running code that you write using one of the AWS SDKs. ARC offers extreme reliability with the API in the data plane.

**Test application recovery with ARC**  
Test application recovery regularly with ARC Region switch, to activate a secondary application stack in another AWS Region, or to switch over an active-active configuration by running a Region switch plan to deactivate one of the Regions.  
It's important to make sure that the Region switch plans that you've created are aligned with the correct resources in your stack, and that everything works as you expect it to. You should test this after you set up Region switch for your environment, and continue to test periodically, so that you validate that your recovery processes work correctly. Do this testing regularly, before you experience a failure situation, to help avoid downtime for your users.

**ARC Region switch DNS failover versus Route 53 Accelerated recovery**  
 Accelerated recovery provides a target RTO of 60-minutes for APIs used to update your public hosted zone records that are enabled for this capability. If you need to maintain control over your RTO and not wait for AWS to complete recovery of the APIs needed, you should use ARC Routing control or ARC Region switch Route 53 health check execution block. 

### Tutorial: Create an active/passive Region switch plan
<a name="tutorial-region-switch"></a>

This tutorial guides you through creating an active/passive Region switch plan for an application running in us-east-1 and recovering into us-west-2. The example includes Amazon EC2 instances for compute, Amazon Aurora Global Database for storage, and Amazon Route 53 for DNS.

In this tutorial, you'll complete the following steps:
+ Create a Region switch plan
+ Build the plan's workflows and execution blocks
+ Build an EC2 Auto Scaling group execution block
+ Build two manual approval execution blocks
+ Build two custom action Lambda execution blocks
+ Build an Amazon Aurora Global Database execution block
+ Build an ARC routing control block
+ Execute the Region switch plan

#### Prerequisites
<a name="tutorial-rs-prerequisites"></a>

Before you begin this tutorial, verify that you have the following prerequisites in both Regions:
+ IAM roles with appropriate permissions
+ EC2 Auto Scaling groups
+ Lambda functions for maintenance page and fencing
+ Aurora Global Database
+ ARC routing controls

#### Step 1: Create the Region switch plan
<a name="tutorial-rs-create-plan"></a>

1. From the Region switch console, choose **Create Region switch plan**.

1. Provide the following details:
   + **Primary Region**: Choose us-east-1
   + **Standby Region**: Choose us-west-2
   + **Desired recovery time objective (RTO)** (optional)
   + **IAM role**: Enter the plan execution IAM role. This IAM role allows Region switch to call AWS services during execution.

1. Choose **Create**.

(Optional) Add resources from different AWS accounts to your Region switch plan:

1. Create the cross-account role:
   + In the account hosting the resource, create an IAM role.
   + Add permissions for the specific resources that the plan will access.
   + Add a trust policy that allows the execution role to assume the new role.
   + Enter and take note of an external ID that you will use as a shared secret.

1. Configure the resource in your plan:
   + When you add the resource to your plan, specify two additional fields:
     + **crossAccountRole**: The ARN of the role that you created in step 1
     + **externalId**: The external ID that you entered in step 1

Example configuration for an EC2 Auto Scaling execution block accessing resources in account 987654321:

```
{
  "executionBlock": "EC2AutoScaling",
  "name": "ASG",
  "crossAccountRole": "arn:aws:iam::987654321:role/RegionSwitchCrossAccountRole",
  "externalId": "unique-external-id-123",
  "autoScalingGroupArn": "arn:aws:autoscaling:us-west-2:987654321:autoScalingGroup:*:autoScalingGroupName/CrossAccountASG"
}
```

Required permissions:
+ The execution role must have sts:AssumeRole permission for the cross-account role.
+ The cross-account role must have permissions only for the specific resources being accessed.
+ The cross-account role's trust policy must include:
  + The execution role's account as a trusted entity.
  + The external ID condition.
+ For more information on configuring a cross-account role, see [Cross-account resource permissions](#security_iam_region_switch_cross_account).

Before executing the plan, Region switch will verify the following:
+ The execution role can assume the cross-account role.
+ The cross-account role has the required permissions.
+ The external ID matches the trust policy.

#### Step 2: Build the plan's workflows and execution blocks
<a name="tutorial-rs-build-workflows"></a>

1. From the Region switch plan details page, choose **Build workflows**.

1. Select **Build the same activation workflow for all Regions**.

1. Enter a Region activation workflow description (optional). This will be used to easily identify the workflow when executing the plan.

1. Choose **Save and continue**.

##### Add EC2 Auto Scaling execution block
<a name="tutorial-rs-build-workflows-ec2"></a>

For more information about this execution block, see [Amazon EC2 Auto Scaling group execution block](#ec2-auto-scaling-block).

1. Choose **Add a step**, and then select **Run in sequence**.

1. Select the **EC2 Auto Scaling execution block**, and then choose **Add and edit**. This block will allow you to start increasing capacity in the passive Region.

1. In the right panel, configure the block:
   + **Step name**: Enter "Scale"
   + **Step description** (optional)
   + **Auto Scaling group ARN for us-east-1**: The ARN of your ASG in us-east-1
   + **Auto Scaling group ARN for us-west-2**: The ARN of your ASG in us-west-2
   + **Percent to match the source Region's capacity**: Enter 100
   + **Capacity monitoring approach**: Leave as "Most recent"
   + **Timeout** (optional)

   For information about the required IAM permissions for this execution block, see [EC2 Auto Scaling execution block sample policy](#security_iam_region_switch_ec2_autoscaling).

1. Choose **Save step**.

##### Add manual approval execution block
<a name="tutorial-rs-build-workflows-manual-approval-1"></a>

For more information about this execution block, see [Manual approval execution block](#manual-approval-block).

1. Choose **Add a step**.

1. Select the **Manual approval execution block** and add it to the design window. This block allows for human verification before proceeding.

1. In the right panel, configure the block:
   + **Step name**: Enter "Manual approval before setup"
   + **Step description** (optional)
   + **IAM approval role**: The role a user must assume in order to approve the execution
   + **Timeout** (optional). After timeout, execution pauses and you can choose to retry, skip, or cancel.

   For information about the required IAM permissions for this execution block, see [Manual approval execution block sample policy](#security_iam_region_switch_manual_approval).

1. Choose **Save step**.

##### Add custom action Lambda execution block for maintenance page
<a name="tutorial-rs-build-workflows-lambda-maintenance"></a>

For more information about this execution block, see [Custom action Lambda execution block](#custom-action-lambda-block).

1. Choose **Add a step**.

1. Select the **Custom action Lambda execution block**, and then choose **Add and edit**. This block publishes a maintenance page in the Region that is activating.

1. In the right panel, configure the block:
   + **Step name**: Enter "Display maintenance page"
   + **Step description** (optional)
   + **Lambda ARN for activating us-east-1**: The ARN of the maintenance page Lambda function deployed in us-east-1
   + **Lambda ARN for activating us-west-2**: The ARN of the maintenance page Lambda function deployed in us-west-2
   + **Region to run the Lambda function**: Choose **Run in activating Region**
   + **Timeout** (optional)
   + **Retry interval** (optional)

   For information about the required IAM permissions for this execution block, see [Custom action Lambda execution block sample policy](#security_iam_region_switch_lambda).

1. Choose **Save step**.

##### Add Aurora Global Database execution block
<a name="tutorial-rs-build-workflows-aurora"></a>

For more information about this execution block, see [Amazon Aurora Global Database execution block](#aurora-global-database-block).

1. Choose **Add a step**.

1. Select the **Aurora Global Database execution block**, and then choose **Add and edit**. This block triggers an Aurora global database switchover (no data loss). For more information, see [Using switchover or failover for Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) in the *Aurora User Guide*.

1. In the right panel, configure the block:
   + **Step name**: Enter **Aurora switchover**
   + **Step description** (optional)
   + **Aurora global database identifier**: The name of the Aurora cluster
   + **Cluster ARN used for activating us-east-1**: The Aurora cluster ARN in us-east-1
   + **Cluster ARN used for activating us-west-2**: The Aurora cluster ARN in us-west-2
   + **Select the option for Aurora database**: Choose **Switchover**
   + **Timeout** (optional)

   For information about the required IAM permissions for this execution block, see [Aurora Global Database execution block sample policy](#security_iam_region_switch_aurora).

1. Choose **Save step**.

##### Add ARC routing control execution block
<a name="tutorial-rs-build-workflows-routing-control"></a>

For more information about this execution block, see [ARC routing control execution block](#arc-routing-controls-block).

1. Choose **Add a step**.

1. Select **ARC routing control execution block**, and then choose **Add and edit**. This block performs a DNS failover to shift traffic to the passive Region.

1. In the right panel, configure the block:
   + **Step name**: Enter **Toggle DNS**
   + **Step description** (optional)
   + **Routing controls used in activating us-east-1**: Choose **Add routing controls**
   + **Timeout**: Enter a timeout value.

1. Choose **Add routing control**:
   + **Routing control ARN**: The ARN of the routing control that controls us-east-1
   + **Routing control state**: Choose **On**

1. Choose **Add routing control** again:
   + **Routing control ARN**: The ARN of the routing control that controls us-west-2
   + **Routing control state**: Choose **Off**

1. Choose **Save**.

1. **Routing controls used in activating us-west-2**: Choose **Add routing controls**

1. Choose **Add routing control**:
   + **Routing control ARN**: The ARN of the routing control that controls us-west-2
   + **Routing control state**: Choose **On**

1. Choose **Add routing control** again:
   + **Routing control ARN**: The ARN of the routing control that controls us-east-1
   + **Routing control state**: Choose **Off**

1. Choose **Save**.

1. Choose **Save step**.

   For information about the required IAM permissions for this execution block, see [ARC routing controls execution block sample policy](#security_iam_region_switch_arc_routing).

1. Choose **Save**.

#### Step 3: Execute the plan
<a name="tutorial-rs-execute-plan"></a>

1. On the Region switch plan details page, in the top right, choose **Execute**.

1. Enter the execution details:
   + Select the Region to activate.
   + Select the plan execution mode.
   + (Optional) View the execution steps.
   + Acknowledge the plan execution.

1. Choose **Start**.

1. You can view detailed steps as the plan executes on the execution details page. You can see each step in the plan execution, including start time, end time, resource ARN, and log messages.

When the impaired Region has recovered, you can execute the plan again (changing the parameters that you provide) to activate the original Region, to switch back your application operations to the original primary Region.

### Tutorial: Configure plan execution report autogeneration
<a name="tutorial-report-generation"></a>

This tutorial guides you through configuring plan execution report autogeneration for a Region switch plan. Reports provide comprehensive PDF documentation of plan executions for compliance purposes.

In this tutorial, you'll complete the following steps:
+ Create an Amazon S3 bucket for report storage
+ Enable report autogeneration on a Region switch plan
+ Execute the plan and download the report

#### Prerequisites
<a name="tutorial-report-prerequisites"></a>

Before you begin this tutorial, verify that you have the following:
+ An existing Region switch plan with configured workflows
+ Permissions to create Amazon S3 buckets
+ Your plan's execution IAM role configured with the required permissions. For more information, see [Automatic plan execution reports permissions](#security_iam_region_switch_reports).

#### Step 1: Create an Amazon S3 bucket for reports
<a name="tutorial-report-create-bucket"></a>

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**.

1. Provide the following details:
   + **Bucket name**: Enter a unique name, such as `my-region-switch-reports`
   + **Block Public Access settings**: Keep all public access blocked (recommended)
   + **Bucket Versioning**: Enable versioning (optional but recommended)
   + **Default encryption**: Select the encryption. If using SSM-KMS, the planExecutionRole needs kms:Encrypt and kms:GenerateDataKey permissions on the s3 bucket's default CMK

1. Choose **Create bucket**.

1. Note the bucket name for use in the next step.

#### Step 2: Enable report autogeneration on your plan
<a name="tutorial-report-enable-reports"></a>

1. Open the Region switch console at [https://console.aws.amazon.com/route53recovery/regionswitch/home](https://console.aws.amazon.com/route53recovery/regionswitch/home).

1. Select the plan you want to configure reports for.

1. Choose **In the navigation bar, go to Actions and select Edit plan details**.

1. In the **Report settings** section, provide the following:
   + Select **Enable report autogeneration**
   + **Amazon S3 URI:** Select or enter the bucket S3 URI you created in Step 1
   + **Account ID that owns bucket:** Enter the bucket owner account ID

1. Choose **Save**.

1. Wait for plan evaluation to complete. If there are any configuration issues, warnings will appear on the plan details page.

#### Step 3: Execute the plan and download the report
<a name="tutorial-report-execute-download"></a>

1. On the plan details page, choose **Execute**.

1. Complete the plan execution as normal, selecting the Region to activate and execution mode.

1. After the plan execution completes, navigate to the execution details page.

1. In the **Plan execution report** section, monitor the report generation status. Report generation typically completes within 30 minutes of execution completion.

1. When the report status shows **Completed**, choose **Download plan execution report** to download the PDF.

1. Alternatively, navigate to your Amazon S3 bucket to access the report directly. Reports are stored with the following naming pattern: `ExecutionReport-${planVersion.ownerAccountId}-${planName}-${execution.regionTo}-${event.executionId}-${dateStr}.pdf`

The generated report includes:
+ Executive summary with service overview and report creation date
+ Plan configuration details as they existed at execution time
+ Detailed execution timeline with steps, affected resources, and statuses
+ Plan warnings that were present when the execution started
+ Amazon CloudWatch alarm states and alarm history for associated alarms
+ For parent plans, configuration and execution details of child plans
+ Glossary of terms and concepts

#### Troubleshooting
<a name="tutorial-report-troubleshooting"></a>

If report generation fails, check the following:
+ **Permission errors**: Verify that the execution role has the correct IAM permissions. For more information, see [Automatic plan execution reports permissions](#security_iam_region_switch_reports). Check the plan evaluation warnings for specific permission issues.
+ **Amazon S3 bucket access**: Ensure the Amazon S3 bucket exists and is accessible from the Region where the plan is configured. Verify that bucket policies don't block access from the execution role.
+ **Bucket encryption**: If using customer-managed KMS keys for bucket encryption, ensure the execution role has permissions to use the KMS key.

For additional help, view detailed error messages on the execution details page or contact AWS Support.

### Tutorial: Execute an RDS post-recovery workflow
<a name="tutorial-post-recovery"></a>

This tutorial guides you through executing a post-recovery workflow after a successful RDS failover. This post-recovery execution restores redundancy by re-establishing cross-Region replication for the RDS database, ensuring your RDS database is prepared for future regional events.

In this tutorial, you'll complete the following steps:
+ Verify prerequisites for post-recovery execution
+ Create a post-recovery workflow with RDS Create Cross-Region Replica execution block
+ Execute the post-recovery workflow

#### Prerequisites
<a name="tutorial-post-recovery-prerequisites"></a>

Before you begin this tutorial, verify that you have the following:
+ A Region switch active/passive plan with an activate workflow that includes an RDS Promote Read Replica execution block
+ A successful activate execution that promoted a read replica in the other Region
+ Both Regions are healthy and accessible
+ The execution ID from the most recent recovery execution

#### Step 1: Create a post-recovery workflow
<a name="tutorial-post-recovery-create-workflow"></a>

1. From the Region switch console choose the plan, choose **Edit workflows**, select **Config**, check **Include post recovery workflow in the plan** and save.

1. In the Edit workflows page, Select the **Select a workflow to add steps** drop down and choose **Post-recovery**.

1. Choose **Add a step**.

1. Select the **Amazon RDS create cross Region replica execution block**.

1. In the right panel, configure the block:
   + **Step name**: Enter "Create cross-Region read replica"
   + **Step description** (optional)
   + **RDS DB instance ARN for primary Region**: The ARN of the database in primary Region, should be the same as the promote read replica step
   + **RDS DB instance ARN for secondary Region**: The ARN of the promoted database in secondary, should be the same as the promote read replica step
   + **Timeout** (optional): Enter a timeout value, such as 90 minutes

   For information about the required IAM permissions for this execution block, see [Amazon RDS execution block sample policy](#security_iam_region_switch_rds).

1. Choose **Save step**.

1. Choose **Save workflow**.

#### Step 2: Execute the post-recovery workflow
<a name="tutorial-post-recovery-execute"></a>

1. On the Region switch plan details page, in the top right, choose **Execute post-recovery**.

1. Enter the execution details:
   + **Recovery execution ID**: Enter the execution ID of the most recent recovery execution. This field is used to identify the Region that is active currently.
   + **Region to execute in**: Select the inactive Region which is not receiving any application traffic. This is the Region where a read replica will be created.

1. Review the execution steps and acknowledge the execution.

1. Choose **Start Execution**.

1. Monitor the execution progress on the execution details page. The RDS Create Cross-Region Replica execution block will rename your old primary instance and create a new read replica in the previously impaired Region.

After the post-recovery execution completes successfully, your application will have cross-Region replication re-established, and you'll be prepared for future regional events. You can verify if the new read replica was created by checking the RDS console in the target Region. The old primary will be renamed and tagged with *renamedByRegionSwitch*.

**Important**  
Region switch validates that the recovery execution ID matches the last known execution for the plan. If the execution ID is invalid or is not ID of the last known recovery execution, the post-recovery execution will not run.

### Region switch API operations
<a name="actions.region-switch"></a>

The following table lists ARC operations that you can use for Region switch, with links to relevant documentation.


| Action | Using the ARC console | Using the ARC API | Data plane API | 
| --- | --- | --- | --- | 
| Approve or deny a plan execution step | See [Manual approval execution block](#manual-approval-block) | See [ApprovePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ApprovePlanExecutionStep.html) | Yes | 
| Cancel a plan execution | See [Create a Region switch plan](#working-with-rs-create-plan) | See [CancelPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CancelPlanExecution.html) | Yes | 
| Create a plan | See [Create a Region switch plan](#working-with-rs-create-plan) | See [CreatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CreatePlan.html) | No | 
| Delete a plan | See [Working with Region switch](#working-with-rs) | See [DeletePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_DeletePlan.html) | No | 
| Get a plan | See [Working with Region switch](#working-with-rs) | See [GetPlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlan.html) | No | 
| Get plan evaluation status | See [Plan evaluation](#region-switch-plans.plan-evaluation) | See [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html) | Yes | 
| Get a plan execution | See [Region switch dashboards](#region-switch.dashboarding-and-reports) | See [GetPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanExecution.html) | Yes | 
| Get a plan in Region | See [Working with Region switch](#working-with-rs) | See [GetPlanInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanInRegion.html) | Yes | 
| List plan execution events | See [Execute a Region switch plan to recover an application](#plan-execution-rs) | See [ListPlanExecutionEvents](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutionEvents.html) | Yes | 
| List plan executions | See [Execute a Region switch plan to recover an application](#plan-execution-rs) | See [ListPlanExecutions](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutions.html) | Yes | 
| List plans | See [Working with Region switch](#working-with-rs) | See [ListPlans](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlans.html) | No | 
| List plans in Region | See [Working with Region switch](#working-with-rs) | See [ListPlansInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlansInRegion.html) | Yes | 
| List Route 53 health checks for a plan | See [Amazon Route 53 health check execution block](#route53-health-check-block) | See [ListRoute53HealthChecksForPlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecks.html) | No | 
| List Route 53 health checks for a plan in Region | See [Amazon Route 53 health check execution block](#route53-health-check-block) | See [ListRoute53HealthChecksForPlanInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecksInRegion.html) | Yes | 
| List tags for a resource | See [Tagging for ARC Region switch;](#tagging.region-switch) | See [ListTagsForResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListTagsForResource.html) | No | 
| Start a plan execution | See [Execute a Region switch plan to recover an application](#plan-execution-rs) | See [StartPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_StartPlanExecution.html) | Yes | 
| Tag a resource | See [Create a Region switch plan](#working-with-rs-create-plan) | See [TagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TagResource.html) | No | 
| Remove tags from a resource | See [Tagging for ARC Region switch;](#tagging.region-switch) | See [UntagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UntagResource.html) | No | 
| Update a plan | See [Create a Region switch plan](#working-with-rs-create-plan) | See [UpdatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlan.html) | No | 
| Update a plan execution | See [Create a Region switch plan](#working-with-rs-create-plan) | See [UpdatePlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecution.html) | Yes | 
| Update a plan execution step | See [Create a Region switch plan](#working-with-rs-create-plan) | See [UpdatePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecutionStep.html) | Yes | 

### Working with Region switch
<a name="working-with-rs"></a>

This section provides step-by-step instructions for working with Region switch plans, which you can use to recover multi-Region applications. Region switch enables you to create plans for both active/passive and active/active recovery approaches.

To create a recovery plan for your application, you do the following:

1. Create a Region switch plan. A plan is a structure with certain attributes, such as the specific AWS Regions that your application runs in. Each plan includes one or more *workflows*.

   Optionally, you can create several plans, and nest those *child plans* within an overall recovery plan.

1. Create a workflow for the plan. You can’t execute a plan without creating a workflow first.

1. In the workflow, add one or more steps that are each an *execution block*.

   For example, you could add a step to scale up EC2 Auto Scaling groups in a destination Region.

1. After you add steps to your workflow, additional steps might be required, such as configuring health checks in Amazon Route 53. Each execution block section includes the configuration information that you need. For more information, see [Add execution blocks](#working-with-rs-execution-blocks).

1. To recover your application when it's running in an impaired AWS Region, execute the plan.

   You can track the progress of a plan execution by viewing information in the global dashboard or a Regional dashboard.

The following sections provide detailed information and steps for creating a plan and workflows, and adding execution block steps in your workflows.

**Topics**
+ [Plan evaluation](#working-with-rs-plan-evaluation)
+ [Service quota checks](#working-with-rs-service-quota-checks)
+ [Create a plan](#working-with-rs-create-plan)
+ [Create workflows](#working-with-rs-workflows)
+ [Add execution blocks](#working-with-rs-execution-blocks)
+ [Create child plans](#working-with-rs-child-plan)
+ [Create triggers](#working-with-rs-triggers)
+ [Execute a plan](#plan-execution-rs)

The procedures in this section illustrate how to work with plans, workflows, execution blocks, and triggers by using the AWS Management Console. To work with Region switch API operations instead, see [Region switch API operations](#actions.region-switch).

#### Plan evaluation for Region switch plans
<a name="working-with-rs-plan-evaluation"></a>

When you create a multi-Region recovery plan, you need confidence that the plan will execute successfully, without errors, when you need it most. With Region switch plan evaluation, you can continuously validate your plan's configuration and permissions, and identify issues before they block a recovery.

##### How can you use plan evaluation
<a name="working-with-rs-plan-evaluation-how"></a>

Plan evaluation runs check the resource configurations and IAM permissions in your plan, and surface execution-blocking warnings that you can proactively resolve. You don't need to configure or opt in to plan evaluation. With every Region switch plan, you get plan evaluation automatically. Region switch automatically evaluates your plan multiple times per hour. If any checks fail, Region switch returns warning messages that you can view in the AWS Management Console. You can also receive validation warnings through Amazon EventBridge or by using the [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html) API.

##### What is evaluated by execution block
<a name="working-with-rs-plan-evaluation-checks"></a>

Region switch performs specific checks for each execution block type in your plan. The following table lists the checks performed for each execution block.


**Plan evaluation checks by execution block**  


- **[Amazon EC2 Auto Scaling group execution block](#ec2-auto-scaling-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that Auto Scaling groups exist and are accessible to Region switch via the plan's configured execution role or cross-account role.
  - **Check category:** Capacity / **Description:** Checks that the maximum capacity of the target Region's Auto Scaling group is sufficient to scale up to the source Region's capacity.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Auto Scaling operations. If the plan has service quota checks enabled, also checks that the role has the permissions required to read and compare quotas for this execution block (for example, servicequotas:GetServiceQuota, autoscaling:DescribeAutoScalingGroups, and ec2:DescribeInstances).

- **[Amazon EKS resource scaling execution block](#eks-resource-scaling-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Amazon EKS cluster exists and the Kubernetes resource is present in the cluster.
  - **Check category:** Kubernetes permissions / **Description:** Checks that the IAM role is mapped to the AmazonARCRegionSwitchScalingPolicy EKS Access Entry so Region switch can act on the Kubernetes resources. The EKS Access Entry policy is not mandatory as long as the required EKS permissions are supplied through k8 User Groups.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon EKS operations. If the plan has service quota checks enabled, also checks that the role has the permissions required to read and compare quotas for this execution block (for example, servicequotas:GetServiceQuota and eks:ListNodegroups).

- **[Amazon ECS service scaling execution block](#ecs-service-scaling-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Amazon ECS cluster and service exist and are correctly associated.
  - **Check category:** Capacity / **Description:** Checks that the maximum autoscaling capacity of the target Amazon ECS service is sufficient to handle the required traffic load during failover.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon ECS operations. If the plan has service quota checks enabled, also checks that the role has the permissions required to read and compare quotas for this execution block (for example, servicequotas:GetServiceQuota and ecs:DescribeServices).

- **[ARC routing control execution block](#arc-routing-controls-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the routing control exists and the role is authorized to access the control panel.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for routing control operations.

- **[Amazon Aurora Global Database execution block](#aurora-global-database-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the global cluster exists, DB clusters are members of the global cluster, DB clusters are in an available state, and DB instances exist in both clusters.
  - **Check category:** Engine compatibility / **Description:** Checks that the engine version supports switchover and that clusters have compatible versions across Regions.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Aurora failover and switchover.

- **[Aurora Provisioned Scaling execution block](#aurora-provisioned-scaling-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that instance and cluster ARNs are well-formed, instances exist, instances belong to the expected cluster, and clusters are members of the specified global cluster.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Aurora provisioned scaling. If the plan has service quota checks enabled, also checks that the role has the permissions required to read and compare quotas for this execution block (for example, servicequotas:GetServiceQuota and rds:DescribeDBInstances).

- **[Aurora Serverless Scaling execution block](#aurora-serverless-scaling-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that Aurora Serverless clusters are present in the expected Regions and contain Serverless v2 instances.
  - **Check category:** Capacity / **Description:** Checks that the scaling target for the target Region's cluster is within the 256 ACU limit.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Aurora Serverless scaling.

- **[Amazon DocumentDB Global Cluster execution block](#documentdb-global-cluster-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the global cluster exists, clusters are members of the global cluster, clusters are in an available state, and instances exist in both clusters.
  - **Check category:** Engine compatibility / **Description:** Checks that cluster engine versions are compatible and the global cluster has the expected engine type.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon DocumentDB failover and switchover.

- **[Amazon Neptune Global Cluster execution block](#neptune-global-database-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the global cluster exists, DB clusters are members of the global cluster, DB clusters exist in both Regions, and DB clusters are in an available state.
  - **Check category:** Engine compatibility / **Description:** Checks that engine versions are consistent across regional clusters and meet the minimum required version for failover/switchover.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon Neptune failover and switchover.

- **[Amazon RDS Promote Read Replica execution block](#rds-promote-read-replica-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that DB instances exist, instances in non-primary Regions are read replicas, and the source instance is correctly configured for replication.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon RDS read replica promotion.

- **[Amazon RDS Create Cross-Region Replica execution block](#rds-create-cross-region-replica-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that DB instances exist and backup is enabled on the source instance.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for creating Amazon RDS read replicas. If the plan has service quota checks enabled, also checks that the role has the permissions required to read and compare quotas for this execution block (for example, servicequotas:GetServiceQuota and rds:DescribeDBInstances).

- **[Amazon RDS Switchover Read Replica execution block](#rds-switchover-read-replica-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the standby instance is in mounted or open read-only state, is actively replicating, and has automatic backups enabled.
  - **Check category:** Engine compatibility / **Description:** Checks that the engine version supports switchover (Oracle 19c or higher) and that both instances have the same engine version.
  - **Check category:** Configuration / **Description:** Checks that no pending maintenance actions block switchover and that the option group is exclusive to the replication configuration.

- **[Manual approval execution block](#manual-approval-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the manual approval IAM role ARN is well-formed and the role exists.
  - **Check category:** Configuration / **Description:** Checks that the manual approval role is in the same account that owns the plan.
  - **Check category:** IAM permissions / **Description:** Checks that the approver role has the arc-region-switch:ApprovePlanExecutionStep permission.

- **[Custom action Lambda execution block](#custom-action-lambda-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Lambda function exists and is in an Active state.
  - **Check category:** Configuration / **Description:** Checks that the Lambda function concurrency is greater than 0, that a dry-run invocation succeeds, and that durable Lambda functions have an execution timeout of 15 minutes or less.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Lambda execution.

- **[Lambda event source mapping execution block](#lambda-event-source-mapping-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Lambda event source mapping exists and the associated Lambda function exists and is in an Active state.
  - **Check category:** Configuration / **Description:** Checks that the Lambda function for the Lambda event source mapping has reserved concurrency greater than 0.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for managing event source mappings.

- **[Amazon Route 53 health check execution block](#route53-health-check-block)**
  - **Check category:** Resource accessibility / **Description:** Checks that the hosted zone exists and record sets can be mapped to the configured Regions.
  - **Check category:** Configuration / **Description:** Checks that the Region switch-allocated health check is associated with the correct record set.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role is authorized to access the hosted zone.



**Note**  
When an execution block accesses a resource in a different AWS account through a cross-account role, grant that cross-account role the same permissions listed for the block in the preceding table. Region switch assumes the cross-account role to perform these checks, so the cross-account role must have the required IAM and service quota permissions for the resource that it accesses.

##### Plan-level evaluation checks
<a name="working-with-rs-plan-evaluation-plan-level"></a>

In addition to execution block checks, Region switch evaluates plan-level configurations including triggers, report generation, and application health alarms.


**Plan-level evaluation checks**  


- **Triggers**
  - **Check category:** Resource accessibility / **Description:** Checks that the CloudWatch alarm configured for the trigger exists and is accessible with the configured role.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's execution role has the arc-region-switch:StartPlanExecution permission required for automated trigger-based execution.

- **Report generation**
  - **Check category:** IAM permissions / **Description:** Checks that the plan's execution role has the s3:PutObject permission required to write reports to the configured Amazon S3 bucket.
  - **Check category:** Role assumption / **Description:** Checks that the plan's execution role can be assumed for report generation validation.

- **Application health alarms**
  - **Check category:** Resource accessibility / **Description:** Checks that the CloudWatch alarm exists and is accessible with the configured role.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's role has cloudwatch:DescribeAlarms and cloudwatch:DescribeAlarmHistory permissions required to validate alarm state.
  - **Check category:** Cross-account configuration / **Description:** Checks that the external ID is provided and valid when a cross-account role is specified for the alarm.



#### Working with service quota checks
<a name="working-with-rs-service-quota-checks"></a>

In a multi-Region application, your standby Region often runs at reduced capacity until you need to recover into it. As demand grows in your active Region, you might raise service quotas there to keep up, but forget to request matching increases in your standby Region. This gap can cause a healthy-looking plan to fail during execution, because the standby Region can't launch enough resources to take over. To help you catch these gaps, Region switch performs service quota checks on the compute and database resources in your plan's execution blocks.

##### Configuration
<a name="working-with-rs-service-quota-checks-configuration"></a>

Service quota checks are controlled by the `serviceQuotaChecksEnabled` setting on a plan. New plans have service quota checks enabled by default; plans that you created before service quota checks were available have them disabled by default.

To change the setting, set `serviceQuotaChecksEnabled` to `true` or `false` with the Region switch API, the AWS CLI, or AWS CloudFormation. In the console, select **Enable service quota warnings** or **Disable service quota warnings** on the **Edit plan details** page. When you update a plan without specifying the field, Region switch keeps the plan's current setting.

##### How it works
<a name="working-with-rs-service-quota-checks-how"></a>

Region switch service quota checks compare the applied quota limits for resources defined in the plan, in each Region and account, to identify and attempt to remediate mismatches which could prevent recovery operations.

When Region switch finds a Region or account whose applied quota is lower than the matching one, it can request an increase to raise the lower quota to match the higher one. This helps ensure that either Region can provision the capacity that the plan requires, preventing constraints during failover.

Frequency of checks: Quota checks run automatically within 30 minutes of plan creation or update, and then every 24 hours. This cadence is independent of plan evaluation.

Request limits: To avoid exhausting the account-level limit on open quota increase requests, Region switch uses at most half of the allowed open requests, reserving the rest for your own submissions. In practice:
+ Commercial Regions: Up to 5 concurrent requests per account per Region
+ Opt-in Regions: Up to 1 concurrent request per account

When this limit is reached, additional mismatches are surfaced as warnings. Once open requests are approved or resolved, Region switch submits the remaining increases on the next check cycle.

**Note**  
Quota checks enforce parity between Regions only. They do not adjust quotas based on current resource consumption.

##### Service quotas that Region switch checks
<a name="working-with-rs-service-quota-checks-quotas"></a>

Region switch determines which service quotas are relevant to a plan based on the compute and database resources in the plan's execution blocks. For example, on a compute execution block, Region switch identifies the resource to scale (an Amazon EC2 Auto Scaling group, an Amazon ECS service, or an Amazon EKS cluster). It describes the resource to determine the instance families and configuration it uses, and then maps that configuration to the service quotas the resource consumes.

###### Permissions
<a name="working-with-rs-service-quota-checks-permissions"></a>

For Region switch to perform service quota checks, grant the required permissions to the IAM role that Region switch uses to access your resources. Region switch performs service quota checks only for plans whose execution role, and any cross-account roles that the plan uses, include these permissions.
+ `servicequotas:GetServiceQuota` allows Region switch to read applied quota values and generate warnings when it finds a mismatch.
+ `servicequotas:RequestServiceQuotaIncrease` and `servicequotas:GetRequestedServiceQuotaChange` allow Region switch to automatically submit quota increase requests on your behalf.

To determine which quotas to check, Region switch also needs `Describe` and `List` permissions for the resources in the plan. Grant the permissions for the execution block types that the plan uses.

An Amazon EC2 Auto Scaling group sometimes has no running instances, such as in a standby Region that is scaled to zero. In this case, Region switch determines the instance families from the group's launch template or launch configuration. This way, Region switch can still perform a parity check. When the group has running instances, Region switch uses those instances as the source of truth instead.

If a role is missing a required permission, plan evaluation surfaces a warning that identifies the missing permission instead of the quota result. Review these plan evaluation warnings to learn which permissions to grant. For cross-account resources, grant these permissions to the cross-account role for each account that contains resources in the plan. For more information about the permissions that Region switch requires, see [Identity and Access Management for Region switch in ARC](#security-iam-region-switch).

**Note**  
Service Quotas requires a service-linked role in each account where quota increase requests are made, in order to create support cases. Quota increase requests fail if the service-linked role has never been created in an account. To create a service-linked role, submit a service quota increase request in your account. To let Region switch submit the first quota increase request in an account, grant `iam:CreateServiceLinkedRole` at the account level. This permission is needed only until the service-linked role exists.

**Note**  
Submitting a service quota increase request doesn't create any resources and doesn't change the resources in your account. Service quota increase requests can take several hours, or in some cases days, to be applied.

###### Service quotas that Region switch checks by execution block
<a name="working-with-rs-service-quota-checks-by-block"></a>


| Execution block | Service quotas checked | Permissions required in the execution role | 
| --- | --- | --- | 
| Amazon EC2 Auto Scaling | On-Demand and Spot instance vCPUs per instance family; Amazon EBS storage and IOPS per volume type; network interfaces per Region (when applicable). | autoscaling:DescribeAutoScalingGroups, autoscaling:DescribeLaunchConfigurations, ec2:DescribeInstances, and ec2:DescribeLaunchTemplateVersions | 
| Amazon ECS service scaling | On-Demand and Spot instance vCPUs per instance family (Amazon ECS on Amazon EC2); Fargate vCPUs for On-Demand and Spot (Amazon ECS on Fargate); Amazon EBS storage and IOPS per volume type; network interfaces per Region (when applicable). | ecs:DescribeServices, ecs:DescribeTaskDefinition, ecs:DescribeClusters, and ecs:DescribeCapacityProviders | 
| Amazon EKS resource scaling | On-Demand and Spot instance vCPUs per instance family (Amazon EC2 managed node groups); Fargate vCPUs for On-Demand and Spot (Fargate profiles); Amazon EBS storage and IOPS per volume type; network interfaces per Region (when applicable). | eks:ListNodegroups, eks:DescribeNodegroup, and eks:ListFargateProfiles | 
| Amazon RDS create cross-Region replica and Aurora provisioned scaling | Amazon RDS DB instances per Region; total storage for all DB instances per Region. | rds:DescribeDBInstances | 

##### Remediating service quota warnings
<a name="working-with-rs-service-quota-checks-remediating"></a>

Service quota warnings identify quotas in your recovery plan where one Region's applied value is lower than the matching Region's. You can view these warnings on the Service quota warnings tab under the Plan evaluation tab in the console, or retrieve them programmatically using the [ListServiceQuotaWarnings](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListServiceQuotaWarnings.html) API.

###### Retrieving warnings
<a name="working-with-rs-service-quota-checks-retrieving"></a>

The `ListServiceQuotaWarnings` API returns warnings for all plans accessible to the caller, including plans you own and plans shared with your account through AWS Resource Access Manager. To narrow the results, provide a list of plan Amazon Resource Names (ARNs). Region switch ignores any plan ARN that the caller cannot access. If no plan ARNs are specified, Region switch returns warnings for all accessible plans.

**Note**  
Service quota warnings are separate from plan evaluation warnings retrieved with [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html). Plan evaluation reports whether the plan's execution role is missing IAM permissions required by service quota checks. It does not report quota mismatches or the status of quota increase requests. Those details appear only in the service quota warnings returned by `ListServiceQuotaWarnings`. For more information, see the [Region Switch API Reference Guide](https://docs.aws.amazon.com/arc-region-switch/latest/api/Welcome.html) for Amazon Application Recovery Controller (ARC). For an overview of service quota checks, see [Service quota checks](#region-switch-plans.service-quota-checks).

###### Warning details
<a name="working-with-rs-service-quota-checks-warning-details"></a>

Each service quota warning includes the following information:
+ The affected service and quota
+ The Region and account where the quota is insufficient
+ If Region switch submitted an increase request, the request ID and support case ID

Because service quotas are scoped to the account and Region level, a single quota mismatch can affect more than one plan.

###### Warning lifecycle
<a name="working-with-rs-service-quota-checks-warning-lifecycle"></a>

A service quota warning follows this lifecycle:
+ Increase request submitted: When Region switch submits a quota increase request, the warning remains on the plan while the request is open. After the request is approved and the new quota value is applied, Region switch removes the warning on the next check cycle.
+ Increase request denied: If the request is denied, the warning persists. Region switch submits a new request after a cooldown period, provided the mismatch still exists.
+ Increase request not submitted: When Region switch cannot submit an increase request, the warning remains until the mismatch is resolved. This can occur when Region switch has reached its limit on open requests, or when the account has reached the maximum number of open requests.

The mismatch resolves when one of the following occurs:
+ You request the increase yourself.
+ The resources in the plan change such that the existing quota is sufficient.
+ You remove the affected execution block from the plan.

**Canceling a service quota increase request**  
Service quota increase requests submitted by Region switch cannot be canceled through the Region switch API. To cancel a request, respond to the associated AWS Support case.

**Service quota warnings don't block plan execution**  
A service quota warning doesn't prevent you from executing a plan. Executing a plan while a service quota warning is active carries the same risk as executing any plan whose recovery Region has a lower quota than the matching Region: the execution can fail. Service quota warnings appear in the console when you start a plan execution, and in plan execution reports, so that you can decide whether to proceed.

#### Create a Region switch plan
<a name="working-with-rs-create-plan"></a>

You can create two different kinds of plans in Region switch: an active/active plan or an active/passive plan. When you create a plan, specify the type that applies to how you want to manage failover.
+ An *active/passive* approach deploys two application replicas into two Regions, with traffic routed to the active Region only. You can activate the replica in the passive Region by executing the Region switch plan.
+ An *active/active* approach deploys two application replicas into two Regions, and both replicas are processing work or receiving traffic.

#### To create a Region switch plan


1. From the Region switch console, choose **Create Region switch plan** with active/passive approach.

1. Provide the following details:
   + **Plan name** - Enter a descriptive name for your plan.
   + **Multi-Region approach** - Select **Active/passive** or **Active/active**. This approach means two application replicas are deployed into two Regions, with traffic routed into the active Region only. You can activate the replica in the passive Region by executing the Region switch plan.
     + Choose **active/passive** if you have deployed two application replicas into two Regions, with traffic routed to the active Region only. Then, you can activate the replica in the passive Region by executing the Region switch plan that specifies *Active/passive*.
     + Choose **Active/active** if you have deployed two application replicas into two Regions, and both replicas are processing work or receiving traffic.
   + **Primary and standby Regions** or **Regions** - Select the primary and standby Regions for your application. For an active/active deployment, select the Regions where the replicas are deployed.
   + **Recovery time objective (RTO)** - Enter your desired RTO. Region switch uses this to provide insight into how long Region switch plan executions take to complete in comparison to your desired RTO.
   + **IAM role** - Provide an IAM role for Region switch to use to execute the plan. For more information about permissions, see [Identity and Access Management for Region switch in ARC](#security-iam-region-switch).
   + **Amazon CloudWatch alarm** - Provide an application health alarm that you've created with Amazon CloudWatch, to indicate the health of your application in each Region. Region switch uses these application health alarms to help determine the actual recovery time after you switch Regions to implement recovery.

     Before you add CloudWatch alarms to a Region switch plan, make sure that you have the correct IAM policy in place. For more information, see [CloudWatch alarms for application health permissions](#security_iam_region_switch_cloudwatch).
   + **Automatic report generation** - Optionally, enable automatic report generation for plan executions. When enabled, Region switch generates a comprehensive PDF report after each plan execution completes and delivers it to an Amazon S3 bucket that you specify. Provide the Amazon S3 URI and the account ID that owns the bucket.

     Before enabling automatic report generation for plans, make sure that you have the correct IAM policy in place. For more information about report generation and required permissions, see [Automatic plan execution reports](#region-switch-plans.plan-execution-reports).
   + **Tags** - Optionally, add one or more tags to your plan.

#### Create Region switch plan workflows
<a name="working-with-rs-workflows"></a>

After you create a Region switch plan, you need to define and create workflows that specify the recovery process for your application. For each plan, you define one or more workflows that complete recovery for your application. In each workflow, you add steps that include *execution blocks* that define each action you want Region switch to perform for your application recovery.

The number of workflows that you create depends on your application deployment scenario and your preferences for managing recovery. For example:
+ If your Region switch plan is for an active/active application deployment, you also need to create a deactivation workflow. This means that for or active/active deployments, you'll have a minimum of two workflows: an activation workflow and a deactivation workflow.
+ If your Region switch plan is for an active/passive application deployment, you have a primary and a secondary Region. If you choose to have separate activation workflows for each Region, you'll create two workflows: one for each Region.

#### To create Region switch plan workflows


1. In the Region switch plan that you created, choose **Build workflows**.

1. Select one of the following workflow options:
   + **Build the same activation workflow for all Regions** - Enables you to use the same activation workflow across Regions.
   + **Build workflows separately for each Region** - Builds an individual activation workflow for each Region.

1. Optionally, provide a description for each workflow.

1. Define the workflow required to recover your application. In your workflow, you add *execution blocks* to define the steps that you want Region switch to perform for your recovery. Each execution block defines actions, such as application traffic rerouting or database recovery in an activating Region, and supports resources in another AWS account. You can opt to have execution blocks run in parallel or sequentially. For detailed information about the specific execution blocks that you can add to workflows, see [Add execution blocks](#working-with-rs-execution-blocks).

1. Depending on the workflow option that you selected, do the following:
   + If you selected **Build the same activation workflow for all Regions**, one activation workflow is required.
   + If you selected **Build workflows separately for each Region**, two activation workflows are required.

   For active/active plans, you must define both an activation workflow and a deactivation workflow.

#### Add execution blocks
<a name="working-with-rs-execution-blocks"></a>

You add steps to workflows in your Region switch plan, to perform the individual steps to complete failover or switchover for your application. For details about the functionality and behavior of each type of execution block, see the following descriptions.

Region switch runs a plan evaluation immediately after you create a plan or update it, and then every 30 minutes during steady state. Region switch stores information about plan evaluation in all the Regions where your plan is configured. Each execution block section here includes information about what is evaluated when Region switch runs plan evaluation.

Region switch includes execution block types that help scale compute resources as part of recovery. If you use these execution blocks in a plan, be aware that Region switch does not guarantee that the desired compute capacity with be attained. If you have a critical application and need to guarantee access to capacity, we recommend that you reserve the capacity. There are strategies that you can follow to reserve compute capacity in a secondary Region while also limiting cost. To learn more, see [ Pilot light with reserved capacity: How to optimize DR cost using On-Demand Capacity Reservations](https://aws.amazon.com/blogs/architecture/pilot-light-with-reserved-capacity-how-to-optimize-dr-cost-using-on-demand-capacity-reservations/).

Region switch supports the following execution blocks.



| Execution block | Function | Ungraceful configuration | 
| --- | --- | --- | 
| [ARC Region switch plan execution block](#region-switch-plan-block) | Orchestrate recovery for multiple applications in one execution by specifying child plans to execute. | Start child plans with their ungraceful configurations. | 
| [Amazon EC2 Auto Scaling group execution block](#ec2-auto-scaling-block) | Scale EC2 compute resources that are in an Auto Scaling group as part of your plan execution. | Specify the minimum percentage of compute capacity that should be matched in the Region that you're activating. | 
| [Amazon EKS resource scaling execution block](#eks-resource-scaling-block) | Scale Amazon EKS cluster pods as part of your plan execution. | N/A | 
| [Amazon ECS service scaling execution block](#ecs-service-scaling-block) | Scale Amazon ECS service tasks as part of your plan execution. | N/A | 
| [ARC routing control execution block](#arc-routing-controls-block) | Add a step to change the state of one or more ARC routing controls, to redirect your application traffic to a target AWS Region. | N/A | 
| [Amazon Aurora Global Database execution block](#aurora-global-database-block) | Perform a recovery workflow for an Aurora global database. | Perform an Aurora global databases failover (can potentially cause data loss). | 
| [Aurora Provisioned Scaling execution block](#aurora-provisioned-scaling-block) | Scale Aurora provisioned cluster instances to match the instance class of the source Region. | N/A | 
| [Aurora Serverless Scaling execution block](#aurora-serverless-scaling-block) | Scale Aurora Serverless cluster capacity as part of your multi-Region recovery process. | N/A | 
| [Amazon DocumentDB Global Cluster execution block](#documentdb-global-cluster-block) | Perform a recovery workflow for a Amazon DocumentDB global cluster. | Perform a Amazon DocumentDB global cluster failover (can potentially cause data loss). | 
| [Amazon Neptune Global Cluster execution block](#neptune-global-database-block) | Perform a recovery workflow for a Amazon Neptune global database. | Perform a Amazon Neptune global database failover (can potentially cause data loss). | 
| [Amazon RDS Promote Read Replica execution block](#rds-promote-read-replica-block) | Promote an Amazon RDS read replica to a standalone database instance. | N/A | 
| [Amazon RDS Create Cross-Region Replica execution block](#rds-create-cross-region-replica-block) | Create a cross-Region read replica for an Amazon RDS database instance as part of post-recovery. | N/A | 
| [Amazon RDS Switchover Read Replica execution block](#rds-switchover-read-replica-block) | Perform a switchover of an Amazon RDS Oracle read replica to make it the primary database instance. | Promote the read replica directly (can potentially cause data loss). | 
| [Manual approval execution block](#manual-approval-block) | Insert an approval step, to require approval or cancellation of an execution before proceeding. | N/A | 
| [Custom action Lambda execution block](#custom-action-lambda-block) | Add a custom step for running a Lambda function, to enable custom actions. | Skip the step. | 
| [Amazon Route 53 health check execution block](#route53-health-check-block) | Specifies the Regions that your application traffic will be redirected to during failover. | N/A | 
| [Lambda event source mapping execution block](#lambda-event-source-mapping-block) | Add a step to enable or disable a Lambda event source mapping. | Skip the step. | 

##### ARC Region switch plan execution block
<a name="region-switch-plan-block"></a>

The Region switch plan execution block allows you to orchestrate the order in which multiple applications switch over to the Region that you want to activate, by referencing other, child Region switch plans. Using this parent/child relationship, you can create complex, coordinated recovery processes that manage multiple resources and dependencies across your infrastructure. 

###### Configuration
<a name="region-switch-plan-block-config"></a>

When you use the Region switch plan execution block, you select a specific Region switch plan that you want to be executed in the workflow of the plan you're creating.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Region switch plan execution block sample policy](#security_iam_region_switch_plan_execution).

To configure a Region switch plan execution block, enter the following values:

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Region switch plan: **Select a plan to execute in the workflow for the current plan.

Then, choose **Save step.**

###### How it works
<a name="region-switch-plan-block-how"></a>

Use the Region switch plan execution block to create parent workflows with parent/child relationships. Note that this execution block does not support additional levels of child plans, and limits the number of parent child plans. Child plans must support the same Regions that the parent plan supports, and must have the same recovery approach as the parent plan (that is, active/active or active/passive).

This block supports both graceful and ungraceful execution modes. Ungraceful settings will start child plans with their ungraceful configuration. If Region switch block was executed gracefully, and then switched to ungraceful execution mode, any child plan will also switch to ungraceful execution mode.

##### Amazon EC2 Auto Scaling group execution block
<a name="ec2-auto-scaling-block"></a>

The EC2 Auto Scaling group execution block allows you to scale EC2 instances as part of your multi-Region recovery process. You can define a percentage of capacity, relative to the Region you're leaving (source and destination).

###### Configuration
<a name="ec2-auto-scaling-block-config"></a>

When you configure the EC2 Auto Scaling group execution block, you enter the EC2 Auto Scaling ARNs for the specific Regions that are associated with your plan. You should enter EC2 Auto Scaling ARNs in each Region that you want to be scaled up during plan execution.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [EC2 Auto Scaling execution block sample policy](#security_iam_region_switch_ec2_autoscaling).

To configure a EC2 Auto Scaling group execution block, enter the following values:

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **EC2 Auto Scaling group ARN for *Region*: ** Enter the ARN for the EC2 Auto Scaling group in each Region for your plan.

1. **Percentage to match the activated Region's capacity: ** Enter the desired percentage of the number of running instances in the Auto Scaling group to match for the activated Region.

1. **Capacity monitoring approach: **Select one of the following approaches for monitoring capacity for your EC2 Auto Scaling groups:
   + **Max running capacity sampled over 24 hours**: Choose this option to use the **Desired capacity** value specified in your EC2 Auto Scaling group configuration. This option does not create additional costs, but is potentially less accurate than using the other option, CloudWatch metrics.

     In the Region switch API, this option corresponds to specifying `sampledMaxInLast24Hours`.

     For more information, see [Set scaling limits for your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html) in the Amazon EC2 Auto Scaling User Guide.
   + **Max running capacity sampled over 24 hours with CloudWatch**: Choose this option to use metrics specified in Amazon CloudWatch for EC2 Auto Scaling. Using the option can be more accurate, but incurs the additional costs of using CloudWatch metrics.

     In the Region switch API, this option corresponds to specifying `autoscalingMaxInLast24Hours`.

     To use this option, you must first enable group metrics for your Auto Scaling groups. For more information, see [Enable Auto Scaling group metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html#as-enable-group-metrics) in the Amazon EC2 Auto Scaling User Guide.

1. **Wait for target group health: ** Whether Region switch waits for the Auto Scaling group's instances to become healthy in their associated Elastic Load Balancing target groups before completing the step.
   + When enabled, Region switch checks target group health after scaling capacity. Region switch does not proceed to the next step until every associated target group reports the required number of instances as `healthy`. The required number is the desired capacity Region switch calculates for the step, the same capacity it waits for when scaling.
   + When disabled, the step completes as soon as the target Auto Scaling group reaches the desired capacity of `InService` instances, without checking target group health.

   In the Region switch API, this option corresponds to specifying `waitELBTargetGroupHealthy` as either `enabled` or `disabled`.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="ec2-auto-scaling-block-how"></a>

When the block runs, Region switch reads the source Region's maximum running capacity over the last 24 hours, measured by the capacity monitoring approach you selected. It calculates the target capacity with the formula `ceil(percentToMatch * source capacity)`, where ceil() rounds up any fractional result, and measures capacity as the number of instances in the `InService` state. It then scales up the destination group to match this capacity. Region switch scales up the destination group only when its current desired capacity is less than the calculated target. If the current desired capacity is already greater than or equal to the target, the block proceeds without scaling (Region switch never scales down). This calculation applies to both active/passive and active/active plans.

The source capacity is always that of the other Region. In an active/active plan, Region switch uses the other configured Region as the source in both the activate and deactivate workflows.

Region switch waits until the destination group's capacity is fulfilled before proceeding to the next step. When you enable **Wait for target group health**, Region switch checks target group health after the destination group reaches its desired capacity. It reads the Elastic Load Balancing target groups attached to the group and polls their health until every attached target group reports the desired capacity as `healthy`. This check runs whether or not scaling occurred, so even if the group already had the desired capacity, Region switch verifies target group health before completing the step. For ungraceful execution, it instead waits for the minimum percentage of capacity to be `healthy`.

An instance counts toward the healthy total only when it is `InService` in the Auto Scaling group and its matching target group entry is `healthy`. Region switch identifies instances by EC2 instance ID and re-reads the group on each poll, so instances that are still launching, running a lifecycle hook, or held in a warm pool aren't counted until they reach `InService`. The step completes only after all required instances are healthy across every attached target group. If the group has no attached target groups, Region switch skips the check and completes the step. If the required instances don't become healthy before the timeout, the step fails.

**Note**  
The **Wait for target group health** option supports only Application Load Balancer (ALB) and Network Load Balancer (NLB) target groups. It doesn't support Classic Load Balancer. If your Auto Scaling group is associated only with a Classic Load Balancer, enabling this option has no effect.

The block supports both graceful and ungraceful execution. For ungraceful execution, you specify the minimum percentage of compute capacity to match in the destination Region before Region switch proceeds. The percentage of capacity you specify in the execution block, or as the minimum percentage for ungraceful execution, applies to both scaling and waiting for target group health.

**Note**  
Executing this block modifies the minimum and desired capacity settings of your Auto Scaling groups, which can cause configuration drift if you manage these values through infrastructure-as-code or other automation. Make sure your configuration management processes account for these changes to prevent unintended rollbacks.

##### Amazon EKS resource scaling execution block
<a name="eks-resource-scaling-block"></a>

The EKS resource scaling execution block enables you to scale EKS resources as part of your multi-Region recovery process. When you configure the execution block, you define a percentage of capacity to scale, relative to the capacity in the Region that is being deactivated. 

###### Configure EKS access entry permissions
<a name="eks-resource-scaling-block-permissions"></a>

Before you can add a step for EKS resource scaling, you must provide Region switch with the necessary permissions to take actions with the Kubernetes resources in your EKS clusters. To provide access for Region switch, you must create an EKS access entry for the IAM role that Region switch uses for plan execution, by using the following Region switch access policy: `arn:aws:eks::aws:cluster-access-policy/AmazonARCRegionSwitchScalingPolicy`

###### Region switch EKS access policy
<a name="eks-resource-scaling-block-permissions.policy"></a>

The following information provides details about the EKS access policy.

**Name:** `AmazonARCRegionSwitchScalingPolicy`

**Policy ARN:** `arn:aws:eks::aws:cluster-access-policy/AmazonARCRegionSwitchScalingPolicy`


| Kubernetes API groups | Kubernetes resources | Kubernetes verbs (permissions) | 
| --- | --- | --- | 
| \* | \*/scale | get, update | 
| \* | \*/status | get | 
| autoscaling | horizontalpodautoscalers | get, patch | 

###### Create an EKS access entry for Region switch
<a name="eks-resource-scaling-block-permissions.create"></a>

The following example describes how to create the required access entry and access policy associations so that Region switch can take specific actions for your Kubernetes resources. In this example, the permissions apply to the namespace {{my-namespace1}} in the EKS cluster {{my-cluster}} for the IAM role `arn:aws:iam::555555555555:role/{{my-role}}`. 

When you configure these permissions, make sure that you take these steps for both EKS clusters in your execution block.

**Prerequisite**  
Before you get started, change the authentication mode of the cluster to either `API_AND_CONFIG_MAP` or `API`. Changing the authorization mode adds the API for access entries. For more information, see [Change authentication mode to use access entries](https://docs.aws.amazon.com/eks/latest/userguide/setting-up-access-entries.html) in the Amazon EKS User Guide.

**Create the access entry**  
The first step is to create the access entry by using an AWS CLI command similar to the following:  

```
aws eks create-access-entry --cluster-name {{my-cluster}} --principal-arn
									arn:aws:iam::555555555555:user/{{my-user}} --type STANDARD
```
For more information, see [Create access entries](https://docs.aws.amazon.com/eks/latest/userguide/creating-access-entries.html) in the Amazon EKS User Guide.

**Create the access entry association**  
Next, create the association to the Region switch access policy by using an AWS CLI command similar to the following:  

```
aws eks associate-access-policy --cluster-name {{my-cluster}} --principal-arn arn:aws:iam::555555555555:role/{{my-role}} \
										--access-scope type=namespace,namespaces={{my-namespace1}} --policy-arn
										arn:aws:eks::aws:cluster-access-policy/AmazonARCRegionSwitchScalingPolicy
```
For more information, see [Associate access policies with access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html) in the Amazon EKS User Guide.

Make sure to repeat these steps with the second EKS cluster in your execution block, in the other Region, to ensure that both clusters can be accessed by Region switch.

###### Configuration
<a name="eks-resource-scaling-block-config"></a>

**Important**  
Before you add an EKS resource scaling step, first, make sure that you have the configured the correct permissions. For more information, see [Configure EKS access entry permissions](#eks-resource-scaling-block-permissions). Also make sure that you have the correct IAM policy in place. For more information, see [Amazon EKS resource scaling execution block sample policy](#security_iam_region_switch_eks).

Note that Region switch currently supports the following ReplicaSet resources: apps/v1, Deployment, and apps/v1.

For the execution block configuration, enter the following values.

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Application name: **Enter the name of your EKS application for example, *myApplication*.

1. **Kubernetes resource kind: **Enter the resource kind for the application, for example, *Deployment*.

1. **Resource for *Region*: **For each Region, enter information for the EKS cluster, including the EKS cluster ARN, resource namespace, and so on.

1. **Percentage to match the activated Region's capacity: ** Enter the desired percentage of running pods in the source Region to match in the activated Region.

1. **Capacity monitoring approach: **The only option for capacity monitoring is already selected, **Max running capacity sampled over 24 hours**.

   This capacity monitoring approach uses the `ReplicaCount` value for EKS service requests. For more information, see [Learn about ARC zonal shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the Amazon Elastic Kubernetes Service User Guide.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="eks-resource-scaling-block-how"></a>

During a plan execution, Region switch retrieves the sampled maximum number of replicas over the previous 24 hours for the target resource in the Region you're activating. Then, it computes the desired replica count for the destination resource by using the following formula: `ceil(percentToMatch * Source replica count)`

If the destination ready replica count is lower than the desired value, Region switch scales the destination resource replica value to the desired capacity. It waits for the replicas to become ready, leveraging your node auto-scaler to increase node capacity if necessary. 

If the optional `hpaName` field is not empty, Region switch patches the HorizontalPodAutoscaler to prevent any automatic scaledown during or after the execution by using the following patch: `{"spec":{"behavior":{"scaleDown":{"selectPolicy":"Disabled"}}}}` 

Make sure to configure any drift-correcting tool, such as GitOps tooling, to ignore the replica field for the resources in the patch, as well as the HorizontalPodAutoscaler field.

##### Amazon ECS service scaling execution block
<a name="ecs-service-scaling-block"></a>

The ECS service scaling execution block allows you to scale your ECS service in a destination Region as part of your multi-Region recovery process. You can define a percentage of capacity, relative to the Region that Region switch fails over from or deactivates.

###### Configuration
<a name="ecs-service-scaling-block-config"></a>

To configure the ECS service scaling execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon ECS service scaling execution block sample policy](#security_iam_region_switch_ecs).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Resource for *Region*: **For each Region, enter the ECS cluster ARN and the ECS service ARN.

1. **Percentage to match the source Region's task count: ** Enter the desired percentage of running tasks in the source Region to match in the activated Region.

1. **Capacity monitoring approach: **Select one of the following approaches for monitoring capacity for Amazon ECS:
   + **Max running capacity sampled over 24 hours**: Choose this option to use the **running tasks count** value in your Amazon ECS service. This option does not create additional costs, but is potentially less accurate than using the other option, CloudWatch metrics.

     In the Region switch API, this option corresponds to specifying `sampledMaxInLast24Hours`.

     For more information, see [Automatically scale your Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) in the Amazon Elastic Container Service Developer Guide.
   + **Max running capacity sampled over 24 hours via container insights**: Choose this option to use Amazon ECS Container Insights metrics. Using the option can be more accurate, but incurs the additional costs of using Container Insights.

     In the Region switch API, this option corresponds to specifying `autoscalingMaxInLast24Hours`.

     To use this option, you must first enable Container Insights. For more information, see [ Set up Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.html#set-container-insights-ECS-cluster) in the Amazon CloudWatch User Guide.

1. **Wait for target group health: ** Choose whether Region switch waits for the ECS service's tasks to become healthy in their associated Elastic Load Balancing target groups before completing the step.
   + When enabled, Region switch checks target group health after it scales capacity. Region switch does not proceed to the next step until every associated target group reports the required number of tasks as `healthy`. The required number of tasks is the desired count Region switch calculates for the step, the same count it waits for when scaling.
   + When disabled, the step completes as soon as the target service reaches its desired running task count, without checking target group health.

   In the Region switch API, this option corresponds to specifying `waitELBTargetGroupHealthy` as either `enabled` or `disabled`.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="ecs-service-scaling-block-how"></a>

When the block runs, Region switch reads the source Region's maximum running task count over the last 24 hours, measured by the capacity monitoring approach you selected. It calculates the target with the formula `ceil(percentToMatch * source task count)`, where ceil() rounds up any fractional result, using the service's desired count as the capacity. It then scales up the destination service to match this count. Region switch scales up the destination service only when its current desired count is less than the calculated target. If the current desired count is already greater than or equal to the target, the execution proceeds without scaling (Region switch never scales down). If the service has Application Auto Scaling enabled, Region switch updates the minimum capacity in Application Auto Scaling as well as the desired count. This calculation applies to both active/passive and active/active plans.

The source capacity is always that of the other Region. In an active/active plan, Region switch uses the other configured Region as the source in both the activate and deactivate workflows.

Region switch waits until the destination service's desired count is fulfilled before proceeding to the next step. When you enable **Wait for target group health**, Region switch checks target group health after the destination service reaches its desired count. It reads the Elastic Load Balancing target groups attached to the service and polls their health until every attached target group reports the desired count of tasks as `healthy`. This check runs whether or not scaling occurred, so even if the service already had the desired count, Region switch verifies target group health before completing the step. For ungraceful execution, it instead waits for the minimum percentage of the task count to be `healthy`.

A task counts toward the healthy total only when it belongs to this service and its matching target group entry is `healthy`. How Region switch identifies the service's tasks depends on the network mode:
+ In `awsvpc` mode, Amazon ECS registers each task by its task ENI IP address. Region switch matches each task by its IPv4 or IPv6 address, according to the target group's address type.
+ In `bridge` or `host` mode, Amazon ECS registers each task by its container instance and the host port mapped for the container. Region switch matches the container instance's EC2 instance ID together with that host port.

The step completes only after all required tasks are healthy across every associated target group. If the service has no load balancers, Region switch skips the check and completes the step. If the required tasks don't become healthy before the timeout, the step fails.

**Note**  
The **Wait for target group health** option supports only Application Load Balancer (ALB) and Network Load Balancer (NLB) target groups. It doesn't support Classic Load Balancer. If your ECS service uses only a Classic Load Balancer, enabling this option has no effect.

The block supports both graceful and ungraceful execution. For ungraceful execution, you specify the minimum percentage of the source Region's task count to match in the destination Region before Region switch proceeds. The percentage you specify in the execution block, or as the minimum percentage for ungraceful execution, applies to both scaling and waiting for target group health.

##### ARC routing control execution block
<a name="arc-routing-controls-block"></a>

If you've configured Amazon Application Recovery Controller (ARC) routing control for your application, you can add a ARC routing control step to redirect application traffic. This step enables you to change the state of one or more ARC routing controls to redirect your application traffic to a destination AWS Region. ARC routing control redirects traffic by using health checks in Amazon Route 53 that are configured with the DNS records associated with the routing controls.

**Important**  
Amazon Application Recovery Controller (ARC) routing control is only available in the AWS commercial partition.

###### Configuration
<a name="arc-routing-controls-block-config"></a>

To configure a routing control execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [ARC routing controls execution block sample policy](#security_iam_region_switch_arc_routing).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Desired routing controls: ** For each Region that you want to activate or deactivate, enter the routing control ARN and the initial state for the routing control, On or Off.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

The expected pattern for this execution block is to specify routing controls and initial states that align with how you have set up your application in specific AWS Regions. For example, if you have plan that enables you to activate Region A and Region B for your application, then you might have a routing control for Region A where you set the state to On and a routing control for Region B where you set the state to On.

Then, when you execute the plan and specify that you want to activate Region A, the workflow that includes this execution block updates the specified routing control to On, which directs traffic to Region A.

###### How it works
<a name="arc-routing-controls-block-how"></a>

By configuring a ARC routing control execution block, you can reroute application traffic to a destination AWS Region, or, for an active/active approach, stop traffic from being routed to a Region that you're deactivating. If your plan includes multiple workflows, make sure that you provide the same inputs for the DNS records for all routing control execution blocks that you use. 

This block does not support ungraceful execution mode.

###### Comparing ARC routing controls and Route 53 health check execution blocks
<a name="region-switch-compare-routing"></a>

The Amazon Route 53 health check execution block in Region switch provides a lower-cost alternative for DNS-based traffic management. However, this execution block depends on the AWS Region that you're activating, so that Region must be available. This meets the needs of most customers, because they are activating a healthy Region.

ARC routing controls provide highly reliable DNS-based traffic management with a 100% availability SLA. With routing controls, your operations teams can shift traffic between Regions with safety guardrails. Routing controls provide a single-tenant solution with a 100% SLA. A routing control cluster is spread across five Regions and can tolerate two Regions being offline. If you have highly critical applications, consider using routing controls.

Routing controls are not required to use Region switch. You can use Region switch to manage traffic redirection by using Route 53 health check execution blocks without routing controls.

Routing controls add value with Region switch in the following situations:
+ You require the 100% availability SLA for the traffic control mechanism itself.
+ Your organization requires manual operational controls with safety rules for critical applications.
+ You want defense-in-depth so that operations teams can manually override automated traffic routing if needed.

Route 53 health check execution blocks do not depend on the control plane. Health check record changes use the data plane, so they do not require the activating Region to process configuration updates. Route 53 health check execution blocks are sufficient in the following situations:
+ Your application can depend on the AWS Region that you are activating.
+ Automated traffic redirection as part of the recovery workflow meets your requirements.
+ Cost optimization is a priority. Route 53 health check execution blocks have lower cost than routing controls.

Most customers start with Route 53 health check execution blocks as the default traffic routing mechanism and add routing controls only for their most critical applications that require the highest reliability for the traffic management mechanism.

##### Amazon Aurora Global Database execution block
<a name="aurora-global-database-block"></a>

The Amazon Aurora Global Database execution block allows you to perform a *failover* or *switchover* recovery workflow for a global database.
+ Failover – Use this approach to recover from an unplanned outage. With this approach, you perform a cross-Region failover to one of the secondary DB clusters in your Aurora global databases. The recovery point objective (RPO) for this approach is typically a non-zero value measured in seconds. The amount of data loss depends on the Aurora global databases replication lag across the AWS Regions at the time of the failure. For more information, see [ Recovering an Amazon Aurora global database from an unplanned outage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover) in the Amazon Aurora User Guide.
+ Switchover – This operation was previously called *managed planned failover*. Use this approach for controlled scenarios, such as operational maintenance and other planned operational procedures where all the Aurora clusters and other services they interact with are in a healthy state. Because this feature synchronizes secondary DB clusters with the primary before making any other changes, RPO is 0 (no data loss). For more information, see [ Performing switchovers for Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover) in the Amazon Aurora User Guide.

###### Configuration
<a name="aurora-global-database-block-config"></a>

To configure an Aurora Global Database execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Aurora Global Database execution block sample policy](#security_iam_region_switch_aurora).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Aurora Global Database cluster name: **Enter the identifier for the global database.

1. **Cluster ARN for *Region*: **Enter the cluster ARN to use in each Region in the plan.

1. **Specify the option for Aurora database: **Choose either **Switchover** or **Failover (data loss)**, depending on how you want 

1. **Aurora Global Database cluster name: **

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="aurora-global-database-block-how"></a>

By configuring a Aurora Global Databases execution block, you can failover or switchover global databases as part of your application recovery. If you’re using an active/active approach, Region switch uses the other configured Region as the source. That is, if a Region is being deactivated, Region switch uses the other active Region as the source to match for the percent to scale.

This block supports both graceful and ungraceful execution modes. Ungraceful settings perform an Aurora Global Database *failover*, which might cause data loss.

For more information about Aurora Global Database disaster recovery, including failover and switchover, see [ Using switchover or failover in Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) in the Amazon Aurora User Guide.



##### Amazon DocumentDB Global Cluster execution block
<a name="documentdb-global-cluster-block"></a>

The Amazon DocumentDB Global Cluster execution block allows you to perform a *failover* or *switchover* recovery workflow for a global cluster.
+ Failover – Use this approach to recover from an unplanned outage. With this approach, you perform a cross-Region failover to one of the secondary clusters in your Amazon DocumentDB global cluster. The recovery point objective (RPO) for this approach is typically a non-zero value measured in seconds. The amount of data loss depends on the Amazon DocumentDB global cluster replication lag across the AWS Regions at the time of the failure.
+ Switchover – Use this approach for controlled scenarios, such as operational maintenance and other planned operational procedures where all the Amazon DocumentDB clusters are in a healthy state. Because this feature synchronizes secondary clusters with the primary before making any other changes, RPO is 0 (no data loss).

###### Configuration
<a name="documentdb-global-cluster-block-config"></a>

To configure a Amazon DocumentDB Global Cluster execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon DocumentDB Global Cluster execution block sample policy](#security_iam_region_switch_documentdb).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Amazon DocumentDB Global Cluster identifier: **Enter the identifier for the global cluster.

1. **Cluster ARN for *Region*: **Enter the cluster ARN to use in each Region in the plan.

1. **Specify the option for Amazon DocumentDB cluster: **Choose either **Switchover** or **Failover (data loss)**.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="documentdb-global-cluster-block-how"></a>

By configuring a Amazon DocumentDB Global Cluster execution block, you can failover or switchover global clusters as part of your application recovery. If you're using an active/active approach, Region switch uses the other configured Region as the source. That is, if a Region is being deactivated, Region switch uses the other active Region as the source to match for the percent to scale.

This block supports both graceful and ungraceful execution modes. Ungraceful settings perform a Amazon DocumentDB Global Cluster *failover*, which might cause data loss.

During switchover or failover operations, the DNS endpoint that customers use to write will be changed. Customers are responsible for ensuring they are using the correct endpoint after the operation completes.

##### Aurora Provisioned Scaling execution block
<a name="aurora-provisioned-scaling-block"></a>

**Category:** Database scaling

When you switch Regions, your Aurora provisioned database in the destination Region may be running a smaller instance class than your source Region — leaving you with insufficient compute capacity to handle production traffic. The Aurora Provisioned Scaling execution block automatically scales the destination instance to match the source instance class, ensuring your database is ready to serve full production load the moment traffic arrives.

###### Key benefits
<a name="aurora-provisioned-scaling-block-benefits"></a>
+ **Automatic capacity matching:** Region switch reads the source instance class and scales the destination instance to match, eliminating the risk of under-provisioned databases receiving production traffic after a failover.
+ **Instance creation when needed:** If the destination instance doesn't exist yet, Region switch creates it with the correct instance class.
+ **Cross-family intelligence:** When the source instance type isn't available in the destination Region, Region switch automatically selects an equivalent or larger instance type with the same or more vCPU and memory, so you don't need to maintain instance-type compatibility mappings yourself.

###### When to use
<a name="aurora-provisioned-scaling-block-when"></a>

Any recovery plan where Aurora provisioned instances must be at production capacity before traffic shifts.
+ **Active-passive Aurora Global Databases:** Your secondary Region runs a smaller (cheaper) reader instance that must be scaled up before receiving write traffic.
+ **Cost-optimized standby Regions:** You intentionally run smaller instances in your standby Region to save costs, and need automated right-sizing during failover.

###### How Aurora Provisioned Scaling compares to alternatives
<a name="aurora-provisioned-scaling-block-comparison"></a>

Without this execution block, customers must ensure destination database capacity manually or through custom automation before switching Regions.


|  | Approach | Pros/Cons | 
| --- | --- | --- | 
| 1 | Aurora Provisioned Scaling block | Fully automated, handles cross-family mapping, creates missing instances, integrated with Region switch orchestration | 
| 2 | Manual scaling | Full control over timing and instance selection, but slow, error-prone under pressure, requires operator availability during incident | 
| 3 | Scripted automation (Lambda/SSM) | Customizable logic; Must build, test, and maintain; not integrated with Region switch sequencing; cannot leverage native plan evaluation | 
| 4 | Pre-provisioning (always match) | Zero failover delay. Doubles cost in standby Region; wasteful for active-passive architectures | 

The Aurora Provisioned Scaling block is the right choice when you want automated, validated capacity scaling as an integrated step in your Region switch recovery plan.

###### How it works
<a name="aurora-provisioned-scaling-block-how"></a>

When the Aurora Provisioned Scaling execution block runs during plan execution, Region switch scales the target instance to match the instance class of the source instance through the following sequence:
+ If the target instance exists but is not in an `available` state, Region switch waits for it to become available before proceeding.
+ If the target instance does not exist, Region switch creates it in the target cluster with the instance class from the source instance.
+ If the target instance exists, Region switch validates that it belongs to the expected cluster, then compares the instance classes.
+ If both instances are in the same family and the target is smaller, Region switch modifies the target instance to match the source class.
+ If the instances are in different families, or the target is already at a larger size, no scaling is performed.
+ If the source instance type doesn't exist in the target Region, Region switch selects another instance type with the same or more vCPU and memory (for both create and modify operations).
+ Region switch polls the target instance until it reaches `available` status, then marks the step as complete.

**Note**  
Region switch only scales up. If the destination instance is already equal to or larger than the source, no modification is made.

###### Configuration
<a name="aurora-provisioned-scaling-block-config"></a>

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Aurora provisioned scaling execution block sample policy](#security_iam_region_switch_aurora_provisioned_scaling).

To configure an Aurora Provisioned Scaling execution block, enter the following values:
+ **Step name:** Enter a name.
+ **Step description (optional):** Enter a description of the step.
+ **Global cluster identifier:** Enter the identifier for the Aurora global cluster.
+ **Cluster ARN for {{Region}}:** Enter the Aurora database cluster ARN for each Region in the plan.
+ **Instance ARN for {{Region}}:** Enter the Aurora database instance ARN for each Region in the plan.
+ **Timeout:** Enter a timeout value.

Then, choose **Save step.**

###### Related resources
<a name="aurora-provisioned-scaling-block-resources"></a>
+ [Aurora provisioned scaling execution block sample policy](#security_iam_region_switch_aurora_provisioned_scaling)
+ [Amazon Aurora DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the *Amazon Aurora User Guide*

##### Aurora Serverless Scaling execution block
<a name="aurora-serverless-scaling-block"></a>

**Category:** Database scaling

During a Region switch, your destination Aurora Serverless cluster may have ACU (Aurora Capacity Unit) settings that are far below what's needed to absorb production traffic. The Aurora Serverless Scaling execution block automatically calculates and applies the correct min and max ACU capacity to your destination cluster based on the source cluster's actual usage, ensuring your serverless database can handle the incoming workload without throttling or connection failures.

###### Key benefits
<a name="aurora-serverless-scaling-block-benefits"></a>
+ **Usage-based capacity calculation:** Rather than relying on static configuration, Region switch derives target capacity from the source cluster's actual peak utilization over the last 24 hours, giving you right-sized capacity based on real traffic patterns.
+ **Cross-engine-type intelligence:** Whether your source is Serverless, Provisioned, or a hybrid configuration, Region switch knows how to translate the source capacity into appropriate ACU settings for the destination Serverless cluster.
+ **Percentage-based scaling for active-active:** Configure a target percentage above 100% (for example, 200%) for active-active architectures where the destination must absorb combined traffic from both Regions.

###### When to use
<a name="aurora-serverless-scaling-block-when"></a>
+ **Active-passive with Serverless standby:** Your destination Region runs a Serverless cluster at minimal ACUs and needs to scale up before receiving production traffic.
+ **Active-active failover:** Both Regions serve traffic, and during a switch the remaining Region must handle the combined load – use a target percentage above 100%.
+ **Mixed-engine Global Databases:** Your source Region uses provisioned instances but your destination uses Serverless – Region switch handles the capacity translation automatically.

###### How Aurora Serverless Scaling compares to alternatives
<a name="aurora-serverless-scaling-block-comparison"></a>

Without this execution block, customers must manually calculate ACU requirements and modify cluster settings before switching traffic – a complex, error-prone process especially when source and destination use different engine types.


|  | Approach | Pros | Cons | 
| --- | --- | --- | --- | 
| 1 | Aurora Serverless Scaling block | Automated calculation from real usage, handles cross-engine translation, percentage-based control, integrated with plan orchestration | Only scales up; modifies ACU settings which may drift from IaC | 
| 2 | Manual ACU adjustment | Full control | Requires calculating ACU equivalents under pressure; slow; error-prone | 
| 3 | Scripted automation | Customizable | Must replicate cross-engine translation logic; no plan evaluation; maintenance burden | 
| 4 | Pre-provisioning (max ACU always high) | No failover delay | Expensive; defeats the cost benefit of Serverless; wasteful in standby Region | 

The Aurora Serverless Scaling block is the right choice when you need automated, usage-aware capacity scaling that handles the complexity of cross-engine ACU translation.

###### How it works
<a name="aurora-serverless-scaling-block-how"></a>

After you configure an Aurora Serverless Scaling execution block, Region switch confirms that there is one source cluster and one destination cluster in the specified global database. The target capacity is determined based on the source cluster type:
+ **Source is Serverless:**
  + Min ACU = source cluster's peak observed ACU utilization (the `ServerlessDatabaseCapacity` CloudWatch metric) over the last 24 hours
  + Max ACU = peak of the source cluster's max ACU over the last 24 hours
+ **Source is Provisioned:**
  + Maps the source cluster's EC2 instance memory to equivalent ACUs (instance memory in GiB ÷ 2)
  + Sets max ACU to 256
+ **Source is Hybrid (Provisioned \+ Serverless):**
  + Min ACU = maximum of the provisioned instance ACU equivalent and the observed serverless ACU utilization over 24 hours
  + Max ACU = 256

Region switch then applies the target percentage to calculate final values:

```
destination min ACU = round_to_nearest_0.5(targetPercent × source min ACU)
destination max ACU = round_to_nearest_0.5(targetPercent × source max ACU)
```

If the destination cluster's current capacity is already at or above the calculated target, Region switch completes the step without making changes. Region switch does not scale down cluster capacity. When the destination cluster is not Serverless, the block completes successfully as a no-op.

For active-active plans, Region switch uses the other configured Region as the source. If a Region is being deactivated, Region switch uses the other active Region as the source to calculate the percentage to scale.

**Note**  
Executing this block modifies the min and max ACU capacity settings of your Aurora Serverless clusters, which may cause configuration drift if you manage these values through infrastructure-as-code tools or other automation. Ensure your configuration management processes account for these changes to prevent unintended rollbacks.

###### Configuration
<a name="aurora-serverless-scaling-block-config"></a>

When you configure the Aurora Serverless Scaling execution block, you enter the global cluster identifier for your Aurora Global Database and the database cluster ARNs for each Region that you want to be scaled up during plan execution.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Aurora serverless scaling execution block sample policy](#security_iam_region_switch_aurora_serverless_scaling).

To configure an Aurora Serverless Scaling execution block, enter the following values:

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Aurora Global Database cluster name: **Enter the global cluster identifier.

1. **Cluster ARN for *Region*: **Enter the database cluster ARN to use in each Region for your plan.

1. **Target percent (optional): **Enter the percentage of derived source capacity to scale the destination cluster to. Defaults to 100. For active-active plans, consider a higher value (for example, 200%) to account for combined traffic.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### Related resources
<a name="aurora-serverless-scaling-block-resources"></a>
+ [Aurora serverless scaling execution block sample policy](#security_iam_region_switch_aurora_serverless_scaling)
+ [Managing Aurora Serverless v2 capacity](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-administration.html) in the *Amazon Aurora User Guide*

##### Amazon Neptune Global Cluster execution block
<a name="neptune-global-database-block"></a>

The Amazon Neptune Global Database execution block allows you to perform a *failover* or *switchover* recovery workflow for a Neptune global database.
+ Switchover – This operation was previously called *managed planned failover*. Use this approach for controlled scenarios, such as operational maintenance and other planned operational procedures where all the Amazon Neptune clusters and other services they interact with are in a healthy state. Because this feature synchronizes secondary DB clusters with the primary before making any other changes, RPO is 0 (no data loss).
+ Failover – Use this approach to recover from an unplanned outage. With this approach, you perform a cross-Region failover to one of the secondary DB clusters in your Amazon Neptune global database. The recovery point objective (RPO) for this approach is typically a non-zero value measured in seconds. The amount of data loss depends on the Amazon Neptune global database replication lag across the AWS Regions at the time of the failure.

###### Configuration
<a name="neptune-global-database-block-config"></a>

To configure a Amazon Neptune Global Database execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon Neptune Global Cluster execution block sample policy](#security_iam_region_switch_neptune).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Neptune Global Database cluster name: **Enter the identifier for the global database.

1. **Cluster ARN for *Region*: **Enter the cluster ARN to use in each Region in the plan.

1. **Specify the option for Neptune database: **Choose either **Switchover** or **Failover (data loss)**, depending on your recovery requirements. Choose switchover for planned operations with zero data loss, or failover for unplanned outage recovery where some data loss is acceptable.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="neptune-global-database-block-how"></a>

By configuring a Amazon Neptune Global Database execution block, you can failover or switchover global databases as part of your application recovery.

This block supports both graceful and ungraceful execution modes:
+ **Graceful** – Region switch performs the operation that you specified in the configuration (switchover or failover). If you configured switchover, Region switch calls `SwitchoverGlobalCluster`, which synchronizes all secondary clusters with the primary before promoting the target cluster (zero data loss). If you configured failover, Region switch calls `FailoverGlobalCluster`, which immediately promotes the target cluster without waiting for replication to complete (potential data loss).
+ **Ungraceful** – If you have configured ungraceful settings, Region switch calls `FailoverGlobalCluster` with `AllowDataLoss=true` on the target secondary cluster. Amazon Neptune immediately promotes the target cluster to be the new primary without waiting for replication to complete. This may result in data loss equal to the replication lag at the time of failover.

If an ungraceful execution is requested while a switchover is already in progress, Region switch first reverses the in-progress switchover (by switching back to the original primary), waits for the cluster to become available, and then performs the failover to the target cluster.

In both modes, Region switch polls the global cluster status until the target cluster becomes the writer and the cluster returns to an `available` state, or until the configured timeout is reached.

If the target cluster is already the writer when the block executes, Region switch detects this and completes the step immediately without making any changes.

For more information about Amazon Neptune Global Database disaster recovery, see [ Using switchover or failover in Amazon Neptune global databases](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-global-database-failover.html) in the Amazon Neptune User Guide.

##### Amazon RDS Promote Read Replica execution block
<a name="rds-promote-read-replica-block"></a>

The Amazon RDS Promote Read Replica execution block allows you to promote an Amazon RDS read replica to a standalone database instance as part of your multi-Region recovery process. This enables you to failover to a healthy Region by promoting the read replica in that Region to become the new primary database.

###### Configuration
<a name="rds-promote-read-replica-block-config"></a>

To configure an Amazon RDS Promote Read Replica execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon RDS execution block sample policy](#security_iam_region_switch_rds).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **RDS DB instance ARN for Region: **Enter the database instance ARN for the read replica in each Region in the plan.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="rds-promote-read-replica-block-how"></a>

By configuring an Amazon RDS Promote Read Replica execution block, you can promote a read replica to a standalone database instance as part of your application recovery. When you execute the plan, Region switch promotes the read replica in the Region that you're activating to become an independent database instance.

**Note**  
This block only supports active/passive plans

During promotion, the DNS endpoint that you use to connect to the database will remain the same. However, the promoted instance will no longer replicate from the original primary database. You are responsible for ensuring their application is configured to use the correct endpoint after the operation completes.

After promotion, the promoted instance inherits the following settings from the original primary instance:
+ Backup retention period
+ Preferred backup window
+ Multi-AZ configuration

##### Amazon RDS Create Cross-Region Replica execution block
<a name="rds-create-cross-region-replica-block"></a>

The Amazon RDS Create Cross-Region Replica execution block allows you to create a cross-Region read replica for an Amazon RDS database instance as part of your post-recovery process. This execution block is typically used after promoting a read replica to re-establish cross-Region replication, ensuring your application is prepared for future regional events.

###### Configuration
<a name="rds-create-cross-region-replica-block-config"></a>

To configure an Amazon RDS Create Cross-Region Replica execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon RDS execution block sample policy](#security_iam_region_switch_rds).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Source DB instance ARN for Region: **Enter the database instance ARN for the source database in each Region in the plan. The execution block uses the identifier from the Region being activated as the source database for creating the cross-Region read replica.

1. **Replica DB instance ARN: **Enter the instance ARN to use for the new read replica.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="rds-create-cross-region-replica-block-how"></a>

By configuring an Amazon RDS Create Cross-Region Replica execution block, you can create a read replica in the other Region as part of your post-recovery process. This execution block is designed to run after a successful failover to re-establish cross-Region replication.

This block can only be added to active/passive plans.

During the execution, the old primary instance will be renamed and tagged with *renamedByRegionSwitch*. Then a new read replica instance will be created with the following settings copied from the old primary:
+ Instance identifier
+ DB parameter groups
+ DB subnet groups
+ KMS key
+ VPC security groups
+ Option groups
+ Domain authentication secret ARN

**Important**  
The renamed primary instance remains running and continues to incur charges. Region switch tags it with *renamedByRegionSwitch* for identification, but does not otherwise modify or delete it. You are responsible for managing the renamed instance, including deciding whether to keep it running, stop it, or delete it based on your operational and cost requirements.

**Note**  
This execution block is designed for post-recovery workflows and requires the source Region to be healthy and accessible. It should be used after a successful failover to re-establish cross-Region replication.

##### Amazon RDS Switchover Read Replica execution block
<a name="rds-switchover-read-replica-block"></a>

**Category:** Database switchover

The Amazon RDS Switchover Read Replica execution block allows you to perform a controlled switchover of an Amazon RDS Oracle read replica, making it the new primary database instance. This enables multi-Region database failover for Amazon RDS Oracle deployments that use cross-Region read replicas, without data loss in the graceful path.

###### Key benefits
<a name="rds-switchover-read-replica-block-benefits"></a>
+ **Zero data loss switchover:** The graceful switchover path ensures that all data is synchronized between the primary and standby before promoting the read replica, preventing any data loss.
+ **Automated validation:** Region switch validates engine compatibility, replication state, backup configuration, and pending maintenance before attempting the switchover.
+ **Ungraceful fallback:** If a graceful switchover is not possible or an ungraceful execution is requested, Region switch can promote the read replica directly, prioritizing recovery speed.

###### Configuration
<a name="rds-switchover-read-replica-block-config"></a>

When you configure the Amazon RDS Switchover Read Replica execution block, you provide the database instance ARNs for each Region in your multi-Region Amazon RDS Oracle deployment.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon RDS Switchover Read Replica execution block sample policy](#security_iam_region_switch_rds_switchover_read_replica).

To configure an Amazon RDS Switchover Read Replica execution block, enter the following values:

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **DB Instance ARN for *Region*: **Enter the database instance ARN for each Region in your plan. You must provide an ARN for each Region.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="rds-switchover-read-replica-block-how"></a>

When you execute a plan with an Amazon RDS Switchover Read Replica execution block, Region switch performs the following operations:

**Graceful switchover (default):**

1. Region switch waits for the target read replica instance to reach an available state.

1. Region switch verifies that the target instance is an Oracle 19c or later read replica in a valid standby mode (mounted or open-read-only).

1. Region switch confirms that replication is active between the primary and standby instances.

1. Region switch validates that automatic backups are enabled on the standby instance.

1. Region switch checks for blocking pending maintenance actions on both instances.

1. Region switch validates that the primary instance in the other Region is available.

1. Region switch calls `SwitchoverReadReplica` to promote the standby to primary.

1. Region switch waits for the instance to become the primary and reach an available state.

1. If the original primary had Multi-AZ enabled, Region switch enables Multi-AZ on the new primary to match the original configuration.

**Ungraceful execution (promote read replica):**

When an ungraceful execution is requested with the `promoteReadReplica` behavior, Region switch promotes the read replica directly using `PromoteReadReplica`. This is faster but may result in data loss if replication has not fully synchronized. After promotion, Region switch restores the backup retention period, preferred backup window, and Multi-AZ settings from the original primary's configuration.

If an ungraceful execution is requested without specifying a behavior, Region switch falls back to the graceful switchover path.

**Note**  
This execution block supports only Amazon RDS Oracle 19c and later. Aurora databases should use the Aurora Global Databases execution block instead.

###### What is evaluated as part of plan evaluation
<a name="rds-switchover-read-replica-block-eval"></a>

When Region switch evaluates your plan, Region switch performs several checks on your Amazon RDS Switchover Read Replica execution block configuration:
+ The database instance ARNs are valid and the instances exist in their respective Regions.
+ One instance is a read replica of the other (a valid replication relationship exists).
+ The engine is Oracle 19c or later (not Aurora, not custom).
+ Engine versions match between primary and standby instances.
+ The standby instance is in mounted or open-read-only mode.
+ The standby instance has automatic backups enabled with a non-zero retention period.
+ Replication is actively replicating between instances.
+ No blocking pending maintenance actions exist on the in-region instance.
+ Option groups are not shared with unrelated instances (which could cause issues during switchover).
+ Resource monitor data exists for the other-region instance (used for configuration restoration after ungraceful promote).

Region switch also validates that the plan's IAM role has the correct permissions for Amazon RDS switchover. For more information about the required permissions for Region switch execution blocks, see [Amazon RDS Switchover Read Replica execution block sample policy](#security_iam_region_switch_rds_switchover_read_replica). If any of the checks fail, Region switch returns warning messages, which you can view in the console. Or, you can receive the validation warnings through or by using API operations.

###### Related resources
<a name="rds-switchover-read-replica-block-resources"></a>
+ [Amazon RDS Switchover Read Replica execution block sample policy](#security_iam_region_switch_rds_switchover_read_replica)
+ [Working with Oracle replicas for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the *Amazon RDS User Guide*

##### Manual approval execution block
<a name="manual-approval-block"></a>

The manual approval execution block enables you to insert an approval step that you associate with an IAM role. Users with access to the role can approve or decline the execution of a step, to pause the step until approval is granted, or, potentially, prevent the plan from progressing.

To ensure that manual approval is required during plan execution, you input a manual approval step at a specific location in the workflow, and then configure the IAM role to specify who can approve the step. 

###### Configuration
<a name="manual-approval-block-config"></a>

To configure a manual approval execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Manual approval execution block sample policy](#security_iam_region_switch_manual_approval).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **IAM approval role: **Enter the ARN for an IAM role that has permission to manually approve execution continuing for the Region switch plan. The IAM role must be within the account that is the owner of the plan. 

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

###### How it works
<a name="manual-approval-block-how"></a>

By configuring a manual approval execution block, you can require an approval as part of your application recovery. For a manual execution block, Region switch does the following:
+ When Region switch runs a manual approval execution block, it pauses execution and sets the plan's execution status to pending approval.
+ Anyone who has access to the role defined in the execution block can approve or decline execution of the step.
+ If they approve the step execution, Region switch proceeds with execution the plan. If they decline, Region switch cancels the plan execution.

This block does not support ungraceful execution mode.

##### Custom action Lambda execution block
<a name="custom-action-lambda-block"></a>

The custom action Lambda execution block enables you to add a customized step to a plan by using a Lambda function.

###### Configuration
<a name="custom-action-lambda-block-config"></a>

To configure a Lambda execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Custom action Lambda execution block sample policy](#security_iam_region_switch_lambda).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **ARN of the Lambda function to be invoked in *primary* and *secondary* Regions**: Specify the ARN of the Lambda function to run for this step.

1. **Region to run Lambda function: **In the drop-down menu, choose the Region that you want to run the Lambda functions in.

1. **Timeout: **Enter a timeout value.

1. **Retry interval: **Enter a retry interval, to rerun the Lambda function if it does not succeed within this interval.

Then, choose **Save step.**

###### How it works
<a name="custom-action-lambda-block-how"></a>
+ When you create a custom action Lambda execution block, you're required to specify two Lambda functions for the step to execute—one in each of the plan's Regions.
+ You can configure which Region you want the Lambda to run in, for example, in the activating Region or in the deactivating Region. However, if you execute in the deactivating Region, you take a dependency on that Region. We do not recommend that you take a dependency on the deactivating Region.

This block supports both graceful and ungraceful execution modes. In ungraceful execution mode, Region switch skips the Lambda execution block step.

##### Amazon Route 53 health check execution block
<a name="route53-health-check-block"></a>

The Amazon Route 53 health check execution block enables you to specify the Regions that your application's traffic will be redirected to during failover. The execution block creates Amazon Route 53 health checks, which you then attach to Route 53 DNS records in your account. When you execute your Region switch plan, the Route 53 health check state is updated, and traffic is redirected based on your DNS configuration.

**Important**  
The Route 53 hosted zone must be in the same partition as the Region switch plan.

###### Configuration
<a name="route53-health-check-block-config"></a>

To configure a Route 53 health check execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Route 53 health check execution block sample policy](#security_iam_region_switch_route53).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Hosted zone ID: **The hosted zone Id for your domain and DNS records in Route 53.

1. **Record name: **Enter the record name (domain name) for the records that you use, with the associated health checks, to redirect traffic for your application. Region switch will find the Route 53 record sets for the record name and attempt to map each record set to a Region, based on the Region name inside the **Value** or **Set Identifier** of the record set.

1. **Record set identifiers (optional): **You have the option to manually provide the record set identifiers if Region switch cannot automatically map the record sets to Regions from the record name provided in step 4 after you have created the plan. If plan evaluation returns a warning that indicates that more information is required, update your plan with record set identifiers by including the following for each Region:
   + **Record set identifier: **Enter the **Set identifier** or the **Value/Route traffic to** for the record set.
   + **Region: ** Enter the Region associated with the record set that has the record set identifier information.

1. Choose **Save step.**

1. Configure health checks in Route 53.

   Region switch provides a health check ID, for each Region, for each record name within a hosted zone defined in the execution block. Make sure that you configure the health checks for the corresponding record sets in your account in Route 53 so that Region switch can correctly redirect traffic for your application during plan execution. In the **Health checks** tab on the plan details page, you can view the health checks for all execution blocks and Regions. 

###### How the Route 53 health check execution block works as a highly available DNS failover mechanism
<a name="route53-health-check-block-how"></a>

ARC Region Switch Route53 health check execution block creates two sets of health checks — one for each Region if your workload is deployed in two Regions. It vends these health checks to you. You can view them through the Region switch console in "Monitoring" tab or via the ListRoute53HealthChecks API. You then associate these health checks with your Route 53 DNS records.

When the Route 53 health check execution block is executed, it uses the STOP (Standby Takes Over Primary) pattern under the hood to change the state of your health checks to orchestrate the DNS failover. The primary health check is marked "unhealthy" and the secondary health check is marked "healthy" when you orchestrate a failover from primary to secondary. This change in health check state is used by Route 53 to redirect traffic during failover.

For active/passive: the primary Region's health check starts healthy; the passive Region starts unhealthy. When you use the Route53 health check execution block to failover, these states flip.

For active/active: all health checks start healthy. When you use the Route53 health check execution block in a deactivate workflow, the workflow sets the deactivating Region's health check state to unhealthy. When you use the Route53 health check execution block in an activate workflow for a Region, the workflow sets the activating Region's health check state to healthy.

###### Why is this a highly available failover mechanism?
<a name="route53-health-check-block-why-ha"></a>

Two reasons make this a reliable failover mechanism:

1. **Route 53 health check state transitions are part of Route 53 data plane, which is designed for 100% availability**

   Changing the state of a Route53 health check state is a data plane operation. The Route53 data plane is globally distributed and designed for 100% availability. There is no control plane dependency to Route53 health check state changes. This means health check state change works even if the primary Region is impaired.

1. **The STOP pattern (Standby Takes Over Primary)**

   The STOP pattern is a mechanism to orchestrate a DNS failover and it was published in the blog post here: [ Creating disaster recovery mechanisms using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/). This pattern is used by the Route53 health check execution block under the hood. The STOP pattern entails using the healthy Region as a "decision agent" to change the state of the health check in the impaired Region. The STOP pattern does not take dependency on the impaired Region.

Here's how it works in practice:
+ When you create a Route53 health check execution block, health checks are created by Region switch in each Region for your workload and vended to you through Region switch console in the Monitoring tab or the ListRoute53HealthChecks API.
+ You then associate these with each Region's DNS record manually. One health check is associated with the primary Region's DNS record and the other is associated with the secondary Region's DNS record by you.
+ The health check is associated with primary Region's DNS records, but it monitors a resource in the standby (secondary) Region (for example: presence of a file in S3) to change the state of the health check.
+ The health check is inverted — if the standby resource is unreachable, the health check for the primary Region defaults to healthy. If the standby resource is discovered, the health check for the primary Region is changed to unhealthy. This prevents accidental failover.
+ To trigger a failover, the file is created by Region switch in the standby Region. The health check detects it, marks primary unhealthy, and Route53 flips DNS. The standby resource is managed by the Region switch service and is not dependent on the customer.

The combination of no control plane dependency (globally distributed data plane) and no impaired Region dependency (STOP pattern) makes this a highly available DNS failover mechanism when the customer is only operating from two Regions. See STOP pattern documented here: [ Creating disaster recovery mechanisms using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/).

###### Comparing ARC routing controls and Route 53 health check execution blocks
<a name="region-switch-compare-routing"></a>

The Amazon Route 53 health check execution block in Region switch provides a lower-cost alternative for DNS-based traffic management. However, this execution block depends on the AWS Region that you're activating, so that Region must be available. This meets the needs of most customers, because they are activating a healthy Region.

ARC routing controls provide highly reliable DNS-based traffic management with a 100% availability SLA. With routing controls, your operations teams can shift traffic between Regions with safety guardrails. Routing controls provide a single-tenant solution with a 100% SLA. A routing control cluster is spread across five Regions and can tolerate two Regions being offline. If you have highly critical applications, consider using routing controls.

Routing controls are not required to use Region switch. You can use Region switch to manage traffic redirection by using Route 53 health check execution blocks without routing controls.

Routing controls add value with Region switch in the following situations:
+ You require the 100% availability SLA for the traffic control mechanism itself.
+ Your organization requires manual operational controls with safety rules for critical applications.
+ You want defense-in-depth so that operations teams can manually override automated traffic routing if needed.

Route 53 health check execution blocks do not depend on the control plane. Health check record changes use the data plane, so they do not require the activating Region to process configuration updates. Route 53 health check execution blocks are sufficient in the following situations:
+ Your application can depend on the AWS Region that you are activating.
+ Automated traffic redirection as part of the recovery workflow meets your requirements.
+ Cost optimization is a priority. Route 53 health check execution blocks have lower cost than routing controls.

Most customers start with Route 53 health check execution blocks as the default traffic routing mechanism and add routing controls only for their most critical applications that require the highest reliability for the traffic management mechanism.

##### Lambda event source mapping execution block
<a name="lambda-event-source-mapping-block"></a>

The Lambda event source mapping execution block allows you to enable or disable Lambda event source mappings as part of your recovery operations. Event source mappings are Lambda resources that read from event sources such as Amazon Kinesis, Amazon DynamoDB Streams, Amazon Simple Queue Service, and Amazon Managed Streaming for Apache Kafka (Amazon MSK), and invoke Lambda functions with batches of records.

**Note**  
This execution block manages event source mappings only. Lambda triggers, which are service-side event-driven invocations from services such as Amazon S3, Amazon Simple Notification Service, and Amazon Simple Email Service, are not supported by this execution block.

###### Configuration
<a name="lambda-event-source-mapping-block-config"></a>

This block can be configured to perform one action (enable or disable) on one event source mapping resource at a time.

To configure a Lambda event source mapping execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Lambda event source mapping execution block sample policy](#security_iam_region_switch_lambda_esm).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Action: **Choose whether to **Enable** or **Disable** the event source mapping when this step runs.

1. **Lambda event source mapping ARN to enable or disable when activating/deactivating {{Region-1}}: **Enter the event source mapping ARN to act on when you activate/deactivate {{Region-1}}.

1. **Lambda event source mapping ARN to enable or disable when activating/deactivating {{Region-2}}: **Enter the event source mapping ARN to act on when you activate/deactivate {{Region-2}}.

1. **Timeout: **Enter a timeout value.

1. **Ungraceful execution: **Choose whether to skip this execution block during ungraceful (unplanned) executions.

Then, choose **Save step.**

The event source mappings must be in one of the Regions that the plan is configured for. However, the Region you are activating and the Region where the event source mapping is acted on do not need to match.

For example, to disable event processing in the deactivating Region when you activate the other Region:
+ **Event source mapping ARN to disable when activating {{us-west-2}}**: `arn:aws:lambda:{{us-east-1}}:123456789012:event-source-mapping:uuid-1`.
+ **Event source mapping ARN to disable when activating {{us-east-1}}**: `arn:aws:lambda:{{us-west-2}}:123456789012:event-source-mapping:uuid-2`.

This block supports both graceful and ungraceful execution modes. Ungraceful mode is designed for unplanned failover scenarios. You typically enable skipping the step during ungraceful executions on this execution block when the step is configured to perform an action in the deactivating Region. During a failover, you may want to stop processing events in deactivating Region and start processing in activating Region. To achieve this, you set up two Lambda event source mapping execution blocks in a sequence: one to disable the event source mapping resource in deactivating Region, and one to enable the event source mapping resource in activating Region. 

###### How it works
<a name="lambda-event-source-mapping-block-how"></a>

The Lambda event source mapping execution block enables or disables an event source mapping on a Lambda function. When the block is called during plan execution, Region switch invokes the Lambda `UpdateEventSourceMapping` API to perform the configured action (enable or disable) on the specified Lambda event source mapping. Region switch then waits until the event source mapping reaches the target state and updates the status of this step (complete or paused because of failure) before proceeding to the next step in the plan. If the mapping is already in the desired state, Region switch marks the step as complete immediately. When a plan containing this execution block configured for ungraceful execution is run in ungraceful mode, the plan skips the execution of this step.

#### Create child plans
<a name="working-with-rs-child-plan"></a>

To support more complex recovery scenarios, you can create child plans by adding them with Region switch plan execution blocks. The hierarchy is limited to two levels, but one parent plan can include multiple child plans.

**Important**  
Before you create a child plan, make sure that you have the correct IAM policy in place. For more information, see [Region switch plan execution block sample policy](#security_iam_region_switch_plan_execution).

For compatibility, child plans must support all Regions that the parent plan supports. In addition, the recovery approach, active/active or active/passive, must be the same for the parent and child plans.



Keep in mind the following ways in which a child plan respond to changes that you make to a parent plan and to parent plan scenarios.
+ A parent execution block is marked as completed when all child plans and other execution blocks within it are completed.
+ If any step fails in any child plan, the Region switch plan execution block fails in the parent plan.
+ Control actions that are initiated in the parent plan during the Region switch step, such as pause, a graceful or ungraceful switches, or a cancellation, are automatically attempted on the child plan, regardless of the child plan's current step.
+ Skips operations have a special behavior: the parent plan is skipped, but the child plan will still execute.
+ If a child plan is already executing in a Region switch block, to determine if it continues to run, Region switch assesses the child plan's compatibility with the parent plan. If the child plan's configuration matches the parent plan's requirements, Region switch treats the child plan as if it were initiated by the parent plan.
+ The parent plan step will fail if the child plan is running with incompatible configuration parameters, such as the following:
  + The child plan is operating in a different Region
  + The child plan is executing a deactivating operation when Region switch expects it to execute an activating operation
+ If the child plan completes successfully during a time that a parent plan is paused, the parent plan will succeed when the parent plan resumes.

#### Create a trigger for a Region switch plan
<a name="working-with-rs-triggers"></a>

If you want to automate recovery for your application in Region switch, you can create one or more triggers for your Region switch plan. Triggers automatically start executing a Region switch plan, based on CloudWatch alarm conditions that you choose.

#### To create a trigger for a Region switch plan


1. After you create a plan, on the **Plan details** page, select the **Triggers** tab.

1. Choose **Manage triggers**.

1. Select the workflows that you want to automate execution for, and then choose **Add trigger**.

1. Provide a description for the trigger.

1. Select a CloudWatch alarm, and then select up to 10 CloudWatch alarms to create the conditions for the trigger.

   When you select more than one condition, all conditions must be met before automated execution of the plan will start.

The trigger starts plan execution when a CloudWatch alarm transitions to meet the conditions for the trigger. When the trigger is added to the plan, if the conditions are already met, the plan does not execute, which prevents unintended failover events.

#### Execute a Region switch plan to recover an application
<a name="plan-execution-rs"></a>

To recover an application when an AWS Region is impaired, you execute a Region switch plan in Amazon Application Recovery Controller (ARC).
+ If your application is deployed with an active/active approach, the workflows in your plan deactivate the Region that is impaired so that your other active Region is appropriately scaled and begins to receive all of your application traffic. 
+ If your application is deployed with an active/passive approach, the workflows in your plan deactivate the impaired Region and activate your standby Region, by scaling up your resources there, if needed, and redirecting your application traffic to the standby Region. 

To perform application recovery manually, run your Region switch plan by doing the following.

Another option is to trigger an execution automatically with specific Amazon CloudWatch alarms that you specify to start a plan execution. You can specify triggers for plan execution when you create or update a plan. For more information, see [Create a trigger for a Region switch plan](#working-with-rs-triggers).

#### To execute a Region switch plan


1. In the AWS Management Console, navigate to the AWS Region that you want to activate for your application.

1. On the Amazon Application Recovery Controller (ARC) console, choose **Region switch**, and then select the plan that you want to run.

1. Choose **Execute plan**.

1. If your plan includes manual approval steps, approve each step when prompted.

While a plan is executing, you can track its progress on the execution details page, which opens when you choose to execute a plan. 

You can also view information about in-progress application recovery on the Region switch dashboards. On the Region switch console, in the left navigation, under **Region switch**, choose one of the following:
+ **Global dashboard**
+ **Executions in *Region name***

Be aware that, if there are impairments in a Region, the global dashboard might not show all your plan data. Because of this, we recommend that you rely only on Regional executions dashboard during operational events. The Regional executions dashboard is more resilient because it uses the local Region switch data plane. 

When plan execution is complete, you can see information about the plan execution, and other plans that Region switch has run, on the **Plan details** page in the **Plan execution history** tab.

### Region switch dashboards
<a name="region-switch.dashboarding-and-reports"></a>

Region switch includes a global dashboard that you can use to observe the state of Region switch plans across your organization and Regions. Region switch also has a Regional executions dashboard that displays only plan executions in the Region where you are currently logged in to the AWS Management Console.

Be aware that, if there are impairments in a Region, the global dashboard might not show all your plan data. Because of this, we recommend that you rely only on Regional executions dashboard during operational events. The Regional executions dashboard is more resilient because it uses the local Region switch data plane. 

### To open the Region switch global dashboard


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Under **Region switch**, choose **Global dashboard**.

### To open the Region switch Regional dashboard


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Under **Region switch**, choose **Regional dashboard**.

### Cross-account support in Region switch
<a name="cross-account-resources-rs"></a>

In Region switch, you can add resources from other accounts to your plans. You can also share a Region switch plan with other accounts. For more information, see the following sections.

#### Cross-account resources
<a name="cross-account-resources-rs-in-plan"></a>

Region switch allows resources to be hosted in an account that is separate from the account that contains the Region switch plan. When Region switch executes a plan, it assumes the executionRole. If the plan uses resources from an account that is different than the account that hosts the plan, then Region switch uses the executionRole to assume the crossAccountRole to access those resources.

Each resource in the Region switch plan has two optional fields: crossAccountRole and externalId.
+ crossAccountRole: This role allows access to resources in an account that is different than the account that hosts the Region switch plan. The role only needs permissions to act on the resources within its account – it does not need permissions to act on the resources in the account that hosts the Region switch plan.
+ ExternalId: This is the STS external ID from the trust policy of the account that contains the resource that requires action. It is an alphanumeric string that is the shared secret between the two accounts.

#### Sharing Region switch plans
<a name="sharing-plans"></a>

Region switch integrates with AWS Resource Access Manager (AWS RAM) to allow you to share plans across AWS accounts. When you share a plan, accounts that you specify can view the plan details, execute the plan, and view the plan's executions, which provides more control and flexibility for recovery capabilities across different teams.

To get started with cross-account sharing in Region switch, you create a resource share in AWS RAM. The resource share specifies participants who are authorized to share the plan that your account owns. Participants can view and execute the shared plan through the console, the CLI, or AWS SDKs.

Important: Your AWS account must own the plans that you want to share. You cannot share a plan that has been shared with you. To share a plan with your organization, or with an organizational unit in AWS Organizations, you must enable sharing with Organizations.

For more information about AWS RAM, see [Support sharing plans across accounts for ARC Region switch](#resource-sharing.region-switch). 

#### Support sharing plans across accounts for ARC Region switch
<a name="resource-sharing.region-switch"></a>

Amazon Application Recovery Controller (ARC) integrates with AWS Resource Access Manager to enable resource sharing. AWS RAM is a service that enables you to share resources with other AWS accounts or through AWS Organizations. For ARC Region switch, you can share the Region switch plan. (To use resources from another account in your plan, you use a crossAccount role. To learn more, see [Cross-account resources](#cross-account-resources-rs-in-plan).)

With AWS RAM, you share resources that you own by creating a *resource share*. A resource share specifies the resources to share, and the *participants* to share them with. Participants can include:
+ Specific AWS accounts inside or outside of owner's organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations

For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.

By using AWS Resource Access Manager to share plans across accounts in ARC, you can use one plan with several different AWS accounts. When you opt to share a plan, other AWS accounts that you specify can execute the plan to perform application recovery.

AWS RAM is a service that helps AWS customers to securely share resources across AWS accounts. With AWS RAM, you can share resources within an organization or organizational units (OUs) in AWS Organizations, by using IAM roles and users. AWS RAM is a centralized and controlled way to share a plan. 

When you share a plan, you can reduce the number of total plans that your organization requires. With a shared plan, you can allocate the total cost of running the plan across different teams, to maximize the benefits of ARC with lower cost. Sharing plans across accounts can also ease the process of onboarding multiple applications to ARC, especially if you have a large number of applications distributed across several accounts and operations teams.

To get started with cross-account sharing in ARC, you create a *resource share* i n AWS RAM. The resource share specifies *participants* who are authorized to share the plan that your account owns.

This topic explains how to share resources that you own, and how to use resources that are shared with you.

**Topics**
+ [Prerequisites for sharing plans](#sharing-prereqs-rs)
+ [Sharing a plan](#sharing-share-rs)
+ [Unsharing a shared plan](#sharing-unshare-rs)
+ [Identifying a shared plan](#sharing-identify-rs)
+ [Responsibilities and permissions for shared plans](#sharing-perms-rs)
+ [Billing costs](#sharing-billing-rs)
+ [Quotas](#sharing-quotas-rs)

##### Prerequisites for sharing plans
<a name="sharing-prereqs-rs"></a>
+ To share a plan, you must own it in your AWS account. This means that the resource must be allocated or provisioned in your account. You cannot share a plan that has been shared with you.
+ To share a plan with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [ Enable sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

##### Sharing a plan
<a name="sharing-share-rs"></a>

When you share a plan, the participants that you specify to share the plan can view and, if you grant additional permissions, execute the plan.

To share a plan, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the participants they're shared with. To share a plan you can create a new resource share or add the resource to an existing resource share. To create a new resource share, you can use the [AWS RAM console](https://console.aws.amazon.com/ram), or use AWS RAM API operations with the AWS Command Line Interface or AWS SDKs.

If you are part of an organization in AWS Organizations and sharing within your organization is enabled, participants in your organization are automatically granted access to the shared plan. Otherwise, participants receive an invitation to join the resource share and are granted access to the shared plan after accepting the invitation.

You can share a plan that you own by using the AWS RAM console, or by using AWS RAM API operations with the AWS CLI or SDKs.

**To share a plan that you own by using the AWS RAM console**  
See [ Creating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html) in the *AWS RAM User Guide*.

**To share a plan that you own by using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command.

**Granting permissions to share plans**

Sharing plans across accounts requires the following additional permissions for the IAM principal sharing the plan by using AWS RAM:

```
# read and execute plan permissions
"arc-region-switch:GetPlan",
"arc-region-switch:GetPlanInRegion",  
"arc-region-switch:GetPlanExecution",  
"arc-region-switch:ListPlanExecutionEvents",
"arc-region-switch:ListPlanExecutions", 
"arc-region-switch:ListRoute53HealthChecks",  
"arc-region-switch:GetPlanEvaluationStatus",
"arc-region-switch:StartPlanExecution",
"arc-region-switch:CancelPlanExecution",  
"arc-region-switch:UpdatePlanExecution", 
"arc-region-switch:UpdatePlanExecutionStep"
```

The owner who shares the plan must have the following permissions. If you attempt to share a plan through AWS RAM without having these permissions, an error is returned.

```
"arc-region-switch:PutResourcePolicy" # Permission only apis
"arc-region-switch:DeleteResourcePolicy" # Permission only apis
"arc-region-switch:GetResourcePolicy" # Permission only apis
```

For more information about the way that AWS Resource Access Manager uses IAM see [ How AWS Resource Access Manager uses IAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html) in the *AWS RAM User Guide*.

##### Unsharing a shared plan
<a name="sharing-unshare-rs"></a>

When you unshare a plan, the following applies to participants and owners:
+ Participants can no longer view or execute the unshared plan.

To unshare a shared plan that you own, remove it from the resource share. You can do this by using the AWS RAM console or by using AWS RAM API operations with the AWS CLI or SDKs.

**To unshare a shared plan that you own using the AWS RAM console**  
See [Updating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared plan that you own using the AWS CLI**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

##### Identifying a shared plan
<a name="sharing-identify-rs"></a>

Owners and participants can identify shared plans by viewing information in AWS RAM. They can also get information about shared resources by using the ARC console and AWS CLI.

In general, to learn more about the resources that you've shared or that have been shared with you, see the information in the AWS Resource Access Manager User Guide:
+ As an owner, you can view all resources that you are sharing with others by using AWS RAM. For more information, see [Viewing your shared resources in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-view-sr.html).
+ As a participant, you can view all resources shared with you by using AWS RAM. For more information, see [Viewing your shared resources in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-view-sr.html).

As an owner, you can determine if you're sharing a plan by viewing information in the AWS Management Console or by using the AWS Command Line Interface with ARC API operations.

**To identify if a plan that you own is shared by using the console**  
In the AWS Management Console, on the details page for a plan, see the **plan sharing status**.

As a participant, when a plan is shared with you, you typically must accept the share so that you can access the plan.

##### Responsibilities and permissions for shared plans
<a name="sharing-perms-rs"></a>

###### Permissions for owners
<a name="perms-owner-rs"></a>

Participants can view or execute the plan (if they have the correct permissions). 

###### Permissions for participants
<a name="perms-consumer-rs"></a>

When you share a plan that you own with other AWS accounts, participants can view or execute the plan (if they have the correct permissions). 

When you share a plan by using AWS RAM, a participant has, by default, read-only permissions. To review a list of read-only permissions for Region switch, see [Read-only permissions](#security_iam_region_switch_read_only). Participants need additional permissions to execute a Region switch plan. Participants who need to execute plans need additional permissions. Be aware that you cannot grant permission to a AWS RAM participant for the following operations:
+ ` ApprovePlanExecutionStep`
+ ` UpdatePlan`

##### Billing costs
<a name="sharing-billing-rs"></a>

The owner of a plan in ARC is billed for costs associated with the plan. There are no additional costs, for plan owners or for participants, for creating resources hosted in a plan.

For detailed pricing information and examples, see [Amazon Application Recovery Controller (ARC) Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

##### Quotas
<a name="sharing-quotas-rs"></a>

All resources created in a shared plan count toward quotas for the plan owner.

For a list of Region switch plan quotas, see [Quotas for Region switch](#quotas.region-switch).

### Identity and Access Management for Region switch in ARC
<a name="security-iam-region-switch"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use ARC resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [How Region switch works with IAM](#security_iam_service-with-iam-region-switch)
+ [Identity-based policy examples](#security_iam_id-based-policy-examples-region-switch)

#### How Region switch in ARC works with IAM
<a name="security_iam_service-with-iam-region-switch"></a>

Before you use IAM to manage access to ARC, learn what IAM features are available to use with ARC.

Before you use IAM to manage access to Region switch in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with Region switch.


**IAM features you can use with Region switch in Amazon Application Recovery Controller (ARC)**  

| IAM feature | Region switch support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-region-switch-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-region-switch-resource-based-policies) |  Yes | 
| [Policy actions](#security_iam_service-with-iam-region-switch-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-region-switch-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-region-switch-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-region-switch-acls) |  Yes | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-region-switch-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-region-switch-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-region-switch-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-region-switch-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-region-switch-roles-service-linked) |  No  | 

To get a high-level, overall view of how AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Identity-based policies for Region switch
<a name="security_iam_service-with-iam-region-switch-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To view examples of ARC identity-based policies, see [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](#security_iam_id-based-policy-examples).

##### Resource-based policies within Region switch
<a name="security_iam_service-with-iam-region-switch-resource-based-policies"></a>

**Supports resource-based policies:** Yes

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

##### Policy actions for Region switch
<a name="security_iam_service-with-iam-region-switch-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in ARC for Region switch use the following prefixes before the action:

```
arc-region-switch
```

To specify multiple actions in a single statement, separate them with commas. For example, the following:

```
"Action": [
      "arc-region-switch:{{action1}}",
      "arc-region-switch:{{action2}}"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "arc-region-switch:Describe*"
```

To view examples of ARC identity-based policies for Region switch, see [Identity-based policy examples for Region switch in ARC](#security_iam_id-based-policy-examples-region-switch).

##### Policy resources for Region switch
<a name="security_iam_service-with-iam-region-switch-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To view examples of ARC identity-based policies for Region switch, see [Identity-based policy examples for Region switch in ARC](#security_iam_id-based-policy-examples-region-switch).

##### Policy condition keys for Region switch
<a name="security_iam_service-with-iam-region-switch-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To view examples of ARC identity-based policies for Region switch, see [Identity-based policy examples for Region switch in ARC](#security_iam_id-based-policy-examples-region-switch).

##### Access control lists (ACLs) in Region switch
<a name="security_iam_service-with-iam-region-switch-acls"></a>

**Supports ACLs:** Yes

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

##### Attribute-based access control (ABAC) with Region switch
<a name="security_iam_service-with-iam-region-switch-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

##### Using temporary credentials with Region switch
<a name="security_iam_service-with-iam-region-switch-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

##### Cross-service principal permissions for Region switch
<a name="security_iam_service-with-iam-region-switch-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

When you use an IAM entity (user or role) to perform actions in AWS, you are considered a principal. Policies grant permissions to a principal. When you use some services, you might perform an action that then triggers another action in a different service. In this case, you must have permissions to perform both actions.

##### Service roles for Region switch
<a name="security_iam_service-with-iam-region-switch-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

##### Service-linked roles for Region switch
<a name="security_iam_service-with-iam-region-switch-roles-service-linked"></a>

**Supports service-linked roles:** No 

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.

#### Identity-based policy examples for Region switch in ARC
<a name="security_iam_id-based-policy-examples-region-switch"></a>

By default, users and roles don't have permission to create or modify ARC resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by ARC, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices-zonal)
+ [Plan execution role trust policy](#security_iam_region_switch_trust_policy)
+ [Full access permissions](#security_iam_region_switch_full_access)
+ [Read-only permissions](#security_iam_region_switch_read_only)
+ [Execution block permissions](#security_iam_region_switch_execution_blocks)
+ [CloudWatch alarms for application health permissions](#security_iam_region_switch_cloudwatch)
+ [Automatic plan execution reports permissions](#security_iam_region_switch_reports)
+ [Cross-account resource permissions](#security_iam_region_switch_cross_account)
+ [Complete plan execution role permissions](#security_iam_region_switch_complete_policy)

##### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices-zonal"></a>

Identity-based policies determine whether someone can create, access, or delete ARC resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

##### Plan execution role trust policy
<a name="security_iam_region_switch_trust_policy"></a>

 Region switch assumes your plan's execution role to perform actions on your behalf. This trust policy authorizes the `arc-region-switch.amazonaws.com` service principal to assume the role. 

 Region switch assumes the execution role in two cases: 
+  Region switch assumes the execution role during plan evaluation to validate your plan configuration. For the complete list of warnings surfaced during plan evaluation, see [Plan evaluation for Region switch plans](#working-with-rs-plan-evaluation). 
+  Region switch assumes the execution role during plan execution when an execution block acts on resources in your account, such as database failover, Auto Scaling capacity, Amazon ECS or Amazon EKS capacity, Lambda invocations, or routing-control blocks. 

 If the trust policy is missing, Region switch cannot assume the role. During plan evaluation, a warning is generated stating that the role cannot be assumed. During execution, any execution block that requires the execution role to act on resources in your account fails. The error states that the role could not be assumed. 

 The manual approval and Route 53 health check execution blocks do not assume the execution role as part of a plan execution. As a result, a plan composed only of these blocks can execute successfully even if the trust policy is missing. We recommend applying the trust policy to your execution role so that plan evaluation can identify any issues with your plan configuration. 

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
        "Service": "arc-region-switch.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

##### Full access permissions
<a name="security_iam_region_switch_full_access"></a>

The following IAM policy grants full access for all Region switch APIs:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "arc-region-switch.amazonaws.com"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "arc-region-switch:CreatePlan",
        "arc-region-switch:UpdatePlan",
        "arc-region-switch:GetPlan",
        "arc-region-switch:ListPlans",
        "arc-region-switch:DeletePlan",
        "arc-region-switch:GetPlanInRegion",
        "arc-region-switch:ListPlansInRegion",
        "arc-region-switch:ApprovePlanExecutionStep",
        "arc-region-switch:GetPlanEvaluationStatus",
        "arc-region-switch:GetPlanExecution",
        "arc-region-switch:StartPlanExecution",
        "arc-region-switch:CancelPlanExecution",
        "arc-region-switch:ListRoute53HealthChecks",
        "arc-region-switch:ListRoute53HealthChecksInRegion",
        "arc-region-switch:ListPlanExecutions",
        "arc-region-switch:ListPlanExecutionEvents",
        "arc-region-switch:ListTagsForResource", 
        "arc-region-switch:TagResource",
        "arc-region-switch:UntagResource",
        "arc-region-switch:UpdatePlanExecution",
        "arc-region-switch:UpdatePlanExecutionStep"
      ],
      "Resource": "*"
    }
  ]
}
```

------

##### Read-only permissions
<a name="security_iam_region_switch_read_only"></a>

 The following IAM policy grants read-only access permissions for Region switch: 

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
        "arc-region-switch:GetPlan",
        "arc-region-switch:ListPlans",
        "arc-region-switch:GetPlanInRegion",
        "arc-region-switch:ListPlansInRegion",
        "arc-region-switch:GetPlanEvaluationStatus",
        "arc-region-switch:GetPlanExecution",
        "arc-region-switch:ListRoute53HealthChecks",
        "arc-region-switch:ListRoute53HealthChecksInRegion",
        "arc-region-switch:ListPlanExecutions",
        "arc-region-switch:ListPlanExecutionEvents",
        "arc-region-switch:ListTagsForResource"
      ],
      "Resource": "*"
    }
  ]
}
```

------

##### Execution block permissions
<a name="security_iam_region_switch_execution_blocks"></a>

 The following sections provide sample IAM policies that provide the required permissions for specific execution blocks that you add to a Region switch plan. 

**Topics**
+ [EC2 Auto Scaling execution block sample policy](#security_iam_region_switch_ec2_autoscaling)
+ [Amazon EKS resource scaling execution block sample policy](#security_iam_region_switch_eks)
+ [Amazon ECS service scaling execution block sample policy](#security_iam_region_switch_ecs)
+ [ARC routing controls execution block sample policy](#security_iam_region_switch_arc_routing)
+ [Aurora Global Database execution block sample policy](#security_iam_region_switch_aurora)
+ [Amazon DocumentDB Global Cluster execution block sample policy](#security_iam_region_switch_documentdb)
+ [Amazon Neptune Global Cluster execution block sample policy](#security_iam_region_switch_neptune)
+ [Amazon RDS execution block sample policy](#security_iam_region_switch_rds)
+ [Aurora provisioned scaling execution block sample policy](#security_iam_region_switch_aurora_provisioned_scaling)
+ [Aurora serverless scaling execution block sample policy](#security_iam_region_switch_aurora_serverless_scaling)
+ [Amazon RDS Switchover Read Replica execution block sample policy](#security_iam_region_switch_rds_switchover_read_replica)
+ [Manual approval execution block sample policy](#security_iam_region_switch_manual_approval)
+ [Custom action Lambda execution block sample policy](#security_iam_region_switch_lambda)
+ [Route 53 health check execution block sample policy](#security_iam_region_switch_route53)
+ [Lambda event source mapping execution block sample policy](#security_iam_region_switch_lambda_esm)
+ [Region switch plan execution block sample policy](#security_iam_region_switch_plan_execution)

###### EC2 Auto Scaling execution block sample policy
<a name="security_iam_region_switch_ec2_autoscaling"></a>

**(Optional) Permission to wait for target group health**  
 When the `waitELBTargetGroupHealthy` option is enabled on your EC2 Auto Scaling execution block, add the `elasticloadbalancing:DescribeTargetHealth` permission. If this option is disabled, you can omit this permission. For more information about this option, see [Amazon EC2 Auto Scaling group execution block](#ec2-auto-scaling-block). 

 The following is a sample JSON policy to attach if you add execution blocks to a Region switch plan for EC2 Auto Scaling groups: 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "autoscaling:DescribeAutoScalingGroups"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "autoscaling:UpdateAutoScalingGroup"
      ],
      "Resource": [
        "arn:aws:autoscaling:us-east-1:111122223333:autoScalingGroup:123d456e-123e-1111-abcd-EXAMPLE22222:autoScalingGroupName/app-asg-primary",
        "arn:aws:autoscaling:us-west-2:111122223333:autoScalingGroup:1234a321-123e-1234-aabb-EXAMPLE33333:autoScalingGroupName/app-asg-secondary"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "cloudwatch:namespace": "AWS/AutoScaling"
        }
      }
    },
    {
      "Sid": "RequiredOnlyWhenWaitELBTargetGroupHealthyEnabled",
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeTargetHealth"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Amazon EKS resource scaling execution block sample policy
<a name="security_iam_region_switch_eks"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon EKS resource scaling. 

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
        "eks:DescribeCluster"
      ],
      "Resource": [
        "arn:aws:eks:us-east-1:123456789012:cluster/app-eks-primary",
        "arn:aws:eks:us-west-2:123456789012:cluster/app-eks-secondary"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "eks:ListAssociatedAccessPolicies"
      ],
      "Resource": [
        "arn:aws:eks:us-east-1:123456789012:access-entry/app-eks-primary/*",
        "arn:aws:eks:us-west-2:123456789012:access-entry/app-eks-secondary/*"
      ]
    }
  ]
}
```

------

 Note: In addition to this IAM policy, the plan execution role needs to be added to the Amazon EKS cluster's access entries with the `AmazonArcRegionSwitchScalingPolicy` access policy. For more information, see [Configure EKS access entry permissions](#eks-resource-scaling-block-permissions). 

###### Amazon ECS service scaling execution block sample policy
<a name="security_iam_region_switch_ecs"></a>

**(Optional) Permissions to wait for target group health**  
 When the `waitELBTargetGroupHealthy` option is enabled on your Amazon ECS service scaling execution block, add the following permissions. For more information about this option, see [Amazon ECS service scaling execution block](#ecs-service-scaling-block).   
`ecs:ListTasks` — to list the service's running tasks so Region switch knows which targets to check.
`ecs:DescribeTasks` — to get each task's network details (the task ENI IP address, or the container instance and host port) that identify its target group entry.
`elasticloadbalancing:DescribeTargetHealth` — to read the health of the service's targets in the associated target groups.
`ecs:DescribeContainerInstances` — to resolve a task's container instance to its EC2 instance ID for target matching. Required only when the service runs tasks that use the `bridge` or `host` network mode.
 If `waitELBTargetGroupHealthy` option is disabled, you can omit these permissions. 

 The following is a sample JSON policy to attach if you add execution blocks to a Region switch plan for Amazon ECS service scaling: 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeServices",
        "ecs:UpdateService"
      ],
      "Resource": [
        "arn:aws:ecs:us-east-1:111122223333:service/app-cluster-primary/app-service",
        "arn:aws:ecs:us-west-2:111122223333:service/app-cluster-secondary/app-service"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeClusters"
      ],
      "Resource": [
        "arn:aws:ecs:us-east-1:111122223333:cluster/app-cluster-primary",
        "arn:aws:ecs:us-west-2:111122223333:cluster/app-cluster-secondary"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecs:ListServices"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "application-autoscaling:DescribeScalableTargets",
        "application-autoscaling:RegisterScalableTarget"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*"
    },
    {
      "Sid": "RequiredOnlyWhenWaitELBTargetGroupHealthyEnabled",
      "Effect": "Allow",
      "Action": [
        "ecs:ListTasks",
        "elasticloadbalancing:DescribeTargetHealth"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DescribeTasksWhenWaitELBTargetGroupHealthyEnabled",
      "Effect": "Allow",
      "Action": [
         "ecs:DescribeTasks"
      ],
      "Resource": [
         "arn:aws:ecs:us-east-1:111122223333:task/app-cluster-primary/*",
         "arn:aws:ecs:us-west-2:111122223333:task/app-cluster-secondary/*"
      ]
    },
    {
      "Sid": "RequiredOnlyForBridgeOrHostNetworkModeTasks",
      "Effect": "Allow",
      "Action": [
         "ecs:DescribeContainerInstances"
      ],
      "Resource": [
         "arn:aws:ecs:us-east-1:111122223333:container-instance/app-cluster-primary/*",
         "arn:aws:ecs:us-west-2:111122223333:container-instance/app-cluster-secondary/*"
      ]
    }
  ]
}
```

###### ARC routing controls execution block sample policy
<a name="security_iam_region_switch_arc_routing"></a>

 Note: The Amazon ARC routing controls execution block requires that any service control policies (SCPs) applied to the plan's execution role allow the access to the following Regions for these services: 
+ `route53-recovery-control-config: us-west-2`
+ `route53-recovery-cluster: us-west-2, us-east-1, eu-west-1, ap-southeast-2, ap-northeast-1`

The following is a sample policy to attach if you add execution blocks to a Region switch plan for ARC routing controls.

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
        "route53-recovery-control-config:DescribeControlPanel",
        "route53-recovery-control-config:DescribeCluster"
      ],
      "Resource": [
        "arn:aws:route53-recovery-control::123456789012:controlpanel/abcd1234abcd1234abcd1234abcd1234",
        "arn:aws:route53-recovery-control::123456789012:cluster/4b325d3b-0e28-4dcf-ba4a-EXAMPLE11111"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "route53-recovery-cluster:GetRoutingControlState",
        "route53-recovery-cluster:UpdateRoutingControlStates"
      ],
      "Resource": [
        "arn:aws:route53-recovery-control::123456789012:controlpanel/1234567890abcdef1234567890abcdef/routingcontrol/abcdef1234567890", 
        "arn:aws:route53-recovery-control::123456789012:controlpanel/1234567890abcdef1234567890abcdef/routingcontrol/1234567890abcdef" 
      ]
    }
  ]
}
```

------

You can retrieve the routing control control panel ID and the cluster ID by using CLI. For more information, see [Set up routing control components](#getting-started-cli-routing-config).

###### Aurora Global Database execution block sample policy
<a name="security_iam_region_switch_aurora"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Aurora databases. 

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
        "rds:DescribeGlobalClusters",
        "rds:DescribeDBClusters"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "rds:FailoverGlobalCluster",
        "rds:SwitchoverGlobalCluster"
      ],
      "Resource": [
        "arn:aws:rds::123456789012:global-cluster:app-global-db",
	      "arn:aws:rds:us-east-1:123456789012:cluster:app-db-primary", 
        "arn:aws:rds:us-west-2:123456789012:cluster:app-db-secondary"  
      ]
    }
  ]
}
```

------

###### Amazon DocumentDB Global Cluster execution block sample policy
<a name="security_iam_region_switch_documentdb"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon DocumentDB global clusters. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeGlobalClusters",
        "rds:DescribeDBClusters",
        "rds:FailoverGlobalCluster",
        "rds:SwitchoverGlobalCluster"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Amazon Neptune Global Cluster execution block sample policy
<a name="security_iam_region_switch_neptune"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon Neptune global clusters. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeGlobalClusters",
        "rds:DescribeDBClusters",
        "rds:FailoverGlobalCluster",
        "rds:SwitchoverGlobalCluster"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Amazon RDS execution block sample policy
<a name="security_iam_region_switch_rds"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon RDS read replica promotion or cross-Region replica creation. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:PromoteReadReplica",
        "rds:CreateDBInstanceReadReplica",
        "rds:ModifyDBInstance"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Aurora provisioned scaling execution block sample policy
<a name="security_iam_region_switch_aurora_provisioned_scaling"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Aurora provisioned cluster scaling. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:DescribeDBClusters",
        "rds:DescribeGlobalClusters",
        "rds:CreateDBInstance",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:db:{{instance-name}}",
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:cluster:{{cluster-name}}",
        "arn:aws:rds::{{111122223333}}:global-cluster:{{global-cluster-name}}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeOrderableDBInstanceOptions",
        "ec2:DescribeInstanceTypes"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Aurora serverless scaling execution block sample policy
<a name="security_iam_region_switch_aurora_serverless_scaling"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Aurora Serverless cluster scaling. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:DescribeDBClusters",
        "rds:DescribeGlobalClusters",
        "rds:ModifyDBCluster",
        "rds:RebootDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:cluster:{{cluster-name}}",
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:db:{{instance-name}}",
        "arn:aws:rds::{{111122223333}}:global-cluster:{{global-cluster-name}}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricData"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstanceTypes"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Amazon RDS Switchover Read Replica execution block sample policy
<a name="security_iam_region_switch_rds_switchover_read_replica"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon RDS Oracle read replica switchover. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:SwitchoverReadReplica",
        "rds:DescribePendingMaintenanceActions",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:db:{{instance-name}}"
      ]
    }
  ]
}
```

If you configure an ungraceful behavior (`promoteReadReplica`), add the following action to the policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:SwitchoverReadReplica",
        "rds:DescribePendingMaintenanceActions",
        "rds:PromoteReadReplica",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:db:{{instance-name}}"
      ]
    }
  ]
}
```

###### Manual approval execution block sample policy
<a name="security_iam_region_switch_manual_approval"></a>

The following is a sample policy to attach if you add execution blocks to a Region switch plan for manual approvals.

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
        "arc-region-switch:ApprovePlanExecutionStep"
      ],
      "Resource": "arn:aws:arc-region-switch::123456789012:plan/sample-plan:0123abc"
    }
  ]
}
```

------

###### Custom action Lambda execution block sample policy
<a name="security_iam_region_switch_lambda"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Lambda functions. 

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
        "lambda:GetFunction",
        "lambda:InvokeFunction"
      ],
      "Resource": [
        "arn:aws:lambda:us-east-1:123456789012:function:app-recovery-primary",
        "arn:aws:lambda:us-west-2:123456789012:function:app-recovery-secondary"
      ]
    }
  ]
}
```

------

###### Route 53 health check execution block sample policy
<a name="security_iam_region_switch_route53"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Route 53 health checks. 

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
        "route53:ListResourceRecordSets"
      ],
      "Resource": [
        "arn:aws:route53:::hostedzone/Z1234567890ABCDEFGHIJ"
      ]
    }
  ]
}
```

------

###### Lambda event source mapping execution block sample policy
<a name="security_iam_region_switch_lambda_esm"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Lambda event source mappings. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:GetEventSourceMapping",
        "lambda:UpdateEventSourceMapping"
      ],
      "Resource": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:event-source-mapping:{{uuid}}"
    },
    {
      "Effect": "Allow",
      "Action": [
        "lambda:GetFunction"
      ],
      "Resource": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:function:{{function-name}}"
    }
  ]
}
```

###### Region switch plan execution block sample policy
<a name="security_iam_region_switch_plan_execution"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan to run child plans. 

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
        "arc-region-switch:StartPlanExecution",
        "arc-region-switch:GetPlanExecution",
        "arc-region-switch:CancelPlanExecution",
        "arc-region-switch:UpdatePlanExecution",
        "arc-region-switch:ListPlanExecutions"
      ],
      "Resource": [
        "arn:aws:arc-region-switch::123456789012:plan/child-plan-1/abcde1",
        "arn:aws:arc-region-switch::123456789012:plan/child-plan-2/fghij2"
      ]
    }
  ]
}
```

------

##### CloudWatch alarms for application health permissions
<a name="security_iam_region_switch_cloudwatch"></a>

 The following is a sample policy to attach to access CloudWatch alarms for application health, which are used to help determine actual recovery time. 

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
        "cloudwatch:DescribeAlarmHistory",
        "cloudwatch:DescribeAlarms"
      ],
      "Resource": [
        "arn:aws:cloudwatch:us-east-1:123456789012:alarm:app-health-primary",
        "arn:aws:cloudwatch:us-west-2:123456789012:alarm:app-health-secondary"
      ]
    }
  ]
}
```

------

##### Automatic plan execution reports permissions
<a name="security_iam_region_switch_reports"></a>

 The following is a sample policy to attach if you configure automatic report generation for a Region switch plan. This policy includes permissions to write reports to Amazon S3, access CloudWatch alarm data, and retrieve child plan information for parent plans. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:DescribeAlarms",
        "cloudwatch:DescribeAlarmHistory"
      ],
      "Resource": [
        "arn:aws:cloudwatch:us-east-1:111122223333:alarm:app-health-primary",
        "arn:aws:cloudwatch:us-west-2:111122223333:alarm:app-health-secondary"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "arc-region-switch:GetPlanExecution",
        "arc-region-switch:ListPlanExecutionEvents"
      ],
      "Resource": [
        "arn:aws:arc-region-switch::111122223333:plan/child-plan-1/abcde1",
        "arn:aws:arc-region-switch::111122223333:plan/child-plan-2/fghij2"
      ]
    }
  ]
}
```

 Note: If you configure a customer managed AWS KMS key for Amazon S3 bucket encryption, you must also add `kms:GenerateDataKey` and `kms:Encrypt` permissions for the key. 

##### Cross-account resource permissions
<a name="security_iam_region_switch_cross_account"></a>

 If resources are in different accounts, you'll need a cross-account role. The following is a sample trust policy for a cross-account role. 

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
        "AWS": "arn:aws:iam::123456789012:role/RegionSwitchExecutionRole"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "UniqueExternalId123"
        }
      }
    }
  ]
}
```

------

 And the following is the permission for the plan execution role to assume this cross-account role: 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::987654321098:role/RegionSwitchCrossAccountRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "UniqueExternalId123"
        }
      }
    }
  ]
}
```

------

##### Complete plan execution role permissions
<a name="security_iam_region_switch_complete_policy"></a>

 Creating a comprehensive policy that includes permissions for all execution blocks would require a policy that is quite large. In practice, you should only include permissions for the execution blocks that you use in your specific plans. 

The following is an example policy that you can use as a starting place for a plan execution role policy. Make sure that you add additional policies that required for specific execution blocks that you include in your plan. Only include the permissions required for the specific execution blocks that you use in your plan, to follow the principle of least privilege

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:SimulatePrincipalPolicy",
            "Resource": "arn:aws:iam::123456789012:role/RegionSwitchExecutionRole"
        },
        {
            "Effect": "Allow",
            "Action": [
                "arc-region-switch:GetPlan",
                "arc-region-switch:GetPlanExecution",
                "arc-region-switch:ListPlanExecutions"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Logging and monitoring for Region switch in ARC
<a name="logging-and-monitoring-rs"></a>

You can use Amazon CloudWatch, AWS CloudTrail, and Amazon EventBridge for monitoring Region switch in Amazon Application Recovery Controller (ARC), to get alerts, analyze patterns, and help troubleshoot issues.

**Topics**
+ [Logging Region switch API calls using AWS CloudTrail](#cloudtrail-region-switch)
+ [Using Region switch in ARC with Amazon EventBridge](#eventbridge-region-switch)

#### Logging Region switch API calls using AWS CloudTrail
<a name="cloudtrail-region-switch"></a>

Amazon Application Recovery Controller (ARC) Region switch is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in ARC. CloudTrail captures all API calls for ARC as events. The calls captured include calls from the ARC console and code calls to the ARC API operations. 

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for ARC. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**.

Using the information collected by CloudTrail, you can determine the request that was made to ARC, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

##### ARC information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in ARC, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for ARC, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All ARC actions are logged by CloudTrail and are documented in the TBD API REFERENCE LINK. For example, calls to the `TBD`, `TBD` and `TBD` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

##### Viewing Region switch events in event history
<a name="amazon-arc-events-in-cloudtrail-event-history-rs"></a>

CloudTrail lets you view recent events in **Event history**. Most events for Region switch API requests are in the Region where you work with a Region switch plan, for example, where you create a plan or execute a plan. However, some Region switch actions that you run in the ARC console are made using control plan API operations, rather than data plane operations. For control plane operations, you view events in US East (N. Virginia). To learn about which API calls are control plane operations, see [Region switch API operations](#actions.region-switch).

##### Understanding ARC log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `StartPlanExecution` action for Region switch.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/admin",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA33L3W36EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/admin",
                "accountId": "111122223333",
                "userName": "EXAMPLENAME"
            },
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2025-07-06T17:38:05Z"
            }
        }
    },
    "eventTime": "2025-07-06T18:08:03Z",
    "eventSource": "arc-region-switch.amazonaws.com",
    "eventName": "StartPlanExecution",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.50",
    "userAgent": "Boto3/1.17.101 Python/3.8.10 Linux/4.14.231-180.360.amzn2.x86_64 exec-env/AWS_Lambda_python3.8 Botocore/1.20.102",
    "requestParameters": {
        "planArn": "arn:aws:arc-region-switch::555555555555:plan/CloudTrailIntegTestPlan:bbbbb",
        "targetRegion": "us-east-1",
        "action": "activate"    }
    "responseElements": {
        "executionId": "us-east-1/dddddddEXAMPLE",
        "plan": "arn:aws:arc-region-switch::555555555555:plan/CloudTrailIntegTestPlan:bbbbb",
        "planVersion": "1",
        "activateRegion": "us-east-1"    },
    "requestID": "fd42dcf7-6446-41e9-b408-d096example",
    "eventID": "4b5c42df-1174-46c8-be99-d67aexample",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
      "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "us-east-1.arc.amazon.aws"
}
```

#### Using Region switch in ARC with Amazon EventBridge
<a name="eventbridge-region-switch"></a>

Using Amazon EventBridge, you can set up event-driven rules that monitor your Region switch resources in Amazon Application Recovery Controller (ARC), and then initiate target actions that use other AWS services. For example, you can set a rule for sending out email notifications by signaling an Amazon SNS topic whenever a Region switch plan completes execution.

You can create rules in Amazon EventBridge to act on the following ARC Region switch events:
+ *Region switch plan execution.* The event specifies that a Region switch plan has been run (executed).
+ *Region switch plan evaluation.* The event specifies that a Region switch plan evaluation has completed.

To capture specific ARC events that you're interested in, define event-specific patterns that EventBridge can use to detect the events. Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for. 

Events are emitted on a best effort basis. They're delivered from ARC to EventBridge in near real-time under normal operational circumstances. However, situations can arise that might delay or prevent delivery of an event.

For information about how EventBridge rules work with event patterns, see [Events and Event Patterns in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html). 

##### Monitor a Region switch resource with EventBridge
<a name="arc-eventbridge-tasks-readiness"></a>

With EventBridge, you can create rules that define actions to take when ARC emits events for Region switch resources. 

To type or copy and paste an event pattern into the EventBridge console, in the console, select to the option **Enter my own** option. To help you determine event patterns that might be useful for you, this topic includes [example Region switch patterns](#arc-eventbridge-examples-region-switch).

**To create a rule for a resource event**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. For the AWS Region to create the rule in, choose the Region where you created the plan that you want to monitor events for.

1. Choose **Create rule**.

1. Enter a **Name** for the rule, and, optionally, a description.

1. For **Event bus**, leave the default value, **default**.

1. Choose **Next**.

1. For the **Build event pattern** step, for **Event source**, leave the default value, **AWS events**.

1. Under **Sample event**, choose **Enter my own**.

1. For **Sample events**, type or copy and paste an event pattern. For examples, see the next section.

##### Example Region switch patterns
<a name="arc-eventbridge-examples-region-switch"></a>

Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for.

You can copy and paste event patterns from this section into EventBridge to create rules that you can use to monitor ARC actions and resources.

The following event patterns provide examples that you might use in EventBridge for the Region switch capability in ARC.
+ *Select all events from Region switch for PlanExecution*.

  ```
  {
      "source": [ "aws.arc-region-switch" ],
      "detail-type": [ "ARC Region Switch Plan Execution" ] 
  }
  ```
+ *Select all events from Region switch for PlanEvaluation*.

  ```
      	{
      	"source": [ "aws.arc-region-switch" ],
      	"detail-type": [ "ARC Region Switch Plan Evaluation" ] 
      	}
  ```

The following is an example ARC event for a *Region switch plan execution*:

```
{
  	"version": "0",
  	"id": "1111111-bbbb-aaaa-cccc-dddddEXAMPLE", # Random uuid
  	"detail-type": "ARC Region Switch Plan Execution",
  	"source": "aws.arc-region-switch",
  	"account": "111122223333",
  	"time": "2023-11-16T23:38:14Z",
  	"region": "us-east-1",
  	"resources": ["arn:aws:arc-region-switch::111122223333:plan/aaaaaExample"], # planArn
  	"detail": {
  		"version": "0.0.1",
  		"eventType": "ExecutionStarted",
  		"executionId": "bbbbbbEXAMPLE",
  		"executionAction": "activating/deactivating {region}",
  		"idempotencyKey": "1111111-2222-3333-4444-5555555555", # As there is a possibility of dual logging
  	}
}
```

The following is an example ARC event for a *Region switch plan step level execution*:

```
{
  	"version": "0",
  	"id": "1111111-bbbb-aaaa-cccc-dddddEXAMPLE", # Random uuid
  	"detail-type": "ARC Region Switch Plan Execution",
  	"source": "aws.arc-region-switch",
  	"account": "111122223333",
  	"time": "2023-11-16T23:38:14Z",
  	"region": "us-east-1",
  	"resources": ["arn:aws:arc-region-switch::111122223333:plan/aaaaaExample"], # planArn
  	"detail": {
  		"version": "0.0.1",
  		"eventType": "StepStarted",
  		"executionId": "bbbbbbEXAMPLE",
  		"executionAction": "activating/deactivating {region}",
  		"idempotencyKey": "1111111-2222-3333-4444-5555555555", # As there is a possibility of dual logging
  		"stepDetails" : { 
  			"stepName": "Routing control step",
  			"resource": ["arn:aws:route53-recovery-control::111122223333:controlpanel/abcdefghiEXAMPLE/routingcontrol/jklmnopqrsEXAMPLE"]   
  		}
  	}
}
```

The following is an example ARC event for a *Region switch plan evaluation warning*.

For a Region switch plan evaluation, an event is emitted when a warning is returned. If the warning is not cleared, an event is emitted for the warning only once every 24 hours. When the event is cleared, no further events are emitted for that warning.

```
{
  	"version": "0",
  	"id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4", # Random uuid
  	"detail-type": "ARC Region Switch Plan Execution",
  	"source": "aws.arc-region-switch",
  	"account": "111122223333",
  	"time": "2023-11-16T23:38:14Z",
  	"region": "us-east-1",
  	"resources": ["arn:aws:arc-region-switch::111122223333:plan/a2b89be4821bfd1d"],
  	"detail": {
    	"version": "0.0.1",
    	"idempotencyKey": "1111111-2222-3333-4444-5555555555",
    	"metadata": {
        "evaluationTime" : "timestamp",
        "warning" : "There is a plan evaluation warning for arn:aws:arc-region-switch::111122223333:plan/a2b89be4821bfd1d. Navigate to the Region switch console to resolve."
    	}  	
  	}
}
```

##### Specify a CloudWatch log group to use as a target
<a name="arc-eventbridge-cw-loggroup-rs"></a>

When you create an EventBridge rule, you must specify the target where events that are matched to the rule are sent. For a list of available targets for EventBridge, see [Targets available in the EventBridge console](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html#eb-console-targets). One of the targets that you can add to an EventBridge rule is an Amazon CloudWatch log group. This section describes the requirements for adding CloudWatch log groups as targets, and provides a procedure for adding a log group when you create a rule.

To add a CloudWatch log group as a target, you can do one of the following:
+ Create a new log group 
+ Choose an existing log group

If you specify a new log group using the console when you create a rule, EventBridge automatically creates the log group for you. Make sure that the log group that you use as a target for the EventBridge rule starts with `/aws/events`. If you want to choose an existing log group, be aware that only log groups that start with `/aws/events` appear as options in the drop-down menu. For more information, see [Create a new log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group) in the *Amazon CloudWatch User Guide*.

If you create or use a CloudWatch log group to use as a target using CloudWatch operations outside of the console, make sure that you set permissions correctly. If you use the console to add a log group to an EventBridge rule, then the resource-based policy for the log group is updated automatically. But, if you use the AWS Command Line Interface or an AWS SDK to specify a log group, then you must update resource-based policy for the log group. The following example policy illustrates the permissions that you must define in a resource-based policy for the log group:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "events.amazonaws.com",
          "delivery.logs.amazonaws.com"
        ]
      },
      "Resource": "arn:aws:logs:us-east-1:222222222222:log-group:/aws/events/*:*",
      "Sid": "TrustEventsToStoreLogEvent"
    }
  ]
}
```

------

You can't configure a resource-based policy for a log group by using the console. To add the required permissions to a resource-based policy, use the CloudWatch [PutResourcePolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html) API operation. Then, you can use the [ describe-resource-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-resource-policies.html) CLI command to check that your policy was applied correctly.

**To create a rule for a resource event and specify a CloudWatch log group target**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose the AWS Region that you want to create the rule in.

1. Choose **Create rule** and then enter any information about that rule, such as the event pattern or schedule details.

   For more information about creating EventBridge rules for readiness, see [ Monitor a readiness check resource with EventBridge](#RCEventBridgeCreateRule).

1. On the **Select target** page, choose **CloudWatch** as your target.

1. Choose a CloudWatch log group from the drop-down menu.

### Quotas for Region switch
<a name="quotas.region-switch"></a>

Region switch in Amazon Application Recovery Controller (ARC) is subject to the following quotas.


| Entity | Quota | 
| --- | --- | 
| Number of plans per account | 10<br />You can [ request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/arc-region-switch/quotas). | 
| Number of execution blocks per plan | 100 | 
| Number of parallel execution blocks per step | 20 | 
| Number of CloudWatch alarms per trigger condition | 10 | 
| Number of Route 53 health check execution blocks per plan | 25 | 

# Code examples for Application Recovery Controller using AWS SDKs
<a name="service_code_examples"></a>

The following code examples show how to use Application Recovery Controller with an AWS software development kit (SDK). 

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

**Contents**
+ [Basics](#service_code_examples_basics)
  + [Actions](#service_code_examples_actions)
    + [`GetRoutingControlState`](#example_route53-recovery-cluster_GetRoutingControlState_section)
    + [`UpdateRoutingControlState`](#example_route53-recovery-cluster_UpdateRoutingControlState_section)

## Basic examples for Application Recovery Controller using AWS SDKs
<a name="service_code_examples_basics"></a>

The following code examples show how to use the basics of Amazon Route 53 Application Recovery Controller with AWS SDKs. 

**Contents**
+ [Actions](#service_code_examples_actions)
  + [`GetRoutingControlState`](#example_route53-recovery-cluster_GetRoutingControlState_section)
  + [`UpdateRoutingControlState`](#example_route53-recovery-cluster_UpdateRoutingControlState_section)

### Actions for Application Recovery Controller using AWS SDKs
<a name="service_code_examples_actions"></a>

The following code examples demonstrate how to perform individual Application Recovery Controller actions with AWS SDKs. Each example includes a link to GitHub, where you can find instructions for setting up and running the code. 

 The following examples include only the most commonly used actions. For a complete list, see the [Amazon Route 53 Application Recovery Controller API Reference](https://docs.aws.amazon.com/routing-control/latest/APIReference/Welcome.html). 

**Topics**
+ [`GetRoutingControlState`](#example_route53-recovery-cluster_GetRoutingControlState_section)
+ [`UpdateRoutingControlState`](#example_route53-recovery-cluster_UpdateRoutingControlState_section)

#### Use `GetRoutingControlState` with an AWS SDK
<a name="example_route53-recovery-cluster_GetRoutingControlState_section"></a>

The following code examples show how to use `GetRoutingControlState`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53recoverycluster#code-examples). 

```
    public static GetRoutingControlStateResponse getRoutingControlState(List<ClusterEndpoint> clusterEndpoints,
            String routingControlArn) {
        // As a best practice, we recommend choosing a random cluster endpoint to get or
        // set routing control states.
        // For more information, see
        // https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html#route53-arc-best-practices.regional
        Collections.shuffle(clusterEndpoints);
        for (ClusterEndpoint clusterEndpoint : clusterEndpoints) {
            try {
                System.out.println(clusterEndpoint);
                Route53RecoveryClusterClient client = Route53RecoveryClusterClient.builder()
                        .endpointOverride(URI.create(clusterEndpoint.endpoint()))
                        .region(Region.of(clusterEndpoint.region())).build();
                return client.getRoutingControlState(
                        GetRoutingControlStateRequest.builder()
                                .routingControlArn(routingControlArn).build());
            } catch (Exception exception) {
                System.out.println(exception);
            }
        }
        return null;
    }
```
+  For API details, see [GetRoutingControlState](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-recovery-cluster-2019-12-02/GetRoutingControlState) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/route53-recovery-cluster#code-examples). 

```
import boto3


def create_recovery_client(cluster_endpoint):
    """
    Creates a Boto3 Route 53 Application Recovery Controller client for the specified
    cluster endpoint URL and AWS Region.

    :param cluster_endpoint: The cluster endpoint URL and Region.
    :return: The Boto3 client.
    """
    return boto3.client(
        "route53-recovery-cluster",
        endpoint_url=cluster_endpoint["Endpoint"],
        region_name=cluster_endpoint["Region"],
    )



def get_routing_control_state(routing_control_arn, cluster_endpoints):
    """
    Gets the state of a routing control. Cluster endpoints are tried in
    sequence until the first successful response is received.

    :param routing_control_arn: The ARN of the routing control to look up.
    :param cluster_endpoints: The list of cluster endpoints to query.
    :return: The routing control state response.
    """

    # As a best practice, we recommend choosing a random cluster endpoint to get or set routing control states.
    # For more information, see https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html#route53-arc-best-practices.regional
    random.shuffle(cluster_endpoints)
    for cluster_endpoint in cluster_endpoints:
        try:
            recovery_client = create_recovery_client(cluster_endpoint)
            response = recovery_client.get_routing_control_state(
                RoutingControlArn=routing_control_arn
            )
            return response
        except Exception as error:
            print(error)
            raise error
```
+  For API details, see [GetRoutingControlState](https://docs.aws.amazon.com/goto/boto3/route53-recovery-cluster-2019-12-02/GetRoutingControlState) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/r5v#code-examples). 

```
    CONSTANTS cv_pfl TYPE /aws1/rt_profile_id VALUE 'ZCODE_DEMO'.
    DATA lo_exception TYPE REF TO /aws1/cx_rt_generic.
    DATA lo_session TYPE REF TO /aws1/cl_rt_session_base.
    DATA lo_client TYPE REF TO /aws1/if_r5v.
    DATA lt_endpoints TYPE TABLE OF string.
    DATA lv_endpoint TYPE string.
    DATA lv_region TYPE /aws1/rt_region_id.

    " Parse the comma-separated cluster endpoints
    " Expected format: "https://endpoint1.com|us-west-2,https://endpoint2.com|us-east-1"
    SPLIT iv_cluster_endpoints AT ',' INTO TABLE lt_endpoints.

    " As a best practice, shuffle cluster endpoints to distribute load
    " For more information, see https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html#route53-arc-best-practices.regional
    " For simplicity, we'll try them in order (shuffling can be added if needed)

    " Try each endpoint in order
    LOOP AT lt_endpoints INTO lv_endpoint.
      TRY.
          " Parse endpoint and region from the format "url|region"
          DATA(lv_pos) = find( val = lv_endpoint sub = '|' ).
          IF lv_pos > 0.
            DATA(lv_url) = substring( val = lv_endpoint len = lv_pos ).
            lv_region = substring( val = lv_endpoint off = lv_pos + 1 ).
          ELSE.
            " If no region specified, use default
            lv_url = lv_endpoint.
            lv_region = 'us-east-1'.
          ENDIF.

          " Create session for this region
          lo_session = /aws1/cl_rt_session_aws=>create( cv_pfl ).

          " Create client with the specific endpoint
          lo_client = create_recovery_client(
            iv_endpoint = lv_url
            iv_region   = lv_region
            io_session  = lo_session ).

          " Try to get the routing control state
          oo_result = lo_client->getroutingcontrolstate(
            iv_routingcontrolarn = iv_routing_control_arn ).

          " If successful, return the result
          RETURN.

        CATCH /aws1/cx_r5vendpttmpyunavailex INTO DATA(lo_endpoint_ex).
          " This endpoint is temporarily unavailable, try the next one
          lo_exception = lo_endpoint_ex.
          CONTINUE.

        CATCH /aws1/cx_r5vaccessdeniedex
              /aws1/cx_r5vinternalserverex
              /aws1/cx_r5vresourcenotfoundex
              /aws1/cx_r5vthrottlingex
              /aws1/cx_r5vvalidationex
              /aws1/cx_rt_generic INTO lo_exception.
          " For other errors, re-raise immediately
          RAISE EXCEPTION lo_exception.
      ENDTRY.
    ENDLOOP.

    " If we get here, all endpoints failed - re-raise the last exception
    IF lo_exception IS BOUND.
      RAISE EXCEPTION lo_exception.
    ENDIF.
```
+  For API details, see [GetRoutingControlState](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `UpdateRoutingControlState` with an AWS SDK
<a name="example_route53-recovery-cluster_UpdateRoutingControlState_section"></a>

The following code examples show how to use `UpdateRoutingControlState`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53recoverycluster#code-examples). 

```
    public static UpdateRoutingControlStateResponse updateRoutingControlState(List<ClusterEndpoint> clusterEndpoints,
            String routingControlArn,
            String routingControlState) {
        // As a best practice, we recommend choosing a random cluster endpoint to get or
        // set routing control states.
        // For more information, see
        // https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html#route53-arc-best-practices.regional
        Collections.shuffle(clusterEndpoints);
        for (ClusterEndpoint clusterEndpoint : clusterEndpoints) {
            try {
                System.out.println(clusterEndpoint);
                Route53RecoveryClusterClient client = Route53RecoveryClusterClient.builder()
                        .endpointOverride(URI.create(clusterEndpoint.endpoint()))
                        .region(Region.of(clusterEndpoint.region()))
                        .build();
                return client.updateRoutingControlState(
                        UpdateRoutingControlStateRequest.builder()
                                .routingControlArn(routingControlArn).routingControlState(routingControlState).build());
            } catch (Exception exception) {
                System.out.println(exception);
            }
        }
        return null;
    }
```
+  For API details, see [UpdateRoutingControlState](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-recovery-cluster-2019-12-02/UpdateRoutingControlState) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/route53-recovery-cluster#code-examples). 

```
import boto3


def create_recovery_client(cluster_endpoint):
    """
    Creates a Boto3 Route 53 Application Recovery Controller client for the specified
    cluster endpoint URL and AWS Region.

    :param cluster_endpoint: The cluster endpoint URL and Region.
    :return: The Boto3 client.
    """
    return boto3.client(
        "route53-recovery-cluster",
        endpoint_url=cluster_endpoint["Endpoint"],
        region_name=cluster_endpoint["Region"],
    )



def update_routing_control_state(
    routing_control_arn, cluster_endpoints, routing_control_state
):
    """
    Updates the state of a routing control. Cluster endpoints are tried in
    sequence until the first successful response is received.

    :param routing_control_arn: The ARN of the routing control to update the state for.
    :param cluster_endpoints: The list of cluster endpoints to try.
    :param routing_control_state: The new routing control state.
    :return: The routing control update response.
    """

    # As a best practice, we recommend choosing a random cluster endpoint to get or set routing control states.
    # For more information, see https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html#route53-arc-best-practices.regional
    random.shuffle(cluster_endpoints)
    for cluster_endpoint in cluster_endpoints:
        try:
            recovery_client = create_recovery_client(cluster_endpoint)
            response = recovery_client.update_routing_control_state(
                RoutingControlArn=routing_control_arn,
                RoutingControlState=routing_control_state,
            )
            return response
        except Exception as error:
            print(error)
```
+  For API details, see [UpdateRoutingControlState](https://docs.aws.amazon.com/goto/boto3/route53-recovery-cluster-2019-12-02/UpdateRoutingControlState) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/r5v#code-examples). 

```
    CONSTANTS cv_pfl TYPE /aws1/rt_profile_id VALUE 'ZCODE_DEMO'.
    DATA lo_exception TYPE REF TO /aws1/cx_rt_generic.
    DATA lo_session TYPE REF TO /aws1/cl_rt_session_base.
    DATA lo_client TYPE REF TO /aws1/if_r5v.
    DATA lt_endpoints TYPE TABLE OF string.
    DATA lv_endpoint TYPE string.
    DATA lv_region TYPE /aws1/rt_region_id.

    " Parse the comma-separated cluster endpoints
    " Expected format: "https://endpoint1.com|us-west-2,https://endpoint2.com|us-east-1"
    SPLIT iv_cluster_endpoints AT ',' INTO TABLE lt_endpoints.

    " As a best practice, shuffle cluster endpoints to distribute load
    " For more information, see https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html#route53-arc-best-practices.regional
    " For simplicity, we'll try them in order (shuffling can be added if needed)

    " Try each endpoint in order
    LOOP AT lt_endpoints INTO lv_endpoint.
      TRY.
          " Parse endpoint and region from the format "url|region"
          DATA(lv_pos) = find( val = lv_endpoint sub = '|' ).
          IF lv_pos > 0.
            DATA(lv_url) = substring( val = lv_endpoint len = lv_pos ).
            lv_region = substring( val = lv_endpoint off = lv_pos + 1 ).
          ELSE.
            " If no region specified, use default
            lv_url = lv_endpoint.
            lv_region = 'us-east-1'.
          ENDIF.

          " Create session for this region
          lo_session = /aws1/cl_rt_session_aws=>create( cv_pfl ).

          " Create client with the specific endpoint
          lo_client = create_recovery_client(
            iv_endpoint = lv_url
            iv_region   = lv_region
            io_session  = lo_session ).

          " Try to update the routing control state
          oo_result = lo_client->updateroutingcontrolstate(
            iv_routingcontrolarn     = iv_routing_control_arn
            iv_routingcontrolstate   = iv_routing_control_state
            it_safetyrulestooverride = it_safety_rules_override ).

          " If successful, return the result
          RETURN.

        CATCH /aws1/cx_r5vendpttmpyunavailex INTO DATA(lo_endpoint_ex).
          " This endpoint is temporarily unavailable, try the next one
          lo_exception = lo_endpoint_ex.
          CONTINUE.

        CATCH /aws1/cx_r5vaccessdeniedex
              /aws1/cx_r5vconflictexception
              /aws1/cx_r5vinternalserverex
              /aws1/cx_r5vresourcenotfoundex
              /aws1/cx_r5vthrottlingex
              /aws1/cx_r5vvalidationex
              /aws1/cx_rt_generic INTO lo_exception.
          " For other errors, re-raise immediately
          RAISE EXCEPTION lo_exception.
      ENDTRY.
    ENDLOOP.

    " If we get here, all endpoints failed - re-raise the last exception
    IF lo_exception IS BOUND.
      RAISE EXCEPTION lo_exception.
    ENDIF.
```
+  For API details, see [UpdateRoutingControlState](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

# Security in Amazon Application Recovery Controller
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Application Recovery Controller, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using ARC. The following topics show you how to configure ARC to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your ARC resources. 

**Topics**
+ [Data protection in Amazon Application Recovery Controller](#data-protection)
+ [Identity and Access Management for Amazon Application Recovery Controller (ARC)](#security-iam)
+ [Logging and monitoring in ARC](#logging-and-monitoring)
+ [Compliance validation for Amazon Application Recovery Controller](#r53-recovery-controller-compliance)
+ [Resilience in Amazon Application Recovery Controller](#disaster-recovery-resiliency)
+ [Infrastructure security in Amazon Application Recovery Controller](#infrastructure-security)

## Data protection in Amazon Application Recovery Controller
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Application Recovery Controller. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with ARC or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.



### Encryption at rest
<a name="encryption-rest"></a>

Customer configuration information stored by Amazon Application Recovery Controller is encrypted at rest.

### Encryption in transit
<a name="encryption-transit"></a>

Customer requests and responses for Amazon Application Recovery Controller are encrypted during transport throughout the service by using TLS.

## Identity and Access Management for Amazon Application Recovery Controller (ARC)
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use ARC resources. IAM is an AWS service that you can use with no additional charge.

### Audience
<a name="security_iam_audience"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting Amazon Application Recovery Controller (ARC) identity and access](#security_iam_troubleshoot))
+ **Service administrator** - determine user access and submit permission requests (see [How Amazon Application Recovery Controller (ARC) capabilities work with IAM](#security_iam_service-with-iam))
+ **IAM administrator** - write policies to manage access (see [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](#security_iam_id-based-policy-examples))

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

### How Amazon Application Recovery Controller (ARC) capabilities work with IAM
<a name="security_iam_service-with-iam"></a>

For information about how each Amazon Application Recovery Controller (ARC) capability works with IAM, see the following topics:
+ [IAM for zonal shift](#security-iam-zonalshift)
+ [IAM for zonal autoshift](#security-iam-zonalautoshift)
+ [IAM for routing control](#security-iam-routing)
+ [IAM for readiness check](#security-iam-readiness)
+ [IAM for Region switch](#security-iam-region-switch)

### Identity-based policy examples in Amazon Application Recovery Controller (ARC)
<a name="security_iam_id-based-policy-examples"></a>

To see identity-based policy examples for each capability in Amazon Application Recovery Controller (ARC), see the following topics in the AWS Identity and Access Management chapters for each capability:
+ [Identity-based policy examples for zonal autoshift in ARC](#security-iam-zonalshift)
+ [Identity-based policy examples for zonal shift in ARC](#security-iam-zonalautoshift)
+ [Identity-based policy examples for routing control in ARC](#security-iam-routing)
+ [Identity-based policy examples for readiness check in ARC](#security-iam-readiness)

### AWS managed policies for Amazon Application Recovery Controller (ARC)
<a name="security-iam-awsmanpol"></a>

For information about the AWS managed policies for the ARC capabilities with managed policies, including a managed policy for a service-linked role, see the following topics:
+ [Managed polices for zonal autoshift](#security-iam-awsmanpol-zonal-autoshift)
+ [Managed polices for routing control](#security-iam-awsmanpol-routing)
+ [Managed polices for readiness check](#security-iam-awsmanpol-readiness)

#### Updates to AWS managed policies for Amazon Application Recovery Controller (ARC)
<a name="security-iam-awsmanpol-arc-updates"></a>

View details about updates to AWS managed policies for capabilities in ARC since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the ARC [Document history page](#doc-history).


| Change | Description | Date | 
| --- | --- | --- | 
| [AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy.html) – Updated policy | Amazon Application Recovery Controller (ARC) updated this policy to add permissions for service quota remediation.<br />These permissions allow Region switch to read service quota values, check the status of quota increase requests, and request quota increases so that service quotas stay in sync across the Regions used by a plan. | October 1st, 2026 | 
| [AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy.html) – New policy | Amazon Application Recovery Controller (ARC) released a new managed policy that grants permissions for Region switch plan execution and evaluation.<br />This policy provides read-only access to Region switch plan information, execution status, and Amazon CloudWatch monitoring data. It also includes permission to simulate IAM principal policies for plan evaluation. | November 3rd, 2025 | 
| [AWSZonalAutoshiftPracticeRunSLRPolicy managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSZonalAutoshiftPracticeRunSLRPolicy.html) – Updated policy | Adds the policy statement `AutoshiftPracticeCheckPermissions` with the permissions `autoscaling:DescribeAutoScalingGroups`, `ec2:DescribeInstances`, `elasticloadbalancing:DescribeTargetHealth`, and `elasticloadbalancing:DescribeTargetHealth` to support balanced capacity checks.<br />To learn more, see [How zonal autoshift and practice runs work](#arc-zonal-autoshift.how-it-works). | June 30, 2025 | 
|  [ AWSZonalAutoshiftPracticeRunSLRPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSZonalAutoshiftPracticeRunSLRPolicy.html) – New policy | ARC added a new service-linked role for autoshift and practice runs.<br />ARC uses the permissions enabled by the service-linked role to monitor customer-provided Amazon CloudWatch alarms and customer Health Dashboard events for practice runs, and to start practice runs.<br />To learn more about the new service-linked role, see [Service-linked role permissions for AWSServiceRoleForZonalAutoshiftPracticeRun](#slr-permissions-slr2). | November 30, 2023 | 
| [AmazonRoute53RecoveryControlConfigReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryControlConfigReadOnlyAccess) – Updated policy | Adds permissions for `GetResourcePolicy`, to support returning details about AWS Resource Access Manager resource policies for shared resources. | October 18, 2023 | 
|  [Route53RecoveryReadinessServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Route53RecoveryReadinessServiceRolePolicy.html) – Updated policy | ARC added new permissions to query information about Amazon EC2 instances.<br />ARC uses the following permissions to support polling Amazon EC2 instances, to run readiness checks and determine the readiness status for the instances.<br />`ec2:DescribeVpnGateways`<br />`ec2:DescribeCustomerGateways` | February 17, 2023 | 
|  [Route53RecoveryReadinessServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Route53RecoveryReadinessServiceRolePolicy.html) – Updated policy | ARC added a new permission to query information about Lambda functions.<br />ARC uses the following permission to query information about Lambda functions to run readiness checks and determine the readiness status for the functions.<br />`lambda:ListProvisionedConcurrencyConfigs` | August 31, 2022 | 
| [AmazonRoute53RecoveryControlConfigFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigFullAccess.html) – Updated policy | Removed Amazon Route 53 permissions from the policy and added note listing the optional permissions. | May 26, 2022 | 
| [AmazonRoute53RecoveryControlConfigFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigFullAccess.html) – Updated policy | Added missing required Amazon Route 53 permissions to the policy. | April 15, 2022 | 
| [AmazonRoute53RecoveryClusterReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterReadOnlyAccess.html) – Updated policy | ARC added a new permission, `route53-recovery-cluster:ListRoutingControls`, to allow listing routing control ARNs with high availability. | March 15, 2022 | 
| [AmazonRoute53RecoveryControlConfigReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigReadOnlyAccess.html) – Updated policy | ARC added a new permission, `route53-recovery-control-config:ListTagsForResources`, to allow listing tags for a resource. | December 20, 2021 | 
|  [Route53RecoveryReadinessServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Route53RecoveryReadinessServiceRolePolicy.html) – Updated policy | ARC added a new permission to query information about Amazon API Gateway.<br />ARC uses the permission, `apigateway:GET`, to query information about API Gateway to run readiness checks and determine the readiness status. | October 28, 2021 | 
| [AmazonRoute53RecoveryReadinessReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryReadinessReadOnlyAccess.html) – Added new permissions | ARC added two new permissions to [ AmazonRoute53RecoveryReadinessReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryReadinessReadOnlyAccess):<br />ARC uses `route53-recovery-readiness:GetArchitectureRecommendations` and `route53-recovery-readiness:GetCellReadinessSummary` to allow read-only access to these actions for working with recovery readiness. | October 15, 2021 | 
|  [Route53RecoveryReadinessServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Route53RecoveryReadinessServiceRolePolicy.html) – Updated policy | ARC added new permissions to query information about Lambda functions.<br />ARC uses the following permissions to query information about Lambda functions to run readiness checks and determine the readiness status for those functions.<br />`lambda:GetFunctionConcurrency`<br />`lambda:GetFunctionConfiguration`<br />`lambda:GetProvisionedConcurrencyConfig`<br />`lambda:ListAliases`<br />`lambda:ListVersionsByFunction`<br />`lambda:ListEventSourceMappings`<br />`lambda:ListFunctions` | October 8, 2021 | 
|  [Route53RecoveryReadinessServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Route53RecoveryReadinessServiceRolePolicy.html) – Added new managed policies | ARC added the following new managed policies:<br />[AmazonRoute53RecoveryReadinessFullAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryReadinessFullAccess)<br />[AmazonRoute53RecoveryReadinessReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryReadinessReadOnlyAccess)<br />[AmazonRoute53RecoveryClusterFullAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryClusterFullAccess)<br />[AmazonRoute53RecoveryClusterReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryClusterReadOnlyAccess)<br />[AmazonRoute53RecoveryControlConfigFullAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryControlConfigFullAccess)<br />[AmazonRoute53RecoveryControlConfigReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53RecoveryControlConfigReadOnlyAccess) | August 18, 2021 | 
| ARC started tracking changes | ARC started tracking changes for its AWS managed policies. | July 27, 2021 | 

### Troubleshooting Amazon Application Recovery Controller (ARC) identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Application Recovery Controller (ARC) and IAM.

**Topics**
+ [I am not authorized to perform an action in ARC](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I want to allow people outside of my AWS account to access my ARC resources](#security_iam_troubleshoot-cross-account-access)

#### I am not authorized to perform an action in ARC
<a name="security_iam_troubleshoot-no-permissions"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your credentials.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but does not have the fictional `route53-recovery-readiness:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: route53-recovery-readiness:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `{{my-example-widget}}` resource using the `route53-recovery-readiness:{{GetWidget}}` action.

#### I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to ARC.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in ARC. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I want to allow people outside of my AWS account to access my ARC resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether ARC supports these features, see [How Amazon Application Recovery Controller (ARC) capabilities work with IAM](#security_iam_service-with-iam).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

### Access Amazon Application Recovery Controller (ARC) zonal shift using an interface endpoint (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and Amazon Application Recovery Controller (ARC) zonal shift. You can access ARC zonal shift as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access ARC zonal shift.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for ARC zonal shift.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

#### Considerations for ARC zonal shift
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for ARC zonal shift, review [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

ARC zonal shift supports making calls to all of its API actions through the interface endpoint.

#### Create an interface endpoint for ARC zonal shift
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for ARC zonal shift using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface endpoint for ARC zonal shift using the following service name:

```
com.amazonaws.{{region}}.arc-zonal-shift
```

If you enable private DNS for the interface endpoint, you can make API requests to ARC zonal shift using its default Regional DNS name. For example, `arc-zonal-shift.us-east-1.amazonaws.com`.

#### Create an endpoint policy for your interface endpoint
<a name="vpc-endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy allows full access to ARC zonal shift through the interface endpoint. To control the access allowed to ARC zonal shift from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
+ The actions that can be performed.
+ The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for ARC zonal shift actions**  
The following is an example of a custom endpoint policy. When you attach this policy to your interface endpoint, it grants access to the listed ARC zonal shift actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "arc-zonal-shift:ListManagedResources",
            "arc-zonal-shift:StartZonalShift",
            "arc-zonal-shift:CancelZonalShift"
         ],
         "Resource":"*"
      }
   ]
}
```

The `Resource` can also be listed as `arn:aws:elasticloadbalancing:us-east-{{1:111122223333}}:loadbalancer/app/Testing/{{1111111ecd42dc05}}`.

## Logging and monitoring in ARC
<a name="logging-and-monitoring"></a>

Monitoring is an important part of maintaining the availability and performance of ARC and your AWS solutions. You should collect monitoring data from all of the parts of your AWS solution so that you can more easily debug a multi-point failure if one occurs. AWS provides several tools for monitoring your ARC resources and activity, and responding to potential incidents, for example, AWS CloudTrail and Amazon CloudWatch.

For information about monitoring for each capability in ARC, see the following topics:
+ [Logging and monitoring for zonal shift](#monitoring-zonal-shift)
+ [Logging and monitoring for zonal autoshift](#monitoring-zonal-autoshift)
+ [Logging and monitoring for routing control](#monitoring-routing)
+ [Logging and monitoring for Region switch](#logging-and-monitoring-rs)
+ [Logging and monitoring for readiness check](#monitoring-readiness)

## Compliance validation for Amazon Application Recovery Controller
<a name="r53-recovery-controller-compliance"></a>

Third-party auditors assess the security and compliance of Amazon Application Recovery Controller as part of multiple AWS compliance programs. These include SOC, PCI, HIPAA, and others.

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Resilience in Amazon Application Recovery Controller
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, ARC offers several features to help support your data resiliency and backup needs.

## Infrastructure security in Amazon Application Recovery Controller
<a name="infrastructure-security"></a>

As a managed service, is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access ARC through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

# Document history for the Amazon Application Recovery Controller (ARC) Developer Guide
<a name="doc-history"></a>

The following entries describe important changes made to the Amazon Application Recovery Controller (ARC) documentation.
+ **Version:** latest
+ **Latest documentation update: **September 24th, 2026



| Change | Description | Date | 
| --- | --- | --- | 
| Zonal shift support for additional Network Load Balancer target group configurations | You can now use zonal shift with cross-zone enabled Network Load Balancers that have target groups with connection termination for unhealthy targets enabled, UDP target groups, or Application Load Balancers as targets.<br />For more information, see [Network Load Balancers](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html). | September 24, 2026 | 
| Readiness check availability change | The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal.<br />For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html). | April 30, 2026 | 
| Readiness check availability change | The readiness check feature in Amazon Application Recovery Controller (ARC) will no longer be open to new customers starting April 30, 2026. Existing customers can continue to use the service as normal.<br />For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html). | March 31, 2026 | 
| New managed policy for Region switch plan execution | Amazon Application Recovery Controller (ARC) released a new managed policy, `AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy`, that grants permissions for Region switch plan execution and evaluation.<br />For more information, see [Amazon Application Recovery Controller (ARC) updates to AWS managed policies](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol.html#security-iam-awsmanpol-updates). | November 3rd, 2025 | 
| You can now use AWS PrivateLink between your VPC and Amazon Application Recovery Controller (ARC) zonal shift. | You can use an AWS PrivateLink to create a private connection between your VPC and Amazon Application Recovery Controller (ARC) zonal shift.<br />For more information, see [Access Amazon Application Recovery Controller (ARC) zonal shift using an interface endpoint (AWS PrivateLink)](https://docs.aws.amazon.com/r53recovery/latest/dg/vpc-interface-endpoints.html). | August 11, 2025 | 
| New Region switch service | Region switch enables customers to orchestrate the specific steps, supporting cross-account, that are needed to operate their multi-Region application out of another AWS Region.<br />For more information, see [Region switch in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html). | August 1, 2025 | 
| Enhancements to practice runs | You can now start on-demand practice runs in ARC. In addition, practice runs now include checks for sufficient capacity in other AZs in the Region.<br />For more information, see [How it works](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html). | June 30, 2025 | 
| Updates a managed policy | Updates the `AWSZonalAutoshiftPracticeRunSLRPolicy` managed policy by adding the policy statement `AutoshiftPracticeCheckPermissions` with the permissions `autoscaling:DescribeAutoScalingGroups`, `ec2:DescribeInstances`, `elasticloadbalancing:DescribeTargetHealth`, and `elasticloadbalancing:DescribeTargetHealth` to support balanced capacity checks.<br />For more information, see [AWSZonalAutoshiftPracticeRunSLRPolicy managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSZonalAutoshiftPracticeRunSLRPolicy.html). | June 30, 2025 | 
| Updates to exception types for zonal autoshift | You can now interact with zonal autoshift on a per-resource basis.<br />For more information, see [How it works](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html). | April 21, 2025 | 
| Test ARC zonal autoshift with AWS FIS | You can use AWS FIS to test how ARC zonal autoshift automatically recovers your application during an AZ power interruption<br />For more information, see [Testing zonal autoshift with AWS FIS](https://docs.aws.amazon.com/r53recovery/latest/dg/testing-zonal-autoshift-fis.html). | March 26, 2025 | 
| ARC now supports IPv6 endpoints for routing controls and zonal shift. | ARC now supports IPv6 endpoints for routing controls and zonal shift.<br />For more information, see [Set up routing control components](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-routing-config.html). | November 21, 2024 | 
| Zonal shift capability for Amazon EC2 Auto Scaling groups | ARC now supports zonal shift for Amazon EC2 Auto Scaling groups.<br />For more information, see [Support for Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html). | November 18, 2024 | 
| Zonal shift capability for Amazon EKS | You can start a zonal shift for an Amazon EKS cluster, or you can allow AWS to do it for you by enabling zonal autoshift. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs.<br />For more information, see [Support for Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ekd.html). | October 22, 2024 | 
| Zonal shift capability for Network Load Balancers | ARC now supports zonal shift for Network Load Balancers with cross-zone enabled or cross-zone disabled configurations.<br />For more information, see [Support for Network Load Balancers](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html). | October 11, 2024 | 
| Autoshift observer notifications | With autoshift observer notifications, you can configure zonal autoshift to notify you, through Amazon EventBridge, whenever AWS starts an autoshift to shift traffic away from a potentially impaired Availability Zone. You do not have to configure any specific resources with zonal autoshift to enable these separate notifications.<br />For more information, see [Using zonal autoshift with Amazon EventBridge](https://docs.aws.amazon.com/r53recovery/latest/dg/eventbridge-zonal-autoshift.html). | July 12, 2024 | 
| Doc reorganization by each capability | Reorganizes the developer guide content to be siloed into sub-dev guides. That is, there are now separate sections that contain comprehensive information for each capability in ARC: zonal shift and zonal autoshift for multi-AZ recovery, and routing control and readiness check for multi-Region recovery.<br />For more information, see [What is Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html). | April 30, 2024 | 
| Adds zonal autoshift capability | Adds a new capability in ARC where you authorize AWS to shift away resource traffic for an application from an Availability Zone, on your behalf, to help reduce time to recovery during events.<br />For more information, see [Zonal autoshift in Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.html). | November 30, 2023 | 
| Adds new service-linked role | Adds a new service-linked role, **AWSServiceRoleForZonalAutoshiftPracticeRun**, for zonal autoshift practice runs.<br />For more information, see [Service-linked role permissions for AWSServiceRoleForZonalAutoshiftPracticeRun](https://docs.aws.amazon.com/r53recovery/latest/dg/slr-permissions-slr2.html). | November 30, 2023 | 
| Adds cross-account support for clusters | Adds cross-account support for clusters in ARC with AWS Resource Access Manager, so that you can easily and securely use one cluster to host control panels and routing controls owned by several different AWS accounts.<br />For more information, see [Support cross-account for clusters in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.failover-different-accounts). | October 18, 2023 | 
| Updates a managed policy | Updates the `AmazonRoute53RecoveryControlConfigReadOnly` managed policy to add permissions for `GetResourcePolicy`, to support returning details about AWS Resource Access Manager resource policies for shared resources.<br />For more information, see [AWS managed policies](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-route53-recovery.html). | September 19, 2023 | 
| Updated service-linked role | Added new permissions, `ec2:DescribeVpnGateways` and `ec2:DescribeCustomerGateways`, to the service-linked role for ARC, to support polling Amazon EC2 instances.<br />For more information, see [Using service-linked roles for ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/using-service-linked-roles.html). | February 17, 2023 | 
| GA release for zonal shift | Supports the GA release of zonal shift for ARC, which includes attribute-based access control (ABAC) for managed resources that are registered in ARC for zonal shift.<br />For more information, see [Attribute-based access control (ABAC) with ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam.html#security_iam_service-with-iam-tags). | January 10, 2023 | 
| Added new multi-AZ zonal shift | Added content describing a new service in ARC, zonal shift, for multi-AZ applications. You can start a zonal shift to temporarily move traffic for a load balancer resource away from an Availability Zone.<br />For more information, see [Zonal shift in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.how-it-works.html). | November 28, 2022 | 
| Updated service-linked role | Added a new permission, `lambda:ListProvisionedConcurrencyConfigs`, to the service-linked role for ARC to query information about Lambda functions.<br />For more information, see [Using service-linked roles for ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/using-service-linked-roles.html). | August 31, 2022 | 
| Updated managed policy | Updated the `AmazonRoute53RecoveryControlConfigFullAccess` managed policy to remove Amazon Route 53 permissions and list them as optional.<br />For more information, see [AWS managed policies for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-route53-recovery.html). | May 26, 2022 | 
| Updated managed policy | Updated the `AmazonRoute53RecoveryControlConfigFullAccess` managed policy to include required Amazon Route 53 permissions.<br />For more information, see [AWS managed policies for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-route53-recovery.html). | April 15, 2022 | 
| Added CLI example for the new list routing controls API | Added example CLI command and best practices recommendations for the new list routing controls API operation included in the extremely reliable ARC data plane API.<br />For more information, see [List and update routing controls and states](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-routing.control-state.html). | March 31, 2022 | 
| Added support for overriding safety rules | Added support for overriding safety rules, which allows you to bypass routing control safeguards that are enforced with safety rules that you've configured. Safety rule overrides could be required, for example, in a "break glass" scenario during failover for disaster recovery.<br />For more information, see [Override safety rules to reroute traffic](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html). | March 2, 2022 | 
| Added additional tagging support | Added support for tagging additional resources in ARC, including clusters, control panels, routing controls, and safety rules.<br />For more information, see [Tagging in Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-tagging.html). | December 20, 2021 | 
| Updated managed policy | Updated the `AmazonRoute53RecoveryControlConfigReadOnly` managed policy to add permission to list tags for a resource.<br />For more information, see [AWS managed policies for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-route53-recovery.html) | December 20, 2021 | 
| Added support for real-time alerts with EventBridge | Added support for EventBridge, which means that now you can add rules to get alerts and act on ARC readiness check status changes, for example, when a status changes from **READY** to **NOT READY**.<br />For more information, see [Using ARC with Amazon EventBridge](https://docs.aws.amazon.com/r53recovery/latest/dg/eventbridge.html). | December 20, 2021 | 
| Added routing control state code samples | Added code samples to illustrate trying cluster endpoints in sequence when you use API operations to get or update routing control states.<br />For more information, see [API examples for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_api.html). | November 16, 2021 | 
| Added new permissions to a read-only policy | Added two new permissions to the policy `AmazonRoute53RecoveryReadinessReadOnlyAccess`: `route53-recovery-readiness:GetArchitectureRecommendations` and `route53-recovery-readiness:GetCellReadinessSummary`.<br />For more information, see [AWS managed policies for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-route53-recovery.html). | November 9, 2021 | 
| Added support for Amazon API Gateway resource type | Added a new resource type, Amazon API Gateway, and updated the ARC service-linked role permissions so that ARC can audit API Gateway with readiness checks.<br />For more information, see [ Readiness rules and supported resource types](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.rules-resources.html) and [ Using service-linked roles for ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/using-service-linked-roles.html). | October 28, 2021 | 
| Added support for Lambda functions resource type | Added a new resource type, Lambda functions, and updated the ARC service-linked role permissions so that ARC can audit Lambda functions with readiness checks.<br />For more information, see [ Readiness rules and supported resource types](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.rules-resources.html) and [ Using service-linked roles for ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/using-service-linked-roles.html). | October 8, 2021 | 
| Added links to CloudFormation and Terraform templates | Added links to downloadable CloudFormation and Hashicorp Terraform templates to help you quickly get started with using ARC.For more information, see [Recovery readiness with a new application](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-setup-new.html).  | September 13, 2021 | 
| Added new managed policies | Added the following AWS managed policies for ARC: `AmazonRoute53RecoveryReadinessFullAccess`, `AmazonRoute53RecoveryReadinessReadOnlyAccess`, `AmazonRoute53RecoveryClusterFullAccess`, `AmazonRoute53RecoveryClusterReadOnlyAccess`, `AmazonRoute53RecoveryControlConfigFullAccess`, and `AmazonRoute53RecoveryControlConfigReadOnlyAccess`.<br />For more information, see [AWS managed policies for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-route53-recovery.html). | August 18, 2021 | 
| Started tracking AWS managed policies for Amazon Application Recovery Controller (ARC) | Updates for managed policies will be tracked from the initial release date forward.<br />For more information, see [AWS managed policies for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-route53-recovery.html). | July 27, 2021 | 
| Initial release of Amazon Application Recovery Controller (ARC) | ARC improves application availability by centrally coordinating failovers within an AWS Region or across multiple Regions. ARC provides readiness checks to ensure that your applications are scaled to handle failover traffic and configured to route around failures. It also provides extremely reliable routing control so that you can recover applications by rerouting traffic, for example, across Availability Zones or Regions. For more information, see [ What is ARC?](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route-53-recovery.html). | July 27, 2021 | 