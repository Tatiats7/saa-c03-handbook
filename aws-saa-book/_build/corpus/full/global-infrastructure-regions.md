# AWS Regions and Availability Zones User Guide

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
+ [AWS Regions and Availability Zones](#aws-regions-availability-zones)
+ [AWS Regions](#aws-regions)
+ [AWS Availability Zones](#aws-availability-zones)
+ [AZ IDs](#az-ids)
+ [AWS Region billing codes](#aws-region-billing-codes)
+ [Document history for AWS Regions and Availability Zones](#doc-history)

-----



# AWS Regions and Availability Zones
<a name="aws-regions-availability-zones"></a>

AWS services are hosted in multiple locations world-wide. These locations are composed of AWS Regions, Availability Zones, Local Zones, and Wavelength Zones.
+ Each [Region](#concepts-regions) is a separate geographic area.
+ [Availability Zones](#concepts-availability-zones) are isolated locations within each Region.
+ [Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/) provide you the ability to place resources, such as compute and storage, in multiple locations closer to your end users.
+ [Wavelength Zones](https://docs.aws.amazon.com/wavelength/latest/developerguide/) allow developers to build applications that deliver ultra-low latencies to 5G devices and end users. Wavelength deploys standard AWS compute and storage services to the edge of telecommunication carriers' 5G networks.

AWS operates state-of-the-art, highly available data centers. Although rare, failures can occur that affect the availability of resources that are in the same location. For example, if you host all of your EC2 instances in a single Availability Zones and that Availability Zone is affected by a failure, none of your EC2 instances would be available.

For more information, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

## Regions
<a name="concepts-regions"></a>

Each Region is designed to be isolated from the other Regions. This achieves the greatest possible fault tolerance and stability.

Most AWS services support regional resources. A regional resource is specific to the Region in which you create it. When you view your AWS resources, you must specify a Region, and then you see only the resources that are tied to that Region. You can replicate some types of resources across Regions, but we don't automatically replicate them for you.

The following diagram illustrates multiple Regions in the AWS Cloud.

![Multiple Regions in the AWS cloud.](https://docs.aws.amazon.com/global-infrastructure/latest/regions/images/regions.png)


For more information, see [Regions](#aws-regions).

## Availability Zones
<a name="concepts-availability-zones"></a>

Each Region has multiple, independent locations known as Availability Zones. The Availability Zones in a Region are connected through low-latency, high-bandwidth, highly-redundant networking, over dedicated metro fiber.

Each Availability Zone consists of one or more discrete data centers, each with redundant power, networking, and connectivity, and housed in separate facilities. Because they are physically separate, only a single Availability Zone would be affected in the unlikely event of a fire, tornado, or flooding.

Some AWS services support zonal resources. A zonal resource is specific to the Availability Zone in which you create it. It is a best practice to deploy your application in multiple Availability Zones, so that your application remains available even if one Availability Zone fails.

The following diagram illustrates multiple Availability Zones in an AWS Region.

![A Region three Availability Zones.](https://docs.aws.amazon.com/global-infrastructure/latest/regions/images/availability-zones.png)


For more information, see [Availability Zones](#aws-availability-zones).

# AWS Regions
<a name="aws-regions"></a>

When you are preparing to deploy a workload, consider which Region or Regions best meet your needs. For example, select a Region that has the AWS services and features that you need. Also, you can lower network latency when you select a Region that is close to the majority of your users.

Your account determines the Regions that are available to you.

**Account types**
+ An AWS account provides multiple Regions so that you can create AWS resources in the locations that meet your requirements. For example, you want to create resources in Europe to be closer to your European customers or to meet legal requirements.
+ An AWS GovCloud (US) account provides access to the AWS GovCloud (US-West) Region and the AWS GovCloud (US-East) Region. For more information, see [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/).
+ An Amazon AWS (China) account provides access to the Beijing and Ningxia Regions only. For more information, see [Amazon Web Services in China](https://www.amazonaws.cn/about-aws/china/).

You can't describe or access the Regions of one type of account from another. For example, you can't access the AWS GovCloud (US) Regions or the China Regions from an AWS account.

For more information about the availability of AWS services by Region for AWS accounts and AWS GovCloud (US) accounts, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

## Available AWS Regions
<a name="available-regions"></a>

The geography for a Region is the specific physical location of its infrastructure. This information can help you meet your regulatory, compliance, and operational requirements.

There are currently 34 Regions. The following table lists the Regions provided by an AWS account.


| Code | Name | AZs | Geography | Opt-in status | 
| --- | --- | --- | --- | --- | 
| us-east-1 | US East (N. Virginia) | 6 | United States of America | Not required | 
| us-east-2 | US East (Ohio) | 3 | United States of America | Not required | 
| us-west-1 | US West (N. California) | 3  † | United States of America | Not required | 
| us-west-2 | US West (Oregon) | 4 | United States of America | Not required | 
| af-south-1 | Africa (Cape Town) | 3 | South Africa | Required | 
| ap-east-1 | Asia Pacific (Hong Kong) | 3 | Hong Kong | Required | 
| ap-south-2 | Asia Pacific (Hyderabad) | 3 | India | Required | 
| ap-southeast-3 | Asia Pacific (Jakarta) | 3 | Indonesia | Required | 
| ap-southeast-5 | Asia Pacific (Malaysia) | 3 | Malaysia | Required | 
| ap-southeast-4 | Asia Pacific (Melbourne) | 3 | Australia | Required | 
| ap-south-1 | Asia Pacific (Mumbai) | 3 | India | Not required | 
| ap-southeast-6 | Asia Pacific (New Zealand) | 3 | New Zealand | Required | 
| ap-northeast-3 | Asia Pacific (Osaka) | 3 | Japan | Not required | 
| ap-northeast-2 | Asia Pacific (Seoul) | 4 | South Korea | Not required | 
| ap-southeast-1 | Asia Pacific (Singapore) | 3 | Singapore | Not required | 
| ap-southeast-2 | Asia Pacific (Sydney) | 3 | Australia | Not required | 
| ap-east-2 | Asia Pacific (Taipei) | 3 | Taiwan | Required | 
| ap-southeast-7 | Asia Pacific (Thailand) | 3 | Thailand | Required | 
| ap-northeast-1 | Asia Pacific (Tokyo) | 4 | Japan | Not required | 
| ca-central-1 | Canada (Central) | 3 | Canada | Not required | 
| ca-west-1 | Canada West (Calgary) | 3 | Canada | Required | 
| eu-central-1 | Europe (Frankfurt) | 3 | Germany | Not required | 
| eu-west-1 | Europe (Ireland) | 3 | Ireland | Not required | 
| eu-west-2 | Europe (London) | 3 | United Kingdom | Not required | 
| eu-south-1 | Europe (Milan) | 3 | Italy | Required | 
| eu-west-3 | Europe (Paris) | 3 | France | Not required | 
| eu-south-2 | Europe (Spain) | 3 | Spain | Required | 
| eu-north-1 | Europe (Stockholm) | 3 | Sweden | Not required | 
| eu-central-2 | Europe (Zurich) | 3 | Switzerland | Required | 
| il-central-1 | Israel (Tel Aviv) | 3 | Israel | Required | 
| mx-central-1 | Mexico (Central) | 3 | Mexico | Required | 
| me-south-1 | Middle East (Bahrain) | 3 | Bahrain | Required | 
| me-central-1 | Middle East (UAE) | 3 | United Arab Emirates | Required | 
| sa-east-1 | South America (São Paulo) | 3 | Brazil | Not required | 

† Newer accounts can access two Availability Zones in US West (N. California).

## Opt-in status
<a name="regions-opt-in-status"></a>

To use a Region introduced after March 20, 2019, you must enable the Region before you can access it. The earlier Regions are enabled by default, which means that you can begin creating resources immediately.

You can enable a Region in one of the following ways:

------
#### [ AWS Global View console ]

**To enable a Region**

1. Sign in to the [AWS Global View console](https://console.aws.amazon.com/awsglobalview/home#RegionsAndZones).

1. From the navigation pane, choose **Regions and Zones**.

1. From the **Regions** tab, find Region that you want to enable. You can scroll down the list or enter a term in the Search field.

1. Select the row for the Region.

1. Choose **Enable Region**.

1. On the **Enable Region** pop-up, choose **Enable Region**.

------
#### [ AWS Billing and Cost Management console ]

To enable a Region from the AWS Billing and Cost Management console, see [Enable or disable AWS Regions in your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the *AWS Account Management Reference Guide*.

------

**Regions enabled by default**
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ US West (Oregon)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Europe (Stockholm)
+ South America (São Paulo)

**Regions disabled by default**
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (New Zealand)
+ Asia Pacific (Taipei)
+ Asia Pacific (Thailand)
+ Canada West (Calgary)
+ Europe (Milan)
+ Europe (Spain)
+ Europe (Zurich)
+ Israel (Tel Aviv)
+ Mexico (Central)
+ Middle East (Bahrain)
+ Middle East (UAE)

## View Region information
<a name="regions-example-commands"></a>

You can list the Regions for your account, get the opt-in status of a Region, and get the long name of a Region.

------
#### [ Console ]

**To view Regions and their status in the console**

1. Sign in to the [AWS Global View console](https://console.aws.amazon.com/awsglobalview/home#RegionsAndZones).

1. On the **Regions** tab, the **Status** column shows whether a Region is **Enabled by default**, **Enabled**, or **Disabled**.

1. To filter the Regions by a particular status, choose the Search field, choose **Status**, and then choose a value.

------
#### [ AWS CLI ]

**To list the Regions enabled by default**  
Use the following AWS CLI [list-regions](https://docs.aws.amazon.com/cli/latest/reference/account/list-regions.html) command.

```
aws account list-regions --region-opt-status-contains ENABLED_BY_DEFAULT --query Regions[*].RegionName
```

The following is example output:

```
[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2"
]
```

**To list the Regions enabled for your account**  
Use the following AWS CLI [list-regions](https://docs.aws.amazon.com/cli/latest/reference/account/list-regions.html) command to list both Regions enabled by default and Regions enabled for your account.

```
aws account list-regions --region-opt-status-contains ENABLED_BY_DEFAULT ENABLED --query Regions[*].RegionName
```

**To get the opt-in status of a Region**  
Use the following AWS CLI [get-region-opt-status](https://docs.aws.amazon.com/cli/latest/reference/account/get-region-opt-status.html) command.

```
aws account get-region-opt-status --region-name af-south-1
```

The following is example output:

```
{
    "RegionName": "af-south-1",
    "RegionOptStatus": "DISABLED"
}
```

**To get the long name of a Region**  
Use the following AWS CLI [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command. Replace {{region-code}} with the code for the Region. You might need to modify the quotes to get the example to work with your terminal.

```
aws ssm get-parameters-by-path \
    --path /aws/service/global-infrastructure/regions/{{region-code}} \
    --query 'Parameters[?Name.contains(@,`longName`)].Value' \
    --output text
```

The following is example output where {{region-code}} is `af-south-1`:

```
Africa (Cape Town)
```

------
#### [ PowerShell ]

**To list the Regions enabled by default**  
Use the following AWS Tools for PowerShell [Get-ACCTRegionList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ACCTRegionList.html) command.

```
(Get-ACCTRegionList -RegionOptStatusContain ENABLED_BY_DEFAULT).RegionName
```

The following is example output:

```
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-south-1
ap-southeast-1
ap-southeast-2
ca-central-1
eu-central-1
eu-north-1
eu-west-1
eu-west-2
eu-west-3
sa-east-1
us-east-1
us-east-2
us-west-1
us-west-2
```

**To list the Regions enabled for your account**  
Use the following AWS Tools for PowerShell [Get-ACCTRegionList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ACCTRegionList.html) command to list both Regions enabled by default and Regions enabled for your account.

```
(Get-ACCTRegionList -RegionOptStatusContain ENABLED_BY_DEFAULT,ENABLED).RegionName
```

**To get the opt-in status of a Region**  
Use the following AWS Tools for PowerShell [Get-ACCTRegionOptStatus](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ACCTRegionOptStatus.html) command.

```
Get-ACCTRegionOptStatus -RegionName af-south-1
```

The following is example output:

```
Value
-----
DISABLED
```

**To get the long name of a Region**  
Use the following AWS Tools for PowerShell [Get-SSMParametersByPath](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMParametersByPath.html) command. Replace {{region-code}} with the code for the Region.

```
(Get-SSMParametersByPath -Path /aws/service/global-infrastructure/regions/{{region-code}} | Where-Object Name -like "*longName*").Value
```

The following is example output where {{region-code}} is `af-south-1`:

```
Africa (Cape Town)
```

------

# AWS Availability Zones
<a name="aws-availability-zones"></a>

Each Region has at least three Availability Zones. This helps you to design highly available applications on AWS.

The code for an Availability Zone is its Region code followed by a letter identifier. For example, `us-east-2a`, `us-east-2b`, and `us-east-2c` are the Availability Zones in the `us-east-2` Region.

For accounts created before November 2025, in our oldest Regions, we independently map Availability Zones to codes for each AWS account. For example, the `us-east-1a` Availability Zone for your account might not be the same physical location as it is in another account. Accounts created starting November 2025, get the same Availability Zones mapped to codes. For more information, see [Regions with independently mapped Availability Zones](#independently-mapped-azs).

Each Availability Zone has an AZ ID, which is the same physical location in every AWS account. An AZ ID consists of a Region-specific prefix, followed by `-az`, followed by a number. For example, `euw1-az1`, `euw1-az2`, and `euw1-az3` are the AZ IDs for the Availability Zones in the `eu-west-1` Region. For more information, see [AZ IDs](#az-ids).

The geography for an Availability Zone is the specific physical location of its infrastructure. This information can help you meet your regulatory, compliance, and operational requirements.

**Topics**
+ [North America](#zones-north-america)
+ [Africa](#zones-africa)
+ [Asia Pacific](#zones-asia-pacific)
+ [Europe](#zones-europe)
+ [Middle East](#zones-middle-east)
+ [South America](#zones-south-america)
+ [Constrained Availability Zones](#constrained-zones)
+ [View Availability Zone information](#zones-example-commands)

## North America
<a name="zones-north-america"></a>

The following table lists the Availability Zones in North America.


| AZ ID | Region | Geography | 
| --- | --- | --- | 
| use1-az1 | us-east-1 | Virginia, United States of America | 
| use1-az2 | us-east-1 | Virginia, United States of America | 
| use1-az3 | us-east-1 | Virginia, United States of America | 
| use1-az4 | us-east-1 | Virginia, United States of America | 
| use1-az5 | us-east-1 | Virginia, United States of America | 
| use1-az6 | us-east-1 | Virginia, United States of America | 
| Coming in 2026 | us-east-1 | Maryland, United States of America | 
| use2-az1 | us-east-2 | Ohio, United States of America | 
| use2-az2 | us-east-2 | Ohio, United States of America | 
| use2-az3 | us-east-2 | Ohio, United States of America | 
| usw1-az1 | us-west-1  † | California, United States of America | 
| usw1-az2 | us-west-1  † | California, United States of America | 
| usw1-az3 | us-west-1  † | California, United States of America | 
| usw2-az1 | us-west-2 | Oregon, United States of America | 
| usw2-az2 | us-west-2 | Oregon, United States of America | 
| usw2-az3 | us-west-2 | Oregon, United States of America | 
| usw2-az4 | us-west-2 | Oregon, United States of America | 
| cac1-az1 | ca-central-1 | Canada | 
| cac1-az2 | ca-central-1 | Canada | 
| cac1-az4 | ca-central-1 | Canada | 
| caw1-az1 | ca-west-1 | Canada | 
| caw1-az2 | ca-west-1 | Canada | 
| caw1-az3 | ca-west-1 | Canada | 
| mxc1-az1 | mx-central-1 | Mexico | 
| mxc1-az2 | mx-central-1 | Mexico | 
| mxc1-az3 | mx-central-1 | Mexico | 

† Newer accounts can access two Availability Zones in US West (N. California).

## Africa
<a name="zones-africa"></a>

The following table lists the Availability Zones in Africa.


| AZ ID | Region | Geography | 
| --- | --- | --- | 
| afs1-az1 | af-south-1 | South Africa | 
| afs1-az2 | af-south-1 | South Africa | 
| afs1-az3 | af-south-1 | South Africa | 

## Asia Pacific
<a name="zones-asia-pacific"></a>

The following table lists the Asia Pacific Availability Zones.


| AZ ID | Region | Geography | 
| --- | --- | --- | 
| ape1-az1 | ap-east-1 | Hong Kong | 
| ape1-az2 | ap-east-1 | Hong Kong | 
| ape1-az3 | ap-east-1 | Hong Kong | 
| ape2-az1 | ap-east-2 | Taiwan | 
| ape2-az2 | ap-east-2 | Taiwan | 
| ape2-az3 | ap-east-2 | Taiwan | 
| apne1-az1 | ap-northeast-1 | Japan | 
| apne1-az2 | ap-northeast-1 | Japan | 
| apne1-az3 | ap-northeast-1 | Japan | 
| apne1-az4 | ap-northeast-1 | Japan | 
| apne2-az1 | ap-northeast-2 | South Korea | 
| apne2-az2 | ap-northeast-2 | South Korea | 
| apne2-az3 | ap-northeast-2 | South Korea | 
| apne2-az4 | ap-northeast-2 | South Korea | 
| apne3-az1 | ap-northeast-3 | Japan | 
| apne3-az2 | ap-northeast-3 | Japan | 
| apne3-az3 | ap-northeast-3 | Japan | 
| aps1-az1 | ap-south-1 | India | 
| aps1-az2 | ap-south-1 | India | 
| aps1-az3 | ap-south-1 | India | 
| aps2-az1 | ap-south-2 | India | 
| aps2-az2 | ap-south-2 | India | 
| aps2-az3 | ap-south-2 | India | 
| apse1-az1 | ap-southeast-1 | Singapore | 
| apse1-az2 | ap-southeast-1 | Singapore | 
| apse1-az3 | ap-southeast-1 | Singapore | 
| apse2-az1 | ap-southeast-2 | Australia | 
| apse2-az2 | ap-southeast-2 | Australia | 
| apse2-az3 | ap-southeast-2 | Australia | 
| apse3-az1 | ap-southeast-3 | Indonesia | 
| apse3-az2 | ap-southeast-3 | Indonesia | 
| apse3-az3 | ap-southeast-3 | Indonesia | 
| apse4-az1 | ap-southeast-4 | Australia | 
| apse4-az2 | ap-southeast-4 | Australia | 
| apse4-az3 | ap-southeast-4 | Australia | 
| apse5-az1 | ap-southeast-5 | Malaysia | 
| apse5-az2 | ap-southeast-5 | Malaysia | 
| apse5-az3 | ap-southeast-5 | Malaysia | 
| apse6-az1 | ap-southeast-6 | New Zealand | 
| apse6-az2 | ap-southeast-6 | New Zealand | 
| apse6-az3 | ap-southeast-6 | New Zealand | 
| apse7-az1 | ap-southeast-7 | Thailand | 
| apse7-az2 | ap-southeast-7 | Thailand | 
| apse7-az3 | ap-southeast-7 | Thailand | 

## Europe
<a name="zones-europe"></a>

The following table lists the Availability Zones in Europe.


| AZ ID | Region | Geography | 
| --- | --- | --- | 
| euc1-az1 | eu-central-1 | Germany | 
| euc1-az2 | eu-central-1 | Germany | 
| euc1-az3 | eu-central-1 | Germany | 
| euc2-az1 | eu-central-2 | Switzerland | 
| euc2-az2 | eu-central-2 | Switzerland | 
| euc2-az3 | eu-central-2 | Switzerland | 
| eun1-az1 | eu-north-1 | Sweden | 
| eun1-az2 | eu-north-1 | Sweden | 
| eun1-az3 | eu-north-1 | Sweden | 
| eus1-az1 | eu-south-1 | Italy | 
| eus1-az2 | eu-south-1 | Italy | 
| eus1-az3 | eu-south-1 | Italy | 
| eus2-az1 | eu-south-2 | Spain | 
| eus2-az2 | eu-south-2 | Spain | 
| eus2-az3 | eu-south-2 | Spain | 
| euw1-az1 | eu-west-1 | Ireland | 
| euw1-az2 | eu-west-1 | Ireland | 
| euw1-az3 | eu-west-1 | Ireland | 
| euw2-az1 | eu-west-2 | United Kingdom | 
| euw2-az2 | eu-west-2 | United Kingdom | 
| euw2-az3 | eu-west-2 | United Kingdom | 
| euw2-az4 | eu-west-2 | United Kingdom | 
| euw3-az1 | eu-west-3 | France | 
| euw3-az2 | eu-west-3 | France | 
| euw3-az3 | eu-west-3 | France | 

## Middle East
<a name="zones-middle-east"></a>

The following table lists the Availability Zones in the Middle East.


| AZ ID | Region | Geography | 
| --- | --- | --- | 
| ilc1-az1 | il-central-1 | Israel | 
| ilc1-az2 | il-central-1 | Israel | 
| ilc1-az3 | il-central-1 | Israel | 
| mec1-az1 | me-central-1 | United Arab Emirates | 
| mec1-az2 | me-central-1 | United Arab Emirates | 
| mec1-az3 | me-central-1 | United Arab Emirates | 
| mes1-az1 | me-south-1 | Bahrain | 
| mes1-az2 | me-south-1 | Bahrain | 
| mes1-az3 | me-south-1 | Bahrain | 

## South America
<a name="zones-south-america"></a>

The following table lists the Availability Zones in South America.


| AZ ID | Region | Geography | 
| --- | --- | --- | 
| sae1-az1 | sa-east-1 | Brazil | 
| sae1-az2 | sa-east-1 | Brazil | 
| sae1-az3 | sa-east-1 | Brazil | 

## Constrained Availability Zones
<a name="constrained-zones"></a>

As Availability Zones grow over time, our ability to expand them can become constrained. If this happens, we might restrict you from creating zonal resources in a constrained Availability Zone, unless you already have resources in that Availability Zone. Eventually, we might also remove the constrained Availability Zone from the list of Availability Zones for new accounts. Therefore, your account might have a different number of available Availability Zones in a Region than another account does.

## View Availability Zone information
<a name="zones-example-commands"></a>

You can list the Availability Zones for your account and describe a single Availability Zone, including the AZ ID for each Availability Zone.

------
#### [ Console ]

**To view AZ IDs in the console**

1. Open the [AWS Global View console](https://console.aws.amazon.com/awsglobalview/home#RegionsAndZones).

1. On the **Regions** tab, select a Region, and then choose **View details**.

1. On the **Zones** tab, find the rows with a **Zone type** of **Availability zone**. The **Zone ID** column shows the AZ ID for each Availability Zone.

------
#### [ AWS CLI ]

**To list the Availability Zones in a Region**  
Use the following [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command. To include any Local Zones and Wavelength Zones that are opted in for your account, omit the `--filters` option.

```
aws ec2 describe-availability-zones \
  --filters Name=zone-type,Values=availability-zone \
  --region {{us-east-2}} \
  --query "AvailabilityZones[].{ZoneName:ZoneName,ZoneId:ZoneId}"
```

The following is example output for the US East (Ohio) Region.

```
[
    {
        "ZoneName": "us-east-2a",
        "ZoneId": "use2-az1"
    },
    {
        "ZoneName": "us-east-2b",
        "ZoneId": "use2-az2"
    },
    {
        "ZoneName": "us-east-2c",
        "ZoneId": "use2-az3"
    }
]
```

**To describe an Availability Zone**  
To view the details of a single Availability Zone, use the following [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command.

```
aws ec2 describe-availability-zones \
  --zone-name {{us-east-2a}} \
  --region {{us-east-2}}
```

The following is example output for `us-east-2a` in the US East (Ohio) Region.

```
{
    "AvailabilityZones": [
        {
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "us-east-2",
            "ZoneName": "us-east-2a",
            "ZoneId": "use2-az1",
            "GroupName": "us-east-2-zg-1",
            "NetworkBorderGroup": "us-east-2",
            "ZoneType": "availability-zone",
            "GroupLongName": "US East (Ohio) 1",
            "Geography": [
                {
                    "Name": "United States of America"
                }
            ],
            "SubGeography": [
                {
                    "Name": "Ohio"
                }
            ],
            "State": "available"
        }
    ]
}
```

------
#### [ PowerShell ]

**To list the Availability Zones in a Region**  
Use the following [Get-EC2AvailabilityZone](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2AvailabilityZone.html) command. To include any Local Zones and Wavelength Zones that are opted in for your account, omit the `-Filter` parameter.

```
Get-EC2AvailabilityZone `
    -Filter @{Name="zone-type";Values="availability-zone"} `
    -Region {{us-east-2}} |
Select-Object ZoneName, ZoneId
```

The following is example output for the US East (Ohio) Region.

```
ZoneName   ZoneId
--------   ------
us-east-2a use2-az1
us-east-2b use2-az2
us-east-2c use2-az3
```

**To describe an Availability Zone**  
To view the details of a single Availability Zone, use the following [Get-EC2AvailabilityZone](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2AvailabilityZone.html) command.

```
Get-EC2AvailabilityZone -ZoneName {{us-east-2a}} -Region {{us-east-2}}
```

The following is example output for `us-east-2a` in the US East (Ohio) Region.

```
Geography          : {United States of America}
GroupLongName      : US East (Ohio) 1
GroupName          : us-east-2-zg-1
Messages           :
NetworkBorderGroup : us-east-2
OptInStatus        : opt-in-not-required
ParentZoneId       :
ParentZoneName     :
RegionName         : us-east-2
State              : available
SubGeography       : {Ohio}
ZoneId             : use2-az1
ZoneName           : us-east-2a
ZoneType           : availability-zone
```

------

# AZ IDs
<a name="az-ids"></a>

Originally, we decided to independently map Availability Zones to codes in each AWS account. This ensures that resources are distributed across the Availability Zones for these Regions, even if most customers chose the first Availability Zone in the Region. For example, the `us-east-1a` for your AWS account might not be the same physical location as the `us-east-1a` for another AWS account. As AWS learned more about customer usage patterns, and as AWS evolved, we determined that it was not necessary to continue to independently map Availability Zones to codes. All Regions introduced after November 2012 use a uniform mapping of Availability Zones to codes.

To coordinate Availability Zones across accounts in all Regions, even those that independently map Availability Zones, use the *AZ IDs*, which are unique and consistent identifiers for Availability Zones. For example, `use1-az1` is an AZ ID for the `us-east-1` Region, and it has the same physical location in every AWS account. You can view the AZ IDs for your account to determine the physical location of your resources relative to the resources in another account. For example, if you share a subnet in the Availability Zone with the AZ ID `use1-az2` with another account, this subnet is available to that account in the Availability Zone whose AZ ID is also `use1-az2`.

To view the AZ IDs for your account, check the **Service health** panel on the [EC2 Dashboard](https://console.aws.amazon.com/ec2/) or use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) AWS CLI command.

The following diagram illustrates two accounts with different mappings of Availability Zone code to AZ ID.

![Two accounts with different mappings of Availability Zone code to AZ ID.](https://docs.aws.amazon.com/global-infrastructure/latest/regions/images/availability-zone-mapping.png)


## Regions with independently mapped Availability Zones
<a name="independently-mapped-azs"></a>

In the following Regions, for accounts created before November 2025, we independently map Availability Zones to codes for each AWS account. Accounts created starting November 2025, get the same Availability Zones mapped to codes. All other Regions use a uniform mapping.
+ US East (N. Virginia)
+ US West (N. California)
+ US West (Oregon)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Europe (Ireland)
+ South America (São Paulo)
+ AWS GovCloud (US-West)

## Example commands
<a name="az-ids-example-commands"></a>

The following AWS CLI commands demonstrate how to get information about the AZ IDs for your account.

**To list Availability Zone names and IDs using the CLI**  
Use the following [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command to describe the Availability Zones for the current Region. To describe the Availability Zones for a different Region, add the `--region` option.

```
aws ec2 describe-availability-zones --query "AvailabilityZones[].{Name:ZoneName,ID:ZoneId}" --output table
```

The following is example output for US East (Ohio).

```
----------------------------
| DescribeAvailabilityZones|
+-----------+--------------+
|    ID     |    Name      |
+-----------+--------------+
|  use2-az1 |  us-east-2a  |
|  use2-az2 |  us-east-2b  |
|  use2-az3 |  us-east-2c  |
+-----------+--------------+
```

**To get the AZ ID using instance metadata**  
You can use [instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) to get the AZ ID of the Availability Zone in which an instance is launched.

------
#### [ IMDSv2 ]

```
[ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone-id
```

------
#### [ IMDSv1 ]

```
[ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/placement/availability-zone-id
```

------

# AWS Region billing codes
<a name="aws-region-billing-codes"></a>

AWS billing and usage reports often use abbreviations for Region codes. For example, the `line_item_usage_type` value `APE1-USE1-AWS-In-Bytes` shows the short codes for the Asia Pacific (Hong Kong) and US East (N. Virginia) Regions.

## North America
<a name="billing-codes-north-america"></a>


| Region short code | Code | Region | 
| --- | --- | --- | 
| USE1 | us-east-1 | US East (N. Virginia) | 
| USE2 | us-east-2 | US East (Ohio) | 
| USW1 | us-west-1 | US West (N. California) | 
| USW2 | us-west-2 | US West (Oregon) | 
| CAN1 | ca-central-1 | Canada (Central) | 
| CAN2 | ca-west-1 | Canada West (Calgary) | 
| MXC1 | mx-central-1 | Mexico (Central) | 

## Africa
<a name="billing-codes-africa"></a>


| Region short code | Code | Region | 
| --- | --- | --- | 
| AFS1 | af-south-1 | Africa (Cape Town) | 

## Asia Pacific
<a name="billing-codes-asia-pacific"></a>


| Region short code | Code | Region | 
| --- | --- | --- | 
| APE1 | ap-east-1 | Asia Pacific (Hong Kong) | 
| APE2 | ap-east-2 | Asia Pacific (Taipei) | 
| APN1 | ap-northeast-1 | Asia Pacific (Tokyo) | 
| APN2 | ap-northeast-2 | Asia Pacific (Seoul) | 
| APN3 | ap-northeast-3 | Asia Pacific (Osaka) | 
| APS1 | ap-southeast-1 | Asia Pacific (Singapore) | 
| APS2 | ap-southeast-2 | Asia Pacific (Sydney) | 
| APS3 | ap-south-1 | Asia Pacific (Mumbai) | 
| APS4 | ap-southeast-3 | Asia Pacific (Jakarta) | 
| APS5 | ap-south-2 | Asia Pacific (Hyderabad) | 
| APS6 | ap-southeast-4 | Asia Pacific (Melbourne) | 
| APS7 | ap-southeast-5 | Asia Pacific (Malaysia) | 
| APS8 | ap-southeast-6 | Asia Pacific (New Zealand) | 
| APS9 | ap-southeast-7 | Asia Pacific (Thailand) | 

## Europe
<a name="billing-codes-europe"></a>


| Region short code | Code | Region | 
| --- | --- | --- | 
| EU | eu-west-1 | Europe (Ireland) | 
| EUC1 | eu-central-1 | Europe (Frankfurt) | 
| EUC2 | eu-central-2 | Europe (Zurich) | 
| EUW2 | eu-west-2 | Europe (London) | 
| EUW3 | eu-west-3 | Europe (Paris) | 
| EUN1 | eu-north-1 | Europe (Stockholm) | 
| EUS1 | eu-south-1 | Europe (Milan) | 
| EUS2 | eu-south-2 | Europe (Spain) | 

## Middle East
<a name="billing-codes-middle-east"></a>


| Region short code | Code | Region | 
| --- | --- | --- | 
| ILC1 | il-central-1 | Israel (Tel Aviv) | 
| MEC1 | me-central-1 | Middle East (UAE) | 
| MES1 | me-south-1 | Middle East (Bahrain) | 

## South America
<a name="billing-codes-south-america"></a>


| Region short code | Code | Region | 
| --- | --- | --- | 
| SAE1 | sa-east-1 | South America (São Paulo) | 

# Document history for AWS Regions and Availability Zones
<a name="doc-history"></a>

The following table describes the documentation releases for Regions and Zones.

| Change | Description | Date | 
| --- |--- |--- |
| [Asia Pacific (New Zealand)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-new-zealand-region/) | Launched the Asia Pacific (New Zealand) Region (`ap-southeast-6`). | September 2, 2025 | 
| [Asia Pacific (Taipei)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-taipei-region/) | Launched the Asia Pacific (Taipei) Region (`ap-east-2`). | June 6, 2025 | 
| [Geography](#doc-history) | The geography of a Region is the specific physical location of its infrastructure. This information can help you meet your regularly, compliance, and operational requirements. | March 25, 2025 | 
| [Mexico (Central)](https://aws.amazon.com/blogs/aws/now-open-aws-mexico-central-region/) | Launched the Mexico (Central) Region (`mx-central-1`). | January 14, 2025 | 
| [Asia Pacific (Thailand)](https://aws.amazon.com/blogs/aws/announcing-the-new-aws-asia-pacific-thailand-region/) | Launched the Asia Pacific (Thailand) Region (`ap-southeast-7`). | January 7, 2025 | 
| [Asia Pacific (Malaysia)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-malaysia-region/) | Launched the Asia Pacific (Malaysia) Region (`ap-southeast-5`). | August 21, 2024 | 
| [Canada West (Calgary)](https://aws.amazon.com/blogs/aws/the-aws-canada-west-calgary-region-is-now-available/) | Launched the Canada West (Calgary) Region (`ca-west-1`). | December 20, 2023 | 
| [Israel (Tel Aviv)](https://aws.amazon.com/blogs/aws/now-open-aws-israel-tel-aviv-region/) | Launched the Israel (Tel Aviv) Region (`il-central-1`). | August 1, 2023 | 
| [Asia Pacific (Melbourne)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-melbourne-region-in-australia/) | Launched the Asia Pacific (Melbourne) Region (`ap-southeast-4`). | January 23, 2023 | 
| [Asia Pacific (Hyderabad)](https://aws.amazon.com/blogs/aws/now-open-the-30th-aws-region-asia-pacific-hyderabad-region-in-india/) | Launched the Asia Pacific (Hyderabad) Region (`ap-south-2`). | November 22, 2022 | 
| [Europe (Spain)](https://aws.amazon.com/blogs/aws/now-open-aws-region-in-spain/) | Launched the Europe (Spain) Region (`eu-south-2`). | November 15, 2022 | 
| [Europe (Zurich)](https://aws.amazon.com/blogs/aws/a-new-aws-region-opens-in-switzerland/) | Launched the Europe (Zurich) Region (`eu-central-2`). | November 8, 2022 | 
| [Middle East (UAE)](https://aws.amazon.com/blogs/aws/now-open-aws-region-in-the-united-arab-emirates-uae/) | Launched the Middle East (UAE) Region (`me-central-1`). | August 29, 2022 | 
| [Asia Pacific (Jakarta)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-jakarta-region/) | Launched the Asia Pacific (Jakarta) Region (`ap-southeast-3`). | December 13, 2021 | 
| [Europe (Milan)](https://aws.amazon.com/blogs/aws/now-open-aws-europe-milan-region/) | Launched the Europe (Milan) Region (`eu-south-1`). | April 27, 2020 | 
| [Africa (Cape Town)](https://aws.amazon.com/blogs/aws/now-open-aws-africa-cape-town-region/) | Launched the Africa (Cape Town) Region (`af-south-1`). | April 22, 2020 | 
| [Middle East (Bahrain)](https://aws.amazon.com/blogs/aws/now-open-aws-middle-east-bahrain/) | Launched the Middle East (Bahrain) Region (`me-south-1`). | July 30, 2019 | 
| [Asia Pacific (Hong Kong)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-hong-kong-region/) | Launched the Asia Pacific (Hong Kong) Region (`ap-east-1`). | April 25, 2019 | 
| [Europe (Stockholm)](https://aws.amazon.com/blogs/aws/now-open-aws-europe-stockholm-region/) | Launched the Europe (Stockholm) Region (`eu-north-1`). | December 12, 2018 | 
| [AZ IDs](#doc-history) | An AZ ID is the unique and consistent identifier for an Availability Zone. Use AZ IDs to determine the physical location of your resources relative to resources in another account. | November 27, 2018 | 
| [Asia Pacific (Osaka)](#doc-history) | Launched the Asia Pacific (Osaka) Region (`ap-northeast-3`) as a local Region. It became a generally available Region on March 1, 2021. | February 12, 2018 | 
| [Europe (Paris)](https://aws.amazon.com/blogs/aws/now-open-aws-eu-paris-region/) | Launched the Europe (Paris) Region (`eu-west-3`). | December 18, 2017 | 
| [Europe (London)](https://aws.amazon.com/blogs/publicsector/aws-europe-london-region-now-open/) | Launched the Europe (London) Region (`eu-west-2`). | December 14, 2016 | 
| [Canada (Central)](https://aws.amazon.com/blogs/aws/now-open-aws-canada-central-region/) | Launched the Canada (Central) Region (`ca-central-1`). | December 8, 2016 | 
| [US East (Ohio)](https://aws.amazon.com/about-aws/whats-new/2016/10/announcing-the-aws-us-east-ohio-region/) | Launched the US East (Ohio) Region (`us-east-2`). | October 17, 2016 | 
| [Asia Pacific (Mumbai)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-mumbai-region/) | Launched the Asia Pacific (Mumbai) Region (`ap-south-1`). | June 27, 2016 | 
| [Asia Pacific (Seoul)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-seoul-region/) | Launched the Asia Pacific (Seoul) Region (`ap-northeast-2`). | January 6, 2016 | 
| [Europe (Frankfurt)](https://aws.amazon.com/about-aws/whats-new/2014/10/23/announcing-the-aws-eu-frankfurt-region/) | Launched the Europe (Frankfurt) Region (`eu-central-1`). | October 23, 2014 | 
| [Asia Pacific (Sydney)](https://aws.amazon.com/about-aws/whats-new/2012/11/12/announcing-the-aws-asia-pacific-sydney-region/) | Launched the Asia Pacific (Sydney) Region (`ap-southeast-2`). | November 12, 2012 | 
| [South America (São Paulo)](https://aws.amazon.com/about-aws/whats-new/2011/12/14/announcing-the-south-america-sao-paulo-region/) | Launched the South America (São Paulo) Region (`sa-east-1`). | December 14, 2011 | 
| [US West (Oregon)](https://aws.amazon.com/blogs/aws/now-open-us-west-portland-region/) | Launched the US West (Oregon) Region (`us-west-2`). | November 9, 2011 | 
| [Asia Pacific (Tokyo)](https://aws.amazon.com/about-aws/whats-new/2011/03/02/announcing-asia-pacific-tokyo-region/) | Launched the Asia Pacific (Tokyo) Region (`ap-northeast-1`). | March 2, 2011 | 
| [Asia Pacific (Singapore)](https://aws.amazon.com/about-aws/whats-new/2010/04/29/announcing-asia-pacific-singapore-region/) | Launched the Asia Pacific (Singapore) Region (`ap-southeast-1`). | April 29, 2010 | 
| [US West (N. California)](https://aws.amazon.com/about-aws/whats-new/2009/12/03/aws-launches-the-northern-california-region/) | Launched the US West (N. California) Region (`us-west-1`). | December 3, 2009 | 
| [Europe (Ireland)](https://aws.amazon.com/about-aws/whats-new/2008/12/10/amazon-ec2-crosses-the-atlantic/) | Launched the Europe (Ireland) Region (`eu-west-1`). | December 10, 2008 | 
| [US East (N. Virginia)](#doc-history) | Launched the US East (N. Virginia) Region (`us-east-1`). | August 25, 2006 | 