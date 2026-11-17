# AWS Direct Connect User Guide

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
+ [What is Direct Connect?](#Welcome)
   + [Access to AWS Regions](#remote_regions)
   + [Direct Connect routing policies and BGP communities](#routing-and-bgp)
      + [Direct Connect private virtual interface routing example](#private-transit-vif-example)
+ [Direct Connect connection options](#connection_options)
   + [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit)
      + [Configure Direct Connect for maximum resiliency with the AWS Direct Connect Resiliency Toolkit](#max-resiliency-set-up)
      + [Configure Direct Connect for high resiliency with the AWS Direct Connect Resiliency Toolkit](#high-resiliency-set-up)
      + [Configure AWS Direct Connect for development and test resiliency with the AWS Direct Connect Resiliency Toolkit](#devtest-resiliency-set-up)
      + [Direct Connect Failover Test](#resiliency_failover)
         + [Start an AWS Direct Connect Resiliency Toolkit virtual interface failover test](#start_failover_test)
         + [View AWS Direct Connect Resiliency Toolkit virtual interface failover test history](#view_failover_test)
         + [Stop an AWS Direct Connect Resiliency Toolkit virtual interface failover test](#stop_failover_test)
   + [Direct Connect Classic connection](#classic_connection)
      + [Configure a Direct Connect Classic connection](#toolkit-classic)
+ [Direct Connect maintenance](#dx-maintenance)
+ [MAC Security in Direct Connect](#MACsec)
   + [Get started using MACsec on a dedicated Direct Connect connection](#create-macsec-dedicated)
+ [Direct Connect dedicated and hosted connections](#WorkingWithConnections)
   + [Dedicated Direct Connect connections](#dedicated_connection)
      + [Create a Direct Connect dedicated connection using the Connection wizard](#create-connection)
      + [Download the Direct Connect LOA-CFA](#download-loa-cfa)
      + [Associate a MACsec CKN/CAK with a Direct Connect connection](#associate-key-connection)
      + [Remove the association between a MACsec secret key and a Direct Connect connection](#disassociate-key-connection)
   + [Hosted Direct Connect connections](#hosted_connection)
      + [Accept a Direct Connect hosted connection](#accept-hosted-connection)
   + [Delete a Direct Connect connection](#deleteconnection)
   + [Update a Direct Connect connection](#updateconnection)
   + [View Direct Connect connection details](#viewdetails)
+ [Flat-rate billing for dedicated connections](#flat-rate-connections)
+ [Requesting cross connects at Direct Connect locations](#Colocation)
+ [Direct Connect virtual interfaces and hosted virtual interfaces](#WorkingWithVirtualInterfaces)
   + [Direct Connect virtual interfaces](#create-vif)
      + [Create a Direct Connect public virtual interface](#create-public-vif)
      + [Create a Direct Connect private virtual interface](#create-private-vif)
      + [Create a transit virtual interface to the Direct Connect gateway](#create-transit-vif-dx)
      + [Download the Direct Connect router configuration file](#vif-router-config)
   + [Virtual interface Rate Limiters](#vif-rate-limiters)
   + [Hosted Direct Connect virtual interfaces](#hosted-vif)
      + [Create a hosted private virtual interface in Direct Connect](#create-hosted-private-vif)
      + [Create a hosted public virtual interface in Direct Connect](#create-hosted-public-vif)
      + [Create a Direct Connect hosted transit virtual interface](#create-hosted-transit-vif)
   + [View Direct Connect virtual interface details](#viewvifdetails)
   + [BGP-specific settings](#bgp-specific-settings)
   + [Long ASN support in Direct Connect](#long-asn-support)
   + [Add a BGP peer to a Direct Connect virtual interface](#add-peer-to-vif)
   + [Delete a Direct Connect virtual interface BGP peer](#delete-bgp-peer-vif)
   + [Set the MTU of a Direct Connect private virtual interface](#interface-set-mtu)
   + [Add or remove Direct Connect virtual interface tags](#modify-tags-vif)
   + [Delete a Direct Connect virtual interface](#deletevif)
   + [Accept a hosted Direct Connect virtual interface](#accepthostedvirtualinterface)
   + [Migrate a Direct Connect virtual interface](#migratevirtualinterface)
+ [Inbound prefix controls for Direct Connect](#prefix-controls)
+ [Managing prefix allocations for Direct Connect virtual interfaces](#prefix-allocations)
+ [Direct Connect link aggregation groups (LAGs)](#lags)
   + [Create a LAG at a Direct Connect endpoint](#create-lag)
   + [View LAG details at a Direct Connect endpoint](#view-lag)
   + [Update a LAG at a Direct Connect endpoint](#update-lag)
   + [Associate a connection with a LAG at a Direct Connect endpoint](#associate-connection-with-lag)
   + [Disassociate a connection from a LAG at a Direct Connect endpoint](#disassociate-connection-from-lag)
   + [Associate a MACsec CKN/CAK with a Direct Connect endpoint LAG](#associate-key-lag)
   + [Remove the association between a MACsec secret key and a Direct Connect endpoint LAG](#disassociate-key-lag)
   + [Delete a Direct Connect endpoint LAG](#delete-lag)
+ [Direct Connect gateways](#direct-connect-gateways)
   + [Direct Connect gateways](#direct-connect-gateways-intro)
      + [Create a Direct Connect gateway](#create-direct-connect-gateway)
      + [Migrate from a virtual private gateway to a Direct Connect gateway](#migrate-to-direct-connect-gateway)
      + [Delete a Direct Connect gateway](#delete-direct-connect-gateway)
   + [Direct Connect virtual private gateway associations](#virtualgateways)
      + [Create a Direct Connect virtual private gateway](#create-virtual-private-gateway)
      + [Associate or disassociate Direct Connect virtual private gateways](#associate-vgw-with-direct-connect-gateway)
      + [Create a private virtual interface to the Direct Connect gateway](#create-private-vif-for-gateway)
      + [Associate a Direct Connect virtual private gateway across accounts](#multi-account-associate-vgw)
   + [Direct Connect gateways and Transit Gateway associations](#direct-connect-transit-gateways)
      + [Associate or disassociate Direct Connect with a Transit Gateway](#associate-tgw-with-direct-connect-gateway)
      + [Create a transit virtual interface to the Direct Connect gateway](#create-transit-vif-for-gateway)
      + [Create a Transit Gateway and Direct Connect association proposal](#multi-account-tgw-create-proposal)
      + [Accept or reject a Transit Gateway and Direct Connect association proposal](#multi-account-tgw-accept-reject-proposal)
      + [Update the allowed prefixes for a transit gateway and Direct Connect association](#multi-account-tgw-update-proposal-routes)
      + [Delete a Transit Gateway and Direct Connect association proposal](#multi-account-tgw-delete-proposal)
   + [Direct Connect gateway and AWS Cloud WAN core network associations](#direct-connect-cloud-wan)
      + [Verify a Direct Connect gateway association to an AWS Cloud WAN core network](#edit-cloudwan-with-direct-connect-gateway)
   + [Allowed prefixes interactions for Direct Connect gateways](#allowed-to-prefixes)
+ [Tag AWS Direct Connect resources](#using-tags)
+ [Security in AWS Direct Connect](#security)
   + [Data protection in AWS Direct Connect](#data-protection)
      + [Internetwork traffic privacy in AWS Direct Connect](#encryption-at-rest)
      + [Encryption in AWS Direct Connect](#encryption-in-transit)
   + [Identity and Access Management for Direct Connect](#security-iam)
      + [How Direct Connect works with IAM](#security_iam_service-with-iam)
      + [Identity-based policy examples for Direct Connect](#security_iam_id-based-policy-examples)
         + [Direct Connect identity-based policy examples using tag-based conditions](#security_iam_resource-based-policy-examples)
      + [Service-linked roles for Direct Connect](#using-service-linked-roles)
      + [AWS managed policies for AWS Direct Connect](#security-iam-awsmanpol)
      + [Troubleshooting Direct Connect identity and access](#security_iam_troubleshoot)
   + [Logging and monitoring in AWS Direct Connect](#dc-incident-response)
   + [Compliance validation for AWS Direct Connect](#DirectConnect-compliance)
   + [Resilience in AWS Direct Connect](#disaster-recovery-resiliency)
   + [Infrastructure security in Direct Connect](#infrastructure-security)
+ [Use the Direct Connect CLI](#using-cli)
+ [Log Direct Connect API calls using AWS CloudTrail](#logging_dc_api_calls)
+ [Direct Connect operational event notifications](#dx-operational-notifications)
+ [Monitoring and visibility with Direct Connect](#monitoring-overview)
   + [Monitor with Amazon CloudWatch](#monitoring-cloudwatch)
      + [View Direct Connect CloudWatch metrics](#viewing-metrics)
      + [Create Amazon CloudWatch alarms to monitor Direct Connect connections](#creating-alarms)
   + [BGP route visibility](#bgp-route-visibility)
+ [Direct Connect quotas](#limits)
+ [Troubleshoot Direct Connect](#Troubleshooting)
   + [Troubleshoot layer 1 (physical) issues](#ts_layer_1)
   + [Troubleshoot layer 2 (data link) issues](#ts-layer-2)
   + [Troubleshoot layer 3/4 (Network/Transport) issues](#ts-layer-3)
   + [Troubleshoot BGP TTL security (GTSM) issues](#ts-ttl-security)
   + [Troubleshoot long ASN issues](#ts-long-asn)
   + [Troubleshoot routing issues](#ts-routing)
+ [Document history](#AboutThisGuide)

-----



# What is Direct Connect?
<a name="Welcome"></a>

Direct Connect links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router. With this connection, you can create *virtual interfaces* directly to public AWS services (for example, to Amazon S3) or to Amazon VPC, bypassing internet service providers in your network path. A Direct Connect location provides access to AWS in the Region with which it is associated. You can use a single connection in a public Region or AWS GovCloud (US) to access public AWS services in all other public Regions. 
+ For a list of Direct Connect locations and their associated Regions, see [Locations and their associated Regions](#locations-and-associated-regions).
+ For information about available port speeds at each location, see [AWS Direct Connect Locations](https://aws.amazon.com/directconnect/locations/).
+ For answers to questions about Direct Connect, see the [Direct Connect FAQ](https://aws.amazon.com/directconnect/faqs/#AWS_Transit_Gateway_support/).

The following diagram shows a high-level overview of how Direct Connect interfaces with your network. 

![Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dx-vifs.png)


**Topics**
+ [Direct Connect components](#overview-components)
+ [Network requirements](#overview_requirements)
+ [Supported Direct Connect virtual interface types](#dx-vif-types)
+ [Pricing for Direct Connect](#Paying)
+ [Access to AWS Regions](#remote_regions)
+ [Routing policies and BGP communities](#routing-and-bgp)

## Direct Connect components
<a name="overview-components"></a>

The following are the key components that you use for Direct Connect:

**Connections**  
Create a *connection* in a Direct Connect location to establish a network connection from your premises to an AWS Region. For more information, see [Direct Connect dedicated and hosted connections](#WorkingWithConnections). 

**Virtual interfaces**  
Create a *virtual interface* to enable access to AWS services. A public virtual interface enables access to public services, such as Amazon S3. A private virtual interface enables access to your VPC. The types of supported interfaces are described below in [Supported Direct Connect virtual interface types](#dx-vif-types). For more details about the supported interfaces, see [Direct Connect virtual interfaces and hosted virtual interfaces](#WorkingWithVirtualInterfaces) and [Prerequisites for virtual interfaces](#vif-prerequisites).

## Network requirements
<a name="overview_requirements"></a>

To use Direct Connect in a Direct Connect location, your network must meet one of the following conditions:
+ Your network is colocated with an existing Direct Connect location. For more information about available Direct Connect locations, see [AWS Direct Connect Product Details](https://aws.amazon.com/directconnect/details). 
+ You are working with a Direct Connect partner who is a member of the AWS Partner Network (APN). For information, see [APN Partners Supporting AWS Direct Connect](https://aws.amazon.com//directconnect/partners/).
+ You are working with an independent service provider to connect to Direct Connect.

In addition, your network must meet the following conditions:
+ Your network must use single-mode fiber with a 1000BASE-LX (1310 nm) transceiver for 1 gigabit Ethernet, a 10GBASE-LR (1310 nm) transceiver for 10 gigabit, a 100GBASE-LR4 for 100 gigabit Ethernet, or a 400GBASE-LR4 for 400 Gbps Ethernet.
+ Depending on the AWS Direct Connect endpoint serving your connection, on-premises device auto-negotiation might need to be enabled or disabled for any dedicated connection. If a virtual interface remains down when a Direct Connect connection is up, see [Troubleshoot layer 2 (data link) issues](#ts-layer-2).
+ 802.1Q VLAN encapsulation must be supported across the entire connection, including intermediate devices.
+ Your device must support Border Gateway Protocol (BGP) and BGP MD5 authentication.
+ (Optional) You can configure Bidirectional Forwarding Detection (BFD) on your network. Asynchronous BFD is automatically enabled for each Direct Connect virtual interface. It's automatically enabled for Direct Connect virtual interfaces, but does not take effect until you configure it on your router. For more information, see [Enable BFD for a Direct Connect connection](https://aws.amazon.com/premiumsupport/knowledge-center/enable-bfd-direct-connect/). 

Direct Connect supports both the IPv4 and IPv6 communication protocols. IPv6 addresses provided by public AWS services are accessible through Direct Connect public virtual interfaces.

Direct Connect supports an Ethernet frame size of 1522 or 9023 bytes (14 bytes Ethernet header \+ 4 bytes VLAN tag \+ bytes for the IP datagram \+ 4 bytes FCS) at the link layer. You can set the MTU of your private virtual interfaces. For more information, see [MTUs for private virtual interfaces or transit virtual interfaces](#set-jumbo-frames-vif).

## Supported Direct Connect virtual interface types
<a name="dx-vif-types"></a>

AWS Direct Connect supports the following three virtual interface (VIF) types:
+ **Private virtual interface**

  This type of interface is used to access an Amazon Virtual Private Cloud (VPC) using private IP addresses. With a private virtual interface you can 
  + Connect directly to a single VPC per private virtual interface to access those resources using private IPs in the same Region.
  + Connect a private virtual interface to a Direct Connect gateway to access multiple virtual private gateways across any account and AWS Region (except the AWS China Regions).
+ **Public virtual interface**

  This type of virtual interface is used to access all AWS public services using public IP addresses. With a public virtual interface you can connect to all AWS public IP addresses and services globally.
+ **Transit virtual interface**

  This type of interface is used to access one or more Amazon VPC Transit Gateways associated with Direct Connect gateways. With a transit virtual interface you connect multiple Amazon VPC Transit Gateways across multiple accounts and AWS Regions (except the AWS China Regions). 
**Note**  
There are limits to the number of different types of associations between a Direct Connect gateway and a virtual interface. For more information about specific limits, see the [Direct Connect quotas](#limits) page.

For more information about virtual interfaces, see [Direct Connect virtual interfaces and hosted virtual interfaces](#WorkingWithVirtualInterfaces).

## Pricing for Direct Connect
<a name="Paying"></a>

AWS Direct Connect has two billing elements: port hours and outbound data transfer. Port hour pricing is determined by capacity and connection type (dedicated connection or hosted connection). 

Data Transfer Out charges for private interfaces and transit virtual interfaces are allocated to the AWS account responsible for the Data Transfer. There are no additional charges to use a multi-account AWS Direct Connect gateway.

For publicly addressable AWS resources (for example, Amazon S3 buckets, Classic EC2 instances, or EC2 traffic that goes through an internet gateway), if the outbound traffic is destined for public prefixes owned by the same AWS payer account and actively advertised to AWS through a Direct Connect public virtual Interface, the Data Transfer Out (DTO) usage is metered toward the resource owner at Direct Connect data transfer rate.

For more information, see [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/).

## Access to AWS Regions
<a name="remote_regions"></a>

From any Direct Connect location in a public Region or AWS GovCloud (US), you can access all public AWS Regions (except those in China (Beijing and Ningxia)), AWS GovCloud (US) Regions, and [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/). You can use Direct Connect to build multi-Region services. All networking traffic remains on the AWS global network backbone, regardless of whether you access public AWS services or a VPC.

You connect to Regions using one of the following virtual interface types:
+ **Public virtual interface** — Provides access to public resources. After you create a public virtual interface and establish a BGP session, your router learns routes for the public AWS Regions. For more information, see [Virtual interfaces and hosted virtual interfaces](#WorkingWithVirtualInterfaces). For prefixes currently advertised by AWS, see [AWS IP Address Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the *Amazon Web Services General Reference*.
+ **Private virtual interface with a Direct Connect gateway** — Reaches VPCs in any AWS Region. For more information, see [Direct Connect gateways](#direct-connect-gateways).
+ **Private virtual interface without a Direct Connect gateway** — Reaches a VPC in the associated Region only. The VPC must have a virtual private gateway in the same Region as the connection. For more information, see [Virtual private gateway associations](#virtualgateways).
+ **Transit virtual interface with a Direct Connect gateway** — Reaches transit gateways in any AWS Region. For more information, see [Transit Gateway associations](#direct-connect-transit-gateways).

Data transferred out is billed at the rate of the source Region or Local Zone where the resource resides. For more information about data transfer pricing, see the [Pricing](http://aws.amazon.com/directconnect/pricing/) section on the AWS Direct Connect detail page.

For information about routing policies and supported BGP communities, see [Routing policies and BGP communities](#routing-and-bgp).

### Associated Region
<a name="associated-region"></a>

Each Direct Connect device is associated with a specific AWS Region. When you create a connection at a Direct Connect location, the connection inherits the associated Region of the device that it terminates on.

The associated Region determines where the connection is managed, not where your data flows. Traffic is routed based on the type of virtual interface and gateway that you create, not the associated Region. The associated Region controls:
+ **Management and configuration** — The connection and its virtual interfaces appear in the Direct Connect console and the AWS CLI in the associated Region, and you make all API operations for these resources against this Region.
+ **CloudWatch metrics** — Direct Connect publishes metrics for the connection and its virtual interfaces to Amazon CloudWatch in the associated Region.

The one exception is when you attach a private virtual interface directly to a virtual private gateway, described earlier under **Private virtual interface without a Direct Connect gateway**. In that case, the virtual private gateway must be in the same Region as the associated Region. This is the only case where the associated Region constrains which AWS resources you can reach.

**Note**  
In AWS terminology, the associated Region affects the *control plane* (management and monitoring) but not the *data plane* (the path that your traffic takes). For more information, see [Control planes and data planes](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html) in the *AWS Fault Isolation Boundaries* whitepaper.

### Locations and their associated Regions
<a name="locations-and-associated-regions"></a>

The following table lists each Direct Connect location and its associated Region.

A single Direct Connect location can host devices that are associated with different AWS Regions. In the following table, these locations list more than one associated Region, each with its own available port speeds and capabilities (**(M)** indicates MACsec encryption support at that port speed). Each device is associated with exactly one Region, and a location has separate devices for each Region that it lists.

For example, STT Hyderabad DC1 lists both Asia Pacific (Hyderabad) with 10G and 100G (MACsec) and Asia Pacific (Mumbai) with 1G and 10G. To connect at this location, you choose the associated Region whose port speed and capabilities you need. Your connection then terminates on a device for that Region and is managed in it.

**Note**  
Some associated Regions are [opt-in Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#opt-in-region) (Regions that are disabled by default). To create a connection that is associated with an opt-in Region, you must first enable the Region in your AWS account. Until you opt in, the Direct Connect location does not appear in the Direct Connect console or in API responses for that Region. For more information, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *AWS General Reference*.


**Direct Connect locations and their associated Regions ((M) indicates MACsec encryption support at that port speed)**  

| Direct Connect location | Associated Region | 
| --- | --- | 
| East Africa Data Centres NBO1, Nairobi, Kenya | Africa (Cape Town) | 
| Rack Centre LGS1, Lagos, Nigeria | Africa (Cape Town): 10G (M), 100G (M); Europe (London): 1G, 10G (M) | 
| Teraco CT1, Cape Town, South Africa | Africa (Cape Town): 10G (M), 100G (M); Europe (Ireland): 1G, 10G | 
| Equinix HK1, Tsuen Wan, N.T., Hong Kong | Asia Pacific (Hong Kong) | 
| STT Hyderabad DC1, Hyderabad, IND | Asia Pacific (Hyderabad): 10G (M), 100G (M); Asia Pacific (Mumbai): 1G, 10G | 
| DCI Indonesia, JK3 | Asia Pacific (Jakarta) | 
| NTT Jakarta 2 Data Center | Asia Pacific (Jakarta) | 
| CMC Tower, Hanoi, Vietnam | Asia Pacific (Malaysia) | 
| Menara AIMS, Kuala Lumpur, MYS | Asia Pacific (Malaysia): 10G (M), 100G (M); Asia Pacific (Singapore): 1G, 10G (M) | 
| Telcohub 1 (CX1) | Asia Pacific (Malaysia) | 
| ePLDT VM2, Makati City | Asia Pacific (Malaysia): 10G (M), 100G (M); Asia Pacific (Singapore): 1G, 10G (M) | 
| Equinix ME2, Melbourne Australia | Asia Pacific (Melbourne) | 
| Equinix MB1, Mumbai, India | Asia Pacific (Mumbai): 1G, 10G (M), 100G (M); Asia Pacific (Singapore): 1G, 10G | 
| Equinix MB2, Mumbai | Asia Pacific (Mumbai) | 
| NetMagic DC2, Bangalore, IND | Asia Pacific (Mumbai) | 
| STT Delhi DC2, Delhi, IND | Asia Pacific (Mumbai) | 
| STT GDC INDIA PVT. LTD. VSB, Chennai, IND | Asia Pacific (Mumbai) | 
| STT Kolkata, DC1 | Asia Pacific (Mumbai) | 
| Sify Rabale, Mumbai, IND | Asia Pacific (Mumbai) | 
| Spark MDR, Auckland, NZ | Asia Pacific (New Zealand) | 
| KDDI Telehouse Osaka 2 | Asia Pacific (Osaka) | 
| Digital Realty ICN10, Seoul, KOR | Asia Pacific (Seoul) | 
| KINX Gasen, Seoul, KOR | Asia Pacific (Seoul) | 
| LG U\+ Pyeong-Chon Mega Center, Seoul, KOR | Asia Pacific (Seoul) | 
| Equinix SG2, Singapore, SGP | Asia Pacific (Singapore) | 
| Global Switch, Singapore, SGP | Asia Pacific (Singapore) | 
| TCC, Bangkok | Asia Pacific (Singapore) | 
| iAdvantage MEGA-i, Hong Kong, HKG | Asia Pacific (Singapore) | 
| CDC Hume 2, Canberra | Asia Pacific (Sydney) | 
| Datacom DH6, Auckland | Asia Pacific (Sydney) | 
| Equinix SY1 - SY4, Sydney, AUS | Asia Pacific (Sydney) | 
| Global Switch SY6, Sydney, AUS | Asia Pacific (Sydney) | 
| NEXTDC B2, Brisbane | Asia Pacific (Sydney) | 
| NEXTDC C1, Canberra, AUS | Asia Pacific (Sydney) | 
| NEXTDC M1, Melbourne, AUS | Asia Pacific (Sydney) | 
| NEXTDC P1, Perth, AUS | Asia Pacific (Sydney) | 
| NEXTDC S2, Sydney, AUS | Asia Pacific (Sydney) | 
| Chief Telecom HD, Taipei, TWN | Asia Pacific (Taipei) | 
| Chunghwa Telecom, Taipei, TWN | Asia Pacific (Taipei): 10G (M), 100G (M); Asia Pacific (Tokyo): 1G, 10G (M) | 
| Telehouse Bangkok | Asia Pacific (Thailand) | 
| AT Tokyo Chuo Data Center, Tokyo, JPN | Asia Pacific (Tokyo) | 
| Chief Telecom LY, Taipei, TWN | Asia Pacific (Tokyo) | 
| Equinix OS1, Osaka, JPN | Asia Pacific (Tokyo) | 
| Equinix TY2, Tokyo, Japan | Asia Pacific (Tokyo) | 
| NEC Inzai, Japan | Asia Pacific (Tokyo) | 
| Cologix MTL3, Montreal, CAN | Canada (Central) | 
| Cologix VAN2, Vancouver, CAN | Canada (Central) | 
| Cologix VAN3, Vancouver, CAN | Canada (Central) | 
| Equinix TR2, Toronto | Canada (Central) | 
| Telehouse, Toronto, CAN | Canada (Central) | 
| eStruxture, Montreal, CAN | Canada (Central) | 
| Equinix CL1, Calgary | Canada West (Calgary) | 
| Equinix CL3, Calgary | Canada West (Calgary) | 
| CIDS Jiachuang IDC, Beijing, China | China (Beijing) | 
| GDS No. 3 DC, Shanghai, CHN | China (Beijing) | 
| Sinnet Jiuxianqiao IDC, Beijing, China | China (Beijing) | 
| Industrial Park IDC, Ningxia, CHN | China (Ningxia) | 
| Shapotou IDC, Ningxia, China | China (Ningxia) | 
| CDLAN srl Via Caldera 21, Milano | Europe (Frankfurt) | 
| CE Colo, Prague, CZE | Europe (Frankfurt) | 
| DigiPlex Ulven, Oslo, NOR | Europe (Frankfurt) | 
| Digital Realty AMS7, Amsterdam, Netherlands | Europe (Frankfurt) | 
| Digital Realty ATH3, Athens, Greece | Europe (Frankfurt) | 
| Digital Realty CPH2, Copenhagen, Denmark | Europe (Frankfurt) | 
| Digital Realty FRA6, Frankfurt, Germany | Europe (Frankfurt) | 
| Digital Realty MAD2, Madrid, Spain | Europe (Frankfurt) | 
| Digital Realty MAD3, Madrid, Spain | Europe (Frankfurt) | 
| Digital Realty STO1, Stockholm, Sweden | Europe (Frankfurt): 1G, 10G (M); Europe (Stockholm): 10G (M), 100G (M) | 
| Digital Realty VIE2, Vienna, Austria | Europe (Frankfurt) | 
| Digital Realty ZUR1, Zurich, Switzerland | Europe (Frankfurt) | 
| Equinix AM3, Amsterdam | Europe (Frankfurt) | 
| Equinix FR5, Frankfurt, DEU | Europe (Frankfurt) | 
| Equinix HE6, Helsinki, FIN | Europe (Frankfurt) | 
| Equinix IL4, Istanbul, Türkiye | Europe (Frankfurt) | 
| Equinix Itconic MD2, Madrid, ESP | Europe (Frankfurt) | 
| Equinix WA1, Warsaw, POL | Europe (Frankfurt) | 
| IPB GmbH, Berlin, DEU | Europe (Frankfurt) | 
| IPHH H3, Hamburg | Europe (Frankfurt) | 
| MedOne, Israel Haifa, ISR | Europe (Frankfurt): 1G, 10G; Israel (Tel Aviv): 10G (M), 100G (M) | 
| Telehouse Voltaire, Paris, FRA | Europe (Frankfurt): 1G, 10G (M); Europe (Paris): 1G, 10G (M), 100G (M) | 
| Digital Realty DUB2, Dublin, Ireland | Europe (Ireland) | 
| Digital Realty LHR20, London, GBR | Europe (Ireland): 1G, 10G (M); Europe (London): 1G, 10G (M) | 
| Digital Realty MRS1, Marseille, France | Europe (Ireland) | 
| Eircom Clonshaugh, Dublin, IRL | Europe (Ireland) | 
| Equinix DX1, Dubai UAE | Europe (Ireland) | 
| Equinix LD5, Slough, GBR | Europe (Ireland): 1G, 10G (M); Europe (London): 1G, 10G (M), 100G (M) | 
| Equinix LS1, Lisbon | Europe (Ireland) | 
| Etisalat Smart Hub Data Center, Fujairah, UAE | Europe (Ireland) | 
| Servecentric Unit 9, Blanchardstown, Dublin | Europe (Ireland) | 
| Teraco JB1, Johannesburg, South Africa | Europe (Ireland) | 
| Equinix MA3, Manchester, GBR | Europe (London) | 
| Telehouse West, London, GBR | Europe (London) | 
| Equinix ML2, Milano, Italy | Europe (Milan) | 
| Digital Realty PAR7, Paris, France | Europe (Paris) | 
| Equinix PA3, Paris, FRA | Europe (Paris) | 
| Equinix BA1, Barcelona, Spain | Europe (Spain) | 
| Equinix Sweden SK1 | Europe (Stockholm) | 
| Equinix ZH5, Zurich, CHE | Europe (Zurich) | 
| Edgeconnex, Herzliya, ISR | Israel (Tel Aviv) | 
| Equinix MX1, Queretaro | Mexico (Central) | 
| Cirion BNARAGMS, Buenos Aires | South America (São Paulo) | 
| Cirion LIMAPUCD, Lima | South America (São Paulo) | 
| Equinix BG1, Bogota | South America (São Paulo) | 
| Equinix RJ2, Rio de Janeiro, BRA | South America (São Paulo) | 
| Equinix SP4, Sao Paulo, BRA | South America (São Paulo) | 
| Sonda Quilicura, Santiago | South America (São Paulo) | 
| Tivit, Sao Paulo, BRA | South America (São Paulo) | 
| 165 Halsey Street, Newark, NJ | US East (N. Virginia) | 
| CoreSite NY1, New York, NY | US East (N. Virginia) | 
| CoreSite VA1, Reston, VA | US East (N. Virginia) | 
| Crown Castle, Philadelphia, PA | US East (N. Virginia) | 
| Digital Realty ATL13, Atlanta, GA | US East (N. Virginia) | 
| Digital Realty IAD38, Ashburn, VA | US East (N. Virginia) | 
| Equinix DA2, Dallas, TX | US East (N. Virginia) | 
| Equinix DC2/DC11, Ashburn, VA | US East (N. Virginia) | 
| Equinix MI1, Miami, FL | US East (N. Virginia) | 
| Equinix NY5, Secaucus, NJ | US East (N. Virginia) | 
| KIO Networks QRO 1, Queretaro | US East (N. Virginia) | 
| Markley, One Summer Street, Boston, MA | US East (N. Virginia) | 
| QTS ATL1, Atlanta, GA | US East (N. Virginia) | 
| Cologix COL2, Columbus, OH | US East (Ohio) | 
| Cologix MIN3, Minneapolis, MN | US East (Ohio) | 
| CoreSite CH1, Chicago, IL | US East (Ohio) | 
| CyrusOne Aurora A1 | US East (Ohio) | 
| DataBank HOU3, Houston, TX | US East (Ohio) | 
| Equinix CH2, Chicago, IL | US East (Ohio) | 
| Netrality Data Centers, Kansas City, MO | US East (Ohio) | 
| QTS, Chicago, IL | US East (Ohio) | 
| CoreSite LA1, Los Angeles, CA | US West (N. California) | 
| CoreSite SV4, Santa Clara, CA | US West (N. California) | 
| Coresite SV2, Milpitas, CA | US West (N. California) | 
| EdgeConnex PHX01, Phoenix, AZ | US West (N. California) | 
| Equinix LA3, El Segundo, CA | US West (N. California) | 
| Equinix SV5, San Jose, CA | US West (N. California) | 
| PhoenixNAP, Phoenix, AZ | US West (N. California) | 
| AlohaNap, Kapolei, HI | US West (Oregon) | 
| CoreSite DE1, Denver, CO | US West (Oregon) | 
| DataBank LAS1 | US West (Oregon) | 
| EdgeConnex, Hillsboro, OR | US West (Oregon) | 
| Pittock Block, Portland, OR | US West (Oregon) | 
| Serverfarm LAX1 El Segundo, CA | US West (Oregon) | 
| Switch SUPERNAP 8, Las Vegas, NV | US West (Oregon) | 
| TierPoint, Seattle, WA | US West (Oregon) | 
| Westin Building Exchange, Seattle, WA | US West (Oregon) | 
| Equinix SV5, San Jose, CA | AWS GovCloud (US-West) | 
| Atlas Edge BER001, Berlin, DEU | EU Sovereign Cloud (Germany) | 
| IPB GmbH, Berlin, DEU | EU Sovereign Cloud (Germany) | 

## Direct Connect routing policies and BGP communities
<a name="routing-and-bgp"></a>

Direct Connect applies inbound (from your on-premises data center) and outbound (from your AWS Region) routing policies for a public Direct Connect connection. You can also use Border Gateway Protocol (BGP) community tags on routes advertised by Amazon and apply BGP community tags on the routes you advertise to Amazon.

### Public virtual interface routing policies
<a name="routing-policies"></a>

If you're using Direct Connect to access public AWS services, you must specify the public IPv4 prefixes or IPv6 prefixes to advertise over BGP. 

The following inbound routing policies apply:
+ You must own the public prefixes and they must be registered as such in the appropriate regional internet registry.
+ Traffic must be destined to Amazon public prefixes. Transitive routing between connections is not supported.
+ Direct Connect performs inbound packet filtering to validate that the source of the traffic originated from your advertised prefix. 

The following outbound routing policies apply:
+ AS\_PATH and Longest Prefix Match are used to determine the routing path. AWS recommends advertising more specific routes using Direct Connect if the same prefix is being advertised to both the Internet and to a public virtual interface. 
+ Direct Connect advertises all local and remote AWS Region prefixes where available and includes on-net prefixes from other AWS non-Region points of presence (PoP) where available; for example, CloudFront and Route 53.
**Note**  
 Prefixes listed in the AWS IP address ranges JSON file, ip-ranges.json, for the AWS China Regions are only advertised in the AWS China Regions.
 Prefixes listed in the AWS IP address ranges JSON file, ip-ranges.json, for the AWS Commercial Regions are only advertised in the AWS Commercial Regions. 
For more information about the ip-ranges.json file, see [AWS IP address ranges ](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the *AWS General Reference*.
+ Direct Connect advertises prefixes with a minimum path length of 3.
+ Direct Connect advertises all public prefixes with the well-known `NO_EXPORT` BGP community.
+ If you advertise the same prefixes from two different Regions using two different public virtual interfaces, and both have the same BGP attributes and longest prefix length, AWS will prioritize the home Region for outbound traffic.
+ If you have multiple Direct Connect connections, you can adjust the load-sharing of inbound traffic by advertising prefixes with the same path attributes.
+ The prefixes advertised by Direct Connect must not be advertised beyond the network boundaries of your connection. For example, these prefixes must not be included in any public internet routing table.
+ Direct Connect keeps prefixes advertised by customers within the Amazon network. We do not re-advertise customer prefixes learned from a public VIF to any of the following: 
  + Other Direct Connect customers
  + Networks that peer with the AWS Global Network
  + Amazon's transit providers
+ When using a public interface, you can use either a public or private ASN. However, there are important considerations:
  + Public ASNs: You must own the ASN and have the right to announce it. AWS will verify your ownership of the ASN. Both ASNs (1-2147483647) and long ASNs (1-4294967295) are supported.
  + Private ASNs: You can use private ASNs from the following ranges: 
    + private ASNs: 64512-65534
    + private long ASNs: 4200000000-4294967294

     However, Direct Connect will replace the private ASN with the AWS ASN (7224) when advertising your prefixes to other AWS customers or the internet.
  + ASN prepending:
    + With a public ASN (both ASN and long ASN), prepending will work as expected, and your prepended ASN will be visible to other networks.
    + With a private ASN (both ASN and long ASN), any prepending you do will be stripped when AWS replaces your private ASN with 7224. This means ASN prepending is not effective for influencing routing decisions outside of AWS when using a private ASN on a public virtual interface.
+ When establishing a BGP peering session with AWS over a public virtual interface, use 7224 for the autonomous system numbers (ASN) to establish the BGP session on the AWS side. The ASN on your router or customer gateway device should be different from that ASN. Your customer ASN can be either anASN (1-2147483647, excluding reserved ranges) or a long ASN (1-4294967295, excluding reserved ranges).

### Public virtual interface BGP communities
<a name="bgp-communities"></a>

Direct Connect supports scope BGP community tags to help control the scope (Regional or global) and route preference of traffic on public virtual interfaces. AWS treats all routes received from a public VIF as if they were tagged with the NO\_EXPORT BGP community tag, meaning only the AWS network will use that routing information.

#### Scope BGP communities
<a name="scope-bgp-communities"></a>

You can apply BGP community tags on the public prefixes that you advertise to Amazon to indicate how far to propagate your prefixes in the Amazon network, for the local AWS Region only, all Regions within a continent, or all public Regions.

##### AWS Region communities
<a name="bgp-region-communities"></a>

For inbound routing policies, you can use the following BGP communities for your prefixes:
+ `7224:9100`—Local AWS Regions
+ `7224:9200`—All AWS Regions for a continent:
  + North America-wide
  + Asia Pacific
  + Europe, the Middle East and Africa
+ `7224:9300`—Global (all public AWS Regions)

**Note**  
If you do not apply any community tags, prefixes are advertised to all public AWS Regions (global) by default.  
Prefixes that are marked with the same communities, and have identical AS\_PATH attributes are candidates for multi-pathing.

The communities `7224:1` – `7224:65535` are reserved by Direct Connect.

For outbound routing policies, Direct Connect applies the following BGP communities to its advertised routes:
+ `7224:8100`—Routes that originate from the same AWS Region in which the Direct Connect point of presence is associated.
+ `7224:8200`—Routes that originate from the same continent with which the Direct Connect point of presence is associated.
+ No tag—Routes that originate from other continents.

**Note**  
To receive all AWS public prefixes do not apply any filter. 

Communities that are not supported for a Direct Connect public connection are removed.

#### `NO_EXPORT` BGP community
<a name="no-export-bgp-communities"></a>

For outbound routing policies, the `NO_EXPORT` BGP community tag is supported for public virtual interfaces.

Direct Connect also provides BGP community tags on advertised Amazon routes. If you use Direct Connect to access public AWS services, you can create filters based on these community tags. 

For public virtual interfaces, all routes that Direct Connect advertises to customers are tagged with the NO\_EXPORT community tag.

### Private virtual interface and transit virtual interface routing policies
<a name="private-routing-policies"></a>

If you're using AWS Direct Connect to access your private AWS resources, you must specify the IPv4 or IPv6 prefixes to advertise over BGP. These prefixes can be public or private.

The following outbound routing rules apply based on the prefixes advertised:
+ AWS evaluates the longest prefix length first. AWS recommends advertising more specific routes using multiple Direct Connect virtual interfaces if the desired routing paths are meant for active/passive connections. See [ Influencing Traffic over Hybrid Networks using Longest Prefix Match](https://aws.amazon.com/blogs/networking-and-content-delivery/influencing-traffic-over-hybrid-networks-using-longest-prefix-match/) for more information.
+ Local preference is the BGP attribute recommended to use when desired routing paths are meant for active/passive connections and the prefix lengths advertised are the same. This value is set per Region to prefer Direct Connect locations that have the same associated AWS Region using the `7224:7200`—Medium local preference community value. Where the local Region is not associated with the Direct Connect location, it is set to a lower value. This applies only if no local preference community tags are assigned. For more information about associated Regions, see [Associated Region](#associated-region).
+ AS\_PATH length can be used to determine the routing path when the prefix length and local preference are the same. 
+ Multi-Exit Discriminator (MED) can be used to determine the routing path when prefix length, local preference, and AS\_PATH are the same. AWS does not recommend using MED values given their lower priority in evaluation.
+ AWS uses equal-cost multi-path (ECMP) routing across multiple transit or private virtual interfaces when prefixes have the same AS\_PATH length and BGP attributes. The ASNs in the AS\_PATH of the prefixes do not need to match.

#### Private virtual interface and transit virtual interface BGP communities
<a name="bgp-communities-private-transit"></a>

When an AWS Region routes traffic to on-premises locations via Direct Connect private or transit virtual interfaces, the associated AWS Region of the Direct Connect location influences the ability to use ECMP. AWS Regions prefer Direct Connect locations in the same associated AWS Region by default. See [Associated Region](#associated-region) to identify the associated AWS Region of any Direct Connect location.

When there are no local preference community tags applied, Direct Connect supports ECMP over private or transit virtual interfaces for prefixes with the same, AS\_PATH length, and MED value over two or more paths in the following scenarios:
+ The AWS Region sending traffic has two or more virtual interface paths from locations in the same associated AWS Region, whether in the same or different colocation facilities.
+ The AWS Region sending traffic has two or more virtual interface paths from locations not in the same Region.

Fore more information, see [How do I set up an Active/Active or Active/Passive Direct Connect connection to AWS from a private or transit virtual interface?](https://repost.aws/knowledge-center/direct-connect-private-transit-interface/)

**Note**  
This has no effect on ECMP to an AWS Region from on-premises locations.

To control route preferences, Direct Connect supports local preference BGP community tags for private virtual interfaces and transit virtual interfaces.

##### Local preference BGP communities
<a name="local-pref-bgp-communities"></a>

You can use local preference BGP community tags to achieve load balancing and route preference for incoming traffic to your network. For each prefix that you advertise over a BGP session, you can apply a community tag to indicate the priority of the associated path for returning traffic. 

The following local preference BGP community tags are supported:
+ `7224:7100`—Low preference
+ `7224:7200`—Medium preference 
+ `7224:7300`—High preference

Local preference BGP community tags are mutually exclusive. To load balance traffic across multiple Direct Connect connections (active/active) homed to the same or different AWS Regions, apply the same community tag; for example, `7224:7200` (medium preference) across the prefixes for the connections. If one of the connections fails, traffic will be then load balance using ECMP across the remaining active connections regardless of their home Region associations . To support failover across multiple Direct Connect connections (active/passive), apply a community tag with a higher preference to the prefixes for the primary or active virtual interface and a lower preference to the prefixes for the backup or passive virtual interface. For example, set the BGP community tags for your primary or active virtual interfaces to `7224:7300` (high preference) and `7224:7100` (low preference) for your passive virtual interfaces.

Local preference BGP community tags are evaluated before any AS\_PATH attribute, and are evaluated in order from lowest to highest preference (where highest preference is preferred).

### Direct Connect private virtual interface routing example
<a name="private-transit-vif-example"></a>

Consider the configuration where the Direct Connect location 1 home Region is the same as the VPC home Region. There is a redundant Direct Connect location in a different Region There are two private VIFs (VIF A and VIF B) from Direct Connect location 1 (us-east-1) to the Direct Connect gateway. There is one private VIF (VIF C) from Direct Connect location (us-west-1) to the Direct Connect gateway. To have AWS route traffic over VIF B before VIF A, set the AS\_PATH attribute of VIF B to be shorter than the VIF A AS\_PATH attribute.

The VIFs have the following configurations:
+ VIF A (in us-east-1) advertises 172.16.0.0/16 and has an AS\_PATH attribute of 65001, 65001, 65001
+ VIF B (in us-east-1) advertises 172.16.0.0/16 and has an AS\_PATH attribute of 65001, 65001
+ VIF C (in us-west-1) advertises 172.16.0.0/16 and has an AS\_PATH attribute of 65001

![Private VIF Routing no AS_PATH](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/private-vif-as-path-1.png)


If you change the CIDR range configuration of VIF C, routes that fall in to the VIF C CIDR range use VIF C because it has the longest prefix length. 
+ VIF C (in us-west-1) advertises 172.16.0.0/24 and has an AS\_PATH attribute of 65001

![Private VIF Routing](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/private-vif-as-path-2.png)


# Direct Connect connection options
<a name="connection_options"></a>

AWS offers customers the ability to achieve highly resilient network connections between Amazon Virtual Private Cloud (Amazon VPC) and their on-premises infrastructure. The AWS Direct Connect Resiliency Toolkit provides a connection wizard with multiple resiliency models. These models help you to determine, and then place an order for the number of dedicated connections to achieve your SLA objective. You select a resiliency model, and then the AWS Direct Connect Resiliency Toolkit guides you through the dedicated connection ordering process. The resiliency models are designed to ensure that you have the appropriate number of dedicated connections in multiple locations. 

The following connection options are available for Direct Connect.
+ **Maximum Resiliency**: This model is available in the AWS Direct Connect Resiliency Toolkit and provides you a way to order dedicated connections to achieve an SLA of 99.99%. It requires you to meet all of the requirements for achieving the SLA that are specified in the [Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/). For more information, see the [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit).
+ **High Resiliency**: This model is available in the AWS Direct Connect Resiliency Toolkit and provides you a way to order dedicated connections to achieve an SLA of 99.9%. It requires you to meet all of the requirements for achieving the SLA that are specified in the [Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/). For more information, see the [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit).
+ **Development and Test**: This model is available in the AWS Direct Connect Resiliency Toolkit and provides you a way to achieve development and test resiliency for non-critical workloads by using separate connections that terminate on separate devices in one location. For more information, see the [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit).
+ **Classic**: A Classic connection creates a connection without the need of the AWS Direct Connect Resiliency Toolkit. It's intended for users that have existing connections and want to add additional connections without using the toolkit. This model has a 95% SLA but does not provide resiliency or redundancy. For more information, see [Classic connection](#classic_connection).

**Topics**
+ [Connection prerequisites](#prerequisites)
+ [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit)
+ [Classic connection](#classic_connection)

## Connection prerequisites
<a name="prerequisites"></a>

Direct Connect supports the following port speeds over single-mode fiber: 1000BASE-LX (1310 nm) transceiver for 1 gigabit Ethernet, a 10GBASE-LR (1310 nm) transceiver for 10 gigabit, a 100GBASE-LR4 for 100 gigabit Ethernet, or a 400GBASE-LR4 for 400 Gbps Ethernet.

You can set up a Direct Connect connection using the AWS Direct Connect Resiliency Toolkit or a Classic connection in one of the following ways:


| Model | Bandwidth | Method | 
| --- | --- | --- | 
| Dedicated connection | 1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps | Work with a Direct Connect Partner or a network provider to connect a router from your data center, office, or colocation environment to a Direct Connect location. The network provider does not have to be an [AWS Direct Connect Partner](https://aws.amazon.com/directconnect/partners) to connect you to a dedicated connection. Direct Connect dedicated connections support these port speeds over single-mode fiber: 1 Gbps: 1000BASE-LX (1310 nm), 10 Gbps: 10GBASE-LR (1310 nm), 100Gbps: 100GBASE-LR4, or 400GBASE-LR4 for 400 Gbps Ethernet. | 
| Hosted connection | 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, and 25 Gbps. | Work with a partner in the [AWS Direct Connect Partner Program](https://aws.amazon.com/directconnect/partners) to connect a router from your data center, office, or colocation environment to a Direct Connect location.<br />Only certain partners provide higher capacity connections.  | 

For connections to Direct Connect with bandwidths of 1 Gbps or higher, ensure that your network meets the following requirements:
+ Your network must use single-mode fiber with a 1000BASE-LX (1310 nm) transceiver for 1 gigabit Ethernet, a 10GBASE-LR (1310 nm) transceiver for 10 gigabit, a 100GBASE-LR4 for 100 gigabit Ethernet, or a 400GBASE-LR4 for 400 Gbps Ethernet.
+ Depending on the AWS Direct Connect endpoint serving your connection, on-premises device auto-negotiation might need to be enabled or disabled for any dedicated connection. If a virtual interface remains down when a Direct Connect connection is up, see [Troubleshoot layer 2 (data link) issues](#ts-layer-2).
+ 802.1Q VLAN encapsulation must be supported across the entire connection, including intermediate devices.
+ Your device must support Border Gateway Protocol (BGP) and BGP MD5 authentication.
+ (Optional) You can configure Bidirectional Forwarding Detection (BFD) on your network. Asynchronous BFD is automatically enabled for each Direct Connect virtual interface. It's automatically enabled for Direct Connect virtual interfaces, but does not take effect until you configure it on your router. For more information, see [Enable BFD for a Direct Connect connection](https://aws.amazon.com/premiumsupport/knowledge-center/enable-bfd-direct-connect/). 

Make sure you have the following information before you begin your configuration:
+ The resiliency model that you want to use if you're not creating a Classic connection. For AWS Direct Connect Resiliency Toolkit connection options, see the [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit).
+ The speed, location, and partner for all of your connections.

  You only need the speed for one connection. 

## AWS Direct Connect Resiliency Toolkit
<a name="resiliency_toolkit"></a>

AWS offers customers the ability to achieve highly resilient network connections between Amazon Virtual Private Cloud (Amazon VPC) and their on-premises infrastructure. The AWS Direct Connect Resiliency Toolkit provides a connection wizard with multiple resiliency models. These models help you to determine, and then place an order for the number of dedicated connections to achieve your SLA objective. You select a resiliency model, and then the AWS Direct Connect Resiliency Toolkit guides you through the dedicated connection ordering process. The resiliency models are designed to ensure that you have the appropriate number of dedicated connections in multiple locations. 

The AWS Direct Connect Resiliency Toolkit has the following benefits:
+ Provides guidance on how you determine and then order the appropriate redundant Direct Connect dedicated connections.
+ Ensures that the redundant dedicated connections have the same speed.
+ Automatically configures the dedicated connection names.
+ Automatically approves your dedicated connections when you have an existing AWS account and you select a known AWS Direct Connect Partner. The Letter of Authority (LOA) is available for immediate download.
+ Automatically creates a support ticket for the dedicated connection approval when you are a new AWS customer, or you select an unknown (**Other**) partner.
+ Provides an order summary for your dedicated connections, with the SLA that you can achieve and the port-hour cost for the ordered dedicated connections.
+ Creates link aggregation groups (LAGs), and adds the appropriate number of dedicated connections to the LAGs when you choose a speed other than 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps.
+ Provides a LAG summary with the dedicated connection SLA that you can achieve, and the total port-hour cost for each ordered dedicated connection as part of the LAG.
+ Prevents you from terminating the dedicated connections on the same Direct Connect device.
+ Provides a way for you to test your configuration for resiliency. You work with AWS to bring down the BGP peering session in order to verify that traffic routes to one of your redundant virtual interfaces. For more information, see [Direct Connect Failover Test](#resiliency_failover).
+ Provides Amazon CloudWatch metrics for connections and virtual interfaces. For more information, see [Monitoring and visibility with Direct Connect](#monitoring-overview).

After you select the resiliency model, the AWS Direct Connect Resiliency Toolkit steps you through the following procedures:
+ Selecting the number of dedicated connections
+ Selecting the connection capacity, and the dedicated connection location
+ Ordering the dedicated connections
+ Verifying that the dedicated connections are ready to use
+ Downloading your Letter of Authority (LOA-CFA) for each dedicated connection
+ Verifying that your configuration meets your resiliency requirements

### Available resiliency models
<a name="available_models"></a>

The following resiliency models are available in the AWS Direct Connect Resiliency Toolkit:
+ **Maximum resiliency**: This model provides you a way to order dedicated connections to achieve an SLA of 99.99%. It requires you to meet all of the requirements for achieving the SLA that are specified in the [Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/). 
+ **High resiliency**: This model provides you a way to order dedicated connections to achieve an SLA of 99.9%. It requires you to meet all of the requirements for achieving the SLA that are specified in the [Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/). 
+ **Development and test**: This model provides you a way to achieve development and test resiliency for non-critical workloads, by using separate connections that terminate on separate devices in one location.

The best practice is to use the **Connection wizard** in the AWS Direct Connect Resiliency Toolkit to order to achieve your SLA objective.

**Note**  
If you do not want to create a resiliency model using the AWS Direct Connect Resiliency Toolkit, you can create a Classic connection. For more information about Classic connections, see [Classic connection](#classic_connection).

### AWS Direct Connect Resiliency Toolkit prerequisites
<a name="prerequisites"></a>

Note the following information before you begin your configuration:
+ Familiarize yourself with the [Connection prerequisites](#connect-prereqs.title).
+ The available resiliency model that you want to use.

### Maximum resiliency
<a name="maximum_resiliency"></a>

You can achieve maximum resiliency for critical workloads by using separate connections that terminate on separate devices in more than one location (as shown in the following figure). This model provides resiliency against device, connectivity, and complete location failures. The following figure shows both connections from each customer data center going to the same Direct Connect locations. You can optionally have each connection from a customer data center going to different locations.

![Maximum resiliency model](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dc-max-resiliency.png)


For the procedure for using the AWS Direct Connect Resiliency Toolkit to configure a maximum resiliency model, see [Configure maximum resiliency](#max-resiliency-set-up).

### High resiliency
<a name="high_resiliency"></a>

You can achieve high resiliency for critical workloads by using two single connections to multiple locations (as shown in the following figure). This model provides resiliency against connectivity failures caused by a fiber cut or a device failure. It also helps prevent a complete location failure.

![High resiliency model](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dc-high-resiliency.png)


For the procedure for using the AWS Direct Connect Resiliency Toolkit to configure a high resiliency model, see [Configure high resiliency](#high-resiliency-set-up).

### Development and test
<a name="dev-test-resiliency"></a>

You can achieve development and test resiliency for non-critical workloads by using separate connections that terminate on separate devices in one location (as shown in the following figure). This model provides resiliency against device failure, but does not provide resiliency against location failure.

![Development and Test Model](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dc-devtest.png)


For the procedure for using the AWS Direct Connect Resiliency Toolkit to configure a maximum resiliency model, see [Configure development and test resiliency](#devtest-resiliency-set-up).

### AWS Direct Connect FailoverTest
<a name="toolkit-failover-test"></a>

Use the AWS Direct Connect Resiliency Toolkit to verify traffic routes and that those routes meet your resiliency requirements.

For the procedures for using the AWS Direct Connect Resiliency Toolkit to perform failover tests, see [Direct Connect failover test](#resiliency_failover).

### Configure Direct Connect for maximum resiliency with the AWS Direct Connect Resiliency Toolkit
<a name="max-resiliency-set-up"></a>

In this example, the Direct Connect Resiliency Toolkit is used to configure a maximum resiliency model

**Topics**
+ [Step 1: Sign up for AWS](#max-resiliency-signup)
+ [Step 2: Configure the resiliency model](#max-resiliency-select-model)
+ [Step 3: Create your virtual interfaces](#max-resiliency-createvirtualinterface)
+ [Step 4: Verify your virtual interface resiliency configuration](#max-resiliency-failover)
+ [Step 5: Verify your virtual interfaces connectivity](#max-resiliency-connected)

#### Step 1: Sign up for AWS
<a name="max-resiliency-signup"></a>

To use Direct Connect, you need an AWS account if you don't already have one.

##### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

#### Step 2: Configure the resiliency model
<a name="max-resiliency-select-model"></a>

**To configure a maximum resiliency model**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**, and then choose **Create a connection**.

1. Under **Connection ordering type**, choose **Connection wizard**.

1. Under **Resiliency level**, choose **Maximum Resiliency**, and then choose **Next**.

1. On the **Configure connections** pane, under **Connection settings,** do the following:

   1. For **Bandwidth**, choose the dedicated connection bandwidth.

      This bandwidth applies to all of the created connections.

   1. For **First location service provider**, select the appropriate Direct Connect location for the dedicated connection.

   1. If applicable, for **First Sub location**, choose the floor closest to you or your network provider. This option is only available if the location has meet-me rooms (MMRs) on multiple floors of the building.

   1. If you selected **Other** for **First location service provider**, for **Name of other provider**, enter the name of the partner that you use.

   1. For **Second location service provider**, select the appropriate Direct Connect location.

   1. If applicable, for **Second Sub location**, choose the floor closest to you or your network provider. This option is only available if the location has meet-me rooms (MMRs) on multiple floors of the building.

   1. If you selected **Other** for **Second location service provider**, for **Name of other provider**, enter the name of the partner that you use.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Next**.

1. Review your connections, and then choose **Continue**.

   If your LOAs are ready, you can choose **Download LOA**, and then click **Continue**.

   It can take up to 72 business hours for AWS to review your request and provision a port for your connection. During this time, you might receive an email with a request for more information about your use case or the specified location. The email is sent to the email address that you used when you signed up for AWS. You must respond within 7 days or the connection is deleted. 

#### Step 3: Create your virtual interfaces
<a name="max-resiliency-createvirtualinterface"></a>

You can create a private virtual interface to connect to your VPC. Or, you can create a public virtual interface to connect to public AWS services that aren't in a VPC. When you create a private virtual interface to a VPC, you need a private virtual interface for each VPC that you're connecting to. For example, you need three private virtual interfaces to connect to three VPCs.

Before you begin, ensure that you have the following information:


| Resource | Required information | 
| --- | --- | 
| Connection | The Direct Connect connection or link aggregation group (LAG) for which you are creating the virtual interface. | 
| Virtual interface name | A name for the virtual interface. | 
| Virtual interface owner | If you're creating the virtual interface for another account, you need the AWS account ID of the other account. | 
| (Private virtual interface only) Connection | For connecting to a VPC in the same AWS Region, you need the virtual private gateway for your VPC. The ASN for the Amazon side of the BGP session is inherited from the virtual private gateway. When you create a virtual private gateway, you can specify your own private ASN. Otherwise, Amazon provides a default ASN. For more information, see [Create a Virtual Private Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg) in the Amazon VPC User Guide. For connecting to a VPC through a Direct Connect gateway, you need the Direct Connect gateway. For more information, see [Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html). | 
| VLAN | A unique virtual local area network (VLAN) tag that's not already in use on your connection. The value must be between 1 and 4094 and must comply with the Ethernet 802.1Q standard. This tag is required for any traffic traversing the Direct Connect connection. If you have a hosted connection, your AWS Direct Connect Partner provides this value. You can’t modify the value after you have created the virtual interface. | 
| Peer IP addresses |  A virtual interface can support a BGP peering session for IPv4, IPv6, or one of each (dual-stack). Do not use Elastic IPs (EIPs) or Bring your own IP addresses (BYOIP) from the Amazon Pool to create a public virtual interface. You cannot create multiple BGP sessions for the same IP addressing family on the same virtual interface. The IP address ranges are assigned to each end of the virtual interface for the BGP peering session. +  IPv4:   (Public virtual interface only) You must specify unique public IPv4 addresses that you own. The value can be one of the following:  A customer-owned IPv4 CIDR <br />These can be any public IPs (customer-owned or provided by AWS), but the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/31` range, such as `203.0.113.0/31`, you could use `203.0.113.0` for your peer IP and `203.0.113.1` for the AWS peer IP. Or, if you allocate a `/24` range, such as `198.51.100.0/24`, you could use `198.51.100.10` for your peer IP and `198.51.100.20` for the AWS peer IP.  An IP range owned by your AWS Direct Connect Partner or ISP, along with an LOA-CFA authorization  An AWS-provided /31 CIDR. Contact [AWS Support](https://aws.amazon.com/support/createCase) to request a public IPv4 CIDR (and provide a use case in your request)We cannot guarantee that we will be able to fulfill all requests for AWS-provided public IPv4 addresses.     (Private virtual interface only) Amazon can generate private IPv4 addresses for you. If you specify your own, ensure that you specify private CIDRs for your router interface and the AWS Direct Connect interface only. For example, do not specify other IP addresses from your local network. Similar to a public virtual interface, the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/30` range, such as `192.168.0.0/30`, you could use `192.168.0.1` for your peer IP and `192.168.0.2` for the AWS peer IP.   <br />+  IPv6: Amazon automatically allocates you a /125 IPv6 CIDR. You cannot specify your own peer IPv6 addresses.   | 
| Address family | Whether the BGP peering session will be over IPv4 or IPv6. | 
| BGP information | +  A public or private Border Gateway Protocol (BGP) Autonomous System Number (ASN) for your side of the BGP session. If you are using a public ASN, you must own it. If you are using a private ASN, you can set a custom ASN value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 1 to 4294967294 range. Autonomous System (AS) prepending does not work if you use a private ASN for a public virtual interface. <br />+  AWS enables MD5 by default. You cannot modify this option. <br />+  An MD5 BGP authentication key. You can provide your own, or you can let Amazon generate one for you.  | 
| (Public virtual interface only) Prefixes you want to advertise |  Public IPv4 routes or IPv6 routes to advertise over BGP. You must advertise at least one prefix using BGP, up to a maximum of 1,000 prefixes.+  IPv4: The IPv4 CIDR can overlap with another public IPv4 CIDR announced using Direct Connect when either of the following is true:  The CIDRs are from different AWS Regions. Make sure that you apply BGP community tags on the public prefixes. You use AS\_PATH when you have a public ASN in an active/passive configuration.  <br />For more information, see [Routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html). <br />+  Over a Direct Connect public virtual interface, you can specify any prefix length from /1 to /32 for IPv4 and from /1 to /64 for IPv6. <br />+  You may add additional prefixes to an existing public VIF and advertise those by contacting [AWS support](https://aws.amazon.com/support/createCase). In your support case, provide a list of additional CIDR prefixes you want to add to the public VIF and advertise.  | 
| (Private and transit virtual interfaces only) Jumbo frames | The maximum transmission unit (MTU) of packets over Direct Connect. The default is 1500. Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. Jumbo frames apply only to propagated routes from Direct Connect. If you add static routes to a route table that point to your virtual private gateway, then traffic routed through the static routes is sent using 1500 MTU. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find Jumbo frame capable on the virtual interface General configuration page. | 

If your public prefixes or ASNs belong to an ISP or network carrier, we request additional information from you. This can be a document using an official company letterhead, or an email from the company's domain name verifying that the network prefix/ASN can be used by you.

When you create a public virtual interface, it can take up to 72 business hours for AWS to review and approve your request.

**To provision a public virtual interface to non-VPC services**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Public**.

1. Under **Public virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol (BGP) Autonomous System Number (ASN) of your gateway.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer IP**, enter the IPv4 CIDR address to use to send traffic to AWS.

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To provide your own BGP key, enter your BGP MD5 key.

      If you do not enter a value, we generate a BGP key.

   1. To advertise prefixes to Amazon, for **Prefixes you want to advertise**, enter the IPv4 CIDR destination addresses (separated by commas) to which traffic should be routed over the virtual interface. 

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

**To provision a private virtual interface to a VPC**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Private**.

1. Under **Private virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Gateway type**, choose **Virtual private gateway**, or **Direct Connect gateway**. 

   1. For **Virtual interface owner**, choose **Another AWS account**, and then enter the AWS account.

   1. For **Virtual private gateway**, choose the virtual private gateway to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 9001 (jumbo frames), select **Jumbo MTU (MTU size 9001)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

#### Step 4: Verify your virtual interface resiliency configuration
<a name="max-resiliency-failover"></a>

After you have established virtual interfaces to the AWS Cloud or to Amazon VPC, perform a virtual interface failover test to verify that your configuration meets your resiliency requirements. For more information, see [Direct Connect Failover Test](#resiliency_failover). 

#### Step 5: Verify your virtual interfaces connectivity
<a name="max-resiliency-connected"></a>

After you have established virtual interfaces to the AWS Cloud or to Amazon VPC, you can verify your AWS Direct Connect connection using the following procedures. 

**To verify your virtual interface connection to the AWS Cloud**
+ Run `traceroute` and verify that the Direct Connect identifier is in the network trace.

**To verify your virtual interface connection to Amazon VPC**

1. Using a pingable AMI, such as an Amazon Linux AMI, launch an EC2 instance into the VPC that is attached to your virtual private gateway. The Amazon Linux AMIs are available in the **Quick Start** tab when you use the instance launch wizard in the Amazon EC2 console. For more information, see [Launch an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance_linux.html) in the *Amazon EC2 User Guide.* Ensure that the security group that's associated with the instance includes a rule permitting inbound ICMP traffic (for the ping request).

1. After the instance is running, get its private IPv4 address (for example, 10.0.0.4). The Amazon EC2 console displays the address as part of the instance details.

1. Ping the private IPv4 address and get a response.

### Configure Direct Connect for high resiliency with the AWS Direct Connect Resiliency Toolkit
<a name="high-resiliency-set-up"></a>

In this example, the Direct Connect Resiliency Toolkit is used to configure a high resiliency model

**Topics**
+ [Step 1: Sign up for AWS](#high-resiliency-signup)
+ [Step 2: Configure the resiliency model](#high-resiliency-select-model)
+ [Step 3: Create your virtual interfaces](#high-resiliency-createvirtualinterface)
+ [Step 4: Verify your virtual interface resiliency configuration](#high-res-resiliency-failover)
+ [Step 5: Verify your virtual interfaces connectivity](#high-resiliency-connected)

#### Step 1: Sign up for AWS
<a name="high-resiliency-signup"></a>

To use Direct Connect, you need an AWS account if you don't already have one.

##### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

#### Step 2: Configure the resiliency model
<a name="high-resiliency-select-model"></a>

**To configure a high resiliency model**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**, and then choose **Create a connection**.

1. Under **Connection ordering type**, choose **Connection wizard**.

1. Under **Resiliency level**, choose **High Resiliency**, and then choose **Next**.

1. On the **Configure connections** pane, under **Connection settings,** do the following:

   1. For **bandwidth**, choose the connection bandwidth.

      This bandwidth applies to all of the created connections.

   1. For **First location service provider**, select the appropriate Direct Connect location.

   1. If applicable, for **First Sub location**, choose the floor closest to you or your network provider. This option is only available if the location has meet-me rooms (MMRs) on multiple floors of the building.

   1. If you selected **Other** for **First location service provider**, for **Name of other provider**, enter the name of the partner that you use.

   1. For **Second location service provider**, select the appropriate Direct Connect location.

   1. If applicable, for **Second Sub location**, choose the floor closest to you or your network provider. This option is only available if the location has meet-me rooms (MMRs) on multiple floors of the building.

   1. If you selected **Other** for **Second location service provider**, for **Name of other provider**, enter the name of the partner that you use.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Next**.

1. Review your connections, and then choose **Continue**.

   If your LOAs are ready, you can choose **Download LOA**, and then click **Continue**.

   It can take up to 72 business hours for AWS to review your request and provision a port for your connection. During this time, you might receive an email with a request for more information about your use case or the specified location. The email is sent to the email address that you used when you signed up for AWS. You must respond within 7 days or the connection is deleted. 

#### Step 3: Create your virtual interfaces
<a name="high-resiliency-createvirtualinterface"></a>

You can create a private virtual interface to connect to your VPC. Or, you can create a public virtual interface to connect to public AWS services that aren't in a VPC. When you create a private virtual interface to a VPC, you need a private virtual interface for each VPC that you're connecting to. For example, you need three private virtual interfaces to connect to three VPCs.

Before you begin, ensure that you have the following information:


| Resource | Required information | 
| --- | --- | 
| Connection | The Direct Connect connection or link aggregation group (LAG) for which you are creating the virtual interface. | 
| Virtual interface name | A name for the virtual interface. | 
| Virtual interface owner | If you're creating the virtual interface for another account, you need the AWS account ID of the other account. | 
| (Private virtual interface only) Connection | For connecting to a VPC in the same AWS Region, you need the virtual private gateway for your VPC. The ASN for the Amazon side of the BGP session is inherited from the virtual private gateway. When you create a virtual private gateway, you can specify your own private ASN. Otherwise, Amazon provides a default ASN. For more information, see [Create a Virtual Private Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg) in the Amazon VPC User Guide. For connecting to a VPC through a Direct Connect gateway, you need the Direct Connect gateway. For more information, see [Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html). | 
| VLAN | A unique virtual local area network (VLAN) tag that's not already in use on your connection. The value must be between 1 and 4094 and must comply with the Ethernet 802.1Q standard. This tag is required for any traffic traversing the Direct Connect connection. If you have a hosted connection, your AWS Direct Connect Partner provides this value. You can’t modify the value after you have created the virtual interface. | 
| Peer IP addresses |  A virtual interface can support a BGP peering session for IPv4, IPv6, or one of each (dual-stack). Do not use Elastic IPs (EIPs) or Bring your own IP addresses (BYOIP) from the Amazon Pool to create a public virtual interface. You cannot create multiple BGP sessions for the same IP addressing family on the same virtual interface. The IP address ranges are assigned to each end of the virtual interface for the BGP peering session. +  IPv4:   (Public virtual interface only) You must specify unique public IPv4 addresses that you own. The value can be one of the following:  A customer-owned IPv4 CIDR <br />These can be any public IPs (customer-owned or provided by AWS), but the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/31` range, such as `203.0.113.0/31`, you could use `203.0.113.0` for your peer IP and `203.0.113.1` for the AWS peer IP. Or, if you allocate a `/24` range, such as `198.51.100.0/24`, you could use `198.51.100.10` for your peer IP and `198.51.100.20` for the AWS peer IP.  An IP range owned by your AWS Direct Connect Partner or ISP, along with an LOA-CFA authorization  An AWS-provided /31 CIDR. Contact [AWS Support](https://aws.amazon.com/support/createCase) to request a public IPv4 CIDR (and provide a use case in your request)We cannot guarantee that we will be able to fulfill all requests for AWS-provided public IPv4 addresses.     (Private virtual interface only) Amazon can generate private IPv4 addresses for you. If you specify your own, ensure that you specify private CIDRs for your router interface and the AWS Direct Connect interface only. For example, do not specify other IP addresses from your local network. Similar to a public virtual interface, the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/30` range, such as `192.168.0.0/30`, you could use `192.168.0.1` for your peer IP and `192.168.0.2` for the AWS peer IP.   <br />+  IPv6: Amazon automatically allocates you a /125 IPv6 CIDR. You cannot specify your own peer IPv6 addresses.   | 
| Address family | Whether the BGP peering session will be over IPv4 or IPv6. | 
| BGP information | +  A public or private Border Gateway Protocol (BGP) Autonomous System Number (ASN) for your side of the BGP session. If you are using a public ASN, you must own it. If you are using a private ASN, you can set a custom ASN value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 1 to 4294967294 range. Autonomous System (AS) prepending does not work if you use a private ASN for a public virtual interface. <br />+  AWS enables MD5 by default. You cannot modify this option. <br />+  An MD5 BGP authentication key. You can provide your own, or you can let Amazon generate one for you.  | 
| (Public virtual interface only) Prefixes you want to advertise |  Public IPv4 routes or IPv6 routes to advertise over BGP. You must advertise at least one prefix using BGP, up to a maximum of 1,000 prefixes.+  IPv4: The IPv4 CIDR can overlap with another public IPv4 CIDR announced using Direct Connect when either of the following is true:  The CIDRs are from different AWS Regions. Make sure that you apply BGP community tags on the public prefixes. You use AS\_PATH when you have a public ASN in an active/passive configuration.  <br />For more information, see [Routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html). <br />+  Over a Direct Connect public virtual interface, you can specify any prefix length from /1 to /32 for IPv4 and from /1 to /64 for IPv6. <br />+  You may add additional prefixes to an existing public VIF and advertise those by contacting [AWS support](https://aws.amazon.com/support/createCase). In your support case, provide a list of additional CIDR prefixes you want to add to the public VIF and advertise.  | 
| (Private and transit virtual interfaces only) Jumbo frames | The maximum transmission unit (MTU) of packets over Direct Connect. The default is 1500. Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. Jumbo frames apply only to propagated routes from Direct Connect. If you add static routes to a route table that point to your virtual private gateway, then traffic routed through the static routes is sent using 1500 MTU. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find Jumbo frame capable on the virtual interface General configuration page. | 

If your public prefixes or ASNs belong to an ISP or network carrier, AWS requests additional information from you. This can be a document using an official company letterhead, or an email from the company's domain name verifying that the network prefix/ASN can be used by you.

When you create a public virtual interface, it can take up to 72 business hours for AWS to review and approve your request.

**To provision a public virtual interface to non-VPC services**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Public**.

1. Under **Public virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol (BGP) Autonomous System Number (ASN) of your gateway.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer IP**, enter the IPv4 CIDR address to use to send traffic to AWS.

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To provide your own BGP key, enter your BGP MD5 key.

      If you do not enter a value, we generate a BGP key.

   1. To advertise prefixes to Amazon, for **Prefixes you want to advertise**, enter the IPv4 CIDR destination addresses (separated by commas) to which traffic should be routed over the virtual interface. 

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

**To provision a private virtual interface to a VPC**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Private**.

1. Under **Private virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Gateway type**, choose **Virtual private gateway**, or **Direct Connect gateway**. 

   1. For **Virtual interface owner**, choose **Another AWS account**, and then enter the AWS account.

   1. For **Virtual private gateway**, choose the virtual private gateway to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 9001 (jumbo frames), select **Jumbo MTU (MTU size 9001)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

#### Step 4: Verify your virtual interface resiliency configuration
<a name="high-res-resiliency-failover"></a>

After you have established virtual interfaces to the AWS Cloud or to Amazon VPC, perform a virtual interface failover test to verify that your configuration meets your resiliency requirements. For more information, see [Direct Connect Failover Test](#resiliency_failover). 

#### Step 5: Verify your virtual interfaces connectivity
<a name="high-resiliency-connected"></a>

After you have established virtual interfaces to the AWS Cloud or to Amazon VPC, you can verify your AWS Direct Connect connection using the following procedures. 

**To verify your virtual interface connection to the AWS Cloud**
+ Run `traceroute` and verify that the Direct Connect identifier is in the network trace.

**To verify your virtual interface connection to Amazon VPC**

1. Using a pingable AMI, such as an Amazon Linux AMI, launch an EC2 instance into the VPC that is attached to your virtual private gateway. The Amazon Linux AMIs are available in the **Quick Start** tab when you use the instance launch wizard in the Amazon EC2 console. For more information, see [Launch an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance_linux.html) in the *Amazon EC2 User Guide.* Ensure that the security group that's associated with the instance includes a rule permitting inbound ICMP traffic (for the ping request).

1. After the instance is running, get its private IPv4 address (for example, 10.0.0.4). The Amazon EC2 console displays the address as part of the instance details.

1. Ping the private IPv4 address and get a response.

### Configure AWS Direct Connect for development and test resiliency with the AWS Direct Connect Resiliency Toolkit
<a name="devtest-resiliency-set-up"></a>

In this example, the Direct Connect Resiliency Toolkit is used to configure a development and test resiliency model

**Topics**
+ [Step 1: Sign up for AWS](#dev-test-signup)
+ [Step 2: Configure the resiliency model](#dev-test-select-model)
+ [Step 3: Create a virtual interface](#dev-test-createvirtualinterface)
+ [Step 4: Verify your virtual interface resiliency configuration](#dev-test-resiliency-failover)
+ [Step 5: Verify your virtual interface](#dev-test-connected)

#### Step 1: Sign up for AWS
<a name="dev-test-signup"></a>

To use Direct Connect, you need an AWS account if you don't already have one.

##### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

#### Step 2: Configure the resiliency model
<a name="dev-test-select-model"></a>

**To configure the resiliency model**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**, and then choose **Create a connection**.

1. Under **Connection ordering type**, choose **Connection wizard**.

1. Under **Resiliency level**, choose **Development and test**, and then choose **Next**.

1. On the **Configure connections** pane, under **Connection settings,** do the following:

   1. For **bandwidth**, choose the connection bandwidth.

      This bandwidth applies to all of the created connections.

   1. For **First location service provider**, select the appropriate Direct Connect location.

   1. If applicable, for **First Sub location**, choose the floor closest to you or your network provider. This option is only available if the location has meet-me rooms (MMRs) on multiple floors of the building.

   1. If you selected **Other** for **First location service provider**, for **Name of other provider**, enter the name of the partner that you use.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Next**.

1. Review your connections, and then choose **Continue**.

   If your LOAs are ready, you can choose **Download LOA**, and then click **Continue**.

   It can take up to 72 business hours for AWS to review your request and provision a port for your connection. During this time, you might receive an email with a request for more information about your use case or the specified location. The email is sent to the email address that you used when you signed up for AWS. You must respond within 7 days or the connection is deleted. 

#### Step 3: Create a virtual interface
<a name="dev-test-createvirtualinterface"></a>

To begin using your Direct Connect connection, you must create a virtual interface. You can create a private virtual interface to connect to your VPC. Or, you can create a public virtual interface to connect to public AWS services that aren't in a VPC. When you create a private virtual interface to a VPC, you need a private virtual interface for each VPC that you're connecting to. For example, you need three private virtual interfaces to connect to three VPCs.

Before you begin, ensure that you have the following information:


| Resource | Required information | 
| --- | --- | 
| Connection | The Direct Connect connection or link aggregation group (LAG) for which you are creating the virtual interface. | 
| Virtual interface name | A name for the virtual interface. | 
| Virtual interface owner | If you're creating the virtual interface for another account, you need the AWS account ID of the other account. | 
| (Private virtual interface only) Connection | For connecting to a VPC in the same AWS Region, you need the virtual private gateway for your VPC. The ASN for the Amazon side of the BGP session is inherited from the virtual private gateway. When you create a virtual private gateway, you can specify your own private ASN. Otherwise, Amazon provides a default ASN. For more information, see [Create a Virtual Private Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg) in the Amazon VPC User Guide. For connecting to a VPC through a Direct Connect gateway, you need the Direct Connect gateway. For more information, see [Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html). | 
| VLAN | A unique virtual local area network (VLAN) tag that's not already in use on your connection. The value must be between 1 and 4094 and must comply with the Ethernet 802.1Q standard. This tag is required for any traffic traversing the Direct Connect connection. If you have a hosted connection, your AWS Direct Connect Partner provides this value. You can’t modify the value after you have created the virtual interface. | 
| Peer IP addresses |  A virtual interface can support a BGP peering session for IPv4, IPv6, or one of each (dual-stack). Do not use Elastic IPs (EIPs) or Bring your own IP addresses (BYOIP) from the Amazon Pool to create a public virtual interface. You cannot create multiple BGP sessions for the same IP addressing family on the same virtual interface. The IP address ranges are assigned to each end of the virtual interface for the BGP peering session. +  IPv4:   (Public virtual interface only) You must specify unique public IPv4 addresses that you own. The value can be one of the following:  A customer-owned IPv4 CIDR <br />These can be any public IPs (customer-owned or provided by AWS), but the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/31` range, such as `203.0.113.0/31`, you could use `203.0.113.0` for your peer IP and `203.0.113.1` for the AWS peer IP. Or, if you allocate a `/24` range, such as `198.51.100.0/24`, you could use `198.51.100.10` for your peer IP and `198.51.100.20` for the AWS peer IP.  An IP range owned by your AWS Direct Connect Partner or ISP, along with an LOA-CFA authorization  An AWS-provided /31 CIDR. Contact [AWS Support](https://aws.amazon.com/support/createCase) to request a public IPv4 CIDR (and provide a use case in your request)We cannot guarantee that we will be able to fulfill all requests for AWS-provided public IPv4 addresses.     (Private virtual interface only) Amazon can generate private IPv4 addresses for you. If you specify your own, ensure that you specify private CIDRs for your router interface and the AWS Direct Connect interface only. For example, do not specify other IP addresses from your local network. Similar to a public virtual interface, the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/30` range, such as `192.168.0.0/30`, you could use `192.168.0.1` for your peer IP and `192.168.0.2` for the AWS peer IP.   <br />+  IPv6: Amazon automatically allocates you a /125 IPv6 CIDR. You cannot specify your own peer IPv6 addresses.   | 
| Address family | Whether the BGP peering session will be over IPv4 or IPv6. | 
| BGP information | +  A public or private Border Gateway Protocol (BGP) Autonomous System Number (ASN) for your side of the BGP session. If you are using a public ASN, you must own it. If you are using a private ASN, you can set a custom ASN value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 1 to 4294967294 range. Autonomous System (AS) prepending does not work if you use a private ASN for a public virtual interface. <br />+  AWS enables MD5 by default. You cannot modify this option. <br />+  An MD5 BGP authentication key. You can provide your own, or you can let Amazon generate one for you.  | 
| (Public virtual interface only) Prefixes you want to advertise |  Public IPv4 routes or IPv6 routes to advertise over BGP. You must advertise at least one prefix using BGP, up to a maximum of 1,000 prefixes.+  IPv4: The IPv4 CIDR can overlap with another public IPv4 CIDR announced using Direct Connect when either of the following is true:  The CIDRs are from different AWS Regions. Make sure that you apply BGP community tags on the public prefixes. You use AS\_PATH when you have a public ASN in an active/passive configuration.  <br />For more information, see [Routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html). <br />+  Over a Direct Connect public virtual interface, you can specify any prefix length from /1 to /32 for IPv4 and from /1 to /64 for IPv6. <br />+  You may add additional prefixes to an existing public VIF and advertise those by contacting [AWS support](https://aws.amazon.com/support/createCase). In your support case, provide a list of additional CIDR prefixes you want to add to the public VIF and advertise.  | 
| (Private and transit virtual interfaces only) Jumbo frames | The maximum transmission unit (MTU) of packets over Direct Connect. The default is 1500. Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. Jumbo frames apply only to propagated routes from Direct Connect. If you add static routes to a route table that point to your virtual private gateway, then traffic routed through the static routes is sent using 1500 MTU. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find Jumbo frame capable on the virtual interface General configuration page. | 

If your public prefixes or ASNs belong to an ISP or network carrier, we request additional information from you. This can be a document using an official company letterhead, or an email from the company's domain name verifying that the network prefix/ASN can be used by you.

When you create a public virtual interface, it can take up to 72 business hours for AWS to review and approve your request.

**To provision a public virtual interface to non-VPC services**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Public**.

1. Under **Public virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol (BGP) Autonomous System Number (ASN) of your gateway.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer IP**, enter the IPv4 CIDR address to use to send traffic to AWS.

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To provide your own BGP key, enter your BGP MD5 key.

      If you do not enter a value, we generate a BGP key.

   1. To advertise prefixes to Amazon, for **Prefixes you want to advertise**, enter the IPv4 CIDR destination addresses (separated by commas) to which traffic should be routed over the virtual interface. 

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

**To provision a private virtual interface to a VPC**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Private**.

1. Under **Private virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Gateway type**, choose **Virtual private gateway**, or **Direct Connect gateway**. 

   1. For **Virtual interface owner**, choose **Another AWS account**, and then enter the AWS account.

   1. For **Virtual private gateway**, choose the virtual private gateway to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 9001 (jumbo frames), select **Jumbo MTU (MTU size 9001)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

#### Step 4: Verify your virtual interface resiliency configuration
<a name="dev-test-resiliency-failover"></a>

After you have established virtual interfaces to the AWS Cloud or to Amazon VPC, perform a virtual interface failover test to verify that your configuration meets your resiliency requirements. For more information, see [Direct Connect Failover Test](#resiliency_failover). 

#### Step 5: Verify your virtual interface
<a name="dev-test-connected"></a>

After you have established virtual interfaces to the AWS Cloud or to Amazon VPC, you can verify your AWS Direct Connect connection using the following procedures. 

**To verify your virtual interface connection to the AWS Cloud**
+ Run `traceroute` and verify that the Direct Connect identifier is in the network trace.

**To verify your virtual interface connection to Amazon VPC**

1. Using a pingable AMI, such as an Amazon Linux AMI, launch an EC2 instance into the VPC that is attached to your virtual private gateway. The Amazon Linux AMIs are available in the **Quick Start** tab when you use the instance launch wizard in the Amazon EC2 console. For more information, see [Launch an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance_linux.html) in the *Amazon EC2 User Guide.* Ensure that the security group that's associated with the instance includes a rule permitting inbound ICMP traffic (for the ping request).

1. After the instance is running, get its private IPv4 address (for example, 10.0.0.4). The Amazon EC2 console displays the address as part of the instance details.

1. Ping the private IPv4 address and get a response.

### Direct Connect Failover Test
<a name="resiliency_failover"></a>

The AWS Direct Connect Resiliency Toolkit resiliency models are designed to ensure that you have the appropriate number of virtual interface connections in multiple locations. After you complete the wizard, use the AWS Direct Connect Resiliency Toolkit failover test to bring down the BGP peering session in order to verify that traffic routes to one of your redundant virtual interfaces, and meets your resiliency requirements.

Use the test to make sure that traffic routes over redundant virtual interfaces when a virtual interface is out of service. You start the test by selecting a virtual interface, BGP peering session, and how long to run the test. AWS places the selected virtual interface BGP peering session in the down state. When the interface is in this state, traffic should go over a redundant virtual interface. If your configuration does not contain the appropriate redundant connections, the BGP peering session fails, and traffic does not get routed. When the test completes, or you manually stop the test, AWS restores the BGP session. After the test is complete, you can use the AWS Direct Connect Resiliency Toolkit to adjust your configuration.

**Note**  
Do not use this feature during a Direct Connect maintenance period as the BGP session might be restored prematurely either during or after the maintenance.

#### Test history
<a name="test_history"></a>

AWS deletes the test history after 365 days. The test history includes the status for tests that were run on all BGP peers. The history includes which BGP peering sessions were tested, the start and end times, and the test status, which can be any of the following values:
+ **In progress** - The test is currently running.
+ **Completed** - The test ran for the time that you specified.
+ **Cancelled** - The test was cancelled before the specified time.
+ **Failed** - The test did not run for the time that you specified. This can happen when there is an issue with the router.

For more information, see [View AWS Direct Connect Resiliency Toolkit virtual interface failover test history](#view_failover_test).

#### Validation permissions
<a name="permissions"></a>

The only account that has permission to run the failover test is the account that owns the virtual interface. The account owner receives an indication through AWS CloudTrail that a test ran on a virtual interface.

**Topics**
+ [Test history](#test_history)
+ [Validation permissions](#permissions)
+ [Start a virtual interface failover test](#start_failover_test)
+ [View a virtual interface failover test history](#view_failover_test)
+ [Stop a virtual interface failover test](#stop_failover_test)

#### Start an AWS Direct Connect Resiliency Toolkit virtual interface failover test
<a name="start_failover_test"></a>

You can start the virtual interface failover test using the Direct Connect console, or the AWS CLI.

**To start the virtual interface failover test from the Direct Connect console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Virtual interfaces**.

1. Select the virtual interfaces and then choose **Actions**, **Bring down BGP**.

   You can run the test on a public, private, or transit virtual interface.

1. In the **Start failure test** dialog box, do the following:

   1. For **Peerings to bring down to test**, choose which peering sessions to test, for example IPv4.

   1. For **Test maximum time**, enter the number of minutes that the test will last.

      The maximum value is 4,320 minutes (72 business hours).

      The default value is 180 minutes (3 hours).

   1. For **To confirm test**, enter **Confirm**.

   1. Choose **Confirm**.

   The BGP peering session is placed in the DOWN state. You can send traffic to verify that there are no outages. If needed, you can stop the test immediately.

**To start the virtual interface failover test using the AWS CLI**  
Use [StartBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StartBgpFailoverTest.html).

#### View AWS Direct Connect Resiliency Toolkit virtual interface failover test history
<a name="view_failover_test"></a>

You can view the virtual interface failover test history using the Direct Connect console, or the AWS CLI.

**To view the virtual interface failover test history from the Direct Connect console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Virtual interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Choose **Test history**.

   The console displays the virtual interface tests that you performed for the virtual interface.

1. To view the details for a specific test, select the test id.

**To view the virtual interface failover test history using the AWS CLI**  
Use [ListVirtualInterfaceTestHistory](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html).

#### Stop an AWS Direct Connect Resiliency Toolkit virtual interface failover test
<a name="stop_failover_test"></a>

You can stop the virtual interface failover test using the Direct Connect console, or the AWS CLI.

**To stop the virtual interface failover test from the Direct Connect console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Virtual interfaces**.

1. Select the virtual interface, and then choose **Actions**, **Cancel test**.

1. Choose **Confirm**.

AWS restores the BGP peering session. The testing history displays "cancelled" for the test. 

**To stop the virtual interface failover test using the AWS CLI**  
Use [StopBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html).

## Direct Connect Classic connection
<a name="classic_connection"></a>

A Classic connection offers a straightforward approach to establishing dedicated network connectivity between your on-premises infrastructure and AWS. This connection type is ideal for organizations that prefer to manage their own network configurations and have existing Direct Connect infrastructure in place. The Classic connection does not rely on the AWS Direct Connect Resiliency Toolkit.

Select Classic when you have existing connections and you want to add additional connections. A Classic connection has a 95% SLA. However, it does not provide resiliency or redundancy, which are found only in the AWS Direct Connect Resiliency Toolkit when creating a connection.

**Note**  
Before you configure a Classic connection, familiarize yourself with the [Connection prerequisites](#connect-prereqs.title).

**Topics**
+ [Configure a Classic connection](#toolkit-classic)

### Configure a Direct Connect Classic connection
<a name="toolkit-classic"></a>

Configure a Classic connection when you have existing Direct Connect connections.

#### Step 1: Sign up for AWS
<a name="get-started-signup"></a>

To use Direct Connect, you need an account if you don't already have one.

##### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

#### Step 2: Request a Direct Connect dedicated connection
<a name="ConnectionRequest"></a>

For dedicated connections, you can submit a connection request using the Direct Connect console. For hosted connections, work with an AWS Direct Connect Partner to request a hosted connection. Ensure that you have the following information:
+ The port speed that you require. You cannot change the port speed after you create the connection request. 
+ The Direct Connect location at which the connection is to be terminated.

**Note**  
You cannot use the Direct Connect console to request a hosted connection. Instead, contact an AWS Direct Connect Partner, who can create a hosted connection for you, which you then accept. Skip the following procedure and go to [Accept your hosted connection](#get-started-accept-hosted-connection).

**To create a new Direct Connect connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane choose **Connections**, and then choose **Create a connection**.

1. Choose **Classic**.

1. On the **Create Connection** pane, under **Connection settings,** do the following:

   1. For **Name**, enter a name for the connection.

   1. For **Location**, select the appropriate Direct Connect location.

   1. If applicable, for **Sub Location**, choose the floor closest to you or your network provider. This option is only available if the location has meet-me rooms (MMRs) in multiple floors of the building.

   1. For **Port Speed**, choose the connection bandwidth.

   1. For **On-premises**, select **Connect through a Direct Connect partner** when you use this connection to connect to your data center.

   1. For **Service provider**, select the AWS Direct Connect Partner. If you use a partner that is not in the list, select **Other**.

   1. If you selected **Other** for **Service provider**, for** Name of other provider**, enter the name of the partner that you use.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create Connection**.

It can take up to 72 business hours for AWS to review your request and provision a port for your connection. During this time, you might receive an email with a request for more information about your use case or the specified location. The email is sent to the email address that you used when you signed up for AWS. You must respond within 7 days or the connection is deleted.

For more information, see [Direct Connect dedicated and hosted connections](#WorkingWithConnections).

##### Accept your hosted connection
<a name="get-started-accept-hosted-connection"></a>

 You must accept the hosted connection in the Direct Connect console before you can create a virtual interface. This step only applies to hosted connections.

**To accept a hosted virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**. 

1. Select the hosted connection, and then choose **Accept**.

   Choose **Accept**.

#### (Dedicated connection) Step 3: Download the LOA-CFA
<a name="DedicatedConnection"></a>

After you request a connection, we make a Letter of Authorization and Connecting Facility Assignment (LOA-CFA) available to you to download, or emails you with a request for more information. The LOA-CFA is the authorization to connect to AWS, and is required by the colocation provider or your network provider to establish the cross-network connection (cross-connect).

**To download the LOA-CFA**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the connection and choose **View Details**.

1. Choose **Download LOA-CFA**.

   The LOA-CFA is downloaded to your computer as a PDF file.
**Note**  
If the link is not enabled, the LOA-CFA is not yet available for you to download. Check your email for a request for more information. If it's still unavailable, or you haven't received an email after 72 business hours, contact [AWS Support](https://aws.amazon.com/support/createCase).

1. After you download the LOA-CFA, do one of the following:
   + If you're working with an AWS Direct Connect Partner or network provider, send them the LOA-CFA so that they can order a cross-connect for you at the Direct Connect location. If they cannot order the cross-connect for you, you can [contact the colocation provider](#Colocation) directly.
   + If you have equipment at the Direct Connect location, contact the colocation provider to request a cross-network connection. You must be a customer of the colocation provider. You must also present them with the LOA-CFA that authorizes the connection to the AWS router, and the necessary information to connect to your network.

Direct Connect locations that are listed as multiple sites (for example, Equinix DC1-DC6 & DC10-DC11) are set up as a campus. If your or your network provider’s equipment is located in any of these sites, you can request a cross-connect to your assigned port even if it resides in a different campus building. 

**Important**  
A campus is treated as a single Direct Connect location. To achieve high availability, configure connections to different Direct Connect locations.

If you or your network provider experience issues establishing a physical connection, see [Troubleshoot layer 1 (physical) issues](#ts_layer_1).

#### Step 4: Create a virtual interface
<a name="createvirtualinterface"></a>

To begin using your Direct Connect connection, you must create a virtual interface. You can create a private virtual interface to connect to your VPC. Or, you can create a public virtual interface to connect to public AWS services that aren't in a VPC. When you create a private virtual interface to a VPC, you need a private virtual interface for each VPC to which to connect. For example, you need three private virtual interfaces to connect to three VPCs.

Before you begin, ensure that you have the following information:


| Resource | Required information | 
| --- | --- | 
| Connection | The Direct Connect connection or link aggregation group (LAG) for which you are creating the virtual interface. | 
| Virtual interface name | A name for the virtual interface. | 
| Virtual interface owner | If you're creating the virtual interface for another account, you need the AWS account ID of the other account. | 
| (Private virtual interface only) Connection | For connecting to a VPC in the same AWS Region, you need the virtual private gateway for your VPC. The ASN for the Amazon side of the BGP session is inherited from the virtual private gateway. When you create a virtual private gateway, you can specify your own private ASN. Otherwise, Amazon provides a default ASN. For more information, see [Create a Virtual Private Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg) in the Amazon VPC User Guide. For connecting to a VPC through a Direct Connect gateway, you need the Direct Connect gateway. For more information, see [Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html). | 
| VLAN | A unique virtual local area network (VLAN) tag that's not already in use on your connection. The value must be between 1 and 4094 and must comply with the Ethernet 802.1Q standard. This tag is required for any traffic traversing the Direct Connect connection. If you have a hosted connection, your AWS Direct Connect Partner provides this value. You can’t modify the value after you have created the virtual interface. | 
| Peer IP addresses |  A virtual interface can support a BGP peering session for IPv4, IPv6, or one of each (dual-stack). Do not use Elastic IPs (EIPs) or Bring your own IP addresses (BYOIP) from the Amazon Pool to create a public virtual interface. You cannot create multiple BGP sessions for the same IP addressing family on the same virtual interface. The IP address ranges are assigned to each end of the virtual interface for the BGP peering session. +  IPv4:   (Public virtual interface only) You must specify unique public IPv4 addresses that you own. The value can be one of the following:  A customer-owned IPv4 CIDR <br />These can be any public IPs (customer-owned or provided by AWS), but the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/31` range, such as `203.0.113.0/31`, you could use `203.0.113.0` for your peer IP and `203.0.113.1` for the AWS peer IP. Or, if you allocate a `/24` range, such as `198.51.100.0/24`, you could use `198.51.100.10` for your peer IP and `198.51.100.20` for the AWS peer IP.  An IP range owned by your AWS Direct Connect Partner or ISP, along with an LOA-CFA authorization  An AWS-provided /31 CIDR. Contact [AWS Support](https://aws.amazon.com/support/createCase) to request a public IPv4 CIDR (and provide a use case in your request)We cannot guarantee that we will be able to fulfill all requests for AWS-provided public IPv4 addresses.     (Private virtual interface only) Amazon can generate private IPv4 addresses for you. If you specify your own, ensure that you specify private CIDRs for your router interface and the AWS Direct Connect interface only. For example, do not specify other IP addresses from your local network. Similar to a public virtual interface, the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/30` range, such as `192.168.0.0/30`, you could use `192.168.0.1` for your peer IP and `192.168.0.2` for the AWS peer IP.   <br />+  IPv6: Amazon automatically allocates you a /125 IPv6 CIDR. You cannot specify your own peer IPv6 addresses.   | 
| Address family | Whether the BGP peering session will be over IPv4 or IPv6. | 
| BGP information | +  A public or private Border Gateway Protocol (BGP) Autonomous System Number (ASN) for your side of the BGP session. If you are using a public ASN, you must own it. If you are using a private ASN, you can set a custom ASN value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 1 to 4294967294 range. Autonomous System (AS) prepending does not work if you use a private ASN for a public virtual interface. <br />+  AWS enables MD5 by default. You cannot modify this option. <br />+  An MD5 BGP authentication key. You can provide your own, or you can let Amazon generate one for you.  | 
| (Public virtual interface only) Prefixes you want to advertise |  Public IPv4 routes or IPv6 routes to advertise over BGP. You must advertise at least one prefix using BGP, up to a maximum of 1,000 prefixes.+  IPv4: The IPv4 CIDR can overlap with another public IPv4 CIDR announced using Direct Connect when either of the following is true:  The CIDRs are from different AWS Regions. Make sure that you apply BGP community tags on the public prefixes. You use AS\_PATH when you have a public ASN in an active/passive configuration.  <br />For more information, see [Routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html). <br />+  Over a Direct Connect public virtual interface, you can specify any prefix length from /1 to /32 for IPv4 and from /1 to /64 for IPv6. <br />+  You may add additional prefixes to an existing public VIF and advertise those by contacting [AWS support](https://aws.amazon.com/support/createCase). In your support case, provide a list of additional CIDR prefixes you want to add to the public VIF and advertise.  | 
| (Private and transit virtual interfaces only) Jumbo frames | The maximum transmission unit (MTU) of packets over Direct Connect. The default is 1500. Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. Jumbo frames apply only to propagated routes from Direct Connect. If you add static routes to a route table that point to your virtual private gateway, then traffic routed through the static routes is sent using 1500 MTU. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find Jumbo frame capable on the virtual interface General configuration page. | 

We request additional information from you if your public prefixes or ASNs belong to an ISP or network carrier. This can be a document using an official company letterhead or an email from the company's domain name verifying that the network prefix/ASN may be used by you.

For private virtual interface and public virtual interfaces, the maximum transmission unit (MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a private virtual interface can be either 1500 or 9001 (jumbo frames). The MTU of a transit virtual interface can be either 1500 or 8500 (jumbo frames). You can specify the MTU when you create the interface or update it after you create it. Setting the MTU of a virtual interface to 8500 (jumbo frames) or 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find **Jumbo Frame Capable** on the **Summary** tab.

When you create a public virtual interface, it can take up to 72 business hours for AWS to review and approve your request.

**To provision a public virtual interface to non-VPC services**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Public**.

1. Under **Public virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the The Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface. The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer IP**, enter the IPv4 CIDR address to use to send traffic to AWS.

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To provide your own BGP key, enter your BGP MD5 key.

      If you do not enter a value, we generate a BGP key.

   1. To advertise prefixes to Amazon, for **Prefixes you want to advertise**, enter the IPv4 CIDR destination addresses (separated by commas) to which traffic should be routed over the virtual interface. 

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

**To provision a private virtual interface to a VPC**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Private**.

1. Under **Private virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Gateway type**, choose **Virtual private gateway**, or **Direct Connect gateway**. 

   1. For **Virtual interface owner**, choose **Another AWS account**, and then enter the AWS account.

   1. For **Virtual private gateway**, choose the virtual private gateway to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 9001 (jumbo frames), select **Jumbo MTU (MTU size 9001)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

1. You need to use your BGP device to advertise the network that you use for the public VIF connection. 

#### Step 5: Download the router configuration
<a name="routerconfig"></a>

After you have created a virtual interface for your Direct Connect connection, you can download the router configuration file. The file contains the necessary commands to configure your router for use with your private or public virtual interface.

**To download a router configuration**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the connection and choose **View Details**.

1. Choose **Download router configuration**.

1. For **Download router configuration**, do the following:

   1. For **Vendor**, select the manufacturer of your router.

   1. For **Platform**, select the model of your router.

   1. For **Software**, select the software version for your router.

1. Choose **Download**, and then use the appropriate configuration for your router to ensure that you can connect to Direct Connect.

For more information about manually configuring your router, see [Download the router configuration file](#vif-router-config).

After you configure your router, the status of the virtual interface goes to `UP`. If the virtual interface remains down and you cannot ping the Direct Connect device's peer IP address, see [Troubleshoot layer 2 (data link) issues](#ts-layer-2). If you can ping the peer IP address, see [Troubleshoot layer 3/4 (Network/Transport) issues](#ts-layer-3). If the BGP peering session is established but you cannot route traffic, see [Troubleshoot routing issues](#ts-routing).

#### Step 6: Verify your virtual interface
<a name="connected"></a>

After you have established virtual interfaces to the AWS Cloud or to Amazon VPC, you can verify your AWS Direct Connect connection using the following procedures. 

**To verify your virtual interface connection to the AWS Cloud**
+ Run `traceroute` and verify that the Direct Connect identifier is in the network trace.

**To verify your virtual int\+erface connection to Amazon VPC**

1. Using a pingable AMI, such as an Amazon Linux AMI, launch an EC2 instance into the VPC that is attached to your virtual private gateway. The Amazon Linux AMIs are available in the **Quick Start** tab when you use the instance launch wizard in the Amazon EC2 console. For more information, see [Launch an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance_linux.html) in the *Amazon EC2 User Guide.* Ensure that the security group that's associated with the instance includes a rule permitting inbound ICMP traffic (for the ping request).

1. After the instance is running, get its private IPv4 address (for example, 10.0.0.4). The Amazon EC2 console displays the address as part of the instance details.

1. Ping the private IPv4 address and get a response.

#### (Recommended) Step 7: Configure redundant connections
<a name="RedundantConnections"></a>

To provide for failover, we recommend that you request and configure two dedicated connections to AWS, as shown in the following figure. These connections can terminate on one or two routers in your network.

![Redundant connection diagram](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/redundant_connection.png)


There are different configuration choices available when you provision two dedicated connections:
+ Active/Active (BGP multipath). This is the default configuration, where both connections are active. Direct Connect supports multipathing to multiple virtual interfaces within the same location, and traffic is load-shared between interfaces based on flow. If one connection becomes unavailable, all traffic is routed through the other connection.
+ Active/Passive (failover). One connection is handling traffic, and the other is on standby. If the active connection becomes unavailable, all traffic is routed through the passive connection. You need to prepend the AS path to the routes on one of your links for that to be the passive link.

How you configure the connections doesn't affect redundancy, but it does affect the policies that determine how your data is routed over both connections. We recommend that you configure both connections as active.

If you use a VPN connection for redundancy, ensure that you implement a health check and failover mechanism. If you use either of the following configurations, then you need to check your [route table routing](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-configure-routing) to route to the new network interface. 
+ You use your own instances for routing, for example the instance is the firewall. 
+ You use your own instance that terminates a VPN connection.

To achieve high availability, we strongly recommend that you configure connections to different Direct Connect locations. 

For more information about Direct Connect resiliency, see [Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/).

# Direct Connect maintenance
<a name="dx-maintenance"></a>

Direct Connect is committed to ensuring service security, availability, and scalability. To maintain these standards, periodic maintenance is required on the hardware network devices. Direct Connect maintenance is divided into two types - **planned** and **emergency**.

These maintenance events include addressing security vulnerabilities, hardware issues, performing device migrations to comply with standards, fixing defects, and delivering new features. By following the practices described in [Maintenance event preparation](#overview-maintenance-prep), you can better prepare your Direct Connect environment to avoid disruptions during maintenance events. If you have a non-resilient network setup or a single connection, you’ll experience an interruption in connectivity between your on-premises network and AWS resources.

Direct Connect sends email notifications about planned and emergency maintenance events to the email address associated with the AWS account that owns the Direct Connect connection or virtual interface resource. If you’re using a Direct Connect hosted connection with one of the Direct Connect Delivery Partners, email notifications are sent to both you and the partner account about the maintenance event. You can also add additional email addresses or distribution lists to receive notifications. See [Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html) for more information.

**Topics**
+ [Planned maintenance](#operations-maintenance-planned)
+ [Emergency maintenance](#operations-maintenance-emergency)
+ [Third-party maintenance](#operations-maintenance-partner)
+ [Maintenance event preparation](#overview-maintenance-prep)
+ [Maintenance event postponement](#operations-maintenance-rescehedule)

## Direct Connect planned maintenance
<a name="operations-maintenance-planned"></a>

Planned maintenance events involve network upgrades such as operating system patching and configuration updates on hardware device endpoints that are required to improve availability and deliver new features. 

These maintenance events are scheduled 14 days in advance and typically occur during a four-hour window in low-traffic hours at the Direct Connect location where the device endpoint resides. Maintenance activities usually complete before the full four-hour window expires and you’ll receive a notification once work is complete. In rare cases where unforeseen circumstances require extending the maintenance window, we'll send a separate notification with the revised completion estimate. 

Using the following schedule, the initial notification and reminder notifications are sent to the AWS account that owns the resource:
+ 14 calendar days before planned maintenance event,
+ 7 calendar days before planned maintenance event, and 
+ 1 day prior to the planned maintenance event. 

**Note**  
Calendar days include non-business days and local holidays. 

In addition, 
+ Receive notifications in your monitoring or ticketing system by integrating with AWS Health. To integrate AWS Health, see [Monitoring events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) in the *AWS Health User Guide*.
+ View planned maintenance schedules on your [Health Dashboard](https://health.aws.amazon.com/health/status).

Under rare circumstances, a planned maintenance event cannot happen as scheduled. Should this occur, we'll send a cancellation notification and will reschedule the event in the future following the same process as above.

## Direct Connect emergency maintenance
<a name="operations-maintenance-emergency"></a>

Emergency maintenance events are initiated on a critical basis to prevent imminent service impacting events or resolve impairments which have already resulted in a disruption to connectivity. In such cases, taking immediate action is necessary to restore the affected endpoint to a healthy state.

While we strive to provide advance notice whenever possible, some situations may require maintenance to start immediately. You will receive notifications when emergency maintenance is scheduled or underway, and again when it is completed.

These events typically occur during a two-hour window at the Direct Connect location where the device endpoint resides. Maintenance activities usually complete within this window. In cases where unforeseen circumstances require extending the maintenance window, such as hardware replacement, we’ll send a separate notification with the revised completion estimate.

## Third-party maintenance
<a name="operations-maintenance-partner"></a>

Beyond AWS initiated maintenance events, your Direct Connect Delivery partner or network service provider who is providing network connectivity from your on-premises to the Direct Connect location might perform maintenance activities. Direct Connect Delivery partners receive maintenance event notifications from AWS so that they can plan their own maintenance schedules to avoid overlap. AWS does not have visibility into a partner’s maintenance activities, so you’ll need to check with them for their scheduling process, notification methods, and best practices.

## Maintenance event preparation
<a name="overview-maintenance-prep"></a>

To ensure production workloads continue to function during a maintenance event, Direct Connect recommends that you use the AWS Direct Connect Resiliency Toolkit to configure your network connections for maximum resiliency. For an example model of maximum resiliency, see [Maximum resiliency](#maximum_resiliency).

Using maximum resiliency, connections are spread across at least two Direct Connect locations, with termination on two unique device endpoints within each Direct Connect location. This provides multiple layers of redundancy, which reduces the risk of a single endpoint failure and helps to maintain connectivity during maintenance events. Direct Connect will never schedule a planned maintenance event that will simultaneously take down your redundant connections. For the steps to use the AWS Direct Connect Resiliency Toolkit to configure maximum resiliency, see [Configure maximum resiliency](#max-resiliency-set-up).

During a planned maintenance event, Direct Connect drains traffic to and from the connection endpoint undergoing maintenance and forces traffic to use your redundant connections. This allows for more seamless network traffic re-routing without the need for manual intervention if maximum resiliency were not configured. Alternately, you might choose to control traffic re-routing between redundant connections during the maintenance windows by using local preference Border Gateway Protocol (BGP) communities. For more information about BGP communities, see [Routing policies and BGP communities](#routing-and-bgp).

Configuring your Direct Connect environment with the maximum resiliency model helps ensure your business is not impacted during maintenance events and infrastructure failures. When properly implemented and tested, you typically do not need to take any actions for these maintenance events.

### Resiliency validation
<a name="operations-maintenance-validate"></a>

If you’ve configured your Direct Connect environment to be resilient, regularly validate that your traffic routes through other redundant connections when a connection is out-of-service. Regular proactive testing can help identify and resolve any potential issues before they impact production workloads during a real maintenance event or failure scenario. This will ensure greater confidence in the reliability of your network during a maintenance event. Use the Direct Connect Failover test to validate the resiliency of your redundant connections. For the steps to use the Direct Connect Failover test, see [Direct Connect failover test](#resiliency_failover).

You can also leverage Amazon CloudWatch Network Monitor to provide active monitoring of your Direct Connect connections. For more information, see [Monitor hybrid connectivity with Amazon CloudWatch Network Synthetic Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/).

You can also use the Network Resilience Agent, an open-source sample solution, to discover, visualize, and assess your Direct Connect topology against resiliency best practices. For more information, see [Network Resilience Agent](https://github.com/aws-samples/sample-network-resilience-agent) on GitHub.

## Requests for maintenance event postponement or cancellation
<a name="operations-maintenance-rescehedule"></a>

Direct Connect devices are shared across multiple customers. Therefore, we do not accommodate specific requests for maintenance rescheduling or cancellation. Rescheduling or cancellation requests for one customer can negatively impact other customers using that endpoint. This can also pose a risk for mitigating availability or security issues in a timely manner. 

# MAC Security in Direct Connect
<a name="MACsec"></a>

MAC Security (MACsec) is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity. MACsec provides Layer 2 point-to-point encryption over the cross-connect to AWS, operating between two Layer 3 routers. While MACsec secures the connection between your router and Direct Connect location at Layer 2, AWS provides additional security by encrypting all data at the physical layer as it flows across the network between Direct Connect locations and AWS Regions. This creates a layered security approach where your traffic is protected both during initial entry into AWS and during transit across the AWS network.

In the following diagram, the Direct Connect cross-connect must be connected to a MACsec-capable interface on the customer's edge device. MACsec over Direct Connect provides layer 2 encryption for point-to-point traffic between the Direct Connect edge device and the customer's edge device. This encryption occurs after security keys are exchanged and verified between the interfaces at both ends of the cross-connect. 

**Note**  
MACsec provides point-to-point security on Ethernet links; therefore it does not provide end-to-end encryption across multiple sequential Ethernet or other network segments.

![MACsec overview](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/macsec-overview.png)


## MACsec concepts
<a name="concepts"></a>

The following are the key concepts for MACsec:
+ **MAC Security (MACsec)** — An IEEE 802.1 Layer 2 standard that provides data confidentiality, data integrity, and data origin authenticity. For more information about the protocol, see [802.1AE: MAC Security (MACsec)](https://1.ieee802.org/security/802-1ae/). 
+ **Secure association key (SAK)** — A session key that establishes the MACsec connectivity between the customer on-premises router and the connection port at the Direct Connect location. The SAK is not pre-shared, but rather automatically derived from the CKN/CAK pair through a cryptographic key generation process. This derivation happens at both ends of the connection after you provide and provision the CKN/CAK pair. The SAK is regenerated periodically for security purposes and whenever a MACsec session is established. 
+ **Connectivity Association Key Name (CKN)** and **Connectivity Association Key (CAK)** — The values in this pair are used to generate the MACsec key. You generate the pair values, associate them with a Direct Connect connection, and then provision them on your edge device at your end of the Direct Connect connection. Direct Connect supports only static CAK mode but not dynamic CAK mode. Since only static CAK mode is supported, it's recommended that you follow your own key management policies for key generation, distribution, and rotation.
+ **Key format **— The key format should use hexadecimal characters, exactly 64 characters in length. Direct Connect supports only Advanced Encryption Standard (AES) 256-bit keys for dedicated connections, which corresponds to a 64-character hexadecimal string.
+ **Key Distribution Channel** — To deliver a new CKN-CAK pair to AWS, use the AWS Console or the Direct Connect CLI or SDK using `associate-mac-sec-key`. We recommend you only use TLS 1.3 and enforce a post-quantum key exchange algorithm such as ML-KEM (Module-Lattice-Based Key Encapsulation Mechanism) when associating a new CKN-CAK pair with your dedicated connection. For more information, review the AWS [SDK and CLI guides](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html). When using the AWS Console, use a web browser that supports ML-KEM and review the connection security.
+ **Encryption modes** — Direct Connect supports two MACsec encryption modes:
  + must\_encrypt — In this mode, the connection requires MACsec encryption for all traffic. If MACsec negotiation fails or encryption cannot be established, the connection will not transmit any traffic. This mode provides the highest security guarantee but may impact availability if there are any MACsec-related issues.
  + should\_encrypt — In this mode, the connection attempts to establish MACsec encryption but will fall back to unencrypted communication if MACsec negotiation fails. This mode provides more flexibility and higher availability but may allow unencrypted traffic in certain failure scenarios.

  The encryption mode can be set during connection configuration and can be modified later. By default, new MACsec-enabled connections are set to "should\_encrypt" mode to prevent potential connectivity issues during initial setup.

## MACsec key rotation
<a name="macset-key-rotation"></a>
+ **CNN/CAK rotation (manual) **

  Direct Connect MACsec supports MACsec keychains with capacity for storing up to three CKN/CAK pairs. This allows you to manually rotate these long-term keys without connection disruption. When you associate a new CKN/CAK pair using the `associate-mac-sec-key` command, you must configure the same pair on your device. The Direct Connect device attempts to use the most recently added key. If that key doesn't match your device's key, it falls back to the previous working key, ensuring connection stability during rotation. 

  For information on using `associate-mac-sec-key`, see [associate-mac-sec-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-mac-sec-key.html).
+ **Secure Association Key (SAK) rotation (automatic)**

  The SAK, which is derived from the active CKN/CAK pair, undergoes automatic rotation based on the following:
  + time intervals
  + volume of encrypted traffic
  + MACsec session establishment

  This rotation is handled automatically by the protocol, occurs transparently without disrupting the connection, and requires no manual intervention. The SAK is never stored persistently and is regenerated through a secure key derivation process that follows the IEEE 802.1X standard.

## Supported connections
<a name="supported-connections"></a>

MACsec is available on dedicated Direct Connect connections and link aggregation groups:

**Topics**
+ [Dedicated connections](#direct-connect-mac-sec-dedicated)
+ [LAGs](#direct-connect-mac-sec-lags)
+ [Partner interconnects](#direct-connect-mac-sec-partners)

**Note**  
Partners using supported devices can use MACsec to encrypt the Layer 2 connection between their edge network device and the Direct Connect device. Partners who enable the feature can encrypt all traffic traversing the secured link. MACsec encryption operates between the two specific devices on Layer 2 and is not supported on hosted connections.

For information about how to order connections that support MACsec, see [AWS Direct Connect](https://aws.amazon.com/directconnect/?nc=sn&loc=0).

### Dedicated connections
<a name="direct-connect-mac-sec-dedicated"></a>

The following helps you become familiar with MACsec on Direct Connect dedicated connections. There are no additional charges for using MACsec. The steps to configure MACsec on a dedicated connection can be found in [Get started with MACsec on a dedicated connection](#create-macsec-dedicated).

Partner interconnect operations follow the same procedures as dedicated connections. When you run CLI or SDK commands for partner interconnects, the responses will include MACsec-related information where applicable.

#### MACsec prerequisites for dedicated connections
<a name="mac-sec-prerequisites"></a>

Note the following requirements for MACsec on dedicated connections:
+ MACsec is supported on 10 Gbps , 100 Gbps, and 400 Gbps dedicated Direct Connect connections at selected points of presence. For these connections, the following MACsec cipher suites are supported:
  +  For 10Gbps connections, GCM-AES-256 and GCM-AES-XPN-256.
  + For 100 Gbps and 400 Gbps connections, GCM-AES-XPN-256.
+ Only 256-bit MACsec keys are supported.
+ Extended Packet Numbering (XPN) is required for 100Gbps and 400 Gbps connections. For 10Gbps connections Direct Connect supports both GCM-AES-256 and GCM-AES-XPN-256. High-speed connections, such as 100 Gbps and 400 Gbps dedicated connections, can quickly exhaust MACsec’s original 32-bit packet numbering space, which would require you to rotate your encryption keys every few minutes to establish a new Connectivity Association. To avoid this situation, the IEEE Std 802.1AEbw-2013 amendment introduced extended packet numbering, increasing the numbering space to 64-bits, easing the timeliness requirement for key rotation.
+ Secure Channel Identifier (SCI) is required and must be turned on. This setting can't be adjusted.
+ IEEE 802.1Q (Dot1q/VLAN) tag offset/dot1q-in-clear is not supported for moving a VLAN tag outside of an encrypted payload.

In addition you should complete the following tasks before you configure MACsec on a dedicated connection.
+ Create a CKN/CAK pair for the MACsec key.

  You can create the pair using an open standard tool. The pair must meet the requirements specified in [Step 4: Configure your on-premises router](#associate-key-router).
+ Make sure that you have a device on your end of the connection that supports MACsec.
+ Secure Channel Identifier (SCI) must be turned on. 
+ Only 256-bit MACsec keys are supported, providing the latest advanced data protection.

### LAGs
<a name="direct-connect-mac-sec-lags"></a>

The following requirements help you become familiar with MACsec for Direct Connect link aggregation groups (LAGs):
+  LAGs must be composed of MACsec-capable dedicated connections support MACsec encryption
+ All connections within a LAG must be of the same bandwidth and support MACsec
+ MACsec configuration applies uniformly across all connections in the LAG
+ Enabling LAG creation and MACsec can be done simultaneously
+ Only a single MACsec key can be utilized across all LAG links at any time. The ability to support multiple MACsec keys is for key rotation purposes only.

### Partner interconnects
<a name="direct-connect-mac-sec-partners"></a>

The partner account that owns the interconnect can use MACsec on that physical connection or LAG. The operations are the same as for dedicated connections, however they are performed using the partner-specific API/SDK calls.

## Service-Linked roles
<a name="mac-sec-service-linked-roles"></a>

Direct Connect uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Direct Connect. Service-linked roles are predefined by Direct Connect and include all of the permissions that the service requires to call other AWS services on your behalf. A service-linked role makes setting up Direct Connect easier because you don’t have to manually add the necessary permissions. Direct Connect defines the permissions of its service-linked roles, and unless defined otherwise, only Direct Connect can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity. For more information, see [Service-linked roles for Direct Connect](#security_iam_service-with-iam-roles-service-linked).

## MACsec pre-shared CKN/CAK key considerations
<a name="mac-sec-key-consideration"></a>

AWS Direct Connect uses AWS managed CMKs for the pre-shared keys that you associate with connections or LAGs. Secrets Manager stores your pre-shared CKN and CAK pairs as a secret that the Secrets Manager’s root key encrypts. For more information, see [AWS managed CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) in the *AWS Key Management Service Developer Guide*.

The stored key is read-only by design, but you can schedule a seven- to thirty-day deletion using the AWS Secrets Manager console or API. When you schedule a deletion, the CKN cannot be read, and this might affect your network connectivity. We apply the following rules when this happens:
+ If the connection is in a pending state, we disassociate the CKN from the connection.
+ If the connection is in an available state, we notify the connection owner by email. If you do not take any action within 30 days, we disassociate the CKN from your connection.

When we disassociate the last CKN from your connection and the connection encryption mode is set to "must encrypt", we set the mode to "should\_encrypt" to prevent sudden packet loss.

## Get started using MACsec on a dedicated Direct Connect connection
<a name="create-macsec-dedicated"></a>

The following task gets you started setting up MACsec to use on a Direct Connect dedicated connection

### Step 1: Create a connection
<a name="step-create-connection"></a>

 To start using MACsec, you must turn the feature on when you create a dedicated connection. 

### (Optional) Step 2: Create a link aggregation group (LAG)
<a name="step-create-lag"></a>

 If you use multiple connections for redundancy, you can create a LAG that supports MACsec. For more information, see [MACsec considerations](#lag-macsec-considerations) and [Create a LAG](#create-lag).

### Step 3: Associate the CKN/CAK with the connection or LAG
<a name="step-associate-key"></a>

After you create the connection or LAG that supports MACsec, you need to associate a CKN/CAK with the connection. For more information, see one of the following:
+ [Associate a MACsec CKN/CAK with a connection](#associate-key-connection)
+ [Associate a MACsec CKN/CAK with a LAG](#associate-key-lag)

### Step 4: Configure your on-premises router
<a name="associate-key-router"></a>

Update your on-premises router with the MACsec secret key. The MACsec secret key on the on-premises router and in the Direct Connect location must match. For more information, see [Download the router configuration file](#vif-router-config).

### Step 5: (Optional) Remove the association between the CKN/CAK and the connection or LAG
<a name="step-disassociate-key"></a>

You can optionally remove the association between the CKN/CAK and the connection or LAG. f you need to remove the association, see one of the following:
+ [Remove the association between a MACsec secret key and a connection](#disassociate-key-connection)
+ [Remove the association between a MACsec secret key and a LAG](#disassociate-key-lag)

# Direct Connect dedicated and hosted connections
<a name="WorkingWithConnections"></a>

Direct Connect enables you to establish a dedicated network connection between your network and one of the Direct Connect locations.

There are two types of connections:
+ **Dedicated Connection**: A physical Ethernet connection associated with a single customer. Customers can request a dedicated connection through the Direct Connect console, the CLI, or the API. For more information, see [Dedicated connections](#dedicated_connection).
+ **Hosted Connection**: A physical Ethernet connection that an AWS Direct Connect Partner provisions on behalf of a customer. Customers request a hosted connection by contacting a partner in the AWS Direct Connect Partner Program, who provisions the connection. For more information, see [Hosted connections](#hosted_connection).

**Topics**
+ [Dedicated connections](#dedicated_connection)
+ [Hosted connections](#hosted_connection)
+ [Delete a connection](#deleteconnection)
+ [Update a connection](#updateconnection)
+ [View connection details](#viewdetails)

## Dedicated Direct Connect connections
<a name="dedicated_connection"></a>

To create a Direct Connect dedicated connection, you need the following information:

**Direct Connect location**  
Work with a partner in the AWS Direct Connect Partner Program to help you establish network circuits between a Direct Connect location and your data center, office, or colocation environment. They can also help provide colocation space within the same facility as the location. For more information, see [APN Partners Supporting Direct Connect](https://aws.amazon.com/directconnect/partners).

**Port speed**  
The possible values are 1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps. 

You can't change the port speed after you create the connection request. To change the port speed, you must create and configure a new connection.

You can create a connection using either the Connection wizard or create a Classic connection. Using the Connection wizard you can set up connections using resiliency recommendations. The wizard is recommended if you're setting up connections for the first time. If you prefer, you can use Classic to create connections one-at-a-time. Classic is recommended if you've already got an existing setup that you want to add connections to. You can create a standalone connection, or you can create a connection to associate with a LAG in your account. If you associate a connection with a LAG, it's created with the same port speed and location that is specified in the LAG.

After you request the connection, we make a Letter of Authorization and Connecting Facility Assignment (LOA-CFA) available to you to download or email you with a request for more information. If you receive a request for more information, you must respond within 7 days or the connection is deleted. The LOA-CFA is the authorization to connect to AWS, and is required by your network provider to order a cross connect for you. If you do not have equipment in the Direct Connect location, you cannot order a cross connect for yourself there. 

The following operations are available for dedicated connections:
+ [Create a connection using the Connection wizard](#create-connection)
+ [Create a Classic connection](#connection-classic)
+ [View Direct Connect connection details](#viewdetails)
+ [Update a Direct Connect connection](#updateconnection)
+ [Associate a MACsec CKN/CAK with a connection](#associate-key-connection)
+ [Remove the association between a MACsec secret key and a Direct Connect connection](#disassociate-key-connection)
+ [Delete a Direct Connect connection](#deleteconnection)

You can add a dedicated connection to a link aggregation group (LAG) allowing you to treat multiple connections as a single one. For information, see [Associate a connection with a LAG](#associate-connection-with-lag).

After you create a connection, create a virtual interface to connect to public and private AWS resources. For more information, see [Virtual interfaces and hosted virtual interfaces](#WorkingWithVirtualInterfaces).

If you do not have equipment at a Direct Connect location, first contact an AWS Direct Connect Partner at the AWS Direct Connect Partner Program. For more information, see [APN Partners Supporting Direct Connect](https://aws.amazon.com/directconnect/partners).

If you want to create a connection that uses MAC Security (MACsec), review the prerequisites before you create the connection. For more information, see [MACsec prerequisites for dedicated connections](#mac-sec-prerequisites).

### Letter of Authorization and Connecting Facility Assignment (LOA-CFA)
<a name="create-connection-loa-cfa"></a>

After we have processed your connection request, you can download the LOA-CFA. If the link is not enabled, the LOA-CFA is not yet available for you to download. Check your email for a request for information. 

The downloaded LoA is digitally signed and watermarked to validate the authenticity of the LoA issued by AWS. The digital signature and watermark in the LoA. The PDF document prevents a modified or potentially fraudulent LoA from being acted upon by the facilities provider at Direct Connect sites. The digital signature can be authenticated by opening the PDF and reviewing the signature panel. A valid document will show the "Signature is valid" and "Document has not been modified since the signature was applied". The watermark repeats the patch panel and strands assigned across the body of the LoA as a visual, but non-secure, indicator of authenticity.

Billing automatically starts when the port is active or 90 days after the LOA has been issued, whichever comes first. You can avoid billing charges by deleting the port prior to activation or within 90 days of the LOA being issued.

If your connection is not up after 90 days, and the LOA-CFA has not been issued, we will send you an email alerting you that the port will be deleted in 10 days. If you fail to activate the port within the additional 10 day period, the port will automatically be deleted and you'll need to restart the port creation process.

For the steps to download the LoA-CFA, see [Download the LOA-CFA](#download-loa-cfa).

**Note**  
For more information about pricing, see [Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/). If you no longer want the connection after you have reissued the LOA-CFA, you must delete the connection yourself. For more information, see [Delete a Direct Connect connection](#deleteconnection).

**Topics**
+ [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](#create-connection-loa-cfa)
+ [Create a connection using the Connection wizard](#create-connection)
+ [Create a Classic connection](#connection-classic)
+ [Download the LOA-CFA](#download-loa-cfa)
+ [Associate a MACsec CKN/CAK with a connection](#associate-key-connection)
+ [Remove the association between a MACsec secret key and a connection](#disassociate-key-connection)

### Create a Direct Connect Classic connection
<a name="connection-classic"></a>

For dedicated connections, you can submit a connection request using the Direct Connect console. For hosted connections, work with an AWS Direct Connect Partner to request a hosted connection. Ensure that you have the following information:
+ The port speed that you require. For dedicated connections, you can't change the port speed after you create the connection request. For hosted connections, your AWS Direct Connect Partner can change the speed.
+ The Direct Connect location at which the connection is to be terminated.

**Note**  
You cannot use the Direct Connect console to request a hosted connection. Instead, contact an AWS Direct Connect Partner, who can create a hosted connection for you, which you then accept. Skip the following procedure and go to [Accept your hosted connection](#get-started-accept-hosted-connection).

**To create a new Direct Connect connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. On the **Direct Connect** screen, under **Get started**, choose **Create a connection**.

1. Choose **Classic**.

1. For **Name**, enter a name for the connection.

1. For **Location**, select the appropriate Direct Connect location.

1.  If applicable, for **Sub Location**, choose the floor closest to you or your network provider. This option is only available if the location has meet-me rooms (MMRs) in multiple floors of the building.

1.  For **Port Speed**, choose the connection bandwidth.

1.  For **On-premises**, select **Connect through an Direct Connect partner** when you use this connection to connect to your data center.

1.  For **Service provider**, select the AWS Direct Connect Partner. If you use a partner that is not in the list, select **Other**.

1.  If you selected **Other** for **Service provider**, for** Name of other provider**, enter the name of the partner that you use.

1. (Optional) Choose **Add tag** to add key/value pairs to further help identify this connection.
   +  For **Key**, enter the key name. 
   + For **Value**, enter the key value.

   To remove an existing tag, choose the tag and then choose **Remove tag**. You can't have empty tags.

1. Choose **Create Connection**.

It can take up to 72 business hours for AWS to review your request and provision a port for your connection. During this time, you might receive an email with a request for more information about your use case or the specified location. The email is sent to the email address that you used when you signed up for AWS. You must respond within 7 days or the connection is deleted.

For more information, see [Dedicated and hosted connections](#WorkingWithConnections).

### Create a Direct Connect dedicated connection using the Connection wizard
<a name="create-connection"></a>

This section describes creating a connection using the Connection wizard. If you prefer to create a Classic connection, see the steps at [Step 2: Request a Direct Connect dedicated connection](#ConnectionRequest).

**To create a Connection wizard connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**, and then choose **Create connection**.

1. On the **Create Connection** page, under **Connection ordering type**, choose **Connection wizard**.

1. Choose a **Resiliency Level** for your network connections. A resiliency level can be one of the following:
   + **Maximum Resiliency**
   + **High Resiliency**
   + **Development and Test**

   For descriptions and more detailed information about these resiliency levels, see [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit).

1. Choose **Next**.

1. On the **Configure connections** page, provide the following details.

   1. From the **Bandwidth** drop-down list, choose the bandwidth required for the connection. This can be anywhere from **1Gbps** to **400 Gbps**.

   1. For **Location**, choose the appropriate Direct Connect location, and then choose the **First location service provider**, select the service provider providing connectivity for the connection at this location.

   1. For **Second location**, choose the appropriate Direct Connect at the second location, and then choose the **Second location service provider**, select the service provider providing connectivity for the connection at this second location.

   1. (Optional) Configure MAC security (MACsec) for the connection. Under **Additional Settings**, select **Request a MACsec capable port**.

      MACsec is only available on dedicated connections.

   1. (Optional) Choose **Add tag** to add key/value pairs to further help identify this connection.
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      To remove an existing tag, choose the tag and then choose **Remove tag**. You can't have empty tags.

1. Choose **Next**.

1. On the **Review and create page**, verify the connection. This page also displays estimated costs for port usage and additional data transfer charges. 

1. Choose **Create**.

1. Download your Letter of Authorization and Connecting Facility Assignment (LOA-CFA), For more information, see [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](#create-connection-loa-cfa).

Use one of the following commands.
+ [create-connection](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-connection.html) (AWS CLI)
+ [CreateConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateConnection.html) (Direct Connect API)

### Download the Direct Connect LOA-CFA
<a name="download-loa-cfa"></a>

You can download the LOA-CFA using either the Direct Connect console or through the command line. Once you've downloadeded the LOA-CFA and provided that to your network or colocation provider, that provider can order the cross-connect for you.

**To download the LOA-CFA**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the connection, and then choose **View details**.

1. Choose **Download LOA-CFA**. 
**Note**  
If the link is not enabled, the LOA-CFA is not yet available for you to download. A Support case will be created requesting additional information. Once you've responded to the request, and the request processed, the LOA-CFA will be available for download. If it's still unavailable, contact [AWS Support](https://aws.amazon.com/support/createCase).

1. Send the LOA-CFA to your network provider or colocation provider so that they can order a cross connect for you. The contact process can vary for each colocation provider. For more information, see [Requesting cross connects at Direct Connect locations](#Colocation).

**To download the LOA-CFA using the command line or API**
+ [describe-loa](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-loa.html) (AWS CLI)
+ [DescribeLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLoa.html) (Direct Connect API)

### Associate a MACsec CKN/CAK with a Direct Connect connection
<a name="associate-key-connection"></a>

After you create the connection that supports MACsec, you can associate a CKN/CAK with the connection. You can create the association using either the Direct Connect console or through the command-line or API.

**Note**  
You cannot modify a MACsec secret key after you associate it with a connection. If you need to modify the key, disassociate the key from the connection, and then associate a new key with the connection. For information about removing an association, see [Remove the association between a MACsec secret key and a connection](#disassociate-key-connection).

**To associate a MACsec key with a connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **Connections**.

1. Select a connection, and then choose **View details**.

1. Choose **Associate key**.

1. Enter the MACsec key.

   [Use the CAK/CKN pair] Choose **Key Pair**, and then do the following:
   + For **Connectivity Association Key (CAK)**, enter the CAK.
   + For **Connectivity Association Key Name (CKN)**, enter the CKN.

   [Use the secret] Choose **Existing Secret Manager secret**, and then for **Secret**, select the MACsec secret key.

1. Choose **Associate key**.

**To associate a MACsec key with a connection using the command line or API**
+ [associate-mac-sec-key](https://docs.aws.amazon.com/cli/latest/reference/directconnect/associate-mac-sec-key.html) (AWS CLI)
+ [AssociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateMacSecKey.html) (Direct Connect API)

### Remove the association between a MACsec secret key and a Direct Connect connection
<a name="disassociate-key-connection"></a>

You can remove the association between the connection and the MACsec key using either the Direct Connect console or through the command-line or API.

**To remove an association between a connection and a MACsec key**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. 

1. In the left pane, choose **Connections**.

1. Select a connection, and then choose **View details**.

1. Select the MACsec secret to remove, and then choose **Disassociate key**.

1. In the confirmation dialog box, enter **disassociate**, and then choose **Disassociate**.

**To remove an association between a connection and a MACsec key using the command line or API**
+ [disassociate-mac-sec-key](https://docs.aws.amazon.com/cli/latest/reference/directconnect/disassociate-mac-sec-key.html) (AWS CLI)
+ [DisassociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API__DisassociateMacSecKey.html) (Direct Connect API)

## Hosted Direct Connect connections
<a name="hosted_connection"></a>

To create a Direct Connect hosted connection, you need the following information:

**Direct Connect location**  
Work with an AWS Direct Connect Partner in the AWS Direct Connect Partner Program to help you establish network circuits between a Direct Connect location and your data center, office, or colocation environment. They can also help provide colocation space within the same facility as the location. For more information, see [Direct Connect Delivery Partners](https://aws.amazon.com/directconnect/partners).  
You can't request a hosted connection through the Direct Connect console. However, an AWS Direct Connect Partner can create and configure a hosted connection for you. Once configured, the connection appears in the **Connections** pane in the console.   
You must accept the hosted connection before you can use it. For more information, see [Accept a hosted connection](#accept-hosted-connection).

**Port speed**  
For hosted connections, the possible values are 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, and 25 Gbps. Note that only those Direct Connect partners who have met specific requirements may create a 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps hosted connection. 25 Gbps connections are available only in Direct Connect locations where 100 Gbps port speeds are available.

Note the following:
+ Connection port speeds can only be changed by your AWS Direct Connect Partner. Please check with your AWS Direct Connect Partner to see if they support upgrade or downgrade of an existing connection. If your Partner supports upgrade/downgrade of your connection, you are no longer required to delete and then recreate a connection in order to upgrade or downgrade an existing hosted connection's bandwidth. 
+ AWS uses traffic policing on hosted connections, which means that when the traffic rate reaches the configured maximum rate, excess traffic is dropped. This might result in bursty traffic having a lower throughput than non-bursty traffic.
+ Jumbo frames can be enabled on connections only if originally enabled on the Direct Connect hosted parent connection. If Jumbo frames isn't enabled on that parent connection, then it can't be enabled on any connection.

The following console operations are available after you've requested a hosted connection and accepted it:
+ [Delete a connection](#deleteconnection)
+ [Update a connection](#updateconnection)
+ [View connection details](#viewdetails)

 After you accept a connection, create a virtual interface to connect to public and private AWS resources. For more information, see [Virtual interfaces and hosted virtual interfaces](#WorkingWithVirtualInterfaces).

### Accept a Direct Connect hosted connection
<a name="accept-hosted-connection"></a>

If you are interested in purchasing a hosted connection, you must contact an AWS Direct Connect Partner in the AWS Direct Connect Partner Program. The partner provisions the connection for you. After the connection is configured, it appears in the **Connections** pane in the Direct Connect console.

Before you can begin using a hosted connection, you must accept the connection. You can accept a hosted connection using either the Direct Connect console or using the command line or API.

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the hosted connection and choose **View details**.

1. Select the confirmation check box and choose **Accept**.

**To accept a hosted connection using the command line or API**
+ [confirm-connection](https://docs.aws.amazon.com/cli/latest/reference/directconnect/confirm-connection.html) (AWS CLI)
+ [ConfirmConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmConnection.html) (Direct Connect API)

## Delete a Direct Connect connection
<a name="deleteconnection"></a>

You can delete a connection as long as there are no virtual interfaces attached to it. Deleting your connection stops all port hour charges for this connection, but you may still incur cross-connect or network circuit charges (see below). Direct Connectdata transfer charges are associated with virtual interfaces. For more information about how to delete a virtual interface, see [Delete a virtual interface](#deletevif).

Before deleting a connection, download the LOA for the connection containing the cross-account information so you have the relevant information about the circuits being disconnected. For the steps to download the connection LOA, see [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](#create-connection-loa-cfa).

When you delete a connection, AWS will instruct the colocation provider to disconnect your network device from the Direct Connect router by removing the fiber-optic cross-connect cable from the applicable AWS patch panel. However, your colocation or circuit provider may still charge you cross-connect or network circuit charges because the cross-connect cable may still be connected to your network device. These charges for the cross-connect are independent of Direct Connect, and must be cancelled with the colocation or circuit provider using information from the LOA.

If the connection is part of a link aggregation group (LAG), you cannot delete the connection if doing so causes the LAG to fall below its setting for the minimum number of operational connections. 

You can delete a connection using either the Direct Connect console or using the command line or API.

**To delete a connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the connections and choose **Delete**.

1. In the **Delete confirmation** dialog box, choose **Delete**.

**To delete a connection using the command line or API**
+ [delete-connection](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-connection.html) (AWS CLI)
+ [DeleteConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteConnection.html) (Direct Connect API)

## Update a Direct Connect connection
<a name="updateconnection"></a>

You can update the following connection attribute using either the Direct Connect console or using the command line or API.
+ The name of the connection.
+ The connection's MACsec encryption mode.
**Note**  
While you cannot directly modify MACSec properties on hosted connections, partners can enable MACSec on their own interconnects to provide secure hosted connections to their customers.

  The valid values are:
  + `should_encrypt`
  + `must_encrypt`

    When you set the encryption mode to this value, the connection goes down when the encryption is down.
  + `no_encrypt`

**To update a connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the connection, and then choose **Edit**.

1. Modify the connection:

   [Change the name] For **Name**, enter a new connection name.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Edit connection**.

**To update a connection using the command line or API**
+ [update-connection](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-connection.html) (AWS CLI)
+ [UpdateConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateConnection.html) (Direct Connect API)

## View Direct Connect connection details
<a name="viewdetails"></a>

You can view the current status of your connection using either the Direct Connect console or using the command line or API. You can also view your connection ID (for example, `dxcon-12nikabc`) and verify that it matches the connection ID on the LOA-CFA that you received or downloaded.

For information on monitoring connections, see [Monitoring and visibility with Direct Connect](#monitoring-overview).

**To view details about a connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **Connections**.

1. Select a connection, and then choose **View details**.

**To describe a connection using the command line or API**
+ [describe-connections](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-connections.html) (AWS CLI)
+ [DescribeConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnections.html) (Direct Connect API)

# Flat-rate billing for dedicated connections
<a name="flat-rate-connections"></a>

Direct Connect offers flat-rate as a new billing mode for dedicated connections, available alongside the existing pay-as-you-go model. You set the billing mode per connection, and you can switch a connection back to pay-as-you-go at any time. Flat-rate billing introduces **port-pairs**, a recommended setup that builds resiliency into your connection by default.

Flat-rate billing applies to **dedicated** connections only. Hosted connections provisioned by a Direct Connect partner are not eligible.

**Note**  
For how flat-rate connections are priced — the fixed hourly rate, pricing tiers, and what the flat rate includes — see the [Direct Connect Pricing Guide](https://docs.aws.amazon.com/directconnect/latest/PricingGuide/pricing-flat-rate.html).

## Creating a flat-rate connection
<a name="flat-rate-creating"></a>

When you create a Direct Connect dedicated connection, you choose the following:

1. **Location** – The Direct Connect location where your connection is provisioned.

1. **Bandwidth** – The port speed. Bandwidth can't be changed after the connection is created. To use a different bandwidth, you must create a new connection.

1. **Billing mode** – Either pay-as-you-go or flat-rate.

1. **Pricing tier** – The tier determines which AWS Regions are covered under flat-rate billing for that Direct Connect location. For more information about pricing tiers, see the Direct Connect Pricing Guide.

Direct Connect flat-rate billing is built around port-pairs, which is the recommended setup. It gives you a resilient architecture by default, with the redundant port included at no additional charge. You can also use flat-rate billing on a single connection if you prefer to provide your own redundancy, such as a VPN. For more information, see [Using flat-rate billing on a single connection](#flat-rate-single).

## Port-pairs and resiliency
<a name="flat-rate-port-pairs"></a>

Direct Connect flat-rate billing applies to **port-pairs**. A port-pair builds redundancy into your connection by default, so you get a resilient architecture without having to design it yourself.

### What is a port-pair?
<a name="flat-rate-what-is-port-pair"></a>

A port-pair is two dedicated Direct Connect ports, provisioned on different devices or in different locations, that share the same pricing tier. One port carries your traffic and the other stands by for redundancy. If one port becomes unavailable — for example, during an outage or a maintenance window — your connection stays up through the redundant port. Both ports can carry traffic simultaneously; however, the effective bandwidth of the port-pair is limited to the capacity of a single connection. For more information, see [Effective bandwidth](#flat-rate-effective-bandwidth).

The second port is included at no additional charge.

To create a port-pair, place two qualifying flat-rate connections into a resiliency group, a logical grouping that declares your intended redundancy model. AWS matches the qualifying connections in the group as a port-pair. For more information, see [Resiliency groups](#flat-rate-resiliency-groups).

A connection is part of a port-pair when all of the following are true:
+ The connection is set to flat-rate billing mode.
+ The connection belongs to a resiliency group.
+ The group contains at least one other flat-rate connection on a different device.
+ The qualifying connections share the same port speed and the same pricing tier.

Both connections in a port-pair must use the same pricing tier. Because the second port exists solely for resiliency, differing billing properties within a pair are not supported.

The two connections do not need to be in the same Direct Connect location. You can pair ports across locations as long as they meet the preceding requirements. Pairing across locations protects you against a complete location failure as well as a device failure.

A resiliency group can contain any number of connections. AWS looks for pairs within the group. It pairs any two connections on separate devices that share the same billing mode, pricing tier, and port speed. Connections in the group with no match are treated as single connections. A link aggregation group (LAG) counts as a single connection for resiliency group purposes.

After the connections are matched as a port-pair, the billing mode updates on each connection. The following example shows a resiliency group with two associated connections that are billed as a port-pair.

![The Direct Connect console showing a resiliency group named test-RG with two associated connections, each with a billing mode of PortPairFlatRateTier2, confirming that they are billed together as a port-pair.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/flat-rate-port-pair-billing.png)


If you delete a connection or change a property that breaks the pairing requirements, both connections revert to single connections. Because flat-rate billing is calculated per hour, changes are reflected within the next billing hour.

All members of a LAG must use the same billing mode. A LAG can't mix flat-rate and pay-as-you-go connections. A flat-rate connection that leaves a LAG keeps flat-rate as its billing mode. A pay-as-you-go connection added to a LAG that already uses flat-rate billing converts to flat-rate automatically.

### Effective bandwidth
<a name="flat-rate-effective-bandwidth"></a>

The usable capacity that you purchase is the capacity of a **single** port. The second port exists solely for redundancy and does not add throughput. For example, a 10 Gbps port-pair at any Direct Connect location gives you an effective usable capacity of **10 Gbps, not 20 Gbps**. If one port fails, the other maintains your full 10 Gbps of connectivity. Plan your port-pairs based on the total capacity that you need. For example, if your workload requires 20 Gbps, provision two 10 Gbps port-pairs.

By enrolling in flat-rate pricing, you agree to use the service in accordance with the AWS Customer Agreement and AWS Service Terms.

### Using flat-rate billing on a single connection
<a name="flat-rate-single"></a>

A port-pair is the recommended setup, but you can also set a single connection to flat-rate billing mode, assign it a pricing tier, and run it without adding it to a resiliency group. This suits you if you want to run one connection at high utilization and provide redundancy yourself — for example, using AWS Site-to-Site VPN as backup. You can also deploy two full-bandwidth connections independently.

Keep the following in mind:
+ A single flat-rate connection costs the same as a port-pair at the same bandwidth and tier. Running one port instead of two does not reduce your price, so there is no cost saving. What you gain is flat-rate billing on a single connection.
+ Your usable bandwidth equals the capacity of that connection, and you can use its full capacity.
+ You do not receive a redundant port and must design for resiliency yourself.

If resiliency matters for the workload, use a port-pair or provide separate backup connectivity such as a VPN.

## Resiliency groups
<a name="flat-rate-resiliency-groups"></a>

To form a flat-rate port-pair, your connections must belong to a **resiliency group** — a logical grouping of Direct Connect connections that declares your intended redundancy model, so that AWS can pair connections correctly.


| How you order | How connections join a resiliency group | 
| --- | --- | 
| Console (Create connection wizard) | You select a resiliency model and create a new resiliency group or add your connections to an existing group. | 
| API | You create or identify the resiliency group, create your connections, and then associate the connections with the group. | 
| Existing connections | Two existing connections provisioned on different devices can be paired by adding them to a resiliency group. | 

## Switching billing modes
<a name="flat-rate-switching"></a>

Billing mode is a per-connection setting that you can change, so you can switch a connection between pay-as-you-go and flat-rate. Billing mode changes are limited to three per connection in any rolling six-month period.

To convert existing pay-as-you-go connections to flat-rate and create a port-pair, complete the following steps:

1. Update the billing mode for each connection to flat-rate.

1. Associate the connections with a new or existing resiliency group.

If you convert a connection to flat-rate without adding it to a resiliency group, the connection is treated as a single flat-rate connection rather than part of a port-pair.

## Limitations
<a name="flat-rate-limitations"></a>

All Direct Connect connections under a single account at a given Direct Connect location must use the same billing mode, either pay-as-you-go or flat-rate. You cannot mix billing modes within the same account at a location.

To use a mix of billing modes at the same location, create and maintain the connections under separate AWS accounts.

## Frequently asked questions
<a name="flat-rate-faq-ug"></a>

**Does the second port double my bandwidth?**

No. Usable bandwidth equals the capacity of a single port. A 10 Gbps port-pair gives you 10 Gbps of usable capacity, not 20 Gbps. The second port protects your connection; it does not add throughput.

**Can I switch a connection back to pay-as-you-go?**

Yes. Billing mode is a per-connection setting that you can change. Billing mode changes are limited to three per connection in any rolling six-month period.

**Is flat-rate billing available for hosted connections?**

No. Flat-rate billing applies to dedicated connections only.

**Does flat-rate pricing cover point-to-point (PTP) routes?**

Yes, if you advertise them over BGP. After Direct Connect learns your PTP routes, flat-rate pricing applies to traffic on those routes. Traffic on PTP routes that you don't advertise is billed at standard Direct Connect data transfer rates.

# Requesting cross connects at Direct Connect locations
<a name="Colocation"></a>

 After you have downloaded your Letter of Authorization and Connecting Facility Assignment (LOA-CFA), you must complete your cross-network connection, also known as a *cross connect*. If you already have equipment located in a Direct Connect location, contact the appropriate provider to complete the cross connect. For specific instructions for each provider, see the tables below. Partners and contact information are organized by Region. For specific cross connect pricing you'll need to contact the Direct Connect Partner directly. After the cross connect is established, you can create the virtual interfaces using the Direct Connect console.

Some locations are set up as a campus. For more information, including available speeds available at each location, see [Direct Connect Locations](https://aws.amazon.com/directconnect/details/#AWS_Direct_Connect_Locations).

If you do not already have equipment located in a Direct Connect location, you can work with one of the partners in the AWS Partner Network (APN). They help you to connect to a Direct Connect location. For more information, see [APN Partners supporting Direct Connect](https://aws.amazon.com/directconnect/partners/). You must share the LOA-CFA with your selected provider to facilitate your cross connect request.

A Direct Connect connection can provide access to resources in other Regions. For more information, see [Access to AWS Regions](#remote_regions). 

**Note**  
If the cross connect is not completed within 90 days, the authority granted by the LOA-CFA expires. To renew a LOA-CFA that has expired, you can download it again from the Direct Connect console. For more information, see [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](#create-connection-loa-cfa).

## Connectivity options
<a name="connectivity-options"></a>

The options available to connect to a Direct Connect location might vary by Partner and AWS Region. You can work with one of the partners in the AWS Partner Network (APN) who can provide one or more of the following connectivity options:
+ If you have resources deployed in the same data center/colocation facility as the Direct Connect location, the facility can provide a cross-connect between the Direct Connect equipment and your resources. You must first provide LOA-CFA to the facility for this. See [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](#create-connection-loa-cfa) for more information. The following shows an example of this Direct Connect connectivity option:  
![Image showing Direct Connect connectivity with resources deployed in the same data center as the Direct Connect location.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dx-connectivity-1.png)
+ Extend the Direct Connect connection at Layer 2 (data link layer) via a "circuit" from the Direct Connect location to the customer location by working with Direct Connect Partners. The router installed at the customer location will directly form a BGP session with the AWS equipment. For example, technologies that can be used are Metro Ethernet, Dark Fibre, or Wavelength. The following shows an example of this Direct Connect connectivity option.  
![Image showing Direct Connect Layer 2 connectivity.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dx-connectivity-2.png)
+ Extend the Direct Connect connection at Layer 3 (Network layer) from the Direct Connect location to your location by working with Direct Connect Partners. For this connectivity option, the Direct Connect Partner provides a router within the Direct Connect location that forms a Border Gateway Protocol (BGP) session with the AWS equipment. The Direct Connect partner then established another BGP with you; for example, this might be over Multiprotocol Label Switching (MPLS). The following shows an example of this Direct Connect connectivity option.  
![Image showing Direct Connect Layer 3 connectivity.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dx-connectivity-3.png)

## US East (Ohio)
<a name="cross-connect-us-east-2"></a>


| Location | How to request a connection | 
| --- | --- | 
| Cologix COL2, Columbus | Contact Cologix at [sales@cologix.com](mailto:sales@cologix.com). | 
| Cologix MIN3, Minneapolis | Contact Cologix at [sales@cologix.com](mailto:sales@cologix.com). | 
| CyrusOne West III, Houston | Submit a request using the [customer contact](https://cyrusone.com/contact/) form. | 
| Equinix CH2, Chicago | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect).  | 
| QTS, Chicago | Contact QTS at [AConnect@qtsdatacenters.com](mailto:AConnect@qtsdatacenters.com). | 
| Netrality Data Centers, 1102 Grand, Kansas City | Contact Netrality Data Centers at [support@netrality.com](mailto:support@netrality.com). | 

## US East (N. Virginia)
<a name="cross-connect-us-east-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| 165 Halsey Street, Newark | Contact [operations@165halsey.com](mailto:operations@165halsey.com). | 
| CoreSite 32k, New York | Place an order using the [CoreSite Customer Portal](https://mycoresite.coresite.com/login). After you complete the form, review the order for accuracy, and then approve it using the website. | 
| CoreSite VA1-VA2, Reston  | Place an order at the [CoreSite Customer Portal](https://mycoresite.coresite.com/login). After you complete the form, review the order for accuracy, and then approve it using the website. | 
| Digital Realty ATL1 &ATL2, Atlanta | Contact Digital Realty at [amazon.orders@digitalrealty.com](mailto:amazon.orders@digitalrealty.com). | 
| Digital Realty IAD38, Ashburn | Contact Digital Realty at [amazon.orders@digitalrealty.com](mailto:amazon.orders@digitalrealty.com). | 
| Equinix DC1-DC6 & DC10-D12, Ashburn | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix DAA1-DC3 & DC6, Dallas  | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix MI1, Miami | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix NY5, Seacaucus | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| KIO Networks QRO1, Queretaro, MX | Contact [KIO Networks](https://www.kio.tech/en/#formcontacto)". | 
| Markley, One Summer Street, Boston | For current customers, create a request using the [customer portal](https://support.markleygroup.com/). For new queries, contact [sales@markleygroup.com](mailto:sales@markleygroup.com). | 
| Netrality Data Centers, 2nd floor MMR, Philadelphia | Contact Netrality Data Centers at [support@netrality.com](mailto:support@netrality.com). | 
| QTS ATL1, Atlanta | Contact QTS at [AConnect@qtsdatacenters.com](mailto:AConnect@qtsdatacenters.com). | 

## US West (N. California)
<a name="cross-connect-us-west-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| CoreSite, LA1, Los Angeles | Place an order using the [CoreSite Customer Portal](https://mycoresite.coresite.com/login). After you complete the form, review the order for accuracy, and then approve it using the website. | 
| CoreSite SV2, Milpitas  | Place an order using the [CoreSite Customer Portal](https://mycoresite.coresite.com/login). After you complete the form, review the order for accuracy, and then approve it using the website. | 
| CoreSite SV4, Santa Clara  | Place an order using the [CoreSite Customer Portal](https://mycoresite.coresite.com/login). After you complete the form, review the order for accuracy, and then approve it using the MyCoreSite website. | 
| EdgeConneX, Phoenix | Place an order using the [EdgeOS Customer Portal](https://edgeos.edgeconnex.com/portal/). After you have submitted the form, EdgeConneX will provide a service order form for approval. You can send questions to [cloudaccess@edgeconnex.com](mailto:cloudaccess@edgeconnex.com). | 
| Equinix LA3, El Segundo | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect).  | 
| Equinix SV1 & SV5, San Jose | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect).  | 
| PhoenixNAP, Phoenix | Contact phoenixNAP Provisioning at [provisioning@phoenixnap.com](mailto:provisioning@phoenixnap.com). | 

## US West (Oregon)
<a name="cross-connect-us-west-2"></a>


| Location | How to request a connection | 
| --- | --- | 
| CoreSite DE1, Denver | Place an order using the [CoreSite Customer Portal](https://mycoresite.coresite.com/login). After you complete the form, review the order for accuracy, and then approve it using the website. | 
| Digital Realty SEA10, Westin Building, Seattle | Contact Digital Realty at [amazon.orders@digitalrealty.com](mailto:amazon.orders@digitalrealty.com). | 
| EdgeConneX, Portland | Place an order using the [EdgeOS Customer Portal](https://edgeos.edgeconnex.com/portal/). After you have submitted the form, EdgeConneX will provide a service order form for approval. You can send questions to [cloudaccess@edgeconnex.com](mailto:cloudaccess@edgeconnex.com). | 
| Equinix SE2, Seattle | Contact Equinix at [support@equinix.com](mailto:support@equinix.com). | 
| Pittock Block, Portland | Send requests by email to [crossconnect@pittock.com](mailto:crossconnect@pittock.com) or by phone at \+1 503 226 6777. | 
| Switch SUPERNAP 8, Las Vegas | Contact Switch SUPERNAP at [orders@supernap.com](mailto:orders@supernap.com). | 
| TierPoint Seattle | Contact TierPoint at [sales@tierpoint.com](mailto:sales@tierpoint.com). | 

## Africa (Cape Town)
<a name="cross-connect-af-south-1"></a>


| Location | How to request a connection | 
| --- | --- | 
|  Cape Town Internet Exchange/ Teraco Data Centres | Contact Teraco at [support@teraco.co.za](mailto:support@teraco.co.za) for existing Teraco customers or [connect@teraco.co.za](mailto:connect@teraco.co.za) for new customers. | 
|  Teraco JB1, Johannesburg, South Africa | Contact Teraco at [support@teraco.co.za](mailto:support@teraco.co.za) for existing Teraco customers or [connect@teraco.co.za](mailto:connect@teraco.co.za) for new customers. | 

## Asia Pacific (Jakarta)
<a name="cross-connect-ap-southeast-3"></a>


| Location | How to request a connection | 
| --- | --- | 
|  DCI JK3, Jakarta | Contact DCI Indonesia at [awsdx@dci-indonesia.com](mailto:awsdx@dci-indonesia.com). | 
|  NTT 2 Data Center, Jakarta | Contact NTT at [tps.cms.presales@global.ntt](mailto:tps.cms.presales@global.ntt). | 

## Asia Pacific (Mumbai)
<a name="cross-connect-ap-south-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Equinix, Mumbai | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| NetMagic DC2, Bangalore | Contact NetMagic Sales and Marketing toll-free at 18001033130 or at [marketing@netmagicsolutions.com](mailto:marketing@netmagicsolutions.com). | 
| Sify Rabale, Mumbai | Contact Sify at [aws.directconnect@sifycorp.com](mailto:aws.directconnect@sifycorp.com). | 
| STT Delhi DC2, Delhi | Contact STT at [enquiry.AWSDX@sttelemediagdc.in](mailto:enquiry.AWSDX@sttelemediagdc.in). | 
| STT GDC Pvt. Ltd. VSB, Chennai | Contact STT at [enquiry.AWSDX@sttelemediagdc.in](mailto:enquiry.AWSDX@sttelemediagdc.in). | 
| STT Hyderabad DC1, Hyderabad | Contact STT at [enquiry.AWSDX@sttelemediagdc.in](mailto:enquiry.AWSDX@sttelemediagdc.in). | 

## Asia Pacific (Seoul)
<a name="cross-connect-ap-northeast-2"></a>


| Location | How to request a connection | 
| --- | --- | 
| Digital Realty ICN1, Seoul | Contact Digital Realty at [amazon.orders@digitalrealty.com](mailto:amazon.orders@digitalrealty.com). | 
| KINX Gasan Data Center, Seoul | Contact KINX at [sales@kinx.net](mailto:sales@kinx.net). | 
| LG U\+ Pyeong-Chon Mega Center, Seoul | Submit the LOA document to [kidcadmin@lguplus.co.kr](mailto:kidcadmin@lguplus.co.kr) and [center8@kidc.net](mailto:center8@kidc.net). | 

## Asia Pacific (Singapore)
<a name="cross-connect-ap-southeast-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Equinix HK1, Tsuen Wan N.T., Hong Kong SAR | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix SG2, Singapore  | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Global Switch, Singapore | Contact Global Switch at [salessingapore@globalswitch.com](mailto:salessingapore@globalswitch.com). | 
| GPX, Mumbai | Contact GPX (Equinix) at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| iAdvantage Mega-i, Hong Kong | Contact iAdvantage at [cs@iadvantage.net](mailto:cs@iadvantage.net) or place an order using [iAdvantage Cabling Order e-Form](https://cable.iadvantage.net). | 
| Menara AIMS, Kuala Lumpur | Existing AIMS custom ers can request an X-Connect order using the Customer Service portal by filling out the Engineering Work Order Request Form. Contacting [service.delivery@aims.com.my](mailto:service.delivery@aims.com.my) if there are any problems submitting the request. | 
| TCC Data Center, Bangkok  | Contact TCC Technology Co., Ltd at [gateway.ne@tcc-technology.com](mailto:gateway.ne@tcc-technology.com). | 

## Asia Pacific (Sydney)
<a name="cross-connect-ap-southeast-2"></a>


| Location | How to request a connection | 
| --- | --- | 
| CDC Hume 2, Canberra | Log in to the customer portal at [CDC Customer Portal](https://cdcdatacentres.freshworks.com/). | 
| Datacom DH6, Auckland | Contact Datacom at [Datacom Orbit –Auckland](https://datacom.com/au/en/products/data-centres/orbit-auckland/).  | 
| Equinix ME2, Melbourne | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix SY3, Sydney | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Global Switch, Sydney | Contact Global Switch at [salessydney@globalswitch.com](mailto:salessydney@globalswitch.com). | 
| NEXTDC C1, Canberra | Contact NEXTDC at [nxtops@nextdc.com](mailto:nxtops@nextdc.com). | 
| NEXTDC M1, Melbourne | Contact NEXTDC at [nxtops@nextdc.com](mailto:nxtops@nextdc.com). | 
| NEXTDC P1, Perth | Contact NEXTDC at [nxtops@nextdc.com](mailto:nxtops@nextdc.com). | 
| NEXTDC S2, Sydney | Contact NEXTDC at [nxtops@nextdc.com](mailto:nxtops@nextdc.com). | 

## Asia Pacific (Tokyo)
<a name="cross-connect-ap-northeast-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| AT Tokyo Chuo Data Center, Tokyo | Contact AT TOKYO at [at-sales@attokyo.co.jp](mailto:at-sales@attokyo.co.jp). | 
| Chief Telecom LY, Taipei | Contact Chief Telecom at [vicky\_chan@chief.com.tw](mailto:vicky_chan@chief.com.tw). | 
| Chunghwa Telecom, Taipei | Contact CHT Taipei IDC NOC at [taipei\_idc@cht.com.tw](mailto:taipei_idc@cht.com.tw). | 
| Equinix OS1, Osaka  | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix TY2, Tokyo  | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| NEC Inzai, Inzai | Contact NEC Inzai at [connection\_support@ices.jp.nec.com ](mailto:connection_support@ices.jp.nec.com).  | 

## Canada (Central)
<a name="cross-connect-ca-central-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Telehouse, 250 Front St W, Toronto | Contact [product@ca.telehouse.com](mailto:product@ca.telehouse.com). | 
| Cologix MTL3, Montreal | Contact Cologix at [sales@cologix.com](mailto:sales@cologix.com). | 
| Cologix VAN2, Vancouver | Contact Cologix at [sales@cologix.com](mailto:sales@cologix.com). | 
| eStruxture, Montreal | Contact eStruxture at [directconnect@estruxture.com](mailto:directconnect@estruxture.com). | 

## China (Beijing)
<a name="cross-connect-cn-north-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| CIDS Jiachuang IDC, Beijing | Contact [dx-order@sinnet.com.cn](mailto:dx-order@sinnet.com.cn). | 
| Sinnet Jiuxianqiao IDC, Beijing | Contact [dx-order@sinnet.com.cn](mailto:dx-order@sinnet.com.cn). | 
| GDS No. 3 Data Center, Shanghai | Contact [dx@nwcdcloud.cn](mailto:ddx@nwcdcloud.cn). | 
| GDS No. 3 Data Center, Shenzhen | This location is no longer accepting new connection requests. | 

## China (Ningxia)
<a name="cross-connect-cn-northwest-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Industrial Park IDC, Ningxia | Contact [dx@nwcdcloud.cn](mailto:dx@nwcdcloud.cn). | 
| Shapotou IDC, Ningxia | Contact [dx@nwcdcloud.cn](mailto:dx@nwcdcloud.cn). | 

## Europe (Frankfurt)
<a name="cross-connect-eu-central-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| CE Colo, Prague, Czech Republic | Contact CE Colo at [info@cecolo.com](mailto:info@cecolo.com). | 
| DigiPlex Ulven, Oslo, Norway | Contact DigiPlex at [helpme@digiplex.com](mailto:helpme@digiplex.com). | 
| Equinix AM3, Amsterdam, Netherlands | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix FR5, Frankfurt  | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect).  | 
| Equinix HE6, Helsinki | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix MU1, Munich  | End of support July 2027. No new connections available. Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix WA1, Warsaw | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Interxion AMS7, Amsterdam | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| Interxion CPH2, Copenhagen | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| Interxion FRA6, Frankfurt | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| Interxion MAD2, Madrid | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| Interxion VIE2, Vienna | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| Interxion ZUR1, Zurich | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| IPB, Berlin | Contact IPB at [kontakt@ipb.de](mailto:kontakt@ipb.de). | 
| Equinix ITConic MD2, Madrid | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 

## Europe (Ireland)
<a name="cross-connect-eu-west-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Digital Realty (UK), Docklands | Contact Digital Realty (UK) at [amazon.orders@digitalrealty.com](mailto:amazon.orders@digitalrealty.com). | 
| Eircom Clonshaugh | Contact Eircom at [datacentre@eirevo.ie](mailto:datacentre@eirevo.ie). | 
| Equinix DX1, Dublin | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix LD5, London (Slough)  | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect).  | 
| Interxion DUB2, Dublin | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| Interxion MRS1, Marseille | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 

## Europe (Milan)
<a name="cross-connect-eu-south-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| CDLAN srl Via Caldera 21, Milano | Contact CDLAN at [sales@cdlan.it](mailto:mailto:sales@cdlan.it). | 
| Equinix, ML2, Milano, Italy | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 

## Europe (London)
<a name="cross-connect-eu-west-2"></a>


| Location | How to request a connection | 
| --- | --- | 
| Digital Realty (UK), Docklands | Contact Digital Realty (UK) at [amazon.orders@digitalrealty.com](mailto:amazon.orders@digitalrealty.com). | 
| Equinix LD5, London (Slough)  | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix MA3, Manchester | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Telehouse West, London | Contact Telehouse UK at [sales.support@uk.telehouse.net](mailto:sales.support@uk.telehouse.net). | 

## Europe (Paris)
<a name="cross-connect-eu-west-3"></a>


| Location | How to request a connection | 
| --- | --- | 
| Equinix PA3, Paris | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Interxion PAR7, Paris | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 
| Telehouse Voltaire, Paris  | Contact Telehouse Paris Voltaire using the [Contact Us](https://www.telehouse.net/contact-telehouse/) page. | 

## Europe (Stockholm)
<a name="cross-connect-eu-north-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Interxion STO1, Stockholm | Contact Interxion at [customer.services@interxion.com](mailto:customer.services@interxion.com). | 

## Europe (Zurich)
<a name="cross-connect-eu-central-2"></a>


| Location | How to request a connection | 
| --- | --- | 
| Equinix ZRH51, Oberengstringen, Switzerland | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 

## Israel (Tel Aviv)
<a name="cross-connect-il-central-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| MedOne, Haifa | Contact MedOne at [support@Medone.co.il](mailto:support@Medone.co.il) | 
| EdgeConnex, Herzliya | Contact EdgeConnect at [info@edgeconnecx.com](mailto:info@dgeconnecx.com) | 

## Middle East (Bahrain)
<a name="cross-connect-me-south-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| AWS Bahrain DC53, Manama | To complete the connection, you can work with one of our [network provider partners](https://aws.amazon.com/directconnect/partners/) at the location to establish connectivity. You will then provide a Letter of Authorization (LOA) from the network provider to AWS through the [AWS Support Center](https://console.aws.amazon.com/support/home). AWS completes the cross-connect at this location.  | 
| AWS Bahrain DC52, Manama | To complete the connection, you can work with one of our [network provider partners](https://aws.amazon.com/directconnect/partners/) at the location to establish connectivity. You will then provide a Letter of Authorization (LOA) from the network provider to AWS through the [AWS Support Center](https://console.aws.amazon.com/support/home). AWS completes the cross-connect at this location.  | 

## Middle East (UAE)
<a name="cross-connect-me-central-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Equinix DX1, Dubai, UAE | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Etisalat SmartHub Data Centre, Fujairah, UAE | Contact Etisalat SmartHub Data Centre at [IntlSales-C&WS@etisalat.ae](mailto:UAE        IntlSales-C&WS@etisalat.ae). | 

## South America (São Paulo)
<a name="cross-connect-sa-east-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Cirion BNARAGMS, Buenos Aires | Contact Cirion at [cloud.connect@ciriontechnologies.com](mailto:cloud.connect@ciriontechnologies.com). | 
| Equinix RJ2, Rio de Janeiro | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Equinix SP4, São Paulo | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 
| Tivit | Contact Tivit at [aws@tivit.com.br](mailto:aws@tivit.com.br). | 

## AWS GovCloud (US-East)
<a name="cross-connect-gov-us-east-1"></a>

You can't order connections in this Region.

## AWS GovCloud (US-West)
<a name="cross-connect-gov-us-west-1"></a>


| Location | How to request a connection | 
| --- | --- | 
| Equinix SV5, San Jose | Contact Equinix at [https://digital.equinix.com/AWS-Direct-Connect](https://digital.equinix.com/AWS-Direct-Connect). | 

# Direct Connect virtual interfaces and hosted virtual interfaces
<a name="WorkingWithVirtualInterfaces"></a>

You must create one of the following virtual interfaces (VIFs) to begin using your Direct Connect connection. 
+ Private virtual interface: A private virtual interface should be used to access an Amazon VPC using private IP addresses.
+ Public virtual interface: A public virtual interface can access all AWS public services using public IP addresses.
+ Transit virtual interface: A transit virtual interface should be used to access one or more Amazon VPC Transit Gateways associated with Direct Connect gateways. You can use transit virtual interfaces with any Direct Connect dedicated or hosted connection of any speed. For information about Direct Connect gateway configurations, see [Direct Connect gateways](#direct-connect-gateways-intro).

To connect to other AWS services using IPv6 addresses, check the service documentation to verify that IPv6 addressing is supported.

## Public virtual interface prefix advertisement rules
<a name="advertise-prefixes"></a>

We advertise appropriate Amazon prefixes to you so that you can reach the public IP addresses of workloads in your VPCs and other AWS services. You can access all AWS prefixes through this connection; for example, public IP addresses used by Amazon EC2 instances, Amazon S3, API endpoints for AWS services, and Amazon.com. You do not have access to non-Amazon prefixes. For a current list of prefixes used by AWS, see [AWS IP Address Ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html) in the *Amazon VPC User Guide*. On this page you can download a `.json` file of the currently published AWS IP ranges. Note that for published IP address ranges:
+ Prefixes announced via BGP over a public virtual interface might be aggregated or de-aggregated compared to what is listed in the AWS IP address ranges list.
+ Any IP address ranges that you bring to AWS through your own IP addresses (BYOIP) are not included in the `.json` file, but AWS still advertises these BYOIP addresses over a public virtual interface.
+  AWS does not re-advertise customer prefixes that were received over Direct Connect public virtual interfaces to networks outside of AWS. Prefixes advertised on a public virtual interface will be visible to all customers on AWS.

**Note**  
We recommend that you use a firewall filter (based on the source/destination address of packets) to control traffic to and from some prefixes. 

For more information about public virtual interfaces and routing policies, see [Public virtual interface routing policies](#routing-policies).

## SiteLink
<a name="dx-sitelink"></a>

If you're creating a private or transit virtual interface, you can use SiteLink.

SiteLink is an optional Direct Connect feature for private virtual interfaces that enables connectivity between any two Direct Connect points of presence (PoPs) in the same AWS partition using the shortest available path over the AWS network. This allows you to connect your on-premises network through the AWS global network without needing to route your traffic through a Region. For more information about SiteLink see [Introducing Direct Connect SiteLink](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-direct-connect-sitelink/).

**Note**  
SiteLink is not available in AWS GovCloud (US) and the China Regions.
SiteLink does not work if an on-premises router advertises the same route to AWS on multiple virtual interfaces.

There's a separate pricing fee for using SiteLink. For more information, see [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/).

SiteLink doesn't support all virtual interface types. The following table shows the interface type and whether it's supported. 


| Virtual interface type | Supported/Not supported | 
| --- | --- | 
|  Transit virtual interface  |  Supported  | 
|  Private virtual interface attached to a Direct Connect gateway with a virtual gateway  |  Supported  | 
|  Private virtual interface attached to a Direct Connect gateway not associated with a virtual gateway or Transit Gateway  |  Supported  | 
|  Private virtual interface attached to a virtual gateway  |  Not supported  | 
|  Public virtual interface  |  Not supported  | 

Traffic routing behavior for traffic from AWS Regions (virtual or Transit Gateways) to on-premises locations over a SiteLink enabled virtual interface varies slightly from the default Direct Connect virtual interface behavior with an AWS path prepend. When SiteLink is enabled, virtual interfaces from an AWS Region prefer a BGP path with a lower AS path length from a Direct Connect location, regardless of the associated Region. For example , an associated Region is advertised for each Direct Connect location. If SiteLink is disabled, by default traffic coming from a virtual or Transit Gateway prefers a Direct Connect location that is associated with that AWS Region, even if the router from Direct Connect locations associated with different Regions advertises a path with a shorter AS path length. The virtual or Transit Gateway still prefers the path from Direct Connect locations local to the associated AWS Region.

For a list of Direct Connect locations and their associated Regions, see [Associated Region](#associated-region).

SiteLink supports a maximum jumbo frame MTU size of either 8500 or 9001, depending on the virtual interface type. For more information, see [MTUs for private virtual interfaces or transit virtual interfaces](#set-jumbo-frames-vif).

## Prerequisites for virtual interfaces
<a name="vif-prerequisites"></a>

Before you create a virtual interface, do the following:
+ Create a connection. For more information, see [Create a connection using the Connection wizard](#create-connection).
+ Create a link aggregation group (LAG) when you have multiple connections that you want to treat as a single one. For information, see [Associate a connection with a LAG](#associate-connection-with-lag).

To create a virtual interface, you need the following information:


| Resource | Required information | 
| --- | --- | 
| Connection | The Direct Connect connection or link aggregation group (LAG) for which you are creating the virtual interface. | 
| Virtual interface name | A name for the virtual interface. | 
| Virtual interface owner | If you're creating the virtual interface for another account, you need the AWS account ID of the other account. | 
| (Private virtual interface only) Connection | For connecting to a VPC in the same AWS Region, you need the virtual private gateway for your VPC. When you attach a private virtual interface directly to a virtual private gateway (with no Direct Connect gateway), the Amazon side of the BGP session uses the ASN that is configured on the virtual private gateway. When you attach the private virtual interface to a Direct Connect gateway instead, the Amazon side uses the Direct Connect gateway's ASN. When you create a virtual private gateway, you can specify your own private ASN. Otherwise, Amazon provides a default ASN. For more information, see [Create a Virtual Private Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg) in the Amazon VPC User Guide. For connecting to a VPC through a Direct Connect gateway, you need the Direct Connect gateway. For more information, see [Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html).    You *can't* use the same ASN for the customer gateway and virtual gateway/Direct Connect gateway on the virtual interface.   You *can* use the same customer gateway ASN for multiple virtual interfaces.   Multiple virtual interfaces can have the same virtual gateway/Direct Connect gateway ASN and customer gateway ASN as long as they are a part of different Direct Connect connections. For example: <br />Virtual gateway (ASN 64,496) <---Virtual interface 1 (Direct Connect connection 1)---> Customer gateway (ASN 64,511) <br />Virtual gateway (ASN 64,496) <---Virtual interface 2 (Direct Connect connection 2)---> Customer gateway (ASN 64,511)     | 
| VLAN | A unique virtual local area network (VLAN) tag that's not already in use on your connection. The value must be between 1 and 4094 and must comply with the Ethernet 802.1Q standard. This tag is required for any traffic traversing the Direct Connect connection. If you have a hosted connection, your AWS Direct Connect Partner provides this value. You can’t modify the value after you have created the virtual interface. | 
| Peer IP addresses |  A virtual interface can support a BGP peering session for IPv4, IPv6, or one of each (dual-stack). Do not use Elastic IPs (EIPs) or Bring your own IP addresses (BYOIP) from the Amazon Pool to create a public virtual interface. You cannot create multiple BGP sessions for the same IP addressing family on the same virtual interface. The IP address ranges are assigned to each end of the virtual interface for the BGP peering session.+  IPv6: Amazon automatically allocates you a /125 IPv6 CIDR. You cannot specify your own peer IPv6 addresses.   | 
| Address family | Whether the BGP peering session will be over IPv4 or IPv6. | 
| BGP information | +  A public or private Border Gateway Protocol (BGP) Autonomous System Number (ASN) for your side of the BGP session. If you are using a public ASN, you must own it. If you are using a private ASN, you can set a custom ASN value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 1 to 2147483647 range. Autonomous System (AS) prepending does not work if you use a private ASN for a public virtual interface. <br />+  AWS enables MD5 by default. You cannot modify this option. <br />+  An MD5 BGP authentication key. You can provide your own, or you can let Amazon generate one for you.  | 
| (Public virtual interface only) Prefixes you want to advertise |  Public IPv4 routes or IPv6 routes to advertise over BGP. You must advertise at least one prefix using BGP, up to a maximum of 1,000 prefixes.+  IPv4: The IPv4 CIDR can overlap with another public IPv4 CIDR announced using Direct Connect when either of the following is true:  The CIDRs are from different AWS Regions. Make sure that you apply BGP community tags on the public prefixes. You use AS\_PATH when you have a public ASN in an active/passive configuration.  <br />For more information, see [Routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html). <br />+  Over a Direct Connect public virtual interface, you can specify any prefix length from /1 to /32 for IPv4 and from /1 to /64 for IPv6. <br />+  You may add additional prefixes to an existing public VIF and advertise those by contacting [AWS support](https://aws.amazon.com/support/createCase). In your support case, provide a list of additional CIDR prefixes you want to add to the public VIF and advertise.  | 
| (Private and transit virtual interfaces only) Jumbo frames | The maximum transmission unit (MTU) of packets over Direct Connect. The default is 1500. Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. Jumbo frames are supported up to 8500 MTU for Direct Connect. Static routes and propagated routes configured in the Transit Gateway Route Table will support Jumbo Frames, including from EC2 instances with VPC static route table entries to the Transit Gateway Attachment. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find Jumbo frame capable on the virtual interface General configuration page. | 

When you create a virtual interface, you can specify the account that owns the virtual interface. When you choose an AWS account that is not your account, the following rules apply:
+ For private VIFs and transit VIFs, the account applies to the virtual interface and the virtual private gateway/Direct Connect gateway destination.
+ For public VIFs, the account is used for virtual interface billing. The Data Transfer Out (DTO) usage is metered toward the resource owner at Direct Connect data transfer rate.

**Note**  
31-Bit prefixes are supported on all Direct Connect virtual interface types. See [RFC 3021: Using 31-Bit Prefixes on IPv4 Point-to-Point Links](https://datatracker.ietf.org/doc/html/rfc3021) for more information.

## MTUs for private virtual interfaces or transit virtual interfaces
<a name="set-jumbo-frames-vif"></a>

Direct Connect supports an Ethernet frame size of 1522 or 9023 bytes (14 bytes Ethernet header \+ 4 bytes VLAN tag \+ bytes for the IP datagram \+ 4 bytes FCS) at the link layer.

The maximum transmission unit (MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a private virtual interface can be either 1500 or 9001 (jumbo frames). The MTU of a transit virtual interface can be either 1500 or 8500 (jumbo frames). You can specify the MTU when you create the interface or update it after you create it. Setting the MTU of a virtual interface to 8500 (jumbo frames) or 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find **Jumbo Frame Capable** on the **Summary** tab.

After you enable jumbo frames for your private virtual interface or transit virtual interface, you can only associate it with a connection or LAG that is jumbo frame capable. Jumbo frames are supported on a private virtual interface attached to either a virtual private gateway or a Direct Connect gateway, or on a transit virtual interface attached to a Direct Connect gateway. If you have two private virtual interfaces that advertise the same route but use different MTU values, or if you have a Site-to-Site VPN that advertise the same route, 1500 MTU is used.

**Important**  
Jumbo frames will apply only to propagated routes via Direct Connect and static routes via Transit Gateways. Jumbo frames on Transit Gateways support only 8500 bytes.   
If an EC2 instance doesn't support jumbo frames, it drops jumbo frames from Direct Connect. All EC2 instance types support jumbo frames except for C1, CC1, T1, and M1. For more information, see [Network Maximum Transmission Unit (MTU) for Your EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network_mtu.html) in the *Amazon EC2 User Guide*.  
For hosted connections, Jumbo frames can be enabled only if originally enabled on the Direct Connect hosted parent connection. If Jumbo frames isn't enabled on that parent connection, then it can't be enabled on any connection.

For the steps to set the MTU for a private virtual interface, see [Set the MTU of a private virtual interface](#interface-set-mtu).

## Direct Connect virtual interfaces
<a name="create-vif"></a>

You can create a transit virtual interface to connect to a Transit Gateway, a public virtual interface to connect to public resources (non-VPC services), or a private virtual interface to connect to a VPC.

To create a virtual interface for accounts within your AWS Organizations, or AWS Organizations that are different from yours, create a hosted virtual interface. 

See the following to create a virtual interface:
+ [Create a public virtual interface](#create-public-vif)
+ [Create a private virtual interface](#create-private-vif)
+ [Create a transit virtual interface to the Direct Connect gateway](#create-transit-vif-dx)

**Prerequisites**  
Before you begin, ensure that you have read the information in [Prerequisites for virtual interfaces](#vif-prerequisites).

### Prerequisites for transit virtual interfaces to a Direct Connect gateway
<a name="dx-vifs-prereqs"></a>

To connect your Direct Connect connection to the Transit Gateway, you must create a transit interface for your connection. Specify the Direct Connect gateway to which to connect.

The maximum transmission unit (MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a private virtual interface can be either 1500 or 9001 (jumbo frames). The MTU of a transit virtual interface can be either 1500 or 8500 (jumbo frames). You can specify the MTU when you create the interface or update it after you create it. Setting the MTU of a virtual interface to 8500 (jumbo frames) or 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find **Jumbo Frame Capable** on the **Summary** tab.

**Important**  
If you associate your Transit Gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the Transit Gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both the Transit Gateway and the Direct Connect gateway, the association request fails.

### Create a Direct Connect public virtual interface
<a name="create-public-vif"></a>

When you create a public virtual interface, it can take up to 72 business hours for us to review and approve your request.

**To provision a public virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Public**.

1. Under **Public virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number (ASN) of your on-premises peer router for the new virtual interface.

       The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support).
**Note**  
When establishing a BGP peering session with AWS over a public virtual interface, use `7224` as the ASN to establish the BGP session on the AWS side. The ASN on your router or customer gateway device should be different from that ASN.

1. Under **Additional settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer IP**, enter the IPv4 CIDR address to use to send traffic to AWS.

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To provide your own BGP key, enter your BGP MD5 key.

      If you do not enter a value, we generate a BGP key. If you provided your own key, or if we generated the key for you, that value displays in the **BGP authentication key** column on the virtual interface details page of **Virtual interfaces**.

   1. To advertise prefixes to Amazon, for **Prefixes you want to advertise**, enter the IPv4 CIDR destination addresses (separated by commas) to which traffic should be routed over the virtual interface. 
**Important**  
You may add additional prefixes to an existing public VIF and advertise those by contacting [AWS support](https://aws.amazon.com/support/createCase). In your support case, provide a list of additional CIDR prefixes you want to add to the public VIF and advertise.

   1. (Optional) For **Bandwidth**, select a bandwidth value to apply a Rate Limiter to this virtual interface. The Rate Limiter sets a maximum bandwidth that the VIF can use, helping prevent this VIF from congesting other VIFs on the same connection. This option is only available on Dedicated connections. For more information, see [Virtual interface Rate Limiters](#vif-rate-limiters).

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

1. Download the router configuration for your device. For more information, see [Download the router configuration file](#vif-router-config).

**To create a public virtual interface using the command line or API**
+ [create-public-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-public-virtual-interface.html) (AWS CLI)
+ [CreatePublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePublicVirtualInterface.html) (Direct Connect API)

### Create a Direct Connect private virtual interface
<a name="create-private-vif"></a>

You can provision a private virtual interface to a virtual private gateway in the same Region as your Direct Connect connection. For more information about provisioning a private virtual interface to a Direct Connect gateway, see [Direct Connect gateways](#direct-connect-gateways).

If you use the VPC wizard to create a VPC, route propagation is automatically enabled for you. With route propagation, routes are automatically populated to the route tables in your VPC. If you choose, you can disable route propagation. For more information, see [Enable Route Propagation in Your Route Table](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-configure-routing) in the *Amazon VPC User Guide*.

The maximum transmission unit (MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a private virtual interface can be either 1500 or 9001 (jumbo frames). The MTU of a transit virtual interface can be either 1500 or 8500 (jumbo frames). You can specify the MTU when you create the interface or update it after you create it. Setting the MTU of a virtual interface to 8500 (jumbo frames) or 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find **Jumbo Frame Capable** on the **Summary** tab.

**To provision a private virtual interface to a VPC**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, choose **Private**.

1. Under **Private virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Virtual interface owner**, choose **My AWS account** if the virtual interface is for your AWS account.

   1.  For **Direct Connect gateway**, select the Direct Connect gateway.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support).

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 8500 (jumbo frames), select **Jumbo MTU (MTU size 8500)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) For **Bandwidth**, select a bandwidth value to apply a Rate Limiter to this virtual interface. The Rate Limiter sets a maximum bandwidth that the VIF can use, helping prevent this VIF from congesting other VIFs on the same connection. This option is only available on Dedicated connections. For more information, see [Virtual interface Rate Limiters](#vif-rate-limiters).

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

1. Download the router configuration for your device. For more information, see [Download the router configuration file](#vif-router-config).

**To create a private virtual interface using the command line or API**
+ [create-private-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-private-virtual-interface.html) (AWS CLI)
+ [CreatePrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePrivateVirtualInterface.html) (Direct Connect API)

### Create a transit virtual interface to the Direct Connect gateway
<a name="create-transit-vif-dx"></a>

Before connecting a transit virtual interface to the Direct Connect gateway, familiarize yourself with the [prerequisites for transit virtual interfaces](#dx-vifs-prereqs).

**To provision a transit virtual interface to a Direct Connect gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Transit**.

1. Under **Transit virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Virtual interface owner**, choose **My AWS account** if the virtual interface is for your AWS account.

   1.  For **Direct Connect gateway**, select the Direct Connect gateway.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.  
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 8500 (jumbo frames), select **Jumbo MTU (MTU size 8500)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) For **Bandwidth**, select a bandwidth value to apply a Rate Limiter to this virtual interface. The Rate Limiter sets a maximum bandwidth that the VIF can use, helping prevent this VIF from congesting other VIFs on the same connection. This option is only available on Dedicated connections. For more information, see [Virtual interface Rate Limiters](#vif-rate-limiters).

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

After you create the virtual interface, you can download the router configuration for your device. For more information, see [Download the router configuration file](#vif-router-config).

**To create a transit virtual interface using the command line or API**
+ [create-transit-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-transit-virtual-interface.html) (AWS CLI)
+ [CreateTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateTransitVirtualInterface.html) (Direct Connect API)

**To view the virtual interfaces that are attached to a Direct Connect gateway using the command line or API**
+ [describe-direct-connect-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-attachments.html) (AWS CLI)
+ [DescribeDirectConnectGatewayAttachments](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.html) (Direct Connect API)

### Download the Direct Connect router configuration file
<a name="vif-router-config"></a>

After you create the virtual interface and the interface state is up, you can download the router configuration file for your router.

If you use any of the following routers for virtual interfaces that have MACsec turned on, we automatically create the configuration file for your router:
+ Cisco Nexus 9K\+ Series switches running NX-OS 9.3 or later software
+ Juniper Networks M/MX Series Routers running JunOS 9.5 or later software

**To download the router configuration file**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Choose **Download router configuration**.

1. For **Download router configuration**, do the following:

   1. For **Vendor**, select the manufacturer of your router.

   1. For **Platform**, select the model of your router.

   1. For **Software**, select the software version for your router.

1. Choose **Download**, and then use the appropriate configuration for your router to ensure that you can connect to Direct Connect.

1. If you need to manually configure your router for MACsec, use the following table as a guideline.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>CKN length</td><td>This is a 64 hexadecimal character (0–9, A–E) string. Use the full length to maximize cross-platform compatibility.</td></tr>
  <tr><td>CAK length</td><td>This is a 64 hexadecimal character (0–9, A–E) string. Use the full length to maximize cross-platform compatibility.</td></tr>
  <tr><td>Cryptographic algorithm</td><td>AES_256_CMAC</td></tr>
  <tr><td>SAK Cipher Suite</td><td> <ul><li> For 100 Gbps connections: GCM_AES_XPN_256  </li><li> For 10 Gbps connections: GCM_AES_XPN_256 or GCM_AES _256 </li></ul> </td></tr>
  <tr><td>Key Cipher Suite</td><td>16</td></tr>
  <tr><td>Confidentiality Offset</td><td>0</td></tr>
  <tr><td>ICV Indicator</td><td>No</td></tr>
  <tr><td>SAK Rekey Time</td><td>PN Rollover&gt;</td></tr>
</tbody>
</table>


## Virtual interface Rate Limiters
<a name="vif-rate-limiters"></a>

Use virtual interface (VIF) Rate Limiters to set a maximum bandwidth allocation for individual VIFs on a Direct Connect Dedicated connection. Rate Limiters help prevent network congestion caused by unexpected traffic spikes on a VIF, which can potentially consume all available bandwidth and impact workloads on other VIFs sharing the same dedicated connection. This feature is only supported on Dedicated connections. Hosted connections are always rate-limited to the purchased capacity.

### How VIF Rate Limiters work
<a name="vif-rate-limiters-how-it-works"></a>

A Dedicated connection supports multiple private, transit, and public VIFs (see [Direct Connect quotas](#limits) for current details). By default, all VIFs on a connection can utilize 100% of the underlying connection's capacity. This means that a workload on one VIF can unexpectedly increase its utilization, causing congestion, packet loss, and potential disruption to workloads on other VIFs on that connection. This situation is commonly referred to as a "noisy neighbor" congestion event.

When you apply a Rate Limiter to a VIF, you set a maximum bandwidth that the VIF can use. If traffic on the rate-limited VIF exceeds the configured capacity, excess packets are dropped by the Direct Connect edge devices, preventing that VIF from consuming bandwidth needed by other VIFs on the same connection.

**Rate Limiters and traffic direction**  
Rate Limiters operate both on traffic leaving AWS to on-premises, and coming from on-premises into AWS. However, customer physical connections can terminate on the same device that applies the Rate Limiter policy or a different device. Direct Connect uses different device configurations to offer the service globally. The difference in devices will result in different behavior for Rate Limiters depending on the direction of your traffic.
+ **Traffic leaving AWS (Egress):** For egress traffic, VIFs are always provisioned on the same device that applies the Rate Limiter. Your applications can send traffic to on-premises in excess of a VIF's set bandwidth and the device will apply the Rate Limiter, dropping traffic down to your set bandwidth. This will protect all VIFs on the connection.
+ **Traffic coming into AWS (Ingress):** For traffic flowing from on-premises to AWS, your VIFs may be provisioned on a different upstream device than the device that terminates your physical connection. Therefore, your on-premises applications could potentially send traffic in excess of a VIF's set bandwidth, and congest the physical port before the Rate Limiters are applied. We recommend that you consider applying policers on your on-premises device to mitigate unexpected congestion events before traffic leaves your network towards AWS.

### Prerequisites and limitations
<a name="vif-rate-limiters-prerequisites"></a>
+ Rate Limiters are supported only on **Dedicated connections**. They are not supported on hosted connections.
+ You can apply Rate Limiters to VIFs of any type: private, public, and transit.
+ Each dedicated connection supports up to **10 rate limiters**. You can request a limit increase through AWS Service Quotas.
+ Hosted connections are automatically rate-limited to their purchased bandwidth. VIFs created on hosted connections cannot exceed the hosted connection's purchased speed.

### Available bandwidth options
<a name="vif-rate-limiters-bandwidth-options"></a>

The available bandwidth options depend on the speed of your underlying dedicated connection or link aggregation group (LAG). Rate Limiters are fully supported on VIFs created on link aggregation groups (LAGs). When you use a LAG, the feature is aware of the LAG's combined capacity and offers higher bandwidth options than would be available on a single connection.

For example:
+ On a 1 Gbps Dedicated connection, you can set Rate Limiters between 50 Mbps and 1 Gbps.
+ On a LAG combining 2×1 Gbps connections, you can set Rate Limiters between 50 Mbps and 2 Gbps.

### Rate Limiters and oversubscription
<a name="vif-rate-limiters-oversubscription"></a>

Rate Limiters are a static bandwidth allocation at the VIF level. They do not track actual utilization of other VIFs on the same Dedicated connection. You can allocate bandwidth to your VIFs in excess of the underlying connection's capacity (oversubscription).

VIFs without a Rate Limiter applied are considered **Unlimited** and can use up to 100% of the connection or LAG's capacity. Unlimited VIFs can congest other VIFs on the same connection, but rate-limited VIFs cannot exceed their allocated bandwidth.

You can use this behavior to establish a priority hierarchy between your VIFs. For example, you can leave a critical workload's VIF as Unlimited while applying Rate Limiters to non-critical workloads, ensuring that non-critical VIFs cannot congest the critical one.

Use the **Rate Limiters** tab in the Connection/LAG view to get a summary view of all VIFs on the connection and their bandwidth allocation. The **Rate Limiters** tab also shows the connection's current level of oversubscription. This is calculated as the allocated bandwidth across all VIFs over the underlying connection's maximum capacity. Unlimited VIFs are counted as 100% of the capacity. This allows you to quickly understand which VIFs can potentially congest others.

### Monitoring with CloudWatch
<a name="vif-rate-limiters-monitoring"></a>

When you apply a Rate Limiter to a VIF, the following metrics are published to CloudWatch. You can use these metrics to create CloudWatch alarms.

#### Policed packets and bytes metrics
<a name="vif-rate-limiters-policed-metrics"></a>

These metrics report the amount of traffic dropped by the Rate Limiter when a VIF exceeds its allocated bandwidth.


| Metric | Description | 
| --- | --- | 
| VirtualInterfacePolicedPpsIngress | The number of packets per second traveling from your on-premises network to AWS that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 
| VirtualInterfacePolicedPpsEgress | The number of packets per second traveling from AWS to your on-premises network that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 
| VirtualInterfacePolicedBpsIngress | The number of bytes per second traveling from your on-premises network to AWS that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 
| VirtualInterfacePolicedBpsEgress | The number of bytes per second traveling from AWS to your on-premises network that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 

#### Utilization metrics
<a name="vif-rate-limiters-utilization-metrics"></a>

These metrics report the percentage utilization of a rate-limited VIF relative to its configured bandwidth. This metric is derived automatically, and does not require you to apply CloudWatch Math.

**Note**  
When you change a VIF's allocated bandwidth, you might see a step change in the percentage utilization of the VIF, depending on the traffic going through when you make the change. For example, if you have a VIF configured to be rate-limited at 1 Gbps and that VIF had a constant 500 Mbps of egress traffic, you will see `VirtualInterfaceUtilizationEgress` at 50% utilization. If you increase that VIF's allocation to 2 Gbps, that utilization will drop to 25% as soon as the change is provisioned and the utilization metric is recalculated using the new configured capacity for that VIF.


| Metric | Description | 
| --- | --- | 
| VirtualInterfaceUtilizationIngress | Percentage utilization of the VIF based on its configured bandwidth, for traffic traveling from your on-premises network to AWS. | 
| VirtualInterfaceUtilizationEgress | Percentage utilization of the VIF based on its configured bandwidth, for traffic traveling from AWS to your on-premises network. | 

**Note**  
The utilization metric reports traffic *before* rate limiting is applied. During congestion, you may see utilization above 100% in the direction where traffic exceeds the VIF's bandwidth. At the same time, the corresponding `PolicedPps` and `PolicedBps` metrics report the amount of traffic dropped. This behavior helps you:  
Understand the total volume of traffic being received, which is useful when you are actively remediating a congestion event by shutting down traffic sources.
Determine by how much your application exceeded the bandwidth allocation, helping you decide whether to adjust the VIF's bandwidth setting.

### Configuring a Rate Limiter
<a name="vif-rate-limiters-configure"></a>

Rate Limiters can be configured on a VIF when it is created (in the Additional Settings section of the Create virtual interface view), or on an existing VIF.

**To apply or remove a Rate Limiter from an existing virtual interface (Console)**

1. Open the Direct Connect console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the Dedicated connection that contains the VIF you want to rate-limit.

1. Choose the **Rate Limiters** tab to view the current rate limiter allocations for the connection.

1. Select the virtual interface you want to configure.

1. Choose **Edit**.

1. For **Bandwidth**, select a bandwidth value from the available options. To remove a Rate Limiter, select **Unlimited**.

1. Choose **Edit virtual interface** to save changes.

## Hosted Direct Connect virtual interfaces
<a name="hosted-vif"></a>

To use your Direct Connect connection with another account, you can create a hosted virtual interface for that account. The owner of the other account must accept the hosted virtual interface to begin using it. A hosted virtual interface works the same as a standard virtual interface and can connect to public resources or a VPC.

You can use transit virtual interfaces with Direct Connect dedicated or hosted connections of any speed. Hosted connections support only one virtual interface.

To create a virtual interface, you need the following information:


| Resource | Required information | 
| --- | --- | 
| Connection | The Direct Connect connection or link aggregation group (LAG) for which you are creating the virtual interface. | 
| Virtual interface name | A name for the virtual interface. | 
| Virtual interface owner | If you're creating the virtual interface for another account, you need the AWS account ID of the other account. | 
| (Private virtual interface only) Connection | For connecting to a VPC in the same AWS Region, you need the virtual private gateway for your VPC. The ASN for the Amazon side of the BGP session is inherited from the virtual private gateway. When you create a virtual private gateway, you can specify your own private ASN. Otherwise, Amazon provides a default ASN. For more information, see [Create a Virtual Private Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg) in the Amazon VPC User Guide. For connecting to a VPC through a Direct Connect gateway, you need the Direct Connect gateway. For more information, see [Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html). | 
| VLAN | A unique virtual local area network (VLAN) tag that's not already in use on your connection. The value must be between 1 and 4094 and must comply with the Ethernet 802.1Q standard. This tag is required for any traffic traversing the Direct Connect connection. If you have a hosted connection, your AWS Direct Connect Partner provides this value. You can’t modify the value after you have created the virtual interface. | 
| Peer IP addresses |  A virtual interface can support a BGP peering session for IPv4, IPv6, or one of each (dual-stack). Do not use Elastic IPs (EIPs) or Bring your own IP addresses (BYOIP) from the Amazon Pool to create a public virtual interface. You cannot create multiple BGP sessions for the same IP addressing family on the same virtual interface. The IP address ranges are assigned to each end of the virtual interface for the BGP peering session. +  IPv4:   (Public virtual interface only) You must specify unique public IPv4 addresses that you own. The value can be one of the following:  A customer-owned IPv4 CIDR <br />These can be any public IPs (customer-owned or provided by AWS), but the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/31` range, such as `203.0.113.0/31`, you could use `203.0.113.0` for your peer IP and `203.0.113.1` for the AWS peer IP. Or, if you allocate a `/24` range, such as `198.51.100.0/24`, you could use `198.51.100.10` for your peer IP and `198.51.100.20` for the AWS peer IP.  An IP range owned by your AWS Direct Connect Partner or ISP, along with an LOA-CFA authorization  An AWS-provided /31 CIDR. Contact [AWS Support](https://aws.amazon.com/support/createCase) to request a public IPv4 CIDR (and provide a use case in your request)We cannot guarantee that we will be able to fulfill all requests for AWS-provided public IPv4 addresses.     (Private virtual interface only) Amazon can generate private IPv4 addresses for you. If you specify your own, ensure that you specify private CIDRs for your router interface and the AWS Direct Connect interface only. For example, do not specify other IP addresses from your local network. Similar to a public virtual interface, the same subnet mask must be used for both your peer IP and the AWS router peer IP. For example, if you allocate a `/30` range, such as `192.168.0.0/30`, you could use `192.168.0.1` for your peer IP and `192.168.0.2` for the AWS peer IP.   <br />+  IPv6: Amazon automatically allocates you a /125 IPv6 CIDR. You cannot specify your own peer IPv6 addresses.   | 
| Address family | Whether the BGP peering session will be over IPv4 or IPv6. | 
| BGP information | +  A public or private Border Gateway Protocol (BGP) Autonomous System Number (ASN) for your side of the BGP session. If you are using a public ASN, you must own it. If you are using a private ASN, you can set a custom ASN value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 1 to 4294967294 range. Autonomous System (AS) prepending does not work if you use a private ASN for a public virtual interface. <br />+  AWS enables MD5 by default. You cannot modify this option. <br />+  An MD5 BGP authentication key. You can provide your own, or you can let Amazon generate one for you.  | 
| (Public virtual interface only) Prefixes you want to advertise |  Public IPv4 routes or IPv6 routes to advertise over BGP. You must advertise at least one prefix using BGP, up to a maximum of 1,000 prefixes.+  IPv4: The IPv4 CIDR can overlap with another public IPv4 CIDR announced using Direct Connect when either of the following is true:  The CIDRs are from different AWS Regions. Make sure that you apply BGP community tags on the public prefixes. You use AS\_PATH when you have a public ASN in an active/passive configuration.  <br />For more information, see [Routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html). <br />+  Over a Direct Connect public virtual interface, you can specify any prefix length from /1 to /32 for IPv4 and from /1 to /64 for IPv6. <br />+  You may add additional prefixes to an existing public VIF and advertise those by contacting [AWS support](https://aws.amazon.com/support/createCase). In your support case, provide a list of additional CIDR prefixes you want to add to the public VIF and advertise.  | 
| (Private and transit virtual interfaces only) Jumbo frames | The maximum transmission unit (MTU) of packets over Direct Connect. The default is 1500. Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. Jumbo frames apply only to propagated routes from Direct Connect. If you add static routes to a route table that point to your virtual private gateway, then traffic routed through the static routes is sent using 1500 MTU. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find Jumbo frame capable on the virtual interface General configuration page. | 

### Create a hosted private virtual interface in Direct Connect
<a name="create-hosted-private-vif"></a>

Before you begin, ensure that you have read the information in [Prerequisites for virtual interfaces](#vif-prerequisites).

**To create a hosted private virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Private**.

1. Under **Private virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Virtual interface owner**, choose **Another AWS account**, and then for **Virtual interface owner**, enter the ID of the account to own this virtual interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.  
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 8500 (jumbo frames), select **Jumbo MTU (MTU size 8500)**.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. After the hosted virtual interface is accepted by the owner of the other AWS account, you can download the configuration file. For more information, see [Download the router configuration file](#vif-router-config).

**To create a hosted private virtual interface using the command line or API**
+ [allocate-private-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/allocate-private-virtual-interface.html) (AWS CLI)
+ [AllocatePrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocatePrivateVirtualInterface.html) (Direct Connect API)

### Create a hosted public virtual interface in Direct Connect
<a name="create-hosted-public-vif"></a>

Before you begin, ensure that you have read the information in [Prerequisites for virtual interfaces](#vif-prerequisites).

**To create a hosted public virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Public**.

1. Under **Public Virtual Interface Settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Virtual interface owner**, choose **Another AWS account**, and then for **Virtual interface owner**, enter the ID of the account to own this virtual interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. To configure an IPv4 BGP or an IPv6 peer, do the following:

   [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
   + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
   + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.

   [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

1. To advertise prefixes to Amazon, for **Prefixes you want to advertise**, enter the IPv4 CIDR destination addresses (separated by commas) to which traffic should be routed over the virtual interface. 

1. To provide your own key to authenticate the BGP session, under **Additional Settings**, for **BGP authentication key**, enter the key.

   If you do not enter a value, then we generate a BGP key.

1. (Optional) Add or remove a tag.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

1. After the hosted virtual interface is accepted by the owner of the other AWS account, you can download the configuration file. For more information, see [Download the router configuration file](#vif-router-config).

**To create a hosted public virtual interface using the command line or API**
+ [allocate-public-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/allocate-public-virtual-interface.html) (AWS CLI)
+ [AllocatePublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocatePublicVirtualInterface.html) (Direct Connect API)

### Create a Direct Connect hosted transit virtual interface
<a name="create-hosted-transit-vif"></a>

**To create a hosted transit virtual interface**
**Important**  
If you associate your Transit Gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the Transit Gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both the Transit Gateway and the Direct Connect gateway, the association request fails.

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Transit**.

1. Under **Transit virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Virtual interface owner**, choose **Another AWS account**, and then for **Virtual interface owner**, enter the ID of the account to own this virtual interface.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

       The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support).

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 8500 (jumbo frames), select **Jumbo MTU (MTU size 8500)**.

   1. [Optional] Add a tag. Do the following:

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

1. After the hosted virtual interface is accepted by the owner of the other AWS account, you can download the router configuration file for your device. For more information, see [Download the router configuration file](#vif-router-config).

**To create a hosted transit virtual interface using the command line or API**
+ [allocate-transit-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/allocate-public-transit-interface.html) (AWS CLI)
+ [AllocateTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateTransitVirtualInterface.html) (Direct Connect API)

## View Direct Connect virtual interface details
<a name="viewvifdetails"></a>

You can view the current status of your virtual interface using either the Direct Connect console or using the command line or API. Details include:
+ Connection state
+ Name
+ Location
+ VLAN
+ BGP details
+ Peer IP addresses

**To view details about a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

**To describe virtual interfaces using the command line or API**
+ [describe-virtual-interfaces](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-virtual-interfaces.html) (AWS CLI)
+ [DescribeVirtualInterfaces](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualInterfaces.html) (Direct Connect API)

## BGP-specific settings
<a name="bgp-specific-settings"></a>

The following Border Gateway Protocol (BGP) settings are used by Direct Connect:

### BGP settings
<a name="bgp-settings"></a>


| Setting | Value | Notes | 
| --- | --- | --- | 
| Default hold timer | 90 seconds |  | 
| Minimum hold timer | 3 seconds | A hold value of 0 is not supported. | 
| Default keepalive timer | 30 seconds |  | 
| Minimum keepalive timer | 1 second |  | 
| Graceful restart timer | 120 seconds | We recommend that you do not configure graceful restart and BFD at the same time. | 
| BFD liveness detection minimum interval | 300 ms |  | 
| BFD minimum multiplier | 3 |  | 
| BGP Packet TTL Value | 1 | Your device must support accepting BGP packets with a TTL value of 1. Direct Connect currently does not support multihop BGP or setting a different TTL value. | 

BGP timers negotiate down to the lowest configured value between the peers. BFD intervals use the largest mutually agreed upon timer (the slower rate), where the actual transmission rate is the maximum of the local minimum transmission interval (`DesiredMinTxInterval`) and the peer's minimum receive interval (`RequiredMinRxInterval`). Because transmission rates are negotiated independently for each direction, BFD intervals can be asymmetric. The final failure detection time is calculated by multiplying the negotiated transmission interval by the local detection multiplier.

### Autonomous System Number (ASN) ranges
<a name="asn-ranges"></a>

When configuring your virtual interface you must set an ASN. Direct Connect supports 2-byte and 4-byte ASNs. For more information, see [Long ASN support in Direct Connect](#long-asn-support). The following ranges are supported:

**Customer-side ASN range**: 1 to 4,294,967,294
+ ASNs: 1 to 2,147,483,647
+ Long ASNs: 1 to 4,294,967,294

**Private ASN ranges**:
+ Private ASNs: 64,512 to 65,534
+ Private long ASNs: 4,200,000,000 to 4,294,967,294

**Note**  
For public virtual interfaces, your ASN must be either a private ASN or a public ASN already registered and allowed for use with the virtual interface.

## Long ASN support in Direct Connect
<a name="long-asn-support"></a>

Support for long ASNs (4-byte) allows you to configure long Autonomous System Numbers (ASNs) as part of the parameters of the BGP session established between the AWS network device and your network device. This feature is enabled or disabled on a per-account basis.

You can set an ASN or Long ASN range on either the console or through the APIs.
+ When using the console, the **ASN** field supports both ASNs and long ASNs. You can add any range from 1 to 4294967294.
+ When using the APIs to create a virtual interface, you can specify either an ASN (`asn`) or the Long ASN (`asnLong`) but not both. For more information on using ASN or Long ASN, see the following APIs in the [*Direct Connect API Reference*](https://docs.aws.amazon.com/directconnect/latest/APIReference/Welcome.html):
  + `BGPPeer`
  + `DeleteBGPPeerRequest`
  + `NewBGPPeer`
  + `NewPrivateVirtualInterface`
  + `NewPrivateVirtualInterfaceAllocation`
  + `NewPublicVirtualInterface`
  + `NewPublicVirtualInterfaceAllocation`
  + `NewTransitVirtualInterface`
  + `NewTransitVirtualInterfaceAllocation`
  + `VirtualInterface`

### Considerations
<a name="long-asn-considerations"></a>

When choosing to use either an ASN or a long ASN, note the following:
+ **Backward compatibility**: Direct Connect automatically handles BGP sessions with both ASN and long ASN-capable routers. If your router doesn't support long ASNs, the BGP session will operate in ASN mode.
+ **ASN format**: Specify 4-byte ASNs in asplain format, for example, `4200000000`. Direct Connect displays 4-byte ASNs in asplain format.
+ **Private ASN ranges**: When using private long ASNs (`4200000000-4294967294`), the same replacement behavior applies as with private ASNs. Direct Connect will replace your private ASN with `7224` when advertising to other networks.
+ **BGP community tags**: All existing BGP community tags (`7224:xxxx`) work with long ASNs. The community tag format remains unchanged.
+ **Monitoring and troubleshooting**: CloudWatch metrics, BGP session logs, and troubleshooting tools display long ASNs in asplain format for consistency.

## Add a BGP peer to a Direct Connect virtual interface
<a name="add-peer-to-vif"></a>

Add or delete an IPv4 or IPv6 BGP peering session to your virtual interface using either the Direct Connect console or using the command line or API.

A virtual interface can support a single IPv4 BGP peering session and a single IPv6 BGP peering session. You cannot specify your own peer IPv6 addresses for an IPv6 BGP peering session. Amazon automatically allocates you a /125 IPv6 CIDR. 

Multi-protocol BGP is not supported. IPv4 and IPv6 operate in dual-stack mode for the virtual interface.

AWS enables MD5 by default. You cannot modify this option.

Use the following procedure to add a BGP peer.

**To add a BGP peer**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Choose **Add peering**.

1. (Private virtual interface) To add IPv4 BGP peers, do the following:
   + Choose **IPv4**.
   + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.

1. (Public virtual interface) To add IPv4 BGP peers, do the following:
   + For **Your router peer ip**, enter the IPv4 CIDR destination address where traffic should be sent.
   + For **Amazon router peer IP**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

1. (Private or public virtual interface) To add IPv6 BGP peers, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses; you cannot specify custom IPv6 addresses.

1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

   For a public virtual interface, the ASN must be private or already on the allow list for the virtual interface.

   The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483646) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support).

   Note that if you do not enter a value, we automatically assign one.

1. To provide your own BGP key, for **BGP Authentication Key**, enter your BGP MD5 key.

1. Choose **Add peering**.

**To create a BGP peer using the command line or API**
+ [create-bgp-peer](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-bgp-peer.html) (AWS CLI)
+ [CreateBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateBGPPeer.html) (Direct Connect API)

## Delete a Direct Connect virtual interface BGP peer
<a name="delete-bgp-peer-vif"></a>

If your virtual interface has both an IPv4 and IPv6 BGP peering session, you can delete one of the BGP peering sessions (but not both). You can delete a virtual interface BGP peer using either the Direct Connect console or using the command line or API.

**To delete a BGP peer**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Under **Peerings,** select the peering that you want to delete and then choose **Delete**.

1. In the **Remove peering from virtual interface** dialog box, choose **Delete**.

**To delete a BGP peer using the command line or API**
+ [delete-bgp-peer](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-bgp-peer.html) (AWS CLI)
+ [DeleteBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteBGPPeer.html) (Direct Connect API)

## Set the MTU of a Direct Connect private virtual interface
<a name="interface-set-mtu"></a>

If your virtual interface has both an IPv4 and IPv6 BGP peering session, you can delete one of the BGP peering sessions (but not both). For more information about MTUs and private virtual interfaces, see [MTUs for private virtual interfaces or transit virtual interfaces](#set-jumbo-frames-vif.title).

You can set the MTU of a private virtual interface using either the Direct Connect console or using the command line or API.

**To set the MTU of a private virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1.  Select the virtual interface and then choose **Edit**.

1. Under **Jumbo MTU (MTU size 8500)**, select **Enabled**.

1. Under **Acknowledge**, select **I understand the selected connection(s) will go down for a brief period**. The state of the virtual interface is `pending` until the update is complete.

**To set the MTU of a private virtual interface using the command line or API**
+ [update-virtual-interface-attributes](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-virtual-interface-attributes.html) (AWS CLI)
+ [UpdateVirtualInterfaceAttributes](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateVirtualInterfaceAttributes.html) (Direct Connect API)

## Add or remove Direct Connect virtual interface tags
<a name="modify-tags-vif"></a>

Tags provide a way to identify the virtual interface. You can add or remove a tag using either the Direct Connect console or using the command line or API if you are the account owner for the virtual interface.

**To add or remove a virtual interface tag**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1.  Select the virtual interface and then choose **Edit**.

1. Add or remove a tag.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Edit virtual interface**.

**To add a tag or remove a tag using the command line**
+ [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/tag-resource.html) (AWS CLI) 
+ [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/untag-resource.html) (AWS CLI) 

## Delete a Direct Connect virtual interface
<a name="deletevif"></a>

Delete one or more virtual interfaces. Before you can delete a connection, you must delete its virtual interface. Deleting a virtual interface stops Direct Connect data transfer charges associated with the virtual interface.

You can delete a virtual interface using either the Direct Connect console or the command line or API.

**To delete a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **Virtual Interfaces**.

1. Select the virtual interfaces and then choose **Delete**.

1. In the **Delete** confirmation dialog box, choose **Delete**.

**To delete a virtual interface using the command line or API**
+ [delete-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-virtual-interface.html) (AWS CLI)
+ [DeleteVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteVirtualInterface.html) (Direct Connect API)

## Accept a hosted Direct Connect virtual interface
<a name="accepthostedvirtualinterface"></a>

Before you can begin using a hosted virtual interface, you must accept the virtual interface. For a private virtual interface, you must also have an existing virtual private gateway or Direct Connect gateway. For a transit virtual interface, you must have an existing Transit Gateway or Direct Connect gateway.

You can accept a hosted virtual interface using either the Direct Connect console or the command line or API.

**To accept a hosted virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Choose **Accept**.

1. This applies to private virtual interfaces and transit virtual interfaces.

   (Transit virtual interface) In the **Accept virtual interface** dialog box, select a Direct Connect gateway, and then choose **Accept virtual interface**.

   (Private virtual interface) In the **Accept virtual interface** dialog box, select a virtual private gateway or Direct Connect gateway, and then choose **Accept virtual interface**.

1. After you accept the hosted virtual interface, the owner of the Direct Connect connection can download the router configuration file. The **Download router configuration** option is not available for the account that accepts the hosted virtual interface.

**To accept a hosted private virtual interface using the command line or API**
+ [confirm-private-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/confirm-private-virtual-interface.html) (AWS CLI)
+ [ConfirmPrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmPrivateVirtualInterface.html) (Direct Connect API)

**To accept a hosted public virtual interface using the command line or API**
+ [confirm-public-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/confirm-public-virtual-interface.html) (AWS CLI)
+ [ConfirmPublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmPublicVirtualInterface.html) (Direct Connect API)

**To accept a hosted transit virtual interface using the command line or API**
+ [confirm-transit-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/confirm-transit-virtual-interface.html) (AWS CLI)
+ [ConfirmTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirTransitVirtualInterface.html) (Direct Connect API)

## Migrate a Direct Connect virtual interface
<a name="migratevirtualinterface"></a>

Use this procedure when you want to perform any of the following virtual interface migration operations:
+  Migrate an existing virtual interface associated with a connection to another LAG.
+  Migrate an existing virtual interface associated with an existing LAG to a new LAG.
+ Migrate an existing virtual interface associated with a connection to another connection.

**Note**  
You can migrate a virtual interface to a new connection within the same Region, but you can't migrate it from one Region to another. When you migrate or associate an existing virtual interface to a new connection, the configuration parameters associated with those virtual interfaces are the same. To work around this, you can pre-stage the configuration on the connection, and then update the BGP configuration. 
You can't migrate a VIF from one hosted connection to another hosted connection. VLAN IDs are unique; therefore, migrating a VIF in this way would mean the VLANs don't match. You either need to delete the connection or VIF, and then recreate that using a VLAN that's the same for both the connection and the VIF.

**Important**  
The virtual interface will go down for a brief period. We recommend you perform this procedure during a maintenance window.

**To migrate a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface, and then choose **Edit**.

1. For **Connection**, select the LAG or connection.

1. Choose **Edit virtual interface**.

**To migrate a virtual interface using the command line or API**
+ [associate-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/associate-virtual-interface.html) (AWS CLI)
+ [AssociateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateVirtualInterface.html) (Direct Connect API)

# Inbound prefix controls for Direct Connect
<a name="prefix-controls"></a>

Inbound prefix controls let you manage how many on-premises route prefixes you can advertise to AWS on your Direct Connect private and transit virtual interfaces (VIFs). Prefix controls create capacity pools of prefixes at the dedicated connection level and at the Direct Connect gateway (DXGW) level. With the new controls, you allocate a specific number of prefixes to a new private or transit VIF, or edit an existing VIF's allocation. You then attach that VIF to a DXGW or a virtual private gateway (VGW). That VIF then consumes the value you allocated from the dedicated connection's pool and from the DXGW's pool. This allows you to have, on the same dedicated connection, for example, a transit VIF with an allocation of 1,000 prefixes and a private VIF with an allocation of 50 prefixes. If you don't select any value, AWS applies the default allocation of 100 prefixes per address family.

The following table summarizes the key limits for inbound prefix controls.


| Limit | Value | 
| --- | --- | 
| Prefix pool per dedicated connection | 5,000 (1/10 Gbps), 30,000 (100 Gbps), 50,000 (400 Gbps) | 
| Maximum allocation per VIF | 1,000 per address family (IPv4 and IPv6) | 
| Default allocation per VIF | 100 per address family (IPv4 and IPv6) | 
| Total allocations per DXGW | 10,000 (combined IPv4 \+ IPv6) | 
| Maximum VIF attachments per DXGW | 30 | 

Public VIFs are not managed by inbound prefix controls. Public VIFs retain the existing limit of 1,000 inbound prefixes.

## How prefix controls work
<a name="prefix-controls-how-it-works"></a>

Each Direct Connect dedicated connection has a prefix pool — the total number of inbound route prefixes allowed across all VIFs on that connection. The pool size depends on the connection speed. In the case of hosted connections, the underlying physical connections are owned by a partner, so there is no pool that can be managed by the end customers of the hosted connections. Private and transit VIFs created on a hosted connection can be allocated a prefix number by the customer, and that allocation is not counted against a connection's pool.

The following table shows the prefix pool sizes for each connection speed.


| Connection speed | Prefix pool size (IPv4) | Prefix pool size (IPv6) | 
| --- | --- | --- | 
| 1 Gbps | 5,000 | 5,000 | 
| 10 Gbps | 5,000 | 5,000 | 
| 100 Gbps | 30,000 | 30,000 | 
| 400 Gbps | 50,000 | 50,000 | 

When you create or update a VIF, you specify how many prefixes to allocate to that VIF from the connection's pool. The default allocation is 100 prefixes per VIF for each address family (IPv4 and IPv6). You can increase the allocation up to 1,000 prefixes per VIF for each address family. To request a higher limit, contact your Solutions Architect (SA) or Technical Account Manager (TAM). Manual limit increase requests are reviewed on a case-by-case basis.

The prefix pool tracks the following four states:

Pool size (Allowed)  
The total number of prefixes the connection can support. The connection speed determines this value, and you cannot change it.

Allocated  
The number of prefixes reserved on a specific VIF. You set this value when you create or update a VIF.

Available (Unallocated)  
The remaining prefixes in the pool that you haven't allocated to any VIF. This value equals the pool size minus the sum of all VIF allocations.

In use  
The actual number of prefixes your on-premises router is currently advertising on a VIF.

**Important**  
If the number of prefixes advertised on a VIF exceeds the allocated count, the BGP session on that VIF will go down and enter an idle state (BGP DOWN). Ensure that your allocation is at least as large as the number of prefixes you plan to advertise.

**Note**  
You cannot reduce the allocated prefix count for a VIF below the number of prefixes currently in use. To reduce the allocation, first reduce the number of prefixes advertised by your on-premises device.

**Note**  
A private virtual interface can be attached to a virtual private gateway that propagates routes into a VPC route table. When it is, the propagated routes are also subject to VPC route table quotas. This quota can be lower than the prefix allocation you set on the VIF, and increasing the VIF's inbound prefix allocation does not raise it. If your private virtual interface advertises more routes than the VPC route table quota allows, the route table might not install all of the propagated routes. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-route-tables) in the *Amazon VPC User Guide*.

## DXGW prefix limits
<a name="prefix-controls-dx-gateway-limits"></a>

Each DXGW has a total prefix pool limit of 10,000 that is shared between all the VIFs attached to it. This limit adds all IPv4 and IPv6 prefix allocations across all VIFs attached to the DXGW. The DXGW also maintains the maximum of 30 VIF attachments. If attaching a new VIF would exceed either the 10,000 prefix allocation limit or the 30 VIF attachment limit, the attachment request is rejected.

Example 1: You attach 10 VIFs with an IPv4 allocation of 1,000. The sum of all the allocations is 10,000 (10 VIFs x 1,000 IPv4 prefix allocation). The DXGW allows it.

Example 2: You attach 20 VIFs with an IPv4 allocation of 200 prefixes and an IPv6 allocation of 200 prefixes. The sum of allocations is 8,000 (20 VIFs x [200 IPv4 prefixes \+ 200 IPv6 prefixes]). The DXGW allows it.

You can view the current total allocation of all VIFs attached to a DXGW using the console on the gateway details page, or using the `totalPrefixPoolAllocations` value for a DXGW by using the `DescribeDirectConnectGateways` CLI/API call.

**Note**  
AWS Interconnect connections consume 2,000 prefixes from the 10,000 per-DXGW allocation limit. Account for this when planning prefix allocations across VIFs on a DXGW with an AWS Interconnect connection attached.

## Link aggregation groups (LAGs)
<a name="prefix-controls-lags"></a>

For LAGs, the prefix pool scales based on the number of billable member connections. The pool size equals the per-connection pool size multiplied by the number of active member connections. For 1 Gbps and 10 Gbps LAGs, the pool includes resources from up to 4 member connections. For 100 Gbps and 400 Gbps LAGs, the pool includes resources from up to 2 member connections. Unbilled connections are connections that have been created and added to the LAG but whose Layer 1 connectivity has not been completed.

Example: You create a LAG with four 10 Gbps connections. The LAG's pool size is 20,000 prefixes each for IPv4 and IPv6 (4 10 Gbps members x 5,000 prefixes, per address family). You then remove two members from that LAG, reducing the pool to 10,000 prefixes (2 10 Gbps members x 5,000 prefixes, per address family).

### LAG prefix pool guardrail
<a name="lag-prefix-pool-guardrail"></a>

You cannot remove a LAG member if doing so would reduce the LAG's pool size below the current total allocated prefixes across all VIFs on the LAG. To remove the LAG member, first reduce the allocations of the VIFs on that LAG so that the sum of all the allocations is less than the LAG's pool size will be after you remove the member connection.

Example: You have a LAG with three 10 Gbps members. That LAG's pool is 15,000 prefixes per address family (3 10 Gbps members x 5,000, per family). You have 15 VIFs on that LAG with IPv4 allocations of 1,000 each, totaling 15,000 prefixes. Removing a member of the LAG would take its pool down to 10,000 per address family, which is less than the 15,000 prefixes you have allocated on IPv4. The system rejects the removal. You then reduce the IPv4 allocations of the 15 VIFs to 500. The sum of allocations across all VIFs on that LAG is now 7,500 prefixes (15 x 500). The system now allows the removal of the LAG member, because the new pool size (10,000) is greater than the sum of allocations across all VIFs on the LAG (7,500).

## Hosted connections
<a name="prefix-controls-hosted-connections"></a>

Hosted connections support a single VIF, so the connection-level prefix pool is not used. You can set the per-VIF prefix allocation on a hosted connection. The default allocation is 100 for each address family (IPv4 and IPv6), and you can increase it up to 1,000 using the `CreatePrivateVirtualInterface` or `UpdateVirtualInterfaceAttributes` API.

Connection-level prefix pool information (pool size and unallocated count) is not displayed in the console for hosted connections.

## Hosted virtual interfaces
<a name="prefix-controls-hosted-vifs"></a>

The prefix allocation for hosted VIFs is managed by the owner account of the parent connection. A new hosted VIF is always created with the default allocation of 100 prefixes each for IPv4 and IPv6. In the case of dedicated connections, the initial allocation is subtracted from the connection's pool. After the recipient AWS account accepts the hosted VIF, the owner account of the connection can adjust the hosted VIF's prefix allocation.

## Additional resources
<a name="prefix-controls-additional-resources"></a>

For more information, see the following resources:
+ [Managing prefix allocations](#prefix-allocations)
+ [Direct Connect quotas](#limits)
+ [Direct Connect gateways](#direct-connect-gateways-intro)

# Managing prefix allocations for Direct Connect virtual interfaces
<a name="prefix-allocations"></a>

You can manage the number of inbound route prefixes allocated to each virtual interface on your Direct Connect connection. Use the AWS Management Console, AWS CLI, or AWS SDKs to view your connection's prefix pool, allocate prefixes to virtual interfaces, and adjust allocations as your routing needs change.

**Important**  
If the number of advertised prefixes on a virtual interface exceeds the allocated count, the BGP session on that virtual interface goes to an idle state (BGP DOWN). Ensure that your allocation is at least as large as the number of prefixes you plan to advertise.

## Prerequisites
<a name="prefix-allocations-prerequisites"></a>

Before you manage prefix allocations, ensure that you have the following:
+ An active Direct Connect dedicated connection or LAG.
+ At least one private or transit virtual interface.
+ Permissions to call Direct Connect APIs (`directconnect:DescribeConnections`, `directconnect:DescribeVirtualInterfaces`, `directconnect:DescribeDirectConnectGateways`, `directconnect:UpdateVirtualInterfaceAttributes`, `directconnect:CreatePrivateVirtualInterface`, `directconnect:CreateTransitVirtualInterface`).

## View your connection's prefix pool
<a name="prefix-allocations-view-pool"></a>

You can view the prefix pool for your connection to determine how many prefixes are available and how they are allocated across your virtual interfaces.

------
#### [ Console ]

**To view your connection's prefix pool**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select your connection.

1. On the connection details page, locate the **Inbound prefixes** card.

1. Review the following values: **Pool size**, **Unallocated**, and **Allocated**. IPv4 and IPv6 values are shown separately.

------
#### [ Command line ]

Use the [describe-connections](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-connections.html) command.

```
aws directconnect describe-connections \
    --connection-id {{dxcon-abc12345}}
```

In the response, check the following fields:
+ `prefixPoolSizeIpv4` and `prefixPoolSizeIpv6` — The total number of prefixes in the pool.
+ `prefixPoolUnallocatedCountIpv4` and `prefixPoolUnallocatedCountIpv6` — The number of prefixes that are not allocated to a virtual interface.

------

## Set the prefix allocation when creating a virtual interface
<a name="prefix-allocations-create-vif"></a>

You can set the prefix allocation for a virtual interface when you create it. This reserves a portion of the connection's prefix pool for the new virtual interface.

------
#### [ Console ]

**To set the prefix allocation when creating a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Configure the virtual interface settings, including the type, VLAN, and BGP ASN.

1. In the **Inbound prefix allocation** section, enter the number of IPv4 and IPv6 prefixes to allocate.

1. Choose **Create virtual interface**.

------
#### [ Command line ]

Use the [create-private-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-private-virtual-interface.html) command. The following example creates a private virtual interface with prefix allocations.

```
aws directconnect create-private-virtual-interface \
    --connection-id {{dxcon-abc12345}} \
    --new-private-virtual-interface '{
        "virtualInterfaceName": "{{my-private-vif}}",
        "vlan": {{101}},
        "asn": {{65000}},
        "directConnectGatewayId": "{{d2113d06-a0d8-476b-91a7-8555d9973d12}}",
        "prefixPoolAllocatedCountIpv4": {{500}},
        "prefixPoolAllocatedCountIpv6": {{100}}
    }'
```

------

## Update the prefix allocation on an existing virtual interface
<a name="prefix-allocations-update"></a>

You can update the prefix allocation on an existing virtual interface to increase or decrease the number of prefixes reserved for that interface.

------
#### [ Console ]

**To update the prefix allocation on a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface that you want to update.

1. Choose **Edit**.

1. Update the **IPv4 prefix allocation** value, the **IPv6 prefix allocation** value, or both.

1. Choose **Update virtual interface**.

------
#### [ Command line ]

Use the [update-virtual-interface-attributes](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-virtual-interface-attributes.html) command.

```
aws directconnect update-virtual-interface-attributes \
    --virtual-interface-id {{dxvif-abc12345}} \
    --prefix-pool-allocated-count-ipv4 {{500}} \
    --prefix-pool-allocated-count-ipv6 {{100}}
```

------

## View the Direct Connect gateway total prefix allocations
<a name="prefix-allocations-view-dxgw"></a>

You can view the total prefix allocations across all virtual interfaces attached to a Direct Connect gateway.

------
#### [ Console ]

**To view the Direct Connect gateway total prefix allocations**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways**.

1. Select your gateway.

1. On the gateway details page, review the **Total prefix pool allocations** value.

------
#### [ Command line ]

Use the [describe-direct-connect-gateways](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateways.html) command.

```
aws directconnect describe-direct-connect-gateways \
    --direct-connect-gateway-id {{d2113d06-a0d8-476b-91a7-8555d9973d12}}
```

In the response, check the `totalPrefixPoolAllocations` field.

------

## Verify the allocation change
<a name="prefix-allocations-expected-results"></a>

After you update a prefix allocation, the new value takes effect immediately. The BGP session remains up as long as the number of advertised prefixes does not exceed the new allocation. The API rejects requests to reduce an allocation below the number of prefixes currently in use on the VIF.

## Troubleshooting
<a name="prefix-allocations-troubleshooting"></a>

The following are common issues that you might encounter when managing prefix allocations.

BGP session goes down after adding prefixes  
The number of advertised prefixes exceeded the allocated count. Increase the allocation by using the `UpdateVirtualInterfaceAttributes` API or the console.

Cannot decrease allocation  
You cannot reduce a VIF's allocated value below the number of prefixes currently in use. First reduce the number of prefixes advertised by your on-premises device, then reduce the allocation.

Cannot increase allocation  
The connection's prefix pool might be fully allocated. Check the `prefixPoolUnallocatedCountIpv4` and `prefixPoolUnallocatedCountIpv6` values on the connection. You might need to reduce allocations on other virtual interfaces first.

Direct Connect gateway total exceeds 10,000  
The sum of all combined IPv4 and IPv6 allocations across virtual interfaces attached to a single Direct Connect gateway cannot exceed 10,000. Reduce allocations on other virtual interfaces or use a second gateway.

# Direct Connect link aggregation groups (LAGs)
<a name="lags"></a>

You can use multiple connections to increase available bandwidth. A link aggregation group (LAG) is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple connections at a single Direct Connect endpoint, allowing you to treat them as a single, managed connection. LAGs streamline configuration because the LAG configuration applies to all connections in the group. 

**Note**  
Multi-chassis LAG (MLAG) is not supported by AWS.

In the following diagram, you have four connections, with two connections to each location. You can create a LAG for connections that terminate on the same AWS device and in the same location, and then use the two LAGs instead of the four connections for configuration and management.

![Link Aggregation Group](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/LAG_description.png)


You can create a LAG from existing connections, or you can provision new connections. After you've created the LAG, you can associate existing connections (whether standalone or part of another LAG) with the LAG.

The following rules apply:
+ All connections must be dedicated connections and have a port speed of 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps. 
+ All connections in the LAG must use the same bandwidth.
+ You can have a maximum of two 100 Gbps or 400 Gbps connections, or four connections with a port speed less than 100 Gbps in a LAG. Each connection in the LAG counts towards your overall connection limit for the Region. 
+ All connections in the LAG must terminate at the same Direct Connect endpoint. 
+ LAGs are supported for all virtual interface types—public, private, and transit.

When you create a LAG, you can download the Letter of Authorization and Connecting Facility Assignment (LOA-CFA) for a new physical connection individually from the Direct Connect console. For more information, see [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](#create-connection-loa-cfa).

All LAGs have an attribute that determines the minimum number of connections in the LAG that must be operational for the LAG itself to be operational. By default, new LAGs have this attribute set to 0. You can update your LAG to specify a different value—doing so means that your entire LAG becomes non-operational if the number of operational connections falls below this threshold. This attribute can be used to prevent over-utilization of the remaining connections. 

All connections in a LAG operate in Active/Active mode. 

**Note**  
When you create a LAG or associate more connections with the LAG, we may not be able to guarantee enough available ports on a given Direct Connect endpoint. 

**Topics**
+ [MACsec considerations](#lag-macsec-considerations)
+ [Create a LAG](#create-lag)
+ [View LAG details](#view-lag)
+ [Update a LAG](#update-lag)
+ [Associate a connection with a LAG](#associate-connection-with-lag)
+ [Disassociate a connection from a LAG](#disassociate-connection-from-lag)
+ [Associate a MACsec CKN/CAK with a LAG](#associate-key-lag)
+ [Remove the association between a MACsec secret key and a LAG](#disassociate-key-lag)
+ [Delete a LAG](#delete-lag)

## MACsec considerations for Direct Connect
<a name="lag-macsec-considerations"></a>

Take the following into consideration when you want to configure MACsec on LAGs:
+ When you create a LAG from existing connections, we disassociate all of the MACsec keys from the connections. Then we add the connections to the LAG, and associate the LAG MACsec key with the connections.
+ When you associate an existing connection to a LAG, the MACsec keys that are currently associated with the LAG are associated with the connection. Therefore, we disassociate the MACsec keys from the connection, add the connection to the LAG, and then associate the LAG MACsec key with the connection.
+ Only a single MACsec key can be utilized across all LAG links at any time. The ability to support multiple MACsec keys is for key rotation purposes only.

## Create a LAG at a Direct Connect endpoint
<a name="create-lag"></a>

You can create a LAG by provisioning new connections, or aggregating existing connections.

You cannot create a LAG with new connections if this results in you exceeding the overall connections limit for the Region.

To create a LAG from existing connections, the connections must be on the same AWS device (terminate at the same Direct Connect endpoint). They must also use the same bandwidth. You cannot migrate a connection from an existing LAG if removing the connection causes the original LAG to fall below its setting for the minimum number of operational connections.

**Important**  
For existing connections, connectivity to AWS is interrupted during the creation of the LAG.

**To create a LAG with new connections**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Choose **Create LAG**.

1. Under** Lag creation type**, choose **Request new connections**, and provide the following information:
   + **LAG name**: A name for the LAG.
   + **Location**: The location for the LAG.
   + **Port speed**: The port speed for the connections.
   + **Number of new connections**: The number of new connections to create. You can have a maximum of four connections when the port speed is 1G or 10G, or two when the port speed is 100 Gbps or 400 Gbps.
   + (Optional) Configure MAC security (MACsec) for the connection. Under **Additional Settings**, select **Request a MACsec capable port**.

     MACsec is only available on dedicated connections.
   + (Optional) Add or remove a tag.

     [Add a tag] Choose **Add tag** and do the following:
     + For **Key**, enter the key name.
     + For **Value**, enter the key value.

     [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create LAG**.

**To create a LAG from existing connections**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Choose **Create LAG**.

1. Under** Lag creation type**, choose **Use existing connections**, and provide the following information:
   + **LAG name**: A name for the LAG.
   + **Existing connections**: The Direct Connect connection to use for the LAG.
   + (Optional) **Number of new connections**: The number of new connections to create. You can have a maximum of four connections when the port speed is 1G or 10G, or two when the port speed 100 Gbps or 400 Gbps.

1. (Optional) Add or remove a tag.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create LAG**.

**To create a LAG using the command line or API**
+ [create-lag](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-lag.html) (AWS CLI)
+ [CreateLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateLag.html) (Direct Connect API)

**To describe your LAGs using the command line or API**
+ [describe-lags](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-lags.html) (AWS CLI)
+ [DescribeLags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLags.html) (Direct Connect API)

**To download the LOA-CFA using the command line or API**
+ [describe-loa](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-loa.html) (AWS CLI)
+ [DescribeLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLoa.html) (Direct Connect API)

After you create a LAG, you can associate or disassociate connections from it. For more information, see [Associate a connection with a LAG](#associate-connection-with-lag) and [Disassociate a connection from a LAG](#disassociate-connection-from-lag).

## View LAG details at a Direct Connect endpoint
<a name="view-lag"></a>

After you create a LAG, you can view its details using either the Direct Connect console or using the command line or API.

**To view information about your LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG and choose **View details**.

1. You can view information about the LAG, including its ID, and the Direct Connect endpoint on which the connections terminate.

**To view information about your LAG using the command line or API**
+ [describe-lags](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-lags.html) (AWS CLI)
+ [DescribeLags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLags.html) (Direct Connect API)

## Update a LAG at a Direct Connect endpoint
<a name="update-lag"></a>

You can update the following link aggregation group (LAG) attributes using either the Direct Connect console or using the command line or API:
+ The name of the LAG.
+ The value for the minimum number of connections that must be operational for the LAG itself to be operational. 
+ The LAG's MACsec encryption mode.

  MACsec is only available on dedicated connections.

  AWS assigns this value to each connection that is part of the LAG.

  The valid values are:
  + `should_encrypt`
  + `must_encrypt`

    When you set the encryption mode to this value, the connections go down when the encryption is down.
  + `no_encrypt`
+ The tags.

**Note**  
If you adjust the threshold value for the minimum number of operational connections, ensure that the new value does not cause the LAG to fall below the threshold and become non-operational.

**To update a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG, and then choose **Edit**.

1. Modify the LAG

   [Change the name] For **LAG Name**, enter a new LAG name.

   [Adjust the minimum number of connections] For **Minimum Links**, enter minimum number of operational connections.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Edit LAG**.

**To update a LAG using the command line or API**
+ [update-lag](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-lag.html) (AWS CLI)
+ [UpdateLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateLag.html) (Direct Connect API)

## Associate a connection with a LAG at a Direct Connect endpoint
<a name="associate-connection-with-lag"></a>

You can associate an existing connection with a LAG using either the Direct Connect console or using the command line or API. The connection can be standalone, or it can be part of another LAG. The connection must be on the same AWS device and must use the same bandwidth as the LAG. If the connection is already associated with another LAG, you cannot re-associate it if removing the connection causes the original LAG to fall below its threshold for the minimum number of operational connections.

Associating a connection to a LAG automatically re-associates its virtual interfaces to the LAG.

**Important**  
Connectivity to AWS over the connection is interrupted during association.

**To associate a connection with a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG, and then choose **View details**.

1. Under **Connections**, choose **Associate connection**.

1. For **Connection**, choose the Direct Connect connection to use for the LAG.

1. Choose **Associate Connection**.

**To associate a connection using the command line or API**
+ [associate-connection-with-lag](https://docs.aws.amazon.com/cli/latest/reference/directconnect/associate-connection-with-lag.html) (AWS CLI)
+ [AssociateConnectionWithLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateConnectionWithLag.html) (Direct Connect API)

## Disassociate a connection from a LAG at a Direct Connect endpoint
<a name="disassociate-connection-from-lag"></a>

Convert a connection to standalone by disassociating it from a LAG using either the Direct Connect console or using the command line or API. You can't disassociate a connection if it causes the LAG to fall below its threshold for the minimum number of operational connections.

Disassociating a connection from a LAG does not automatically disassociate any virtual interfaces.

**Important**  
Your connection to AWS is broken off during disassociation.

**To disassociate a connection from a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **LAGs**.

1. Select the LAG, and then choose **View details**.

1. Under **Connections**, select the connection from the list of available connections and choose **Disassociate**.

1. In the confirmation dialog box, choose **Disassociate**.

**To disassociate a connection using the command line or API**
+ [disassociate-connection-from-lag](https://docs.aws.amazon.com/cli/latest/reference/directconnect/disassociate-connection-from-lag.html) (AWS CLI)
+ [DisassociateConnectionFromLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DisassociateConnectionFromLag.html) (Direct Connect API)

## Associate a MACsec CKN/CAK with a Direct Connect endpoint LAG
<a name="associate-key-lag"></a>

After you create the LAG that supports MACsec, you can associate a CKN/CAK with the connection using either the Direct Connect console or using the command line or API.

**Note**  
You cannot modify a MACsec secret key after you associate it with a LAG. If you need to modify the key, disassociate the key from the connection, and then associate a new key with the connection. For information about removing an association, see [Remove the association between a MACsec secret key and a Direct Connect endpoint LAG](#disassociate-key-lag).

**To associate a MACsec key with a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG and choose **View details**.

1. Choose **Associate key**.

1. Enter the MACsec key.

   [Use the CAK/CKN pair] Choose **Key Pair**, and then do the following:
   + For **Connectivity Association Key (CAK)**, enter the CAK.
   + For **Connectivity Association Key Name (CKN)**, enter the CKN.

   [Use the secret] Choose **Existing Secret Manager secret**, and then for **Secret**, select the MACsec secret key.

1. Choose **Associate key**.

**To associate a MACsec key with a LAG using the command line or API**
+ [associate-mac-sec-key](https://docs.aws.amazon.com/cli/latest/reference/directconnect/associate-mac-sec-key.html) (AWS CLI)
+ [AssociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateMacSecKey.html) (Direct Connect API)

## Remove the association between a MACsec secret key and a Direct Connect endpoint LAG
<a name="disassociate-key-lag"></a>

You can remove the association between the LAG and the MACsec key using either the Direct Connect console or using the command line or API.

**To remove an association between a LAG and a MACsec key**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG and choose **View details**.

1. Select the MACsec secret to remove, and then choose **Disassociate key**.

1. In the confirmation dialog box, enter **disassociate**, and then choose **Disassociate**.

**To remove an association between a LAG and a MACsec key using the command line or API**
+ [disassociate-mac-sec-key](https://docs.aws.amazon.com/cli/latest/reference/directconnect/disassociate-mac-sec-key.html) (AWS CLI)
+ [DisassociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API__DisassociateMacSecKey.html) (Direct Connect API)

## Delete a Direct Connect endpoint LAG
<a name="delete-lag"></a>

If you no longer need LAGs, you can delete them. You cannot delete a LAG if it has virtual interfaces associated with it. You must first delete the virtual interfaces, or associate them with a different LAG or connection. Deleting a LAG does not delete the connections in the LAG; you must delete the connections yourself. For more information, see [Delete a connection](#deleteconnection).

You can delete a LAG using either the Direct Connect console or using the command line or API.

**To delete a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAGs, and then choose **Delete**.

1. In the confirmation dialog box, choose **Delete**.

**To delete a LAG using the command line or API**
+ [delete-lag](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-lag.html) (AWS CLI)
+ [DeleteLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteLag.html) (Direct Connect API)

# Direct Connect gateways
<a name="direct-connect-gateways"></a>

You can work with Direct Connect gateways using the Amazon VPC console or the AWS CLI.
+ [Direct Connect gateways](#direct-connect-gateways-intro)

  Using a Direct Connect gateway, you can associate the Direct Connect gateway with a transit gateway with multiple VPCs, a virtual private gateway, or if you use AWS Cloud WAN, to a Cloud WAN core network.
+ [Virtual private gateway associations](#virtualgateways)

  Using a virtual private gateway, you can associate the Direct Connect gateway over a private virtual interface to one or more VPCs in any account located in the same or different Regions.
+ [Transit Gateway associations](#direct-connect-transit-gateways)

  Use a Direct Connect gateway to connect your Direct Connect connection over a transit virtual interface to the VPCs or VPNs that are attached to your Transit Gateway.
+ [Cloud WAN core network associations](#direct-connect-cloud-wan)

  Use a Direct Connect gateway to associate a Direct Connect gateway with an AWS Network Manager core network. 
+ [Allowed prefixes interactions](#allowed-to-prefixes)

  Use allowed prefixes to interact with Transit Gateways and virtual private gateways.

**Topics**
+ [Direct Connect gateways](#direct-connect-gateways-intro)
+ [Virtual private gateway associations](#virtualgateways)
+ [Transit Gateway associations](#direct-connect-transit-gateways)
+ [Cloud WAN core network associations](#direct-connect-cloud-wan)
+ [Allowed prefixes interactions](#allowed-to-prefixes)

## Direct Connect gateways
<a name="direct-connect-gateways-intro"></a>

Use Direct Connect gateway to connect your VPCs. You associate a Direct Connect gateway with any of the following: 
+ A Transit Gateway when you have multiple VPCs in the same Region
+ A virtual private gateway
+ An AWS Cloud WAN core network

You can also use a virtual private gateway to extend your Local Zone. This configuration allows the VPC associated with the Local Zone to connect to a Direct Connect gateway. The Direct Connect gateway connects to a Direct Connect location in a Region. The on-premises data center has a Direct Connect connection to the Direct Connect location. For more information, see [Accessing Local Zones using a Direct Connect gateway](https://docs.aws.amazon.com/vpc/latest/userguide/Extend_VPCs.html#access-local-zone) in the *Amazon VPC User Guide*.

A Direct Connect gateway is a globally available resource. You can connect to any Region globally using a Direct Connect gateway. This includes AWS GovCloud (US), but it does not include the AWS China Regions. A Direct Connect gateway is a virtual component of Direct Connect designed to act as a distributed set of BGP route reflectors. Because it operates outside the data traffic path, it avoids creating a single point of failure or introducing dependencies on specific AWS Regions. High availability is inherently built into its design, eliminating the need for multiple Direct Connect gateways.

Customers using Direct Connect with VPCs that currently bypass a parent Availability Zone will not be able to migrate their Direct Connect connections or virtual interfaces.

The following describe scenarios where you can use a Direct Connect gateway.

A Direct Connect gateway does not allow gateway associations that are on the same Direct Connect gateway to send traffic to each other (for example, a virtual private gateway to another virtual private gateway). An exception to this rule, implemented in November 2021, is when a supernet is advertised across two or more VPCs, which have their attached virtual private gateways (VGWs) associated to the same Direct Connect gateway and on the same virtual interface. In this case, VPCs can communicate with each other via the Direct Connect endpoint. For example, if you advertise a supernet (for example, 10.0.0.0/8 or 0.0.0.0/0) that overlaps with the VPCs attached to a Direct Connect gateway (for example, 10.0.0.0/24 and 10.0.1.0/24), and on the same virtual interface, then from your on-premises network, the VPCs can communicate with each other. 

If you want to block VPC-to-VPC communication within a Direct Connect gateway, do the following: 

1. Set up security groups on the instances and other resources in the VPC to block traffic between VPCs, also using this as part of the default security group in the VPC.

1. Avoid advertising a supernet from your on- premises network that overlaps with your VPCs. Instead you can advertise more specific routes from your on-premises network that do not overlap with your VPCs.

1. Provision a single Direct Connect Gateway for each VPC that you want to connect to your on-premises network instead of using the same Direct Connect Gateway for multiple VPCs. For example, instead of using a single Direct Connect Gateway for your development and production VPCs, use separate Direct Connect Gateways for each of these VPCs.

A Direct Connect gateway does not prevent traffic from being sent from one gateway association back to the gateway association itself (for example when you have an on-premises supernet route that contains the prefixes from the gateway association). If you have a configuration with multiple VPCs connected to Transit Gateways associated to same Direct Connect gateway, the VPCs could communicate. To prevent the VPCs from communicating, associate a route table with the VPC attachments that have the **blackhole** option set.

**Topics**
+ [Scenarios](#dx-gateway-scenarios)
+ [Create a Direct Connect gateway](#create-direct-connect-gateway)
+ [Migrate from a virtual private gateway to a Direct Connect gateway](#migrate-to-direct-connect-gateway)
+ [Delete a Direct Connect gateway](#delete-direct-connect-gateway)

### Scenarios
<a name="dx-gateway-scenarios"></a>

The following describe just a few scenarios for using Direct Connect gateways. 

#### Scenario: Virtual private gateway associations
<a name="virtual-private-gateway"></a>

In the following diagram, the Direct Connect gateway enables you to use your Direct Connect connection in the US East (N. Virginia) Region to access VPCs in your account in both the US East (N. Virginia) and US West (N. California) Regions.

Each VPC has a virtual private gateway that connects to the Direct Connect gateway using a virtual private gateway association. The Direct Connect gateway uses a private virtual interface for the connection to the Direct Connect location. There is an Direct Connect connection from the location to the customer data center.

![A Direct Connect gateway that connects VPCs in two AWS Regions and your data center.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dx-gateway.png)


#### Scenario: Virtual private gateway associations across accounts
<a name="virtual-private-gateway-across-accounts"></a>

Consider this scenario of a Direct Connect gateway owner (Account Z) who owns the Direct Connect gateway. Account A and Account B want to use the Direct Connect gateway. Account A and Account B each send an association proposal to Account Z. Account Z accepts the association proposals and can optionally update the prefixes that are allowed from Account A's virtual private gateway or Account B's virtual private gateway. After Account Z accepts the proposals, Account A and Account B can route traffic from their virtual private gateway to the Direct Connect gateway. Account Z also owns the routing to the customers because Account Z owns the gateway.

![A Direct Connect gateway that connects three AWS accounts and your data center.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dx-gateway-shared.png)


#### Scenario: Transit Gateway associations
<a name="transit-gateway"></a>

The following diagram illustrates how the Direct Connect gateway enables you to create a single connection to your Direct Connect connection that all of your VPCs can use.

![A Direct Connect gateway associated with a Transit Gateway with multiple VPC attachments.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/direct-connect-tgw.png)


The solution involves the following components:
+ A Transit Gateway that has VPC attachments.
+ A Direct Connect gateway.
+ An association between the Direct Connect gateway and the Transit Gateway.
+ A transit virtual interface that is attached to the Direct Connect gateway.

This configuration offers the following benefits. You can:
+ Manage a single connection for multiple VPCs or VPNs that are in the same Region.
+ Advertise prefixes from on-premises to AWS and from AWS to on-premises.

For information about configuring Transit Gateways, see [Working with Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html) in the *Amazon VPC Transit Gateways Guide*.

#### Scenario: Transit Gateway associations across accounts
<a name="transit-gateway-across-accounts"></a>

Consider this scenario of a Direct Connect gateway owner (Account Z) who owns the Direct Connect gateway. Account A owns the Transit Gateway and wants to use the Direct Connect gateway. Account Z accepts the association proposals and can optionally update the prefixes that are allowed from Account A's Transit Gateway. After Account Z accepts the proposals, the VPCs attached to the Transit Gateway can route traffic from the Transit Gateway to the Direct Connect gateway. Account Z also owns the routing to the customers because Account Z owns the gateway.

![A Direct Connect gateway from an AWS account associated with a Transit Gateway from another AWS account.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/direct-connect-ma-tgw.png)


### Create a Direct Connect gateway
<a name="create-direct-connect-gateway"></a>

You can create a Direct Connect gateway in any supported Region using either the Direct Connect console or using the command line or API.

**To create a Direct Connect gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways**.

1. Choose **Create Direct Connect gateway**.

1. Specify the following information, and choose **Create Direct Connect gateway**.
   + **Name**: Enter a name to help you identify the Direct Connect gateway.
   + **Amazon side ASN**: Specify the ASN for the Amazon side of the BGP session. The ASN must be in the 64,512 to 65,534 range or 4,200,000,000 to 4,294,967,294 range.
**Note**  
If you want to create a Direct Connect gateway to use with an AWS Cloud WAN core network. The ASN must not be in the same range as the ASN of the core network.

**To create a Direct Connect gateway using the command line or API**
+ [create-direct-connect-gateway](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway.html) (AWS CLI)
+ [CreateDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGateway.html) (Direct Connect API)

### Migrate from a virtual private gateway to a Direct Connect gateway
<a name="migrate-to-direct-connect-gateway"></a>

You can migrate a virtual private gateway attached to a virtual interface to a Direct Connect gateway. 

If you're using Direct Connect with VPCs that currently bypass a parent Availability Zone you won't be able to migrate your Direct Connect connections or virtual interfaces.

The following steps describe the steps you need to take to migrate a virtual private gateway to a Direct Connect gateway.

**To migrate to a Direct Connect gateway**

1. Create a Direct Connect gateway. 

   If the Direct Connect gateway does not yet exist, you'll need to create it. For the steps to create a Direct Connect gateway, see [Create a Direct Connect gateway](#create-direct-connect-gateway).

1. Create a virtual interface for the Direct Connect gateway. 

   A virtual interface is required for migration. If the interface does not exist, you'll need to create it. For the steps to create the virtual interface, see [Virtual interfaces](#create-vif).

1. Associate the virtual private gateway with the Direct Connect gateway. 

   Both the Direct Connect gateway and a virtual private gateway need to be associated. For the steps to create the association, see [Associate or disassociate virtual private gateways](#associate-vgw-with-direct-connect-gateway).

1. Delete the virtual interface that was associated with the virtual private gateway. For more information, see [Delete a virtual interface](#deletevif).

### Delete a Direct Connect gateway
<a name="delete-direct-connect-gateway"></a>

If you no longer require a Direct Connect gateway, you can delete it. You must first disassociate all associated virtual private gateways and delete the attached private virtual interface. Once you've disassociated any associated virtual private gateways and deleted any attached private virtual interfaces, you can delete the Direct Connect gateway using either the Direct Connect console or using the command line or API. 
+ For the steps to disassociate a virutal private gateway, see [Associate or disassociate virtual private gateways](#associate-vgw-with-direct-connect-gateway).
+ For the steps to delete a virtual interface, see [Delete a virtual interface](#deletevif).

**To delete a Direct Connect gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways**.

1. Select the gateways and choose **Delete**.

**To delete a Direct Connect gateway using the command line or API**
+ [delete-direct-connect-gateway](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway.html) (AWS CLI)
+ [DeleteDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGateway.html) (Direct Connect API)

## Direct Connect virtual private gateway associations
<a name="virtualgateways"></a>

You can associate a virtual private gateway with a Direct Connect gateway to enable connectivity between your Direct Connect connection and VPCs across different accounts and Regions. Each VPC requires a virtual private gateway that you associate with the Direct Connect gateway. Once these associations are established, you create private virtual interfaces on your Direct Connect connection to the Direct Connect gateway, allowing multiple VPCs to share the same Direct Connect connection through their respective virtual private gateway associations..

The following rules apply to virtual private gateway associations:
+ Do not enable route propagation until after you've associated a virtual gateway with a Direct Connect gateway. If you enable route propagation before associating the gateways, routes might be propagated incorrectly.
+ There are limits for creating and using Direct Connect gateways. For more information, see [Direct Connect quotas](#limits).
+  You cannot attach a Direct Connect gateway to a virtual private gateway when the Direct Connect gateway is already associated with a Transit Gateway.
+ The VPCs to which you connect through a Direct Connect gateway cannot have overlapping CIDR blocks. If you add an IPv4 CIDR block to a VPC that's associated with a Direct Connect gateway, ensure that the CIDR block does not overlap with an existing CIDR block for any other associated VPC. For more information, see [Adding IPv4 CIDR Blocks to a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-resize) in the *Amazon VPC User Guide*.
+ You cannot create a public virtual interface to a Direct Connect gateway.
+ A Direct Connect gateway supports communication between attached private virtual interfaces and associated virtual private gateways only, and may enable a virtual private gateway to another private gateway. The following traffic flows are not supported:
  + Direct communication between the VPCs that are associated with a single Direct Connect gateway. This includes traffic from one VPC to another by using a hairpin through an on-premises network through a single Direct Connect gateway.
  + Direct communication between the virtual interfaces that are attached to a single Direct Connect gateway. 
  + Direct communication between the virtual interfaces that are attached to a single Direct Connect gateway and a VPN connection on a virtual private gateway that's associated with the same Direct Connect gateway.
+ You cannot associate a virtual private gateway with more than one Direct Connect gateway and you cannot attach a private virtual interface to more than one Direct Connect gateway.
+ A virtual private gateway that you associate with a Direct Connect gateway must be attached to a VPC.
+ A virtual private gateway association proposal expires 7 days after it is created.
+ An accepted virtual private gateway proposal, or a deleted virtual private gateway proposal remains visible for 3 days.
+ A virtual private gateway can be associated with a Direct Connect gateway and also attached to a virtual interface.
+ Detaching a virtual private gateway from a VPC also disassociates the virtual private gateway from a Direct Connect gateway.
+ If you are planning to use the virtual private gateway for a Direct Connect gateway and a dynamic VPN connection, set the ASN on the virtual private gateway to the value that you require for the VPN connection. Otherwise, the ASN on the virtual private gateway can be set to any permitted value. The Direct Connect gateway advertises all connected VPCs over the ASN assigned to it.
**Note**  
When you associate a Direct Connect gateway with a virtual private gateway, the virtual private gateway ASN is not visible in the AS\_PATH advertised to your on-premises router; only the Direct Connect gateway ASN appears. The virtual private gateway ASN is advertised on-premises only when a private virtual interface attaches directly to the virtual private gateway, without a Direct Connect gateway.

To connect your Direct Connect connection to a VPC in the same Region only, you can create a Direct Connect gateway. Or, you can create a private virtual interface and attach it to the virtual private gateway for the VPC. For more information, see [Create a private virtual interface](#create-private-vif) and [VPN CloudHub](https://docs.aws.amazon.com/vpc/latest/userguide/VPN_CloudHub.html).

To use your Direct Connect connection with a VPC in another account, you can create a hosted private virtual interface for that account. When the owner of the other account accepts the hosted virtual interface, they can choose to attach it either to a virtual private gateway or to a Direct Connect gateway in their account. For more information, see [Virtual interfaces and hosted virtual interfaces](#WorkingWithVirtualInterfaces).

**Topics**
+ [Create a virtual private gateway](#create-virtual-private-gateway)
+ [Associate or disassociate virtual private gateways](#associate-vgw-with-direct-connect-gateway)
+ [Create a private virtual interface to the Direct Connect gateway](#create-private-vif-for-gateway)
+ [Associate a virtual private gateway across accounts](#multi-account-associate-vgw)

### Create a Direct Connect virtual private gateway
<a name="create-virtual-private-gateway"></a>

The virtual private gateway must be attached to the VPC to which you want to connect. You can create a virtual private gateway and attach it to a VPC using either the Direct Connect console or using the command line or API.

**Note**  
If you are planning to use the virtual private gateway for a Direct Connect gateway and a dynamic VPN connection, set the ASN on the virtual private gateway to the value that you require for the VPN connection. Otherwise, the ASN on the virtual private gateway can be set to any permitted value. The Direct Connect gateway advertises all connected VPCs over the ASN assigned to it.

After you create a virtual private gateway, you must attach it to your VPC.

**To create a virtual private gateway and attach it to your VPC**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Private Gateways**, and then choose **Create Virtual Private Gateway**.

1. (Optional) Enter a name for your virtual private gateway. Doing so creates a tag with a key of `Name` and the value that you specify.

1. For **ASN**, leave the default selection to use the default Amazon ASN. Otherwise, choose **Custom ASN** and enter a value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 4200000000 to 4294967294 range. 

1. Choose **Create Virtual Private Gateway**.

1. Select the virtual private gateway that you created, and then choose **Actions**, **Attach to VPC**.

1. Select your VPC from the list and choose **Yes, Attach**.

**To create a virtual private gateway using the command line or API**
+ [CreateVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateVpnGateway.html) (Amazon EC2 Query API)
+ [create-vpn-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpn-gateway.html) (AWS CLI)
+ [New-EC2VpnGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpnGateway.html) (AWS Tools for Windows PowerShell)

**To attach a virtual private gateway to a VPC using the command line or API**
+ [AttachVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-AttachVpnGateway.html) (Amazon EC2 Query API)
+ [attach-vpn-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-vpn-gateway.html) (AWS CLI)
+ [Add-EC2VpnGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2VpnGateway.html) (AWS Tools for Windows PowerShell)

### Associate or disassociate Direct Connect virtual private gateways
<a name="associate-vgw-with-direct-connect-gateway"></a>

You can associate or disassociate a virtual private gateway and Direct Connect gateway using either the Direct Connect console or using the command line or API. The account owner of the virtual private gateway performs these operations.

**To associate a virtual private gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways** and then choose the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations**, and then choose **Associate gateway**.

1. For **Gateways**, choose the virtual private gateways to associate, and then choose **Associate gateway**.

You can view all of the virtual private gateways that are associated with the Direct Connect gateway by choosing **Gateway associations**. 

**To disassociate a virtual private gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways** and then select the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations** and then select the virtual private gateway.

1. Choose **Disassociate**.

**To associate a virtual private gateway using the command line or API**
+ [create-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway-association.html) (AWS CLI)
+ [CreateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociation.html) (Direct Connect API)

**To view the virtual private gateways associated with a Direct Connect gateway using the command line or API**
+ [describe-direct-connect-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.html) (AWS CLI)
+ [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html) (Direct Connect API)

**To disassociate a virtual private gateway using the command line or API**
+ [delete-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociation.html) (Direct Connect API)

### Create a private virtual interface to the Direct Connect gateway
<a name="create-private-vif-for-gateway"></a>

To connect your Direct Connect connection to the remote VPC, you must create a private virtual interface for your connection. Specify the Direct Connect gateway to which to connect. You can create a private virtual interface using either the Direct Connect console or using the command line or API.

**Note**  
If you're accepting a hosted private virtual interface, you can associate it with a Direct Connect gateway in your account. For more information, see [Accept a hosted virtual interface](#accepthostedvirtualinterface).

**To provision a private virtual interface to a Direct Connect gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, choose **Private**.

1. Under **Private virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Virtual interface owner**, choose **My AWS account** if the virtual interface is for your AWS account.

   1.  For **Direct Connect gateway**, select the Direct Connect gateway.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.   
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 9001 (jumbo frames), select **Jumbo MTU (MTU size 9001)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

After you've created the virtual interface, you can download the router configuration for your device. For more information, see [Download the router configuration file](#vif-router-config).

**To create a private virtual interface using the command line or API**
+ [create-private-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-private-virtual-interface.html) (AWS CLI)
+ [CreatePrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePrivateVirtualInterface.html) (Direct Connect API)

**To view the virtual interfaces that are attached to a Direct Connect gateway using the command line or API**
+ [describe-direct-connect-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-attachments.html) (AWS CLI)
+ [DescribeDirectConnectGatewayAttachments](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.html) (Direct Connect API)

### Associate a Direct Connect virtual private gateway across accounts
<a name="multi-account-associate-vgw"></a>

You can associate a Direct Connect gateway with a virtual private gateway that is owned by any AWS account. The Direct Connect gateway can be an existing gateway, or you can create a new gateway. The owner of the virtual private gateway creates an *association proposal* and the owner of the Direct Connect gateway must accept the association proposal.

An association proposal can contain prefixes that will be allowed from the virtual private gateway. The owner of the Direct Connect gateway can optionally override any requested prefixes in the association proposal.

#### Allowed prefixes
<a name="allowed-prefixes"></a>

When you associate a virtual private gateway with a Direct Connect gateway, you specify a list of Amazon VPC prefixes to advertise to the Direct Connect gateway. The prefix list acts as a filter that allows the same CIDRs, or smaller CIDRs to be advertised to the Direct Connect gateway. You must set the **Allowed prefixes** to a range that is the same or wider than the VPC CIDR because we provision entire VPC CIDR on the virtual private gateway. 

Consider the case where the VPC CIDR is 10.0.0.0/16. You can set the **Allowed prefixes** to 10.0.0.0/16 (the VPC CIDR value), or 10.0.0.0/15 ( a value that is wider than the VPC CIDR). 

Any virtual interface inside network prefixes advertised over Direct Connect are only propagated to Transit Gateways across Regions, not within the same Region. For more information on how allowed prefixes interact with virtual private gateways and Transit Gateways, see [Allowed prefixes interactions](#allowed-to-prefixes).

## Direct Connect gateways and Transit Gateway associations
<a name="direct-connect-transit-gateways"></a>

You can use Direct Connect gateway to connect your Direct Connect connection over a transit virtual interface to the VPCs or VPNs that are attached to your Transit Gateway. You associate a Direct Connect gateway with the Transit Gateway. Then, create a transit virtual interface for your Direct Connect connection to the Direct Connect gateway. 

The following rules apply to Transit Gateway associations:
+ You cannot attach a Direct Connect gateway to a Transit Gateway when the Direct Connect gateway is already associated with a virtual private gateway or is attached to a private virtual interface.
+ There are limits for creating and using Direct Connect gateways. For more information, see [Direct Connect quotas](#limits).
+ A Direct Connect gateway supports communication between attached transit virtual interfaces and associated Transit Gateways.
+ If you connect to multiple Transit Gateways that are in different Regions, use unique ASNs for each Transit Gateway.
+ Any point-to-point connectivity address using a `/30` range — for example, `192.168.0.0/30` — does not propagate to a Transit Gateway.

### Associating a Transit Gateway across accounts
<a name="multi-account-associate-tgw"></a>

You can associate an existing Direct Connect gateway or a new Direct Connect gateway with a Transit Gateway that is owned by any AWS account. The owner of the Transit Gateway creates an *association proposal* and the owner of the Direct Connect gateway must accept the association proposal.

An association proposal can contain prefixes that will be allowed from the Transit Gateway. The owner of the Direct Connect gateway can optionally override any requested prefixes in the association proposal.

#### Allowed prefixes
<a name="allowed-prefixes-transit-gateway"></a>

For a Transit Gateway association, you provision the allowed prefixes list on the Direct Connect gateway. The list is used to route traffic from on-premises to AWS into the Transit Gateway even if the VPCs attached to the Transit Gateway do not have assigned CIDRs. Prefixes in the Direct Connect gateway allowed prefix list originate on the Direct Connect gateway and are advertised to the on-premises network. For more information on how allowed prefixes interact with Transit Gateway and virtual private gateways, see [Allowed prefixes interactions](#allowed-to-prefixes).

**Topics**
+ [Associating a Transit Gateway across accounts](#multi-account-associate-tgw)
+ [Associate or disassociate a Transit Gateway with Direct Connect.](#associate-tgw-with-direct-connect-gateway)
+ [Create a transit virtual interface to the Direct Connect gateway](#create-transit-vif-for-gateway)
+ [Create a Transit Gateway association proposal](#multi-account-tgw-create-proposal)
+ [Accept or reject a Transit Gateway association proposal](#multi-account-tgw-accept-reject-proposal)
+ [Update the allowed prefixes for a Transit Gateway association](#multi-account-tgw-update-proposal-routes)
+ [Delete a Transit Gateway association proposal](#multi-account-tgw-delete-proposal)

### Associate or disassociate Direct Connect with a Transit Gateway
<a name="associate-tgw-with-direct-connect-gateway"></a>

Associate or disassociate a Transit Gateway using either the Direct Connect console or using the command line or API.

**To associate a Transit Gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways** and then select the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations** and then choose **Associate gateway**.

1. For **Gateways**, choose the Transit Gateway to associate.

1. In **Allowed prefixes**, enter the prefixes (separated by a comma, or on a new line) which the Direct Connect gateway advertises to the on-premises data center. For more information on allowed prefixes, see [Allowed prefixes interactions](#allowed-to-prefixes).

1. Choose **Associate gateway**

You can view all of the gateways that are associated with the Direct Connect gateway by choosing **Gateway associations**. 

**To disassociate a Transit Gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways** and then select the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations** and then select the Transit Gateway.

1. Choose **Disassociate**.

**To update allowed prefixes for a Transit Gateway**

You can add or remove allowed prefixes to the Transit Gateway.

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways** and then choose the Direct Connect gateway you want to add or remove allowed prefixes for.

1. Choose the **Gateway associations** tab.

1. Choose the gateway you want to modify allowed prefixes for, and then choose **Edit**.

1. In **Allowed prefixes**, enter the prefixes which the Direct Connect gateway advertises to the on-premises data center. For multiple prefixes, separate each prefix by a comma or put each prefix on a new line. The prefixes you add should match the Amazon VPC CIDRs for all virtual private gateways. For more information on allowed prefixes, see [Allowed prefixes interactions](#allowed-to-prefixes).

1. Choose **Edit association**. 

   In the **Gateway association** section the **State** displays **updating**. When complete, the **State** changes to **associated**. This might take several minutes or longer to complete.

**To associate a Transit Gateway using the command line or API**
+ [create-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway-association.html) (AWS CLI)
+ [CreateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociation.html) (Direct Connect API)

**To view the Transit Gateways associated with a Direct Connect gateway using the command line or API**
+ [describe-direct-connect-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.html) (AWS CLI)
+ [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html) (Direct Connect API)

**To disassociate a Transit Gateway using the command line or API**
+ [delete-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociation.html) (Direct Connect API)

**To update allowed prefixes for a Transit Gateway using the command line or API**
+ [update-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-direct-connect-gateway-association.html) (AWS CLI)
+ [UpdateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGatewayAssociation.html) (Direct Connect API)

### Create a transit virtual interface to the Direct Connect gateway
<a name="create-transit-vif-for-gateway"></a>

To connect your Direct Connect connection to the Transit Gateway, you must create a transit interface for your connection. Specify the Direct Connect gateway to which to connect. You can use either the Direct Connect console or use the command line or API.

**Important**  
If you associate your Transit Gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the Transit Gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both the Transit Gateway and the Direct Connect gateway, the association request fails.

Although the Transit Gateway and Direct Connect gateway must use different ASNs, the Transit Gateway ASN is not included in the AS\_PATH that is advertised to your on-premises router. The Direct Connect gateway replaces the AS\_PATH with its own ASN.

**To provision a transit virtual interface to a Direct Connect gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Under **Virtual interface type**, for **Type**, choose **Transit**.

1. Under **Transit virtual interface settings**, do the following:

   1. For **Virtual interface name**, enter a name for the virtual interface.

   1. For **Connection**, choose the Direct Connect connection that you want to use for this interface.

   1. For **Virtual interface owner**, choose **My AWS account** if the virtual interface is for your AWS account.

   1.  For **Direct Connect gateway**, select the Direct Connect gateway.

   1. For **VLAN**, enter the ID number for your virtual local area network (VLAN). 

   1. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

      The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](#long-asn-support). 

1. Under **Additional Settings**, do the following:

   1. To configure an IPv4 BGP or an IPv6 peer, do the following:

      [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of the following:
      + To specify these IP addresses yourself, for **Your router peer ip**, enter the destination IPv4 CIDR address to which Amazon should send traffic. 
      + For **Amazon router peer ip**, enter the IPv4 CIDR address to use to send traffic to AWS.
**Important**  
When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.  
For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).
For more information about RFC 3927, see [Dynamic Configuration of IPv4 Link-Local Addresses](https://datatracker.ietf.org/doc/html/rfc3927).

      [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses.

   1. To change the maximum transmission unit (MTU) from 1500 (default) to 8500 (jumbo frames), select **Jumbo MTU (MTU size 8500)**.

   1. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence.

   1. (Optional) For **Bandwidth**, select a bandwidth value to apply a Rate Limiter to this virtual interface. The Rate Limiter sets a maximum bandwidth that the VIF can use, helping prevent this VIF from congesting other VIFs on the same connection. This option is only available on Dedicated connections. For more information, see [Virtual interface Rate Limiters](#vif-rate-limiters).

   1. (Optional) Add or remove a tag.

      [Add a tag] Choose **Add tag** and do the following:
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create virtual interface**.

After you've created the virtual interface, you can download the router configuration for your device. For more information, see [Download the router configuration file](#vif-router-config).

**To create a transit virtual interface using the command line or API**
+ [create-transit-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-transit-virtual-interface.html) (AWS CLI)
+ [CreateTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateTransitVirtualInterface.html) (Direct Connect API)

**To view the virtual interfaces that are attached to a Direct Connect gateway using the command line or API**
+ [describe-direct-connect-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-attachments.html) (AWS CLI)
+ [DescribeDirectConnectGatewayAttachments](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.html) (Direct Connect API)

### Create a Transit Gateway and Direct Connect association proposal
<a name="multi-account-tgw-create-proposal"></a>

If you own the Transit Gateway, you must create the association proposal. The owner of the Direct Connect gateway must share the ID of the Direct Connect gateway and the ID of its AWS account. After you create the proposal, the owner of the Direct Connect gateway must accept it in order for you to gain access to the on-premises network over Direct Connect. You can create an association proposal using either the Direct Connect console or using the command line or API.

**To create an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Transit Gateways** and then select the Transit Gateway.

1. Choose **View details**.

1. Choose **Direct Connect gateway associations** and then choose **Associate Direct Connect gateway**.

1. Under **Association account type**, for **Account owner**, choose **Another account**.

1. For **Direct Connect gateway owner**, enter the ID of the account that owns the Direct Connect gateway.

1. Under **Association settings**, do the following:

   1. For **Direct Connect gateway ID**, enter the ID of the Direct Connect gateway.

   1. For **Virtual interface owner**, enter the ID of the account that owns the virtual interface for the association.

   1. (Optional) To specify a list of prefixes to be allowed from the Transit Gateway, add the prefixes to **Allowed prefixes**, separating them using commas, or entering them on separate lines.

1. Choose **Associate Direct Connect gateway**.

**To create an association proposal using the command line or API**
+ [create-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [CreateDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociationProposal.html) (Direct Connect API)

### Accept or reject a Transit Gateway and Direct Connect association proposal
<a name="multi-account-tgw-accept-reject-proposal"></a>

If you own the Direct Connect gateway, you must accept the association proposal in order to create the association. You also have the option of rejecting the association proposal. You can accept or reject the association proposal using either the Direct Connect console or using the command line or API.

**To accept an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways**.

1. Select the Direct Connect gateway with pending proposals and then choose **View details**.

1. On the **Pending proposals** tab, select the proposal and then choose **Accept proposal**.

1. ((Optional) To specify a list of prefixes to be allowed from the Transit Gateway, add the prefixes to **Allowed prefixes**, separating them using commas, or entering them on separate lines.

1. Choose **Accept proposal**.

**To reject an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways**.

1. Select the Direct Connect gateway with pending proposals and then choose **View details**.

1. On the **Pending proposals** tab, select the transit gateway and then choose **Reject proposal**.

1. In the **Reject proposal** dialog box, enter Delete and then choose **Reject proposal**.

**To view association proposals using the command line or API**
+ [describe-direct-connect-gateway-association-proposals](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.htm) (AWS CLI)
+ [DescribeDirectConnectGatewayAssociationProposals](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociationProposals.html) (Direct Connect API)

**To accept an association proposal using the command line or API**
+ [accept-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [AcceptDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AcceptDirectConnectGatewayAssociationProposal.html) (Direct Connect API)

**To reject an association proposal using the command line or API**
+ [delete-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociationProposal.html) (Direct Connect API)

### Update the allowed prefixes for a transit gateway and Direct Connect association
<a name="multi-account-tgw-update-proposal-routes"></a>

You can update the prefixes that are allowed from the Transit Gateway over the Direct Connect gateway using either the Direct Connect console or using the command line or API. To update the allowed prefixes for a Transit Gateway and Direct Connect association using the Direct Connect console, 
+  If you're the owner of the Transit Gateway. you'll need to create a new association proposal for that Direct Connect gateway, specifying the prefixes to allow. For the steps to create a new association proposal, see [Create a Transit Gateway association proposal](#multi-account-tgw-create-proposal).
+  If you're the owner of the Direct Connect gateway you can update the allowed prefixes when you accept the association proposal, or if you update the allowed prefixes for an existing association. For the steps to update the allowed prefixes when you accept the association, see [Accept or reject a Transit Gateway association proposal](#multi-account-tgw-accept-reject-proposal).

**To update the allowed prefixes for an existing association using the command line or API**
+ [update-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-direct-connect-gateway-association.html) (AWS CLI)
+ [UpdateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGatewayAssociation.html) (Direct Connect API)

### Delete a Transit Gateway and Direct Connect association proposal
<a name="multi-account-tgw-delete-proposal"></a>

The owner of the Transit Gateway can delete the Direct Connect gateway association proposal if it is still pending acceptance. After an association proposal is accepted, you can't delete it, but you can disassociate the transit gateway from the Direct Connect gateway. For more information, see [Create a Transit Gateway association proposal](#multi-account-tgw-create-proposal).

You can delete a Transit Gateway and Direct Connect association proposal using either the Direct Connect console or using the command line or API.

**To delete an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Transit Gateways** and then select the Transit Gateway.

1. Choose **View details**.

1. Choose **Pending gateway associations**, select the association and then choose **Delete association**.

1. In the **Delete association proposal** dialog box, enter **Delete** and then choose **Delete**.

**To delete a pending association proposal using the command line or API**
+ [delete-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociationProposal.html) (Direct Connect API)

## Direct Connect gateway and AWS Cloud WAN core network associations
<a name="direct-connect-cloud-wan"></a>

Associate a Direct Connect gateway to an AWS Cloud WAN core network using a Direct Connect attachment type in Cloud WAN. This direct association routes traffic between your core network’s selected edge locations and your Direct Connect connections using the shortest available path

The Direct Connect gateway attachment type supports BGP (Border Gateway protocol) for automatic propagation of routing information between your core network and on-premises locations. The Direct Connect attachment also supports the standard Cloud WAN features such as central policy-based management, tag-based attachment automation, and segmentation for advanced security configurations.

**Note**  
The association between a core network and a Direct Connect gateway is created, deleted, and managed from the Cloud WAN Console in Network Manager. When using a Direct Connect gateway with Cloud WAN, the Direct Connect Console and the APIs and CLI will reflect the association, but cannot be used to modify it. You can, however, use the Direct Connect API or command line to verify if an association was created.

The following example shows a Cloud WAN global network with three Regions within the Cloud WAN core network. Each Region has its own VPC connected to a core network Development segment shared across those three Regions. Using Cloud WAN, a Direct Connect gateway attachment is created within Cloud WAN using a Direct Connect gateway, which was created using Direct Connect. The attachment is associated with two of the three Regions, ap-southeast-2 and us-west-2 and is allowed access to the Development segment. Even though us-east-1 shares the same Development segment, the Direct Connect gateway attachment is not shared with that Region and is therefore not available. 

![A Direct Connect gateway attachment association with an AWS Cloud WAN core network.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dxattachment-cloudwan.png)


**Topics**
+ [Prerequisites](#direct-connect-cloud-wan-prereq)
+ [Considerations](#direct-connect-cloud-wan-limits)
+ [Direct Connect gateway associations to a Cloud WAN core network](#associate-cloudwan-with-direct-connect-gateway)
+ [Verify a Direct Connect gateway association](#edit-cloudwan-with-direct-connect-gateway)

### Prerequisites
<a name="direct-connect-cloud-wan-prereq"></a>

A Direct Connect gateway association with a Cloud WAN core network requires the following:
+ An existing Direct Connect gateway. For the steps to create a Direct Connect gateway, see [Create a Direct Connect gateway](#create-direct-connect-gateway).
+ An AWS Cloud WAN core network. For information about Cloud WAN, see the [*AWS Cloud WAN User Guide*](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html).

### Considerations
<a name="direct-connect-cloud-wan-limits"></a>

The following limits apply for Direct Connect gateway associations with a Cloud WAN core network:
+ A Direct Connect gateway can be associated with a single Cloud WAN core network and to a single segment of that core network. Once an association is created, that gateway cannot associated to other resources in AWS regions. If you disassociate the gateway from the core network, you can then use that gateway for other association types.
+ The Cloud WAN Direct Connect gateway attachment uses the transit virtual interface type for connectivity.
+ The Cloud WAN attachment does not support allowed prefixes lists. All prefixes in a core network segment will be advertised to the Direct Connect gateway associated to that segment.
+ The quota for maximum prefixes that can be advertised from on-premises to AWS via a transit virtual interface is different from the quota for prefixes advertised from a Cloud WAN core network to on-premises. Quotas for other Direct Connect resources used with a Cloud WAN association are also applicable. See [Direct Connect quotas](#limits).
+ The AS-PATH BGP attribute will be retained across the core network, Direct Connect gateway, and virtual interface.
+ The ASN of a Direct Connect gateway must be outside of the ASN range configured for the Cloud WAN core network. For example, if you have an ASN range of 64512 - 65534 for the core network, the ASN of the Direct Connect gateway must use an ASN outside of that range. 
+ Cloud WAN might not support specific attachment types using the Direct Connect attachment type for transport. For more information about Direct Connect gateway attachments to a Cloud WAN core network, see [Direct Connect gateway attachments in AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-attachment.html) in the *AWS Cloud WAN User Guide*.
+ CloudWatch Network Monitor supports latency and packet loss metrics when used with a Cloud WAN Direct Connect gateway attachment type. The Network Health Indicator feature is not supported. For more information, see [Using Amazon CloudWatch Network Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html) in the *Amazon CloudWatch User Guide*.

### Direct Connect gateway associations to a Cloud WAN core network
<a name="associate-cloudwan-with-direct-connect-gateway"></a>

Associating a Direct Connect gateway to an AWS Cloud WAN core network is performed using either the AWS Cloud WAN console or the Cloud WAN APIs or command line.

To associate an existing Direct connect gateway to a Cloud WAN core network, create a new Direct Connect attachment in the Cloud WAN Console. After the Direct Connect attachment has been created the association is established. By default, when creating the association you can choose the default to include all core network edge locations in the chosen core network segment. Alternatively, you can specify individual edge locations. 

For more information about Direct Connect gateway attachments to a Cloud WAN core network, see [Direct Connect gateway attachments in AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-dxattach-about.html) in the *AWS Cloud WAN User Guide*.

### Verify a Direct Connect gateway association to an AWS Cloud WAN core network
<a name="edit-cloudwan-with-direct-connect-gateway"></a>

You can verify the association of a Direct Connect gateway to a Cloud WAN core network using the Direct Connect console or the Direct Connect API or command line.

**To verify a Direct Connect gateway association to a Cloud WAN core network using the console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Direct Connect gateways** in the navigation pane.

1. Choose the Direct Connect gateway attachment that you want to view the association for.

1. Choose the **Gateway associations** tab. 
   + The **ID** column displays the core network ID that the Direct Connect gateway is associated with.
   + The **State** column displays **associated**.
   + The **Association type** column displays **Cloud WAN Core Network**.

**To verify a Direct Connect gateway association to a Cloud WAN core network using the command line or API**
+ [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html.html) (Direct Connect API)
+ [describe-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-association.html) (AWS CLI)

## Allowed prefixes interactions for Direct Connect gateways
<a name="allowed-to-prefixes"></a>

Learn how allowed prefixes interact with Transit Gateways and virtual private gateways. For more information, see [Routing policies and BGP communities](#routing-and-bgp).

### Virtual private gateway associations
<a name="allowed-to-prefixes-virtual-private-gateway"></a>

The prefix list (IPv4 and IPv6) acts as a filter that allows the same CIDRs, or a smaller range of CIDRs to be advertised to the Direct Connect gateway. You must set the prefixes to a range that is the same or wider than the VPC CIDR block.

**Note**  
The allowed list only functions as a filter, and only the associated VPC CIDR will be advertised to the customer gateway. 

Consider the scenario where you have a VPC with CIDR 10.0.0.0/16 is attached to a virtual private gateway.
+ When the allowed prefixes list is set to 22.0.0.0/24, you do not receive any route because 22.0.0.0/24 is not the same as, or wider than 10.0.0.0/16.
+ When the allowed prefixes list is set to 10.0.0.0/24, you do not receive any route because 10.0.0.0/24 is not the same as 10.0.0.0/16.
+ When the allowed prefixes list is set to 10.0.0.0/15, you do receive 10.0.0.0/16, because the IP address is wider than 10.0.0.0/16.

When you remove or add an allowed prefix, traffic which doesn't use that prefix is not impacted. During updates the status changes from `associated` to `updating`. Modifying an existing prefix can delay or drop only that traffic which uses that prefix. 

### Transit Gateway associations
<a name="allowed-to-prefixes-transit-gateway"></a>

For a Transit Gateway association, you provision the allowed prefixes list on the Direct Connect gateway. The list routes on-premises traffic to or from a Direct Connect gateway to the Transit Gateway, even when the VPCs attached to the Transit Gateway do not have assigned CIDRs. Allowed prefixes work differently, depending on the gateway type:
+ For Transit Gateway associations, only the allowed prefixes entered will be advertised to on-premises. These will show as originating from the Direct Connect gateway ASN. 
+ For virtual private gateways, the allowed prefixes entered act as a filter to allow the same or smaller CIDRs. 

Consider the scenario where you have a VPC with CIDR 10.0.0.0/16 attached to a Transit Gateway.
+ When the allowed prefixes list is set to 22.0.0.0/24, you receive 22.0.0.0/24 through BGP on your transit virtual interface. You do not receive 10.0.0.0/16 because we directly provision the prefixes that are in the allowed prefix list.
+ When the allowed prefixes list is set to 10.0.0.0/24, you receive 10.0.0.0/24 through BGP on your transit virtual interface. You do not receive 10.0.0.0/16 because we directly provision the prefixes that are in the allowed prefix list.
+ When the allowed prefixes list is set to 10.0.0.0/8, you receive 10.0.0.0/8 through BGP on your transit virtual interface. 

Allowed prefix overlaps are not allowed when multiple Transit Gateways are associated with a Direct Connect gateway. For example, if you have a Transit Gateway with an allowed prefix list that includes 10.1.0.0/16, and a second Transit Gateway with an allowed prefix list that includes 10.2.0.0/16 and 0.0.0.0/0, you can't set the associations from the second Transit Gateway to 0.0.0.0/0. Since 0.0.0.0/0 includes all IPv4 networks, you can't configure 0.0.0.0/0 if multiple Transit Gateways are associated with a Direct Connect gateway. An error is returned indicating that the allowed routes overlap one or more existing allowed routes on the Direct Connect gateway.

When you remove or add an allowed prefix, traffic which doesn't use that prefix is not impacted. During updates the status changes from `associated` to `updating`. Modifying an existing prefix can delay or drop only that traffic which uses that prefix. 

### Example: Allowed to prefixes in a Transit Gateway configuration
<a name="prefix-example"></a>

Consider the configuration where you have instances in two different AWS Regions which need to access the corporate data center. You can use the following resources for this configuration:
+ A Transit Gateway in each Region.
+ A Transit Gateway peering connection.
+ A Direct connect gateway.
+ A Transit Gateway association between one of the Transit Gateways (the one in us-east-1) to the Direct Connect gateway.
+ A transit virtual interface from the on-premises location and the Direct Connect location.

![Private VIF Routing no AS_PATH](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/dxg-asn.png)


Configure the following options for the resources:
+ Direct Connect gateway: Set the ASN to 65030. For more information, see [Create a Direct Connect gateway](#create-direct-connect-gateway).
+ Transit virtual interface: Set the VLAN to 899, and the customer router peer ASN to 65020. For more information, see [Create a transit virtual interface to the Direct Connect gateway](#create-transit-vif-dx).
+ Direct Connect gateway association with the Transit Gateway: Set the allowed prefixes to 10.0.0.0/8. 

  This CIDR block encompasses both VPC CIDR blocks (10.0.0.0/16 and 10.2.0.0/16). For more information, see [Associate or disassociate a Transit Gateway with Direct Connect.](#associate-tgw-with-direct-connect-gateway).
+ VPC route: To route traffic from the 10.2.0.0/16 VPC, create a route in the VPC route table with a Destination of 0.0.0.0/0 and the Transit Gateway ID as the Target. This enables traffic from the VPC to reach the Direct Connect gateway. For more information about routing to a Transit Gateway, see [Routing for a Transit Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-tgw) in the * Amazon VPC User Guide*.

# Tag AWS Direct Connect resources
<a name="using-tags"></a>

A tag is a label that a resource owner assigns to their Direct Connect resources. Each tag consists of a key and an optional value, both of which you define. Tags enable the resource owner to categorize your Direct Connect resources in different ways, for example, by purpose, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags you've assigned to it. 

For example, you have two Direct Connect connections in a Region, each in different locations. Connection `dxcon-11aa22bb` is a connection serving production traffic, and is associated with virtual interface `dxvif-33cc44dd`. Connection `dxcon-abcabcab` is a redundant (backup) connection, and is associated with virtual interface `dxvif-12312312`. You might choose to tag your connections and virtual interfaces as follows, to help distinguish them:



- **`dxcon-11aa22bb`**
  - **Tag key:** Purpose / **Tag value:** Production
  - **Tag key:** Location / **Tag value:** Amsterdam

- **`dxvif-33cc44dd`**
  - **Tag key:** Purpose
  - **Tag value:** Production

- **`dxcon-abcabcab`**
  - **Tag key:** Purpose / **Tag value:** Backup
  - **Tag key:** Location / **Tag value:** Frankfurt

- **`dxvif-12312312`**
  - **Tag key:** Purpose
  - **Tag value:** Backup



We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. Tags don't have any semantic meaning to Direct Connect and are interpreted strictly as a string of characters. Also, tags are not automatically assigned to your resources. You can edit tag keys and values, and you can remove tags from a resource at any time. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value. If you delete a resource, any tags for the resource are also deleted. 

You can tag the following Direct Connect resources using the Direct Connect console, the Direct Connect API, the AWS CLI, the AWS Tools for Windows PowerShell, or an AWS SDK. When you use these tools to manage tags, you must specify the Amazon Resource Name (ARN) for the resource. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference*.


| Resource | Supports tags | Supports tags on creation | Supports tags controlling access and resource allocation | Supports cost allocation | 
| --- | --- | --- | --- | --- | 
| Connections |  Yes | Yes | Yes | Yes | 
| Virtual interfaces | Yes | Yes | Yes | No | 
| Link aggregation groups (LAG) | Yes | Yes | Yes | Yes | 
| Interconnects | Yes | Yes | Yes | Yes | 
| Direct Connect gateways | Yes | Yes | Yes | No | 

## Tag restrictions
<a name="using-tags-restrictions"></a>

The following rules and restrictions apply to tags:
+ Maximum number of tags per resource: 50
+ Maximum key length: 128 Unicode characters
+ Maximum value length: 265 Unicode characters
+ Tag keys and values are case-sensitive.
+ The `aws:` prefix is reserved for AWS use. You can’t edit or delete a tag’s key or value when the tag has a tag key with the `aws:` prefix. Tags with a tag key with the `aws:` prefix do not count against your tags per resource limit.
+ Allowed characters are letters, spaces, and numbers representable in UTF-8, plus the following special characters: \+ - = . \_ : / @
+ Only the resource owner can add or remove tags. For example, if there is a hosted connection, the partner will not be able to add, remove, or view the tags. 
+ Cost allocation tags are only supported for connections, interconnects, and LAGs. For information about how to use tags with cost management, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the* AWS Billing and Cost Management User Guide*.

## Working with tags using the CLI or API
<a name="working-with-tags"></a>

Use the following to add, update, list, and delete the tags for your resources.


| Task | API | CLI | 
| --- | --- | --- | 
| Add or overwrite one or more tags. |  [TagResource](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_TagResource.html) | [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/tag-resource.html) | 
| Delete one or more tags. |  [UntagResource](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UntagResource.html) | [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/untag-resource.html) | 
| Describe one or more tags. | [DescribeTags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeTags.html) | [describe-tags](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-tags.html) | 

### Examples
<a name="working-with-tags-examples"></a>

Use the [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/tag-resource.html) command to tag the Connection `dxcon-11aa22bb`.

```
aws directconnect tag-resource --resource-arn arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-11aa22bb --tags "key=Purpose,value=Production"
```

Use the [describe-tags](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-tags.html) command to describe the Connection `dxcon-11aa22bb` tags.

```
aws directconnect describe-tags --resource-arn arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-11aa22bb
```

Use the [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/untag-resource.html) command to remove a tag from Connection `dxcon-11aa22bb`.

```
aws directconnect untag-resource --resource-arn arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-11aa22bb --tag-keys Purpose
```

# Security in AWS Direct Connect
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Direct Connect, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using Direct Connect. The following topics show you how to configure Direct Connect to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Direct Connect resources. 

**Topics**
+ [Data protection](#data-protection)
+ [Identity and Access Management](#security-iam)
+ [Logging and monitoring](#dc-incident-response)
+ [Compliance validation](#DirectConnect-compliance)
+ [Resilience in Direct Connect](#disaster-recovery-resiliency)
+ [Infrastructure security](#infrastructure-security)

## Data protection in AWS Direct Connect
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Direct Connect. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Direct Connect or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

For more information about data protection, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post on the *AWS Security Blog*.

**Topics**
+ [Internetwork traffic privacy](#encryption-at-rest)
+ [Encryption](#encryption-in-transit)

### Internetwork traffic privacy in AWS Direct Connect
<a name="encryption-at-rest"></a>

#### Traffic between service and on-premises clients and applications
<a name="inter-network-traffic-privacy-on-prem"></a>

You have two connectivity options between your private network and AWS: 
+ An association to an AWS Site-to-Site VPN. For more information, see [Infrastructure security](#infrastructure-security).
+ An association to VPCs. For more information, see [Virtual private gateway associations](#virtualgateways) and [Transit Gateway associations](#direct-connect-transit-gateways).

#### Traffic between AWS resources in the same Region
<a name="inter-network-traffic-privacy-within-region"></a>

You have two connectivity options:
+ An association to an AWS Site-to-Site VPN. For more information, see [Infrastructure security](#infrastructure-security).
+ An association to VPCs. For more information, see [Virtual private gateway associations](#virtualgateways) and [Transit Gateway associations](#direct-connect-transit-gateways).

### Encryption in AWS Direct Connect
<a name="encryption-in-transit"></a>

AWS Direct Connect does not encrypt your traffic that is in transit by default. To encrypt the data in transit that traverses AWS Direct Connect, you must use the transit encryption options for that service. To learn about EC2 instance traffic encryption, see [Encryption in Transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the Amazon EC2 User Guide.

With AWS Direct Connect and AWS Site-to-Site VPN, you can combine one or more AWS Direct Connect dedicated network connections with the Amazon VPC VPN. This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections. For more information, see [Amazon VPC-to-Amazon VPC Connectivity Options](https://aws.amazon.com/answers/networking/aws-single-data-center-ha-network-connectivity/).

MAC Security (MACsec) is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity. You can use Direct Connect connections that support MACsec to encrypt your data from your corporate data center to the Direct Connect location. For more information, see [MAC Security in Direct Connect](#MACsec).

## Identity and Access Management for Direct Connect
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Direct Connect resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [Audience](#security_iam_audience)
+ [Authenticating with identities](#security_iam_authentication)
+ [Managing access using policies](#security_iam_access-manage)
+ [How Direct Connect works with IAM](#security_iam_service-with-iam)
+ [Identity-based policy examples for Direct Connect](#security_iam_id-based-policy-examples)
+ [Service-linked roles](#using-service-linked-roles)
+ [AWS managed policies](#security-iam-awsmanpol)
+ [Troubleshooting](#security_iam_troubleshoot)

### Audience
<a name="security_iam_audience"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting Direct Connect identity and access](#security_iam_troubleshoot))
+ **Service administrator** - determine user access and submit permission requests (see [How Direct Connect works with IAM](#security_iam_service-with-iam))
+ **IAM administrator** - write policies to manage access (see [Identity-based policy examples for Direct Connect](#security_iam_id-based-policy-examples))

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

### How Direct Connect works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Direct Connect, learn what IAM features are available to use with Direct Connect.


**IAM features you can use with Direct Connect**  

| IAM feature | Direct Connect support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Partial | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  Yes | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  No  | 

To get a high-level view of how Direct Connect and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

#### Identity-based policies for Direct Connect
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

##### Identity-based policy examples for Direct Connect
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Direct Connect identity-based policies, see [Identity-based policy examples for Direct Connect](#security_iam_id-based-policy-examples).

#### Resource-based policies within Direct Connect
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

#### Policy actions for Direct Connect
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Direct Connect actions, see [Actions Defined by Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Direct Connect use the following prefix before the action:

```
Direct Connect
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "directconnect:{{action1}}",
      "directconnect{{action2}}"
         ]
```

#### Policy resources for Direct Connect
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Direct Connect resource types and their ARNs, see [Resources Defined by Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-resources-for-iam-policies) in the *AWS Direct Connect API Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-actions-as-permissions).

To view examples of Direct Connect identity-based policies, see [Identity-based policy examples for Direct Connect](#security_iam_id-based-policy-examples).

To view examples of Direct Connect resource-based policies, see [Direct Connect identity-based policy examples using tag-based conditions](#security_iam_resource-based-policy-examples).

#### Policy condition keys for Direct Connect
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Direct Connect condition keys, see [Condition Keys for Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-policy-keys) in the *AWS Direct Connect API Reference*. To learn with which actions and resources you can use a condition key, see [Actions, Resources, and Condition Keys for Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html) in the *Service Authorization Reference*.

To view examples of Direct Connect identity-based policies, see [Identity-based policy examples for Direct Connect](#security_iam_id-based-policy-examples).

#### ACLs in Direct Connect
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

#### ABAC with Direct Connect
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

#### Using temporary credentials with Direct Connect
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

#### Cross-service principal permissions for Direct Connect
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

#### Service roles for Direct Connect
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break Direct Connect functionality. Edit service roles only when Direct Connect provides guidance to do so.

#### Service-linked roles for Direct Connect
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** No 

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.

### Identity-based policy examples for Direct Connect
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify Direct Connect resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Direct Connect, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Actions, resources, and conditions](#security_iam_service-dx-id-based-policies)
+ [Using the console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Read-only access to Direct Connect](#security_iam_id-based-policy-examples-read-access)
+ [Full access to Direct Connect](#security_iam_id-based-policy-examples-full-access)
+ [Tag-based condition keys](#security_iam_resource-based-policy-examples)

#### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Direct Connect resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

#### Direct Connect actions, resources, and conditions
<a name="security_iam_service-dx-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. Direct Connect supports specific actions, resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

##### Actions
<a name="security_iam_service_dx_actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Direct Connect use the following prefix before the action: `directconnect:`. For example, to grant someone permission to run an Amazon EC2 instance with the Amazon EC2 `DescribeVpnGateways` API operation, you include the `ec2:DescribeVpnGateways` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Direct Connect defines its own set of actions that describe tasks that you can perform with this service.

The following example policy grants read access to Direct Connect.

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
                "directconnect:Describe*",
                "ec2:DescribeVpnGateways"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The following example policy grants full access to Direct Connect.

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
                "directconnect:*",
                "ec2:DescribeVpnGateways"
            ],
            "Resource": "*"
        }
    ]
}
```

------

To see a list of Direct Connect actions, see [Actions Defined by Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-actions-as-permissions) in the *IAM User Guide*.

##### Resources
<a name="security_iam_service-dx-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Direct Connect uses the following ARNs:


**Direct connect resource ARNs**  

| Resource Type | ARN | 
| --- | --- | 
| dxcon | arn:${Partition}:directconnect:${Region}:${Account}:dxcon/${ConnectionId} | 
| dxlag |  arn:${Partition}:directconnect:${Region}:${Account}:dxlag/${LagId} | 
| dx-vif | arn:${Partition}:directconnect:${Region}:${Account}:dxvif/${VirtualInterfaceId} | 
| dx-gateway | arn:${Partition}:directconnect::${Account}:dx-gateway/${DirectConnectGatewayId} | 

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `dxcon-11aa22bb` interface in your statement, use the following ARN:

```
"Resource": "arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-11aa22bb
```

To specify all virtual interfaces that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:directconnect:*:*:dxvif/*"
```

Some Direct Connect actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*). 

```
"Resource": "*"
```

To see a list of Direct Connect resource types and their ARNs, see [Resource Types Defined by Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-resources-for-iam-policies) in the *IAM User Guide*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-actions-as-permissions).

If a resource ARN or a resource ARN pattern other than `*` is specified in the `Resource` field of the IAM policy statement for DescribeConnections, DescribeVirtualInterfaces, DescribeDirectConnectGateways, DescribeInterconnects, or DescribeLags, then the specified `Effect` will not occur unless the matching resource ID is also passed in the API call. However, if you provide `*` as the resource instead of a specific resource ID in the IAM policy statement, the specified `Effect` will work. 

In the following example, neither specified `Effect` will succeed if the `DescribeConnections` action is called without a `connectionId` passed in the request.

```
"Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "directconnect:DescribeConnections"
        ],
        "Resource": [
            "arn:aws:directconnect:*:123456789012:dxcon/*"
        ]
    },
{
        "Effect": "Deny",
        "Action": [
            "directconnect:DescribeConnections"
        ],
        "Resource": [
            "arn:aws:directconnect:*:123456789012:dxcon/example1"
        ]
    }
]
```

 However, in the following example, `"Effect": "Allow"` will succeed for the `DescribeConnections` action since `*` was provided for the `Resource` field of the IAM policy statement, regardless of whether the `connectionId` was specified in the request. 

```
"Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "directconnect:DescribeConnections
        ],
        "Resource": [
            "*"
        ]
    }
]
```

##### Condition keys
<a name="security_iam_service-dx-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Direct Connect defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

You can use condition keys with the tag resource. For more information, see [Example: Restricting Access to a Specific Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html#iam-example-region). 

To see a list of Direct Connect condition keys, see [Condition Keys for Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-policy-keys) in the *IAM User Guide*. To learn with which actions and resources you can use a condition key, see [Actions Defined by Direct Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsdirectconnect.html#awsdirectconnect-actions-as-permissions).

#### Using the Direct Connect console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the Direct Connect console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Direct Connect resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (s or roles) with that policy.

To ensure that those entities can still use the Direct Connect console, also attach the following AWS managed policy to the entities. For more information, see [Adding Permissions to a User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*:

```
directconnect
```

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

#### Read-only access to Direct Connect
<a name="security_iam_id-based-policy-examples-read-access"></a>

The following example policy grants read access to Direct Connect.

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
                "directconnect:Describe*",
                "ec2:DescribeVpnGateways"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Full access to Direct Connect
<a name="security_iam_id-based-policy-examples-full-access"></a>

The following example policy grants full access to Direct Connect.

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
                "directconnect:*",
                "ec2:DescribeVpnGateways"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Direct Connect identity-based policy examples using tag-based conditions
<a name="security_iam_resource-based-policy-examples"></a>

You can control access to resources and requests by using tag key conditions. You can also use a condition in your IAM policy to control whether specific tag keys can be used on a resource or in a request. 

For information about how to use tags with IAM policies, see [Controlling Access Using Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html) in the *IAM User Guide*.

##### Associating Direct Connect virtual interfaces based on tags
<a name="security_iam_resource-based-policy-examples-associate-interface"></a>

The following example shows how you might create a policy that allows associating a virtual interface only if the tag contains the environment key and the preprod or production values. 

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
            "directconnect:AssociateVirtualInterface"
          ],
          "Resource": "arn:aws:directconnect:*:*:dxvif/*",
          "Condition": {
            "StringEquals": {
              "aws:ResourceTag/environment": [
                "preprod",
                "production"
              ]
            }
          }
        },
        {
          "Effect": "Allow",
          "Action": "directconnect:DescribeVirtualInterfaces",
          "Resource": "*"
        }
      ]
    }
```

------

##### Controlling access to requests based on tags
<a name="security_iam_resource-based-policy-examples-associate-interface-requests"></a>

You can use conditions in your IAM policies to control which tag key–value pairs can be passed in a request that tags an AWS resource. The following example shows how you might create a policy that allows using the Direct Connect TagResource action to attach tags to a virtual interface only if the tag contains the environment key and the preprod or production values. As a best practice, use the `ForAllValues` modifier with the `aws:TagKeys` condition key to indicate that only the key environment is allowed in the request. 

 

------
#### [ JSON ]

****  

```
    {
        "Version":"2012-10-17",		 	 	 
        "Statement": {
            "Effect": "Allow",
            "Action": "directconnect:TagResource",
            "Resource": "arn:aws:directconnect:*:*:dxvif/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/environment": [
                        "preprod",
                        "production"
                    ]
                },
                "ForAllValues:StringEquals": {"aws:TagKeys": "environment"}
            }
        }
    }
```

------

##### Controlling tag keys
<a name="security_iam_resource-based-policy-examples-associate-interface-keys"></a>

You can use a condition in your IAM policies to control whether specific tag keys can be used on a resource or in a request. 

The following example shows how you might create a policy that allows you to tag resources, but only with the tag key environment

------
#### [ JSON ]

****  

```
     {
      "Version":"2012-10-17",		 	 	 
      "Statement": {
        "Effect": "Allow",
        "Action": "directconnect:TagResource",
        "Resource": "*",
        "Condition": {
          "ForAllValues:StringEquals": {
            "aws:TagKeys": [
              "environment"
            ]
          }
        }
      }
    }
```

------

### Service-linked roles for Direct Connect
<a name="using-service-linked-roles"></a>

AWS Direct Connect uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Direct Connect. Service-linked roles are predefined by Direct Connect and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up Direct Connect easier because you don’t have to manually add the necessary permissions. Direct Connect defines the permissions of its service-linked roles, and unless defined otherwise, only Direct Connect can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Direct Connect resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

#### Service-linked role permissions for Direct Connect
<a name="slr-permissions"></a>

Direct Connect uses a service-linked role named `AWSServiceRoleForDirectConnect`. This allows Direct Connect to retrieve the MACSec secret stored in AWS Secrets Manager on your behalf. 

The `AWSServiceRoleForDirectConnect` service-linked role trusts the following services to assume the role:
+ `directconnect.amazonaws.com`

The `AWSServiceRoleForDirectConnect` service-linked role uses the managed policy `AWSDirectConnectServiceRolePolicy`.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For the `AWSServiceRoleForDirectConnect` service-linked role to be created successfully, the IAM identity that you use Direct Connect with must have the required permissions. To grant the required permissions, attach the following policy to the IAM identity.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": "iam:CreateServiceLinkedRole",
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "directconnect.amazonaws.com"
                }
            },
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Action": "iam:GetRole",
            "Effect": "Allow",
            "Resource": "*"
       }
    ]
}
```

------

For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

#### Creating a service-linked role for Direct Connect
<a name="create-slr"></a>

You don't need to manually create a service-linked role. AWS Direct Connect creates the service-linked role for you. When you run the `associate-mac-sec-key` command, AWS creates a service-linked role that allows Direct Connect to retrieve the MACsec secrets that are stored in AWS Secrets Manager on your behalf in the AWS Management Console, the AWS CLI, or the AWS API. 

**Important**  
This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role. To learn more, see [A New Role Appeared in My IAM Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. Direct Connect creates the service-linked role for you again. 

You can also use the IAM console to create a service-linked role with the AWS Direct Connect use case. In the AWS CLI or the AWS API, create a service-linked role with the `directconnect.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

#### Editing a service-linked role for Direct Connect
<a name="edit-slr"></a>

Direct Connect does not allow you to edit the `AWSServiceRoleForDirectConnect` service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

#### Deleting a service-linked role for Direct Connect
<a name="delete-slr"></a>

You don't need to manually delete the `AWSServiceRoleForDirectConnect` role. When you delete your service linked role, you must delete all the associated resources that are stored in AWS Secrets Manager web service. The AWS Management Console, the AWS CLI, or the AWS API, Direct Connect cleans up the resources and deletes the service-linked role for you.

You can also use the IAM console to delete the service-linked role. To do this, you must first manually clean up the resources for your service-linked role and then you can delete it.

**Note**  
If the Direct Connect service is using the role when you try to delete the resources, then deletion might fail. If this happens, wait a few minutes, and then try the operation again.

**To delete Direct Connect resources used by the `AWSServiceRoleForDirectConnect`**

1. Remove the association between all MACsec keys and connections. For more information, see [Remove the association between a MACsec secret key and a Direct Connect connection](#disassociate-key-connection)

1. Remove the association between all MACsec keys and LAGs. For more information, see [Remove the association between a MACsec secret key and a Direct Connect endpoint LAG](#disassociate-key-lag)

**To manually delete the service-linked role using IAM**  
Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForDirectConnect` service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

#### Supported regions for Direct Connect service-linked roles
<a name="slr-regions"></a>

Direct Connect supports using service-linked roles in all AWS Regions where the MAC Security feature is available. For more information, see [AWS Direct Connect Locations](https://aws.amazon.com/directconnect/locations/).

### AWS managed policies for AWS Direct Connect
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

#### AWS managed policy: AWSDirectConnectFullAccess
<a name="security-iam-awsmanpol-AWSDirectConnectFullAccess"></a>

You can attach the `AWSDirectConnectFullAccess` policy to your IAM identities. This policy grants permissions that allow full access to Direct Connect.

To view the permissions for this policy, see [AWSDirectConnectFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectFullAccess) in the AWS Management Console.

#### AWS managed policy: AWSDirectConnectReadOnlyAccess
<a name="security-iam-awsmanpol-AWSDirectConnectReadOnlyAccess"></a>

You can attach the `AWSDirectConnectReadOnlyAccess` policy to your IAM identities. This policy grants permissions that allow read-only access to Direct Connect.

To view the permissions for this policy, see [AWSDirectConnectReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess) in the AWS Management Console.

#### AWS managed policy: AWSDirectConnectServiceRolePolicy
<a name="security-iam-awsmanpol-AWSDirectConnectServiceRolePolicy"></a>

This policy is attached to the service-linked role named **AWSServiceRoleForDirectConnect** to allow Direct Connect to retrieve MAC Security secrets on your behalf. For more information, see [Service-linked roles for Direct Connect](#using-service-linked-roles).

To view the permissions for this policy, see [AWSDirectConnectServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSDirectConnectServiceRolePolicy) in the AWS Management Console.

#### Direct Connect updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Direct Connect since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Direct Connect Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSDirectConnectServiceRolePolicy](#security-iam-awsmanpol-AWSDirectConnectServiceRolePolicy) - New policy | To support MAC Security, the AWSServiceRoleForDirectConnect service-linked role was added. | March 31, 2021 | 
| Direct Connect started tracking changes | Direct Connect started tracking changes to its AWS managed policies. | March 31, 2021 | 

### Troubleshooting Direct Connect identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Direct Connect and IAM.

**Topics**
+ [I am not authorized to perform an action in Direct Connect](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I want to allow people outside of my AWS account to access my Direct Connect resources](#security_iam_troubleshoot-cross-account-access)

#### I am not authorized to perform an action in Direct Connect
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but doesn't have the fictional `directconnect:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: directconnect:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the `{{my-example-widget}}` resource by using the `directconnect:{{GetWidget}}` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Direct Connect.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Direct Connect. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I want to allow people outside of my AWS account to access my Direct Connect resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Direct Connect supports these features, see [How Direct Connect works with IAM](#security_iam_service-with-iam).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Logging and monitoring in AWS Direct Connect
<a name="dc-incident-response"></a>

You can use the following automated monitoring tools to watch Direct Connect and report when something is wrong:
+ **Amazon CloudWatch Alarms** – Watch a single metric over a time period that you specify. Perform one or more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon SNS topic. CloudWatch alarms do not invoke actions simply because they are in a particular state; the state must have changed and been maintained for a specified number of periods. For more information, see [Monitor with Amazon CloudWatch](#monitoring-cloudwatch).
+ **AWS CloudTrail Log Monitoring** – Share log files between accounts and monitor CloudTrail log files in real time by sending them to CloudWatch Logs. You can also write log processing applications in Java and validate that your log files have not changed after delivery by CloudTrail. For more information, see [Log Direct Connect API calls using AWS CloudTrail](#logging_dc_api_calls) and [Working with CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.html) in the *AWS CloudTrail User Guide*.

For more information, see [Monitoring and visibility with Direct Connect](#monitoring-overview).

## Compliance validation for AWS Direct Connect
<a name="DirectConnect-compliance"></a>

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Resilience in AWS Direct Connect
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, Direct Connect offers several features to help support your data resiliency and backup needs.

For information about how to use VPN with AWS Direct Connect, see [AWS Direct Connect Plus VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-plus-vpn-network-to-amazon.html).

### Failover
<a name="failover"></a>

The AWS Direct Connect Resiliency Toolkit provides a connection wizard with multiple resiliency models that helps you order dedicated connections to achieve your SLA objective. You select a resiliency model, and then the AWS Direct Connect Resiliency Toolkit guides you through the dedicated connection ordering process. The resiliency models are designed to ensure that you have the appropriate number of dedicated connections in multiple locations. 
+ **Maximum Resiliency**: You can achieve maximum resiliency for critical workloads by using separate connections that terminate on separate devices in more than one location. This model provides resiliency against device, connectivity, and complete location failures.
+ **High Resiliency**: You can achieve high resiliency for critical workloads by using two single connections to multiple locations. This model provides resiliency against connectivity failures caused by a fiber cut or a device failure. It also helps prevent a complete location failure.
+ **Development and Test**: You can achieve development and test resiliency for non-critical workloads by using separate connections that terminate on separate devices in one location. This model provides resiliency against device failure, but does not provide resiliency against location failure.

For more information, see [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit).

## Infrastructure security in Direct Connect
<a name="infrastructure-security"></a>

As a managed service, AWS Direct Connect is protected by the AWS global network security procedures. You use AWS published API calls to access Direct Connect through the network. Clients must support Transport Layer Security (TLS) 1.2 or later. We recommend TLS 1.3. Clients must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) (AWS STS) to generate temporary security credentials to sign requests.

You can call these API operations from any network location, but Direct Connect supports resource-based access policies, which can include restrictions based on the source IP address. You can also use Direct Connect policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs. Effectively, this isolates network access to a given Direct Connect resource from only the specific VPC within the AWS network. For example, see [Identity-based policy examples for Direct Connect](#security_iam_id-based-policy-examples). 

### Border Gateway Protocol (BGP) security
<a name="security-bgp"></a>

The internet relies in large part on BGP for routing information between network systems. BGP routing can some times be susceptible to malicious attacks, or BGP hijacking. To understand how AWS works to more securely safeguard your network from BGP hijacking, see [How AWS is helping to secure internet routing](https://aws.amazon.com/blogs/networking-and-content-delivery/how-aws-is-helping-to-secure-internet-routing).

# Use the Direct Connect CLI
<a name="using-cli"></a>

You can use the AWS CLI to create and work with Direct Connect resources.

The following example uses the AWS CLI commands to create a Direct Connect connection. You can also download the Letter of Authorization and Connecting Facility Assignment (LOA-CFA) or provision a private or public virtual interface.

Before you begin, ensure that you have installed and configured the AWS CLI. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

**Topics**
+ [Step 1: Create a connection](#using-cli-create-connection)
+ [Step 2: Download the LOA-CFA](#using-cli-loa-cfa)
+ [Step 3: Create a virtual interface and get the router configuration](#using-cli-create-vif)

## Step 1: Create a connection
<a name="using-cli-create-connection"></a>

The first step is to submit a connection request. Ensure that you know the port speed that you require and the Direct Connect location. For more information, see [Dedicated and hosted connections](#WorkingWithConnections).

**To create a connection request**

1. Describe the Direct Connect locations for your current Region. In the output that's returned, take note of the location code for the location in which you want to establish the connection.

   ```
   aws directconnect describe-locations
   ```

   ```
   {
       "locations": [
           {
               "locationName": "City 1, United States",
               "locationCode": "Example Location 1"
           },
           {
               "locationName": "City 2, United States",
               "locationCode": "Example location"
           }
       ]
   }
   ```

1. Create the connection and specify a name, the port speed, and the location code. In the output that's returned, take note of the connection ID. You need the ID to get the LOA-CFA in the next step.

   ```
   aws directconnect create-connection --location {{Example location}} --bandwidth {{1Gbps}} --connection-name "{{Connection to AWS}}"
   ```

   ```
   {
       "ownerAccount": "123456789012",
       "connectionId": "dxcon-EXAMPLE",
       "connectionState": "requested",
       "bandwidth": "1Gbps",
       "location": "Example location",
       "connectionName": "Connection to AWS",
       "region": "sa-east-1"
   }
   ```

## Step 2: Download the LOA-CFA
<a name="using-cli-loa-cfa"></a>

After you've requested a connection, you can get the LOA-CFA using the `describe-loa` command. The output is base64-encoded. You must extract the relevant LOA content, decode it, and create a PDF file.

**To get the LOA-CFA using Linux or macOS**  
In this example, the final part of the command decodes the content using the base64 utility, and sends the output to a PDF file.

```
aws directconnect describe-loa --connection-id {{dxcon-fg31dyv6}} --output text --query loaContent|base64 --decode > {{myLoaCfa}}.pdf
```

**To get the LOA-CFA using Windows**  
In this example, the output is extracted to a file called myLoaCfa.base64. The second command uses the `certutil` utility to decode the file and send the output to a PDF file.

```
aws directconneawsct describe-loa --connection-id {{dxcon-fg31dyv6}} --output text --query loaContent > myLoaCfa.base64
```

```
certutil -decode myLoaCfa.base64 {{myLoaCfa}}.pdf
```

After you've downloaded the LOA-CFA, send it to your network provider or colocation provider. 

## Step 3: Create a virtual interface and get the router configuration
<a name="using-cli-create-vif"></a>

After you have placed an order for a Direct Connect connection, you must create a virtual interface to begin using it. You can create a private virtual interface to connect to your VPC. Or, you can create a public virtual interface to connect to AWS services that aren't in a VPC. You can create a virtual interface that supports IPv4 or IPv6 traffic.

Before you begin, ensure that you've read the prerequisites in [Prerequisites for virtual interfaces](#vif-prerequisites). 

When you create a virtual interface using the AWS CLI, the output includes generic router configuration information. To create a router configuration that's specific to your device, use the Direct Connect console. For more information, see [Download the router configuration file](#vif-router-config).

**To create a private virtual interface**

1. Get the ID of the virtual private gateway (vgw-*xxxxxxxx*) that's attached to your VPC. You need the ID to create the virtual interface in the next step.

   ```
   aws ec2 describe-vpn-gateways
   ```

   ```
   {
       "VpnGateways": [
           {
               "State": "available", 
               "Tags": [
                   {
                       "Value": "DX_VGW", 
                       "Key": "Name"
                   }
               ], 
               "Type": "ipsec.1", 
               "VpnGatewayId": "vgw-ebaa27db", 
               "VpcAttachments": [
                   {
                       "State": "attached", 
                       "VpcId": "vpc-24f33d4d"
                   }
               ]
           }
       ]
   }
   ```

1. Create a private virtual interface. You must specify a name, a VLAN ID, and a BGP Autonomous System Number (ASN). 

   For IPv4 traffic, you need private IPv4 addresses for each end of the BGP peering session. You can specify your own IPv4 addresses, or you can let Amazon generate the addresses for you. In the following example, the IPv4 addresses are generated for you.

   ```
   aws directconnect create-private-virtual-interface --connection-id {{dxcon-fg31dyv6}} --new-private-virtual-interface virtualInterfaceName={{PrivateVirtualInterface}},vlan={{101}},asn={{65000}},virtualGatewayId={{vgw-ebaa27db}},addressFamily=ipv4
   ```

   ```
   {
       "virtualInterfaceState": "pending",
       "asn": 65000,
       "vlan": 101,
       "customerAddress": "192.168.1.2/30",
       "ownerAccount": "123456789012",
       "connectionId": "dxcon-fg31dyv6",
       "addressFamily": "ipv4", 
       "virtualGatewayId": "vgw-ebaa27db",
       "virtualInterfaceId": "dxvif-ffhhk74f",
       "authKey": "asdf34example",
       "routeFilterPrefixes": [],
       "location": "Example location",
       "bgpPeers": [
           {
               "bgpStatus": "down", 
               "customerAddress": "192.168.1.2/30", 
               "addressFamily": "ipv4", 
               "authKey": "asdf34example", 
               "bgpPeerState": "pending", 
               "amazonAddress": "192.168.1.1/30", 
               "asn": 65000
           }
       "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-ffhhk74f\">\n  <vlan>101</vlan>\n  <customer_address>192.168.1.2/30</customer_address>\n  <amazon_address>192.168.1.1/30</amazon_address>\n  <bgp_asn>65000</bgp_asn>\n  <bgp_auth_key>asdf34example</bgp_auth_key>\n  <amazon_bgp_asn>7224</amazon_bgp_asn>\n  <connection_type>private</connection_type>\n</logical_connection>\n",
       "amazonAddress": "192.168.1.1/30",
       "virtualInterfaceType": "private",
       "virtualInterfaceName": "PrivateVirtualInterface"
   }
   ```

   To create a private virtual interface that supports IPv6 traffic, use the same command as above and specify `ipv6` for the `addressFamily` parameter. You cannot specify your own IPv6 addresses for the BGP peering session; Amazon allocates you IPv6 addresses.

1. To view the router configuration information in XML format, describe the virtual interface you created. Use the `--query` parameter to extract the `customerRouterConfig` information, and the `--output` parameter to organize the text into tab-delimited lines.

   ```
   aws directconnect describe-virtual-interfaces --virtual-interface-id {{dxvif-ffhhk74f}} --query virtualInterfaces[*].customerRouterConfig --output text
   ```

   ```
   <?xml version="1.0" encoding="UTF-8"?>
   <logical_connection id="dxvif-ffhhk74f">
     <vlan>101</vlan>
     <customer_address>192.168.1.2/30</customer_address>
     <amazon_address>192.168.1.1/30</amazon_address>
     <bgp_asn>65000</bgp_asn>
     <bgp_auth_key>asdf34example</bgp_auth_key>
     <amazon_bgp_asn>7224</amazon_bgp_asn>
     <connection_type>private</connection_type>
   </logical_connection>
   ```

**To create a public virtual interface**

1. To create a public virtual interface, you must specify a name, a VLAN ID, and a BGP Autonomous System Number (ASN). 

   For IPv4 traffic, you must also specify public IPv4 addresses for each end of the BGP peering session, and public IPv4 routes that you will advertise over BGP. The following example creates a public virtual interface for IPv4 traffic.

   ```
   aws directconnect create-public-virtual-interface --connection-id {{dxcon-fg31dyv6}} --new-public-virtual-interface virtualInterfaceName={{PublicVirtualInterface}},vlan={{2000}},asn={{65000}},amazonAddress={{203.0.113.1/30}},customerAddress={{203.0.113.2/30}},addressFamily=ipv4,routeFilterPrefixes=[{cidr={{203.0.113.0/30}}},{cidr={{203.0.113.4/30}}}]
   ```

   ```
   {
       "virtualInterfaceState": "verifying",
       "asn": 65000,
       "vlan": 2000,
       "customerAddress": "203.0.113.2/30",
       "ownerAccount": "123456789012",
       "connectionId": "dxcon-fg31dyv6",
       "addressFamily": "ipv4",
       "virtualGatewayId": "",
       "virtualInterfaceId": "dxvif-fgh0hcrk",
       "authKey": "asdf34example",
       "routeFilterPrefixes": [
           {
               "cidr": "203.0.113.0/30"
           },
           {
               "cidr": "203.0.113.4/30"
           }
       ],
       "location": "Example location",
       "bgpPeers": [
           {
               "bgpStatus": "down", 
               "customerAddress": "203.0.113.2/30", 
               "addressFamily": "ipv4", 
               "authKey": "asdf34example", 
               "bgpPeerState": "verifying", 
               "amazonAddress": "203.0.113.1/30", 
               "asn": 65000
           }
       ],
       "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fgh0hcrk\">\n  <vlan>2000</vlan>\n  <customer_address>203.0.113.2/30</customer_address>\n  <amazon_address>203.0.113.1/30</amazon_address>\n  <bgp_asn>65000</bgp_asn>\n  <bgp_auth_key>asdf34example</bgp_auth_key>\n  <amazon_bgp_asn>7224</amazon_bgp_asn>\n  <connection_type>public</connection_type>\n</logical_connection>\n",
       "amazonAddress": "203.0.113.1/30",
       "virtualInterfaceType": "public",
       "virtualInterfaceName": "PublicVirtualInterface"
   }
   ```

   To create a public virtual interface that supports IPv6 traffic, you can specify IPv6 routes that you will advertise over BGP. You cannot specify IPv6 addresses for the peering session; Amazon allocates IPv6 addresses to you. The following example creates a public virtual interface for IPv6 traffic.

   ```
   aws directconnect create-public-virtual-interface --connection-id {{dxcon-fg31dyv6}} --new-public-virtual-interface virtualInterfaceName={{PublicVirtualInterface}},vlan={{2000}},asn={{65000}},addressFamily=ipv6,routeFilterPrefixes=[{cidr={{2001:db8:64ce:ba00::/64}}},{cidr={{2001:db8:64ce:ba01::/64}}}]
   ```

1. To view the router configuration information in XML format, describe the virtual interface you created. Use the `--query` parameter to extract the `customerRouterConfig` information, and the `--output` parameter to organize the text into tab-delimited lines.

   ```
   aws directconnect describe-virtual-interfaces --virtual-interface-id {{dxvif-fgh0hcrk}} --query virtualInterfaces[*].customerRouterConfig --output text
   ```

    

   ```
   <?xml version="1.0" encoding="UTF-8"?>
   <logical_connection id="dxvif-fgh0hcrk">
     <vlan>2000</vlan>
     <customer_address>203.0.113.2/30</customer_address>
     <amazon_address>203.0.113.1/30</amazon_address>
     <bgp_asn>65000</bgp_asn>
     <bgp_auth_key>asdf34example</bgp_auth_key>
     <amazon_bgp_asn>7224</amazon_bgp_asn>
     <connection_type>public</connection_type>
   </logical_connection>
   ```

# Log Direct Connect API calls using AWS CloudTrail
<a name="logging_dc_api_calls"></a>

Direct Connect is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Direct Connect. CloudTrail captures all API calls for Direct Connect as events. The calls captured include calls from the Direct Connect console and code calls to the Direct Connect API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Direct Connect. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Direct Connect, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Direct Connect information in CloudTrail
<a name="direct-connect-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Direct Connect, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for Direct Connect, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Direct Connect actions are logged by CloudTrail and are documented in the [Direct Connect API Reference](https://docs.aws.amazon.com/directconnect/latest/APIReference/). For example, calls to the `CreateConnection` and `CreatePrivateVirtualInterface` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management (IAM user) credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail `userIdentity` Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understand Direct Connect log file entries
<a name="understanding-direct-connect-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following are example CloudTrail log records for Direct Connect.

**Example: CreateConnection**  

```
{
    "Records": [
    {
        "eventVersion": "1.0",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:user/Alice",
            "accountId": "123456789012",
            "accessKeyId": "EXAMPLE_KEY_ID",
            "userName": "Alice",
            "sessionContext": {
                "attributes": {
                    "mfaAuthenticated": "false",
                    "creationDate": "2014-04-04T12:23:05Z"
                }
            }
        },
        "eventTime": "2014-04-04T17:28:16Z",
        "eventSource": "directconnect.amazonaws.com",
        "eventName": "CreateConnection",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "127.0.0.1",
        "userAgent": "Coral/Jakarta",
        "requestParameters": {
            "location": "EqSE2",
            "connectionName": "MyExampleConnection",
            "bandwidth": "1Gbps"
        },
        "responseElements": {
            "location": "EqSE2",
            "region": "us-west-2",
            "connectionState": "requested",
            "bandwidth": "1Gbps",
            "ownerAccount": "123456789012",
            "connectionId": "dxcon-fhajolyy",
            "connectionName": "MyExampleConnection"
        }
    },
    ...
  ]
}
```

**Example: CreatePrivateVirtualInterface**  

```
{
    "Records": [
    {
        "eventVersion": "1.0",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:user/Alice",
            "accountId": "123456789012",
            "accessKeyId": "EXAMPLE_KEY_ID",
            "userName": "Alice",
            "sessionContext": {
                "attributes": {
                    "mfaAuthenticated": "false",
                    "creationDate": "2014-04-04T12:23:05Z"
                }
            }
        },
        "eventTime": "2014-04-04T17:39:55Z",
        "eventSource": "directconnect.amazonaws.com",
        "eventName": "CreatePrivateVirtualInterface",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "127.0.0.1",
        "userAgent": "Coral/Jakarta",
        "requestParameters": {
            "connectionId": "dxcon-fhajolyy",
            "newPrivateVirtualInterface": {
                "virtualInterfaceName": "MyVirtualInterface",
                "customerAddress": "[PROTECTED]",
                "authKey": "[PROTECTED]",
                "asn": -1,
                "virtualGatewayId": "vgw-bb09d4a5",
                "amazonAddress": "[PROTECTED]",
                "vlan": 123
            }
        },
        "responseElements": {
            "virtualInterfaceId": "dxvif-fgq61m6w",
            "authKey": "[PROTECTED]",
            "virtualGatewayId": "vgw-bb09d4a5",
            "customerRouterConfig": "[PROTECTED]",
            "virtualInterfaceType": "private",
            "asn": -1,
            "routeFilterPrefixes": [],
            "virtualInterfaceName": "MyVirtualInterface",
            "virtualInterfaceState": "pending",
            "customerAddress": "[PROTECTED]",
            "vlan": 123,
            "ownerAccount": "123456789012",
            "amazonAddress": "[PROTECTED]",
            "connectionId": "dxcon-fhajolyy",
            "location": "EqSE2"
        }
    },
    ...
  ]
}
```

**Example: DescribeConnections**  

```
{
    "Records": [
    {
        "eventVersion": "1.0",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:user/Alice",
            "accountId": "123456789012",
            "accessKeyId": "EXAMPLE_KEY_ID",
            "userName": "Alice",
            "sessionContext": {
                "attributes": {
                    "mfaAuthenticated": "false",
                    "creationDate": "2014-04-04T12:23:05Z"
                }
            }
        },
        "eventTime": "2014-04-04T17:27:28Z",
        "eventSource": "directconnect.amazonaws.com",
        "eventName": "DescribeConnections",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "127.0.0.1",
        "userAgent": "Coral/Jakarta",
        "requestParameters": null,
        "responseElements": null
    },
    ...
  ]
}
```

**Example: DescribeVirtualInterfaces**  

```
{
    "Records": [
    {
        "eventVersion": "1.0",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:user/Alice",
            "accountId": "123456789012",
            "accessKeyId": "EXAMPLE_KEY_ID",
            "userName": "Alice",
            "sessionContext": {
                "attributes": {
                    "mfaAuthenticated": "false",
                    "creationDate": "2014-04-04T12:23:05Z"
                }
            }
        },
        "eventTime": "2014-04-04T17:37:53Z",
        "eventSource": "directconnect.amazonaws.com",
        "eventName": "DescribeVirtualInterfaces",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "127.0.0.1",
        "userAgent": "Coral/Jakarta",
        "requestParameters": {
            "connectionId": "dxcon-fhajolyy"
        },
        "responseElements": null
    },
    ...
  ]
}
```

# Direct Connect operational event notifications
<a name="dx-operational-notifications"></a>

Direct Connect continuously monitors your connections for operational events that may affect your connectivity. When Direct Connect detects an operational event, it sends notifications through [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) to inform you of the event.

Direct Connect monitors for packet loss in the following connectivity segments:
+ **To your Region** – Packet loss on the path between your Direct Connect location and its associated AWS Region.
+ **Between Regions** – Packet loss on the inter-Region path when you use a [Direct Connect gateway](#direct-connect-gateways) to route traffic across AWS Regions.

Direct Connect targets sending an initial notification to the affected account within the following timeframes:


| Connectivity segment | Target notification time | 
| --- | --- | 
| To your Region | Within 5 minutes of detection | 
| Between Regions | Within 15 minutes of detection | 

**Note**  
Notification timing begins when the packet loss event is detected by Direct Connect monitoring systems. Some events may require additional time for detection, scope assessment, and notification delivery.

## What to expect in a notification
<a name="operational-notifications-content"></a>

When Direct Connect detects packet loss affecting your connections, you receive notifications through AWS Health in the following sequence:

1. **Initial notification** – Indicates that Direct Connect has detected packet loss affecting your connection(s). Includes the impacted Direct Connect location and the start time of the event.

1. **Update notifications** – Indicates that the previously reported event is still ongoing.

1. **Resolution notification** – Indicates that the event has been resolved and connectivity has been restored.

Each notification includes the Direct Connect location where the event was detected, the start time of the event, and the current status (open, update, or resolved).

## Recommended actions
<a name="operational-notifications-actions"></a>

When you receive an operational event notification, take the following actions:
+ **Verify your traffic** – Check whether your applications are experiencing connectivity issues consistent with the notification.
+ **Monitor your CloudWatch metrics** – Review your [CloudWatch metrics for Direct Connect](#monitoring-cloudwatch) to assess impact. `ConnectionState` indicates whether your connection is up, `ConnectionBpsEgress` and `ConnectionBpsIngress` show throughput changes, and `ConnectionPpsEgress` and `ConnectionPpsIngress` show packet rate changes that may indicate loss.
+ **Check Network Synthetic Monitor** – If you have configured [Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html), review your packet loss and latency metrics for additional context. Direct Connect operational event notifications and Network Synthetic Monitor metrics may not always correlate.
+ **Rely on redundant connections** – If you have configured your deployment for [Maximum resiliency](#maximum_resiliency), traffic should automatically route to healthy connections during an event.

If you are monitoring for packet loss on your Direct Connect connections and do not receive an AWS Health notification within the expected timeframe, the packet loss may be occurring outside of the AWS network. Check your on-premises router, cross-connect, or contact your colocation provider or network service provider for further investigation. If the issue persists after troubleshooting with those parties, contact [AWS Support](https://console.aws.amazon.com/support/) for additional assistance.

## Integrating with AWS Health
<a name="operational-notifications-health-integration"></a>

To receive and act on Direct Connect operational event notifications, you can use the following AWS Health features:
+ **Health Dashboard** – View active and recent events in the [Health Dashboard](https://health.aws.amazon.com/health/home) in the AWS Management Console.
+ **Amazon EventBridge** – Create rules to route AWS Health events to targets such as Amazon SNS topics, Lambda functions, or other AWS services for automated alerting or remediation. For more information, see [Monitoring AWS Health events with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html).
+ **AWS Health API** – Programmatically query for events affecting your resources. For more information, see the [AWS Health API Reference](https://docs.aws.amazon.com/health/latest/APIReference/).

Direct Connect operational event notifications are generated for packet loss events detected within AWS network infrastructure and apply to dedicated and hosted connections that are part of the Direct Connect service. Events occurring on partner networks, colocation provider infrastructure, or customer on-premises equipment are not covered by these notifications.

## Related resources
<a name="operational-notifications-related"></a>
+ [Direct Connect maintenance](#dx-maintenance)
+ [Monitoring and visibility with Direct Connect](#monitoring-overview)
+ [AWS Direct Connect Resiliency Toolkit](#resiliency_toolkit)
+ [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)

# Monitoring and visibility with Direct Connect
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of your Direct Connect resources. You should collect monitoring data from all of the parts of your AWS solution so that you can more easily debug a multi-point failure if one occurs. Before you start monitoring Direct Connect; however, you should create a monitoring plan that includes answers to the following questions:
+ What are your monitoring goals?
+ What resources should be monitored?
+ How often should you monitor these resources?
+ What monitoring tools can you use?
+ Who performs the monitoring tasks?
+ Who should be notified when something goes wrong?

The next step is to establish a baseline for normal Direct Connect performance in your environment, by measuring performance at various times and under different load conditions. As you monitor Direct Connect, store historical monitoring data. That way, you can compare it with current performance data, identify normal performance patterns and performance anomalies, and devise methods to address issues.

To establish a baseline, you should monitor the usage, state, and health of your physical Direct Connect connections.

**Topics**
+ [Monitoring tools](#monitoring-automated-manual)
+ [Monitor with Amazon CloudWatch](#monitoring-cloudwatch)
+ [BGP route visibility](#bgp-route-visibility)

## Monitoring tools
<a name="monitoring-automated-manual"></a>

AWS provides various tools that you can use to monitor a Direct Connect connection. You can configure some of these tools to do the monitoring for you, while some of the tools require manual intervention. We recommend that you automate monitoring tasks as much as possible.

### Automated monitoring tools
<a name="monitoring-automated_tools"></a>

You can use the following automated monitoring tools to watch Direct Connect and report when something is wrong:
+ **Amazon CloudWatch Alarms** – Watch a single metric over a time period that you specify. Perform one or more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon SNS topic. CloudWatch alarms do not invoke actions simply because they are in a particular state; the state must have changed and been maintained for a specified number of periods. For information about available metrics and dimensions, see [Monitor with Amazon CloudWatch](#monitoring-cloudwatch).
+ **AWS CloudTrail Log Monitoring** – Share log files between accounts and monitor CloudTrail log files in real time by sending them to CloudWatch Logs. You can also write log processing applications in Java and validate that your log files have not changed after delivery by CloudTrail. For more information, see [Log API calls](#logging_dc_api_calls) and [Working with CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.html) in the *AWS CloudTrail User Guide*.

### Manual monitoring tools
<a name="monitoring-manual-tools"></a>

Another important part of monitoring a Direct Connect connection involves manually monitoring those items that the CloudWatch alarms don't cover. The Direct Connect and CloudWatch console dashboards provide an at-a-glance view of the state of your AWS environment. 
+ The Direct Connect console shows:
  + Connection status (see the **State** column)
  + Virtual interface status (see the **State** column)
+ The CloudWatch home page shows:
  + Current alarms and status
  + Graphs of alarms and resources
  + Service health status

  In addition, you can use CloudWatch to do the following: 
  + Create [customized dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.html) to monitor the services you care about.
  + Graph metric data to troubleshoot issues and discover trends.
  + Search and browse all your AWS resource metrics.
  + Create and edit alarms to be notified of problems.

## Monitor with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor physical Direct Connect connections, and virtual interfaces, using CloudWatch. CloudWatch collects raw data from Direct Connect, and processes it into readable metrics. By default, CloudWatch provides Direct Connect metric data in 5-minute intervals. The metric data in every interval is an aggregation of at least two samples collected during that interval. 

For detailed information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). You can also monitor your services CloudWatch to see what ones are using resources. For more information, see [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html).

**Topics**
+ [Direct Connect metrics and dimensions](#metrics-dimensions)
+ [View Direct Connect CloudWatch metrics](#viewing-metrics)
+ [Create alarms to monitor connections](#creating-alarms)

### Direct Connect metrics and dimensions
<a name="metrics-dimensions"></a>

Metrics are available for Direct Connect physical connections, and virtual interfaces.

#### Direct Connect Connection metrics
<a name="connection-metrics-dimensions"></a>

The following metrics are available from Direct Connect dedicated connections. 


| Metric | Description | 
| --- | --- | 
| `ConnectionState` | The state of the connection.1 indicates **up** and 0 indicates **down**.<br />This metric is available for dedicated and hosted connections.This metric is also available in hosted virtual interface owner accounts in addition to connection owner accounts.<br />Units: There are no units returned for this metric. | 
| `ConnectionBpsEgress` | The bitrate for outbound data from the AWS side of the connection.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Bits per second | 
| `ConnectionBpsIngress` | The bitrate for inbound data to the AWS side of the connection.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Bits per second | 
| `ConnectionPpsEgress` | ` The packet rate for outbound data from the AWS side of the connection.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Packets per second | 
| `ConnectionPpsIngress` | The packet rate for inbound data to the AWS side of the connection.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Packets per second | 
| `ConnectionCRCErrorCount` | This count is no longer in use. Use `ConnectionErrorCount` instead. | 
| `ConnectionErrorCount` | The total error count for all types of MAC level errors recorded by the AWS device. The total includes cyclic redundancy check (CRC) errors. The root cause of these errors can be on either the customer side or the AWS side.<br />This metric is the error count that occurred since the last reported datapoint. When there are errors on the interface, the metric reports non-zero values. To get the total count of all errors for the selected interval in CloudWatch, for example, 5 minutes, apply the "sum" statistic. <br />The metric value is set to 0 when the errors on the interface stop. This metric replaces `ConnectionCRCErrorCount`, which is no longer in use. <br />Units: Count | 
| ConnectionLightLevelTx | Indicates the health of the fiber connection for outbound (egress) traffic from the AWS side of the connection.<br />There are two dimensions for this metric. For more information, see [Direct Connect available dimensions](#metrics-available-dimensions).<br />Units: dBm | 
| `ConnectionLightLevelRx` | Indicates the health of the fiber connection for inbound (ingress) traffic to the AWS side of the connection.<br />There are two dimensions for this metric. For more information, see [Direct Connect available dimensions](#metrics-available-dimensions).<br />Units: dBm | 
| ConnectionEncryptionState | Indicates the connection encryption status. 1 indicates the connection encryption is `up`, and 0 indicates the connection encryption is `down`. When this metric is applied to a LAG, 1 indicates that all connections in the LAG have encryption `up`. 0 indicates at least one LAG connection encryption is `down`. | 
| ConnectionDiscardsPpsEgress | The packet discard rate for outbound data from the AWS side of the connection. This metric tracks packets that are dropped due to buffer overflows, interface congestion, or other network conditions.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />Units: Packets per second | 

#### Direct Connect virtual interface metrics
<a name="virtual-interfaces-metrics-dimensions"></a>

The following metrics are available from Direct Connect virtual interfaces. 


| Metric | Description | 
| --- | --- | 
| `VirtualInterfaceBpsEgress` | The bitrate for outbound data from the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Bits per second | 
| `VirtualInterfaceBpsIngress` | The bitrate for inbound data to the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Bits per second | 
| `VirtualInterfacePpsEgress` | The packet rate for outbound data from the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Packets per second | 
| `VirtualInterfacePpsIngress` | The packet rate for inbound data to the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Packets per second | 
| `VirtualInterfaceBgpStatus` | The state of the BGP peering session for the virtual interface. 1 indicates **up** and 0 indicates **down**.<br />Units: There are no units returned for this metric. | 
| `VirtualInterfaceBgpPrefixesAccepted` | The number of BGP prefixes accepted from the BGP peer on the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Count | 
| `VirtualInterfaceBgpPrefixesAdvertised` | The number of BGP prefixes advertised to the BGP peer on the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Count | 

#### Direct Connect available dimensions
<a name="metrics-available-dimensions"></a>

You can filter the Direct Connect data using the following dimensions.


| Dimension | Description | 
| --- | --- | 
| `ConnectionId` | This dimension is available on the metrics for Direct Connect connection, and virtual interface. This dimension filters the data by the connection. | 
| OpticalLaneNumber | This dimension filters the ConnectionLightLevelTx data and the ConnectionLightLevelRx data, and filters the data by the optical lane number of the Direct Connect connection. | 
| VirtualInterfaceId | This dimension is available on the metrics for Direct Connect virtual interface, and filters the data by the virtual interface. | 
| IpAddressFamily | This dimension is available on the BGP metrics for Direct Connect virtual interfaces (VirtualInterfaceBgpStatus, VirtualInterfaceBgpPrefixesAccepted, VirtualInterfaceBgpPrefixesAdvertised). This dimension filters the data by IP address family. Valid values are ipv4 and ipv6. | 

**Topics**
+ [Direct Connect metrics and dimensions](#metrics-dimensions)
+ [View Direct Connect CloudWatch metrics](#viewing-metrics)
+ [Create alarms to monitor connections](#creating-alarms)

### View Direct Connect CloudWatch metrics
<a name="viewing-metrics"></a>

Direct Connect sends the following metrics about your Direct Connect connections. Amazon CloudWatch then aggregates these data points to 1-minute or 5-minute intervals. By default, Direct Connect metric data is written to CloudWatch at 5-minute intervals. 

**Note**  
When monitoring Direct Connect through CloudWatch, you can request metrics at 1-minute intervals. However, the actual update frequency is controlled by CloudWatch. Because CloudWatch controls the interval, Direct Connect can't always guarantee intervals shorter than five minutes.

You can use the following procedures to view the metrics for Direct Connect connections.

**To view metrics using the CloudWatch console**

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace. For more information about using Amazon CloudWatch to view Direct Connect metrics, including adding math functions or prebuilt queries, see [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working-with-metrics.html) in the *Amazon CloudWatch User Guide*. 

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**, and then choose **All metrics**.

1. In the **Metrics** section, choose **DX**. 

1. Choose a **ConnectionId** or **Metric name**, and then choose any of the following to further define the metric:
   + **Add to search** — Adds this metric to your search results.
   + **Search for this only** — Searches only for this metric.
   + **Remove from graph** — Removes this metric from the graph.
   + **Graph this metric only** — Graphs only this metric.
   + **Graph all search results** — Graphs all metrics.
   + **Graph with SQL query** — Opens **Metric Insights -query builder**, allowing you to choose what you want to graph by creating an SQL query. For more information on using Metric Insights, see [Query your metrics with CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) in the *Amazon CloudWatch User Guide*. 

**To view metrics using the Direct Connect console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select your connection. 

1. Choose the **Monitoring** tab to display the metrics for your connection.

**To view metrics using the AWS CLI**  
At a command prompt, use the following command.

```
aws cloudwatch list-metrics --namespace "AWS/DX"
```

### Create Amazon CloudWatch alarms to monitor Direct Connect connections
<a name="creating-alarms"></a>

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An alarm watches a single metric over a time period that you specify. It sends a notification to an Amazon SNS topic based on the value of the metric relative to a given threshold over a number of time periods. 

For example, you can create an alarm that monitors the state of a Direct Connect connection. It sends a notification when the connection state is **down** for five consecutive 1-minute periods. For details on what to know for creating an alarm and for more information on creating an alarm, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*. 

**To create a CloudWatch alarm.**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, and then choose **All alarms**.

1. Choose **Create Alarm**.

1. Choose **Select metric**, and then choose **DX** .

1. Choose the **Connection Metrics** metric.

1. Select the Direct Connect connection, and then choose the **Select metric** metric.

1. On the** Specify metric and conditions** page, configure the parameters for the alarm. For more specifying metrics and conditions, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

1. Choose **Next**.

1. Configure the alarm actions on the **Configure actions** page. For more information on configuring alarm actions, see [Alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions) in the *Amazon CloudWatch User Guide*.

1. Choose **Next**. 

1. On the **Add name and description** page, enter a **Name** and an optional **Alarm description** to describe this alarm, and then choose **Next**.

1. Verify the proposed alarm on the **Preview and create** page. 

1. If needed choose **Edit** to change any information, and then choose **Create alarm**.

   The **Alarms** page displays a new row with information about the new alarm. The **Actions** status displays **Actions enabled**, indicating that the alarm is active.

## BGP route visibility
<a name="bgp-route-visibility"></a>

With Direct Connect, you can view the BGP routes on your virtual interfaces (VIFs). You can see which routes AWS accepted from your router. You can also see which routes AWS is sending to your router. Each route shows its AS path and community values.

View routes in the Direct Connect console, or use the `ListVirtualInterfaceRoutes` API action. For more information about the API, see [ListVirtualInterfaceRoutes](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceRoutes.html) in the *Direct Connect API Reference*.

### BGP route visibility concepts
<a name="bgp-route-visibility-concepts"></a>

Accepted routes and advertised routes  
Each route has a direction:  
+ *Accepted routes* – Routes that AWS received from your router. AWS keeps these routes after it applies inbound routing policy.
+ *Advertised routes* – Routes that AWS sends to your router over the VIF.

Route age  
Each route includes the time that AWS received or advertised it on the virtual interface. The console shows this as the route age. In the API and AWS CLI response, the value is an epoch-seconds timestamp; to find the route age, subtract this value from the current time.

Communities  
Routes show their BGP community values in `ASN:value` format. AWS shows only the supported Direct Connect communities and hides all other (internal) community values. The supported communities are:  
+ *Scope communities* (advertised to your router): `7224:9100`, `7224:9200`, and `7224:9300`.
+ *Region and continent communities* (accepted from your router): `7224:8100` and `7224:8200`.
+ *Local preference communities* (accepted from your router): `7224:7100`, `7224:7200`, and `7224:7300`.
The communities that appear depend on the VIF type and route direction. For more information about these communities and how AWS uses them, see [Routing policies and BGP communities](#routing-and-bgp).

### View BGP routes
<a name="bgp-route-visibility-console"></a>

The Direct Connect console shows BGP route data on the virtual interface detail page. Choose the **Accepted routes** or **Advertised routes** tab to see routes.

Each route tab shows a table with the following columns:
+ Prefix/Network
+ Address family
+ AS path
+ Communities
+ Route age

You can filter routes by prefix, AS path, community, or address family.

------
#### [ Console ]

**To view BGP routes for a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface.

1. Choose the **Accepted routes** or **Advertised routes** tab to view the corresponding routes.

------
#### [ Command line ]

Use the [list-virtual-interface-routes](https://docs.aws.amazon.com/cli/latest/reference/directconnect/list-virtual-interface-routes.html) command. Use the `routeDirection` filter to return accepted or advertised routes. The following example returns the routes that AWS accepted from your router on the specified virtual interface.

```
aws directconnect list-virtual-interface-routes \
    --virtual-interface-id {{dxvif-abc12345}} \
    --filters '{"routeDirection": "accepted"}'
```

You can also filter the results by address family (`addressFamily`), prefix (`cidrs`), AS path (`asPath`), or community (`communities`).

------

# Direct Connect quotas
<a name="limits"></a>

The following table lists the quotas related to Direct Connect.


| Component | Quota | Comments | 
| --- | --- | --- | 
| Private or public virtual interfaces per Direct Connect dedicated connection | 50 | This limit cannot be increased. | 
| Transit virtual interfaces per Direct Connect dedicated connection.Transit virtual interfaces can be used to connect to an Transit Gateway or an AWS Cloud WAN core network. For more information, see [Direct Connect gateways](#direct-connect-gateways). | 4 | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Private or public virtual interfaces per Direct Connect dedicated connection and transit virtual interfaces per Direct Connect dedicated connection | 51 | When AWS Direct Connect support for Amazon VPC Transit Gateways was launched, a quota of one (1) transit virtual interface was added to the quota of 50 private or public virtual interfaces per dedicated connection. The number of transit virtual interfaces allowed is now four (4) and is counted against the maximum of 51 virtual interfaces per dedicated connection. This limit cannot be increased. | 
| Private, public, or transit virtual interfaces per Direct Connect hosted connection | 1 | This limit cannot be increased. | 
| Active Direct Connect connections per Direct Connect location per Region per account | 10 | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Number of virtual interfaces per Link Aggregation Group (LAG) | 51 | When AWS Direct Connect support for Amazon VPC Transit Gateways was launched, a quota of one (1) transit virtual interface was added to the quota of 50 private or public virtual interfaces per LAG. The number of transit virtual interfaces allowed is now four (4) and is counted against the maximum of 51 virtual interfaces per LAG. This limit cannot be increased. | 
| Rate Limiters per Dedicated connection | 10 | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Routes per Border Gateway Protocol (BGP) session on a private virtual interface or transit virtual interface from on-premises to AWS.<br />If you advertise more route prefixes than your configured allocations for IPv4 and IPv6 over the BGP session, the BGP session will go into an idle state and be reported with BGP session status DOWN. | Default of 100 each for IPv4 and IPv6. Can be increased [using prefix controls](#prefix-controls) up to 1,000 each for IPv4 and IPv6. | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Routes per Border Gateway Protocol (BGP) session on a public virtual interface | 1,000 | This limit cannot be increased. | 
| Dedicated connections per link aggregation group (LAG) | 4 when the port speed is less than 100G 2 when the port speed is 100G |  | 
| Link aggregation groups (LAGs) per Region | 10 | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Direct Connect gateways per account | 200 | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Virtual private gateways per Direct Connect gateway | 20 | This limit cannot be increased. | 
| Transit Gateways per Direct Connect gateway  | 6 | This limit cannot be increased. | 
| Maximum number of advertised route prefixes from an AWS Cloud WAN core network Direct Connect gateway attachment to on-premises. All transit virtual interfaces attached to that Direct Connect gateway will receive all route prefixes advertised by the core network.  | 5,000 | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Virtual interfaces (private or transit) per Direct Connect gateway | 30 | This limit cannot be increased. | 
| Number of prefixes per AWS Transit Gateway from AWS to on-premise on a transit virtual interface | 200 combined total for IPv4 and IPv6 | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 
| Number of virtual interfaces per virtual private gateway | There is no limit. |  | 
| Number of Direct Connect gateways associated to a Transit Gateway | 20 | This limit cannot be increased. | 
| SiteLink prefix limit | Up to 1,000 each for IPv4 and IPv6, configured on your private or transit virtual interface [using prefix controls](#prefix-controls). | Contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance. | 

Direct Connect supports these port speeds over single-mode fiber: 1 Gbps: 1000BASE-LX (1310 nm), 10 Gbps: 10GBASE-LR (1310 nm) , 100Gbps: 100GBASE-LR4, and 400 Gbps: 400GBASE-LR4.

## Load balance considerations
<a name="load-balance-considerations"></a>

If you want to use load balancing with multiple public VIFs, all the VIFs must be in the same Region.

# Troubleshoot Direct Connect
<a name="Troubleshooting"></a>

The following troubleshooting information can help you diagnose and fix issues with your Direct Connect connection.

**Contents**
+ [Layer 1 (physical) issues](#ts_layer_1)
+ [Layer 2 (data link) issues](#ts-layer-2)
+ [Layer 3/4 (Network/Transport) issues](#ts-layer-3)
+ [BGP TTL security (GTSM)](#ts-ttl-security)
+ [Long ASN issues](#ts-long-asn)
+ [Routing issues](#ts-routing)

## Troubleshoot layer 1 (physical) issues
<a name="ts_layer_1"></a>

If you or your network provider are having difficulty establishing physical connectivity to a Direct Connect device, use the following steps to troubleshoot the issue.

1. Verify with the colocation provider that the cross connect is complete. Ask them or your network provider to provide you with a cross connect completion notice and compare the ports with those listed on your LOA-CFA.

1. Verify that your router or your provider's router is powered on and that the ports are activated.

1. Ensure that the routers are using the correct optical transceiver. Auto-negotiation for the port must be disabled if you have a connection with a port speed more than 1 Gbps. However, depending on the AWS Direct Connect endpoint serving your connection, auto-negotiation might need to be enabled or disabled for 1 Gbps connections. If auto-negotation needs to be disabled for your connections, port speed and full-duplex mode must be configured manually. If your virtual interface remains down, see [Troubleshoot layer 2 (data link) issues](#ts-layer-2). Depending on the Direct Connect endpoint serving your connection terminates, auto-negotiation might need to be enabled or disabled accordingly.

1. Verify that the router is receiving an acceptable optical signal over the cross connect.

1. Try flipping (also known as rolling) the Tx/Rx fiber strands.

1. Check the Amazon CloudWatch metrics for Direct Connect. You can verify the Direct Connect device's Tx/Rx optical readings (both 1 Gbps and 10 Gbps), physical error count, and operational status. For more information, see [Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html).

1. Contact the colocation provider and request a written report for the Tx/Rx optical signal across the cross connect.

1. If the above steps do not resolve physical connectivity issues, [contact AWS Support](https://aws.amazon.com/support/createCase) and provide the cross connect completion notice and optical signal report from the colocation provider.

The following flow chart contains the steps to diagnose issues with the physical connection.

![Troubleshoot Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/layer1-ts.png)


## Troubleshoot layer 2 (data link) issues
<a name="ts-layer-2"></a>

If your Direct Connect physical connection is up but your virtual interface is down, use the following steps to troubleshoot the issue.

1. If you cannot ping the Amazon peer IP address, verify that your peer IP address is configured correctly and in the correct VLAN. Ensure that the IP address is configured in the VLAN subinterface and not the physical interface (for example, GigabitEthernet0/0.123 instead of GigabitEthernet0/0). 

1. Verify if the router has a MAC address entry from the AWS endpoint in your address resolution protocol (ARP) table.

1. Ensure that any intermediate devices between endpoints have VLAN trunking enabled for your 802.1Q VLAN tag. ARP cannot be established on the AWS side until AWS receives tagged traffic.

1. Clear your or your provider's ARP table cache.

1. If the above steps do not establish ARP or you still cannot ping the Amazon peer IP, [contact AWS Support](https://aws.amazon.com/support/createCase).

The following flow chart contains the steps to diagnose issues with the data link.

![Troubleshoot Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/troubleshooting-chart-layer-2.png)


If the BGP session is still not established after verifying these steps, see [Troubleshoot layer 3/4 (Network/Transport) issues](#ts-layer-3). If the BGP session is established but you are experiencing routing issues, see [Troubleshoot routing issues](#ts-routing).

## Troubleshoot layer 3/4 (Network/Transport) issues
<a name="ts-layer-3"></a>

Consider a situation where your Direct Connect physical connection is up and you can ping the Amazon peer IP address. If your virtual interface is up and the BGP peering session cannot be established, use the following steps to troubleshoot the issue:

1. Ensure that your BGP local Autonomous System Number (ASN) and Amazon's ASN are configured correctly.

1. Ensure that the peer IPs for both sides of the BGP peering session are configured correctly.

1. Ensure that your MD5 authentication key is configured and exactly matches the key in the downloaded router configuration file. Check that there are no extra spaces or characters.

1. Verify that you or your provider are not advertising more than 100 prefixes for private virtual interfaces or 1,000 prefixes for public virtual interfaces. These are hard limits and cannot be exceeded.

1. Ensure that there are no firewall or ACL rules that are blocking TCP port 179 or any high-numbered ephemeral TCP ports. These ports are necessary for BGP to establish a TCP connection between the peers.

1. Check your BGP logs for any errors or warning messages.

1. If the above steps do not establish the BGP peering session, [contact AWS Support](https://aws.amazon.com/support/createCase).

The following flow chart contains the steps to diagnose issues with the BGP peering session.

![Troubleshoot Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/troubleshooting-chart-layer-3-4.png)


If the BGP peering session is established but you are experiencing routing issues, see [Troubleshoot routing issues](#ts-routing).

## Troubleshoot BGP TTL security (GTSM) issues
<a name="ts-ttl-security"></a>

If your BGP session with Direct Connect fails to establish, BGP TTL security on your router might be the cause. Direct Connect uses single-hop external BGP (eBGP) on virtual interfaces and sends BGP packets with an IP Time-to-Live (TTL) value of 1. Some routers support BGP TTL security, also known as the Generalized TTL Security Mechanism (GTSM). For more information about GTSM, see [RFC 5082](https://datatracker.ietf.org/doc/html/rfc5082) on the Internet Engineering Task Force (IETF) website. When this feature is enabled (for example, with the `neighbor ttl-security hops` command), your router expects incoming BGP packets to arrive with a high TTL value. Your router discards the low-TTL packets that AWS sends.

**BGP session remains in the Active or OpenSent state**  
*Symptoms*: The BGP session does not establish and remains in the Active or OpenSent state. This occurs even though a packet capture on your device shows the AWS BGP packets arriving on the interface.  
*Cause*: BGP TTL security is configured on the BGP neighbor facing Direct Connect, causing your router to discard the BGP packets that AWS sends with a TTL of 1.  
*Resolution*:  

1. Remove the TTL security (GTSM) configuration from the BGP neighbor facing Direct Connect.

1. Verify that the BGP session state transitions to Established.
Direct Connect uses single-hop eBGP and does not support multihop eBGP on virtual interfaces by default. The single-hop protection that GTSM provides is already inherent in this peering.

**Note**  
Use this guidance for the BGP session on a Direct Connect virtual interface. BGP peering to a Transit Gateway over a transit virtual interface uses multihop BGP and is configured differently.

If the BGP session does not establish after you remove the TTL security configuration, [contact AWS Support](https://aws.amazon.com/support/createCase).

## Troubleshoot long ASN issues
<a name="ts-long-asn"></a>

If you are experiencing issues with long ASN configurations, use the following steps to troubleshoot:

**BGP session fails with a long ASN**  
*Symptoms*: BGP session cannot establish after configuring a long ASN  
*Cause*: On-premises router may not support long ASN capability  
*Resolution*:  
+ Verify your router supports RFC 6793
+ Check BGP configuration for consistent ASN format
+ Review BGP logs for capability negotiation errors

**API responses show ASN as 0**  
*Symptoms*: API responses display `asn` field as 0  
*Cause*: This is expected behavior when actual ASN exceeds 2,147,483,647  
*Resolution*: Use the `asnLong` field in API responses for the correct ASN value

**Migration from ASN to long ASN issues**  
*Symptoms*: Connectivity loss during ASN migration  
*Cause*: BGP session re-establishment required for ASN changes  
*Resolution*:  
+ Plan migration during maintenance windows
+ Update one virtual interface at a time
+ Monitor BGP session status during changes
+ Verify routing table convergence after migration

If you continue to experience issues with long ASN configurations after following these troubleshooting steps, [contact AWS Support](https://aws.amazon.com/support/createCase) with the following information:
+ Virtual interface ID or BGP peer ID
+ Configured ASN values (both ASN and long ASN)
+ Router model and software version
+ BGP configuration and logs
+ Error messages or symptoms observed

## Troubleshoot routing issues
<a name="ts-routing"></a>

Consider a situation where your virtual interface is up and you've established a BGP peering session. If you cannot route traffic over the virtual interface, use the following steps to troubleshoot the issue:

1. Ensure that you are advertising a route for your on-premises network prefix over the BGP session. For a private virtual interface, this can be a private or public network prefix. For a public virtual interface, this must be your publicly routable network prefix.

1. For a private virtual interface, ensure that your VPC security groups and network ACLs allow inbound and outbound traffic for your on-premises network prefix. For more information, see [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) and [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html) in the *Amazon VPC User Guide*.

1. For a private virtual interface, ensure that your VPC route tables have prefixes pointing to the virtual private gateway to which your private virtual interface is connected. For example, if you prefer to have all your traffic routed towards your on-premises network by default, you can add the default route (0.0.0.0/0 or ::/0) with the virtual private gateway as the target in your VPC route tables.
   + Alternatively, enable route propagation to automatically update routes in your route tables based on your dynamic BGP route advertisement. You can have up to 100 propagated routes per route table. This limit cannot be increased. For more information, see [Enabling and Disabling Route Propagation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#EnableDisableRouteProp) in the *Amazon VPC User Guide*.

1. If the above steps do not resolve your routing issues, [contact AWS Support](https://aws.amazon.com/support/createCase).

The following flow chart contains the steps to diagnose routing issues.

![Troubleshoot Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/troubleshooting-chart-routing.png)


# Document history
<a name="AboutThisGuide"></a>

The following table describes the releases for AWS Direct Connect. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Flat-rate billing for dedicated connections](#AboutThisGuide) | Direct Connect now supports flat-rate billing, a fixed-price billing mode for dedicated connections that you set per connection. For more information, see [Flat-rate billing for dedicated connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/flat-rate-connections.html). | September 15, 2026 | 
| [BGP route visibility](#AboutThisGuide) | You can now view the BGP routes that AWS has accepted from your router and the routes that AWS is advertising to you on your Direct Connect virtual interfaces. For more information, see [BGP route visibility](https://docs.aws.amazon.com/directconnect/latest/UserGuide/bgp-route-visibility.html). | July 30, 2026 | 
| [GDS No. 3 Data Center, Shenzhen end of support](#AboutThisGuide) | The GDS No. 3 Data Center, Shenzhen location is no longer accepting new connections after June 30, 2026. End of support July 2027. | June 30, 2026 | 
| [Support for long ASN](#AboutThisGuide) | You can now use long ASN values for BGP sessions with Direct Connect virtual interfaces. | July 24, 2025 | 
| [Create an association between Direct Connect gateway and an AWS Network Manager core network](#AboutThisGuide) | You can now create a Direct Connect gateway association directly between Direct Connect and an AWS Cloud WAN core network. | November 25, 2024 | 
| [Support for 400G](#AboutThisGuide) | Updated topics to include support for 400G connections. | July 18, 2024 | 
| [Added a SiteLink prefix limit](#AboutThisGuide) | A prefix limit for SiteLink was added to the quotas and limits topic. | June 15, 2023 | 
| [Support for SiteLink](#AboutThisGuide) | You can create a private virtual interface that enables connectivity between two Direct Connect points of presence (PoPs) in the same AWS Region. | December 1, 2021 | 
| [Support MAC Security](#AboutThisGuide) | You can use Direct Connect connections that support MACsec to encrypt your data from your corporate data center to the Direct Connect location. | March 31, 2021 | 
| [Support for 100G](#AboutThisGuide) | Updated topics to include support for 100G dedicated connections. | February 12, 2021 | 
| [New location in Italy](#AboutThisGuide) | Updated topic to include the addition of the new location in Italy. | January 22, 2021 | 
| [New location in Israel](#AboutThisGuide) | Updated topic to include the addition of the new location in Israel. | July 7, 2020 | 
| [Resiliency Toolkit Failover Testing support](#AboutThisGuide) | Use the Resiliency Toolkit Failover Testing feature to test the resiliency of your connections. | June 3, 2020 | 
| [CloudWatch VIF metric support](#AboutThisGuide) | You can monitor physical Direct Connect connections, and virtual interfaces, using CloudWatch. | May 11, 2020 | 
| [AWS Direct Connect Resiliency Toolkit](#AboutThisGuide) | The AWS Direct Connect Resiliency Toolkit provides a connection wizard with multiple resiliency models that helps you order dedicated connections to achieve your SLA objective. | October 7, 2019 | 
| [Additional Region support for Support for AWS Transit Gateway across accounts](#AboutThisGuide) | Additional Region support for AWS Transit Gateway across accounts. | September 30, 2019 | 
| [AWS Direct Connect support for AWS Transit Gateway](#AboutThisGuide) | You can use a Direct Connect gateway to connect your Direct Connect connection over a transit virtual interface to the VPCs or VPNs attached to your Transit Gateway. You associate a Direct Connect gateway with the Transit Gateway. Then, create a transit virtual interface for your Direct Connect connection to the Direct Connect gateway. | March 27, 2019 | 
| [Jumbo frames support](#AboutThisGuide) | You can send jumbo frames (9001 MTU) over Direct Connect. | October 11, 2018 | 
| [Local preference BGP communities](#AboutThisGuide) | You can use local preference BGP community tags to achieve load balancing and route preference for incoming traffic to your network. | February 6, 2018 | 
| [Direct Connect gateway](#AboutThisGuide) | You can use a Direct Connect gateway to connect your Direct Connect connection to VPCs in remote Regions. | November 1, 2017 | 
| [Amazon CloudWatch metrics](#AboutThisGuide) | You can view CloudWatch metrics for your Direct Connect connections. | June 29, 2017 | 
| [Link aggregation groups](#AboutThisGuide) | You can create a link aggregation group (LAG) to aggregate multiple Direct Connect connections. | February 13, 2017 | 
| [IPv6 support](#AboutThisGuide) | Your virtual interface can now support an IPv6 BGP peering session. | December 1, 2016 | 
| [Tagging support](#AboutThisGuide) | You can now tag your Direct Connect resources. | November 4, 2016 | 
| [Self-service LOA-CFA](#AboutThisGuide) | You can now download your Letter of Authorization and Connecting Facility Assignment (LOA-CFA) using the Direct Connect console or API. | June 22, 2016 | 
| [New location in Silicon Valley](#AboutThisGuide) | Updated topic to include the addition of the new Silicon Valley location in the US West (N. California) Region. | June 3, 2016 | 
| [New location in Amsterdam](#AboutThisGuide) | Updated topic to include the addition of the new Amsterdam location in the Europe (Frankfurt) Region. | May 19, 2016 | 
| [New locations in Portland, Oregon, and Singapore](#AboutThisGuide) | Updated topic to include the addition of the new Portland, Oregon, and Singapore locations in the US West (Oregon) and Asia Pacific (Singapore) Regions. | April 27, 2016 | 
| [New location in Sao Paulo, Brasil](#AboutThisGuide) | Updated topic to include the addition of the new Sao Paulo location in the South America (São Paulo) Region. | December 9, 2015 | 
| [New locations in Dallas, London, Silicon Valley, and Mumbai](#AboutThisGuide) | Updated topics to include the addition of the new locations in Dallas (US East (N. Virginia) Region), London (Europe (Ireland) Region), Silicon Valley (AWS GovCloud (US-West) Region), and Mumbai (Asia Pacific (Singapore) Region). | November 27, 2015 | 
| [New location in the China (Beijing) Region](#AboutThisGuide) | Updated topics to include the addition of the new Beijing location in the China (Beijing) Region. | April 14, 2015 | 
| [New Las Vegas location in the US West (Oregon) Region](#AboutThisGuide) | Updated topics to include the addition of the new Direct Connect Las Vegas location in the US West (Oregon) Region. | November 10, 2014 | 
| [New EU (Frankfurt) Region](#AboutThisGuide) | Updated topics to include the addition of the new Direct Connect locations serving the EU (Frankfurt) Region. | October 23, 2014 | 
| [New locations in the Asia Pacific (Sydney) Region](#AboutThisGuide) | Updated topics to include the addition of the new Direct Connect locations serving the Asia Pacific (Sydney) Region. | July 14, 2014 | 
| [Support for AWS CloudTrail](#AboutThisGuide) | Added a new topic to explain how you can use CloudTrail to log activity in Direct Connect. | April 4, 2014 | 
| [Support for accessing remote AWS Regions](#AboutThisGuide) | Added a new topic to explain how you can access public resources in a remote Region. | December 19, 2013 | 
| [Support for hosted connections](#AboutThisGuide) | Updated topics to include support for hosted connections. | October 22, 2013 | 
| [New location in the EU (Ireland) Region](#AboutThisGuide) | Updated topics to include the addition of the new Direct Connect location serving the EU (Ireland) Region. | June 24, 2013 | 
| [New Seattle location in the US West (Oregon) Region](#AboutThisGuide) | Updated topics to include the addition of the new Direct Connect location in Seattle serving the US West (Oregon) Region. | May 8, 2013 | 
| [Support for using IAM with Direct Connect](#AboutThisGuide) | Added a topic about using AWS Identity and Access Management with Direct Connect. | December 21, 2012 | 
| [New Asia Pacific (Sydney) Region](#AboutThisGuide) | Updated topics to include the addition of the new Direct Connect location serving the Asia Pacific (Sydney) Region. | December 14, 2012 | 
| [New AWS Direct Connect console, and the US East (N. Virginia) and South America (Sao Paulo) Regions](#AboutThisGuide) | Replaced the Direct Connect Getting Started Guide with the Direct Connect User Guide. Added new topics to cover the new Direct Connect console, added a billing topic, added router configuration information, and updated topics to include the addition of two new Direct Connect locations serving the US East (N. Virginia) and South America (Sao Paulo) Regions. | August 13, 2012 | 
| [Support for the EU (Ireland), Asia Pacific (Singapore), and Asia Pacific (Tokyo) Regions](#AboutThisGuide) | Added a new troubleshooting section and updated topics to include the addition of four new Direct Connect locations serving the US West (Northern California), EU (Ireland), Asia Pacific (Singapore), and Asia Pacific (Tokyo) Regions. | January 10, 2012 | 
| [Support for the US West (Northern California) Region](#AboutThisGuide) | Updated topics to include the addition of the US West (Northern California) Region. | September 8, 2011 | 
| [Public release](#AboutThisGuide) | The first release of Direct Connect. | August 3, 2011 | 