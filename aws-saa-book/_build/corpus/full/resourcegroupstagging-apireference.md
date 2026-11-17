# Resource Groups Tagging API Tagging API Reference

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
+ [Welcome](#Welcome)
+ [Actions](#API_Operations)
   + [DescribeReportCreation](#API_DescribeReportCreation)
   + [GetComplianceSummary](#API_GetComplianceSummary)
   + [GetResources](#API_GetResources)
   + [GetTagKeys](#API_GetTagKeys)
   + [GetTagValues](#API_GetTagValues)
   + [ListRequiredTags](#API_ListRequiredTags)
   + [StartReportCreation](#API_StartReportCreation)
   + [TagResources](#API_TagResources)
   + [UntagResources](#API_UntagResources)
+ [Data Types](#API_Types)
   + [ComplianceDetails](#API_ComplianceDetails)
   + [FailureInfo](#API_FailureInfo)
   + [RequiredTag](#API_RequiredTag)
   + [ResourceTagMapping](#API_ResourceTagMapping)
   + [Summary](#API_Summary)
   + [Tag](#API_Tag)
   + [TagFilter](#API_TagFilter)
+ [Common Parameters](#CommonParameters)
+ [Common Error Types](#CommonErrors)

-----



# Welcome
<a name="Welcome"></a>

The AWS services in the following list support the Resource Groups Tagging API `TagResources` and `UntagResources` operations.

The `GetResources`, `GetTagKeys`, and `GetTagValues` operations support all resource types.

**Note**  
This list includes only those AWS services that work with the Resource Groups Tagging API.  
If an AWS service isn't listed below, you might still be able to tag that service's resources by using the service's native tagging operations instead of using the Resource Groups Tagging API operations. See the documentation for an individual service for information about that service's native tagging operations.  
This lets you tag resources by using the AWS CLI version of the service's operation. For example, you could tag an IAM role by using a command similar to the following:   
 `aws iam tag-role --role-name ProdAppRole --tags Key=CostCenter,Value=1234`   
For a list of the AWS services that work with Tag Editor, see [Supported Resources](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the * AWS Resource Groups User Guide*.  
IAM users and roles can only be used in `TagResources` and `UntagResources` operations. The `GetResources` operation does not currently support IAM users and roles.
+  [AWS Amplify](https://docs.aws.amazon.com/amplify) 
+  [AWS Amplify UI Builder](https://docs.aws.amazon.com/amplify) 
+  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway) 
+  [Amazon Route 53 Application Recovery Controller](https://docs.aws.amazon.com/amazonarc) 
+  [Recovery readiness in Amazon Route 53 Application Recovery Controller](https://docs.aws.amazon.com/recovery-readiness/latest/api/what-is-recovery-readiness.html) 
+  [AWS AppConfig](https://docs.aws.amazon.com/appconfig) 
+  [Amazon AppFlow](https://docs.aws.amazon.com/appflow) 
+  [Amazon AppIntegrations](https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html#Welcome_Amazon_AppIntegrations_Service) 
+  [AWS App Runner](https://docs.aws.amazon.com/apprunner) 
+  [Amazon AppStream 2.0](https://docs.aws.amazon.com/appstream2) 
+  [AWS AppSync](https://docs.aws.amazon.com/appsync) 
+  [AWS App Mesh](https://docs.aws.amazon.com/app-mesh) 
+  [Amazon Athena](https://docs.aws.amazon.com/athena) 
+  [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager) 
+  [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide) 
+  [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling) 

  The `TagResources` and `UntagResources` operations of AWS Resource Groups Tagging API work as documented with Amazon EC2 Auto Scaling Groups. However, the `GetTagKeys`, `GetTagValues` and `GetResources` operations aren't supported at this time and return an empty response for this service.
+  [AWS B2B Data Interchange](https://docs.aws.amazon.com/b2bi/latest/userguide) 
+  [AWS Backup](https://docs.aws.amazon.com/aws-backup) 
+  [AWS Backup Gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Operations_AWS_Backup_Gateway.html) 
+  [AWS Batch](https://docs.aws.amazon.com/batch) 
+  [Amazon Bedrock](https://docs.aws.amazon.com/bedrock) 
+  [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore) 
+  [AWS Billing and Cost Management Data Exports](https://docs.aws.amazon.com/account-billing) 
+  [AWS Billing and Cost Management Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html) 
+  [Amazon Braket](https://docs.aws.amazon.com/braket) 
+  [AWS Certificate Manager](https://docs.aws.amazon.com/acm) 
+  [AWS Private Certificate Authority](https://docs.aws.amazon.com/acm) 
+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide) 
+  [AWS Cloud9](https://docs.aws.amazon.com/cloud9) 
+  [Amazon Cloud Directory](https://docs.aws.amazon.com/clouddirectory) 
+  [AWS Cloud Map](https://docs.aws.amazon.com/cloud-map) 
+  [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation) 
+  [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront) 
+  [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm) 
+  [AWS CloudTrail](https://docs.aws.amazon.com/cloudtrail) 
+  [Amazon CloudWatch (alarms only)](https://docs.aws.amazon.com/cloudwatch) 
+  [Amazon CloudWatch Events](https://docs.aws.amazon.com/cloudwatch/?id=docs_gateway#amazon-cloudwatch-events) 
+  [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) 
+  [Amazon CloudWatch Logs](https://docs.aws.amazon.com/cloudwatch/?id=docs_gateway#amazon-cloudwatch-logs) 
+  [Amazon CloudWatch Observability Access Manager](https://docs.aws.amazon.com/OAM/latest/APIReference/Welcome.html) 
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) 
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/cloudwatch) 
+  [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact) 
+  [AWS CodeBuild](https://docs.aws.amazon.com/codebuild) 
+  [AWS CodeCommit](https://docs.aws.amazon.com/codecommit) 
+  [AWS CodeConnections](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/) 
+  [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy) 
+  [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/) 
+  [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/) 
+  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline) 
+  [AWS CodeStar](https://docs.aws.amazon.com/codestar) 
+  [Amazon Cognito Identity](https://docs.aws.amazon.com/cognito) 
+  [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito) 
+  [Amazon Comprehend](https://docs.aws.amazon.com/comprehend) 
+  [AWS Config](https://docs.aws.amazon.com/config) 
+  [Amazon Connect](http://aws.amazon.com/connect/resources/?whats-new-cards#Documentation) 
+  [Amazon Connect Campaigns](https://docs.aws.amazon.com/connect) 
+  [Amazon Connect Customer Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles.html) 
+  [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange) 
+  [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) 
+  [AWS Data Pipeline](https://docs.aws.amazon.com/data-pipeline) 
+  [AWS Database Migration Service](https://docs.aws.amazon.com/dms) 
+  [AWS DataSync](https://docs.aws.amazon.com/datasync) 
+  [Amazon DataZone](https://docs.aws.amazon.com/datazone) 
+  [AWS Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/userguide) 
+  [Amazon Detective](https://docs.aws.amazon.com/detective) 
+  [AWS Device Farm](https://docs.aws.amazon.com/devicefarm) 
+  [AWS Direct Connect](https://docs.aws.amazon.com/directconnect) 
+  [AWS Directory Service](https://docs.aws.amazon.com/directory-service) 
+  [Amazon DocumentDB Elastic Clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html) 
+  [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb) 
+  [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs) 
+  [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2) 
+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder) 
+  [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/ecr) 
+  [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/ecs) 
+  [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks) 
+  [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elastic-beanstalk) 
+  [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs) 
+  [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing) 
+  [Amazon Elastic Inference](https://docs.aws.amazon.com/elastic-inference) 
+  [Amazon ElastiCache](https://docs.aws.amazon.com/elasticache) 
+  [AWS Elemental MediaConnect](https://docs.aws.amazon.com/mediaconnect) 
+  [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert) 
+  [AWS Elemental MediaLive](https://docs.aws.amazon.com/medialive) 
+  [AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage) 
+  [AWS Elemental MediaPackage v2](https://docs.aws.amazon.com/mediapackage) 
+  [AWS Elemental MediaPackage VoD](https://docs.aws.amazon.com/mediapackage) 
+  [AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor) 
+  [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb) 
+  [Amazon EMR](https://docs.aws.amazon.com/emr) 
+  [Amazon EMR on EKS (EMR containers)](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/) 
+  [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide) 
+  [AWS Entity Resolution](https://docs.aws.amazon.com/entityresolution/latest/userguide) 
+  [Amazon EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) 
+  [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide) 
+  [Amazon EventBridge Schema](https://docs.aws.amazon.com/eventbridge) 
+  [AWS Fault Injection Simulator](https://docs.aws.amazon.com/fis/latest/userguide) 
+  [AWS Firewall Manager](https://docs.aws.amazon.com/firewall-manager) 
+  [Amazon Forecast](https://docs.aws.amazon.com/forecast) 
+  [Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector) 
+  [Amazon FSx](https://docs.aws.amazon.com/fsx) 
+  [Amazon GameLift](https://docs.aws.amazon.com/gamelift) 
+  [Amazon S3 Glacier](https://docs.aws.amazon.com/s3/?id=docs_gateway#amazon-s3-glacier) 
+  [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator) 
+  [AWS Ground Station](https://docs.aws.amazon.com/ground-station) 
+  [AWS Glue](https://docs.aws.amazon.com/glue) 
+  [AWS Glue DataBrew](https://docs.aws.amazon.com/glue) 
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty) 
+  [AWS Health Imaging](https://docs.aws.amazon.com/healthimaging/latest/devguide) 
+  [AWS HealthLake](https://docs.aws.amazon.com/healthlake) 
+  [Amazon HealthOmics](https://docs.aws.amazon.com/omics) 
+  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/iam) – at this time, you can tag only the following IAM resources using the Resource Groups Tagging API:
  +  `instance-profile` 
  +  `mfa` 
  +  `oidc-provider` 
  +  `policy` 
  +  `role` 
  +  `saml-provider` 
  +  `server-certificate` 
  +  `user` 

This document was last published on October 12, 2026. 

# Actions
<a name="API_Operations"></a>

The following actions are supported:
+  [DescribeReportCreation](#API_DescribeReportCreation) 
+  [GetComplianceSummary](#API_GetComplianceSummary) 
+  [GetResources](#API_GetResources) 
+  [GetTagKeys](#API_GetTagKeys) 
+  [GetTagValues](#API_GetTagValues) 
+  [ListRequiredTags](#API_ListRequiredTags) 
+  [StartReportCreation](#API_StartReportCreation) 
+  [TagResources](#API_TagResources) 
+  [UntagResources](#API_UntagResources) 

## DescribeReportCreation
<a name="API_DescribeReportCreation"></a>

Describes the status of the `StartReportCreation` operation. 

You can call this operation only from the organization's management account and from the us-east-1 Region.

### Response Syntax
<a name="API_DescribeReportCreation_ResponseSyntax"></a>

```
{
   "ErrorMessage": "string",
   "S3Location": "string",
   "Status": "string"
}
```

### Response Elements
<a name="API_DescribeReportCreation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ErrorMessage](#API_DescribeReportCreation_ResponseSyntax) **   <a name="resourcegrouptagging-DescribeReportCreation-response-ErrorMessage"></a>
Details of the common errors that all operations return.  
Type: String

 ** [S3Location](#API_DescribeReportCreation_ResponseSyntax) **   <a name="resourcegrouptagging-DescribeReportCreation-response-S3Location"></a>
The path to the Amazon S3 bucket where the report was stored on creation.  
Type: String

 ** [Status](#API_DescribeReportCreation_ResponseSyntax) **   <a name="resourcegrouptagging-DescribeReportCreation-response-Status"></a>
Reports the status of the operation.  
The operation status can be one of the following:  
+  `RUNNING` - Report creation is in progress.
+  `SUCCEEDED` - Report creation is complete. You can open the report from the Amazon S3 bucket that you specified when you ran `StartReportCreation`.
+  `FAILED` - Report creation timed out or the Amazon S3 bucket is not accessible. 
+  `NO REPORT` - No report was generated in the last 90 days.
Type: String

### Errors
<a name="API_DescribeReportCreation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** ConstraintViolationException **   
The request failed because performing the operation would violate a constraint.  
Some of the reasons in the following list might not apply to this specific operation.  
+ You must meet the prerequisites for using tag policies. For information, see [Prerequisites and permissions](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs) in the *Tagging AWS resources and Tag Editor* user guide. 
+ You must enable the tag policies service principal (`tagpolicies.tag.amazonaws.com`) to integrate with AWS Organizations For information, see [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html).
+ You must have a tag policy attached to the organization root, an OU, or an account.
HTTP Status Code: 400

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_DescribeReportCreation_Examples"></a>

#### Example
<a name="API_DescribeReportCreation_Example_1"></a>

This example illustrates one usage of DescribeReportCreation.

##### Sample Request
<a name="API_DescribeReportCreation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 20
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.DescribeReportCreation
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42 
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS

{}
```

##### Sample Response
<a name="API_DescribeReportCreation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Date: Sun, 1 Dec 2019 21:45:25 GMT

{
    "ErrorMessage":null,
    "S3Location":"s3://amzn-s3-demo-bucket/AwsTagPolicies/o-exampleorgid/2019-12-01-T21:45:24Z/report.csv",
    "Status":"SUCCEEDED"
}
```

### See Also
<a name="API_DescribeReportCreation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation) 

## GetComplianceSummary
<a name="API_GetComplianceSummary"></a>

Returns a table that shows counts of resources that are noncompliant with their tag policies.

For more information on tag policies, see [Tag Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in the * AWS Organizations User Guide.* 

You can call this operation only from the organization's management account and from the us-east-1 Region.

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

### Request Syntax
<a name="API_GetComplianceSummary_RequestSyntax"></a>

```
{
   "GroupBy": [ "{{string}}" ],
   "MaxResults": {{number}},
   "PaginationToken": "{{string}}",
   "RegionFilters": [ "{{string}}" ],
   "ResourceTypeFilters": [ "{{string}}" ],
   "TagKeyFilters": [ "{{string}}" ],
   "TargetIdFilters": [ "{{string}}" ]
}
```

### Request Parameters
<a name="API_GetComplianceSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [GroupBy](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-GroupBy"></a>
Specifies a list of attributes to group the counts of noncompliant resources by. If supplied, the counts are sorted by those attributes.  
Type: Array of strings  
Valid Values: `TARGET_ID | REGION | RESOURCE_TYPE`   
Required: No

 ** [MaxResults](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-MaxResults"></a>
Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the `PaginationToken` response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [PaginationToken](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-PaginationToken"></a>
Specifies a `PaginationToken` response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*`   
Required: No

 ** [RegionFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-RegionFilters"></a>
Specifies a list of AWS Regions to limit the output to. If you use this parameter, the count of returned noncompliant resources includes only resources in the specified Regions.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\s\S]*`   
Required: No

 ** [ResourceTypeFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-ResourceTypeFilters"></a>
Specifies that you want the response to include information for only resources of the specified types. The format of each resource type is `service[:resourceType]`. For example, specifying a resource type of `ec2` returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of `ec2:instance` returns only EC2 instances.  
The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN). Consult the * [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/) * for the following:  
+ For a list of service name strings, see [AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces).
+ For resource type strings, see [Example ARNs](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax).
+ For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
For the list of services whose resources you can tag using the Resource Groups Tagging API, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html). If an AWS service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the `Get*` operation.
You can specify multiple resource types by using a comma separated array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter.   
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\s\S]*`   
Required: No

 ** [TagKeyFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-TagKeyFilters"></a>
Specifies that you want the response to include information for only resources that have tags with the specified tag keys. If you use this parameter, the count of returned noncompliant resources includes only resources that have the specified tag keys.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*`   
Required: No

 ** [TargetIdFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-TargetIdFilters"></a>
Specifies target identifiers (usually, specific account IDs) to limit the output by. If you use this parameter, the count of returned noncompliant resources includes only resources with the specified target IDs.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 6. Maximum length of 68.  
Pattern: `[a-zA-Z0-9-]*`   
Required: No

### Response Syntax
<a name="API_GetComplianceSummary_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
   "SummaryList": [ 
      { 
         "LastUpdated": "string",
         "NonCompliantResources": number,
         "Region": "string",
         "ResourceType": "string",
         "TargetId": "string",
         "TargetIdType": "string"
      }
   ]
}
```

### Response Elements
<a name="API_GetComplianceSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_GetComplianceSummary_ResponseSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-response-PaginationToken"></a>
A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*` 

 ** [SummaryList](#API_GetComplianceSummary_ResponseSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-response-SummaryList"></a>
A table that shows counts of noncompliant resources.  
Type: Array of [Summary](#API_Summary) objects

### Errors
<a name="API_GetComplianceSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** ConstraintViolationException **   
The request failed because performing the operation would violate a constraint.  
Some of the reasons in the following list might not apply to this specific operation.  
+ You must meet the prerequisites for using tag policies. For information, see [Prerequisites and permissions](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs) in the *Tagging AWS resources and Tag Editor* user guide. 
+ You must enable the tag policies service principal (`tagpolicies.tag.amazonaws.com`) to integrate with AWS Organizations For information, see [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html).
+ You must have a tag policy attached to the organization root, an OU, or an account.
HTTP Status Code: 400

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_GetComplianceSummary_Examples"></a>

#### Example
<a name="API_GetComplianceSummary_Example_1"></a>

This example illustrates one usage of GetComplianceSummary.

##### Sample Request
<a name="API_GetComplianceSummary_Example_1_Request"></a>

```
HTTP/1.1
Host: tagging.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 663
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.GetComplianceSummary
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42 
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS
{
   "GroupBy": [
        "TARGET_ID",
        "REGION",
        "RESOURCE_TYPE"
    ]
}
```

##### Sample Response
<a name="API_GetComplianceSummary_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Date: Sun, 1 Dec 2019 21:45:25 GMT

{
    "SummaryList": [
        {
            "LastUpdated":"2019-10-28T21:53:16Z",
            "NonCompliantResources":1,
            "Region":"us-east-1",
            "ResourceType":"ec2:instance",
            "TargetId":"333333333333",
            "TargetIdType":"ACCOUNT"
        },
        {
            "LastUpdated":"2019-10-28T21:53:17Z",
            "NonCompliantResources":0,
            "Region":"us-east-1",
            "ResourceType":"ec2:snapshot",
            "TargetId":"222222222222",
            "TargetIdType":"ACCOUNT"
        },
        {
            "LastUpdated":"2019-10-28T21:53:16Z",
            "NonCompliantResources":1,
            "Region":"us-east-1",
            "ResourceType":"ec2:volume",
            "TargetId":"111111111111",
            "TargetIdType":"ACCOUNT"
        }
    ]
}
```

### See Also
<a name="API_GetComplianceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary) 

## GetResources
<a name="API_GetResources"></a>

Returns all the tagged or previously tagged resources that are located in the specified AWS Region for the account. 

Depending on what information you want returned, you can also specify the following:
+  *Filters* that specify what tags and resource types you want returned. The response includes all tags that are associated with the requested resources.
+ Information about compliance with the account's effective tag policy. For more information on tag policies, see [Tag Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in the * AWS Organizations User Guide.* 

**Note**  
This operation has a rate limit that specifies the maximum number of times you can call it per second. For the current value of this limit, see [Service Quotas for Resource Groups Tagging API](https://docs.aws.amazon.com/tag-editor/latest/userguide/reference.html) in the *Tag Editor Users Guide*.

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

**Note**  
 `GetResources` does not return untagged resources.   
To find untagged resources in your account, use AWS Resource Explorer with a query that uses `tag:none`. For more information, see [ Search query syntax reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html). 

### Request Syntax
<a name="API_GetResources_RequestSyntax"></a>

```
{
   "ExcludeCompliantResources": {{boolean}},
   "IncludeComplianceDetails": {{boolean}},
   "PaginationToken": "{{string}}",
   "ResourceARNList": [ "{{string}}" ],
   "ResourcesPerPage": {{number}},
   "ResourceTypeFilters": [ "{{string}}" ],
   "TagFilters": [ 
      { 
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "TagsPerPage": {{number}}
}
```

### Request Parameters
<a name="API_GetResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [ExcludeCompliantResources](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ExcludeCompliantResources"></a>
Specifies whether to exclude resources that are compliant with the tag policy. Set this to `true` if you are interested in retrieving information on noncompliant resources only.  
You can use this parameter only if the `IncludeComplianceDetails` parameter is also set to `true`.  
Type: Boolean  
Required: No

 ** [IncludeComplianceDetails](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-IncludeComplianceDetails"></a>
Specifies whether to include details regarding the compliance with the effective tag policy. Set this to `true` to determine whether resources are compliant with the tag policy and to get details.  
Type: Boolean  
Required: No

 ** [PaginationToken](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-PaginationToken"></a>
Specifies a `PaginationToken` response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*`   
Required: No

 ** [ResourceARNList](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ResourceARNList"></a>
Specifies a list of ARNs of resources for which you want to retrieve tag data.  
You can't specify both this parameter and the `ResourceTypeFilters` parameter in the same request. If you do, you get an `Invalid Parameter` exception.  
You can't specify both this parameter and the `TagFilters` parameter in the same request. If you do, you get an `Invalid Parameter` exception.  
You can't specify both this parameter and any of the pagination parameters (`ResourcesPerPage`, `TagsPerPage`, `PaginationToken`) in the same request. If you do, you get an `Invalid Parameter` exception.  
If a resource specified by this parameter doesn't exist, it doesn't generate an error; it simply isn't included in the response.  
An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `[\s\S]*`   
Required: No

 ** [ResourcesPerPage](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ResourcesPerPage"></a>
Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the `PaginationToken` response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.  
Type: Integer  
Required: No

 ** [ResourceTypeFilters](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ResourceTypeFilters"></a>
Specifies the resource types that you want included in the response. The format of each resource type is `service[:resourceType]`. For example, specifying a service of `ec2` returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of `ec2:instance` returns only EC2 instances.   
You can't specify both this parameter and the `ResourceArnList` parameter in the same request. If you do, you get an `Invalid Parameter` exception.  
The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN).  
For the list of services whose resources you can tag using the Resource Groups Tagging API, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html). If an AWS service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the `Get*` operation.
You can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter. For example, the following string would limit the response to only Amazon EC2 instances, Amazon S3 buckets, or any AWS Audit Manager resource:  
 `ec2:instance,s3:bucket,auditmanager`   
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\s\S]*`   
Required: No

 ** [TagFilters](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-TagFilters"></a>
Specifies a list of TagFilters (keys and values) to restrict the output to only those resources that have tags with the specified keys and, if included, the specified values. Each `TagFilter` must contain a key with values optional. A request can include up to 50 keys, and each key can include up to 20 values.   
You can't specify both this parameter and the `ResourceArnList` parameter in the same request. If you do, you get an `Invalid Parameter` exception.  
Note the following when deciding how to use TagFilters:  
+ If you *don't* specify a `TagFilter`, the response includes all resources that are currently tagged or ever had a tag. Resources that were previously tagged, *but do not currently* have tags, are shown with an empty tag set, like this: `"Tags": []`.
+ If you specify more than one filter in a single request, the response returns only those resources that satisfy all filters.
+ If you specify a filter that contains more than one value for a key, the response returns resources that match *any* of the specified values for that key.
+ If you don't specify a value for a key, the response returns all resources that are tagged with that key, with any or no value.

  For example, for the following filters: `filter1= {key1,{value1}}`, `filter2={key2,{value2,value3,value4}}`, `filter3= {key3}`:
  +  `GetResources({filter1})` returns resources tagged with `key1=value1` 
  +  `GetResources({filter2})` returns resources tagged with `key2=value2` or `key2=value3` or `key2=value4` 
  +  `GetResources({filter3})` returns resources tagged with any tag with the key `key3`, and with any or no value
  +  `GetResources({filter1,filter2,filter3})` returns resources tagged with `(key1=value1) and (key2=value2 or key2=value3 or key2=value4) and (key3, any or no value)` 
Type: Array of [TagFilter](#API_TagFilter) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** [TagsPerPage](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-TagsPerPage"></a>
 AWS recommends using `ResourcesPerPage` instead of this parameter.  
A limit that restricts the number of tags (key and value pairs) returned by `GetResources` in paginated output. A resource with no tags is counted as having one tag (one key and value pair).  
 `GetResources` does not split a resource and its associated tags across pages. If the specified `TagsPerPage` would cause such a break, a `PaginationToken` is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a `TagsPerPage` of `100` and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of three pages. The first page displays the first 10 resources, each with its 10 tags. The second page displays the next 10 resources, each with its 10 tags. The third page displays the remaining 2 resources, each with its 10 tags.  
You can set `TagsPerPage` to a minimum of 100 items up to a maximum of 500 items.  
Type: Integer  
Required: No

### Response Syntax
<a name="API_GetResources_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
   "ResourceTagMappingList": [ 
      { 
         "ComplianceDetails": { 
            "ComplianceStatus": boolean,
            "KeysWithNoncompliantValues": [ "string" ],
            "MissingTagKeys": [ "string" ],
            "NoncompliantKeys": [ "string" ]
         },
         "ResourceARN": "string",
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

### Response Elements
<a name="API_GetResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_GetResources_ResponseSyntax) **   <a name="resourcegrouptagging-GetResources-response-PaginationToken"></a>
A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*` 

 ** [ResourceTagMappingList](#API_GetResources_ResponseSyntax) **   <a name="resourcegrouptagging-GetResources-response-ResourceTagMappingList"></a>
A list of resource ARNs and the tags (keys and values) associated with each.  
Type: Array of [ResourceTagMapping](#API_ResourceTagMapping) objects

### Errors
<a name="API_GetResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** PaginationTokenExpiredException **   
The request failed because the specified `PaginationToken` has expired. A `PaginationToken` is valid for a maximum of 15 minutes.  
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_GetResources_Examples"></a>

#### Example
<a name="API_GetResources_Example_1"></a>

This example illustrates one usage of GetResources.

##### Sample Request
<a name="API_GetResources_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 80
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.GetResources
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "ExcludeCompliantResources": null,
    "IncludeComplianceDetails": true,
    "PaginationToken": 1
}
```

##### Sample Response
<a name="API_GetResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 14bc735b-26da-11e7-a933-67e2d2f3ef37
Content-Type: application/x-amz-json-1.1
Content-Length: 4060
Date: Sun, 1 Dec 2019 21:45:25 GMT
{
    "PaginationToken": "",
    "ResourceTagMappingList": [
        {
            "ComplianceDetails": {
                "ComplianceStatus":true,
                "KeysWithNoncompliantValues":[],
                "NoncompliantKeys":[]
            },
            "ResourceARN": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0",
            "Tags": []
        }
    ]
}
```

### See Also
<a name="API_GetResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/GetResources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/GetResources) 

## GetTagKeys
<a name="API_GetTagKeys"></a>

Returns all tag keys currently in use in the specified AWS Region for the calling account.

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

### Request Syntax
<a name="API_GetTagKeys_RequestSyntax"></a>

```
{
   "PaginationToken": "{{string}}"
}
```

### Request Parameters
<a name="API_GetTagKeys_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [PaginationToken](#API_GetTagKeys_RequestSyntax) **   <a name="resourcegrouptagging-GetTagKeys-request-PaginationToken"></a>
Specifies a `PaginationToken` response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*`   
Required: No

### Response Syntax
<a name="API_GetTagKeys_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
   "TagKeys": [ "string" ]
}
```

### Response Elements
<a name="API_GetTagKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_GetTagKeys_ResponseSyntax) **   <a name="resourcegrouptagging-GetTagKeys-response-PaginationToken"></a>
A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*` 

 ** [TagKeys](#API_GetTagKeys_ResponseSyntax) **   <a name="resourcegrouptagging-GetTagKeys-response-TagKeys"></a>
A list of all tag keys in the AWS account.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*` 

### Errors
<a name="API_GetTagKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** PaginationTokenExpiredException **   
The request failed because the specified `PaginationToken` has expired. A `PaginationToken` is valid for a maximum of 15 minutes.  
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_GetTagKeys_Examples"></a>

#### Example
<a name="API_GetTagKeys_Example_1"></a>

This example illustrates one usage of GetTagKeys.

##### Sample Request
<a name="API_GetTagKeys_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.GetTagKeys
X-Amz-Date: 20170421T214126Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{}
```

##### Sample Response
<a name="API_GetTagKeys_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 462f0799-26db-11e7-a88c-a74e0c5622c9
Content-Type: application/x-amz-json-1.1
Content-Length: 79
Date: Fri, 21 Apr 2017 21:41:27 GMT

{
    "PaginationToken": "",
    "TagKeys": [
        "Example",
        "Example1",
        "Example2"
    ]
}
```

### See Also
<a name="API_GetTagKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/GetTagKeys) 

## GetTagValues
<a name="API_GetTagValues"></a>

Returns all tag values for the specified key that are used in the specified AWS Region for the calling account.

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

### Request Syntax
<a name="API_GetTagValues_RequestSyntax"></a>

```
{
   "Key": "{{string}}",
   "PaginationToken": "{{string}}"
}
```

### Request Parameters
<a name="API_GetTagValues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [Key](#API_GetTagValues_RequestSyntax) **   <a name="resourcegrouptagging-GetTagValues-request-Key"></a>
Specifies the tag key for which you want to list all existing values that are currently used in the specified AWS Region for the calling account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*`   
Required: Yes

 ** [PaginationToken](#API_GetTagValues_RequestSyntax) **   <a name="resourcegrouptagging-GetTagValues-request-PaginationToken"></a>
Specifies a `PaginationToken` response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*`   
Required: No

### Response Syntax
<a name="API_GetTagValues_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
   "TagValues": [ "string" ]
}
```

### Response Elements
<a name="API_GetTagValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_GetTagValues_ResponseSyntax) **   <a name="resourcegrouptagging-GetTagValues-response-PaginationToken"></a>
A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*` 

 ** [TagValues](#API_GetTagValues_ResponseSyntax) **   <a name="resourcegrouptagging-GetTagValues-response-TagValues"></a>
A list of all tag values for the specified key currently used in the specified AWS Region for the calling account.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\s\S]*` 

### Errors
<a name="API_GetTagValues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** PaginationTokenExpiredException **   
The request failed because the specified `PaginationToken` has expired. A `PaginationToken` is valid for a maximum of 15 minutes.  
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_GetTagValues_Examples"></a>

#### Example
<a name="API_GetTagValues_Example_1"></a>

This example illustrates one usage of GetTagValues.

##### Sample Request
<a name="API_GetTagValues_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 18
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.GetTagValues
X-Amz-Date: 20170421T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "Key": "Example_key"
}
```

##### Sample Response
<a name="API_GetTagValues_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Content-Length: 42
Date: Fri, 21 Apr 2017 21:45:25 GMT

{
    "PaginationToken": "",
    "TagValues": [
        "Example_value"
    ]
}
```

### See Also
<a name="API_GetTagValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/GetTagValues) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/GetTagValues) 

## ListRequiredTags
<a name="API_ListRequiredTags"></a>

Lists the required tags for supported resource types in an AWS account.

### Request Syntax
<a name="API_ListRequiredTags_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

### Request Parameters
<a name="API_ListRequiredTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRequiredTags_RequestSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-request-MaxResults"></a>
The maximum number of required tags.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 200.  
Required: No

 ** [NextToken](#API_ListRequiredTags_RequestSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-request-NextToken"></a>
A token for requesting another page of required tags if the `NextToken` response element indicates that more required tags are available. Use the value of the returned `NextToken` element in your request until the token comes back as null. Pass null if this is the first call.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*`   
Required: No

### Response Syntax
<a name="API_ListRequiredTags_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RequiredTags": [ 
      { 
         "CloudFormationResourceTypes": [ "string" ],
         "ReportingTagKeys": [ "string" ],
         "ResourceType": "string"
      }
   ]
}
```

### Response Elements
<a name="API_ListRequiredTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRequiredTags_ResponseSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-response-NextToken"></a>
A token for requesting another page of required tags if the `NextToken` response element indicates that more required tags are available. Use the value of the returned `NextToken` element in your request until the token comes back as null. Pass null if this is the first call.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]*` 

 ** [RequiredTags](#API_ListRequiredTags_ResponseSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-response-RequiredTags"></a>
The required tags.  
Type: Array of [RequiredTag](#API_RequiredTag) objects

### Errors
<a name="API_ListRequiredTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** PaginationTokenExpiredException **   
The request failed because the specified `PaginationToken` has expired. A `PaginationToken` is valid for a maximum of 15 minutes.  
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_ListRequiredTags_Examples"></a>

#### Example
<a name="API_ListRequiredTags_Example_1"></a>

This example illustrates one usage of ListRequiredTags.

##### Sample Request
<a name="API_ListRequiredTags_Example_1_Request"></a>

```
                    POST / HTTP/1.1
                    Host: tagging.us-east-1.amazonaws.com
                    Accept-Encoding: identity
                    Content-Length: 20
                    X-Amz-Target: ResourceGroupsTaggingAPI_20170126.ListRequiredTags
                    X-Amz-Date: 20191201T214524Z
                    User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
                    Content-Type: application/x-amz-json-1.1
                    Authorization:  AUTHPARAMS

                    {}
```

##### Sample Response
<a name="API_ListRequiredTags_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
                    x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
                    Content-Type: application/x-amz-json-1.1
                    Date: Sun, 1 Dec 2019 21:45:25 GMT

                    {
                        "RequiredTags": [
                            {
                                "ResourceType": "ec2:instance",
                                "CloudFormationResourceTypes": ["AWS::EC2::Instance"],
                                "ReportingTagKeys": ["example_tag_key"]
                            },
                            {
                                "ResourceType": "s3:bucket",
                                "CloudFormationResourceTypes": ["AWS::S3:Bucket"],
                                "ReportingTagKeys": ["example_tag_key"]
                            }
                        ]
                    }
```

### See Also
<a name="API_ListRequiredTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags) 

## StartReportCreation
<a name="API_StartReportCreation"></a>

Generates a report that lists all tagged resources in the accounts across your organization and tells whether each resource is compliant with the effective tag policy. Compliance data is refreshed daily. The report is generated asynchronously.

The generated report is saved to the following location:

 `s3://amzn-s3-demo-bucket/AwsTagPolicies/o-exampleorgid/YYYY-MM-ddTHH:mm:ssZ/report.csv` 

For more information about evaluating resource compliance with tag policies, including the required permissions, review [Permissions for evaluating organization-wide compliance](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-permissions-org) in the *Tagging AWS Resources and Tag Editor* user guide. 

You can call this operation only from the organization's management account and from the us-east-1 Region.

If the account associated with the identity used to call `StartReportCreation` is different from the account that owns the Amazon S3 bucket, there must be a bucket policy attached to the bucket to provide access. For more information, review [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS Resources and Tag Editor* user guide.

### Request Syntax
<a name="API_StartReportCreation_RequestSyntax"></a>

```
{
   "S3Bucket": "{{string}}"
}
```

### Request Parameters
<a name="API_StartReportCreation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [S3Bucket](#API_StartReportCreation_RequestSyntax) **   <a name="resourcegrouptagging-StartReportCreation-request-S3Bucket"></a>
The name of the Amazon S3 bucket where the report will be stored; for example:  
 `amzn-s3-demo-bucket`   
For more information on S3 bucket requirements, including an example bucket policy, see the example Amazon S3 bucket policy on this page.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `[a-z0-9.-]*`   
Required: Yes

### Response Elements
<a name="API_StartReportCreation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

### Errors
<a name="API_StartReportCreation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** ConcurrentModificationException **   
The request failed because the target of the operation is currently being modified by a different request. Try again later.  
HTTP Status Code: 400

 ** ConstraintViolationException **   
The request failed because performing the operation would violate a constraint.  
Some of the reasons in the following list might not apply to this specific operation.  
+ You must meet the prerequisites for using tag policies. For information, see [Prerequisites and permissions](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs) in the *Tagging AWS resources and Tag Editor* user guide. 
+ You must enable the tag policies service principal (`tagpolicies.tag.amazonaws.com`) to integrate with AWS Organizations For information, see [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html).
+ You must have a tag policy attached to the organization root, an OU, or an account.
HTTP Status Code: 400

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_StartReportCreation_Examples"></a>

#### Example
<a name="API_StartReportCreation_Example_1"></a>

This example illustrates one usage of StartReportCreation.

##### Sample Request
<a name="API_StartReportCreation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 20
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.StartReportCreation
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42 
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS

{
    "S3Bucket": "amzn-s3-demo-bucket"
}
```

##### Sample Response
<a name="API_StartReportCreation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Date: Sun, 1 Dec 2019 21:45:25 GMT

{}
```

### See Also
<a name="API_StartReportCreation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/StartReportCreation) 

## TagResources
<a name="API_TagResources"></a>

Applies one or more tags to the specified resources. Note the following:
+ Not all resources can have tags. For a list of services with resources that support tagging using this operation, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html). If the resource doesn't yet support this operation, the resource's service might support tagging using its own API operations. For more information, refer to the documentation for that service.
+ Each resource can have up to 50 tags. For other limits, see [Tag Naming and Usage Conventions](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions) in the * AWS General Reference.* 
+ You can only tag resources that are located in the specified AWS Region for the AWS account.
+ To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.
+ When you use the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html) to update tags for AWS CloudFormation stack sets, AWS calls the [AWS CloudFormation `UpdateStack`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStack.html) operation. This operation may initiate additional resource property updates in addition to the desired tag updates. To avoid unexpected resource updates, AWS recommends that you only apply or update tags to your CloudFormation stack sets using AWS CloudFormation. 

**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

 **Minimum permissions** 

In addition to the `tag:TagResources` permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag an Amazon EC2 instance using the `TagResources` operation, you must have both of the following permissions:
+  `tag:TagResources` 
+  `ec2:CreateTags` 

**Note**  
In addition, some services might have specific requirements for tagging some types of resources. For example, to tag an Amazon S3 bucket, you must also have the `s3:GetBucketTagging` permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.

### Request Syntax
<a name="API_TagResources_RequestSyntax"></a>

```
{
   "ResourceARNList": [ "{{string}}" ],
   "Tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

### Request Parameters
<a name="API_TagResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [ResourceARNList](#API_TagResources_RequestSyntax) **   <a name="resourcegrouptagging-TagResources-request-ResourceARNList"></a>
Specifies the list of ARNs of the resources that you want to apply tags to.  
An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `[\s\S]*`   
Required: Yes

 ** [Tags](#API_TagResources_RequestSyntax) **   <a name="resourcegrouptagging-TagResources-request-Tags"></a>
Specifies a list of tags that you want to add to the specified resources. A tag consists of a key and a value that you define.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[\s\S]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[\s\S]*`   
Required: Yes

### Response Syntax
<a name="API_TagResources_ResponseSyntax"></a>

```
{
   "FailedResourcesMap": { 
      "string" : { 
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "StatusCode": number
      }
   }
}
```

### Response Elements
<a name="API_TagResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedResourcesMap](#API_TagResources_ResponseSyntax) **   <a name="resourcegrouptagging-TagResources-response-FailedResourcesMap"></a>
A map containing a key-value pair for each failed item that couldn't be tagged. The key is the ARN of the failed resource. The value is a `FailureInfo` object that contains an error code, a status code, and an error message. If there are no errors, the `FailedResourcesMap` is empty.  
Type: String to [FailureInfo](#API_FailureInfo) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 1011.  
Key Pattern: `[\s\S]*` 

### Errors
<a name="API_TagResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_TagResources_Examples"></a>

#### Example
<a name="API_TagResources_Example_1"></a>

This example illustrates one usage of TagResources.

##### Sample Request
<a name="API_TagResources_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 82
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.TagResources
X-Amz-Date: 20170421T214834Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS
{
    "ResourceARNList": [
        "arn:aws:s3:::amzn-s3-demo-bucket"
    ],
    "Tags": {
        "key": "Example_key"
    }
}
```

##### Sample Response
<a name="API_TagResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 45352206-26dc-11e7-8812-6fb02084e31d
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Fri, 21 Apr 2017 21:48:35 GMT
```

### See Also
<a name="API_TagResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/TagResources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/TagResources) 

## UntagResources
<a name="API_UntagResources"></a>

Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:
+ To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see the documentation for the service whose resource you want to untag.
+ You can only tag resources that are located in the specified AWS Region for the calling AWS account.

 **Minimum permissions** 

In addition to the `tag:UntagResources` permission required by this operation, you must also have the remove tags permission defined by the service that created the resource. For example, to remove the tags from an Amazon EC2 instance using the `UntagResources` operation, you must have both of the following permissions:
+  `tag:UntagResources` 
+  `ec2:DeleteTags` 

**Note**  
In addition, some services might have specific requirements for untagging some types of resources. For example, to untag AWS Glue Connection, you must also have the `glue:GetConnection` permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.

### Request Syntax
<a name="API_UntagResources_RequestSyntax"></a>

```
{
   "ResourceARNList": [ "{{string}}" ],
   "TagKeys": [ "{{string}}" ]
}
```

### Request Parameters
<a name="API_UntagResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](#CommonParameters).

The request accepts the following data in JSON format.

 ** [ResourceARNList](#API_UntagResources_RequestSyntax) **   <a name="resourcegrouptagging-UntagResources-request-ResourceARNList"></a>
Specifies a list of ARNs of the resources that you want to remove tags from.  
An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `[\s\S]*`   
Required: Yes

 ** [TagKeys](#API_UntagResources_RequestSyntax) **   <a name="resourcegrouptagging-UntagResources-request-TagKeys"></a>
Specifies a list of tag keys that you want to remove from the specified resources.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*`   
Required: Yes

### Response Syntax
<a name="API_UntagResources_ResponseSyntax"></a>

```
{
   "FailedResourcesMap": { 
      "string" : { 
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "StatusCode": number
      }
   }
}
```

### Response Elements
<a name="API_UntagResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedResourcesMap](#API_UntagResources_ResponseSyntax) **   <a name="resourcegrouptagging-UntagResources-response-FailedResourcesMap"></a>
A map containing a key-value pair for each failed item that couldn't be untagged. The key is the ARN of the failed resource. The value is a `FailureInfo` object that contains an error code, a status code, and an error message. If there are no errors, the `FailedResourcesMap` is empty.  
Type: String to [FailureInfo](#API_FailureInfo) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 1011.  
Key Pattern: `[\s\S]*` 

### Errors
<a name="API_UntagResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** InternalServiceException **   
The request processing failed because of an unknown error, exception, or failure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
The request failed because of one of the following reasons:  
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide. 
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** ThrottledException **   
The request failed because it exceeded the allowed frequency of submitted requests.  
HTTP Status Code: 400

### Examples
<a name="API_UntagResources_Examples"></a>

#### Example
<a name="API_UntagResources_Example_1"></a>

This example illustrates one usage of UntagResources.

##### Sample Request
<a name="API_UntagResources_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 74
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.UntagResources
X-Amz-Date: 20170421T215122Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS
{
    "TagKeys": [
        "key"
    ],
    "ResourceARNList": [
        "arn:aws:s3:::amzn-s3-demo-bucket"
    ]
}
```

##### Sample Response
<a name="API_UntagResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: a923ddd9-26dc-11e7-bf86-49f2fe9ee8df
Content-Type: application/x-amz-json-1.1
Content-Length: 25
Date: Fri, 21 Apr 2017 21:51:23 GMT

{
    "FailedResourcesMap": {}
}
```

### See Also
<a name="API_UntagResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/UntagResources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/UntagResources) 

# Data Types
<a name="API_Types"></a>

The Resource Groups Tagging API API contains several data types that various actions use. This section describes each data type in detail.

**Note**  
The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:
+  [ComplianceDetails](#API_ComplianceDetails) 
+  [FailureInfo](#API_FailureInfo) 
+  [RequiredTag](#API_RequiredTag) 
+  [ResourceTagMapping](#API_ResourceTagMapping) 
+  [Summary](#API_Summary) 
+  [Tag](#API_Tag) 
+  [TagFilter](#API_TagFilter) 

## ComplianceDetails
<a name="API_ComplianceDetails"></a>

Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.

### Contents
<a name="API_ComplianceDetails_Contents"></a>

 ** ComplianceStatus **   <a name="resourcegrouptagging-Type-ComplianceDetails-ComplianceStatus"></a>
Whether a resource is compliant with the effective tag policy.  
Type: Boolean  
Required: No

 ** KeysWithNoncompliantValues **   <a name="resourcegrouptagging-Type-ComplianceDetails-KeysWithNoncompliantValues"></a>
These are keys defined in the effective policy that are on the resource with either incorrect case treatment or noncompliant values.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*`   
Required: No

 ** MissingTagKeys **   <a name="resourcegrouptagging-Type-ComplianceDetails-MissingTagKeys"></a>
These tag keys are defined as required in the `report_required_tag_for` block of the effective tag policy, but are missing from the resource.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*`   
Required: No

 ** NoncompliantKeys **   <a name="resourcegrouptagging-Type-ComplianceDetails-NoncompliantKeys"></a>
These tag keys on the resource are noncompliant with the effective tag policy.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*`   
Required: No

### See Also
<a name="API_ComplianceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/ComplianceDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/ComplianceDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/ComplianceDetails) 

## FailureInfo
<a name="API_FailureInfo"></a>

Information about the errors that are returned for each failed resource. This information can include `InternalServiceException` and `InvalidParameterException` errors. It can also include any valid error code returned by the AWS service that hosts the resource that the ARN key represents.

The following are common error codes that you might receive from other AWS services:
+  **InternalServiceException** – This can mean that the Resource Groups Tagging API didn't receive a response from another AWS service. It can also mean that the resource type in the request is not supported by the Resource Groups Tagging API. In these cases, it's safe to retry the request and then call [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) to verify the changes.
+  **AccessDeniedException** – This can mean that you need permission to call the tagging operations in the AWS service that contains the resource. For example, to use the Resource Groups Tagging API to tag a Amazon CloudWatch alarm resource, you need permission to call both [`TagResources`](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) *and* [`TagResource`](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) in the CloudWatch API. 

For more information on errors that are generated from other AWS services, see the documentation for that service. 

### Contents
<a name="API_FailureInfo_Contents"></a>

 ** ErrorCode **   <a name="resourcegrouptagging-Type-FailureInfo-ErrorCode"></a>
The code of the common error. Valid values include `InternalServiceException`, `InvalidParameterException`, and any valid error code returned by the AWS service that hosts the resource that you want to tag.  
Type: String  
Valid Values: `InternalServiceException | InvalidParameterException`   
Required: No

 ** ErrorMessage **   <a name="resourcegrouptagging-Type-FailureInfo-ErrorMessage"></a>
The message of the common error.  
Type: String  
Required: No

 ** StatusCode **   <a name="resourcegrouptagging-Type-FailureInfo-StatusCode"></a>
The HTTP status code of the common error.  
Type: Integer  
Required: No

### See Also
<a name="API_FailureInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/FailureInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/FailureInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/FailureInfo) 

## RequiredTag
<a name="API_RequiredTag"></a>

Information that describes the required tags for a given resource type.

### Contents
<a name="API_RequiredTag_Contents"></a>

 ** CloudFormationResourceTypes **   <a name="resourcegrouptagging-Type-RequiredTag-CloudFormationResourceTypes"></a>
Describes the CloudFormation resource type assigned the required tag keys.  
Type: Array of strings  
Required: No

 ** ReportingTagKeys **   <a name="resourcegrouptagging-Type-RequiredTag-ReportingTagKeys"></a>
These tag keys are marked as `required` in the `report_required_tag_for` block of the effective tag policy.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\s\S]*`   
Required: No

 ** ResourceType **   <a name="resourcegrouptagging-Type-RequiredTag-ResourceType"></a>
Describes the resource type for the required tag keys.  
Type: String  
Required: No

### See Also
<a name="API_RequiredTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/RequiredTag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/RequiredTag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/RequiredTag) 

## ResourceTagMapping
<a name="API_ResourceTagMapping"></a>

A list of resource ARNs and the tags (keys and values) that are associated with each.

### Contents
<a name="API_ResourceTagMapping_Contents"></a>

 ** ComplianceDetails **   <a name="resourcegrouptagging-Type-ResourceTagMapping-ComplianceDetails"></a>
Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.  
Type: [ComplianceDetails](#API_ComplianceDetails) object  
Required: No

 ** ResourceARN **   <a name="resourcegrouptagging-Type-ResourceTagMapping-ResourceARN"></a>
The ARN of the resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `[\s\S]*`   
Required: No

 ** Tags **   <a name="resourcegrouptagging-Type-ResourceTagMapping-Tags"></a>
The tags that have been applied to one or more AWS resources.  
Type: Array of [Tag](#API_Tag) objects  
Required: No

### See Also
<a name="API_ResourceTagMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/ResourceTagMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/ResourceTagMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/ResourceTagMapping) 

## Summary
<a name="API_Summary"></a>

A count of noncompliant resources.

### Contents
<a name="API_Summary_Contents"></a>

 ** LastUpdated **   <a name="resourcegrouptagging-Type-Summary-LastUpdated"></a>
The timestamp that shows when this summary was generated in this Region.   
Type: String  
Required: No

 ** NonCompliantResources **   <a name="resourcegrouptagging-Type-Summary-NonCompliantResources"></a>
The count of noncompliant resources.  
Type: Long  
Required: No

 ** Region **   <a name="resourcegrouptagging-Type-Summary-Region"></a>
The AWS Region that the summary applies to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\s\S]*`   
Required: No

 ** ResourceType **   <a name="resourcegrouptagging-Type-Summary-ResourceType"></a>
The AWS resource type.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\s\S]*`   
Required: No

 ** TargetId **   <a name="resourcegrouptagging-Type-Summary-TargetId"></a>
The account identifier or the root identifier of the organization. If you don't know the root ID, you can call the AWS Organizations [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html) API.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 68.  
Pattern: `[a-zA-Z0-9-]*`   
Required: No

 ** TargetIdType **   <a name="resourcegrouptagging-Type-Summary-TargetIdType"></a>
Whether the target is an account, an OU, or the organization root.  
Type: String  
Valid Values: `ACCOUNT | OU | ROOT`   
Required: No

### See Also
<a name="API_Summary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/Summary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/Summary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/Summary) 

## Tag
<a name="API_Tag"></a>

The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.

### Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="resourcegrouptagging-Type-Tag-Key"></a>
One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`   
Required: Yes

 ** Value **   <a name="resourcegrouptagging-Type-Tag-Value"></a>
One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`   
Required: Yes

### See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/Tag) 

## TagFilter
<a name="API_TagFilter"></a>

A list of tags (keys and values) that are used to specify the associated resources.

### Contents
<a name="API_TagFilter_Contents"></a>

 ** Key **   <a name="resourcegrouptagging-Type-TagFilter-Key"></a>
One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`   
Required: No

 ** Values **   <a name="resourcegrouptagging-Type-TagFilter-Values"></a>
One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 256 items.  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\s\S]*`   
Required: No

### See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/TagFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/TagFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/TagFilter) 

# Common Parameters
<a name="CommonParameters"></a>

The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string. Any action-specific parameters are listed in the topic for that action. For more information about Signature Version 4, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

 **X-Amz-Algorithm**   <a name="CommonParameters-X-Amz-Algorithm"></a>
The hash algorithm that you used to create the request signature.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Valid Values: `AWS4-HMAC-SHA256`   
Required: Conditional

 **X-Amz-Credential**   <a name="CommonParameters-X-Amz-Credential"></a>
The credential scope value, which is a string that includes your access key, the date, the region you are targeting, the service you are requesting, and a termination string ("aws4\_request"). The value is expressed in the following format: *access\_key*/*YYYYMMDD*/*region*/*service*/aws4\_request.  
For more information, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the *IAM User Guide*.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

 **X-Amz-Date**   <a name="CommonParameters-X-Amz-Date"></a>
The date that is used to create the signature. The format must be ISO 8601 basic format (YYYYMMDD'T'HHMMSS'Z'). For example, the following date time is a valid X-Amz-Date value: `20120325T120000Z`.  
Condition: X-Amz-Date is optional for all requests; it can be used to override the date used for signing requests. If the Date header is specified in the ISO 8601 basic format, X-Amz-Date is not required. When X-Amz-Date is used, it always overrides the value of the Date header. For more information, see [Elements of an AWS API request signature](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-signing-elements.html) in the *IAM User Guide*.  
Type: string  
Required: Conditional

 **X-Amz-Security-Token**   <a name="CommonParameters-X-Amz-Security-Token"></a>
The temporary security token that was obtained through a call to AWS Security Token Service (AWS STS). For a list of services that support temporary security credentials from AWS STS, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.  
Condition: If you're using temporary security credentials from AWS STS, you must include the security token.  
Type: string  
Required: Conditional

 **X-Amz-Signature**   <a name="CommonParameters-X-Amz-Signature"></a>
Specifies the hex-encoded signature that was calculated from the string to sign and the derived signing key.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

 **X-Amz-SignedHeaders**   <a name="CommonParameters-X-Amz-SignedHeaders"></a>
Specifies all the HTTP headers that were included as part of the canonical request. For more information about specifying signed headers, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the *IAM User Guide*.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

# Common Error Types
<a name="CommonErrors"></a>

This section lists common error types that this AWS service may return. Not all services return all error types listed here. For errors specific to an API action for this service, see the topic for that API action.

 **AccessDeniedException**   <a name="CommonErrors-AccessDeniedException"></a>
You don't have permission to perform this action. Verify that your IAM policy includes the required permissions.  
HTTP Status Code: 403

 **ExpiredTokenException**   <a name="CommonErrors-ExpiredTokenException"></a>
The security token included in the request has expired. Request a new security token and try again.  
HTTP Status Code: 403

 **IncompleteSignature**   <a name="CommonErrors-IncompleteSignature"></a>
The request signature doesn't conform to AWS standards. Verify that you're using valid AWS credentials and that your request is properly formatted. If you're using an SDK, ensure it's up to date.  
HTTP Status Code: 403

 **InternalFailure**   <a name="CommonErrors-InternalFailure"></a>
The request can't be processed right now because of an internal server issue. Try again later. If the problem persists, contact AWS Support.  
HTTP Status Code: 500

 **MalformedHttpRequestException**   <a name="CommonErrors-MalformedHttpRequestException"></a>
The request body can't be processed. This typically happens when the request body can't be decompressed using the specified content encoding algorithm. Verify that the content encoding header matches the compression format used.  
HTTP Status Code: 400

 **NotAuthorized**   <a name="CommonErrors-NotAuthorized"></a>
You don't have permissions to perform this action. Verify that your IAM policy includes the required permissions.  
HTTP Status Code: 401

 **OptInRequired**   <a name="CommonErrors-OptInRequired"></a>
Your AWS account needs a subscription for this service. Verify that you've enabled the service in your account.  
HTTP Status Code: 403

 **RequestAbortedException**   <a name="CommonErrors-RequestAbortedException"></a>
The request was aborted before a response could be returned. This typically happens when the client closes the connection.  
HTTP Status Code: 400

 **RequestEntityTooLargeException**   <a name="CommonErrors-RequestEntityTooLargeException"></a>
The request entity is too large. Reduce the size of the request body and try again.  
HTTP Status Code: 413

 **RequestTimeoutException**   <a name="CommonErrors-RequestTimeoutException"></a>
The request timed out. The server didn't receive the complete request within the expected time frame. Try again.  
HTTP Status Code: 408

 **ServiceUnavailable**   <a name="CommonErrors-ServiceUnavailable"></a>
The service is temporarily unavailable. Try again later.  
HTTP Status Code: 503

 **ThrottlingException**   <a name="CommonErrors-ThrottlingException"></a>
Your request rate is too high. The AWS SDKs automatically retry requests that receive this exception. Reduce the frequency of requests.  
HTTP Status Code: 400

 **UnknownOperationException**   <a name="CommonErrors-UnknownOperationException"></a>
The action or operation isn't recognized. Verify that the action name is spelled correctly and that it's supported by the API version you're using.  
HTTP Status Code: 404

 **UnrecognizedClientException**   <a name="CommonErrors-UnrecognizedClientException"></a>
The X.509 certificate or AWS access key ID you provided doesn't exist in our records. Verify that you're using valid credentials and that they haven't expired.  
HTTP Status Code: 403

 **ValidationError**   <a name="CommonErrors-ValidationError"></a>
The input doesn't meet the required format or constraints. Check that all required parameters are included and that values are valid.  
HTTP Status Code: 400