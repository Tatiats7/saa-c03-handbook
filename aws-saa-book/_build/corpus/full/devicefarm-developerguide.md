# AWS Device Farm Developer Guide

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
+ [What is AWS Device Farm?](#welcome)
+ [Setting up AWS Device Farm](#setting-up)
+ [Getting started with Device Farm](#getting-started)
+ [Purchasing a device slot in Device Farm](#how-to-purchase-device-slots)
   + [Cancelling a device slot in Device Farm](#how-to-cancel-device-slots)
+ [AWS Device Farm concepts](#concepts)
   + [Device support in AWS Device Farm](#devices)
   + [Test environments in AWS Device Farm](#test-environments)
   + [Runs in AWS Device Farm](#test-runs)
   + [Apps in AWS Device Farm](#apps)
   + [Reports in AWS Device Farm](#reports)
   + [Sessions in AWS Device Farm](#sessions)
+ [Projects in AWS Device Farm](#projects)
   + [Creating a project in AWS Device Farm](#how-to-create-project)
   + [Viewing the projects list in AWS Device Farm](#how-to-view-projects-list)
+ [Test runs in AWS Device Farm](#runs)
   + [Creating a test run in Device Farm](#how-to-create-test-run)
   + [Setting the execution timeout for test runs in AWS Device Farm](#how-to-set-default-timeout-for-test-runs)
   + [Simulating network connections and conditions for your AWS Device Farm runs](#how-to-simulate-network-connections-and-conditions)
   + [Stopping a run in AWS Device Farm](#how-to-stop-test-runs)
   + [Viewing a list of runs in AWS Device Farm](#how-to-view-runs-list)
   + [Creating a device pool in AWS Device Farm](#how-to-create-device-pool)
   + [Analyzing test results in AWS Device Farm](#analyzing-results)
      + [Viewing test reports in Device Farm](#how-to-use-reports)
         + [Device Farm test result statuses](#how-to-use-reports-displaying-results)
      + [Downloading artifacts in Device Farm](#artifacts)
         + [Downloading artifacts in a custom test environment](#using-artifacts-custom)
+ [Tagging AWS Device Farm resources](#tagging)
+ [Test frameworks and built-in tests in AWS Device Farm](#test-types)
   + [Automatically run Appium tests in Device Farm](#test-types-appium)
      + [Integrating Appium tests with Device Farm](#test-types-appium-integrate)
   + [Android tests in AWS Device Farm](#test-types-android-tests)
      + [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation)
         + [Integrating Android Instrumentation with Device Farm](#test-types-android-instrumentation-integrate)
   + [iOS tests in AWS Device Farm](#test-types-ios-tests)
      + [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest)
      + [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui)
   + [Web app tests in AWS Device Farm](#test-types-web-app-tests)
   + [Built-in tests in AWS Device Farm](#test-types-built-in-tests)
      + [Running Device Farm's built-in fuzz test (Android and iOS)](#test-types-built-in-fuzz)
+ [Custom test environments in AWS Device Farm](#custom-test-environments)
   + [Test spec reference and syntax](#custom-test-environment-test-spec)
   + [Hosts for custom test environments](#custom-test-environments-hosts)
      + [Supported software within custom test environments](#custom-test-environments-hosts-software)
         + [Using the devicefarm-cli tool in custom test environments](#custom-test-environments-hosts-software-cli)
      + [Test environment for Android devices](#custom-test-environments-hosts-android)
         + [Supported IP ranges for the Amazon Linux 2 test environment in Device Farm](#amazon-linux-2-ip-ranges)
      + [Test environment for iOS devices](#custom-test-environments-hosts-ios)
         + [Migrating your custom test environments to the new iOS test hosts](#ios-host-migration)
   + [Access AWS resources using an IAM Execution Role](#custom-test-environments-iam-roles)
   + [Environment variables for custom test environments](#custom-test-environment-variables)
   + [Best practices for custom test environment execution](#custom-test-environments-best-practices)
   + [Migrating tests from a standard to custom test environment](#custom-test-environment-migration)
   + [Extending custom test environments in Device Farm](#custom-test-environments-extending)
      + [Setting a device PIN when running tests in Device Farm](#custom-test-environments-extending-set-pin)
      + [Speeding up Appium-based tests in Device Farm through desired capabilities](#custom-test-environments-extending-speed)
      + [Using Webhooks and other APIs after your tests run in Device Farm](#custom-test-environments-extending-webhooks)
      + [Adding extra files to your test package in Device Farm](#custom-test-environments-extending-files)
+ [Remote access in AWS Device Farm](#remote-access)
   + [Creating a remote access session in AWS Device Farm](#how-to-create-session)
   + [Using a remote access session in AWS Device Farm](#how-to-use-session)
   + [Retrieving the results of a remote access session in AWS Device Farm](#how-to-access-session-results)
+ [Appium testing in AWS Device Farm](#appium-endpoint)
   + [Getting started with Appium testing](#appium-endpoint-getting-started)
   + [Interacting with the device using Appium](#appium-endpoint-interaction)
   + [Reviewing your Appium server logs](#appium-endpoint-server-logs)
   + [Supported features and versions](#appium-endpoint-support)
+ [Private devices in AWS Device Farm](#working-with-private-devices)
   + [Creating an instance profile in AWS Device Farm](#set-up-private-devices-account-settings)
   + [Request additional private devices in AWS Device Farm](#managing-private-device-instance)
   + [Creating a test run or starting a remote access session in AWS Device Farm](#create-test-run-using-private-devices)
   + [Selecting private devices in a device pool in AWS Device Farm](#selecting-private-devices)
   + [Skipping app re-signing on private devices in AWS Device Farm](#skip-app-re-signing-on-private-devices)
   + [Amazon VPC across AWS Regions in AWS Device Farm](#amazon-vpc-cross-region)
   + [Terminating private devices in Device Farm](#terminate-private-device)
+ [VPC-ENI in AWS Device Farm](#vpc-eni)
   + [AWS access control and IAM](#vpc-eni-access-control)
   + [Service-linked roles](#vpc-eni-service-linked-role)
   + [Prerequisites](#vpc-eni-prerequisites)
   + [Connecting to Amazon VPC](#connecting-to-amazon-vpc)
   + [Limits](#vpc-eni-limits)
   + [Using Amazon VPC endpoint services with Device Farm - Legacy (not recommended)](#amazon-vpc-endpoints)
+ [Logging AWS Device Farm API calls with AWS CloudTrail](#logging-using-cloudtrail)
+ [Integrating AWS Device Farm in a CodePipeline test stage](#codepipeline)
+ [AWS CLI reference for AWS Device Farm](#cli-ref)
+ [Windows PowerShell reference for AWS Device Farm](#powershell-ref)
+ [Automating AWS Device Farm](#api-ref)
+ [Troubleshooting Device Farm errors](#troubleshooting)
   + [Troubleshooting Android application tests in AWS Device Farm](#troubleshooting-android-applications)
   + [Troubleshooting Appium Java JUnit tests in AWS Device Farm](#troubleshooting-appium-java-junit)
   + [Troubleshooting Appium Java JUnit web application tests in AWS Device Farm](#troubleshooting-appium-web-java-junit-tests)
   + [Troubleshooting Appium Java TestNG tests in AWS Device Farm](#troubleshooting-appium-java-testng)
   + [Troubleshooting Appium Java TestNG web applications in AWS Device Farm](#troubleshooting-appium-web-java-testng)
   + [Troubleshooting Appium Python tests in AWS Device Farm](#troubleshooting-appium-python)
   + [Troubleshooting Appium Python web application tests in AWS Device Farm](#troubleshooting-appium-web-python)
   + [Troubleshooting instrumentation tests in AWS Device Farm](#troubleshooting-instrumentation-tests)
   + [Troubleshooting iOS application tests in AWS Device Farm](#troubleshooting-ios-applications)
   + [Troubleshooting XCTest tests in AWS Device Farm](#troubleshooting-xctest)
   + [Troubleshooting XCTest UI tests in AWS Device Farm](#troubleshooting-xctest-ui)
+ [Security in AWS Device Farm](#security)
   + [Identity and access management in AWS Device Farm](#security-iam)
      + [How AWS Device Farm works with IAM](#security_iam_service-with-iam)
      + [AWS Device Farm identity-based policy examples](#security_iam_id-based-policy-examples)
      + [Troubleshooting AWS Device Farm identity and access](#security_iam_troubleshoot)
   + [Compliance validation for AWS Device Farm](#ATP-compliance)
   + [Data protection in AWS Device Farm](#data-protection)
   + [Resilience in AWS Device Farm](#disaster-recovery-resiliency)
   + [Infrastructure security in AWS Device Farm](#infrastructure-security)
   + [Configuration vulnerability analysis and management in Device Farm](#security-vulnerability-analysis-and-management)
   + [Incident response in Device Farm](#security-incident-response)
   + [Logging and monitoring in Device Farm](#security-logging-monitoring)
   + [Security best practices for Device Farm](#security-best-practices)
+ [Limits in AWS Device Farm](#limits)
+ [Tools and plugins for AWS Device Farm](#aws-device-farm-tools-plugins)
   + [Integrating Device Farm with a Jenkins CI server](#continuous-integration-jenkins-plugin)
   + [Integrating Device Farm with a Gradle build system](#aws-device-farm-android-gradle-plugin)
+ [AWS Device Farm document history](#history)
+ [AWS Glossary](#glossary)

-----



# What is AWS Device Farm?
<a name="welcome"></a>

Device Farm is an app testing service that you can use to test and interact with your Android, iOS, and web apps on real, physical phones and tablets that are hosted by Amazon Web Services (AWS).

There are two main ways to use Device Farm:
+ Remotely access a device from your local computer, either interactively in your web browser or automatically testing it using Appium from a local client.
+ Automatically execute app tests using Device Farm's managed test execution environment.

**Note**  
Device Farm is only available in the `us-west-2` (Oregon) region.

## Remote access
<a name="remote-access-intro"></a>

Remote access allows you to interact with a device through your web browser in real time. Remote access also lets you to run Appium tests from your local client against remote Device Farm devices using a managed Appium endpoint.

Real-time interaction with a device can be useful for a number of scenarios, such as manual app testing, reproducing bugs on a specific device, checking the visual rendering of your app on different screen types, and app install and upgrade sequences. Device Farm's fully managed Appium endpoint enables you to develop, test, and debug your Appium tests, giving fast feedback.

The Appium endpoint supports any language of your choice, any local IDE, live debugging with breakpoints, live video and logs, and tools like [Appium Inspector](https://github.com/appium/appium-inspector). You can execute tests as many times as you like on the same device during your remote access session with a [150-minute limit](#service-limits).

During a remote access session, Device Farm logs details about actions that take place as you interact with the device. Logs with these details and a video capture of the session are produced at the end of the session.

## Automated app testing
<a name="automated-test-intro"></a>

Device Farm allows you to run automated tests on multiple devices in parallel by uploading your app and tests. The tests are automatically executed in a fully managed environment on test hosts that you can configure [a test spec file](#custom-test-environment-test-spec). The environment uses Device Farm's [test hosts](#custom-test-environments-hosts), so you don't need to worry about provisioning your own infrastructure for running tests. The test hosts and devices can securely connect to your VPC to access your private endpoints.

As tests are completed, a test report is generated that contains high-level results, low-level logs, screenshots, and your test artifacts.

Device Farm supports testing of native and hybrid Android and iOS apps. For more information about supported test types, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

## Terminology
<a name="welcome-terminology"></a>

Device Farm introduces the following terms that define the way information is organized:

**device pool**  
A collection of devices that typically share similar characteristics, such as platform, manufacturer, or model.

**job**  
A request for Device Farm to test a single app against a single device. A job contains one or more suites.

**metering**  
Refers to billing for devices. You might see references to metered devices or unmetered devices in the documentation and API reference. For more information about pricing, see [AWS Device Farm Pricing](https://aws.amazon.com/device-farm/pricing/).

**project**  
A logical workspace that contains runs, one run for each test of a single app against one or more devices. You can use projects to organize workspaces in whatever way you choose. For example, you can have one project per app title or one project per platform. You can create as many projects as you need.

**report**  
Contains information about a run, which is a request for Device Farm to test a single app against one or more devices. For more information, see [Reports in AWS Device Farm](#reports).

**run**  
A specific build of your app, with a specific set of tests, to be run on a specific set of devices. A run produces a report of the results. A run contains one or more jobs. For more information, see [Runs](#test-runs).

**session**  
A real-time interaction with an actual, physical device through your web browser. For more information, see [Sessions](#sessions).

**suite**  
The hierarchical organization of tests in a test package. A suite contains one or more tests.

**test**  
An individual test case in a test package.

For more information about Device Farm, see [Concepts](#concepts).

## Setting up
<a name="welcome-setting-up"></a>

To use Device Farm, see [Setting up](#setting-up).

# Setting up AWS Device Farm
<a name="setting-up"></a>

Before you use Device Farm for the first time, you must complete the following tasks:

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Step 3: Give the IAM user permission to access Device Farm](#setting-up-permissions)
+ [Next step](#setting-up-next-step)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Step 3: Give the IAM user permission to access Device Farm
<a name="setting-up-permissions"></a>

Give the IAM user permission to access Device Farm. To do this, create an access policy in IAM, and then assign the access policy to the IAM user, as follows.

**Note**  
The AWS root account or IAM user that you use to complete the following steps must have permission to create the following IAM policy and attach it to the IAM user. For more information, see [Working with Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies_manage.html).

1. Create a policy with the following JSON body. Give it a descriptive title, such as {{DeviceFarmAdmin}}.

   For more information on creating IAM policies, see [Creating IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the IAM User Guide.

1. Attach the IAM policy you created to your new user. For more information on attaching IAM policies to users, see [Adding and Removing IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the IAM User Guide. 

Attaching the policy provides the IAM user with access to all Device Farm actions and resources associated with that IAM user. For information about how to restrict IAM users to a limited set of Device Farm actions and resources, see [Identity and access management in AWS Device Farm](#security-iam).

## Next step
<a name="setting-up-next-step"></a>

You are now ready to start using Device Farm. See [Getting started with Device Farm](#getting-started).

# Getting started with Device Farm
<a name="getting-started"></a>

This walkthrough shows you how to use Device Farm to test a native Android or iOS app. You use the Device Farm console to create a project, upload an .apk or .ipa file, run a suite of standard tests, and then view the results.

**Note**  
Device Farm is available only in the `us-west-2` (Oregon) AWS Region.

**Topics**
+ [Prerequisites](#getting-started-prepare)
+ [Step 1: Sign in to the console](#getting-started-console)
+ [Step 2: Create a project](#getting-started-create-project)
+ [Step 3: Create and start a run](#getting-started-create-run)
+ [Step 4: View the run's results](#getting-started-view-run-results)
+ [Next steps](#getting-started-next-steps)

## Prerequisites
<a name="getting-started-prepare"></a>

Before you begin, make sure you have completed the following requirements:
+ Complete the steps in [Setting up](#setting-up). You need an AWS account and an AWS Identity and Access Management (IAM) user with permission to access Device Farm.
+ For Android, you can bring an .apk (Android app package) file, or use the sample application we provide. For iOS, you need an .ipa (iOS app archive) file. You upload the file to Device Farm later in this walkthrough.
**Note**  
Make sure that your .ipa file is built for an iOS device and not for a simulator.
+ (Optional) You need a test from one of the testing frameworks that Device Farm supports. You upload this test package to Device Farm, and then run the test later in this walkthrough. If you don't have a test package available, you can specify and run a standard built-in test suite. For more information, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

## Step 1: Sign in to the console
<a name="getting-started-console"></a>

You can use the Device Farm console to create and manage projects and runs for testing. You learn about projects and runs later in this walkthrough.
+ Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

## Step 2: Create a project
<a name="getting-started-create-project"></a>

To test an app in Device Farm, you must first create a project.

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Under **Mobile Device Testing Projects**, choose **Create project**.

1. Under **Create project**, enter a **Project Name** (for example, **MyDemoProject**).

1. Choose **Create**.

   The console opens the **Automated tests** page of your newly created project.

## Step 3: Create and start a run
<a name="getting-started-create-run"></a>

Now that you have a project, you can create and then start a run. For more information, see [Runs](#test-runs).

1. On the **Automated tests** tab, choose **Create run**. Alternatively, you can follow the in-console tutorial by selecting **Create run with tutorial**.

1. Under **Select app and run type**, in the **Run type** section, select your run type. Select **Android app** if you do not have an app ready for testing, or if you are testing an android (.apk) app. Select **iOS app** if you are testing an iOS (.ipa) app.

1. Under **Select app**, in the **App selection options** section, choose **Select sample app provided by Device Farm** if you do not have an app available for testing. If you are bringing your own app, select **Upload own app**, and choose your application file. If you're uploading an iOS app, be sure to choose **iOS device**, as opposed to a simulator.

1. Under **Configure test**, in the **Select test framework** section, choose one of the testing frameworks or built-in test suites. For information about each option, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).
   + If you have not yet packaged your tests for Device Farm, choose **Built-in: Fuzz** to run a standard, built-in test suite. You can keep the default values for **Event count**, **Event throttle**, and **Randomizer seed**. For more information, see [Running Device Farm's built-in fuzz test (Android and iOS)](#test-types-built-in-fuzz).
   + If you have a test package from one of the supported testing frameworks, choose the corresponding testing framework, and then upload the file that contains your tests.

1. Under **Select devices**, choose **Use Device Pool** and **Top Devices**.

1. (Optional) To add additional configuration, open the **Additional configuration** dropdown. In this section, you can do any of the following:
   + To provide other data for Device Farm to use during the run, next to **Add extra data**, choose **Choose File**, and then browse to and choose the .zip file that contains the data.
   + To install an additional app for Device Farm to use during the run, next to **Install other apps**, choose **Choose File**, and then browse to and choose the .apk or .ipa file that contains the app. Repeat this for other apps you want to install. You can change the installation order by dragging and dropping the apps after you upload them. 
   + To specify whether Wi-Fi, Bluetooth, GPS, or NFC is enabled during the run, next to **Set radio states**, select the appropriate boxes.
   + To preset the device latitude and longitude for the run, next to **Device location**, enter the coordinates.
   + To preset the device locale for the run, in **Device locale**, choose the locale.
   + Select **Enable video recording** to record video during testing.
**Note**  
Setting the device radio state and locale are options only available for Android native tests at this time.
**Note**  
If you have private devices, configuration specific to private devices is also displayed.

1. (Optional) To configure run-level properties, update the **Run Settings** section. Here you can do the following:
   + Assign your run with a custom **Run name**. If no name is provided, the Device Farm console will name your run 'My Device Farm run' by default.
   + Choose **Generate test report** under **Test Insights** to get a detailed structured test report for each job and an aggregated summary at the run level. This insight is generated in addition to any test report that you might generate as part of your test execution.
   + Assign a **Job timeout**, which is the maximum number of minutes a job can run on a device. If your tests are complete before the job timeout, the job completes, and you are not charged for the remainder of the job timeout. The default is 150 minutes.
   + Choose a **Billing method**. By default, if you do not have slots purchased on your account, the Device Farm console selects Metered. If you have slots, the console defaults to Unmetered.

1. At the bottom of the page, choose **Confirm and start run** to schedule the run.

Device Farm starts the run as soon as devices are available, typically within a few minutes. To view the run status, on the **Automated tests** page of your project, choose the name of your run. One the run page, under **Devices**, each device starts with the pending icon ![Device Farm scheduled a job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-calendar.png) in the device table, then switches to the running icon ![Device Farm progress indicator.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-progress.png) when the test begins. As each test finishes, the console displays a test result icon next to the device name. When all tests are complete, the pending icon next to the run changes to a test result icon.

## Step 4: View the run's results
<a name="getting-started-view-run-results"></a>

To view test results from the run, on the **Automated tests** page of your project, choose the name of your run. A summary page displays:
+ The total number of tests, by outcome.
+ Lists of tests with unique warnings or failures.
+ A list of devices with test results for each.
+ Any screenshots captured during the run, grouped by device.
+ A section to download the parsing result.

For more information, see [Viewing test reports in Device Farm](#how-to-use-reports).

## Next steps
<a name="getting-started-next-steps"></a>

For more information about Device Farm, see [Concepts](#concepts).

# Purchasing a device slot in Device Farm
<a name="how-to-purchase-device-slots"></a>

Device farm has two billing methods for testing on public mobile devices: metered and unmetered. With metered billing, you pay-as-you-go based on device minutes. To learn more about metered, pay-as-you-go pricing, visit here: [https://aws.amazon.com/device-farm/pricing/](https://aws.amazon.com/device-farm/pricing/). With unmetered billing, you reserve device concurrency through Device slots, which are billed at a flat monthly rate. This page covers unmetered, device slot billing.

Device slots correspond to your concurrency in Device Farm, determining how many test jobs (devices) or remote access sessions you can run simultaneously with unmetered billing. Device slots are specific to testing type (automated testing or remote access) and device platform (android or ios). Slots are not tied to any specific device make or model. You can use the Device Farm console, AWS Command Line Interface (AWS CLI), or Device Farm API to purchase device slots.

## Purchase device slots
<a name="how-to-purchase-device-slots-methods"></a>

------
#### [ Console ]

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Device slots**.

1. On the **Device slots** page, you can choose the number of **Automated testing** and **Remote access** device slots per platform that you want to purchase. Specify slot amounts in the **Desired slots** column.

   As you change the slot amount, the text dynamically updates with the billing amount. For more information, see [AWS Device Farm pricing](https://aws.amazon.com/device-farm/pricing/).
**Important**  
If you change the number of device slots but see a **contact us** or **contact us to purchase** message, your AWS account is not yet approved to purchase the number of device slots that you requested.  
These options prompt you to send an email to the Device Farm support team. In the email, specify the number of each device type that you want to purchase and for which billing cycle.
**Note**  
Changes to the device slots apply to your entire account and affect all projects.  
![Device slots page on the Device Farm console](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-console-device-slots-default-view.png)

1. Choose **Purchase**. A **Confirm purchase** window will appear. Review the information. When you are ready, type **confirm** and then choose **Confirm** to complete the transaction.

![Purchase confirmation page on the Device Farm console](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-console-device-slots-purchase-confirm.png)


On the **Device slots** page, you can see the number of device slots that you currently have, as well as the number of device slots you will have for your next billing period.

------
#### [ AWS CLI ]

You can run the **purchase-offering** command to purchase the offering.

To list your Device Farm account settings, including the maximum number of device slots that you can purchase and the number of remaining free trial minutes, run the **get-account-settings** command. You'll see output similar to the following:

```
{
    "accountSettings": {
        "maxSlots": {
            "{{GUID}}": 1,
            "{{GUID}}": 1,
            "{{GUID}}": 1,
            "{{GUID}}": 1
        },
        "unmeteredRemoteAccessDevices": {
            "ANDROID": 0,
            "IOS": 0
        },
        "maxJobTimeoutMinutes": 150,
        "trialMinutes": {
            "total": 1000.0,
            "remaining": 954.1
        },
        "defaultJobTimeoutMinutes": 150,
        "awsAccountNumber": "{{AWS-ACCOUNT-NUMBER}}",
        "unmeteredDevices": {
            "ANDROID": 0,
            "IOS": 0
        }
    }
}
```

To list the device slot offerings that are available to you, run the **list-offerings** command. You should see output similar to the following:

```
{
    "offerings": [
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "IOS",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "iOS Unmetered Device Slot"
        },
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "ANDROID",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "Android Unmetered Device Slot"
        },
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "ANDROID",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "Android Remote Access Unmetered Device Slot"
        },
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "IOS",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "iOS Remote Access Unmetered Device Slot"
        }
    ]
}
```

To list the available offering promotions, run the **list-offering-promotions** command.

**Note**  
This command returns only promotions that you haven't yet purchased. As soon as you purchase one or more slots across any offering using a promotion, that promotion no longer appears in the results.

You should see output similar to the following:

```
{
    "offeringPromotions": [
        {
            "id": "2FREEMONTHS",
            "description": "New device slot customers get 3 months for the price of 1."
        }
    ]
}
```

To get the offering status, run the **get-offering-status** command. You should see output similar to the following: 

```
{
    "current": {
        "{{GUID}}": {
            "offering": {
                "platform": "IOS",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "iOS Unmetered Device Slot"
            },
            "quantity": 1
        },
        "{{GUID}}": {
            "offering": {
                "platform": "ANDROID",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "Android Unmetered Device Slot"
            },
            "quantity": 1
        }
    },
    "nextPeriod": {
        "{{GUID}}": {
            "effectiveOn": 1459468800.0,
            "offering": {
                "platform": "IOS",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "iOS Unmetered Device Slot"
            },
            "quantity": 1
        },
        "{{GUID}}": {
            "effectiveOn": 1459468800.0,
            "offering": {
                "platform": "ANDROID",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "Android Unmetered Device Slot"
            },
            "quantity": 1
        }
    }
}
```

The **renew-offering** and **list-offering-transactions** commands are also available for this feature. For more information, see the [AWS CLI reference](#cli-ref).

------
#### [ API ]

1. Call the [GetAccountSettings](../../latest/APIReference/API_GetAccountSettings.html) operation to list your account settings.

1. Call the [ListOfferings](../../latest/APIReference/API_ListOfferings.html) operation to list the device slot offerings available to you.

1. Call the [ListOfferingPromotions](../../latest/APIReference/API_ListOfferingPromotions.html) operation to list the offering promotions that are available.
**Note**  
This operation returns only promotions that you haven't yet purchased. As soon as you purchase one or more slots using an offering promotion, that promotion no longer appears in the results.

1. Call the [PurchaseOffering](../../latest/APIReference/API_PurchaseOffering.html) operation to purchase an offering.

1. Call the [GetOfferingStatus](../../latest/APIReference/API_GetOfferingStatus.html) operation to get the offering status.

The [RenewOffering](../../latest/APIReference/API_RenewOffering.html) and [ListOfferingTransactions](../../latest/APIReference/API_ListOfferingTransactions.html) operations are also available for this feature.

For information about using the Device Farm API, see [Automating Device Farm](#api-ref).

------

## Cancelling a device slot in Device Farm
<a name="how-to-cancel-device-slots"></a>

You can cancel the number of device slots for both automated testing and remote access. The amount charged to your account for the next billing cycle will be listed underneath the billing period field..

For more information about device slots, see [Purchasing a device slot in Device Farm](#how-to-purchase-device-slots).

------
#### [ Console ]

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Device slots**.

1. On the **Device slots** page, you can decrease the number of device slots to your desired amount by inputting the value into the **Desired slots** field corresponding to the device slot type you wish to modify. The amount charged to your account for the next billing cycle will be listed underneath **Next billing period cost**.

1. Choose **Save**. A **Confirm Change** window will appear. Review the information. When you are ready, type **confirm** and then choose **Confirm** to complete the transaction.

------
#### [ AWS CLI ]

You can run the **renew-offering** command to change the amount of devices for the next billing cycle.

------
#### [ API ]

Call the [RenewOffering](../../latest/APIReference/API_RenewOffering.html) operation to change the quantity of devices in your account.

------

# AWS Device Farm concepts
<a name="concepts"></a>

Device Farm is an app testing service that you can use to test and interact with your Android, iOS, and web apps on real, physical phones and tablets that are hosted by Amazon Web Services (AWS).

This section describes important Device Farm concepts.
+ [Device support in AWS Device Farm](#devices)
+ [Test environments in AWS Device Farm](#test-environments)
+ [Runs](#test-runs)
+ [Apps](#apps)
+ [Reports in AWS Device Farm](#reports)
+ [Sessions](#sessions)

For more information about supported test types in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

## Device support in AWS Device Farm
<a name="devices"></a>

The following sections provide information about device support in Device Farm.

**Topics**
+ [Supported devices](#devices-supported)
+ [Device pools](#devices-pools)
+ [Private devices](#devices-private)
+ [Device branding](#devices-branding)
+ [Device slots](#device-slots)
+ [Preinstalled device apps](#devices-apps)
+ [Device capabilities](#devices-capabilities)

### Supported devices
<a name="devices-supported"></a>

Device Farm provides support for hundreds of unique, popular Android and iOS devices and operating system combinations. The list of available devices grows as new devices enter the market. For the full list of devices, see the [interactive device list in your AWS console](https://us-west-2.console.aws.amazon.com/devicefarm/home?region=us-west-2#/mobile/publicdevices).

### Device pools
<a name="devices-pools"></a>

Device Farm organizes its devices into device pools that you can use for your testing. These device pools contain related devices, such as devices that run only on Android or only on iOS. Device Farm provides curated device pools, such as those for top devices. You can also create device pools that mix public and private devices.

### Private devices
<a name="devices-private"></a>

Private devices allow you to specify exact hardware and software configurations for your testing needs. Certain configurations, such as rooted Android devices, can be supported as private devices. Each private device is a physical device that Device Farm deploys on your behalf in an Amazon data center. Your private devices are available exclusively to you for both automated and manual testing. After you choose to end your subscription, the hardware is removed from our environment. For more information, see [Private Devices](https://aws.amazon.com/device-farm/pricing/#privateDevices) and [Private devices in AWS Device Farm](#working-with-private-devices).

### Device branding
<a name="devices-branding"></a>

Device Farm runs tests on physical mobile and tablet devices from a variety of OEMs.

### Device slots
<a name="device-slots"></a>

Device slots correspond to concurrency in which the number of device slots you have purchased determines how many devices you can run in tests or remote access sessions. 

There are two types of device slots:
+ A *remote access device slot* is one you can run in remote access sessions concurrently.

  If you have one remote access device slot, you can only run one remote access session at a time. If you purchase additional remote testing device slots, you can run multiple sessions concurrently.
+ An *automated testing device slot* is one on which you can run tests concurrently.

  If you have one automated testing device slot, you can only run tests on one device at a time. If you purchase additional automated testing device slots, you can run multiple tests concurrently, on multiple devices, to get test results faster.

 You can purchase device slots based on the device family (Android or iOS devices for automated testing and Android or iOS devices for remote access). For more information, see [Device Farm Pricing](https://aws.amazon.com/device-farm/pricing/).

### Preinstalled device apps
<a name="devices-apps"></a>

Devices in Device Farm include a small number of apps that are already installed by manufacturers and carriers.

### Device capabilities
<a name="devices-capabilities"></a>

All devices have internet connectivity. They do not have carrier connections and cannot make phone calls or send SMS messages.

You can take photos with any device that supports a front- or rear-facing camera. Due to the way the devices are mounted, photos might look dark and blurry.

Google Play Services and Google Chrome are installed on Android devices.

## Test environments in AWS Device Farm
<a name="test-environments"></a>

AWS Device Farm provides both custom and standard test environments for running your automated tests. You can choose a custom test environment for complete control over your automated tests. Or, you can choose the Device Farm default standard test environment, which offers granular reporting of each test in your automated test suite.

**Topics**
+ [Standard test environment](#test-environments-standard)
+ [Custom test environment](#custom-test-environment)

### Standard test environment
<a name="test-environments-standard"></a>

 When you run a test in the standard environment, Device Farm provides detailed logs and reporting for every case in your test suite. You can view videos, screenshots, and logs for each test to pinpoint and fix issues in your app.

**Note**  
Because Device Farm provides granular reporting in the standard environment, test execution times can be longer than when you run your tests locally. If you want faster execution times, run your tests in a custom test environment. 

### Custom test environment
<a name="custom-test-environment"></a>

When you customize the test environment, you can specify the commands Device Farm should run to execute your tests. This ensures that tests on Device Farm run in a way that is similar to tests run on your local machine. Running your tests in this mode also enables live log and video streaming of your tests. When you run tests in a customized test environment, you do not get granular reports for each test case. For more information, see [Custom test environments in AWS Device Farm](#custom-test-environments).

You have the option to use a custom test environment when you use the Device Farm console, AWS CLI, or Device Farm API to create a test run.

For more information, see [Uploading a Custom Test Spec Using the AWS CLI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html#how-to-create-test-run-cli-step5) and [Creating a test run in Device Farm](#how-to-create-test-run).

## Runs in AWS Device Farm
<a name="test-runs"></a>

The following sections contain information about runs in Device Farm.

A run in Device Farm represents a specific build of your app, with a specific set of tests, to be run on a specific set of devices. A run produces a report that contains information about the results of the run. A run contains one or more jobs.

**Topics**
+ [Run configuration](#test-runs-configuration)
+ [Run files retention](#test-runs-retention)
+ [Run device state](#test-runs-device-state)
+ [Parallel runs](#test-runs-parallel)
+ [Setting the execution timeout](#test-runs-default-timeout)
+ [Ads in runs](#test-runs-ads)
+ [Media in runs](#test-runs-media)
+ [Common tasks for runs](#test-runs-tasks)

### Run configuration
<a name="test-runs-configuration"></a>

As part of a run, you can supply settings Device Farm can use to override current device settings. These include latitude and longitude coordinates, extra data (contained in a .zip file), and auxiliary apps (apps that should be installed before the app to be tested). On Android, some additional settings can be changed, such as locale and radio states (Bluetooth, GPS, NFC, and Wi-Fi).

### Run files retention
<a name="test-runs-retention"></a>

Device Farm stores your apps and files for 30 days and then deletes them from its system. You can delete your files at any time, however.

Device Farm stores your run results, logs, and screenshots for 400 days and then deletes them from its system.

### Run device state
<a name="test-runs-device-state"></a>

Device Farm always reboots a device before making it available for the next job.

### Parallel runs
<a name="test-runs-parallel"></a>

Device Farm runs tests in parallel as devices become available.

### Setting the execution timeout
<a name="test-runs-default-timeout"></a>

You can set a value for how long a test run should execute before you stop each device from running a test. For example, if your tests take 20 minutes per device to complete, you should choose a timeout of 30 minutes per device.

For more information, see [Setting the execution timeout for test runs in AWS Device Farm](#how-to-set-default-timeout-for-test-runs).

### Ads in runs
<a name="test-runs-ads"></a>

We recommend that you remove ads from your apps before you upload them to Device Farm. We cannot guarantee that ads are displayed during runs.

### Media in runs
<a name="test-runs-media"></a>

You can provide media or other data to accompany your app. Additional data must be provided in a .zip file no more than 4 GB in size.

### Common tasks for runs
<a name="test-runs-tasks"></a>

For more information, see [Creating a test run in Device Farm](#how-to-create-test-run) and [Test runs in AWS Device Farm](#runs).

## Apps in AWS Device Farm
<a name="apps"></a>

The following sections contain information about app behaviors in Device Farm.

**Topics**
+ [Instrumenting apps](#test-runs-instrumenting)
+ [Re-signing apps in runs](#test-runs-app-resigning)
+ [Obfuscated apps in runs](#test-runs-obfuscated-apps)

### Instrumenting apps
<a name="test-runs-instrumenting"></a>

You do not need to instrument your apps or provide Device Farm with the source code for your apps. Android apps can be submitted unmodified. iOS apps must be built with the **iOS Device** target instead of with the simulator.

### Re-signing apps in runs
<a name="test-runs-app-resigning"></a>

For iOS apps, you do not need to add any Device Farm UUIDs to your provisioning profile. Device Farm replaces the embedded provisioning profile with a wildcard profile and then re-signs the app. If you provide auxiliary data, Device Farm adds it to the app's package before Device Farm installs it, so that the auxiliary exists in your app's sandbox. Re-signing the app removes entitlements such as App Group, Associated Domains, Game Center, HealthKit, HomeKit, Wireless Accessory Configuration, In-App Purchase, Inter-App Audio, Apple Pay, Push Notifications, and VPN Configuration & Control.

For Android apps, Device Farm re-signs the app. This might break any functionality that depends on the app's signature, such as the Google Maps Android API, or it might trigger antipiracy or antitamper detection from products such as DexGuard. 

### Obfuscated apps in runs
<a name="test-runs-obfuscated-apps"></a>

For Android apps, if the app is obfuscated, you can still test it with Device Farm if you use ProGuard. However, if you use DexGuard with antipiracy measures, Device Farm cannot re-sign and run tests against the app.

## Reports in AWS Device Farm
<a name="reports"></a>

The following sections provide information about Device Farm test reports.

**Topics**
+ [Report retention](#reports-retention)
+ [Report components](#reports-components)
+ [Logs in reports](#reports-logs)
+ [Common tasks for reports](#reports-tasks)

### Report retention
<a name="reports-retention"></a>

Device Farm stores your reports for 400 days. These reports include metadata, logs, and screenshots.

### Report components
<a name="reports-components"></a>

Reports in Device Farm contain pass and fail information, crash reports, test and device logs, and screenshots. The report includes detailed per-device data and high-level results, such as the number of occurrences of a given problem.

#### Test Insights
<a name="reports-test-insights"></a>

For supported frameworks such as Appium TestNG, XCUI, and Instrumentation, Device Farm provides an optional **Test Insights** report. Test Insights include the following information:
+ Passed, failed, skipped, and errored test counts for each job and for each run
+ Detailed test output with timestamps and stack traces for each test, where applicable
+ Median test execution time for each job, and median and average job execution duration for each run

Test Insights helps you understand your test suite performance at both the job and run level. With Test Insights, you get the detailed test reporting of standard mode combined with the faster execution speed of custom mode. For more information about test environments, see [Test environments in AWS Device Farm](#test-environments).

To schedule a run with Test Insights, see [Step 3: Create and start a run](#getting-started-create-run).

### Logs in reports
<a name="reports-logs"></a>

Reports include complete logcat captures for Android tests and complete Device Console logs for iOS tests.

### Common tasks for reports
<a name="reports-tasks"></a>

For more information, see [Viewing test reports in Device Farm](#how-to-use-reports).

## Sessions in AWS Device Farm
<a name="sessions"></a>

You can use Device Farm to perform interactive testing of Android and iOS apps through remote access sessions. This includes both manual interaction in a web browser and running Appium tests from a local client against the remote device. Developers can reproduce issues with their app or with their Appium tests on a specific device to isolate and resolve problems.

**Topics**
+ [Supported devices for remote access](#session-devices-supported)
+ [Session files retention](#session-files-retention)
+ [Instrumenting apps](#session-instrumenting)
+ [Re-signing apps in sessions](#session-resigning-apps)
+ [Obfuscated apps in sessions](#session-obfuscated-apps)

### Supported devices for remote access
<a name="session-devices-supported"></a>

Device Farm provides support for a number of unique, popular Android and iOS devices. The list of available devices grows as new devices enter the market. The Device Farm console displays the current list of Android and iOS devices available for remote access. For more information, see [Device support in AWS Device Farm](#devices).

### Session files retention
<a name="session-files-retention"></a>

Device Farm stores your apps and files for 30 days and then deletes them from its system. You can delete your files at any time, however.

Device Farm stores your session logs and captured video for 400 days and then deletes them from its system.

### Instrumenting apps
<a name="session-instrumenting"></a>

You do not need to instrument your apps or provide Device Farm with the source code for your apps. Android and iOS apps can be submitted unmodified. 

### Re-signing apps in sessions
<a name="session-resigning-apps"></a>

Device Farm re-signs Android and iOS apps. This can break functionality that depends on the app's signature. For example, the Google Maps API for Android depends on your app's signature. App re-signing can also trigger antipiracy or antitamper detection from products such as DexGuard for Android devices. 

### Obfuscated apps in sessions
<a name="session-obfuscated-apps"></a>

For Android apps, if the app is obfuscated, you can still test it with Device Farm if you use ProGuard. However, if you use DexGuard with antipiracy measures, Device Farm cannot re-sign the app. 

# Projects in AWS Device Farm
<a name="projects"></a>

A project in Device Farm represents a logical workspace in Device Farm that contains runs, one run for each test of a single app against one or more devices. Projects enable you to organize workspaces in whatever way you choose. For example, there can be one project per app title, or there can be one project per platform. You can create as many projects as you need.

You can use the AWS Device Farm console, AWS Command Line Interface (AWS CLI), or AWS Device Farm API to work with projects.



**Topics**
+ [Creating a project in AWS Device Farm](#how-to-create-project)
+ [Viewing the projects list in AWS Device Farm](#how-to-view-projects-list)

## Creating a project in AWS Device Farm
<a name="how-to-create-project"></a>

You can create a project by using the AWS Device Farm console, AWS CLI, or AWS Device Farm API.

### Prerequisites
<a name="how-to-create-project-prerequisites"></a>
+ Complete the steps in [Setting up](#setting-up).

### Create a project (console)
<a name="how-to-create-project-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose **New project**.

1. Enter a name for your project. Optionally, you may supply one or more of the parameters below, then choose **Submit**.

   Optional configuration parameters:  
**Virtual Private Cloud (VPC) settings**  
Select a VPC, subnets, and security group to be applied to the device under test and its paired test host. This feature is only supported with private devices. See [VPC-ENI in AWS Device Farm](#vpc-eni) for more information.  
**Execution Role ARN**  
An IAM role to be assumed by the test runner in custom test environments. For more information, see [Access AWS resources using an IAM Execution Role](#custom-test-environments-iam-roles).  
**Environment Variables**  
One or more variables to be inserted into the environment of the test execution runner process. Variable names beginning with "DEVICEFARM\_" are reserved for service use. We recommend against storing sensitive values in these environment variables, and instead suggest using an IAM execution role to fetch such values from AWS Secrets Manager during your test.

### Create a project (AWS CLI)
<a name="how-to-create-project-cli"></a>
+ Run **create-project**, specifying the project name.

  Example:

  ```
  aws devicefarm create-project --name {{MyProjectName}}
  ```

  The AWS CLI response includes the Amazon Resource Name (ARN) of the project.

  ```
  {
      "project": {
          "name": "MyProjectName",
          "arn": "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
          "created": 1535675814.414
      }
  }
  ```

  For more information, see [**create-project**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-project.html) and [AWS CLI reference](#cli-ref).

### Create a project (API)
<a name="how-to-create-project-api"></a>
+ Call the [`CreateProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateProject.html) API.

For information about using the Device Farm API, see [Automating Device Farm](#api-ref).

## Viewing the projects list in AWS Device Farm
<a name="how-to-view-projects-list"></a>

You can use the AWS Device Farm console, AWS CLI, or AWS Device Farm API to view the list of projects.

**Topics**
+ [Prerequisites](#how-to-view-projects-list-prerequisites)
+ [View the projects list (console)](#how-to-view-projects-list-console)
+ [View the projects list (AWS CLI)](#how-to-view-projects-list-cli)
+ [View the projects list (API)](#how-to-view-projects-list-api)

### Prerequisites
<a name="how-to-view-projects-list-prerequisites"></a>
+ Create at least one project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](#how-to-create-project), and then return to this page.

### View the projects list (console)
<a name="how-to-view-projects-list-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. To find the list of available projects, do the following:
   + For mobile device testing projects, on the Device Farm navigation menu, choose **Mobile Device Testing**, then choose **Projects**.
   + For desktop browser testing projects, on the Device Farm navigation menu, choose **Desktop Browser Testing**, then choose **Projects**.

### View the projects list (AWS CLI)
<a name="how-to-view-projects-list-cli"></a>
+ To view the projects list, run the [**list-projects**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/list-projects.html) command.

  To view information about a single project, run the [**get-project**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/get-project.html) command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](#cli-ref).

### View the projects list (API)
<a name="how-to-view-projects-list-api"></a>
+ To view the projects list, call the [`ListProjects`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListProjects.html) API.

  To view information about a single project, call the [`GetProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetProject.html) API.

For information about the AWS Device Farm API, see [Automating Device Farm](#api-ref).

# Test runs in AWS Device Farm
<a name="runs"></a>

A run in Device Farm represents a specific build of your app, with a specific set of tests, to be run on a specific set of devices. A run produces a report that contains information about the results of the run. A run contains one or more jobs. For more information, see [Runs](#test-runs).

You can use the AWS Device Farm console, AWS Command Line Interface (AWS CLI), or AWS Device Farm API to work with test runs.

**Topics**
+ [Creating a test run in Device Farm](#how-to-create-test-run)
+ [Setting the execution timeout for test runs in AWS Device Farm](#how-to-set-default-timeout-for-test-runs)
+ [Simulating network connections and conditions for your AWS Device Farm runs](#how-to-simulate-network-connections-and-conditions)
+ [Stopping a run in AWS Device Farm](#how-to-stop-test-runs)
+ [Viewing a list of runs in AWS Device Farm](#how-to-view-runs-list)
+ [Creating a device pool in AWS Device Farm](#how-to-create-device-pool)
+ [Analyzing test results in AWS Device Farm](#analyzing-results)

## Creating a test run in Device Farm
<a name="how-to-create-test-run"></a>

You can use the Device Farm console, AWS CLI, or Device Farm API to create a test run. You can also use a supported plugin, such as the Jenkins or Gradle plugins for Device Farm. For more information about plugins, see [Tools and plugins](#aws-device-farm-tools-plugins). For information about runs, see [Runs](#test-runs).

**Topics**
+ [Prerequisites](#how-to-create-test-run-prerequisites)
+ [Create a test run (console)](#how-to-create-test-run-console)
+ [Create a test run (AWS CLI)](#how-to-create-test-run-cli)
+ [Create a test run (API)](#how-to-create-test-run-api)
+ [Next steps](#how-to-create-test-run-console-next-steps)

### Prerequisites
<a name="how-to-create-test-run-prerequisites"></a>

You must have a project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](#how-to-create-project), and then return to this page.

### Create a test run (console)
<a name="how-to-create-test-run-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. If you already have a project, you can upload your tests to it. Otherwise, choose **New project**, enter a **Project Name**, and then choose **Create**.

1. Open your project, and then choose **Create run**.

1. Under **Select app and run type**, in the **Run type** section, select your run type. Select **Android app** if you do not have an app ready for testing, or if you are testing an android (.apk) app. Select **iOS app** if you are testing an iOS (.ipa) app. Select **Web app** if you want to test web applications.

1. Under **Select app**, in the **App selection options** section, choose **Select sample app provided by Device Farm** if you do not have an app available for testing. If you are bringing your own app, select **Upload own app**, and choose your application file. If you're uploading an iOS app, be sure to choose **iOS device**, as opposed to a simulator.

1. Under **Configure test**, choose one of the available test frameworks.
**Note**  
If you don't have any tests available, choose **Built-in: Fuzz** to run a standard, built-in test suite. If you choose **Built-in: Fuzz**, and the **Event count**, **Event throttle**, and **Randomizer seed** boxes appear, you can change or keep the values. 

   For information about the available test suites, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

1. If you didn't choose **Built-in: Fuzz**, select **Choose File** under **Select test package**. Browse to and choose the file that contains your tests.

1. For your testing environment, choose **Run your test in our standard environment** or **Run your test in a custom environment**. For more information, see [Test environments in AWS Device Farm](#test-environments).

1. If you're using a custom test environment, you can optionally do the following:
   + If you want to edit the default test spec in a custom test environment, choose **Edit** to update the default YAML specification.
   + If you changed the test spec, choose **Save as New** to update it.
   + You may configure envirnonment variables. Variables supplied here will take precedence over any that may be configured on the parent project.

1. Under **Select devices**, do one of the following:
   + To choose a built-in device pool to run the tests against, for **Device pool**, choose **Top Devices**. 
   + To create your own device pool to run the tests against, follow the instructions in [Creating a device pool](#how-to-create-device-pool), and then return to this page.
   + If you created your own device pool earlier, for **Device pool**, choose your device pool. 
   + Select **Manually select devices** and choose the desired devices you want to run against. This configuration will not be saved.

   For more information, see [Device support in AWS Device Farm](#devices).

1. (Optional) To configure run-level properties, update the **Run Settings** section. Here you can do the following:
   + Assign your run with a custom **Run name**. If no name is provided, the Device Farm console will name your run 'My Device Farm run' by default.
   + Choose **Generate test report** under **Test Insights** to get a detailed structured test report for each job and an aggregated summary at the run level. This insight is generated in addition to any test report that you might generate as part of your test execution.
   + Assign a **Job timeout**, which is the maximum number of minutes a job can run on a device. If your tests are complete before the job timeout, the job completes, and you are not charged for the remainder of the job timeout. The default is 150 minutes.
   + Choose a **Billing method**. By default, if you do not have slots purchased on your account, the Device Farm console selects Metered. If you have slots, the console defaults to Unmetered.

1. (Optional) To add additional configuration, open the **Additional configuration** dropdown. In this section, you can do any of the following:
   + To provide an execution role ARN, or override one configured on the parent project, use the Exectuion role ARN field.
   + To provide other data for Device Farm to use during the run, next to **Add extra data**, choose **Choose File**, and then browse to and choose the .zip file that contains the data.
   + To install an additional app for Device Farm to use during the run, next to **Install other apps**, choose **Choose File**, and then browse to and choose the .apk or .ipa file that contains the app. Repeat this for other apps you want to install. You can change the installation order by dragging and dropping the apps after you upload them. 
   + To specify whether Wi-Fi, Bluetooth, GPS, or NFC is enabled during the run, next to **Set radio states**, select the appropriate boxes.
   + To preset the device latitude and longitude for the run, next to **Device location**, enter the coordinates.
   + To preset the device locale for the run, in **Device locale**, choose the locale.
   + Select **Enable video recording** to record video during testing.
**Note**  
Setting the device radio state and locale are options only available for Android native tests at this time.
**Note**  
If you have private devices, configuration specific to private devices is also displayed.

1. At the bottom of the page, choose **Confirm and start run** to schedule the run.

Device Farm starts the run as soon as devices are available, typically within a few minutes. During your test run, the Device Farm console displays a pending icon ![Device Farm scheduled a job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-calendar.png) in the run table. Each device in the run will also start with the pending icon, then switch to the running icon ![Device Farm progress indicator.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-progress.png) when the test begins. As each test finishes, a test result icon is displayed next to the device name. When all tests have been completed, the pending icon next to the run changes to a test result icon.

If you want to stop the test run, see [Stopping a run in AWS Device Farm](#how-to-stop-test-runs).

### Create a test run (AWS CLI)
<a name="how-to-create-test-run-cli"></a>

You can use the AWS CLI to create a test run.

**Topics**
+ [Step 1: Choose a project](#how-to-create-test-run-cli-step1)
+ [Step 2: Choose a device pool](#how-to-create-test-run-cli-step2)
+ [Step 3: Upload your application file](#how-to-create-test-run-cli-step3)
+ [Step 4: Upload your test scripts package](#how-to-create-test-run-cli-step4)
+ [Step 5: (Optional) Upload your custom test spec](#how-to-create-test-run-cli-step5)
+ [Step 6: Schedule a test run](#how-to-create-test-run-cli-step6)

#### Step 1: Choose a project
<a name="how-to-create-test-run-cli-step1"></a>

You must associate your test run with a Device Farm project.

1. To list your Device Farm projects, run **list-projects**. If you do not have a project, see [Creating a project in AWS Device Farm](#how-to-create-project).

   Example:

   ```
   aws devicefarm list-projects
   ```

   The response includes a list of your Device Farm projects.

   ```
   {
       "projects": [
           {
               "name": "MyProject",
               "arn": "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
               "created": 1503612890.057
           }
       ]
   }
   ```

1. Choose a project to associate with your test run, and make a note of its Amazon Resource Name (ARN).

#### Step 2: Choose a device pool
<a name="how-to-create-test-run-cli-step2"></a>

You must choose a device pool to associate with your test run.

1. To view your device pools, run **list-device-pools**, specifying your project ARN.

   Example:

   ```
   aws devicefarm list-device-pools --arn {{arn:MyProjectARN}}
   ```

   The response includes the built-in Device Farm device pools, such as **Top Devices**, and any device pools previously created for this project:

   ```
   {
       "devicePools": [
           {
               "rules": [
                   {
                       "attribute": "ARN",
                       "operator": "IN",
                       "value": "[\"arn:aws:devicefarm:us-west-2::device:example1\",\"arn:aws:devicefarm:us-west-2::device:example2\",\"arn:aws:devicefarm:us-west-2::device:example3\"]"
                   }
               ],
               "type": "CURATED",
               "name": "Top Devices",
               "arn": "arn:aws:devicefarm:us-west-2::devicepool:example",
               "description": "Top devices"
           },
           {
               "rules": [
                   {
                       "attribute": "PLATFORM",
                       "operator": "EQUALS",
                       "value": "\"ANDROID\""
                   }
               ],
               "type": "PRIVATE",
               "name": "MyAndroidDevices",
               "arn": "arn:aws:devicefarm:us-west-2:605403973111:devicepool:example2"
           }
       ]
   }
   ```

1. Choose a device pool, and make a note of its ARN.

   You can also create a device pool, and then return to this step. For more information, see [Create a device pool (AWS CLI)](#how-to-create-device-pool-cli).

#### Step 3: Upload your application file
<a name="how-to-create-test-run-cli-step3"></a>

To create your upload request and get an Amazon Simple Storage Service (Amazon S3) presigned upload URL, you need:
+ Your project ARN.
+ The name of your app file.
+ The type of the upload.

For more information, see [**create-upload**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-upload.html).

1. To upload a file, run **create-upload** with the `–-project-arn`, `--name`, and `--type` parameters.

   This example creates an upload for an Android app:

   ```
   aws devicefarm create-upload -–project-arn arn:MyProjectArn -–name {{MyAndroid.apk}} -–type ANDROID_APP
   ```

   The response includes your app upload ARN and a presigned URL.

   ```
   {
       "upload": {
           "status": "INITIALIZED",
           "name": "MyAndroid.apk",
           "created": 1535732625.964,
           "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
           "type": "ANDROID_APP",
           "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
       }
   }
   ```

1. Make a note of the app upload ARN and the presigned URL.

1. Upload your app file using the Amazon S3 presigned URL. This example uses **curl** to upload an Android .apk file:

   ```
   curl -T MyAndroid.apk "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL"
   ```

   For more information, see [Uploading objects using presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html) in the *Amazon Simple Storage Service User Guide*.

1. To check the status of your app upload, run **get-upload** and specify the ARN of the app upload.

   ```
   aws devicefarm get-upload –-arn arn:MyAppUploadARN
   ```

   Wait until the status in the response is **SUCCEEDED** before you upload your test scripts package.

   ```
   {
       "upload": {
           "status": "SUCCEEDED",
           "name": "MyAndroid.apk",
           "created": 1535732625.964,
           "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL", 
           "type": "ANDROID_APP",
           "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
           "metadata": "{"valid": true}"
       }
   }
   ```

#### Step 4: Upload your test scripts package
<a name="how-to-create-test-run-cli-step4"></a>

Next, you upload your test scripts package.

1. To create your upload request and get an Amazon S3 presigned upload URL, run **create-upload** with the `–-project-arn`, `--name`, and `--type` parameters.

   This example creates an Appium Java TestNG test package upload:

   ```
   aws devicefarm create-upload –-project-arn {{arn:MyProjectARN}} -–name {{MyTests.zip}} –-type APPIUM_JAVA_TESTNG_TEST_PACKAGE
   ```

   The response includes your test package upload ARN and a presigned URL.

   ```
   {
       "upload": {
           "status": "INITIALIZED",
           "name": "MyTests.zip",
           "created": 1535738627.195,
           "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
           "type": "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
           "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
       }    
   }
   ```

1. Make a note of the ARN of the test package upload and the presigned URL.

1. Upload your test scripts package file using the Amazon S3 presigned URL. This example uses **curl** to upload a zipped Appium TestNG scripts file:

   ```
   curl -T MyTests.zip "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL"
   ```

1. To check the status of your test scripts package upload, run **get-upload** and specify the ARN of the test package upload from step 1.

   ```
   aws devicefarm get-upload –-arn arn:MyTestsUploadARN
   ```

   Wait until the status in the response is **SUCCEEDED** before you continue to the next, optional step.

   ```
   {
       "upload": {
           "status": "SUCCEEDED",
           "name": "MyTests.zip",
           "created": 1535738627.195,
           "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL", 
           "type": "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
           "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
           "metadata": "{"valid": true}"
       }
   }
   ```

#### Step 5: (Optional) Upload your custom test spec
<a name="how-to-create-test-run-cli-step5"></a>

If you're running your tests in a standard test environment, skip this step.

Device Farm maintains a default test spec file for each supported test type. Next, you download your default test spec and use it to create a custom test spec upload for running your tests in a custom test environment. For more information, see [Test environments in AWS Device Farm](#test-environments).

1. To find the upload ARN for your default test spec, run **list-uploads** and specify your project ARN.

   ```
   aws devicefarm list-uploads --arn {{arn:MyProjectARN}}
   ```

   The response contains an entry for each default test spec:

   ```
   {
       "uploads": [
           {
   
               {
                   "status": "SUCCEEDED",
                   "name": "Default TestSpec for Android Appium Java TestNG",
                   "created": 1529498177.474,
                   "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL", 
                   "type": "APPIUM_JAVA_TESTNG_TEST_SPEC",
                   "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
               }
           }
       ]
   }
   ```

1. Choose your default test spec from the list. Make a note of its upload ARN.

1. To download your default test spec, run **get-upload** and specify the upload ARN.

   Example:

   ```
   aws devicefarm get-upload –-arn {{arn:MyDefaultTestSpecARN}}
   ```

   The response contains a presigned URL where you can download your default test spec.

1. This example uses **curl** to download the default test spec and save it as `MyTestSpec.yml`:

   ```
   curl "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL" > MyTestSpec.yml
   ```

1. You can edit the default test spec to meet your testing requirements, and then use your modified test spec in future test runs. Skip this step to use the default test spec as-is in a custom test environment. 

1. To create an upload of your custom test spec, run **create-upload**, specifying your test spec name, test spec type, and project ARN.

   This example creates an upload for an Appium Java TestNG custom test spec:

   ```
   aws devicefarm create-upload --name MyTestSpec.yml --type APPIUM_JAVA_TESTNG_TEST_SPEC --project-arn {{arn:MyProjectARN}}
   ```

   The response includes the test spec upload ARN and presigned URL:

   ```
   {
       "upload": {
           "status": "INITIALIZED",
           "category": "PRIVATE",
           "name": "MyTestSpec.yml",
           "created": 1535751101.221,
           "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL", 
           "type": "APPIUM_JAVA_TESTNG_TEST_SPEC",
           "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
       }
   }
   ```

1. Make a note of the ARN for the test spec upload and the presigned URL.

1. Upload your test spec file using the Amazon S3 presigned URL. This example uses **curl** to upload an Appium JavaTestNG test spec:

   ```
   curl -T MyTestSpec.yml "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL"
   ```

1. To check the status of your test spec upload, run **get-upload** and specify the upload ARN.

   ```
   aws devicefarm get-upload –-arn {{arn:MyTestSpecUploadARN}}
   ```

   Wait until the status in the response is **SUCCEEDED** before you schedule your test run.

   ```
   {
       "upload": {
           "status": "SUCCEEDED",
           "name": "MyTestSpec.yml",
           "created": 1535732625.964,
           "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL", 
           "type": "APPIUM_JAVA_TESTNG_TEST_SPEC",
           "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
           "metadata": "{"valid": true}"
       }
   }
   ```

   To update your custom test spec, run **update-upload**, specifying the upload ARN for the test spec. For more information, see [**update-upload**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/update-upload.html).

#### Step 6: Schedule a test run
<a name="how-to-create-test-run-cli-step6"></a>

To schedule a test run with the AWS CLI, run **schedule-run**, specifying:
+ The project ARN from [step 1](#how-to-create-test-run-cli-step1).
+ The device pool ARN from [step 2](#how-to-create-test-run-cli-step2).
+ The app upload ARN from [step 3](#how-to-create-test-run-cli-step3).
+ The test package upload ARN from [step 4](#how-to-create-test-run-cli-step4).

 If you are running tests in a custom test environment, you also need your test spec ARN from [step 5](#how-to-create-test-run-cli-step5).

**To schedule a run in a standard test environment**
+ Run **schedule-run**, specifying your project ARN, device pool ARN, application upload ARN, and test package information.

  Example:

  ```
  aws devicefarm schedule-run --project-arn {{arn:MyProjectARN}} --app-arn {{arn:MyAppUploadARN}} --device-pool-arn {{arn:MyDevicePoolARN}} --name {{MyTestRun}} --test type=APPIUM_JAVA_TESTNG,testPackageArn={{arn:MyTestPackageARN}}
  ```

  The response contains a run ARN that you can use to check the status of your test run.

  ```
  {
      "run": {
          "status": "SCHEDULING",
          "appUpload": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345appEXAMPLE",
          "name": "MyTestRun",
          "radios": {
              "gps": true,
              "wifi": true,
              "nfc": true,
              "bluetooth": true
          },
          "created": 1535756712.946,
          "totalJobs": 179,
          "completedJobs": 0,
          "platform": "ANDROID_APP",
          "result": "PENDING",
          "devicePoolArn": "arn:aws:devicefarm:us-west-2:123456789101:devicepool:5e01a8c7-c861-4c0a-b1d5-12345devicepoolEXAMPLE",
          "jobTimeoutMinutes": 150,
          "billingMethod": "METERED",
          "type": "APPIUM_JAVA_TESTNG",
          "testSpecArn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345specEXAMPLE",
          "arn": "arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-12345runEXAMPLE",
          "counters": {
              "skipped": 0,
              "warned": 0,
              "failed": 0,
              "stopped": 0,
              "passed": 0,
              "errored": 0,
              "total": 0
          }
      }
  }
  ```

  For more information, see [**schedule-run**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/schedule-run.html).

**To schedule a run in a custom test environment**
+ The steps are the almost the same as those for the standard test environment, with an additional `testSpecArn` attribute in the `--test` parameter.

  Example:

  ```
  aws devicefarm schedule-run --project-arn {{arn:MyProjectARN}} --app-arn {{arn:MyAppUploadARN}} --device-pool-arn {{arn:MyDevicePoolARN}} --name {{MyTestRun}} --test testSpecArn={{arn:MyTestSpecUploadARN}},type={{APPIUM_JAVA_TESTNG}},testPackageArn={{arn:MyTestPackageARN}}
  ```

**To check the status of your test run**
+ Use the **get-run** command and specify the run ARN:

  ```
  aws devicefarm get-run --arn arn:aws:devicefarm:us-west-2:111122223333:run:5e01a8c7-c861-4c0a-b1d5-12345runEXAMPLE
  ```

For more information, see [**get-run**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/get-run.html). For information about using Device Farm with the AWS CLI, see [AWS CLI reference](#cli-ref).

### Create a test run (API)
<a name="how-to-create-test-run-api"></a>

The steps are the same as those described in the AWS CLI section. See [Create a test run (AWS CLI)](#how-to-create-test-run-cli).

You need this information to call the [`ScheduleRun`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRun.html) API:
+ A project ARN. See [Create a project (API)](#how-to-create-project-api) and [`CreateProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateProject.html).
+ An application upload ARN. See [`CreateUpload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html).
+ A test package upload ARN. See [`CreateUpload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html).
+ A device pool ARN. See [Creating a device pool](#how-to-create-device-pool) and [`CreateDevicePool`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateDevicePool.html).

**Note**  
If you're running tests in a custom test environment, you also need your test spec upload ARN. For more information, see [Step 5: (Optional) Upload your custom test spec](#how-to-create-test-run-cli-step5) and [`CreateUpload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html).

For information about using the Device Farm API, see [Automating Device Farm](#api-ref).

### Next steps
<a name="how-to-create-test-run-console-next-steps"></a>

In the Device Farm console, the clock icon ![Device Farm scheduled a job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-calendar.png) changes to a result icon such as success ![The test succeeded.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-success.png) when the run is complete. A report for the run appears as soon as tests are complete. For more information, see [Reports in AWS Device Farm](#reports).

To use the report, follow the instructions in [Viewing test reports in Device Farm](#how-to-use-reports).

## Setting the execution timeout for test runs in AWS Device Farm
<a name="how-to-set-default-timeout-for-test-runs"></a>

You can set a value for how long a test run should execute before you stop each device from running a test. The default execution timeout is 150 minutes per device, but you can set a value as low as 5 minutes. You can use the AWS Device Farm console, AWS CLI, or AWS Device Farm API to set the execution timeout. 

**Important**  
The execution timeout option should be set to the *maximum duration* for a test run, along with some buffer. For example, if your tests take 20 minutes per device, you should choose a timeout of 30 minutes per device.

If the execution exceeds your timeout, the execution on that device is forcibly stopped. Partial results are available, if possible. You are billed for execution up to that point, if you're using the metered billing option. For more information about pricing, see [Device Farm Pricing](https://aws.amazon.com/device-farm/pricing/).

You might want to use this feature if you know how long a test run is supposed to take to execute on each device. When you specify an execution timeout for a test run, you can avoid the situation where a test run is stuck for some reason and you are being billed for device minutes when no tests are being executed. In other words, using the execution timeout feature lets you stop that run if it's taking longer than expected.

You can set the execution timeout in two places, at the project level and the test run level. 

### Prerequisites
<a name="how-to-set-default-timeout-prerequisites"></a>

1. Complete the steps in [Setting up](#setting-up).

1. Create a project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](#how-to-create-project), and then return to this page.

### Set the execution timeout for a project
<a name="how-to-set-execution-timeout-project-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. If you already have a project, choose it from the list. Otherwise, choose **New project**, enter a name for your project, then choose **Submit**.

1. Choose **Project settings**.

1. On the **General** tab, for **Execution timeout**, enter a value or use the slider bar.

1. Choose **Save**.

   All the test runs in your project now use the execution timeout value that you specified, unless you override the timeout value when you schedule a run.

### Set the execution timeout for a test run
<a name="how-to-set-execution-timeout-test-run-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. If you already have a project, choose it from the list. Otherwise, choose **New project**, enter a name for your project, then choose **Submit**.

1. Choose **Create a new run**.

1. Follow the steps to choose an application, configure your test, select your devices, and specify a device state.

1. On **Review and start run**, for **Set execution timeout**, enter a value or use the slider bar.

1. Choose **Confirm and start run**.

## Simulating network connections and conditions for your AWS Device Farm runs
<a name="how-to-simulate-network-connections-and-conditions"></a>

You can use network shaping to simulate network connections and conditions while testing your Android, iOS and web apps in Device Farm. For example, you can simulate lossy or intermittent internet connectivity.

When you create a run using the default network settings, each device has a full, unhindered Wi-Fi connection with internet connectivity. When you use network shaping, you can change the Wi-Fi connection to specify a network profile like **3G** or **Lossy WiFi** that controls throughput, delay, jitter, and loss for both inbound and outbound traffic.

**Topics**
+ [Set up network shaping when scheduling a test run](#network-shaping-how-to-choose-a-curated-profile-when-scheduling-a-test-run)
+ [Create a network profile](#network-shaping-how-to-create-a-network-profile)
+ [Change network conditions during your test](#change-network-conditions-during-test)

### Set up network shaping when scheduling a test run
<a name="network-shaping-how-to-choose-a-curated-profile-when-scheduling-a-test-run"></a>

When you schedule a run, you can choose from any of the Device Farm-curated profiles, or you can create and manage your own.

1. From any Device Farm project, choose **Create a new run**.

   If you don't have a project yet, see [Creating a project in AWS Device Farm](#how-to-create-project).

1. Choose your application, and then choose **Next**.

1. Configure your test, and then choose **Next**.

1. Select your devices, and then choose **Next**.

1. In the **Location and network settings** section, choose a network profile or choose **Create network profile** to create your own.  
![Network profile for a test run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-set-up-network-profile.png)

1. Choose **Next**.

1. Review and start your test run.

### Create a network profile
<a name="network-shaping-how-to-create-a-network-profile"></a>

When you create a test run, you can create a network profile.

1. Choose **Create network profile**.  
![Create a new network profile](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-create-a-new-network-profile.png)

1. Enter a name and settings for your network profile.

1. Choose **Create**.

1. Finish creating your test run and start the run.

After you have created a network profile, you'll be able to see and manage it on the **Project settings** page.

![Network profiles in Project settings](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-network-profiles-in-project-settings.png)


### Change network conditions during your test
<a name="change-network-conditions-during-test"></a>

You can call an API from your device host using a framework like Appium to simulate dynamic network conditions such as reduced bandwidth during your test run. For more information, see [CreateNetworkProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateNetworkProfile.html).

## Stopping a run in AWS Device Farm
<a name="how-to-stop-test-runs"></a>

You might want to stop a run after you have started it. For example, if you notice an issue while your tests are running you might want to restart the run with an updated test script. 

You can use the Device Farm console, AWS CLI, or API to stop a run.

**Topics**
+ [Stop a run (console)](#how-to-stop-run-console)
+ [Stop a run (AWS CLI)](#how-to-stop-test-run-cli)
+ [Stop a run (API)](#how-to-stop-test-run-api)

### Stop a run (console)
<a name="how-to-stop-run-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose the project where you have an active test run.

1. On the **Automated tests** page, choose the test run.

   The pending or running icon should appear to the left of the device name.  
![Device Farm - Stop a test run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-stop-run.png)

1. Choose **Stop run**.

   After a short time, an icon with a red circle with a minus inside it appears next to the device name. When the run has been stopped, the icon color changes from red to black.
**Important**  
If a test has already been run, Device Farm cannot stop it. If a test is in progress, Device Farm stops the test. The total minutes for which you will be billed appears in the **Devices** section. In addition, you will also be billed for the total minutes that Device Farm takes to run the setup suite and the teardown suite. For more information, see [Device Farm Pricing](http://aws.amazon.com/device-farm/faq/#pricing).

   The following image shows an example **Devices** section after a test run was successfully stopped.  
![Device Farm - Details page of a stopped run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-stop-run-view-details.png)

### Stop a run (AWS CLI)
<a name="how-to-stop-test-run-cli"></a>

 You can run the following command to stop the specified test run, where {{myARN}} is the Amazon Resource Name (ARN) of the test run. 

```
$ aws devicefarm stop-run --arn {{myARN}}
```

You should see output similar to the following:

```
{
    "run": {
        "status": "STOPPING",
        "name": "Name of your run",
        "created": 1458329687.951,
        "totalJobs": 7,
        "completedJobs": 5,
        "deviceMinutes": {
            "unmetered": 0.0,
            "total": 0.0,
            "metered": 0.0
        },
        "platform": "ANDROID_APP",
        "result": "PENDING",
        "billingMethod": "METERED",
        "type": "BUILTIN_EXPLORER",
        "arn": "myARN",
        "counters": {
            "skipped": 0,
            "warned": 0,
            "failed": 0,
            "stopped": 0,
            "passed": 0,
            "errored": 0,
            "total": 0
        }
    }
}
```

To get the ARN of your run, use the `list-runs` command. The output should be similar to the following:

```
{
    "runs": [
        {
            "status": "RUNNING",
            "name": "Name of your run",
            "created": 1458329687.951,
            "totalJobs": 7,
            "completedJobs": 5,
            "deviceMinutes": {
                "unmetered": 0.0,
                "total": 0.0,
                "metered": 0.0
            },
            "platform": "ANDROID_APP",
            "result": "PENDING",
            "billingMethod": "METERED",
            "type": "BUILTIN_EXPLORER",
            "arn": "{{Your ARN will be here}}",
            "counters": {
                "skipped": 0,
                "warned": 0,
                "failed": 0,
                "stopped": 0,
                "passed": 0,
                "errored": 0,
                "total": 0
            }
        }
    ]
}
```

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](#cli-ref).

### Stop a run (API)
<a name="how-to-stop-test-run-api"></a>
+ Call the [StopRun](../../latest/APIReference/API_StopRun.html) operation to the test run.

For information about using the Device Farm API, see [Automating Device Farm](#api-ref).

## Viewing a list of runs in AWS Device Farm
<a name="how-to-view-runs-list"></a>

You can use the Device Farm console, AWS CLI, or API to view a list of runs for a project.

**Topics**
+ [View a list of runs (console)](#how-to-view-runs-list-console)
+ [View a list of runs (AWS CLI)](#how-to-view-runs-list-cli)
+ [View a list of runs (API)](#how-to-view-runs-list-api)

### View a list of runs (console)
<a name="how-to-view-runs-list-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. In the list of projects, choose the project that corresponds to the list you want to view.
**Tip**  
You can use the search bar to filter the project list by name.

### View a list of runs (AWS CLI)
<a name="how-to-view-runs-list-cli"></a>
+ Run the [**list-runs**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/list-runs.html) command.

  To view information about a single run, run the [**get-run**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/get-run.html) command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](#cli-ref).

### View a list of runs (API)
<a name="how-to-view-runs-list-api"></a>
+ Call the [`ListRuns`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListRuns.html) API.

  To view information about a single run, call the [`GetRun`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRun.html) API.

For information about the Device Farm API, see [Automating Device Farm](#api-ref).

## Creating a device pool in AWS Device Farm
<a name="how-to-create-device-pool"></a>

You can use the Device Farm console, AWS CLI, or API to create a device pool.

**Topics**
+ [Prerequisites](#how-to-create-device-pool-prerequisites)
+ [Create a device pool (console)](#how-to-create-device-pool-console)
+ [Create a device pool (AWS CLI)](#how-to-create-device-pool-cli)
+ [Create a device pool (API)](#how-to-create-device-pool-api)

### Prerequisites
<a name="how-to-create-device-pool-prerequisites"></a>
+ Create a run in the Device Farm console. Follow the instructions in [Creating a test run in Device Farm](#how-to-create-test-run). When you get to the **Select devices** page, continue with the instructions in this section. 

### Create a device pool (console)
<a name="how-to-create-device-pool-console"></a>

1. On the **Projects** page, choose your project. In the **Project details** page, choose **Project settings**. In the **Device pools** tab, choose **Create device pool**.

1. For **Name**, enter a name that makes this device pool easy to identify.

1. For **Description**, enter a description that makes this device pool easy to identify.

1. If you want to use one or more selection criteria for the devices in this device pool, do the following:

   1. Choose **Create dynamic device pool**.

   1. Choose **Add a rule**.

   1. For **Field** (first drop-down list), choose one of the following:
      + To include devices by their manufacturer name, choose **Device Manufacturer**.
      + To include devices by their form factor (tablet or phone), choose **Form Factor**.
      + To include devices by their availability status based on load, choose **Availability**.
      + To include only public or private devices, choose **Fleet Type**.
      + To include devices by their operating system, choose **Platform**.
      + Some devices have an additional label tag or description about the device. You can find devices based on their label contents by choosing **Instance labels**.
      + To include devices by their operating system version, choose **OS Version**.
      + To include devices by their model, choose **Model**.

   1. For **Operator** (second drop-down list), choose a logical operation (EQUALS, CONTAINS, etc.) to include devices based on the query. For example, you could choose {{Availability EQUALS AVAILABLE}} to include devices that currently have the `Available` status.

   1. For **Value** (third drop-down list), enter or choose the value you want to specify for the **Field** and **Operator** values. Values are limited based on your **Field** choice. For example, if you choose **Platform** for **Field**, the only available selections are **ANDROID** and **IOS**. Similarly, if you choose **Form Factor** for **Field**, the only available selections are **PHONE** and **TABLET**.

   1. To add another rule, choose **Add a rule**. 

      After you create the first rule, in the list of devices, the box next to each device that matches the rule is selected. After you create or change rules, in the list of devices, the box next to each device that matches those combined rules is selected. Devices with selected boxes are included in the device pool. Devices with cleared boxes are excluded.

   1. Under **Max devices**, enter the number of devices you want to use in your device pool. If you do not enter the max number of devices, Device Farm will pick all devices in the fleet that match the rule(s) you created. To avoid additional charges, set this number to an amount that matches your actual parallel execution and device variety requirements.

   1. To delete a rule, choose **Remove rule**.

1. If you want to manually include or exclude individual devices, do the following:

   1. Choose **Create static device pool**.

   1. Select or clear the box next to each device. You can select or clear the boxes only if you do not have any rules specified.

1. If you want to include or exclude all displayed devices, select or clear the box in the column header row of the list. If you want to view private device instances only, choose **See private device instances only**.
**Important**  
Although you can use the boxes in the column header row to change the list of displayed devices, this does not mean that the remaining displayed devices are the only ones included or excluded. To confirm which devices are included or excluded, be sure to clear the contents of all of the boxes in the column header row, and then browse the boxes.

1. Choose **Create**.

### Create a device pool (AWS CLI)
<a name="how-to-create-device-pool-cli"></a>

**Tip**  
If you do not enter the max number of devices, Device Farm will pick all devices in the fleet that match the rule(s) you created. To avoid additional charges, set this number to an amount that matches your actual parallel execution and device variety requirements.
+ Run the [**create-device-pool**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-device-pool.html) command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](#cli-ref).

### Create a device pool (API)
<a name="how-to-create-device-pool-api"></a>

**Tip**  
If you do not enter the max number of devices, Device Farm will pick all devices in the fleet that match the rule(s) you created. To avoid additional charges, set this number to an amount that matches your actual parallel execution and device variety requirements.
+ Call the [`CreateDevicePool`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateDevicePool.html) API.

For information about using the Device Farm API, see [Automating Device Farm](#api-ref).

## Analyzing test results in AWS Device Farm
<a name="analyzing-results"></a>

With AWS Device Farm, you can choose from [two modes of execution](#test-environments): standard and custom mode. Standard mode was designed to provide granular reporting as a replacement for any test report that you might generate. The report contains test artifacts, such as videos and logs, presented separately for each test. When you choose standard mode, Device Farm does not guarantee that the test execution sequence matches your local execution order. Because it involves post-processing for each test, standard mode typically takes longer to execute compared to your local execution.

In contrast, custom mode generates the same reports you create locally for any framework. It also provides an optional detailed Test Insights report for each job and run when using select frameworks such as Appium TestNG, Instrumentation, and XCUITest. Because it does not involve separating individual test artifacts, this mode maintains parity with local execution in test sequencing and execution time. The generation of Test Insights happens asynchronously after your tests are complete.

Standard mode is not recommended for new test projects. We recommend using custom mode with Test Insights instead because it is flexible and can replicate the reports that standard mode provides for supported frameworks. Test Insights helps you understand your test suite performance at both the job and run level.

Test Insights include the following information:
+ Passed, failed, skipped, and errored test counts for each job and for each run
+ Detailed test output with timestamps and stack traces for each test, where applicable
+ Median test execution time for each job, and median and average job execution duration for each run

Regardless of the mode you choose, Device Farm gathers artifacts you can download after your test run completes. These include device and test logs, test spec output, network TCP dump, and screenshots. This information can help you analyze how your app is behaving on real devices, identify issues or bugs, and diagnose problems.

**Topics**
+ [Viewing test reports in Device Farm](#how-to-use-reports)
+ [Downloading artifacts in Device Farm](#artifacts)

### Viewing test reports in Device Farm
<a name="how-to-use-reports"></a>

Use the Device Farm console to view your test reports. For more information, see [Reports in AWS Device Farm](#reports).

**Topics**
+ [Prerequisites](#how-to-use-reports-prerequisites)
+ [View reports](#how-to-use-reports-viewing-reports)
+ [Device Farm test result statuses](#how-to-use-reports-displaying-results)

#### Prerequisites
<a name="how-to-use-reports-prerequisites"></a>

Set up a test run and verify that it is complete.

1.  To create a run, see [Creating a test run in Device Farm](#how-to-create-test-run), and then return to this page.

1. Verify that the run is complete. During your test run, the Device Farm console displays a pending icon ![Device Farm scheduled a job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-calendar.png) for runs that are in progress. Each device in the run will also start with the pending icon, then switch to the running ![Device Farm progress indicator.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-progress.png) icon when the test begins. As each test finishes, a test result icon is displayed next to the device name. When all tests have been completed, the pending icon next to the run changes to a test result icon. For more information, see [Device Farm test result statuses](#how-to-use-reports-displaying-results).

#### View reports
<a name="how-to-use-reports-viewing-reports"></a>

You can view the results of your test in the Device Farm console.

**Topics**
+ [View the test run summary page](#how-to-use-reports-console-summary)
+ [View unique problem reports](#how-to-use-reports-console-unique-problems)
+ [View device reports](#how-to-use-reports-console-by-device)
+ [View test suite reports](#how-to-use-reports-console-by-suite)
+ [View test reports](#how-to-use-reports-console-by-test)
+ [View log information for a problem, device, suite, or test in a report](#how-to-use-reports-console-log)

##### View the test run summary page
<a name="how-to-use-reports-console-summary"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. In the list of projects, choose the project for the run.
**Tip**  
To filter the project list by name, use the search bar.

1. Choose a completed run to view its summary report page.

1. The test run summary page displays an overview of your test results.
   + The **Unique problems** section lists unique warnings and failures. To view unique problems, follow the instructions in [View unique problem reports](#how-to-use-reports-console-unique-problems).
   + The **Devices** section displays the total number of tests, by outcome, for each device.

     ![Device Farm device summary results.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-device-summary-results-bar.png)

     In this example, there are several devices. In the first table entry, the Google Pixel 4 XL device running Android version 10 reports three successful tests that took 02:36 minutes to run.

     To view the results by device, follow the instructions in [View device reports](#how-to-use-reports-console-by-device).
   + The **Screenshots** section displays a list of any screenshots that Device Farm captured during the run, grouped by device.
   + In the **Parsing result** section, you can download the parsing result.

##### View unique problem reports
<a name="how-to-use-reports-console-unique-problems"></a>

1. In **Unique problems**, choose the problem that you want to view. 

1. Choose the device. The report displays information about the problem.

   The **Video** section displays a downloadable video recording of the test.

   The **Result** section displays the result of the test. The status is represented as a result icon. For more information, see [Statuses of an individual test](#how-to-use-reports-displaying-results-individual).

   The **Logs** section displays any information that Device Farm logged during the test. To view this information, follow the instructions in [View log information for a problem, device, suite, or test in a report](#how-to-use-reports-console-log).

   The **Files** tab displays a list of any of the test's associated files (such as log files) that you can download. To download a file, choose the file's link in the list.

   The **Screenshots** tab displays a list of any screenshots that Device Farm captured during the test.

##### View device reports
<a name="how-to-use-reports-console-by-device"></a>
+ In the **Devices** section, choose the device.

  The **Video** section displays a downloadable video recording of the test.

  The **Suites** section displays a table containing information about the suites for the device.

  In this table, the **Test results** column summarizes the number of tests by outcome for each of the test suites that have run on the device. This data also has a graphical component. For more information, see [Statuses for multiple tests](#how-to-use-reports-displaying-results-summary).

  To view the full results by suite, follow the instructions in [View test suite reports](#how-to-use-reports-console-by-suite).

  The **Logs** section displays any information that Device Farm logged for the device during the run. To view this information, follow the instructions in [View log information for a problem, device, suite, or test in a report](#how-to-use-reports-console-log).

  The **Files** section displays a list of suites for the device and any associated files (such as log files) that you can download. To download a file, choose the file's link in the list.

  The **Screenshots** section displays a list of any screenshots that Device Farm captured during the run for the device, grouped by suite.

##### View test suite reports
<a name="how-to-use-reports-console-by-suite"></a>

1. In the **Devices** section, choose the device.

1. In the **Suites** section, choose the suite from the table.

   The **Video** section displays a downloadable video recording of the test.

   The **Tests** section displays a table containing information about the tests in the suite.

   In the table, the **Test results** column displays the result. This data also has a graphical component. For more information, see [Statuses for multiple tests](#how-to-use-reports-displaying-results-summary).

   To view the full results by test, follow the instructions in [View test reports](#how-to-use-reports-console-by-test).

   The **Logs** section displays any information that Device Farm logged during the run for the suite. To view this information, follow the instructions in [View log information for a problem, device, suite, or test in a report](#how-to-use-reports-console-log).

   The **Files** section displays a list of tests for the suite and any associated files (such as log files) that you can download. To download a file, choose the file's link in the list.

   The **Screenshots** section displays a list of any screenshots that Device Farm captured during the run for the suite, grouped by test.

##### View test reports
<a name="how-to-use-reports-console-by-test"></a>

1. In the **Devices** section, choose the device.

1. In the **Suites** section, choose the suite.

1. In the **Tests** section, choose the test.

1. The **Video** section displays a downloadable video recording of the test.

   The **Result** section displays the result of the test. The status is represented as a result icon. For more information, see [Statuses of an individual test](#how-to-use-reports-displaying-results-individual).

   The **Logs** section displays any information that Device Farm logged during the test. To view this information, follow the instructions in [View log information for a problem, device, suite, or test in a report](#how-to-use-reports-console-log).

   The **Files** tab displays a list of any of the test's associated files (such as log files) that you can download. To download a file, choose the file's link in the list.

   The **Screenshots** tab displays a list of any screenshots that Device Farm captured during the test.

##### View log information for a problem, device, suite, or test in a report
<a name="how-to-use-reports-console-log"></a>

The **Logs** section displays the following information:
+ **Source** represents the source of a log entry. Possible values include:
  + **Harness** represents a log entry that Device Farm created. These log entries are typically created during start and stop events.
  + **Device** represents a log entry that the device created. For Android, these log entries are logcat-compatible. For iOS, these log entries are syslog-compatible.
  + **Test** represents a log entry that either a test or its test framework created.
+ **Time** represents the elapsed time between the first log entry and this log entry. The time is expressed in {{MM:SS.SSS}} format, where {{M}} represents minutes and {{S}} represents seconds.
+ **PID** represents the process identifier (PID) that created the log entry. All log entries created by an app on a device have the same PID.
+ **Level** represents the logging level for the log entry. For example, `Logger.debug("This is a message!")` logs a **Level** of `Debug`. These are the possible values:
  + **Alert**
  + **Critical**
  + **Debug**
  + **Emergency**
  + **Error**
  + **Errored**
  + **Failed**
  + **Info**
  + **Internal**
  + **Notice**
  + **Passed**
  + **Skipped**
  + **Stopped**
  + **Verbose**
  + **Warned**
  + **Warning**
+ **Tag** represents arbitrary metadata for the log entry. For example, Android logcat can use this to describe which part of the system created the log entry (for example, `ActivityManager`).
+ **Message** represents the message or data for the log entry. For example, `Logger.debug("Hello, World!")` logs a **Message** of `"Hello, World!"`.

To display only a portion of the information:
+ To show all log entries that match a value for a specific column, enter the value into the search bar. For example, to show all log entries with a **Source** value of `Harness`, enter **Harness** in the search bar.
+ To remove all of the characters from a column header box, choose the **X** in that column header box. Removing all of the characters from a column header box is the same as entering **\*** in that column header box.

To download all of the log information for the device, including all of the suites and tests that you ran, choose **Download logs**.

#### Device Farm test result statuses
<a name="how-to-use-reports-displaying-results"></a>

The Device Farm console displays icons that help you quickly assess the state of your completed test run. For more information about tests in Device Farm, see [Reports in AWS Device Farm](#reports).

**Topics**
+ [Statuses of an individual test](#how-to-use-reports-displaying-results-individual)
+ [Statuses for multiple tests](#how-to-use-reports-displaying-results-summary)

##### Statuses of an individual test
<a name="how-to-use-reports-displaying-results-individual"></a>

For reports that describe an individual test, Device Farm displays an icon representing the test result status:


| Description | Icon | 
| --- | --- | 
| The test succeeded. | ![The test succeeded.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-success.png) | 
| The test failed. | ![The test failed.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-failure.png) | 
| Device Farm skipped the test. | ![The test was skipped.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-skipped.png) | 
| The test stopped. | ![The test was stopped.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-stopped.png) | 
| Device Farm returned a warning. | ![Device Farm returned a warning.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-warning.png) | 
| Device Farm returned an error. | ![Device Farm returned an error.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-error.png) | 

##### Statuses for multiple tests
<a name="how-to-use-reports-displaying-results-summary"></a>

If you choose a finished run, Device Farm displays a summary graph showing the percentage of tests in various states.

![Device Farm test results summary graph.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-summary-results-graph.png)

For example, this test run results graph shows that the run had 4 stopped tests, 1 failed test, and 10 successful tests.

Graphs are always color coded and labeled.

### Downloading artifacts in Device Farm
<a name="artifacts"></a>

Device Farm gathers artifacts such as reports, log files, and images for each test in the run.

You can download artifacts created during your test run:

**Files**  
Files generated during the test run including Device Farm reports. For more information, see [Viewing test reports in Device Farm](#how-to-use-reports).

**Logs**  
Output from each test in the test run.

**Screenshots**  
Screen images recorded for each test in the test run.

![Diagram showing AWS Device Farm workflow from Project to Run to Job on device to Test suite to Test.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/hierarchy.png)


#### Download artifacts (console)
<a name="artifacts-console"></a>

1. On the test run report page, from **Devices**, choose a mobile device.

1. To download a file, choose one from **Files**.

1. To download the logs from your test run, from **Logs**, choose **Download logs**.

1. To download a screenshot, choose a screenshot from **Screenshots**.

For more information about downloading artifacts in a custom test environment, see [Downloading artifacts in a custom test environment](#using-artifacts-custom).

#### Download artifacts (AWS CLI)
<a name="artifacts-cli"></a>

You can use the AWS CLI to list your test run artifacts.

**Topics**
+ [Step 1: Get your Amazon Resource Names (ARN)](#artifacts-cli-step1)
+ [Step 2: List your artifacts](#artifacts-cli-step2)
+ [Step 3: Download your artifacts](#artifacts-cli-step3)

##### Step 1: Get your Amazon Resource Names (ARN)
<a name="artifacts-cli-step1"></a>

You can list your artifacts by run, job, test suite, or test. You need the corresponding ARN. This table shows the input ARN for each of the AWS CLI list commands:


| AWS CLI List Command | Required ARN | 
| --- | --- | 
| list-projects | This command returns all projects and does not require an ARN. | 
| list-runs | project | 
| list-jobs | run | 
| list-suites | job | 
| list-tests | suite | 

For example, to find a test ARN, run **list-tests** using your test suite ARN as an input parameter.

Example:

```
aws devicefarm list-tests –-arn {{arn:MyTestSuiteARN}}
```

The response includes a test ARN for each test in the test suite.

```
{
    "tests": [
        {
            "status": "COMPLETED",
            "name": "Tests.FixturesTest.testExample",
            "created": 1537563725.116,
            "deviceMinutes": {
                "unmetered": 0.0,
                "total": 1.89,
                "metered": 1.89
            },
            "result": "PASSED",
            "message": "testExample passed",
            "arn": "arn:aws:devicefarm:us-west-2:123456789101:test:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
            "counters": {
                "skipped": 0,
                "warned": 0,
                "failed": 0,
                "stopped": 0,
                "passed": 1,
                "errored": 0,
                "total": 1
            }
        }
    ]
}
```

##### Step 2: List your artifacts
<a name="artifacts-cli-step2"></a>

The AWS CLI [list-artifacts](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/list-artifacts.html) command returns a list of artifacts, such as files, screenshots, and logs. Each artifact has a URL so you can download the file.
+ Call **list-artifacts** specifying a run, job, test suite, or test ARN. Specify a type of FILE, LOG, or SCREENSHOT.

  This example returns a download URL for each artifact available for an individual test:

  ```
  aws devicefarm list-artifacts --arn {{arn:MyTestARN}} --type "FILE"
  ```

  The response contains a download URL for each artifact.

  ```
  {
      "artifacts": [
          {
              "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
              "extension": "txt",
              "type": "APPIUM_JAVA_OUTPUT",
              "name": "Appium Java Output",
              "arn": "arn:aws:devicefarm:us-west-2:123456789101:artifact:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
          }
      ]
  }
  ```

##### Step 3: Download your artifacts
<a name="artifacts-cli-step3"></a>
+ Download your artifact using the URL from the previous step. This example uses **curl** to download an Android Appium Java output file:

  ```
  curl "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL" > {{MyArtifactName.txt}}
  ```

#### Download artifacts (API)
<a name="artifacts-api"></a>

The Device Farm API [ListArtifacts](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) method returns a list of artifacts, such as files, screenshots, and logs. Each artifact has a URL so you can download the file.

#### Downloading artifacts in a custom test environment
<a name="using-artifacts-custom"></a>

In a custom test environment, Device Farm gathers artifacts such as custom reports, log files, and images. These artifacts are available for each device in the test run.

You can download these artifacts created during your test run:

**Test spec output**  
The output from running the commands in the test spec YAML file.

**Customer artifacts**  
A zipped file that contains the artifacts from the test run. It is configured in the **artifacts:** section of your test spec YAML file.

**Test spec shell script**  
An intermediate shell script file created from your YAML file. Because it is used in the test run, the shell script file can be used for debugging the YAML file.

**Test spec file**  
The YAML file used in the test run.

For more information, see [Downloading artifacts in Device Farm](#artifacts).

![Device Farm hierarchy of operations in a custom test environment](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/hierarchy.png)


# Tagging AWS Device Farm resources
<a name="tagging"></a>

AWS Device Farm works with the AWS Resource Groups Tagging API. This API allows you to manage resources in your AWS account with *tags*. You can add tags to resources, such as projects and test runs. 

You can use tags to:
+ Organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with an application name, and then organize your billing information to see the total cost of that application across several services. For more information, see [Cost Allocation and Tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in *About AWS Billing and Cost Management*. 
+ Control access through IAM policies. To do so, create a policy that allows access to a resource or set of resources using a tag value condition.
+ Identify and manage runs that have certain properties as tags, such as the branch used for testing. 

 For more information about tagging resources, see the [Tagging Best Practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) whitepaper. 

**Topics**
+ [Tagging resources](#tagging-resources)
+ [Looking up resources by tag](#tagging-looking-up-resources)
+ [Removing tags from resources](#tagging-removing-tags)

## Tagging resources
<a name="tagging-resources"></a>

The AWS Resource Group Tagging API allows you to add, remove, or modify tags on resources. For more information, see the [AWS Resource Group Tagging API Reference](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html). 

To tag a resource, use the [`TagResources`](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) operation from the `resourcegroupstaggingapi` endpoint. This operation takes a list of ARNs from supported services and a list of key-value pairs. The value is optional. An empty string indicates that there should be no value for that tag. For example, the following Python example tags a series of project ARNs with the tag `build-config` with the value `release`:

```
import boto3

client = boto3.client('resourcegroupstaggingapi')

client.tag_resources(ResourceARNList=["arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655440000",
                                      "arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655441111",
                                      "arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655442222"]
                     Tags={"build-config":"release", "git-commit":"8fe28cb"})
```

A tag value is not required. To set a tag with no value, use an empty string (`""`) when specifying a value. A tag can only have one value. Any previous value a tag has for a resource will be overwritten with the new value. 

## Looking up resources by tag
<a name="tagging-looking-up-resources"></a>

To look up resources by their tags, use the `GetResources` operation from the `resourcegrouptaggingapi` endpoint. This operation takes a series of filters, none of which are required, and returns the resources that match the given criteria. With no filters, all tagged resources are returned. The `GetResources` operation allows you to filter resources based on
+ Tag value
+ Resource type (for example, `devicefarm:run`)

For more information, see the [AWS Resource Group Tagging API Reference](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html).

The following example looks up Device Farm desktop browser testing sessions (`devicefarm:testgrid-session` resources) with the tag `stack` that have the value `production`:

```
import boto3
client = boto3.client('resourcegroupstaggingapi')
sessions = client.get_resources(ResourceTypeFilters=['devicefarm:testgrid-session'],
                                TagFilters=[
                                  {"Key":"stack","Values":["production"]}
                                ])
```

## Removing tags from resources
<a name="tagging-removing-tags"></a>

To remove a tag, use the `UntagResources` operation, specifying a list of resources and the tags to remove:

```
import boto3
client = boto3.client('resourcegroupstaggingapi')
client.UntagResources(ResourceARNList=["arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655440000"], TagKeys=["RunCI"])
```

# Test frameworks and built-in tests in AWS Device Farm
<a name="test-types"></a>

This section describes Device Farm support for testing frameworks and built-in test types.

Device Farm runs automated tests by having you upload your app and tests to a secure Amazon S3 bucket managed by the service. Once uploaded, it spins up the underlying infrastructure, including service-managed [test hosts](#custom-test-environments-hosts), and executes the tests in parallel on multiple devices. The test results are stored in a service managed S3 bucket. This architecture is called **service-side execution**, and is a fast and efficient way to run tests on hosts that are physically close to the device, without needing to manage the test host infrastructure yourself. This approach scales well for testing on many devices independently, as well as testing from the context of a CI/CD pipeline.

For more information about how Device Farm runs tests, see [Test environments in AWS Device Farm](#test-environments).

**Note**  
For Appium testers, you may prefer to run your Appium tests from your local environment. With a [remote access session](#remote-access), you can run **client-side** Appium tests. For more information, please see [client-side Appium testing](#appium-endpoint).

## Testing frameworks
<a name="test-types-framework"></a>

Device Farm supports these mobile automation testing frameworks:

### Android application testing frameworks
<a name="test-types-framework-android-list"></a>
+ [Automatic Appium tests](#test-types-appium)
+ [Instrumentation](#test-types-android-instrumentation)

### iOS application testing frameworks
<a name="test-types-framework-ios-list"></a>
+ [Automatic Appium tests](#test-types-appium)
+ [XCTest](#test-types-ios-xctest)
+ [XCTest UI](#test-types-ios-xctest-ui)

### Web application testing frameworks
<a name="test-types-framework-web-app-list"></a>

Web applications are supported using Appium. For more information on bringing your tests to Appium, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### Frameworks in a custom test environment
<a name="test-types-framework-custom-support"></a>

Device Farm does not provide support for customizing the test environment for the XCTest framework. For more information, see [Custom test environments in AWS Device Farm](#custom-test-environments).

### Appium version support
<a name="test-types-framework-appium"></a>

For tests running in a custom environment, Device Farm supports Appium version 1. For more information, see [Test environments in AWS Device Farm](#test-environments).

## Built-in test types
<a name="test-types-built-in"></a>

With built-in tests, you can test your application on multiple devices without having to write and maintain test automation scripts. Device Farm offers one built-in test type:
+ [Built-in: fuzz (Android and iOS)](#test-types-built-in-fuzz)

## Automatically run Appium tests in Device Farm
<a name="test-types-appium"></a><a name="test-types-ios-appium-java-testng"></a><a name="test-types-ios-appium-java-junit"></a><a name="test-types-ios-appium-python"></a><a name="test-types-ios-appium-ruby"></a><a name="test-types-ios-appium-node"></a><a name="test-types-android-appium-java-testng"></a><a name="test-types-android-appium-java-junit"></a><a name="test-types-android-appium-python"></a><a name="test-types-android-appium-ruby"></a><a name="test-types-android-appium-node"></a><a name="test-types-web-app-appium-java-testng"></a><a name="test-types-web-app-appium-java-junit"></a><a name="test-types-web-app-appium-python"></a><a name="test-types-web-app-appium-ruby"></a><a name="test-types-web-app-appium-node"></a>

**Note**  
This page covers running Appium tests in Device Farm's managed **server-side** execution environment. To run Appium tests from your local **client-side** environment during a remote access session, see [client-side Appium testing](#appium-endpoint).

This section describes how to configure, package, and upload your Appium tests for running on Device Farm's managed server-side environment. Appium is an open source tool for automating native and mobile web applications. For more information, see [Introduction to Appium](http://appium.io/docs/en/latest/intro) on the Appium website.

For a sample app and links to working tests, see [Device Farm Sample App for Android](https://github.com/aws-samples/aws-device-farm-sample-app-for-android) and [Device Farm Sample App for iOS](https://github.com/aws-samples/aws-device-farm-sample-app-for-ios) on GitHub.

For more information about testing in Device Farm and how server-side works, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

### Selecting an Appium version
<a name="w2aac24c15c41"></a>

**Note**  
 Support for specific Appium versions, Appium drivers, or programming SDKs will depend on the device and test host selected for the test run. 

 Device Farm test hosts come pre-installed with Appium in order to enable quicker setup of tests for more straightforward use cases. However, the use of the test spec file allows you to install differing versions of Appium if needed. 

#### Scenario 1: Pre-configured Appium version
<a name="w2aac24c15c41b7b1"></a>

 Device Farm comes pre-configured with different Appium server versions based on the test host. The host comes with tooling that enables the pre-configured version with the device platform's default driver (UiAutomator2 for Android, and XCUITest for iOS). For example, on the macos\_tahoe test host, Appium 3 is the default version and comes preinstalled with a compatible XCUITest driver for iOS. 

```
phases:
  install:
    commands:
      - export APPIUM_VERSION={{3}}
      - devicefarm-cli use appium $APPIUM_VERSION
```

 To view a list of supported software, see the topic on [Supported software within custom test environments](#custom-test-environments-hosts-software). 

#### Scenario 2: Custom Appium version
<a name="w2aac24c15c41b7b3"></a>

 To select a custom version of Appium, use the `npm` command to install it. The following example shows how to install the latest version of Appium 2. 

```
phases:
  install:
    commands:
      - export APPIUM_VERSION={{2}}
      - npm install -g appium@$APPIUM_VERSION
```

#### Scenario 3: Appium on Legacy iOS hosts
<a name="w2aac24c15c41b7b5"></a>

 On the [Legacy iOS test host](#legacy-ios-host), you can choose specific Appium versions with `avm`. For example, to use the `avm` command to set the Appium server version to `2.1.2`, add these commands to your test spec YAML file. 

```
phases:
  install:
    commands:
      - export APPIUM_VERSION={{2.1.2}}
      - avm $APPIUM_VERSION
```

### Selecting a WebDriverAgent version for iOS tests
<a name="test-types-appium-select-wda"></a>

 In order to run Appium tests on iOS devices, the use of WebDriverAgent is required. This application must be signed in order to be installed on iOS devices. Device Farm provides pre-signed versions of WebDriverAgent that are available during custom test environment runs. 

 The following code snippet can be used to select a WebDriverAgent version on Device Farm within your test spec file that is compatible with your XCTestUI Driver version.. 

```
phases:
  pre_test:
    commands:
      - |-
        APPIUM_DRIVER_VERSION=$(appium driver list --installed --json | jq -r ".xcuitest.version" | cut -d "." -f 1);
        CORRESPONDING_APPIUM_WDA=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V${APPIUM_DRIVER_VERSION}")
        if [[ ! -z "$APPIUM_DRIVER_VERSION" ]] && [[ ! -z "$CORRESPONDING_APPIUM_WDA" ]]; then
          echo "Using a prebuilt version of the WDA app corresponding with your XCUITest driver version ${APPIUM_DRIVER_VERSION}";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $CORRESPONDING_APPIUM_WDA | cut -d "=" -f2)
        else
          LATEST_SUPPORTED_WDA_VERSION=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V" | sort -V -r | head -n 1)
          echo "Unknown driver version $APPIUM_DRIVER_VERSION; falling back to the Device Farm default version of $LATEST_SUPPORTED_WDA_VERSION";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $LATEST_SUPPORTED_WDA_VERSION | cut -d "=" -f2)
        fi;
```

 For more information about the WebDriverAgent, see Appium's [ documentation](https://appium.github.io/appium-xcuitest-driver/9.10/guides/run-prebuilt-wda/). 

### Integrating Appium tests with Device Farm
<a name="test-types-appium-integrate"></a>

Use the following instructions to integrate Appium tests with AWS Device Farm. For more information about using Appium tests in Device Farm, see [Automatically run Appium tests in Device Farm](#test-types-appium).

#### Configure your Appium test package
<a name="test-types-appium-prepare"></a>

Use the following instructions to configure your test package.

------
#### [ Java (JUnit) ]

1. Modify `pom.xml` to set packaging to a JAR file:

   ```
   <groupId>com.acme</groupId>
   <artifactId>acme-myApp-appium</artifactId>
   <version>1.0-SNAPSHOT</version>
   <packaging>jar</packaging>
   ```

1. Modify `pom.xml` to use `maven-jar-plugin` to build your tests into a JAR file.

   The following plugin builds your test source code (anything in the `src/test` directory) into a JAR file:

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-jar-plugin</artifactId>
     <version>2.6</version>
     <executions>
       <execution>
         <goals>
           <goal>test-jar</goal>
         </goals>
       </execution>
     </executions>
   </plugin>
   ```

1. Modify `pom.xml` to use `maven-dependency-plugin` to build dependencies as JAR files.

   The following plugin copies your dependencies into the `dependency-jars` directory: 

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-dependency-plugin</artifactId>
     <version>2.10</version>
     <executions>
       <execution>
         <id>copy-dependencies</id>
         <phase>package</phase>
         <goals>
           <goal>copy-dependencies</goal>
         </goals>
         <configuration>
           <outputDirectory>${project.build.directory}/dependency-jars/</outputDirectory>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

1. Save the following XML assembly to `src/main/assembly/zip.xml`.

   The following XML is an assembly definition that, when configured, instructs Maven to build a .zip file that contains everything in the root of your build output directory and the `dependency-jars` directory: 

   ```
   <assembly
       xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0 http://maven.apache.org/xsd/assembly-1.1.0.xsd">
     <id>zip</id>
     <formats>
       <format>zip</format>
     </formats>
     <includeBaseDirectory>false</includeBaseDirectory>
     <fileSets>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>*.jar</include>
         </includes>
       </fileSet>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>/dependency-jars/</include>
         </includes>
       </fileSet>
     </fileSets>
   </assembly>
   ```

1. Modify `pom.xml` to use `maven-assembly-plugin` to package tests and all dependencies into a single .zip file.

   The following plugin uses the preceding assembly to create a .zip file named `zip-with-dependencies` in the build output directory every time **mvn package** is run: 

   ```
   <plugin>
     <artifactId>maven-assembly-plugin</artifactId>
     <version>2.5.4</version>
     <executions>
       <execution>
         <phase>package</phase>
         <goals>
           <goal>single</goal>
         </goals>
         <configuration>
           <finalName>zip-with-dependencies</finalName>
           <appendAssemblyId>false</appendAssemblyId>
           <descriptors>
             <descriptor>src/main/assembly/zip.xml</descriptor>
           </descriptors>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

**Note**  
If you receive an error that says annotation is not supported in 1.3, add the following to `pom.xml`:  

```
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>1.7</source>
    <target>1.7</target>
  </configuration>
</plugin>
```

------
#### [ Java (TestNG) ]

1. Modify `pom.xml` to set packaging to a JAR file:

   ```
   <groupId>com.acme</groupId>
   <artifactId>acme-myApp-appium</artifactId>
   <version>1.0-SNAPSHOT</version>
   <packaging>jar</packaging>
   ```

1. Modify `pom.xml` to use `maven-jar-plugin` to build your tests into a JAR file.

   The following plugin builds your test source code (anything in the `src/test` directory) into a JAR file:

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-jar-plugin</artifactId>
     <version>2.6</version>
     <executions>
       <execution>
         <goals>
           <goal>test-jar</goal>
         </goals>
       </execution>
     </executions>
   </plugin>
   ```

1. Modify `pom.xml` to use `maven-dependency-plugin` to build dependencies as JAR files.

   The following plugin copies your dependencies into the `dependency-jars` directory: 

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-dependency-plugin</artifactId>
     <version>2.10</version>
     <executions>
       <execution>
         <id>copy-dependencies</id>
         <phase>package</phase>
         <goals>
           <goal>copy-dependencies</goal>
         </goals>
         <configuration>
           <outputDirectory>${project.build.directory}/dependency-jars/</outputDirectory>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

1. Save the following XML assembly to `src/main/assembly/zip.xml`.

   The following XML is an assembly definition that, when configured, instructs Maven to build a .zip file that contains everything in the root of your build output directory and the `dependency-jars` directory: 

   ```
   <assembly
       xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0 http://maven.apache.org/xsd/assembly-1.1.0.xsd">
     <id>zip</id>
     <formats>
       <format>zip</format>
     </formats>
     <includeBaseDirectory>false</includeBaseDirectory>
     <fileSets>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>*.jar</include>
         </includes>
       </fileSet>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>/dependency-jars/</include>
         </includes>
       </fileSet>
     </fileSets>
   </assembly>
   ```

1. Modify `pom.xml` to use `maven-assembly-plugin` to package tests and all dependencies into a single .zip file.

   The following plugin uses the preceding assembly to create a .zip file named `zip-with-dependencies` in the build output directory every time **mvn package** is run: 

   ```
   <plugin>
     <artifactId>maven-assembly-plugin</artifactId>
     <version>2.5.4</version>
     <executions>
       <execution>
         <phase>package</phase>
         <goals>
           <goal>single</goal>
         </goals>
         <configuration>
           <finalName>zip-with-dependencies</finalName>
           <appendAssemblyId>false</appendAssemblyId>
           <descriptors>
             <descriptor>src/main/assembly/zip.xml</descriptor>
           </descriptors>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

**Note**  
If you receive an error that says annotation is not supported in 1.3, add the following to `pom.xml`:  

```
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>1.7</source>
    <target>1.7</target>
  </configuration>
</plugin>
```

------
#### [ Node.JS ]

To package your Appium Node.js tests and upload them to Device Farm, you must install the following on your local machine:
+ [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm) 

  Use this tool when you develop and package your tests so that unnecessary dependencies are not included in your test package.
+ Node.js
+ npm-bundle (installed globally)

1. Verify that nvm is present

   ```
   command -v nvm
   ```

   You should see `nvm` as output.

   For more information, see [nvm](https://github.com/nvm-sh/nvm) on GitHub.

1. Run this command to install Node.js:

   ```
   nvm install node
   ```

   You can specify a particular version of Node.js:

   ```
   nvm install 11.4.0
   ```

1. Verify that the correct version of Node is in use:

   ```
   node -v
   ```

1. Install **npm-bundle** globally:

   ```
   npm install -g npm-bundle
   ```

------
#### [ Python ]

1. We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for developing and packaging tests so that unnecessary dependencies are not included in your app package.

   ```
   $ virtualenv workspace
   $ cd workspace
   $ source bin/activate
   ```
**Tip**  
Do not create a Python virtualenv with the `--system-site-packages` option, because it inherits packages from your global site-packages directory. This can result in including dependencies in your virtual environment that are not required by your tests.
You should also verify that your tests do not use dependencies that are dependent on native libraries, because these native libraries might not be present on the instance where these tests run.

1. Install **py.test** in your virtual environment.

   ```
   $ pip install pytest
   ```

1. Install the Appium Python client in your virtual environment.

   ```
   $ pip install Appium-Python-Client
   ```

1. Unless you specify a different path in custom mode, Device Farm expects your tests to be stored in `tests/`. You can use `find` to show all files inside a folder:

   ```
   $ find tests/
   ```

   Confirm that these files contain test suites you wand to run on Device Farm

   ```
   tests/
   tests/{{my-first-tests.py}}
   tests/{{my-second-tests/py}}
   ```

1. Run this command from your virtual environment workspace folder to show a list of your tests without running them.

   ```
   $ py.test --collect-only tests/
   ```

   Confirm the output shows the tests that you want to run on Device Farm.

1. Clean all cached files under your tests/ folder:

   ```
   $ find . -name '__pycache__' -type d -exec rm -r {} +
   $ find . -name '*.pyc' -exec rm -f {} +
   $ find . -name '*.pyo' -exec rm -f {} +
   $ find . -name '*~' -exec rm -f {} +
   ```

1. Run the following command in your workspace to generate the requirements.txt file:

   ```
   $ pip freeze > requirements.txt
   ```

------
#### [ Ruby ]

To package your Appium Ruby tests and upload them to Device Farm, you must install the following on your local machine:
+ [Ruby Version Manager (RVM)](https://rvm.io/rvm/install)

  Use this command-line tool when you develop and package your tests so that unnecessary dependencies are not included in your test package. 
+ Ruby
+ Bundler (This gem is typically installed with Ruby.)

1. Install the required keys, RVM, and Ruby. For instructions, see [Installing RVM](https://rvm.io/rvm/install) on the RVM website.

   After the installation is complete, reload your terminal by signing out and then signing in again.
**Note**  
RVM is loaded as a function for the bash shell only.

1. Verify that **rvm** is installed correctly

   ```
   command -v rvm
   ```

   You should see `rvm` as output.

1. If you want to install a specific version of Ruby, such as {{2.5.3}}, run the following command:

   ```
   rvm install ruby 2.5.3 --autolibs=0
   ```

   Verify that you are on the requested version of Ruby:

   ```
   ruby -v
   ```

1. Configure the bundler to compile packages for your desired testing platforms:

   ```
   bundle config specific_platform true
   ```

1. Update your .lock file to add the platforms needed to run tests.
   + If you're compiling tests to run on Android devices, then run this command to configure the Gemfile to use dependencies for the Android test host:

     ```
     bundle lock --add-platform x86_64-linux
     ```
   + If you're compiling tests to run on iOS devices, then run this command to configure the Gemfile to use dependencies for the iOS test host:

     ```
     bundle lock --add-platform x86_64-darwin
     ```

1. The **bundler** gem is usually installed by default. If it is not, install it:

   ```
   gem install bundler -v 2.3.26
   ```

------

#### Create a zipped test package file
<a name="test-types-appium-create-a-zip"></a>

**Warning**  
In Device Farm, the folder structure of files in your zipped test package matters, and some archival tools will change the structure of your ZIP file implicitly. We recommend that you follow the specified command-line utilities below rather than use the archival utilities built into the file manager of your local desktop (such as Finder or Windows Explorer).

Now, bundle your tests for Device Farm.

------
#### [ Java (JUnit) ]

Build and package your tests:

```
$ mvn clean package -DskipTests=true
```

The file `zip-with-dependencies.zip` will be created as a result. This is your test package.

------
#### [ Java (TestNG) ]

Build and package your tests:

```
$ mvn clean package -DskipTests=true
```

The file `zip-with-dependencies.zip` will be created as a result. This is your test package.

------
#### [ Node.JS ]

1. Check out your project.

   Make sure you are at the root directory of your project. You can see `package.json` at the root directory.

1. Run this command to install your local dependencies.

   ```
   npm install
   ```

   This command also creates a `node_modules` folder inside your current directory.
**Note**  
At this point, you should be able to run your tests locally.

1. Run this command to package the files in your current folder into a \*.tgz file. The file is named using the `name` property in your `package.json` file.

   ```
   npm-bundle
   ```

   This tarball (.tgz) file contains all your code and dependencies.

1. Run this command to bundle the tarball (\*.tgz file) generated in the previous step into a single zipped archive:

   ```
   zip -r {{MyTests.zip}} *.tgz
   ```

   This is the `MyTests.zip` file that you upload to Device Farm in the following procedure.

------
#### [ Python ]

Python 2  
Generate an archive of the required Python packages (called a "wheelhouse") using pip:  

```
$ pip wheel --wheel-dir wheelhouse -r requirements.txt
```
Package your wheelhouse, tests, and pip requirements into a zip archive for Device Farm:  

```
$ zip -r {{test_bundle.zip}} tests/ wheelhouse/ requirements.txt
```

Python 3  
Package your tests and pip requirements into a zip file:  

```
$ zip -r {{test_bundle.zip}} tests/ requirements.txt
```

------
#### [ Ruby ]

1. Run this command to create a virtual Ruby environment:

   ```
   # myGemset is the name of your virtual Ruby environment
   rvm gemset create {{myGemset}}
   ```

1. Run this command to use the environment you just created:

   ```
   rvm gemset use {{myGemset}}
   ```

1. Check out your source code.

   Make sure you are at the root directory of your project. You can see `Gemfile` at the root directory.

1. Run this command to install your local dependencies and all gems from the `Gemfile`:

   ```
   bundle install
   ```
**Note**  
At this point, you should be able to run your tests locally. Use this command to run a test locally:  

   ```
   bundle exec $test_command
   ```

1. Package your gems in the `vendor/cache` folder.

   ```
   # This will copy all the .gem files needed to run your tests into the vendor/cache directory
   bundle package --all-platforms
   ```

1. Run the following command to bundle your source code, along with all your dependencies, into a single zipped archive:

   ```
   zip -r MyTests.zip Gemfile vendor/ $(any other source code directory files)
   ```

   This is the `MyTests.zip` file that you upload to Device Farm in the following procedure.

------

#### Run your Appium tests
<a name="test-types-appium-upload"></a>

You can use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. If you are a new user, choose **New project**, enter a name for the project, and then choose **Submit**. If you already have a project, you can choose it to upload your tests to it.

1. Open your project, and then choose **Create run**.

1. Under **Select app and run type**, in the **Run type** section, select your run type. Select **Android app** if you are testing an Android app (.apk file format). Select **iOS app** if you are testing an iOS app (.ipa file format). Select **Web App** if you are testing a mobile web application.

1. Under **Select app**, in the **App selection options** section, choose **Select sample app provided by Device Farm** if you do not have an app. If you are bringing your own app, select **Upload own app**. Then choose your APK (.apk file format) for Android or your IPA (.ipa file format) for iOS. If you are uploading an iOS app, make sure that you choose **iOS device**, not a simulator.

1. Under **Configure test**, in the **Select test framework** section, choose the Appium framework that you test with, and then select **Upload your own test package**. Browse to and choose the .zip file that contains your tests. The .zip file must follow the format described in [Configure your Appium test package](#test-types-appium-prepare).

1. You can use the default test spec, or choose **Upload own test spec** to provide your own.

1. Under **Select devices**, choose a device selection method. Select **Use Device Pool** to choose from a curated collection of devices or a custom device pool you created. Select **Manually select devices** to pick individual devices to run your tests against. The **Device compatibility** section shows how many devices in the selected pool are compatible with your app. For more information, see [Device support in AWS Device Farm](#devices).

1. (Optional) To configure run-level properties, update the **Run settings** section:
   + Device Farm currently supports test insights only for Appium TestNG. To have Device Farm generate a test report after your run completes, select **Generate test report**. This option is available in a custom test environment only.

     The following prerequisites apply:
     + Your tests must generate a `testng-results.xml` file and write it to `$DEVICEFARM_LOG_DIR`. For example, pass `-d $DEVICEFARM_LOG_DIR/test-output` to the TestNG command in your test spec file. The default Appium Java TestNG test spec produces and stores this file automatically if you keep the default configuration.

1. Choose **Confirm and start run**. For more information, see [Creating a test run in Device Farm](#how-to-create-test-run).

**Note**  
Device Farm does not modify Appium tests.

#### View a test report
<a name="test-types-appium-view-insights"></a>

After your run completes, Device Farm generates a test report for each device. The report shows a per-test breakdown, including each test's name, class, result, and duration, plus a stack trace for any failed test. You can view the test report in the console or retrieve it through the API.

To open a completed job in the Device Farm console:

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Choose the project that contains the run you want to inspect.

1. Choose the completed run to open its details.

1. Choose one of the completed jobs to open the results for that device.

What you see in the job results depends on the test framework and whether you enabled test insights. Choose your framework tab to view the results.

------
#### [ Java (TestNG) ]

The job results include a **Test report** tab. Choose it to see a per-test breakdown. The following screenshot shows the **Test report** tab.

![The Test report tab for a completed Appium Java TestNG job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-testng-insights-enabled-test-report-column.png)


The tab shows the following fields for each test:

`testName`  
The name of the test method.

`testClass`  
The name of the test class.

`result`  
The Device Farm result for the test.

`frameworkResult`  
The result that TestNG reported (`PASS`, `FAIL`, or `SKIP`). Device Farm maps this value to the normalized `result` field.

`durationSeconds`  
The duration of the test, in seconds.

`startTimestamp`  
The time when the test started.

`endTimestamp`  
The time when the test ended.

`params`  
For a parameterized test, the parameter values that TestNG passed to the test.

`stackTrace`  
For a failed test, the stack trace of the failure.

To download the full test report as a JSON file, choose **Download full summary** at the top of the job details.

To choose which columns appear, choose the gear icon. In the settings, you can select the columns to display and turn **Group by class** on or off. **Group by class** is on by default, which groups the tests by their test class. Turn it off to see a flat list of all tests, as shown in the following screenshot.

![The Test report tab with Group by class turned off, showing a flat list of tests.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-testng-insights-enabled-test-report-without-grouping.png)


The job results show the standard test output and artifacts, but no **Test report** tab. To generate a test report, schedule a new run with test insights enabled.

![The job results for a completed Appium Java TestNG job without test insights enabled.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-disabled-test-report.png)


Run **get-job** and specify the job ARN:

```
aws devicefarm get-job --arn {{arn:aws:devicefarm:us-west-2:123456789012:job:PROJECT_ID/RUN_ID/00000}}
```

If you did not enable test insights, the response contains the standard job fields, such as the job status, result, counters, and device:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "name": "Example Android Phone",
        "created": "2026-07-31T16:58:20.000000-07:00",
        "status": "COMPLETED",
        "result": "FAILED",
        "counters": {
            "total": 3,
            "passed": 1,
            "failed": 1,
            "warned": 0,
            "errored": 0,
            "stopped": 0,
            "skipped": 1
        },
        "device": {
            "arn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
            "name": "Example Android Phone",
            "platform": "ANDROID",
            "os": "14",
            "formFactor": "PHONE",
            "fleetType": "PUBLIC"
        },
        "deviceMinutes": {
            "total": 1.42,
            "metered": 0.0,
            "unmetered": 1.17
        },
        "videoCapture": true
    }
}
```

If you enabled test insights, the response also includes an `insights` object. This object contains the test report status, high-level metrics, and a presigned URL to the detailed report:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "status": "COMPLETED",
        "result": "FAILED",
        "counters": { ... },
        "device": { ... },
        "deviceMinutes": { ... },
        "videoCapture": true,
        "insights": {
            "status": "COMPLETED",
            "testReport": {
                "message": "Results: 3 Executed | 1 passed, 1 failed, 1 skipped. Median test duration: 1.83 seconds.",
                "metrics": {
                    "testsTotal": 3,
                    "testsPassed": 1,
                    "testsFailed": 1,
                    "testsSkipped": 1,
                    "testsErrored": 0,
                    "testsOther": 0,
                    "testsPassedPercentage": 33.33
                },
                "testDetailsUrl": "https://EXAMPLE-PRESIGNED-URL"
            }
        }
    }
}
```

The `testDetailsUrl` field is a presigned URL to the full test report JSON. Download it to get the per-test breakdown:

```
curl -o test-report.json "{{PRESIGNED_URL}}"
```

The following is an example test report for an Appium Java TestNG job:

```
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
  "deviceName": "Google Pixel 7",
  "deviceArn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
  "deviceOsVersion": "14",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 1,
    "testsFailed": 1,
    "testsSkipped": 1,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 33.33,
    "totalTestExecutionDurationSeconds": 5.421,
    "medianTestExecutionDurationSeconds": 1.83
  },
  "testDetails": [
    {
      "testName": "testValidLogin",
      "testClass": "com.example.app.LoginTest",
      "frameworkResult": "PASS",
      "result": "PASSED",
      "durationSeconds": 1.83,
      "startTimestamp": "2026-07-31T16:58:26.646000Z",
      "endTimestamp": "2026-07-31T16:58:28.476000Z"
    },
    {
      "testName": "testCheckout",
      "testClass": "com.example.app.CheckoutTest",
      "frameworkResult": "FAIL",
      "result": "FAILED",
      "durationSeconds": 3.102,
      "startTimestamp": "2026-07-31T16:58:28.500000Z",
      "endTimestamp": "2026-07-31T16:58:31.602000Z",
      "stackTrace": "java.lang.AssertionError: expected [true] but found [false]\n\tat org.testng.Assert.fail(Assert.java:99)\n\t...",
      "params": ["premium-user", "US"]
    },
    {
      "testName": "testLogout",
      "testClass": "com.example.app.LoginTest",
      "frameworkResult": "SKIP",
      "result": "SKIPPED",
      "durationSeconds": 0.489,
      "startTimestamp": "2026-07-31T16:58:31.700000Z",
      "endTimestamp": "2026-07-31T16:58:32.189000Z"
    }
  ]
}
```

The report contains the following top-level fields:

`version`  
The report schema version.

`jobArn`  
The ARN of the job.

`deviceName`, `deviceArn`, `deviceOsVersion`  
The device that the tests ran on, and its operating system version.

`metrics`  
Aggregate results for the job. The `metrics` object contains the following fields:    
`testsTotal`  
The total number of tests in the job.  
`testsPassed`  
The number of tests that passed.  
`testsFailed`  
The number of tests that failed.  
`testsSkipped`  
The number of tests that were skipped.  
`testsErrored`  
The number of tests that errored.  
`testsOther`  
The number of tests with another result.  
`testsPassedPercentage`  
The percentage of tests that passed.  
`totalTestExecutionDurationSeconds`  
The total duration of all tests, in seconds.  
`medianTestExecutionDurationSeconds`  
The median duration of a test, in seconds.

`testDetails`  
A list of per-test results. Each entry in `testDetails` contains the following fields:    
`testName`  
The name of the test method.  
`testClass`  
The name of the test class.  
`result`  
The Device Farm result for the test.  
`frameworkResult`  
The result that TestNG reported (`PASS`, `FAIL`, or `SKIP`). Device Farm maps this value to the normalized `result` field.  
`durationSeconds`  
The duration of the test, in seconds.  
`startTimestamp`  
The time when the test started.  
`endTimestamp`  
The time when the test ended.  
`params`  
For a parameterized test, the parameter values that TestNG passed to the test.  
`stackTrace`  
For a failed test, the stack trace of the failure.

------

#### Take screenshots of your tests (Optional)
<a name="test-types-appium-screenshots"></a>

You can take screenshots as part of your tests.

Device Farm sets the `DEVICEFARM_SCREENSHOT_PATH` property to a fully qualified path on the local file system where Device Farm expects Appium screenshots to be saved. The test-specific directory where the screenshots are stored is defined at runtime. The screenshots are pulled into your Device Farm reports automatically. To view the screenshots, in the Device Farm console, choose the **Screenshots** section.

 For more information on taking screenshots in Appium tests, see [Take Screenshot](http://appium.io/docs/en/commands/session/screenshot/) in the Appium API documentation. 

## Android tests in AWS Device Farm
<a name="test-types-android-tests"></a>

Device Farm provides support for several automation test types for Android devices, and two built-in tests. 

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

### Android application testing frameworks
<a name="test-types-framework-android"></a>

The following tests are available for Android devices.
+ [Automatic Appium tests](#test-types-appium)
+ [Instrumentation](#test-types-android-instrumentation)

### Built-in test types for Android
<a name="test-types-built-in-android"></a>

There's one built-in test type available for Android devices:
+ [Built-in: fuzz (Android and iOS)](#test-types-built-in-fuzz)

### Instrumentation for Android and AWS Device Farm
<a name="test-types-android-instrumentation"></a>

Device Farm provides support for Instrumentation (JUnit, Espresso, Robotium, or any Instrumentation-based tests) for Android.

Device Farm also provides a sample Android application and links to working tests in three Android automation frameworks, including Instrumentation (Espresso). The [Device Farm sample app for Android](https://github.com/awslabs/aws-device-farm-sample-app-for-android) is available for download on GitHub.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

**Topics**
+ [What is instrumentation?](#test-types-android-instrumentation-what-is)
+ [Considerations for Android instrumentation tests](#test-types-android-instrumentation-settings)
+ [Standard mode test parsing](#test-types-android-standard-mode-test-parse)
+ [Integrating Android Instrumentation with Device Farm](#test-types-android-instrumentation-integrate)

#### What is instrumentation?
<a name="test-types-android-instrumentation-what-is"></a>

Android instrumentation makes it possible for you to invoke callback methods in your test code so you can run through the lifecycle of a component step by step, as if you were debugging the component. For more information, see [Instrumented tests](https://developer.android.com/studio/test/test-in-android-studio#test_types_and_locations) in the *Test types and locations* section of the *Android Developer Tools* documentation.

#### Considerations for Android instrumentation tests
<a name="test-types-android-instrumentation-settings"></a>

When using Android instrumentation, consider the following recommendations and notes.

**Check Android OS Compatibility**  
 Check the [Android documentation ](https://developer.android.com/jetpack/androidx/releases/test#orchestrator-1.5.0), to ensure Instrumentation is compatible with your Android OS version. 

**Running from the Command Line**  
 To run Instrumentation tests from the command line, please follow the [Android documentation.](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-command) 

**System Animations**  
 Per the [Android documentation for Espresso testing](https://developer.android.com/training/testing/espresso), it is recommended that system animations are turned off when testing on real devices. Device Farm automatically disables **Window Animation Scale**, **Transition Animation Scale**, and **Animator Duration Scale** settings when it executes with the [android.support.test.runner.AndroidJUnitRunner](http://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner.html) instrumentation test runner.

**Test Recorders**  
Device Farm supports frameworks, such as Robotium, that have record-and-playback scripting tools.

#### Standard mode test parsing
<a name="test-types-android-standard-mode-test-parse"></a>

In the standard mode of a run, Device Farm parses your test suite and identifies the unique test classes and methods that it will run. This is done through a tool called [Dex Test Parser](https://github.com/linkedin/dex-test-parser). 

When given an Android instrumentation .apk file as input, the parser returns the fully qualified method names of the tests that match JUnit 3 and JUnit 4 conventions. 

To test this in a local environment: 

1. Download the [`dex-test-parser`](https://github.com/linkedin/dex-test-parser) binary.

1. Run the following command to get the list of test methods that will run on Device Farm:

   ```
   java -jar parser.jar path/to/apk path/for/output
   ```

#### Integrating Android Instrumentation with Device Farm
<a name="test-types-android-instrumentation-integrate"></a>

**Note**  
Use the following instructions to integrate Android instrumentation tests with AWS Device Farm. For more information about using instrumentation tests in Device Farm, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation). 

##### Run Android Instrumentation tests (console)
<a name="test-types-android-instrumentation-upload"></a>

Use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. In the list of projects, choose the project that you want to upload your tests to.
**Tip**  
You can use the search bar to filter the project list by name.  
To create a project, follow the instructions in [Creating a project in AWS Device Farm](#how-to-create-project).

1. Select **Create run**.

1. Under **Select app and run type**, in the **Run type** section, select **Android app**.

1. Under **Select app**, in the **App selection options** section, choose **Select sample app provided by Device Farm** if you do not have an app. If you are bringing your own app, select **Upload own app**, and then choose your APK (.apk file format).

1. Under **Configure test**, in the **Select test framework** section, choose **Instrumentation**, and then choose **Choose File**. Browse to and choose the APK file (.apk file format) that contains your tests.

1. Under **Choose your execution environment**, select either **Run your test in a custom environment** or **Run your test in our standard environment**. For more information, see [Test environments in AWS Device Farm](#test-environments).

1. If you chose the custom environment, you can use the default test spec that is populated for instrumentation tests, or choose **Upload own test spec** to provide your own.

1. Under **Select devices**, choose a device selection method. Select **Use Device Pool** to choose from a curated collection of devices or a custom device pool you created. Select **Manually select devices** to pick individual devices to run your tests against. The **Device compatibility** section shows how many devices in the selected pool are compatible with your app. For more information, see [Device support in AWS Device Farm](#devices).

1. To configure run-level properties, update the **Run settings** section. Here you can do the following:

   1. (Optional) To have Device Farm generate a test report after your run completes, select **Generate test report**. This option is available in a custom test environment only. Device Farm generates the report from instrumentation results included in your test spec output. If you upload your own test spec, make sure it outputs instrumentation results to your test spec output.

1. Complete the remaining steps, and then start the run.

##### View a test report (console)
<a name="test-types-android-instrumentation-view-insights-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Choose the project that contains the run you want to inspect.

1. Choose the completed run to open its details.

1. Choose one of the completed jobs to open the results for that device.

###### With test insights enabled
<a name="test-types-android-instrumentation-view-insights-console-with"></a>

The job results include a **Test report** tab. Choose it to see a per-test breakdown. The following screenshots show the **Test report** tab with all columns visible.

![The first set of columns on the Test report tab for a completed instrumentation job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-enabled-test-report-column-start.png)


![The remaining columns on the Test report tab for a completed instrumentation job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-enabled-test-report-column-end.png)


The tab shows the following fields for each test:

`testName`  
The name of the test method.

`testClass`  
The name of the test class.

`result`  
The Device Farm result for the test.

`frameworkResult`  
The result that the instrumentation framework reported. Device Farm maps this value to the normalized `result` field.

`durationSeconds`  
The duration of the test, in seconds.

`startTimestamp`  
The time when the test started.

`endTimestamp`  
The time when the test ended.

`current`  
The position of the test in the run.

`numTests`  
The total number of tests in the run.

`statusCode`  
The instrumentation status code that the test reported.

`stream`  
A human-readable version of the instrumentation output for the test.

`stackTrace`  
For a failed test, the stack trace of the failure.

To download the full test report as a JSON file, choose **Download full summary** at the top of the job details.

To choose which columns appear, choose the gear icon. In the settings, you can select the columns to display and turn **Group by class** on or off. **Group by class** is on by default, which groups the tests by their test class. Turn it off to see a flat list of all tests, as shown in the following screenshot.

![The Test report tab with Group by class turned off, showing a flat list of tests.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-enabled-test-report-without-grouping.png)


###### Without test insights enabled
<a name="test-types-android-instrumentation-view-insights-console-without"></a>

The job results show the standard test output and artifacts, but no **Test report** tab. To generate a test report, schedule a new run with test insights enabled.

![The job results for a completed instrumentation job without test insights enabled.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-disabled-test-report.png)


##### View a test report (AWS CLI)
<a name="test-types-android-instrumentation-view-insights-cli"></a>

Run **get-job** and specify the job ARN:

```
aws devicefarm get-job --arn {{arn:aws:devicefarm:us-west-2:123456789012:job:PROJECT_ID/RUN_ID/00000}}
```

###### Without test insights enabled
<a name="test-types-android-instrumentation-view-insights-cli-without"></a>

If you did not enable test insights, the response contains the standard job fields, such as the job status, result, counters, and device:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "name": "Example Android Phone",
        "created": "2026-08-05T14:26:56.959000-07:00",
        "status": "COMPLETED",
        "result": "PASSED",
        "counters": {
            "total": 3,
            "passed": 3,
            "failed": 0,
            "warned": 0,
            "errored": 0,
            "stopped": 0,
            "skipped": 0
        },
        "message": "Successful test lifecycle of Setup Test",
        "device": {
            "arn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
            "name": "Example Android Phone",
            "platform": "ANDROID",
            "os": "16",
            "formFactor": "PHONE",
            "fleetType": "PUBLIC"
        },
        "deviceMinutes": {
            "total": 1.38,
            "metered": 0.0,
            "unmetered": 1.13
        },
        "videoCapture": true
    }
}
```

###### With test insights enabled
<a name="test-types-android-instrumentation-view-insights-cli-with"></a>

If you enabled test insights, the response also includes an `insights` object. This object contains the test report status, high-level metrics, and a presigned URL to the detailed report:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "status": "COMPLETED",
        "result": "PASSED",
        "counters": { ... },
        "device": { ... },
        "deviceMinutes": { ... },
        "videoCapture": true,
        "insights": {
            "status": "COMPLETED",
            "testReport": {
                "message": "Results: 2 Executed | 2 passed, Median test duration: 28.926 seconds.",
                "metrics": {
                    "testsTotal": 2,
                    "testsPassed": 2,
                    "testsFailed": 0,
                    "testsSkipped": 0,
                    "testsErrored": 0,
                    "testsOther": 0,
                    "testsPassedPercentage": 100.0
                },
                "testDetailsUrl": "https://EXAMPLE-PRESIGNED-URL"
            }
        }
    }
}
```

The `testDetailsUrl` field is a presigned URL to the full test report JSON. Download it to get the per-test breakdown:

```
curl -o test-report.json "{{PRESIGNED_URL}}"
```

The following is an example test report for an instrumentation job:

```
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 2,
    "testsFailed": 1,
    "testsSkipped": 0,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 66.67,
    "totalTestExecutionDurationSeconds": 26.004,
    "medianTestExecutionDurationSeconds": 1.598
  },
  "testDetails": [
    {
      "testName": "testConnect",
      "testClass": "com.example.myapp.GpsConnectInstrumentedTest",
      "frameworkResult": "PASSED",
      "result": "PASSED",
      "durationSeconds": 24.399,
      "startTimestamp": "2026-08-05T20:38:30.131514Z",
      "endTimestamp": "2026-08-05T20:38:54.530369Z",
      "statusCode": 0,
      "current": 1,
      "numTests": 3
    },
    {
      "testName": "testHistoryOff",
      "testClass": "com.example.myapp.NotificationHistoryInstrumentedTest",
      "frameworkResult": "PASSED",
      "result": "PASSED",
      "durationSeconds": 1.598,
      "startTimestamp": "2026-08-05T20:38:54.531765Z",
      "endTimestamp": "2026-08-05T20:38:56.130032Z",
      "statusCode": 0,
      "current": 2,
      "numTests": 3
    },
    {
      "testName": "testConnect",
      "testClass": "com.example.myapp.WifiConnectInstrumentedTest",
      "frameworkResult": "FAILED",
      "result": "FAILED",
      "durationSeconds": 0.002,
      "startTimestamp": "2026-08-05T20:38:56.131857Z",
      "endTimestamp": "2026-08-05T20:38:56.133770Z",
      "stackTrace": "java.lang.NullPointerException: Attempt to invoke virtual method 'boolean androidx.test.uiautomator.UiDevice.pressHome()' on a null object reference\n\tat com.example.myapp.WifiConnectInstrumentedTest.testConnect(WifiConnectInstrumentedTest.java:93)\n\t...",
      "stream": "\nError in testConnect(com.example.myapp.WifiConnectInstrumentedTest):\njava.lang.NullPointerException: Attempt to invoke virtual method 'boolean androidx.test.uiautomator.UiDevice.pressHome()' on a null object reference\n\t...",
      "statusCode": -2,
      "current": 3,
      "numTests": 3
    }
  ],
  "errorMessage": "There was 1 failure:\n1) testConnect(com.example.myapp.WifiConnectInstrumentedTest)\njava.lang.NullPointerException: Attempt to invoke virtual method 'boolean androidx.test.uiautomator.UiDevice.pressHome()' on a null object reference\n\t...\nFAILURES!!!\nTests run: 3,  Failures: 1",
  "instrumentationCode": -1
}
```

The report contains the following top-level fields:

`version`  
The report schema version.

`jobArn`  
The ARN of the job.

`metrics`  
Aggregate results for the job. The `metrics` object contains the following fields:    
`testsTotal`  
The total number of tests in the job.  
`testsPassed`  
The number of tests that passed.  
`testsFailed`  
The number of tests that failed.  
`testsSkipped`  
The number of tests that were skipped.  
`testsErrored`  
The number of tests that errored.  
`testsOther`  
The number of tests with another result.  
`testsPassedPercentage`  
The percentage of tests that passed.  
`totalTestExecutionDurationSeconds`  
The total duration of all tests, in seconds.  
`medianTestExecutionDurationSeconds`  
The median duration of a test, in seconds.

`errorMessage`  
If the run had failures, an error message that summarizes them.

`instrumentationCode`  
The overall instrumentation exit code for the job.

`testDetails`  
A list of per-test results. Each entry in `testDetails` contains the following fields:    
`testName`  
The name of the test method.  
`testClass`  
The name of the test class.  
`result`  
The Device Farm result for the test.  
`frameworkResult`  
The result that the instrumentation framework reported. Device Farm maps this value to the normalized `result` field.  
`durationSeconds`  
The duration of the test, in seconds.  
`startTimestamp`  
The time when the test started.  
`endTimestamp`  
The time when the test ended.  
`current`  
The position of the test in the run.  
`numTests`  
The total number of tests in the run.  
`statusCode`  
The instrumentation status code that the test reported.  
`stream`  
A human-readable version of the instrumentation output for the test.  
`stackTrace`  
For a failed test, the stack trace of the failure.

##### (Optional) Take screenshots in Android instrumentation tests
<a name="test-types-android-instrumentation-screenshots"></a>

You can take screenshots as part of your Android Instrumentation tests.

To take screenshots, call one of the following methods:
+ For Robotium, call the `takeScreenShot` method (for example, `solo.takeScreenShot();`).
+ For Spoon, call the `screenshot` method, for example:

  ```
  Spoon.screenshot(activity, "initial_state");
  /* Normal test code... */
  Spoon.screenshot(activity, "after_login");
  ```

During a test run, Device Farm gets screenshots from the following locations on the devices, if they exist, and then adds them to the test reports:
+ `/sdcard/robotium-screenshots`
+ `/sdcard/test-screenshots`
+ `/sdcard/Download/spoon-screenshots/{{test-class-name}}/{{test-method-name}}`
+ `/data/data/{{application-package-name}}/app_spoon-screenshots/{{test-class-name}}/{{test-method-name}}`

## iOS tests in AWS Device Farm
<a name="test-types-ios-tests"></a>

Device Farm provides support for several automation test types for iOS devices, and a built-in test.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

### iOS application testing frameworks
<a name="test-types-framework-ios"></a>

The following tests are available for iOS devices.
+ [Automatic Appium tests](#test-types-appium)
+ [XCTest](#test-types-ios-xctest)
+ [XCTest UI](#test-types-ios-xctest-ui)

### Built-in test types for iOS
<a name="test-types-built-in-ios"></a>

There is currently one built-in test type available for iOS devices.
+ [Built-in: fuzz (Android and iOS)](#test-types-built-in-fuzz)

### Integrating Device Farm with XCTest for iOS
<a name="test-types-ios-xctest"></a>

With Device Farm, you can use the XCTest framework to test your app on real devices. For more information about XCTest, see [Testing Basics](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/03-testing_basics.html) in *Testing with Xcode*.

To run a test, you create the packages for your test run, and you upload these packages to Device Farm.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

**Topics**
+ [Create the packages for your XCTest run](#test-types-ios-xctest-create-packages)
+ [Upload the packages for your XCTest run to Device Farm](#test-types-ios-xctest-upload)

#### Create the packages for your XCTest run
<a name="test-types-ios-xctest-create-packages"></a>

To test your app by using the XCTest framework, Device Farm requires the following:
+ Your app package as a `.ipa` file.
+ Your XCTest package as a `.zip` file.

You create these packages by using the build output that Xcode generates. Complete the following steps to create the packages so that you can upload them to Device Farm.

**To generate the build output for your app**

1. Open your app project in Xcode.

1. In the scheme dropdown menu in the Xcode toolbar, choose **Generic iOS Device** as the destination.

1. In the **Product** menu, choose **Build For**, and then choose **Testing**.

**To create the app package**

1. In the project navigator in Xcode, under **Products**, open the contextual menu for the file named `{{app-project-name}}.app`. Then, choose **Show in Finder**. Finder opens a folder named `Debug-iphoneos`, which contains the output that Xcode generated for your test build. This folder includes your `.app` file.

1. In Finder, create a new folder, and name it `Payload`.

1. Copy the `{{app-project-name}}.app` file, and paste it in the `Payload` folder.

1. Open the contextual menu for the `Payload` folder and choose **Compress "Payload"**. A file named `Payload.zip` is created.

1. Change the file name and extension of `Payload.zip` to `{{app-project-name}}.ipa`.

   In a later step, you provide this file to Device Farm. To make the file easier to find, you might want to move it to another location, such as your desktop.

1. Optionally, you can delete the `Payload` folder and the `.app` file in it.

**To create the XCTest package**

1. In Finder, in the `Debug-iphoneos` directory, open the contextual menu for the `{{app-project-name}}.app` file. Then, choose **Show Package Contents**.

1. In the package contents, open the `Plugins` folder. This folder contains a file named `{{app-project-name}}.xctest`.

1. Open the contextual menu for this file and choose **Compress "`{{app-project-name}}.xctest`"**. A file named `{{app-project-name}}.xctest.zip` is created.

   In a later step, you provide this file to Device Farm. To make the file easier to find, you might want to move it to another location, such as your desktop.

#### Upload the packages for your XCTest run to Device Farm
<a name="test-types-ios-xctest-upload"></a>

Use the Device Farm console to upload the packages for your test.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. If you don't have a project already, create one. For the steps to create a project, see [Creating a project in AWS Device Farm](#how-to-create-project).

   Otherwise, on the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose the project that you want to use to run the test.

1. Choose **Create run**.

1. Under **Run settings**, in the **Run type** section, choose **iOS app**.

1. Under **Select app**, in the **App selection options** section, select **Upload own app**. Then, select **Choose file** under **Upload app**.

1. Browse to the `.ipa` file for your app and upload it.
**Note**  
Your `.ipa` package must be built for testing.

1. Under **Configure test**, in the **Select test framework** section, choose **XCTest**. Then, select **Choose file** under **Upload app**.

1. Browse to the `.zip` file that contains the XCTest package for your app and upload it.

1. Complete the remaining steps in the project creation process. You will select the devices that you want to test on and specify the device state.

1. Choose **Create run**. Device Farm runs your test and shows the results in the console.

### Integrating XCTest UI for iOS with Device Farm
<a name="test-types-ios-xctest-ui"></a>

Device Farm provides support for the XCTest UI testing framework. Specifically, Device Farm supports XCTest UI tests written in both Objective-C and [Swift](https://developer.apple.com/swift/). 

 The XCTest UI framework enables UI testing in iOS development, built on top of XCTest. For more information, see [User Interface Testing](https://developer.apple.com/library/prerelease/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/09-ui_testing.html#//apple_ref/doc/uid/TP40014132-CH13-SW1) in the iOS Developer Library.

For general information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

Use the following instructions to integrate Device Farm with the XCTest UI testing framework for iOS.

**Topics**
+ [Prepare your iOS XCTest UI tests](#test-types-ios-xctest-ui-prepare)
+ [Option 1: Creating an XCTest UI .ipa package](#how-to-use-create-XCTestUI-ipa-package)
+ [Option 2: Creating an XCTest UI .zip package](#how-to-use-create-XCTestUI-zip-package)
+ [Run iOS XCTest UI tests (console)](#test-types-ios-xctest-ui-upload)
+ [View a test report (console)](#test-types-ios-xctest-ui-view-insights-console)
+ [View a test report (AWS CLI)](#test-types-ios-xctest-ui-view-insights-cli)

#### Prepare your iOS XCTest UI tests
<a name="test-types-ios-xctest-ui-prepare"></a>

You can either upload an `.ipa` file or a `.zip` file for your XCTEST\_UI test package.

An `.ipa` file is an application archive containing the iOS Runner app in bundle format. *Additional files cannot be included inside the `.ipa` file.*

If you upload a `.zip` file, it can contain either the iOS Runner app directly or an `.ipa` file. You can also include other files within the `.zip` file if you want to use them during the tests. For example you can include files like `.xctestrun`, `.xcworkspace` or `.xcodeproj` inside `.zip` file to run XCUI Test Plans on device farm. Detailed instructions on how to run Test Plans are available in the default test specification file for the XCUI Test type. 

#### Option 1: Creating an XCTest UI .ipa package
<a name="how-to-use-create-XCTestUI-ipa-package"></a>

The *yourAppName*UITest-Runner.app bundle is produced by Xcode when you build your project for testing. It can be found in the Products directory for your project.

To create an .ipa file:

1. Create a directory called {{Payload}}.

1. Add your app directory to the Payload directory.

1. Archive the Payload directory into a `.zip` file and then change the file extension to `.ipa`.

 The following folder structure shows how an example app named {{my-project-nameUITest-Runner.app}} would be packaged as an `.ipa` file: 

```
.
└── my-project-nameUITest.ipa
    └── Payload (directory)
        └── my-project-nameUITest-Runner.app
```

#### Option 2: Creating an XCTest UI .zip package
<a name="how-to-use-create-XCTestUI-zip-package"></a>

Device Farm automatically generates a `.xctestrun` file for you for running your full XCTest UI test suite. If you want to use your own `.xctestrun` file on Device Farm, you can compress your `.xctestrun` files and app directory into a `.zip` file. If you already have a `.ipa` file for your test package you can include that here instead of {{\*-Runner.app}}.

```
.
└── swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   ├── SampleTestPlan_2.xctestrun
   ├── SampleTestPlan_1.xctestrun
   └── (any other files)
```

 If you want to run an Xcode test plan for your XCUI tests on Device Farm, you can create a zip containing your *my-project-nameUITest-Runner.app* **or** *my-project-nameUITest.ipa* file and xcode source code files required to run XCTEST\_UI with test plans, including either a `.xcworkspace` or `.xcodeproj` file.

Here is a sample zip using a `.xcodeproj` file: 

```
.
└── swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   ├── (any directory)
   └── {{SampleXcodeProject.xcodeproj}}
        ├── Testplan_1.xctestplan
        ├── Testplan_2.xctestplan
        └── (any other source code files created by xcode with .xcodeproj)
```

Here is a sample zip using a `.xcworkspace` file: 

```
.
└──swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   └── (any directory)
   │   ├── SampleXcodeProject.xcodeproj
   │   ├── Testplan_1.xctestplan
   │   ├── Testplan_2.xctestplan
   |   └── (any other source code files created by xcode with .xcodeproj)
   └── {{SampleWorkspace.xcworkspace}}
       └── contents.xcworkspacedata
```

**Note**  
Please ensure that you do not have a directory named "Payload" inside your XCTest UI .zip package. 

#### Run iOS XCTest UI tests (console)
<a name="test-types-ios-xctest-ui-upload"></a>

Use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. In the list of projects, choose the project that you want to upload your tests to.
**Tip**  
You can use the search bar to filter the project list by name.  
To create a project, follow the instructions in [Creating a project in AWS Device Farm](#how-to-create-project)

1. Choose **Create run**.

1. Under **Select app and run type**, in the **Run type** section, choose **iOS app**.

1. In the **Select app** section, in **App selection options**, select **Upload own app**. Then, select **Choose file** under **Upload app**.

1. Browse to and choose your iOS app file. The file must be an .ipa file.
**Note**  
Make sure that your .ipa file is built for an iOS device and not for a simulator.

1. Under **Configure test**, in the **Select test framework** section, choose **XCTest UI**. Then, select **Choose file** under **Upload app**.

1. Browse to and choose the .ipa or .zip file that contains your iOS XCTest UI test runner. 

1. (Optional) To configure run-level properties, update the **Run settings** section:

   1. To have Device Farm generate a Test Insights report after your run completes, enable **Generate test report**. This option is available in a custom test environment only.

      The following prerequisites apply:

      1. Your tests must generate an Xcode `.xcresult` bundle and write it to `$DEVICEFARM_DERIVED_DATA_PATH`. For example, pass `-derivedDataPath $DEVICEFARM_DERIVED_DATA_PATH` to `xcodebuild`. The default XCTest UI test spec produces and stores this bundle automatically if you keep the default configuration.

      For more information about viewing your report, see [View a test report (console)](#test-types-ios-xctest-ui-view-insights-console).

1. Complete the remaining steps in the run creation process. Select the devices that you want to test on and optionally specify additional configuration.

1. Choose **Create run**. Device Farm runs your test and shows the results in the console.

#### View a test report (console)
<a name="test-types-ios-xctest-ui-view-insights-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Choose the project that contains the run you want to inspect.

1. Choose the completed run to open its details.

1. Choose one of the completed jobs to open the results for that device.

##### With test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-console-with"></a>

The job results include a **Test report** tab. Choose it to see a summary of the test results, including the total number of tests, how many passed and failed, the total test execution time, and the median test execution time. Below the summary, the **Tests** table shows a per-test breakdown.

![The first set of columns on the Test report tab for a completed XCTest UI job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-column-start.png)


![The remaining columns on the Test report tab for a completed XCTest UI job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-column-end.png)


Each row in the **Tests** table includes the following columns:
+ **Result** – whether the test passed, failed, or was skipped.
+ **Test class** – the class that the test belongs to.
+ **Test name** – the name of the test method.
+ **Stack trace** – for a failed test, a link to the stack trace of the failure.
+ **Duration** – how long the test took to run.
+ **Start time** and **End time** – when the test started and ended.
+ **Framework result** – the result string that the XCTest framework reported for the test.
+ **Test bundle** – the test bundle that the test belongs to.
+ **Node identifier** – the xcresult node identifier for the test case.

You can search for a test by name, class, or status. To choose which columns appear, choose the **Settings** icon. In the settings, you can select the columns to display and turn **Group by class** on or off. **Group by class** is on by default, which groups the tests by their test class. Expand a class to see its individual tests, as shown in the following screenshot.

![The Test report tab with tests grouped by class, showing each class expanded to its individual tests.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-grouped.png)


To download the full test report as a JSON file, choose **Download full summary** at the top of the job details.

##### Without test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-console-without"></a>

The job results show the standard test output and artifacts, such as the **Suites**, **Logs**, and **Screenshots** tabs, but no **Test report** tab. To generate a test report, schedule a new run with test insights enabled.

![The job results for a completed XCTest UI job without test insights enabled, showing the standard tabs and no Test report tab.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/passing.png)


#### View a test report (AWS CLI)
<a name="test-types-ios-xctest-ui-view-insights-cli"></a>

Run **get-job** and specify the job ARN:

```
aws devicefarm get-job --arn {{arn:aws:devicefarm:us-west-2:123456789012:job:PROJECT_ID/RUN_ID/00000}}
```

##### Without test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-cli-without"></a>

If you did not enable test insights, the response contains the standard job fields, such as the job status, result, counters, and device:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "name": "Example Apple iPhone",
        "created": "2026-08-05T14:26:56.959000-07:00",
        "status": "COMPLETED",
        "result": "PASSED",
        "counters": {
            "total": 3,
            "passed": 3,
            "failed": 0,
            "warned": 0,
            "errored": 0,
            "stopped": 0,
            "skipped": 0
        },
        "message": "Successful test lifecycle of Setup Test",
        "device": {
            "arn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
            "name": "Example Apple iPhone",
            "platform": "IOS",
            "os": "18",
            "formFactor": "PHONE",
            "fleetType": "PUBLIC"
        },
        "deviceMinutes": {
            "total": 1.38,
            "metered": 0.0,
            "unmetered": 1.13
        },
        "videoCapture": true
    }
}
```

##### With test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-cli-with"></a>

If you enabled test insights, the response also includes an `insights` object that contains the test report status, high-level metrics, and a presigned URL to the detailed report:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "status": "COMPLETED",
        "result": "PASSED",
        "counters": { ... },
        "device": { ... },
        "deviceMinutes": { ... },
        "videoCapture": true,
        "insights": {
            "status": "COMPLETED",
            "testReport": {
                "message": "Results: 2 Executed | 2 passed, Median test duration: 3.214 seconds.",
                "metrics": {
                    "testsTotal": 2,
                    "testsPassed": 2,
                    "testsFailed": 0,
                    "testsSkipped": 0,
                    "testsErrored": 0,
                    "testsOther": 0,
                    "testsPassedPercentage": 100.0
                },
                "testDetailsUrl": "https://EXAMPLE-PRESIGNED-URL"
            }
        }
    }
}
```

The `testDetailsUrl` field is a presigned URL to the full test report JSON. Download it to get the per-test breakdown:

```
curl -o test-report.json "{{PRESIGNED_URL}}"
```

The following is an example test report for an XCTest UI job:

```
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE/a1b2c3d4-e5f6-4a7b-8c9d-67890EXAMPLE/00000",
  "deviceName": "Apple iPhone 15",
  "deviceArn": "arn:aws:devicefarm:us-west-2::device:A1B2C3D4E5F60718293A4B5C6D7E8F90",
  "deviceOsVersion": "17.5",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 2,
    "testsFailed": 1,
    "testsSkipped": 0,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 66.67,
    "totalTestExecutionDurationSeconds": 6.914,
    "medianTestExecutionDurationSeconds": 2.062
  },
  "testDetails": [
    {
      "testName": "test_execute()",
      "testClass": "AlertsTest",
      "frameworkResult": "Passed",
      "result": "PASSED",
      "durationSeconds": 2.062,
      "startTimestamp": "2026-07-31T16:58:26.646000Z",
      "endTimestamp": "2026-07-31T16:58:28.708000Z",
      "testBundle": "AWSDeviceFarmiOSReferenceAppSwiftUITests",
      "nodeIdentifier": "AlertsTest/test_execute()"
    },
    {
      "testName": "test_login()",
      "testClass": "LoginTest",
      "frameworkResult": "Failed",
      "result": "FAILED",
      "durationSeconds": 3.541,
      "startTimestamp": "2026-07-31T16:58:29.000000Z",
      "endTimestamp": "2026-07-31T16:58:32.541000Z",
      "stackTrace": "LoginTest.swift:88: XCTAssertEqual failed: (\"Welcome\") is not equal to (\"Error\")\nLoginTest.swift:91: XCTAssertTrue failed",
      "testBundle": "AWSDeviceFarmiOSReferenceAppSwiftUITests",
      "nodeIdentifier": "LoginTest/test_login()"
    },
    {
      "testName": "test_themeRendering()",
      "testClass": "ThemeTest",
      "frameworkResult": "Passed",
      "result": "PASSED",
      "durationSeconds": 1.311,
      "testBundle": "AWSDeviceFarmiOSReferenceAppSwiftUITests",
      "nodeIdentifier": "ThemeTest/test_themeRendering()",
      "testArguments": "Dark Appearance, Portrait"
    }
  ]
}
```

The report contains the following top-level fields:

`version`, `jobArn`  
The report schema version and the ARN of the job.

`deviceName`, `deviceArn`, `deviceOsVersion`  
The name and ARN of the device that ran the job, and its operating system version.

`metrics`  
Aggregate results for the job: the total number of tests (`testsTotal`) and how many passed (`testsPassed`), failed (`testsFailed`), were skipped (`testsSkipped`), errored (`testsErrored`), or had another result (`testsOther`), along with the pass rate (`testsPassedPercentage`), the total test duration (`totalTestExecutionDurationSeconds`), and the median test duration (`medianTestExecutionDurationSeconds`).

Each entry in `testDetails` contains the following fields:

`testName`, `testClass`  
The name of the test method and its test class.

`result`, `frameworkResult`  
The Device Farm result for the test, and the result string that the XCTest framework reported. Device Farm maps `frameworkResult` to the normalized `result` field.

`durationSeconds`, `startTimestamp`, `endTimestamp`  
The duration of the test in seconds, and the times when it started and ended.

`testBundle`, `nodeIdentifier`  
The test bundle that the test belongs to, and the xcresult node identifier for the test case.

`testArguments`  
For a parameterized test invocation, the argument label for the invocation.

`stackTrace`  
For a failed test, the stack trace of the failure.

## Web app tests in AWS Device Farm
<a name="test-types-web-app-tests"></a>

Device Farm provides testing with Appium for web applications. For more information on setting up your Appium tests on Device Farm, see [Automatically run Appium tests in Device Farm](#test-types-appium).

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

### Rules for metered and unmetered devices
<a name="web-app-tests-metered-unmetered-devices-rules"></a>

Metering refers to billing for devices. By default, Device Farm devices are metered and you are charged per minute after the free trial minutes are used up. You can also choose to purchase unmetered devices, which allow unlimited testing for a flat monthly fee. For more information about pricing, see [AWS Device Farm Pricing](https://aws.amazon.com/device-farm/).

If you choose to start a run with a device pool that contains both iOS and Android devices, there are rules for metered and unmetered devices. For example, if you have five unmetered Android devices and five unmetered iOS devices, your web test runs use your unmetered devices.

 Here is another example: Suppose you have five unmetered Android devices and 0 unmetered iOS devices. If you select only Android devices for your web run, your unmetered devices are used. If you select both Android and iOS devices for your web run, the billing method is metered, and your unmetered devices are not used.

## Built-in tests in AWS Device Farm
<a name="test-types-built-in-tests"></a>

Device Farm provides support for built-in test types for Android and iOS devices. 

With built-in tests, you can test your application on multiple devices without having to write and maintain test automation scripts. This can save you time and effort, especially when you're getting started with Device Farm. Device Farm offers the following built-in test type:
+ [Built-in: fuzz (Android and iOS)](#test-types-built-in-fuzz) – The fuzz test randomly sends user interface events to devices and then reports results.

For more information about tests and testing frameworks in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).



### Running Device Farm's built-in fuzz test (Android and iOS)
<a name="test-types-built-in-fuzz"></a>

Device Farm's built-in fuzz test randomly sends user interface events to devices and then reports results.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

**To run the built-in fuzz test**

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. In the list of projects, choose the project where you want to run the built-in fuzz test.
**Tip**  
You can use the search bar to filter the project list by name.  
To create a project, follow the instructions in [Creating a project in AWS Device Farm](#how-to-create-project).

1. Choose **Create run**.

1. Under **Run settings**, select your run type in the **Run type** section. Select **Android app** if you do not have an app ready for testing, or if you are testing an android (.apk) app. Select **iOS app** if you are testing an iOS (.ipa) app.

1. Under **Select app**, choose **Select sample app provided by Device Farm** if you do not have an app available for testing. If you are bringing your own app, select **Upload own app **, and choose your application file.

1. Under **Configure test**, in the **Select test framework** section, choose **Built-in: Fuzz**.

1. If any of the following settings appear, you can either accept the default values or specify your own:
   + **Event count**: Specify a number between 1 and 10,000, representing the number of user interface events for the fuzz test to perform.
   + **Event throttle**: Specify a number between 0 and 1,000, representing the number of milliseconds for the fuzz test to wait before performing the next user interface event.
   + **Randomizer seed**: Specify a number for the fuzz test to use for randomizing user interface events. Specifying the same number for subsequent fuzz tests ensures identical event sequences.

1. Complete the remaining instructions to select devices and start the run.

# Custom test environments in AWS Device Farm
<a name="custom-test-environments"></a>

**Note**  
iOS 27 public devices are now available on Device Farm, served by the macos\_tahoe test host running Xcode 27. Point your test spec at macos\_tahoe and choose an iOS 27 device to get started.

AWS Device Farm enables configuring a custom environment for automated testing (custom mode), which is the recommended approach for all Device Farm users. To learn more about environments in Device Farm, see [Test environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-environments.html). 

Benefits of the Custom Mode as opposed to the Standard Mode include: 
+ **Faster end-to-end test execution**: The test package isn't parsed to detect every test in the suite, avoiding preprocessing/postprocessing overhead. 
+ **Live log and video streaming**: Your client-side test logs and video are live streamed when using Custom Mode. This feature isn't available in the standard mode. 
+ **Captures all artifacts**: On the host and device, Custom Mode allows you to capture all test artifacts. This may not be possible in the standard mode. 
+ **More consistent and replicable local environment**: When in Standard Mode, artifacts will be provided for each individual test separately, which can be beneficial under certain circumstances. However, your local test environment may deviate from the original configuration as Device Farm handles each executed test differently. 

  In contrast, Custom Mode enables you to make your Device Farm test execution environment consistently in line with with your local test environment.

 Custom environments are configured using a YAML-formatted test specification (test spec) file. Device Farm provides a default test spec file for each supported test type that can be used as is or customized; customizations like test filters or config files can be added to the test spec. Edited test specs can be saved for future test runs. 

For more information, see [Uploading a Custom Test Spec Using the AWS CLI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html#how-to-create-test-run-cli-step5) and [Creating a test run in Device Farm](#how-to-create-test-run).

**Topics**
+ [Test spec reference and syntax](#custom-test-environment-test-spec)
+ [Hosts for custom test environments](#custom-test-environments-hosts)
+ [Access AWS resources using an IAM Execution Role](#custom-test-environments-iam-roles)
+ [Environment variables for custom test environments](#custom-test-environment-variables)
+ [Best practices for custom test environment execution](#custom-test-environments-best-practices)
+ [Migrating tests from a standard to custom test environment](#custom-test-environment-migration)
+ [Extending custom test environments in Device Farm](#custom-test-environments-extending)

## Test spec reference and syntax
<a name="custom-test-environment-test-spec"></a>

 The test spec (test specification) is a file that you use to define custom test environments in Device Farm. 

### Test spec workflow
<a name="custom-test-environment-test-spec-workflow"></a>

 The Device Farm test spec executes phases and their commands in a pre-determined order, letting you customize the way your environment is prepared and executed. When each phase is executed, its commands are run in the order listed within the test spec file. Phases are executed in the following sequence 

1. `install` - This is where actions like downloading, installing, and setting up tooling should be defined.

1. `pre_test` - This is where pre-test actions like starting background processes should be defined.

1. `test` - This is where the command that invokes your test should be defined.

1. `post_test` - This is where any final tasks that need to be run after your test concludes should be defined, such as test report generation and artifact file aggregation.

### Test spec syntax
<a name="custom-test-environment-test-spec-syntax"></a>

The following is the YAML schema for a test spec file

```
version: 0.1

android_test_host: "string"
ios_test_host: "string"

phases:
  install:
    commands:
      - "string"
      - "string"
  pre_test:
    commands:
      - "string"
      - "string"
  test:
    commands:
      - "string"
      - "string"
  post_test:
    commands:
      - "string"
      - "string"

artifacts:
    - "string"
    - "string"
```

** `version` **  
 *(Required, number)*   
 Reflects the Device Farm supported test spec version. The current version number is ` 0.1`. 

** `android_test_host` **  
 *(Optional, string)*   
 The test host that will be selected for test runs performed on Android devices. This field is required for test runs on Android devices. For more information, see [Available test hosts for custom test environments](#custom-test-environments-hosts-available). 

** `ios_test_host` **  
 *(Optional, string)*   
 The test host that will be selected for test runs performed on iOS devices. This field is required for test runs on iOS devices with a major version greater than 26. For more information, see [Available test hosts for custom test environments](#custom-test-environments-hosts-available). 

** `phases` **  
This section contains groups of commands executed during a test run, where each phase is optional The allowed test phase names are: `install`, `pre_test` , `test`, and `post_test`.  
+ `install` - Default dependencies for testing frameworks supported by Device Farm are already installed. This phase contains additional commands, if any, that Device Farm runs during installation.
+ `pre_test` - The commands, if any, executed before your automated test.
+ `test` - The commands executed during your automated test run. If any command in the test phase fails (meaning it returns a non-zero exit code), the test is marked as failed
+ `post_test` - The commands, if any, executed after your automated test run. This will be executed whether or not your test in the `test` phase succeeds or fails.  
** `commands` **  
 *(Optional, List[string])*   
 A list of strings to execute as a shell command during the phase. 

** `artifacts` **  
 *(Optional, List[string])*   
 Device Farm gathers artifacts such as custom reports, log files, and images from a location specified here. Wildcard characters are not supported as part of an artifact location, so you must specify a valid path for each location.   
These test artifacts are available for each device in your test run. For information about retrieving your test artifacts, see [Downloading artifacts in a custom test environment](#using-artifacts-custom).

**Important**  
A test spec must be formatted as a valid YAML file. If the indenting or spacing in your test spec are invalid, your test run can fail. Tabs are not allowed in YAML files. You can use a YAML validator to test whether your test spec is a valid YAML file. For more information, see the [YAML website](http://yaml.org/spec/1.2/spec.html).

### Test spec examples
<a name="custom-test-environment-test-spec-example"></a>

 The following examples show test specs that can be executed on Device Farm. 

------
#### [ Simple Demo ]

 The following is an example test spec file that simply logs `Hello world!` as a test run artifact. 

```
version: 0.1

# The following field(s) allow you to select which Device Farm test host is used for your test run.
android_test_host: {{amazon_linux_2}}

# Let Device Farm automatically select the iOS test host based on the device's iOS version.
ios_test_host: default

phases:
  install:
    commands:
      # Setup your environment by installing and/or validating software
      - devicefarm-cli use python 3.12
      - python --version

  pre_test:
    commands:
      # Setup your tests by starting background tasks or setting up
      # additional environment variables.
      - OUTPUT_FILE="/tmp/hello.log"

  test:
    commands:
      # Run your tests within this phase.
      - python -c 'print("Hello world!")' &> $OUTPUT_FILE

  post_test:
    commands:
      # Perform any remaining tasks within this phase, such as copying
      # artifacts to the DEVICEFARM_LOG_DIR for upload
      - cp $OUTPUT_FILE $DEVICEFARM_LOG_DIR

artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```

------
#### [  Appium Android  ]

 The following is an example test spec file that configures an Appium Java TestNG test run on Android.. 

```
version: 0.1

# The following fields(s) allow you to select which Device Farm test host is used for your test run. 
android_test_host: {{amazon_linux_2}}

phases:

  # The install phase contains commands for installing dependencies to run your tests.
  # Certain frequently used dependencies are preinstalled on the test host to accelerate and 
  # simplify your test setup. To find these dependencies, versions supported and additional 
  # software installation please see: 
  # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software.html
  install:
    commands:
      # The Appium server is written using Node.js. In order to run your desired version of Appium,
      # you first need to set up a Node.js environment that is compatible with your version of Appium.
      - devicefarm-cli use node 22
      - node --version

      # Use the devicefarm-cli to select a preinstalled major version of Appium.
      - devicefarm-cli use appium 3
      - appium --version

      # The Device Farm service periodically updates the preinstalled Appium versions over time to
      # incorporate the latest minor and patch versions for each major version. If you wish to
      # select a specific version of Appium, you can use NPM to install it.
      # - npm install -g appium@3.3.0

      # When running Android tests with Appium version 3, the UiAutomator2 driver
      # version 6 is pre-installed.
      # If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing uiautomator2 driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "Android" ];
      #   then
      #     appium driver uninstall uiautomator2;
      #     appium driver install uiautomator2@7.1.2;
      #   fi;

      # Based on Appium framework's recommendation, we recommend setting the Appium server's
      # base path explicitly for accepting commands. For Appium 3, this is empty by default.
      # If you prefer the legacy base path of /wd/hub, please set it here.
      - export APPIUM_BASE_PATH=

      # Use the devicefarm-cli to setup a Java environment, with which you can run your test suite.
      - devicefarm-cli use java 17
      - java -version

  # The pre-test phase contains commands for setting up your test environment.
  pre_test:
    commands:
      # Setup the CLASSPATH so that Java knows where to find your test classes.
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/*
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*

      # We recommend starting the Appium server process in the background using the command below.
      # The Appium server log will be written to the $DEVICEFARM_LOG_DIR directory.
      # The environment variables passed as capabilities to the server will be automatically assigned
      # during your test run based on your test's specific device.
      # For more information about which environment variables are set and how they're set, please see
      # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html
      - |-
        appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
          --log-no-colors --relaxed-security --default-capabilities \
          "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
          \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
          \"appium:app\": \"$DEVICEFARM_APP_PATH\", \
          \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID\", \
          \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
          \"appium:automationName\": \"UiAutomator2\"}" \
          >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &

      # This code snippet is to wait until the Appium server starts.
      - |-
        appium_initialization_time=0;
        until curl --silent --fail "http://0.0.0.0:4723${APPIUM_BASE_PATH}/status"; do
          if [[ $appium_initialization_time -gt 30 ]]; then
            echo "Appium did not start within 30 seconds. Exiting...";
            exit 1;
          fi;
          appium_initialization_time=$((appium_initialization_time + 1));
          echo "Waiting for Appium to start on port 4723...";
          sleep 1;
        done;

  # The test phase contains commands for running your tests.
  test:
    commands:
      # Your test package is downloaded and unpackaged into the $DEVICEFARM_TEST_PACKAGE_PATH directory.
      - cd $DEVICEFARM_TEST_PACKAGE_PATH
      - echo "Starting the Appium TestNG test"

      # The following command runs your Appium Java TestNG test.
      # For more information, please see TestNG's documentation here:
      # https://testng.org/#_running_testng
      - |-
        java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
          -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

      # To run your tests with a testng.xml file that is a part of your test package, 
      # use the following commands instead:

      # - echo "Unzipping the tests JAR file"
      # - unzip *-tests.jar
      # - |-
      #   java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
      #     testng.xml -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

  # The post-test phase contains commands that are run after your tests have completed.
  # If you need to run any commands to generate logs and reports on how your test performed,
  # we recommend adding them to this section.
  post_test:
    commands:

# Artifacts are a list of paths on the filesystem where you can store test output and reports.
# All files in these paths will be collected by Device Farm, with certain limits (see limit details
# here: https://docs.aws.amazon.com/devicefarm/latest/developerguide/limits.html#file-limits).
# These files will be available through the ListArtifacts API as your "Customer Artifacts".
artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```

------
#### [  Appium iOS  ]

 The following is an example test spec file that configures an Appium Java TestNG test run on iOS. 

```
version: 0.1

# The following fields(s) allow you to select which Device Farm test host is used for your test run. 
ios_test_host: {{macos_tahoe}}

phases:

  # The install phase contains commands for installing dependencies to run your tests.
  # Certain frequently used dependencies are preinstalled on the test host to accelerate and 
  # simplify your test setup. To find these dependencies, versions supported and additional 
  # software installation please see: 
  # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software.html
  install:
    commands:
      # The Appium server is written using Node.js. In order to run your desired version of Appium,
      # you first need to set up a Node.js environment that is compatible with your version of Appium.
      - devicefarm-cli use node 24
      - node --version

      # Use the devicefarm-cli to select a preinstalled major version of Appium.
      - devicefarm-cli use appium 3
      - appium --version

      # The Device Farm service periodically updates the preinstalled Appium versions over time to
      # incorporate the latest minor and patch versions for each major version. If you wish to
      # select a specific version of Appium, you can use NPM to install it.
      # - npm install -g appium@3.3.0

      # When running iOS tests with Appium version 3, the XCUITest driver version 10 is pre-installed. 
      # If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing XCUITest driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ];
      #   then
      #     appium driver uninstall xcuitest;
      #     appium driver install xcuitest@11.17.7;
      #   fi;

      # Based on Appium framework's recommendation, we recommend setting the Appium server's
      # base path explicitly for accepting commands. For Appium 3, this is empty by default.
      # If you prefer the legacy base path of /wd/hub, please set it here.
      - export APPIUM_BASE_PATH=

      # Use the devicefarm-cli to setup a Java environment, with which you can run your test suite.
      - devicefarm-cli use java 25
      - java -version

  # The pre-test phase contains commands for setting up your test environment.
  pre_test:
    commands:
      # Setup the CLASSPATH so that Java knows where to find your test classes.
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/*
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*

      # Device Farm provides multiple pre-built versions of WebDriverAgent (WDA), a required 
      # Appium dependency for iOS, where each version corresponds to a version of the XCUITest driver. 
      # If Device Farm cannot find a corresponding version of WDA for your XCUITest driver, 
      # the latest available version is selected by default.
      - |-
        APPIUM_DRIVER_VERSION=$(appium driver list --installed --json | jq -r ".xcuitest.version" | cut -d "." -f 1);
        CORRESPONDING_APPIUM_WDA=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V${APPIUM_DRIVER_VERSION}")
        if [[ ! -z "$APPIUM_DRIVER_VERSION" ]] && [[ ! -z "$CORRESPONDING_APPIUM_WDA" ]]; then
          echo "Using a prebuilt version of the WDA app corresponding with your XCUITest driver version ${APPIUM_DRIVER_VERSION}";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $CORRESPONDING_APPIUM_WDA | cut -d "=" -f2)
        else
          LATEST_SUPPORTED_WDA_VERSION=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V" | sort -V -r | head -n 1)
          echo "Unknown driver version $APPIUM_DRIVER_VERSION; falling back to the Device Farm default version of $LATEST_SUPPORTED_WDA_VERSION";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $LATEST_SUPPORTED_WDA_VERSION | cut -d "=" -f2)
        fi;

      # For iOS versions 16 and below only, the device unique identifier (UDID) needs to modified for Appium tests
      # on Device Farm to remove the hyphens.
      - |-
        if [ $(echo $DEVICEFARM_DEVICE_OS_VERSION | cut -d "." -f 1) -le 16 ];
        then
          DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$(echo $DEVICEFARM_DEVICE_UDID | tr -d "-");
        else
          DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$DEVICEFARM_DEVICE_UDID;
        fi;

      # We recommend starting the Appium server process in the background using the command below.
      # The Appium server log will be written to the $DEVICEFARM_LOG_DIR directory.
      # The environment variables passed as capabilities to the server will be automatically assigned
      # during your test run based on your test's specific device.
      # For more information about which environment variables are set and how they're set, please see
      # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html
      - |-
        appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
          --log-no-colors --relaxed-security --default-capabilities \
          "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
          \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
          \"appium:app\": \"$DEVICEFARM_APP_PATH\", \
          \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID_FOR_APPIUM\", \
          \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
          \"appium:derivedDataPath\": \"$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH\", \
          \"appium:usePrebuiltWDA\": true, \
          \"appium:automationName\": \"XCUITest\"}" \
          >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &

      # This code snippet is to wait until the Appium server starts.
      - |-
        appium_initialization_time=0;
        until curl --silent --fail "http://0.0.0.0:4723${APPIUM_BASE_PATH}/status"; do
          if [[ $appium_initialization_time -gt 30 ]]; then
            echo "Appium did not start within 30 seconds. Exiting...";
            exit 1;
          fi;
          appium_initialization_time=$((appium_initialization_time + 1));
          echo "Waiting for Appium to start on port 4723...";
          sleep 1;
        done;

  # The test phase contains commands for running your tests.
  test:
    commands:
      # Your test package is downloaded and unpackaged into the $DEVICEFARM_TEST_PACKAGE_PATH directory.
      - cd $DEVICEFARM_TEST_PACKAGE_PATH
      - echo "Starting the Appium TestNG test"

      # The following command runs your Appium Java TestNG test.
      # For more information, please see TestNG's documentation here:
      # https://testng.org/#_running_testng
      - |-
        java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
          -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

      # To run your tests with a testng.xml file that is a part of your test package, 
      # use the following commands instead:

      # - echo "Unzipping the tests JAR file"
      # - unzip *-tests.jar
      # - |-
      #   java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
      #     testng.xml -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

  # The post-test phase contains commands that are run after your tests have completed.
  # If you need to run any commands to generate logs and reports on how your test performed,
  # we recommend adding them to this section.
  post_test:
    commands:

# Artifacts are a list of paths on the filesystem where you can store test output and reports.
# All files in these paths will be collected by Device Farm, with certain limits (see limit details
# here: https://docs.aws.amazon.com/devicefarm/latest/developerguide/limits.html#file-limits).
# These files will be available through the ListArtifacts API as your "Customer Artifacts".
artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```

------
#### [ Appium (Both Platforms) ]

 The following is an example test spec file that configures an Appium Java TestNG test run on both Android and iOS. 

```
version: 0.1

# The following fields(s) allow you to select which Device Farm test host is used for your test run. 
android_test_host: {{amazon_linux_2}}
ios_test_host: {{macos_tahoe}}

phases:

  # The install phase contains commands for installing dependencies to run your tests.
  # Certain frequently used dependencies are preinstalled on the test host to accelerate and 
  # simplify your test setup. To find these dependencies, versions supported and additional 
  # software installation please see: 
  # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software.html
  install:
    commands:
      # The Appium server is written using Node.js. In order to run your desired version of Appium,
      # you first need to set up a Node.js environment that is compatible with your version of Appium.
      - devicefarm-cli use node 22
      - node --version

      # Use the devicefarm-cli to select a preinstalled major version of Appium.
      - devicefarm-cli use appium 3
      - appium --version

      # The Device Farm service periodically updates the preinstalled Appium versions over time to
      # incorporate the latest minor and patch versions for each major version. If you wish to
      # select a specific version of Appium, you can use NPM to install it.
      # - npm install -g appium@3.3.0

      # When running Android tests with Appium version 3, the UiAutomator2 driver
      # version 6 is pre-installed.
      # If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing uiautomator2 driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "Android" ];
      #   then
      #     appium driver uninstall uiautomator2;
      #     appium driver install uiautomator2@7.1.2;
      #   fi;

      # When running iOS tests with Appium version 3, the XCUITest driver version 10 is pre-installed. 
      # If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing XCUITest driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ];
      #   then
      #     appium driver uninstall xcuitest;
      #     appium driver install xcuitest@11.17.7;
      #   fi;

      # Based on Appium framework's recommendation, we recommend setting the Appium server's
      # base path explicitly for accepting commands. For Appium 3, this is empty by default.
      # If you prefer the legacy base path of /wd/hub, please set it here.
      - export APPIUM_BASE_PATH=

      # Use the devicefarm-cli to setup a Java environment.
      - devicefarm-cli use java 17
      - java -version

  # The pre-test phase contains commands for setting up your test environment.
  pre_test:
    commands:
      # Setup the CLASSPATH so that Java knows where to find your test classes.
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/*
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*

      # Device Farm provides different pre-built versions of WebDriverAgent (WDA), an essential Appium
      # dependency for iOS devices, and each version is suggested for its corresponding version of 
      # XCUITest driver. If Device Farm cannot find a corresponding version of WDA for your XCUITest 
      # driver, the latest available version is selected by default.
      - |-
        if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ]; then
          APPIUM_DRIVER_VERSION=$(appium driver list --installed --json | jq -r ".xcuitest.version" | cut -d "." -f 1);
          CORRESPONDING_APPIUM_WDA=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V${APPIUM_DRIVER_VERSION}")
          if [[ ! -z "$APPIUM_DRIVER_VERSION" ]] && [[ ! -z "$CORRESPONDING_APPIUM_WDA" ]]; then
            echo "Using a prebuilt version of the WDA app corresponding with your XCUITest driver version ${APPIUM_DRIVER_VERSION}";
            DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $CORRESPONDING_APPIUM_WDA | cut -d "=" -f2)
          else
            LATEST_SUPPORTED_WDA_VERSION=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V" | sort -V -r | head -n 1)
            echo "Unknown driver version $APPIUM_DRIVER_VERSION; falling back to the Device Farm default version of $LATEST_SUPPORTED_WDA_VERSION";
            DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $LATEST_SUPPORTED_WDA_VERSION | cut -d "=" -f2)
          fi;
        fi;

      # For iOS versions 16 and below only, the device unique identifier (UDID) needs to modified for Appium tests
      # on Device Farm to remove the hyphens.
      - |-
        if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ]; then
          DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$DEVICEFARM_DEVICE_UDID;
          if [ $(echo $DEVICEFARM_DEVICE_OS_VERSION | cut -d "." -f 1) -le 16 ]; then
            DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$(echo $DEVICEFARM_DEVICE_UDID | tr -d "-");
          fi;
        fi;

      # Appium downloads Chromedriver using a feature that is considered insecure for multitenant
      # environments. This is not a problem for Device Farm because each test host is allocated
      # exclusively for one customer, then terminated entirely. For more information, please see
      # https://github.com/appium/appium/blob/master/packages/appium/docs/en/guides/security.md

      # We recommend starting the Appium server process in the background using the command below.
      # The Appium server log will be written to the $DEVICEFARM_LOG_DIR directory.
      # The environment variables passed as capabilities to the server will be automatically assigned
      # during your test run based on your test's specific device.
      # For more information about which environment variables are set and how they're set, please see
      # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html
      - |-
        if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "Android" ];
        then
          appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
            --log-no-colors --relaxed-security --default-capabilities \
            "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
            \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
            \"browserName\": \"Chrome\", \
            \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID\", \
            \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
            \"appium:chromedriverExecutableDir\": \"$DEVICEFARM_CHROMEDRIVER_EXECUTABLE_DIR\", \
            \"appium:automationName\": \"UiAutomator2\"}" \
            >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &
        else
          appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
            --log-no-colors --relaxed-security --default-capabilities \
            "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
            \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
            \"browserName\": \"Safari\", \
            \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID_FOR_APPIUM\", \
            \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
            \"appium:derivedDataPath\": \"$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH\", \
            \"appium:usePrebuiltWDA\": true, \
            \"appium:automationName\": \"XCUITest\"}" \
            >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &
        fi;

      # This code will wait until the Appium server starts.
      - |-
        appium_initialization_time=0;
        until curl --silent --fail "http://0.0.0.0:4723${APPIUM_BASE_PATH}/status"; do
          if [[ $appium_initialization_time -gt 30 ]]; then
            echo "Appium did not start within 30 seconds. Exiting...";
            exit 1;
          fi;
          appium_initialization_time=$((appium_initialization_time + 1));
          echo "Waiting for Appium to start on port 4723...";
          sleep 1;
        done;

  # The test phase contains commands for running your tests.
  test:
    commands:
      # Your test package is downloaded and unpackaged into the $DEVICEFARM_TEST_PACKAGE_PATH directory.
      - cd $DEVICEFARM_TEST_PACKAGE_PATH
      - echo "Starting the Appium TestNG Web test"

      # The following command runs your Appium Java TestNG test.
      # For more information, please see TestNG's documentation here:
      # https://testng.org/#_running_testng
      - |-
        java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
          -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

      # To run your tests with a testng.xml file, use the following commands instead:
      # - echo "Unzipping the tests JAR file"
      # - unzip *-tests.jar
      # - |-
      #   java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
      #     testng.xml -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

  # The post-test phase contains commands that are run after your tests have completed.
  # If you need to run any commands to generate logs and reports on how your test performed,
  # we recommend adding them to this section.
  post_test:
    commands:

# Artifacts are a list of paths on the filesystem where you can store test output and reports.
# All files in these paths will be collected by Device Farm, with certain limits (see limit details
# here: https://docs.aws.amazon.com/devicefarm/latest/developerguide/limits.html#file-limits).
# These files will be available through the ListArtifacts API as your "Customer Artifacts".
artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```

------

## Hosts for custom test environments
<a name="custom-test-environments-hosts"></a>

**Note**  
iOS 27 public devices are now available on Device Farm, served by the macos\_tahoe test host running Xcode 27. Point your test spec at macos\_tahoe and choose an iOS 27 device to get started.

 Device Farm supports a set of operating systems with pre-configured software through the use of a test host environment. During test execution, Device Farm utilizes Amazon-managed instances (hosts) that dynamically connect to the selected device under test. This instance is fully cleaned up and not re-used between runs, and is terminated with its generated artifacts after the test run concludes. 

**Topics**
+ [Available test hosts for custom test environments](#custom-test-environments-hosts-available)
+ [Selecting a test host for custom test environments](#test-host-selection)
+ [Operating system version](#test-host-os)
+ [Supported software within custom test environments](#custom-test-environments-hosts-software)
+ [Test environment for Android devices](#custom-test-environments-hosts-android)
+ [Test environment for iOS devices](#custom-test-environments-hosts-ios)

### Available test hosts for custom test environments
<a name="custom-test-environments-hosts-available"></a>

 The test hosts are fully managed by Device Farm. The following table lists the currently available and supported Device Farm test hosts for custom test environments. 


| Device Platform | Test Host | Operating System | Architecture(s) | Supported Devices | 
| --- | --- | --- | --- | --- | 
|  Android  |  amazon\_linux\_2  |  Amazon Linux 2  |  x86\_64  | Android 6 and above | 
|  iOS  |  macos\_tahoe  | macOS Tahoe (version 26) |  arm64  | iOS 17 to 27 | 
|  iOS  |  macos\_sequoia  | macOS Sequoia (version 15) |  arm64  | iOS 15 to 26 | 

**Note**  
Periodically, Device Farm adds new test hosts for a device platform to support newer device OS versions and its dependencies. When this occurs, older test hosts for the respective device platform are subject to end of support.

### Selecting a test host for custom test environments
<a name="test-host-selection"></a>

To select your desired test host, specify the Android and iOS test host in the appropriate `android_test_host` and `ios_test_host` variables of your [test spec file](#custom-test-environment-test-spec-syntax).

You can select a test host in one of the following ways:

1. **Select a specific host** – You name the exact test host you want to use.

1. **Let Device Farm choose** – You set the test host to `default`, and Device Farm picks the host based on the device's OS version.

1. **Use the fallback host** – You omit the field, and Device Farm assigns a legacy test host as a fallback. ***This option is not recommended.*** For more information, see the [Legacy iOS test host](#legacy-ios-host).

Managing test hosts is a shared responsibility between Device Farm and you. Your responsibilities vary depending on the selection type you choose. This is summarized in the following table for the recommended selection types.


| Selection type | Device Farm's responsibility | Customer's responsibility | 
| --- | --- | --- | 
| [Select a specific host](#select-specific-test-host) | Run your tests on the exact host you name, with a consistent set of software versions on every run. | Specify the host that provides the software versions your tests require (for example, macos\_sequoia or amazon\_linux\_2). Update your test spec to a newer host for each major device OS version, because Device Farm ends support for older hosts over time. | 
| [Let Device Farm choose](#select-default-ios-test-host) | Select a host that is compatible with the device's OS version, and route your tests on future OS versions to a supported host. | Set the test host value to `default`. If your tests require a specific software version, specify the host explicitly instead, because in rare cases an older version of a dependency might not be available on a newer host. | 

For more information about shared responsibility with AWS, see the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) on the AWS website.

#### Option 1: Select a specific host
<a name="select-specific-test-host"></a>

When you create your test spec file, provide the exact test host value in the corresponding `android_test_host` or `ios_test_host` field.

**Example**  

```
version: 0.1
android_test_host: {{amazon_linux_2}}
ios_test_host: {{macos_tahoe}}

phases:
  # ...
```

#### Option 2: Let Device Farm choose
<a name="select-default-ios-test-host"></a>

You can set the test host to the value `default` to have Device Farm select a host based on the OS version of the device under test.

**Note**  
For the time being, `default` applies to `ios_test_host` only. Support for `android_test_host` is planned for a future release.

The following table shows the default host mapping by device OS version.


| Platform | Device OS version | Assigned test host | 
| --- | --- | --- | 
| iOS | 17 to 27 | macos\_tahoe | 
| iOS | 15 to 16 | macos\_sequoia | 

**Example**  

```
version: 0.1
ios_test_host: default

phases:
  # ...
```

### Operating system version
<a name="test-host-os"></a>

 Each available test host uses a specific version of the operating system supported on Device Farm at the time. Device Farm periodically updates the operating system with minor version updates and security patches. 

 You can find the exact OS version used during your test run, including the minor version. To do this, add the following snippet to any phase of your test spec file: 

**Example**  

```
phases:
  install:
    commands:
      # The following example prints the instance's operating system version details
      - |-
        if [[ "Darwin" == "$(uname)" ]]; then
          echo "$(sw_vers --productName) $(sw_vers --productVersion) ($(sw_vers --buildVersion))";
        else
          echo "$(. /etc/os-release && echo $PRETTY_NAME) ($(uname -r))";
        fi
```

### Supported software within custom test environments
<a name="custom-test-environments-hosts-software"></a>

 Device Farm uses host machines that are pre-installed with many of the necessary software libraries to run test frameworks supported on our service, providing a ready testing environment on launch. Device Farm supports multiple languages through the use of our software selection mechanism, and will periodically update the versions of the languages included in the environment. 

For any other required software, you can modify the test spec file to install from your test package, download from the internet, or access private sources within your VPC (see [VPC ENI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni.html) for more information). For more information, see [Test spec examples](#custom-test-environment-test-spec-example).

#### Pre-configured software
<a name="custom-test-environments-hosts-software-configured"></a>

 In order to facilitate device testing on each platform, the following tooling is provided on the test host: 


| Tools | Device Platform(s) | 
| --- | --- | 
|  Android SDK Build-Tools  |  Android  | 
|  Android SDK Platform-Tools (includes `adb`)  |  Android  | 
|  Xcode  |  iOS  | 

#### Selectable software
<a name="custom-test-environments-hosts-software-selection"></a>

 In addition to the pre-configured software on the host, Device Farm offers a way to select certain versions of supported software via the `devicefarm-cli` tooling. 

 The following table contains the selectable software and the test hosts that contain them. 


| Software / Tool | Hosts that support this software | Command to use in your test spec | 
| --- | --- | --- | 
|  Java 25  |  macos\_tahoe  |  `devicefarm-cli use java 25`  | 
|  Java 17  |  amazon\_linux\_2 <br /> macos\_sequoia <br /> macos\_tahoe  |  `devicefarm-cli use java 17`  | 
|  Java 11  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use java 11`  | 
|  Java 8  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use java 8`  | 
|  Node.js 24  |  macos\_tahoe  |  `devicefarm-cli use node 24`  | 
|  Node.js 22  |  amazon\_linux\_2 <br /> macos\_sequoia <br /> macos\_tahoe  |  `devicefarm-cli use node 22`  | 
|  Node.js 20  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use node 20`  | 
|  Node.js 18  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use node 18`  | 
|  Node.js 16  |  amazon\_linux\_2  |  `devicefarm-cli use node 16`  | 
|  Python 3.14  |  macos\_tahoe  |  `devicefarm-cli use python 3.14`  | 
|  Python 3.12  |  amazon\_linux\_2 <br /> macos\_sequoia <br /> macos\_tahoe  |  `devicefarm-cli use python 3.12`  | 
|  Python 3.11  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use python 3.11`  | 
|  Python 3.10  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use python 3.10`  | 
|  Python 3.9  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use python 3.9`  | 
|  Python 3.8  |  amazon\_linux\_2  |  `devicefarm-cli use python 3.8`  | 
|  Ruby 4.0  |  amazon\_linux\_2 <br /> macos\_tahoe  |  `devicefarm-cli use ruby 4.0`  | 
|  Ruby 3.2  |  amazon\_linux\_2 <br /> macos\_sequoia  |  `devicefarm-cli use ruby 3.2`  | 
|  Ruby 2.7  |  amazon\_linux\_2  |  `devicefarm-cli use ruby 2.7`  | 
|  Appium 3  |  amazon\_linux\_2 <br /> macos\_sequoia <br /> macos\_tahoe  |  `devicefarm-cli use appium 3`  | 
|  Appium 2  |  amazon\_linux\_2 <br /> macos\_sequoia <br /> macos\_tahoe  |  `devicefarm-cli use appium 2`  | 
|  Appium 1  |  amazon\_linux\_2  |  `devicefarm-cli use appium 1`  | 
|  Xcode 27  |  macos\_tahoe <br />(supports iOS 18 to 27) |  `devicefarm-cli use xcode 27`  | 
|  Xcode 26  |  macos\_sequoia <br /> macos\_tahoe  |  `devicefarm-cli use xcode 26`  | 
|  Xcode 16  |  macos\_sequoia  |  `devicefarm-cli use xcode 16`  | 

The test host also includes commonly used supporting tools for each software version, such as the `pip` and `npm` package managers (included with Python and Node.js respectively) and dependencies (such as the Appium UIAutomator2 Driver) for tools like Appium. This ensures you have the tools needed to work with the supported test frameworks.

#### Using the devicefarm-cli tool in custom test environments
<a name="custom-test-environments-hosts-software-cli"></a>

The test host uses a standardized version management tool called ` devicefarm-cli` to select software versions. This tool is separate from the AWS CLI and only available on the Device Farm test host. With `devicefarm-cli`, you can switch to any pre-installed software version on the test host. This provides a straightforward way to maintain your Device Farm test spec file over time and gives you a predictable mechanism to upgrade software versions in the future.

**Important**  
 This command line tool is not available on legacy iOS hosts. For more information, see the topic on the [Legacy iOS test host](#legacy-ios-host). 

The snippet below shows the `help` page of `devicefarm-cli`:

```
$ devicefarm-cli help
 Usage: devicefarm-cli COMMAND [ARGS]
     
     Commands:
         help                         Prints this usage message.
         list                         Lists all versions of software configurable
                                      via this CLI.
         use <software> <version>     Configures the software for usage within the
                                      current shell's environment.
```

Let's review a couple of examples using `devicefarm-cli`. To use the tool to change the Python version from {{3.10}} to {{3.9}} in your test spec file, run the following commands:

```
$ python --version
Python 3.10.12
$ devicefarm-cli use python 3.9
$ python --version
Python 3.9.17
```

To change the Appium version from {{1}} to {{2}} :

```
$ appium --version
1.22.3
$ devicefarm-cli use appium 2
$ appium --version
2.1.2
```

**Tip**  
Note that when you select a software version, `devicefarm-cli` also switches the supporting tools for those languages, such as `pip` for Python and `npm` for NodeJS. 

For more information about the preinstalled software on the test host, see [Supported software within custom test environments](#custom-test-environments-hosts-software).

### Test environment for Android devices
<a name="custom-test-environments-hosts-android"></a>

For the full list of available test hosts and how to select one, see [Hosts for custom test environments](#custom-test-environments-hosts). 

AWS Device Farm utilizes Amazon Elastic Compute Cloud (EC2) host machines running Amazon Linux 2 to execute Android tests. When you schedule a test run, Device Farm allocates a dedicated host for each device to independently run tests. The host machines terminate after the test run along with any generated artifacts. 

The Amazon Linux 2 host provides several advantages: 
+ **Faster, more reliable testing**: Compared to the legacy host, the new test host significantly improves test speed, especially reducing test start times. The Amazon Linux 2 host also demonstrates greater stability and reliability during testing.
+ **Enhanced Remote Access for manual testing**: Upgrades to the latest test host and improvements lead to lower latency and better video performance for Android manual testing. 
+ **Standard software version selection**: Device Farm now standardizes major programming language support on the test host as well as Appium framework versions. For supported languages (currently Java, Python, Node.js, and Ruby) and Appium, the new test host provides long-term stable releases soon after launch. Centralized version management through the `devicefarm-cli` tool enables test spec file development with a consistent experience across frameworks. 

**Topics**
+ [Supported IP ranges for the Amazon Linux 2 test environment in Device Farm](#amazon-linux-2-ip-ranges)

#### Supported IP ranges for the Amazon Linux 2 test environment in Device Farm
<a name="amazon-linux-2-ip-ranges"></a>

Customers often need to know the IP range from which Device Farm's traffic originates, particularly for configuring their firewalls and security settings. For Amazon EC2 test hosts, the IP range encompasses the entire `us-west-2` region. For Amazon Linux 2 test hosts, which is the default option for new Android runs, the ranges have been restricted. The traffic now originates from a specific set of NAT gateways, restricting the IP range to the following addresses:



| IP Ranges | 
| --- | 
| **44.236.137.143** | 
| **52.13.151.244** | 
| **52.35.189.191** | 
| **54.201.250.26** | 

For more information about Android test environments in Device Farm, see [Test environment for Android devices](#custom-test-environments-hosts-android).

### Test environment for iOS devices
<a name="custom-test-environments-hosts-ios"></a>

 For the full list of available test hosts and how to select one, see [Hosts for custom test environments](#custom-test-environments-hosts). 

 Device Farm utilizes Amazon-managed macOS instances (hosts) that dynamically connect to the iOS device during the test run. Each host is pre-configured with software that enables device testing on various popular test platforms, such as XCTestUI and Appium. 

 The current iteration of the iOS test host has improved upon the testing experience when compared to previous versions, including: 
+  ** Consistent host OS and tooling experience for iOS 15 and greater ** Before, the test host was determined by the device in use, leading to a fragmented software environment when executing on multiple iOS versions. The current experience allows simple host selection to enable a consistent environment across devices. This will enable the same macOS version and tooling (such as Xcode) to be available across each iOS device. 
+  ** Performance improvements ** Using updated infrastructure, test setup time has improved substantially.
+  ** Standardized selectable software versions for supported dependencies ** We now have the `devicefarm-cli` software selection system on both iOS and Android test hosts, enabling you to select your preferred version of our supported dependencies. For supported dependencies (such as Java, Python, Node.js, Ruby, and Appium), versions will be selectable via the test spec. For an idea of how this feature works, please see the topic on [Supported software within custom test environments](#custom-test-environments-hosts-software).

**Warning**  
 If you test on iOS 18 or below and don't explicitly select a test host, Device Farm runs your tests on a legacy test host as a fallback. Legacy test hosts are not recommended. To move to a supported test host, see [Migrating your custom test environments to the new iOS test hosts](#ios-host-migration). 

#### Legacy iOS test host
<a name="legacy-ios-host"></a>

 For existing tests on iOS 18 and below, Device Farm uses a legacy test host as a fallback when you don't explicitly select a test host for custom test environments. Legacy test hosts are not recommended. We recommend that you select a test host explicitly, or set `ios_test_host` to `default`. Legacy test hosts are not available for iOS 26 and greater; those versions require a supported test host. The following table contains the test host version that is used for each iOS device version. 


| Operating System | Architecture(s) | Default for Devices | 
| --- | --- | --- | 
|  macOS Sonoma (version 14)  |  arm64  |  iOS 18  | 
|  macOS Ventura (version 13) |  arm64  |  iOS 17  | 
|  macOS Monterey (version 12) |  x86\_64  |  iOS 16 and below | 

 In order to select the newer test hosts, see the topic regarding [Migrating your custom test environments to the new iOS test hosts](#ios-host-migration). 

#### Supported software for iOS devices
<a name="ios-host-software-support"></a>

 In order to support iOS device testing, Device Farm test hosts for iOS devices come pre-configured with Xcode and its associated command line tooling. For other available software, please review the topic regarding [Supported software within custom test environments](#custom-test-environments-hosts-software). 

#### Migrating your custom test environments to the new iOS test hosts
<a name="ios-host-migration"></a>

 For the full list of available test hosts and how to select one, see [Hosts for custom test environments](#custom-test-environments-hosts). 

 To migrate existing tests from the legacy host to the new macOS test host, you will need to develop new test spec files based on your pre-existing ones. 

 The recommended approach is to start with the example test spec file for your desired test types, then migrate relevant commands from your old test spec file to the new one. This lets you leverage new features and optimizations of the example test spec for the new host while reusing snippets your existing code. 

**Topics**
+ [Tutorial: Migrating iOS test spec files with the console](#ios-host-migration-console-tutorial)
+ [Differences between the new and legacy test hosts](#ios-host-migration-differences)

##### Tutorial: Migrating iOS test spec files with the console
<a name="ios-host-migration-console-tutorial"></a>

 In this example, the Device Farm console will be used to onboard an existing iOS device test spec to use the new test host. 

###### Step 1: Creating a new test spec files with the console
<a name="ios-host-migration-console-tutorial-step1"></a>

1. Decide which test host you want to use. For the list of available iOS test hosts and how to select one, see [Hosts for custom test environments](#custom-test-environments-hosts).

1. Sign in to the [AWS Device Farm console](https://console.aws.amazon.com/devicefarm).

1. Navigate to the Device Farm project containing your automation tests.

1. Download a copy of the existing test spec your wish to onboard with.

   1. Click the "Project Settings" option and navigate to the **Uploads** tab.

   1. Navigate to the test spec file that you wish to onboard with.

   1. Click the **Download** button to make a local copy of this file.

1. Navigate back to the Project page and click **Create run**.

1. Fill in the options on the wizard as if you were to start a new run, but stop at the **Select test spec** option.

1. Using the iOS test spec selected by default, click the **Create a test spec** button.

1. Modify the test specification that was selected by *default* in the text editor.

   1.  Set `ios_test_host` to the test host that fits your test requirements. For example: 

      ```
      ios_test_host: macos_tahoe
      ```

   1. From the copy of your test spec downloaded in a prior step, review each ` phase`.

   1.  Copy commands from the old test spec's phases into each respective phase in the new test spec, ignoring commands related to installing or selecting Java, Python, Node.js, Ruby, Appium, or Xcode. 

1.  Enter a new file name in the **Save as** text box.

1.  Click the **Save as new** button to save your changes. 

 For an example of a test spec file you can use as a reference, see the example provided in [Test spec examples](#custom-test-environment-test-spec-example). 

###### Step 2: Selecting software pre-installed software
<a name="ios-host-migration-console-tutorial-step2"></a>

 In the new test host, pre-installed software versions are selected using a new standardized version management tool called `devicefarm-cli`. This tooling is now the recommended approach for using the various software we provide on the test hosts. 

 For example, add the following line to use JDK 25 in your test environment: 

```
- devicefarm-cli use java 25
```

 For more information on the software supported available, please review: [Supported software within custom test environments](#custom-test-environments-hosts-software). 

###### Step 3: Using Appium and its dependencies via the software selection tooling
<a name="ios-host-migration-console-tutorial-step3"></a>

 Explicitly select the Appium version using the `devicefarm-cli`. On the macos\_tahoe test host, Appium 3 is the default version: 

```
- devicefarm-cli use appium 3 # Selects the version
- appium --version            # Prints the version
```

The Appium version selected with `devicefarm-cli` comes preinstalled with a compatible version of the XCUITest driver for iOS.

When you use the default test spec, Device Farm automatically selects WebDriverAgent (WDA) to match your installed XCUITest driver. For more information about how this selection works, see [Selecting a WebDriverAgent version for iOS tests](#test-types-appium-select-wda) and [Environment variables for Appium tests](#custom-test-environment-variables-appium).

##### Differences between the new and legacy test hosts
<a name="ios-host-migration-differences"></a>

 When you're editing your test spec file to use the new iOS test host and transitioning your tests from the legacy test host, be aware of these key environment differences: 
+  ** Xcode versions: ** In the legacy test host environment, the Xcode version available was based on the iOS version of the device used for testing. For example, tests on iOS 18 devices used Xcode 16 in the legacy host, whereas tests on iOS 17 used Xcode 15. In the new host environment, all devices can access the same versions of Xcode, allowing a consistent environment for tests on devices with different versions. For a list of currently available Xcode versions, see [Supported software](#custom-test-environments-hosts-software). 
+  ** Selecting software versions: ** In many instances, the default software versions have changed, so if you weren't explicitly selecting your software version in the legacy test host before, you may want to specify it now in the new test host using [`devicefarm-cli`](#custom-test-environments-hosts-software-cli). In the vast majority of use cases, we recommend that customers explicitly select the versions of software they use. By selecting a software version with `devicefarm-cli` you'll have a predictable and consistent experience with it and receive ample amounts of warnings if Device Farm plans to remove that version from the test host. 

   Moreover, software selection tools like `nvm`, `pyenv`, ` avm`, and `rvm` have been removed in favor of the new ` devicefarm-cli` software selection system. 
+  ** Available software versions: ** Many versions of previously pre-installed software have been removed, and many new versions have been added. So, ensure that when using the `devicefarm-cli` to select your software versions, you select versions which are in the [supported version list](#custom-test-environments-hosts-software).
+  ** The `libimobiledevice` suite of tools have been removed ** in favor of newer / first party tooling to track current iOS device testing and industry standards. For iOS 17 and above, you can migrate most commands to use similar Xcode tooling, called `devicectl`. For information on `devicectl`, you can run `xcrun devicectl help` from a machine with Xcode installed.
+  ** File paths that are hard-coded ** in your legacy host test spec file as absolute paths will most likely not work as expected in the new test host, and they're generally not recommended for test spec file use. We recommend that you use relative paths and environment variables for all test spec file code. For more information, review the topic on [Best practices for custom test environment execution](#custom-test-environments-best-practices). 
+  ** Operating system version and architecture: ** The legacy test hosts were using a variety of macOS versions and CPU architectures based on the assigned device. As a result, users may notice some differences in the available system libraries available in the environment. For more information on the previous host OS version, review [Legacy iOS test host](#legacy-ios-host). 
+  **For Appium** users, the way to select the WebDriverAgent has changed to a use environment variable prefix ` DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V` instead of the old ` DEVICEFARM_WDA_DERIVED_DATA_PATH_V` prefix. For more information on the updated variable, review [Environment variables for Appium tests](#custom-test-environment-variables-appium).
+  **For Appium Java** users, the new test host does not contain any pre-installed JAR files in its class path, whereas the previous host contained one for the TestNG framework (via an environment variable `$DEVICEFARM_TESTNG_JAR`). We recommend that customers package the necessary JAR files for their test frameworks inside their test package and remove instances of the `$DEVICEFARM_TESTNG_JAR` variable from their test spec files.

 We recommend reaching out to the service team through a support case if you have any feedback or questions about the differences between the test hosts from a software perspective. 

## Access AWS resources using an IAM Execution Role
<a name="custom-test-environments-iam-roles"></a>

 Device Farm supports specifying an IAM role that will be assumed by the custom test runtime environment during test execution. This feature allows your tests to securely access AWS resources in your account, such as Amazon S3 buckets, DynamoDB tables, or other AWS services on which your application depends. 

**Topics**
+ [Overview](#iam-execution-role-overview)
+ [IAM role requirements](#iam-role-requirements)
+ [Configuring an IAM execution role](#configuring-iam-execution-role)
+ [Best practices](#iam-role-best-practices)
+ [Troubleshooting](#troubleshooting-iam-roles)

### Overview
<a name="iam-execution-role-overview"></a>

 When you specify an IAM execution role, Device Farm assumes this role during test execution, allowing your tests to interact with AWS services using the permissions defined in the role. 

 Common use cases for IAM execution roles include: 
+ Accessing test data stored in Amazon S3 buckets
+ Pushing test artifacts to Amazon S3 buckets
+ Retrieving application configuration from AWS AppConfig
+ Writing test logs and metrics to Amazon CloudWatch
+ Sending test results or status messages to Amazon SQS queues
+ Calling AWS Lambda functions as part of test workflows

### IAM role requirements
<a name="iam-role-requirements"></a>

 To use an IAM execution role with Device Farm, your role must meet the following requirements: 
+ **Trust relationship**: The Device Farm service principal must be trusted to assume the role. The trust policy must include `devicefarm.amazonaws.com` as a trusted entity.
+ **Permissions**: The role must have the necessary permissions to access the AWS resources your tests require.
+ **Session duration**: The role's maximum session duration must be at least as long as your Device Farm project's job timeout setting. By default, Device Farm projects have a job timeout of 150 minutes, so your role must support a session duration of at least 150 minutes.
+ **Same account requirement**: The IAM role must be in the same AWS account as the one used to call Device Farm. Cross-account role assumption is not supported.
+ **PassRole permission**: The caller must be authorized to pass the IAM role by a policy allowing the `iam:PassRole` action on the specified execution role.

#### Example trust policy
<a name="trust-policy-example"></a>

 The following example shows a trust policy that allows Device Farm to assume your execution role. This trust policy should only be attached to the specific IAM role you intend to use with Device Farm, not to other roles in your account: 

**Example**  

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "devicefarm.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

#### Example permissions policy
<a name="permissions-policy-example"></a>

 The following example shows a permissions policy that grants access to common AWS services used in testing: 

**Example**  

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-test-bucket",
        "arn:aws:s3:::my-test-bucket/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "appconfig:GetConfiguration",
        "appconfig:StartConfigurationSession"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:log-group:/devicefarm/test-*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "sqs:SendMessage",
        "sqs:GetQueueUrl"
      ],
      "Resource": "arn:aws:sqs:*:*:test-results-*"
    }
  ]
}
```

### Configuring an IAM execution role
<a name="configuring-iam-execution-role"></a>

 You can specify an IAM execution role at the project level or for individual test runs. When configured at the project level, all runs within that project will inherit the execution role. An execution role configured on a run will supersede any configured on its parent project. 

 For detailed instructions on configuring execution roles, see: 
+ [Creating a project in AWS Device Farm](#how-to-create-project) - for configuring execution roles at the project level
+ [Creating a test run in Device Farm](#how-to-create-test-run) - for configuring execution roles for individual runs

 You can also configure execution roles using the Device Farm API. For more information, see the [Device Farm API Reference](https://docs.aws.amazon.com/devicefarm/latest/APIReference/). 

### Best practices
<a name="iam-role-best-practices"></a>

 Follow these best practices when configuring IAM execution roles for your Device Farm tests: 
+ **Principle of least privilege**: Grant only the minimum permissions necessary for your tests to function. Avoid using overly broad permissions like `*` actions or resources.
+ **Use resource-specific permissions**: When possible, limit permissions to specific resources (e.g., specific S3 buckets or DynamoDB tables) rather than all resources of a type.
+ **Separate test and production resources**: Use dedicated test resources and roles to avoid accidentally affecting production systems during testing.
+ **Regular role review**: Periodically review and update your execution roles to ensure they still meet your testing needs and follow security best practices.
+ **Use condition keys**: Consider using IAM condition keys to further restrict when and how the role can be used.

### Troubleshooting
<a name="troubleshooting-iam-roles"></a>

 If you encounter issues with IAM execution roles, check the following: 
+ **Trust relationship**: Verify that the role's trust policy includes `devicefarm.amazonaws.com` as a trusted service.
+ **Permissions**: Check that the role has the necessary permissions for the AWS services your tests are trying to access.
+ **Test logs**: Review the test execution logs for specific error messages related to AWS API calls or permission denials.

## Environment variables for custom test environments
<a name="custom-test-environment-variables"></a>

 Device Farm dynamically configures several environment variables for use as part of your custom test environment run. 

**Topics**
+ [Custom environment variables](#custom-test-environment-variables-custom)
+ [Common environment variables](#custom-test-environment-variables-common)
+ [Environment variables for Appium tests](#custom-test-environment-variables-appium)
+ [Environment variables for XCUITest tests](#custom-test-environment-variables-xcuitest)

### Custom environment variables
<a name="custom-test-environment-variables-custom"></a>

 Device Farm supports the configuration of key-value pairs that are applied as environment variables on the test host. These may be configured on a Device Farm project or during run creation; any variables configured on a run will supersede any that may be configured on its parent project. The following restrictions apply: 
+ Custom environment variables are not supported on legacy iOS test hosts. For more information, see [Legacy iOS test host](#legacy-ios-host).
+ Variable names beginning with `$DEVICEFARM_` are reserved for internal service use.
+ Custom environment variables may not be used to configure test host compute selection in your test spec.

### Common environment variables
<a name="custom-test-environment-variables-common"></a>

 This section describes environment variables common to all tests in Device Farm. 

** `$DEVICEFARM_DEVICE_NAME` **  
 The device on which your tests run. It represents the unique device identifier (UDID) of the device. 

** `$DEVICEFARM_DEVICE_UDID` **  
 The device's unique identifier. 

** `$DEVICEFARM_DEVICE_PLATFORM_NAME` **  
 The device's platform name. It is either `Android` or `iOS`. 

** `$DEVICEFARM_DEVICE_OS_VERSION` **  
 The device's OS version. 

** `$DEVICEFARM_APP_PATH` **  
 *(mobile app tests)*   
 The path to the mobile app on the host machine where the tests are being executed. This variable is not available during web tests. 

** `$DEVICEFARM_LOG_DIR` **  
 The path to the default directory where customer logs, artifacts, and other wanted files will be stored for later retrieval. Using an [example test spec](#custom-test-environment-test-spec-example), files in this directory are archived in a ZIP file and made available as an artifact after your test run. 

** `$DEVICEFARM_SCREENSHOT_PATH` **  
 The path to the screenshots, if any, captured during the test run. 

** `$DEVICEFARM_PROJECT_ARN` **  
 The ARN of the job's parent project. 

** `$DEVICEFARM_RUN_ARN` **  
 The ARN of the job's parent run. 

** `$DEVICEFARM_DEVICE_ARN` **  
 The ARN of the device under test. 

** `$DEVICEFARM_TOTAL_JOBS` **  
 The total number of jobs associated with its parent Device Farm run. 

** `$DEVICEFARM_JOB_NUMBER` **  
 This job's number within `$DEVICEFARM_TOTAL_JOBS`. For example, a run may contain 5 jobs, and each will have a unique `$DEVICEFARM_JOB_NUMBER` ranging from 0 to 4. 

** `$AWS_REGION` **  
 The AWS region. The service will set this to match the region in which the device under test is located. It can be overridden by a custom environment variable if needed. 

** `$ANDROID_HOME` **  
 *(Android only)*   
 The path to the Android SDK installation directory. 

### Environment variables for Appium tests
<a name="custom-test-environment-variables-appium"></a>

 This section describes environment variables used by any Appium test in a custom test environment in Device Farm. 

** `$DEVICEFARM_CHROMEDRIVER_EXECUTABLE_DIR` **  
 *(Android only)*   
 The location of a directory which contains the necessary ChromeDriver executables for use in Appium web and hybrid tests. 

** `$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V<N>` **  
 *(iOS only)*   
 The derived data path of a version of WebDriverAgent built to run on Device Farm. The numbering on the variable will correspond to the major version of the WebDriverAgent. As an example, `DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V9` will point to the a WebDriverAgent version of 9.x. For more information, see [Selecting a WebDriverAgent version for iOS tests](#test-types-appium-select-wda).  
 The `$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V<N>` environment variables are only present on non-legacy iOS hosts. For more information, see [Legacy iOS test host](#legacy-ios-host). 

** `$DEVICEFARM_WDA_DERIVED_DATA_PATH_V9` **  
 *(iOS only, deprecated)*   
 The derived data path of a version of WebDriverAgent built to run on Device Farm. Refer to `$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V<N>` for the replacement naming scheme.

### Environment variables for XCUITest tests
<a name="custom-test-environment-variables-xcuitest"></a>

 This section describes environment variables used by the XCUITest test in a custom test environment in Device Farm. 

** `$DEVICEFARM_XCUITESTRUN_FILE` **  
 The path to the Device Farm `.xctestun` file. It is generated from your app and test packages. 

** `$DEVICEFARM_DERIVED_DATA_PATH` **  
Expected path of Device Farm xcodebuild output.

** `$DEVICEFARM_XCTEST_BUILD_DIRECTORY` **  
The path to the unzipped contents of the test package file.

## Best practices for custom test environment execution
<a name="custom-test-environments-best-practices"></a>

 The following topics cover recommended best practices for using custom test execution with Device Farm. 

**Run configuration**
+  ** Rely on Device Farm managed software and API features for run configuration ** wherever possible, as opposed to applying similar configurations via shell commands in the test spec file. This includes the configuration of the test host and the device, as this will be more sustainable and consistent across test hosts and devices. 

   While Device Farm encourages you to customize your test spec file as greatly as you need in order to run your tests, the test spec file can become difficult to maintain over time as more customized commands are added to it. Using Device Farm managed software (through tools like ` devicefarm-cli` and the default available tools in the `$PATH`), and using managed features (like the [`deviceProxy`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRunConfiguration.html#devicefarm-Type-ScheduleRunConfiguration-deviceProxy) request parameter) to simplify the test spec file by shifting the responsibility of maintenance to Device Farm itself. 

**Test spec and test package code**
+  **Do not use absolute paths or rely on specific minor versions ** in your test spec file or test package code. Device Farm applies routine updates to the selected test host and its included software versions. Using specific or absolute paths (such as ` /usr/local/bin/python` instead of `python`) or requiring specific minor versions (such as Node.js `20.3.1` instead of just ` 20`) may lead to your tests failing to locate the required executable / file. 

   As part of the custom test execution, Device Farm sets up various environment variables and the `$PATH` variable to ensure tests to have a consistent experience within our dynamic environments. See [Environment variables for custom test environments](#custom-test-environment-variables) and [Supported software within custom test environments](#custom-test-environments-hosts-software) for more information. 
+  **Save generated or copied files within the temp directory during the test run. ** Today, we make sure that the temp directory (`/tmp`) will be accessible to the user during the test execution (besides managed directories, such as the `$DEVICEFARM_LOG_DIR`). Other directories that the user has access to may change over time due to the needs of the service or the operating system in use. 
+  **Save your test execution logs to `$DEVICEFARM_LOG_DIR`**. This is the default artifact directory provided for your execution to add execution logs / artifacts into. The [example test specs](#custom-test-environment-test-spec-example) we provide each uses this directory for artifacts by default. 
+  **Ensure your commands return a non-zero code on failure** during the `test` phase of your test spec. We determine if your execution failed by checking for a non-zero exit code of each shell command invoked during the `test` phase. You should ensure your logic or test framework will return a non-zero exit code for all desired scenarios, which may require additional configuration. 

   For example, certain test frameworks (such as JUnit5) do not consider zero tests run to be a failure, which will cause your tests to be detected to have run successfully even if nothing was executed. Using JUnit5 as the example, you would need to specify the command line option `--fail-if-no-tests` to ensure this scenario exits with a non-zero exit code. 
+  **Review the compatibility of software** with the device OS version and test host version you will be using for the test run. As an example, there are certain features in testing software frameworks (ie: Appium) that may not work as intended on all OS versions of the device being tested. 

**Security**
+  ** Avoid storing or logging sensitive variables (like AWS keys) in your test spec file. ** Test spec files, the test spec generated scripts, and the test spec script's logs are all provided as downloadable artifacts at the end of the test execution. This may lead to the unintended exposure of secrets for other users in your account with read access to your test run.

## Migrating tests from a standard to custom test environment
<a name="custom-test-environment-migration"></a>

You can switch from a standard test execution mode to a custom execution mode in AWS Device Farm. Migration primarily involves two different forms of execution:

1. **Standard mode**: This test execution mode is primarily built to provide customers with granular reporting and a fully-managed environment. 

1. **Custom mode**: This test execution mode is built for different use cases that require faster test runs, the ability to lift and shift and achieve parity with their local environment, and live video streaming.

For more information about standard and custom modes in Device Farm, see [Test environments in AWS Device Farm](#test-environments) and [Custom test environments in AWS Device Farm](#custom-test-environments).

### Considerations when migrating
<a name="considerations-when-migrating"></a>

This section lists some of the prominent use cases to consider when migrating to the custom mode:

1. **Speed**: In the standard mode of execution, Device Farm parses the metadata of the tests that you have packaged and uploaded using the packaging instructions for your particular framework. Parsing detects the number of tests in your package. Thereafter, Device Farm runs each test separately and presents the logs, videos, and other result artifacts individually for each test. However, this steadily adds to the total end-to-end test execution time as there are the pre- and post-processing of tests and result artifacts on the service end. 

   By contrast, the custom mode of execution doesn't parse your test package; this means no pre-processing and minimal post-processing for tests or result artifacts. This results in total end-to-end execution times close to your local setup. The tests are executed in the same format as they would be if they ran on your local machine(s). The results of the tests are the same as what you get locally and are available for download at the end of the job execution. 

1. **Customization or Flexibility**: The standard mode of execution parses your test package to detect the number of tests and then runs each test separately. Note that there is no guarantee that the tests will run in the order you specified. As a result, tests requiring a particular sequence of execution may not work as expected. In addition, there is no way to customize the host machine environment or pass config files that may be needed to run your tests a certain way. 

   By contrast, custom mode lets you configure the host machine environment including the ability to install additional software, pass filters to your tests, pass config files, and control the test execution setup. It achieves this via a yaml file (also called the testspec file) that you can modify by adding shell commands to it. This yaml file gets converted to a shell script which gets executed on the test host machine. You can save multiple yaml files and choose one dynamically as per your requirements when you schedule a run.

1. **Live video and logging**: Both standard and custom modes of execution provide you with videos and logs for your tests. However, in standard mode, you get the video and predefined logs of your tests only after your tests are completed. 

   By contrast, custom mode gives you a live stream of the video and client-side logs of your tests. In addition, you are able to download the video and other artifacts at the end of the test(s).

**Tip**  
If your use case involves at least one of the factors above, we strongly recommend switching to the custom mode of execution.

### Migration steps
<a name="migrating-to-custom"></a>

To migrate from standard to custom mode, do the following:

1. Sign in to the AWS Management Console and open the Device Farm console at [https://console.aws.amazon.com/devicefarm/](https://console.aws.amazon.com/devicefarm/).

1. Choose your project and then start a new automation run. 

1. Upload your app (or select `web app`), choose your test framework type, upload your test package, then under the `Choose your execution environment` parameter, choose the option to `Run your test in a custom environment`. 

1. By default, Device Farm's example test spec file will appear for you to view and edit. This example file can be used as a starting place to try your tests out in [custom environment mode](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html). Then, once you've verified that your tests are working properly from the console, you can then alter any of your API, CLI, and pipeline integrations with Device Farm to use this test spec file as a parameter when scheduling test runs. For information on how to add a test spec file as a parameter for your runs, see the `testSpecArn` parameter section for the `ScheduleRun` API in our [API guide](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRun.html). 

### Appium framework
<a name="custom-test-environment-migration-appium"></a>

In a custom test environnment, Device Farm does not insert or override any Appium capabilities in your Appium framework tests. You must specify your test's Appium capabilities in either the test spec YAML file or your test code.

### Android instrumentation
<a name="custom-test-environment-migration-instrumentation"></a>

You do not need to make changes to move your Android instrumentation tests to a custom test environment. 

### iOS XCUITest
<a name="custom-test-environment-migration-xcuitest"></a>

You do not need to make changes to move your iOS XCUITest tests to a custom test environment.

## Extending custom test environments in Device Farm
<a name="custom-test-environments-extending"></a>

AWS Device Farm enables configuring a custom environment for automated testing (custom mode), which is the recommended approach for all Device Farm users. The Device Farm custom mode enables you to run more than just your test suite. In this section, you learn how to extend your test suite and optimize your tests.

For more information about custom test environments in Device Farm, see [Custom test environments in AWS Device Farm](#custom-test-environments).

**Topics**
+ [Setting a device PIN when running tests in Device Farm](#custom-test-environments-extending-set-pin)
+ [Speeding up Appium-based tests in Device Farm through desired capabilities](#custom-test-environments-extending-speed)
+ [Using Webhooks and other APIs after your tests run in Device Farm](#custom-test-environments-extending-webhooks)
+ [Adding extra files to your test package in Device Farm](#custom-test-environments-extending-files)

### Setting a device PIN when running tests in Device Farm
<a name="custom-test-environments-extending-set-pin"></a>

 Some applications require that you set a PIN on the device. Device Farm does not support setting a PIN on devices natively. However, this is possible with the following caveats: 
+ The device must be running Android 8 or above.
+ The PIN must be removed after the test is complete.

 To set the PIN in your tests, use the `pre_test` and `post_test` phases to set and remove the PIN, as shown following: 

```
phases:
    pre_test:
      - # ... among your pre_test commands
      - DEVICE_PIN_CODE="1234"
      - adb shell locksettings set-pin "$DEVICE_PIN_CODE"
    post_test:
      - # ... Among your post_test commands
      - adb shell locksettings clear --old "$DEVICE_PIN_CODE"
```

 When your test suite begins, the PIN 1234 is set. After your test suite exits, the PIN is removed. 

**Warning**  
If you don't remove the PIN from the device after the test is complete, the device and your account will be quarantined.

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](#custom-test-environments-extending).

### Speeding up Appium-based tests in Device Farm through desired capabilities
<a name="custom-test-environments-extending-speed"></a>

When using Appium, you might find that the standard mode test suite is very slow. This is because Device Farm applies the default settings and doesn't make any assumptions about how you want to use the Appium environment. While these defaults are built around industry best practices, they might not apply to your situation. To fine-tune the parameters of the Appium server, you can adjust the default Appium capabilities in your test spec. For example, the following sets the `usePrebuildWDA` capability to `true` in an iOS test suite to speed up initial start time: 

```
phases:
  pre_test:
    - # ... Start up Appium
    - >-
    appium --log-timestamp
    --default-capabilities "{\"usePrebuiltWDA\": true, \"derivedDataPath\":\"$DEVICEFARM_WDA_DERIVED_DATA_PATH\",
    \"deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \"platformName\":\"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \"app\":\"$DEVICEFARM_APP_PATH\",
    \"automationName\":\"XCUITest\", \"udid\":\"$DEVICEFARM_DEVICE_UDID_FOR_APPIUM\", \"platformVersion\":\"$DEVICEFARM_DEVICE_OS_VERSION\"}"
    >> $DEVICEFARM_LOG_DIR/appiumlog.txt 2>&1 &
```

Appium capabilities must be a shell-escaped, quoted JSON structure. 

The following Appium capabilities are common sources of performance improvements:

`noReset` and `fullReset`  
These two capabilities, which are mutually exclusive, describe the behavior of Appium after each session is complete. When `noReset` is set to `true`, the Appium server doesn't remove data from your application when an Appium session ends, effectively doing no cleanup whatsoever. `fullReset` uninstalls and clears all application data from the device after the session has closed. For more information, see [Reset Strategies](http://appium.io/docs/en/writing-running-appium/other/reset-strategies/) in the Appium documentation.

`ignoreUnimportantViews` (Android only)  
Instructs Appium to compress the Android UI hierarchy only to *relevant* views for the test, speeding up certain element lookups. However, this can break some XPath-based test suites because the hierarchy of the UI layout has been changed.

`skipUnlock` (Android only)  
Informs Appium that there is no PIN code currently set, which speeds up tests after a screen off event or other lock event.

`webDriverAgentUrl` (iOS only)  
Instructs Appium to assume that an essential iOS dependency, `webDriverAgent`, is already running and available to accept HTTP requests at the specified URL. If `webDriverAgent` isn't already up and running, it can take Appium some time at the beginning of a test suite to start the `webDriverAgent`. If you start `webDriverAgent` yourself and set `webDriverAgentUrl` to `http://localhost:8100` when starting Appium, you can boot up your test suite faster. Note that this capability should never be used alongside the `useNewWDA` capability.  
You can use the following code to start `webDriverAgent` from your test spec file on the device's local port `8100`, then forward it to the test host's local port `8100` (this allows you to set `webDriverAgentUrl`'s value to `http://localhost:8100`). This code should be run during the install phase after any code for setting up the Appium and `webDriverAgent` environment variables has been defined:  

```
      # Start WebDriverAgent and iProxy
      - >-
        xcodebuild test-without-building -project /usr/local/avm/versions/$APPIUM_VERSION/node_modules/appium/node_modules/appium-webdriveragent/WebDriverAgent.xcodeproj
        -scheme WebDriverAgentRunner -derivedDataPath $DEVICEFARM_WDA_DERIVED_DATA_PATH
        -destination id=$DEVICEFARM_DEVICE_UDID_FOR_APPIUM IPHONEOS_DEPLOYMENT_TARGET=$DEVICEFARM_DEVICE_OS_VERSION
        GCC_TREAT_WARNINGS_AS_ERRORS=0 COMPILER_INDEX_STORE_ENABLE=NO >> $DEVICEFARM_LOG_DIR/webdriveragent_log.txt 2>&1 &
        
        iproxy 8100 8100 >> $DEVICEFARM_LOG_DIR/iproxy_log.txt 2>&1 &
```
Then, you can add the following code to your test spec file to ensure that `webDriverAgent` started successfully. This code should be run at the end of the pre-test phase after ensuring that Appium started successfully:  

```
      # Wait for WebDriverAgent to start
      - >-
        start_wda_timeout=0;
        while [ true ];
        do
          if [ $start_wda_timeout -gt 60 ];
          then
              echo "WebDriverAgent server never started in 60 seconds.";
              exit 1;
          fi;
          grep -i "ServerURLHere" $DEVICEFARM_LOG_DIR/webdriveragent_log.txt >> /dev/null 2>&1;
          if [ $? -eq 0 ];
          then
              echo "WebDriverAgent REST http interface listener started";
              break;
          else
              echo "Waiting for WebDriverAgent server to start. Sleeping for 1 seconds";
              sleep 1;
              start_wda_timeout=$((start_wda_timeout+1));
          fi;
        done;
```

For more information on the capabilities that Appium supports, see [Appium Desired Capabilities](http://appium.io/docs/en/writing-running-appium/caps/) in the Appium documentation. 

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](#custom-test-environments-extending).

### Using Webhooks and other APIs after your tests run in Device Farm
<a name="custom-test-environments-extending-webhooks"></a>

You can have Device Farm call a webhook after every test suite finishes using **curl**. The process to do this varies with the destination and formatting. For your specific webhook, see the documentation for that webhook. The following example posts a message each time a test suite has finished to a Slack webhook:

```
phases:
  post_test:
    - curl -X POST -H 'Content-type: application/json' --data '{"text":"Tests on '$DEVICEFARM_DEVICE_NAME' have finished!"}' {{https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX}}
```

For more information on using webhooks with Slack, see [Sending your first Slack message using Webhook](https://api.slack.com/tutorials/slack-apps-hello-world) in the Slack API reference.

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](#custom-test-environments-extending).

You are not limited to using **curl** to call webhooks. Test packages can include extra scripts and tools, as long as they are compatible with the Device Farm execution environment. For example, your test package may include auxiliary scripts that make requests to other APIs. Make sure that any required packages are installed alongside your test suite's requirements. To add a script that runs after your test suite is complete, include the script in your test package and add the following to your test spec:

```
phases:
  post_test:
    - {{python post_test.py}}
```

**Note**  
Maintaining any API keys or other authentication tokens used in your test package is your responsibility. We recommend that you keep any form of security credential out of source control, use credentials with the fewest possible privileges, and use revokable, short-lived tokens whenever possible. To verify security requirements, see the documentation for the third-party APIs that you use.

If you plan on using AWS services as a part of your test execution suite, you should use IAM temporary credentials, generated outside of your test suite and included in your test package. These credentials should have the fewest granted permissions and shortest lifespan possible. For more information on creating temporary credentials, see [Requesting temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the *IAM User Guide*.

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](#custom-test-environments-extending).

### Adding extra files to your test package in Device Farm
<a name="custom-test-environments-extending-files"></a>

You may want to use additional files as a part of your tests either as extra configuration files or additional test data. You can add these additional files to your test package before uploading it to AWS Device Farm, then access them from the custom environment mode. Fundamentally, all test package upload formats (ZIP, IPA, APK, JAR, etc.) are package archive formats that support standard ZIP operations.

You can add files to your test archive before uploading it to AWS Device Farm by using the following command:

```
$ zip zip-with-dependencies.zip extra_file
```

For a directory of extra files:

```
$ zip -r zip-with-dependencies.zip extra_files/
```

These commands work as expected for all test package upload formats except for IPA files. For IPA files, especially when used with XCUITests, we recommend that you put any extra files in a slightly different location due to how AWS Device Farm resigns iOS test packages. When building your iOS test, the test application directory will be located inside of another directory named {{Payload}}.

For example, this is how one such iOS test directory may look:

```
$ tree
.
└── Payload
    └── ADFiOSReferenceAppUITests-Runner.app
        ├── ADFiOSReferenceAppUITests-Runner
        ├── Frameworks
        │   ├── XCTAutomationSupport.framework
        │   │   ├── Info.plist
        │   │   ├── XCTAutomationSupport
        │   │   ├── _CodeSignature
        │   │   │   └── CodeResources
        │   │   └── version.plist
        │   └── XCTest.framework
        │       ├── Info.plist
        │       ├── XCTest
        │       ├── _CodeSignature
        │       │   └── CodeResources
        │       ├── en.lproj
        │       │   └── InfoPlist.strings
        │       └── version.plist
        ├── Info.plist
        ├── PkgInfo
        ├── PlugIns
        │   ├── ADFiOSReferenceAppUITests.xctest
        │   │   ├── ADFiOSReferenceAppUITests
        │   │   ├── Info.plist
        │   │   └── _CodeSignature
        │   │       └── CodeResources
        │   └── ADFiOSReferenceAppUITests.xctest.dSYM
        │       └── Contents
        │           ├── Info.plist
        │           └── Resources
        │               └── DWARF
        │                   └── ADFiOSReferenceAppUITests
        ├── _CodeSignature
        │   └── CodeResources
        └── embedded.mobileprovision
```

For these XCUITest packages, add any extra files to the directory ending in {{.app}} inside of the {{Payload}} directory. For example, the following commands show how you can add a file to this test package:

```
$ mv extra_file Payload/*.app/
$ zip -r my_xcui_tests.ipa Payload/
```

When you add a file to your test package, you can expect slightly different interaction behavior in AWS Device Farm based on its upload format. If the upload used the ZIP file extension, AWS Device Farm will automatically unzip the upload before your test and leave the unzipped files at the location with the {{$DEVICEFARM\_TEST\_PACKAGE\_PATH}} environment variable. (This means that if you added a file called {{extra\_file}} to the root of the archive as in the first example, it would be located at {{$DEVICEFARM\_TEST\_PACKAGE\_PATH/extra\_file}} during the test). 

To use a more practical example, if you’re an Appium TestNG user who wants to include a {{testng.xml}} file with your test, you can include it in your archive using the following command:

```
$ zip zip-with-dependencies.zip testng.xml
```

Then, you can change your test command in the custom environment mode to the following:

```
java -D appium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar -d $DEVICEFARM_LOG_DIR/test-output $DEVICEFARM_TEST_PACKAGE_PATH/testng.xml
```

If your test package upload extension isn't ZIP (e.g., APK, IPA, or JAR file), the uploaded package file itself is found at {{$DEVICEFARM\_TEST\_PACKAGE\_PATH}}. Because these are still archive format files, you can unzip the file in order to access the additional files from within. For example, the following command will unzip the contents of the test package (for APK, IPA, or JAR files) to the {{/tmp}} directory:

```
unzip $DEVICEFARM_TEST_PACKAGE_PATH -d /tmp
```

In the case of an APK or JAR file, you would find your extra files unzipped to the {{/tmp}} directory (e.g., {{/tmp/extra\_file}}). In the case of an IPA file, as explained before, extra files would be in a slightly different location inside the folder ending in {{.app}}, which is inside of the {{Payload}} directory. For example, based on the IPA example above, the file would be found at the location {{/tmp/Payload/ADFiOSReferenceAppUITests-Runner.app/extra\_file}} (referenceable as {{/tmp/Payload/\*.app/extra\_file}}).

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](#custom-test-environments-extending).

# Remote access in AWS Device Farm
<a name="remote-access"></a>

 Remote access, or manual testing, allows you to swipe, gesture, and interact with a device through your web browser in real time to test functionality and reproduce customer issues. You interact with a specific device by creating a remote access session with that device. The following key features are supported on Remote Access:
+ **App(s) upload:** Upload app files (.apk, .ipa) or test on web browsers.
+ **Appium Endpoint:** Connect to an Appium Endpoint right from your remote access session.
+ **Orientation change:** Change between Portrait and Landscape mode.
+ **Network shaping:** Select a pre-configured network profile or create your own.
+ **Location mocking:** Mock a location by providing the latitude and longitude.
+ **Screenshot:** Capture the screenshot of any screen.
+ **Video recording:** Capture the video of your entire test run.
+ **Logs:** Stream live log for Appium and get device, network, and activity logs at the end of your session.

A session in Device Farm is a real-time interaction with an actual, physical device hosted in a web browser. A session displays the single device you select when you start the session. A user can start more than one session at a time with the total number of simultaneous devices limited by the number of device slots you have. You can purchase device slots based on the device family (Android or iOS devices). For more information, see [Device Farm Pricing](https://aws.amazon.com/device-farm/pricing/). 

Device Farm currently offers a subset of devices for remote access testing. New devices are added to the device pool all the time.

Device Farm captures video of each remote access session and generates logs of activity during the session. These results include any information you provide during a session.

**Note**  
For security reasons, we recommend that you avoid providing or entering sensitive information, such as account numbers, personal login information, and other details during a remote access session. If possible, use alternatives developed specifically for testing, such as test accounts.

**Topics**
+ [Creating a remote access session in AWS Device Farm](#how-to-create-session)
+ [Using a remote access session in AWS Device Farm](#how-to-use-session)
+ [Retrieving the results of a remote access session in AWS Device Farm](#how-to-access-session-results)

## Creating a remote access session in AWS Device Farm
<a name="how-to-create-session"></a>

For information about remote access sessions, see [Sessions](#sessions).
+ [Prerequisites](#how-to-create-session-prerequisites)
+ [Create a remote session](#how-to-create-remote-session)
+ [Next steps](#how-to-create-session-next-steps)

### Prerequisites
<a name="how-to-create-session-prerequisites"></a>
+ Create a project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](#how-to-create-project), and then return to this page.

### Create a remote session
<a name="how-to-create-remote-session"></a>

------
#### [ Console ]

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. If you already have a project, choose it from the list. Otherwise, create a project by following the instructions in [Creating a project in AWS Device Farm](#how-to-create-project).

1. On the **Remote access** tab, choose **Create remote access session**.

1. Choose a device for your session. You can choose from the list of available devices or search for a device using the search bar at the top of the list.

1. In **Session name**, enter a name for the session.

1. *(Optional)* Under **Select applications**, include your own app or choose the Device Farm Sample App as part of the session. These can be newly uploaded apps, or apps previously uploaded in this project from the past 30 days (after 30 days, app uploads [will expire](#data-protection-retention)).

1. *(Optional)* Under **Advanced Configuration**, you can add a http/s **Device Proxy** which will get set for the duration of your session.

1. Choose **Confirm and start session**.

------
#### [ AWS CLI ]

*Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](#upload-example)*

First, verify that your AWS CLI version is up-to-date by [downloading and installing the latest version](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Important**  
Certain commands mentioned in this document aren't available in older versions of the AWS CLI.

Then, you can determine which device you'd like to test on:

```
$ aws devicefarm list-devices
```

This will show output such as the following:

```
{
    "devices":
    [
        {
            "arn": "arn:aws:devicefarm:us-west-2::device:DE5BD47FF3BD42C3A14BF7A6EFB1BFE7",
            "name": "Google Pixel 8",
            "remoteAccessEnabled": true,
            "availability": "HIGHLY_AVAILABLE"
            ...
        },
        ...
    ]
}
```

Then, you can create your remote access session with a device ARN of your choice:

```
$ aws devicefarm create-remote-access-session \
  --project-arn arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef \
  --device-arn arn:aws:devicefarm:us-west-2::device:DE5BD47FF3BD42C3A14BF7A6EFB1BFE7 \
  --app-arn arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef \
  --configuration '{
      "auxiliaryApps": [
          "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
          "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1"
      ]
  }'
```

This will show output such as the following:

```
{
    "remoteAccessSession": {
        "arn": "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000",
        "name": "Google Pixel 8",
        "status": "PENDING",
        ...
}
```

Now, optionally, we can poll and wait for the session to be ready:

```
$ POLL_INTERVAL=3
TIMEOUT=600
DEADLINE=$(( $(date +%s) + TIMEOUT ))

while [[ "$(date +%s)" -lt "$DEADLINE" ]]; do

  STATUS=$(aws devicefarm get-remote-access-session \
    --arn "$DEVICE_FARM_SESSION_ARN" \
    --query 'remoteAccessSession.status' \
    --output text)

  case "$STATUS" in
    RUNNING)
      echo "Session is ready with status: $STATUS"
      break
      ;;
    STOPPING|COMPLETED)
      echo "Session ended early with status: $STATUS"
      exit 1
      ;;
  esac

done
```

------
#### [ Python ]

*Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](#upload-example)*

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
import random
import time
import boto3

client = boto3.client("devicefarm", region_name="us-west-2")

# 1) Gather all matching devices via paginated ListDevices with filters
filters = [
    {"attribute": "MODEL",        "operator": "CONTAINS", "values": ["Pixel"]},
    {"attribute": "AVAILABILITY", "operator": "EQUALS",   "values": ["AVAILABLE"]},
]

matching_arns = []
next_token = None
while True:
    args = {"filters": filters}
    if next_token:
        args["nextToken"] = next_token
    page = client.list_devices(**args)
    for d in page.get("devices", []):
        matching_arns.append(d["arn"])
    next_token = page.get("nextToken")
    if not next_token:
        break

if not matching_arns:
    raise RuntimeError("No available Google Pixel device found.")

# Randomly select one device from the full matching set
device_arn = random.choice(matching_arns)
print("Selected device ARN:", device_arn)

# 2) Create remote access session and wait until RUNNING
resp = client.create_remote_access_session(
    projectArn="arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
    deviceArn=device_arn,
    appArn="arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef",  # optional
    configuration={
        "auxiliaryApps": [  # optional
            "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
            "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1",
        ]
    },
)

session_arn = resp["remoteAccessSession"]["arn"]
print(f"Created Remote Access Session: {session_arn}")

poll_interval = 3
timeout = 600
deadline = time.time() + timeout
terminal_states = ["STOPPING", "COMPLETED"]

while True:
    out = client.get_remote_access_session(arn=session_arn)
    status = out["remoteAccessSession"]["status"]
    print(f"Current status: {status}")

    if status == "RUNNING":
        print(f"Session is ready with status: {status}")
        break
    if status in terminal_states:
        raise RuntimeError(f"Session ended early with status: {status}")
    if time.time() >= deadline:
        raise RuntimeError("Timed out waiting for session to be ready.")
    time.sleep(poll_interval)
```

------
#### [ Java ]

*Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](#upload-example)*

*Note: this example uses the AWS SDK for Java v2, and is compatible with JDK versions 11 and higher.*

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionConfiguration;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionResponse;
import software.amazon.awssdk.services.devicefarm.model.Device;
import software.amazon.awssdk.services.devicefarm.model.DeviceFilter;
import software.amazon.awssdk.services.devicefarm.model.DeviceFilterAttribute;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionResponse;
import software.amazon.awssdk.services.devicefarm.model.ListDevicesRequest;
import software.amazon.awssdk.services.devicefarm.model.ListDevicesResponse;
import software.amazon.awssdk.services.devicefarm.model.RuleOperator;

public class CreateRemoteAccessSession {
  public static void main(String[] args) throws Exception {
    DeviceFarmClient client = DeviceFarmClient.builder()
        .region(Region.US_WEST_2)
        .build();

    String projectArn = "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef";
    String appArn     = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef";
    String aux1       = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0";
    String aux2       = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1";

    // 1) Gather all matching devices via paginated ListDevices with filters
    List<DeviceFilter> filters = Arrays.asList(
        DeviceFilter.builder()
            .attribute(DeviceFilterAttribute.MODEL)
            .operator(RuleOperator.CONTAINS)
            .values("Pixel")
            .build(),
        DeviceFilter.builder()
            .attribute(DeviceFilterAttribute.AVAILABILITY)
            .operator(RuleOperator.EQUALS)
            .values("AVAILABLE")
            .build()
    );

    List<String> matchingDeviceArns = new ArrayList<>();
    String next = null;
    do {
      ListDevicesResponse page = client.listDevices(
          ListDevicesRequest.builder().filters(filters).nextToken(next).build());
      for (Device d : page.devices()) {
        matchingDeviceArns.add(d.arn());
      }
      next = page.nextToken();
    } while (next != null);

    if (matchingDeviceArns.isEmpty()) {
      throw new RuntimeException("No available Google Pixel device found.");
    }

    // Randomly select one device from the full matching set
    String deviceArn = matchingDeviceArns.get(
        ThreadLocalRandom.current().nextInt(matchingDeviceArns.size()));
    System.out.println("Selected device ARN: " + deviceArn);

    // 2) Create Remote Access session and wait until it is RUNNING
    CreateRemoteAccessSessionConfiguration cfg = CreateRemoteAccessSessionConfiguration.builder()
        .auxiliaryApps(Arrays.asList(aux1, aux2))
        .build();

    CreateRemoteAccessSessionResponse res = client.createRemoteAccessSession(
        CreateRemoteAccessSessionRequest.builder()
            .projectArn(projectArn)
            .deviceArn(deviceArn)
            .appArn(appArn)       // optional
            .configuration(cfg)   // optional
            .build());

    String sessionArn = res.remoteAccessSession().arn();
    System.out.println("Created Remote Access Session: " + sessionArn);

    int pollIntervalMs = 3000;
    long timeoutMs = 600_000L;
    long deadline = System.currentTimeMillis() + timeoutMs;

    while (true) {
      GetRemoteAccessSessionResponse get = client.getRemoteAccessSession(
          GetRemoteAccessSessionRequest.builder().arn(sessionArn).build());
      String status = get.remoteAccessSession().statusAsString();
      System.out.println("Current status: " + status);

      if ("RUNNING".equals(status)) {
        System.out.println("Session is ready with status: " + status);
        break;
      }
      if ("STOPPING".equals(status) || "COMPLETED".equals(status)) {
        throw new RuntimeException("Session ended early with status: " + status);
      }
      if (System.currentTimeMillis() >= deadline) {
        throw new RuntimeException("Timed out waiting for session to be ready.");
      }
      Thread.sleep(pollIntervalMs);
    }
  }
}
```

------
#### [ JavaScript ]

*Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](#upload-example)*

*Note: this example uses AWS SDK for JavaScript v3.*

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
import {
  DeviceFarmClient,
  ListDevicesCommand,
  CreateRemoteAccessSessionCommand,
  GetRemoteAccessSessionCommand,
} from "@aws-sdk/client-device-farm";

const client = new DeviceFarmClient({ region: "us-west-2" });

// 1) Gather all matching devices via paginated ListDevices with filters
const filters = [
  { attribute: "MODEL",        operator: "CONTAINS", values: ["Pixel"] },
  { attribute: "AVAILABILITY", operator: "EQUALS",   values: ["AVAILABLE"] },
];

let nextToken;
const matching = [];

while (true) {
  const page = await client.send(new ListDevicesCommand({ filters, nextToken }));
  for (const d of page.devices ?? []) {
    matching.push(d.arn);
  }
  nextToken = page.nextToken;
  if (!nextToken) break;
}

if (matching.length === 0) {
  throw new Error("No available Google Pixel device found.");
}

// Randomly select one device from the full matching set
const deviceArn = matching[Math.floor(Math.random() * matching.length)];
console.log("Selected device ARN:", deviceArn);

// 2) Create remote access session and wait until RUNNING
const out = await client.send(new CreateRemoteAccessSessionCommand({
  projectArn: "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
  deviceArn,
  appArn: "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef", // optional
  configuration: {
    auxiliaryApps: [ // optional
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1",
    ],
  },
}));

const sessionArn = out.remoteAccessSession?.arn;
console.log("Created Remote Access Session:", sessionArn);

const pollIntervalMs = 3000;
const timeoutMs = 600000;
const deadline = Date.now() + timeoutMs;

while (true) {
  const get = await client.send(new GetRemoteAccessSessionCommand({ arn: sessionArn }));
  const status = get.remoteAccessSession?.status;
  console.log("Current status:", status);

  if (status === "RUNNING") {
    console.log("Session is ready with status:", status);
    break;
  }
  if (status === "STOPPING" || status === "COMPLETED") {
    throw new Error(`Session ended early with status: ${status}`);
  }
  if (Date.now() >= deadline) {
    throw new Error("Timed out waiting for session to be ready.");
  }
  await new Promise((r) => setTimeout(r, pollIntervalMs));
}
```

------
#### [ C\# ]

*Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](#upload-example)*

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Amazon;
using Amazon.DeviceFarm;
using Amazon.DeviceFarm.Model;

class Program
{
    static async Task Main()
    {
        var client = new AmazonDeviceFarmClient(RegionEndpoint.USWest2);

        // 1) Gather all matching devices via paginated ListDevices with filters
        var filters = new List<DeviceFilter>
        {
            new DeviceFilter { Attribute = DeviceAttribute.MODEL,        Operator = RuleOperator.CONTAINS, Values = new List<string>{ "Pixel" } },
            new DeviceFilter { Attribute = DeviceAttribute.AVAILABILITY, Operator = RuleOperator.EQUALS,   Values = new List<string>{ "AVAILABLE" } },
        };

        var matchingArns = new List<string>();
        string nextToken = null;

        do
        {
            var list = await client.ListDevicesAsync(new ListDevicesRequest
            {
                Filters = filters,
                NextToken = nextToken
            });

            foreach (var d in list.Devices)
                matchingArns.Add(d.Arn);

            nextToken = list.NextToken;
        }
        while (nextToken != null);

        if (matchingArns.Count == 0)
            throw new Exception("No available Google Pixel device found.");

        // Randomly select one device from the full matching set
        var rnd = new Random();
        var deviceArn = matchingArns[rnd.Next(matchingArns.Count)];
        Console.WriteLine($"Selected device ARN: {deviceArn}");

        // 2) Create remote access session and wait until RUNNING
        var request = new CreateRemoteAccessSessionRequest
        {
            ProjectArn = "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
            DeviceArn  = deviceArn,
            AppArn     = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef", // optional
            Configuration = new CreateRemoteAccessSessionConfiguration
            {
                AuxiliaryApps = new List<string>
                {
                    "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
                    "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1"
                }
            }
        };

        request.Configuration.AuxiliaryApps.RemoveAll(string.IsNullOrWhiteSpace);

        var response = await client.CreateRemoteAccessSessionAsync(request);
        var sessionArn = response.RemoteAccessSession.Arn;
        Console.WriteLine($"Created Remote Access Session: {sessionArn}");

        var pollIntervalMs = 3000;
        var timeoutMs = 600000;
        var deadline = DateTime.UtcNow.AddMilliseconds(timeoutMs);

        while (true)
        {
            var get = await client.GetRemoteAccessSessionAsync(new GetRemoteAccessSessionRequest { Arn = sessionArn });
            var status = get.RemoteAccessSession.Status.Value;
            Console.WriteLine($"Current status: {status}");

            if (status == "RUNNING")
            {
                Console.WriteLine($"Session is ready with status: {status}");
                break;
            }
            if (status == "STOPPING" || status == "COMPLETED")
            {
                throw new Exception($"Session ended early with status: {status}");
            }
            if (DateTime.UtcNow >= deadline)
            {
                throw new TimeoutException("Timed out waiting for session to be ready.");
            }

            await Task.Delay(pollIntervalMs);
        }
    }
}
```

------
#### [ Ruby ]

*Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](#upload-example)*

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
require 'aws-sdk-devicefarm'

client = Aws::DeviceFarm::Client.new(region: 'us-west-2')

# 1) Gather all matching devices via paginated ListDevices with filters
filters = [
  { attribute: 'MODEL',        operator: 'CONTAINS', values: ['Pixel'] },
  { attribute: 'AVAILABILITY', operator: 'EQUALS',   values: ['AVAILABLE'] },
]

matching_arns = []
next_token = nil
loop do
  resp = client.list_devices(filters: filters, next_token: next_token)
  resp.devices&.each { |d| matching_arns << d.arn }
  next_token = resp.next_token
  break unless next_token
end

abort "No available Google Pixel device found." if matching_arns.empty?

# Randomly select one device from the full matching set
device_arn = matching_arns.sample
puts "Selected device ARN: #{device_arn}"

# 2) Create remote access session and wait until RUNNING
resp = client.create_remote_access_session(
  project_arn: "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
  device_arn:  device_arn,
  app_arn:     "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef", # optional
  configuration: {
    auxiliary_apps: [ # optional
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1"
    ].compact
  }
)

session_arn = resp.remote_access_session.arn
puts "Created Remote Access Session: #{session_arn}"

poll_interval = 3
timeout = 600
deadline = Time.now + timeout
terminal = %w[STOPPING COMPLETED]

loop do
  get = client.get_remote_access_session(arn: session_arn)
  status = get.remote_access_session.status
  puts "Current status: #{status}"

  if status == 'RUNNING'
    puts "Session is ready with status: #{status}"
    break
  end

  abort "Session ended early with status: #{status}" if terminal.include?(status)
  abort "Timed out waiting for session to be ready." if Time.now >= deadline
  sleep poll_interval
end
```

------

### Next steps
<a name="how-to-create-session-next-steps"></a>

Device Farm starts the session as soon as the requested device and infrastructure are available, typically within a few minutes. The **Device Requested** dialog box appears until the session starts. To cancel the session request, choose **Cancel request**. 

If the selected device is unavailable or busy, the session status shows as **Pending Device**, indicating that you may need to wait for some time before the device is available for testing.

If your account has reached its concurrency limit for public metered or unmetered devices, the session status shows as **Pending concurrency**. For unmetered device slots, you can increase concurrency by [purchasing more device slots](#how-to-purchase-device-slots). For metered pay-as-you-go devices, please contact AWS via a support ticket to request [a service quota increase](#limits).

When the session setup begins, it first shows a status of **In-Progress**, then a status of **Connecting** while your local web browser attempts to open a remote connection to the device.

After a session starts, if you should close the browser or browser tab without stopping the session or if the connection between the browser and the internet is lost, the session remains active for five minutes. After that, Device Farm ends the session. Your account is charged for the idle time. 

After the session starts, you can interact with the device in the web browser, or test the device using [Appium](#appium-endpoint).

## Using a remote access session in AWS Device Farm
<a name="how-to-use-session"></a>

For information about performing interactive testing of Android and iOS apps through remote access sessions, see [Sessions](#sessions).
+ [Prerequisites](#how-to-use-session-prerequisites)
+ [Use a session in the Device Farm console](#how-to-use-session-console)
+ [Next steps](#how-to-use-session-next-steps)
+ [Tips and tricks](#how-to-use-session-tips)

### Prerequisites
<a name="how-to-use-session-prerequisites"></a>
+ Create a session. Follow the instructions in [Creating a session](#how-to-create-session), and then return to this page.

### Use a session in the Device Farm console
<a name="how-to-use-session-console"></a>

As soon as the device that you requested for a remote access session becomes available, the console displays the device screen. The session has a maximum length of 150 minutes. The time remaining in the session appears in the **Time left** field in the top-right corner above the device.

### Actions
<a name="how-to-use-actions"></a>

All actions you can take with the device and your session reside in the menu on the left-hand side of the device. The available actions are explained in detail below. 

![The remote access session page](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/actions_menu.png)


### Navigating the device
<a name="how-to-navigate-the-device"></a>

You can interact with the device displayed in the console as you would with a real physical device, by using your mouse or a pointer device like touchpad for touch and your local keyboard. The swipe action works based on starting and ending coordinates of your click. This means a three or more point swipe does not work. On an Android device, you have the **Home**, **Back**, and **Switch apps** buttons. On an iOS device, you have the **Home** button. These buttons on both function just as real device controls. 

![Navigating the device](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/navigating_device.png)


### Taking a screenshot
<a name="how-to-use-screenshot"></a>

A common pattern while doing manual testing is to take a device screenshot. You can do this by using the **Screenshot** button in the left menu bar. On clicking this button, a screenshot of the current device screen is downloaded in your browser's download folder as a .jpeg extension. The button greys out when the screenshot is being processed and downloaded.

### Switching between portrait and landscape mode
<a name="how-to-use-session-switch-between-portrait-landscape-mode"></a>

You can switch between portrait (vertical) and landscape (horizontal) view on the device using the **Rotate** option. The orientation of the device display only changes if the active view on the device supports it. For example, the home page on a smaller iPhone does not support orientation change. Thus, you will not see the orientation change when using **Rotate**. 

![Change orientation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/change_orientation_remote_access.gif)


### Changing network
<a name="how-to-use-network-shaping"></a>

You can change the network behavior by changing parameters such as upload/download speeds, bandwidth, packet loss for the device under test. Click the **Network** button in the left side menu. This opens up a right hand side overlay where you can choose from a list of curated network settings or create your own network profile.

![Change network](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/network_settings.gif)


### Mocking location
<a name="how-to-use-location-mocking"></a>

You can mock a location on the device by providing the latitude and longitude of your desired location. This does not physically get a device in that region but when an app queries the OS for its location, the device returns the location you entered. If your app uses multiple data points such as Wi-Fi, cellular signal, and other methods rather than just querying the OS for location then this feature will most likely not work for your app. Click the **Set location** button in the left-side menu. This opens up a right hand side overlay where you can input the latitude and longitude of your desired location. 

![Mock location](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/mock_location.gif)


### Installing an application
<a name="how-to-use-session-install-app"></a>

You can install apps in a remote access session in two ways: 1) During session launch, you can upload an app or specify a recently used app. 2) After the remote access session has started, you can manually upload/install the app using the **Install app** option in the left side menu, and then choose the .apk file (Android) or the .ipa file (iOS) that you want to install. Applications that you run in a remote access session don't require any test instrumentation or provisioning.

**Note**  
When you upload an app, the service first uploads the app to a secure Amazon S3 bucket and then installs it which takes a few seconds depending on the size of the app. A confirmation message will appear to let you know if the app was successfully installed or not.

![Install app in remote access session](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/install_app_remote_access.gif)


### Installing a recently uploaded application
<a name="how-to-use-recent-apps"></a>

To install an application recently uploaded, select **Recent apps** in the left side menu, and then choose the .apk file (Android) or the .ipa file (iOS) that you want to install from the dropdown selection.

**Note**  
When you select a recent app, the service first downloads the previously uploaded app from a secure service managed S3 bucket to the host machine running your session and then installs it which takes a few seconds depending on the size of the app. A confirmation message will appear to let you know if the app was successfully installed or not.

![Install recent apps in remote access](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/install_recent_apps_remote_access.gif)


### View device details
<a name="how-to-get-device-info"></a>

You can view device details such as the ARN, Model ID, CPU, Resolution, Memory, and Heap Size of the device being used in your session by clicking on the **Device details** button. This action displays the device details in a new tab. For a public device, the details do not include UDID as that can change across every session. For private devices, the device details page displays the Instance and Device ARN along with UDID and Labels assigned to the private device instance. 

![Public device details page](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/public_device_details.gif)


### Appium Session
<a name="how-to-get-appium-session-info"></a>

You can get the Appium Session details attached to your remote access session by clicking on the **Appium Session** button.

![Set up Appium session](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/appium_session_remote_access.gif)


### Session ARN
<a name="how-to-get-session-arn"></a>

You can copy the session ARN of your remote access session using the **Session ARN** button.

### Appium URL
<a name="how-to-get-appium-url"></a>

You can copy the Appium URL for your remote access session using the **Appium URL** button.

### Minimize left side menu
<a name="how-to-minimize-actions-menu"></a>

You can get a minimized icons-only version of all the actions in the left-hand side menu of remote access session using the **Minimize** button.

![Minimize actions menu](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/minimize_actions_menu.gif)


### Next steps
<a name="how-to-use-session-next-steps"></a>

Device Farm continues the session until you stop it manually or the 150-minute time limit is reached. To end the session, choose **Stop Session**. After the session stops, you can access the video that was captured and the logs that were generated. For more information, see [Retrieving session results](#how-to-access-session-results).

### Tips and tricks
<a name="how-to-use-session-tips"></a>

You might experience performance issues with the remote access session if you are located in a region geographically distant from us-west-2. This is due, in part, to latency in some Regions. If you experience performance issues, give the remote access session a chance to catch up before you interact with the app again.

## Retrieving the results of a remote access session in AWS Device Farm
<a name="how-to-access-session-results"></a>

For information about sessions, see [Sessions](#sessions).
+ [Prerequisites](#how-to-access-session-results-prerequisites)
+ [Viewing session details](#how-to-view-session-details)
+ [Downloading session video or logs](#how-to-access-session-files)

### Prerequisites
<a name="how-to-access-session-results-prerequisites"></a>
+ Complete a session. Follow the instructions in [Using a remote access session in AWS Device Farm](#how-to-use-session), and then return to this page.

### Viewing session details
<a name="how-to-view-session-details"></a>

When a remote access session ends, the Device Farm console displays a table that contains details about activity during the session. For more information, see [Analyzing Log Information](#how-to-use-reports-console-log).

To return to the details of a session at a later time:

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose the project containing the session.

1. Choose **Remote access**, and then choose the session you want to review from the list.

### Downloading session video or logs
<a name="how-to-access-session-files"></a>

When a remote access session ends, the Device Farm console provides access to a video capture of the session and activity logs. In the session results, choose the **Files** tab for a list of links to the session video and logs. You can view these files in the browser or save them locally.

# Appium testing in AWS Device Farm
<a name="appium-endpoint"></a>

During a remote access session, you can run Appium tests from your local environment, targeting the session's device using a managed Appium endpoint. With an Appium endpoint, you're able to develop, test, and execute Appium code with fast feedback and rapid iteration. This **client-side** approach to testing offers the flexibility to connect to a Device Farm device from any Appium client environment of your choice.

To complement client-side testing, Device Farm also supports running tests on infrastructure managed by the service, called **server-side** execution. In this approach, you can upload your app and tests to the service, then executes the tests in parallel on multiple devices using service-managed [test hosts](#custom-test-environments-hosts). This approach scales well for testing on many devices independently, as well as testing from the context of a CI/CD pipeline.

To learn more about server-side execution, please see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

**Topics**
+ [What is an Appium endpoint?](#appium-endpoint-what-is)
+ [Getting started with Appium testing](#appium-endpoint-getting-started)
+ [Interacting with the device using Appium](#appium-endpoint-interaction)
+ [Reviewing your Appium server logs](#appium-endpoint-server-logs)
+ [Supported features and versions](#appium-endpoint-support)

## What is an Appium endpoint?
<a name="appium-endpoint-what-is"></a>

[Appium](https://appium.io/) is a popular open-source software testing framework for testing native, hybrid, and mobile web applications on different devices, including mobile phones and tablets, for both iOS and Android. It allows developers and QA (Quality Assurance) engineers to write scripts that can remotely control a device, simulate user interactions, and verify that the application under test is behaving as expected. Appium interacts with apps from the perspective of an end-user, enabling testers to develop tests that simulate how real users will use the app for their tests.

Appium is built on the client-server model, where a local client requests a (local or remote) Appium server to command a device on their behalf. The Appium server manages a driver for communicating with the device, such as the [UIAutomator2 driver](https://github.com/appium/appium-uiautomator2-driver/) for Android or the [XCUITest driver](https://appium.github.io/appium-xcuitest-driver/9.10/) for iOS. All commands follow the [W3C WebDriver](https://www.w3.org/TR/webdriver2/) standards for how to control a device.

Device Farm's Appium endpoint exposes an Appium server URL for the device in your remote access session. The Appium endpoint URL will be specific to that device in that session, and remain valid for the duration of the session, allowing you to iterate on the same device without additional setup time. For more information about Remote Access, please see [Remote access in AWS Device Farm](#remote-access).

## Getting started with Appium testing
<a name="appium-endpoint-getting-started"></a>

For most Appium users, using Device Farm for Appium testing requires only minor changes to your existing test configuration.

At a high level, there are three steps to using Device Farm for client-side Appium tests:

1. First, you need to [create a remote access session](#how-to-create-session) for testing a Device Farm device. You can include your apps as a part of your remote access request, or install apps after the session has started.

1. Once the session is running, you can [copy the Appium endpoint URL](#appium-endpoint-interaction), and use it either through a stand-alone tool (like [Appium Inspector](https://github.com/appium/appium-inspector)) or from your Appium test code in your IDE. The URL will be valid for the duration of the remote access session.

1. And finally, once your Appium test has started, you can [review your Appium server logs](#appium-endpoint-server-logs) live during the test execution alongside the video stream of your device.

## Interacting with the device using Appium
<a name="appium-endpoint-interaction"></a>

After you [create a remote access session](#how-to-create-session), the device will be available for Appium testing. For the duration of the remote access session, you can run as many Appium sessions as you want on the device, with no limits on what clients you use. For example, you can start by running a test using your local Appium code from your IDE, then switch to using Appium Inspector to troubleshoot any issues you encounter. The session can last up to [150 minutes](#service-limits). However, if there is no activity for more than 5 minutes (through either the interactive console or the Appium endpoint), the session times out.

### Using apps for testing with your Appium session
<a name="appium-endpoint-using-apps"></a>

There are several ways to provide an app for use with your Appium session:
+ Upload an app to Device Farm and install it in the session.
+ Specify an HTTPS URL or an Amazon Simple Storage Service (Amazon S3) URI as the `appium:app` capability.
+ Reference an already-installed app by its package name (using `appium:appPackage` on Android or `appium:bundleId` on iOS).
+ Test a web app by specifying the `browserName` capability (`Chrome` on Android, `Safari` on iOS).

Standard [app size limits](#file-limits) (4 GB) apply to all app sources.

**Note**  
Device Farm does not support passing a local filesystem path in `appium:app` during a remote access session.

#### Uploading, installing, and using apps
<a name="appium-endpoint-app-uploaded"></a>

To use an uploaded app with your Appium session, follow these steps:

1. 

**Upload and install your app**

   There are two ways to upload and install an app onto the device under test:
   + Include the app ARN in your [`CreateRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateRemoteAccessSession.html) request. The app is automatically installed onto the device when the session starts. You can also include auxiliary app ARNs, which will be installed alongside the primary app.
   + Install the app during an active session using the [`InstallToRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_InstallToRemoteAccessSession.html) API, or by uploading it through the Device Farm console. This allows you to change the app under test without creating a new session.

1. 

**Use the installed app**

   Once installed, the app is automatically injected as the default `appium:app` capability for any subsequent Appium sessions. If you included auxiliary apps, they are set as the `appium:otherApps` capability.

   For example, if you create a remote access session using `com.aws.devicefarm.sample` as your app, and `com.aws.devicefarm.other.sample` as one of your auxiliary apps, then when you go to create an Appium session, it will have capabilities similar to the following:

   ```
   {
       "value":
       {
           "sessionId": "abcdef123456-1234-5678-abcd-abcdef123456",
           "capabilities":
           {
               "app": "/tmp/com.aws.devicefarm.sample.apk",
               "otherApps": "[\"/tmp/com.aws.devicefarm.other.sample.apk\"]",
               ...
           }
       }
   }
   ```

   If you install a new app during the session, it replaces the current `appium:app` capability. If the previously installed app has a distinct package name, it remains on the device and moves to the `appium:otherApps` capability.

   For example, if you initially use `com.aws.devicefarm.sample` when creating your remote access session, but then install `com.aws.devicefarm.other.sample` during the session, your Appium sessions will have capabilities similar to the following:

   ```
   {
       "value":
       {
           "sessionId": "abcdef123456-1234-5678-abcd-abcdef123456",
           "capabilities":
           {
               "app": "/tmp/com.aws.devicefarm.other.sample.apk",
               "otherApps": "[\"/tmp/com.aws.devicefarm.sample.apk\"]",
               ...
           }
       }
   }
   ```

**Note**  
For more information about automatically uploading apps as part of your remote access session, see [Automating Device Farm](#api-ref).

#### Using an HTTPS URL
<a name="appium-endpoint-app-https-url"></a>

You can specify a publicly accessible HTTPS URL as the `appium:app` desired capability when creating an Appium session. The URL must point directly to a downloadable app file (for example, an `.apk` or `.ipa` file). Device Farm downloads the app from the specified URL and installs it onto the device under test.

**Important**  
Only HTTPS URLs are supported. Plain HTTP URLs are rejected.

For example, the following Appium session creation request downloads an app from an HTTPS URL:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:app": "https://example.com/path/to/MyApp.apk"
            }
        ]
    }
}
```

#### Using an Amazon S3 URI
<a name="appium-endpoint-app-s3-uri"></a>

You can specify an Amazon S3 URI (for example, `s3://amzn-s3-demo-bucket/path/to/MyApp.ipa`) as the `appium:app` desired capability when creating an Appium session. Device Farm downloads the app from the specified Amazon S3 location and installs it onto the device under test.

To use an Amazon S3 URI, the following requirements must be met:
+ The remote access session must be started from a project that has an [IAM execution role](#custom-test-environments-iam-roles) configured.
+ The IAM execution role must have a maximum session duration of at least 150 minutes. This is the case because the role is assumed for the duration of the remote access session.
+ The IAM execution role must have permission to call `s3:GetObject` on the S3 object specified in the URI. This permission also authorizes the `HeadObject` API call on the same object, which allows Device Farm to validate the object's existence before attempting the download.

For example, the following Appium session creation request downloads an app from an Amazon S3 URI:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:app": "s3://amzn-s3-demo-bucket/apps/MyApp.ipa"
            }
        ]
    }
}
```

The following is an example of an IAM permissions policy that grants the recommended access for downloading an app from Amazon S3. The `s3:GetObject` permission also authorizes the `HeadObject` API call, which is used to validate the object's existence. For more information about configuring IAM execution roles, see [Access AWS resources using an IAM Execution Role](#custom-test-environments-iam-roles).

**Example**  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/apps/*"
    }
  ]
}
```

#### Using an already-installed app
<a name="appium-endpoint-app-package-name"></a>

If the app you want to test is already installed on the device, you can reference it directly by its package name instead of uploading it. Use the `appium:appPackage` and `appium:appActivity` capabilities on Android, or the `appium:bundleId` capability on iOS.

For example, the following Appium session creation request launches an Android app that's already installed:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:appPackage": "com.example.myapp",
                "appium:appActivity": "com.example.myapp.MainActivity"
            }
        ]
    }
}
```

On iOS, use `appium:bundleId` instead:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:bundleId": "com.example.myapp"
            }
        ]
    }
}
```

#### Testing a web app
<a name="appium-endpoint-app-web"></a>

To test a web app, specify the `browserName` capability in your Appium session creation request. Use `Chrome` on Android devices or `Safari` on iOS devices.

For example, the following request opens Chrome on an Android device:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "browserName": "Chrome"
            }
        ]
    }
}
```

### How to use the Appium endpoint
<a name="appium-endpoint-how-to-use"></a>

Here are the steps to access the session's Appium endpoint from the console, the AWS CLI, and the AWS SDKs. These steps include how to get started with running tests by using various Appium client testing frameworks:

------
#### [ Console ]

1. Open your remote access session page in your web browser:  
![The remote access session page](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-appium-endpoint.png)

1. For running a session by using Appium Inspector, do the following:

   1. Choose **Setup Appium session**.

   1. Follow the instructions on the page to start a session by using Appium Inspector.

1. For running an Appium test from your local IDE, do the following:

   1. Choose the copy icon next to **Appium endpoint URL**.

   1. Paste the copied URL into your local Appium code wherever you currently specify your remote address or command executor. For language-specific examples, refer to other tabs in this section.

------
#### [ AWS CLI ]

First, verify that your AWS CLI version is up-to-date by [downloading and installing the latest version](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Important**  
The Appium endpoint field isn't available in older versions of the AWS CLI.

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRemoteAccessSession.html) API:

```
$ aws devicefarm get-remote-access-session \
    --arn "arn:aws:devicefarm:us-west-2:123456789876:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000"
```

This will show output such as the following:

```
{
    "remoteAccessSession": {
        "arn": "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000",
        "name": "Google Pixel 8",
        "status": "RUNNING",
        "endpoints": {
            "remoteDriverEndpoint": "https://devicefarm-interactive-global.us-west-2.api.aws/remote-endpoint/ABCD1234...",
        ...
}
```

You can use this URL in your local Appium code wherever you currently specify your remote address or command executor. For language-specific examples, please click one of the tabs in this example window for your language of choice.

For an example of how to interact with the endpoint directly from the command line, you can use the [command-line tool curl](https://curl.se/) to call a WebDriver endpoint directly:

```
$ curl "https://devicefarm-interactive-global.us-west-2.api.aws/remote-endpoint/ABCD1234.../status"
```

This will show output such as the following:

```
{
    "value":
    {
        "ready": true,
        "message": "The server is ready to accept new connections",
        "build":
        {
            "version": "2.5.1"
        }
    }
}
```

------
#### [ Python ]

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRemoteAccessSession.html) API:

```
# To get the URL
import sys
import boto3
from botocore.exceptions import ClientError

def get_appium_endpoint() -> str:
    session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000"
    device_farm_client = boto3.client("devicefarm", region_name="us-west-2")

    try:
        resp = device_farm_client.get_remote_access_session(arn=session_arn)
    except ClientError as exc:
        sys.exit(f"Failed to call Device Farm: {exc}")

    remote_access_session = resp.get("remoteAccessSession", {})
    endpoints = remote_access_session.get("endpoints", {})
    endpoint = endpoints.get("remoteDriverEndpoint")

    if not endpoint:
        sys.exit("Device Farm response did not include endpoints.remoteDriverEndpoint")

    return endpoint

# To use the URL
from appium import webdriver
from appium.options.android import UiAutomator2Options

opts = UiAutomator2Options()
driver = webdriver.Remote(get_appium_endpoint(), options=opts)
# ...
driver.quit()
```

------
#### [ Java ]

*Note: this example uses the AWS SDK for Java v2, and is compatible with JDK versions 11 and higher.*

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRemoteAccessSession.html) API:

```
// To get the URL
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionResponse;

public class AppiumEndpointBuilder {
    public static String getAppiumEndpoint() throws Exception {
        String session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000";

        try (DeviceFarmClient client = DeviceFarmClient.builder()
                .region(Region.US_WEST_2)
                .credentialsProvider(DefaultCredentialsProvider.create())
                .build()) {

            GetRemoteAccessSessionResponse resp = client.getRemoteAccessSession(
                    GetRemoteAccessSessionRequest.builder().arn(session_arn).build()
            );

            String endpoint = resp.remoteAccessSession().endpoints().remoteDriverEndpoint();
            if (endpoint == null || endpoint.isEmpty()) {
                throw new IllegalStateException("remoteDriverEndpoint missing from response");
            }
            return endpoint;
        }
    }
}

// To use the URL
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;

import java.net.URL;

public class ExampleTest {
    public static void main(String[] args) throws Exception {
        String endpoint = AppiumEndpointBuilder.getAppiumEndpoint();
        UiAutomator2Options options = new UiAutomator2Options();
        AndroidDriver driver = new AndroidDriver(new URL(endpoint), options);

        try {
            // ... your test ...
        } finally {
            driver.quit();
        }
    }
}
```

------
#### [ JavaScript ]

*Note: this example uses AWS SDK for JavaScript v3 and WebdriverIO v8\+ using Node 18\+.*

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRemoteAccessSession.html) API:

```
// To get the URL
import { DeviceFarmClient, GetRemoteAccessSessionCommand } from "@aws-sdk/client-device-farm";

export async function getAppiumEndpoint() {
  const sessionArn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000";

  const client = new DeviceFarmClient({ region: "us-west-2" });
  const resp = await client.send(new GetRemoteAccessSessionCommand({ arn: sessionArn }));

  const endpoint = resp?.remoteAccessSession?.endpoints?.remoteDriverEndpoint;
  if (!endpoint) throw new Error("remoteDriverEndpoint missing from response");
  return endpoint;
}

// To use the URL with WebdriverIO
import { remote } from "webdriverio";

(async () => {
  const endpoint = await getAppiumEndpoint();
  const u = new URL(endpoint);

  const driver = await remote({
    protocol: u.protocol.replace(":", ""),
    hostname: u.hostname,
    port: u.port ? Number(u.port) : (u.protocol === "https:" ? 443 : 80),
    path: u.pathname + u.search,
    capabilities: {
      platformName: "Android",
      "appium:automationName": "UiAutomator2",
      // ...other caps...
    },
  });

  try {
    // ... your test ...
  } finally {
    await driver.deleteSession();
  }
})();
```

------
#### [ C\# ]

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRemoteAccessSession.html) API:

```
// To get the URL
using System;
using System.Threading.Tasks;
using Amazon;
using Amazon.DeviceFarm;
using Amazon.DeviceFarm.Model;

public static class AppiumEndpointBuilder
{
    public static async Task<string> GetAppiumEndpointAsync()
    {
        var sessionArn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000";

        var config = new AmazonDeviceFarmConfig
        {
            RegionEndpoint = RegionEndpoint.USWest2
        };
        using var client = new AmazonDeviceFarmClient(config);

        var resp = await client.GetRemoteAccessSessionAsync(new GetRemoteAccessSessionRequest { Arn = sessionArn });
        var endpoint = resp?.RemoteAccessSession?.Endpoints?.RemoteDriverEndpoint;

        if (string.IsNullOrWhiteSpace(endpoint))
            throw new InvalidOperationException("RemoteDriverEndpoint missing from response");

        return endpoint;
    }
}

// To use the URL
using OpenQA.Selenium.Appium;
using OpenQA.Selenium.Appium.Android;

class Example
{
    static async Task Main()
    {
        var endpoint = await AppiumEndpointBuilder.GetAppiumEndpointAsync();

        var options = new AppiumOptions();
        options.PlatformName = "Android";
        options.AutomationName = "UiAutomator2";

        using var driver = new AndroidDriver(new Uri(endpoint), options);
        try
        {
            // ... your test ...
        }
        finally
        {
            driver.Quit();
        }
    }
}
```

------
#### [ Ruby ]

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRemoteAccessSession.html) API:

```
# To get the URL
require 'aws-sdk-devicefarm'

def get_appium_endpoint
  session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000"

  client = Aws::DeviceFarm::Client.new(region: 'us-west-2')
  resp = client.get_remote_access_session(arn: session_arn)
  endpoint = resp.remote_access_session.endpoints.remote_driver_endpoint
  raise "remote_driver_endpoint missing from response" if endpoint.nil? || endpoint.empty?
  endpoint
end

# To use the URL
require 'appium_lib_core'

endpoint = get_appium_endpoint
opts = {
  server_url: endpoint,
  capabilities: {
    'platformName' => 'Android',
    'appium:automationName' => 'UiAutomator2'
  }
}

driver = Appium::Core.for(opts).start_driver
begin
  # ... your test ...
ensure
  driver.quit
end
```

------

## Reviewing your Appium server logs
<a name="appium-endpoint-server-logs"></a>

Once you've [started an Appium session](#appium-endpoint-interaction), you can view the Appium server logs live in the Device Farm console, or download them after the remote access session ends. Here are the instructions for doing so:

------
#### [ Console ]

1. In the Device Farm console, open the Remote access session for your device.

1. Start an Appium endpoint session with the device from your local IDE or Appium Inspector

1. Then, the Appium server log will appear alongside the device in the remote access session page, with the "session information" available at the bottom of the page below the device:  
![The Appium server logs appear as your Appium session starts](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-appium-endpoint-logs.gif)

------
#### [ AWS CLI ]

*Note: this example uses the [command-line tool `curl`](https://curl.se/) to pull the log from Device Farm.*

During or after the session, you can use Device Farm's [`ListArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) API to download the Appium server log.

```
$ aws devicefarm list-artifacts \
  --type FILE \
  --arn arn:aws:devicefarm:us-west-2:111122223333:session:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000
```

This will show output such as the following during the session:

```
{
    "artifacts": [
        {
            "arn": "arn:aws:devicefarm:us-west-2:111122223333:artifact:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000",
            "name": "AppiumServerLogOutput",
            "type": "APPIUM_SERVER_LOG_OUTPUT",
            "extension": "",
            "url": "https://prod-us-west-2-results.s3.dualstack.us-west-2.amazonaws.com/111122223333/12345678..."
        }
    ]
}
```

And the following after the session is done:

```
{
    "artifacts": [
        {
            "arn": "arn:aws:devicefarm:us-west-2:111122223333:artifact:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000",
            "name": "Appium Server Output",
            "type": "APPIUM_SERVER_OUTPUT",
            "extension": "log",
            "url": "https://prod-us-west-2-results.s3.dualstack.us-west-2.amazonaws.com/111122223333/12345678..."
        }
    ]
}
```

```
$ curl "https://prod-us-west-2-results.s3.dualstack.us-west-2.amazonaws.com/111122223333/12345678..."
```

This will show output such as the following:

```
info Appium Welcome to Appium v2.5.4
info Appium Non-default server args:
info Appium { address: '127.0.0.1',
info Appium   allowInsecure:
info Appium    [ 'execute_driver_script',
info Appium      'session_discovery',
info Appium      'perf_record',
info Appium      'adb_shell',
info Appium      'chromedriver_autodownload',
info Appium      'get_server_logs' ],
info Appium   keepAliveTimeout: 0,
info Appium   logNoColors: true,
info Appium   logTimestamp: true,
info Appium   longStacktrace: true,
info Appium   sessionOverride: true,
info Appium   strictCaps: true,
info Appium   useDrivers: [ 'uiautomator' ] }
```

------
#### [ Python ]

*Note: this example uses the third-party `requests` package to download the log, as well as the AWS SDK for Python `boto3`.*

During or after the session, you can use Device Farm's [`ListArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) API to retrieve the Appium server log URL, then download it.

```
import pathlib
import requests
import boto3

def download_appium_log():
    session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000"
    client = boto3.client("devicefarm", region_name="us-west-2")

    # 1) List artifacts for the session (FILE artifacts), handling pagination
    artifacts = []
    token = None
    while True:
        kwargs = {"arn": session_arn, "type": "FILE"}
        if token:
            kwargs["nextToken"] = token
        resp = client.list_artifacts(**kwargs)
        artifacts.extend(resp.get("artifacts", []))
        token = resp.get("nextToken")
        if not token:
            break

    if not artifacts:
        raise RuntimeError("No artifacts found in this session")

    # Filter strictly to Appium server logs
    allowed = {"APPIUM_SERVER_OUTPUT", "APPIUM_SERVER_LOG_OUTPUT"}
    filtered = [a for a in artifacts if a.get("type") in allowed]
    if not filtered:
        raise RuntimeError("No Appium server log artifacts found (expected APPIUM_SERVER_OUTPUT or APPIUM_SERVER_LOG_OUTPUT)")

    # Prefer the final 'OUTPUT' log, else the live 'LOG_OUTPUT'
    chosen = (next((a for a in filtered if a.get("type") == "APPIUM_SERVER_OUTPUT"), None)
              or next((a for a in filtered if a.get("type") == "APPIUM_SERVER_LOG_OUTPUT"), None))

    url = chosen["url"]
    ext = chosen.get("extension") or "log"
    out = pathlib.Path(f"./appium_server_log.{ext}")

    # 2) Download the artifact
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(out, "wb") as fh:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    fh.write(chunk)

    print(f"Saved Appium server log to: {out.resolve()}")

download_appium_log()
```

This will show output such as the following:

```
info Appium Welcome to Appium v2.5.4
info Appium Non-default server args:
info Appium { address: '127.0.0.1', allowInsecure: [ 'execute_driver_script', ... ], useDrivers: [ 'uiautomator' ] }
```

------
#### [ Java ]

*Note: this example uses the AWS SDK for Java v2 and `HttpClient` to download the log, and is compatible with JDK versions 11 and higher.*

During or after the session, you can use Device Farm's [`ListArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) API to retrieve the Appium server log URL, then download it.

```
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Path;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.Artifact;
import software.amazon.awssdk.services.devicefarm.model.ArtifactCategory;
import software.amazon.awssdk.services.devicefarm.model.ListArtifactsRequest;
import software.amazon.awssdk.services.devicefarm.model.ListArtifactsResponse;

public class AppiumLogDownloader {

    public static void main(String[] args) throws Exception {
        String sessionArn = "arn:aws:devicefarm:us-west-2:111122223333:session:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000";

        try (DeviceFarmClient client = DeviceFarmClient.builder()
                .region(Region.US_WEST_2)
                .build()) {

            // 1) List artifacts for the session (FILE artifacts) with pagination
            List<Artifact> all = new ArrayList<>();
            String token = null;
            do {
                ListArtifactsRequest.Builder b = ListArtifactsRequest.builder()
                        .arn(sessionArn)
                        .type(ArtifactCategory.FILE);
                if (token != null) b.nextToken(token);
                ListArtifactsResponse page = client.listArtifacts(b.build());
                all.addAll(page.artifacts());
                token = page.nextToken();
            } while (token != null && !token.isBlank());

            // Filter strictly to Appium logs
            List<Artifact> filtered = all.stream()
                    .filter(a -> {
                        String t = a.typeAsString();
                        return "APPIUM_SERVER_OUTPUT".equals(t) || "APPIUM_SERVER_LOG_OUTPUT".equals(t);
                    })
                    .toList();

            if (filtered.isEmpty()) {
                throw new RuntimeException("No Appium server log artifacts found (expected APPIUM_SERVER_OUTPUT or APPIUM_SERVER_LOG_OUTPUT).");
            }

            // Prefer OUTPUT; else LOG_OUTPUT
            Artifact chosen = filtered.stream()
                    .filter(a -> "APPIUM_SERVER_OUTPUT".equals(a.typeAsString()))
                    .findFirst()
                    .orElseGet(() -> filtered.stream()
                            .filter(a -> "APPIUM_SERVER_LOG_OUTPUT".equals(a.typeAsString()))
                            .findFirst()
                            .get());

            String url = chosen.url();
            String ext = (chosen.extension() == null || chosen.extension().isBlank()) ? "log" : chosen.extension();
            Path out = Path.of("appium_server_log." + ext);

            // 2) Download the artifact with HttpClient
            HttpClient http = HttpClient.newBuilder()
                    .connectTimeout(Duration.ofSeconds(10))
                    .build();

            HttpRequest get = HttpRequest.newBuilder(URI.create(url))
                    .timeout(Duration.ofMinutes(5))
                    .GET()
                    .build();

            HttpResponse<Path> resp = http.send(get, HttpResponse.BodyHandlers.ofFile(out));
            if (resp.statusCode() / 100 != 2) {
                throw new IOException("Failed to download log, HTTP " + resp.statusCode());
            }
            System.out.println("Saved Appium server log to: " + out.toAbsolutePath());
        }
    }
}
```

This will show output such as the following:

```
info Appium Welcome to Appium v2.5.4
info Appium Non-default server args:
info Appium { address: '127.0.0.1', ..., useDrivers: [ 'uiautomator' ] }
```

------
#### [ JavaScript ]

*Note: this example uses AWS SDK for JavaScript (v3) and Node 18\+ `fetch` to download the log.*

During or after the session, you can use Device Farm's [`ListArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) API to retrieve the Appium server log URL, then download it.

```
import { DeviceFarmClient, ListArtifactsCommand } from "@aws-sdk/client-device-farm";
import { createWriteStream } from "fs";
import { pipeline } from "stream";
import { promisify } from "util";

const pipe = promisify(pipeline);
const client = new DeviceFarmClient({ region: "us-west-2" });

const sessionArn = "arn:aws:devicefarm:us-west-2:111122223333:session:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000";

// 1) List artifacts for the session (FILE artifacts), handling pagination
const artifacts = [];
let nextToken;
do {
  const page = await client.send(new ListArtifactsCommand({
    arn: sessionArn,
    type: "FILE",
    nextToken
  }));
  artifacts.push(...(page.artifacts ?? []));
  nextToken = page.nextToken;
} while (nextToken);

if (!artifacts.length) throw new Error("No artifacts found");

// Strict filter to Appium logs
const filtered = (artifacts ?? []).filter(a =>
  a.type === "APPIUM_SERVER_OUTPUT" || a.type === "APPIUM_SERVER_LOG_OUTPUT"
);
if (!filtered.length) {
  throw new Error("No Appium server log artifacts found (expected APPIUM_SERVER_OUTPUT or APPIUM_SERVER_LOG_OUTPUT).");
}

// Prefer OUTPUT; else LOG_OUTPUT
const chosen =
  filtered.find(a => a.type === "APPIUM_SERVER_OUTPUT") ??
  filtered.find(a => a.type === "APPIUM_SERVER_LOG_OUTPUT");

const url = chosen.url;
const ext = chosen.extension || "log";
const outPath = `./appium_server_log.${ext}`;

// 2) Download the artifact
const resp = await fetch(url);
if (!resp.ok) {
  throw new Error(`Failed to download log: ${resp.status} ${await resp.text().catch(()=>"")}`);
}
await pipe(resp.body, createWriteStream(outPath));
console.log("Saved Appium server log to:", outPath);
```

This will show output such as the following:

```
info Appium Welcome to Appium v2.5.4
info Appium Non-default server args:
info Appium { address: '127.0.0.1', allowInsecure: [ 'execute_driver_script', ... ], useDrivers: [ 'uiautomator' ] }
```

------
#### [ C\# ]

*Note: this example uses the AWS SDK for .NET and `HttpClient` to download the log.*

During or after the session, you can use Device Farm's [`ListArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) API to retrieve the Appium server log URL, then download it.

```
using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;
using System.Linq;
using Amazon;
using Amazon.DeviceFarm;
using Amazon.DeviceFarm.Model;

class AppiumLogDownloader
{
    static async Task Main()
    {
        var sessionArn = "arn:aws:devicefarm:us-west-2:111122223333:session:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000";

        using var client = new AmazonDeviceFarmClient(RegionEndpoint.USWest2);

        // 1) List artifacts for the session (FILE artifacts), handling pagination
        var all = new List<Artifact>();
        string? token = null;
        do
        {
            var page = await client.ListArtifactsAsync(new ListArtifactsRequest
            {
                Arn = sessionArn,
                Type = ArtifactCategory.FILE,
                NextToken = token
            });
            if (page.Artifacts != null) all.AddRange(page.Artifacts);
            token = page.NextToken;
        } while (!string.IsNullOrEmpty(token));

        if (all.Count == 0)
            throw new Exception("No artifacts found");

        // Strict filter to Appium logs
        var filtered = all.Where(a =>
            a.Type == "APPIUM_SERVER_OUTPUT" || a.Type == "APPIUM_SERVER_LOG_OUTPUT").ToList();

        if (filtered.Count == 0)
            throw new Exception("No Appium server log artifacts found (expected APPIUM_SERVER_OUTPUT or APPIUM_SERVER_LOG_OUTPUT).");

        // Prefer OUTPUT; else LOG_OUTPUT
        var chosen = filtered.FirstOrDefault(a => a.Type == "APPIUM_SERVER_OUTPUT")
                    ?? filtered.First(a => a.Type == "APPIUM_SERVER_LOG_OUTPUT");
        
        var url = chosen.Url;
        var ext = string.IsNullOrWhiteSpace(chosen.Extension) ? "log" : chosen.Extension;
        var outPath = $"./appium_server_log.{ext}";

        // 2) Download the artifact
        using var http = new HttpClient();
        using var resp = await http.GetAsync(url, HttpCompletionOption.ResponseHeadersRead);
        resp.EnsureSuccessStatusCode();
        await using (var fs = File.Create(outPath))
        {
            await resp.Content.CopyToAsync(fs);
        }
        Console.WriteLine($"Saved Appium server log to: {Path.GetFullPath(outPath)}");
    }
}
```

This will show output such as the following:

```
info Appium Welcome to Appium v2.5.4
info Appium Non-default server args:
info Appium { address: '127.0.0.1', ..., useDrivers: [ 'uiautomator' ] }
```

------
#### [ Ruby ]

*Note: this example uses the AWS SDK for Ruby and `Net::HTTP` to download the log.*

During or after the session, you can use Device Farm's [`ListArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) API to retrieve the Appium server log URL, then download it.

```
require "aws-sdk-devicefarm"
require "net/http"
require "uri"

client = Aws::DeviceFarm::Client.new(region: "us-west-2")
session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000"

# 1) List artifacts for the session (FILE artifacts), handling pagination
artifacts = []
token = nil
loop do
  page = client.list_artifacts(arn: session_arn, type: "FILE", next_token: token)
  artifacts.concat(page.artifacts || [])
  token = page.next_token
  break if token.nil? || token.empty?
end

raise "No artifacts found" if artifacts.empty?

# Strict filter to Appium logs
filtered = (artifacts || []).select { |a| ["APPIUM_SERVER_OUTPUT", "APPIUM_SERVER_LOG_OUTPUT"].include?(a.type) }
raise "No Appium server log artifacts found (expected APPIUM_SERVER_OUTPUT or APPIUM_SERVER_LOG_OUTPUT)." if filtered.empty?

# Prefer OUTPUT; else LOG_OUTPUT
chosen = filtered.find { |a| a.type == "APPIUM_SERVER_OUTPUT" } ||
         filtered.find { |a| a.type == "APPIUM_SERVER_LOG_OUTPUT" }

url = chosen.url
ext = (chosen.extension && !chosen.extension.empty?) ? chosen.extension : "log"
out_path = "./appium_server_log.#{ext}"

# 2) Download the artifact
uri = URI.parse(url)
Net::HTTP.start(uri.host, uri.port, use_ssl: (uri.scheme == "https")) do |http|
  req = Net::HTTP::Get.new(uri)
  http.request(req) do |resp|
    raise "Failed GET: #{resp.code} #{resp.body}" unless resp.code.to_i / 100 == 2
    File.open(out_path, "wb") { |f| resp.read_body { |chunk| f.write(chunk) } }
  end
end
puts "Saved Appium server log to: #{File.expand_path(out_path)}"
```

This will show output such as the following:

```
info Appium Welcome to Appium v2.5.4
info Appium Non-default server args:
info Appium { address: '127.0.0.1', allowInsecure: [ 'execute_driver_script', ... ], useDrivers: [ 'uiautomator' ] }
```

------

## Supported features and versions
<a name="appium-endpoint-support"></a>

During a remote access session, you can select the major version of the Appium server that runs on your device. Choose the version that supports the Appium features that your tests require.

The Device Farm Appium endpoint also supports most of the same commands and desired capabilities that you use on local devices, with a few exceptions. The following sections list the capabilities and commands that aren't supported.

**Topics**
+ [Supported Appium server versions](#appium-endpoint-supported-versions)
+ [Supported capabilities](#appium-endpoint-unsupported-capabilities)
+ [Supported commands](#appium-endpoint-unsupported-commands)

### Supported Appium server versions
<a name="appium-endpoint-supported-versions"></a>

The following table lists the supported Appium server major versions in remote access sessions, and the device operating system (OS) versions that each version supports.


| Appium server version | Supported Android versions | Supported iOS versions | 
| --- | --- | --- | 
|  3  | All versions | 15 and above | 
|  2  | All versions | 15 and above | 

**Note**  
The set of supported versions might change over time. We recommend that you check this page for the current list.

You must set the Appium server version on iOS devices running version 27 or later. On older devices, selecting a version is optional. If you don't specify a version, Device Farm uses server version 2 on those devices.

#### Select a server version
<a name="appium-endpoint-selecting-version"></a>

To select a version, set the `appium:version` parameter in your request with the desired major version as the value. If that version isn't available for the device, Device Farm rejects the request.

------
#### [ Console ]

**To create a remote access session with a selected Appium server version**

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. If you already have a project, choose it from the list. Otherwise, create a project by following the instructions in [Creating a project in AWS Device Farm](#how-to-create-project).

1. On the **Remote access** tab, choose **Create remote access session**.

1. Choose a device from the list of available devices, or use the search bar at the top of the list to find one.

1. In **Session name**, enter a name for the session.

1. *(Optional)* Under **Select applications**, include your own app or choose the Device Farm Sample App as part of the session. These can be newly uploaded apps, or apps previously uploaded to this project. App uploads [expire after 30 days](#data-protection-retention).

1. Under **Advanced Configuration**, for **Appium server version**, choose the major version that you want to use. If you don't select a version, the Device Farm console uses a pre-selected version for the device. This pre-selected version might change over time.

1. Choose **Confirm and start session**.

------
#### [ AWS CLI ]

The following example creates a remote access session with a selected Appium server version.

This example uses the AWS CLI v2.

```
$ aws devicefarm create-remote-access-session \
    --project-arn "{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}" \
    --device-arn "{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}" \
    --configuration '{"parameters":{"appium:version":"{{3}}"}}'
```

------
#### [ Node.js ]

The following example creates a remote access session with a selected Appium server version.

This example uses the AWS SDK for JavaScript v3 with Node.js 18 or later.

```
import { DeviceFarmClient, CreateRemoteAccessSessionCommand } from "@aws-sdk/client-device-farm";

const client = new DeviceFarmClient({ region: "us-west-2" });

const command = new CreateRemoteAccessSessionCommand({
  projectArn: "{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
  deviceArn: "{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}",
  configuration: { parameters: { "appium:version": "{{3}}" } },
});

const resp = await client.send(command);
```

------
#### [ Python ]

The following example creates a remote access session with a selected Appium server version.

```
import boto3

client = boto3.client("devicefarm", region_name="us-west-2")

resp = client.create_remote_access_session(
    projectArn="{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    deviceArn="{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}",
    configuration={"parameters": {"appium:version": "{{3}}"}},
)
```

------
#### [ Java ]

The following example creates a remote access session with a selected Appium server version.

This example uses the AWS SDK for Java v2.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionConfiguration;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionResponse;

import java.util.Map;

public class SelectAppiumVersionExample {
    public static void main(String[] args) {
        try (DeviceFarmClient client = DeviceFarmClient.builder()
                .region(Region.US_WEST_2)
                .build()) {

            CreateRemoteAccessSessionConfiguration configuration = CreateRemoteAccessSessionConfiguration.builder()
                    .parameters(Map.of("appium:version", "{{3}}"))
                    .build();
            CreateRemoteAccessSessionRequest request = CreateRemoteAccessSessionRequest.builder()
                    .projectArn("{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}")
                    .deviceArn("{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}")
                    .configuration(configuration)
                    .build();

            CreateRemoteAccessSessionResponse resp = client.createRemoteAccessSession(request);
        }
    }
}
```

------
#### [ Ruby ]

The following example creates a remote access session with a selected Appium server version.

```
require 'aws-sdk-devicefarm'

client = Aws::DeviceFarm::Client.new(region: 'us-west-2')

resp = client.create_remote_access_session(
  project_arn: "{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
  device_arn: "{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}",
  configuration: { parameters: { "appium:version" => "{{3}}" } }
)
```

------

### Supported capabilities
<a name="appium-endpoint-unsupported-capabilities"></a>

When creating an Appium session on Device Farm, we recommend having a distinct set of capabilities which exclude any capabilities specific to your local device. On Device Farm, session creation may fail if certain unsupported capabilities are set. This includes device-specific capabilities like `udid` and `platformVersion`. Additionally, certain capabilities related to ChromeDriver on Android and WebDriverAgent on iOS aren't supported, as well as capabilities that are only supported on emulators and simulators.

### Supported commands
<a name="appium-endpoint-unsupported-commands"></a>

Most Appium commands that run properly on real Android and iOS devices will run as-expected on Device Farm, with the following exclusions: 

#### Appium device commands (`/appium/device`)
<a name="appium-endpoint-unsupported-device-commands"></a>
+ `install_app`
+ `finger_print`
+ `send_sms`
+ `gsm_call`
+ `gsm_signal`
+ `gsm_voice`
+ `power_ac`
+ `power_capacity`
+ `network_speed`
+ `shake`

#### Appium execute methods and scripts (`/execute`)
<a name="appium-endpoint-unsupported-execute-methods"></a>
+ `installApp`
+ `execEmuConsoleCommand`
+ `fingerprint`
+ `gsmCall`
+ `gsmSignal`
+ `sendSms`
+ `gsmVoice`
+ `powerAC`
+ `powerCapacity`
+ `networkSpeed`
+ `sensorSet`
+ `injectEmulatorCameraImage`
+ `isGpsEnabled`
+ `shake`
+ `clearApp`
+ `clearKeychains`
+ `configureLocalization`
+ `enrollBiometric`
+ `getPasteboard`
+ `installXCTestBundle`
+ `listXCTestBundles`
+ `listXCTestsInTestBundle`
+ `runXCTest`
+ `sendBiometricMatch`
+ `setPasteboard`
+ `setPermission`
+ `startAudioRecording`
+ `startLogsBroadcast`
+ `startRecordingScreen`
+ `startScreenStreaming`
+ `startXCTestScreenRecording`
+ `stopAudioRecording`
+ `stopLogsBroadcast`
+ `stopRecordingScreen`
+ `stopScreenStreaming`
+ `stopXCTestScreenRecording`
+ `updateSafariPreferences`

# Private devices in AWS Device Farm
<a name="working-with-private-devices"></a>

A private device is a physical mobile device that AWS Device Farm deploys on your behalf in an Amazon data center. This device is exclusive to your AWS account.

**Note**  
Currently, private devices are available only in the AWS US West (Oregon) Region (`us-west-2`).

If you have a private device fleet, you can create remote access sessions and schedule test runs with your private devices. For more information, see [Creating a test run or starting a remote access session in AWS Device Farm](#create-test-run-using-private-devices). You can also create instance profiles to control the behavior of your private devices during a remote access session or a test run. For more information, see [Creating an instance profile in AWS Device Farm](#set-up-private-devices-account-settings). Optionally, you can request that certain Android private devices be deployed as rooted devices.

You can also create an Amazon Virtual Private Cloud endpoint service to test private apps that your company has access to, but are not reachable through the internet. For example, you might have a web application running in your VPC that you want to test on mobile devices. For more information, see [Using Amazon VPC endpoint services with Device Farm - Legacy (not recommended)](#amazon-vpc-endpoints).

If you're interested in using a fleet of private devices, [contact us](mailto:aws-devicefarm-support@amazon.com). The Device Farm team must work with you to set up and deploy a fleet of private devices for your AWS account.

**Topics**
+ [Creating an instance profile in AWS Device Farm](#set-up-private-devices-account-settings)
+ [Request additional private devices in AWS Device Farm](#managing-private-device-instance)
+ [Creating a test run or starting a remote access session in AWS Device Farm](#create-test-run-using-private-devices)
+ [Selecting private devices in a device pool in AWS Device Farm](#selecting-private-devices)
+ [Skipping app re-signing on private devices in AWS Device Farm](#skip-app-re-signing-on-private-devices)
+ [Amazon VPC across AWS Regions in AWS Device Farm](#amazon-vpc-cross-region)
+ [Terminating private devices in Device Farm](#terminate-private-device)

## Creating an instance profile in AWS Device Farm
<a name="set-up-private-devices-account-settings"></a>

You can set up a fleet that contains one or more private devices. These devices are dedicated to your AWS account. After you set up the devices, you can optionally create one or more instance profiles for them. Instance profiles can help you automate test runs and consistently apply the same settings to device instances. Instances profiles can also help you control the behavior of remote access session. For more information about private devices in Device Farm, see [Private devices in AWS Device Farm](#working-with-private-devices).

**To create an instance**

1. Open the Device Farm console at [https://console.aws.amazon.com/devicefarm/](https://console.aws.amazon.com/devicefarm/).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Private devices**.

1. Choose **Instance profiles**.

1. Choose **Create instance profile**.

1. Enter a name for the instance profile.  
![Settings for an instance profile](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-private-devices-create-new-instance-profile.png)

1. (Optional) Enter a description for the instance profile.

1. (Optional) Change any of the following settings to specify which actions you want Device Farm to take on a device after each test run or session ends:
   + **Reboot after use** – To reboot the device, select this check box. By default, this check box is cleared (`false`).
   + **Package cleanup** – To remove all the app packages that you installed on the device, select this check box. By default, this check box is cleared (`false`). To keep all the app packages that you installed on the device, leave this check box cleared.
   + **Exclude packages from cleanup** – To keep only selected app packages on the device, select the **Package Cleanup** check box, and then choose **Add new**. For the package name, enter the fully qualified name of the app package that you want to keep on the device (for example, `com.test.example`). To keep more app packages on the device, choose **Add new**, and then enter the fully qualified name of each package.

1. Choose **Save**.

## Request additional private devices in AWS Device Farm
<a name="managing-private-device-instance"></a>

In AWS Device Farm, you can request an additional private device instances to be added to your fleet. You can also view and change the settings of existing private device instances in your fleet. For more information about private devices, see [Private devices in AWS Device Farm](#working-with-private-devices).

**To request additional private devices or change their settings**

1. Open the Device Farm console at [https://console.aws.amazon.com/devicefarm/](https://console.aws.amazon.com/devicefarm/).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Private devices**.

1. Choose **Device instances**. The **Device instances** tab displays a table of the private devices that are in your fleet. To quickly search or filter the table, enter search terms in the search bar above the columns.

1. To request a new private device instance, choose **Request device instance** or [contact us](mailto:aws-devicefarm-support@amazon.com). Private devices require additional setup with help from the Device Farm team.

1. In the table of device instances, choose the toggle option next to the instance that you want to view information about or manage, then choose **Edit**.  
![Settings for a device instance](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-edit-device-instance.png)

1. To attach an instance profile to the device instance, choose it from the **Profile** drop-down list. Attaching an instance profile can be helpful if you want to always exclude a specific app package from cleanup tasks, for example. For more information about using instance profiles with devices, see [Creating an instance profile in AWS Device Farm](#set-up-private-devices-account-settings).

1. (Optional) Under **Labels**, choose **Add new** to add a label to the device instance. Labels can help you categorize your devices and find specific devices more easily.

1. Choose **Save**.

## Creating a test run or starting a remote access session in AWS Device Farm
<a name="create-test-run-using-private-devices"></a>

In AWS Device Farm, after you set up a private device fleet, you can create test runs or start remote access sessions with one or more private devices in your fleet. For more information about private devices, see [Private devices in AWS Device Farm](#working-with-private-devices).

**To create a test run or start a remote access session**

1. Open the Device Farm console at [https://console.aws.amazon.com/devicefarm/](https://console.aws.amazon.com/devicefarm/).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

   

1. Choose an existing project from the list or create a new one. To create a new project, choose **New project**, enter a name for the project, and then choose **Submit**.

1. Do one of the following:
   + To create a test run, choose **Automated tests**, and then choose **Create a new run**. The wizard guides you through the steps to create the run. For the **Select devices** step, you can edit an existing device pool or create a new device pool that includes only those private devices that the Device Farm team set up and associated with your AWS account. For more information, see [Creating a private device pool with private devices (console)](#create-new-device-pool).
   + To start a remote access session, choose **Remote access**, and then choose **Start a new session**. On the **Choose a device** page, select **Private device instances only** to limit the list to only those private devices that the Device Farm team set up and associated with your AWS account. Then, choose the device that you want to access, enter a name for the remote access session, and choose **Confirm and start session**.

       
![Private instances in a remote access session](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-use-private-device-instances-only-remote-access-session.png)

## Selecting private devices in a device pool in AWS Device Farm
<a name="selecting-private-devices"></a>

To use private devices in your test run, you can create a device pool that selects your private devices. Device pools enable you to select private devices primarily through three types of device pool rules: 

1. Rules based on the device ARN

1. Rules based on the device instance label

1. Rules based on the device instance ARN

In the following sections, each rule type and their use cases are described in depth. You can use the Device Farm console, AWS Command Line Interface (AWS CLI), or the Device Farm API to create or modify a device pool with private devices using these rules. 

**Topics**
+ [Device ARN](#device-arn-rules)
+ [Device instance labels](#device-instance-labels-rules)
+ [Instance ARN](#instance-arn-rules)
+ [Creating a private device pool with private devices (console)](#create-new-device-pool)
+ [Creating a private device pool with private devices (AWS CLI)](#how-to-create-device-pool-cli-private-devices)
+ [Creating a private device pool with private devices (API)](#how-to-create-device-pool-api-private-devices)

### Device ARN
<a name="device-arn-rules"></a>

A device ARN is an identifier representing a type of device rather than any specific physical device instance. A device type is defined by the following attributes:
+ The device’s fleet ID
+ The device’s OEM
+ The device’s model number
+ The device’s operating system version
+ The device's state that indicates whether it's rooted or not

Many physical device instances can be represented by a single device type where every instance of that type has the same values for these attributes. For example, if you had three {{Apple iPhone 13}} devices on iOS version {{16.1.0}} in your private fleet, each device would share the same device ARN. If any devices were added or removed from your fleet with these same attributes, the device ARN would continue to represent whatever available devices you had in your fleet for that device type.

The device ARN is the most robust way of selecting private devices for a device pool because it allows the device pool to continue selecting devices regardless of the specific device instances you have deployed at any given time. Individual private device instances can experience hardware failures, prompting Device Farm to automatically replace them with new working instances of the same device type. In these scenarios, the device ARN rule ensures that your device pool can continue to select devices in the event of a hardware failure. 

When you use a device ARN rule for private devices in your device pool and schedule a test run with that pool, Device Farm will automatically check which private device instances are represented by that device ARN. Of the instances that are currently available, one of them will be assigned to run your test. If no instances are currently available, Device Farm will wait for the first available instance of that device ARN to become available, and assign it to run your test.

### Device instance labels
<a name="device-instance-labels-rules"></a>

A device instance label is a textual identifier you can attach as metadata for a device instance. You can attach multiple labels to each device instance and the same label to multiple device instances. For more information about adding, modifying, or removing device labels from device instances, see [Managing private devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/managing-private-devices.html). 

The device instance label can be a robust way of selecting private devices for a device pool because, if you have multiple device instances with the same label, then it allows the device pool to select from any one of them for your test. If the device ARN isn’t a good rule for your use case (for example, if you want to select from devices of multiple device types, or if you want to select from a subset of all devices of a device type), then device instance labels can enable you to select from multiple devices for your device pool with greater granularity. Individual private device instances can experience hardware failures, prompting Device Farm to automatically replace them with new working instances of the same device type. In these scenarios, the replacement device instance will not retain any instance label metadata of the replaced device. So, if you apply the same device instance label to multiple device instances, then the device instance label rule ensures that your device pool can continue to select device instances in the event of a hardware failure. 

When you use a device instance label rule for private devices in your device pool and schedule a test run with that pool, Device Farm will automatically check which private device instances are represented by that device instance label, and of those instances, randomly select one which is available to run your test. If none are available, Device Farm will randomly select any device instance with the device instance label to run your test and queue the test to run on the device once it’s available.

### Instance ARN
<a name="instance-arn-rules"></a>

A device instance ARN is an identifier representing a physical bare metal device instance deployed in a private fleet. For example, if you had three {{iPhone 13}} devices on OS {{15.0.0}} in your private fleet, while each device would share the same device ARN, each device would also have its own instance ARN representing that instance alone.

The device instance ARN is the least robust way to select private devices for a device pool and is only recommended if the device ARNs and device instance labels don’t fit your use case. Device instance ARNs are often used as rules for device pools when a specific device instance is configured in a unique and specific way as a prerequisite for your test and if that configuration needs to be known and verified before the test is ran on it. Individual private device instances can experience hardware failures, prompting Device Farm to automatically replace them with new working instances of the same device type. In these scenarios, the replacement device instance will have a different device instance ARN than the replaced device. So, if you rely on device instance ARNs for your device pool, then you’ll need to manually change your device pool’s rule definition from using the old ARN to using the new ARN. If you do need to manually preconfigure the device for its test, then this can be an effective workflow (compared to device ARNs). For testing at scale, it is recommended to try to adapt these use cases to work with device instance labels and if possible, have multiple device instances preconfigured for testing.

When you use a device instance ARN rule for private devices in your device pool and schedule a test run with that pool, Device Farm will automatically assign that test to that device instance. If that device instance isn’t available, Device Farm will queue the test on the device once it’s available.

### Creating a private device pool with private devices (console)
<a name="create-new-device-pool"></a>

When you create a test run, you can create a device pool for the test run and ensure that the pool includes only your private devices.

**Note**  
When creating a device pool with private devices in the console, you can only use any one of the three available rules for selecting private devices. If you want to create a device pool that contains multiple types of rules for private devices (for example, device pools that contain rules for device ARNs and device instance ARNs), then you need to create the pool through the CLI or API.

1. Open the Device Farm console at [https://console.aws.amazon.com/devicefarm/](https://console.aws.amazon.com/devicefarm/).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose an existing project from the list or create a new one. To create a new project, choose **New project**, enter a name for the project, and then choose **Submit**.

1. Choose **Project settings**, and then navigate to the **Device pools** tab.

1. Choose **Create device pool**, and enter a name and optional description for your device pool.

   1. To use device ARN rules for your device pool, choose **Create static device pool**, then select the specific device types from the list that you would like to use in the device pool. Do not select **Private device instances only** because this option causes the device pool to be created with device instance ARN rules (instead of device ARN rules).  
![Create static device pool option selected with See private device instances only checkbox.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-create-new-device-pool-private-devices.png)

   1. To use device instance label rules for your device pool, choose **Create dynamic device pool**. Then, for each label you would like to use in the device pool, choose **Add a rule**. For each rule, choose **Instance Labels** as the `Field`, choose **Contains** as the `Operator`, and specify your desired device instance label as the `Value`.  
![Device selection method section with dynamic pool option selected and filter rule configured.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-create-new-device-pool-private-devices-add-rule.png)

   1. To use device instance ARN rules for your device pool, choose **Create static device pool**, then select **Private device instances only** to limit the list of devices to only those private device instances that Device Farm has associated with your AWS account.  
![Create static device pool option selected with See private device instances only checkbox.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-create-new-device-pool-private-device-instance-only.png)

1. Choose **Create**.

### Creating a private device pool with private devices (AWS CLI)
<a name="how-to-create-device-pool-cli-private-devices"></a>
+ Run the [**create-device-pool**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-device-pool.html) command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](#cli-ref).

### Creating a private device pool with private devices (API)
<a name="how-to-create-device-pool-api-private-devices"></a>
+ Call the [`CreateDevicePool`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateDevicePool.html) API.

For information about using the Device Farm API, see [Automating Device Farm](#api-ref).

## Skipping app re-signing on private devices in AWS Device Farm
<a name="skip-app-re-signing-on-private-devices"></a>

App signing is a process that involves digitally signing an app package (e.g., [APK](https://developer.android.com/studio/publish/app-signing), [IPA](https://support.apple.com/guide/security/app-code-signing-process-sec7c917bf14/web)) with a private key before it can be installed on a device or published to an app store like the Google Play Store or the Apple App Store. To streamline testing by reducing the number of signatures and profiles needed and increase data security on remote devices, AWS Device Farm will re-sign your app after it has been uploaded to the service.

Once you upload your app to AWS Device Farm, the service will generate a new signature for the app using its own signing certificates and provisioning profiles. This process replaces the original app signature with AWS Device Farm's signature. The re-signed app is then installed on the test devices provided by AWS Device Farm. The new signature allows the app to be installed and run on these devices without the need for the original developer's certificates.

On iOS, we replace the embedded provisioning profile with a wildcard profile and re-sign the app. If you provide it, we will add auxiliary data to the application package before installation so the data will be present in your app’s sandbox. Re-signing the iOS app results in the removal of all entitlements.

On Android, we re-sign the app. This may break functionality that depends on the app signature, such as the Google Maps Android API. It may also trigger anti-piracy and anti-tamper detection available from products such as DexGuard. For built-in tests, we may modify the manifest to include permissions required to capture and save screenshots.

When you use private devices, you can skip the step where AWS Device Farm re-signs your app. This is different from public devices, where Device Farm always re-signs your app on the Android and iOS platforms.

You can skip app re-signing when you create a remote access session or a test run. This can be helpful if your app has functionality that breaks when Device Farm re-signs your app. For example, push notifications might not work after re-signing. For more information about the changes that Device Farm makes when it tests your app, see the [AWS Device Farm FAQs](https://aws.amazon.com/device-farm/faq/) or the [Apps](https://docs.aws.amazon.com/devicefarm/latest/developerguide/apps.html) page.

To skip app re-signing for a test run, select **Skip app re-signing** under **Additional configuration**. This option is only available for private devices.

![Select Skip app re-signing when using private device instances on a test run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-skip-app-re-signing.png)




**Note**  
If you're using the XCTest framework, the **Skip app re-signing** option is not available. For more information, see [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest).

Additional steps for configuring your app-signing settings vary, depending on whether you're using private Android or iOS devices.

### Skipping app re-signing on Android devices
<a name="signing-apps-on-android-devices"></a>

If you're testing your app on a private Android device, select **Skip app re-signing** when you create your test run or your remote access session. No other configuration is required.

### Skipping app re-signing on iOS devices
<a name="signing-apps-on-ios-devices"></a>

Apple requires you to sign an app for testing before you load it onto a device. For iOS devices, you have two options for signing your app. 
+ If you're using an in-house (Enterprise) developer profile, you can skip to the next section, [Creating a remote access session to trust your iOS app](#create-remote-session-trust-your-app).

  
+ If you're using an ad hoc iOS app development profile, you must first register the device with your Apple developer account, and then update your provisioning profile to include the private device. You must then re-sign your app with the provisioning profile that you updated. You can then run your re-signed app in Device Farm. 

**To register a device with an ad hoc iOS app development provisioning profile**

1. Sign in to your Apple developer account.

1. Navigate to the **Certificates, IDs, and Profiles** section of the console.

1. Go to **Devices**.

1. Register the device in your Apple developer account. To get the name and UDID of the device, use the `ListDeviceInstances` operation of the Device Farm API.

1. Go to your provisioning profile and choose **Edit**.

1. Choose the device from the list.

1. In Xcode, fetch your updated provisioning profile, and then re-sign the app.

No other configuration is required. You can now create a remote access session or a test run and select **Skip app re-signing**.

### Creating a remote access session to trust your iOS app
<a name="create-remote-session-trust-your-app"></a>

If you're using an in-house (Enterprise) developer provisioning profile, you must perform a one-time procedure to trust the in-house app developer certificate on each of your private devices.

To do so, you must install a placeholder app that's signed with the same certificate as the app that you want to test. After the device trusts the configuration profile or enterprise app developer, all apps from that developer are trusted on the private device until you delete them. Therefore, when you install new versions of the app that you want to test, you won't have to trust the app developer again each time. This is particularly useful if you run test automations and you don't want to create a remote access session each time you test your app.

A common procedure many customers use is to re-sign the [Device Farm sample app for iOS](https://github.com/aws-samples/aws-device-farm-sample-app-for-ios/blob/master/prebuilt/prebuiltSampleApp.ipa), then install this onto their device as the placeholder app.

Before you start your remote access session, follow the steps in [Creating an instance profile in AWS Device Farm](#set-up-private-devices-account-settings) to create or modify an instance profile in Device Farm. In the instance profile, add the bundle ID of the placeholder app to the **Exclude packages from cleanup** setting. Then, attach the instance profile to the private device instance to ensure that Device Farm doesn't remove this app from the device before it starts a new test run. This ensures that your developer certificate remains trusted.

You can upload the placeholder app to the device by using a remote access session, which allows you to launch the app and trust the developer.

1. Follow the instructions in [Creating a session](#how-to-create-session) to create a remote access session that uses the private device instance profile that you created. When you create your session, be sure to select **Skip app re-signing**.  
![Skip app re-signing when creating a remote access session](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-create-reomte-access-session-skip-app-resigning.png)

   
**Important**  
To filter the list of devices to include only private devices, select **Private device instances only** to ensure that you use a private device with the correct instance profile.

   Be sure to also add the placeholder app or the app that you want to test to the **Exclude packages from cleanup** setting for the instance profile that's attached to this instance.

1. When your remote session starts, choose **Choose File** to install an application that uses your in-house provisioning profile.

1. Launch the app that you just uploaded.

1. Confirm that an iOS dialogue box appears indicating that the enterprise app developer is untrusted.

1. Then, if the iOS device is on iOS version 18 or greater, open a support ticket with the AWS Device Farm team to have our team trust the app for you, since these devices require the app to be manually trusted. Otherwise, if the iOS version is 17 or lower, you can go into the **Settings** app, and, under **General** settings, trust the app yourself from the **VPN and Profiles** menu.

All apps from this configuration profile or enterprise app developer are now trusted on this private device until you delete them.

## Amazon VPC across AWS Regions in AWS Device Farm
<a name="amazon-vpc-cross-region"></a>

Device Farm services are located only in the US West (Oregon) (`us-west-2`) Region. You can use Amazon Virtual Private Cloud (Amazon VPC) to reach a service in your Amazon Virtual Private Cloud in another AWS Region using Device Farm. If Device Farm and your service are in the same Region, see [Using Amazon VPC endpoint services with Device Farm - Legacy (not recommended)](#amazon-vpc-endpoints).

There are two ways to access your private services located in a different Region. If you have services located in one other Region that's not `us-west-2`, you can use VPC Peering in order to peer that Region’s VPC to another VPC that is interfacing with Device Farm in `us-west-2`. However, if you have services in multiple Regions, a Transit Gateway will allow you to access those services with a simpler network configuration.

For more information, see [VPC peering scenarios](https://docs.aws.amazon.com/vpc/latest/peering/peering-scenarios.html) in the *Amazon VPC Peering Guide*.

### VPC peering overview for VPCs in different Regions in AWS Device Farm
<a name="device-farm-vpce-configuration-cross-region-vpc-overview"></a>

You can peer any two VPCs in different Regions as long as they have distinct, non-overlapping CIDR blocks. This ensures that all of the private IP addresses are unique, and it allows all of the resources in the VPCs to address each other without the need for any form of network address translation (NAT). For more information about CIDR notation, see [RFC 4632](https://tools.ietf.org/html/rfc4632).

This topic includes a cross-Region example scenario in which Device Farm (referred to as *VPC-1*) is located in the US West (Oregon) (`us-west-2`) Region. The second VPC in this example (referred to as *VPC-2*) is in another Region.


**Device Farm VPC cross-Region example**  

| VPC Component | VPC-1 | VPC-2 | 
| --- | --- | --- | 
| CIDR | 10.0.0.0/16 | 172.16.0.0/16 | 

**Important**  
Establishing a peering connection between two VPCs can change the security posture of the VPCs. In addition, adding new entries to their route tables can change the security posture of the resources within the VPCs. It is your responsibility to implement these configurations in a way that meets your organization's security requirements. For more information, please see the [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

The following diagram shows the components in the example and the interactions between these components.

![Work with private devices across AWS Regions.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/device-farm-vpc-across-region-vpn.png)


**Topics**
+ [VPC peering overview for VPCs in different Regions in AWS Device Farm](#device-farm-vpce-configuration-cross-region-vpc-overview)
+ [Prerequisites for using Amazon VPC in AWS Device Farm](#device-farm-vpce-configuration-cross-region-prerequisites)
+ [Step 1: Setting up a peering connection between VPC-1 and VPC-2](#device-farm-vpce-configuration-cross-region-step1)
+ [Step 2: Updating the route tables in VPC-1 and VPC-2](#device-farm-vpce-configuration-cross-region-step2)
+ [Step 3: Creating a target group](#device-farm-vpce-configuration-cross-region-step3)
+ [Step 4: Creating a Network Load Balancer](#device-farm-vpce-configuration-cross-region-step4)
+ [Step 5: Creating a VPC endpoint service to connect your VPC to Device Farm](#device-farm-vpce-configuration-cross-region-step5)
+ [Step 6: Create a VPC endpoint configuration between your VPC and Device Farm](#device-farm-vpce-configuration-cross-region-step6)
+ [Step 7: Creating a test run to use the VPC endpoint configuration](#device-farm-vpce-configuration-cross-region-step7)
+ [Creating a scalable network with Transit Gateway](#device-farm-vpce-configuration-cross-region-transit-gateways)

### Prerequisites for using Amazon VPC in AWS Device Farm
<a name="device-farm-vpce-configuration-cross-region-prerequisites"></a>

This example requires the following:
+ Two VPCs that are configured with subnets containing non-overlapping CIDR blocks.
+ *VPC-1* must be in the `us-west-2` Region and contain subnets for Availability Zones `us-west-2a`, `us-west-2b`, and `us-west-2c`.

For more information on creating VPCs and configuring subnets, see [Working with VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html) in the *Amazon VPC Peering Guide*.

### Step 1: Setting up a peering connection between VPC-1 and VPC-2
<a name="device-farm-vpce-configuration-cross-region-step1"></a>

Establish a peering connection between the two VPCs containing non-overlapping CIDR blocks. To do this, see [Create and accept VPC peering connections](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html) in the *Amazon VPC Peering Guide*. Using this topic's cross-Region scenario and the *Amazon VPC Peering Guide*, the following example peering connection configuration is created:

**Name**  
`Device-Farm-Peering-Connection-1`

**VPC ID (Requester)**  
`vpc-0987654321gfedcba (VPC-2)`

**Account**  
`My account`

**Region**  
`US West (Oregon) (us-west-2)`

**VPC ID (Accepter)**  
`vpc-1234567890abcdefg (VPC-1)`

**Note**  
Ensure that you consult your VPC peering connection quotas when establishing any new peering connections. For more information, please see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-peering) in the *Amazon VPC Peering Guide*.

### Step 2: Updating the route tables in VPC-1 and VPC-2
<a name="device-farm-vpce-configuration-cross-region-step2"></a>

After setting up a peering connection, you must establish a destination route between the two VPCs to transfer data between them. To establish this route, you can manually update the route table of *VPC-1* to point to the subnet of *VPC-2* and vice versa. To do this, see [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html) in the *Amazon VPC Peering Guide*. Using this topic's cross-Region scenario and the *Amazon VPC Peering Guide*, the following example route table configuration is created:


**Device Farm VPC route table example**  

| VPC component | VPC-1 | VPC-2 | 
| --- | --- | --- | 
| Route table ID | rtb-1234567890abcdefg | rtb-0987654321gfedcba | 
| Local address range | 10.0.0.0/16 | 172.16.0.0/16 | 
| Destination address range | 172.16.0.0/16 | 10.0.0.0/16 | 

### Step 3: Creating a target group
<a name="device-farm-vpce-configuration-cross-region-step3"></a>

After you set up your destination routes, you can configure a Network Load Balancer in *VPC-1* to route requests to *VPC-2*.

The Network Load Balancer must first contain a target group that contains the IP addresses to which requests are sent.

**To create a target group**

1. Identify the IP addresses of the service that you want to target in *VPC-2*.
   + These IP addresses must be members of the subnet used in the peering connection.
   + The targeted IP addresses must be static and immutable. If your service has dynamic IP addresses, consider targeting a static resource (such as a Network Load Balancer) and having that static resource route requests to your true target.
**Note**  
If you're targeting one or more stand-alone Amazon Elastic Compute Cloud (Amazon EC2) instances, open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2), then choose **Instances**.
If you're targeting an Amazon EC2 Auto Scaling group of Amazon EC2 instances, you must associate the Amazon EC2 Auto Scaling group to a Network Load Balancer. For more information, see [Attaching a load balancer to your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html) in the *Amazon EC2 Auto Scaling User Guide*.  
Then, you can open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2), and then choose **Network Interfaces**. From there you can view the IP addresses for each of the Network Load Balancer's network interfaces in each **Availability Zone**.

1. Create a target group in *VPC-1*. To do this, see [Create a target group for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html) in the *User Guide for Network Load Balancers*.

   Target groups for services in a different VPC require the following configuration:
   + For **Choose a target type**, choose **IP addresses**.
   + For **VPC**, choose the VPC that will host the load balancer. For the topic example, this will be *VPC-1*.
   + On the **Register targets** page, register a target for each IP address in *VPC-2*.

     For **Network**, choose **Other private IP address**.

     For **Availability Zone**, choose your desired zones in *VPC-1*.

     For **IPv4 address**, choose the *VPC-2* IP address.

     For **Ports**, choose your ports.
   + Choose **Include as pending below**. When you're finished specifying addresses, choose **Register pending targets**.

Using this topic's cross-Region scenario and the *User Guide for Network Load Balancers*, the following values are used in the target group configuration:

**Target type**  
`IP addresses`

**Target group name**  
`my-target-group`

**Protocol/Port**  
`TCP : 80`

**VPC**  
`vpc-1234567890abcdefg (VPC-1)`

**Network**  
`Other private IP address`

**Availability Zone**  
`all`

**IPv4 address**  
`172.16.100.60`

**Ports**  
`80`

### Step 4: Creating a Network Load Balancer
<a name="device-farm-vpce-configuration-cross-region-step4"></a>

Create a Network Load Balancer using the target group described in [step 3](#device-farm-vpce-configuration-cross-region-step3). To do this, see [Creating a Network Load Balancer](#device-farm-create-nlb).

Using this topic's cross-Region scenario, the following values are used in an example Network Load Balancer configuration:

**Load balancer name**  
`my-nlb`

**Scheme**  
`Internal`

**VPC**  
`vpc-1234567890abcdefg (VPC-1)`

**Mapping**  
`us-west-2a` - `subnet-4i23iuufkdiufsloi`  
`us-west-2b` - `subnet-7x989pkjj78nmn23j`  
`us-west-2c` - `subnet-0231ndmas12bnnsds`

**Protocol/Port**  
`TCP : 80`

**Target Group**  
`my-target-group`

### Step 5: Creating a VPC endpoint service to connect your VPC to Device Farm
<a name="device-farm-vpce-configuration-cross-region-step5"></a>

You can use the Network Load Balancer to create a VPC endpoint service. Through this VPC endpoint service, Device Farm can connect to your service in *VPC-2* without any additional infrastructure, such as an internet gateway, NAT instance, or VPN connection.

To do this, see [Creating an Amazon VPC endpoint service](#device-farm-vpce-configuration-vpc-endpoint).

### Step 6: Create a VPC endpoint configuration between your VPC and Device Farm
<a name="device-farm-vpce-configuration-cross-region-step6"></a>

Now you can establish a private connection between your VPC and Device Farm. You can use Device Farm to test private services without exposing them through the public internet. To do this, see [Creating a VPC endpoint configuration in Device Farm](#device-farm-edit-devicefarm-settings-vpc-endpoint).

Using this topic's cross-Region scenario, the following values are used in an example VPC endpoint configuration:

**Name**  
`My VPCE Configuration`

**VPCE service name**  
`com.amazonaws.vpce.us-west-2.vpce-svc-1234567890abcdefg`

**Service DNS name**  
`devicefarm.com`

### Step 7: Creating a test run to use the VPC endpoint configuration
<a name="device-farm-vpce-configuration-cross-region-step7"></a>

You can create test runs that use the VPC endpoint configuration described in [step 6](#device-farm-vpce-configuration-cross-region-step6). For more information, see [Creating a test run in Device Farm](#how-to-create-test-run) or [Creating a session](#how-to-create-session).

### Creating a scalable network with Transit Gateway
<a name="device-farm-vpce-configuration-cross-region-transit-gateways"></a>

To create a scalable network using more than two VPCs, you can use Transit Gateway to act as a network transit hub to interconnect your VPCs and on-premises networks. To configure a VPC in the same region as Device Farm to use a Transit Gateway, you can follow the [Amazon VPC endpoint services with Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/amazon-vpc-endpoints.html) guide to target resources in another region based on their private IP addresses.

For more information about Transit Gateway, see [What is a transit gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) in the *Amazon VPC Transit Gateways Guide*.

## Terminating private devices in Device Farm
<a name="terminate-private-device"></a>

To terminate a private device after your initial agreed term, you must provide a 30-day notice of non-renewal via our email at aws-devicefarm-support@amazon.com. For more information about private devices, see [Private devices in AWS Device Farm](#working-with-private-devices).

**Important**  
These instructions **only** apply to terminating private device agreements. For all other AWS services and billing issues, see the respective documentation for those products or contact AWS support.

# VPC-ENI in AWS Device Farm
<a name="vpc-eni"></a>

**Warning**  
This feature is only available on [private devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/working-with-private-devices.html). To request private device use on your AWS account, please [contact us](mailto:aws-devicefarm-support@amazon.com). If you already have private devices added to your AWS account, we strongly recommend using this method of VPC connectivity.

AWS Device Farm's VPC-ENI connectivity feature helps customers securely connect to their private endpoints hosted on AWS, on-premise software, or another cloud provider. 

You can connect both Device Farm mobile devices and their host machines to an Amazon Virtual Private Cloud (Amazon VPC) environment in the `us-west-2` Region, which enables access to isolated, non-internet-facing services and applications through an [elastic network interface](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ElasticNetworkInterfaces.html). For more information on VPCs, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/). 

If your private endpoint or VPC is not in the `us-west-2` Region, you can link it with a VPC in the `us-west-2` Region using solutions such as a [Transit Gateway](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html) or [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html). In such situations, Device Farm will create an ENI in a subnet you provide for your `us-west-2` Region VPC, and you'll be responsible for ensuring that a connection can be established between the `us-west-2` Region VPC and the VPC in the other Region.

![Architecture diagram showing Device Farm connecting devices to VPCs in us-west-2 and other regions.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/VPC-ENI-Customer-Flow.jpg)


For information on using AWS CloudFormation to automatically create and peer VPCs, see the [VPCPeering templates](https://github.com/awslabs/aws-cloudformation-templates/tree/master/aws/solutions/VPCPeering) in the AWS CloudFormation template repository on GitHub. 

**Note**  
Device Farm doesn't charge anything for creating ENIs in a customer's VPC in `us-west-2`. The cost for cross-Region or external inter-VPC connectivity isn't included in this feature.

Once you configure VPC access, the devices and host machines that you use for your tests won't be able to connect to resources outside of the VPC (e.g., public CDNs) unless there is a NAT gateway that you specify within the VPC. For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*. 

**Topics**
+ [AWS access control and IAM](#vpc-eni-access-control)
+ [Service-linked roles](#vpc-eni-service-linked-role)
+ [Prerequisites](#vpc-eni-prerequisites)
+ [Connecting to Amazon VPC](#connecting-to-amazon-vpc)
+ [Limits](#vpc-eni-limits)
+ [Using Amazon VPC endpoint services with Device Farm - Legacy (not recommended)](#amazon-vpc-endpoints)

## AWS access control and IAM
<a name="vpc-eni-access-control"></a>

AWS Device Farm allows you to use [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) to create policies granting or restricting access to Device Farm's features. To use the VPC Connectivity feature with AWS Device Farm, the following IAM Policy is required for the user account or role that you are using to access AWS Device Farm:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "devicefarm:*",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:CreateNetworkInterface"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/devicefarm.amazonaws.com/AWSServiceRoleForDeviceFarm",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "devicefarm.amazonaws.com"
        }
      }
    }
  ]
}
```

------

To create or update a Device Farm project with a VPC configuration, your IAM policy must allow you to call the following actions against the resources listed in the VPC configuration:

```
"ec2:DescribeVpcs"
"ec2:DescribeSubnets"
"ec2:DescribeSecurityGroups"
"ec2:CreateNetworkInterface"
```

Additionally, your IAM policy must also allow for the creation of the service-linked role:

```
"iam:CreateServiceLinkedRole"
```

**Note**  
None of these permissions are required for users who don't use VPC configurations in their projects.

## Service-linked roles
<a name="vpc-eni-service-linked-role"></a>

AWS Device Farm uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Device Farm. Service-linked roles are predefined by Device Farm and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up Device Farm easier because you don’t have to manually add the necessary permissions. Device Farm defines the permissions of its service-linked roles, and unless defined otherwise, only Device Farm can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Device Farm resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

### Service-linked role permissions for Device Farm
<a name="slr-permissions"></a>

Device Farm uses the service-linked role named **AWSServiceRoleForDeviceFarm** – Allows Device Farm to access AWS resources on your behalf.

The AWSServiceRoleForDeviceFarm service-linked role trusts the following services to assume the role:
+ `devicefarm.amazonaws.com`

The role permissions policy allows Device Farm to complete the following actions:
+ For your account
  + Create network interfaces
  + Describe network interfaces
  + Describe VPCs
  + Describe subnets
  + Describe security groups
  + Delete interfaces
  + Modify network interfaces
+ For network interfaces
  + Create tags
+ For EC2 network interfaces managed by Device Farm
  + Create network interface permissions

The full IAM policy reads:

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
				"ec2:DescribeNetworkInterfaces",
				"ec2:DescribeVpcs",
				"ec2:DescribeSubnets",
				"ec2:DescribeSecurityGroups"
			],
			"Resource": "*"
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:CreateNetworkInterface"
			],
			"Resource": [
				"arn:aws:ec2:*:*:subnet/*",
				"arn:aws:ec2:*:*:security-group/*"
			]
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:CreateNetworkInterface"
			],
			"Resource": [
				"arn:aws:ec2:*:*:network-interface/*"
			],
			"Condition": {
				"StringEquals": {
					"aws:RequestTag/AWSDeviceFarmManaged": "true"
				}
			}
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:CreateTags"
			],
			"Resource": "arn:aws:ec2:*:*:network-interface/*",
			"Condition": {
				"StringEquals": {
					"ec2:CreateAction": "CreateNetworkInterface"
				}
			}
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:CreateNetworkInterfacePermission",
				"ec2:DeleteNetworkInterface"
			],
			"Resource": "arn:aws:ec2:*:*:network-interface/*",
			"Condition": {
				"StringEquals": {
					"aws:ResourceTag/AWSDeviceFarmManaged": "true"
				}
			}
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:ModifyNetworkInterfaceAttribute"
			],
			"Resource": [
				"arn:aws:ec2:*:*:security-group/*",
				"arn:aws:ec2:*:*:instance/*"
			]
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:ModifyNetworkInterfaceAttribute"
			],
			"Resource": "arn:aws:ec2:*:*:network-interface/*",
			"Condition": {
				"StringEquals": {
					"aws:ResourceTag/AWSDeviceFarmManaged": "true"
				}
			}
		}
	]
}
```

------

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

### Creating a service-linked role for Device Farm
<a name="create-slr"></a>

When you provide a VPC config for a mobile testing project, you don't need to manually create a service-linked role. When you create your first Device Farm resource in the AWS Management Console, the AWS CLI, or the AWS API, Device Farm creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create your first Device Farm resource, Device Farm creates the service-linked role for you again. 

You can also use the IAM console to create a service-linked role with the **Device Farm** use case. In the AWS CLI or the AWS API, create a service-linked role with the `devicefarm.amazonaws.com` service name. For more information, see [Creating a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

### Editing a service-linked role for Device Farm
<a name="edit-slr"></a>

Device Farm does not allow you to edit the AWSServiceRoleForDeviceFarm service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

### Deleting a service-linked role for Device Farm
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

**Note**  
If the Device Farm service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForDeviceFarm service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

### Supported Regions for Device Farm service-linked roles
<a name="slr-regions"></a>

Device Farm supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).

Device Farm does not support using service-linked roles in every region where the service is available. You can use the AWSServiceRoleForDeviceFarm role in the following regions.



| Region name | Region identity | Support in Device Farm | 
| --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | No | 
| US East (Ohio) | us-east-2 | No | 
| US West (N. California) | us-west-1 | No | 
| US West (Oregon) | us-west-2 | Yes | 
| Asia Pacific (Mumbai) | ap-south-1 | No | 
| Asia Pacific (Osaka) | ap-northeast-3 | No | 
| Asia Pacific (Seoul) | ap-northeast-2 | No | 
| Asia Pacific (Singapore) | ap-southeast-1 | No | 
| Asia Pacific (Sydney) | ap-southeast-2 | No | 
| Asia Pacific (Tokyo) | ap-northeast-1 | No | 
| Canada (Central) | ca-central-1 | No | 
| Europe (Frankfurt) | eu-central-1 | No | 
| Europe (Ireland) | eu-west-1 | No | 
| Europe (London) | eu-west-2 | No | 
| Europe (Paris) | eu-west-3 | No | 
| South America (São Paulo) | sa-east-1 | No | 
| AWS GovCloud (US) | us-gov-west-1 | No | 

## Prerequisites
<a name="vpc-eni-prerequisites"></a>

The following list describes some requirements and suggestions to review when creating VPC-ENI configurations:
+ Private devices must be assigned to your AWS Account.
+ You must have an AWS account user or role with permissions to create a Service-linked role. When using Amazon VPC endpoints with Device Farm mobile testing features, Device Farm creates an AWS Identity and Access Management (IAM) service-linked role. 
+ Device Farm can connect to VPCs only in the `us-west-2` Region. If you don't have a VPC in the `us-west-2` Region, you need to create one. Then, to access resources in a VPC in another Region, you must establish a peering connection between the VPC in the `us-west-2` Region and the VPC in the other Region. For information on peering VPCs, see the [Amazon VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/).

  You should verify that you have access to your specified VPC when you configure the connection. You must configure certain Amazon Elastic Compute Cloud (Amazon EC2) permissions for Device Farm. 
+ DNS resolution is required in the VPC that you use.
+ Once your VPC has been created, you will need the following information about the VPC in the `us-west-2` Region:
  + VPC ID
  + Subnet IDs (private subnets only)
  + Security group IDs
+ You must configure Amazon VPC connections on a per-project basis. At this time, you can configure only one VPC configuration per project. When you configure a VPC, Amazon VPC creates an interface within your VPC and assigns it to the specified subnets and security groups. All future sessions associated with the project will use the configured VPC connection.
+ You cannot use VPC-ENI configurations along with the legacy VPCE feature. 
+ We strongly recommend **not updating an existing project** with a VPC-ENI configuration as existing projects may have VPCE settings that persist on the run level. Instead, if you already use the existing VPCE features, use VPC-ENI for all new projects.

## Connecting to Amazon VPC
<a name="connecting-to-amazon-vpc"></a>

You can configure and update your project to use Amazon VPC endpoints. The VPC-ENI configuration is configured on a per-project basis. A project can have only one VPC-ENI endpoint at any given time. To configure VPC access for a project, you must know the following details:
+ The VPC ID in `us-west-2` if your app is hosted there or the `us-west-2` VPC ID that connects to some other VPC in a different Region. 
+ The applicable security groups to apply to the connection.
+ The subnets that will be associated with the connection. When a session starts, the largest available subnet is used. We recommend having multiple subnets associated with different availability zones to improve the availability posture of your VPC connectivity.
+ When using VPC-ENI, the DNS resolver used by the Device Farm test hosts and devices will be the server provided by DHCP services in the customer subnet. In a default configuration, this will be the VPC's default resolver. Customers wishing to specify custom DNS resolvers may configure a DHCP Option Set in their VPC.

Once you have created your VPC-ENI configuration, you can update its details using the console or CLI using the steps below.

------
#### [ Console ]

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Under **Mobile Testing projects**, choose the name of your project from the list.

1. Choose **Project settings**.

1. In the **Virtual Private Cloud (VPC) Settings** section, you can change the `VPC`, `Subnets` (private subnets only), and `Security Groups`.

1. Choose **Save**.

------
#### [ CLI ]

Use the following AWS CLI command to update the Amazon VPC:

```
$  aws devicefarm update-project \
--arn arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef \
--vpc-config \
securityGroupIds=sg-02c1537701a7e3763,sg-005dadf9311efda25,\
subnetIds=subnet-09b1a45f9cac53717,subnet-09b1a45f9cac12345,\
vpcId=vpc-0238fb322af81a368
```

You can also configure an Amazon VPC when creating your project:

```
$  aws devicefarm create-project \
--name VPCDemo \
--vpc-config \
securityGroupIds=sg-02c1537701a7e3763,sg-005dadf9311efda25,\
subnetIds=subnet-09b1a45f9cac53717,subnet-09b1a45f9cac12345,\
vpcId=vpc-0238fb322af81a368
```

------

## Limits
<a name="vpc-eni-limits"></a>

The following limitations are applicable to the VPC-ENI feature:
+ You can provide up to five security groups in the VPC configuration of a Device Farm project. 
+ You can provide up to eight subnets in the VPC configuration of a Device Farm project.
+ When configuring a Device Farm project to work with your VPC, the smallest subnet you can provide must have a minimum of five available IPv4 addresses.
+ Public IP addresses aren’t supported at this time. Instead, we recommend that you use private subnets in your Device Farm projects. If your need public internet access during your tests, use a [ network address translation (NAT) gateway](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-internet). Configuring a Device Farm project with a public subnet doesn't give your tests internet access or a public IP address.
+ VPC-ENI integration only supports private subnets in your VPC.
+ Only outgoing traffic from the service-managed ENI is supported. This means that the ENI cannot receive unsolicited inbound requests from the VPC.

## Using Amazon VPC endpoint services with Device Farm - Legacy (not recommended)
<a name="amazon-vpc-endpoints"></a>

**Warning**  
We strongly recommend using the VPC-ENI connectivity described on [this](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni.html) page for private endpoint connectivity as VPCE is now considered a legacy feature. VPC-ENI provides more flexibility, simpler configurations, is more cost efficient, and requires significantly less maintenance overhead when compared to the VPCE connectivity method.  
VPC endpoint (VPCE) connectivity is not supported on newer test hosts, including macos\_tahoe. To run tests that require private connectivity on these hosts, use VPC-ENI.

**Note**  
Using Amazon VPC Endpoint Services with Device Farm is only supported for customers with configured private devices. To enable your AWS account to use this feature with private devices, please [contact us](mailto:aws-devicefarm-support@amazon.com).

Amazon Virtual Private Cloud (Amazon VPC) is an AWS service that you can use to launch AWS resources in a virtual network that you define. With a VPC, you have control over your network settings, such as the IP address range, subnets, routing tables, and network gateways.

If you use Amazon VPC to host private applications in the US West (Oregon) (`us-west-2`) AWS Region, you can establish a private connection between your VPC and Device Farm. With this connection, you can use Device Farm to test private applications without exposing them through the public internet. To enable your AWS account to use this feature with private devices, [contact us](mailto:aws-devicefarm-support@amazon.com).

To connect a resource in your VPC to Device Farm, you can use the Amazon VPC console to create a VPC endpoint service. This endpoint service lets you provide the resource in your VPC to Device Farm through a Device Farm VPC endpoint. The endpoint service provides reliable, scalable connectivity to Device Farm without requiring an internet gateway, network address translation (NAT) instance, or VPN connection. For more information, see [VPC endpoint services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html) in the *AWS PrivateLink Guide*.

**Important**  
The Device Farm VPC endpoint feature helps you securely connect private internal services in your VPC to the Device Farm public VPC by using AWS PrivateLink connections. Although the connection is secure and private, that security depends on your protection of your AWS credentials. If your AWS credentials are compromised, an attacker can access or expose your service data to the outside world.

After you create a VPC endpoint service in Amazon VPC, you can use the Device Farm console to create a VPC endpoint configuration in Device Farm. This topic shows you how to create the Amazon VPC connection and the VPC endpoint configuration in Device Farm.

### Before you begin
<a name="device-farm-vpce-configuration-before-you-begin"></a>

The following information is for Amazon VPC users in the US West (Oregon) (`us-west-2`) Region, with a subnet in each of the following Availability Zones: us-west-2a, us-west-2b, and us-west-2c.

Device Farm has additional requirements for the VPC endpoint services that you can use it with. When you create and configure a VPC endpoint service to work with Device Farm, make sure that you choose options that meet the following requirements:
+ The Availability Zones for the service must include us-west-2a, us-west-2b, and us-west-2c. The Network Load Balancer that's associated with a VPC endpoint service determines the Availability Zones for that VPC endpoint service. If your VPC endpoint service doesn't show all three of these Availability Zones, you must re-create your Network Load Balancer to enable these three zones, and then reassociate the Network Load Balancer with your endpoint service.
+ The allowed principals for the endpoint service must include the Amazon Resource Name (ARN) of the Device Farm VPC endpoint (service ARN). After you create your endpoint service, add the Device Farm VPC endpoint service ARN to your allow list to give Device Farm permission to access your VPC endpoint service. To get the Device Farm VPC endpoint service ARN, [contact us](mailto:aws-devicefarm-support@amazon.com).

In addition, if you keep the **Acceptance required** setting turned on when you create your VPC endpoint service, you must manually accept each connection request that Device Farm sends to the endpoint service. To change this setting for an existing endpoint service, choose the endpoint service on the Amazon VPC console, choose **Actions**, and then choose **Modify endpoint acceptance setting**. For more information, see [Change the load balancers and acceptance settings](https://docs.aws.amazon.com/vpc/latest/privatelink/modify-endpoint-service.html) in the *AWS PrivateLink Guide*.

The next section explains how to create an Amazon VPC endpoint service that meets these requirements.

### Step 1: Creating a Network Load Balancer
<a name="device-farm-create-nlb"></a>

The first step in establishing a private connection between your VPC and Device Farm is to create a Network Load Balancer to route requests to a target group.

------
#### [ New console ]

**To create a Network Load Balancer using the new console**

1. Open the Amazon Elastic Compute Cloud (Amazon EC2) console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2).

1. In the navigation pane, under **Load balancing**, choose **Load balancers**.

1. Choose **Create load balancer**.

1. Under **Network load balancer**, choose **Create**.

1. On the **Create network load balancer** page, under **Basic configuration**, do the following:

   1. Enter a load balancer **Name**.

   1. For **Scheme**, choose **Internal**.

1. Under **Network mapping**, do the following:

   1. Choose the **VPC** for your target group.

   1. Select the following **Mappings**:
      + `us-west-2a`
      + `us-west-2b`
      + `us-west-2c`

1. Under **Listeners and routing**, use the **Protocol** and **Port** options to choose your target group.
**Note**  
By default, cross-availability zone load balancing is disabled.  
Because the load balancer uses the Availability Zones `us-west-2a`, `us-west-2b`, and `us-west-2c`, it either requires targets to be registered in each of those Availability Zones, or, if you register targets in less than all three zones, it requires that you enable cross-zone load balancing. Otherwise, the load balancer might not work as expected.

1. Choose **Create load balancer**.

------
#### [ Old console ]

**To create a Network Load Balancer using the old console**

1. Open the Amazon Elastic Compute Cloud (Amazon EC2) console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2).

1. In the navigation pane, under **Load balancing**, choose **load balancers**.

1. Choose **Create load balancer**.

1. Under **Network load balancer**, choose **Create**.

1. On the **Configure load balancer** page, under **Basic configuration**, do the following:

   1. Enter a load balancer **Name**.

   1. For **Scheme**, choose **Internal**.

1. Under **Listeners**, select the **Protocol** and **Port** that your target group is using.

1. Under **Availability zones**, do the following:

   1. Choose the **VPC** for your target group.

   1. Select the following **Availability zones**:
      + `us-west-2a`
      + `us-west-2b`
      + `us-west-2c`

   1. Choose **Next: configure security settings**.

1. (Optional) Configure your security settings, then choose **Next: configure routing**.

1. On the **Configure Routing** page, do the following:

   1. For **Target group**, choose **Existing target group**.

   1. For **Name**, choose your target group.

   1. Choose **Next: register targets**.

1. On the **Register targets** page, review your targets, then choose **Next: review**.
**Note**  
By default, cross-availability zone load balancing is disabled.  
Because the load balancer uses the Availability Zones `us-west-2a`, `us-west-2b`, and `us-west-2c`, it either requires targets to be registered in each of those Availability Zones, or, if you register targets in less than all three zones, it requires that you enable cross-zone load balancing. Otherwise, the load balancer might not work as expected.

1. Review your load balancer configuration, then choose **Create**.

------

### Step 2: Creating an Amazon VPC endpoint service
<a name="device-farm-vpce-configuration-vpc-endpoint"></a>

After creating the Network Load Balancer, use the Amazon VPC console to create an endpoint service in your VPC.

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Under **Resources by region**, choose **Endpoint services**.

1. Choose **Create endpoint service**.

1. Do one of the following:
   + If you already have a Network Load Balancer that you want the endpoint service to use, choose it under **Available load balancers**, and then continue to step 5.
   + If you haven't yet created a Network Load Balancer, choose **Create new load balancer**. The Amazon EC2 console opens. Follow the steps in [Creating a Network Load Balancer](#device-farm-create-nlb) beginning with step 3, then continue with these steps in the Amazon VPC console.

   

1. For **Included availability zones**, verify that `us-west-2a`, `us-west-2b`, and `us-west-2c` appear in the list.

1. If you don't want to manually accept or deny each connection request that is sent to the endpoint service, under **Additional settings**, clear **Acceptance required**. If you clear this check box, the endpoint service automatically accepts each connection request that it receives.

1. Choose **Create**.

1. In the new endpoint service, choose **Allow principals**.

1. [Contact us](mailto:aws-devicefarm-support@amazon.com) to get the ARN of the Device Farm VPC endpoint (service ARN) to add to the allow list for the endpoint service, and then add that service ARN to the allow list for the service.

1. On the **Details** tab for the endpoint service, make a note of the name of the service (**service name**). You need this name when you create the VPC endpoint configuration in the next step.

Your VPC endpoint service is now ready to use with Device Farm.

### Step 3: Creating a VPC endpoint configuration in Device Farm
<a name="device-farm-edit-devicefarm-settings-vpc-endpoint"></a>

After you create an endpoint service in Amazon VPC, you can create an Amazon VPC endpoint configuration in Device Farm.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile device testing**, then **Private devices**.

1. Choose **VPCE configurations**.

1. Choose **Create VPCE configuration**.

1. Under **Create a new VPCE configuration**, enter a **Name** for the VPC endpoint configuration.

1. For **VPCE service name**, enter the name of the Amazon VPC endpoint service (**service name**) that you noted in the Amazon VPC console. The name looks like `com.amazonaws.vpce.us-west-2.vpce-svc-id`.

1. For **Service DNS name**, enter the service DNS name for the app that you want to test (for example, `devicefarm.com`). Don't specify `http` or `https` before the service DNS name.

   The domain name is not accessible through the public internet. In addition, this new domain name, which maps to your VPC endpoint service, is generated by Amazon Route 53 and is available exclusively for you in your Device Farm session.

1. Choose **Save**.  
![The Create a New VPC Configuration page with sample data](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-create-vpce-configuration.png)

### Step 4: Creating a test run
<a name="device-farm-create-test-run"></a>

After you save the VPC endpoint configuration, you can use the configuration to create test runs or remotely access sessions. For more information, see [Creating a test run in Device Farm](#how-to-create-test-run) or [Creating a session](#how-to-create-session).

# Logging AWS Device Farm API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Device Farm is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Device Farm. CloudTrail captures all API calls for AWS Device Farm as events. The calls captured include calls from the AWS Device Farm console and code calls to the AWS Device Farm API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Device Farm. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Device Farm, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## AWS Device Farm information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Device Farm, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for AWS Device Farm, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

When CloudTrail logging is enabled in your AWS account, API calls made to Device Farm actions are tracked in log files. Device Farm records are written together with other AWS service records in a log file. CloudTrail determines when to create and write to a new file based on a time period and file size.

All of the Device Farm actions are logged and documented in the [AWS CLI reference](#cli-ref) and the [Automating Device Farm](#api-ref). For example, calls to create a new project or run in Device Farm generate entries in CloudTrail log files. 

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding AWS Device Farm log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the Device Farm `ListRuns` action:

```
{
  "Records": [
    {
      "eventVersion": "1.03",
      "userIdentity": {
        "type": "Root",
        "principalId": "AKIAI44QH8DHBEXAMPLE",
        "arn": "arn:aws:iam::123456789012:root",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2015-07-08T21:13:35Z"
          }
        }
      },
      "eventTime":"2015-07-09T00:51:22Z",
      "eventSource": "devicefarm.amazonaws.com",
      "eventName":"ListRuns",
      "awsRegion":"us-west-2",
      "sourceIPAddress":"203.0.113.11",
      "userAgent":"example-user-agent-string",
      "requestParameters": {
        "arn":"arn:aws:devicefarm:us-west-2:123456789012:project:a9129b8c-df6b-4cdd-8009-40a25EXAMPLE"},
        "responseElements": { 
          "runs": [
            {
              "created": "Jul 8, 2015 11:26:12 PM",
              "name": "example.apk",
              "completedJobs": 2,
              "arn": "arn:aws:devicefarm:us-west-2:123456789012:run:a9129b8c-df6b-4cdd-8009-40a256aEXAMPLE/1452d105-e354-4e53-99d8-6c993EXAMPLE",
              "counters": {
                "stopped": 0,
                "warned": 0,
                "failed": 0,
                "passed": 4,
                "skipped": 0,
                "total": 4,
                "errored": 0
              },
              "type": "BUILTIN_FUZZ",
              "status": "RUNNING",
              "totalJobs": 3,
              "platform": "ANDROID_APP",
              "result": "PENDING"
            },
            ... additional entries ...
          ]
        }
      }
    }
  ]
}
```

# Integrating AWS Device Farm in a CodePipeline test stage
<a name="codepipeline"></a>

 You can use [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) to incorporate mobile app tests configured in Device Farm into an AWS-managed automated release pipeline. You can configure your pipeline to run tests on demand, on a schedule, or as part of a continuous integration flow.

The following diagram shows the continuous integration flow in which an Android app is built and tested each time a push is committed to its repository. To create this pipeline configuration, see the [Tutorial: Build and Test an Android App When Pushed to GitHub](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-codebuild-devicefarm.html). 

![Continuos integration setup for building and testing Android source code from a GitHub repository on each push.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-push-build-test.png)




|  |  |  |  |  | 
| --- |--- |--- |--- |--- |
| 1. Configure | 2. Add definitions | 3. Push | 4. Build and test | 5. Report | 
| Configure pipeline resources | Add build and test definitions to your package | Push a package to your repository |  App build and test of build output artifact kicked off automatically | View test results | 

To learn how to configure a pipeline that continually tests a compiled app (such as an iOS `.ipa` or Android `.apk` file) as its source, see [Tutorial: Test an iOS App Each Time You Upload an .ipa File to an Amazon S3 Bucket](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-codebuild-devicefarm-S3.html). 

## Configure CodePipeline to use your Device Farm tests
<a name="codepipeline-configure-tests"></a>

 In these steps, we assume that you have [configured a Device Farm project](#how-to-create-project) and [created a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-codepipeline.html). The pipeline should be configured with a test stage that receives an [input artifact](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html#welcome-introducing-artifacts) that contains your test definition and compiled app package files. The test stage input artifact can be the output artifact of either a source or build stage configured in your pipeline. 

**To configure a Device Farm test run as an CodePipeline test action**

1. Sign in to the AWS Management Console and open the CodePipeline console at [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/).

1. Choose the pipeline for your app release.

1. On the test stage panel, choose the pencil icon, and then choose **Action**.

1. On the **Add action** panel, for **Action category**, choose **Test**.

1. In **Action name**, enter a name. 

1. In **Test provider**, choose **AWS Device Farm**.  
![Add a Device Farm test action to your pipeline.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-add-action.png)

1. In **Project name**, choose your existing Device Farm project or choose **Create a new project**. 

1. In **Device pool**, choose your existing device pool or choose **Create a new device pool**. If you create a device pool, you need to select a set of test devices.

1. In **App type**, choose the platform for your app.  
![Configure CodePipeline to use Device Farm as a test provider for stages of your pipeline.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-choose-test-provider.png)

1. In **App file path**, enter the path of the compiled app package. The path is relative to the root of the input artifact for your test.

1. In **Test type**, do one of the following: 
   + If you're using one of the built-in Device Farm tests, choose the type of test configured in your Device Farm project.
   + If you aren't using one of the Device Farm built-in tests, in the **Test file path**, enter the path of the test definition file. The path is relative to the root of the input artifact for your test.  
![Device Farm test types.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-test-type.png)

1. In the remaining fields, provide the configuration that is appropriate for your test and application type.

1. (Optional) In **Advanced**, provide detailed configuration for your test run.  
![Advanced AWS Device Farm configurations.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-advanced.png)

1. In **Input artifacts**, choose the input artifact that matches the output artifact of the stage that comes before the test stage in the pipeline.   
![Advanced AWS Device Farm configurations.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-input-artifact.png)

    In the CodePipeline console, you can find the name of the output artifact for each stage by hovering over the information icon in the pipeline diagram. If your pipeline tests your app directly from the **Source** stage, choose **MyApp**. If your pipeline includes a **Build** stage, choose **MyAppBuild**.  
![Advanced AWS Device Farm configurations.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-output-artifact.png)

1. At the bottom of the panel, choose **Add Action**.

1. In the CodePipeline pane, choose **Save pipeline change**, and then choose **Save change**.

1. To submit your changes and start a pipeline build, choose **Release change**, and then choose **Release**.

# AWS CLI reference for AWS Device Farm
<a name="cli-ref"></a>

To use the AWS Command Line Interface (AWS CLI) to run Device Farm commands, see the [AWS CLI Reference for AWS Device Farm](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/index.html).

For general information about the AWS CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/) and the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).

# Windows PowerShell reference for AWS Device Farm
<a name="powershell-ref"></a>

To use Windows PowerShell to run Device Farm commands, see the [Device Farm Cmdlet Reference](http://docs.aws.amazon.com/powershell/latest/reference/items/AWS_Device_Farm_cmdlets.html) in the [AWS Tools for Windows PowerShell Cmdlet Reference](http://docs.aws.amazon.com/powershell/latest/reference/Index.html). For more information, see [Setting up the AWS Tools for Windows PowerShell](http://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html) in the *AWS Tools for PowerShell User Guide*.

# Automating AWS Device Farm
<a name="api-ref"></a>

 Programmatic access to Device Farm is a powerful way to automate the common tasks that you need to accomplish, such as scheduling a run or downloading the artifacts for a run, suite, or test. The AWS SDK and AWS CLI provide means to do so. 

 The AWS SDK provides access to every AWS service, including Device Farm, Amazon S3, and more. For more information, see
+ the [AWS tools and SDKs](https://aws.amazon.com/tools/)
+ the [AWS Device Farm API Reference](https://docs.aws.amazon.com/devicefarm/latest/APIReference/Welcome.html)

## Example: Using the AWS CLI or SDK to upload an app or test to Device Farm
<a name="upload-example"></a>

The following examples show how to create an upload on Device Farm using the AWS CLI or using the AWS SDK in various languages. Uploads are the core building blocks for scheduling test runs on Device Farm, and include the following:
+ Your app
+ Your test
+ Your [test spec file](#custom-test-environment-test-spec)

Uploads are created using the [`CreateUpload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html) API. This API returns an S3 presigned URL that you can push your upload to using an HTTP PUT request. The URL expires after 24 hours.

------
#### [ AWS CLI ]

*Note: this example uses the [command-line tool `curl`](https://curl.se/) to push the app to Device Farm.*

First, create a project if you haven't already done so.

```
$ aws devicefarm create-project --name MyProjectName
```

This will show output such as the following:

```
{
    "project": {
        "name": "MyProjectName",
        "arn": "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
        "created": 1535675814.414
    }
}
```

Then, do the following to create your upload and push it to Device Farm. In this example, we'll be creating an Android app upload using a local APK file. For more upload type information, including details about iOS app upload types, please see our API documentation for creating an [`Upload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html).

```
$ export APP_PATH="/local/path/to/my_sample_app.apk"
$ export APP_TYPE="ANDROID_APP"
```

First, we create the upload in Device Farm:

```
$ aws devicefarm create-upload \
  --project-arn "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE" \
  --name "$(basename "$APP_PATH")" \
  --type "$APP_TYPE"
```

This will show output such as the following:

```
{
    "upload": {
        "arn": "arn:aws:devicefarm:us-west-2:385076942068:upload:490a6350-0ba3-43e5-83f5-d2896b069a34/a120e848-c57b-4e8d-a720-d750a0c4d936",
        "name": "my_sample_app.apk",
        "created": 1760747318.266,
        "type": "ANDROID_APP",
        "status": "INITIALIZED",
        "url": "https://prod-us-west-2-uploads.s3.dualstack.us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2...",
        "category": "PRIVATE"
    }
}
```

Then, do a PUT call using curl to push the app to Device Farm's S3 bucket:

```
$ curl -T "$APP_PATH" "https://prod-us-west-2-uploads.s3.dualstack.us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2..."
```

Finally, wait for the app to be in "succeeded" status:

```
$ aws devicefarm get-upload --arn "arn:aws:devicefarm:us-west-2:385076942068:upload:490a6350-0ba3-43e5-83f5-d2896b069a34/a120e848-c57b-4e8d-a720-d750a0c4d936"
```

This will show output such as the following:

```
{
    "upload": {
        "arn": "arn:aws:devicefarm:us-west-2:385076942068:upload:490a6350-0ba3-43e5-83f5-d2896b069a34/a120e848-c57b-4e8d-a720-d750a0c4d936",
        "name": "my_sample_app.apk",
        "created": 1760747318.266,
        "type": "ANDROID_APP",
        "status": "SUCCEEDED",
        "url": "https://prod-us-west-2-uploads.s3.dualstack.us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2...",
        "metadata": "{\"activity_name\":\"com.amazonaws.devicefarm.android.referenceapp.Activities.MainActivity\",\"package_name\":\"com.amazonaws.devicefarm.android.referenceapp\",...}",
        "category": "PRIVATE"
    }
}
```

------
#### [ Python ]

*Note: this example uses the third-party `requests` package to push the app to Device Farm, as well as the AWS SDK for Python `boto3`.*

First, create a project if you haven't already done so.

```
import boto3

client = boto3.client("devicefarm", region_name="us-west-2")
resp = client.create_project(name="MyProjectName")

print(resp)
# Response will be something like:
# {
#     "project": {
#         "name": "MyProjectName",
#         "arn": "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
#         "created": 1535675814.414
#     }
# }
```

Then, do the following to create your upload and push it to Device Farm. In this example, we'll be creating an Android app upload using a local APK file. For more upload type information, including details about iOS app upload types, please see our API documentation for creating an [`Upload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html).

```
import os
import time
import datetime
import requests
from pathlib import Path
import boto3


def upload_device_farm_file():
    project_arn = "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
    app_path = Path("/local/path/to/my_sample_app.apk")
    file_type = "ANDROID_APP"

    if not app_path.is_file():
        raise RuntimeError(f"{app_path} is not a valid app file path")

    client = boto3.client("devicefarm", region_name="us-west-2")

    # 1) Create the upload in Device Farm
    create = client.create_upload(
        projectArn=project_arn,
        name=app_path.name,
        type=file_type,
        contentType="application/octet-stream",
    )
    upload = create["upload"]
    upload_arn = upload["arn"]
    upload_url = upload["url"]
    # This will show output such as the following:
    # { "upload": { "arn": "...", "name": "my_sample_app.apk", "type": "ANDROID_APP", "status": "INITIALIZED", "url": "https://..." } }

    # 2) Do an HTTP PUT command to push the file to the pre-signed S3 URL
    with app_path.open("rb") as fh:
        print(f"Uploading {app_path.name} to Device Farm...")
        put_resp = requests.put(upload_url, data=fh, headers={"Content-Type": "application/octet-stream"})
        put_resp.raise_for_status()

    # 3) Wait for the app to be in "SUCCEEDED" status (or fail/timeout)
    timeout_seconds = 30
    start = time.time()
    while True:
        get_resp = client.get_upload(arn=upload_arn)
        status = get_resp["upload"]["status"]
        msg = get_resp["upload"].get("message") or get_resp["upload"].get("metadata") or ""
        elapsed = datetime.timedelta(seconds=int(time.time() - start))
        print(f"[{elapsed}] status={status}{' - ' + msg if msg else ''}")

        if status == "SUCCEEDED":
            print(f"Upload complete: {upload_arn}")
            return upload_arn
        if status == "FAILED":
            raise RuntimeError(f"Device Farm failed to process upload: {msg}")

        if (time.time() - start) > timeout_seconds:
            raise RuntimeError(f"Timed out after {timeout_seconds}s waiting for upload to process (last status={status}).")
        
        time.sleep(1)
        
upload_device_farm_file()
```

------
#### [ Java ]

*Note: this example uses the AWS SDK for Java v2 and `HttpClient` to push the app to Device Farm, and is compatible with JDK versions 11 and higher.*

First, create a project if you haven't already done so.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.CreateProjectRequest;
import software.amazon.awssdk.services.devicefarm.model.CreateProjectResponse;

try (DeviceFarmClient client = DeviceFarmClient.builder()
        .region(Region.US_WEST_2)
        .build()) {
    CreateProjectResponse resp = client.createProject(
        CreateProjectRequest.builder().name("MyProjectName").build());
    System.out.println(resp.project());
    // Response will be something like:
    // Project{name=MyProjectName, arn=arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-..., created=...}
}
```

Then, do the following to create your upload and push it to Device Farm. In this example, we'll be creating an Android app upload using a local APK file. For more upload type information, including details about iOS app upload types, please see our API documentation for creating an [`Upload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html).

```
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.Instant;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.CreateUploadRequest;
import software.amazon.awssdk.services.devicefarm.model.CreateUploadResponse;
import software.amazon.awssdk.services.devicefarm.model.GetUploadRequest;
import software.amazon.awssdk.services.devicefarm.model.GetUploadResponse;
import software.amazon.awssdk.services.devicefarm.model.Upload;
import software.amazon.awssdk.services.devicefarm.model.UploadType;

public class DeviceFarmUploader {

    public static String upload(String projectArn, Path appPath) throws Exception {
        if (projectArn == null || projectArn.isEmpty()) {
            throw new IllegalArgumentException("Missing projectArn");
        }
        if (!Files.isRegularFile(appPath)) {
            throw new IllegalArgumentException("Invalid app path: " + appPath);
        }

        String fileName = appPath.getFileName().toString().trim();
        UploadType type = UploadType.ANDROID_APP;

        // Build a reusable HttpClient
        HttpClient http = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_1_1)
                .connectTimeout(Duration.ofSeconds(10))
                .build();

        try (DeviceFarmClient client = DeviceFarmClient.builder()
                .region(Region.US_WEST_2)
                .build()) {

            // 1) Create the upload in Device Farm
            CreateUploadResponse create = client.createUpload(CreateUploadRequest.builder()
                    .projectArn(projectArn)
                    .name(fileName)
                    .type(type)
                    .contentType("application/octet-stream")
                    .build());

            Upload upload = create.upload();
            String uploadArn = upload.arn();
            String url = upload.url();
            // This will show output such as the following:
            // { "upload": { "arn": "...", "name": "my_sample_app.apk", "type": "ANDROID_APP", "status": "INITIALIZED", "url": "https://..." } }

            // 2) PUT file to pre-signed URL using HttpClient
            HttpRequest put = HttpRequest.newBuilder(URI.create(url))
                    .timeout(Duration.ofMinutes(15))
                    .header("Content-Type", "application/octet-stream")
                    .PUT(HttpRequest.BodyPublishers.ofFile(appPath))
                    .build();

            HttpResponse<Void> resp = http.send(put, HttpResponse.BodyHandlers.discarding());
            int code = resp.statusCode();
            if (code / 100 != 2) {
                throw new IOException("Failed PUT to S3 pre-signed URL, HTTP " + code);
            }

            // 3) Wait for the app to be in "SUCCEEDED" status (or fail/timeout)
            Instant deadline = Instant.now().plusSeconds(30); // 30-second timeout
            while (true) {
                GetUploadResponse got = client.getUpload(GetUploadRequest.builder()
                        .arn(uploadArn)
                        .build());

                String status = got.upload().statusAsString();
                String msg = got.upload().metadata();
                System.out.println("status=" + status + (msg != null ? " - " + msg : ""));

                if ("SUCCEEDED".equals(status)) return uploadArn;
                if ("FAILED".equals(status)) throw new RuntimeException("Upload failed: " + msg);
                if (Instant.now().isAfter(deadline)) {
                    throw new RuntimeException("Timeout waiting for processing, last status=" + status);
                }
                Thread.sleep(2000);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        String projectArn = "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE";
        Path appPath = Paths.get("/local/path/to/my_sample_app.apk");
        String result = upload(projectArn, appPath);
        System.out.println("Upload ARN: " + result);
    }
}
```

------
#### [ JavaScript ]

*Note: this example uses AWS SDK for JavaScript (v3) and Node 18\+ `fetch` to push the app to Device Farm.*

First, create a project if you haven't already done so.

```
import { DeviceFarmClient, CreateProjectCommand } from "@aws-sdk/client-device-farm";

const df = new DeviceFarmClient({ region: "us-west-2" });
const resp = await df.send(new CreateProjectCommand({ name: "MyProjectName" }));
console.log(resp);
// Response will be something like:
// { project: { name: 'MyProjectName', arn: 'arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-...', created: 1535675814.414 } }
```

Then, do the following to create your upload and push it to Device Farm. In this example, we'll be creating an Android app upload using a local APK file. For more upload type information, including details about iOS app upload types, please see our API documentation for creating an [`Upload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html).

```
import { DeviceFarmClient, CreateUploadCommand, GetUploadCommand } from "@aws-sdk/client-device-farm";
import { createReadStream } from "fs";
import { basename } from "path";

const projectArn = "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE";
const appPath = "/local/path/to/my_sample_app.apk";
const name = basename(appPath).trim();
const type = "ANDROID_APP";

const client = new DeviceFarmClient({ region: "us-west-2" });

// 1) Create the upload in Device Farm
const create = await client.send(new CreateUploadCommand({
  projectArn,
  name,
  type,
  contentType: "application/octet-stream",
}));

const uploadArn = create.upload.arn;
const url = create.upload.url;
// This will show output such as the following:
// { upload: { arn: '...', name: 'my_sample_app.apk', type: 'ANDROID_APP', status: 'INITIALIZED', url: 'https://...' } }

// 2) PUT to pre-signed URL
const putResp = await fetch(url, {
  method: "PUT",
  headers: { "Content-Type": "application/octet-stream" },
  body: createReadStream(appPath),
});
if (!putResp.ok) {
  throw new Error(`Failed PUT to pre-signed URL: ${putResp.status} ${await putResp.text().catch(()=>"")}`);
}

// 3) Wait for the app to be in "SUCCEEDED" status (or fail/timeout)
const deadline = Date.now() + (30 * 1000); // 30-second timeout
while (true) {
  const response = await client.send(new GetUploadCommand({ arn: uploadArn }));
  const { status, message, metadata } = response.upload;
  console.log(`status=${status}${message ? " - " + message : metadata ? " - " + metadata : ""}`);
  if (status === "SUCCEEDED") {
    console.log("Upload complete:", uploadArn);
    break;
  }
  if (status === "FAILED") {
    throw new Error(`Upload failed: ${message || metadata || "unknown"}`);
  }
  if (Date.now() > deadline) throw new Error(`Timeout waiting for processing (last status=${status})`);
  await new Promise(r => setTimeout(r, 2000));
}
```

------
#### [ C\# ]

*Note: this example uses the AWS SDK for .NET and `HttpClient` to push the app to Device Farm.*

First, create a project if you haven't already done so.

```
using System;
using Amazon;
using Amazon.DeviceFarm;
using Amazon.DeviceFarm.Model;

using var client = new AmazonDeviceFarmClient(RegionEndpoint.USWest2);
var resp = await client.CreateProjectAsync(new CreateProjectRequest { Name = "MyProjectName" });
Console.WriteLine(resp.Project);
// Response will be something like:
// { Name = MyProjectName, Arn = arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-..., Created = ... }
```

Then, do the following to create your upload and push it to Device Farm. In this example, we'll be creating an Android app upload using a local APK file. For more upload type information, including details about iOS app upload types, please see our API documentation for creating an [`Upload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html).

```
using System;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;
using System.Net.Http.Headers;
using Amazon;
using Amazon.DeviceFarm;
using Amazon.DeviceFarm.Model;

class DeviceFarmUploader
{
    public static async Task<string> UploadAsync(string projectArn, string appPath)
    {
        if (string.IsNullOrWhiteSpace(projectArn)) throw new ArgumentException("Missing projectArn");
        if (!File.Exists(appPath)) throw new ArgumentException($"Invalid app path: {appPath}");
        var type = UploadType.ANDROID_APP;

        using var client = new AmazonDeviceFarmClient(RegionEndpoint.USWest2);
        // 1) Create the upload in Device Farm
        var create = await client.CreateUploadAsync(new CreateUploadRequest
        {
            ProjectArn = projectArn,
            Name = Path.GetFileName(appPath),
            Type = type,
            ContentType = "application/octet-stream"
        });

        var uploadArn = create.Upload.Arn;
        var url = create.Upload.Url;
        // This will show output such as the following:
        // { Upload: { Arn = ..., Name = my_sample_app.apk, Type = ANDROID_APP, Status = INITIALIZED, Url = https://... } }

        // 2) PUT file to pre-signed URL
        using (var http = new HttpClient())
        using (var fs = File.OpenRead(appPath))
        using (var content = new StreamContent(fs))
        {
            content.Headers.Add("Content-Type", "application/octet-stream");
            var resp = await http.PutAsync(url, content);
            if (!resp.IsSuccessStatusCode)
                throw new Exception($"Failed PUT to pre-signed URL: {(int)resp.StatusCode} {await resp.Content.ReadAsStringAsync()}");
        }

        // 3) Wait for the app to be in "SUCCEEDED" status (or fail/timeout)
        var deadline = DateTime.UtcNow.AddSeconds(30); // 30-second timeout
        while (true)
        {
            var got = await client.GetUploadAsync(new GetUploadRequest { Arn = uploadArn });
            var status = got.Upload.Status.Value;
            var msg = got.Upload.Message ?? got.Upload.Metadata;
            Console.WriteLine($"status={status}{(string.IsNullOrEmpty(msg) ? "" : " - " + msg)}");

            if (status == UploadStatus.SUCCEEDED.Value) return uploadArn;
            if (status == UploadStatus.FAILED.Value) throw new Exception($"Upload failed: {msg}");
            if (DateTime.UtcNow > deadline) throw new TimeoutException($"Timeout waiting for processing (last status={status})");
            await Task.Delay(2000);
        }
    }

    static async Task Main()
    {
        var projectArn = "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE";
        var appPath = "/local/path/to/my_sample_app.apk";
        var result = await UploadAsync(projectArn!, appPath!);
        Console.WriteLine("Upload ARN: " + result);
    }
}
```

------
#### [ Ruby ]

*Note: this example uses the AWS SDK for Ruby and `Net::HTTP` to push the app to Device Farm.*

First, create a project if you haven't already done so.

```
require "aws-sdk-devicefarm"

client = Aws::DeviceFarm::Client.new(region: "us-west-2")
resp = client.create_project(name: "MyProjectName")
puts resp.project.inspect
# Response will be something like:
# #<struct Aws::DeviceFarm::Types::Project name="MyProjectName", arn="arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-...", created=1535675814.414>
```

Then, do the following to create your upload and push it to Device Farm. In this example, we'll be creating an Android app upload using a local APK file. For more upload type information, including details about iOS app upload types, please see our API documentation for creating an [`Upload`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html).

```
require "aws-sdk-devicefarm"
require "net/http"
require "uri"

project_arn = "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
app_path    = "/local/path/to/my_sample_app.apk"
raise "Invalid APP_PATH: #{app_path}" unless File.file?(app_path)
type = "ANDROID_APP"

client = Aws::DeviceFarm::Client.new(region: "us-west-2")

# 1) Create the upload in Device Farm
create = client.create_upload(
  project_arn: project_arn,
  name: File.basename(app_path),
  type: type,
  content_type: "application/octet-stream"
)

upload_arn = create.upload.arn
url = create.upload.url
# This will show output such as the following:
# #<Upload arn="...", name="my_sample_app.apk", type="ANDROID_APP", status="INITIALIZED", url="https://...">

# 2) PUT the file to the pre-signed URL
uri = URI.parse(url)
Net::HTTP.start(uri.host, uri.port, use_ssl: (uri.scheme == "https")) do |http|
  req = Net::HTTP::Put.new(uri)
  req["Content-Type"] = "application/octet-stream"
  req.body_stream = File.open(app_path, "rb")
  req.content_length = File.size(app_path)
  resp = http.request(req)
  raise "Failed PUT: #{resp.code} #{resp.body}" unless resp.code.to_i / 100 == 2
end

# 3) Wait for the app to be in "SUCCEEDED" status (or fail/timeout)
deadline = Time.now + 30 # 30-second timeout
loop do
  got = client.get_upload(arn: upload_arn)
  status = got.upload.status
  msg = got.upload.message || got.upload.metadata
  puts "status=#{status}#{msg ? " - #{msg}" : ""}"

  case status
  when "SUCCEEDED" then puts "Upload complete: #{upload_arn}"; break
  when "FAILED"    then raise "Upload failed: #{msg}"
  end
  raise "Timeout waiting for processing (last status=#{status})" if Time.now > deadline
  sleep 2
end
```

------

## Example: Using the AWS SDK to start a Device Farm run and collect artifacts
<a name="automation-example"></a>

 The following example provides a beginning-to-end demonstration of how you can use the AWS SDK to work with Device Farm. This example does the following: 
+ Uploads a test and application packages to Device Farm
+ Starts a test run and waits for its completion (or failure)
+ Downloads all artifacts produced by the test suites

This example depends on the third-party `requests` package to interact with HTTP.

```
import boto3
import os
import requests
import string
import random
import time
import datetime
import time
import json

# The following script runs a test through Device Farm
#
# Things you have to change:
config = {
    # This is our app under test.
    "appFilePath":"app-debug.apk",
    "projectArn": "arn:aws:devicefarm:us-west-2:111122223333:project:1b99bcff-1111-2222-ab2f-8c3c733c55ed",
    # Since we care about the most popular devices, we'll use a curated pool.
    "testSpecArn":"arn:aws:devicefarm:us-west-2::upload:101e31e8-12ac-11e9-ab14-d663bd873e83",
    "poolArn":"arn:aws:devicefarm:us-west-2::devicepool:082d10e5-d7d7-48a5-ba5c-b33d66efa1f5",
    "namePrefix":"MyAppTest",
    # This is our test package. This tutorial won't go into how to make these. 
    "testPackage":"tests.zip"
}

client = boto3.client('devicefarm')

unique = config['namePrefix']+"-"+(datetime.date.today().isoformat())+(''.join(random.sample(string.ascii_letters,8)))

print(f"The unique identifier for this run is going to be {unique} -- all uploads will be prefixed with this.")

def upload_df_file(filename, type_, mime='application/octet-stream'):
    response = client.create_upload(projectArn=config['projectArn'],
        name = (unique)+"_"+os.path.basename(filename),
        type=type_,
        contentType=mime
        )
    # Get the upload ARN, which we'll return later.
    upload_arn = response['upload']['arn']
    # We're going to extract the URL of the upload and use Requests to upload it 
    upload_url = response['upload']['url']
    with open(filename, 'rb') as file_stream:
        print(f"Uploading {filename} to Device Farm as {response['upload']['name']}... ",end='')
        put_req = requests.put(upload_url, data=file_stream, headers={"content-type":mime})
        print(' done')
        if not put_req.ok:
            raise Exception("Couldn't upload, requests said we're not ok. Requests says: "+put_req.reason)
    started = datetime.datetime.now()
    while True:
        print(f"Upload of {filename} in state {response['upload']['status']} after "+str(datetime.datetime.now() - started))
        if response['upload']['status'] == 'FAILED':
            raise Exception("The upload failed processing. DeviceFarm says reason is: \n"+(response['upload']['message'] if 'message' in response['upload'] else response['upload']['metadata']))
        if response['upload']['status'] == 'SUCCEEDED':
            break
        time.sleep(5)
        response = client.get_upload(arn=upload_arn)
    print("")
    return upload_arn

our_upload_arn = upload_df_file(config['appFilePath'], "ANDROID_APP")
our_test_package_arn = upload_df_file(config['testPackage'], 'APPIUM_PYTHON_TEST_PACKAGE')
print(our_upload_arn, our_test_package_arn)
# Now that we have those out of the way, we can start the test run...
response = client.schedule_run(
    projectArn = config["projectArn"],
    appArn = our_upload_arn,
    devicePoolArn = config["poolArn"],
    name=unique,
    test = {
        "type":"APPIUM_PYTHON",
        "testSpecArn": config["testSpecArn"],
        "testPackageArn": our_test_package_arn
        }
    )
run_arn = response['run']['arn']
start_time = datetime.datetime.now()
print(f"Run {unique} is scheduled as arn {run_arn} ")

try:

    while True:
        response = client.get_run(arn=run_arn)
        state = response['run']['status']
        if state == 'COMPLETED' or state == 'ERRORED':
            break
        else:
            print(f" Run {unique} in state {state}, total time "+str(datetime.datetime.now()-start_time))
            time.sleep(10)
except:
    # If something goes wrong in this process, we stop the run and exit. 

    client.stop_run(arn=run_arn)
    exit(1)
print(f"Tests finished in state {state} after "+str(datetime.datetime.now() - start_time))
# now, we pull all the logs.
jobs_response = client.list_jobs(arn=run_arn)
# Save the output somewhere. We're using the unique value, but you could use something else
save_path = os.path.join(os.getcwd(), unique)
os.mkdir(save_path)
# Save the last run information
for job in jobs_response['jobs'] :
    # Make a directory for our information
    job_name = job['name']
    os.makedirs(os.path.join(save_path, job_name), exist_ok=True)
    # Get each suite within the job
    suites = client.list_suites(arn=job['arn'])['suites']
    for suite in suites:
        for test in client.list_tests(arn=suite['arn'])['tests']:
            # Get the artifacts
            for artifact_type in ['FILE','SCREENSHOT','LOG']:
                artifacts = client.list_artifacts(
                    type=artifact_type,
                    arn = test['arn']
                )['artifacts']
                for artifact in artifacts:
                    # We replace : because it has a special meaning in Windows & macos
                    path_to = os.path.join(save_path, job_name, suite['name'], test['name'].replace(':','_') )
                    os.makedirs(path_to, exist_ok=True)
                    filename = artifact['type']+"_"+artifact['name']+"."+artifact['extension']
                    artifact_save_path = os.path.join(path_to, filename)
                    print("Downloading "+artifact_save_path)
                    with open(artifact_save_path, 'wb') as fn, requests.get(artifact['url'],allow_redirects=True) as request:
                        fn.write(request.content)
                    #/for artifact in artifacts
                #/for artifact type in []
            #/ for test in ()[]
        #/ for suite in suites
    #/ for job in _[]
# done
print("Finished")
```

# Troubleshooting Device Farm errors
<a name="troubleshooting"></a>

In this section, you will find error messages and procedures to help you fix common problems with Device Farm.

**Note**  
To troubleshoot Appium tests that unexpectedly fail on Device Farm, please see our guide for [client-side Appium testing](#appium-endpoint)

**Topics**
+ [Troubleshooting Android application tests in AWS Device Farm](#troubleshooting-android-applications)
+ [Troubleshooting Appium Java JUnit tests in AWS Device Farm](#troubleshooting-appium-java-junit)
+ [Troubleshooting Appium Java JUnit web application tests in AWS Device Farm](#troubleshooting-appium-web-java-junit-tests)
+ [Troubleshooting Appium Java TestNG tests in AWS Device Farm](#troubleshooting-appium-java-testng)
+ [Troubleshooting Appium Java TestNG web applications in AWS Device Farm](#troubleshooting-appium-web-java-testng)
+ [Troubleshooting Appium Python tests in AWS Device Farm](#troubleshooting-appium-python)
+ [Troubleshooting Appium Python web application tests in AWS Device Farm](#troubleshooting-appium-web-python)
+ [Troubleshooting instrumentation tests in AWS Device Farm](#troubleshooting-instrumentation-tests)
+ [Troubleshooting iOS application tests in AWS Device Farm](#troubleshooting-ios-applications)
+ [Troubleshooting XCTest tests in AWS Device Farm](#troubleshooting-xctest)
+ [Troubleshooting XCTest UI tests in AWS Device Farm](#troubleshooting-xctest-ui)

## Troubleshooting Android application tests in AWS Device Farm
<a name="troubleshooting-android-applications"></a>

The following topic lists error messages that occur during the upload of Android application tests and recommends workarounds to resolve each error.

### ANDROID\_APP\_UNZIP\_FAILED
<a name="ANDROID_APP_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your application. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's name is **app-debug.apk**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip app-debug.apk
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Android application package should produce output like the following:

   ```
   .
   |-- AndroidManifest.xml
   |-- classes.dex
   |-- resources.arsc
   |-- assets (directory)
   |-- res (directory)
   `-- META-INF (directory)
   ```

   For more information, see [Android tests in AWS Device Farm](#test-types-android-tests).

### ANDROID\_APP\_AAPT\_DEBUG\_BADGING\_FAILED
<a name="ANDROID_APP_AAPT_DEBUG_BADGING_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not extract information about your application. Please verify that the application is valid by running the command `aapt debug badging {{<path to your test package>}}`, and try again after the command does not print any error. 

During the upload validation process, AWS Device Farm parses out information from the output of an `aapt debug badging {{<path to your package>}}` command. 

Make sure that you can run this command on your Android application successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the command:

  ```
  $ aapt debug badging app-debug.apk
  ```

  A valid Android application package should produce output like the following:

  ```
  package: name='com.amazon.aws.adf.android.referenceapp' versionCode='1' versionName='1.0' platformBuildVersionName='5.1.1-1819727'
  sdkVersion:'9'
  application-label:'ReferenceApp'
  application: label='ReferenceApp' icon='res/mipmap-mdpi-v4/ic_launcher.png'
  application-debuggable
  launchable-activity: name='com.amazon.aws.adf.android.referenceapp.Activities.MainActivity'  label='ReferenceApp' icon=''
  uses-feature: name='android.hardware.bluetooth'
  uses-implied-feature: name='android.hardware.bluetooth' reason='requested android.permission.BLUETOOTH permission, and targetSdkVersion > 4'
  main
  supports-screens: 'small' 'normal' 'large' 'xlarge'
  supports-any-density: 'true'
  locales: '--_--'
  densities: '160' '213' '240' '320' '480' '640'
  ```

  For more information, see [Android tests in AWS Device Farm](#test-types-android-tests).

### ANDROID\_APP\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="ANDROID_APP_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the package name value in your application. Please verify that the application is valid by running the command `aapt debug badging {{<path to your test package>}}`, and try again after finding the package name value behind the keyword "package: name."

During the upload validation process, AWS Device Farm parses out the package name value from the output of an `aapt debug badging {{<path to your package>}}` command.

Make sure that you can run this command on your Android application and find the package name value successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

  ```
  $ aapt debug badging app-debug.apk | grep "package: name="
  ```

  A valid Android application package should produce output like the following:

  ```
  package: name='com.amazon.aws.adf.android.referenceapp' versionCode='1' versionName='1.0' platformBuildVersionName='5.1.1-1819727'
  ```

  For more information, see [Android tests in AWS Device Farm](#test-types-android-tests).

### ANDROID\_APP\_SDK\_VERSION\_VALUE\_MISSING
<a name="ANDROID_APP_SDK_VERSION_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the SDK version value in your application. Please verify that the application is valid by running the command `aapt debug badging {{<path to your test package>}}`, and try again after finding the SDK version value behind the keyword `sdkVersion`.

During the upload validation process, AWS Device Farm parses out the SDK version value from the output of an `aapt debug badging {{<path to your package>}}` command.

Make sure that you can run this command on your Android application and find the package name value successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

  ```
  $ aapt debug badging app-debug.apk | grep "sdkVersion"
  ```

  A valid Android application package should produce output like the following:

  ```
  sdkVersion:'9'
  ```

  For more information, see [Android tests in AWS Device Farm](#test-types-android-tests).

### ANDROID\_APP\_AAPT\_DUMP\_XMLTREE\_FAILED
<a name="ANDROID_APP_AAPT_DUMP_XMLTREE_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the valid AndroidManifest.xml in your application. Please verify that the test package is valid by running the command `aapt dump xmltree {{<path to your test package>}} AndroidManifest.xml`, and try again after the command does not print any error.

During the upload validation process, AWS Device Farm parses out information from the XML parse tree for an XML file contained within the package using the command `aapt dump xmltree {{<path to your package>}} AndroidManifest.xml`.

Make sure that you can run this command on your Android application successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

  ```
  $ aapt dump xmltree app-debug.apk. AndroidManifest.xml
  ```

  A valid Android application package should produce output like the following:

  ```
  N: android=http://schemas.android.com/apk/res/android
    E: manifest (line=2)
      A: android:versionCode(0x0101021b)=(type 0x10)0x1
      A: android:versionName(0x0101021c)="1.0" (Raw: "1.0")
      A: package="com.amazon.aws.adf.android.referenceapp" (Raw: "com.amazon.aws.adf.android.referenceapp")
      A: platformBuildVersionCode=(type 0x10)0x16 (Raw: "22")
      A: platformBuildVersionName="5.1.1-1819727" (Raw: "5.1.1-1819727")
      E: uses-sdk (line=7)
        A: android:minSdkVersion(0x0101020c)=(type 0x10)0x9
        A: android:targetSdkVersion(0x01010270)=(type 0x10)0x16
      E: uses-permission (line=11)
        A: android:name(0x01010003)="android.permission.INTERNET" (Raw: "android.permission.INTERNET")
      E: uses-permission (line=12)
        A: android:name(0x01010003)="android.permission.CAMERA" (Raw: "android.permission.CAMERA")
  ```

  For more information, see [Android tests in AWS Device Farm](#test-types-android-tests).

### ANDROID\_APP\_DEVICE\_ADMIN\_PERMISSIONS
<a name="ANDROID_APP_DEVICE_ADMIN_PERMISSIONS"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found that your application requires device admin permissions. Please verify that the permissions are not required by run the command `aapt dump xmltree {{<path to your test package>}} AndroidManifest.xml`, and try again after making sure that output does not contain the keyword `android.permission.BIND_DEVICE_ADMIN`.

During the upload validation process, AWS Device Farm parses out permission information from the xml parse tree for an xml file contained within the package using the command `aapt dump xmltree {{<path to your package>}} AndroidManifest.xml`.

Make sure that your application does not require device admin permission. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

  ```
  $ aapt dump xmltree app-debug.apk AndroidManifest.xml
  ```

  You should find output like the following:

  ```
  N: android=http://schemas.android.com/apk/res/android
    E: manifest (line=2)
      A: android:versionCode(0x0101021b)=(type 0x10)0x1
      A: android:versionName(0x0101021c)="1.0" (Raw: "1.0")
      A: package="com.amazonaws.devicefarm.android.referenceapp" (Raw: "com.amazonaws.devicefarm.android.referenceapp")
      A: platformBuildVersionCode=(type 0x10)0x16 (Raw: "22")
      A: platformBuildVersionName="5.1.1-1819727" (Raw: "5.1.1-1819727")
      E: uses-sdk (line=7)
        A: android:minSdkVersion(0x0101020c)=(type 0x10)0xa
        A: android:targetSdkVersion(0x01010270)=(type 0x10)0x16
      E: uses-permission (line=11)
        A: android:name(0x01010003)="android.permission.INTERNET" (Raw: "android.permission.INTERNET")
      E: uses-permission (line=12)
        A: android:name(0x01010003)="android.permission.CAMERA" (Raw: "android.permission.CAMERA")
          ……
  ```

  If the Android application is valid, the output should not contain the following: `A: android:name(0x01010003)="android.permission.BIND_DEVICE_ADMIN" (Raw: "android.permission.BIND_DEVICE_ADMIN")`. 

  For more information, see [Android tests in AWS Device Farm](#test-types-android-tests).

### Certain windows in my Android application show a blank or black screen
<a name="flag-secure-screen-issue"></a>

If you are testing an Android application and notice that certain windows in the application appear with a black screen in Device Farm's video recording of your test, your application may be using Android's `FLAG_SECURE` feature. This flag (as described in [Android's official documentation](https://developer.android.com/reference/android/view/WindowManager.LayoutParams.html#FLAG_SECURE)) is used to prevent certain windows of an application from being recorded by screen recording tools. As a result, Device Farm's screen recording feature (for both automation and remote access testing) may show a black screen in place of your application's window if the window uses this flag. 

This flag is often used by developers for pages in their application that contain sensitive information such as login pages. If you are seeing a black screen in place of your application's screen for certain pages like its login page, work with your developer(s) to obtain a build of the application that doesn't use this flag for testing.

Additionally, note that Device Farm can still interact with application windows that have this flag. So, if your application's login page appears as a black screen, you may still be able to enter your credentials in order to log in to the application (and thus view pages not blocked by the `FLAG_SECURE` flag).

## Troubleshooting Appium Java JUnit tests in AWS Device Farm
<a name="troubleshooting-appium-java-junit"></a>

The following topic lists error messages that occur during the upload of Appium Java JUnit tests and recommends workarounds to resolve each error.

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the dependency-jars directory inside your test package. Please unzip your test package, verify that the dependency-jars directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. After you successfully extract the files, you should find at least one class in the working directory tree by running the command: 

   ```
   $ tree .
   ```

   You should see output like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `-{{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_JUNIT\_VERSION\_VALUE\_UNKNOWN
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_JUNIT_VERSION_VALUE_UNKNOWN"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JUnit version value. Please unzip your test package and open the dependency-jars directory, verify that the JUnit JAR file is inside the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working-directory tree structure by running the following command:

   ```
   tree .
   ```

   The output should look like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
       |— {{junit-4.10.jar}}
       |— com.some-dependency.bar-4.1.jar
       |— com.another-dependency.thing-1.0.jar
       |— joda-time-2.7.jar
       `— log4j-1.2.14.jar
   ```

   If the Appium Java JUnit package is valid, you will find the JUnit dependency file that is similar to the jar file {{junit-4.10.jar}} in our example. The name should consist of the keyword {{junit}} and its version number, which in this example is 4.10.

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_INVALID\_JUNIT\_VERSION
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_INVALID_JUNIT_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the JUnit version was lower than the minimum version 4.10 we support. Please change the JUnit version and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find a JUnit dependency file like {{junit-4.10.jar}} in our example and its version number, which in our example is 4.10:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{junit-4.10.jar}}
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```
**Note**  
Your tests may not execute correctly if the JUnit version specified in your test package is lower than the minimum version 4.10 we support.

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

## Troubleshooting Appium Java JUnit web application tests in AWS Device Farm
<a name="troubleshooting-appium-web-java-junit-tests"></a>

The following topic lists error messages that occur during the upload of Appium Java JUnit Web application tests and recommends workarounds to resolve each error. For more information on using Appium with Device Farm, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the dependency-jars directory inside your test package. Please unzip your test package, verify that the dependency-jars directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. After you successfully extract the files, you should find at least one class in the working directory tree by running the command: 

   ```
   $ tree .
   ```

   You should see output like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `-{{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_JUNIT\_VERSION\_VALUE\_UNKNOWN
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_JUNIT_VERSION_VALUE_UNKNOWN"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JUnit version value. Please unzip your test package and open the dependency-jars directory, verify that the JUnit JAR file is inside the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working-directory tree structure by running the following command:

   ```
   tree .
   ```

   The output should look like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{junit-4.10.jar}}
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   If the Appium Java JUnit package is valid, you will find the JUnit dependency file that is similar to the jar file {{junit-4.10.jar}} in our example. The name should consist of the keyword {{junit}} and its version number, which in this example is 4.10.

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_INVALID\_JUNIT\_VERSION
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_INVALID_JUNIT_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the JUnit version was lower than the minimum version 4.10 we support. Please change the JUnit version and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find a JUnit dependency file like {{junit-4.10.jar}} in our example and its version number, which in our example is 4.10:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{junit-4.10.jar}}
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```
**Note**  
Your tests may not execute correctly if the JUnit version specified in your test package is lower than the minimum version 4.10 we support.

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

## Troubleshooting Appium Java TestNG tests in AWS Device Farm
<a name="troubleshooting-appium-java-testng"></a>

The following topic lists error messages that occur during the upload of Appium Java TestNG tests and recommends workarounds to resolve each error.

### Upload errors
<a name="troubleshooting-appium-java-testng-upload"></a>

The following errors can occur when you upload your Appium Java TestNG tests.

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the `dependency-jars` directory inside your test package. Please unzip your test package, verify that the `dependency-jars` directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory. 

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. To extract files from the jar file, you can run the following command: 

   ```
   $ jar xf acme-android-appium-1.0-SNAPSHOT-tests.jar
   ```

1. After you successfully extract the files, run the following command:

   ```
   $ tree .
   ```

   You should find at least one class in the working directory tree:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `— {{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### Test insights
<a name="troubleshooting-appium-java-testng-insights"></a>

When you opt in to test insights, Device Farm generates a summarized report for your run and each job under it. If the service cannot generate the report, the insights report status is `SKIPPED` or `ERRORED`, and the report message explains why. The following messages can occur when generating insights for Appium Java TestNG tests.

#### The job did not run to completion
<a name="ti-appium-java-testng-job-not-complete"></a>

`Unable to generate test insights because the job was {{status}}.`

The job ended in a non-successful state (where {{status}} is `STOPPED`, `ERRORED`, or `SKIPPED`), so there was no result to summarize. A run that ends in a failed state still receives insights.

To resolve this issue, investigate why the job did not run to completion. In many cases, the `message` field of the job itself might explain why the job didn't complete.

#### The results contained no test cases
<a name="ti-appium-java-testng-no-test-cases"></a>

`Test insights could not be generated. The testng-results.xml file was parsed successfully but contained no test cases.`

The results artifact parsed successfully but contained zero test cases.

To resolve this issue, verify that your test suite includes at least one test case and that results are stored correctly under `$DEVICEFARM_LOG_DIR`.

#### The test output exceeds the maximum supported size
<a name="ti-appium-java-testng-output-too-large"></a>

`Unable to generate test insights: test output "testng-results.xml" exceeds the maximum supported size of 1GB.`

The testng-results.xml is larger than 1 GB.

To resolve this issue, reduce the testng-results.xml size to below 1 GB by trimming logs or attachments.

#### The testng-results.xml file was not found
<a name="ti-appium-java-testng-testng-xml-not-found"></a>

`Unable to generate test insights. The test results file (testng-results.xml) was not found.`

No `testng-results.xml` file (and no XML entry with the TestNG root signature) was found.

To resolve this issue, configure your framework to emit TestNG XML into the artifacts directory (`$DEVICEFARM_LOG_DIR`).

#### The testng-results.xml file could not be processed
<a name="ti-appium-java-testng-testng-xml-error"></a>

`Test insights could not be generated because of an error while processing testng-results.xml.`

The XML file was malformed or could not be parsed.

To resolve this issue, ensure that the file is a well-formed XML in the standard TestNG report format.

## Troubleshooting Appium Java TestNG web applications in AWS Device Farm
<a name="troubleshooting-appium-web-java-testng"></a>

The following topic lists error messages that occur during the upload of Appium Java TestNG Web application tests and recommends workarounds to resolve each error.

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the dependency-jars directory inside your test package. Please unzip your test package, verify that the dependency-jars directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory. 

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. To extract files from the jar file, you can run the following command: 

   ```
   $ jar xf acme-android-appium-1.0-SNAPSHOT-tests.jar
   ```

1. After you successfully extract the files, run the following command:

   ```
   $ tree .
   ```

   You should find at least one class in the working directory tree:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `— {{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium).

## Troubleshooting Appium Python tests in AWS Device Farm
<a name="troubleshooting-appium-python"></a>

The following topic lists error messages that occur during the upload of Appium Python tests and recommends workarounds to resolve each error.

### APPIUM\_PYTHON\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your Appium test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Python package should produce output like the following:

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEEL\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEEL_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a dependency wheel file in the wheelhouse directory tree. Please unzip your test package and then open the wheelhouse directory, verify that at least one wheel file is in the directory, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_PLATFORM
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_PLATFORM"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found at least one wheel file specified a platform that we do not support. Please unzip your test package and then open the wheelhouse directory, verify that names of wheel files end with -any.whl or -linux\_x86\_64.whl, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory. The file's name may be different, but it should end with {{-any.whl}} or {{-linux\_x86\_64.whl}}, which specifies the platform. Any other platforms like `windows` are not supported.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_TEST\_DIR\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_TEST_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the tests directory inside your test package. Please unzip your test package, verify that the tests directory is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- {{tests}} (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_TEST\_FILE\_NAME
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_TEST_FILE_NAME"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a valid test file in the tests directory tree. Please unzip your test package and then open the tests directory, verify that at least one file's name starts or ends with the keyword "test", and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory. The file's name may be different, but it should start with {{test\_}} or end with {{\_test.py}}.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- {{test_unittest.py}}
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_REQUIREMENTS\_TXT\_FILE\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_REQUIREMENTS_TXT_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the requirements.txt file inside your test package. Please unzip your test package, verify that the requirements.txt file is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_PYTEST\_VERSION
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_PYTEST_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the pytest version was lower than the minimum version 2.8.0 we support. Please change the pytest version inside the requirements.txt file, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `--test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

1. To get the pytest version, you can run the following command:

   ```
   $ grep "pytest" requirements.txt
   ```

   You should find output like the following:

   ```
   pytest==2.9.0
   ```

   It shows the pytest version, which in this example is 2.9.0. If the Appium Python package is valid, the pytest version should be larger than or equal to 2.8.0. 

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INSTALL\_DEPENDENCY\_WHEELS\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_INSTALL_DEPENDENCY_WHEELS_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to install the dependency wheels. Please unzip your test package and then open the requirements.txt file and the wheelhouse directory, verify that the dependency wheels specified in the requirements.txt file exactly match the dependency wheels inside the wheelhouse directory, and try again.

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To test installing wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

   A valid Appium Python package should produce output like the following:

   ```
   Ignoring indexes: https://pypi.python.org/simple
   Collecting Appium-Python-Client==0.20 (from -r ./requirements.txt (line 1))
   Collecting py==1.4.31 (from -r ./requirements.txt (line 2))
   Collecting pytest==2.9.0 (from -r ./requirements.txt (line 3))
   Collecting selenium==2.52.0 (from -r ./requirements.txt (line 4))
   Collecting wheel==0.26.0 (from -r ./requirements.txt (line 5))
   Installing collected packages: selenium, Appium-Python-Client, py, pytest, wheel
     Found existing installation: wheel 0.29.0
       Uninstalling wheel-0.29.0:
         Successfully uninstalled wheel-0.29.0
   Successfully installed Appium-Python-Client-0.20 py-1.4.31 pytest-2.9.0 selenium-2.52.0 wheel-0.26.0
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_PYTEST\_COLLECT\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_PYTEST_COLLECT_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to collect tests in the tests directory. Please unzip your test package, very that the test package is valid by running the command `py.test --collect-only <path to your tests directory>`, and try again after the command does not print any error. 

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To install wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

1. To collect tests, you can run the following command:

   ```
   $ py.test --collect-only tests
   ```

   A valid Appium Python package should produce output like the following:

   ```
   ==================== test session starts ====================
   platform darwin -- Python 2.7.11, pytest-2.9.0, py-1.4.31, pluggy-0.3.1
   rootdir: /Users/zhena/Desktop/Ios/tests, inifile:
   collected 1 items
   <Module 'test_unittest.py'>
     <UnitTestCase 'DeviceFarmAppiumWebTests'>
       <TestCaseFunction 'test_devicefarm'>
   
   ==================== no tests ran in 0.11 seconds ====================
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEELS\_INSUFFICIENT
<a name="APPIUM_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEELS_INSUFFICIENT"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find enough wheel dependencies in the wheelhouse directory. Please unzip your test package, and then open the wheelhouse directory. Verify that you have all the wheel dependencies specified in the requirements.txt file.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. Check the length of the {{requirements.txt}} file as well as the number of {{.whl}} dependent files in the wheelhouse directory:

   ```
   $ cat requirements.txt | egrep "." |wc -l
   ﻿    12
   $ ls wheelhouse/ | egrep ".+\.whl" | wc -l
       11
   ```

   If the number of {{.whl}} dependent files is less than the number of non-empty rows in your {{requirements.txt}} file, then you need to ensure the following: 
   + There is a {{.whl}} dependent file corresponding to each row in the {{requirements.txt}} file.
   + There are no other lines in the {{requirements.txt}} file that contain information other than the dependency package names.
   + No dependency names are duplicated in multiple lines in the {{requirements.txt}} file such that two lines in the file may correspond to one {{.whl}} dependent file.

   AWS Device Farm doesn't support lines in the {{requirements.txt}} file that don't directly correspond to dependency packages, such as lines that specify global options for the `pip install` command. See [Requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/#global-options) for a list of global options.

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

## Troubleshooting Appium Python web application tests in AWS Device Farm
<a name="troubleshooting-appium-web-python"></a>

The following topic lists error messages that occur during the upload of Appium Python Web application tests and recommends workarounds to resolve each error.

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your Appium test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Python package should produce output like the following:

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEEL\_MISSING
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEEL_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a dependency wheel file in the wheelhouse directory tree. Please unzip your test package and then open the wheelhouse directory, verify that at least one wheel file is in the directory, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INVALID\_PLATFORM
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_PLATFORM"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found at least one wheel file specified a platform that we do not support. Please unzip your test package and then open the wheelhouse directory, verify that names of wheel files end with -any.whl or -linux\_x86\_64.whl, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory. The file's name may be different, but it should end with {{-any.whl}} or {{-linux\_x86\_64.whl}}, which specifies the platform. Any other platforms like `windows` are not supported.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_TEST\_DIR\_MISSING
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_TEST_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the tests directory inside your test package. Please unzip your test package, verify that the tests directory is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- {{tests}} (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INVALID\_TEST\_FILE\_NAME
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_TEST_FILE_NAME"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a valid test file in the tests directory tree. Please unzip your test package and then open the tests directory, verify that at least one file's name starts or ends with the keyword "test", and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory. The file's name may be different, but it should start with {{test\_}} or end with {{\_test.py}}.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- {{test_unittest.py}}
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_REQUIREMENTS\_TXT\_FILE\_MISSING
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_REQUIREMENTS_TXT_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the requirements.txt file inside your test package. Please unzip your test package, verify that the requirements.txt file is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INVALID\_PYTEST\_VERSION
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_PYTEST_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the pytest version was lower than the minimum version 2.8.0 we support. Please change the pytest version inside the requirements.txt file, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{requirement.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `--test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

1. To get the pytest version, you can run the following command:

   ```
   $ grep "pytest" requirements.txt
   ```

   You should find output like the following:

   ```
   pytest==2.9.0
   ```

   It shows the pytest version, which in this example is 2.9.0. If the Appium Python package is valid, the pytest version should be larger than or equal to 2.8.0. 

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INSTALL\_DEPENDENCY\_WHEELS\_FAILED
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INSTALL_DEPENDENCY_WHEELS_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to install the dependency wheels. Please unzip your test package and then open the requirements.txt file and the wheelhouse directory, verify that the dependency wheels specified in the requirements.txt file exactly match the dependency wheels inside the wheelhouse directory, and try again.

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To test installing wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

   A valid Appium Python package should produce output like the following:

   ```
   Ignoring indexes: https://pypi.python.org/simple
   Collecting Appium-Python-Client==0.20 (from -r ./requirements.txt (line 1))
   Collecting py==1.4.31 (from -r ./requirements.txt (line 2))
   Collecting pytest==2.9.0 (from -r ./requirements.txt (line 3))
   Collecting selenium==2.52.0 (from -r ./requirements.txt (line 4))
   Collecting wheel==0.26.0 (from -r ./requirements.txt (line 5))
   Installing collected packages: selenium, Appium-Python-Client, py, pytest, wheel
     Found existing installation: wheel 0.29.0
       Uninstalling wheel-0.29.0:
         Successfully uninstalled wheel-0.29.0
   Successfully installed Appium-Python-Client-0.20 py-1.4.31 pytest-2.9.0 selenium-2.52.0 wheel-0.26.0
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_PYTEST\_COLLECT\_FAILED
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_PYTEST_COLLECT_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to collect tests in the tests directory. Please unzip your test package, very that the test package is valid by running the command "py.test --collect-only <path to your tests directory>", and try again after the command does not print any error. 

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To install wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

1. To collect tests, you can run the following command:

   ```
   $ py.test --collect-only tests
   ```

   A valid Appium Python package should produce output like the following:

   ```
   ==================== test session starts ====================
   platform darwin -- Python 2.7.11, pytest-2.9.0, py-1.4.31, pluggy-0.3.1
   rootdir: /Users/zhena/Desktop/Ios/tests, inifile:
   collected 1 items
   <Module 'test_unittest.py'>
     <UnitTestCase 'DeviceFarmAppiumWebTests'>
       <TestCaseFunction 'test_devicefarm'>
   
   ==================== no tests ran in 0.11 seconds ====================
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](#test-types-appium). 

## Troubleshooting instrumentation tests in AWS Device Farm
<a name="troubleshooting-instrumentation-tests"></a>

The following topic lists error messages that occur during the upload of Instrumentation tests and recommends workarounds to resolve each error.

**Note**  
For important considerations when using Instrumentation tests in AWS Device Farm, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation). 

### Upload errors
<a name="troubleshooting-instrumentation-tests-upload"></a>

The following errors can occur when you upload your Instrumentation tests.

#### INSTRUMENTATION\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="INSTRUMENTATION_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

```
Warning: We could not open your test APK file. Please verify that the file is valid and
    try again.
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip app-debug-androidTest-unaligned.apk
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Instrumentation test package will produce output like the following:

   ```
   .
   |-- AndroidManifest.xml
   |--  classes.dex
   |-- resources.arsc
   |-- LICENSE-junit.txt
   |-- junit (directory)
   `-- META-INF (directory)
   ```

   For more information, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_AAPT\_DEBUG\_BADGING\_FAILED
<a name="INSTRUMENTATION_TEST_PACKAGE_AAPT_DEBUG_BADGING_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not extract information about your test package. Please verify that the
      test package is valid by running the command "aapt debug badging <path to your test
      package>", and try again after the command does not print any error.
```

During the upload validation process, Device Farm parses out information from the output of the `aapt debug badging <path to your package>` command.

Make sure that you can run this command on your Instrumentation test package successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

  ```
  $ aapt debug badging app-debug-androidTest-unaligned.apk
  ```

  A valid Instrumentation test package will produce output like the following:

  ```
  package: name='com.amazon.aws.adf.android.referenceapp.test' versionCode='' versionName='' platformBuildVersionName='5.1.1-1819727'
  sdkVersion:'9'
  targetSdkVersion:'22'
  application-label:'Test-api'
  application: label='Test-api' icon=''
  application-debuggable
  uses-library:'android.test.runner'
  feature-group: label=''
  uses-feature: name='android.hardware.touchscreen'
  uses-implied-feature: name='android.hardware.touchscreen' reason='default feature for all apps'
  supports-screens: 'small' 'normal' 'large' 'xlarge'
  supports-any-density: 'true'
  locales: '--_--'
  densities: '160'
  ```

  For more information, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_INSTRUMENTATION\_RUNNER\_VALUE\_MISSING
<a name="INSTRUMENTATION_TEST_PACKAGE_INSTRUMENTATION_RUNNER_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not find the instrumentation runner value in the AndroidManifest.xml.
      Please verify the test package is valid by running the command "aapt dump xmltree <path to
      your test package> AndroidManifest.xml", and try again after finding the instrumentation
      runner value behind the keyword "instrumentation."
```

During the upload validation process, Device Farm parses out the instrumentation runner value from the XML parse tree for an XML file contained within the package. You can use the following command: `aapt dump xmltree <path to your package> AndroidManifest.xml`.

Make sure that you can run this command on your Instrumentation test package and find the instrumentation value successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

  ```
  $ aapt dump xmltree app-debug-androidTest-unaligned.apk AndroidManifest.xml | grep -A5 "instrumentation"
  ```

  A valid Instrumentation test package will produce output like the following:

  ```
  E: instrumentation (line=9)
        A: android:label(0x01010001)="Tests for com.amazon.aws.adf.android.referenceapp" (Raw: "Tests for com.amazon.aws.adf.android.referenceapp")
        A: android:name(0x01010003)="{{android.support.test.runner.AndroidJUnitRunner}}" (Raw: "android.support.test.runner.AndroidJUnitRunner")
        A: android:targetPackage(0x01010021)="com.amazon.aws.adf.android.referenceapp" (Raw: "com.amazon.aws.adf.android.referenceapp")
        A: android:handleProfiling(0x01010022)=(type 0x12)0x0
        A: android:functionalTest(0x01010023)=(type 0x12)0x0
  ```

  For more information, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_AAPT\_DUMP\_XMLTREE\_FAILED
<a name="INSTRUMENTATION_TEST_PACKAGE_AAPT_DUMP_XMLTREE_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not find the valid AndroidManifest.xml in your test package. Please
      verify that the test package is valid by running the command "aapt dump xmltree <path to
      your test package> AndroidManifest.xml", and try again after the command does not print any
      error.
```

During the upload validation process, Device Farm parses out information from the XML parse tree for an XML file contained within the package using the following command: `aapt dump xmltree <path to your package> AndroidManifest.xml`.

Make sure that you can run this command on your instrumentation test package successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

  ```
  $ aapt dump xmltree app-debug-androidTest-unaligned.apk AndroidManifest.xml
  ```

  A valid Instrumentation test package will produce output like the following:

  ```
  N: android=http://schemas.android.com/apk/res/android
    E: manifest (line=2)
      A: package="com.amazon.aws.adf.android.referenceapp.test" (Raw: "com.amazon.aws.adf.android.referenceapp.test")
      A: platformBuildVersionCode=(type 0x10)0x16 (Raw: "22")
      A: platformBuildVersionName="5.1.1-1819727" (Raw: "5.1.1-1819727")
      E: uses-sdk (line=5)
        A: android:minSdkVersion(0x0101020c)=(type 0x10)0x9
        A: android:targetSdkVersion(0x01010270)=(type 0x10)0x16
      E: instrumentation (line=9)
        A: android:label(0x01010001)="Tests for com.amazon.aws.adf.android.referenceapp" (Raw: "Tests for com.amazon.aws.adf.android.referenceapp")
        A: android:name(0x01010003)="android.support.test.runner.AndroidJUnitRunner" (Raw: "android.support.test.runner.AndroidJUnitRunner")
        A: android:targetPackage(0x01010021)="com.amazon.aws.adf.android.referenceapp" (Raw: "com.amazon.aws.adf.android.referenceapp")
        A: android:handleProfiling(0x01010022)=(type 0x12)0x0
        A: android:functionalTest(0x01010023)=(type 0x12)0x0
      E: application (line=16)
        A: android:label(0x01010001)=@0x7f020000
        A: android:debuggable(0x0101000f)=(type 0x12)0xffffffff
        E: uses-library (line=17)
          A: android:name(0x01010003)="android.test.runner" (Raw: "android.test.runner")
  ```

  For more information, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_TEST\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="INSTRUMENTATION_TEST_PACKAGE_TEST_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not find the package name in your test package. Please verify that the
      test package is valid by running the command "aapt debug badging <path to your test
      package>", and try again after finding the package name value behind the keyword "package:
      name."
```

During the upload validation process, Device Farm parses out the package name value from the output of the following command: `aapt debug badging <path to your package>`.

Make sure that you can run this command on your Instrumentation test package and find the package name value successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

  ```
  $ aapt debug badging app-debug-androidTest-unaligned.apk | grep "package: name="
  ```

  A valid Instrumentation test package will produce output like the following:

  ```
  package: name='com.amazon.aws.adf.android.referenceapp.test' versionCode='' versionName='' platformBuildVersionName='5.1.1-1819727'
  ```

  For more information, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation). 

### Test insights
<a name="troubleshooting-instrumentation-tests-insights"></a>

When you opt in to test insights, Device Farm generates a summarized report for your run and each job under it. If the service cannot generate the report, the insights report status is `SKIPPED` or `ERRORED`, and the report message explains why. The following messages can occur when generating insights for Instrumentation tests.

#### The job did not run to completion
<a name="ti-instrumentation-job-not-complete"></a>

`Unable to generate test insights because the job was {{status}}.`

The job ended in a non-successful state (where {{status}} is `STOPPED`, `ERRORED`, or `SKIPPED`), so there was no result to summarize. A run that ends in a failed state still receives insights.

To resolve this issue, investigate why the job did not run to completion. In many cases, the `message` field of the job itself might explain why the job didn't complete.

#### The results contained no test cases
<a name="ti-instrumentation-no-test-cases"></a>

`Test insights could not be generated. The test spec output file was parsed successfully but contained no test cases.`

The results artifact parsed successfully but contained zero test cases.

To resolve this issue, verify that your test suite includes at least one test case and that results are stored correctly under `$DEVICEFARM_LOG_DIR`.

#### The test output exceeds the maximum supported size
<a name="ti-instrumentation-output-too-large"></a>

`Unable to generate test insights: test output "test spec output" exceeds the maximum supported size of 1GB.`

The test spec output is larger than 1 GB.

To resolve this issue, investigate commands that are generating large numbers of lines in your test spec output. Then, remove or modify them.

#### No instrumentation output was found in the test spec output
<a name="ti-instrumentation-no-instrumentation-output"></a>

`Unable to generate test insights. No instrumentation test output was found in the test spec output file.`

The test spec output file was present but contained no instrumentation output lines.

To resolve this issue, ensure that your framework emits instrumentation output to `stdout` in the test spec file.

## Troubleshooting iOS application tests in AWS Device Farm
<a name="troubleshooting-ios-applications"></a>

The following topic lists error messages that occur during the upload of iOS application tests and recommends workarounds to resolve each error.

### IOS\_APP\_UNZIP\_FAILED
<a name="IOS_APP_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your application. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid iOS application package should produce output like the following:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- Info.plist
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_PAYLOAD\_DIR\_MISSING
<a name="IOS_APP_PAYLOAD_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the Payload directory inside your application. Please unzip your application, verify that the Payload directory is inside the package, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the iOS application package is valid, you will find the {{Payload}} directory inside the working directory.

   ```
   .
   `-- {{Payload}} (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- Info.plist
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_APP\_DIR\_MISSING
<a name="IOS_APP_APP_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the .app directory inside the Payload directory. Please unzip your application and then open the Payload directory, verify that the .app directory is inside the directory, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the iOS application package is valid, you will find an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example inside the {{Payload}} directory.

   ```
   .
   `-- Payload (directory)
           `-- {{AWSDeviceFarmiOSReferenceApp.app}} (directory)
                         |-- Info.plist
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_PLIST\_FILE\_MISSING
<a name="IOS_APP_PLIST_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the Info.plist file inside the .app directory. Please unzip your application and then open the .app directory, verify that the Info.plist file is inside the directory, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the iOS application package is valid, you will find the {{Info.plist}} file inside the {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example.

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_CPU\_ARCHITECTURE\_VALUE\_MISSING
<a name="IOS_APP_CPU_ARCHITECTURE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the CPU architecture value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "UIRequiredDeviceCapabilities" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the CPU architecture value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['UIRequiredDeviceCapabilities']
   ```

   A valid iOS application package should produce output like the following:

   ```
   ['armv7']
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_PLATFORM\_VALUE\_MISSING
<a name="IOS_APP_PLATFORM_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the platform value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "CFBundleSupportedPlatforms" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A valid iOS application package should produce output like the following:

   ```
   ['iPhoneOS']
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_WRONG\_PLATFORM\_DEVICE\_VALUE
<a name="IOS_APP_WRONG_PLATFORM_DEVICE_VALUE"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the platform device value was wrong in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the value of the key "CFBundleSupportedPlatforms" does not contain the keyword "simulator", and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A valid iOS application package should produce output like the following:

   ```
   ['iPhoneOS']
   ```

   If the iOS application is valid, the value should not contain the keyword `simulator`.

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_FORM\_FACTOR\_VALUE\_MISSING
<a name="IOS_APP_FORM_FACTOR_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the form factor value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "UIDeviceFamily" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the form factor value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['UIDeviceFamily']
   ```

   A valid iOS application package should produce output like the following:

   ```
   [1, 2]
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="IOS_APP_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the package name value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "CFBundleIdentifier" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid iOS application package should produce output like the following:

   ```
   Amazon.AWSDeviceFarmiOSReferenceApp
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

### IOS\_APP\_EXECUTABLE\_VALUE\_MISSING
<a name="IOS_APP_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the executable value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "CFBundleExecutable" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the executable value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid iOS application package should produce output like the following:

   ```
   AWSDeviceFarmiOSReferenceApp
   ```

   For more information, see [iOS tests in AWS Device Farm](#test-types-ios-tests).

## Troubleshooting XCTest tests in AWS Device Farm
<a name="troubleshooting-xctest"></a>

The following topic lists error messages that occur during the upload of XCTest tests and recommends workarounds to resolve each error.

**Note**  
The instructions below assume you are using MacOS.

### XCTEST\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="XCTEST_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid XCTest package should produce output like the following:

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- Info.plist
                 `-- (any other files)
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest).

### XCTEST\_TEST\_PACKAGE\_XCTEST\_DIR\_MISSING
<a name="XCTEST_TEST_PACKAGE_XCTEST_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the .xctest directory inside your test package. Please unzip your test package, verify that the .xctest directory is inside the package, and try again. 

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest package is valid, you will find a directory with a name similar to {{swiftExampleTests.xctest}} inside the working directory. The name should end with {{.xctest}}.

   ```
   .
   `-- {{swiftExampleTests.xctest}} (directory)
                 |-- Info.plist
                 `-- (any other files)
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest).

### XCTEST\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING
<a name="XCTEST_TEST_PACKAGE_PLIST_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the Info.plist file inside the .xctest directory. Please unzip your test package and then open the .xctest directory, verify that the Info.plist file is inside the directory, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest package is valid, you will find the {{Info.plist}} file inside the {{.xctest}} directory. In our example below, the directory is called {{swiftExampleTests.xctest}}.

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- {{Info.plist}}
                 `-- (any other files)
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest).

### XCTEST\_TEST\_PACKAGE\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="XCTEST_TEST_PACKAGE_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the package name value in the Info.plist file. Please unzip your test package and then open Info.plist file, verify that the key "CFBundleIdentifier" is specified, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.xctest}} directory like {{swiftExampleTests.xctest}} in our example:

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- {{Info.plist}}
                 `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('swiftExampleTests.xctest/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid XCtest application package should produce output like the following:

   ```
   com.amazon.kanapka.swiftExampleTests
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest).

### XCTEST\_TEST\_PACKAGE\_EXECUTABLE\_VALUE\_MISSING
<a name="XCTEST_TEST_PACKAGE_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the executable value in the Info.plist file. Please unzip your test package and then open Info.plist file, verify that the key "CFBundleExecutable" is specified, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.xctest}} directory like {{swiftExampleTests.xctest}} in our example:

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- {{Info.plist}}
                 `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('swiftExampleTests.xctest/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid XCtest application package should produce output like the following:

   ```
   swiftExampleTests
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest).

## Troubleshooting XCTest UI tests in AWS Device Farm
<a name="troubleshooting-xctest-ui"></a>

The following topic lists error messages that occur during the upload of XCTest UI tests and recommends workarounds to resolve each error.

### Upload errors
<a name="troubleshooting-xctest-ui-upload"></a>

The following errors can occur when you upload your XCTest UI tests.

#### XCTEST\_UI\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="XCTEST_UI_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

`We could not open your test IPA file. Please verify that the file is valid and try again.`

Make sure that you can unzip the application package without errors. In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid iOS application package should produce output like the following:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_PAYLOAD\_DIR\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PAYLOAD_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Payload directory inside your test package. Please unzip your test package, verify that the Payload directory is inside the package, and try again. `

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find the {{Payload}} directory inside the working directory.

   ```
   .
   `-- {{Payload}} (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_APP\_DIR\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_APP_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the .app directory inside the Payload directory. Please unzip your test package and then open the Payload directory, verify that the .app directory is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example inside the {{Payload}} directory.

   ```
   .
   `-- Payload (directory)
           `-- {{swift-sampleUITests-Runner.app}} (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLUGINS\_DIR\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PLUGINS_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Plugins directory inside the .app directory. Please unzip your test package and then open the .app directory, verify that the Plugins directory is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find the {{Plugins}} directory inside an {{.app}} directory. In our example, the directory is called {{swift-sampleUITests-Runner.app}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- {{Plugins}} (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_XCTEST\_DIR\_MISSING\_IN\_PLUGINS\_DIR
<a name="XCTEST_UI_TEST_PACKAGE_XCTEST_DIR_MISSING_IN_PLUGINS_DIR"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the .xctest directory inside the plugins directory. Please unzip your test package and then open the plugins directory, verify that the .xctest directory is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find an {{.xctest}} directory inside the {{Plugins}} directory. In our example, the directory is called {{swift-sampleUITests.xctest}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `{{swift-sampleUITests.xctest}} (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PLIST_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Info.plist file inside the .app directory. Please unzip your test package and then open the .app directory, verify that the Info.plist file is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find the {{Info.plist}} file inside the {{.app}} directory. In our example below, the directory is called {{swift-sampleUITests-Runner.app}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING\_IN\_XCTEST\_DIR
<a name="XCTEST_UI_TEST_PACKAGE_PLIST_FILE_MISSING_IN_XCTEST_DIR"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Info.plist file inside the .xctest directory. Please unzip your test package and then open the .xctest directory, verify that the Info.plist file is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find the {{Info.plist}} file inside the {{.xctest}} directory. In our example below, the directory is called {{swift-sampleUITests.xctest}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- {{Info.plist}}
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_CPU\_ARCHITECTURE\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_CPU_ARCHITECTURE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not the CPU architecture value in the Info.plist file. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "UIRequiredDeviceCapabilities" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the CPU architecture value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist') 
   print info_plist['UIRequiredDeviceCapabilities']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   ['armv7']
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLATFORM\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PLATFORM_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the platform value in the Info.plist. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "CFBundleSupportedPlatforms" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   ['iPhoneOS']
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_WRONG\_PLATFORM\_DEVICE\_VALUE
<a name="XCTEST_UI_TEST_PACKAGE_WRONG_PLATFORM_DEVICE_VALUE"></a>

If you see the following message, follow these steps to fix the issue.

`We found the platform device value was wrong in the Info.plist file. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the value of the key "CFBundleSupportedPlatforms" does not contain the keyword "simulator", and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   ['iPhoneOS']
   ```

   If the XCTest UI package is valid, the value should not contain the keyword `simulator`.

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_FORM\_FACTOR\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_FORM_FACTOR_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not the form factor value in the Info.plist. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "UIDeviceFamily" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the form factor value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['UIDeviceFamily']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   [1, 2]
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the package name value in the Info.plist file. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "CFBundleIdentifier" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   com.apple.test.swift-sampleUITests-Runner
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_EXECUTABLE\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the executable value in the Info.plist file. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "CFBundleExecutable" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the executable value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   XCTRunner
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_TEST\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_TEST_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the package name value in the Info.plist file inside the .xctest directory. Please unzip your test package and then open the Info.plist file inside the .xctest directory, verify that the key "CFBundleIdentifier" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Plugins/swift-sampleUITests.xctest/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   com.amazon.swift-sampleUITests
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_TEST\_EXECUTABLE\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_TEST_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the executable value in the Info.plist file inside the .xctest directory. Please unzip your test package and then open the Info.plist file inside the .xctest directory, verify that the key "CFBundleExecutable" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the executable value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Plugins/swift-sampleUITests.xctest/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   swift-sampleUITests
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_MULTIPLE\_APP\_DIRS
<a name="XCTEST_UI_TEST_PACKAGE_MULTIPLE_APP_DIRS"></a>

If you see the following message, follow these steps to fix the issue.

`We found multiple .app directories inside your test package. Please unzip your test package, verify that only a single .app directory is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should find only single `.app` directory like `swift-sampleUITests-Runner.app` in our example inside the .zip test package. 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{swift-sampleUITests-Runner.app}} (directory)
               |-- Info.plist
               |-- Plugins (directory)
               |       `swift-sampleUITests.xctest (directory)
              |            |-- Info.plist
              |            `-- (any other files)
               `-- (any other files)
       `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_MULTIPLE\_IPA\_DIRS
<a name="XCTEST_UI_TEST_PACKAGE_MULTIPLE_IPA_DIRS"></a>

If you see the following message, follow these steps to fix the issue.

`We found multiple .ipa directories inside your test package. Please unzip your test package, verify that only a single .ipa directory is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should find only single `.ipa` directory like `sampleUITests.ipa` in our example inside the .zip test package. 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{sampleUITests.ipa}} (directory)
               `-- Payload (directory)
                   `-- swift-sampleUITests-Runner.app (directory)
       `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_BOTH\_APP\_AND\_IPA\_DIR\_PRESENT
<a name="XCTEST_UI_TEST_PACKAGE_BOTH_APP_AND_IPA_DIR_PRESENT"></a>

If you see the following message, follow these steps to fix the issue.

`We found both .app and .ipa files inside your test package. Please unzip your test package, verify that only a single .app or .ipa file is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should find either `.ipa` directory like `sampleUITests.ipa` or `.app` directory like `swift-sampleUITests-Runner.app` in our example inside the .zip test package. You can refer to an example of valid XCTEST\_UI Test package in our documentation on [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui). 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{sampleUITests.ipa}} (directory)
               `-- Payload (directory)
                   `-- swift-sampleUITests-Runner.app (directory)
      `-- (any other files)
   ```

    or 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{swift-sampleUITests-Runner.app}} (directory)
               |-- Info.plist
               |-- Plugins (directory)
               `-- (any other files)
      `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

#### XCTEST\_UI\_TEST\_PACKAGE\_PAYLOAD\_DIR\_PRESENT\_IN\_ZIP
<a name="XCTEST_UI_TEST_PACKAGE_PAYLOAD_DIR_PRESENT_IN_ZIP"></a>

If you see the following message, follow these steps to fix the issue.

`We found a Payload directory inside your .zip test package. Please unzip your test package, ensure that a Payload directory is not present in the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should not find a Payload Directory inside your test package.

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- swift-sampleUITests-Runner.app (directory)
               |-- Info.plist
               |-- Plugins (directory)
               `-- (any other files)
      `-- {{Payload (directory) [This directory should not be present]}}
               |-- (any other files)
      `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui).

### Test insights
<a name="troubleshooting-xctest-ui-insights"></a>

When you opt in to test insights, Device Farm generates a summarized report for your run and each job under it. If the service cannot generate the report, the insights report status is `SKIPPED` or `ERRORED`, and the report message explains why. The following messages can occur when generating insights for XCTest UI tests.

#### The job did not run to completion
<a name="ti-xctest-ui-job-not-complete"></a>

`Unable to generate test insights because the job was {{status}}.`

The job ended in a non-successful state (where {{status}} is `STOPPED`, `ERRORED`, or `SKIPPED`), so there was no result to summarize. A run that ends in a failed state still receives insights.

To resolve this issue, investigate why the job did not run to completion. In many cases, the `message` field of the job itself might explain why the job didn't complete.

#### The results contained no test cases
<a name="ti-xctest-ui-no-test-cases"></a>

`Test insights could not be generated. The xcresult_summary.json file was parsed successfully but contained no test cases.`

The results artifact parsed successfully but contained zero test cases.

To resolve this issue, verify that your test suite includes at least one test case and that results are stored correctly under `$DEVICEFARM_LOG_DIR`.

#### The test output exceeds the maximum supported size
<a name="ti-xctest-ui-output-too-large"></a>

`Unable to generate test insights: test output "xcresult bundle" exceeds the maximum supported size of 1GB.`

The xcresult bundle is larger than 1 GB.

To resolve this issue, reduce the xcresult bundle size to below 1 GB by trimming logs or attachments.

#### The xcresult bundle was not found
<a name="ti-xctest-ui-xcresult-not-found"></a>

`Unable to generate test insights. The xctestresult bundle file (.xcresult) was not found in the output artifacts.`

Device Farm could not find an `.xcresult` bundle for this job, so there were no results to summarize.

Device Farm looks for the bundle anywhere under `$DEVICEFARM_DERIVED_DATA_PATH`. The default XCTest UI test spec produces it there automatically, so this message usually indicates that a customized test spec did not write results to that location.

To confirm whether a bundle was produced, download the customer artifacts for the job and look for an `.xcresult` directory under the derived data folder.

#### The xcresult test results could not be processed
<a name="ti-xctest-ui-xcresult-error"></a>

`Test insights could not be generated because of an error while processing the .xcresult test results.`

Device Farm found an `.xcresult` bundle but could not read the test results from it.

To resolve this issue, ensure that your test run produces a valid `.xcresult` bundle. Verify that your test spec does not modify, truncate, or archive the bundle before the run finishes, and that the **xcodebuild** command completes rather than being interrupted by a timeout.

# Security in AWS Device Farm
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Device Farm, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using Device Farm. The following topics show you how to configure Device Farm to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Device Farm resources. 

**Topics**
+ [Identity and access management in AWS Device Farm](#security-iam)
+ [Compliance validation for AWS Device Farm](#ATP-compliance)
+ [Data protection in AWS Device Farm](#data-protection)
+ [Resilience in AWS Device Farm](#disaster-recovery-resiliency)
+ [Infrastructure security in AWS Device Farm](#infrastructure-security)
+ [Configuration vulnerability analysis and management in Device Farm](#security-vulnerability-analysis-and-management)
+ [Incident response in Device Farm](#security-incident-response)
+ [Logging and monitoring in Device Farm](#security-logging-monitoring)
+ [Security best practices for Device Farm](#security-best-practices)

## Identity and access management in AWS Device Farm
<a name="security-iam"></a>

### Audience
<a name="security_iam_audience"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting AWS Device Farm identity and access](#security_iam_troubleshoot))
+ **Service administrator** - determine user access and submit permission requests (see [How AWS Device Farm works with IAM](#security_iam_service-with-iam))
+ **IAM administrator** - write policies to manage access (see [AWS Device Farm identity-based policy examples](#security_iam_id-based-policy-examples))

### Authenticating with identities
<a name="security_iam_authentication"></a>

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

#### AWS account root user
<a name="security_iam_authentication-rootuser"></a>

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*. 

#### IAM Users and groups
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

The following table outlines the Device Farm AWS managed policies.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSDeviceFarmFullAccess](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn:aws:iam::aws:policy/AWSDeviceFarmFullAccess$jsonEditor) | Provides full access to all AWS Device Farm operations. | July 15, 2015 | 
| [AWSServiceRoleForDeviceFarmTestGrid](https://docs.aws.amazon.com/devicefarm/latest/testgrid/using-service-linked-roles.html) | Allows Device Farm to access AWS resources on your behalf. | May 20, 2021 | 

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

### How AWS Device Farm works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Device Farm, you should understand which IAM features are available to use with Device Farm. To get a high-level view of how Device Farm and other AWS services work with IAM, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Device Farm identity-based policies](#security_iam_service-with-iam-id-based-policies)
+ [Device Farm resource-based policies](#security_iam_service-with-iam-resource-based-policies)
+ [Access control lists](#security_iam_service-with-iam-acls)
+ [Authorization based on Device Farm tags](#security_iam_service-with-iam-tags)
+ [Device Farm IAM roles](#security_iam_service-with-iam-roles)

#### Device Farm identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources and the conditions under which actions are allowed or denied. Device Farm supports specific actions, resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

##### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Device Farm use the following prefix before the action: `devicefarm:`. For example, to grant someone permission to start Selenium sessions with the Device Farm desktop browser testing `CreateTestGridUrl` API operation, you include the `devicefarm:CreateTestGridUrl` action in the policy. Policy statements must include either an `Action` or `NotAction` element. Device Farm defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "devicefarm:action1",
      "devicefarm:action2"
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `List`, include the following action:

```
"Action": "devicefarm:List*"
```



To see a list of Device Farm actions, see [Actions defined by AWS Device Farm](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdevicefarm.html#awsdevicefarm-actions-as-permissions) in the *IAM Service Authorization Reference*.

##### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```



The Amazon EC2 instance resource has the following ARN:

```
arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `i-1234567890abcdef0` instance in your statement, use the following ARN:

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
```

To specify all instances that belong to an account, use the wildcard (\*):

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*"
```

Some Device Farm actions, such as those for creating resources, cannot be performed on a resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Many Amazon EC2 API actions involve multiple resources. For example, `AttachVolume` attaches an Amazon EBS volume to an instance, so an IAM user must have permissions to use the volume and the instance. To specify multiple resources in a single statement, separate the ARNs with commas. 

```
"Resource": [
      "resource1",
      "resource2"
```

To see a list of Device Farm resource types and their ARNs, see [Resource types defined by AWS Device Farm](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdevicefarm.html#awsdevicefarm-resources-for-iam-policies) in the *IAM Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by AWS Device Farm](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdevicefarm.html#awsdevicefarm-actions-as-permissions) in the *IAM Service Authorization Reference*.

##### Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Device Farm defines its own set of condition keys and also supports the use of some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Device Farm condition keys, see [Condition keys for AWS Device Farm](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdevicefarm.html#awsdevicefarm-policy-keys) in the *IAM Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions defined by AWS Device Farm](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdevicefarm.html#awsdevicefarm-actions-as-permissions) in the *IAM Service Authorization Reference*. 

##### Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Device Farm identity-based policies, see [AWS Device Farm identity-based policy examples](#security_iam_id-based-policy-examples).

#### Device Farm resource-based policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Device Farm does not support resource-based policies.

#### Access control lists
<a name="security_iam_service-with-iam-acls"></a>

Device Farm does not support access control lists (ACLs).

#### Authorization based on Device Farm tags
<a name="security_iam_service-with-iam-tags"></a>

You can attach tags to Device Farm resources or pass tags in a request to Device Farm. To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. For more information about tagging Device Farm resources, see [Tagging AWS Device Farm resources](#tagging). 

To view an example identity-based policy for limiting access to a resource based on the tags on that resource, see [Viewing Device Farm desktop browser testing projects based on tags](#security_iam_id-based-policy-examples-view-project-tags).

#### Device Farm IAM roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity in your AWS account that has specific permissions.

##### Using temporary credentials with Device Farm
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

Device Farm supports the use of temporary credentials. 

You can use temporary credentials to sign in with federation to assume an IAM role orcross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html). 

##### Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view, but cannot edit, the permissions for service-linked roles.

Device Farm uses service-linked roles in the Device Farm desktop browser testing feature. For information on these roles, see [ Using Service-Linked Roles in Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/using-service-linked-roles.html) in the developer guide.

##### Service roles
<a name="security_iam_service-with-iam-roles-service"></a>

Device Farm does not support service roles. 

This feature allows a service to assume a [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) on your behalf. This role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your IAM account and are owned by the account. This means that an IAM administrator can change the permissions for this role. However, doing so might break the functionality of the service.



### AWS Device Farm identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, IAM users and roles don't have permission to create or modify Device Farm resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Accessing one Device Farm desktop browser testing project](#security_iam_id-based-policy-examples-access-one-project)
+ [Viewing Device Farm desktop browser testing projects based on tags](#security_iam_id-based-policy-examples-view-project-tags)

#### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Device Farm resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

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

#### Accessing one Device Farm desktop browser testing project
<a name="security_iam_id-based-policy-examples-access-one-project"></a>

In this example, you want to grant an IAM user in your AWS account access to one of your Device Farm destktop browser testing projects, `arn:aws:devicefarm:us-west-2:111122223333:testgrid-project:123e4567-e89b-12d3-a456-426655441111`. You want the account to be able to see items related to the project.

In addition to the `devicefarm:GetTestGridProject` endpoint, the account must have the `devicefarm:ListTestGridSessions`, `devicefarm:GetTestGridSession`, `devicefarm:ListTestGridSessionActions`, and `devicefarm:ListTestGridSessionArtifacts` endpoints. 

If you are using CI systems, you should give each CI runner unique access credentials. For example, a CI system is unlikely to need more permissions than `devicefarm:ScheduleRun` or `devicefarm:CreateUpload`. The following IAM policy outlines a minimal policy to allow a CI runner to start a test of a new Device Farm native app test by creating an upload and using it to schedule a test run:

#### Viewing Device Farm desktop browser testing projects based on tags
<a name="security_iam_id-based-policy-examples-view-project-tags"></a>

You can use conditions in your identity-based policy to control access to Device Farm resources based on tags. This example shows how you might create a policy that allows the viewing of projects and sessions. Permission is granted if the `Owner` tag of the requested resource matches the username of the requesting account.

You can attach this policy to the IAM users in your account. If a user named `richard-roe` attempts to view a Device Farm project or session, the project must be tagged `Owner=richard-roe` or `owner=richard-roe`. Otherwise, the user is denied access. The condition tag key `Owner` matches both `Owner` and `owner` because condition key names are not case sensitive. For more information, see [IAM JSON Policy Elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

### Troubleshooting AWS Device Farm identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Device Farm and IAM.

#### I am not authorized to perform an action in Device Farm
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error in the AWS Management Console that says you're not authorized to perform an action, you must contact your administrator for assistance. Your administrator is the person who provided you with your user name and password.

The following example error occurs when the IAM user, `mateojackson`, tries to use the console to view details about a run, but does not have `devicefarm:GetRun` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: devicefarm:GetRun on resource: arn:aws:devicefarm:us-west-2:123456789101:run:123e4567-e89b-12d3-a456-426655440000/123e4567-e89b-12d3-a456-426655441111
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `devicefarm:GetRun` on resource `arn:aws:devicefarm:us-west-2:123456789101:run:123e4567-e89b-12d3-a456-426655440000/123e4567-e89b-12d3-a456-426655441111` resource using the `devicefarm:GetRun` action.

#### I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Device Farm.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Device Farm. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I want to view my access keys
<a name="security_iam_troubleshoot-access-keys"></a>

After you create your IAM user access keys, you can view your access key ID at any time. However, you can't view your secret access key again. If you lose your secret key, you must create a new access key pair. 

Access keys consist of two parts: an access key ID (for example, `AKIAIOSFODNN7EXAMPLE`) and a secret access key (for example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`). Like a user name and password, you must use both the access key ID and secret access key together to authenticate your requests. Manage your access keys as securely as you do your user name and password.

**Important**  
Do not provide your access keys to a third party, even to help [find your canonical user ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindCanonicalId). By doing this, you might give someone permanent access to your AWS account.

When you create an access key pair, you are prompted to save the access key ID and secret access key in a secure location. The secret access key is available only at the time you create it. If you lose your secret access key, you must add new access keys to your IAM user. You can have a maximum of two access keys. If you already have two, you must delete one key pair before creating a new one. To view instructions, see [Managing access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey) in the *IAM User Guide*.

#### I'm an administrator and want to allow others to access Device Farm
<a name="security_iam_troubleshoot-admin-delegate"></a>

To allow others to access Device Farm, you must grant permission to the people or applications that need access. If you are using AWS IAM Identity Center to manage people and applications, you assign permission sets to users or groups to define their level of access. Permission sets automatically create and assign IAM policies to IAM roles that are associated with the person or application. For more information, see [Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) in the *AWS IAM Identity Center User Guide*.

If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people or applications that need access. You must then attach a policy to the entity that grants them the correct permissions in Device Farm. After the permissions are granted, provide the credentials to the user or application developer. They will use those credentials to access AWS. To learn more about creating IAM users, groups, policies, and permissions, see [IAM Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) and [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

#### I want to allow people outside of my AWS account to access my Device Farm resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Device Farm supports these features, see [How AWS Device Farm works with IAM](#security_iam_service-with-iam).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Compliance validation for AWS Device Farm
<a name="ATP-compliance"></a>

Third-party auditors assess the security and compliance of AWS Device Farm as part of multiple AWS compliance programs. These include SOC, PCI, FedRAMP, HIPAA, and others. AWS Device Farm is not in scope of any AWS compliance programs.

For a list of AWS services in scope of specific compliance programs, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/). For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using Device Farm is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. AWS provides the following resources to help with compliance:
+ [Security and Compliance Quick Start Guides](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance) – These deployment guides discuss architectural considerations and provide steps for deploying security- and compliance-focused baseline environments on AWS.
+ [AWS Compliance Resources](https://aws.amazon.com/compliance/resources/) – This collection of workbooks and guides might apply to your industry and location.
+ [Evaluating Resources with Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) in the *AWS Config Developer Guide* – AWS Config assesses how well your resource configurations comply with internal practices, industry guidelines, and regulations.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) – This AWS service provides a comprehensive view of your security state within AWS that helps you check your compliance with security industry standards and best practices.

## Data protection in AWS Device Farm
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Device Farm (Device Farm). As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Device Farm or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

### Encryption in transit
<a name="data-protection-encryption-transit"></a>

 The Device Farm endpoints only support signed HTTPS (SSL/TLS) requests except where otherwise noted. All content retrieved from or placed in Amazon S3 through upload URLs is encrypted using SSL/TLS. For more information on how HTTPS requests are signed in AWS, see [Signing AWS API requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html) in the AWS General Reference.

It is your responsibility to encrypt and secure any communications that your tested applications make and any applications installed in the process of running on-device tests.

### Encryption at rest
<a name="data-protection-encryption-rest"></a>

Device Farm's desktop browser testing feature supports encryption at rest for artifacts generated during tests.

Device Farm's physical mobile device testing data is not encrypted at rest.

### Data retention
<a name="data-protection-retention"></a>

Data in Device Farm is retained for a limited time. After the retention period expires, the data is removed from Device Farm's backing storage.


| Content type | Retention period (days) | Metadata Retention period (days) | 
| --- | --- | --- | 
| Uploaded applications | 30 | 30 | 
| Uploaded test packages | 30 | 30 | 
| Logs | 400 | 400 | 
| Video recordings and other artifacts | 400 | 400 | 

It is your responsibility to archive any content that you want to retain for longer periods. 

### Data management
<a name="data-protection-management"></a>

Data in Device Farm is managed differently depending on which features are used. This section explains how data is managed while and after you use Device Farm. 

#### Desktop browser testing
<a name="data-protection-management-testgrid"></a>

Instances used during Selenium sessions are not saved. All data generated as a result of browser interactions is discarded when the session ends.

This feature currently supports encryption at rest for artifacts generated during the test.

#### Physical device testing
<a name="data-protection-management-physical"></a>

The following sections provide information about the steps AWS takes to clean up or destroy devices after you have used Device Farm.

Device Farm's physical mobile device testing data is not encrypted at rest.

##### Public device fleets
<a name="data-protection-management-public"></a>

After test execution is complete, Device Farm performs a series of cleanup tasks on each device in the public device fleet, including uninstallation of your app. If we cannot verify uninstallation of your app or any of the other cleanup steps, the device receives a factory reset before it is put back into use.

**Note**  
It is possible for data to persist between sessions in some cases, especially if you make use of the device system outside the context of your app. For this reason, and because Device Farm captures video and logs of activity taking place during your use of each device, we recommend that you do not enter sensitive information (for example, Google account or Apple ID), personal information, and other security-sensitive details during your automated test and remote access sessions.

##### Private devices
<a name="data-protection-management-private"></a>

After expiration or termination of your private device contract, the device is removed from use and securely destroyed in accordance with AWS destruction policies. For more information, see [Private devices in AWS Device Farm](#working-with-private-devices).

### Key management
<a name="data-protection-key-management"></a>

 Currently, Device Farm does not offer any external key management for encryption of data, at rest or in transit. 

### Internetwork traffic privacy
<a name="data-protection-traffic-privacy"></a>

 Device Farm can be configured, for private devices only, to use Amazon VPC endpoints to connect to your resources in AWS. Access to any non-public AWS infrastructure associated with your account (for example, Amazon EC2 instances without a public IP address) must use an Amazon VPC endpoint. Regardless of VPC endpoint configuration, Device Farm isolates your traffic from other users throughout the Device Farm network. 

Your connections outside the AWS network are not guaranteed to be secured or safe, and it is your responsibility to secure any internet connections your applications make. 

## Resilience in AWS Device Farm
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

Because Device Farm is available in the `us-west-2` Region only, we strongly recommend that you implement backup and recovery processes. Device Farm should not be the only source of any uploaded content.

Device Farm makes no guarantees of the availability of public devices. These devices are taken in and out of the public device pool depending on a variety of factors, such as failure rate and quarantine status. We do not recommend that you depend on the availability of any one device in the public device pool. 

## Infrastructure security in AWS Device Farm
<a name="infrastructure-security"></a>

As a managed service, AWS Device Farm is protected by the AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Device Farm through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) (AWS STS) to generate temporary security credentials to sign requests.

### Infrastructure security for physical device testing
<a name="infrastructure-security-physical-device-testing"></a>

Devices are physically separated during physical device testing. Network isolation prevents cross-device communication over wireless networks.

Public devices are shared, and Device Farm makes a best-effort attempt at keeping devices safe over time. Certain actions, such as attempts to acquire complete administrator rights on a device (a practice referred to as *rooting* or *jailbreaking*), cause public devices to become quarantined. They are removed from the public pool automatically and placed into manual review.

Private devices are accessible only by AWS accounts explicitly authorized to do so. Device Farm physically isolates these devices from other devices and keeps them on a separate network.

On privately managed devices, tests can be configured to use an Amazon VPC endpoint to secure connections in and out of your AWS account.

### Infrastructure security for desktop browser testing
<a name="infrastructure-security-desktop-browser-testing"></a>

When you use the desktop browser testing feature, all test sessions are separated from one another. Selenium instances cannot cross-communicate without an intermediate third party, external to AWS.

All traffic to Selenium WebDriver controllers must be made through the HTTPS endpoint generated with `createTestGridUrl`. 

You are responsible for making sure that each Device Farm test instance has secure access to resources it tests. By default, Device Farm's desktop browser testing instances have access to the public internet. When you attach your instance to a VPC, it behaves like any other EC2 instance, with access to resources determined by the VPC's configuration and its associated networking components. AWS provides [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) and [network Access Control Lists (ACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) to increase security in your VPC. Security groups control inbound and outbound traffic for your resources, and network ACLs control inbound and outbound traffic for your subnets. Security groups provide enough access control for most subnets. You can use network ACLs if you want an additional layer of security for your VPC. For general guidelines on security best practices when using Amazon VPCs, see [security best practices ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html) for your VPC in the *Amazon Virtual Private Cloud User Guide*.

## Configuration vulnerability analysis and management in Device Farm
<a name="security-vulnerability-analysis-and-management"></a>

Device Farm allows you to run software that is not actively maintained or patched by the vendor, such as the OS vendor, hardware vendor, or phone carrier. Device Farm makes a best-effort attempt to maintain up to date software, but makes no guarantees that any particular version of the software on a physical device is up to date, by design allowing potentially vulnerable software to be put into use.

For example, if a test is performed on a device running Android 4.4.2, Device Farm makes no guarantee that the device is patched against the [vulnerability in Android known as StageFright](https://en.wikipedia.org/wiki/Stagefright_(bug)). It is up to the vendor (and sometimes the carrier) of the device to provide security updates to devices. A malicious application that uses this vulnerability is not guaranteed to be caught by our automated quarantining. 

Private devices are maintained as per your agreement with AWS.

 Device Farm makes a best-faith effort to prevent customer applications from actions such as *rooting* or *jailbreaking*. Device Farm removes devices that are quarantined from the public pool until they have been manually reviewed. 

You are responsible for keeping any libraries or versions of software that you use in your tests, such as Python wheels and Ruby gems, up to date. Device Farm recommends that you update your test libraries.

These resources can help keep your test dependencies up to date: 
+ For information about how to secure Ruby gems, see [Security Practices](https://guides.rubygems.org/security/) on the RubyGems website. 
+ For information about the safety package used by Pipenv and endorsed by the Python Packaging Authority to scan your dependency graph for known vulnerabilities, see the [Detection of Security Vulnerabilities](https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-detection-of-security-vulnerabilities) on GitHub.
+ For information about the Open Web Application Security Project (OWASP) Maven dependency checker, see [OWASP DependencyCheck](https://owasp.org/www-project-dependency-check/) on the OWASP website. 

It is important to remember that even if an automated system does not believe there are any known security issues, it does not mean that there are no security issues. Always use due diligence when using libraries or tools from third parties and verify cryptographic signatures when possible or reasonable.

## Incident response in Device Farm
<a name="security-incident-response"></a>

Device Farm continuously monitors devices for behaviors that might indicate security issues. If AWS is made aware of a case where customer data, such as test results or files written to a public device, is accessible by another customer, AWS contacts affected customers, according to the standard incident alerting and reporting policies used throughout AWS services.

## Logging and monitoring in Device Farm
<a name="security-logging-monitoring"></a>

This service supports AWS CloudTrail, which is a service that records AWS calls for your AWS account and delivers log files to an Amazon S3 bucket. By using information collected by CloudTrail, you can determine what requests were successfully made to AWS services, who made the request, when it was made, and so on. To learn more about CloudTrail, including how to turn it on and find your log files, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

For information about using CloudTrail with Device Farm, see [Logging AWS Device Farm API calls with AWS CloudTrail](#logging-using-cloudtrail).

## Security best practices for Device Farm
<a name="security-best-practices"></a>

 Device Farm provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions. 
+ Grant any continuous integration (CI) system you use the least privilege possible under IAM. Consider using temporary credentials for each CI system test so that even if a CI system is compromised, it cannot make spurious requests. For more information about temporary credentials, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerole).
+ Use `adb` commands in a custom test environment to clean up any content created by your application. For more information about custom test environments, see [Custom test environments in AWS Device Farm](#custom-test-environments).
+ Avoid logging sensitive data, such as credentials or personal information, on the device or in your test framework. Logs, videos, screenshots, and other artifacts generated during a run are retained by Device Farm so that you can review them after the run completes. For more information on best practices in custom test environments, see [Best practices for custom test environment execution](#custom-test-environments-best-practices).

# Limits in AWS Device Farm
<a name="limits"></a>

**Topics**
+ [Service limits](#service-limits)
+ [File limits](#file-limits)
+ [API limits](#api-limits)
+ [Appium endpoint limits](#appium-endpoint-limits)
+ [Custom environment variable limits](#custom-environment-variable-limits)

## Service limits
<a name="service-limits"></a>
+  There is no limit to the number of devices that you can include in a test run. However, the maximum number of devices that Device Farm will test simultaneously during a test run is five. This number may be increased upon request and evaluated on per-case basis by the service team. 
+ There is no limit to the number of runs that you can schedule. Note that they can only remain queued for up to 24 hours.
+  There is a 150-minute hard limit to the duration of a remote access session. 
+  There is a 150-minute hard limit to the duration of an automated test run 
+  The maximum number of in-flight jobs, including pending queued jobs across your account, is 250. This is a soft limit. 
+  There's no limit to the number of devices you can include in a test run. The number of devices (jobs) that can execute your tests in parallel at any given time is equal to your account-level concurrency. The default account-level concurrency for metered use in Device Farm is five. 
+ The metered concurrency limit may be increased upon request up to a certain threshold depending on the use case. The default account-level concurrency for unmetered use is equal to the number of slots you are subscribed to for that platform. 

   For more information concerning the default metered concurrency limits or quotas in general, see the [Quotas](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html) page. 
+ An automation run that doesn't use a [custom test environment](#custom-test-environments) can only have up to 250 individual test cases in it. Otherwise, the run may be skipped. 

## File limits
<a name="file-limits"></a>
+  The maximum file size of an app that you can upload is 4 GB. Note that we do not currently accept .aab format files for Android. 
+  The maximum size of Device Farm's automatically-generated video during your test run is 1GB. Any video exceeding this size will have all remaining video content truncated. Customers can still use their own video recording solution, if present, and store it outside of Device Farm's managed storage. 
+  The maximum size of Device Farm's automatically-generated device log (logcat on Android or syslog on iOS) during your test run is 1GB. Any log exceeding this size will have all remaining logs truncated. For logs larger than 1 GB, Customers can store these logs outside of Device Farm's managed storage. 
+  The maximum size cumulative of Device Farm's custom environment mode customer artifacts is 1GB. If this size is exceeded by your artifacts, then none of the artifacts will be available. 
+  If the cumulative size of all artifacts generated during a test run exceeds 4GB, then some artifacts may be dropped (including the video, device logs, and customer artifacts). 

## API limits
<a name="api-limits"></a>
+  Device Farm follows a token-bucket algorithm to throttle API call rates. For example, imagine creating a bucket that holds tokens. Each token represents one transaction, and one API call uses up a token. Tokens are added to the bucket at a fixed rate (e.g., 10 tokens per second), and the bucket has a maximum capacity (e.g., 100 tokens). When a request or packet arrives, it must claim a token from the bucket to be processed. If there are enough tokens, the request is allowed through and tokens are removed. If there aren't enough tokens, the request is either delayed or dropped, depending on the implementation. 

   In Device Farm, this is how the algorithm is implemented: 
  +  The **Burst API requests** is the maximum number of requests the service is able to respond to for a specified API in a specified customer account ID. In other words, this is the capacity of the bucket. You can call the API as many times as there are tokens remaining in the bucket, and each request consumes one token. 
  +  The **Transactions-per-second (TPS) rate** is the minimum rate at which your API requests can be executed. In other words, this is the rate at which the bucket refills with tokens per second. For example, if an API has a burst number of ten but a TPS of one, you could call it ten times instantly. However, the bucket would only regain tokens at a rate of one token per second, resulting in being throttled to one call per second unless you stopped calling the API to let the bucket refill. 

 Here are the rates for Device Farm APIs: 
+  For List and Get APIs, the **Burst API requests** capacity is `50`, and the **Transactions-per-second (TPS) rate** is `10`. 
+  For all other APIs, the **Burst API requests** capacity is `10`, and the **Transactions-per-second (TPS) rate** is `1`. 

## Appium endpoint limits
<a name="appium-endpoint-limits"></a>

The following limits apply to all Appium endpoint sessions. For questions and guidance on how to best handle limits, please open a support case.
+ Every Appium command has an execution duration limit of 4 minutes, after which the command times out.
+ The endpoint accepts input payload sizes of up to 20MB, and allows output payload sizes of up to 20MB. Any request with a larger input or output size than this will receive a WebDriver error of `'unsupported operation'`.
+ Requests execute sequentially on the device in the order that they are received. As a result, we highly recommend sending commands sequentially, and waiting for each command's response before sending a new one. That said, certain Appium server commands can be sent in parallel, specifically:
  + [getStatus](https://appium.io/docs/en/2.19/commands/base-driver/#getstatus)
  + [getSessions](https://appium.io/docs/en/2.19/commands/base-driver/#getsessions)
+ The endpoint does not support the [WebDriver BiDi protocol](https://appium.io/docs/en/2.19/guides/caps/#bidi-protocol-support) at this time.
+ The endpoint does not support Appium Plugins or drivers other than the XCUITest and UIAutomator2 drivers.
+ A maximum of 3 apps can be used as auxiliary apps with a remote access session creation request. That said, there is no limit on how many apps can be installed during a session using the [`InstallToRemoteAccessSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_InstallToRemoteAccessSession.html) API.

## Custom environment variable limits
<a name="custom-environment-variable-limits"></a>

The following limits apply to all custom environment variables. For questions and guidance on how to best handle limits, please open a support case.
+ A maxiumum of 32 variables can be configured on a given Device Farm project or run.
+ Variable names cannot exceed 256 characters in length.
+ Variable names are subject to the limitations imposed by `bash`. Namely, they must contain only alphanumeric and underscore characters, and cannot start with a number.
+ Variable names beginning with `$DEVICEFARM_` are reserved for internal service use.
+ Variable values cannot exceed 256 characters in length.
+ Environment variables cannot be used to configure test host compute selection in the test spec file.

# Tools and plugins for AWS Device Farm
<a name="aws-device-farm-tools-plugins"></a>

This section contains links and information about working with AWS Device Farm tools and plugins. You can find Device Farm plugins on [AWS Labs on GitHub](https://github.com/awslabs/).

If you are an Android developer, we also have an [AWS Device Farm sample app for Android on GitHub](https://github.com/awslabs/aws-device-farm-sample-app-for-android). You can use the app and example tests as a reference for your own Device Farm test scripts.

**Topics**
+ [Integrating Device Farm with a Jenkins CI server](#continuous-integration-jenkins-plugin)
+ [Integrating Device Farm with a Gradle build system](#aws-device-farm-android-gradle-plugin)

## Integrating Device Farm with a Jenkins CI server
<a name="continuous-integration-jenkins-plugin"></a>

The Jenkins CI plugin provides AWS Device Farm functionality from your own Jenkins continuous integration (CI) server. For more information, see [Jenkins (software)](https://en.wikipedia.org/wiki/Jenkins_%28software%29).

**Note**  
To download the Jenkins plugin, go to [GitHub](https://github.com/awslabs/aws-device-farm-jenkins-plugin) and follow the instructions in [Step 1: Installing the Jenkins CI plugin for AWS Device Farm](#jenkins-ci-installing-the-plugin).

This section contains a series of procedures to set up and use the Jenkins CI plugin with AWS Device Farm.

The following images show the features of the Jenkins CI plugin.

![Integration with Jenkins CI Hello World application](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-jenkins-plugin-continuous-integration-project-hello-world-app.png)


![Integration with Jenkins CI post-build actions](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-jenkins-plugin-continuous-integration-post-build-actions.png)


The plugin can also pull down all the test artifacts (logs, screenshots, etc.) locally:

![Integration with Jenkins CI test artifacts](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-jenkins-plugin-continuous-integration-test-artifacts.png)


**Topics**
+ [Dependencies](#jenkins-plugin-dependencies)
+ [Step 1: Installing the Jenkins CI plugin for AWS Device Farm](#jenkins-ci-installing-the-plugin)
+ [Step 2: Creating an AWS Identity and Access Management user for your Jenkins CI Plugin for AWS Device Farm](#jenkins-ci-set-up-iam-user)
+ [Step 3: Configuring the Jenkins CI plugin for the first time in AWS Device Farm](#jenkins-ci-first-time-configuration-instructions)
+ [Step 4: Using the plugin in a Jenkins job](#jenkins-ci-using-plugin-jenkins-job)

### Dependencies
<a name="jenkins-plugin-dependencies"></a>

The Jenkins CI Plugin requires the AWS Mobile SDK 1.10.5 or later. For more information and to install the SDK, see [AWS Mobile SDK](https://aws.amazon.com/mobile/sdk/).

### Step 1: Installing the Jenkins CI plugin for AWS Device Farm
<a name="jenkins-ci-installing-the-plugin"></a>

There are two options for installing the Jenkins continuous integration (CI) plugin for AWS Device Farm. You can search for the plugin from within the **Available Plugins** dialog in the Jenkins Web UI, or you can download the `hpi` file and install it from within Jenkins.

#### Install from within the Jenkins UI
<a name="installing-jenkins-from-within-ui"></a>

1. Find the plugin within the Jenkins UI by choosing **Manage Jenkins**, **Manage Plugins**, and then choose **Available**.

1. Search for **aws-device-farm**.

1. Install the AWS Device Farm plugin.

1. Ensure that the plugin is owned by the `Jenkins` user.

1. Restart Jenkins.

#### Download the plugin
<a name="installing-jenkins-manual-install"></a>

1. Download the `hpi` file directly from [http://updates.jenkins-ci.org/latest/aws-device-farm.hpi](http://updates.jenkins-ci.org/latest/aws-device-farm.hpi).

1. Ensure that the plugin is owned by the `Jenkins` user.

1. Install the plugin using one of the following options:
   + Upload the plugin by choosing **Manage Jenkins**, **Manage Plugins**, **Advanced**, and then choose **Upload plugin**.
   + Place the `hpi` file in the Jenkins plugin directory (usually `/var/lib/jenkins/plugins`).

1. Restart Jenkins.

### Step 2: Creating an AWS Identity and Access Management user for your Jenkins CI Plugin for AWS Device Farm
<a name="jenkins-ci-set-up-iam-user"></a>

We recommend that you do not use your AWS root account to access Device Farm. Instead, create a new AWS Identity and Access Management (IAM) user (or use an existing IAM user) in your AWS account, and then access Device Farm with that IAM user.

To create a new IAM user, see [Creating an IAM User (AWS Management Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_SettingUpUser.html#Using_CreateUser_console). Be sure to generate an access key for each user and download or save the user security credentials. You will need the credentials later.

#### Give the IAM user permission to access Device Farm
<a name="jenkins-ci-setting-up-permissions"></a>

To give the IAM user permission to access Device Farm, create a new access policy in IAM, and then assign the access policy to the IAM user as follows.

**Note**  
The AWS root account or IAM user that you use to complete the following steps must have permission to create the following IAM policy and attach it to the IAM user. For more information, see [Working with Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies_manage.html)

**To create the access policy in IAM**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Policies**.

1. Choose **Create Policy**. (If a **Get Started** button appears, choose it, and then choose **Create Policy**.)

1. Next to **Create Your Own Policy**, choose **Select**.

1. For **Policy Name**, type a name for the policy (for example, **AWSDeviceFarmAccessPolicy**).

1. For **Description**, type a description that helps you associate this IAM user with your Jenkins project.

1. For **Policy Document**, type the following statement:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DeviceFarmAll",
               "Effect": "Allow",
               "Action": [ "devicefarm:*" ],
               "Resource": [ "*" ]
           }
       ]
   }
   ```

------

1. Choose **Create Policy**.

**To assign the access policy to the IAM user**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Users**.

1. Choose the IAM user to whom you will assign the access policy.

1. In the **Permissions** area, for **Managed Policies**, choose **Attach Policy**.

1. Select the policy you just created (for example, **AWSDeviceFarmAccessPolicy**). 

1. Choose **Attach Policy**.

### Step 3: Configuring the Jenkins CI plugin for the first time in AWS Device Farm
<a name="jenkins-ci-first-time-configuration-instructions"></a>

The first time you run your Jenkins server, you will need to configure the system as follows.

**Note**  
 If you are using [device slots](#how-to-purchase-device-slots), the device slots feature is disabled by default. 

1. Log into your Jenkins Web user interface.

1. On the left-hand side of the screen, choose **Manage Jenkins**.

1. Choose **Configure System**.

1. Scroll down to the **AWS Device Farm** header.

1. Copy your security credentials from [Creating an IAM user for your Jenkins CI Plugin](#jenkins-ci-set-up-iam-user) and paste your Access Key ID and Secret Access Key into their respective boxes.

1. Choose **Save**.

### Step 4: Using the plugin in a Jenkins job
<a name="jenkins-ci-using-plugin-jenkins-job"></a>

Once you have installed the Jenkins plugin, follow these instructions to use the plugin in a Jenkins job.

1. Log into your Jenkins web UI.

1. Click the job you want to edit.

1. On the left-hand side of the screen, choose **Configure**.

1. Scroll down to the **Post-build Actions** header.

1. Click **Add post-build action** and select **Run Tests on AWS Device Farm**.

1. Select the project you would like to use.

1. Select the device pool you would like to use.

1. Select whether you'd like to have the test artifacts (such as the logs and screenshots) archived locally.

1. In **Application**, fill in the path to your compiled application.

1. Select the test you would like run and fill in all the required fields.

1. Choose **Save**.

## Integrating Device Farm with a Gradle build system
<a name="aws-device-farm-android-gradle-plugin"></a>

The Device Farm Gradle plugin provides AWS Device Farm integration with the Gradle build system in Android Studio. For more information, see [Gradle](https://gradle.org).

**Note**  
To download the Gradle plugin, go to [GitHub](https://github.com/awslabs/aws-device-farm-gradle-plugin) and follow the instructions in [Building the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-building).

The Device Farm Gradle Plugin provides Device Farm functionality from your Android Studio environment. You can kick off tests on real Android phones and tablets hosted by Device Farm.

This section contains a series of procedures to set up and use the Device Farm Gradle Plugin.

**Topics**
+ [Dependencies](#aws-device-farm-gradle-plugin-dependencies)
+ [Step 1: Building the AWS Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-building)
+ [Step 2: Setting up the AWS Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-setting-up)
+ [Step 3: Generating an IAM user in the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-generating-iam-user)
+ [Step 4: Configuring test types](#aws-device-farm-gradle-plugin-configuring-test-types)

### Dependencies
<a name="aws-device-farm-gradle-plugin-dependencies"></a>

**Runtime**
+ The Device Farm Gradle Plugin requires the AWS Mobile SDK 1.10.15 or later. For more information and to install the SDK, see [AWS Mobile SDK](https://aws.amazon.com/mobile/sdk/).
+ Android tools builder test api 0.5.2
+ Apache Commons Lang3 3.3.4

**For Unit Tests**
+ Testng 6.8.8
+ Jmockit 1.19
+ Android gradle tools 1.3.0

### Step 1: Building the AWS Device Farm Gradle plugin
<a name="aws-device-farm-gradle-plugin-building"></a>

This plugin provides AWS Device Farm integration with the Gradle build system in Android Studio. For more information, see [Gradle](https://gradle.org).

**Note**  
Building the plugin is optional. The plugin is published through Maven Central. If you wish to allow Gradle to download the plugin directly, skip this step and jump to [Step 2: Setting up the AWS Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-setting-up).

**To build the plugin**

1. Go to [GitHub](https://github.com/awslabs/aws-device-farm-gradle-plugin) and clone the repository.

1. Build the plugin using `gradle install`.

   The plugin is installed to your local maven repository.

Next step: [Step 2: Setting up the AWS Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-setting-up)

### Step 2: Setting up the AWS Device Farm Gradle plugin
<a name="aws-device-farm-gradle-plugin-setting-up"></a>

If you haven't done so already, clone the repository and install the plugin using the procedure here: [Building the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-building).

**To configure the AWS Device Farm Gradle Plugin**

1. Add the plugin artifact to your dependency list in `build.gradle`.

   ```
       buildscript {
   
           repositories {        
               mavenLocal()            
               mavenCentral()            
           }
   
           dependencies {        
               classpath 'com.android.tools.build:gradle:1.3.0'           
               classpath 'com.amazonaws:aws-devicefarm-gradle-plugin:1.0'            
           }        
       }
   ```

1. Configure the plugin in your `build.gradle` file. The following test specific configuration should serve as your guide:

   ```
   apply plugin: 'devicefarm'
   
   devicefarm {
   
       // Required. The project must already exist. You can create a project in the AWS Device Farm console.
       projectName "My Project" // required: Must already exist.
   
       // Optional. Defaults to "Top Devices"
       // devicePool "My Device Pool Name"
       
       // Optional. Default is 150 minutes
       // executionTimeoutMinutes 150
       
       // Optional. Set to "off" if you want to disable device video recording during a run. Default is "on"
       // videoRecording "on"
       
       // Optional. Add this if you have a subscription and want to use your unmetered slots
       // useUnmeteredDevices()
       
       // Required. You must specify either accessKey and secretKey OR roleArn. roleArn takes precedence. 
       authentication {
           accessKey "AKIAIOSFODNN7EXAMPLE"
           secretKey "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
           
           // OR
           
           roleArn "arn:aws:iam::111122223333:role/DeviceFarmRole"
       }
   
       // Optionally, you can 
       // - enable or disable Wi-Fi, Bluetooth, GPS, NFC radios
       // - set the GPS coordinates
       // - specify files and applications that must be on the device when your test runs
       devicestate {
           // Extra files to include on the device.
           // extraDataZipFile file("path/to/zip")
           
           // Other applications that must be installed in addition to yours. 
           // auxiliaryApps files(file("path/to/app"), file("path/to/app2"))
           
           // By default, Wi-Fi, Bluetooth, GPS, and NFC are turned on.
           // wifi "off"
           // bluetooth "off"
           // gps "off"
           // nfc "off"
           
           // You can specify GPS location. By default, this location is 47.6204, -122.3491
           // latitude 44.97005
           // longitude -93.28872
       }
    
       // By default, the Instrumentation test is used.
       // If you want to use a different test type, configure it here.
       // You can set only one test type (for example, Calabash, Fuzz, and so on)
    
       // Fuzz
       // fuzz { }
   
       // Calabash
       // calabash { tests file("path-to-features.zip") }
          
   }
   ```

1. Run your Device Farm test using the following task: `gradle devicefarmUpload`.

   The build output will print out a link to the Device Farm console where you can monitor your test execution.

Next step: [Generating an IAM user in the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-generating-iam-user)

### Step 3: Generating an IAM user in the Device Farm Gradle plugin
<a name="aws-device-farm-gradle-plugin-generating-iam-user"></a>

AWS Identity and Access Management (IAM) helps you manage permissions and policies for working with AWS resources. This topic walks you through generating an IAM user with permissions to access AWS Device Farm resources.

If you haven't done so already, complete steps 1 and 2 before generating an IAM user.

We recommend that you do not use your AWS root account to access Device Farm. Instead, create a new IAM user (or use an existing IAM user) in your AWS account, and then access Device Farm with that IAM user.

**Note**  
The AWS root account or IAM user that you use to complete the following steps must have permission to create the following IAM policy and attach it to the IAM user. For more information, see [Working with Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies_manage.html).

**To create a new user with the proper access policy in IAM**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Users**.

1. Choose **Create New Users**.

1. Enter the user name of your choice.

   For example, **GradleUser**.

1. Choose **Create**.

1. Choose **Download Credentials** and save them in a location where you can easily retrieve them later.

1. Choose **Close**.

1. Choose the user name in the list.

1. Under **Permissions**, expand the **Inline Policies** header by clicking the down arrow on the right.

1. Choose **Click here** where it says, **There are no inline policies to show. To create one, click here**.

1. On the **Set Permissions** screen, choose **Custom Policy**.

1. Choose **Select**.

1. Give your policy a name, such as **AWSDeviceFarmGradlePolicy**.

1. Paste the following policy into **Policy Document**.

------
#### [ JSON ]

****  

   ```
       {
           "Version":"2012-10-17",		 	 	 
           "Statement": [
               {
                   "Sid": "DeviceFarmAll",
                   "Effect": "Allow",
                   "Action": [ "devicefarm:*" ],
                   "Resource": [ "*" ]
               }
           ]
       }
   ```

------

1. Choose **Apply Policy**.

Next step: [Configuring test types](#aws-device-farm-gradle-plugin-configuring-test-types).

For more information, see [Creating an IAM User (AWS Management Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_SettingUpUser.html#Using_CreateUser_console) or [Setting up](#setting-up).

### Step 4: Configuring test types
<a name="aws-device-farm-gradle-plugin-configuring-test-types"></a>

By default, the AWS Device Farm Gradle plugin runs the [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation) test. If you want to run your own tests or specify additional parameters, you can choose to configure a test type. This topic provides information about each available test type and what you need to do in Android Studio to configure it for use. For more information about the available test types in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](#test-types).

If you haven't done so already, complete steps 1 – 3 before configuring test types.

**Note**  
If you are using [device slots](#how-to-purchase-device-slots), the device slots feature is disabled by default.

#### Appium
<a name="configuring-test-types-appium"></a>

Device Farm provides support for Appium Java JUnit and TestNG for Android.
+ [Appium (under Java (JUnit))](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium.html)
+ [Appium (under Java (TestNG))](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium.html)

You can choose `useTestNG()` or `useJUnit()`. `JUnit` is the default and does not need to be explicitly specified.

```
    appium {
        tests file("path to zip file") // required
        useTestNG() // or useJUnit()
    }
```

#### Built-in: fuzz
<a name="configuring-test-types-built-in-fuzz"></a>

Device Farm provides a built-in fuzz test type, which randomly sends user interface events to devices and then reports the results.

```
    fuzz {

       eventThrottle 50 // optional default
       eventCount 6000  // optional default
       randomizerSeed 1234 // optional default blank

     }
```

For more information, see [Running Device Farm's built-in fuzz test (Android and iOS)](#test-types-built-in-fuzz).

#### Instrumentation
<a name="configuring-test-types-instrumentation"></a>

Device Farm provides support for instrumentation (JUnit, Espresso, Robotium, or any instrumentation-based tests) for Android. For more information, see [Instrumentation for Android and AWS Device Farm](#test-types-android-instrumentation).

When running an instrumentation test in Gradle, Device Farm uses the `.apk` file generated from your **androidTest** directory as the source of your tests.

```
    instrumentation { 

        filter "test filter per developer docs" // optional

    }
```

# AWS Device Farm document history
<a name="history"></a>

The following table describes the important changes to the documentation since the last release of this guide.


| Change | Description | Date Changed | 
| --- | --- | --- | 
| Xcode 27 support |  Device Farm now offers Xcode 27 on the macos\_tahoe test host, supporting iOS 18 to 27. See [Supported software within custom test environments](#custom-test-environments-hosts-software) to learn more.  | September 14, 2026 | 
| Test Insights reports |  Test Insights reports are now available for supported frameworks in custom test environments. Test Insights include passed, failed, skipped, and errored test counts for each job and run; detailed test output with timestamps and stack traces; and test and job execution times. See [Test Insights](#reports-test-insights) to learn more.  | August 6, 2026 | 
| macos\_tahoe iOS test host |  Device Farm now supports the macos\_tahoe test host (macOS Tahoe, version 26) with an updated set of [Supported software within custom test environments](#custom-test-environments-hosts-software).  | August 3, 2026 | 
| Appium endpoint support |  Device Farm now offers a fully-managed Appium endpoint for remote device testing, enabling quick test development and debugging. This complements the existing server-side execution method, where tests are uploaded and run directly on Device Farm. While server-side execution is ideal for CI/CD pipelines and large-scale testing, the new local Appium endpoint allows faster iteration and development of tests on real devices.  | November 17, 2025 | 
| iOS test host improvements |  Device Farm now supports an updated experience for the iOS test environment, enabling consistency in setups between Android and iOS tests. See [Hosts for custom test environments](#custom-test-environments-hosts) to learn more. <br /> Additionally, information related to retired Android test hosts have been removed. Android users are encouraged to use the [Amazon Linux 2 test hosts](#custom-test-environments-hosts).  | October 31, 2025 | 
| AL2 support | Device Farm now supports the AL2 test environment for Android. Learn more about [AL2](https://docs.aws.amazon.com/devicefarm/latest/developerguide/amazon-linux-2.html). | November 6, 2023 | 
| Migration from Standard to Custom test environments | Updated [migration guide](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-migration.html) to document deprecation for standard mode tests in December 2023. | September 3, 2023 | 
| VPC ENI support | Device Farm now allows private devices to use the VPC-ENI connectivity feature to help customers securely connect to their private endpoints hosted on AWS, on-premise software, or another cloud provider. Learn nore about [VPC-ENI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni.html). | May 15, 2023 | 
| Polaris UI updates | The Device Farm console now supports the Polaris framework. | July 28, 2021 | 
| Python 3 support | Device Farm now supports Python 3 in custom mode tests. Learn more about using Python 3 in your test packages:+  [Appium (Python)](#test-types-ios-appium-python) <br />+  [Appium (Python)](#test-types-android-appium-python)  | April 20, 2020 | 
| New security information and information on tagging AWS resources. |  To make securing AWS services easier and more comprehensive, a new section on security has been built. To read more, see [Security in AWS Device Farm](#security) <br />A new section on tagging in Device Farm has been added. To learn more about tagging, see [Tagging in Device Farm](#tagging).  |  March 27, 2020  | 
| Removal of Direct Device Access. | Direct Device Access (remote debugging on private devices) is no longer available for general usage. For inquiries into future availability of Direct Device Access, please [contact us](mailto:aws-devicefarm-support@amazon.com). | September 9, 2019 | 
| Update Gradle plugin configuration | A revised Gradle plugin configuration now includes a customizable version of the gradle configuration, with optional parameters commented out. Learn more about [Setting up the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-setting-up). | August 16, 2019 | 
| New requirement for test runs with XCTest | For test runs that use the XCTest framework, Device Farm now requires an app package that is built for testing. Learn more about [Integrating Device Farm with XCTest for iOS](#test-types-ios-xctest). | February 4, 2019 | 
| Support for Appium Node.js and Appium Ruby test types in custom environments | You can now run your tests in both Appium Node.js and Appium Ruby custom test environments. Learn more about [Test frameworks and built-in tests in AWS Device Farm](#test-types). | January 10, 2019 | 
| Support for Appium server version 1.7.2 in both standard and custom environments. Support for version 1.8.1 using a custom test spec YAML file in a custom test environment. | You can now run your tests in both standard and custom test environments with Appium server versions 1.72, 1.71, and 1.6.5. You can also run your tests with versions 1.8.1 and 1.8.0 using a custom test spec YAML file in a custom test environment. Learn more about [Test frameworks and built-in tests in AWS Device Farm](#test-types).  | October 2, 2018 | 
| Custom test environments | With a custom test environment, you can ensure your tests run like they do in your local environment. Device Farm now provides support for live log and video streaming, so you can get instant feedback on your tests that are run in a custom test environment. Learn more about [Custom test environments in AWS Device Farm](#custom-test-environments). | August, 16 2018 | 
| Support for using Device Farm as an AWS CodePipeline test provider | You can now configure a pipeline in AWS CodePipeline to use AWS Device Farm runs as test actions in your release process. CodePipeline enables you to quickly link your repository to build and test stages to achieve a continuous integration system customized to your needs. Learn more about [Integrating AWS Device Farm in a CodePipeline test stage](#codepipeline). | July, 19 2018 | 
| Support for Private Devices | You can now use private devices to schedule test runs and start remote access sessions. You can manage profiles and settings for these devices, create Amazon VPC endpoints to test private apps, and create remote debugging sessions. Learn more about [Private devices in AWS Device Farm](#working-with-private-devices). | May 2, 2018 | 
| Support for Appium 1.6.3 | You can now set the Appium version for your Appium custom tests. | March 21, 2017 | 
| Set the execution timeout for test runs | You can set the execution timeout for a test run or for all tests in a project. Learn more about [Setting the execution timeout for test runs in AWS Device Farm](#how-to-set-default-timeout-for-test-runs). | February 9, 2017 | 
| Network Shaping | You can now simulate network connections and conditions for a test run. Learn more about [Simulating network connections and conditions for your AWS Device Farm runs](#how-to-simulate-network-connections-and-conditions). | December 8, 2016 | 
| New Troubleshooting Section | You can now troubleshoot test package uploads using a set of procedures designed to resolve error messages you might encounter in the Device Farm console. Learn more about [Troubleshooting Device Farm errors](#troubleshooting). | August 10, 2016 | 
| Remote Access Sessions | You can now remotely access and interact with a single device in the console. Learn more about [Remote access](#remote-access). | April 19, 2016 | 
| Device Slots Self-Service | You can now purchase device slots using the AWS Management Console, the AWS Command Line Interface, or the API. Learn more about how to [Purchasing a device slot in Device Farm](#how-to-purchase-device-slots). | March 22, 2016 | 
| How to stop test runs | You can now stop test runs using the AWS Management Console, the AWS Command Line Interface, or the API. Learn more about how to [Stopping a run in AWS Device Farm](#how-to-stop-test-runs). | March 22, 2016 | 
| New XCTest UI test types | You can now run XCTest UI custom tests on iOS applications. Learn more about the [Integrating XCTest UI for iOS with Device Farm](#test-types-ios-xctest-ui) test type. | March 8, 2016 | 
| New Appium Python test types | You can now run Appium Python custom tests on Android, iOS, and web applications. Learn more about [Test frameworks and built-in tests in AWS Device Farm](#test-types). | January 19, 2016 | 
| Web Application test types | You can now run Appium Java JUnit and TestNG custom tests on web applications. Learn more about [Web app tests in AWS Device Farm](#test-types-web-app-tests). | November 19, 2015 | 
| AWS Device Farm Gradle Plugin | Learn more about how to install and use the [Device Farm Gradle plugin](#aws-device-farm-android-gradle-plugin). | September 28, 2015 | 
| New Android Built-in Test: Explorer | The explorer test crawls your app by analyzing each screen as if it were an end user and takes screenshots as it explores. | September 16, 2015 | 
| iOS support added | Learn more about testing iOS devices and running iOS tests (including XCTest) in [Test frameworks and built-in tests in AWS Device Farm](#test-types). | August 4, 2015 | 
| Initial public release | This is the initial public release of the *AWS Device Farm Developer Guide*. | July 13, 2015 | 

# AWS Glossary
<a name="glossary"></a>

For the latest AWS terminology, see the [AWS glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) in the *AWS Glossary Reference*.