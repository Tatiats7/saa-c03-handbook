# AWS Wavelength Developer Guide

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
+ [What is AWS Wavelength?](#what-is-wavelength)
   + [Use cases for AWS Wavelength](#wavelength-use-cases)
+ [How AWS Wavelength works](#how-wavelengths-work)
+ [Get started with AWS Wavelength](#get-started-wavelength)
+ [Carrier gateway for AWS Wavelength](#carrier-gateways)
+ [Multi-access AWS Wavelength](#multi-access)
+ [Architect apps for Wavelength](#architecture)
+ [Available Wavelength Zones](#available-wavelength-zones)
   + [Find your AWS Wavelength Zones](#wavelength-zones-describe)
+ [Quotas and considerations for Wavelength Zones](#wavelength-quotas)
+ [Security in AWS Wavelength](#security)
   + [Resilience in AWS Wavelength](#disaster-recovery-resiliency)
   + [Compliance validation for AWS Wavelength](#compliance-validation)
+ [Document history for AWS Wavelength Developer Guide](#doc-history)

-----



# What is AWS Wavelength?
<a name="what-is-wavelength"></a>

*AWS Wavelength* enables developers to build applications that require edge computing infrastructure to deliver low latency to mobile devices and end users or increase the resiliency of their existing edge applications. Wavelength deploys standard AWS compute and storage services to the edge of communications service providers' (CSP) networks. You can extend a virtual private cloud (VPC) to one or more Wavelength Zones. You can then use AWS resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances to run the applications that require low latency or edge resiliency within the Wavelength Zone, while seamlessly communicating back to your existing AWS services deployed in the parent [AWS Region](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html).

For more information, see [AWS Wavelength](https://aws.amazon.com/wavelength/).

## Wavelength concepts
<a name="concepts"></a>

The following are the key concepts:
+ **Wavelength** — A new type of AWS infrastructure designed to run workloads that require low latency or edge resiliency.
+ **Wavelength Zone** — A zone in the carrier location where the Wavelength infrastructure is deployed. Wavelength Zones are associated with an AWS Region. A Wavelength Zone is a logical extension of the Region, and is managed by the control plane in the Region. 
+ **VPC** — A customer virtual private cloud (VPC) that spans Availability Zones, Local Zones, and Wavelength Zones, and has deployed resources such as Amazon EC2 instances in the subnets that are associated with the zones.
+ **Wavelength subnet** — A subnet that you create in a Wavelength Zone. You can create one or more subnets, and then run and manage AWS services, such as Amazon EC2 instances, in the subnet.
+ **Carrier gateway** — A carrier gateway serves two purposes. It allows inbound traffic from a carrier network in a specific location, and allows outbound traffic to the carrier network and internet.
+ **Network Border Group** — A unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses.
+ **Wavelength application** — An application that you run on an AWS resource in a Wavelength Zone.

## AWS resources on Wavelength
<a name="services"></a>

You can create Amazon EC2 instances, Amazon EBS volumes, and Amazon VPC subnets and carrier gateways in Wavelength Zones. You can also use the following:
+ Amazon EC2 Auto Scaling
+ Amazon EKS clusters
+ Amazon ECS clusters
+ Amazon EC2 Systems Manager
+ Amazon CloudWatch
+ AWS CloudTrail
+ CloudFormation
+ Application Load Balancer in select Wavelength Zones. For a list of these Zones, see [Load balancing](https://docs.aws.amazon.com/wavelength/latest/developerguide/architecture.html#architecture-load-balancing).

The services in Wavelength are part of a VPC that is connected over a reliable connection to an AWS Region for easy access to services running in Regional subnets.

## Working with Wavelength
<a name="wavelength-interfaces"></a>

You can create, access, and manage your EC2 resources, Wavelength Zones, and carrier gateways using any of the following interfaces:
+ **AWS Management Console**— Provides a web interface that you can use to access your Wavelength resources.
+ **AWS Command Line Interface (AWS CLI)** — Provides commands for a broad set of AWS services, including Amazon VPC, and is supported on Windows, macOS, and Linux. The services you use in Wavelength continue to use their own namespace, for example Amazon EC2 uses the "ec2" namespace, and Amazon EBS uses the "ebs" namespace. For more information, see [AWS Command Line Interface](https://aws.amazon.com/cli/).
+ **AWS SDKs** — Provides language-specific APIs and takes care of many of the connection details, such as calculating signatures, handling request retries, and handling errors. For more information, see [AWS SDKs](http://aws.amazon.com/tools/#SDKs).

When you use any of the interfaces for your Wavelength Zones, use the parent Region.

## Pricing
<a name="pricing"></a>

For more information, see [AWS Wavelength Pricing](https://aws.amazon.com/wavelength/pricing/).

## Use cases for AWS Wavelength
<a name="wavelength-use-cases"></a>

Using AWS Wavelength Zones can help you accomplish a variety of goals. This section lists a few to give you an idea of the possibilities.

**Topics**
+ [Online betting and regulated industries](#wavelength-betting)
+ [Media and entertainment](#wavelength-media)
+ [Healthcare](#wavelength-healthcare)
+ [Augmented reality (AR) and virtual reality (VR)](#wavelength-virtual-reality)
+ [Connected vehicles](#wavelength-connected-vehicles)
+ [Smart factories](#wavelength-smart-factories)
+ [Real-time gaming](#wavelength-gaming)

### Online betting and regulated industries
<a name="wavelength-betting"></a>

AWS Wavelength provides edge resiliency to help address data residency requirements for regulated industries, such as online sports betting. Using a combination of AWS Wavelength alongside existing AWS hybrid and edge services such as AWS Outposts or AWS Local Zones, you can create highly-available architectures within state or country borders.

### Media and entertainment
<a name="wavelength-media"></a>

Wavelength provides the low latency needed to live stream high-resolution video and high-fidelity audio, and to embed interactive experiences into live video streams. Real-time video analytics provide the ability to generate real-time statistics that enhance the live event experience.

### Healthcare
<a name="wavelength-healthcare"></a>

Using AWS Wavelength, medical training providers can offer mobile games, medical simulations for rare disease diagnosis, advanced endoscopic maneuvers, ultrasound equipment and much more. Using AWS Wavelength to host the remote rendering engine, doctors can experience an immersive training experience without procuring the often-required expensive equipment to do so.

### Augmented reality (AR) and virtual reality (VR)
<a name="wavelength-virtual-reality"></a>

By accessing compute resources on AWS Wavelength, AR/VR applications can reduce the Motion to Photon (MTP) latencies to the benchmark that is needed to offer a realistic customer experience. When you use AWS Wavelength, you can offer AR/VR in locations where it is not possible to run local system servers.

### Connected vehicles
<a name="wavelength-connected-vehicles"></a>

Cellular Vehicle-to-Everything (C-V2X) is an increasingly important platform for enabling functionality such as intelligent driving, real-time HD maps, and increased road safety. Low latency access to the compute infrastructure that's needed to run data processing and analytics on AWS Wavelength enables real-time monitoring of data from sensors on the vehicle. This allows for secure connectivity, in-car telematics, and autonomous driving.

### Smart factories
<a name="wavelength-smart-factories"></a>

Industrial automation applications use ML inference at the edge to analyze images and videos to detect quality issues on fast moving assembly lines and to trigger actions that address the issues. With AWS Wavelength, these applications can be deployed without having to use expensive, GPU-based servers on the factory floor.

### Real-time gaming
<a name="wavelength-gaming"></a>

Real-time game streaming depends on low latency to preserve the user experience. With AWS Wavelength, you can stream the most demanding games from Wavelength Zones so that they are available on end devices that have limited processing power.

# How AWS Wavelength works
<a name="how-wavelengths-work"></a>

The following diagram demonstrates how you can create a subnet that uses resources in a communications service provider (CSP) network at a specific location. For resources that must be deployed to the Wavelength Zone, first opt in to the Wavelength Zone, and then create resources in the Wavelength Zone.

![AWS Wavelength overview](https://docs.aws.amazon.com/wavelength/latest/developerguide/images/aws-wz.png)


**Topics**
+ [VPCs](#wavelength-vpc)
+ [Subnets](#wavelength-subnets)
+ [Carrier gateways](#wavelength-carrier-gateway)
+ [Carrier IP address](#provider-owned-ip)
+ [Routing](#wavelength-routing-overview)
+ [DNS](#dns)
+ [Maximum transmission unit](#mtu)

## VPCs
<a name="wavelength-vpc"></a>

After you create a VPC in a Region, create a subnet in a Wavelength Zone that is associated with the VPC. In addition to the Wavelength Zone, you can create resources in all of the Availability Zones and Local Zones that are associated with the VPC. 

You have control over the VPC networking components, such as IP address assignment, subnets, and route table creation.

VPCs that contain a subnet in a Wavelength Zone can connect to a carrier gateway. A carrier gateway allows you to connect to the following resources:
+ 4G/LTE and 5G devices on the telecommunication carrier network
+ Internet access including fixed wireless access for select Wavelength Zone partners. For more information, see [Multi-access AWS Wavelength](#multi-access).
+ Outbound traffic to public internet resources

## Subnets
<a name="wavelength-subnets"></a>

Any subnet that you create in a Wavelength Zone inherits the main VPC route table, which includes the local route. The local route enables connectivity between the subnets in the VPC, including the subnets that are in the Wavelength Zone.

AWS recommends that you configure custom route tables for your subnets in Wavelength Zones. The destinations are the same destinations as a subnet in an Availability Zone or Local Zone, with the addition of a carrier gateway. For more information, see [Routing](#wavelength-routing-overview).

## Carrier gateways
<a name="wavelength-carrier-gateway"></a>

A carrier gateway serves two purposes. It allows inbound traffic from a carrier network in a specific location, and it allows outbound traffic to the carrier network and internet. There is no inbound connection configuration from the internet to a Wavelength Zone through the carrier gateway.

A carrier gateway supports IPv4 traffic.

Carrier gateways are only available for VPCs that contain subnets in a Wavelength Zone. The carrier gateway provides connectivity between your Wavelength Zone and the telecommunication carrier, and devices on the telecommunication carrier network. The carrier gateway performs NAT of the Wavelength instances' IP addresses to the Carrier IP addresses from a pool that is assigned to the network border group. The carrier gateway NAT function is similar to how an internet gateway functions in a Region.

## Carrier IP address
<a name="provider-owned-ip"></a>

A *Carrier IP address* is the address that you assign to a network interface, which resides in a subnet in a Wavelength Zone (for example an EC2 instance). The carrier gateway uses the address for traffic from the interface to the internet or to mobile devices. The carrier gateway uses NAT to translate the address, and then sends the traffic to the destination. Traffic from the telecommunication carrier network routes through the carrier gateway.

You allocate a Carrier IP address from a network border group, which is a unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses, for example, `us-east-1-wl1-bos-wlz-1`.

## Routing
<a name="wavelength-routing-overview"></a>

You can set the carrier gateway as a destination in a route table for the following resources:
+ VPCs that contain subnets in a Wavelength Zone
+ Subnets in Wavelength Zones

Create a custom route table for the subnets in the Wavelength Zones so that the default route goes to the carrier gateway, which then sends traffic to the internet and telecommunication carrier network.

### Example: Carrier gateway routing to the public internet
<a name="example-cgw-route"></a>

Consider a scenario with the following configuration:
+ A VPC with Availability Zones and a Wavelength Zone
+ A subnet in the Wavelength Zone
+ An EC2 instance in the subnet in the Wavelength Zone
+ A Carrier IP address for the network interface associated with the EC2 instance
+ An IP address association that maps the private IP address of the EC2 instance to the Carrier IP address

![Carrier gateway access to internet](https://docs.aws.amazon.com/wavelength/latest/developerguide/images/wavelength-internet-routing.png)


You need the following entries in the Wavelength subnet route table.


| Destination | Target | Notes | 
| --- | --- | --- | 
| {{VPC CIDR}} | Local | This route allows for intra-VPC connectivity, including subnets in the Availability Zones. | 
| 0.0.0.0/0 | {{carrier-gateway-id}} | The Carrier IP address provides internet connectivity through the carrier gateway. | 

#### Carrier gateway access to the public internet
<a name="cgw-to-internet"></a>

The carrier gateway provides access to the internet from your Wavelength subnets. For information about protocol considerations, see [Networking considerations](#networking-considerations).

Traffic initiated from the EC2 instance for the internet uses the 0.0.0.0/0 route to route traffic to the carrier gateway. The carrier gateway maps the EC2 instance IP address to the Carrier IP address, and then sends the traffic to the telecommunication carrier. 

## DNS
<a name="dns"></a>

EC2 instances use EC2 DNS to resolve domain names to IP addresses. Route 53 supports DNS features, such as domain registration, and DNS routing. Both public and private hosted Wavelength Zones are supported for routing traffic to specific domains. Route 53 resolvers are hosted in the Region.

You can also use your own DNS services to resolve domain names.

## Maximum transmission unit
<a name="mtu"></a>

Generally, the maximum transmission unit (MTU) is as follows:
+ 9001 bytes between EC2 instances in the same Wavelength Zone.
+ 1500 bytes between carrier gateway and a Wavelength Zone.
+ 1500 bytes between an EC2 instance in a Wavelength Zone and an EC2 instance in the Region when the traffic uses a public IP address.
+ 1300 bytes between an EC2 instance in a Wavelength Zone and an EC2 instance in the Region when the traffic uses a private IP address.

# Get started with AWS Wavelength
<a name="get-started-wavelength"></a>

The following diagram shows the resources that you need to configure to get started using AWS Wavelength.
+ A VPC in your Region
+ A carrier gateway
+ A public subnet in an Availability Zone in your Region
+ An instance in the public subnet
+ An instance in the Wavelength Zone subnet with a Carrier IP address

![AWS Wavelength getting started overview](https://docs.aws.amazon.com/wavelength/latest/developerguide/images/wavelength-getting-started.png)


**Topics**
+ [Step 1: Opt in to Wavelength Zones](#enable-zone-group)
+ [Step 2: Configure your network](#configure-network)
+ [Step 3: Launch an instance in your Availability Zone public subnet](#instance)
+ [Step 4: Launch an instance in the Wavelength zone](#wavelength-instance)
+ [Step 5: Test the connectivity](#test-connecitivity)

## Step 1: Opt in to Wavelength Zones
<a name="enable-zone-group"></a>

Before you specify a Wavelength Zone for a resource or service, you must opt in to the zone.

**Prerequisites**
+ Some AWS resources are not available in all Regions. Make sure that you can create the resources that you need in the desired Region or Wavelength Zone before launching an instance in a specific Wavelength Zone.
+ Before you begin, review [Quotas and considerations for Wavelength Zones](#wavelength-quotas), which includes information about available Wavelength Zones, service differences, and Service Quotas. You should also speak with your mobile operator about mobile service plans and any additional requirements.

**To opt in to Wavelength Zone using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the Region selector in the navigation bar, select the Region for the Wavelength Zone.

1. On the navigation pane, choose **EC2 Dashboard**.

1. In the upper-right corner of the page, choose **Account attributes**, **Zones**.

1. Under **Wavelength Zones**, choose **Manage**.

1. Choose **Enabled**.

1. Choose **Update zone group**.

**To enable Wavelength Zones using the AWS CLI**  
Alternatively, use the AWS CLI to enable Wavelength Zones. To do so, use the [modify-availability-zone-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-availability-zone-group.html) command.

## Step 2: Configure your network
<a name="configure-network"></a>

After you opt in to the Wavelength Zone, create a VPC, a carrier gateway, and a public subnet in the Availability Zone.

**Topics**
+ [Create a VPC](#create-vpc)
+ [Create a carrier gateway and a subnet associated with the Wavelength Zone](#create-cgw)
+ [Create a public subnet in an Availability Zone](#create-public-subnet)

### Create a VPC
<a name="create-vpc"></a>

Create a VPC to extend to your Wavelength Zone.

**To create a VPC using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Choose **Create VPC**.

1. For **Resources to create**, choose **VPC only**.

1. For **Name tag**, optionally provide a name for your VPC. Doing so creates the tag `Name`=*value*.

1. For **IPv4 CIDR block**, specify an IPv4 CIDR block for the VPC. We recommend that you specify a CIDR block from the private (non-publicly routable) IP address ranges as specified in [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html); for example, `10.0.0.0/16`, or `192.168.0.0/16`.
**Note**  
You can specify a range of publicly routable IPv4 addresses. However, we currently do not support direct access to the internet from publicly routable CIDR blocks in a VPC. Windows instances cannot boot correctly if launched into a VPC with ranges from `224.0.0.0` to `255.255.255.255` (Class D and Class E IP address ranges). 

1. Choose **Create VPC**.

### Create a carrier gateway and a subnet associated with the Wavelength Zone
<a name="create-cgw"></a>

After you create a VPC, create a carrier gateway, and then select the subnets that route traffic to the carrier gateway.

When you choose to automatically route traffic from subnets to the carrier gateway, we create the following resources:
+ A carrier gateway
+ A subnet. You can optionally assign all carrier gateway tags except the `Name` tag to the subnet.
+ A network ACL with the following resources:
  + A subnet association with the subnet in the Wavelength Zone
  + Default inbound and outbound rules for your traffic.
+ A route table with the following resources:
  + A route for local traffic
  + A route that routes non-local traffic to the carrier gateway
  + An association with the subnet

**To create a carrier gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Carrier gateways**, and then choose **Create carrier gateway**.

1. (Optional) For **Name**, enter a name for the carrier gateway.

1. For **VPC**, choose the VPC.

1. Choose **Route subnet traffic to carrier gateway**, and under **Subnets to route** do the following:

   1. Under **Existing subnets in Wavelength Zone**, select the box for each Wavelength subnet to route to the carrier gateway.

   1. To create a subnet in the Wavelength Zone, choose **Add new subnet**, enter the required information, and then choose **Add new subnet**.

1. (Optional) To add a tag to the carrier gateway, choose **Add tag**, and then enter the tag key and tag value.

1. Choose **Create carrier gateway**.

### Create a public subnet in an Availability Zone
<a name="create-public-subnet"></a>

Create a subnet in an Availability Zone in the Region.

**To add a subnet**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**.

1. Choose **Create subnet**.

1. For **VPC**, choose the VPC.

1. For **Subnet name**, provide a name for the subnet. Doing so creates the tag `Name`=*value*.

1. For **Availability Zone**, chose an Availability Zone, or choose **No Preference** to have AWS choose one for you.

1. For **IPv4 CIDR block**, specify an IPv4 address range for your subnet, using CIDR notation.

1. Choose **Create subnet**.

## Step 3: Launch an instance in your Availability Zone public subnet
<a name="instance"></a>

Launch an EC2 instance in the subnet that you created in the Availability Zone. You will use this instance to test the connectivity from the Region to the Wavelength Zone.

You can launch EC2 instances in the public subnet that you created. For information about how to launch an instance using the Amazon EC2 console, see [Launch an EC2 instance using the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html) in the *Amazon EC2 User Guide*.

## Step 4: Launch an instance in the Wavelength zone
<a name="wavelength-instance"></a>

After you complete the networking configuration, launch an instance, and then allocate a Carrier IP address for the instance.

**Topics**
+ [Option 1: Auto assign a Carrier IP address](#wavelength-launch-instances)
+ [Option 2: Allocate and associate a Carrier IP address from the network border group](#wavelength-allocate-carrier-ip)

### Option 1: Auto assign a Carrier IP address
<a name="wavelength-launch-instances"></a>

AWS recommends that you use the AWS CLI because you can automatically allocate and associate the Carrier IP address with the network interface.

Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command as follows to launch an instance in the Wavelength Zone subnet.

```
aws ec2 run-instances --region {{us-east-1}} --network-interfaces "DeviceIndex=0,AssociateCarrierIpAddress=true,SubnetId={{subnet-036aa298f4EXAMPLE}}" --image-id {{ami-04125ecea1EXAMPLE}} --instance-type {{t3.medium}}
```
+ `DeviceIndex` – Specify 0 to indicate the primary network interface (eth0).
+ `SubnetId` – Specify the ID of the subnet in the Wavelength Zone.
+ `AssociateCarrierIpAddress` – Set this value to `true` to assign a Carrier IP address to the network interface.

### Option 2: Allocate and associate a Carrier IP address from the network border group
<a name="wavelength-allocate-carrier-ip"></a>

You can launch EC2 instances in the subnet that you created when you added the carrier gateway. For more information, see [Create a carrier gateway and a subnet associated with the Wavelength Zone](#create-cgw). Security groups control inbound and outbound traffic for instances in a subnet, just as they do for instances in an Availability Zone subnet. To connect to an EC2 instance in a subnet, specify a key pair when you launch the instance, just as you do for instances in an Availability Zone subnet. For information about how to launch an instance using the Amazon EC2 console, see [Launch an EC2 instance using the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html) in the *Amazon EC2 User Guide*.

**To allocate and associate a Carrier IP address**

1. Use the [allocate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-address.html) command as follows to allocate a Carrier IP address.

   ```
   aws ec2 allocate-address --region {{us-east-1}} --domain vpc --network-border-group {{us-east-1-wl1-bos-wlz-1}}
   ```

   The following is example output.

   ```
   {
       "AllocationId": "eipalloc-05807b62acEXAMPLE",
       "PublicIpv4Pool": "amazon",
       "NetworkBorderGroup": "us-east-1-wl1-bos-wlz-1",
       "Domain": "vpc",
       "CarrierIp": "155.146.10.111"
   
   }
   ```

1. Use the [associate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-address.html) command as follows to associate the Carrier IP address with the EC2 instance.

   ```
   aws ec2 associate-address --allocation-id {{eipalloc-05807b62acEXAMPLE}} --network-interface-id {{eni-1a2b3c4d}}
   ```

   The following is example output.

   ```
   {
       "AssociationId": "eipassoc-02463d08ceEXAMPLE",
   }
   ```

## Step 5: Test the connectivity
<a name="test-connecitivity"></a>

Before you test the connectivity, do the following:
+ Review [Networking considerations](#networking-considerations)
+ Configure the instance security group to allow ICMP traffic.

Test the connectivity from the instance in the Region to the Wavelength Zone instance. Depending on your operating system, use SSH or RDP to connect to the Carrier IP address of your Wavelength Zone instance. You can use a secure bastion host.

Run the ping command to the Wavelength Zone instance. In the following example, the IP address of the subnet in the Wavelength Zone is 10.0.3.112.

```
ping 10.0.3.112
Pinging 10.0.3.112
Reply from 10.0.3.112:  bytes=32 time=<1ms TTL=128
Reply from 10.0.3.112:  bytes=32 time=<1ms TTL=128
Reply from 10.0.3.112:  bytes=32 time=<1ms TTL=128

Ping statistics for 10.0.3.112
Packets:  Sent = 3,  Received = 3,  Lost = 0 (0% lost)

Approximate round trip time in milliseconds
Minimum = 0ms,  Maximum = 0ms,  Average = 0ms
```

Test the connectivity from the instance in the Wavelength Zone instance to the carrier network. Depending on your operating system, use SSH or RDP to connect to the Carrier IP address of your Wavelength Zone instance. You can use a secure bastion host.

You need a device on the carrier network in order to test the connectivity from the Wavelength Zone to the carrier network.

Run the **ping** command to an address in the carrier network. In the following example, the carrier network IP address is 198.51.100.130.

```
ping 198.51.100.130
Pinging 198.51.100.130
Reply from 198.51.100.130:  bytes=32 time=<1ms TTL=128
Reply from 198.51.100.130:  bytes=32 time=<1ms TTL=128
Reply from 198.51.100.130:  bytes=32 time=<1ms TTL=128

Ping statistics for 198.51.100.130
Packets:  Sent = 3,  Received = 3,  Lost = 0 (0% lost)

Approximate round trip time in milliseconds
Minimum = 0ms,  Maximum = 0ms,  Average = 0ms
```

# Carrier gateway for AWS Wavelength
<a name="carrier-gateways"></a>

A carrier gateway serves two purposes. It allows inbound traffic from a carrier network in a specific location, and it allows outbound traffic to the carrier network and the internet. There is generally no inbound connection configuration from the internet to a Wavelength Zone through the carrier gateway with the exception of select partners. For more information, see [Multi-access AWS Wavelength](#multi-access).

A carrier gateway supports IPv4 traffic. 

Carrier gateways are only available for VPCs that contain subnets in a Wavelength Zone. The carrier gateway provides connectivity between your Wavelength Zone and the carrier, and devices on the carrier network. The carrier gateway performs NAT of the Wavelength instances' IP addresses to the Carrier IP addresses from a pool that is assigned to the network border group. The carrier gateway NAT function is similar to how an internet gateway functions in a Region.

## Enable access to the carrier network
<a name="enabling-telecom-routing"></a>

To enable access to or from the carrier network for instances in a Wavelength subnet, you must do the following:
+ Create a VPC.
+ Create a carrier gateway and attach the carrier gateway to your VPC. When you create the carrier gateway, you can optionally choose which subnets route to the carrier gateway. When you select this option, we automatically create the resources related to carrier gateways, such as route tables and network ACLs. If you do not choose this option, then you must perform the following tasks: 
  + Select the subnets that route traffic to the carrier gateway.
  + Ensure that your subnet route tables have a route that directs traffic to the carrier gateway.
  + Ensure that instances in your subnet have a globally unique Carrier IP address.
  + Ensure that your network access control lists and security group rules allow the relevant traffic to flow to and from your instance.

## Work with carrier gateways
<a name="working-with-cgw"></a>

The following sections describe how to manually create a carrier gateway for your VPC to support inbound traffic from the carrier network (for example, mobile phones), and to support outbound traffic to the carrier network and the internet.

**Topics**
+ [Create a VPC](#Add_CGW_Create_VPC)
+ [Create a carrier gateway](#Add_CGW_create_Gateway)
+ [Create a security group to access the carrier network](#Add_CGW_Security_Groups)
+ [Allocate and associate a Carrier IP address with the instance in the Wavelength Zone subnet](#wavelength-allocate-carrier-ip)
+ [Routing to a Wavelength Zone carrier gateway](#route-tables-cgw)
+ [View the carrier gateway details](#view-cgw)
+ [Manage carrier gateway tags](#manage-cgw-tags)
+ [Delete a carrier gateway](#delete-cgw)

### Create a VPC
<a name="Add_CGW_Create_VPC"></a>

You can create an empty Wavelength VPC as follows.

**Limitation**  
You can specify a range of publicly routable IPv4 addresses. However, we do not support direct access to the internet from publicly routable CIDR blocks in a VPC. Windows instances cannot boot correctly if launched into a VPC with ranges from `224.0.0.0` to `255.255.255.255` (Class D and Class E IP address ranges).

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Your VPCs**, **Create VPC**.

1. Do the following and then choose **Create**.
   + **Name tag**: Optionally provide a name for your VPC. Doing so creates a tag with a key of `Name` and the value that you specify.
   + **IPv4 CIDR block**: Specify an IPv4 CIDR block for the VPC. We recommend that you specify a CIDR block from the private (non-publicly routable) IP address ranges as specified in [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html); for example, `10.0.0.0/16`, or `192.168.0.0/16`. 

**To create a VPC using the AWS CLI**  
Use the [create-vpc](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc.html) command.

### Create a carrier gateway
<a name="Add_CGW_create_Gateway"></a>

After you create a VPC, create a carrier gateway and then select the subnets that route traffic to the carrier gateway.

If you have not opted in to a Wavelength Zone, the Amazon Virtual Private Cloud Console prompts you to opt in. For more information, see [Manage Zones](#manage-zones).

When you choose to automatically route traffic from subnets to the carrier gateway, we create the following resources:
+ A carrier gateway
+ A subnet. You can optionally assign all carrier gateway tags that do not have a **Key** value of `Name` to the subnet.
+ A network ACL with the following resources:
  + A subnet associated with the subnet in the Wavelength Zone
  + Default inbound and outbound rules for all of your traffic.
+ A route table with the following resources:
  + A route for all local traffic
  + A route that routes all non-local traffic to the carrier gateway
  + An association with the subnet

**To create a carrier gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Carrier Gateways**, and then choose **Create carrier gateway**.

1. Optional: For **Name**, enter a name for the carrier gateway.

1. For **VPC**, choose the VPC.

1. Choose **Route subnet traffic to carrier gateway**, and under **Subnets to route** do the following.

   1. Under **Existing subnets in Wavelength Zone**, select the box for each subnet to route to the carrier gateway.

   1. To create a subnet in the Wavelength Zone, choose **Add new subnet**, specify the following information, and then choose **Add new subnet**:
      + **Name tag**: Optionally provide a name for your subnet. Doing so creates a tag with a key of `Name` and the value that you specify.
      + **VPC**: Choose the VPC.
      + **Availability Zone**: Choose the Wavelength Zone. 
      + **IPv4 CIDR block**: Specify an IPv4 CIDR block for your subnet, for example, `10.0.1.0/24`.
      + To apply the carrier gateway tags to the subnet, select **Apply same tags from this carrier gateway**.

1. (Optional) To add a tag to the carrier gateway, choose **Add tag**, and then do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

1. Choose **Create carrier gateway**.

**To create a carrier gateway using the AWS CLI**

1. Use the [create-carrier-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-carrier-gateway.html) command.

1. Add a VPC route table with the following resources:
   + A route for all VPC local traffic
   + A route that routes all non-local traffic to the carrier gateway
   + An association with the subnets in the Wavelength Zone

   For more information, see [Routing to a Wavelength Zone carrier gateway](#route-tables-cgw).

### Create a security group to access the carrier network
<a name="Add_CGW_Security_Groups"></a>

By default, a VPC security group allows all outbound traffic. You can create a new security group and add rules that allow inbound traffic from the carrier. Then, you associate the security group with instances in the subnet.

**To create a new security group and associate it with your instances**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security Groups**, and then choose **Create Security Group**.

1. To create a security group, choose **Create security group**, specify the following information, and then choose **create**:
   + **Security group name**: Enter a name for the subnet.
   + **Description**: Enter the security group description.
   + **VPC**: Choose the VPC.

1. Select the security group. The details pane displays the details for the security group, plus tabs for working with its inbound rules and outbound rules.

1. On the **Inbound Rules** tab, choose **Edit**. Choose **Add Rule**, and complete the required information. For example, select **HTTP** or **HTTPS** from the **Type** list, and enter the **Source** as `0.0.0.0/0` for IPv4 traffic, or `::/0` for IPv6 traffic. Choose **Save**.

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance, choose **Actions**, **Networking**, and then select **Change Security Groups**. 

1. Clear the check box for the currently selected security group, and then select the new one. Choose **Assign Security Groups**.

**To create a security group using the AWS CLI**  
Use the [create-security-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-security-group.html) command.

### Allocate and associate a Carrier IP address with the instance in the Wavelength Zone subnet
<a name="wavelength-allocate-carrier-ip"></a>

If you used the Amazon EC2 console to launch the instance, or you did not use the `associate-carrier-ip-address` option in the AWS CLI, then you must allocate a Carrier IP address and assign it to the instance: 

**To allocate and associate a Carrier IP address using the AWS CLI**

1. Use the [allocate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-address.html) command as follows.

   ```
   aws ec2 allocate-address --region us-east-1 --domain vpc --network-border-group us-east-1-wl1-bos-wlz-1
   ```

   The following is example output:

   ```
   {
       "AllocationId": "eipalloc-05807b62acEXAMPLE",
       "PublicIpv4Pool": "amazon",
       "NetworkBorderGroup": "us-east-1-wl1-bos-wlz-1",
       "Domain": "vpc",
       "CarrierIp": "155.146.10.111"
   
   }
   ```

1. Use the [associate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-address.html) command to associate the Carrier IP address with the EC2 instance as follows.

   ```
   aws ec2 associate-address --allocation-id eipalloc-05807b62acEXAMPLE --network-interface-id eni-1a2b3c4d
   ```

   The following is example output:

   ```
   {
       "AssociationId": "eipassoc-02463d08ceEXAMPLE",
   }
   ```

### Routing to a Wavelength Zone carrier gateway
<a name="route-tables-cgw"></a>

Subnets that are in Wavelength Zones can have an additional target type of a carrier gateway. Consider the case where you want to have the carrier gateway route traffic to route all non-VPC traffic to the carrier network. To do this, create and attach a carrier gateway to your VPC, and then add the following routes:


| Destination | Target | 
| --- | --- | 
| 0.0.0.0/0 | {{cagw-id}} | 
| ::/0 | {{cagw-id}} | 

### View the carrier gateway details
<a name="view-cgw"></a>

You can view information about your carrier gateway, including the state and the tags.

**To view the carrier gateway details**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Carrier Gateways**.

1. Select the carrier gateway and choose **Actions**, **View details**.

**To view the carrier gateway details using the AWS CLI**  
Use the [describe-carrier-gateways](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-carrier-gateways.html) command.

### Manage carrier gateway tags
<a name="manage-cgw-tags"></a>

Tags help you to identify your carrier gateways. You can add or remove tags.

**To manage the carrier gateway tags**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Carrier Gateways**.

1. Select the carrier gateway and choose **Actions**, **Manage tags**.

1. To add a tag, choose **Add tag**, and then do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

1. To remove a tag, choose **Remove** to the right of the tag’s Key and Value.

1. Choose **Save**.

**To manage the carrier gateway tags using the AWS CLI**
+ To add tags, use the [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) command.
+ To delete tags, use the [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) command.

### Delete a carrier gateway
<a name="delete-cgw"></a>

If you no longer need a carrier gateway, you can delete it. 

**Important**  
If you do not delete the route that has the carrier gateway as the **Target**, the route is a blackhole route.

**To delete a carrier gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Carrier Gateways**.

1. Select the carrier gateway and choose **Actions**, **Delete carrier gateway**.

1. In the **Delete carrier gateway** dialog box, enter **Delete**, and then choose **Delete**.

**To delete a carrier gateway using the AWS CLI**  
Use the [delete-carrier-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-carrier-gateway.html) command.

## Manage Zones
<a name="manage-zones"></a>

Before you specify a Wavelength Zone for a resource or service, you must opt in to the AWS Zone.

# Multi-access AWS Wavelength
<a name="multi-access"></a>

TCP, UDP, and ICMP traffic from the device on the carrier network to an Amazon EC2 instance in the Wavelength Zone is supported. However, when a mobile subscriber connects to an external, non-cellular network offered by the communications service provider (CSP), such as a WiFi network, traffic is denied for most partners because traffic is characterized as *internet facing*.

With the proliferation of high-speed 5G networks, CSPs now offer new connectivity solutions to residential, small-business, and enterprise customers such as Fixed Wireless Access (FWA).

The following CSP partners that offer AWS Wavelength Zones have expanded the available ingress traffic flows:


| Communication service provider | Ingress from outside the carrier network | Ingress from 4G/5G-connected device | Ingress from Fixed Wireless Access | 
| --- | --- | --- | --- | 
| Orange | Yes | Yes | Yes | 
| Verizon | No | Yes | Yes | 

# Architect apps for Wavelength
<a name="architecture"></a>

Wavelength Zones are designed for the following workloads:
+ Applications that require edge resiliency across existing AWS hybrid and edge infrastructure deployments
+ Applications that need to connect to compute with low latency
+ Applications that need to run in a certain geography due to legal or regulatory requirements
+ Applications that need consistent data rates from mobile devices to compute in a Wavelength Zone

Review [Quotas and considerations for Wavelength Zones](#wavelength-quotas), which includes information about available Wavelength Zones, service differences, and Service Quotas.

 Consider the following factors when using Wavelength Zones:
+ AWS recommends that you architect the edge applications in a hub and spoke model with the Region to provide the most scalable, resilient, and cost-effective options for components. For more information, see [Workload placement](#architecture-best-practices)
+ Services that run in Wavelength Zones have different compliance than services in an AWS Region. For more information, see [Compliance validation for AWS Wavelength](#compliance-validation).

Most Wavelength Zones have network access that is specific to a telecommunication carrier and location. Therefore, you might need to have multiple Wavelength Zones for your latency-sensitive applications to meet your latency requirements. For more information, see [Networking considerations](#networking-considerations).

## Discover the closest Wavelength Zone endpoint
<a name="discover-nearest-wavelength-zone"></a>

You can use the following procedures to have client devices discover the closest Wavelength Zone endpoint, for example an Amazon EC2 instance:
+ Register the instance with a discovery service such as AWS Cloud Map. For information about how to register an instance, see [Registering Instances](https://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html) in the *AWS Cloud Map Developer Guide*.
+ Another approach is to use multiple Wavelength Zones across your deployment and utilize adjacent Zones, powered by carrier-developed edge discovery services to route mobile traffic. For more information, see [Deploying dynamic 5G Edge Discovery architectures with AWS Wavelength](https://aws.amazon.com/blogs/industries/deploying-dynamic-5g-edge-discovery-architectures-with-aws-wavelength/).
+ Applications that run on client devices can run latency tests such as `ping` from the client to select the best endpoint that is registered in AWS Cloud Map, or can use the geolocation data from the mobile device.

## Load balancing
<a name="architecture-load-balancing"></a>

Application Load Balancer (ALB) is supported in select Wavelength Zones. Load balancers distribute your incoming traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses, within the Wavelength Zone. Key considerations include:
+ Network Load Balancer (NLB) is not supported in Wavelength Zones. To learn more, see [Enabling load-balancing of non-HTTP(s) traffic on AWS Wavelength](https://aws.amazon.com/blogs/compute/enabling-load-balancing-of-non-https-traffic-on-aws-wavelength/).
+ Cross-Zone load balancing across multiple Wavelength Zones is not supported.

ALB is available in the following Wavelength Zones:
+ All Wavelength Zones in the `us-east-1` Region.
+ All Wavelength Zones in `us-west-2` Region.
+ All Wavelength Zones in the `ap-northeast-1` Region.
+ All Wavelength Zones in the `eu-central-1` Region.

## High availability
<a name="architecture-high-availability"></a>

Follow these strategies to deploy highly available architectures at the edge.

### Deployment
<a name="w2aac15c19b5"></a>

Consider the following:
+ **Multiple Wavelength Zones within a given VPC**: using techniques highlighted in the [Discover the closest Wavelength Zone endpoint](#discover-nearest-wavelength-zone) section, you can steer traffic to the optimal Wavelength Zone based on latency or application health.
+ **Combine Wavelength Zones with other AWS hybrid and edge locations**: you can combine AWS Local Zones subnets with AWS Wavelength Zones subnets to create highly-available deployments within a given geography. For example, you can create an Atlanta AWS Local Zone subnet (`us-east-1-atl-2a`) alongside an Atlanta Wavelength Zone subnet (`us-east-1-wl1-atl-wlz-1`) within the same VPC.

### DNS resolution
<a name="w2aac15c19b7"></a>

One way to create both physical and logical redundancy across your high-availability edge deployments is to utilize the parent Region as the failover, using simple Route 53-based failover policies to steer traffic to an available endpoint. For more information, see [Configuring DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html) in the *Amazon Route 53 Developer Guide*.

## Workload placement
<a name="architecture-best-practices"></a>

Run the following components in the Region:
+ Components that are less latency sensitive
+ Components that do not require data residency
+ Components that need to be shared across Zones
+ Components that need to persist state, such as databases

Run the application components that need low latency and higher bandwidth over mobile networks in Wavelength Zones.

For optimal throughput, AWS recommends that you use a public service endpoint when applications in the Wavelength Zone need to connect to AWS services in the parent Region.

# Available Wavelength Zones
<a name="available-wavelength-zones"></a>

AWS Wavelength Zones are associated with an AWS Region and designed to run workloads that require low latency or edge resiliency. Review the locations, carriers, and other details of each available AWS Wavelength Zone.

**Topics**
+ [US East (N. Virginia) Wavelength Zones](#wavelength-zones-us-east-1)
+ [US West (Oregon) Wavelength Zones](#wavelength-zones-us-west-2)
+ [Asia Pacific (Tokyo) Wavelength Zones](#wavelength-zones-ap-northeast-1)
+ [Canada (Central) Wavelength zones](#wavelength-zones-ca-central-1)
+ [Europe (London) Wavelength Zones](#wavelength-zones-eu-west-2)
+ [Morocco (Casablanca) Wavelength Zones](#wavelength-zones-eu-west-3)
+ [Find your AWS Wavelength Zones](#wavelength-zones-describe)

The following tables list the Wavelength Zones by Region. For more information, see [AWS Wavelength Zone locations](https://aws.amazon.com/wavelength/locations/).

## US East (N. Virginia) Wavelength Zones
<a name="wavelength-zones-us-east-1"></a>


| Location | Carrier | Wavelength Zone Name | Wavelength Zone ID | 
| --- | --- | --- | --- | 
| Atlanta | Verizon | us-east-1-wl1-atl-wlz-1 | use1-wl1-atl-wlz1 | 
| Boston | Verizon | us-east-1-wl1-bos-wlz-1 | use1-wl1-bos-wlz1 | 
| Charlotte | Verizon | us-east-1-wl1-clt-wlz-1 | use1-wl1-clt-wlz1 | 
| Chicago | Verizon | us-east-1-wl1-chi-wlz-1 | use1-wl1-chi-wlz1 | 
| Dallas | Verizon | us-east-1-wl1-dfw-wlz-1 | use1-wl1-dfw-wlz1 | 
| Detroit | Verizon | us-east-1-wl1-dtw-wlz-1 | use1-wl1-dtw-wlz1 | 
| Houston | Verizon | us-east-1-wl1-iah-wlz-1 | use1-wl1-iah-wlz1 | 
| Kansas | Verizon | us-east-1-foe-wlz-1a | use1-foe1-wlz1 | 
| Miami | Verizon | us-east-1-wl1-mia-wlz-1 | use1-wl1-mia-wlz1 | 
| Minneapolis | Verizon | us-east-1-wl1-msp-wlz-1 | use1-wl1-msp-wlz1 | 
| Nashville | Verizon | us-east-1-wl1-bna-wlz-1 | use1-wl1-bna-wlz1 | 
| New York City | Verizon | us-east-1-wl1-nyc-wlz-1 | use1-wl1-nyc-wlz1 | 
| Tampa | Verizon | us-east-1-wl1-tpa-wlz-1 | use1-wl1-tpa-wlz1 | 
| Washington DC | Verizon | us-east-1-wl1-was-wlz-1 | use1-wl1-was-wlz1 | 

## US West (Oregon) Wavelength Zones
<a name="wavelength-zones-us-west-2"></a>


| Location | Carrier | Wavelength Zone Name | Wavelength Zone ID | 
| --- | --- | --- | --- | 
| Denver | Verizon | us-west-2-wl1-den-wlz-1 | usw2-wl1-den-wlz1 | 
| Las Vegas | Verizon | us-west-2-wl1-las-wlz-1 | usw2-wl1-las-wlz1 | 
| Los Angeles | Verizon | us-west-2-wl1-lax-wlz-1 | usw2-wl1-lax-wlz1 | 
| Phoenix | Verizon | us-west-2-wl1-phx-wlz-1 | usw2-wl1-phx-wlz1 | 
| San Francisco Bay area | Verizon | us-west-2-wl1-sfo-wlz-1 | us-west-2-wl1-sfo-wlz-1 | 
| Seattle | Verizon | us-west-2-wl1-sea-wlz-1 | usw2-wl1-sea-wlz1 | 

## Asia Pacific (Tokyo) Wavelength Zones
<a name="wavelength-zones-ap-northeast-1"></a>


| Location | Carrier | Wavelength Zone Name | Wavelength Zone ID | 
| --- | --- | --- | --- | 
| Osaka | KDDI | ap-northeast-1-wl1-kix-wlz-1 | apne1-wl1-kix-wlz1 | 
| Tokyo | KDDI | ap-northeast-1-wl1-nrt-wlz-1 | apne1-wl1-nrt-wlz1 | 

## Canada (Central) Wavelength zones
<a name="wavelength-zones-ca-central-1"></a>


| Location | Carrier | Wavelength Zone Name | Wavelength Zone ID | 
| --- | --- | --- | --- | 
| Toronto | Bell | ca-central-1-wl1-yto-wlz-1 | cac1-wl1-yto-wlz1 | 

## Europe (London) Wavelength Zones
<a name="wavelength-zones-eu-west-2"></a>


| Location | Carrier | Wavelength Zone Name | Wavelength Zone ID | 
| --- | --- | --- | --- | 
| Manchester | British Telecom (BT) | eu-west-2-wl2-man-wlz-1 | euw2-wl2-man-wlz1 | 

## Morocco (Casablanca) Wavelength Zones
<a name="wavelength-zones-eu-west-3"></a>


| Location | Carrier | Wavelength Zone Name | Wavelength Zone ID | 
| --- | --- | --- | --- | 
| Casablanca | Orange | eu-west-3-cmn-wlz-1a | euw3-cmn1-wlz1 | 
| Dakar | Sonatel | eu-west-3-dss-wlz-1a | euw3-dss1-wlz1 | 

## Find your AWS Wavelength Zones
<a name="wavelength-zones-describe"></a>

The number and mapping of Wavelength Zones per Region might vary between AWS accounts. The following procedures demonstrate how to find the Wavelength Zones that are available to your account.

**To find your Wavelength Zones using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar, choose the **Regions** selector and then choose the Region.

1. On the navigation pane, choose **EC2 Dashboard**.

1. In the upper-right corner of the page, choose **Account attributes**, **Zones**.

**To find your Wavelength Zones using the AWS CLI**
+ Use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command as follows to describe the Wavelength Zones within the specified Region that are enabled for your account.

  ```
  aws ec2 describe-availability-zones --region {{region-name}}
  ```
+ Use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command as follows to describe the Wavelength Zones regardless of the opt-in status.

  ```
  aws ec2 describe-availability-zones --all-availability-zones
  ```

# Quotas and considerations for Wavelength Zones
<a name="wavelength-quotas"></a>

Consider the following as you get started with AWS Wavelength.

**Topics**
+ [Networking considerations](#networking-considerations)
+ [Amazon EC2 considerations](#ec2-considerations)
+ [Amazon EBS considerations](#ebs)
+ [Amazon Elastic Kubernetes Service considerations](#eks-considerations)
+ [Amazon VPC considerations](#vpc-considerations)
+ [Service quotas for Amazon VPC](#quotas)

## Networking considerations
<a name="networking-considerations"></a>

Consider the following network information.

### Multiple Wavelength Zone considerations
<a name="multiple-wavelength-zones"></a>

EC2 instances that are in two different Wavelength Zones in the same VPC are not allowed to communicate with each other. If you need communication from one Wavelength Zone to another Wavelength Zone, we recommend that you use multiple VPCs, one for each Wavelength Zone. You can use a transit gateway to connect the VPCs. This configuration enables communication between instances in the Wavelength Zones. For information about how to configure multiple Wavelength Zones, see [Subnets in Wavelength](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-wavelength.html) in the *Amazon VPC User Guide*.

The following controls are enabled by the carrier gateway for internet flows by default and cannot be removed:


| Protocol | Between EC2 instance and the internet | Between EC2 instance and a device on the carrier network | 
| --- | --- | --- | 
| TCP | + Africa-based Wavelength Zones (parent region eu-west-3): Allowed<br />+ All other Wavelength Zones: Outbound and the response  | Allowed | 
| UDP | + Africa-based Wavelength Zones (parent region eu-west-3): Allowed<br />+ All other Wavelength Zones: Denied  | Allowed | 
| ICMP | Allowed | Allowed | 
+ TCP is allowed for outbound and response in most cases
+ UDP from the internet is denied

  UDP traffic from a device on the carrier network is allowed to route to an Amazon EC2 instance in a Wavelength Zone.
+ ICMP is allowed

In addition, inbound routing from the carrier network is optimized for devices in the location of the Wavelength Zone. For example, a Wavelength Zone in the San Francisco Bay area allows low latency access only from devices that are in that metro area and carrier network.

## Amazon EC2 considerations
<a name="ec2-considerations"></a>

Take the following information into consideration when you launch EC2 instances in Wavelength Zones:
+ You cannot use Dedicated Instances or Dedicated Hosts.
+ EC2 quotas are controlled by the quotas for the home Region.
+ The following instance types are supported:


<table>
<thead>
  <tr><th>Instance type</th><th>N. America</th><th>Europe</th><th>Asia</th><th>Africa</th></tr>
</thead>
<tbody>
  <tr><td>t3.medium</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
  <tr><td>t3.xlarge</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td></tr>
  <tr><td>r5.large</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
  <tr><td>r5.2xlarge</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
  <tr><td>m5.2xlarge</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
  <tr><td>c5.xlarge</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
  <tr><td>c5.2xlarge</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
  <tr><td>c5.4xlarge</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/negative_icon.png" alt="" /> No </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
  <tr><td>g4dn.2xlarge</td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td><td> <img src="https://docs.aws.amazon.com/wavelength/latest/developerguide/images/success_icon.png" alt="" /> Yes </td></tr>
</tbody>
</table>


## Amazon EBS considerations
<a name="ebs"></a>

Take the following information into consideration when you use Amazon Elastic Block Store for EC2 instances that are in Wavelength Zones:
+ Snapshots of EBS volumes and AMIs are stored in the AWS Region.
+ You can only use `gp2` volumes.
+ There is a limit for `gp2` storage.

  For more information see [Quotas for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html) in the *Amazon EBS User Guide*.

## Amazon Elastic Kubernetes Service considerations
<a name="eks-considerations"></a>

Take the following information into consideration when you run an Amazon EKS cluster:
+ You must run Kubernetes 1.17 or later.
+ When you create your Amazon EKS cluster, you must select an Availability Zone in the VPC, and not a Wavelength Zone.
+ When you create your Amazon EKS cluster for private subnets only, you need to add VPC endpoints for Amazon ECR and Amazon Simple Storage Service. For more information, see [Amazon VPC considerations](#vpc-considerations).
+ To create node groups in Wavelength Zones for your Amazon EKS cluster, see [Launching self-managed Amazon Linux nodes](https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html) in the *Amazon EKS User Guide*.
+ To apply the `aws-auth` ConfigMap to your Amazon EKS cluster, see [Grant IAM users access to Kubernetes with a ConfigMap](https://docs.aws.amazon.com/eks/latest/userguide/auth-configmap.html) in the *Amazon EKS User Guide*.

## Amazon VPC considerations
<a name="vpc-considerations"></a>

Take the following information into consideration when you run Amazon VPC:
+ To use VPC endpoints, you must create the endpoint in an Availability Zone in the VPC. You cannot create the endpoint in a Wavelength Zone.
+ You cannot assign IPv6 addresses to subnets that are in Wavelength Zones.

## Service quotas for Amazon VPC
<a name="quotas"></a>

Wavelength VPCs and Wavelength subnets count toward your Amazon VPC service quotas. For more information about Amazon VPC quotas, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the *Amazon VPC User Guide*.

For more information about how to view your service quotas, see [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html) in the *Service Quotas User Guide*.

# Security in AWS Wavelength
<a name="security"></a>

Security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Wavelength, see [Compliance validation for AWS Wavelength](#compliance-validation).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

This documentation describes the differences when services run in a Wavelength Zone. For detailed information about service security, see the following:


+ [Security in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html) 
+ [Security in Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/security.html)
+ [Security in Amazon ECS clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html) 
+ [Security in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/security.html) 

**Topics**
+ [Resilience](#disaster-recovery-resiliency)
+ [Compliance validation](#compliance-validation)

## Resilience in AWS Wavelength
<a name="disaster-recovery-resiliency"></a>

AWS recommends that you architect edge applications in a hub and spoke model with the Region providing the most scalable, resilient, and cost effective options for components that are less latency sensitive, that need to be shared across Zones, or that have states that need to persist. Then, use Wavelength Zones for the application components that need low latency, data residency, higher bandwidth, or increased quality of service over 5G mobile networks.

If you need to replicate your data or applications in a Wavelength Zone, AWS recommends that you use an Availability Zone in the Region that is not the parent zone as the failover zone. In the following example, the parent Availability Zone is Availability Zone A, so the resources are replicated to Availability Zone B.

![AWS Wavelength failover](https://docs.aws.amazon.com/wavelength/latest/developerguide/images/wavelength_dr.png)


To learn more about resiliency in Amazon EC2 and Amazon EC2 Auto Scaling, see the following:
+ [Resilience in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disaster-recovery-resiliency.html) in the *Amazon EC2 User Guide*
+ [Resilience in Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/disaster-recovery-resiliency.html) in the *Amazon EC2 Auto Scaling User Guide*.

For more information about AWS Regions, Availability Zones, Local Zones, and Wavelength Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

## Compliance validation for AWS Wavelength
<a name="compliance-validation"></a>

The existing compliance certifications for AWS services apply to services running entirely in an AWS Region. The services running in a Wavelength Zone require a separate evaluation for certifications. 

Under the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS is responsible for the hardware and software that run AWS services. This applies to AWS Wavelength, just as it does to an AWS Region. This includes patching the infrastructure software and configuring infrastructure devices. As a customer, you are responsible for implementing best practices for data encryption, patching the operating system and applications, identity and access management, and operating system, network, and firewall configurations.

AWS has responsibility for configuring and maintaining a network connection between the Wavelength Zone and the AWS Region. Communication sent over this connection between the Wavelength Zone and the Region is encrypted by AWS.

Third-party auditors assess the security and compliance of services in AWS Wavelength as part of multiple AWS compliance programs. 

AWS Wavelength currently supports these certifications and standards:
+ HIPAA
+ ISO (9001, 27001, 27017 and 27018)
+ SOC (1, 2, 3)
+ Payment Card Industry Data Security Standard (PCI DSS)

For information about your compliance responsibility when using Amazon EC2, see [Compliance validation for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/compliance-validation.html) in the *Amazon EC2 User Guide*. For more information about compliance, see [AWS Compliance](https://aws.amazon.com/compliance/).

# Document history for AWS Wavelength Developer Guide
<a name="doc-history"></a>

The following table describes significant updates to *AWS Wavelength Developer Guide*. In addition to the major changes listed here, we also update the documentation frequently to improve the descriptions and examples, and to address the feedback that you send to us.


| Change | Description | Release Date | 
| --- | --- | --- | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces a new Wavelength Zone in Kansas. | April 29, 2025 | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces a new Wavelength Zone in Dakar. | April 15, 2025 | 
| [New Wavelength Zone and use case update](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | Updates about ingress from outside carrier network and additional use cases, introduction of a new Wavelength zone in Casablanca, Morocco. | January 30, 2025 | 
| New and updated content | Multiple updates about multi-access, load balancing, and high availability | April 22, 2024 | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces a new Wavelength Zone in Manchester. | July 25, 2023 | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces a new Wavelength Zone in London. | November 8, 2022 | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces new Wavelength Zones in Seoul, Nashville, and Tampa. | May 25, 2022 | 
| [Wavelength Zone added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces a new Wavelength Zone in Toronto. | April 26, 2022 | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces new Wavelength Zones in Charlotte, Detroit, Los Angeles, and Minneapolis.  | January 18, 2022 | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces new Wavelength Zones in Dortmund, Berlin and Munich.  | December 8, 2021 | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces new Wavelength Zones in Houston, Phoenix and Chicago. | August 5, 2021 | 
| [Wavelength Zone added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces a new Wavelength Zone in London.  | June 16, 2021 | 
| [New certifications added](https://docs.aws.amazon.com/wavelength/latest/developerguide/compliance-validation.html) | AWS Wavelength is now ISO (9001, 27001, 27017 and 27018) and SOC (1, 2, 3) certified and compliant.  | May 26, 2021 | 
| Payment Card Industry Data Security Standard (PCI DSS)  | AWS Wavelength is now certified and compliant with the Payment Card Industry Data Security Standard (PCI DSS).  | January 19, 2021  | 
| [Wavelength Zones added](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) | This release introduces new Wavelength Zones.  | September 22, 2020 | 
| Initial release | This release introduces AWS Wavelength. | August 6, 2020 | 