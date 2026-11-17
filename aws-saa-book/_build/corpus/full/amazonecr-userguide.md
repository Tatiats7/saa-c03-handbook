# Amazon ECR User Guide

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
+ [What is Amazon Elastic Container Registry?](#what-is-ecr)
   + [Concepts and components of Amazon ECR](#concept-and-components)
   + [Common use cases in Amazon ECR](#ecr-use-cases)
+ [Moving an image through its lifecycle in Amazon ECR](#getting-started-cli)
+ [Migrate container images from a third-party registry](#migrate-from-third-party)
+ [Optimizing performance for Amazon ECR](#performance)
+ [Making requests to Amazon ECR registries](#ecr-requests)
+ [Amazon ECR private registry](#Registries)
   + [Private registry authentication in Amazon ECR](#registry_auth)
   + [Private registry settings in Amazon ECR](#registry-settings)
   + [Blob mounting in Amazon ECR](#blob-mounting)
   + [Private registry permissions in Amazon ECR](#registry-permissions)
      + [Private registry policy examples for Amazon ECR](#registry-permissions-examples)
      + [Granting registry permissions for cross account replication in Amazon ECR](#registry-permissions-create-replication)
      + [Granting registry permissions for pull through cache in Amazon ECR](#registry-permissions-create-pullthroughcache)
+ [Amazon ECR private repositories](#Repositories)
   + [Creating an Amazon ECR private repository to store images](#repository-create)
   + [Viewing the contents and details of a private repository in Amazon ECR](#repository-info)
   + [Deleting a private repository in Amazon ECR](#repository-delete)
   + [Private repository policies in Amazon ECR](#repository-policies)
      + [Private repository policy examples in Amazon ECR](#repository-policy-examples)
      + [Setting a private repository policy statement in Amazon ECR](#set-repository-policy)
   + [Tagging a private repository in Amazon ECR](#ecr-using-tags)
      + [Adding tags to a private repository in Amazon ECR](#adding-tags-repositories)
      + [Deleting tags from a private repository in Amazon ECR](#deleting-tags-repositories)
+ [Private images in Amazon ECR](#images)
   + [Pushing an image to an Amazon ECR private repository](#image-push)
      + [IAM permissions for pushing an image to an Amazon ECR private repository](#image-push-iam)
      + [Pushing a Docker image to an Amazon ECR private repository](#docker-push-ecr-image)
      + [Pushing a multi-architecture image to an Amazon ECR private repository](#docker-push-multi-architecture-image)
      + [Pushing a Helm chart to an Amazon ECR private repository](#push-oci-artifact)
   + [Deleting signatures and other artifacts from an Amazon ECR private repository](#image-artifact-delete)
   + [Viewing image details in Amazon ECR](#image-info)
   + [Pulling an image to your local environment from an Amazon ECR private repository](#docker-pull-ecr-image)
   + [Pulling the Amazon Linux container image](#amazon_linux_container_image)
   + [Deleting an image in Amazon ECR](#delete_image)
   + [Archiving an image in Amazon ECR](#archive_restore_image)
      + [Archiving an image](#archive-image)
      + [Restoring an image](#restore-image)
   + [Retagging an image in Amazon ECR](#image-retag)
   + [Preventing image tags from being overwritten in Amazon ECR](#image-tag-mutability)
   + [Container image manifest format support in Amazon ECR](#image-manifest-formats)
   + [Using Amazon ECR images with Amazon ECS](#ECR_on_ECS)
   + [Using Amazon ECR Images with Amazon EKS](#ECR_on_EKS)
      + [Installing a Helm chart on an Amazon EKS cluster](#using-helm-charts-eks)
+ [Sign images in Amazon ECR](#image-signing)
   + [Managed signing](#managed-signing)
   + [Signature verification](#image-signing-verification)
   + [Manual signing](#image-signing-manual)
+ [Scan images for software vulnerabilities in Amazon ECR](#image-scanning)
   + [Filters to choose which repositories are scanned in Amazon ECR](#image-scanning-filters)
   + [Scan images for OS and programming language package vulnerabilities in Amazon ECR](#image-scanning-enhanced)
      + [IAM permissions required for enhanced scanning in Amazon ECR](#image-scanning-enhanced-iam)
      + [Configuring enhanced scanning for images in Amazon ECR](#image-scanning-enhanced-enabling)
      + [EventBridge events sent for enhanced scanning in Amazon ECR](#image-scanning-enhanced-events)
      + [Retrieving the findings for enhanced scans in Amazon ECR](#image-scanning-enhanced-describe-scan-findings)
   + [Scan images for OS vulnerabilities in Amazon ECR](#image-scanning-basic)
      + [Configuring basic scanning for images in Amazon ECR](#image-scanning-basic-enabling)
      + [Manually scanning an image for OS vulnerabilities in Amazon ECR](#manual-scan)
      + [Retrieving the findings for basic scans in Amazon ECR](#describe-scan-findings)
   + [Troubleshooting image scanning in Amazon ECR](#image-scanning-troubleshooting)
+ [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache)
   + [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](#pull-through-cache-iam)
   + [Setting up permissions for cross-account ECR to ECR PTC](#pull-through-cache-private)
   + [Creating a pull through cache rule in Amazon ECR](#pull-through-cache-creating-rule)
   + [Validating pull through cache rules in Amazon ECR](#pull-through-cache-working-validating)
   + [Pulling an image with a pull through cache rule in Amazon ECR](#pull-through-cache-working-pulling)
   + [Storing your upstream repository credentials in an AWS Secrets Manager secret](#pull-through-cache-creating-secret)
   + [Customizing repository prefixes for ECR to ECR pull through cache](#pull-through-cache-private-wildcards)
   + [Troubleshooting pull through cache issues in Amazon ECR](#error-pullthroughcache)
+ [Private image replication in Amazon ECR](#replication)
   + [Private image replication examples for Amazon ECR](#registry-settings-examples)
   + [Configuring private image replication in Amazon ECR](#registry-settings-configure)
   + [Removing private image replication settings in Amazon ECR](#registry-settings-remove)
+ [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates)
   + [Creating a repository creation template in Amazon ECR](#repository-creation-templates-create)
      + [Create a custom policy for repository creation templates](#repository-creation-templates-custom)
      + [Create an IAM role for repository creation templates](#repository-creation-templates-create-iam)
   + [Updating a repository creation template](#repository-creation-templates-updating)
   + [Deleting a repository creation template in Amazon ECR](#repository-creation-templates-delete)
+ [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies)
   + [Creating a lifecycle policy preview in Amazon ECR](#lpp_creation)
   + [Creating a lifecycle policy for a repository in Amazon ECR](#lp_creation)
   + [Examples of lifecycle policies in Amazon ECR](#lifecycle_policy_examples)
   + [Lifecycle policy properties in Amazon ECR](#lifecycle_policy_parameters)
+ [Pull-time update exclusions](#pull-time-update-exclusions)
   + [Managing pull-time update exclusions](#pull-time-update-exclusions-manage)
   + [Considerations for pull-time update exclusions](#pull-time-update-exclusions-considerations)
+ [Security in Amazon Elastic Container Registry](#security)
   + [Identity and Access Management for Amazon Elastic Container Registry](#security-iam)
      + [How Amazon Elastic Container Registry works with IAM](#security_iam_service-with-iam)
      + [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples)
      + [Using Tag-Based Access Control](#ecr-supported-iam-actions-tagging)
      + [AWS managed policies for Amazon Elastic Container Registry](#security-iam-awsmanpol)
      + [Using service-linked roles for Amazon ECR](#using-service-linked-roles)
         + [Amazon ECR service-linked role for replication](#slr-replication)
         + [Amazon ECR service-linked role for pull through cache](#slr-pullthroughcache)
         + [Amazon ECR service-linked role for repository creation templates](#slr-rct)
      + [Troubleshooting Amazon Elastic Container Registry Identity and Access](#security_iam_troubleshoot)
   + [Data protection in Amazon ECR](#data-protection)
      + [Encryption at rest](#encryption-at-rest)
   + [Compliance validation for Amazon Elastic Container Registry](#ecr-compliance)
   + [Infrastructure Security in Amazon Elastic Container Registry](#infrastructure-security)
      + [Amazon ECR interface VPC endpoints (AWS PrivateLink)](#vpc-endpoints)
   + [Cross-service confused deputy prevention](#cross-service-confused-deputy-prevention)
+ [Amazon ECR monitoring](#monitoring)
   + [Visualizing your service quotas and setting alarms](#monitoring-quotas-alarms)
   + [Amazon ECR usage metrics](#monitoring-usage)
   + [Amazon ECR usage reports](#usage-reports)
   + [Amazon ECR repository metrics](#ecr-repository-metrics)
   + [Amazon ECR events and EventBridge](#ecr-eventbridge)
   + [Logging Amazon ECR actions with AWS CloudTrail](#logging-using-cloudtrail)
+ [Using Amazon ECR with an AWS SDK](#sdk-general-information-section)
+ [Code examples for Amazon ECR using AWS SDKs](#service_code_examples)
   + [Basic examples for Amazon ECR using AWS SDKs](#service_code_examples_basics)
      + [Hello Amazon ECR](#example_ecr_Hello_section)
      + [Learn the basics of Amazon ECR with an AWS SDK](#example_ecr_Scenario_RepositoryManagement_section)
      + [Actions for Amazon ECR using AWS SDKs](#service_code_examples_actions)
         + [Use CreateRepository with an AWS SDK or CLI](#example_ecr_CreateRepository_section)
         + [Use DeleteRepository with an AWS SDK or CLI](#example_ecr_DeleteRepository_section)
         + [Use DescribeImages with an AWS SDK or CLI](#example_ecr_DescribeImages_section)
         + [Use DescribeRepositories with an AWS SDK or CLI](#example_ecr_DescribeRepositories_section)
         + [Use GetAuthorizationToken with an AWS SDK or CLI](#example_ecr_GetAuthorizationToken_section)
         + [Use GetRepositoryPolicy with an AWS SDK or CLI](#example_ecr_GetRepositoryPolicy_section)
         + [Use ListImages with an AWS SDK or CLI](#example_ecr_ListImages_section)
         + [Use PushImageCmd with an AWS SDK](#example_ecr_PushImageCmd_section)
         + [Use PutLifeCyclePolicy with an AWS SDK or CLI](#example_ecr_PutLifeCyclePolicy_section)
         + [Use SetRepositoryPolicy with an AWS SDK or CLI](#example_ecr_SetRepositoryPolicy_section)
         + [Use StartLifecyclePolicyPreview with an AWS SDK or CLI](#example_ecr_StartLifecyclePolicyPreview_section)
   + [Scenarios for Amazon ECR using AWS SDKs](#service_code_examples_scenarios)
      + [Getting started with container registries](#example_ecr_GettingStarted_078_section)
+ [Amazon ECR service quotas](#service-quotas)
+ [Amazon ECR troubleshooting](#troubleshooting)
   + [Troubleshooting Docker commands and issues when using Amazon ECR](#common-errors-docker)
   + [Troubleshooting Amazon ECR error messages](#common-errors)
+ [Using Podman with Amazon ECR](#Podman)
+ [Document history](#doc-history)

-----



# What is Amazon Elastic Container Registry?
<a name="what-is-ecr"></a>

Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container image registry service that is secure, scalable, and reliable. Amazon ECR supports private repositories with resource-based permissions using AWS IAM. This is so that specified users or Amazon EC2 instances can access your container repositories and images. You can use your preferred CLI to push, pull, and manage Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts.

**Note**  
Amazon ECR supports public container image repositories as well. For more information, see [What is Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/what-is-ecr.html) in the *Amazon ECR Public User Guide*.

The AWS container services team maintains a public roadmap on GitHub. It contains information about what the teams are working on and allows all AWS customers the ability to give direct feedback. For more information, see [AWS Containers Roadmap](https://github.com/aws/containers-roadmap).

## Features of Amazon ECR
<a name="ecr-features"></a>

Amazon ECR provides the following features:
+ Lifecycle policies help with managing the lifecycle of the images in your repositories. You define rules that result in the cleaning up of unused images. You can test rules before applying them to your repository. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies).
+ Image scanning helps in identifying software vulnerabilities in your container images. Each repository can be configured to **scan on push**. This ensures that each new image pushed to the repository is scanned. You can then retrieve the results of the image scan. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).
+ Cross-Region and cross-account replication makes it easier for you to have your images where you need them. This is configured as a registry setting and is on a per-Region basis. For more information, see [Private registry settings in Amazon ECR](#registry-settings).
+ Pull through cache rules provide a way to cache repositories in an upstream registry in your private Amazon ECR registry. Using a pull through cache rule, Amazon ECR will periodically reach out to the upstream registry to ensure the cached image in your Amazon ECR private registry is up to date. For more information, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache).
+ Repository creation templates allow you to define the settings for repositories created by Amazon ECR on your behalf during pull through cache, create on push, or replication actions. You can specify tag immutability, encryption configuration, repository policies, lifecycle policies, and resource tags for automatically created repositories. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).
+ Managed signing automatically generates cryptographic signatures when images are pushed to Amazon ECR, simplifying container image signing. For more information, see [Managed signing](#managed-signing).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## How to get started with Amazon ECR
<a name="ecr-get-started"></a>

If you are using Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS), note that the setup for those two services is similar to the setup for Amazon ECR because Amazon ECR is an extension of both services.

When using the AWS Command Line Interface with Amazon ECR, use a version of the AWS CLI that supports the latest Amazon ECR features. If you don't see support for an Amazon ECR feature in the AWS CLI, upgrade to the latest version of the AWS CLI. For information about installing the latest version of the AWS CLI, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

To learn how to push a container image to a private Amazon ECR repository using the AWS CLI and Docker, see [Moving an image through its lifecycle in Amazon ECR](#getting-started-cli).

## Pricing for Amazon ECR
<a name="ecr-pricing"></a>

With Amazon ECR, you pay for the amount of data you store in your repositories, data transfer from your image pushes and pulls, and image actions that you opt in to such as image signing and replication. For more information, see [Amazon ECR pricing](https://aws.amazon.com/ecr/pricing/).

## Concepts and components of Amazon ECR
<a name="concept-and-components"></a>

Amazon ECR is a fully managed Docker container registry service provided by AWS. It allows you to store, manage, and deploy Docker container images securely and reliably. These concepts and components work together to provide a secure, scalable, and reliable Docker container registry service within the AWS, enabling you to efficiently manage and deploy your containerized applications. 

Here are some key concepts and components of Amazon ECR: 

**Registry**  
An Amazon ECR registry is a private repository provided to each AWS account, where you can create one or more repositories. These repositories allow you to store and distribute Docker images, Open Container Initiative (OCI) images, and other OCI-compatible artifacts within your AWS environment. For more information, see [Amazon ECR private registry](#Registries).

**Authorization token**  
Your client must authenticate to an Amazon ECR private registry as an AWS user before it can push and pull images. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

**Repository**  
A repository in Amazon ECR is a logical collection where you can store your Docker images, Open Container Initiative (OCI) images, and other OCI-compatible artifacts. Within a single Amazon ECR registry, you can have multiple repositories to organize your container images. For more information, see [Amazon ECR private repositories](#Repositories).

**Repository policy**  
You can control access to your repositories and the contents within them with repository policies. For more information, see [Private repository policies in Amazon ECR](#repository-policies).

**Image**  
You can push and pull container images to your repositories. You can use these images locally on your development system, or you can use them in Amazon ECS task definitions and Amazon EKS pod specifications. For more information, see [Using Amazon ECR images with Amazon ECS](#ECR_on_ECS) and [Using Amazon ECR Images with Amazon EKS](#ECR_on_EKS).

**Lifecycle Policy**  
 Amazon ECR lifecycle policies allow you to manage the lifecycle of your images by defining rules for pruning and expiring old or unused images. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies).

**Image Scanning**  
Amazon ECR provides an integrated image scanning capability that helps identify software vulnerabilities in your container images. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).

**Access Control**  
 Amazon ECR uses IAM to control access to your repositories. You can create IAM users, groups, and roles with specific permissions to push, pull, or manage Amazon ECR repositories. For more information, see [Security in Amazon Elastic Container Registry](#security).

**Cross-account and Cross-region Replication**  
 Amazon ECR supports replicating images across multiple AWS accounts and regions for increased availability and reduced latency. For more information, see [Private image replication in Amazon ECR](#replication).

 **Encryption**  
 Amazon ECR supports server-side encryption of your Docker images at rest using AWS KMS. For more information, see [Data protection in Amazon ECR](#data-protection).

**AWS Command Line Interface Integration**  
The AWS CLI provides commands to interact with Amazon ECR repositories, such as creating, listing, pushing, and pulling images.

**AWS Management Console**  
 Amazon ECR can also be managed through the AWS Management Console, providing a user-friendly web interface for working with your repositories and images. 

**AWS CloudTrail**  
Amazon ECR integrates with AWS CloudTrail, allowing you to log and audit API calls made to Amazon ECR for security and compliance purposes. For more information, see [Logging Amazon ECR actions with AWS CloudTrail](#logging-using-cloudtrail).

**Amazon CloudWatch**  
Amazon ECR provides metrics and logs that can be monitored using Amazon CloudWatch, enabling you to track the performance and usage of your Amazon ECR repositories. For more information, see [Amazon ECR repository metrics](#ecr-repository-metrics).

**Managed signing**  
Managed signing automatically generates cryptographic signatures when images are pushed to Amazon ECR, simplifying container image signing. For more information, see [Managed signing](#managed-signing).

## Common use cases in Amazon ECR
<a name="ecr-use-cases"></a>

Amazon ECR is a fully-managed Docker container registry service offered by AWS. It provides a secure and scalable repository for storing and distributing Docker container images, making it an essential component in containerized application deployments. Amazon ECR simplifies the process of building, distributing, and running containerized applications across various AWS services and on-premises environments. 

Here are some key use cases for Amazon ECR:

**Container Image Storage and Distribution**  
 Amazon ECR serves as a centralized repository for storing and distributing Docker container images within an organization or for public consumption. Developers can push their container images to Amazon ECR and then pull them from any compute environment within AWS, such as Amazon EC2, AWS Fargate, or Amazon EKS. For more information, see [Amazon ECR private repositories](#Repositories).

**Continuous Integration and Continuous Deployment (CI/CD)**  
Amazon ECR integrates seamlessly with AWS CodeBuild, AWS CodePipeline, and other CI/CD tools, enabling automated building, testing, and deployment of containerized applications. Container images can be automatically pushed to Amazon ECR as part of the CI/CD pipeline, ensuring consistent and reliable deployment across different environments.

**Microservices Architecture**  
Amazon ECR is well suited for microservices architectures, where applications are broken down into smaller, decoupled services packaged as containers. Each microservice can have its own container image stored in Amazon ECR, enabling independent development, deployment, and scaling of individual services.

**Hybrid and Multi-Cloud Deployments**  
 Amazon ECR supports the ability to pull container images from other container registries, such as Docker Hub or third party registries. This allows organizations to maintain a consistent deployment model across hybrid or multi-cloud environments, using Amazon ECR as the central repository for container images.

**Access Control and Security**  
Amazon ECR provides fine-grained access control mechanisms, allowing organizations to control who can push or pull container images from the registry. It also integrates with AWS Identity and Access Management for authentication and authorization, ensuring secure access to container images. For more information, see [Security in Amazon Elastic Container Registry](#security).

**Image Vulnerability Scanning**  
Amazon ECR offers automatic scanning of container images for software vulnerabilities and potential misconfiguration, helping to maintain a secure and compliant container environment. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).

**Private Container Registry**  
For organizations with strict security or compliance requirements, Amazon ECR can be used as a private container registry, ensuring that sensitive container images are not exposed to public registries and are accessible only within the organization's AWS environment. For more information, see [Amazon ECR private registry](#Registries).

**Globally Distributed Application Deployment with Amazon ECR Replication**  
Leveraging Amazon ECR replication capability, you can centralize your containerized web application images in a primary repository, enabling automated distribution across multiple AWS regions, ensuring consistent global deployments with low latency worldwide and reducing operational burden. For more information, see [Private image replication in Amazon ECR](#replication)

**Automated Cleanup of Stale Container Images**  
Amazon ECR lifecycle policies enable automated cleanup of stale container images based on defined rules such as age, count, or tags, optimizing storage costs, maintaining an organized registry, enhancing security and compliance, and streamlining development workflows through automation. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies) 

# Moving an image through its lifecycle in Amazon ECR
<a name="getting-started-cli"></a>

If you are using Amazon ECR for the first time, use the following steps with the Docker CLI and the AWS CLI to create a sample image, authenticate to the default registry, and create a private repository. Then push an image to and pull an image from the private repository. When you are finished with the sample image, delete the sample image and the repository.

To use the AWS Management Console instead of the AWS CLI, see [Creating an Amazon ECR private repository to store images](#repository-create).

For more information on the other tools available for managing your AWS resources, including the different AWS SDKs, IDE toolkits, and the Windows PowerShell command line tools, see [http://aws.amazon.com/tools/](http://aws.amazon.com/tools/).

## Prerequisites
<a name="getting-started-cli-prereqs"></a>

If you do not have the latest AWS CLI and Docker installed and ready to use, use the following steps to install both of these tools.

### Install the AWS CLI
<a name="cli-install"></a>

To use the AWS CLI with Amazon ECR, install the latest AWS CLI version. For information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide*.

### Install Docker
<a name="cli-install-docker"></a>

Docker is available on many different operating systems, including most modern Linux distributions, like Ubuntu, and even macOS and Windows. For more information about how to install Docker on your particular operating system, go to the [Docker installation guide](https://docs.docker.com/engine/installation/#installation).

You do not need a local development system to use Docker. If you are using Amazon EC2 already, you can launch an Amazon Linux 2023 instance and install Docker to get started.

If you already have Docker installed, skip to [Step 1: Create a Docker image](#cli-create-image).

**To install Docker on an Amazon EC2 instance using an Amazon Linux 2023 AMI**

1. Launch an instance with the latest Amazon Linux 2023 AMI. For more information, see [Launching an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html) in the *Amazon EC2 User Guide*.

1. Connect to your instance. For more information, see [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide*.

1. Update the installed packages and package cache on your instance.

   ```
   sudo yum update -y
   ```

1. Install the most recent Docker Community Edition package.

   ```
   sudo yum install docker
   ```

1. Start the Docker service.

   ```
   sudo service docker start
   ```

1. Add the `ec2-user` to the `docker` group so you can execute Docker commands without using `sudo`.

   ```
   sudo usermod -a -G docker ec2-user
   ```

1. Log out and log back in again to pick up the new `docker` group permissions. You can accomplish this by closing your current SSH terminal window and reconnecting to your instance in a new one. Your new SSH session will have the appropriate `docker` group permissions.

1. Verify that the `ec2-user` can run Docker commands without `sudo`.

   ```
   docker info
   ```
**Note**  
In some cases, you may need to reboot your instance to provide permissions for the `ec2-user` to access the Docker daemon. Try rebooting your instance if you see the following error:  

   ```
   Cannot connect to the Docker daemon. Is the docker daemon running on this host?
   ```

## Step 1: Create a Docker image
<a name="cli-create-image"></a>

In this step, you create a Docker image of a simple web application, and test it on your local system or Amazon EC2 instance.

**To create a Docker image of a simple web application**

1. Create a file called `Dockerfile`. A Dockerfile is a manifest that describes the base image to use for your Docker image and what you want installed and running on it. For more information about Dockerfiles, go to the [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/).

   ```
   touch Dockerfile
   ```

1. Edit the `Dockerfile` you just created and add the following content.

   ```
   FROM public.ecr.aws/amazonlinux/amazonlinux:latest
   
   # Install dependencies
   RUN yum update -y && \
    yum install -y httpd
   
   # Install apache and write hello world message
   RUN echo 'Hello World!' > /var/www/html/index.html
   
   # Configure apache
   RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
    echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
    echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
    chmod 755 /root/run_apache.sh
   
   EXPOSE 80
   
   CMD /root/run_apache.sh
   ```

   This Dockerfile uses the public Amazon Linux 2 image hosted on Amazon ECR Public. The `RUN` instructions update the package caches, installs some software packages for the web server, and then write the "Hello World\!" content to the web servers document root. The `EXPOSE` instruction exposes port 80 on the container, and the `CMD` instruction starts the web server.

1. <a name="sample-docker-build-step"></a>Build the Docker image from your Dockerfile.
**Note**  
Some versions of Docker may require the full path to your Dockerfile in the following command, instead of the relative path shown below.

   ```
   docker build -t hello-world .
   ```

1. List your container image.

   ```
   docker images --filter reference=hello-world
   ```

   Output:

   ```
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   hello-world         latest              e9ffedc8c286        4 minutes ago       194MB
   ```

1. Run the newly built image. The `-p 80:80` option maps the exposed port 80 on the container to port 80 on the host system. For more information about **docker run**, go to the [Docker run reference](https://docs.docker.com/engine/reference/run/).

   ```
   docker run -t -i -p 80:80 hello-world
   ```
**Note**  
Output from the Apache web server is displayed in the terminal window. You can ignore the "`Could not reliably determine the fully qualified domain name`" message.

1. Open a browser and point to the server that is running Docker and hosting your container.
   + If you are using an EC2 instance, this is the **Public DNS** value for the server, which is the same address you use to connect to the instance with SSH. Make sure that the security group for your instance allows inbound traffic on port 80.
   + If you are running Docker locally, point your browser to [http://localhost/](http://localhost/).
   + If you are using **docker-machine** on a Windows or Mac computer, find the IP address of the VirtualBox VM that is hosting Docker with the **docker-machine ip** command, substituting {{machine-name}} with the name of the docker machine you are using.

     ```
     docker-machine ip {{machine-name}}
     ```

   You should see a web page with your "Hello World\!" statement.

1. Stop the Docker container by typing **Ctrl \+ c**.

## Step 2: Create a repository
<a name="cli-create-repository"></a>

Now that you have an image to push to Amazon ECR, you must create a repository to hold it. In this example, you create a repository called `hello-repository` to which you later push the `hello-world:latest` image. To create a repository, run the following command:

```
aws ecr create-repository \
    --repository-name {{hello-repository}} \
    --region {{region}}
```

## Step 3: Authenticate to your default registry
<a name="cli-authenticate-registry"></a>

After you have installed and configured the AWS CLI, authenticate the Docker CLI to your default registry. That way, the **docker** command can push and pull images with Amazon ECR. The AWS CLI provides a **get-login-password** command to simplify the authentication process.

**Note**  
Your IAM principal must have the `ecr:GetAuthorizationToken` permission to authenticate to a registry. For more information, see [AWS managed policies for Amazon Elastic Container Registry](#security-iam-awsmanpol).

To authenticate Docker to an Amazon ECR registry with get-login-password, run the **aws ecr get-login-password** command. When passing the authentication token to the **docker login** command, use the value `AWS` for the username and specify the Amazon ECR registry URI you want to authenticate to. If authenticating to multiple registries, you must repeat the command for each registry.
**Important**  
If you receive an error, install or upgrade to the latest version of the AWS CLI. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide*.
+ [get-login-password](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html) (AWS CLI)

  ```
  aws ecr get-login-password --region {{region}} | docker login --username AWS --password-stdin {{{{aws_account_id}}}}.dkr.ecr.{{region}}.amazonaws.com
  ```
+ [Get-ECRLoginCommand](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ECRLoginCommand.html) (AWS Tools for Windows PowerShell)

  ```
  (Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin {{{{aws_account_id}}}}.dkr.ecr.{{region}}.amazonaws.com
  ```

## Step 4: Push an image to Amazon ECR
<a name="cli-push-image"></a>

Now you can push your image to the Amazon ECR repository you created in the previous section. Use the **docker** CLI to push images after the following prerequisites are met:
+ The minimum version of **docker** is installed: 1.7.
+ The Amazon ECR authorization token was configured with **docker login**.
+ The Amazon ECR repository exists and the user has access to push to the repository.

After those prerequisites are met, you can push your image to your newly created repository in the default registry for your account.

**To tag and push an image to Amazon ECR**

1. List the images you have stored locally to identify the image to tag and push.

   ```
   docker images
   ```

   Output:

   ```
   REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
   hello-world         latest              e9ffedc8c286        4 minutes ago       241MB
   ```

1. Tag the image to push to your repository.

   ```
   docker tag hello-world:latest {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/hello-repository
   ```

1. Push the image.

   ```
   docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/hello-repository:latest
   ```

   Output:

   ```
   The push refers to a repository [{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/hello-repository] (len: 1)
   e9ae3c220b23: Pushed
   a6785352b25c: Pushed
   0998bf8fb9e9: Pushed
   0a85502c06c9: Pushed
   latest: digest: sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636EXAMPLE size: 6774
   ```

## Step 5: Pull an image from Amazon ECR
<a name="cli-pull-image"></a>

After your image is pushed to your Amazon ECR repository, you can pull it from other locations. Use the **docker** CLI to pull images after the following prerequisites are met:
+ The minimum version of **docker** is installed: 1.7.
+ The Amazon ECR authorization token was configured with **docker login**.
+ The Amazon ECR repository exists and the user has access to pull from the repository.

After those prerequisites are met, you can pull your image. To pull your example image from Amazon ECR, run the following command:

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/hello-repository:latest
```

Output:

```
latest: Pulling from hello-repository
0a85502c06c9: Pull complete
0998bf8fb9e9: Pull complete
a6785352b25c: Pull complete
e9ae3c220b23: Pull complete
Digest: sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636EXAMPLE
Status: Downloaded newer image for {{aws_account_id}}.dkr.{{region}}.amazonaws.com/hello-repository:latest
```

## Step 6: Delete an image
<a name="cli-delete-image"></a>

If you no longer need an image in one of your repositories, you can delete the image. To delete an image, specify the repository that it's in and either an `imageTag` or `imageDigest` value for the image. The following example deletes an image in the `hello-repository` repository with the image tag `latest`. To delete your example image from the repository, run the following command:

```
aws ecr batch-delete-image \
      --repository-name hello-repository \
      --image-ids imageTag=latest \
      --region {{region}}
```

## Step 7: Delete a repository
<a name="cli-delete-repository"></a>

If you no longer need an entire repository of images, you can delete the repository. The following example uses the `--force` flag to delete a repository that contains images. To delete a repository that contains images (and all the images within it), run the following command:

```
aws ecr delete-repository \
      --repository-name hello-repository \
      --force \
      --region {{region}}
```

# Migrate container images from a third-party registry
<a name="migrate-from-third-party"></a>

Use this guide to perform a one-time copy of container images from an external registry into your Amazon ECR private registry where ECR Pull Through Cache is not supported.

If your source is [a supported upstream registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-creating-rule.html), you do not need to perform a one-time copy. See [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache) to configure automatic caching.

**Note**  
Amazon ECR stores the image version you copied. Newer versions from the source registry are not pulled automatically. To update an image, push the new version to your Amazon ECR repository.

## Migration overview
<a name="migrate-overview"></a>

Migrating your container images involves the following six steps:

1. Identify external image references in your build and deployment files.

1. Plan your Amazon ECR repository structure.

1. Copy images to Amazon ECR.

1. Verify image integrity.

1. Update your deployment configurations.

1. Monitor and validate.

## Prerequisites
<a name="migrate-prerequisites"></a>

Before you begin, verify the following:
+ Install and configure the AWS CLI version 2. For more information, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ Install Docker Engine or Docker Desktop version 20.10 or later. For more information, see [Install Docker Engine](https://docs.docker.com/engine/install/) in the Docker documentation.
+ (Optional) Install `skopeo`, an open source tool for copying container images between registries without a local Docker daemon. For installation instructions, see [Skopeo](https://github.com/containers/skopeo) on GitHub.
+ Verify that your IAM identity has permissions to authenticate to your registry, create repositories, and push images. Attach the `AmazonEC2ContainerRegistryFullAccess` managed policy to the IAM user or role that you use to run these commands. For more information, see [AWS managed policies for Amazon Elastic Container Registry](#security-iam-awsmanpol).

## Step 1: Identify external image references
<a name="migrate-identify-references"></a>

Search the files you use to build and deploy container images for references to third-party registries.

The following commands use Linux and macOS shell syntax. On Windows, use Windows Subsystem for Linux (WSL) or Git Bash.

### Identify references in deployment manifests
<a name="migrate-identify-manifests"></a>

Search your Amazon ECS task definitions or Amazon EKS manifests for non-ECR image references.

**For Kubernetes manifests:**

```
grep -rnH --include="*.yaml" --include="*.yml" "image:" . | grep -iv "dkr.ecr"
```

**For running Amazon EKS workloads:**

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"\n"}{end}{range .spec.initContainers[*]}{.image}{"\n"}{end}{end}' | sort -u | grep -iv "dkr.ecr"
```

**For Amazon ECS task definitions:**

```
aws ecs list-task-definitions --status ACTIVE --query 'taskDefinitionArns' --output text | \
  tr '\t' '\n' | \
  xargs -I {} aws ecs describe-task-definition --task-definition {} \
  --query 'taskDefinition.containerDefinitions[].image' --output text | \
  tr '\t' '\n' | sort -u | grep -iv "dkr.ecr"
```

### Identify references in Dockerfiles
<a name="migrate-identify-dockerfiles"></a>

To find `FROM` directives that reference external registries across your build directories:

```
grep -rnH --include="Dockerfile*" "FROM" . | grep -iv "dkr.ecr"
```

The output shows files and line numbers that reference images outside of Amazon ECR. For example:

```
./app/Dockerfile:1:FROM python:3.11-slim
./service/Dockerfile:1:FROM nginx:1.25
./worker/Dockerfile:3:FROM redis:7-alpine
```

### Identify pull frequency (optional)
<a name="migrate-identify-pull-frequency"></a>

To understand how frequently your workloads pull from third-party registries, review your upstream registry's usage analytics (for example, Docker Hub provides pull rate data in the account dashboard). High pull frequency increases your risk of hitting rate limits. For Docker Hub rate limits, see [Docker Hub rate limiting](https://docs.docker.com/docker-hub/download-rate-limit/) in the Docker documentation.

## Step 2: Plan your repository structure
<a name="migrate-plan-structure"></a>

Before you copy images, decide how to organize them in Amazon ECR.

**Repository naming** - Amazon ECR supports namespace prefixes with forward slashes. Use namespaces to group related images by team, environment, or application. Namespaces also enable scoped IAM policies per prefix. For example:

```
base-images/python
base-images/nginx
team-a/web-app
team-b/api-service
```

**Tag immutability** - For production images, enable tag immutability to prevent image tags from being overwritten. For more information, see [Preventing image tags from being overwritten in Amazon ECR](#image-tag-mutability).

**Encryption** - Choose your encryption configuration before creating repositories. You cannot change the encryption configuration after repository creation. For more information, see [Encryption at rest](#encryption-at-rest).

**Storage costs** - Amazon ECR de-duplicates image layers within each repository. If multiple images share the same base layers, you are billed for those layers only once per repository. Factor this into your cost estimates when planning which images to migrate.

**Repository creation templates** - If you are migrating many images, configure a repository creation template for create-on-push actions with your preferred settings (tag immutability, encryption, lifecycle policies). Amazon ECR applies the template settings when it creates repositories on your behalf during the first push. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).

**Managed signing** - If you plan to sign images with managed signing, configure your signing rules before you push images. Signing occurs at push time only. For more information, see [Sign images in Amazon ECR](#image-signing).

**Cross-Region replication** - If your workloads run in multiple AWS Regions, configure replication rules before you push images. Replication only copies images pushed after the rule is configured. For more information, see [Private image replication in Amazon ECR](#replication).

**Note**  
Multi-architecture images (manifest lists) require that you copy all platform-specific manifests in addition to the manifest list. If you use Docker, the **docker pull** and **docker push** commands handle only the platform that matches your local architecture. Use **skopeo copy --all** to copy multi-architecture images with all platforms intact.

## Step 3: Copy images to Amazon ECR
<a name="migrate-copy-images"></a>

Before you copy images, authenticate to your Amazon ECR private registry. Your registry URL follows the format `{{account-id}}.dkr.ecr.{{region}}.amazonaws.com`. Replace `111122223333` with your AWS account ID and `us-east-1` with your Region in the examples below. In the `aws-cn` partition, the registry URL suffix is `.amazonaws.com.cn`. In all other partitions (`aws`, `aws-us-gov`), the suffix is `.amazonaws.com`.

**To find your account ID, run:**

```
aws sts get-caller-identity --query Account --output text
```

For more information about authentication methods, see [Private registry authentication in Amazon ECR](#registry_auth).

**If you use Docker (Option A)**, authenticate with:

```
aws ecr get-login-password --region {{us-east-1}} | \
docker login --username AWS --password-stdin {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com
```

**If you use skopeo (Option B)**, authenticate with **skopeo login** instead. Skopeo maintains its own credential store separate from Docker:

```
aws ecr get-login-password --region {{us-east-1}} | \
skopeo login {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com --username AWS --password-stdin
```

Choose one of the following methods to copy your images.

### Option A: Copy with Docker CLI
<a name="migrate-copy-docker"></a>

Use this method for a *very* small number of single-platform images. For a detailed walk-through of the push workflow, see [Moving an image through its lifecycle in Amazon ECR](#getting-started-cli).

1. Create the destination repository (skip this step if the repository already exists):

   ```
   aws ecr create-repository \
     --repository-name {{base-images/nginx}} \
     --region {{us-east-1}} \
     --image-tag-mutability IMMUTABLE \
     --encryption-configuration encryptionType=AES256
   ```

1. If you pull from Docker Hub with an authenticated account to avoid rate limits, run **docker login docker.io** first. Pull the image from the third-party registry:

   ```
   docker pull nginx:1.25
   ```

1. Tag the image for your Amazon ECR repository:

   ```
   docker tag nginx:1.25 {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. Push the image to Amazon ECR:

   ```
   docker push {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. To retrieve the repository URI after creation, run:

   ```
   aws ecr describe-repositories --repository-names {{base-images/nginx}} --query 'repositories[0].repositoryUri' --output text
   ```

**Note**  
The Docker CLI copies only the platform that matches your local machine. To copy multi-architecture images, use Option B with **skopeo**.

### Option B: Copy with skopeo (recommended for bulk migration)
<a name="migrate-copy-skopeo"></a>

The **skopeo** tool copies images directly between registries without pulling them to your local machine. This approach is faster for bulk operations and supports multi-architecture images. Skopeo uses transport prefixes to identify image locations. Use `docker://` for remote registries.

1. Authenticate to the source registry if required. For example, for Docker Hub:

   ```
   echo YOUR_TOKEN | skopeo login docker.io --username YOUR_USERNAME --password-stdin
   ```

1. Create the destination repository:

   ```
   aws ecr create-repository \
     --repository-name {{base-images/nginx}} \
     --region {{us-east-1}}
   ```

1. Copy the image (single platform):

   ```
   skopeo copy docker://docker.io/library/nginx:1.25 \
     docker://{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. To copy a multi-architecture image with all platforms, add the `--all` flag:

   ```
   skopeo copy --all docker://docker.io/library/nginx:1.25 \
     docker://{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

**Note**  
**skopeo copy** does not copy OCI referrer artifacts (signatures, SBOMs, attestations) associated with an image. If your source images have associated referrer artifacts, copy them separately or re-sign images after migration using managed signing.

**Bulk copy with a script**

To migrate multiple images, create a text file that lists source and destination pairs, then use a script to copy them.

Create a file named `images-to-migrate.txt`:

```
docker.io/library/nginx:1.25 base-images/nginx:1.25
docker.io/library/python:3.11-slim base-images/python:3.11-slim
docker.io/library/redis:7-alpine base-images/redis:7-alpine
ghcr.io/org/custom-app:v2.1.0 team-a/custom-app:v2.1.0
```

Run the following script:

```
#!/usr/bin/env bash
set -euo pipefail
ACCOUNT_ID="{{111122223333}}"
REGION="{{us-east-1}}"
REGISTRY="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"

aws ecr get-login-password --region ${REGION} | \
  skopeo login ${REGISTRY} --username AWS --password-stdin

while IFS=' ' read -r SOURCE DEST; do
  REPO_NAME=$(echo "${DEST}" | cut -d: -f1)

  # Create repository if it does not exist
  aws ecr create-repository \
    --repository-name "${REPO_NAME}" \
    --region "${REGION}" 2>/dev/null || true

  echo "Copying ${SOURCE} to ${REGISTRY}/${DEST}"
  skopeo copy --all "docker://${SOURCE}" "docker://${REGISTRY}/${DEST}"
done < images-to-migrate.txt
```

**Note**  
Amazon ECR enforces API rate limits on push operations. For large migrations, add retry logic with exponential backoff if you encounter throttling. Authorization tokens expire after 12 hours. If your migration takes longer, re-run the authentication command before continuing.

## Step 4: Verify image integrity
<a name="migrate-verify-integrity"></a>

After copying images, verify that the image digests in Amazon ECR match the source.

1. Get the digest of the image in Amazon ECR:

   ```
   aws ecr describe-images \
     --repository-name {{base-images/nginx}} \
     --image-ids imageTag={{1.25}} \
     --query 'imageDetails[0].imageDigest' \
     --output text
   ```
**Note**  
For single-platform images, compare digests directly. For multi-architecture images copied with `--all`, the `imageDigest` in Amazon ECR represents the manifest list. Use **skopeo inspect --raw** (shown below) to compare manifest list contents instead.

1. Compare the digest with the source registry. Use **skopeo** to inspect the source:

   ```
   skopeo inspect docker://docker.io/library/nginx:1.25 | grep Digest
   ```

1. The digests must match for single-platform images copied with **skopeo**. If they do not match, the copy did not complete successfully. Retry the copy operation. If you used Docker (Option A), the digest may differ because Docker can reprocess layers during pull and push. For exact digest preservation, use **skopeo**.

1. For multi-architecture images, **aws ecr describe-images** returns both the manifest list and individual platform manifests. To compare the manifest list digest directly, use **skopeo inspect --raw** on both source and destination:

   ```
   skopeo inspect --raw docker://{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. (Optional) Run an image scan on the migrated images to identify vulnerabilities. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).

## Step 5: Update deployment configurations
<a name="migrate-update-deployments"></a>

After you verify the images, update your deployment configurations to pull from Amazon ECR and update your CI/CD build pipelines to push newly built images to ECR. This ensures future image versions are available without additional manual copies.

### Amazon ECS task definitions
<a name="migrate-update-ecs"></a>

Create a new revision of your task definition with the updated image URI:

```
{
  "containerDefinitions": [
    {
      "name": "web",
      "image": "{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25"
    }
  ]
}
```

For more information, see [Updating a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition.html) in the *Amazon ECS Developer Guide*.

### Amazon EKS or Kubernetes manifests
<a name="migrate-update-eks"></a>

Update the `image` field in your pod specifications:

```
spec:
  containers:
    - name: web
      image: {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
```

Verify that your nodes can authenticate to Amazon ECR. Amazon EKS nodes use the Amazon ECR credential helper by default if the `AmazonEC2ContainerRegistryReadOnly` managed policy is attached to the node IAM role.

### Dockerfiles
<a name="migrate-update-dockerfiles"></a>

Update `FROM` directives in your Dockerfiles:

```
FROM {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/python}}:3.11-slim
```

## Step 6: Monitor and validate
<a name="migrate-monitor"></a>

After redeploying your workloads, verify that all image pulls now come from Amazon ECR.
+ Check CloudWatch metrics for your repositories. The `RepositoryPullCount` metric confirms that pulls are occurring. For more information, see [Amazon ECR repository metrics](#ecr-repository-metrics).
+ Review CloudTrail for `BatchGetImage` and `GetDownloadUrlForLayer` events to confirm that your workloads pull from the expected repositories.
+ (Optional) Set up lifecycle policies to automate cleanup of old image versions. For more information, see .

## Considerations
<a name="migrate-considerations"></a>
+ **Unsupported upstream registries** - Pull Through Cache supports a specific set of upstream registries. For registries not in that list (such as JFrog Artifactory, Harbor, or Sonatype Nexus), use the Docker CLI or **skopeo** to copy images directly.
+ **Large-scale or cross-partition transfers** - For migrations across AWS partitions (for example, `aws` to `aws-cn`) or transfers involving thousands of images, see [Guidance for Data Transfer Hub on AWS](https://aws.amazon.com/solutions/guidance/data-transfer-hub-on-aws/).
+ **Lambda** - Lambda requires container images to reside in Amazon ECR and cannot pull directly from third-party registries. Use Option A or Option B to copy images to ECR before configuring your Lambda function.

## Related approaches
<a name="migrate-related-approaches"></a>

**Pull Through Cache** - If your source registry is one of the supported upstream registries and you want Amazon ECR to automatically pull and cache images rather than performing a one-time copy, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache).

# Optimizing performance for Amazon ECR
<a name="performance"></a>

You can use the following recommendations about settings and strategies to optimize performance when using Amazon ECR.

Use Docker 1.10 and above to take advantage of simultaneous layer uploads  
Docker images are composed of layers, which are intermediate build stages of the image. Each line in a Dockerfile results in the creation of a new layer. When you use Docker 1.10 and above, Docker defaults to pushing as many layers as possible as simultaneous uploads to Amazon ECR, resulting in faster upload times. 

Use a smaller base image   
The default images available through Docker Hub may contain many dependencies that your application doesn't require. Consider using a smaller image created and maintained by others in the Docker community, or build your own base image using Docker's minimal scratch image. For more information, see [Create a base image](https://docs.docker.com/engine/userguide/eng-image/baseimages/) in the Docker documentation.

Place the dependencies that change the least earlier in your Dockerfile   
Docker caches layers, and that speeds up build times. If nothing on a layer has changed since the last build, Docker uses the cached version instead of rebuilding the layer. However, each layer is dependent on the layers that came before it. If a layer changes, Docker recompiles not only that layer, but any layers that come after that layer as well.   
To minimize the time required to rebuild a Dockerfile and to re-upload layers, consider placing the dependencies that change the least frequently earlier in your Dockerfile. Place rapidly changing dependencies (such as your application's source code) later in the stack. 

Chain commands to avoid unnecessary file storage   
Intermediate files created on a layer remain a part of that layer even if they are deleted in a subsequent layer. Consider the following example:  

```
WORKDIR /tmp
RUN wget http://example.com/software.tar.gz 
RUN wget tar -xvf software.tar.gz 
RUN mv software/binary /opt/bin/myapp
RUN rm software.tar.gz
```
In this example, the layers created by the first and second RUN commands contain the original .tar.gz file and all of its unzipped contents. This is even though the .tar.gz file is deleted by the fourth RUN command. These commands can be chained together into a single RUN statement to ensure that these unnecessary files aren't part of the final Docker image:  

```
WORKDIR /tmp
RUN wget http://example.com/software.tar.gz &&\
    wget tar -xvf software.tar.gz &&\
    mv software/binary /opt/bin/myapp &&\
    rm software.tar.gz
```

Use the closest regional endpoint  
You can reduce latency in pulling images from Amazon ECR by ensuring that you are using the regional endpoint closest to where your application is running. If your application is running on an Amazon EC2 instance, you can use the following shell code to obtain the region from the Availability Zone of the instance:  

```
REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone |\
     sed -n 's/\(\d*\)[a-zA-Z]*$/\1/p')
```
The region can be passed to AWS CLI commands using the **--region** parameter, or set as the default region for a profile using the **aws configure** command. You can also set the region when making calls using the AWS SDK. For more information, see the documentation for the SDK for your specific programming language.

# Making requests to Amazon ECR registries
<a name="ecr-requests"></a>

You can push, pull, delete, view, and manage OCI images, Docker images, and OCI-compatible artifacts in Amazon ECR private registries using either IPv4-only endpoints or dual-stack (IPv4 and IPv6) endpoints. For making requests from IPv4 networks, you can use either dual-stack or IPv4 endpoints. For making requests from an IPv6 network, use a dual-stack endpoint. For more information about making requests to Amazon ECR Public registries using IPv4 and dual-stack endpoints, see [Making requests to Amazon ECR Public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-ecr-requests.html). There are no additional charges for accessing Amazon ECR over IPv6. For more information about pricing, see [Amazon Elastic Container Registry pricing](https://aws.amazon.com/ecr/pricing/).

Amazon ECR endpoints are designated by attributes beyond IPv4-only endpoint or dual-stack endpoints support. These attributes can include:
+ **Region** – Each endpoint is specific to a Region.
+ **Type** – Endpoint selection depends on whether you're using the AWS SDK or OCI-compatible and Docker command line interfaces.
+ **Security** – In select Regions Amazon ECR offers FIPS-compliant endpoints. For more information about a list of FIPS-compliant Amazon ECR endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

For more information about service endpoints supported by IPv4, dual-stack, Docker, and OCI client, which handles Amazon ECR API calls from AWS CLI and AWS SDKs see, [ Service endpoints](https://docs.aws.amazon.com/general/latest/gr/ecr.html#ecr_region).

## Getting started with making requests over IPv6
<a name="ipv6-access-getting-started"></a>

To make a request to an Amazon ECR registry over IPv6, you need to use a dual-stack endpoint. Before accessing an Amazon ECR registry over IPv6, verify the following requirements:
+ Your client and network must support IPv6.
+ Amazon ECR supports the following request types over IPv6:
  + OCI and Docker client requests: 

     `{{<registry-id>}}.dkr-ecr.{{<aws-region>}}.on.aws` 
  + AWS API requests:

     `ecr.{{<aws-region>}}.api.aws` 
+ You must update any AWS Identity and Access Management (IAM) or registry policies that use source IP address filtering to include IPv6 address ranges. For more information, see [Using IPv6 addresses in IAM policies](#ecr-request-ipv6-access-iam).
+ When you use IPv6, server access logs display `Remote IP` addresses in IPv6 format. Update your existing tools, scripts, and software to parse these IPv6-formatted IP addresses.
**Note**  
If you experience issues related to the presence of IPv6 addresses in log files, contact [AWS Support](https://aws.amazon.com/premiumsupport/).

## Testing IP address compatibility
<a name="ipv6-access-test-compatabilty"></a>

If you are using use Linux/Unix or Mac OS X, you can test whether you can access a dual-stack endpoint over IPv6 by using the `curl` command as shown in the following example:

**Example**  

```
curl --verbose https://ecr.us-west-2.api.aws
```
You get back information similar to the following example. If you are connected over IPv6 the connected IP address will be an IPv6 address.   

```
* About to connect() to ecr.us-west-2.api.aws port 443 (#0)
* Trying IPv6 address... connected
* Connected to ecr.us-west-2.api.aws (IPv6 address) port 443 (#0)
> Host: ecr.us-west-2.api.aws
* Request completely sent off
```

If you are using Microsoft Windows 7 or Windows 10, you can test whether you can access a dual-stack endpoint over IPv4 or IPv6 by using the `ping` command as shown in the following example.

```
ping ecr.us-west-2.api.aws
```

## Making requests over IPv6 by using dual-stack endpoints
<a name="ecr-access-api"></a>

You can make Amazon ECR API calls over IPv6 using dual-stack endpoints. The functionality and performance of Amazon ECR API operations remain consistent whether you use IPv4 or IPv6.

When you use the AWS Command Line Interface (AWS CLI) and AWS SDKs, you can enable IPv6 either by using a parameter or flag to switch to a dual-stack endpoint, or by directly specifying the dual-stack endpoint in your config file to override the default Amazon ECR endpoint. You can also make configuration changes by using a command, which sets `use_dualstack_endpoint` to true in the default profile. For more information about `use_dualstack_endpoint`, see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html).

**Example Making configuration changes by using a command**  <a name="ecr-private-config-changes"></a>
 `aws configure set default.ecr.use_dualstack_endpoint true` 

**Example Making requests over IPv6 using AWS CLI**  <a name="ecr-private-make-requests-cli"></a>
 ` aws ecr describe-repositories --region us-west-2 --endpoint-url https://ecr.us-west-2.api.aws` 

## Using Amazon ECR endpoints from the docker CLI
<a name="ecr-requests-from-docker-cli"></a>

 After you sign in to your Amazon ECR repository and tag your image, you can push and pull OCI images and Docker images to and from Amazon ECR registries. The following examples demonstrate docker push and Docker pull commands with both dual-stack endpoints. 

**Example Pushing docker images using IPv4 endpoint**  <a name="ecr-private-ecr-push-docker-ipv4"></a>
`docker push {{<registry-id>}}.dkr.ecr.us-west-1.amazonaws.com/my-repository:tag`

**Example Pushing docker images using dual-stack endpoint**  <a name="ecr-private-ecr-push-docker-dual-stack"></a>
`docker push {{<registry-id>}}.dkr-ecr.us-west-1.on.aws/my-repository:tag`

**Example Pulling docker images using IPv4 endpoint**  <a name="ecr-private-ecr-pull-docker-ipv4"></a>
`docker pull {{<registry-id>}}.dkr.ecr.us-west-1.amazonaws.com/my-repository:tag`

**Example Pulling docker images using dual-stack endpoint**  <a name="ecr-private-ecr-pull-docker-dual-stack"></a>
`docker pull {{<registry-id>}}.dkr-ecr.us-west-1.on.aws/my-repository:tag`

## Using IPv6 addresses in IAM policies
<a name="ecr-request-ipv6-access-iam"></a>

Before you access a registry using IPv6, ensure that your IAM user and Amazon ECR registry policies that use IP address filtering include IPv6 address ranges. If IP address filtering policies aren't updated to handle IPv6 addresses, clients might incorrectly lose or gain access to the registry when they start using IPv6. For more information about managing access permissions with IAM, see [Identity and Access Management for Amazon Elastic Container Registry](#security-iam).

IAM policies that filter IP addresses use [IP Address Condition Operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Conditions_IPAddress). The following registry policy example shows how to identify the `54.240.143.*` range of allowed IPv4 addresses by using IP address condition operators. Any IP addresses outside of this range are denied access to the registry (`exampleregistry`). Because all IPv6 addresses are outside of the allowed range, this policy prevents IPv6 addresses from accessing `exampleregistry`.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "IPAllow",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "ecr:*",
      "Resource": "arn:aws:ecr:*:*:repository/{{exampleregistry}}/*",
      "Condition": {
         "IpAddress": {"aws:SourceIp": "54.240.143.0/24"}
      } 
    } 
  ]
}
```

------

To allow both IPv4 (`54.240.143.0/24`) and IPv6 (`2001:DB8:1234:5678::/64`) address ranges, modify the registry policy's Condition element as shown in the following example. You can use this `Condition` block format to update both your IAM user and registry policies.

```
1.        "Condition": {
2.          "IpAddress": {
3.             "aws:SourceIp": [
4.               "54.240.143.0/24",
5.                "2001:DB8:1234:5678::/64"
6.              ]
7.           }
8.         }
```

**Important**  
Before using IPv6 you must update all relevant IAM user and registry policies that use IP address filtering. We don't recommend using IP address filtering in registry policies.

You can review your IAM user policies using the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). For more information about IAM, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

# Amazon ECR private registry
<a name="Registries"></a>

An Amazon ECR private registry hosts your container images in a highly available and scalable architecture. You can use your private registry to manage private image repositories consisting of Docker and Open Container Initiative (OCI) images and artifacts. Each AWS account is provided with a default private Amazon ECR registry. For more information about Amazon ECR public registries, see [Public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html) in the *Amazon Elastic Container Registry Public User Guide*.

## Private registry concepts
<a name="registry_concepts"></a>
+ The URL for your default private registry is  `https://``{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com` .
+ By default, your account has read and write access to the repositories in your private registry. However, users require permissions to make calls to the Amazon ECR APIs and to push or pull images to and from your private repositories. Amazon ECR provides several managed policies to control user access at varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples).
+ You must authenticate your Docker client to your private registry so that you can use the **docker push** and **docker pull** commands to push and pull images to and from the repositories in that registry. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).
+ Private repositories can be controlled with both user access policies and repository policies. For more information about repository policies, see [Private repository policies in Amazon ECR](#repository-policies).
+ The repositories in your private registry can be replicated across AWS Regions in your own private registry and across separate accounts by configuring replication for your private registry. For more information, see [Private image replication in Amazon ECR](#replication).

## Private registry authentication in Amazon ECR
<a name="registry_auth"></a>

You can use the AWS Management Console, the AWS CLI, or the AWS SDKs to create and manage private repositories. You can also use those methods to perform some actions on images, such as listing or deleting them. These clients use standard AWS authentication methods. Even though you can use the Amazon ECR API to push and pull images, you're more likely to use the Docker CLI or a language-specific Docker library.

The Docker CLI doesn't support native IAM authentication methods. Additional steps must be taken so that Amazon ECR can authenticate and authorize Docker push and pull requests.

The registry authentication methods that are detailed in the following sections are available.

### Using the Amazon ECR credential helper
<a name="registry-auth-credential-helper-reg"></a>

Amazon ECR provides a Docker credential helper which makes it easier to store and use Docker credentials when pushing and pulling images to Amazon ECR. For installation and configuration steps, see [Amazon ECR Docker Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper).

**Note**  
The Amazon ECR Docker credential helper doesn't support multi-factor authentication (MFA) currently.

### Using an authorization token
<a name="registry-auth-token"></a>

An authorization token's permission scope matches that of the IAM principal used to retrieve the authentication token. An authentication token is used to access any Amazon ECR registry that your IAM principal has access to and is valid for 12 hours. To obtain an authorization token, you must use the [GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html) API operation to retrieve a base64-encoded authorization token containing the username `AWS` and an encoded password. The AWS CLI ` get-login-password` command simplifies this by retrieving and decoding the authorization token which you can then pipe into a **docker login** command to authenticate.

**To authenticate Docker to an Amazon ECR private registry with get-login**
+ 

  To authenticate Docker to an Amazon ECR registry with get-login-password, run the **aws ecr get-login-password** command. When passing the authentication token to the **docker login** command, use the value `AWS` for the username and specify the Amazon ECR registry URI you want to authenticate to. If authenticating to multiple registries, you must repeat the command for each registry.
**Important**  
If you receive an error, install or upgrade to the latest version of the AWS CLI. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide*.
  + [get-login-password](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html) (AWS CLI)

    ```
    aws ecr get-login-password --region {{region}} | docker login --username AWS --password-stdin {{{{aws_account_id}}}}.dkr.ecr.{{region}}.amazonaws.com
    ```
  + [Get-ECRLoginCommand](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ECRLoginCommand.html) (AWS Tools for Windows PowerShell)

    ```
    (Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin {{{{aws_account_id}}}}.dkr.ecr.{{region}}.amazonaws.com
    ```

### Using HTTP API authentication
<a name="registry_auth_http"></a>

Amazon ECR supports the [Docker Registry HTTP API](https://docs.docker.com/registry/spec/api/). However, because Amazon ECR is a private registry, you must provide an authorization token with every HTTP request. You can add an HTTP authorization header using the `-H` option for **curl** and pass the authorization token provided by the **get-authorization-token** AWS CLI command.

**To authenticate with the Amazon ECR HTTP API**

1. Retrieve an authorization token with the AWS CLI and set it to an environment variable.

   ```
   TOKEN=$(aws ecr get-authorization-token --output text --query 'authorizationData[].authorizationToken')
   ```

1. To authenticate to the API, pass the `$TOKEN` variable to the ` -H` option of **curl**. For example, the following command lists the image tags in an Amazon ECR repository. For more information, see the [Docker Registry HTTP API](https://docs.docker.com/registry/spec/api/) reference documentation.

   ```
   curl -i -H "Authorization: Basic $TOKEN" https://{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/v2/{{amazonlinux}}/tags/list
   ```

   The output is as follows:

   ```
   HTTP/1.1 200 OK
   Content-Type: text/plain; charset=utf-8
   Date: Thu, 04 Jan 2018 16:06:59 GMT
   Docker-Distribution-Api-Version: registry/2.0
   Content-Length: 50
   Connection: keep-alive
   
   {"name":"amazonlinux","tags":["2017.09","latest"]}
   ```

## Private registry settings in Amazon ECR
<a name="registry-settings"></a>

Amazon ECR uses private registry settings to configure features at the registry level. The private registry settings are configured separately for each Region. You can use private registry settings to configure the following features.
+ **Registry permissions** – A registry permissions policy provides control over the replication and pull through cache permissions. For more information, see [Private registry permissions in Amazon ECR](#registry-permissions).
+ **Pull through cache rules** – A pull through cache rule is used to cache images from an upstream registry in your Amazon ECR private registry. For more information, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache).
+ **Replication configuration** – The replication configuration is used to control whether your repositories are copied across AWS Regions or AWS accounts. For more information, see [Private image replication in Amazon ECR](#replication).
+ **Repository creation templates** – A repository creation template is used to define the standard settings to apply when new repositories are created by Amazon ECR on your behalf. For example, repositories created by a pull through cache action, create on push, or replication. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).
+ **Scanning configuration** – By default, your registry is enabled for basic scanning. You may enable enhanced scanning which provides an automated, continuous scanning mode that scans for both operating system and programming language package vulnerabilities. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).
+ **Pull-time update exclusion** – You can configure pull-time update exclusions to prevent the last pull time from being updated for specific images when they are pulled. This is useful for images that are used for testing or CI/CD purposes where you don't want the pull time to affect lifecycle policy decisions. For more information, see [Pull-time update exclusions](#pull-time-update-exclusions).
+ **Blob mounting configuration** – The blob mounting configuration is used to control if the repositories within your registry share common layers rather than store duplicate layers. For more information, see [Blob mounting in Amazon ECR](#blob-mounting).

## Blob mounting in Amazon ECR
<a name="blob-mounting"></a>

 Amazon ECR supports a capability called blob mounting to share common image layers across repositories within a registry. When enabled, repositories within a single registry can reference layers from other repositories within the same registry instead of storing duplicate copies.

When registry blob mounting is enabled, Amazon ECR checks for existing layers in your registry during push operations when mounting parameters are included. If a layer already exists in another repository within the same registry, Amazon ECR will mount the existing layer instead of uploading a duplicate.

**Note**  
OCI clients automatically include mounting parameters if they detect a blob may already exist in a different repository. Amazon ECR attempts mounting only when these parameters are present in the client's POST request.

### Blob mounting concepts
<a name="blob_mounting_concepts"></a>
+  Blob mounting only works within the same registry (same account and region).
+ Repositories must use identical encryption type and keys.
+ Blob mounting is not supported for images created via pull through cache.
+ If you decide to disable blob mounting, existing images that were pushed with blob mounting configured will continue to work and layers will remain mounted.

### Blob mounting configuration
<a name="blob_mounting_configuration"></a>

You can use the AWS Management Console or AWS CLI to configure blob mounting for your registry.

**Note**  
Users need `ecr:GetDownloadUrlForLayer` IAM permission on a repository to mount layers from it.

------
#### [ AWS Management Console ]

Use the following steps to update your registry's blob mounting configuration using the AWS Management Console.

**Turn on the blob mounting configuration for your private registry**

1.  Open the Amazon ECR console at [ https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories)

1. From the navigation bar, choose the Region.

1. In the navigation pane, choose **Private registry**, **Feature & Settings**, and then choose **Blob mounting**.

1. On the **Blob mounting** page, choose **Enable**.

   A banner displays indicating that the blob mounting configuration has been updated to be enabled.

------
#### [ AWS CLI ]

Use the following command to update your registry's blob mounting configuration using the AWS CLI.
+ 

  ```
  aws ecr put-account-setting --name BLOB_MOUNTING --value ENABLED
  ```

------

## Private registry permissions in Amazon ECR
<a name="registry-permissions"></a>

 Amazon ECR uses a **registry policy** to grant permissions to an AWS principal at the private registry level.

Amazon ECR allows all ECR actions in the policy and enforces the registry policy in all ECR requests. You can use registry policies to grant permissions for actions such as replication configuration, pull-through cache rule creation, and repository creation. For the full list of API actions, see the* [Amazon ECR API Guide](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/Welcome.html) *. For information about general settings for your Amazon ECR private registry, see [Private registry settings in Amazon ECR](#registry-settings).

**Note**  
While it is possible to add the `ecr:*` action to a private registry policy, it is considered best practice to only add the specific actions required based on the feature you're using rather than use a wildcard.

**Topics**
+ [Private registry policy examples for Amazon ECR](#registry-permissions-examples)
+ [Granting registry permissions for cross account replication in Amazon ECR](#registry-permissions-create-replication)
+ [Granting registry permissions for pull through cache in Amazon ECR](#registry-permissions-create-pullthroughcache)

### Private registry policy examples for Amazon ECR
<a name="registry-permissions-examples"></a>

The following examples show registry permissions policy statements that you could use to control the permissions that users have to your Amazon ECR registry.

**Note**  
In each example, if the `ecr:CreateRepository` action is removed from your registry policy, replication can still occur. However, for successful replication, you need to create repositories with the same name within your account.

#### Example: Allow all IAM principals in a source account to replicate all repositories
<a name="registry-permissions-examples-all"></a>

The following registry permissions policy allows all IAM principals (users and roles) in a source account to replicate all repositories.

Note the following:
+ **Important:** When you specify an AWS account ID as a principal in a policy, you grant access to all IAM users and roles within that account, not just the root user. This provides broad access across the entire account.
+ **Security Consideration:** Account-level permissions grant access to all IAM entities in the specified account. For more restrictive access, specify individual IAM users, roles, or use condition statements to limit access further.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":[
        {
            "Sid":"ReplicationAccessCrossAccount",
            "Effect":"Allow",
            "Principal":{
                "AWS":"arn:aws:iam::{{111122223333}}:{{root}}"
            },
            "Action":[
                "ecr:CreateRepository",
                "ecr:ReplicateImage"
            ],
            "Resource": [
                "arn:aws:ecr:us-west-2:{{444455556666}}:repository/{{*}}"
            ]
        }
    ]
}
```

------

#### Example: Allow IAM principals from multiple accounts
<a name="registry-permissions-examples-multiple"></a>

The following registry permissions policy has two statements. Each statement allows all IAM principals (users and roles) in a source account to replicate all repositories.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":[
        {
            "Sid":"ReplicationAccessCrossAccount1",
            "Effect":"Allow",
            "Principal":{
                "AWS":"arn:aws:iam::{{111122223333}}:root"
            },
            "Action":[
                "ecr:CreateRepository",
                "ecr:ReplicateImage"
            ],
            "Resource": [
                "arn:aws:ecr:us-west-2:{{123456789012}}:repository/*"
            ]
        },
        {
            "Sid":"ReplicationAccessCrossAccount2",
            "Effect":"Allow",
            "Principal":{
                "AWS":"arn:aws:iam::{{444455556666}}:root"
            },
            "Action":[
                "ecr:CreateRepository",
                "ecr:ReplicateImage"
            ],
            "Resource": [
                "arn:aws:ecr:us-west-2:{{123456789012}}:repository/*"
            ]
        }
    ]
}
```

------

#### Example: Allow all IAM principals in a source account to replicate all repositories with prefix `prod-`.
<a name="registry-permissions-examples-specific"></a>

The following registry permissions policy allows all IAM principals (users and roles) in a source account to replicate all repositories that start with ` prod-`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":[
        {
            "Sid":"ReplicationAccessCrossAccount",
            "Effect":"Allow",
            "Principal":{
                "AWS":"arn:aws:iam::{{111122223333}}:{{root}}"
            },
            "Action":[
                "ecr:CreateRepository",
                "ecr:ReplicateImage"
            ],
            "Resource": [
                "arn:aws:ecr:us-west-2:{{444455556666}}:repository/{{prod-*}}"
            ]
        }
    ]
}
```

------

### Granting registry permissions for cross account replication in Amazon ECR
<a name="registry-permissions-create-replication"></a>

The cross account policy type is used to grant permissions to an AWS principal, allowing the replication of the repositories from a source registry to your registry. By default, you have permission to configure cross-Region replication within your own registry. You only need to configure the registry policy if you're granting another account permission to replicate contents to your registry.

A registry policy must grant permission for the `ecr:ReplicateImage` API action. This API is an internal Amazon ECR API that can replicate images between Regions or accounts. You can also grant permission for the ` ecr:CreateRepository` permission, which allows Amazon ECR to create repositories in your registry if they don't exist already. If the `ecr:CreateRepository` permission isn't provided, a repository with the same name as the source repository must be created manually in your registry. If neither is done, replication fails. Any failed `CreateRepository` or `ReplicateImage` API actions show up in CloudTrail.

#### To configure a permissions policy for replication (AWS Management Console)
<a name="registry-permissions-create-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your registry policy in.

1. In the navigation pane, choose **Private registry**, choose **Features & Settings**, and then choose **Permissions** .

1. On the **Registry permissions** page, choose **Generate statement**.

1. Complete the following steps to define your policy statement using the policy generator.

   1. For **Policy type**, choose **Replication - cross account**.

   1. For **Statement id**, enter a unique statement ID. This field is used as the `Sid` on the registry policy.

   1. For **Accounts**, enter the account IDs for each account you want to grant permissions to. When specifying multiple account IDs, separate them with a comma.

1. Choose **Save**.

#### To configure a permissions policy for replication (AWS CLI)
<a name="registry-permissions-create-cli"></a>

1. Create a file named `registry_policy.json` and populate it with a registry policy.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement":[
           {
               "Sid":"ReplicationAccessCrossAccount",
               "Effect":"Allow",
               "Principal":{
                   "AWS":"arn:aws:iam::{{111122223333}}:{{root}}"
               },
               "Action":[
                   "ecr:CreateRepository",
                   "ecr:ReplicateImage"
               ],
               "Resource": [
                   "arn:aws:ecr:us-west-2:{{444455556666}}:repository/{{*}}"
               ]
           }
       ]
   }
   ```

------

1. Create the registry policy using the policy file.

   ```
   aws ecr put-registry-policy \
         --policy-text file://{{registry_policy.json}} \
         --region {{us-west-2}}
   ```

1. Retrieve the policy for your registry to confirm.

   ```
   aws ecr get-registry-policy \
         --region {{us-west-2}}
   ```

### Granting registry permissions for pull through cache in Amazon ECR
<a name="registry-permissions-create-pullthroughcache"></a>

Amazon ECR private registry permissions may be used to scope the permissions of individual IAM entities to use pull through cache. If an IAM entity has more permissions granted by an IAM policy than the registry permissions policy is granting, the IAM policy takes precedence.

**To create a private registry permissions policy (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry permissions statement in.

1. In the navigation pane, choose **Private registry**, choose **Features & Settings**, and then choose ** Permissions**.

1. On the **Registry permissions** page, choose **Generate statement**.

1. For each pull through cache permissions policy statement you want to create, do the following.

   1. For **Policy type**, choose **Pull through cache policy**.

   1. For **Statement id**, provide a name for the pull through cache statement policy.

   1. For **IAM entities**, specify the users, groups, or roles to include in the policy.

   1. For **Cache namespace**, select the pull through cache rule to associate the policy with.

   1. For **Repository names**, specify the repository base name to apply the rule for. For example, if you want to specify the Amazon Linux repository on Amazon ECR Public, the repository name would be ` amazonlinux`.

# Amazon ECR private repositories
<a name="Repositories"></a>

An Amazon ECR private repository contains your Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts. You can create, monitor, and delete image repositories and set permissions that control who can access them by using Amazon ECR API operations or the **Repositories** section of the Amazon ECR console. Amazon ECR also integrates with the Docker CLI, so that you can push and pull images from your development environments to your repositories.

**Topics**
+ [Private repository concepts](#repository-concepts)
+ [Creating an Amazon ECR private repository to store images](#repository-create)
+ [Viewing the contents and details of a private repository in Amazon ECR](#repository-info)
+ [Deleting a private repository in Amazon ECR](#repository-delete)
+ [Private repository policies in Amazon ECR](#repository-policies)
+ [Tagging a private repository in Amazon ECR](#ecr-using-tags)

## Private repository concepts
<a name="repository-concepts"></a>
+ By default, your account has read and write access to the repositories in your default registry (`{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`). However, users require permissions to make calls to the Amazon ECR APIs and to push or pull images to and from your repositories. Amazon ECR provides several managed policies to control user access at varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples).
+ Repositories can be controlled with both user access policies and individual repository policies. For more information, see [Private repository policies in Amazon ECR](#repository-policies).
+ Repository names can support namespaces, which you can use to group similar repositories. For example, if there are several teams using the same registry, Team A can use the `team-a` namespace, and Team B can use the `team-b` namespace. By doing this, each team has their own image called `web-app` with each image prefaced with the team namespace. This configuration allows these images on each team to be used simultaneously without interference. Team A's image is `team-a/web-app`, and Team B's image is `team-b/web-app`.
+ Your images can be replicated to other repositories across Regions in your own registry and across accounts. You can do this by specifying a replication configuration in your registry settings. For more information, see [Private registry settings in Amazon ECR](#registry-settings).
+ When blob mounting is enabled at the registry level, repositories can share common image layers.

## Creating an Amazon ECR private repository to store images
<a name="repository-create"></a>

**Important**  
Dual-layer server-side encryption with AWS KMS (DSSE-KMS) is only available in the AWS GovCloud (US) Regions. 

Create an Amazon ECR private repository, and then use the repository to store your container images. Use the following steps to create a private repository using the AWS Management Console.

**To create a repository (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region to create your repository in.

1. Choose **Private repositories**, and then choose **Create repository**.

1. For **Repository name**, enter a unique name for your repository. The repository name can be specified on its own (for example `nginx-web-app`). Alternatively, it can be prepended with a namespace to group the repository into a category (for example `project-a/nginx-web-app`).
**Note**  
The repository name may container a maximum of `256` characters. The name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, periods and forward slashes. Using a double forward slash isn't supported.

1. For **Image tag immutability**, choose one of the following tag mutability settings for the repository.
   + **Mutable** – Choose this option if you want image tags to be overwritten. Recommended for repositories using pull through cache actions to ensure Amazon ECR can update cached images. Additionally, to disable tag updates for a few mutable tags, enter tag names or use wildcards (\*) to match multiple similar tags in the **Mutable tag exclusion** text box.
   + **Immutable** – Choose this option if you want to prevent image tags from being overwritten, and it applies to all tags and exclusions in the repository when pushing an image with existing tag. Amazon ECR returns an `ImageTagAlreadyExistsException` if you attempt to push an image with an existing tag. Additionally, to enable tag updates for a few immutable tags, enter tag names or use wildcards (\*) to match multiple similar tags in the **Immutable tag exclusion** text box. 
**Note**  
Individual tag mutability settings aren't supported.

1. For ** Encryption configuration**, choose between **AES-256** or ** AWS KMS**. For more information, see [Encryption at rest](#encryption-at-rest).

   1.  If AWS KMS is chosen, choose between Single-layer encryption and Dual-layer encryption. There are additional charges for using AWS KMS or Dual-layer encryption. For more information, see [Amazon ECR Service Pricing](https://aws.amazon.com/ecr/pricing/).

   1. By default, AWS managed key with the alias `aws/ecr` is chosen. This key is created in your account the first time that you create a repository with AWS KMS encryption enabled. Select ** Customer managed key (advanced)** to choose your own AWS KMS key. The AWS KMS key must be in the same Region as the cluster. Select **Create an AWS KMS key** to navigate to the AWS KMS console to create your own key.

1. For **Image scanning settings**, while you can specify the scan settings at the repository level for basic scanning, it is a best practice to specify the scan configuration at the private registry level. Configuring the scanning settings at the private registry level enables you to choose between enhanced scanning or basic scanning, and also allows you to define filters to specify which repositories should be scanned.

1. Choose **Create**.

**To create a repository (AWS CLI)**

1. You can create a repository using the AWS CLI with the **aws ecr create-repository** command.

   ```
   aws ecr create-repository \
               --repository-name {{hello-repository}} \
               --region {{region}}
   ```

1. If you have a repository creation template defined, you can create a repository by pushing your image using familiar Amazon ECR push commands with your desired repository name. Amazon ECR will automatically create the repository for you using the predefined settings of your repository creation template. If you do not have a repository creation template defined yet, your request to your nonexistent image repository will fail.

   ```
   docker push aws_account_id.dkr.ecr.region.amazonaws.com/prefix/my-new-repository:tag
   ```

### Next steps
<a name="procedure_next_steps"></a>

To view the steps to push an image to your repository, select the repository and choose **View push commands**. For more information about pushing an image to your repository, see [Pushing an image to an Amazon ECR private repository](#image-push).

## Viewing the contents and details of a private repository in Amazon ECR
<a name="repository-info"></a>

After you created a private repository, you can view details about the repository in the AWS Management Console:
+ Which images are stored in a repository
+ Details about each image stored in the repository, including the size and SHA digest for each image
+ The scan frequency specified for the contents of the repository
+ Whether the repository has an active pull through cache rule associated with it
+ The encryption setting for the repository

**Note**  
Starting with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the **docker images** command shows the uncompressed image size. Therefore, keep in mind that Docker might return a larger image than the image shown in the AWS Management Console.

**To view repository information (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository to view.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, choose the **Private** tab and then the repository to view.

1. On the repository detail page, the console defaults to the **Images** view. Use the navigation menu to view other information about the repository.
   + Choose **Summary** to view the repository details and pull count data for the repository.
   + Choose **Images** to view information about the image tags in the repository. To view more information about the image, select the image tag. For more information, see [Viewing image details in Amazon ECR](#image-info).

     If there are untagged images that you want to delete, you can select the box to the left of the repositories to delete and choose **Delete**. For more information, see [Deleting an image in Amazon ECR](#delete_image).
   + Choose **Permissions** to view the repository policies that are applied to the repository. For more information, see [Private repository policies in Amazon ECR](#repository-policies).
   + Choose **Lifecycle Policy** to view the lifecycle policy rules that are applied to the repository. The lifecycle events history is also viewed here. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies).
   + Choose **Tags** to view the metadata tags that are applied to the repository.

## Deleting a private repository in Amazon ECR
<a name="repository-delete"></a>

If you're finished using a repository, you can delete it. When you delete a repository in the AWS Management Console, all of the images contained in the repository are also deleted; this cannot be undone.

**Important**  
Images in the deleted repositories are also deleted. You cannot undo this operation.

**To delete a repository (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository to delete.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, choose the **Private** tab and then select the repository to delete and choose **Delete**.

1. In the **Delete {{repository\_name}}** window, verify that the selected repositories should be deleted and choose **Delete**.

## Private repository policies in Amazon ECR
<a name="repository-policies"></a>

Amazon ECR uses resource-based permissions to control access to repositories. Resource-based permissions let you specify which users or roles have access to a repository and what actions they can perform on the repository. By default, only the AWS account that created the repository has access to the repository. You can apply a repository policy that allows additional access to your repository.

**Topics**
+ [Repository policies vs IAM policies](#repository-policy-vs-iam-policy)
+ [Private repository policy examples in Amazon ECR](#repository-policy-examples)
+ [Setting a private repository policy statement in Amazon ECR](#set-repository-policy)

### Repository policies vs IAM policies
<a name="repository-policy-vs-iam-policy"></a>

Amazon ECR repository policies are a subset of IAM policies that are scoped for, and specifically used for, controlling access to individual Amazon ECR repositories. IAM policies are generally used to apply permissions for the entire Amazon ECR service but can also be used to control access to specific resources as well.

Both Amazon ECR repository policies and IAM policies are used when determining which actions a specific user or role may perform on a repository. If a user or role is allowed to perform an action through a repository policy but is denied permission through an IAM policy (or vice versa) then the action will be denied. A user or role only needs to be allowed permission for an action through either a repository policy or an IAM policy but not both for the action to be allowed.

**Important**  
Amazon ECR requires that users have permission to make calls to the `ecr:GetAuthorizationToken` API through an IAM policy before they can authenticate to a registry and push or pull any images from any Amazon ECR repository. Amazon ECR provides several managed IAM policies to control user access at varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples).

You can use either of these policy types to control access to your repositories, as shown in the following examples.

This example shows an Amazon ECR repository policy, which allows for a specific user to describe the repository and the images within the repository.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ECRRepositoryPolicy",
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::{{111122223333}}:user/{{username}}"},
            "Action": [
                "ecr:DescribeImages",
                "ecr:DescribeRepositories"
            ],
            "Resource": "*"
        }
    ]
}
```

------

This example shows an IAM policy that achieves the same goal as above, by scoping the policy to a repository (specified by the full ARN of the repository) using the resource parameter. For more information about Amazon Resource Name (ARN) format, see [Resources](#security_iam_service-with-iam-id-based-policies-resources).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowDescribeRepoImage",
            "Effect": "Allow",
            "Action": [
                "ecr:DescribeImages",
                "ecr:DescribeRepositories"
            ],
            "Resource": ["arn:aws:ecr:us-east-1:{{111122223333}}:repository/{{repository-name}}"]
        }
    ]
}
```

------

### Private repository policy examples in Amazon ECR
<a name="repository-policy-examples"></a>

**Important**  
The repository policy examples on this page are meant to be applied to Amazon ECR private repositories. They will not work properly if used with an IAM principal directly unless modified to specify the Amazon ECR repository as the resource. For more information on setting repository policies, see [Setting a private repository policy statement in Amazon ECR](#set-repository-policy).

Amazon ECR repository policies are a subset of IAM policies that are scoped for, and specifically used for, controlling access to individual Amazon ECR repositories. IAM policies are generally used to apply permissions for the entire Amazon ECR service but can also be used to control access to specific resources as well. For more information, see [Repository policies vs IAM policies](#repository-policy-vs-iam-policy).

The following repository policy examples show permission statements that you could use to control access to your Amazon ECR private repositories.

**Important**  
Amazon ECR requires that users have permission to make calls to the `ecr:GetAuthorizationToken` API through an IAM policy before they can authenticate to a registry and push or pull any images from any Amazon ECR repository. Amazon ECR provides several managed IAM policies to control user access at varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples).

#### Example: Allow one or more users
<a name="IAM_within_account"></a>

The following repository policy allows one or more users to push and pull images to and from a repository.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowPushPull",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::{{111122223333}}:user/{{push-pull-user-1}}",
                    "arn:aws:iam::{{111122223333}}:user/{{push-pull-user-2}}"
                ]
            },
            "Action": [
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:CompleteLayerUpload",
                "ecr:GetDownloadUrlForLayer",
                "ecr:InitiateLayerUpload",
                "ecr:PutImage",
                "ecr:UploadLayerPart"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Example: Allow another account
<a name="IAM_allow_other_accounts"></a>

The following repository policy allows a specific account to push images.

**Important**  
The account you are granting permissions to must have the Region you are creating the repository policy in enabled, otherwise an error will occur.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCrossAccountPush",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:CompleteLayerUpload",
                "ecr:InitiateLayerUpload",
                "ecr:PutImage",
                "ecr:UploadLayerPart"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The following repository policy allows some users to pull images ({{pull-user-1}} and {{pull-user-2}}) while providing full access to another ({{admin-user}}).

**Note**  
For more complicated repository policies that are not currently supported in the AWS Management Console, you can apply the policy with the [**set-repository-policy**](https://docs.aws.amazon.com/cli/latest/reference/ecr/set-repository-policy.html) AWS CLI command.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowPull",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::{{111122223333}}:user/{{pull-user-1}}",
                    "arn:aws:iam::{{111122223333}}:user/{{pull-user-2}}"
                ]
            },
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowAll",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:user/{{admin-user}}"
            },
            "Action": [
                "ecr:*"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Example: Deny all
<a name="IAM_deny_all"></a>

The following repository policy denies all users in all accounts the ability to pull images.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DenyPull",
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Example: Restricting access to specific IP addresses
<a name="IAM_restrict_ip"></a>

The following example denies permissions to any user to perform any Amazon ECR operations when applied to a repository from a specific range of addresses.

The condition in this statement identifies the `54.240.143.*` range of allowed Internet Protocol version 4 (IPv4) IP addresses.

The `Condition` block uses the `NotIpAddress` conditions and the `aws:SourceIp` condition key, which is an AWS-wide condition key. For more information about these condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html). The `aws:sourceIp` IPv4 values use the standard CIDR notation. For more information, see [IP Address Condition Operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_IPAddress) in the *IAM User Guide*.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "{{ECRPolicyId1}}",
    "Statement": [
        {
            "Sid": "{{IPAllow}}",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "ecr:*",
            "Resource": "*",
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": "{{54.240.143.0/24}}"
                }
            }
        }
    ]
}
```

------

#### Example: Allow an AWS service
<a name="IAM_service_linked"></a>

The following repository policy allows AWS CodeBuild access to the Amazon ECR API actions necessary for integration with that service. When using the following example, you should use the `aws:SourceArn` and `aws:SourceAccount` condition keys to scope which resources can assume these permissions. For more information, see [Amazon ECR sample for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-ecr.html) in the *AWS CodeBuild User Guide*.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"CodeBuildAccess",
         "Effect":"Allow",
         "Principal":{
            "Service":"codebuild.amazonaws.com"
         },
         "Action":[
            "ecr:BatchGetImage",
            "ecr:GetDownloadUrlForLayer"
         ],
         "Resource": "*",
         "Condition":{
            "ArnLike":{
               "aws:SourceArn":"arn:aws:codebuild:us-east-1:{{123456789012}}:project/{{project-name}}"
            },
            "StringEquals":{
               "aws:SourceAccount":"{{123456789012}}"
            }
         }
      }
   ]
}
```

------

### Setting a private repository policy statement in Amazon ECR
<a name="set-repository-policy"></a>

You can add an access policy statement to a repository in the AWS Management Console by following the steps below. You can add multiple policy statements per repository. For example policies, see [Private repository policy examples in Amazon ECR](#repository-policy-examples).

**Important**  
Amazon ECR requires that users have permission to make calls to the `ecr:GetAuthorizationToken` API through an IAM policy before they can authenticate to a registry and push or pull any images from any Amazon ECR repository. Amazon ECR provides several managed IAM policies to control user access at varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples).

**To set a repository policy statement**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository to set a policy statement on.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, choose the repository to set a policy statement on to view the contents of the repository.

1. From the repository image list view, in the navigation pane, choose **Permissions**, **Edit**.
**Note**  
If you don't see the **Permissions** option in the navigation pane, ensure that you are in the repository image list view.

1. On the **Edit permissions** page, choose **Add statement**.

1. For **Statement name**, enter a name for the statement.

1. For **Effect**, choose whether the policy statement will result in an allow or an explicit deny.

1. For **Principal**, choose the scope to apply the policy statement to. For more information, see [AWS JSON Policy Elements: Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in the *IAM User Guide*.
   + You can apply the statement to all authenticated AWS users by selecting the **Everyone (\*)** check box.
   + For **Service principal**, specify the service principal name (for example, `ecs.amazonaws.com`) to apply the statement to a specific service.
   + For **AWS Account IDs**, specify an AWS account number (for example, `111122223333`) to apply the statement to all users under a specific AWS account. Multiple accounts can be specified by using a comma delimited list.
**Important**  
The account you are granting permissions to must have the Region you are creating the repository policy in enabled, otherwise an error will occur.
   + For **IAM Entities**, select the roles or users under your AWS account to apply the statement to.
**Note**  
For more complicated repository policies that are not currently supported in the AWS Management Console, you can apply the policy with the [**set-repository-policy**](https://docs.aws.amazon.com/cli/latest/reference/ecr/set-repository-policy.html) AWS CLI command.

1. For **Actions**, choose the scope of the Amazon ECR API operations that the policy statement should apply to from the list of individual API operations.

1. When you are finished, choose **Save** to set the policy.

1. Repeat the previous step for each repository policy to add.

## Tagging a private repository in Amazon ECR
<a name="ecr-using-tags"></a>

To help you manage your Amazon ECR repositories, you can assign your own metadata to new or existing Amazon ECR repositories by using AWS resource *tags*. For example, you could define a set of tags for your account's Amazon ECR repositories that helps you track the owner of each repository.

### Tag basics
<a name="tag-basics"></a>

Tags don't have any semantic meaning to Amazon ECR and are interpreted strictly as a string of characters. Tags are not automatically assigned to your resources. You can edit tag keys and values, and you can remove tags from a resource at any time. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value. If you delete a resource, any tags for the resource are also deleted.

You can work with tags using the Amazon ECR console, the AWS CLI, and the Amazon ECR API.

Using AWS Identity and Access Management (IAM), you can control which users in your AWS account have permission to create, edit, or delete tags. For information about tags in IAM policies, see [Using Tag-Based Access Control](#ecr-supported-iam-actions-tagging).

### Tagging your resources for billing
<a name="tag-resources-for-billing"></a>

The tags you add to your Amazon ECR repositories are helpful when reviewing cost allocation after enabling them in your Cost & Usage Report. For more information, see [Amazon ECR usage reports](#usage-reports).

To see the cost of your combined resources, you can organize your billing information based on resources that have the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information about setting up a cost allocation report with tags, see [The Monthly Cost Allocation Report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html) in the *AWS Billing User Guide*.

**Note**  
If you've just enabled reporting, data for the current month is available for viewing after 24 hours.

### Adding tags to a private repository in Amazon ECR
<a name="adding-tags-repositories"></a>

You can add tags to a private repository.

For information about names and best practices for tags, see [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions) and [Best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *Tagging AWS Resources User Guide*.

#### Adding tags to a repository (AWS Management Console)
<a name="tag-resources-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, select the region to use.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, select the check box next to the repository you want to tag.

1. From the **Action** menu, select **Repository tags**.

1. On the **Repository tags** page, select **Add tags**, **Add tag**.

1. On the **Edit repository tags** page, specify the key and value for each tag, and then choose **Save**.

#### Adding tags to a repository (AWS CLI or API)
<a name="tag-resources-api-sdk"></a>

You can add or overwrite one or more tags by using the AWS CLI or an API.
+ AWS CLI - [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/ecr/tag-resource.html)
+ API action - [TagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_TagResource.html)

The following examples show how to add tags using the AWS CLI.

**Example 1: Tag a repository**  
The following command tags a repository.

```
aws ecr tag-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}} \
     --tags Key={{stack}},Value={{dev}}
```

**Example 2: Tag a repository with multiple tags**  
The following command adds three tags to a repository.

```
aws ecr tag-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}} \
     --tags Key={{key1}},Value={{value1}} Key={{key2}},Value={{value2}} Key={{key3}},Value={{value3}}
```

**Example 3: List tags for a repository**  
The following command lists the tags associated with a repository.

```
aws ecr list-tags-for-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}}
```

**Example 4: Create a repository and add a tag**  
The following command creates a repository named `test-repo` and adds a tag with key `team` and value `devs`.

```
aws ecr create-repository \
     --repository-name {{test-repo}} \
     --tags Key={{team}},Value={{devs}}
```

### Deleting tags from a private repository in Amazon ECR
<a name="deleting-tags-repositories"></a>

You can delete tags from a private repository.

#### To delete a tag from a private repository (AWS Management Console)
<a name="deleting-tags-repositories-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, select the region to use.

1. On the **Repositories** page, select the check box next to the repository you want to remove a tag from.

1. From the **Action** menu, select **Repository tags**.

1. On the **Repository tags** page, select **Edit**.

1. On the **Edit repository tags** page, select **Remove** for each tag you want to delete, and choose **Save**.

#### To delete a tag from a private repository (AWS CLI)
<a name="deleting-tags-repositories-cli"></a>

You can delete one or more tags by using the AWS CLI or an API.
+ AWS CLI - [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/ecr/untag-resource.html)
+ API action - [UntagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UntagResource.html)

The following example shows how to delete a tag from a repository using the AWS CLI.

```
aws ecr untag-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}} \
     --tag-keys {{tag_key}}
```

# Private images in Amazon ECR
<a name="images"></a>

Amazon ECR stores Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts in private repositories. You can use the Docker CLI, or your preferred client, to push and pull images to and from your repositories.

With Amazon ECR support for OCI v1.1, you can store and manage reference artifacts that are defined by the OCI [Referrers API](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#enabling-the-referrers-api). Artifacts include signatures, Software Bill of Materials (SBoMs), Helm charts, scan results, and attestations. A set of artifacts for a container image is transferred with that container and stored as a separate image that counts as an image consumed for your repository.

The [Sign images in Amazon ECR](#image-signing) and [Deleting signatures and other artifacts from an Amazon ECR private repository](#image-artifact-delete) pages provide examples of how to use signature-related artifacts. For more information on signing container images, see [Signing container images](https://docs.aws.amazon.com/signer/latest/developerguide/container-workflow.html) in the *AWS Signer Developer Guide*.

**Topics**
+ [Pushing an image to an Amazon ECR private repository](#image-push)
+ [Deleting signatures and other artifacts from an Amazon ECR private repository](#image-artifact-delete)
+ [Viewing image details in Amazon ECR](#image-info)
+ [Pulling an image to your local environment from an Amazon ECR private repository](#docker-pull-ecr-image)
+ [Pulling the Amazon Linux container image](#amazon_linux_container_image)
+ [Deleting an image in Amazon ECR](#delete_image)
+ [Archiving an image in Amazon ECR](#archive_restore_image)
+ [Retagging an image in Amazon ECR](#image-retag)
+ [Preventing image tags from being overwritten in Amazon ECR](#image-tag-mutability)
+ [Container image manifest format support in Amazon ECR](#image-manifest-formats)
+ [Using Amazon ECR images with Amazon ECS](#ECR_on_ECS)
+ [Using Amazon ECR Images with Amazon EKS](#ECR_on_EKS)

## Pushing an image to an Amazon ECR private repository
<a name="image-push"></a>

You can push your Docker images, manifest lists, and Open Container Initiative (OCI) images and compatible artifacts to your private repositories.

Amazon ECR provides a way to replicate your images to other repositories. By specifying a replication configuration in your private registry settings, you can replicate across Regions in your own registry and across different accounts. For more information, see [Private registry settings in Amazon ECR](#registry-settings).

**Note**  
If you push an image that is currently archived, that image will be automatically restored and removed from the archive. For more information about archiving and restoring images, see [Archiving an image in Amazon ECR](#archive_restore_image).

When registry blob mounting is enabled and mounting parameters are included, Amazon ECR automatically checks for existing layers in your registry during push operations. If a layer already exists in another repository within the same registry, Amazon ECR will mount the existing layer instead of uploading a duplicate. For more information, see [Blob mounting in Amazon ECR](#blob-mounting).

**Topics**
+ [IAM permissions for pushing an image to an Amazon ECR private repository](#image-push-iam)
+ [Pushing a Docker image to an Amazon ECR private repository](#docker-push-ecr-image)
+ [Pushing a multi-architecture image to an Amazon ECR private repository](#docker-push-multi-architecture-image)
+ [Pushing a Helm chart to an Amazon ECR private repository](#push-oci-artifact)

### IAM permissions for pushing an image to an Amazon ECR private repository
<a name="image-push-iam"></a>

Users need IAM permissions to push images to Amazon ECR private repositories. Following the best practice of granting least privilege, you can grant access to a specific repository. You can also grant access to all repositories.

A user must authenticate to each Amazon ECR registry they want to push images to by requesting an authorization token. Amazon ECR provides several AWS managed policies to control user access at varying levels. For more information, see [AWS managed policies for Amazon Elastic Container Registry](#security-iam-awsmanpol).

You can also create a your own IAM policies. The following IAM policy grants the required permissions for pushing an image to a specific repository. To limit the permissions for a specific repository, use the full Amazon Resource Name (ARN) of the repository.

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
                "ecr:CompleteLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:InitiateLayerUpload",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:BatchGetImage"
            ],
            "Resource": "arn:aws:ecr:us-east-1:{{111122223333}}:repository/{{repository-name}}"
        },
        {
            "Effect": "Allow",
            "Action": "ecr:GetAuthorizationToken",
            "Resource": "*"
        }
    ]
}
```

------

The following IAM policy grants the required permissions for pushing an image to all repositories.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                    "ecr:CompleteLayerUpload",
                    "ecr:GetAuthorizationToken",
                    "ecr:UploadLayerPart",
                    "ecr:InitiateLayerUpload",
                    "ecr:BatchCheckLayerAvailability",
                    "ecr:PutImage",
                    "ecr:BatchGetImage"
            ],
            "Resource": "arn:aws:ecr:us-west-2:111122223333:repository/*"
        } 
    ]
}
```

### Pushing a Docker image to an Amazon ECR private repository
<a name="docker-push-ecr-image"></a>

You can push your container images to an Amazon ECR repository with the **docker push** command.

Amazon ECR also supports creating and pushing Docker manifest lists that are used for multi-architecture images. For information, see [Pushing a multi-architecture image to an Amazon ECR private repository](#docker-push-multi-architecture-image).

**To push a Docker image to an Amazon ECR repository**

The Amazon ECR repository must exist before you push the image, or you must have a repository creation template defined. For more information, see [Creating an Amazon ECR private repository to store images](#repository-create) and [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).

1. Authenticate your Docker client to the Amazon ECR registry to which you intend to push your image. Authentication tokens must be obtained for each registry used, and the tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

   To authenticate Docker to an Amazon ECR registry, run the **aws ecr get-login-password** command. When passing the authentication token to the **docker login** command, use the value `AWS` for the username and specify the Amazon ECR registry URI you want to authenticate to. If authenticating to multiple registries, you must repeat the command for each registry.
**Important**  
If you receive an error, install or upgrade to the latest version of the AWS CLI. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide*.

   ```
   aws ecr get-login-password --region {{<region>}} | docker login --username AWS --password-stdin {{<{{aws_account_id}}>}}.dkr.ecr.{{<region>}}.amazonaws.com
   ```

1. If your image repository doesn't exist in the registry you intend to push to yet, and you have a repository creation template defined, you can push your image using your repository creation template's prefix and your desired repository name. ECR will automatically create the repository for you using the predefined settings of your repository creation template.

   If you do not have a matching repository creation template defined, you will need to create a repository. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates) or [Creating an Amazon ECR private repository to store images](#repository-create).

1. Identify the local image to push. Run the **Docker images** command to list the container images on your system.

   ```
   docker images
   ```

   You can identify an image with the {{repository:tag}} value or the image ID in the resulting command output.

1. <a name="image-tag-step"></a>Tag your image with the Amazon ECR registry, repository, and optional image tag name combination to use. The registry format is  `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`. The repository name should match the repository that you created for your image. If you omit the image tag, we assume that the tag is `latest`.

   The following example tags a local image with the ID {{ e9ae3c220b23}} as `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/my-repository:tag`.

   ```
   docker tag {{e9ae3c220b23}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository:tag}}
   ```

1. <a name="image-push-step"></a>Push the image using the **docker push** command:

   ```
   docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository:tag}}
   ```

1. (Optional) Apply any additional tags to your image and push those tags to Amazon ECR by repeating [Step 4](#image-tag-step) and [Step 5](#image-push-step).

### Pushing a multi-architecture image to an Amazon ECR private repository
<a name="docker-push-multi-architecture-image"></a>

You can push multi-architecture images to an Amazon ECR repository by creating and pushing Docker manifest lists. A *manifest list* is a list of images that is created by specifying one or more image names. In most cases, the manifest list is created from images that serve the same function but are for different operating systems or architectures. The manifest list isn't required. For more information, see [docker manifest](https://docs.docker.com/engine/reference/commandline/manifest/).

A manifest list can be pulled or referenced in an Amazon ECS task definition or Amazon EKS pod spec like other Amazon ECR images.

 **Prerequisites** 
+ In your Docker CLI, turn on experimental features. For information about experimental features, see [Experimental features](https://docs.docker.com/engine/reference/commandline/cli/#experimental-features) in the Docker documentation.
+ The Amazon ECR repository must exist before you push the image. For more information, see [Creating an Amazon ECR private repository to store images](#repository-create).
+ Images must be pushed to your repository before you create the Docker manifest. For information about how to push an image, see [Pushing a Docker image to an Amazon ECR private repository](#docker-push-ecr-image).

**To push a multi-architecture Docker image to an Amazon ECR repository**

1. Authenticate your Docker client to the Amazon ECR registry to which you intend to push your image. Authentication tokens must be obtained for each registry used, and the tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

   To authenticate Docker to an Amazon ECR registry, run the **aws ecr get-login-password** command. When passing the authentication token to the **docker login** command, use the value `AWS` for the username and specify the Amazon ECR registry URI you want to authenticate to. If authenticating to multiple registries, you must repeat the command for each registry.
**Important**  
If you receive an error, install or upgrade to the latest version of the AWS CLI. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide*.

   ```
   aws ecr get-login-password --region {{<region>}} | docker login --username AWS --password-stdin {{<{{aws_account_id}}>}}.dkr.ecr.{{<region>}}.amazonaws.com
   ```

1. List the images in your repository, confirming the image tags.

   ```
   aws ecr describe-images --repository-name {{my-repository}}
   ```

1. Create the Docker manifest list. The `manifest create` command verifies that the referenced images are already in your repository and creates the manifest locally.

   ```
   docker manifest create {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository}}:{{image_one_tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository}}:{{image_two}}
   ```

1. (Optional) Inspect the Docker manifest list. This enables you to confirm the size and digest for each image manifest referenced in the manifest list.

   ```
   docker manifest inspect {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository}}
   ```

1. Push the Docker manifest list to your Amazon ECR repository.

   ```
   docker manifest push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository}}
   ```

### Pushing a Helm chart to an Amazon ECR private repository
<a name="push-oci-artifact"></a>

You can push Open Container Initiative (OCI) artifacts to an Amazon ECR repository. To see an example of this functionality, use the following steps to push a Helm chart to Amazon ECR.

For information about using your Amazon ECR hosted Helm charts with Amazon EKS, see [Installing a Helm chart on an Amazon EKS cluster](#using-helm-charts-eks).

**To push a Helm chart to an Amazon ECR repository**

1. Install the latest version of the Helm client. These steps were written using Helm version `3.18.6`. For compatibility with Amazon EKS supported Kubernetes versions, use Helm version 3.9 or later. For more information, see [Installing Helm](https://helm.sh/docs/intro/install/).

1. Use the following steps to create a test Helm chart. For more information, see [Helm Docs - Getting Started](https://helm.sh/docs/chart_template_guide/getting_started/).

   1. Create a Helm chart named `helm-test-chart` and clear the contents of the `templates` directory.

      ```
      helm create {{helm-test-chart}}
      rm -rf ./{{helm-test-chart}}/templates/*
      ```

   1. Create a `ConfigMap` in the `templates` folder.

      ```
      cd {{helm-test-chart}}/templates
      cat <<EOF > configmap.yaml
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: {{helm-test-chart}}-configmap
      data:
        myvalue: "Hello World"
      EOF
      ```

1. Package the chart. The output will contain the filename of the packaged chart which you use when pushing the Helm chart.

   ```
   cd ../..
   helm package {{helm-test-chart}}
   ```

   Output

   ```
   Successfully packaged chart and saved it to: /Users/{{username}}/{{helm-test-chart}}-0.1.0.tgz
   ```

1. Create a repository to store your Helm chart. The name of your repository should match the name you used when creating the Helm chart in step 2. For more information, see [Creating an Amazon ECR private repository to store images](#repository-create).

   ```
   aws ecr create-repository \
        --repository-name {{helm-test-chart}} \
        --region {{us-west-2}}
   ```

1. Authenticate your Helm client to the Amazon ECR registry to which you intend to push your Helm chart. Authentication tokens must be obtained for each registry used, and the tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

   ```
   aws ecr get-login-password \
        --region {{us-west-2}} | helm registry login \
        --username AWS \
        --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com
   ```

1. Push the Helm chart using the **helm push** command. The output should include the Amazon ECR repository URI and SHA digest.

   ```
   helm push {{helm-test-chart-0.1.0.tgz}} oci://{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/
   ```

1. Describe your Helm chart.

   ```
   aws ecr describe-images \
        --repository-name {{helm-test-chart}} \
        --region {{us-west-2}}
   ```

   In the output, verify that the `artifactMediaType` parameter indicates the proper artifact type.

   ```
   {
       "imageDetails": [
           {
               "registryId": "{{aws_account_id}}",
               "repositoryName": "helm-test-chart",
               "imageDigest": "sha256:dd8aebdda7df991a0ffe0b3d6c0cf315fd582cd26f9755a347a52adEXAMPLE",
               "imageTags": [
                   "0.1.0"
               ],
               "imageSizeInBytes": 1620,
               "imagePushedAt": "2021-09-23T11:39:30-05:00",
               "imageManifestMediaType": "application/vnd.oci.image.manifest.v1+json",
               "artifactMediaType": "application/vnd.cncf.helm.config.v1+json"
           }
       ]
   }
   ```

1. (Optional) For additional steps, install the Helm `ConfigMap` and get started with Amazon EKS. For more information, see [Installing a Helm chart on an Amazon EKS cluster](#using-helm-charts-eks).

## Deleting signatures and other artifacts from an Amazon ECR private repository
<a name="image-artifact-delete"></a>

You can use the ORAS client to list and delete signatures and other reference type artifacts from an Amazon ECR private repository. Deleting signatures and other reference artifacts is similar to how an image is deleted (see [Deleting an image in Amazon ECR](#delete_image)). Here is how to list artifacts and delete signatures: 

**To manage image artifacts using the ORAS CLI**

1. Install and configure the ORAS client.

   For information about installing and configuring the ORAS client, see [Installation](https://oras.land/docs/installation) in the ORAS documentation.

1. To list available artifacts for an Amazon ECR image, use `oras discover`, followed by an image name:

   ```
   oras discover 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci:helloworld
   ```

   The output should look similar to this:

   ```
   111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:88c0c54329bfdc1d94d6f58cd3fcb1226d46f58670f44a8c689cb3c9b37b6925
   └── application/vnd.cncf.notary.signature
       ├── sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42
       └── sha256:6527bcec87adf1d55460666183b9d0968b3cd4e4bc34602d485206a219851171
   ```

1. To delete a signature using the ORAS CLI, given the previous example, run the following command:

   ```
   oras manifest delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42
   ```

   The output should look similar to this:

   ```
   Are you sure you want to delete the manifest "111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42" and all tags associated with it? [y/N] y
   ```

1. Press `y`. The artifact should be deleted.

**To troubleshoot artifact deletion**

If a signature deletion, such as the one just shown, should fail, output similar to the following appears.

```
Error response from registry: failed to delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42:
unsupported: Requested image referenced by manifest list: [sha256:005e2c97a6373e483799fa4ff29ac64a42dd10f08efcc166d6775f9b74943b5b]
```

This failure can happen when deleting an image pushed before the OCI 1.1 launch. As noted in the error, you must delete the manifest referencing the image before you can delete the image as follows:

1. To delete the manifest associated with the signature you want to delete, type:

   ```
    oras manifest delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:005e2c97a6373e483799fa4ff29ac64a42dd10f08efcc166d6775f9b74943b5b
   ```

   The output should look similar to this:

   ```
   Are you sure you want to delete the manifest "sha256:005e2c97a6373e483799fa4ff29ac64a42dd10f08efcc166d6775f9b74943b5b" and all tags associated with it? [y/N] y
   ```

1. Press `y`. The manifest should be deleted.

1. With the manifest gone, you can delete the signature:

   ```
    oras manifest delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42
   ```

   The output should look similar to this. Press `y`.

   ```
   Are you sure you want to delete the manifest "sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42" and all tags associated with it? [y/N] y
   Deleted [registry] 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42
   ```

1. To see that the signature was deleted, type:

   ```
   oras discover 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci:helloworld
   ```

   The output should look similar to this:

   ```
   111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:88c0c54329bfdc1d94d6f58cd3fcb1226d46f58670f44a8c689cb3c9b37b6925
   └── application/vnd.cncf.notary.signature
       └── sha256:6527bcec87adf1d55460666183b9d0968b3cd4e4bc34602d485206a219851171
   ```

## Viewing image details in Amazon ECR
<a name="image-info"></a>

After you push an image to your repository, you can view information about it. The details included are as follows:
+ Image URI
+ Image tags
+ Artifact media type
+ Image manifest type
+ Scanning status
+ The size of the image in MB
+ When the image was pushed to the repository
+ The replication status

**To view image details (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository containing your image.

1. In the navigation pane, under **Private registry**, choose **Repositories**.

1. On the **Private repositories** page, choose the repository to view.

1. On the **Repositories : {{repository\_name}}** page, choose the image to view the details of.

## Pulling an image to your local environment from an Amazon ECR private repository
<a name="docker-pull-ecr-image"></a>

If you want to run a Docker image that is available in Amazon ECR, you can pull it to your local environment with the **docker pull** command. You can do this from either your default registry or from a registry associated with another AWS account. 

To use an Amazon ECR image in an Amazon ECS task definition, see [Using Amazon ECR images with Amazon ECS](#ECR_on_ECS). 

**Important**  
You cannot pull an archived image. Archived images must be restored before they can be pulled. For more information about archiving and restoring images, see [Archiving an image in Amazon ECR](#archive_restore_image).

**Important**  
Amazon ECR requires that users have permission to make calls to the `ecr:GetAuthorizationToken` API through an IAM policy before they can authenticate to a registry and push or pull any images from any Amazon ECR repository. Amazon ECR provides several AWS managed policies to control user access at varying levels. For information about the AWS managed policies for Amazon ECR, see [AWS managed policies for Amazon Elastic Container Registry](#security-iam-awsmanpol).

**To pull a Docker image from an Amazon ECR repository**

1. Authenticate your Docker client to the Amazon ECR registry that you intend to pull your image from. Authentication tokens must be obtained for each registry used, and the tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

1. (Optional) Identify the image to pull.
   + You can list the repositories in a registry with the **aws ecr describe-repositories** command:

     ```
     aws ecr describe-repositories
     ```

     The example registry above has a repository called `amazonlinux` .
   + You can describe the images within a repository with the **aws ecr describe-images** command:

     ```
     aws ecr describe-images --repository-name amazonlinux
     ```

     The example repository above has an image tagged as `latest` and `2016.09`, with the image digest ` sha256:f1d4ae3f7261a72e98c6ebefe9985cf10a0ea5bd762585a43e0700ed99863807`.

1. Pull the image using the **docker pull** command. The image name format should be `{{registry}}/{{repository}} [:{{tag}}]` to pull by tag, or `{{registry}} /{{repository}}[@{{digest}}]` to pull by digest.

   ```
   docker pull {{aws_account_id}}.dkr.ecr.{{us-west-2}}.amazonaws.com/amazonlinux:latest
   ```
**Important**  
If you receive a `{{repository-url}} not found: does not exist or no pull access` error, you might need to authenticate your Docker client with Amazon ECR. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

## Pulling the Amazon Linux container image
<a name="amazon_linux_container_image"></a>

The Amazon Linux container image is built from the same software components that are included in the Amazon Linux AMI. The Amazon Linux container image is available for use in any environment as a base image for Docker workloads. If you use the Amazon Linux AMI for applications in Amazon EC2, you can containerize your applications with the Amazon Linux container image.

You can use the Amazon Linux container image in your local development environment and then push your application to AWS using Amazon ECS. For more information, see [Using Amazon ECR images with Amazon ECS](#ECR_on_ECS).

The Amazon Linux container image is available on Amazon ECR Public and on [Docker Hub](https://hub.docker.com/_/amazonlinux/). For support for the Amazon Linux container image, go to the [AWS developer forums](https://forums.aws.amazon.com/forum.jspa?forumID=228).

**To pull the Amazon Linux container image from Amazon ECR Public**

1. Authenticate your Docker client to the Amazon Linux Public registry. Authentication tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).
**Note**  
The **ecr-public** commands are available in the AWS CLI starting with version `1.18.1.187`, however we recommend using the latest version of the AWS CLI. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide*.

   ```
   aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
   ```

   The output is as follows:

   ```
   Login succeeded
   ```

1. Pull the Amazon Linux container image using the **docker pull** command. To view the Amazon Linux container image on the Amazon ECR Public Gallery, see [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux).

   ```
   docker pull public.ecr.aws/amazonlinux/amazonlinux:latest
   ```

1. (Optional) Run the container locally.

   ```
   docker run -it public.ecr.aws/amazonlinux/amazonlinux /bin/bash
   ```

**To pull the Amazon Linux container image from Docker Hub**

1. Pull the Amazon Linux container image using the **docker pull** command.

   ```
   docker pull amazonlinux
   ```

1. (Optional) Run the container locally.

   ```
   docker run -it amazonlinux:latest /bin/bash
   ```

## Deleting an image in Amazon ECR
<a name="delete_image"></a>

If you're finished using an image, you can delete it from your repository. If you're finished with a repository, you can delete the entire repository and all of the images within it. For more information, see [Deleting a private repository in Amazon ECR](#repository-delete).

As an alternative to deleting images manually, you can create repository lifecycle policies which provide more control over the lifecycle management of images in your repositories. Lifecycle policies automate this process for you. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies).

**Note**  
 If your repository has a mix of images, some of which were pushed before Amazon ECR supported OCI v1.1, some signatures will have image indexes or manifest lists pointing to them. As a result, when you delete a pre-OCI v1.1 image, you might need to manually delete the manifest list that references the image in order to delete the artifact.

**To delete an image (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the image to delete.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, choose the repository that contains the image to delete.

1. On the **Repositories: {{repository\_name}}** page, select the box to the left of the image to delete and choose ** Delete**.

1. In the **Delete image(s)** dialog box, verify that the selected images should be deleted and choose **Delete**.

**To delete an image (AWS CLI)**

1. List the images in your repository. Tagged images will have both an image digest as well as a list of associated tags. Untagged images will only have an image digest.

   ```
   aws ecr list-images \
        --repository-name {{my-repo}}
   ```

1. (Optional) Delete any unwanted tags for the image by specifying the tag associated with the image you want to delete. When the last tag is deleted from an image, the image is also deleted.

   ```
   aws ecr batch-delete-image \
        --repository-name {{my-repo}} \
        --image-ids imageTag={{tag1}} imageTag={{tag2}}
   ```

1. Delete a tagged or untagged image by specifying the image digest. When you delete an image by referencing its digest, the image and all of its tags are deleted.

   ```
   aws ecr batch-delete-image \
        --repository-name {{my-repo}} \
        --image-ids imageDigest={{sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE}}
   ```

   To delete multiple images, you can specify multiple image tags or image digests in the request.

   ```
   aws ecr batch-delete-image \
        --repository-name {{my-repo}} \
        --image-ids imageDigest={{sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE}} imageDigest={{sha256:f5t0e245ssffc302b13e25962d8f7a0bd304EXAMPLE}}
   ```

## Archiving an image in Amazon ECR
<a name="archive_restore_image"></a>

### What is the ECR archival storage class?
<a name="archive-what-is"></a>

Amazon ECR archival storage class is a new storage class that provides low-cost, long-term storage for container images. Amazon ECR offers two storage classes:
+ **ECR standard storage class** – The default storage class for active images that are regularly accessed.
+ **ECR archival storage class** – A low-cost storage class for images that are rarely accessed but need to be retained for compliance or long-term reference. The archival storage class provides cost savings for large amount of images compared to the Standard storage class for long-term image retention. For detailed pricing information, see [Amazon ECR pricing](https://aws.amazon.com/ecr/pricing/). 

To archive images, you have two options. First, you can configure lifecycle rules to automatically archive images based on:
+ Time since the image was pushed
+ Time since the image was last pulled
+ Number of images in the repository

You can also configure settings to permanently delete images after they've been archived for a specified period. Refer to [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies) for more information.

You can also archive images using the Amazon ECR console or AWS CLI. Refer to [Archiving an image](#archive-image) for more information.

When you need to use an archived image again, you can restore it back to the ECR Standard storage class. You can expect ECR to restore the image within 20 minutes. Restored images behave like newly pushed images and are immediately available for use when the restore is complete. Restored images are subject to scanning, replication, and repository lifecycle policies. Refer to [Restoring an image](#restore-image) for more information.

### Archiving an image
<a name="archive-image"></a>

You can archive images manually using the Amazon ECR console or AWS CLI, or automatically using lifecycle policies. When an image is archived:
+ The image is moved to the archival storage class.
+ Archived images cannot be pulled. Requests to pull the archived image will fail with a 404 error.
+ While the image cannot be pulled, it can still be described using the ** describe-images** command, or listed using the **list-images** command. The image status will be shown as `ARCHIVED`.
+ Archived images have a minimum storage duration of 90 days. You cannot configure lifecycle policies that delete images that have been in archive for less than 90 days. If you must delete images that have been archived for less than 90 days, you need to use the **batch-delete-image** API, but you will be charged for the 90-day minimum storage duration.
+ The image appears in an **Archived images** tab in the repository view (this tab will appear only if at least one image is archived in the repository).
+ The image can be restored as an active image by manually selecting it to be restored or by re-pushing the image to the repository.
+ The image will be deleted if the repository has lifecycle policies that delete the image with criteria such as time in archive.

------
#### [ AWS Management Console ]

**To archive an image**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository with the image you want to archive.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, choose the repository containing the image you want to archive.

1. Select the image you want to archive. You will see Image Details.

1. To archive the image, select the **Archive** button and select **Confirm** when you are prompted.

1. If this is the first archived image in the repository, a new **Archived images** tab appears with the newly archived image. If there are other archived images, this image will be added to that tab.

------
#### [ AWS CLI ]

**To archive an image**
+ Use the **update-image-storage-class** command to archive an image by updating its storage class to `ARCHIVE`:

  ```
  aws ecr update-image-storage-class \
      --repository-name {{my-repository}} \
      --image-id imageDigest={{sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE}} \
      --target-storage-class ARCHIVE
  ```

------

**To archive an image using lifecycle policies**
+ You can configure archive rules for your repositories using lifecycle policies to automatically archive images. Lifecycle policies allow you to automatically archive images based on criteria such as:
  + Time since the image was pushed
  + Time since the image was last pulled
  + Maximum number of images to keep active

  You can also configure lifecycle policies to permanently delete images after they've been archived for a specified period. For more information and examples of lifecycle policies with archive actions, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies).
**Note**  
Archived images have a minimum storage duration of 90 days. You cannot configure lifecycle policies that delete images that have been in archive for less than 90 days. If you must delete images that have been archived for less than 90 days, you need to use the **batch-delete-image** API, but you will be charged for the 90-day minimum storage duration.

When you describe images using the **describe-images** command, archived images have an `image-status` of `ARCHIVED`. You can filter images by `image-status` to view only archived images or only active images.

### Restoring an image
<a name="restore-image"></a>

When you restore an archived image, it is moved from the ECR Archive storage class back to the ECR Standard storage class. Restored images are charged at the standard storage rates. The restore process performs similar actions that occur when a new image is created:
+ The image becomes available for pulling when the restore is complete. Restore typically takes up to 20 minutes, though it may complete faster.
+ If scan on push is enabled for the repository, the restored image will be scanned. Note that previous scan results from before the image was archived will not be available.
+ If replication is configured for the repository, the restored image will be replicated if replication was enabled at the time of restore.
+ The restored image appears in the active images list.

Restoring an image typically takes up to 20 minutes, though it may complete faster. During the restore process, the image remains in the archived state and cannot be pulled until the restore completes.

------
#### [ AWS Management Console ]

**To restore an archived image**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository with the archived image you want to restore.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, choose the repository containing the archived image.

1. Choose the **Archived images** tab.

1. Select the archived image you want to restore.

1. Choose **Restore** and confirm the restore action.

1. Wait for the restore to complete. The image will appear in the active images list once restoration is complete.

------
#### [ AWS CLI ]

**To restore an archived image**
+ Use the **update-image-storage-class** command to restore an archived image by updating its storage class to `STANDARD`:

  ```
  aws ecr update-image-storage-class \
      --repository-name {{my-repository}} \
      --image-id imageDigest={{sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE}} \
      --target-storage-class STANDARD
  ```

------

When you describe images using the **describe-images** command, images that are being restored have an `image-status` of `ACTIVATING`. You can filter images by `image-status` with the value `ACTIVATING` to view images that are currently being restored.

An alternative method to restore an archived image is to re-push the image to the repository. When you push an image that is currently archived, that image will be immediately restored and removed from the archive.

## Retagging an image in Amazon ECR
<a name="image-retag"></a>

With Docker Image Manifest V2 Schema 2 images, you can use the `--image-tag` option of the **put-image** command to retag an existing image. You can retag without pulling or pushing the image with Docker. For larger images, this process saves a considerable amount of network bandwidth and time required to retag an image.

### To retag an image (AWS CLI)
<a name="retag-aws-cli"></a>

**To retag an image with the AWS CLI**

1. Use the **batch-get-image** command to get the image manifest for the image to retag and write it to a file. In this example, the manifest for an image with the tag, {{latest}}, in the repository, {{amazonlinux}}, is written to an environment variable named {{MANIFEST}}.

   ```
   MANIFEST=$(aws ecr batch-get-image --repository-name {{amazonlinux}} --image-ids imageTag={{latest}} --output text --query 'images[].imageManifest')
   ```

1. Use the `--image-tag` option of the **put-image** command to put the image manifest to Amazon ECR with a new tag. In this example, the image is tagged as {{2017.03}}.
**Note**  
If the `--image-tag` option isn't available in your version of the AWS CLI, upgrade to the latest version. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide*.

   ```
   aws ecr put-image --repository-name {{amazonlinux}} --image-tag {{2017.03}} --image-manifest "$MANIFEST"
   ```

1. Verify that your new image tag is attached to your image. In the following output, the image has the tags `latest` and ` 2017.03`.

   ```
   aws ecr describe-images --repository-name {{amazonlinux}}
   ```

   The output is as follows:

   ```
   {
       "imageDetails": [
           {
               "imageSizeInBytes": 98755613,
               "imageDigest": "sha256:8d00af8f076eb15a33019c2a3e7f1f655375681c4e5be157a26EXAMPLE",
               "imageTags": [
                   "latest",
                   "2017.03"
               ],
               "registryId": "{{aws_account_id}}",
               "repositoryName": "amazonlinux",
               "imagePushedAt": 1499287667.0
           }
       ]
   }
   ```

### To retag an image (AWS Tools for Windows PowerShell)
<a name="retag-powershell"></a>

**To retag an image with the AWS Tools for Windows PowerShell**

1. Use the **Get-ECRImageBatch** **cmdlet** to obtain the description of the image to retag and write it to an environment variable. In this example, an image with the tag, {{ latest}}, in the repository, {{amazonlinux}}, is written to the environment variable, {{$Image}} .
**Note**  
If you don't have the **Get-ECRImageBatch** ** cmdlet** available on your system, see [Setting up the AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html) in the *AWS Tools for PowerShell User Guide*.

   ```
   $Image = Get-ECRImageBatch -ImageId @{ imageTag="{{latest}}" } -RepositoryName {{amazonlinux}}
   ```

1. Write the manifest of the image to the {{$Manifest}} environment variable.

   ```
   $Manifest = $Image.Images[0].ImageManifest
   ```

1. Use the `-ImageTag` option of the **Write-ECRImage** ** cmdlet** to put the image manifest to Amazon ECR with a new tag. In this example, the image is tagged as {{2017.09}}.

   ```
   Write-ECRImage -RepositoryName {{amazonlinux}} -ImageManifest $Manifest -ImageTag {{2017.09}}
   ```

1. Verify that your new image tag is attached to your image. In the following output, the image has the tags `latest` and ` 2017.09`.

   ```
   Get-ECRImage -RepositoryName {{amazonlinux}}
   ```

   The output is as follows:

   ```
   ImageDigest                                                             ImageTag
   -----------                                                             --------
   sha256:359b948ea8866817e94765822787cd482279eed0c17bc674a7707f4256d5d497 latest
   sha256:359b948ea8866817e94765822787cd482279eed0c17bc674a7707f4256d5d497 2017.09
   ```

## Preventing image tags from being overwritten in Amazon ECR
<a name="image-tag-mutability"></a>

You can prevent image tags from being overwritten by turning on tag immutability in a repository. After tag immutability is turned on, the ` ImageTagAlreadyExistsException` error is returned if you push an image with a tag that is already in the repository. Tag immutability affects all tags. You cannot make some tags immutable while others aren't.

You can use the AWS Management Console and AWS CLI tools to set image tag mutability for a new repository or for an existing repository. To create a repository using console steps, see [Creating an Amazon ECR private repository to store images](#repository-create).

### Setting image tag mutability (AWS Management Console)
<a name="repository-edit"></a>

**To set image tag mutability**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository to edit.

1. In the navigation pane, choose **Repositories** under **Private registry**.

   If you don't see **Repositories**, choose **Private registry** to expand the menu and then choose ** Repositories**.

1. On the **Private repositories** page, choose the radio button before the repository name for which you want to set the image tag mutability settings. 

1. Choose **Actions** and then choose **Repository** under **Edit**.

1. For **Image tag immutability**, choose one of the following tag mutability settings for the repository.
   + **Mutable** – Choose this option if you want image tags to be overwritten. Recommended for repositories using pull through cache actions to ensure Amazon ECR can update cached images. Additionally, to disable tag updates for a few mutable tags, enter tag names or use wildcards (\*) to match multiple similar tags in the **Mutable tag exclusion** text box.
   + **Immutable** – Choose this option if you want to prevent image tags from being overwritten, and it applies to all tags and exclusions in the repository when pushing an image with existing tag. Amazon ECR returns an `ImageTagAlreadyExistsException` if you attempt to push an image with an existing tag. Additionally, to enable tag updates for a few immutable tags, enter tag names or use wildcards (\*) to match multiple similar tags in the **Immutable tag exclusion** text box. 

1. For **Image scan settings**, while you can specify the scan settings at the repository level for basic scanning, it is best practice to specify the scan configuration at the private registry level. Specify the scanning settings at the private registry allow you to enable either enhanced scanning or basic scanning as well as define filters to specify which repositories are scanned. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).

1. For **Encryption settings**, this is a view only field as the encryption settings for a repository can't be changed once the repository is created.

1. Choose **Save** to update the repository settings.

### Setting image tag mutability (AWS CLI)
<a name="image-tag-mutability-cli"></a>

**To create a repository with immutable tags configured**

Use one of the following commands to create a new image repository with immutable tags configured.
+ [create-repository](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository.html) (AWS CLI) with image tag mutability

  ```
  aws ecr create-repository --repository-name {{name}} --image-tag-mutability {{IMMUTABLE}} --region {{us-east-2}}
  ```
+ [create-repository](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository.html) (AWS CLI) with image tag mutability exclusion filters

  ```
  aws ecr create-repository --repository-name {{name}} --image-tag-mutability {{IMMUTABLE_WITH_EXCLUSION}} --image-tag-mutability-exclusion-filters filterType={{WILDCARD}},filter={{filter-text}} --region {{us-east-2}}
  ```
+ [New-ECRRepository](https://docs.aws.amazon.com/powershell/latest/reference/items/New-ECRRepository.html) (AWS Tools for Windows PowerShell) with image tag mutability

  ```
  New-ECRRepository -RepositoryName {{name}} -ImageTagMutability {{IMMUTABLE}} -Region {{us-east-2}} -Force
  ```
+ [New-ECRRepository](https://docs.aws.amazon.com/powershell/latest/reference/items/New-ECRRepository.html) (AWS Tools for Windows PowerShell) with image tag mutability exclusion filters

  ```
  New-ECRRepository -RepositoryName {{name}} -ImageTagMutability {{IMMUTABLE_WITH_EXCLUSION}} -ImageTagMutabilityExclusionFilter @{FilterType={{WILDCARD}} Filter={{filter-text}}} -Region {{us-east-2}} -Force
  ```

**To update the image tag mutability settings for a repository**

Use one of the following commands to update the image tag mutability settings for an existing repository.
+ [ put-image-tag-mutability](https://docs.aws.amazon.com/cli/latest/reference/ecr/put-image-tag-mutability.html) (AWS CLI) with image tag mutability

  ```
  aws ecr put-image-tag-mutability --repository-name {{name}} --image-tag-mutability {{IMMUTABLE}} --region {{us-east-2}}
  ```
+ [ put-image-tag-mutability](https://docs.aws.amazon.com/cli/latest/reference/ecr/put-image-tag-mutability.html) (AWS CLI) with image tag mutability exclusion filters

  ```
  aws ecr put-image-tag-mutability --repository-name {{name}} --image-tag-mutability {{IMMUTABLE_WITH_EXCLUSION}} --image-tag-mutability-exclusion-filters filterType={{WILDCARD}},filter={{latest}} --region {{us-east-2}}
  ```
+ [ Write-ECRImageTagMutability](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-ECRImageTagMutability.html) (AWS Tools for Windows PowerShell) with image tag mutability

  ```
  Write-ECRImageTagMutability -RepositoryName {{name}} -ImageTagMutability {{IMMUTABLE}} -Region {{us-east-2}} -Force
  ```
+ [ Write-ECRImageTagMutability](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-ECRImageTagMutability.html) (AWS Tools for Windows PowerShell) with image tag mutability exclusion filters

  ```
  Write-ECRImageTagMutability -RepositoryName {{name}} -ImageTagMutability {{IMMUTABLE_WITH_EXCLUSION}} -ImageTagMutabilityExclusionFilter @{FilterType={{WILDCARD}} Filter={{latest}}}
  ```

## Container image manifest format support in Amazon ECR
<a name="image-manifest-formats"></a>

Amazon ECR supports the following container image manifest formats:
+ Docker Image Manifest V2 Schema 1 (used with Docker version 1.9 and older)
+ Docker Image Manifest V2 Schema 2 (used with Docker version 1.10 and newer)
+ Open Container Initiative (OCI) Specifications (v1.0 and v1.1)

Support for Docker Image Manifest V2 Schema 2 provides the following functionality:
+ The ability to use multiple tags for a singular image.
+ Support for storing Windows container images.

### Amazon ECR image manifest conversion
<a name="image-manifest-conversion"></a>

When you push and pull images to and from Amazon ECR, your container engine client (for example, Docker) communicates with the registry to agree on a manifest format that is understood by the client and the registry to use for the image. 

When you push an image to Amazon ECR with Docker version 1.9 or earlier, the image manifest format is stored as Docker Image Manifest V2 Schema 1. When you push an image to Amazon ECR with Docker version 1.10 or later, the image manifest format is stored as Docker Image Manifest V2 Schema 2.

When you pull an image from Amazon ECR *by tag*, Amazon ECR returns the image manifest format that is stored in the repository. The format is returned only if that format is understood by the client. If the stored image manifest format isn't understood by the client, Amazon ECR converts the image manifest into a format that is understood. For example, if a Docker 1.9 client requests an image manifest that is stored as Docker Image Manifest V2 Schema 2, Amazon ECR returns the manifest in the Docker Image Manifest V2 Schema 1 format. The following table describes the available conversions supported by Amazon ECR when an image is pulled *by tag*: 


| Schema requested by client | Pushed to ECR as V2, schema 1 | Pushed to ECR as V2, schema 2 | Pushed to ECR as OCI | 
| --- | --- | --- | --- | 
| V2, schema 1 | No translation required | Translated to V2, schema 1 | No translation available | 
| V2, schema 2 | No translation available, client falls back to V2, schema 1 | No translation required | Translated to V2, schema 2 | 
| OCI | No translation available | Translated to OCI | No translation required | 

**Important**  
If you pull an image *by digest*, there is no translation available. Your client must understand the image manifest format that is stored in Amazon ECR. If you request a Docker Image Manifest V2 Schema 2 image by digest on a Docker 1.9 or older client, the image pull fails. For more information, see [Registry compatibility](https://docs.docker.com/registry/compatibility/) in the Docker documentation.  
In this example, if you request the same image *by tag*, Amazon ECR translates the image manifest into a format that the client can understand. The image pull succeeds.

## Using Amazon ECR images with Amazon ECS
<a name="ECR_on_ECS"></a>

You can use your Amazon ECR private repositories to host container images and artifacts that your Amazon ECS tasks may pull from. For this to work, the Amazon ECS, or Fargate, container agent must have permissions to make the `ecr:BatchGetImage`, `ecr:GetDownloadUrlForLayer`, and `ecr:GetAuthorizationToken` APIs.

### Required IAM permissions
<a name="ECR_on_ECS_iampermissions"></a>

The following table shows the IAM role to use, for each launch type, that provides the required permissions for your tasks to pull from an Amazon ECR private repository. Amazon ECS provides managed IAM policies that include the required permissions.



| Launch type | IAM role | AWS managed IAM policy | 
| --- | --- | --- | 
| Amazon ECS on Amazon EC2 instances | Use the container instance IAM role, which is associated with the Amazon EC2 instance registered to your Amazon ECS cluster. For more information, see [Container instance IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*. | `AmazonEC2ContainerServiceforEC2Role`<br />For more information, see [AmazonEC2ContainerServiceforEC2Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role) in the *Amazon Elastic Container Service Developer Guide* | 
| Amazon ECS on Fargate | Use the task execution IAM role that you reference in your Amazon ECS task definition. For more information, see [Task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*. | `AmazonECSTaskExecutionRolePolicy`<br />For more information, see [AmazonECSTaskExecutionRolePolicy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonECSTaskExecutionRolePolicy) in the *Amazon Elastic Container Service Developer Guide*. | 
| Amazon ECS on external instances | Use the container instance IAM role, which is associated with the on-premises server or virtual machine (VM) registered to your Amazon ECS cluster. For more information, see [Container instance Amazon ECS role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*. | `AmazonEC2ContainerServiceforEC2Role`<br />For more information, see [AmazonEC2ContainerServiceforEC2Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role) in the *Amazon Elastic Container Service Developer Guide*. | 

**Important**  
The AWS managed IAM policies contain additional permissions that you may not require for your use. In this case, these are the minimum required permissions to pull from an Amazon ECR private repository.  

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
    ]
}
```

### Specifying an Amazon ECR image in an Amazon ECS task definition
<a name="ECR_on_ECS_taskdef"></a>

When creating an Amazon ECS task definition, you can specify a container image hosted in an Amazon ECR private repository. In the task definition, ensure that you use the full `registry/repository:tag` naming for your Amazon ECR images. For example, `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com``/{{my-repository}}:{{latest}}`.

The following task definition snippet shows the syntax you would use to specify a container image hosted in Amazon ECR in your Amazon ECS task definition.

```
{
    "family": "{{task-definition-name}}",
    ...
    "containerDefinitions": [
        {
            "name": "{{container-name}}",
            "image": "{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository}}:{{latest}}",
            ...
        }
    ],
    ...
}
```

## Using Amazon ECR Images with Amazon EKS
<a name="ECR_on_EKS"></a>

You can use your Amazon ECR images with Amazon EKS.

When referencing an image from Amazon ECR, you must use the full `registry/repository:tag` naming for the image. For example, `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com``/{{my-repository}}:{{latest}}`.

### Required IAM permissions
<a name="ECR_on_EKS_iampermissions"></a>

If you have Amazon EKS workloads hosted on managed nodes, self-managed nodes, or AWS Fargate, review the following:
+ Amazon EKS workloads hosted on managed or self-managed nodes: The Amazon EKS worker node IAM role (`NodeInstanceRole`) is required. The Amazon EKS worker node IAM role must contain the following IAM policy permissions for Amazon ECR.

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
                  "ecr:BatchCheckLayerAvailability",
                  "ecr:BatchGetImage",
                  "ecr:GetDownloadUrlForLayer",
                  "ecr:GetAuthorizationToken"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

------
**Note**  
If you used `eksctl` or the CloudFormation templates in [Getting Started with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) to create your cluster and worker node groups, these IAM permissions are applied to your worker node IAM role by default.
+ Amazon EKS workloads hosted on AWS Fargate: Use the Fargate pod execution role, which provides your pods permission to pull images from private Amazon ECR repositories. For more information, see [Create a Fargate pod execution role](https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html#fargate-sg-pod-execution-role).

### Installing a Helm chart on an Amazon EKS cluster
<a name="using-helm-charts-eks"></a>

Helm charts hosted in Amazon ECR can be installed on your Amazon EKS clusters.

**Prerequisites**
+ Install the latest version of the Helm client. These steps were written using Helm version `3.9.0`. For more information, see [Installing Helm](https://helm.sh/docs/intro/install/).
+ You have at least version `1.23.9` or `2.6.3` of the AWS CLI installed on your computer. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ You have pushed a Helm chart to your Amazon ECR repository. For more information, see [Pushing a Helm chart to an Amazon ECR private repository](#push-oci-artifact).
+ You have configured `kubectl` to work with Amazon EKS. For more information, see [Create a `kubeconfig` for Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html) in the **Amazon EKS User Guide**. If the following commands succeeds for your cluster, you're properly configured.

  ```
  kubectl get svc
  ```

**To install a Helm chart on an Amazon EKS cluster**

1. Authenticate your Helm client to the Amazon ECR registry that your Helm chart is hosted. Authentication tokens must be obtained for each registry used, and the tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

   ```
   aws ecr get-login-password \
        --region {{us-west-2}} | helm registry login \
        --username AWS \
        --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com
   ```

1. Install the chart. Replace {{helm-test-chart}} with your repository and {{0.1.0}} with your Helm chart's tag.

   ```
   helm install ecr-chart-demo oci://{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{helm-test-chart}} --version {{0.1.0}}
   ```

   The output should look similar to this:

   ```
   NAME: ecr-chart-demo
   LAST DEPLOYED: Tue May 31 17:38:56 2022
   NAMESPACE: default
   STATUS: deployed
   REVISION: 1
   TEST SUITE: None
   ```

1. Verify the chart installation. 

   ```
   helm list -n default
   ```

   Example output:

   ```
   NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
   ecr-chart-demo  default         1               2022-06-01 15:56:40.128669157 +0000 UTC deployed        helm-test-chart-0.1.0   1.16.0
   ```

1. (Optional) See the installed Helm chart `ConfigMap`.

   ```
   kubectl describe configmap {{helm-test-chart-configmap}}
   ```

1. When you are finished, you can remove the chart release from your cluster.

   ```
   helm uninstall {{ecr-chart-demo}}
   ```

# Sign images in Amazon ECR
<a name="image-signing"></a>

Amazon ECR integrates with AWS Signer to provide two ways for you to sign your container images: *managed signing* (automatic, recommended) and *manual signing* (client-side). You can store both your container images and the signatures in your private repositories.

## Choose a signing method
<a name="image-signing-choose-method"></a>

Amazon ECR supports two methods for signing container images:

**Managed signing** (recommended)  
Managed signing automatically generates cryptographic signatures when images are pushed to Amazon ECR. This method simplifies setup. Managed signing is the recommended approach for most users. For more information, see [Managed signing](#managed-signing).

**Manual signing**  
Manual signing uses the Notation CLI and AWS Signer plugin to sign images before pushing them to Amazon ECR. This method provides more control over the signing process and is useful when you need to sign images outside of the push workflow or require fine-grained control over signing operations. For more information, see [Manual signing](#image-signing-manual).

## Considerations
<a name="image-signing-considerations"></a>

The following should be considered when using Amazon ECR image signing:
+ Signatures stored in your repository count against the service quota for the maximum number of images per repository. Each signature counts as 1 artifact against the images per repository quota. For more information, see [Amazon ECR service quotas](#service-quotas).
+ When reference artifacts are present in a repository, Amazon ECR lifecycle policies will automatically clean up those artifacts within 24 hours of the deletion of the subject image. The artifact must also remain in its current storage class for at least 24 hours before Amazon ECR lifecycle policies can clean it up.

## Managed signing
<a name="managed-signing"></a>

Amazon ECR managed signing automatically signs your container images by generating cryptographic signatures using [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) when images are pushed to Amazon ECR. This eliminates the need to install and configure client-side tools and allows you to centrally govern signing as a registry configuration.

### Prerequisites
<a name="managed-signing-prerequisites"></a>

To configure managed signing, you create a signing configuration with Amazon ECR that references one or more Signer signing profiles and, optionally, repository filters that restrict which repositories should have their images signed. Once configured, Amazon ECR managed signing automatically signs images as they are pushed using the identity of the entity pushing the image.

Before you can configure managed signing, you must have the following:
+ **A Signer signing profile** — Create at least one Signer [signing profile](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profiles.html). A signing profile is a unique AWS Signer resource that you can use to perform signing operations in Amazon ECR. Signing profiles enable you to sign and verify code artifacts, such as container images and AWS Lambda deployment bundles. Each signing profile designates the signing platform to sign for, a platform ID, and other platform-specific information. For example, a signing profile ARN looks like this: `arn:{{partition}}:signer:{{region}}:{{account-id}}:/signing-profiles/{{profile-name}}`.
+ **IAM permissions** — The IAM principal that pushes the image must have the necessary IAM permissions to access the relevant Signer signing profile and the relevant ECR repository. You need to modify the identity-based policy for the IAM principal to include permissions for both ECR repository operations and Signer signing operations. The following example policy shows the required permissions:

```
{
   "Version": "2012-10-17",		 	 	 
   "Statement": [
   {
       "Sid":"UploadSignaturePermissions",
       "Effect":"Allow",
       "Action":[
           "ecr:CompleteLayerUpload",
           "ecr:UploadLayerPart",
           "ecr:InitiateLayerUpload",
           "ecr:BatchCheckLayerAvailability",
           "ecr:PutImage"
       ],
       "Resource":"arn:aws:ecr:{{region}}:{{account-id}}:repository/{{repository-name}}"
   },
   {
       "Sid": "SignPermissions",
       "Effect": "Allow",
       "Action": [
           "signer:SignPayload"
       ],
       "Resource": "arn:aws:signer:{{region}}:{{account-id}}:/signing-profiles/{{signing-profile-name}}"
   }
   ]
}
```

With Amazon ECR managed signing, you can create multiple signing rules (up to 10 per registry) to create stronger security boundaries. For example, you might run multiple build pipelines and want to limit which repositories each pipeline can sign. Within each rule, you configure a signing profile and specify repository name filters. When a new image is pushed, Amazon ECR matches which signing rule and signing profile can sign the image. If there are multiple matches, Amazon ECR generates multiple signatures.

**Note**  
If you verify signatures manually, you still need to install the Notation CLI.

**Note**  
Amazon ECR managed signing is available in all AWS Regions where container image signing with AWS Signer is available.

### Getting started
<a name="managed-signing-getting-started"></a>

Follow these steps to configure managed signing. You provide Amazon ECR with a reference to a Signer signing profile and, optionally, filters that restrict which repositories should have their images signed.

------
#### [ AWS Management Console ]

Use the following steps to configure managed signing using the AWS Management Console.

1. Open the [ Amazon ECR console](https://console.aws.amazon.com/ecr/private-registry/repositories). In the left navigation pane, select **Private registry**, **Features & settings**, **Managed signing**.

1. On the **Signing rules** page, select **Create rule**.

1. On the **Signing profile** page, under **Select a AWS signer profile**, choose **Create new AWS signer profile**, enter a **Profile name**, and, optionally, change the **Signature validity period**. Then select **Next**.

1. On the **Filters** page, under **Select repositories**, enter a **Repository name filter**. Then select **Next**.

1. On the **Review and create** page, verify the **AWS Signer profile** and **Repository name filters** you have entered. If everything looks correct, select **Save**.

------
#### [ AWS CLI ]

Use the following AWS CLI commands to configure managed signing.
+ **Create a signing rule**

  Create a signing configuration with your signing profile ARN. Create a JSON file with the following contents:

  ```
  {
      "rules": [ 
          { 
              "signingProfileArn": "arn:aws:signer:{{region}}:{{account-id}}:/signing-profiles/{{profile-name}}",
              "repositoryFilters": [ 
                  { 
                      "filter": "{{test*}}",
                      "filterType": "WILDCARD_MATCH"
                  }
              ]
          }
      ]
  }
  ```

  Then run the following command:

  ```
  aws ecr --region {{region}} \
      put-signing-configuration \
      --signing-configuration file://signing-config.json
  ```

  You should see the API response containing the signing configuration.
+ **View your signing configuration**

  Retrieve your signing configuration:

  ```
  aws ecr --region {{region}} \
      get-signing-configuration
  ```

  You should see the API response containing the signing configuration.
+ **Check image signing status**

  Push an image to your repository. For example:

  ```
  docker pull ubuntu
  
  IMAGE_NAME="{{account-id}}.dkr.ecr.{{region}}.amazonaws.com/{{repository-name}}"
  IMAGE_TAG="${IMAGE_NAME}:{{test-1}}"
  
  docker tag ubuntu $IMAGE_TAG
  docker push $IMAGE_TAG
  ```

  After pushing, use your image tag to check the signing status:

  ```
  aws ecr --region {{region}} \
      describe-image-signing-status \
      --repository-name {{repository-name}} \
      --image-id imageTag={{test-1}}
  ```

  If the repository name matches your repository filter defined in the signing configuration, you should see signing status in the API response. If the status is successful, you should see a signature pushed to your repository.
+ **Delete your signing configuration**

  Delete your signing configuration:

  ```
  aws ecr --region {{region}} \
      delete-signing-configuration
  ```

  You should see the API response containing the deleted signing configuration.

------

### Considerations
<a name="managed-signing-considerations"></a>

The following limitations and capabilities apply to managed signing:
+ **Cross-region signing is not supported** — Signing profiles must be in the same region as your Amazon ECR registry. You cannot use a signing profile from one region to sign images in a registry located in a different region.
+ **Cross-account signing is supported** — Signing profiles can be in different accounts than your Amazon ECR registry. This enables organizations to centrally manage signing profiles while allowing developers in other accounts to use them. For more information, see [Set up cross-account signing for Signer](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profile-cross-account.html) in the *AWS Signer Developer Guide*.
+ **Signatures cannot be signed** — You cannot sign signatures themselves. Only container images can be signed.

## Signature verification
<a name="image-signing-verification"></a>

After you sign your container images, you can verify the signatures to ensure that images have not been tampered with and come from a trusted source. Amazon ECR supports several methods for verifying signatures:

### Managed verification with Amazon EKS
<a name="image-signing-verification-managed"></a>

Amazon EKS provides native integration for automatic signature verification. When you configure signature verification in your Amazon EKS clusters, the service automatically verifies image signatures before allowing containers to run. For more information about configuring signature verification, see [Validate container image signatures during deployment](https://docs.aws.amazon.com/eks/latest/userguide/image-verification.html) in the *Amazon EKS User Guide*.

### Lambda admission controller for Amazon ECS
<a name="image-signing-verification-lambda"></a>

Amazon ECS provides service lifecycle hooks that allow you to run custom logic during service deployments. These hooks can trigger AWS Lambda functions at specific points in the deployment process, enabling you to validate container image signatures before allowing services to start. For more information, see [Verify container image signatures for Amazon ECS](https://docs.aws.amazon.com/signer/latest/developerguide/ecs-verification.html) in the *AWS Signer Developer Guide*.

### Manual verification with Notation CLI
<a name="image-signing-verification-manual"></a>

You can verify signatures manually using the Notation CLI. This method requires you to install and configure the Notation CLI on your local machine or in your verification environment. For detailed instructions about verifying an image using Notation CLI, see [Verify an image locally after signing](https://docs.aws.amazon.com/signer/latest/developerguide/image-verification.html) in the *AWS Signer Developer Guide*.

### Configure authentication for the Notation client
<a name="image-signing-authentication"></a>

If you use manual signing or verify signatures manually using the Notation CLI, you must configure the Notation client so it can authenticate to Amazon ECR. If you have Docker installed on the same host where you install the Notation client, then Notation will reuse the same authentication method you use for the Docker client. The Docker `login` and `logout` commands will allow the Notation `sign` and `verify` commands to use those same credentials, and you don't have to separately authenticate Notation. For more information on configuring your Notation client for authentication, see [Authenticate with OCI-compliant registries](https://notaryproject.dev/docs/user-guides/how-to/registry-authentication/) in the Notary Project documentation.

If you are not using Docker or another tool that uses Docker credentials, then we recommend using the Amazon ECR Docker Credential Helper as your credential store. For more information on how to install and configure the Amazon ECR Credential Helper, see [Amazon ECR Docker Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper).

## Manual signing
<a name="image-signing-manual"></a>

Manual signing uses the Notation CLI and AWS Signer plugin to sign images before pushing them to Amazon ECR. This method provides more control over the signing process and is useful when you need to sign images outside of the push workflow or require fine-grained control over signing operations.

For detailed instructions about signing container images using the Notation CLI and AWS Signer, see [Sign container images in Signer](https://docs.aws.amazon.com/signer/latest/developerguide/container-workflow.html) and the related topics in the *AWS Signer Developer Guide*.

### Prerequisites
<a name="image-signing-prerequisites"></a>

Before you begin, The following prerequisites must be met.
+ Install and configure the latest version of the AWS CLI. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.
+ Install the Notation CLI and the AWS Signer plugin for Notation. For more information, see [Prerequisites for signing container images](https://docs.aws.amazon.com/signer/latest/developerguide/image-signing-prerequisites.html) in the *AWS Signer Developer Guide*.
+ Have a container image stored in an Amazon ECR private repository to sign. For more information, see [Pushing an image to an Amazon ECR private repository](#image-push).

# Scan images for software vulnerabilities in Amazon ECR
<a name="image-scanning"></a>

Amazon ECR image scanning helps to identify software vulnerabilities in your container images. The following scanning types are offered.

**Important**  
Switching between **Enhanced scanning** and **Basic scanning** will cause previously established scans to no longer be available. You will have to set up your scans again. However, if you switch back to your previous scanning type the established scans will be available. 

**Note**  
Archived images cannot be scanned. Archived images must be restored before they can be scanned. For more information about archiving and restoring images, see [Archiving an image in Amazon ECR](#archive_restore_image).
+ **Enhanced scanning** – Amazon ECR integrates with Amazon Inspector to provide automated, continuous scanning of your repositories. Your container images are scanned for both operating systems and programming language package vulnerabilities. As new vulnerabilities appear, the scan results are updated and Amazon Inspector emits an event to EventBridge to notify you. Enhanced scanning provides the following:
  + OS and programming languages package vulnerabilities
  + Two scanning frequencies: Scan on push and continuous scan
+ **Basic scanning** – Amazon ECR uses AWS native technology with the Common Vulnerabilities and Exposures (CVEs) database to scan for operating system vulnerabilities.

  With basic scanning, you configure your repositories to scan on push or you can perform manual scans and Amazon ECR provides a list of scan findings. Basic scanning provides the following:
  + OS scans
  + Two scanning frequencies: Manual and scan on push
**Important**  
The new version of Amazon ECR Basic Scanning doesn't use the ` imageScanFindingsSummary` and `imageScanStatus` attributes from the `DescribeImages` API response to return scan results. Use the ` DescribeImageScanFindings` API instead. For more information, see [`DescribeImageScanFindings`](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageScanFindings.html).

## Filters to choose which repositories are scanned in Amazon ECR
<a name="image-scanning-filters"></a>

When you configure image scanning for your private registry, you can use filters to choose which repositories are scanned. 

When **basic** scanning is used, you may specify scan on push filters to specify which repositories are set to do an image scan when new images are pushed. Any repositories not matching a basic scanning scan on push filter will be set to the ** manual** scan frequency which means to perform a scan, you must manually trigger the scan. 

When **enhanced** scanning is used, you may specify separate filters for scan on push and continuous scanning. Any repositories not matching an enhanced scanning filter will have scanning disabled. If you are using enhanced scanning and specify separate filters for scan on push and continuous scanning where multiple filters match the same repository, then Amazon ECR enforces the continuous scanning filter over the scan on push filter for that repository.

### Filter wildcards
<a name="image-scanning-filters-wildcards"></a>

When a filter is specified, a filter with no wildcard will match all repository names that contain the filter. A filter with a wildcard (`*`) matches on any repository name where the wildcard replaces zero or more characters in the repository name.

The following table provides examples where repository names are expressed on the horizontal axis and example filters are specified on the vertical axis.


|  |  prod  |  repo-prod  |  prod-repo  |  repo-prod-repo  |  prodrepo  | 
| --- | --- | --- | --- | --- | --- | 
| prod | Yes | Yes | Yes | Yes | Yes | 
| \*prod | Yes | Yes | No | No | No | 
| prod\* | Yes | No | Yes | No | Yes | 
| \*prod\* | Yes | Yes | Yes | Yes | Yes | 
| prod\*repo | No | No | Yes | No | Yes | 

## Scan images for OS and programming language package vulnerabilities in Amazon ECR
<a name="image-scanning-enhanced"></a>

Amazon ECR enhanced scanning is an integration with Amazon Inspector which provides vulnerability scanning for your container images. Your container images are scanned for both operating systems and programming language package vulnerabilities. You can view the scan findings with both Amazon ECR and with Amazon Inspector directly. For more information about Amazon Inspector, see [Scanning container images with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/enable-disable-scanning-ecr.html) in the *Amazon Inspector User Guide*.

With enhanced scanning, you can choose which repositories are configured for automatic, continuous scanning and which are configured for scan on push. This is done by setting scan filters.

### Considerations for enhanced scanning
<a name="image-scanning-enhanced-considerations"></a>

Consider the following before enabling Amazon ECR enhanced scanning.
+ There is no additional cost from Amazon ECR to use this feature, however there is a cost from Amazon Inspector to scan your images. This feature is available in Regions where Amazon Inspector is supported. For more information, see:
  + Amazon Inspector pricing – [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/).
  + Amazon Inspector supported Regions – [Regions and endpoints](https://docs.aws.amazon.com/inspector/latest/user/inspector_regions.html).
+ Amazon ECR enhanced scanning shows how images are used on Amazon EKS and Amazon ECS. You can see when images were last used and identify how many clusters use each image. This information helps you prioritize vulnerability remediation for actively used images. You can quickly determine which clusters might be affected by newly discovered vulnerabilities. For more information about how to request these information and view the response, see [`DescribeImageScanFindings`](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageScanFindings.html).
+ Amazon Inspector supports scanning for specific operating systems. For a full list, see [Supported operating systems - Amazon ECR scanning](https://docs.aws.amazon.com/inspector/latest/user/supported.html#supported-os) in the *Amazon Inspector User Guide*.
+ Amazon Inspector uses a service-linked IAM role, which provides the permissions needed to provide enhanced scanning for your repositories. The service-linked IAM role is created automatically by Amazon Inspector when enhanced scanning is turned on for your private registry. For more information, see [Using service-linked roles for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/using-service-linked-roles.html) in the *Amazon Inspector User Guide*.
+ When you initially turn on enhanced scanning for your private registry, Amazon Inspector only recognizes images pushed to Amazon ECR in the last 14 days, based on the image push timestamp. Older images will have the ` SCAN_ELIGIBILITY_EXPIRED` scan status. If you'd like these images to be scanned by Amazon Inspector you should push them again to your repository.
+ When enhanced scanning is turned on for your Amazon ECR private registry, repositories matching the scan filters are scanned using enhanced scanning only. Any repositories that don't match a filter will have an `Off` scan frequency and won't be scanned. Manual scans using enhanced scanning aren't supported. For more information, see [Filters to choose which repositories are scanned in Amazon ECR](#image-scanning-filters).
+ If you specify separate filters for scan on push and continuous scanning where multiple filters match the same repository, then Amazon ECR enforces the continuous scanning filter over the scan on push filter for that repository.
+ When enhanced scanning is turned on, Amazon ECR sends an event to EventBridge when the scan frequency for a repository is changed. Amazon Inspector emits events to EventBridge when an initial scan is completed and when an image scan finding is created, updated, or closed.

### Changing the enhanced scanning duration for images in Amazon Inspector
<a name="image-scanning-enhanced-duration"></a>

After enabling enhanced scanning, Amazon ECR continually scans newly pushed images for the configured duration. By default, Amazon Inspector monitors your repositories until images are deleted or enhanced scanning is disabled. You can configure both push date duration (up to Lifetime) and re-scan duration in the Amazon Inspector console to suit your environment's needs. When the scan duration for a repository elapses, the scan status shows as `SCAN_ELIGIBILITY_EXPIRED`. For more information about configuring re-scan duration settings for Amazon ECR in Amazon Inspector, see [Configuring the Amazon ECR re-scan duration](https://docs.aws.amazon.com/inspector/latest/user/enable-disable-scanning-ecr.html#scan-duration-setting) in the *Amazon Inspector User Guide*.

### IAM permissions required for enhanced scanning in Amazon ECR
<a name="image-scanning-enhanced-iam"></a>

Amazon ECR enhanced scanning requires an Amazon Inspector service-linked IAM role and that the IAM principal enabling and using enhanced scanning has permissions to call the Amazon Inspector APIs needed for scanning. The Amazon Inspector service-linked IAM role is created automatically by Amazon Inspector when enhanced scanning is turned on for your private registry. For more information, see [Using service-linked roles for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/using-service-linked-roles.html) in the *Amazon Inspector User Guide*.

The following IAM policy grants the required permissions for enabling and using enhanced scanning. It includes the permission needed for Amazon Inspector to create the service-linked IAM role as well as the Amazon Inspector API permissions needed to turned on and off enhanced scanning and retrieve the scan findings.

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
                "inspector2:Enable",
                "inspector2:Disable",
                "inspector2:ListFindings",
                "inspector2:ListAccountPermissions",
                "inspector2:ListCoverage"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": [
                        "inspector2.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

------

### Configuring enhanced scanning for images in Amazon ECR
<a name="image-scanning-enhanced-enabling"></a>

Configure enhanced scanning per Region for your private registry.

Verify that you have the proper IAM permissions to configure enhanced scanning. For information, see [IAM permissions required for enhanced scanning in Amazon ECR](#image-scanning-enhanced-iam).

------
#### [ AWS Management Console ]

**To turn on enhanced scanning for your private registry**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region to set the scanning configuration for.

1. In the navigation pane, choose **Private registry**, and then choose **Settings** .

1. On the **Scanning configuration** page, for **Scan type** choose **Enhanced scanning**.

   By default, when **Enhanced scanning** is selected, all of your repositories are continuously scanned.

1. To choose specific repositories to continuously scan, clear the **Continuously scan all repositories** box, and then define your filters:
**Important**  
Filters with no wildcard will match all repository names that contain the filter. Filters with wildcards (`*`) match on a repository name where the wildcard replaces zero or more characters in the repository name. To see examples of how filters behave, see [Filter wildcards](#image-scanning-filters-wildcards).

   1. Enter a filter based on repository names, and then choose **Add filter**.

   1. Decide which repositories to scan when an image is pushed:
      + To scan all repositories on push, select **Scan on push all repositories**.
      + To choose specific repositories to scan on push, enter a filter based on repository names, and then choose **Add filter**.

1. Choose **Save**.

1. Repeat these steps in each Region in which you want to turn on enhanced scanning.

------
#### [ AWS CLI ]

Use the following AWS CLI command to turn on enhanced scanning for your private registry using the AWS CLI. You can specify scan filters using the ` rules` object.
+ [ put-registry-scanning-configuration](https://docs.aws.amazon.com/cli/latest/reference/ecr/put-registry-scanning-configuration.html) (AWS CLI)

  The following example turns on enhanced scanning for your private registry. By default, when no `rules` are specified, Amazon ECR sets the scanning configuration to continuous scanning for all repositories.

  ```
  aws ecr put-registry-scanning-configuration \
       --scan-type {{ENHANCED}} \
       --region {{us-east-2}}
  ```

  The following example turns on enhanced scanning for your private registry and specifies a scan filter. The scan filter in the example turns on continuous scanning for all repositories with `prod` in its name.

  ```
  aws ecr put-registry-scanning-configuration \
       --scan-type {{ENHANCED}} \
       --rules '[{"repositoryFilters" : [{"filter":"{{prod}}","filterType" : "WILDCARD"}],"scanFrequency" : "{{CONTINUOUS_SCAN}}"}]' \
       --region {{us-east-2}}
  ```

  The following example turns on enhanced scanning for your private registry and specifies multiple scan filters. The scan filters in the example turns on continuous scanning for all repositories with `prod` in its name and turns on scan on push only for all other repositories.

  ```
  aws ecr put-registry-scanning-configuration \
       --scan-type {{ENHANCED}} \
       --rules '[{"repositoryFilters" : [{"filter":"{{prod}}","filterType" : "WILDCARD"}],"scanFrequency" : "{{CONTINUOUS_SCAN}}"},{"repositoryFilters" : [{"filter":"{{*}}","filterType" : "WILDCARD"}],"scanFrequency" : "{{SCAN_ON_PUSH}}"}]' \
       --region {{us-west-2}}
  ```

------

### EventBridge events sent for enhanced scanning in Amazon ECR
<a name="image-scanning-enhanced-events"></a>

When enhanced scanning is turned on, Amazon ECR sends an event to EventBridge when the scan frequency for a repository is changed. Amazon Inspector sends events to EventBridge when an initial scan is completed and when an image scan finding is created, updated, or closed.

 **Event for a repository scan frequency change** 

When enhanced scanning is turned on for your registry, the following event is sent by Amazon ECR when there is a change with a resource that has enhanced scanning turned on. This includes new repositories being created, the scan frequency for a repository being changed, or when images are created or deleted in repositories with enhanced scanning turned on. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).

```
{
	"version": "0",
	"id": "0c18352a-a4d4-6853-ef53-0abEXAMPLE",
	"detail-type": "ECR Scan Resource Change",
	"source": "aws.ecr",
	"account": "{{123456789012}}",
	"time": "2021-10-14T20:53:46Z",
	"region": "{{us-east-1}}",
	"resources": [],
	"detail": {
		"action-type": "SCAN_FREQUENCY_CHANGE",
		"repositories": [{
				"repository-name": "repository-1",
				"repository-arn": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/repository-1",
				"scan-frequency": "SCAN_ON_PUSH",
				"previous-scan-frequency": "MANUAL"
			},
			{
				"repository-name": "repository-2",
				"repository-arn": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/repository-2",
				"scan-frequency": "CONTINUOUS_SCAN",
				"previous-scan-frequency": "SCAN_ON_PUSH"
			},
			{
				"repository-name": "repository-3",
				"repository-arn": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/repository-3",
				"scan-frequency": "CONTINUOUS_SCAN",
				"previous-scan-frequency": "SCAN_ON_PUSH"
			}
		],
		"resource-type": "REPOSITORY",
		"scan-type": "ENHANCED"
	}
}
```

 **Event for an initial image scan (enhanced scanning)** 

When enhanced scanning is turned on for your registry, the following event is sent by Amazon Inspector when the initial image scan is completed. The `finding-severity-counts` parameter will only return a value for a severity level if one exists. For example, if the image contains no findings at `CRITICAL` level, then no critical count is returned. For more information, see [Scan images for OS and programming language package vulnerabilities in Amazon ECR](#image-scanning-enhanced).

Event pattern:

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["Inspector2 Scan"]
}
```

Example output:

```
{
    "version": "0",
    "id": "739c0d3c-4f02-85c7-5a88-94a9EXAMPLE",
    "detail-type": "Inspector2 Scan",
    "source": "aws.inspector2",
    "account": "{{123456789012}}",
    "time": "2021-12-03T18:03:16Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:ecr:us-east-2:{{123456789012}}:repository/amazon/amazon-ecs-sample"
    ],
    "detail": {
        "scan-status": "INITIAL_SCAN_COMPLETE",
        "repository-name": "arn:aws:ecr:us-east-2:123456789012:repository/amazon/amazon-ecs-sample",
        "finding-severity-counts": {
            "CRITICAL": 7,
            "HIGH": 61,
            "MEDIUM": 62,
            "TOTAL": 158
        },
        "image-digest": "sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77e5EXAMPLE",
        "image-tags": [
            "latest"
        ]
    }
}
```

 **Event for an image scan finding update (enhanced scanning)** 

When enhanced scanning is turned on for your registry, the following event is sent by Amazon Inspector when the image scan finding is created, updated, or closed. For more information, see [Scan images for OS and programming language package vulnerabilities in Amazon ECR](#image-scanning-enhanced).

Event pattern:

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["Inspector2 Finding"]
}
```

Example output:

```
{
    "version": "0",
    "id": "42dbea55-45ad-b2b4-87a8-afaEXAMPLE",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "{{123456789012}}",
    "time": "2021-12-03T18:02:30Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:ecr:us-east-2:{{123456789012}}:repository/amazon/amazon-ecs-sample/sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77eEXAMPLE"
    ],
    "detail": {
        "awsAccountId": "{{123456789012}}",
        "description": "In libssh2 v1.9.0 and earlier versions, the SSH_MSG_DISCONNECT logic in packet.c has an integer overflow in a bounds check, enabling an attacker to specify an arbitrary (out-of-bounds) offset for a subsequent memory read. A crafted SSH server may be able to disclose sensitive information or cause a denial of service condition on the client system when a user connects to the server.",
        "findingArn": "arn:aws:inspector2:us-east-2:{{123456789012}}:finding/be674aaddd0f75ac632055EXAMPLE",
        "firstObservedAt": "Dec 3, 2021, 6:02:30 PM",
        "inspectorScore": 6.5,
        "inspectorScoreDetails": {
            "adjustedCvss": {
                "adjustments": [],
                "cvssSource": "REDHAT_CVE",
                "score": 6.5,
                "scoreSource": "REDHAT_CVE",
                "scoringVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N",
                "version": "3.0"
            }
        },
        "lastObservedAt": "Dec 3, 2021, 6:02:30 PM",
        "packageVulnerabilityDetails": {
            "cvss": [
                {
                    "baseScore": 6.5,
                    "scoringVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N",
                    "source": "REDHAT_CVE",
                    "version": "3.0"
                },
                {
                    "baseScore": 5.8,
                    "scoringVector": "AV:N/AC:M/Au:N/C:P/I:N/A:P",
                    "source": "NVD",
                    "version": "2.0"
                },
                {
                    "baseScore": 8.1,
                    "scoringVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:H",
                    "source": "NVD",
                    "version": "3.1"
                }
            ],
            "referenceUrls": [
                "https://access.redhat.com/errata/RHSA-2020:3915"
            ],
            "source": "REDHAT_CVE",
            "sourceUrl": "https://access.redhat.com/security/cve/CVE-2019-17498",
            "vendorCreatedAt": "Oct 16, 2019, 12:00:00 AM",
            "vendorSeverity": "Moderate",
            "vulnerabilityId": "CVE-2019-17498",
            "vulnerablePackages": [
                {
                    "arch": "X86_64",
                    "epoch": 0,
                    "name": "libssh2",
                    "packageManager": "OS",
                    "release": "12.amzn2.2",
                    "sourceLayerHash": "sha256:72d97abdfae3b3c933ff41e39779cc72853d7bd9dc1e4800c5294dEXAMPLE",
                    "version": "1.4.3"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "Update all packages in the vulnerable packages section to their latest versions."
            }
        },
        "resources": [
            {
                "details": {
                    "awsEcrContainerImage": {
                        "architecture": "amd64",
                        "imageHash": "sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77e5EXAMPLE",
                        "imageTags": [
                            "latest"
                        ],
                        "platform": "AMAZON_LINUX_2",
                        "pushedAt": "Dec 3, 2021, 6:02:13 PM",
                        "lastInUseAt": "Dec 3, 2021, 6:02:13 PM",
                        "inUseCount": 1,
                        "registry": "123456789012",
                        "repositoryName": "amazon/amazon-ecs-sample"
                    }
                },
                "id": "arn:aws:ecr:us-east-2:{{123456789012}}:repository/amazon/amazon-ecs-sample/sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77EXAMPLE",
                "partition": "N/A",
                "region": "N/A",
                "type": "AWS_ECR_CONTAINER_IMAGE"
            }
        ],
        "severity": "MEDIUM",
        "status": "ACTIVE",
        "title": "CVE-2019-17498 - libssh2",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Dec 3, 2021, 6:02:30 PM"
    }
}
```

### Retrieving the findings for enhanced scans in Amazon ECR
<a name="image-scanning-enhanced-describe-scan-findings"></a>

You can retrieve the scan findings for the last completed enhanced image scan, and then open the findings in Amazon Inspector to see more detail. The software vulnerabilities that were discovered are listed by severity based on the Common Vulnerabilities and Exposures (CVEs) database.

For troubleshooting details for some common issues when scanning images, see [Troubleshooting image scanning in Amazon ECR](#image-scanning-troubleshooting).

------
#### [ AWS Management Console ]

Use the following steps to retrieve image scan findings using the AWS Management Console.

**To retrieve image scan findings**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region where your repository exists.

1. In the navigation pane, choose **Repositories** .

1. On the **Repositories** page, choose the repository that contains the image to retrieve the scan findings for.

1. On the **Images** page, under the **Image tag** column, select the image tag to retrieve the scan findings.

1. To view more details in the Amazon Inspector console, choose the vulnerability name in the **Name** column.

------
#### [ AWS CLI ]

Use the following AWS CLI command to retrieve image scan findings using the AWS CLI. You can specify an image using the `imageTag` or ` imageDigest`, both of which can be obtained using the [list-images](https://docs.aws.amazon.com/cli/latest/reference/ecr/list-images.html) CLI command.
+ [ describe-image-scan-findings](https://docs.aws.amazon.com/cli/latest/reference/ecr/describe-image-scan-findings.html) (AWS CLI)

  The following example uses an image tag.

  ```
  aws ecr describe-image-scan-findings \
       --repository-name {{name}} \
       --image-id imageTag={{tag_name}} \
       --region {{us-east-2}}
  ```

  The following example uses an image digest.

  ```
  aws ecr describe-image-scan-findings \
       --repository-name {{name}} \
       --image-id imageDigest={{sha256_hash}} \
       --region {{us-east-2}}
  ```

------

## Scan images for OS vulnerabilities in Amazon ECR
<a name="image-scanning-basic"></a>

Amazon ECR basic scanning uses AWS native technology to scan your container images for software vulnerabilities. Basic scanning provides vulnerability detection across a broad set of popular operating systems, sourcing more than 50 data feeds to generate findings for common vulnerabilities and exposures (CVEs). These sources include vendor security advisories, data feeds, threat intelligence feeds, as well as the National Vulnerability Database (NVD) and MITRE.

Amazon ECR basic scanning is supported in all regions listed in [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). 

Amazon ECR uses the severity for a CVE from the upstream distribution source if available. Otherwise, the Common Vulnerability Scoring System (CVSS) score is used. The CVSS score can be used to obtain the NVD vulnerability severity rating. For more information, see [NVD Vulnerability Severity Ratings](https://nvd.nist.gov/vuln-metrics/cvss).

Amazon ECR basic scanning supports filters to specify which repositories to scan on push. Any repositories that don't match a scan on push filter are set to the ** manual** scan frequency which means you must manually start the scan. An image can be scanned once per 24 hours. The 24 hours includes the initial scan on push, if configured, and any manual scans. With basic scanning, you can scan up to 100,000 images per 24 hours in a given registry.

The last completed image scan findings can be retrieved for each image. When an image scan is completed, Amazon ECR sends an event to Amazon EventBridge. For more information, see [Amazon ECR events and EventBridge](#ecr-eventbridge).

### Operating system support for basic scanning
<a name="image-scan-basic-support-operating-systems"></a>

As a security best practice and for continued coverage, we recommend that you continue to use supported versions of an operating system. In accordance with vendor policy, discontinued operating systems are no longer updated with patches and, in many cases, new security advisories are no longer released for them. In addition, some vendors remove existing security advisories and detections from their feeds when an affected operating system reaches the end of standard support. After a distribution loses support from its vendor, Amazon ECR may no longer support scanning it for vulnerabilities. Any findings that Amazon ECR does generate for a discontinued operating system should be used for informational purposes only. For a full list of supported operating systems and versions, see [Supported operating systems - Amazon Inspector scan](https://docs.aws.amazon.com/inspector/latest/user/supported.html#supported-os-scan-inspector-scan) in the *Amazon Inspector User Guide*.

### Configuring basic scanning for images in Amazon ECR
<a name="image-scanning-basic-enabling"></a>

By default, Amazon ECR turns on basic scanning for all private registries. As a result, unless you've changed the scanning settings on your private registry there is no need to turn on basic scanning. 

You can use the following steps to define one or more scan on push filters.

**To turn on basic scanning for your private registry**

1.  Open the Amazon ECR console at [ https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories)

1. From the navigation bar, choose the Region to set the scanning configuration for.

1. In the navigation pane, choose **Private registry**, ** Scanning**.

1. On the **Scanning configuration** page, For **Scan type** choose **Basic scanning**.

1. By default all of your repositories are set for **Manual** scanning. You can optionally configure scan on push by specifying **Scan on push filters**. You can set scan on push for all repositories or individual repositories. For more information, see [Filters to choose which repositories are scanned in Amazon ECR](#image-scanning-filters).
**Note**  
If scan on push is enabled for a repository, scans are also done on images that are restored after being archived. No old scans will be available from the restored image.

### Manually scanning an image for OS vulnerabilities in Amazon ECR
<a name="manual-scan"></a>

If your repositories aren't configured to **scan on push**, you can manually start image scans. An image can be scanned once per 24 hours. The 24 hours includes the initial scan on push, if configured, and any manual scans.

For troubleshooting details for some common issues when scanning images, see [Troubleshooting image scanning in Amazon ECR](#image-scanning-troubleshooting).

------
#### [ AWS Management Console ]

Use the following steps to start a manual image scan using the AWS Management Console.

1.  Open the Amazon ECR console at [ https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories)

1. From the navigation bar, choose the Region to create your repository in.

1. In the navigation pane, choose **Repositories** .

1. On the **Repositories** page, choose the repository that contains the image to scan.

1. On the **Images** page, select the image to scan and then choose **Scan**.

------
#### [ AWS CLI ]
+ [ start-image-scan](https://docs.aws.amazon.com/cli/latest/reference/ecr/start-image-scan.html) (AWS CLI)

  The following example uses an image tag.

  ```
  aws ecr start-image-scan --repository-name {{name}} --image-id imageTag={{tag_name}} --region {{us-east-2}}
  ```

  The following example uses an image digest.

  ```
  aws ecr start-image-scan --repository-name {{name}} --image-id imageDigest={{sha256_hash}} --region {{us-east-2}}
  ```

------
#### [ AWS Tools for Windows PowerShell ]
+ [ Get-ECRImageScanFinding](https://docs.aws.amazon.com/powershell/latest/reference/items/Start-ECRImageScan.html) (AWS Tools for Windows PowerShell)

  The following example uses an image tag.

  ```
  Start-ECRImageScan -RepositoryName {{name}} -ImageId_ImageTag {{tag_name}} -Region {{us-east-2}} -Force
  ```

  The following example uses an image digest.

  ```
  Start-ECRImageScan -RepositoryName {{name}} -ImageId_ImageDigest {{sha256_hash}} -Region {{us-east-2}} -Force
  ```

------

### Retrieving the findings for basic scans in Amazon ECR
<a name="describe-scan-findings"></a>

You can retrieve the scan findings for the last completed basic image scan. The software vulnerabilities that were discovered are listed by severity based on the Common Vulnerabilities and Exposures (CVEs) database.

For troubleshooting details for some common issues when scanning images, see [Troubleshooting image scanning in Amazon ECR](#image-scanning-troubleshooting).

------
#### [ AWS Management Console ]

Use the following steps to retrieve image scan findings using the AWS Management Console.

**To retrieve image scan findings**

1.  Open the Amazon ECR console at [ https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories)

1. From the navigation bar, choose the Region to create your repository in.

1. In the navigation pane, choose **Repositories** .

1. On the **Repositories** page, choose the repository that contains the image to retrieve the scan findings for.

1. On the **Images** page, under the **Image tag** column, select the image tag to retrieve the scan findings.

------
#### [ AWS CLI ]

Use the following AWS CLI command to retrieve image scan findings using the AWS CLI. You can specify an image using the `imageTag` or ` imageDigest`, both of which can be obtained using the [list-images](https://docs.aws.amazon.com/cli/latest/reference/ecr/list-images.html) CLI command.
+ [ describe-image-scan-findings](https://docs.aws.amazon.com/cli/latest/reference/ecr/describe-image-scan-findings.html) (AWS CLI)

  The following example uses an image tag.

  ```
  aws ecr describe-image-scan-findings --repository-name {{name}} --image-id imageTag={{tag_name}} --region {{us-east-2}}
  ```

  The following example uses an image digest.

  ```
  aws ecr describe-image-scan-findings --repository-name {{name}} --image-id imageDigest={{sha256_hash}} --region {{us-east-2}}
  ```

------
#### [ AWS Tools for Windows PowerShell ]
+ [ Get-ECRImageScanFinding](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ECRImageScanFinding.html) (AWS Tools for Windows PowerShell)

  The following example uses an image tag.

  ```
  Get-ECRImageScanFinding -RepositoryName {{name}} -ImageId_ImageTag {{tag_name}} -Region {{us-east-2}}
  ```

  The following example uses an image digest.

  ```
  Get-ECRImageScanFinding -RepositoryName {{name}} -ImageId_ImageDigest {{sha256_hash}} -Region {{us-east-2}}
  ```

------

## Troubleshooting image scanning in Amazon ECR
<a name="image-scanning-troubleshooting"></a>

The following are common image scan failures. You can view errors like this in the Amazon ECR console by displaying the image details or through the API or AWS CLI by using the ` DescribeImageScanFindings` API.

UnsupportedImageError  
You may get an `UnsupportedImageError` error when attempting to perform a basic scan on an image that was built using an operating system that Amazon ECR doesn't support basic image scanning for. Amazon ECR supports package vulnerability scanning for major versions of Amazon Linux, Amazon Linux 2, Debian, Ubuntu, CentOS, Oracle Linux, Alpine, and RHEL Linux distributions. Once a distribution loses support from its vendor, Amazon ECR may no longer support scanning it for vulnerabilities. Amazon ECR does not support scanning images built from the [Docker scratch](https://hub.docker.com/_/scratch) image.  
When using enhanced scanning, Amazon Inspector supports scanning for specific operating systems and media types. For a full list, see [Supported operating systems and media types](https://docs.aws.amazon.com/inspector/latest/user/enable-disable-scanning-ecr.html#ecr-supported-media) in the *Amazon Inspector User Guide*.

An `UNDEFINED` severity level is returned  
You may receive a scan finding that has a severity level of ` UNDEFINED`. The following are the common causes for this:  
+ The vulnerability was not assigned a priority by the CVE source.
+ The vulnerability was assigned a priority that Amazon ECR did not recognize.
To determine the severity and description of a vulnerability, you can view the CVE directly from the source.

### Understanding scan status `SCAN_ELIGIBILITY_EXPIRED`
<a name="image-scanning-troubleshooting-eligibility"></a>

When enhanced scanning using Amazon Inspector is enabled for your private registry and you are viewing your scan vulnerabilities, you may see a scan status of ` SCAN_ELIGIBILITY_EXPIRED`. The following are the most common causes of this.
+ When you initially turn on enhanced scanning for your private registry, Amazon Inspector only recognizes images pushed to Amazon ECR in the last 30 days, based on the image push timestamp. Older images will have the ` SCAN_ELIGIBILITY_EXPIRED` scan status. If you'd like these images to be scanned by Amazon Inspector you should push them again to your repository.
+ If the **ECR re-scan duration** is changed in the Amazon Inspector console and that time elapses, the scan status of the image is changed to ` inactive` with a reason code of `expired`, and all associated findings for the image are scheduled to be closed. This results in the Amazon ECR console listing the scan status as ` SCAN_ELIGIBILITY_EXPIRED`.

# Sync an upstream registry with an Amazon ECR private registry
<a name="pull-through-cache"></a>

Using pull through cache rules, you can sync the contents of an upstream registry with your Amazon ECR private registry.

Amazon ECR currently supports creating pull through cache rules for the following upstream registries:
+ Amazon ECR Public, Kubernetes container image registry, and Quay (doesn't require authentication)
+ Docker Hub, Microsoft Azure Container Registry, GitHub Container Registry, GitLab Container Registry and Chainguard Registry (requires authentication with AWS Secrets Manager secret)
+ Amazon ECR (requires authentication with AWS IAM role)

For GitLab Container Registry, Amazon ECR supports pull through cache only with GitLab's Software as a Service (SaaS) offering. For more information about using GitLab's SaaS offering, see [GitLab.com](https://docs.gitlab.com/17.5/subscriptions/choosing_subscription/).

For upstream registries that require authentication with secrets (such as Docker Hub), you must store your credentials in an AWS Secrets Manager secret. You can use the Amazon ECR console to create Secrets Manager secrets for each authenticated upstream registry. For more information about creating a Secrets Manager secret using the Secrets Manager console, see [Storing your upstream repository credentials in an AWS Secrets Manager secret](#pull-through-cache-creating-secret).

For Amazon ECR, you must create an IAM role if the upstream and downstream Amazon ECR registries belong to different AWS account. For more information about creating an IAM role, see [IAM policies required for cross-account ECR to ECR pull through cache](#pull-through-cache-private-permissions).

After you've created a pull through cache rule for the upstream registry, pull an image from that upstream registry using your Amazon ECR private registry URI. Amazon ECR then creates a repository and caches that image in your private registry. For subsequent pull requests of the cached image with a given tag, Amazon ECR checks the upstream registry for a new version of the image with that specific tag and attempts to update the image in your private registry at least once every 24 hours.

## Repository creation templates
<a name="pull-through-cache-respository-creation-template"></a>

Amazon ECR has added support for repository creation templates, which gives you the control to specify initial configurations for new repositories created by Amazon ECR on your behalf using pull through cache rules. Each template contains a repository namespace prefix which is used to match new repositories to a specific template. Templates can specify the configuration for all repository settings including resource-based access policies, tag immutability, encryption, and lifecycle policies. The settings in a repository creation template are only applied during repository creation and don't have any effect on existing repositories or repositories created using any other method. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).

## Considerations for using pull through cache rules
<a name="pull-through-cache-considerations"></a>

Consider the following when using Amazon ECR pull through cache rules.
+ AWS Lambda doesn't support pulling container images from Amazon ECR using a pull through cache rule.
+ When pulling images using pull through cache, the Amazon ECR FIPS service endpoints aren't supported the first time an image is pulled. Using the Amazon ECR FIPS service endpoints work on subsequent pulls though.
+ For upstream repositories that require authentication, when an image is pulled through the Amazon ECR private registry URI for the first time or to update the cache, the image pulls are initiated by the user associated to the credentials configured in the pull through cache rule. Subsequent pulls will return the image directly from the cache in the customer's private registry.
+ For upstream repositories that do not require authentication, when an image is pulled through the Amazon ECR private registry URI, the image pulls are initiated by AWS IP addresses.
+ When a customer pulls a cached image through the Amazon ECR private registry URI, Amazon ECR checks whether it has validated the image against the upstream registry within the last 24 hours. If the 24-hour window has expired, Amazon ECR sends a request upstream to check for a newer version and updates the cache if one exists. If the window has not expired, Amazon ECR serves the cached image without contacting the upstream. 
+ Calling the `ListImageReferrers` API to a pull through cache created repository returns the OCI-compliant referrer artifacts to the private cache.
+ Amazon ECR checks whether the referrer artifacts have been updated within the last 6 hours. If the 6-hour window has expired, Amazon ECR sends a request upstream to check for newer versions and updates the cache if they exist.
+ If Amazon ECR is unable to update the image from the upstream registry for any reason and the image is pulled, the last cached image will still be pulled.
+ When creating the Secrets Manager secret that contains the upstream registry credentials, the secret name must use the `ecr-pullthroughcache/` prefix. The secret must also be in the same account and Region that the pull through cache rule is created in.
+ When a multi-architecture image is pulled using a pull through cache rule, the manifest list and each image referenced in the manifest list are pulled to the Amazon ECR repository. If you only want to pull a specific architecture, you can pull the image using the image digest or tag associated with the architecture rather than the tag associated with the manifest list.
+ Amazon ECR uses a service-linked IAM role, which provides the permissions needed for Amazon ECR to create the repository, retrieve the Secrets Manager secret value for authentication, and push the cached image on your behalf. The service-linked IAM role is created automatically when a pull through cache rule is created. For more information, see [Amazon ECR service-linked role for pull through cache](#slr-pullthroughcache).
+ By default, the IAM principal pulling the cached image has the permissions granted to them through their IAM policy. You may use the Amazon ECR private registry permissions policy to further scope the permissions of an IAM entity. For more information, see [Using registry permissions](#pull-through-cache-registry-permissions).
+ Amazon ECR repositories created using the pull through cache workflow are treated like any other Amazon ECR repository. All repository features, such as replication and image scanning are supported.
+ When Amazon ECR creates a new repository on your behalf using a pull through cache action, the following default settings are applied to the repository unless there is a matching repository creation template. You can use a repository creation template to define the settings applied to repositories created by Amazon ECR on your behalf. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).
  + Tag immutability – Tag immutability specifies whether image tags can be overwritten. By default, image tags are mutable (can be overwritten). You can modify tag behavior by configuring tag exclusion filters in either the **Mutable tag exclusion** text box when **Mutable** is selected, or the **Immutable tag exclusion** text box when **Immutable** is selected.
  + Encryption – The default `AES256` encryption is used.
  + Repository permissions – Omitted, no repository permissions policy is applied.
  + Lifecycle policy – Omitted, no lifecycle policy is applied.
  + Resource tags – Omitted, no resource tags are applied.
+ Turning on image tag immutability for repositories using a pull through cache rule will prevent Amazon ECR from updating images using the same tag.
+ When an image is pulled using the pull through cache rule for the first time a route to the internet may be required. There are certain circumstances in which a route to the internet is required so it's best to set up a route to avoid any failures. Thus, if you've configured Amazon ECR to use an interface VPC endpoint using AWS PrivateLink then you need to ensure the first pull has a route to the internet. One way to do this is to create a public subnet in the same VPC, with an internet gateway, and then route all outbound traffic to the internet from their private subnet to the public subnet. Subsequent image pulls using the pull through cache rule don't require this. For more information, see [Example routing options](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html) in the *Amazon Virtual Private Cloud User Guide*.
+ Pushing images directly to a pull through cache repository is not a supported pattern. This practice can cause a temporary inconsistency where subsequent image pulls continue to return the previously cached version instead of the newly pushed image. To resolve this inconsistency, delete the image and then pull it again to refresh the cached copy. Alternatively, wait up to 24 hours for the cache to refresh, and then pull the image again.

## IAM permissions required to sync an upstream registry with an Amazon ECR private registry
<a name="pull-through-cache-iam"></a>

In addition to the Amazon ECR API permissions needed to authenticate to a private registry and to push and pull images, the following additional permissions are needed to use pull through cache rules effectively.
+ `ecr:CreatePullThroughCacheRule` – Grants permission to create a pull through cache rule. This permission must be granted via an identity-based IAM policy.
+ `ecr:BatchImportUpstreamImage` – Grants permission to retrieve the external image and import it to your private registry. This permission can be granted by using the private registry permissions policy, an identity-based IAM policy, or by using the resource-based repository permissions policy. For more information about using repository permissions, see [Private repository policies in Amazon ECR](#repository-policies).
+ `ecr:CreateRepository` – Grants permission to create a repository in a private registry. This permission is required if the repository storing the cached images doesn't already exist. This permission can be granted by either an identity-based IAM policy or the private registry permissions policy.

### Using registry permissions
<a name="pull-through-cache-registry-permissions"></a>

Amazon ECR private registry permissions may be used to scope the permissions of individual IAM entities to use pull through cache. If an IAM entity has more permissions granted by an IAM policy than the registry permissions policy is granting, the IAM policy takes precedence. For example, if user has `ecr:*` permissions granted, no additional permissions are needed at the registry level.

#### To create a private registry permissions policy (AWS Management Console)
<a name="pull-through-cache-registry-permissions-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry permissions statement in.

1. In the navigation pane, choose **Private registry**, **Registry permissions**.

1. On the **Registry permissions** page, choose **Generate statement**.

1. For each pull through cache permissions policy statement you want to create, do the following.

   1. For **Policy type**, choose **Pull through cache policy**.

   1. For **Statement id**, provide a name for the pull through cache statement policy.

   1. For **IAM entities**, specify the users, groups, or roles to include in the policy.

   1. For **Repository namespace**, select the pull through cache rule to associate the policy with.

   1. For **Repository names**, specify the repository base name to apply the rule for. For example, if you want to specify the Amazon Linux repository on Amazon ECR Public, the repository name would be `amazonlinux`.

#### To create a private registry permissions policy (AWS CLI)
<a name="pull-through-cache-registry-permissions-cli"></a>

Use the following AWS CLI command to specify the private registry permissions using the AWS CLI.

1. Create a local file named `ptc-registry-policy.json` with the contents of your registry policy. The following example grants the `ecr-pull-through-cache-user` permission to create a repository and pull an image from Amazon ECR Public, which is the upstream source associated with the previously created pull through cache rule.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "PullThroughCacheFromReadOnlyRole",
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::{{111122223333}}:user/{{ecr-pull-through-cache-user}}"
         },
         "Action": [
           "ecr:CreateRepository",
           "ecr:BatchImportUpstreamImage"
         ],
         "Resource": "arn:aws:ecr:{{us-east-1}}:{{111122223333}}:repository/{{ecr-public}}/*"
       }
     ]
   }
   ```

------
**Important**  
The `ecr-CreateRepository` permission is only required if the repository storing the cached images doesn't already exist. For example, if the repository creation action and the image pull actions are being done by separate IAM principals such as an administrator and a developer.

1. Use the [put-registry-policy](https://docs.aws.amazon.com/cli/latest/reference/ecr/put-registry-policy.html) command to set the registry policy.

   ```
   aws ecr put-registry-policy \
        --policy-text file://{{ptc-registry.policy.json}}
   ```

### Next steps
<a name="pull-through-cache-next-steps"></a>

Once you are ready to start using pull through cache rules, the following are the next steps.
+ Create a pull through cache rule. For more information, see [Creating a pull through cache rule in Amazon ECR](#pull-through-cache-creating-rule).
+ Create a repository creation template. A repository creation template gives you control to define the settings to use for new repositories created by Amazon ECR on your behalf during a pull through cache action. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).

## Setting up permissions for cross-account ECR to ECR PTC
<a name="pull-through-cache-private"></a>

The Amazon ECR to Amazon ECR (ECR to ECR) pull through cache feature enables automatic synchronization of images between Regions, AWS accounts, or both. With ECR to ECR PTC, you can push images to your primary Amazon ECR registry and configure a pull through cache rule to cache images in downstream Amazon ECR registries.

### IAM policies required for cross-account ECR to ECR pull through cache
<a name="pull-through-cache-private-permissions"></a>

To cache images between Amazon ECR registries across different AWS accounts, create an IAM role in the downstream account and configure the policies in this section to provide the following permissions:
+ Amazon ECR needs permissions to pull images from the upstream Amazon ECR registry on your behalf. You can grant these permissions by creating an IAM role and then specifying it in your pull through cache rule. 
+ The upstream registry owner must also grant the cache registry owner with the required permissions to pull the images in to the resource policies.

**Topics**
+ [Creating an IAM role to define the pull through cache permissions](#ecr-policies-for-cross-account-ecr-to-ecr-pull-through-cache)
+ [Creating a Trust policy for the IAM role](#ecr-creating-a-trust-policy-for-the-iam-role)
+ [Creating a resource policy in the upstream Amazon ECR registry](#ecr-creating-registry-permissions-policy-in-upstream-registry)

#### Creating an IAM role to define the pull through cache permissions
<a name="ecr-policies-for-cross-account-ecr-to-ecr-pull-through-cache"></a>

The following example shows a permissions policy that grants an IAM role permission to pull images from the upstream Amazon ECR registry on your behalf. When Amazon ECR assumes the role, it receives the permissions specified in this policy.

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
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetAuthorizationToken",
                "ecr:BatchImportUpstreamImage",
                "ecr:BatchGetImage",
                "ecr:GetImageCopyStatus",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:PutImage"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Creating a Trust policy for the IAM role
<a name="ecr-creating-a-trust-policy-for-the-iam-role"></a>

The following example shows a trust policy that identifies Amazon ECR pull through cache as the AWS service principal that can assume the role.

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
                "Service": "pullthroughcache.ecr.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

#### Creating a resource policy in the upstream Amazon ECR registry
<a name="ecr-creating-registry-permissions-policy-in-upstream-registry"></a>

The upstream Amazon ECR registry owner must also add a registry policy or a repository policy to grant the downstream registry owner the required permissions to perform the following actions. 

**Note**  
The following resource policy is required only for **cross-account** ECR to ECR pull through cache configurations. For **same-account, cross-region** pull through cache, you only need the IAM role policy and trust policy shown in the previous sections. The root account principal permission is not required when the upstream and downstream registries are in the same AWS account.

```
{
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{444455556666}}:root"
    },
    "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchImportUpstreamImage",
        "ecr:GetImageCopyStatus"
    ],
    "Resource": "arn:aws:ecr:{{region:111122223333}}:repository/*"
}
```

## Creating a pull through cache rule in Amazon ECR
<a name="pull-through-cache-creating-rule"></a>

For each upstream registry containing images that you want to cache in your Amazon ECR private registry, you must create a pull through cache rule.

For upstream registries that require authentication with secrets, you must store the credentials in a Secrets Manager secret. You can use an existing secret or create a new secret. You can create the Secrets Manager secret in either the Amazon ECR console or the Secrets Manager console. To create a Secrets Manager secret using the Secrets Manager console instead of the Amazon ECR console, see [Storing your upstream repository credentials in an AWS Secrets Manager secret](#pull-through-cache-creating-secret).

### Prerequisites
<a name="cache-rule-prereq"></a>
+ Verify that you have the proper IAM permissions to create pull through cache rules. For information, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](#pull-through-cache-iam).
+ For upstream registries that require authentication with secrets: If you want to use an existing secret, verify that the Secrets Manager secret meets the following requirements:
  + The name of the secret begins with `ecr-pullthroughcache/`. The AWS Management Console only displays Secrets Manager secrets with the `ecr-pullthroughcache/` prefix.
  + The account and Region that the secret is in must match the account and Region that the pull through cache rule is in.

### To create a pull through cache rule (AWS Management Console)
<a name="pull-through-cache-creating-rule-console"></a>

The following steps show how to create a pull through cache rule and a Secrets Manager secret using the Amazon ECR console. To create a secret using the Secrets Manager console, see [Storing your upstream repository credentials in an AWS Secrets Manager secret](#pull-through-cache-creating-secret).

#### For Amazon ECR Public, Kubernetes container registry, or Quay
<a name="w2aac30c27b9b7b1"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry settings in.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify a source** page, for **Registry**, choose either Amazon ECR Public, Kubernetes, or Quay from the list of upstream registries and then choose **Next**.

1. On the **Step 2: Specify a destination** page, for **Amazon ECR repository prefix**, specify the repository namespace prefix to use when caching images pulled from the source public registry and then choose **Next**. By default, a namespace is populated but a custom namespace can be specified as well.

1. On the **Step 3: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat the previous step for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

#### For Docker Hub
<a name="w2aac30c27b9b7b3"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry settings in.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify a source** page, for **Registry**, choose **Docker Hub**, **Next**. 

1. On the **Step 2: Configure authentication** page, for **Upstream credentials**, you must store your authentication credentials for Docker Hub in an AWS Secrets Manager secret. You can specify an existing secret or use the Amazon ECR console to create a new secret.

   1. To use an existing secret, choose **Use an existing AWS secret**. For **Secret name** use the drop down to select your existing secret, and then choose **Next**.
**Note**  
The AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix. The secret must also be in the same account and Region that the pull through cache rule is created in.

   1. To create a new secret, choose **Create an AWS secret**, do the following, then choose **Next**.

      1. For **Secret name**, specify a descriptive name for the secret. Secret names must contain 1-512 Unicode characters.

      1. For **Docker Hub email**, specify your Docker Hub email.

      1. For **Docker Hub access token**, specify your Docker Hub access token. For more information on creating a Docker Hub access token, see [Create and manage access tokens](https://docs.docker.com/security/for-developers/access-tokens/) in the Docker documentation.

1. On the **Step 3: Specify a destination** page, for **Amazon ECR repository prefix**, specify the repository namespace to use when caching images pulled from the source public registry and then choose **Next**.

   By default, a namespace is populated but a custom namespace can be specified as well.

1. On the **Step 4: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat the previous step for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

#### For GitHub Container Registry
<a name="w2aac30c27b9b7b5"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry settings in.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify a source** page, for **Registry**, choose **GitHub Container Registry**, **Next**. 

1. On the **Step 2: Configure authentication** page, for **Upstream credentials**, you must store your authentication credentials for GitHub Container Registry in an AWS Secrets Manager secret. You can specify an existing secret or use the Amazon ECR console to create a new secret.

   1. To use an existing secret, choose **Use an existing AWS secret**. For **Secret name** use the drop down to select your existing secret, and then choose **Next**.
**Note**  
The AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix. The secret must also be in the same account and Region that the pull through cache rule is created in.

   1. To create a new secret, choose **Create an AWS secret**, do the following, then choose **Next**.

      1. For **Secret name**, specify a descriptive name for the secret. Secret names must contain 1-512 Unicode characters.

      1. For **GitHub Container Registry username**, specify your GitHub Container Registry username.

      1. For **GitHub Container Registry access token**, specify your GitHub Container Registry access token. For more information on creating a GitHub access token, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) in the GitHub documentation.

1. On the **Step 3: Specify a destination** page, for **Amazon ECR repository prefix**, specify the repository namespace to use when caching images pulled from the source public registry and then choose **Next**.

   By default, a namespace is populated but a custom namespace can be specified as well.

1. On the **Step 4: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat the previous step for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

#### For Microsoft Azure Container Registry
<a name="w2aac30c27b9b7b7"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry settings in.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify a source** page, do the following.

   1. For **Registry**, choose **Microsoft Azure Container Registry**

   1. For **Source registry URL**, specify the name of your Microsoft Azure container registry and then choose **Next**.
**Important**  
You only need to specify the prefix, as the `.azurecr.io` suffix is populated on your behalf.

1. On the **Step 2: Configure authentication** page, for **Upstream credentials**, you must store your authentication credentials for Microsoft Azure Container Registry in an AWS Secrets Manager secret. You can specify an existing secret or use the Amazon ECR console to create a new secret.

   1. To use an existing secret, choose **Use an existing AWS secret**. For **Secret name** use the drop down to select your existing secret, and then choose **Next**.
**Note**  
The AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix. The secret must also be in the same account and Region that the pull through cache rule is created in.

   1. To create a new secret, choose **Create an AWS secret**, do the following, then choose **Next**.

      1. For **Secret name**, specify a descriptive name for the secret. Secret names must contain 1-512 Unicode characters.

      1. For **Microsoft Azure Container Registry username**, specify your Microsoft Azure Container Registry username.

      1. For **Microsoft Azure Container Registry access token**, specify your Microsoft Azure Container Registry access token. For more information on creating an Microsoft Azure Container Registry access token, see [Create token - portal](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-repository-scoped-permissions#create-token---portal) in the Microsoft Azure documentation.

1. On the **Step 3: Specify a destination** page, for **Amazon ECR repository prefix**, specify the repository namespace to use when caching images pulled from the source public registry and then choose **Next**.

   By default, a namespace is populated but a custom namespace can be specified as well.

1. On the **Step 4: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat the previous step for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

#### For GitLab Container Registry
<a name="w2aac30c27b9b7b9"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry settings in.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify a source** page, for Registry, choose GitLab Container Registry, Next.

1. On the **Step 2: Configure authentication** page, for **Upstream credentials**, you must store your authentication credentials for GitLab Container Registry in an AWS Secrets Manager secret. You can specify an existing secret or use the Amazon ECR console to create a new secret.

   1. To use an existing secret, choose **Use an existing AWS secret**. For **Secret name** use the drop down to select your existing secret, and then choose **Next**. For more information on creating a Secrets Manager secret using the Secrets Manager console, see [Storing your upstream repository credentials in an AWS Secrets Manager secret](#pull-through-cache-creating-secret).
**Note**  
The AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix. The secret must also be in the same account and Region that the pull through cache rule is created in.

   1. To create a new secret, choose **Create an AWS secret**, do the following, then choose **Next**.

      1. For **Secret name**, specify a descriptive name for the secret. Secret names must contain 1-512 Unicode characters.

      1. For **GitLab Container Registry username**, specify your GitLab Container Registry username.

      1. For **GitLab Container Registry access token**, specify your GitLab Container Registry access token. For more information on creating a GitLab Container Registry access token, see [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html), [Group access tokens](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html), or [Project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html), in the GitLab documentation.

1. On the **Step 3: Specify a destination** page, for **Amazon ECR repository prefix**, specify the repository namespace to use when caching images pulled from the source public registry and then choose **Next**.

   By default, a namespace is populated but a custom namespace can be specified as well.

1. On the **Step 4: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat the previous step for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

#### For Amazon ECR private registry within your AWS account
<a name="ecr-to-pull-images-from-other-regions-within-your-account"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region in which you want to configure your private registry settings.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify upstream** page, for **Registry**, choose **Amazon ECR Private** and **This account**. For **Region**, select the Region for the upstream Amazon ECR registry, and then choose **Next**.

1. On the **Step 2: Specify namespaces** page, for **Cache namespace**, choose whether to create pull through cache repositories with **A specific prefix** or **no prefix**. If you select **A specific prefix**, you must specify a prefix name to be used as part of the namespace for caching images from the upstream registry.

1. For **Upstream namespace**, choose whether to pull from **A specific prefix** that exists in the upstream registry. If you select **no prefix**, you can pull from any repository in the upstream registry. Specify the upstream repository prefix if prompted, and then choose **Next**.
**Note**  
To learn more about customizing cache and upstream namespaces, see [Customizing repository prefixes for ECR to ECR pull through cache](#pull-through-cache-private-wildcards).

1. On the **Step 3: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat these steps for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

#### For Amazon ECR private registry from another AWS account
<a name="w2aac30c27b9b7c13"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry settings in.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify upstream** page, for **Registry**, choose **Amazon ECR Private** and **Cross account**. For **Region**, select the Region for the upstream Amazon ECR registry. For **Account**, specify the AWS account ID for the upstream Amazon ECR registry, and then choose **Next**.

1. On the **Step 2: Specify permissions** page, for **IAM role**, select a role to be used for cross account pull through cache access and then choose **Create**.
**Note**  
Make sure that you select the IAM role which uses the permissions created in [IAM policies required for cross-account ECR to ECR pull through cache](#pull-through-cache-private-permissions).

1. On the **Step 3: Specify namespaces** page, for **Cache namespace**, choose whether to create pull through cache repositories with **A specific prefix** or **no prefix**. If you select **A specific prefix**, you must specify a prefix name to be used as part of the namespace for caching images from the upstream registry.

1. For **Upstream namespace**, choose whether to pull from **A specific prefix** that exists in the upstream registry. If you select **no prefix**, you can pull from any repository in the upstream registry. Specify the upstream repository prefix if prompted, and then choose **Next**.
**Note**  
To learn more about customizing cache and upstream namespaces, see [Customizing repository prefixes for ECR to ECR pull through cache](#pull-through-cache-private-wildcards).

1. On the **Step 4: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat these steps for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

#### For Chainguard Registry
<a name="w2aac30c27b9b7c15"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry settings in.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, choose **Add rule**.

1. On the **Step 1: Specify a source** page, for Registry, choose Chainguard Registry, Next.

1. On the **Step 2: Configure authentication** page, for **Upstream credentials**, you must store your authentication credentials for Chainguard Registry in an AWS Secrets Manager secret. You can specify an existing secret or use the Amazon ECR console to create a new secret.

   1. To use an existing secret, choose **Use an existing AWS secret**. For **Secret name** use the drop down to select your existing secret, and then choose **Next**. For more information on creating a Secrets Manager secret using the Secrets Manager console, see [Storing your upstream repository credentials in an AWS Secrets Manager secret](#pull-through-cache-creating-secret).
**Note**  
The AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix. The secret must also be in the same account and Region that the pull through cache rule is created in.

   1. To create a new secret, choose **Create an AWS secret**, do the following, then choose **Next**.

      1. For **Secret name**, specify a descriptive name for the secret. Secret names must contain 1-512 Unicode characters.

      1. For **Chainguard Registry username**, specify your Chainguard Registry username.

      1. For **Chainguard Registry pull token**, specify your Chainguard Registry pull token. For more information on creating a Chainguard Registry pull token, see [Authenticating with a Pull Token](https://edu.chainguard.dev/chainguard/chainguard-images/chainguard-registry/authenticating/#authenticating-with-a-pull-token) in the Chainguard documentation.

1. On the **Step 3: Specify a destination** page, for **Amazon ECR repository prefix**, specify the repository namespace to use when caching images pulled from the source registry and then choose **Next**.

   By default, a namespace is populated but a custom namespace can be specified as well.

1. On the **Step 4: Review and create** page, review the pull through cache rule configuration and then choose **Create**.

1. Repeat the previous step for each pull through cache you want to create. The pull through cache rules are created separately for each Region.

### To create a pull through cache rule (AWS CLI)
<a name="pull-through-cache-creating-rule-cli"></a>

Use the [create-pull-through-cache-rule](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-pull-through-cache-rule.html) AWS CLI command to create a pull through cache rule for an Amazon ECR private registry. For upstream registries that require authentication with secrets, you must store the credentials in an Secrets Manager secret. To create a secret using the Secrets Manager console, see [Storing your upstream repository credentials in an AWS Secrets Manager secret](#pull-through-cache-creating-secret).

The following examples are provided for each supported upstream registry.

#### For Amazon ECR Public
<a name="w2aac30c27c11b7b1"></a>

The following example creates a pull through cache rule for the Amazon ECR Public registry. It specifies a repository prefix of `ecr-public`, which results in each repository created using the pull through cache rule to have the naming scheme of `ecr-public/{{upstream-repository-name}}`.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{ecr-public}} \
     --upstream-registry-url public.ecr.aws \
     --region {{us-east-2}}
```

#### For Kubernetes Container Registry
<a name="w2aac30c27c11b7b3"></a>

The following example creates a pull through cache rule for the Kubernetes public registry. It specifies a repository prefix of `kubernetes`, which results in each repository created using the pull through cache rule to have the naming scheme of `kubernetes/{{upstream-repository-name}}`.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{kubernetes}} \
     --upstream-registry-url registry.k8s.io \
     --region {{us-east-2}}
```

#### For Quay
<a name="w2aac30c27c11b7b5"></a>

The following example creates a pull through cache rule for the Quay public registry. It specifies a repository prefix of `quay`, which results in each repository created using the pull through cache rule to have the naming scheme of `quay/{{upstream-repository-name}}`.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{quay}} \
     --upstream-registry-url quay.io \
     --region {{us-east-2}}
```

#### For Docker Hub
<a name="w2aac30c27c11b7b7"></a>

The following example creates a pull through cache rule for the Docker Hub registry. It specifies a repository prefix of `docker-hub`, which results in each repository created using the pull through cache rule to have the naming scheme of `docker-hub/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your Docker Hub credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{docker-hub}} \
     --upstream-registry-url registry-1.docker.io \
     --credential-arn arn:aws:secretsmanager:{{us-east-2}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-2}}
```

#### For GitHub Container Registry
<a name="w2aac30c27c11b7b9"></a>

The following example creates a pull through cache rule for the GitHub Container Registry. It specifies a repository prefix of `github`, which results in each repository created using the pull through cache rule to have the naming scheme of `github/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your GitHub Container Registry credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{github}} \
     --upstream-registry-url ghcr.io \
     --credential-arn arn:aws:secretsmanager:{{us-east-2}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-2}}
```

#### For Microsoft Azure Container Registry
<a name="w2aac30c27c11b7c11"></a>

The following example creates a pull through cache rule for the Microsoft Azure Container Registry. It specifies a repository prefix of `azure`, which results in each repository created using the pull through cache rule to have the naming scheme of `azure/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your Microsoft Azure Container Registry credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{azure}} \
     --upstream-registry-url {{myregistry}}.azurecr.io \
     --credential-arn arn:aws:secretsmanager:{{us-east-2}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-2}}
```

#### For GitLab Container Registry
<a name="w2aac30c27c11b7c13"></a>

The following example creates a pull through cache rule for the GitLab Container Registry. It specifies a repository prefix of `gitlab`, which results in each repository created using the pull through cache rule to have the naming scheme of `gitlab/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your GitLab Container Registry credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{gitlab}} \
     --upstream-registry-url registry.gitlab.com \
     --credential-arn arn:aws:secretsmanager:{{us-east-2}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-2}}
```

#### For Amazon ECR private registry within your AWS account
<a name="w2aac30c27c11b7c15"></a>

The following example creates a pull through cache rule for the Amazon ECR private registry for cross-Region within the same AWS account. It specifies a repository prefix of `ecr`, which results in each repository created using the pull through cache rule to have the naming scheme of `ecr/{{upstream-repository-name}}`. 

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix ecr \
     --upstream-registry-url {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com \
     --region {{us-east-2}}
```

#### For Amazon ECR private registry from another AWS account
<a name="w2aac30c27c11b7c17"></a>

The following example creates a pull through cache rule for the Amazon ECR private registry for cross-Region within the same AWS account. It specifies a repository prefix of `ecr`, which results in each repository created using the pull through cache rule to have the naming scheme of `ecr/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the IAM role with the permissions created in [Creating a pull through cache rule in Amazon ECR](#pull-through-cache-creating-rule).

```
aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix ecr \
 --upstream-registry-url {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com \
 --custom-role-arn arn:aws:iam::{{aws_account_id}}:role/{{example-role}} \
 --region {{us-east-2}}
```

#### For Chainguard Registry
<a name="w2aac30c27c11b7c19"></a>

The following example creates a pull through cache rule for the Chainguard Registry. It specifies a repository prefix of `chainguard`, which results in each repository created using the pull through cache rule to have the naming scheme of `chainguard/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your Chainguard Registry credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{chainguard}} \
     --upstream-registry-url cgr.dev \
     --credential-arn arn:aws:secretsmanager:{{us-east-2}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-2}}
```

### Next steps
<a name="pull-through-cache-creating-rule-next-steps"></a>

After you create your pull through cache rules, the following are the next steps:
+ Create a repository creation template. A repository creation template gives you control to define the settings to use for new repositories created by Amazon ECR on your behalf during a pull through cache action. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).
+ Validate your pull through cache rules. When validating a pull through cache rule, Amazon ECR makes a network connection with the upstream registry, verifies that it can access the Secrets Manager secret containing the credentials for the upstream registry, and that authentication was successful. For more information, see [Validating pull through cache rules in Amazon ECR](#pull-through-cache-working-validating).
+ Start using your pull through cache rules. For more information, see [Pulling an image with a pull through cache rule in Amazon ECR](#pull-through-cache-working-pulling).

## Validating pull through cache rules in Amazon ECR
<a name="pull-through-cache-working-validating"></a>

After you create a pull through cache rule, for upstream registries that require authentication you can validate that the rule works properly. When validating a pull through cache rule, Amazon ECR makes a network connection with the upstream registry, verifies that it can access the Secrets Manager secret containing the credentials for the upstream registry, and verifies that authentication was successful.

Before you start working with your pull through cache rules, verify that you have the proper IAM permissions. For more information, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](#pull-through-cache-iam).

### To validate a pull through cache rule (AWS Management Console)
<a name="pull-through-cache-working-verifying-console"></a>

The following steps show how to validate a pull through cache rule using the Amazon ECR console.

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region containing the pull through cache rule to validate.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, select the pull through cache rule to validate. Then, use the **Actions** drop down menu and choose **View details**.

1. On the pull through cache rule detail page, use the **Actions** drop down menu and choose **Verify authentication**. Amazon ECR will display a banner with the result.

1. Repeat these steps for each pull through cache rule you want to validate.

### To validate a pull through cache rule (AWS CLI)
<a name="pull-through-cache-working-verifying-cli"></a>

The [validate-pull-through-cache-rule](https://docs.aws.amazon.com/cli/latest/reference/ecr/validate-pull-through-cache-rule.html) AWS CLI command is used to validate a pull through cache rule for an Amazon ECR private registry. The following example uses the `ecr-public` namespace prefix. Replace that value with the prefix value for the pull through cache rule to validate.

```
aws ecr validate-pull-through-cache-rule \
     --ecr-repository-prefix {{ecr-public}} \
     --region {{us-east-2}}
```

In the response, the `isValid` parameter indicates whether the validation was successful or not. If `true`, Amazon ECR was able to reach the upstream registry and authentication was successful. If `false`, there was an issue and validation failed. The `failure` parameter indicates the cause.

## Pulling an image with a pull through cache rule in Amazon ECR
<a name="pull-through-cache-working-pulling"></a>

The following examples show the command syntax to use when pulling an image using a pull through cache rule. If you receive an error pulling an upstream image using a pull through cache rule, see [Troubleshooting pull through cache issues in Amazon ECR](#error-pullthroughcache) for the most common errors and how to resolve them.

Before you start working with your pull through cache rules, verify that you have the proper IAM permissions. For more information, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](#pull-through-cache-iam).

**Note**  
The following examples use the default Amazon ECR repository namespace values that the AWS Management Console uses. Ensure that you use the Amazon ECR private repository URI that you've configured.

### For Amazon ECR Public
<a name="w2aac30c31b9b1"></a>

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{ecr-public}}/{{repository_name/image_name:tag}}
```

### Kubernetes container registry
<a name="w2aac30c31b9b3"></a>

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{kubernetes}}/{{repository_name/image_name:tag}}
```

### Quay
<a name="w2aac30c31b9b5"></a>

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{quay}}/{{repository_name/image_name:tag}}
```

### Docker Hub
<a name="w2aac30c31b9b7"></a>

For Docker Hub official images:

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/docker-hub/library/{{image_name:tag}}
```

**Note**  
For Docker Hub official images, the `/library` prefix must be included. For all other Docker Hub repositories, you should omit the `/library` prefix.

For all other Docker Hub images:

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{docker-hub}}/{{repository_name/image_name:tag}}
```

### GitHub Container Registry
<a name="w2aac30c31b9b9"></a>

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{github}}/{{repository_name/image_name:tag}}
```

### Microsoft Azure Container Registry
<a name="w2aac30c31b9c11"></a>

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{azure}}/{{repository_name/image_name:tag}}
```

### GitLab Container Registry
<a name="w2aac30c31b9c13"></a>

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{gitlab}}/{{repository_name/image_name:tag}}
```

### Chainguard Registry
<a name="w2aac30c31b9c15"></a>

```
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{chainguard}}/{{repository_name/image_name:tag}}
```

## Storing your upstream repository credentials in an AWS Secrets Manager secret
<a name="pull-through-cache-creating-secret"></a>

When creating a pull through cache rule for an upstream repository that requires authentication, you must store the credentials in a Secrets Manager secret. There may be a cost for using an Secrets Manager secret. For more information, see [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing/).

The following procedures walk you through how to create an Secrets Manager secret for each supported upstream repository. You can optionally use the create pull through cache rule workflow in the Amazon ECR console to create the secret instead of creating the secret using the Secrets Manager console. For more information, see [Creating a pull through cache rule in Amazon ECR](#pull-through-cache-creating-rule).

------
#### [ Docker Hub ]

**To create a Secrets Manager secret for your Docker Hub credentials (AWS Management Console)**To create a Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your Docker Hub credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your Docker Hub username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your Docker Hub access token as the value. For more information on creating a Docker Hub access token, see [Create and manage access tokens](https://docs.docker.com/security/for-developers/access-tokens/) in the Docker documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following.

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ GitHub Container Registry ]

**To create an Secrets Manager secret for your GitHub Container Registry credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your GitHub credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your GitHub username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your GitHub access token as the value. For more information on creating a GitHub access token, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) in the GitHub documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ Microsoft Azure Container Registry ]

**To create an Secrets Manager secret for your Microsoft Azure Container Registry credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your Microsoft Azure credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your Microsoft Azure Container Registry username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your Microsoft Azure Container Registry access token as the value. For more information on creating an Microsoft Azure access token, see [Create token - portal](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-repository-scoped-permissions#create-token---portal) in the Microsoft Azure documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ GitLab Container Registry ]

**To create an Secrets Manager secret for your GitLab Container Registry credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your GitLab credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your GitLab Container Registry username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your GitLab Container Registry access token as the value. For more information on creating a GitLab Container Registry access token, see [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html), [Group access tokens](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html), or [Project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html), in the GitLab documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ Chainguard Registry ]

**To create an Secrets Manager secret for your Chainguard credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your Chainguard credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your Chainguard Registry username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your Chainguard Registry access token as the value. For more information on creating a Chainguard Registry pull token, see [Authenticating with a Pull Token ](https://edu.chainguard.dev/chainguard/chainguard-images/chainguard-registry/authenticating/#authenticating-with-a-pull-token) in the Chainguard documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------

## Customizing repository prefixes for ECR to ECR pull through cache
<a name="pull-through-cache-private-wildcards"></a>

Pull through cache rules support both the **ecr repository prefix** and the **upstream repository prefix**. The **ecr repository prefix** is the repository namespace prefix in Amazon ECR cache registry that's associated with the rule. All repositories using this prefix become pull through cache-enabled repositories for the upstream registry defined in the rule. For example, a prefix of `prod` applies to all repositories beginning with `prod/`. To apply a template to all repositories in your registry that don't have an associated pull through cache rule, use `ROOT` as the prefix.

**Important**  
There is always an assumed `/` applied to the end of the prefix. If you specify `ecr-public` as the prefix, Amazon ECR treats that as `ecr-public/`.

The **upstream repository prefix** matches the upstream repository name. By default, it's set to `ROOT`, which allows matching with any upstream repository. You can set the **upstream repository prefix** only when the Amazon ECR repository prefix has a non-`ROOT` value.

The following table shows the mapping between cache repository names and upstream repository names based on their prefix configurations in pull through cache rules.


|  Cache namespace  |  Upstream namespace  |  Mapping relationship (cache repository → upstream repository)  | 
| --- | --- | --- | 
| ecr-public | ROOT (default) | `ecr-public/my-app/image1` → `my-app/image1`<br />`ecr-public/my-app/image2` → `my-app/image2` | 
| ROOT | ROOT | `my-app/image1` → `my-app/image1` | 
| team-a | team-a | `team-a/myapp/image1` → `team-a/myapp/image1` | 
| my-app | upstream-app | `my-app/image1` → `upstream-app/image1` | 

## Troubleshooting pull through cache issues in Amazon ECR
<a name="error-pullthroughcache"></a>

When pulling an upstream image using a pull through cache rule, the following are the most common errors you may receive.

**Repository does not exist**  
An error indicating that the repository doesn't exist is most often caused by either the repository not existing in your Amazon ECR private registry or the `ecr:CreateRepository` permission not being granted to the IAM principal pulling the upstream image. To resolve this error, you should verify that the repository URI in your pull command is correct, the required IAM permissions are granted to the IAM principal pulling the upstream image, or that the repository for the upstream image to be pushed to is created in your Amazon ECR private registry before doing the upstream image pull. For more information about the required IAM permissions, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](#pull-through-cache-iam)  
The following is an example of this error.  

```
Error response from daemon: repository 111122223333.dkr.ecr.us-east-1.amazonaws.com/ecr-public/amazonlinux/amazonlinux not found: name unknown: The repository with name 'ecr-public/amazonlinux/amazonlinux' does not exist in the registry with id '111122223333'
```

**Requested image not found**  
An error indicating that the image can't be found is most often caused by either the image not existing in the upstream registry or the `ecr:BatchImportUpstreamImage` permission not being granted to the IAM principal pulling the upstream image but the repository already being created in your Amazon ECR private registry. To resolve this error, you should verify the upstream image and image tag name is correct and that it exists and the required IAM permissions are granted to the IAM principal pulling the upstream image. For more information about the required IAM permissions, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](#pull-through-cache-iam).  
The following is an example of this error.  

```
Error response from daemon: manifest for 111122223333.dkr.ecr.us-east-1.amazonaws.com/ecr-public/amazonlinux/amazonlinux:latest not found: manifest unknown: Requested image not found
```

**403 Forbidden when pulling from a Docker Hub repository**  
When pulling from a Docker Hub repository that is tagged as a **Docker Official Image**, you must include the `/library/` in the URI you use. For example, `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/docker-hub/library/{{image_name:tag}}`. If you omit the `/library/` for Docker Hub Official images, a `403 Forbidden` error will be returned when you attempt to pull the image using a pull through cache rule. For more information, see [Pulling an image with a pull through cache rule in Amazon ECR](#pull-through-cache-working-pulling).  
The following is an example of this error.  

```
Error response from daemon: failed to resolve reference "111122223333.dkr.ecr.us-west-2.amazonaws.com/docker-hub/amazonlinux:2023": pulling from host 111122223333.dkr.ecr.us-west-2.amazonaws.com failed with status code [manifests 2023]: 403 Forbidden
```

# Private image replication in Amazon ECR
<a name="replication"></a>

You can configure your Amazon ECR private registry to support the replication of your repositories. Amazon ECR supports both cross-Region and cross-account replication. For cross-account replication to occur, the destination account must configure a registry permissions policy to allow replication from the source registry to occur. For more information, see [Private registry permissions in Amazon ECR](#registry-permissions).

**Topics**
+ [Cross-account replication policy requirements](#replication-policy-clarification)
+ [Considerations for private image replication](#replication-considerations)
+ [Private image replication examples for Amazon ECR](#registry-settings-examples)
+ [Configuring private image replication in Amazon ECR](#registry-settings-configure)
+ [Removing private image replication settings in Amazon ECR](#registry-settings-remove)

## Cross-account replication policy requirements
<a name="replication-policy-clarification"></a>

For cross-account ECR replication to work properly, you must understand which account needs which policies configured. This section clarifies the policy requirements for both source and destination accounts.

### Policy configuration overview
<a name="replication-policy-overview"></a>

Cross-account ECR replication requires policy configuration on the **destination account only**. The source account does not require any special repository or registry policies.
+ **Source Account**: Configure replication rules in the registry settings. No additional policies required on source repositories.
+ **Destination Account**: Configure a registry permissions policy to allow the source account to replicate images.

### Destination registry policy requirements
<a name="destination-registry-policy-requirements"></a>

The destination account must configure a registry permissions policy that grants the source account permission to perform the following actions:
+ `ecr:ReplicateImage` - Allows the source account to replicate images to the destination registry
+ `ecr:CreateRepository` - Allows ECR to automatically create repositories in the destination registry if they don't already exist

**Important**  
If you do not grant the `ecr:CreateRepository` permission, you must manually create repositories with the same names in the destination account before replication can succeed.

Example destination registry policy:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCrossAccountReplication",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": [
                "ecr:ReplicateImage",
                "ecr:CreateRepository"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Source account requirements
<a name="source-account-requirements"></a>

The source account only needs to:
+ Configure replication rules in the registry settings to specify the destination account and regions
+ Ensure the IAM principal configuring replication has the necessary ECR permissions

**No additional policies are required on source repositories.** The source repositories do not need repository policies that grant replication permissions.

### Common misconceptions
<a name="common-misconceptions"></a>

The following are common misconceptions about ECR cross-account replication policies:
+ **Misconception**: The source repository needs a policy allowing the destination account to replicate images.

  **Reality**: Source repositories do not need any special policies for replication.
+ **Misconception**: Both source and destination accounts need registry policies.

  **Reality**: Only the destination account needs a registry permissions policy.
+ **Misconception**: Repository policies and registry policies are the same thing.

  **Reality**: Repository policies control access to individual repositories, while registry policies control registry-level operations like replication.

### Troubleshooting replication failures
<a name="replication-troubleshooting"></a>

If cross-account replication is failing, check the following:
+ Verify the destination account has a registry permissions policy configured
+ Ensure the registry policy includes both `ecr:ReplicateImage` and `ecr:CreateRepository` actions
+ Confirm the source account ID is correctly specified in the destination registry policy
+ Check that the destination repositories exist (if `ecr:CreateRepository` is not granted)
+ Review CloudTrail logs for failed `CreateRepository` or `ReplicateImage` API calls

## Considerations for private image replication
<a name="replication-considerations"></a>

The following should be considered when using private image replication.
+ Only repository content pushed or restored to a repository after replication is configured is replicated. Any preexisting content in a repository isn't replicated. If an image is restored after replication is turned on, it will be replicated. If it is restored before replication is turned on, it won't be replicated.
+ The repository name will remain the same across Regions and accounts when replication has occurred. Amazon ECR doesn't support changing the repository name during replication.
+ The first time you configure your private registry for replication, Amazon ECR creates a service-linked IAM role on your behalf. The service-linked IAM role grants the Amazon ECR replication service the permission it needs to create repositories and replicate images in your registry. For more information, see [Using service-linked roles for Amazon ECR](#using-service-linked-roles).
+ For cross-account replication to occur, the private registry destination must grant permission to allow the source registry to replicate its images. This is done by setting a private registry permissions policy. For more information, see [Private registry permissions in Amazon ECR](#registry-permissions).
+ If the permission policy for a private registry are changed to remove a permission, any in-progress replications previously granted may complete.
+ For cross-Region replication to occur, both the source and destination accounts must be opted-in to the Region prior to any replication actions occurring within or to that Region. For more information, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *Amazon Web Services General Reference*.
+ Cross-Region replication is not supported between AWS partitions. For example, a repository in `us-west-2` can't be replicated to ` cn-north-1`. For more information about AWS partitions, see [ARN format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax) in the *AWS General Reference*.
+ The replication configuration for a private registry may contain up to 25 unique destinations across all rules, with a maximum of 25 rules total. Each rule may contain up to 100 filters. This allows for specifying separate rules for repositories containing images used for production and testing, for example.
+ The replication configuration supports filtering which repositories in a private registry are replicated by specifying a repository prefix. For an example, see [Example: Configuring cross-Region replication using a repository filter](#registry-settings-examples-crr-filter).
+ A replication action only occurs once per image push or image restore. For example, if you configured cross-Region replication from `us-west-2` to ` us-east-1` and from `us-east-1` to `us-east-2`, an image pushed to `us-west-2` replicates to only `us-east-1`, it doesn't replicate again to `us-east-2`. This behavior applies to both cross-Region and cross-account replication.
+ The majority of images replicate in less than 30 minutes, but in rare cases the replication might take longer.
+ Registry replication doesn't perform any delete actions or archive actions. Replicated images and repositories can be deleted or archived when they are no longer being used.
+ If the image to be replicated is archived in the destination, then it will be restored in the destination.
+ When an image is archived in a source region, it will not be archived in a destination region specified by the replication configuration.
+ Repository policies, including IAM policies, and lifecycle policies aren't replicated and don't have any effect other than on the repository they are defined for.
+ Repository settings aren't replicated by default, you can replicate the repository settings using repository creation templates. These settings include tag mutability, encryption, repository permissions, and lifecycle policies. For more information about repository creation templates, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).
+ If tag immutability is enabled on a repository and an image is replicated that uses the same tag as an existing image, the image is replicated but won't contain the duplicated tag. This might result in the image being untagged.
+ When replicating images, if blob mounting has been configured, ECR will check to ensure any layers from the source repository already exist in the destination registry. If any layers already exist in the destination registry, ECR will mount those layers. 

**Note**  
If the source registry is different from its destination registry, blob mounting will need to be enabled for both registries for ECR to mount replicated layers.

## Private image replication examples for Amazon ECR
<a name="registry-settings-examples"></a>

The following examples show common use cases for private image replication. If you configure replication by using the AWS CLI, you can use the JSON examples as a starting point when you create your JSON file. If you configure replication by using the AWS Management Console, you will see similar JSON when you review your replication rule on the **Review and submit** page.

### Example: Configuring cross-Region replication to a single destination Region
<a name="registry-settings-examples-crr-single"></a>

The following shows an example for configuring cross-Region replication within a single registry. This example assumes that your account ID is ` 111122223333` and that you're specifying this replication configuration in a Region other than `us-west-2`.

```
{
    "rules": [
        {
            "destinations": [
                {
                    "region": "{{us-west-2}}",
                    "registryId": "{{111122223333}}"
                }
            ]
        }
    ]
}
```

### Example: Configuring cross-Region replication using a repository filter
<a name="registry-settings-examples-crr-filter"></a>

The following shows an example for configuring cross-Region replication for repositories that match a prefix name value. This example assumes your account ID is ` 111122223333` and that you're specifying this replication configuration in a Region other than `us-west-1` and have repositories with a prefix of `prod`.

```
{
	"rules": [{
		"destinations": [{
			"region": "{{us-west-1}}",
			"registryId": "{{111122223333}}"
		}],
		"repositoryFilters": [{
			"filter": "{{prod}}",
			"filterType": "PREFIX_MATCH"
		}]
	}]
}
```

### Example: Configuring cross-Region replication to multiple destination Regions
<a name="registry-settings-examples-crr-multipledestinations"></a>

The following shows an example for configuring cross-Region replication within a single registry. This example assumes your account ID is ` 111122223333` and that you're specifying this replication configuration in a Region other than `us-west-1` or `us-west-2` .

```
{
    "rules": [
        {
            "destinations": [
                {
                    "region": "{{us-west-1}}",
                    "registryId": "{{111122223333}}"
                },
                {
                    "region": "{{us-west-2}}",
                    "registryId": "{{111122223333}}"
                }
            ]
        }
    ]
}
```

### Example: Configuring cross-account replication
<a name="registry-settings-examples-crossaccount"></a>

The following shows an example for configuring cross-account replication for your registry. This example configures replication to the `444455556666` account and to the `us-west-2` Region.

**Important**  
For cross-account replication to occur, the destination account must configure a registry permissions policy to allow replication to occur. For more information, see [Private registry permissions in Amazon ECR](#registry-permissions).

```
{
    "rules": [
        {
            "destinations": [
                {
                    "region": "{{us-west-2}}",
                    "registryId": "{{444455556666}}"
                }
            ]
        }
    ]
}
```

### Example: Specifying multiple rules in a configuration
<a name="registry-settings-examples-multiple-rules"></a>

The following shows an example for configuring multiple replication rules for your registry. This example configures replication for the {{ 111122223333}} account with one rule that replicates repositories with a prefix of `prod` to the `us-west-2` Region and repositories with a prefix of `test` to the `us-east-2` Region. A replication configuration may contain up to 25 rules, with each rule specifying up to 25 destinations.

```
{
	"rules": [{
			"destinations": [{
				"region": "{{us-west-2}}",
				"registryId": "{{111122223333}}"
			}],
			"repositoryFilters": [{
				"filter": "{{prod}}",
				"filterType": "PREFIX_MATCH"
			}]
		},
		{
			"destinations": [{
				"region": "{{us-east-2}}",
				"registryId": "{{111122223333}}"
			}],
			"repositoryFilters": [{
				"filter": "{{test}}",
				"filterType": "PREFIX_MATCH"
			}]
		}
	]
}
```

### Example: Removing all replication settings
<a name="registry-settings-examples-remove"></a>

The following shows an example for removing all replication settings from your registry. To remove replication settings, you must configure an empty rules array.

```
{
    "rules": []
}
```

**Important**  
Removing replication settings does not delete any previously replicated repositories or images. You must manually delete replicated content if it is no longer needed.

## Configuring private image replication in Amazon ECR
<a name="registry-settings-configure"></a>

Configure replication per Region for your private registry. You can configure cross-Region replication or cross-account replication.

For examples of how replication is commonly used, see [Private image replication examples for Amazon ECR](#registry-settings-examples).

### To configure registry replication settings (AWS Management Console)
<a name="registry-settings-configure-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region to configure your registry replication settings for.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, choose ** Settings** and then choose **Edit** under **Replication configuration**.

1. On the **Replication** page, choose **Add replication rule**.

1. On the **Destination types** page, choose whether to enable cross-Region replication, cross-account replication, or both and then choose **Next**.

1. If cross-Region replication is enabled, then for **Configure destination regions**, choose one or more **Destination regions** and then choose **Next**.

1. If cross-account replication is enabled, then for **Cross-account replication**, choose the cross-account replication setting for the registry. For **Destination account**, enter the account ID for the destination account and one or more **Destination regions** to replicate to. Choose **Destination account \+** to configure additional accounts as replication destinations.
**Important**  
For cross-account replication to occur, the destination account must configure a registry permissions policy to allow replication to occur. For more information, see [Private registry permissions in Amazon ECR](#registry-permissions).

1. (Optional) On the **Add filters** page, specify one or more filters for the replication rule and then choose **Add**. Repeat this step for each filter you want to associate with the replication action. A filter must be specified as a repository name prefix. If no filters are added, the contents of all repositories are replicated. Choose **Next** once all filters have been added.

1. On the **Review and submit** page, review the replication rule configuration and then choose **Submit rule**.

### To configure registry replication settings (AWS CLI)
<a name="registry-settings-configure-cli"></a>

1. Create a JSON file containing the replication rules to define for your registry. A replication configuration may contain up to 10 rules, with up to 25 unique destinations across all rules and 100 filters per each rule. To configure cross-Region replication within your own account, you specify your own account ID. For more examples, see [Private image replication examples for Amazon ECR](#registry-settings-examples).

   ```
   {
   	"rules": [{
   		"destinations": [{
   			"region": "{{destination_region}}",
   			"registryId": "{{destination_accountId}}"
   		}],
   		"repositoryFilters": [{
   			"filter": "{{repository_prefix_name}}",
   			"filterType": "PREFIX_MATCH"
   		}]
   	}]
   }
   ```

1. Create a replication configuration for your registry.

   ```
   aws ecr put-replication-configuration \
        --replication-configuration file://{{replication-settings.json}} \
        --region {{us-west-2}}
   ```

1. Confirm your registry settings.

   ```
   aws ecr describe-registry \
        --region {{us-west-2}}
   ```

## Removing private image replication settings in Amazon ECR
<a name="registry-settings-remove"></a>

To remove or disable replication settings for your private registry, you need to configure an empty replication configuration. There is no dedicated removal command in the AWS CLI.

### To remove registry replication settings (AWS Management Console)
<a name="registry-settings-remove-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region to remove your registry replication settings from.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, choose ** Settings** and then choose **Edit** under **Replication configuration**.

1. Remove all existing replication rules by choosing the delete option for each rule.

1. Choose **Save** to apply the empty replication configuration.

### To remove registry replication settings (AWS CLI)
<a name="registry-settings-remove-cli"></a>

1. Create a JSON file with an empty rules array to remove all replication settings.

   ```
   {
       "rules": []
   }
   ```

1. Apply the empty replication configuration to your registry.

   ```
   aws ecr put-replication-configuration \
        --replication-configuration file://{{empty-replication-settings.json}} \
        --region {{us-west-2}}
   ```

1. Confirm that replication settings have been removed.

   ```
   aws ecr describe-registry \
        --region {{us-west-2}}
   ```

   The output should show an empty `replicationConfiguration` with no rules.

**Important**  
Removing replication settings does not delete any previously replicated repositories or images. You must manually delete replicated content if it is no longer needed.

# Templates to control repositories created during a pull through cache, create on push, or replication action
<a name="repository-creation-templates"></a>

Use Amazon ECR repository creation templates to define the settings for repositories created by Amazon ECR on your behalf. The settings in a repository creation template are only applied during repository creation and don't have any effect on existing repositories or repositories created using any other method. Currently, repository creation templates can be used to apply settings during repository creation for these features:
+ Pull through cache
+ Create on push
+ Replication

## How repository creation templates work
<a name="repository-creation-templates-works"></a>

There are times when Amazon ECR needs to create a new private repository on your behalf. For example:
+ The first time you use a pull through cache rule to retrieve the contents of an upstream repository and store it in your Amazon ECR private registry.
+ When you push an image to a repository that does not yet exist.
+ When you want Amazon ECR to replicate a repository to another region or account.

When there isn't a repository creation template that matches your pull through cache rule or replicated repository, Amazon ECR uses the default settings for the new repository. These default settings include turning off tag immutability, using `AES-256` encryption, and not applying any repository or lifecycle policies.

When there isn't a repository creation template that matches the target repository for an image push, Amazon ECR will not create a repository with default settings.

Using a repository creation template gives you the ability to define the settings Amazon ECR applies to new repositories created through the pull through cache, create on push, and replication actions. You can define the tag immutability, encryption configuration, repository permissions, lifecycle policy, and resource tags for the new repositories.

The following diagram shows the workflow that Amazon ECR uses when a repository creation template is used.

![A display of how repository creation templates are applied to new repositories.](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images/repository_creation_template_light.png)


The following describes each parameter in a repository creation template in detail.

Prefix  
The **Prefix** is the repository namespace prefix to associate with the template. All repositories created using this prefix will have the settings applied that are defined in this template. For example, a prefix of `prod` would apply to all repositories beginning with `prod/`. Similarly, a prefix of `prod/team` would apply to all repositories beginning with `prod/team/`. In a registry containing two templates, if one template has the prefix "prod" and the other has the prefix "prod/team", the template with the prefix "prod/team" will be applied to all repositories whose names start with "prod/team/".  
To apply a template to all repositories in your registry that don't have an associated creation template, you can use `ROOT` as the prefix.  
There is always an assumed `/` applied to the end of the prefix. If you specify `ecr-public` as the prefix, Amazon ECR treats that as `ecr-public/`. When using a pull through cache rule, the repository prefix you specify during rule creation is what you should specify as your repository creation template prefix as well.

Description  
This **template description** is optional and is used to describe the purpose for the repository creation template.

Applied For  
The **applied for** setting determines which Amazon ECR-created repositories will be created with this template. The valid values are `PULL_THROUGH_CACHE`, `CREATE_ON_PUSH`, and `REPLICATION`. For example, the first time you use a pull through cache rule to retrieve the contents of an upstream repository and store it in your Amazon ECR private registry. When there isn't a repository creation template that matches your pull through cache rule, Amazon ECR uses the default settings for the new repository.

Repository creation role  
The ** repository creation role** is an IAM role ARN that will be assumed by Amazon ECR when creating and configuring repositories via repository creation templates. This role must be provided when using repository tags and/or KMS in the template, otherwise the repository creation will fail.

Image tag mutability  
The **tag mutability** setting to use for repositories created using the template. If this parameter is omitted, the default setting of **MUTABLE** will be used which will allow image tags to be overwritten. This is the recommended setting to use for templates used for repositories created by pull through cache actions. This ensures that Amazon ECR can update the cached images when the tags are the same.  
If **IMMUTABLE** is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.

Encryption configuration  
 Dual-layer server-side encryption with AWS KMS (DSSE-KMS) is only available in the AWS GovCloud (US) Regions.
The **encryption configuration** to use for repositories created using the template.  
If you use the **KMS** encryption type, the contents of the repository will be encrypted using server-side encryption with an AWS Key Management Service key stored in AWS KMS. When you use AWS KMS to encrypt your data, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you already created. You can further choose to use Single-layer or Dual-layer encryption with AWS KMS. For more information, see [Encryption at rest](#encryption-at-rest) . If you're using the **KMS** encryption type and using it with cross region replication, you may need additional permissions. For more information, see [Creating a KMS key policy for replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions-create.html).  
If you use the **AES256** encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES-256 encryption algorithm. For more information, see [Protecting data using server-side encryption with Amazon S3-managed encryption keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) in the *Amazon Simple Storage Service User Guide*.

Repository permissions  
The **repository policy** to apply to repositories created using the template. A repository policy uses resource-based permissions to control access to a repository. Resource-based permissions let you specify which IAM users or roles have access to a repository and what actions they can perform on it. By default, only the AWS account that created the repository has access to a repository. You can apply a policy document to grant or deny additional permissions to your repository. For more information, see [Private repository policies in Amazon ECR](#repository-policies).

Repository lifecycle policy  
The **lifecycle policy** to use for repositories created using the template. A lifecycle policy provides more control over the lifecycle management of images in a private repository. A lifecycle policy contains one or more rules, where each rule defines an action for Amazon ECR. This provides a way to automate the cleaning up of your container images by expiring images based on age or count. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies).

Resource tags  
The **resource tags** are metadata to apply to the repository to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. This permission needs to be applied on the destination registry policy if you are using repository creation templates with cross region replication.

## Creating a repository creation template in Amazon ECR
<a name="repository-creation-templates-create"></a>

You can create a repository creation template to define the settings to use for repositories created by Amazon ECR on your behalf during pull through cache, create on push, or replication actions. Once the repository creation template is created, all new repositories created will have the settings applied. This doesn't have any effect on any previously created repositories.

When setting up a repository with templates, you have the option to specify KMS keys and resource tags. If you intend to use KMS keys, resource tags, or a combination of both in one or more templates, you need to: 
+ [Create a custom policy for repository creation templates](#repository-creation-templates-custom).
+ [Create an IAM role for repository creation templates](#repository-creation-templates-create-iam).

Once configured, you can attach the custom role to specific templates in your registry.



### IAM permissions for creating repository creation templates
<a name="repository-creation-templates-iam"></a>

The following permissions are needed for an IAM principal to manage repository creation templates. These permission must be granted using an identity-based IAM policy.
+ `ecr:CreateRepositoryCreationTemplate` – Grants permission to create a repository creation template.
+ `ecr:UpdateRepositoryCreationTemplate` – Grants permission to update a repository creation template.
+ `ecr:DescribeRepositoryCreationTemplates` – Grants permission to list repository creation templates in a registry.
+ `ecr:DeleteRepositoryCreationTemplate` – Grants permission to delete a repository creation template.
+ `ecr:CreateRepository` – Grants permission to create an Amazon ECR repository.
+ `ecr:PutLifecyclePolicy` – Grants permission to create a lifecycle policy and apply it to a repository. This permission is only required if the repository creation template includes a lifecycle policy.
+ `ecr:SetRepositoryPolicy` – Grants permission to create a permissions policy for a repository. This permission is only required if the repository creation template includes a repository policy.
+ `iam:PassRole` – Grants permission to allow an entity to pass a role to a service or application. This permission is necessary for services and applications that need to assume a role to perform actions on your behalf.

### Create a repository creation template
<a name="repository-creation-templates-creating"></a>

Once you've completed the necessary prerequisites for your templates, you can proceed to create the repository creation templates.

------
#### [ AWS Management Console ]

**To create a repository creation template (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to create the repository creation template in.

1. In the navigation pane, choose **Private registry**, **Repository creation templates**.

1. On the **Repository creation templates** page, choose **Create template**.

1. On the **Step 1: Define template** page, for **Template details**, choose **A specific prefix** to apply the template to a specific repository namespace prefix or choose **Any prefix in your ECR registry** to apply the template to all repositories that don't match any other template in the Region.

   1. If you choose **A specific prefix**, for **Prefix** specify the repository namespace prefix to apply the template to. There is always an assumed `/` applied to the end of the prefix. For example, a prefix of `prod` would apply to all repositories beginning with `prod/`. Similarly, a prefix of `prod/team` would apply to all repositories beginning with `prod/team/`. 

   1. If you choose **Any prefix in your ECR registry**, the **Prefix** will be set to `ROOT`.

1. For **Applied for**, specify which Amazon ECR workflows this template will apply to. The options are `PULL_THROUGH_CACHE`, `CREATE_ON_PUSH`, and `REPLICATION`.

1. For **Template description**, specify an optional description for the template and then choose **Next**.

1. On the **Step 2: Add repository creation configuration** page, specify the repository setting configuration to apply to repositories created using the template.

   1. For **Image tag mutability**, choose the tag mutability setting to use. For more information, see [Preventing image tags from being overwritten in Amazon ECR](#image-tag-mutability).
      + **Mutable** – Choose this option if you want image tags to be overwritten. Recommended for repositories using pull through cache actions to ensure Amazon ECR can update cached images. Additionally, to disable tag updates for a few mutable tags, enter tag names or use wildcards (\*) to match multiple similar tags in the **Mutable tag exclusion** text box.
      + **Immutable** – Choose this option if you want to prevent image tags from being overwritten, and it applies to all tags and exclusions in the repository when pushing an image with existing tag. Amazon ECR returns an `ImageTagAlreadyExistsException` if you attempt to push an image with an existing tag. Additionally, to enable tag updates for a few immutable tags, enter tag names or use wildcards (\*) to match multiple similar tags in the **Immutable tag exclusion** text box. 

   1. For **Encryption configuration**, choose the encryption setting to use. For more information, see [Encryption at rest](#encryption-at-rest).

      When **AES-256** is selected, Amazon ECR uses server-side encryption with Amazon Simple Storage Service-managed encryption keys which encrypts your data at rest using an industry standard AES-256 encryption algorithm. This is offered at no additional cost.

      When **AWS KMS** is selected, Amazon ECR uses server-side encryption with keys stored in AWS Key Management Service (AWS KMS). When you use AWS KMS to encrypt your data, you can either use the default AWS managed key, which is managed by Amazon ECR, or specify your own AWS KMS key, which is referred to as a *customer managed key*.
**Note**  
The encryption settings for a repository can't be changed once the repository is created.

   1. For **Repository permissions**, specify the repository permissions policy to apply to repositories created using this template. You can optionally use the drop down to select one of the JSON samples for the most common use cases. For more information, see [Private repository policies in Amazon ECR](#repository-policies).

   1. For **Repository lifecycle policy**, specify the repository lifecycle policy to apply to repositories created using this template. You can optionally use the drop down to select one of the JSON samples for the most common use cases. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies).

   1. For **Repository AWS tags**, specify the metadata, in the form of key-value pairs, to associate with the repositories created using this template and then choose **Next**. For more information, see [Tagging a private repository in Amazon ECR](#ecr-using-tags).

   1. For **Repository creation role**, select a custom IAM role from the drop-down menu to be used for repository creation templates when using repository tags or KMS in the template (see [Create an IAM role for repository creation templates](#repository-creation-templates-create-iam) for details).Then choose **Next**.

1. On the **Step 3: Review and create** page, review the settings you specified for the repository creation template. Choose the **Edit** option to make changes. Choose **Create** once you're done.

------
#### [ AWS CLI ]

The [create-repository-creation-template](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository-creation-template.html) AWS CLI command is used to create a repository creation template for your private registry.

**To create a repository creation template (AWS CLI)**

1. Use the AWS CLI to generate a skeleton for the [create-repository-creation-template](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository-creation-template.html) command.

   ```
   aws ecr create-repository-creation-template \
       --generate-cli-skeleton
   ```

   The output of the command displays the full syntax of the repository creation template. 

   ```
   {
   "appliedFor":[""], // string array, but valid are PULL_THROUGH_CACHE, CREATE_ON_PUSH, and REPLICATION
   "prefix": "string",
       "description": "string",
       "imageTagMutability": "MUTABLE"|"IMMUTABLE"|"IMMUTABLE_WITH_EXCLUSION"|"MUTABLE_WITH_EXCLUSION",
       "imageTagMutabilityExclusionFilters": [
           "filterType": "WILDCARD",
           "filter": "string"
       ],
       "repositoryPolicy": "string",
       "lifecyclePolicy": "string"
   "encryptionConfiguration": {
   "encryptionType": "AES256"|"KMS",
           "kmsKey": "string"
       },
       "resourceTags": [
           {
   "Key": "string",
               "Value": "string"
           }
       ],
       "customRoleArn": "string", // must be a valid IAM Role ARN
   }
   ```

1. Create a file named `repository-creation-template.json` with the output of the previous step. This template sets a KMS encryption key for any repository created under `prod/*` with a repository policy that enables pushing and pulling images to future repositories, sets a lifecycle policy that will expire images older than two weeks and sets a custom role that will let ECR access the KMS key and assign the resource tag `examplekey` to future repositories.

   ```
   {
   "prefix": "prod",
       "description": "For repositories cached from my PTC rule and in my replication configuration that start with 'prod/'",
       "appliedFor": ["PULL_THROUGH_CACHE", "CREATE_ON_PUSH", "REPLICATION"],
       "encryptionConfiguration": {
   "encryptionType": "KMS",
           "kmsKey": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-example11111"
       },
       "resourceTags": [
           {
   "Key": "examplekey",
               "Value": "examplevalue"
           }
       ],
       "imageTagMutability": "IMMUTABLE_WITH_EXCLUSION",
       "imageTagMutabilityExclusionFilters": [
         {
         "filterType": "WILDCARD",
         "filter": "latest"
         },
         {
         "filterType": "WILDCARD",
         "filter": "beta*"
         }
       ]
       "repositoryPolicy": "{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":\"AllowPushPullIAMRole\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::111122223333:user\/IAMusername\"},\"Action\":[\"ecr:BatchGetImage\",\"ecr:BatchCheckLayerAvailability\",\"ecr:CompleteLayerUpload\",\"ecr:GetDownloadUrlForLayer\",\"ecr:InitiateLayerUpload\",\"ecr:PutImage\",\"ecr:UploadLayerPart\"]}]}", 
       "lifecyclePolicy": "{\"rules\":[{\"rulePriority\":1,\"description\":\"Expire images older than 14 days\",\"selection\":{\"tagStatus\":\"any\",\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":14},\"action\":{\"type\":\"expire\"}}]}",
       "customRoleArn": "arn:aws:iam::111122223333:role/myRole"
   }
   ```

1. Use the following command to create a repository creation template. Ensure that you specify the name of the configuration file created in the previous step in place of the `repository-creation-template.json` in the following example.

   ```
   aws ecr create-repository-creation-template \
       --cli-input-json file://{{repository-creation-template.json}}
   ```

------

### Create a custom policy for repository creation templates
<a name="repository-creation-templates-custom"></a>

You can use the AWS Management Console to define a policy that will be subsequently associated with an IAM role. This IAM role can then be utilized as a repository creation role when configuring a repository creation template.

------
#### [ AWS Management Console ]

**To use the JSON policy editor to create a custom policy for repository creation templates.**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane on the left, choose **Policies**. 

1. Choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Enter the following policy in the **JSON** field.

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
                       "ecr:CreateRepository", 
                       "ecr:ReplicateImage", 
                       "ecr:TagResource" 
                   ], 
                   "Resource": "*" 
               }, 
               {
                   "Effect": "Allow", 
                   "Action": [ 
                       "kms:CreateGrant", 
                       "kms:RetireGrant", 
                       "kms:DescribeKey" 
                   ], 
                   "Resource": "*" 
               } 
            ]
   }
   ```

------

1. Resolve any security warnings, errors, or general warnings generated during [ policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html), and then choose **Next**.

1. When you are finished adding permissions to the policy, choose **Next**.

1. On the **Review and create** page, type a **Policy Name** and a **Description** (optional) for the policy that you are creating. Review **Permissions defined in this policy** to see the permissions that are granted by your policy.

1. Choose **Create policy** to save your new policy.

1. Create a role to assign this policy for the creation template, see [Create an IAM role for repository creation templates](#repository-creation-templates-create-iam).

------

### Create an IAM role for repository creation templates
<a name="repository-creation-templates-create-iam"></a>

You can use the AWS Management Console to create a role that can be used by Amazon ECR when you specify the repository creation role in a repository creation template that is using repository tags or KMS in a template.

------
#### [ AWS Management Console ]

**To create a role.**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the console, choose **Roles** and then choose **Create role**.

1. Choose **Custom trust policy** role type.

1. In the **Custom trust policy** section, paste the custom trust policy listed below: 

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
               "Service": "ecr.amazonaws.com"
           },
           "Action": "sts:AssumeRole"
       }
       ]
   }
   ```

------

1. Choose **Next**.

1. From the **Add permissions** page, select the check box next to the custom policy you created earlier from the list of Permissions policies and choose **Next**.

1. For **Role name**, enter a name for your role. Role names must be unique within your AWS account. When a role name is used in a policy or as part of an ARN, the role name is case sensitive. When a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive. Because various entities might reference the role, you can't edit the name of the role after it is created.

1. (Optional) For **Description**, enter a description for the new role.

1. Review the role and then choose **Create role**.

------

## Updating a repository creation template
<a name="repository-creation-templates-updating"></a>

You can edit a repository creation template if you need to change its configurations. Once the repository creation template is edited, the new configurations will apply to the existing template. 

**Important**  
This doesn't have any effect on any previously created repositories.

------
#### [ AWS Management Console ]

**To edit a repository creation template (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region the repository creation template to edit is in.

1. In the navigation pane, choose **Private registry**, then choose **Settings**.

1. From the navigation bar, choose the **Repository creation templates**.

1. On the **Repository creation templates** page, select the repository creation template to edit.

1. From the **Actions** dropdown menu, choose **Edit**.

1. Review and update the configuration settings.

1. Choose update to apply the new creation template configurations.

------
#### [ AWS CLI ]

**To edit a repository creation template (AWS CLI)**
+ Use the [update-repository-creation-template](https://docs.aws.amazon.com/cli/latest/reference/ecr/update-repository-creation-template.html) command to update an existing repository creation template. You must specify the `prefix` value of the template. The following example updates a repository creation template with the `prod` prefix.

  ```
  aws ecr update-repository-creation-template \
       --prefix {{prod}} \
       --image-tag-mutability="IMMUTABLE_WITH_EXCLUSION" \
       --image-tag-mutability-exclusion-filters filterType={{WILDCARD}}, filter={{latest}}
  ```

  The output of the command displays the details of the updated repository creation template.

------

## Deleting a repository creation template in Amazon ECR
<a name="repository-creation-templates-delete"></a>

You can delete a repository creation template if you are finished using it. Once a repository creation template is deleted, any newly created repositories under the associated prefix during a pull through cache or replication action will inherit the default settings, unless another matching template is found, see [How repository creation templates work](#repository-creation-templates-works).

**Important**  
This doesn't have any effect on any previously created repositories.

------
#### [ AWS Management Console ]

**To delete a repository creation template (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region the repository creation template to delete is in.

1. In the navigation pane, choose **Private registry**, **Repository creation templates**.

1. On the **Repository creation templates** page, select the repository creation template to delete.

1. From the **Actions** dropdown menu, choose **Delete**.

------
#### [ AWS CLI ]

**To delete a repository creation template (AWS CLI)**
+ Use the [delete-repository-creation-template.html](https://docs.aws.amazon.com/cli/latest/reference/ecr/delete-repository-creation-template.html) command to delete an existing repository creation template. You must specify the `prefix` value of the template. The following example deletes a repository creation template with the `prod` prefix.

  ```
  aws ecr delete-repository-creation-template \
       --prefix {{prod}}
  ```

  The output of the command displays the details of the deleted repository creation template.

------

# Automate the cleanup of images by using lifecycle policies in Amazon ECR
<a name="LifecyclePolicies"></a>

Amazon ECR lifecycle policies provide more control over the lifecycle management of images in a private repository. A lifecycle policy contains one or more rules, and each rule defines an action for Amazon ECR. Based on the expiration criteria in the lifecycle policy, images can be archived or expired based on the criteria specified in the lifecycle policy within 24 hours. When Amazon ECR performs an action based on a lifecycle policy, this action is captured as an event in AWS CloudTrail. For more information, see [Logging Amazon ECR actions with AWS CloudTrail](#logging-using-cloudtrail).

## How lifecycle policies work
<a name="lifecycle-policy-howitworks"></a>

A lifecycle policy consists of one or more rules that determine which images in a repository should be expired. When considering the use of lifecycle policies, it's important to use the lifecycle policy preview to confirm which images the lifecycle policy expires before applying it to a repository. Once a lifecycle policy is applied to a repository, you should expect that images become expired within 24 hours after they meet the expiration criteria. When Amazon ECR performs an action based on a lifecycle policy, this is captured as an event in AWS CloudTrail. For more information, see [Logging Amazon ECR actions with AWS CloudTrail](#logging-using-cloudtrail).

The following diagram shows the lifecycle policy workflow.

![Diagram showing the process for evaluating and applying a lifecycle policy.](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images/lifecycle-policy.png)


1. Create one or more test rules.

1. Save the test rules and run the preview.

1. The lifecycle policy evaluator goes through all of the rules and marks the images that each rule affects.

1. The lifecycle policy evaluator then applies the rules, based on rule priority, and displays which images in the repository are set to be expired or archived. A lower rule priority number means higher priority. For example, a rule with priority 1 takes precedence over a rule with priority 2.

1. Review the results of the test, ensuring that the images that are marked to be expired or archived are what you intended.

1. Apply the test rules as the lifecycle policy for the repository.

1. Once the lifecycle policy is created, you should expect that images are expired or archived within 24 hours after they meet the expiration criteria.

### Lifecycle policy evaluation rules
<a name="lp_evaluation_rules"></a>

The lifecycle policy evaluator is responsible for parsing the plaintext JSON of the lifecycle policy, evaluating all rules, and then applying those rules based on rule priority to the images in the repository. The following explains the logic of the lifecycle policy evaluator in more detail. For examples, see [Examples of lifecycle policies in Amazon ECR](#lifecycle_policy_examples).
+ When reference artifacts are present in a repository, Amazon ECR lifecycle policies automatically expire or archive those artifacts within 24 hours of the deletion or archival of the subject image.
+ All rules are evaluated at the same time, regardless of rule priority. After all rules are evaluated, they are then applied based on rule priority.
+ An image is expired or archived by exactly one or zero rules.
+ An image that matches the tagging requirements of a rule cannot be expired or archived by a rule with a lower priority.
+ Rules can never mark images that are marked by higher priority rules, but can still identify them as if they haven't been expired or archived.
+ The set of all rules selecting a specific storage class must contain a unique set of prefixes.
+ Only one rule selecting a specific storage class is allowed to select untagged images.
+ If an image is referenced by a manifest list, it cannot be expired or archived without the manifest list being deleted or archived first.
+ Expiration is always ordered by `pushed_at_time` or `transitioned_at_time` and always expires older images before newer ones. If an image was archived and then restored at any point in the past, the image's `last_activated_at` is used instead of `pushed_at_time`.
+ A lifecycle policy rule may specify either `tagPatternList` or `tagPrefixList`, but not both. However, a lifecycle policy may contain multiple rules where different rules use both pattern and prefix lists. An image is successfully matched if all of the tags in the `tagPatternList` or `tagPrefixList` value are matched against any of the image's tags. 
+ The `tagPatternList` or `tagPrefixList` parameters may only used if the `tagStatus` is `tagged`.
+ When using `tagPatternList`, an image is successfully matched if it matches the wildcard filter. For example, if a filter of `prod*` is applied, it would match image-tags whose name begins with `prod` such as `prod`, `prod1`, or `production-team1`. Similarly, if a filter of `*prod*` is applied, it would match image-tags whose name contains `prod` such as `repo-production` or `prod-team`.
**Important**  
There is a maximum limit of four wildcards (`*`) per string. For example, `["*test*1*2*3", "test*1*2*3*"]` is valid but `["test*1*2*3*4*5*6"]` is invalid.
+ When using `tagPrefixList`, an image is successfully matched if ***all*** of the wildcard filters in the `tagPrefixList` value are matched against any of the image's tags.
+ The `countUnit` parameter is only used if `countType` is `sinceImagePushed`, `sinceImagePulled`, or `sinceImageTransitioned`.
+ With `countType = imageCountMoreThan`, images are sorted from youngest to oldest based on `pushed_at_time` and then all images greater than the specified count are expired or archived.
+ With `countType = sinceImagePushed`, all images whose `pushed_at_time` is older than the specified number of days based on `countNumber` are expired or archived.
+ With `countType = sinceImagePulled`, all images whose `last_recorded_pulltime` is older than the specified number of days based on `countNumber` are archived. If an image was never pulled, the image's `pushed_at_time` is used instead of the `last_recorded_pulltime`. If an image was archived and then restored at any point in the past, but never pulled since the image was restored, the image's `last_activated_at` is used instead of the `last_recorded_pulltime`.
+ With `countType = sinceImageTransitioned`, all archived images whose `last_archived_at` is older than the specified number of days based on `countNumber` are expired.
+ Expiration is always ordered by `pushed_at_time` and always expires older images before newer ones.

## Creating a lifecycle policy preview in Amazon ECR
<a name="lpp_creation"></a>

You can use a lifecycle policy preview to see the impact of a lifecycle policy on an image repository before you apply it. It is considered best practice to do a preview before applying a lifecycle policy to a repository.

**Note**  
If you are using Amazon ECR replication to make copies of a repository across different Regions or accounts, note that a lifecycle policy can only take an action on repositories in the Region it was created in. Therefore, if you have replication turned on you may want to create a lifecycle policy in each Region and account you are replicating your repositories to.

**To create a lifecycle policy preview (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository on which to perform a lifecycle policy preview.

1. In the navigation pane, under **Private registry**, choose **Repositories**.

1. On the **Private repositories** page, select a repository and that use the **Actions** drop down to choose **Lifecycle policies**.

1. On the lifecycle policy rules page for the repository, choose **Edit test rules**, **Create rule**.

1. Specify the following details for each test lifecycle policy rule.

   1. For **Rule priority**, type a number for the rule priority. The rule priority determines in what order the lifecycle policy rules are applied. A lower number means higher priority. For example, a rule with priority 1 takes precedence over a rule with priority 2.

   1. For **Rule description**, type a description for the lifecycle policy rule.

   1. For **Image status**, choose **Tagged (wildcard matching)**, **Tagged (prefix matching)**, **Untagged**, or **Any**.
**Important**  
If you specify multiple tags, only the images with all specified tags are selected.

   1. If you chose **Tagged (wildcard matching)** for **Image status**, then for **Specify tags for wildcard matching**, you can specify a list of image tags with a wildcard (**\***) on which to take action with your lifecycle policy. For example, if your images are tagged as `prod`, `prod1`, `prod2`, and so on, you would specify `prod*` to take action on all of them. If you specify multiple tags, only the images with all specified tags are selected.
**Important**  
There is a maximum limit of four wildcards (`*`) per string. For example, `["*test*1*2*3", "test*1*2*3*"]` is valid but `["test*1*2*3*4*5*6"]` is invalid.

   1. If you chose **Tagged (prefix matching)** for **Image status**, then for **Specify tags for prefix matching**, you can specify a list of image tags on which to take action with your lifecycle policy.

   1. For **Match criteria**, choose **Days since image created**, **Days since last recorded pull time**, **Days since image archived**, or **Image count** and then specify a value.

   1. For **Rule action**, choose either **Expire** or **Archive**.

   1. Choose **Save**.

1. Create additional test lifecycle policy rules by repeating steps 5–7.

1. To run the lifecycle policy preview, choose **Save and run test**.

1. Under **Image matches for test lifecycle rules**, review the impact of your lifecycle policy preview.

1. If you are satisfied with the preview results, choose **Apply as lifecycle policy** to create a lifecycle policy with the specified rules. You should expect that after applying a lifecycle policy, the affected images are expired or archived within 24 hours.

1. If you aren't satisfied with the preview results, you may delete one or more test lifecycle rules and create one or more rules to replace them and then repeat the test.

## Creating a lifecycle policy for a repository in Amazon ECR
<a name="lp_creation"></a>

 Use a lifecycle policy to create a set of rules that expire or archive unused repository images. After creating a lifecycle policy, the affected images are expired or archived within 24 hours.

**Note**  
If you are using Amazon ECR replication to make copies of a repository across different Regions or accounts, note that a lifecycle policy can only take an action on repositories in the Region it was created in. Therefore, if you have replication turned on you may want to create a lifecycle policy in each Region and account you are replicating your repositories to.

### Prerequisite
<a name="lp-creation-prerequisite"></a>

**Best practice:** Create a lifecycle policy preview to verify that the images expired or archived by your lifecycle policy rules are what you intend. For instructions, see [Creating a lifecycle policy preview in Amazon ECR](#lpp_creation).

### To create a lifecycle policy (AWS Management Console)
<a name="lp-creation-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository for which to create a lifecycle policy.

1. In the navigation pane, under **Private registry**, choose **Repositories**.

1. On the **Private repositories** page, select a repository and that use the **Actions** drop down to choose **Lifecycle policies**.

1. On the lifecycle policy rules page for the repository, choose **Create rule**.

1. Enter the following details for your lifecycle policy rule.

   1. For **Rule priority**, type a number for the rule priority. The rule priority determines in what order the lifecycle policy rules are applied. A lower rule priority number means higher priority. For example, a rule with priority 1 takes precedence over a rule with priority 2.

   1. For **Rule description**, type a description for the lifecycle policy rule.

   1. For **Image status**, choose **Tagged (wildcard matching)**, **Tagged (prefix matching)**, **Untagged**, or **Any**.
**Important**  
If you specify multiple tags, only the images with all specified tags are selected.

   1. If you chose **Tagged (wildcard matching)** for **Image status**, then for **Specify tags for wildcard matching**, you can specify a list of image tags with a wildcard (**\***) on which to take action with your lifecycle policy. For example, if your images are tagged as `prod`, `prod1`, `prod2`, and so on, you would specify `prod*` to take action on all of them. If you specify multiple tags, only the images with all specified tags are selected.
**Important**  
There is a maximum limit of four wildcards (`*`) per string. For example, `["*test*1*2*3", "test*1*2*3*"]` is valid but `["test*1*2*3*4*5*6"]` is invalid.

   1. If you chose **Tagged (prefix matching)**for **Image status**, then for **Specify tags for prefix matching**, you can specify a list of image tags on which to take action with your lifecycle policy.

   1. For **Match criteria**, choose **Days since image created**, **Days since last recorded pull time**, **Days since image archived**, or **Image count** and then specify a value.

   1. For **Rule action**, choose either **Expire** or **Archive**.

   1. Choose **Save**.

1. Create additional lifecycle policy rules by repeating steps 5–7.

### To create a lifecycle policy (AWS CLI)
<a name="lp-creation-cli"></a>

1. Obtain the name of the repository for which to create the lifecycle policy.

   ```
   aws ecr describe-repositories
   ```

1. Create a local file named `policy.json` with the contents of the lifecycle policy. For lifecycle policy examples, see [Examples of lifecycle policies in Amazon ECR](#lifecycle_policy_examples).

1. Create a lifecycle policy by specifying the repository name and reference the lifecycle policy JSON file you created.

   ```
   aws ecr put-lifecycle-policy \
         --repository-name {{repository-name}} \
         --lifecycle-policy-text file://{{policy.json}}
   ```

## Examples of lifecycle policies in Amazon ECR
<a name="lifecycle_policy_examples"></a>

The following are example lifecycle policies showing the syntax.

To see more information about policy properties, see [Lifecycle policy properties in Amazon ECR](#lifecycle_policy_parameters). For instructions about creating a lifecycle policy by using the AWS CLI, see [To create a lifecycle policy (AWS CLI)](#lp-creation-cli).

### Lifecycle policy template
<a name="lifecycle_policy_syntax"></a>

The contents of your lifecycle policy are evaluated before being associated with a repository. The following is the JSON syntax template for the lifecycle policy.

```
{
        "rules": [
            {
                "rulePriority": {{integer}},
                "description": "{{string}}",
                "selection": {
                    "tagStatus": "{{tagged}}"|"{{untagged}}"|"{{any}}",
                    "tagPatternList": {{list<string>}},
                    "tagPrefixList": {{list<string>}},
                    "storageClass": "{{standard}}"|"{{archive}}",
                    "countType": "{{imageCountMoreThan}}"|"{{sinceImagePushed}}"|"{{sinceImagePulled}}"|"{{sinceImageTransitioned}}",
                    "countUnit": "{{string}}",
                    "countNumber": {{integer}}
                },
                "action": {
                    "type": "{{expire}}"|"{{transition}}",
                    "targetStorageClass": "{{archive}}"
                }
            }
        ]
    }
```

### Filtering on image age
<a name="lifecycle_policy_example_age"></a>

The following example shows the lifecycle policy syntax for a policy that expires images with a tag starting with `prod` by using a `tagPatternList` of `prod*` that are also older than `14` days.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Expire images older than 14 days",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 14
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

### Filtering on last pulled time
<a name="lifecycle_policy_example_last_pulled"></a>

The following example shows the lifecycle policy syntax for a policy that transitions images to archive storage that haven't been pulled in `90` days.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive images not pulled in 90 days",
            "selection": {
                "tagStatus": "any",
                "countType": "sinceImagePulled",
                "countUnit": "days",
                "countNumber": 90
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        }
    ]
}
```

**Important**  
The `sinceImagePulled` count type must be used with the `transition` action. It cannot be used with the `expire` action. To delete images based on pull activity, first transition them to archive storage using `sinceImagePulled`, then use `sinceImageTransitioned` with an `expire` action to delete them. Images must be in archive storage for a minimum of 90 days before deletion.

### Filtering on archive transition time
<a name="lifecycle_policy_example_transitioned"></a>

The following example shows the lifecycle policy syntax for a policy that expires archived images that have been in archive storage for more than `365` days.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Expire images archived for more than 365 days",
            "selection": {
                "tagStatus": "any",
                "storageClass": "archive",
                "countType": "sinceImageTransitioned",
                "countUnit": "days",
                "countNumber": 365
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

**Important**  
The `sinceImageTransitioned` count type must be used with the `expire` action and the `archive` storage class. Images must be in archive storage for a minimum of 90 days before deletion.

### Filtering on image count
<a name="lifecycle_policy_example_number"></a>

The following example shows the lifecycle policy syntax for a policy that keeps only one untagged image and expires all others.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Keep only one untagged image, expire all others",
            "selection": {
                "tagStatus": "untagged",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

### Filtering on multiple rules
<a name="lp_example_multiple"></a>

The following examples use multiple rules in a lifecycle policy. An example repository and lifecycle policy are given along with an explanation of the outcome.

#### Example A
<a name="lp_example_multiple_a"></a>

Repository contents:
+ Image A, Taglist: ["beta-1", "prod-1"], Pushed: 10 days ago
+ Image B, Taglist: ["beta-2", "prod-2"], Pushed: 9 days ago
+ Image C, Taglist: ["beta-3"], Pushed: 8 days ago

Lifecycle policy text:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 2,
            "description": "Rule 2",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["beta*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:
+ Rule 1 identifies images tagged with prefix `prod`. It should mark images, starting with the oldest, until there is one or fewer images remaining that match. It marks Image A for expiration.
+ Rule 2 identifies images tagged with prefix `beta`. It should mark images, starting with the oldest, until there is one or fewer images remaining that match. It marks both Image A and Image B for expiration. However, Image A has already been seen by Rule 1 and if Image B were expired it would violate Rule 1 and thus is skipped.
+ Result: Image A is expired.

#### Example B
<a name="lp_example_multiple_b"></a>

This is the same repository as the previous example but the rule priority order is changed to illustrate the outcome.

Repository contents:
+ Image A, Taglist: ["beta-1", "prod-1"], Pushed: 10 days ago
+ Image B, Taglist: ["beta-2", "prod-2"], Pushed: 9 days ago
+ Image C, Taglist: ["beta-3"], Pushed: 8 days ago

Lifecycle policy text:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["beta*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 2,
            "description": "Rule 2",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:
+ Rule 1 identifies images tagged with prefix `beta`. It should mark images, starting with the oldest, until there is one or fewer images remaining that match. It sees all three images and would mark Image A and Image B for expiration.
+ Rule 2 identifies images tagged with prefix `prod`. It should mark images, starting with the oldest, until there is one or fewer images remaining that match. It would see no images because all available images were already seen by Rule 1 and thus would mark no additional images.
+ Result: Images A and B are expired.

### Filtering on multiple tags in a single rule
<a name="lp_example_difftype"></a>

The following examples specify the lifecycle policy syntax for multiple tag patterns in a single rule. An example repository and lifecycle policy are given along with an explanation of the outcome.

#### Example A
<a name="lp_example_difftype_a"></a>

When multiple tag patterns are specified on a single rule, images must match all listed tag patterns.

Repository contents:
+ Image A, Taglist: ["alpha-1"], Pushed: 12 days ago
+ Image B, Taglist: ["beta-1"], Pushed: 11 days ago
+ Image C, Taglist: ["alpha-2", "beta-2"], Pushed: 10 days ago
+ Image D, Taglist: ["alpha-3"], Pushed: 4 days ago
+ Image E, Taglist: ["beta-3"], Pushed: 3 days ago
+ Image F, Taglist: ["alpha-4", "beta-4"], Pushed: 2 days ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["alpha*", "beta*"],
                "countType": "sinceImagePushed",
                "countNumber": 5,
                "countUnit": "days"
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:
+ Rule 1 identifies images tagged with prefix `alpha` and `beta`. It sees images C and F. It should mark images that are older than five days, which would be Image C.
+ Result: Image C is expired.

#### Example B
<a name="lp_example_difftype_b"></a>

The following example illustrates that tags are not exclusive.

Repository contents:
+ Image A, Taglist: ["alpha-1", "beta-1", "gamma-1"], Pushed: 10 days ago
+ Image B, Taglist: ["alpha-2", "beta-2"], Pushed: 9 days ago
+ Image C, Taglist: ["alpha-3", "beta-3", "gamma-2"], Pushed: 8 days ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["alpha*", "beta*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:
+ Rule 1 identifies images tagged with prefix `alpha` and `beta`. It sees all images. It should mark images, starting with the oldest, until there is one or fewer images remaining that match. It marks image A and B for expiration.
+ Result: Images A and B are expired.

### Filtering on all images
<a name="lp_example_allimages"></a>

The following lifecycle policy examples specify all images with different filters. An example repository and lifecycle policy are given along with an explanation of the outcome.

#### Example A
<a name="lp_example_difftype_a"></a>

The following shows the lifecycle policy syntax for a policy that applies to all rules but keeps only one image and expires all others.

Repository contents:
+ Image A, Taglist: ["alpha-1"], Pushed: 4 days ago
+ Image B, Taglist: ["beta-1"], Pushed: 3 days ago
+ Image C, Taglist: [], Pushed: 2 days ago
+ Image D, Taglist: ["alpha-2"], Pushed: 1 day ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "any",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:
+ Rule 1 identifies all images. It sees images A, B, C, and D. It should expire all images other than the newest one. It marks images A, B, and C for expiration.
+ Result: Images A, B, and C are expired.

#### Example B
<a name="lp_example_difftype_b"></a>

The following example illustrates a lifecycle policy that combines all the rule types in a single policy.

Repository contents:
+ Image A, Taglist: ["alpha-1", "beta-1"], Pushed: 4 days ago
+ Image B, Taglist: [], Pushed: 3 days ago
+ Image C, Taglist: ["alpha-2"], Pushed: 2 days ago
+ Image D, Taglist: ["git hash"], Pushed: 1 day ago
+ Image E, Taglist: [], Pushed: 1 day ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["alpha*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 2,
            "description": "Rule 2",
            "selection": {
                "tagStatus": "untagged",
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 3,
            "description": "Rule 3",
            "selection": {
                "tagStatus": "any",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:
+ Rule 1 identifies images tagged with prefix `alpha`. It identifies images A and C. It should keep the newest image and mark the rest for expiration. It marks image A for expiration.
+ Rule 2 identifies untagged images. It identifies images B and E. It should mark all images older than one day for expiration. It marks image B for expiration.
+ Rule 3 identifies all images. It identifies images A, B, C, D, and E. It should keep the newest image and mark the rest for expiration. However, it can't mark images A, B, C, or E because they were identified by higher priority rules. It marks image D for expiration. 
+ Result: Images A, B, and D are expired.

### Archive examples
<a name="lp_example_archive"></a>

The following examples show lifecycle policies that archive images instead of deleting them.

#### Archiving images older than a specified number of days
<a name="lp_example_archive_age"></a>

The following example shows a lifecycle policy that archives images with tags starting with `prod` that are older than 30 days:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive production images older than 30 days",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 30
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        }
    ]
}
```

#### Archiving images not pulled in a specified number of days
<a name="lp_example_archive_pull"></a>

The following example shows a lifecycle policy that archives images that haven't been pulled in 90 days:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive images not pulled in 90 days",
            "selection": {
                "tagStatus": "any",
                "countType": "sinceImagePulled",
                "countUnit": "days",
                "countNumber": 90
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        }
    ]
}
```

#### Combining archive and expire rules
<a name="lp_example_archive_delete"></a>

The following example shows a lifecycle policy that archives images older than 30 days and then permanently expires images that have been archived for more than 365 days:

**Note**  
Archived images have a minimum storage duration of 90 days. You cannot configure lifecycle policies that delete images that have been in archive for less than 90 days. If you must delete images that have been archived for less than 90 days, you need to use the **batch-delete-image** API, but you will be charged for the 90-day minimum storage duration.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive images older than 30 days",
            "selection": {
                "tagStatus": "any",
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 30
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        },
        {
            "rulePriority": 2,
            "description": "Expire images archived for more than 365 days",
            "selection": {
                "tagStatus": "any",
                "storageClass": "archive",
                "countType": "sinceImageTransitioned",
                "countUnit": "days",
                "countNumber": 365
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

## Lifecycle policy properties in Amazon ECR
<a name="lifecycle_policy_parameters"></a>

Lifecycle policies have the following properties. 

To see examples of lifecycle policies, see [Examples of lifecycle policies in Amazon ECR](#lifecycle_policy_examples). For instructions about creating a lifecycle policy by using the AWS CLI, see [To create a lifecycle policy (AWS CLI)](#lp-creation-cli).

### Rule priority
<a name="lp_rule_priority"></a>

`rulePriority`  
Type: integer  
Required: yes  
Sets the order in which rules are applied, lowest to highest. A lifecycle policy rule with a priority of `1` is applied first, a rule with priority of `2` is next, and so on. When you add rules to a lifecycle policy, you must give them each a unique value for `rulePriority`. Values don't need to be sequential across rules in a policy. A rule with a `tagStatus` value of `any` must have the highest value for `rulePriority` and be evaluated last.

### Description
<a name="lp_description"></a>

`description`  
Type: string  
Required: no  
(Optional) Describes the purpose of a rule within a lifecycle policy.

### Tag status
<a name="lp_tag_status"></a>

`tagStatus`  
Type: string  
Required: yes  
Determines whether the lifecycle policy rule that you are adding specifies a tag for an image. Acceptable options are `tagged`, `untagged`, or `any`. If you specify `any`, then all images have the rule evaluated against them. If you specify `tagged`, then you must also specify a `tagPrefixList` value or a `tagPatternList` value. If you specify `untagged`, then you must omit both `tagPrefixList` and `tagPatternList`.

### Tag pattern list
<a name="lp_tag_pattern_list"></a>

`tagPatternList`  
Type: list[string]  
Required: yes, if `tagStatus` is set to tagged and `tagPrefixList` isn't specified  
When creating a lifecycle policy for tagged images, it's best practice to use a `tagPatternList` to specify the tags to expire. You specify a comma-separated list of image tag patterns that may contain wildcards (`*`) on which to take action with your lifecycle policy. For example, if your images are tagged as `prod`, `prod1`, `prod2`, and so on, you would use the tag pattern list `prod*` to specify all of them. If you specify multiple tags, only the images with all specified tags are selected.  
There is a maximum limit of four wildcards (`*`) per string. For example, `["*test*1*2*3", "test*1*2*3*"]` is valid but `["test*1*2*3*4*5*6"]` is invalid.

### Tag prefix list
<a name="lp_tag_prefix_list"></a>

`tagPrefixList`  
Type: list[string]  
Required: yes, if `tagStatus` is set to tagged and `tagPatternList` isn't specified  
Only used if you specified `"tagStatus": "tagged"` and you aren't specifying a `tagPatternList`. You must specify a comma-separated list of image tag prefixes on which to take action with your lifecycle policy. For example, if your images are tagged as `prod`, `prod1`, `prod2`, and so on, you would use the tag prefix `prod` to specify all of them. If you specify multiple tags, only the images with all specified tags are selected.

### Storage class
<a name="lp_storage_class"></a>

`storageClass`  
Type: string  
Required: yes, if `countType` is `sinceImageTransitioned`  
The rule will only select images of this storage class. When using a `countType` of `imageCountMoreThan`, `sinceImagePushed`, or `sinceImagePulled`, the only supported value is `standard`. When using a count type of `sinceImageTransitioned`, this is required, and the only supported value is `archive`. If you omit this, the value of `standard` will be used.

### Count type
<a name="lp_count_type"></a>

`countType`  
Type: string  
Required: yes  
Specify a count type to apply to the images.   
If `countType` is set to `imageCountMoreThan`, you also specify `countNumber` to create a rule that sets a limit on the number of images that exist in your repository. If `countType` is set to `sinceImagePushed`, `sinceImagePulled`, or `sinceImageTransitioned`, you also specify `countUnit` and `countNumber` to specify a time limit on the images that exist in your repository.

### Count unit
<a name="lp_count_unit"></a>

`countUnit`  
Type: string  
Required: yes, only if `countType` is set to `sinceImagePushed`, `sinceImagePulled`, or `sinceImageTransitioned`  
Specify a count unit of `days` to indicate that as the unit of time, in addition to `countNumber`, which is the number of days.   
This should only be specified when `countType` is `sinceImagePushed`, `sinceImagePulled`, or `sinceImageTransitioned`; an error will occur if you specify a count unit when `countType` is any other value.

### Count number
<a name="lp_count_number"></a>

`countNumber`  
Type: integer  
Required: yes  
Specify a count number. Acceptable values are positive integers (`0` is not an accepted value).   
If the `countType` used is `imageCountMoreThan`, then the value is the maximum number of images that you want to retain in your repository. If the `countType` used is `sinceImagePushed`, then the value is the maximum age limit for your images. If the `countType` used is `sinceImagePulled`, then the value is the maximum number of days since the image was last pulled. If the `countType` used is `sinceImageTransitioned`, then the value is the maximum number of days since the image was archived.

### Action
<a name="lp_action"></a>

`type`  
Type: string  
Required: yes  
Specify an action type. The supported values are `expire` (to delete images) and `transition` (to move images to archive storage).

`targetStorageClass`  
Type: string  
Required: yes, if `type` is `transition`  
The storage class you want the lifecycle policy to transition the image to. `archive` is the only supported value.

# Pull-time update exclusions
<a name="pull-time-update-exclusions"></a>

Amazon ECR updates the `LastRecordedPullTime` timestamp on every pull except for pulls by AWS Inspector. Pull-time update exclusions allow you to specify IAM role ARNs that should not update image pull times when they pull images, such as pulls by third-party scanners (such as Crowdstrike, Snyk, and Trivy). This is useful for images that are used for testing or CI/CD purposes where you don't want the pull time to affect lifecycle policy decisions.

When a role in the exclusion list pulls an image, the pull time remains unchanged. Any other role continues to update pull time (current behavior). You can configure up to 100 exclusions per account.

## Managing pull-time update exclusions
<a name="pull-time-update-exclusions-manage"></a>

To manage pull-time update exclusions, you need the following IAM permissions:
+ `ecr:CreatePullTimeUpdateExclusion` – Grants permission to add a role ARN to the exclusion list.
+ `ecr:DeletePullTimeUpdateExclusion` – Grants permission to remove a role ARN from the exclusion list.
+ `ecr:ListPullTimeUpdateExclusions` – Grants permission to list all role ARNs in the exclusion list.

**Note**  
You don't need `iam:PassRole` permission. Amazon ECR doesn't assume the role to perform an action; it only uses the exclusion configuration ARNs to determine if the pull time of the image should be updated.

You can manage pull-time update exclusions using the Amazon ECR console or the AWS CLI.

------
#### [ AWS Management Console ]

**To manage pull-time update exclusions (AWS Management Console)**

1. Open the Amazon ECR console at [ https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories)

1. From the navigation bar, choose the Region.

1. In the navigation pane, choose **Private registry**, **Features & Settings**, and then choose **Pull-time update exclusions**.

1. To add an exclusion, choose **Add exclusion**, enter the role ARN, and then choose **Add**.

1. To remove an exclusion, select the role ARN from the list and choose **Delete**.

1. To view all exclusions, the list displays all configured role ARNs.

------
#### [ AWS CLI ]

**To create a pull-time update exclusion**
+ Use the **create-pull-time-update-exclusion** command to add a role ARN to the exclusion list:

  ```
  aws ecr create-pull-time-update-exclusion \
      --role-arn {{arn:aws:iam::123456789012:role/scanner-role}}
  ```

  The command returns the role ARN and creation timestamp:

  ```
  {
     "roleArn": "arn:aws:iam::123456789012:role/scanner-role",
     "createdAt": 1745531331.0
  }
  ```

**To delete a pull-time update exclusion**
+ Use the **delete-pull-time-update-exclusion** command to remove a role ARN from the exclusion list:

  ```
  aws ecr delete-pull-time-update-exclusion \
      --role-arn {{arn:aws:iam::123456789012:role/scanner-role}}
  ```

  The command returns the role ARN that was deleted:

  ```
  {
    "roleArn": "arn:aws:iam::123456789012:role/scanner-role"
  }
  ```

**To list pull-time update exclusions**

1. Use the **list-pull-time-update-exclusions** command to list all role ARNs in the exclusion list:

   ```
   aws ecr list-pull-time-update-exclusions
   ```

   If no exclusions are configured, the command returns an empty list:

   ```
   {
      "pullTimeUpdateExclusions": []
   }
   ```

   If exclusions are configured, the command returns the list of role ARNs:

   ```
   {
      "pullTimeUpdateExclusions": [
           "arn:aws:iam::123456789012:role/security-role"
       ]
   }
   ```

1. To paginate results, use the `--max-results` and `--next-token` parameters:

   ```
   aws ecr list-pull-time-update-exclusions \
       --max-results 4
   ```

   The command returns up to the specified number of results and a `nextToken` if more results are available:

   ```
   {
      "pullTimeUpdateExclusions": [
           "arn:aws:iam::123456789012:role/security-role1",
           "arn:aws:iam::123456789012:role/security-role2",
           "arn:aws:iam::123456789012:role/security-role3",
           "arn:aws:iam::123456789012:role/security-role4"
       ],
       "nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ79..."
   }
   ```

   To retrieve the next page of results, use the `nextToken` from the previous response:

   ```
   aws ecr list-pull-time-update-exclusions \
       --max-results 4 \
       --next-token {{ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ79...}}
   ```

------

## Considerations for pull-time update exclusions
<a name="pull-time-update-exclusions-considerations"></a>

Consider the following when using pull-time update exclusions:
+ The default page size for listing exclusions is 100. You can use pagination with `maxResults` and `nextToken` parameters.
+ Only valid IAM role ARNs in the correct ARN format are accepted.
+ If you try to create an exclusion that already exists, you'll receive an `ExclusionAlreadyExistsException` error. If you try to delete an exclusion that doesn't exist, you'll receive an `ExclusionNotFoundException` error.

# Security in Amazon Elastic Container Registry
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon ECR, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using Amazon ECR. The following topics show you how to configure Amazon ECR to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Amazon ECR resources. 

**Topics**
+ [Identity and Access Management for Amazon Elastic Container Registry](#security-iam)
+ [Data protection in Amazon ECR](#data-protection)
+ [Compliance validation for Amazon Elastic Container Registry](#ecr-compliance)
+ [Infrastructure Security in Amazon Elastic Container Registry](#infrastructure-security)
+ [Cross-service confused deputy prevention](#cross-service-confused-deputy-prevention)

## Identity and Access Management for Amazon Elastic Container Registry
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Amazon ECR resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [Audience](#security_iam_audience)
+ [Authenticating with identities](#security_iam_authentication)
+ [Managing access using policies](#security_iam_access-manage)
+ [How Amazon Elastic Container Registry works with IAM](#security_iam_service-with-iam)
+ [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples)
+ [Using Tag-Based Access Control](#ecr-supported-iam-actions-tagging)
+ [AWS managed policies for Amazon Elastic Container Registry](#security-iam-awsmanpol)
+ [Using service-linked roles for Amazon ECR](#using-service-linked-roles)
+ [Troubleshooting Amazon Elastic Container Registry Identity and Access](#security_iam_troubleshoot)

### Audience
<a name="security_iam_audience"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting Amazon Elastic Container Registry Identity and Access](#security_iam_troubleshoot))
+ **Service administrator** - determine user access and submit permission requests (see [How Amazon Elastic Container Registry works with IAM](#security_iam_service-with-iam))
+ **IAM administrator** - write policies to manage access (see [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples))

### Authenticating with identities
<a name="security_iam_authentication"></a>

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

#### AWS account root user
<a name="security_iam_authentication-rootuser"></a>

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*. 

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

### How Amazon Elastic Container Registry works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon ECR, you should understand what IAM features are available to use with Amazon ECR. To get a high-level view of how Amazon ECR and other AWS services work with IAM, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Amazon ECR Identity-based policies](#security_iam_service-with-iam-id-based-policies)
+ [Amazon ECR resource-based policies](#security_iam_service-with-iam-resource-based-policies)
+ [Authorization based on Amazon ECR tags](#security_iam_service-with-iam-tags)
+ [Amazon ECR IAM roles](#security_iam_service-with-iam-roles)

#### Amazon ECR Identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. Amazon ECR supports specific actions, resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

##### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon ECR use the following prefix before the action: `ecr:`. For example, to grant someone permission to create an Amazon ECR repository with the Amazon ECR `CreateRepository` API operation, you include the `ecr:CreateRepository` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Amazon ECR defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "ecr:action1",
      "ecr:action2"
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "ecr:Describe*"
```



To see a list of Amazon ECR actions, see [Actions, Resources, and Condition Keys for Amazon Elastic Container Registry](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticcontainerregistry.html) in the *IAM User Guide*.

##### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```



An Amazon ECR repository resource has the following ARN:

```
arn:${Partition}:ecr:${Region}:${Account}:repository/${Repository-name}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `my-repo` repository in the `us-east-1` Region in your statement, use the following ARN:

```
"Resource": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/my-repo"
```

To specify all repositories that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/*"
```

To specify multiple resources in a single statement, separate the ARNs with commas. 

```
"Resource": [
      "resource1",
      "resource2"
```

To see a list of Amazon ECR resource types and their ARNs, see [Resources Defined by Amazon Elastic Container Registry](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticcontainerregistry.html#amazonelasticcontainerregistry-resources-for-iam-policies) in the *IAM User Guide*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by Amazon Elastic Container Registry](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticcontainerregistry.html#amazonelasticcontainerregistry-actions-as-permissions).

##### Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Amazon ECR defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.



Most Amazon ECR actions support the `aws:ResourceTag` and `ecr:ResourceTag` condition keys. For more information, see [Using Tag-Based Access Control](#ecr-supported-iam-actions-tagging).

To see a list of Amazon ECR condition keys, see [Condition Keys Defined by Amazon Elastic Container Registry](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticcontainerregistry.html#amazonelasticcontainerregistry-policy-keys) in the *IAM User Guide*. To learn with which actions and resources you can use a condition key, see [Actions Defined by Amazon Elastic Container Registry](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticcontainerregistry.html#amazonelasticcontainerregistry-actions-as-permissions).

##### Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Amazon ECR identity-based policies, see [Amazon Elastic Container Registry Identity-based policy examples](#security_iam_id-based-policy-examples).

#### Amazon ECR resource-based policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Resource-based policies are JSON policy documents that specify what actions a specified principal can perform on an Amazon ECR resource and under what conditions. Amazon ECR supports resource-based permissions policies for Amazon ECR repositories. Resource-based policies let you grant usage permission to other accounts on a per-resource basis. You can also use a resource-based policy to allow an AWS service to access your Amazon ECR repositories.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the [principal in a resource-based policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html). Adding a cross-account principal to a resource-based policy is only half of establishing the trust relationship. When the principal and the resource are in different AWS accounts, you must also grant the principal entity permission to access the resource. Grant permission by attaching an identity-based policy to the entity. However, if a resource-based policy grants access to a principal in the same account, you don't need additional Amazon ECR repository permissions in the identity-based policy. For more information, see [How IAM Roles Differ from Resource-based Policies ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html)in the *IAM User Guide*.

The Amazon ECR service supports only one type of resource-based policy called a *repository policy*, which is attached to a *repository*. This policy defines which principal entities (accounts, users, roles, and federated users) can perform actions on the repository. To learn how to attach a resource-based policy to a repository, see [Private repository policies in Amazon ECR](#repository-policies).

**Note**  
In an Amazon ECR repository policy, the policy element `Sid` supports additional characters and spacing not supported in IAM policies.

##### Examples
<a name="security_iam_service-with-iam-resource-based-policies-examples"></a>



To view examples of Amazon ECR resource-based policies, see [Private repository policy examples in Amazon ECR](#repository-policy-examples),

#### Authorization based on Amazon ECR tags
<a name="security_iam_service-with-iam-tags"></a>

You can attach tags to Amazon ECR resources or pass tags in a request to Amazon ECR. To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `ecr:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. For more information about tagging Amazon ECR resources, see [Tagging a private repository in Amazon ECR](#ecr-using-tags).

To view an example identity-based policy for limiting access to a resource based on the tags on that resource, see [Using Tag-Based Access Control](#ecr-supported-iam-actions-tagging).

#### Amazon ECR IAM roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

##### Using Temporary Credentials with Amazon ECR
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html). 

Amazon ECR supports using temporary credentials. 

##### Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view but not edit the permissions for service-linked roles.

Amazon ECR supports service-linked roles. For more information, see [Using service-linked roles for Amazon ECR](#using-service-linked-roles).

### Amazon Elastic Container Registry Identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify Amazon ECR resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Amazon ECR, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Elastic Container Registry](https://docs.aws.amazon.com/service-authorization/latest/reference/ecr.html) in the *Service Authorization Reference*.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy Best Practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the Amazon ECR console](#security_iam_id-based-policy-examples-console)
+ [Allow Users to View Their Own Permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Accessing One Amazon ECR Repository](#security_iam_id-based-policy-examples-access-one-bucket)

#### Policy Best Practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Amazon ECR resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

#### Using the Amazon ECR console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the Amazon Elastic Container Registry console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Amazon ECR resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

To ensure that those entities can still use the Amazon ECR console, add the `AmazonEC2ContainerRegistryReadOnly` AWS managed policy to the entities. For more information, see [Adding Permissions to a User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*:

To view the permissions for this policy, see [AmazonElasticContainerRegistryPublicReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicReadOnly.html) in the *AWS Managed Policy Reference*.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that you're trying to perform.

#### Allow Users to View Their Own Permissions
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

#### Accessing One Amazon ECR Repository
<a name="security_iam_id-based-policy-examples-access-one-bucket"></a>

In this example, you want to grant a user in your AWS account access to one of your Amazon ECR repositories, `my-repo`. You also want to allow the user to push, pull, and list images.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"GetAuthorizationToken",
         "Effect":"Allow",
         "Action":[
            "ecr:GetAuthorizationToken"
         ],
         "Resource":"*"
      },
      {
         "Sid":"ManageRepositoryContents",
         "Effect":"Allow",
         "Action":[
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetRepositoryPolicy",
                "ecr:DescribeRepositories",
                "ecr:ListImages",
                "ecr:DescribeImages",
                "ecr:BatchGetImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:PutImage"
         ],
         "Resource":"arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/{{my-repo}}"
      }
   ]
}
```

------

### Using Tag-Based Access Control
<a name="ecr-supported-iam-actions-tagging"></a>

The Amazon ECR `CreateRepository` API action enables you to specify tags when you create the repository. For more information, see [Tagging a private repository in Amazon ECR](#ecr-using-tags).

To enable users to tag repositories on creation, they must have permissions to use the action that creates the resource (for example, `ecr:CreateRepository`). If tags are specified in the resource-creating action, Amazon performs additional authorization on the `ecr:CreateRepository` action to verify if users have permissions to create tags.

You can use tag-based access control through IAM policies. The following are examples.

The following policy would only allow a user to create or tag a repository as `key=environment,value=dev`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCreateTaggedRepository",
            "Effect": "Allow",
            "Action": [
                "ecr:CreateRepository"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/environment": "dev"
                }
            }
        },
        {
            "Sid": "AllowTagRepository",
            "Effect": "Allow",
            "Action": [
                "ecr:TagResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/environment": "dev"
                }
            }
        }
    ]
}
```

------

The following policy would allow a user to pull images from all repositories unless they were tagged as `key=environment,value=prod`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ecr:ResourceTag/environment": "prod"
                }
            }
        }
    ]
}
```

------

### AWS managed policies for Amazon Elastic Container Registry
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

Amazon ECR provides several managed policies that you can attach to IAM identities or to Amazon EC2 instances. These managed policies allow differing levels of control over access to Amazon ECR resources and API operations. For more information about each API operation mentioned in these policies, see [Actions](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Operations.html) in the *Amazon Elastic Container Registry API Reference*.

**Topics**
+ [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess)
+ [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser)
+ [AmazonEC2ContainerRegistryPullOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly)
+ [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly)
+ [`AWSECRPullThroughCache_ServiceRolePolicy`](#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy)
+ [`ECRReplicationServiceRolePolicy`](#security-iam-awsmanpol-ECRReplicationServiceRolePolicy)
+ [`ECRTemplateServiceRolePolicy`](#security-iam-awsmanpol-ECRTemplateServiceRolePolicy)
+ [Amazon ECR updates to AWS managed policies](#security-iam-awsmanpol-updates)

#### AmazonEC2ContainerRegistryFullAccess
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess"></a>

You can attach the `AmazonEC2ContainerRegistryFullAccess` policy to your IAM identities. This policy grants administrative access to Amazon ECR resources and grants an IAM identity (such as a user, group, or role) access to the AWS services that Amazon ECR is integrated with to use all of Amazon ECR features. Using this policy allows access to all of Amazon ECR features that are available in the AWS Management Console.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryFullAccess.html) in the *AWS Managed Policy Reference*.

#### AmazonEC2ContainerRegistryPowerUser
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser"></a>

You can attach the `AmazonEC2ContainerRegistryPowerUser` policy to your IAM identities. This policy grants administrative permissions that allow IAM users to read and write to repositories, but doesn't allow them to delete repositories or change the policy documents that are applied to them.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryPowerUser](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPowerUser.html) in the *AWS Managed Policy Reference*.

#### AmazonEC2ContainerRegistryPullOnly
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly"></a>

You can attach the `AmazonEC2ContainerRegistryPullOnly` policy to your IAM identities. This policy grants permission to pull container images from Amazon ECR. If the registry is enabled for pull-through cache, it will also allow pulls to import an image from an upstream registry.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryPullOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPullOnly.html) in the *AWS Managed Policy Reference*.

#### AmazonEC2ContainerRegistryReadOnly
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly"></a>

You can attach the `AmazonEC2ContainerRegistryReadOnly` policy to your IAM identities. This policy grants read-only permissions to Amazon ECR. This includes the ability to list repositories and images within the repositories. It also includes the ability to pull images from Amazon ECR with the Docker CLI.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.html) in the *AWS Managed Policy Reference*.

#### `AWSECRPullThroughCache_ServiceRolePolicy`
<a name="security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy"></a>

You can't attach the `AWSECRPullThroughCache_ServiceRolePolicy` managed IAM policy to your IAM entities. This policy is attached to a service-linked role that allows Amazon ECR to push images to your repositories through the pull through cache workflow. For more information, see [Amazon ECR service-linked role for pull through cache](#slr-pullthroughcache).

#### `ECRReplicationServiceRolePolicy`
<a name="security-iam-awsmanpol-ECRReplicationServiceRolePolicy"></a>

You can't attach the `ECRReplicationServiceRolePolicy` managed IAM policy to your IAM entities. This policy is attached to a service-linked role that allows Amazon ECR to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon ECR](#using-service-linked-roles).

#### `ECRTemplateServiceRolePolicy`
<a name="security-iam-awsmanpol-ECRTemplateServiceRolePolicy"></a>

You can't attach the `ECRTemplateServiceRolePolicy` managed IAM policy to your IAM entities. This policy is attached to a service-linked role that allows Amazon ECR to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon ECR](#using-service-linked-roles).

#### Amazon ECR updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon ECR since the time that this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon ECR Document history page.

 


| Change | Description | Date | 
| --- | --- | --- | 
| [Amazon ECR service-linked role for pull through cache](#slr-pullthroughcache) – Update to an existing policy | Amazon ECR added new permissions to the `AWSECRPullThroughCache_ServiceRolePolicy` policy. These permissions allow Amazon ECR to pull images from ECR private registry. This is required when using a pull through cache rule to cache images from another Amazon ECR private registry.  | March 12, 2025 | 
| [AmazonEC2ContainerRegistryPullOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly) – New policy | Amazon ECR added a new policy which grants pull-only permissions to Amazon ECR. | October 10, 2024 | 
| [ECRTemplateServiceRolePolicy](#slr-rct) – New policy | Amazon ECR added a new policy. This policy is associated with the `ECRTemplateServiceRolePolicy` service-linked role for the repository creation template feature. | June 20, 2024 | 
| [AWSECRPullThroughCache\_ServiceRolePolicy](#slr-pullthroughcache) – Update to an existing policy | Amazon ECR added new permissions to the `AWSECRPullThroughCache_ServiceRolePolicy` policy. These permissions allow Amazon ECR to retrieve the encrypted contents of a Secrets Manager secret. This is required when using a pull through cache rule to cache images from an upstream registry that requires authentication. | November 15, 2023 | 
| [AWSECRPullThroughCache\_ServiceRolePolicy](#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy) – New policy | Amazon ECR added a new policy. This policy is associated with the `AWSServiceRoleForECRPullThroughCache` service-linked role for the pull through cache feature. | November 29, 2021 | 
| [ECRReplicationServiceRolePolicy](#security-iam-awsmanpol-ECRReplicationServiceRolePolicy) – New policy | Amazon ECR added a new policy. This policy is associated with the `AWSServiceRoleForECRReplication` service-linked role for the replication feature. | December 4, 2020 | 
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryFullAccess` policy. These permissions allow principals to create the Amazon ECR service-linked role. | December 4, 2020 | 
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryReadOnly` policy which allow principals to read lifecycle policies, list tags, and describe the scan findings for images. | December 10, 2019 | 
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryPowerUser` policy. They allow principals to read lifecycle policies, list tags, and describe the scan findings for images. | December 10, 2019 | 
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryFullAccess` policy. They allow principals to look up management events or AWS CloudTrail Insights events that are captured by CloudTrail. | November 10, 2017 | 
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryReadOnly` policy. They allow principals to describe Amazon ECR images. | October 11, 2016 | 
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryPowerUser` policy. They allow principals to describe Amazon ECR images. | October 11, 2016 | 
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly) – New policy | Amazon ECR added a new policy which grants read-only permissions to Amazon ECR. These permissions include the ability to list repositories and images within the repositories. They also include the ability to pull images from Amazon ECR with the Docker CLI. | December 21, 2015 | 
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser) – New policy | Amazon ECR added a new policy which grants administrative permissions that allow users to read and write to repositories but doesn't allow them to delete repositories or change the policy documents that are applied to them. | December 21, 2015 | 
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess) – New policy | Amazon ECR added a new policy. This policy grants full access to Amazon ECR. | December 21, 2015 | 
| Amazon ECR started tracking changes | Amazon ECR started tracking changes for AWS managed policies. | June 24, 2021 | 

### Using service-linked roles for Amazon ECR
<a name="using-service-linked-roles"></a>

Amazon Elastic Container Registry (Amazon ECR) uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) to provide the permissions necessary to use the replication and pull through cache features. A service-linked role is a unique type of IAM role that is linked directly to Amazon ECR. The service-linked role is predefined by Amazon ECR. It includes all of the permissions that the service requires to support the replication and pull through cache features for your private registry. After you configure replication or pull through cache for your registry, a service-linked role is created automatically on your behalf. For more information, see [Private registry settings in Amazon ECR](#registry-settings).

A service-linked role makes setting up replication and pull through cache with Amazon ECR easier. This is because, by using it, you don’t have to manually add all the necessary permissions. Amazon ECR defines the permissions of its service-linked roles, and unless defined otherwise, only Amazon ECR can assume its roles. The defined permissions include the trust policy and the permissions policy. The permissions policy can't be attached to any other IAM entity.

You can delete the corresponding service-linked role only after disabling either replication or pull through cache on your registry. This ensures that you don't inadvertently remove the permissions Amazon ECR requires for these features.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). On this linked-to page, look for the services that have **Yes **in the **Service-linked role** column. Choose a **Yes** with a link to view the relevant service-linked role documentation for that service.

**Topics**
+ [Supported Regions for Amazon ECR service-linked roles](#slr-regions)
+ [Amazon ECR service-linked role for replication](#slr-replication)
+ [Amazon ECR service-linked role for pull through cache](#slr-pullthroughcache)
+ [Amazon ECR service-linked role for repository creation templates](#slr-rct)

#### Supported Regions for Amazon ECR service-linked roles
<a name="slr-regions"></a>

Amazon ECR supports using service-linked roles in all of the Regions where the Amazon ECR service is available. For more information about Amazon ECR Region availability, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).

#### Amazon ECR service-linked role for replication
<a name="slr-replication"></a>

Amazon ECR uses a service-linked role named **AWSServiceRoleForECRReplication** that allows Amazon ECR to replicate images across multiple accounts.

##### Service-linked role permissions for Amazon ECR
<a name="slr-permissions"></a>

The AWSServiceRoleForECRReplication service-linked role trusts the following services to assume the role:
+ `replication.ecr.amazonaws.com`

The following `ECRReplicationServiceRolePolicy` role permissions policy allows Amazon ECR to use the following actions on resources:

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
                "ecr:CreateRepository",
                "ecr:ReplicateImage"
            ],
            "Resource": "*"
        }
    ]
}
```

------

**Note**  
The `ReplicateImage` is an internal API that Amazon ECR uses for replication and can't be called directly.

You must configure permissions to allow an IAM entity (for example a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

##### Creating a service-linked role for Amazon ECR
<a name="create-slr"></a>

You don't need to manually create the Amazon ECR service-linked role. When you configure replication settings for your registry in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECR creates the service-linked role for you. 

If you delete this service-linked role and need to create it again, you can use the same process to recreate the role in your account. When you configure replication settings for your registry, Amazon ECR creates the service-linked role for you again. 

##### Editing a service-linked role for Amazon ECR
<a name="edit-slr"></a>

Amazon ECR doesn't allow manually editing the AWSServiceRoleForECRReplication service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

##### Deleting the service-linked role for Amazon ECR
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way, you don’t have an unused entity that isn't actively monitored or maintained. However, you must remove the replication configuration for your registry in every Region before you can manually delete the service-linked role.

**Note**  
If you try to delete resources while the Amazon ECR service is still using the roles, your delete action might fail. If that happens, wait for a few minutes and try again.

**To delete Amazon ECR resources used by the AWSServiceRoleForECRReplication**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region your replication configuration is set on.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, on the **Replication configuration** section, choose **Edit**.

1. To delete all of your replication rules, choose **Delete all**. This step requires confirmation.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForECRReplication** service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

#### Amazon ECR service-linked role for pull through cache
<a name="slr-pullthroughcache"></a>

Amazon ECR uses a service-linked role named **AWSServiceRoleForECRPullThroughCache** which gives permission for Amazon ECR to perform actions on your behalf to complete pull through cache actions. For more information about pull through cache, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates).

##### Service-linked role permissions for Amazon ECR
<a name="slr-pullthroughcache-permissions"></a>

The **AWSServiceRoleForECRPullThroughCache** service-linked role trusts the following service to assume the role.
+ `pullthroughcache.ecr.amazonaws.com`

**Permissions details**

The `AWSECRPullThroughCache_ServiceRolePolicy` permissions policy is attached to the service-linked role. This managed policy grants Amazon ECR permission to perform the following actions. For more information, see [`AWSECRPullThroughCache_ServiceRolePolicy`](#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy).
+ `ecr` – Allows the Amazon ECR service to pull and push images to a private repository.
+ `secretsmanager:GetSecretValue` – Allows the Amazon ECR service to retrieve the encrypted contents of an AWS Secrets Manager secret. This is required when using a pull through cache rule to cache images from an upstream registry that requires authentication in your private registry. This permission applies only to secrets with the `ecr-pullthroughcache/` name prefix.

The `AWSECRPullThroughCache_ServiceRolePolicy` policy contains the following JSON.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ECR",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:PutImage",
                "ecr:BatchGetImage",
                "ecr:BatchImportUpstreamImage",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetImageCopyStatus"
            ],
            "Resource": "*",
            "Condition": {
	            "StringEquals": {
	                "aws:ResourceAccount": "${aws:PrincipalAccount}"
	            }
	        }
        },
        {
            "Sid": "SecretsManager",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "arn:aws:secretsmanager:*:*:secret:ecr-pullthroughcache/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```

------

You must configure permissions to allow an IAM entity (for example a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

##### Creating a service-linked role for Amazon ECR
<a name="slr-pullthroughcache-create"></a>

You don't need to manually create the Amazon ECR service-linked role for pull through cache. When you create a pull through cache rule for your private registry in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECR creates the service-linked role for you. 

If you delete this service-linked role and need to create it again, you can use the same process to recreate the role in your account. When you create a pull through cache rule for your private registry, Amazon ECR creates the service-linked role for you again if it doesn't already exist.

##### Editing a service-linked role for Amazon ECR
<a name="slr-pullthroughcache-edit"></a>

Amazon ECR doesn't allow manually editing the **AWSServiceRoleForECRPullThroughCache** service-linked role. After the service-linked role is created, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

##### Deleting the service-linked role for Amazon ECR
<a name="slr-pullthroughcache-delete"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way, you don’t have an unused entity that isn't actively monitored or maintained. However, you must delete the pull through cache rules for your registry in every Region before you can manually delete the service-linked role.

**Note**  
If you try to delete resources while the Amazon ECR service is still using the role, your delete action might fail. If that happens, wait for a few minutes and try again.

**To delete Amazon ECR resources used by the **AWSServiceRoleForECRPullThroughCache** service-linked role**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region where your pull through cache rules are created.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, on the **Pull through cache configuration** section, choose **Edit**.

1. For each pull through cache rule you have created, select the rule and then choose **Delete rule**.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForECRPullThroughCache** service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

#### Amazon ECR service-linked role for repository creation templates
<a name="slr-rct"></a>

Amazon ECR uses a service-linked role named **AWSServiceRoleForECRTemplate** which gives permission for Amazon ECR to perform actions on your behalf to complete repository creation template actions.

##### Service-linked role permissions for Amazon ECR
<a name="slr-rct-permissions"></a>

The **AWSServiceRoleForECRTemplate** service-linked role trusts the following service to assume the role.
+ `ecr.amazonaws.com`

**Permissions details**

The ``ECRTemplateServiceRolePolicy`` permissions policy is attached to the service-linked role. This managed policy grants Amazon ECR permission to perform repository creation actions on your behalf.

The `ECRTemplateServiceRolePolicy` policy contains the following JSON.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
	    "Sid": "CreateRepositoryWithTemplate",
            "Effect": "Allow",
            "Action": [
                "ecr:CreateRepository"
            ],
            "Resource": "*"
        }
    ]
}
```

------

You must configure permissions to allow an IAM entity (for example a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

##### Creating a service-linked role for Amazon ECR
<a name="slr-rct-create"></a>

You don't need to manually create the Amazon ECR service-linked role for repository creation template. When you create a repository creation template rule for your private registry in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECR creates the service-linked role for you. 

If you delete this service-linked role and need to create it again, you can use the same process to recreate the role in your account. When you create a repository creation rule for your private registry, Amazon ECR creates the service-linked role for you again if it doesn't already exist.

##### Editing a service-linked role for Amazon ECR
<a name="slr-rct-edit"></a>

Amazon ECR doesn't allow manually editing the **AWSServiceRoleForECRTemplate** service-linked role. After the service-linked role is created, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

##### Deleting the service-linked role for Amazon ECR
<a name="slr-rct-delete"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way, you don’t have an unused entity that isn't actively monitored or maintained. However, you must delete the repository creation rules for your registry in every Region before you can manually delete the service-linked role.

**Note**  
If you try to delete resources while the Amazon ECR service is still using the role, your delete action might fail. If that happens, wait for a few minutes and try again.

**To delete Amazon ECR resources used by the **AWSServiceRoleForECRTemplate** service-linked role**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region where your repository creation rules are created.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, on the **Repository creation templates** section, choose **Edit**.

1. For each repository creation rule you have created, select the rule and then choose **Delete rule**.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForECRTemplate** service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

### Troubleshooting Amazon Elastic Container Registry Identity and Access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon ECR and IAM.

**Topics**
+ [I Am Not Authorized to Perform an Action in Amazon ECR](#security_iam_troubleshoot-no-permissions)
+ [I Am Not Authorized to Perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I want to allow people outside of my AWS account to access my Amazon ECR resources](#security_iam_troubleshoot-cross-account-access)

#### I Am Not Authorized to Perform an Action in Amazon ECR
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but doesn't have the fictional `ecr:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: ecr:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the `{{my-example-widget}}` resource by using the `ecr:{{GetWidget}}` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I Am Not Authorized to Perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Amazon ECR.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Amazon ECR. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I want to allow people outside of my AWS account to access my Amazon ECR resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Amazon ECR supports these features, see [How Amazon Elastic Container Registry works with IAM](#security_iam_service-with-iam).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Data protection in Amazon ECR
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Elastic Container Service. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon ECS or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

**Topics**
+ [Encryption at rest](#encryption-at-rest)

### Encryption at rest
<a name="encryption-at-rest"></a>

**Important**  
 Dual-layer server-side encryption with AWS KMS (DSSE-KMS) is only available in the AWS GovCloud (US) Regions.

Amazon ECR stores images in Amazon S3 buckets that Amazon ECR manages. By default, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part and is offered at no additional charge. For more information, see [Protecting Data Using Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) in the *Amazon Simple Storage Service User Guide*.

For more control over the encryption for your Amazon ECR repositories, you can use server-side encryption with KMS keys stored in AWS Key Management Service (AWS KMS). When you use AWS KMS to encrypt your data, you can either use the default AWS managed key, which is managed by Amazon ECR, or specify your own KMS key (referred to as a customer managed key). For more information, see [Protecting Data Using Server-Side Encryption with KMS keys Stored in AWS KMS (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service User Guide*.

 You can choose to apply two layers of encryption to your Amazon ECR images using dual-layer server-side encryption with AWS KMS (DSSE-KMS). DSSE-KMS option is similar to SSE-KMS, but applies two individual layers of encryption instead of one layer. For more information, see [Using dual-layer server-side encryption with AWS KMS keys (DSSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingDSSEncryption.html).

Each Amazon ECR repository has an encryption configuration, which is set when the repository is created. You can use different encryption configurations on each repository. For more information, see [Creating an Amazon ECR private repository to store images](#repository-create).

When a repository is created with AWS KMS encryption enabled, a KMS key is used to encrypt the contents of the repository. Moreover, Amazon ECR adds an AWS KMS grant to the KMS key with the Amazon ECR repository as the grantee principal.

The following provides a high-level understanding of how Amazon ECR is integrated with AWS KMS to encrypt and decrypt your repositories:

1. When creating a repository, Amazon ECR sends a [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) call to AWS KMS to validate and retrieve the Amazon Resource Name (ARN) of the KMS key specified in the encryption configuration.

1. Amazon ECR sends two [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) requests to AWS KMS to create grants on the KMS key to allow Amazon ECR to encrypt and decrypt data using the data key.

1. When pushing an image, a [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) request is made to AWS KMS that specifies the KMS key to use for encrypting the image layer and manifest.

1. AWS KMS generates a new data key, encrypts it under the specified KMS key, and sends the encrypted data key to be stored with the image layer metadata and the image manifest.

1. When pulling an image, a [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) request is made to AWS KMS, specifying the encrypted data key.

1. AWS KMS decrypts the encrypted data key and sends the decrypted data key to Amazon S3.

1. The data key is used to decrypt the image layer before the image layer being pulled.

1. When a repository is deleted, Amazon ECR sends two [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) requests to AWS KMS to retire the grants created for the repository.

#### Considerations
<a name="encryption-at-rest-considerations"></a>

The following points should be considered when using AWS KMS based encryption (SSE-KMS or DSSE-KMS) with Amazon ECR.
+ If you create your Amazon ECR repository with KMS encryption and you do not specify a KMS key, Amazon ECR uses an AWS managed key with the alias `aws/ecr` by default. This KMS key is created in your account the first time that you create a repository with KMS encryption enabled.
+  Repository Encryption Configuration can't be changed after a repository is created. 
+ When you use KMS encryption with your own KMS key, the key must exist in the same Region as your repository.
+ The grants that Amazon ECR creates on your behalf should not be revoked. If you revoke the grant that gives Amazon ECR permission to use the AWS KMS keys in your account, Amazon ECR cannot access this data, encrypt new images pushed to the repository, or decrypt them when they are pulled. When you revoke a grant for Amazon ECR, the change occurs immediately. To revoke access rights, you should delete the repository rather than revoking the grant. When a repository is deleted, Amazon ECR retires the grants on your behalf.
+ There is a cost associated with using AWS KMS keys. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).
+ There is a cost associated with using dual-layer server-side encryption. For more information, see [Amazon ECR pricing](https://aws.amazon.com/ecr/pricing/)

#### Required IAM permissions
<a name="encryption-at-rest-iam"></a>

When creating or deleting an Amazon ECR repository with server-side encryption using AWS KMS, the permissions required depend on the specific KMS key you are using. 

##### Required IAM permissions when using the AWS managed key for Amazon ECR
<a name="encryption-aws-managed-key"></a>

By default, when AWS KMS encryption is enabled for an Amazon ECR repository but no KMS key is specified, the AWS managed key for Amazon ECR is used. When the AWS-managed KMS key for Amazon ECR is used to encrypt a repository, any principal that has permission to create a repository can also enable AWS KMS encryption on the repository. However, the IAM principal that deletes the repository must have the `kms:RetireGrant` permission. This enables the retirement of the grants that were added to the AWS KMS key when the repository was created.

The following example IAM policy can be added as an inline policy to a user to ensure they have the minimum permissions needed to delete a repository that has encryption enabled. The KMS key used to encrypt the repository can be specified using the resource parameter.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "ecr-kms-permissions",
    "Statement": [
        {
            "Sid": "AllowAccessToRetireTheGrantsAssociatedWithTheKey",
            "Effect": "Allow",
            "Action": [
                "kms:RetireGrant"
            ],
            "Resource": "arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/{{b8d9ae76-080c-4043-92EXAMPLE}}"
        }
    ]
}
```

------

##### Required IAM permissions when using a customer managed key
<a name="encryption-customer-managed-key"></a>

When creating a repository with AWS KMS encryption enabled using a customer managed key, there are required permissions for both the KMS key policy and the IAM policy for the user or role creating the repository.

When creating your own KMS key, you can either use the default key policy AWS KMS creates or you can specify your own. To ensure that the customer managed key remains manageable by the account owner, the key policy for the KMS key should allow all AWS KMS actions for the root user of the account. Additional scoped permissions may be added to the key policy but at minimum the root user should be given permissions to manage the KMS key. To allow the KMS key to be used only for requests that originate in Amazon ECR, you can use the [kms:ViaService condition key](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) with the `ecr.{{<region>}}.amazonaws.com` value.

The following example key policy gives the AWS account (root user) that owns the KMS key full access to the KMS key. For more information about this example key policy, see [Allows access to the AWS account and enables IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) in the *AWS Key Management Service Developer Guide*.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "ecr-key-policy",
    "Statement": [
        {
            "Sid": "EnableIAMUserPermissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        }
    ]
}
```

------

The IAM user, IAM role, or AWS account creating your repositories must have the `kms:CreateGrant`, `kms:RetireGrant`, and `kms:DescribeKey` permission in addition to the necessary Amazon ECR permissions.

**Note**  
The `kms:RetireGrant` permission must be added to the IAM policy of the user or role creating the repository. The `kms:CreateGrant` and `kms:DescribeKey` permissions can be added to either the key policy for the KMS key or the IAM policy of user or role creating the repository. For more information on how AWS KMS permissions work, see [AWS KMS API permissions: Actions and resources reference](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) in the *AWS Key Management Service Developer Guide*.

The following example IAM policy can be added as an inline policy to a user to ensure they have the minimum permissions needed to create a repository with encryption enabled and delete the repository when they are finished with it. The AWS KMS key used to encrypt the repository can be specified using the resource parameter.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "ecr-kms-permissions",
    "Statement": [
        {
            "Sid": "AllowAccessToCreateAndRetireTheGrantsAssociatedWithTheKeyAsWellAsDescribeTheKey",
            "Effect": "Allow",
            "Action": [
                "kms:CreateGrant",
                "kms:RetireGrant",
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/{{b8d9ae76-080c-4043-92EXAMPLE}}"
        }
    ]
}
```

------

##### Allow a user to list KMS keys in the console when creating a repository
<a name="encryption-at-rest-iam-example"></a>

When using the Amazon ECR console to create a repository, you can grant permissions to enable a user to list the customer managed KMS keys in the Region when enabling encryption for the repository. The following IAM policy example shows the permissions needed to list your KMS keys and aliases when using the console.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": {
    "Effect": "Allow",
    "Action": [
      "kms:ListKeys",
      "kms:ListAliases",
      "kms:DescribeKey"
    ],
    "Resource": "*"
  }
}
```

------

#### Monitoring Amazon ECR interaction with AWS KMS
<a name="encryption-at-rest-monitoring"></a>

You can use AWS CloudTrail to track the requests that Amazon ECR sends to AWS KMS on your behalf. The log entries in the CloudTrail log contain an encryption context key to make them more easily identifiable.

##### Amazon ECR encryption context
<a name="ecr-encryption-context"></a>

An *encryption context* is a set of key–value pairs that contains arbitrary nonsecret data. When you include an encryption context in a request to encrypt data, AWS KMS cryptographically binds the encryption context to the encrypted data. To decrypt the data, you must pass in the same encryption context. 

In its [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) and [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests to AWS KMS, Amazon ECR uses an encryption context with two name–value pairs that identify the repository and Amazon S3 bucket being used. This is shown in the following example. The names do not vary, but combined encryption context values will be different for each value.

```
"encryptionContext": {
    "aws:s3:arn": "arn:aws:s3:::{{us-west-2}}-starport-manifest-bucket/{{EXAMPLE1-90ab-cdef-fedc-ba987BUCKET1}}/sha256:a7766145a775d39e53a713c75b6fd6d318740e70327aaa3ed5d09e0ef33fc3df",
    "aws:ecr:arn": "arn:aws:ecr:{{us-west-2}}:{{111122223333}}:repository/{{repository-name}}"
}
```

You can use the encryption context to identify these cryptographic operation in audit records and logs, such as [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and Amazon CloudWatch Logs, and as a condition for authorization in policies and grants.

The Amazon ECR encryption context consists of two name-value pairs.
+ **aws:s3:arn** – The first name–value pair identifies the bucket. The key is `aws:s3:arn`. The value is the Amazon Resource Name (ARN) of the Amazon S3 bucket.

  ```
  "aws:s3:arn": "{{ARN of an Amazon S3 bucket}}"
  ```

  For example, if the ARN of the bucket is `arn:aws:s3:::{{us-west-2}}-starport-manifest-bucket/{{EXAMPLE1-90ab-cdef-fedc-ba987BUCKET1}}/sha256:a7766145a775d39e53a713c75b6fd6d318740e70327aaa3ed5d09e0ef33fc3df`, the encryption context would include the following pair.

  ```
  "arn:aws:s3:::{{us-west-2}}-starport-manifest-bucket/{{EXAMPLE1-90ab-cdef-fedc-ba987BUCKET1}}/sha256:a7766145a775d39e53a713c75b6fd6d318740e70327aaa3ed5d09e0ef33fc3df"
  ```
+ **aws:ecr:arn** – The second name–value pair identifies the Amazon Resource Name (ARN) of the repository. The key is `aws:ecr:arn`. The value is the ARN of the repository.

  ```
  "aws:ecr:arn": "{{ARN of an Amazon ECR repository}}"
  ```

  For example, if the ARN of the repository is `arn:aws:ecr:{{us-west-2}}:{{111122223333}}:repository/{{repository-name}}`, the encryption context would include the following pair.

  ```
  "aws:ecr:arn": "arn:aws:ecr:{{us-west-2}}:{{111122223333}}:repository/{{repository-name}}"
  ```

#### Troubleshooting
<a name="encryption-at-rest-troubleshooting"></a>

When deleting an Amazon ECR repository with the console, if the repository is successfully deleted but Amazon ECR is unable to retire the grants added to your KMS key for your repository, you will receive the following error.

```
The repository {{[{repository-name}]}} has been deleted successfully but the grants created by the kmsKey {{[{kms_key}]}} failed to be retired
```

When this occurs, you can retire the AWS KMS grants for the repository yourself.

**To retire AWS KMS grants for a repository manually**

1. List the grants for the AWS KMS key used for the repository. The `key-id` value is included in the error you receive from the console. You can also use the `list-keys` command to list both the AWS managed keys and customer managed KMS keys in a specific Region in your account.

   ```
   aws kms list-grants \
        --key-id {{b8d9ae76-080c-4043-9237-c815bfc21dfc}} 
        --region {{us-west-2}}
   ```

   The output include an `EncryptionContextSubset` with the Amazon Resource Name (ARN) of your repository. This can be used to determine which grant added to the key is the one you want to retire. The `GrantId` value will be used when retiring the grant in the next step.

1. Retire each grant for the AWS KMS key added for the repository. Replace the value for {{GrantId}} with the ID of the grant from the output of the previous step.

   ```
   aws kms retire-grant \
        --key-id {{b8d9ae76-080c-4043-9237-c815bfc21dfc}} \
        --grant-id {{GrantId}} \
        --region {{us-west-2}}
   ```

## Compliance validation for Amazon Elastic Container Registry
<a name="ecr-compliance"></a>

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Infrastructure Security in Amazon Elastic Container Registry
<a name="infrastructure-security"></a>

As a managed service, Amazon Elastic Container Registry is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Amazon ECR through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

You can call these API operations from any network location, but Amazon ECR does support resource-based access policies, which can include restrictions based on the source IP address. You can also use Amazon ECR policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs. Effectively, this isolates network access to a given Amazon ECR resource from only the specific VPC within the AWS network. For more information, see [Amazon ECR interface VPC endpoints (AWS PrivateLink)](#vpc-endpoints).

### Amazon ECR interface VPC endpoints (AWS PrivateLink)
<a name="vpc-endpoints"></a>

You can improve the security posture of your VPC by configuring Amazon ECR to use an interface VPC endpoint. VPC endpoints are powered by AWS PrivateLink, a technology that enables you to privately access Amazon ECR APIs through private IP addresses (both IPv4 and IPv6). AWS PrivateLink restricts all network traffic between your VPC and Amazon ECR to the Amazon network. You don't need an internet gateway, a NAT device, or a virtual private gateway.

For more information about AWS PrivateLink and VPC endpoints, see [VPC Endpoints ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) in the *Amazon VPC User Guide*.

#### Considerations for Amazon ECR VPC endpoints
<a name="ecr-vpc-endpoint-considerations"></a>

Before you configure VPC endpoints for Amazon ECR, be aware of the following considerations.
+ To allow your Amazon ECS tasks hosted on Amazon EC2 instances to pull private images from Amazon ECR, create the interface VPC endpoints for Amazon ECS. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html) in the *Amazon Elastic Container Service Developer Guide*.
+ Amazon ECS tasks hosted on Fargate that pull container images from Amazon ECR can restrict access to the specific VPC their tasks use and to the VPC endpoint the service uses by adding condition keys to the task execution IAM role for the task. For more information, see [Optional IAM Permissions for Fargate Tasks Pulling Amazon ECR Images over Interface Endpoints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*.
+ The security group attached to the VPC endpoint must allow incoming connections on port 443 from the private subnet of the VPC.
+ Amazon ECR VPC endpoints support dual-stack (IPv4 and IPv6) connectivity. When you create a dual-stack VPC endpoint, it can handle traffic over both IPv4 and IPv6 private IP addresses.
+ VPC endpoints support Amazon ECR Public repositories through the AWS API SDK endpoint in US East (N. Virginia). 
+ VPC endpoints only support AWS provided DNS through Amazon Route 53. If you want to use your own DNS, you can use conditional DNS forwarding. For more information, see [DHCP Options Sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.
+ If your containers have existing connections to Amazon S3, their connections might be briefly interrupted when you add the Amazon S3 gateway endpoint. If you want to avoid this interruption, create a new VPC that uses the Amazon S3 gateway endpoint and then migrate your Amazon ECS cluster and its containers into the new VPC.
+ When an image is pulled using a pull through cache rule for the first time, if you've configured Amazon ECR to use an interface VPC endpoint using AWS PrivateLink then you need to create a public subnet in the same VPC, with a NAT gateway, and then route all outbound traffic to the internet from their private subnet to the NAT gateway in order for the pull to work. Subsequent image pulls don't require this. For more information, see [Scenario: Access the internet from a private subnet](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#public-nat-internet-access) in the *Amazon Virtual Private Cloud User Guide*.
+ For workloads requiring FIPS 140-3 validated cryptographic modules, Amazon ECR supports FIPS endpoints for VPC endpoints.

##### Considerations for Windows images
<a name="ecr-vpc-endpoint-windows-considerations"></a>

Images based on the Windows operating system include artifacts that are restricted by license from being distributed. By default, when you push Windows images to an Amazon ECR repository, the layers that include these artifacts are not pushed as they are considered *foreign layers*. When the artifacts are provided by Microsoft, the foreign layers are retrieved from Microsoft Azure infrastructure. For this reason, to enable your containers to pull these foreign layers from Azure additional steps are needed beyond creating the VPC endpoints.

It is possible to override this behavior when pushing Windows images to Amazon ECR by using the `--allow-nondistributable-artifacts` flag in the Docker daemon. When enabled, this flag will push the licensed layers to Amazon ECR which enables these images to be pulled from Amazon ECR via the VPC endpoint without additional access to Azure being required.

**Important**  
Using the `--allow-nondistributable-artifacts` flag does not preclude your obligation to comply with the terms of the Windows container base image license; you cannot post Windows content for public or third-party redistribution. Usage within your own environment is allowed.

To enable the use of this flag for your Docker installation, you must modify the Docker daemon configuration file which, depending on your Docker installation, can typically be configured in settings or preferences menu under the **Docker Engine** section or by editing the `C:\ProgramData\docker\config\daemon.json` file directly.

The following is an example of the required configuration. Replace the value with the repository URI you are pushing images to.

```
{
    "allow-nondistributable-artifacts": [
        "{{111122223333}}.dkr.ecr.{{us-west-2}}.amazonaws.com"
    ]
}
```

After modifying the Docker daemon configuration file, you must restart the Docker daemon before attempting to push your image. Confirm the push worked by verifying that the base layer was pushed to your repository.

**Note**  
The base layers for Windows images are large. The layer size will result in a longer time to push and additional storage costs in Amazon ECR for these images. For these reasons, we recommend only using this option when it is strictly required to reduce build times and ongoing storage costs. For example, the `mcr.microsoft.com/windows/servercore` image is approximately 1.7 GiB in size when compressed in Amazon ECR.

#### Create the VPC endpoints for Amazon ECR
<a name="ecr-setting-up-vpc-create"></a>

To create the VPC endpoints for the Amazon ECR service, use the [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) procedure in the *Amazon VPC User Guide*.

Amazon ECR VPC endpoints support dual-stack (IPv4 and IPv6) connectivity. When you create a dual-stack VPC endpoint, it automatically handles traffic over both IPv4 and IPv6 private IP addresses. The endpoint will route traffic using the appropriate IP version based on your client's network configuration and the endpoint's capabilities.

If you have existing IPv4-only VPC endpoints and want to migrate to dual-stack endpoints, you can modify your existing endpoints to support dual-stack connectivity, or create new dual-stack endpoints. When creating or modifying endpoints, ensure that your VPC and subnets support the IP version you want to use. After creating dual-stack endpoints, the endpoints will support both IPv4 and IPv6.

Amazon ECS tasks hosted on Amazon EC2 instances require both Amazon ECR endpoints and the Amazon S3 gateway endpoint.

Amazon ECS tasks hosted on Fargate using platform version `1.4.0` or later require both Amazon ECR VPC endpoints and the Amazon S3 gateway endpoints.

Amazon ECS tasks hosted on Fargate that use platform version `1.3.0` or earlier only require the **com.amazonaws.{{region}}.ecr.dkr** Amazon ECR VPC endpoint and the Amazon S3 gateway endpoints.

**Note**  
The order that the endpoints are created in doesn't matter.

**com.amazonaws.{{region}}.ecr.dkr**  
This endpoint is used for the Docker Registry APIs. Docker client commands such as `push` and `pull` use this endpoint.  
When you create this endpoint, you must enable a private DNS hostname. To do this, ensure that the **Enable Private DNS Name** option is selected in the Amazon VPC console when you create the VPC endpoint.  
For FIPS 140-3 compliant connections, use the FIPS endpoint name **com.amazonaws.{{region}}.ecr-fips.dkr**

**com.amazonaws.{{region}}.ecr.api**  
The specified {{region}} represents the Region identifier for an AWS Region supported by Amazon ECR, such as `us-east-2` for the US East (Ohio) Region.
For FIPS 140-3 compliant connections, use the FIPS endpoint names: **com.amazonaws.{{region}}.ecr-fips.dkr** and **com.amazonaws.{{region}}.ecr-fips.api**.  
This endpoint is used for calls to the Amazon ECR API. API actions such as `DescribeImages` and `CreateRepository` go to this endpoint.  
When this endpoint is created, you have the option to enable a private DNS hostname. Enable this setting by selecting **Enable Private DNS Name** in the VPC console when you create the VPC endpoint. If you enable a private DNS hostname for the VPC endpoint, update your SDK or AWS CLI to the latest version so that specifying an endpoint URL when using the SDK or AWS CLI isn't necessary.  
For FIPS 140-3 compliant connections, use the FIPS endpoint name **com.amazonaws.{{region}}.ecr-fips.api**.  
If you enable a private DNS hostname and are using an SDK or AWS CLI version released before January 24, 2019, you must use the `--endpoint-url` parameter to specify the interface endpoints. The following example shows the format for the endpoint URL.  

```
aws ecr create-repository --repository-name {{name}} --endpoint-url https://api.ecr.{{region}}.amazonaws.com
```
If you don't enable a private DNS hostname for the VPC endpoint, you must use the `--endpoint-url` parameter specifying the VPC endpoint ID for the interface endpoint. The following example shows the format for the endpoint URL.  

```
aws ecr create-repository --repository-name {{name}} --endpoint-url https://{{VPC_endpoint_ID}}.api.ecr.{{region}}.vpce.amazonaws.com
```
For FIPS 140-3 compliant connections, use the FIPS endpoint URL:  

```
aws ecr create-repository --repository-name {{name}} --endpoint-url https://api.ecr-fips.{{region}}.amazonaws.com
```

#### Create the Amazon S3 gateway endpoint
<a name="ecr-setting-up-s3-gateway"></a>

For your Amazon ECS tasks to pull private images from Amazon ECR, you must create a gateway endpoint for Amazon S3. The gateway endpoint is required because Amazon ECR uses Amazon S3 to store your image layers. When your containers download images from Amazon ECR, they must access Amazon ECR to get the image manifest and then Amazon S3 to download the actual image layers. The following is the Amazon Resource Name (ARN) of the Amazon S3 bucket containing the layers for each Docker image.

```
arn:aws:s3:::prod-{{region}}-starport-layer-bucket/*
```

**Note**  
If creating a dual-stack VPC endpoint for Amazon ECR, then you also need to create a dual-stack Amazon S3 Gateway or Interface endpoint. Refer to [S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html#privatelink-ip-address-types) for details.

Use the [Creating a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html#create-gateway-endpoint) procedure in the *Amazon VPC User Guide* to create the following Amazon S3 gateway endpoint for Amazon ECR. When creating the endpoint, be sure to select the route tables for your VPC.

**com.amazonaws.{{region}}.s3**  
The Amazon S3 gateway endpoint uses an IAM policy document to limit access to the service. The **Full Access** policy can be used because any restrictions that you have put in your task IAM roles or other IAM user policies still apply on top of this policy. If you want to limit Amazon S3 bucket access to the minimum required permissions for using Amazon ECR, see [Minimum Amazon S3 Bucket Permissions for Amazon ECR](#ecr-minimum-s3-perms).

##### Minimum Amazon S3 Bucket Permissions for Amazon ECR
<a name="ecr-minimum-s3-perms"></a>

The Amazon S3 gateway endpoint uses an IAM policy document to limit access to the service. To allow only the minimum Amazon S3 bucket permissions for Amazon ECR, restrict access to the Amazon S3 bucket that Amazon ECR uses when you create the IAM policy document for the endpoint. 

The following table describes the Amazon S3 bucket policy permissions needed by Amazon ECR.


| Permission | Description | 
| --- | --- | 
| `arn:aws:s3:::prod-{{region}}-starport-layer-bucket/*` | Provides access to the Amazon S3 bucket containing the layers for each Docker image. Represents the Region identifier for an AWS Region supported by Amazon ECR, such as `us-east-2` for the US East (Ohio) Region. | 

###### Example
<a name="ecr-minimum-s3-perms-example"></a>

The following example illustrates how to provide access to the Amazon S3 buckets required for Amazon ECR operations.

```
{
  "Statement": [
    {
      "Sid": "Access-to-specific-bucket-only",
      "Principal": "*",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::prod-{{region}}-starport-layer-bucket/*"]
    }
  ]
}
```

#### Create the CloudWatch Logs endpoint
<a name="ecr-setting-up-cloudwatch-logs"></a>

Amazon ECS tasks using the Fargate launch type that use a VPC without an internet gateway that also use the `awslogs` log driver to send log information to CloudWatch Logs require that you create the **com.amazonaws.{{region}}.logs** interface VPC endpoint for CloudWatch Logs. For more information, see [Using CloudWatch Logs with interface VPC endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html) in the *Amazon CloudWatch Logs User Guide*.

#### Create an endpoint policy for your Amazon ECR VPC endpoints
<a name="ecr-vpc-endpoint-policy"></a>

A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when you create or modify the endpoint. If you don't attach a policy when you create an endpoint, AWS attaches a default policy for you that allows full access to the service. An endpoint policy doesn't override or replace user policies or service-specific policies. It's a separate policy for controlling access from the endpoint to the specified service. Endpoint policies must be written in JSON format. For more information, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

We recommend creating a single IAM resource policy and attaching it to both of the Amazon ECR VPC endpoints.

The following is an example of an endpoint policy for Amazon ECR. This policy enables a specific IAM role to pull images from Amazon ECR.

```
{
	"Statement": [{
		"Sid": "AllowPull",
		"Principal": {
			"AWS": "arn:aws:iam::{{1234567890}}:role/{{role_name}}"
		},
		"Action": [
			"ecr:BatchGetImage",
			"ecr:GetDownloadUrlForLayer",
                    "ecr:GetAuthorizationToken"
		],
		"Effect": "Allow",
		"Resource": "*"
	}]
}
```

The following endpoint policy example prevents a specified repository from being deleted.

```
{
	"Statement": [{
			"Sid": "AllowAll",
			"Principal": "*",
			"Action": "*",
			"Effect": "Allow",
			"Resource": "*"
		},
		{
			"Sid": "PreventDelete",
			"Principal": "*",
			"Action": "ecr:DeleteRepository",
			"Effect": "Deny",
			"Resource": "arn:aws:ecr:{{region}}:{{1234567890}}:repository/{{repository_name}}"
		}
	]
}
```

The following endpoint policy example combines the two previous examples into a single policy.

```
{
	"Statement": [{
			"Sid": "AllowAll",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "*",
			"Resource": "*"
		},
		{
			"Sid": "PreventDelete",
			"Effect": "Deny",
			"Principal": "*",
			"Action": "ecr:DeleteRepository",
			"Resource": "arn:aws:ecr:{{region}}:{{1234567890}}:repository/{{repository_name}}"
		},
		{
			"Sid": "AllowPull",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::{{1234567890}}:role/{{role_name}}"
			},
			"Action": [
				"ecr:BatchGetImage",
				"ecr:GetDownloadUrlForLayer",
                          "ecr:GetAuthorizationToken"
			],
			"Resource": "*"
		}
	]
}
```

**To modify the VPC endpoint policy for Amazon ECR**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. If you have not already created the VPC endpoints for Amazon ECR, see [Create the VPC endpoints for Amazon ECR](#ecr-setting-up-vpc-create).

1. Select the Amazon ECR VPC endpoint to add a policy to, and choose the **Policy** tab in the lower half of the screen.

1. Choose **Edit Policy** and make the changes to the policy.

1. Choose **Save** to save the policy.

#### Shared subnets
<a name="ecr-vpc-endpoint-shared-subnets"></a>

You can't create, describe, modify, or delete VPC endpoints in subnets that are shared with you. However, you can use the VPC endpoints in subnets that are shared with you.

## Cross-service confused deputy prevention
<a name="cross-service-confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account. 

We recommend using the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) or [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in resource policies to limit the permissions that Amazon ECR gives another service to the resource. Use `aws:SourceArn` if you want only one resource to be associated with the cross-service access. Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn` global condition context key with the full ARN of the resource. If you don't know the full ARN of the resource or if you are specifying multiple resources, use the `aws:SourceArn` global context condition key with wildcard characters (`*`) for the unknown portions of the ARN. For example, `arn:aws:{{servicename}}:{{region}}:{{123456789012}}:*`. 

If the `aws:SourceArn` value does not contain the account ID, such as an Amazon S3 bucket ARN, you must use both global condition context keys to limit permissions. 

The value of `aws:SourceArn` must be ResourceDescription.

The following example shows how you can use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in an Amazon ECR repository policy to allow AWS CodeBuild access to the Amazon ECR API actions necessary for integration with that service while also preventing the confused deputy problem.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"CodeBuildAccess",
         "Effect":"Allow",
         "Principal":{
            "Service":"codebuild.amazonaws.com"
         },
         "Action":[
            "ecr:BatchGetImage",
            "ecr:GetDownloadUrlForLayer"
         ],
         "Resource": "*",
         "Condition":{
            "ArnLike":{
               "aws:SourceArn":"arn:aws:codebuild:{{us-east-1}}:{{123456789012}}:project/{{project-name}}"
            },
            "StringEquals":{
               "aws:SourceAccount":"{{123456789012}}"
            }
         }
      }
   ]
}
```

------

# Amazon ECR monitoring
<a name="monitoring"></a>

You can monitor your Amazon ECR API usage with Amazon CloudWatch, which collects and processes raw data from Amazon ECR into readable, near real-time metrics. These statistics are recorded for a period of two weeks so that you can access historical information and gain perspective on your API usage. Amazon ECR metric data is automatically sent to CloudWatch in one-minute periods. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

Amazon ECR provides metrics based on your API usage for authorization, image push, and image pull actions.

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon ECR and your AWS solutions. We recommend that you collect monitoring data from the resources that make up your AWS solution so that you can more easily debug a multi-point failure if one occurs. Before you start monitoring Amazon ECR, however, you should create a monitoring plan that includes answers to the following questions:
+ What are your monitoring goals?
+ What resources will you monitor?
+ How often will you monitor these resources?
+ What monitoring tools will you use?
+ Who will perform the monitoring tasks?
+ Who should be notified when something goes wrong?

The next step is to establish a baseline for normal Amazon ECR performance in your environment by measuring performance at various times and under different load conditions. As you monitor Amazon ECR, store historical monitoring data so that you can compare it with new performance data, identify normal performance patterns and performance anomalies, and devise methods to address issues.

**Topics**
+ [Visualizing your service quotas and setting alarms](#monitoring-quotas-alarms)
+ [Amazon ECR usage metrics](#monitoring-usage)
+ [Amazon ECR usage reports](#usage-reports)
+ [Amazon ECR repository metrics](#ecr-repository-metrics)
+ [Amazon ECR events and EventBridge](#ecr-eventbridge)
+ [Logging Amazon ECR actions with AWS CloudTrail](#logging-using-cloudtrail)

## Visualizing your service quotas and setting alarms
<a name="monitoring-quotas-alarms"></a>

You can use the CloudWatch console to visualize your service quotas and see how your current usage compares to service quotas. You can also set alarms so that you will be notified when you approach a quota.

**To visualize a service quota and optionally set an alarm**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. On the **All metrics** tab, choose **Usage**, then choose **By AWS Resource**.

   The list of service quota usage metrics appears.

1. Select the check box next to one of the metrics.

   The graph displays your current usage of that AWS resource.

1. To add your service quota to the graph, do the following:

   1. Choose the **Graphed metrics** tab.

   1. Choose **Math expression**, **Start with an empty expression**. Then in the new row, under **Details**, enter **SERVICE\_QUOTA(m1)**.

      A new line is added to the graph, displaying the service quota for the resource represented in the metric.

1. To see your current usage as a percentage of the quota, add a new expression or change the current **SERVICE\_QUOTA** expression. For the new expression, use **m1/60/SERVICE\_QUOTA(m1)\*100**.

1. (Optional) To set an alarm that notifies you if you approach the service quota, do the following:

   1. On the **m1/60/SERVICE\_QUOTA(m1)\*100** row, under **Actions**, choose the alarm icon. It looks like a bell.

      The alarm creation page appears.

   1. Under **Conditions**, ensure that **Threshold type** is **Static** and **Whenever Expression1 is** is set to **Greater**. Under **than**, enter **80**. This creates an alarm that goes into ALARM state when your usage exceeds 80 percent of the quota.

   1. Choose **Next**.

   1. On the next page, select an Amazon SNS topic or create a new one. This topic is notified when the alarm goes to ALARM state. Then choose **Next**.

   1. On the next page, enter a name and description for the alarm, and then choose **Next**.

   1. Choose **Create alarm**.

## Amazon ECR usage metrics
<a name="monitoring-usage"></a>

You can use CloudWatch usage metrics to provide visibility into your account's usage of resources. Use these metrics to visualize your current service usage on CloudWatch graphs and dashboards.

Amazon ECR usage metrics correspond to AWS service quotas. You can configure alarms that alert you when your usage approaches a service quota. For more information about Amazon ECR service quotas, see [Amazon ECR service quotas](#service-quotas).

Amazon ECR publishes the following metrics in the `AWS/Usage` namespace.


|  Metric  |  Description  | 
| --- | --- | 
| `CallCount` | The number of API action calls from your account. The resources are defined by the dimensions associated with the metric.<br />The most useful statistic for this metric is `SUM`, which represents the sum of the values from all contributors during the period defined. | 
| `ResourceCount` | The number of the specified resources in your account. The resources are defined by the dimensions associated with the metric.<br />The most useful statistic for this metric is `MAXIMUM`, which represents the maximum number of resources used during the 5-minute period. | 

The following dimensions are used to refine the API usage metrics that are published by Amazon ECR.


|  Dimension  |  Description  | 
| --- | --- | 
| `Service` | The name of the AWS service containing the resource. For Amazon ECR usage metrics, the value for this dimension is `ECR`. | 
| `Type` | The type of entity that is being reported. Currently, the only valid value for Amazon ECR API usage metrics is `API`. | 
| `Resource` | The type of resource that is running. Currently, Amazon ECR returns information on your API usage for the following API actions.+  `GetAuthorizationToken` <br />+  `BatchCheckLayerAvailability` <br />+  `InitiateLayerUpload` <br />+  `UploadLayerPart` <br />+  `CompleteLayerUpload` <br />+  `PutImage` <br />+  `BatchGetImage` <br />+  `GetDownloadUrlForLayer`  | 
|  Class  | The class of resource being tracked. Currently, Amazon ECR does not use the class dimension. | 

The following dimensions are used to refine the Resource usage metrics that are published by Amazon ECR.


|  Dimension  |  Description  | 
| --- | --- | 
| `Service` | The name of the AWS service containing the resource. For Amazon ECR usage metrics, the value for this dimension is `ECR`. | 
| `Type` | The type of entity that is being reported. Currently, the only valid value for Amazon ECR resource usage metrics is `RESOURCE`. | 
| `Resource` | The type of resource that is running. Currently, Amazon ECR returns information on your resource usage for the following metrics.+  `RepositoryCount` <br />+  `ImagesPerRepositoryCount`  | 
| `ResourceId` | The identifier for the resource that incurred the usage. Currently, ResourceId is only relevant to `ImagesPerRepositoryCount` and its value is formatted as repository/your\_repository\_name. For example: "repository/my-repo" returns the number of images in repository with name "my-repo". | 

## Amazon ECR usage reports
<a name="usage-reports"></a>

AWS provides a free reporting tool called Cost Explorer that enables you to analyze the cost and usage of your Amazon ECR resources.

Use Cost Explorer to view charts of your usage and costs. You can view data from the previous 13 months and forecast how much you are likely to spend for the next three months. You can use Cost Explorer to see patterns in how much you spend on AWS resources over time, identify areas that need further inquiry, and see trends that you can use to understand your costs. You also can specify time ranges for the data and view time data by day or by month.

The metering data in your Cost and Usage Reports shows usage across all of your Amazon ECR repositories. For more information, see [Tagging your resources for billing](#tag-resources-for-billing).

For more information about creating an AWS Cost and Usage Report, see [AWS Cost and Usage Report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage.html) in the *AWS Billing User Guide*.

## Amazon ECR repository metrics
<a name="ecr-repository-metrics"></a>

Amazon ECR sends repository pull count metrics to Amazon CloudWatch. Amazon ECR metric data is automatically sent to CloudWatch in 1-minute periods. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Enabling CloudWatch metrics](#enable_cloudwatch)
+ [Available metrics and dimensions](#available_cloudwatch_metrics)
+ [Viewing Amazon ECR metrics using the CloudWatch console](#viewing_metrics_console)

### Enabling CloudWatch metrics
<a name="enable_cloudwatch"></a>

Amazon ECR sends repository metrics automatically for all repositories. There is no need to take any manual steps.

### Available metrics and dimensions
<a name="available_cloudwatch_metrics"></a>

The following sections list the metrics and dimensions that Amazon ECR sends to Amazon CloudWatch.

#### Amazon ECR metrics
<a name="ecr-metrics"></a>

Amazon ECR provides metrics for you to monitor your repositories. You can measure the pull count.

The `AWS/ECR` namespace includes the following metrics.

`RepositoryPullCount`  
The total number of pulls for the images in the repository.  
Valid dimensions: `RepositoryName`.  
Valid statistics: Average, Minimum, Maximum, Sum, Sample Count. The most useful statistic is Sum.  
Unit: Integer.

#### Dimensions for Amazon ECR metrics
<a name="ecs-metrics-dimensions"></a>

Amazon ECR metrics use the `AWS/ECR` namespace and provide metrics for the following dimensions.

`RepositoryName`  
This dimension filters the data that you request for all container images in a specified repository.

### Viewing Amazon ECR metrics using the CloudWatch console
<a name="viewing_metrics_console"></a>

You can view Amazon ECR repository metrics on the CloudWatch console. The CloudWatch console provides a fine-grained and customizable display of your resources. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

## Amazon ECR events and EventBridge
<a name="ecr-eventbridge"></a>

Amazon EventBridge enables you to automate your AWS services and to respond automatically to system events such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near real time. You can write simple rules to indicate which events are of interest to you and include automated actions to take when an event matches a rule. The actions that can be automatically triggered include the following:
+ Adding events to log groups in CloudWatch Logs
+ Invoking an AWS Lambda function
+ Invoking Amazon EC2 Run Command
+ Relaying the event to Amazon Kinesis Data Streams
+ Activating an AWS Step Functions state machine
+ Notifying an Amazon SNS topic or an Amazon SQS queue

For more information, see [Getting Started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-getting-set-up.html) in the *Amazon EventBridge User Guide*.

### Sample events from Amazon ECR
<a name="ecr-eventbridge-bus"></a>

The following are example events from Amazon ECR. Events are emitted on a best effort basis.

**Event for a completed image push**

The following event is sent when each image push is completed. For more information, see [Pushing a Docker image to an Amazon ECR private repository](#docker-push-ecr-image).

```
{
    "version": "0",
    "id": "13cde686-328b-6117-af20-0e5566167482",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "{{123456789012}}",
    "time": "2019-11-16T01:54:34Z",
    "region": "us-west-2",
    "resources": [],
    "detail": {
        "result": "SUCCESS",
        "repository-name": "{{my-repository-name}}",
        "image-digest": "{{sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234}}",
        "action-type": "PUSH",
        "image-tag": "latest"
    }
}
```

**Event for a pull through cache action**

The following event is sent when a pull through cache action is attempted. For more information, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache).

```
{
    "version": "0",
    "id": "85fc3613-e913-7fc4-a80c-a3753e4aa9ae",
    "detail-type": "ECR Pull Through Cache Action",
    "source": "aws.ecr",
    "account": "{{123456789012}}",
    "time": "2023-02-29T02:36:48Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecr:us-west-2:{{123456789012}}:repository/docker-hub/alpine"
    ],
    "detail": {
        "rule-version": "1",
        "sync-status": "SUCCESS",
        "ecr-repository-prefix": "docker-hub",
        "repository-name": "docker-hub/alpine",
        "upstream-registry-url": "public.ecr.aws",
        "image-tag": "3.17.2",
        "image-digest": "{{sha256:4aa08ef415aecc80814cb42fa41b658480779d80c77ab15EXAMPLE}}",
    }
}
```

**Event for a completed image scan (basic scanning)**

When basic scanning is enabled for your registry, the following event is sent when each image scan is completed. The `finding-severity-counts` parameter will only return a value for a severity level if one exists. For example, if the image contains no findings at `CRITICAL` level, then no critical count is returned. For more information, see [Scan images for OS vulnerabilities in Amazon ECR](#image-scanning-basic).

**Note**  
For details about events that Amazon Inspector emits when enhanced scanning is enabled, see [EventBridge events sent for enhanced scanning in Amazon ECR](#image-scanning-enhanced-events).

```
{
    "version": "0",
    "id": "85fc3613-e913-7fc4-a80c-a3753e4aa9ae",
    "detail-type": "ECR Image Scan",
    "source": "aws.ecr",
    "account": "{{123456789012}}",
    "time": "2019-10-29T02:36:48Z",
    "region": "{{us-east-1}}",
    "resources": [
        "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/{{my-repository-name}}"
    ],
    "detail": {
        "scan-status": "COMPLETE",
        "repository-name": "{{my-repository-name}}",
        "finding-severity-counts": {
	       "CRITICAL": {{10}},
	       "MEDIUM": {{9}}
	     },
        "image-digest": "{{sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234}}",
        "image-tags": []
    }
}
```

**Event for a change notification on a resource with enhanced scanning enabled (enhanced scanning)**

When enhanced scanning is enabled for your registry, the following event is sent by Amazon ECR when there is a change with a resource that has enhanced scanning enabled. This includes new repositories being created, the scan frequency for a repository being changed, or when images are created or deleted in repositories with enhanced scanning enabled. For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning).

```
{
	"version": "0",
	"id": "0c18352a-a4d4-6853-ef53-0ab8638973bf",
	"detail-type": "ECR Scan Resource Change",
	"source": "aws.ecr",
	"account": "{{123456789012}}",
	"time": "2021-10-14T20:53:46Z",
	"region": "{{us-east-1}}",
	"resources": [],
	"detail": {
		"action-type": "SCAN_FREQUENCY_CHANGE",
		"repositories": [{
				"repository-name": "repository-1",
				"repository-arn": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/repository-1",
				"scan-frequency": "SCAN_ON_PUSH",
				"previous-scan-frequency": "MANUAL"
			},
			{
				"repository-name": "repository-2",
				"repository-arn": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/repository-2",
				"scan-frequency": "CONTINUOUS_SCAN",
				"previous-scan-frequency": "SCAN_ON_PUSH"
			},
			{
				"repository-name": "repository-3",
				"repository-arn": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/repository-3",
				"scan-frequency": "CONTINUOUS_SCAN",
				"previous-scan-frequency": "SCAN_ON_PUSH"
			}
		],
		"resource-type": "REPOSITORY",
		"scan-type": "ENHANCED"
	}
}
```

**Event for an image deletion**

The following event is sent when an image is deleted. For more information, see [Deleting an image in Amazon ECR](#delete_image).

```
{
    "version": "0",
    "id": "dd3b46cb-2c74-f49e-393b-28286b67279d",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "{{123456789012}}",
    "time": "2019-11-16T02:01:05Z",
    "region": "us-west-2",
    "resources": [],
    "detail": {
        "result": "SUCCESS",
        "repository-name": "{{my-repository-name}}",
        "image-digest": "{{sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234}}",
        "action-type": "DELETE",
        "image-tag": "latest"
    }
}
```

**Event for an image archival action**

The following event is sent when an image is archived. The `target-storage-class` field will be set to `ARCHIVE`. The event includes the manifest and artifact media types to identify the type of content being archived.

```
{
    "version": "0",
    "id": "4f5ec4d5-4de4-7aad-a046-EXAMPLE",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "{{123456789012}}",
    "time": "2019-08-06T00:58:09Z",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "action-type": "UPDATE_STORAGE_CLASS",
        "target-storage-class": "ARCHIVE",
        "image-digest": "{{sha256:f98d67af8e53a536502bfc600de3266556b06ed635a32d60aa7a5fe6d7e609d7}}",
        "repository-name": "{{ubuntu}}",
        "result": "SUCCESS",
        "manifest-media-type": "application/vnd.oci.image.manifest.v1+json",
        "artifact-media-type": "application/vnd.oci.image.config.v1+json"
    }
}
```

**Event for an image restore action**

The following event is sent when an archived image is restored. The `target-storage-class` field will be set to `STANDARD`. The event includes a `last-activated-at` field showing when the image was last restored.

```
{
    "version": "0",
    "id": "7b8fc5e6-5ef5-8bbe-b157-EXAMPLE",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "{{123456789012}}",
    "time": "2019-08-06T01:15:22Z",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "action-type": "UPDATE_STORAGE_CLASS",
        "target-storage-class": "STANDARD",
        "image-digest": "{{sha256:f98d67af8e53a536502bfc600de3266556b06ed635a32d60aa7a5fe6d7e609d7}}",
        "repository-name": "{{ubuntu}}",
        "result": "SUCCESS",
        "manifest-media-type": "application/vnd.oci.image.manifest.v1+json",
        "artifact-media-type": "application/vnd.oci.image.config.v1+json",
        "last-activated-at": "2025-10-10T19:13:02.74Z"
    }
}
```

**Event for a referrer restore action**

The following event is sent when an archived referrer (reference artifact such as an SBOM, signature, or attestation) is restored. Note that the `detail-type` is `ECR Referrer Action` to distinguish it from regular image actions. The `manifest-media-type` and `artifact-media-type` fields identify the specific type of referrer being restored. In this example, an SBOM artifact is being restored.

```
{
    "version": "0",
    "id": "8c9gd6f7-6fg6-9ccf-c268-EXAMPLE",
    "detail-type": "ECR Referrer Action",
    "source": "aws.ecr",
    "account": "{{123456789012}}",
    "time": "2019-08-06T01:20:45Z",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "action-type": "UPDATE_STORAGE_CLASS",
        "target-storage-class": "STANDARD",
        "image-digest": "{{sha256:f98d67af8e53a536502bfc600de3266556b06ed635a32d60aa7a5fe6d7e609d7}}",
        "repository-name": "{{sbom}}",
        "result": "SUCCESS",
        "manifest-media-type": "application/vnd.cncf.oras.artifact.manifest.v1+json",
        "artifact-media-type": "text/sbom+json",
        "last-activated-at": "2025-10-10T19:13:02.74Z"
    }
}
```

**Event for a completed image replication**

The following event is sent when each image replication is completed. For more information, see [Private image replication in Amazon ECR](#replication).

```
{
  "version": "0",
  "id": "c8b133b1-6029-ee73-e2a1-4f466b8ba999",
  "detail-type": "ECR Replication Action",
  "source": "aws.ecr",
  "account": "{{123456789012}}",
  "time": "2024-05-08T20:44:54Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/docker-hub/alpine"
  ],
  "detail": {
    "result": "SUCCESS",
    "repository-name": "{{docker-hub/alpine}}",
    "image-digest": "{{sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234}}",
    "source-account": "{{123456789012}}",
    "action-type": "REPLICATE",
    "source-region": "{{us-west-2}}",
    "image-tag": "3.17.2"
  }
}
```

## Logging Amazon ECR actions with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon ECR is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, a role, or an AWS service in Amazon ECR. CloudTrail captures the following Amazon ECR actions as events:
+ All API calls, including calls from the Amazon ECR console
+ All actions taken due to the encryption settings on your repositories
+ All actions taken due to lifecycle policy rules, including both successful and unsuccessful actions
**Important**  
Due to the size limitations of individual CloudTrail events, for lifecycle policy actions where 10 or more images are expired Amazon ECR sends multiple events to CloudTrail. Additionally, Amazon ECR includes a maximum of 100 tags per image.

When a trail is created, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon ECR. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using this information, you can determine the request that was made to Amazon ECR, the originating IP address, who made the request, when it was made, and additional details. 

For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

### Amazon ECR information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Amazon ECR, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Amazon ECR, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. When you create a trail in the console, you can apply the trail to a single Region or to all Regions. The trail logs events in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to analyze and act upon the event data collected in CloudTrail logs. For more information, see: 
+ [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [AWS service integrations with CloudTrail logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Amazon ECR API actions are logged by CloudTrail and are documented in the [Amazon Elastic Container Registry API Reference](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/). When you perform common tasks, sections are generated in the CloudTrail log files for each API action that is part of that task. For example, when you create a repository, `GetAuthorizationToken`, `CreateRepository` and `SetRepositoryPolicy` sections are generated in the CloudTrail log files. When you push an image to a repository, `InitiateLayerUpload`, `UploadLayerPart`, `CompleteLayerUpload`, `PutImage`, and, if blob mounting is enabled, `MountLayer` sections are generated. When you pull an image, `GetDownloadUrlForLayer` and `BatchGetImage` sections are generated. When you archive or restore an image `UpdateImageStorageClass` section is generated. When OCI clients that support the OCI 1.1 specification fetch the list of referrers, or reference artifacts, for an image using the Referrers API, a `ListImageReferrers` CloudTrail event is emitted. For examples of these common tasks, see [CloudTrail log entry examples](#cloudtrail-examples).

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or user credentials
+ Whether the request was made with temporary security credentials for a role or federated user
+ Whether the request was made by another AWS service

For more information, see the [CloudTrail `userIdentity` Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

### Understanding Amazon ECR log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and other information. CloudTrail log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order. 

#### CloudTrail log entry examples
<a name="cloudtrail-examples"></a>

The following are CloudTrail log entry examples for a few common Amazon ECR tasks.

These examples have been formatted for improved readability. In a CloudTrail log file, all entries and events are concatenated into a single line. In addition, this example has been limited to a single Amazon ECR entry. In a real CloudTrail log file, you see entries and events from multiple AWS services.

**Important**  
The **sourceIPAddress** is the IP address that the request was made from. For actions that originate from the service console, the address reported is for your underlying resource, not the console web server. For services in AWS, only the DNS name is displayed. We still evaluate the auth with the client source IP even if it's redacted to AWS service DNS name.

**Topics**
+ [Example: Create repository action](#cloudtrail-examples-create-repository)
+ [Example: AWS KMS `CreateGrant` API action when creating an Amazon ECR repository](#cloudtrail-examples-create-repository-kms)
+ [Example: Image push action](#cloudtrail-examples-push-image)
+ [Example: Image pull action](#cloudtrail-examples-image-pull)
+ [Example: Image lifecycle policy action](#cloudtrail-examples-lcp)
+ [Example: Image archival action](#cloudtrail-examples-image-archive)
+ [Example: Image restore action](#cloudtrail-examples-image-restore)
+ [Example: Image referrers action](#cloudtrail-examples-image-referrers-action)

##### Example: Create repository action
<a name="cloudtrail-examples-create-repository"></a>

The following example shows a CloudTrail log entry that demonstrates the `CreateRepository` action.

```
{
    "eventVersion": "1.04",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:account_name",
        "arn": "arn:aws:sts::123456789012:user/Mary_Major",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2018-07-11T21:54:07Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            }
        }
    },
    "eventTime": "2018-07-11T22:17:43Z",
    "eventSource": "ecr.amazonaws.com",
    "eventName": "CreateRepository",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "203.0.113.12",
    "userAgent": "console.amazonaws.com",
    "requestParameters": {
        "repositoryName": "testrepo"
    },
    "responseElements": {
        "repository": {
            "repositoryArn": "arn:aws:ecr:us-east-2:123456789012:repository/testrepo",
            "repositoryName": "testrepo",
            "repositoryUri": "123456789012.dkr.ecr.us-east-2.amazonaws.com/testrepo",
            "createdAt": "Jul 11, 2018 10:17:44 PM",
            "registryId": "123456789012"
        }
    },
    "requestID": "cb8c167e-EXAMPLE",
    "eventID": "e3c6f4ce-EXAMPLE",
    "resources": [
        {
            "ARN": "arn:aws:ecr:us-east-2:123456789012:repository/testrepo",
            "accountId": "123456789012"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```

##### Example: AWS KMS `CreateGrant` API action when creating an Amazon ECR repository
<a name="cloudtrail-examples-create-repository-kms"></a>

The following example shows a CloudTrail log entry that demonstrates the AWS KMS `CreateGrant` action when creating an Amazon ECR repository with KMS encryption enabled. For each repository that is created with KMS encryption is enabled, you should see two `CreateGrant` log entries in CloudTrail.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAIEP6W46J43IG7LXAQ",
        "arn": "arn:aws:iam::123456789012:user/Mary_Major",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Mary_Major",
        "sessionContext": {
            "sessionIssuer": {
                
            },
            "webIdFederationData": {
                
            },
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-06-10T19:22:10Z"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2020-06-10T19:22:10Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "203.0.113.12",
    "userAgent": "console.amazonaws.com",
    "requestParameters": {
        "keyId": "4b55e5bf-39c8-41ad-b589-18464af7758a",
        "granteePrincipal": "ecr.us-west-2.amazonaws.com",
        "operations": [
            "GenerateDataKey",
            "Decrypt"
        ],
        "retiringPrincipal": "ecr.us-west-2.amazonaws.com",
        "constraints": {
            "encryptionContextSubset": {
                "aws:ecr:arn": "arn:aws:ecr:us-west-2:123456789012:repository/testrepo"
            }
        }
    },
    "responseElements": {
        "grantId": "3636af9adfee1accb67b83941087dcd45e7fadc4e74ff0103bb338422b5055f3"
    },
    "requestID": "047b7dea-b56b-4013-87e9-a089f0f6602b",
    "eventID": "af4c9573-c56a-4886-baca-a77526544469",
    "readOnly": false,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:123456789012:key/4b55e5bf-39c8-41ad-b589-18464af7758a"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```

##### Example: Image push action
<a name="cloudtrail-examples-push-image"></a>

The following example shows a CloudTrail log entry that demonstrates an image push which uses the `PutImage` action.

**Note**  
When pushing an image, you will also see `InitiateLayerUpload`, `UploadLayerPart`, and `CompleteLayerUpload` references in the CloudTrail logs.

```
{
    "eventVersion": "1.04",
    "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:account_name",
    "arn": "arn:aws:sts::123456789012:user/Mary_Major",
    "accountId": "123456789012",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"userName": "Mary_Major",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2019-04-15T16:42:14Z"
			}
		}
	},
	"eventTime": "2019-04-15T16:45:00Z",
	"eventSource": "ecr.amazonaws.com",
	"eventName": "PutImage",
	"awsRegion": "us-east-2",
	"sourceIPAddress": "AWS Internal",
	"userAgent": "AWS Internal",
	"requestParameters": {
		"repositoryName": "testrepo",
		"imageTag": "latest",
		"registryId": "123456789012",
		"imageManifest": "{\n   \"schemaVersion\": 2,\n   \"mediaType\": \"application/vnd.docker.distribution.manifest.v2+json\",\n   \"config\": {\n      \"mediaType\": \"application/vnd.docker.container.image.v1+json\",\n      \"size\": 5543,\n      \"digest\": \"sha256:000b9b805af1cdb60628898c9f411996301a1c13afd3dbef1d8a16ac6dbf503a\"\n   },\n   \"layers\": [\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 43252507,\n         \"digest\": \"sha256:3b37166ec61459e76e33282dda08f2a9cd698ca7e3d6bc44e6a6e7580cdeff8e\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 846,\n         \"digest\": \"sha256:504facff238fde83f1ca8f9f54520b4219c5b8f80be9616ddc52d31448a044bd\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 615,\n         \"digest\": \"sha256:ebbcacd28e101968415b0c812b2d2dc60f969e36b0b08c073bf796e12b1bb449\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 850,\n         \"digest\": \"sha256:c7fb3351ecad291a88b92b600037e2435c84a347683d540042086fe72c902b8a\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 168,\n         \"digest\": \"sha256:2e3debadcbf7e542e2aefbce1b64a358b1931fb403b3e4aeca27cb4d809d56c2\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 37720774,\n         \"digest\": \"sha256:f8c9f51ad524d8ae9bf4db69cd3e720ba92373ec265f5c390ffb21bb0c277941\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 30432107,\n         \"digest\": \"sha256:813a50b13f61cf1f8d25f19fa96ad3aa5b552896c83e86ce413b48b091d7f01b\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 197,\n         \"digest\": \"sha256:7ab043301a6187ea3293d80b30ba06c7bf1a0c3cd4c43d10353b31bc0cecfe7d\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 154,\n         \"digest\": \"sha256:67012cca8f31dc3b8ee2305e7762fee20c250513effdedb38a1c37784a5a2e71\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 176,\n         \"digest\": \"sha256:3bc892145603fffc9b1c97c94e2985b4cb19ca508750b15845a5d97becbd1a0e\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 183,\n         \"digest\": \"sha256:6f1c79518f18251d35977e7e46bfa6c6b9cf50df2a79d4194941d95c54258d18\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 212,\n         \"digest\": \"sha256:b7bcfbc2e2888afebede4dd1cd5eebf029bb6315feeaf0b56e425e11a50afe42\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 212,\n         \"digest\": \"sha256:2b220f8b0f32b7c2ed8eaafe1c802633bbd94849b9ab73926f0ba46cdae91629\"\n      }\n   ]\n}"
	},
	"responseElements": {
		"image": {
			"repositoryName": "testrepo",
			"imageManifest": "{\n   \"schemaVersion\": 2,\n   \"mediaType\": \"application/vnd.docker.distribution.manifest.v2+json\",\n   \"config\": {\n      \"mediaType\": \"application/vnd.docker.container.image.v1+json\",\n      \"size\": 5543,\n      \"digest\": \"sha256:000b9b805af1cdb60628898c9f411996301a1c13afd3dbef1d8a16ac6dbf503a\"\n   },\n   \"layers\": [\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 43252507,\n         \"digest\": \"sha256:3b37166ec61459e76e33282dda08f2a9cd698ca7e3d6bc44e6a6e7580cdeff8e\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 846,\n         \"digest\": \"sha256:504facff238fde83f1ca8f9f54520b4219c5b8f80be9616ddc52d31448a044bd\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 615,\n         \"digest\": \"sha256:ebbcacd28e101968415b0c812b2d2dc60f969e36b0b08c073bf796e12b1bb449\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 850,\n         \"digest\": \"sha256:c7fb3351ecad291a88b92b600037e2435c84a347683d540042086fe72c902b8a\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 168,\n         \"digest\": \"sha256:2e3debadcbf7e542e2aefbce1b64a358b1931fb403b3e4aeca27cb4d809d56c2\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 37720774,\n         \"digest\": \"sha256:f8c9f51ad524d8ae9bf4db69cd3e720ba92373ec265f5c390ffb21bb0c277941\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 30432107,\n         \"digest\": \"sha256:813a50b13f61cf1f8d25f19fa96ad3aa5b552896c83e86ce413b48b091d7f01b\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 197,\n         \"digest\": \"sha256:7ab043301a6187ea3293d80b30ba06c7bf1a0c3cd4c43d10353b31bc0cecfe7d\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 154,\n         \"digest\": \"sha256:67012cca8f31dc3b8ee2305e7762fee20c250513effdedb38a1c37784a5a2e71\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 176,\n         \"digest\": \"sha256:3bc892145603fffc9b1c97c94e2985b4cb19ca508750b15845a5d97becbd1a0e\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 183,\n         \"digest\": \"sha256:6f1c79518f18251d35977e7e46bfa6c6b9cf50df2a79d4194941d95c54258d18\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 212,\n         \"digest\": \"sha256:b7bcfbc2e2888afebede4dd1cd5eebf029bb6315feeaf0b56e425e11a50afe42\"\n      },\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 212,\n         \"digest\": \"sha256:2b220f8b0f32b7c2ed8eaafe1c802633bbd94849b9ab73926f0ba46cdae91629\"\n      }\n   ]\n}",
			"registryId": "123456789012",
			"imageId": {
				"imageDigest": "sha256:98c8b060c21d9adbb6b8c41b916e95e6307102786973ab93a41e8b86d1fc6d3e",
				"imageTag": "latest"
			}
		}
	},
	"requestID": "cf044b7d-5f9d-11e9-9b2a-95983139cc57",
	"eventID": "2bfd4ee2-2178-4a82-a27d-b12939923f0f",
	"resources": [{
		"ARN": "arn:aws:ecr:us-east-2:123456789012:repository/testrepo",
		"accountId": "123456789012"
	}],
	"eventType": "AwsApiCall",
	"recipientAccountId": "123456789012"
}
```

##### Example: Image pull action
<a name="cloudtrail-examples-image-pull"></a>

The following example shows a CloudTrail log entry that demonstrates an image pull which uses the `BatchGetImage` action.

**Note**  
When pulling an image, if you don't already have the image locally, you will also see `GetDownloadUrlForLayer` references in the CloudTrail logs.

```
{
    "eventVersion": "1.04",
    "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:account_name",
    "arn": "arn:aws:sts::123456789012:user/Mary_Major",
    "accountId": "123456789012",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"userName": "Mary_Major",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2019-04-15T16:42:14Z"
			}
		}
	},
	"eventTime": "2019-04-15T17:23:20Z",
	"eventSource": "ecr.amazonaws.com",
	"eventName": "BatchGetImage",
	"awsRegion": "us-east-2",
	"sourceIPAddress": "ecr.amazonaws.com",
	"userAgent": "ecr.amazonaws.com",
	"requestParameters": {
		"imageIds": [{
			"imageTag": "latest"
		}],
		"acceptedMediaTypes": [
			"application/json",
			"application/vnd.oci.image.manifest.v1+json",
			"application/vnd.oci.image.index.v1+json",
			"application/vnd.docker.distribution.manifest.v2+json",
			"application/vnd.docker.distribution.manifest.list.v2+json",
			"application/vnd.docker.distribution.manifest.v1+prettyjws"
		],
		"repositoryName": "testrepo",
		"registryId": "123456789012"
	},
	"responseElements": null,
	"requestID": "2a1b97ee-5fa3-11e9-a8cd-cd2391aeda93",
	"eventID": "c84f5880-c2f9-4585-9757-28fa5c1065df",
	"resources": [{
		"ARN": "arn:aws:ecr:us-east-2:123456789012:repository/testrepo",
		"accountId": "123456789012"
	}],
	"eventType": "AwsApiCall",
	"recipientAccountId": "123456789012"
}
```

##### Example: Image lifecycle policy action
<a name="cloudtrail-examples-lcp"></a>

The following example shows a CloudTrail log entry that demonstrates when an image is expired due to a lifecycle policy rule. This event type can be located by filtering for `PolicyExecutionEvent` for the event name field.

When you test a lifecycle policy preview, Amazon ECR generates a CloudTrail log entry with the event name field of `DryRunEvent`, with the exact same structure as the `PolicyExecutionEvent`. By changing the event name to `DryRunEvent`, you can filter on dry run events instead.

**Important**  
Due to the size limitations of individual CloudTrail events, for lifecycle policy actions where 10 or more images are expired Amazon ECR sends multiple events to CloudTrail. Additionally, Amazon ECR includes a maximum of 100 tags per image.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "accountId": "123456789012",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2020-03-12T20:22:12Z",
    "eventSource": "ecr.amazonaws.com",
    "eventName": "PolicyExecutionEvent",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "9354dd7f-9aac-4e9d-956d-12561a4923aa",
    "readOnly": true,
    "resources": [
        {
            "ARN": "arn:aws:ecr:us-west-2:123456789012:repository/testrepo",
            "accountId": "123456789012",
            "type": "AWS::ECR::Repository"
        }
    ],
    "eventType": "AwsServiceEvent",
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "repositoryName": "testrepo",
        "lifecycleEventPolicy": {
            "lifecycleEventRules": [
                {
                    "rulePriority": 1,
                    "description": "remove all images > 2",
                    "lifecycleEventSelection": {
                        "tagStatus": "Any",
                        "tagPrefixList": [],
                        "countType": "Image count more than",
                        "countNumber": 2
                    },
                    "action": "expire"
                }
            ],
            "lastEvaluatedAt": 0,
            "policyVersion": 1,
            "policyId": "ceb86829-58e7-9498-920c-aa042e33037b"
        },
        "lifecycleEventImageActions": [
            {
                "lifecycleEventImage": {
                    "digest": "sha256:ddba4d27a7ffc3f86dd6c2f92041af252a1f23a8e742c90e6e1297bfa1bc0c45",
                    "tagStatus": "Tagged",
                    "tagList": [
                        "alpine"
                    ],
                    "pushedAt": 1584042813000
                },
                "rulePriority": 1
            },
            {
                "lifecycleEventImage": {
                    "digest": "sha256:6ab380c5a5acf71c1b6660d645d2cd79cc8ce91b38e0352cbf9561e050427baf",
                    "tagStatus": "Tagged",
                    "tagList": [
                        "centos"
                    ],
                    "pushedAt": 1584042842000
                },
                "rulePriority": 1
            }
        ],
        "lifecycleEventFailureDetails": [
            {
                "lifecycleEventImage": {
                    "digest": "sha256:9117e1bc28cd20751e584b4ccd19b1178d14cf02d134b04ce6be0cc51bff762a",
                    "tagStatus": "Untagged",
                    "tagList": [],
                    "pushedAt": 1584042844000
                },
                "rulePriority": 1,
                "failureCode": "ImageReferencedByManifestList",
                "failureReason": "Requested image referenced by manifest list: [sha256:4b27c83d44a18c31543039d9e8b2786043ec6c8d00804d5800c5148d6b6f65bc]"
            }
        ]
    }
}
```

##### Example: Image archival action
<a name="cloudtrail-examples-image-archive"></a>

The following example shows a CloudTrail log entry that demonstrates an image being archived using the `UpdateImageStorageClass` action with `targetStorageClass` set to `ARCHIVE`.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:account_name",
        "arn": "arn:aws:sts::123456789012:user/Mary_Major",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"userName": "Mary_Major",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2019-04-15T16:42:14Z"
			}
		}
	},
	"eventTime": "2019-04-15T16:45:00Z",
	"eventSource": "ecr.amazonaws.com",
	"eventName": "UpdateImageStorageClass",
	"awsRegion": "us-east-2",
	"sourceIPAddress": "AWS Internal",
	"userAgent": "AWS Internal",
	"requestParameters": {
		"repositoryName": "testrepo",
		"imageId": {
			"imageDigest": "sha256:98c8b060c21d9adbb6b8c41b916e95e6307102786973ab93a41e8b86d1fc6d3e"
		},
		"targetStorageClass": "ARCHIVE",
		"registryId": "123456789012"
	},
	"responseElements": {
		"image": {
			"registryId": "123456789012",
			"repositoryName": "testrepo",
			"imageId": {
				"imageDigest": "sha256:98c8b060c21d9adbb6b8c41b916e95e6307102786973ab93a41e8b86d1fc6d3e"
			},
			"imageStatus": "ARCHIVED"
		}
	},
	"requestID": "cf044b7d-EXAMPLE",
	"eventID": "2bfd4ee2-EXAMPLE",
	"readOnly": false,
	"resources": [{
		"ARN": "arn:aws:ecr:us-east-2:123456789012:repository/testrepo",
		"accountId": "123456789012"
	}],
	"eventType": "AwsApiCall",
	"managementEvent": true,
	"recipientAccountId": "123456789012",
	"eventCategory": "Management"
}
```

##### Example: Image restore action
<a name="cloudtrail-examples-image-restore"></a>

The following examples show CloudTrail log entries that demonstrate an image being restored. When you restore an archived image, two events are generated:

1. An API call event when the restore is initiated

1. A service event when the asynchronous restore operation completes

**API call event (restore initiation)**

The following example shows the initial API call to restore an image using the `UpdateImageStorageClass` action with `targetStorageClass` set to `STANDARD`. The response shows the image status as `ACTIVATING`.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:account_name",
        "arn": "arn:aws:sts::123456789012:user/Mary_Major",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"userName": "Mary_Major",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2019-04-15T16:42:14Z"
			}
		}
	},
	"eventTime": "2019-04-15T16:45:00Z",
	"eventSource": "ecr.amazonaws.com",
	"eventName": "UpdateImageStorageClass",
	"awsRegion": "us-east-2",
	"sourceIPAddress": "AWS Internal",
	"userAgent": "AWS Internal",
	"requestParameters": {
		"repositoryName": "testrepo",
		"imageId": {
			"imageDigest": "sha256:98c8b060c21d9adbb6b8c41b916e95e6307102786973ab93a41e8b86d1fc6d3e"
		},
		"targetStorageClass": "STANDARD",
		"registryId": "123456789012"
	},
	"responseElements": {
		"image": {
			"registryId": "123456789012",
			"repositoryName": "testrepo",
			"imageId": {
				"imageDigest": "sha256:98c8b060c21d9adbb6b8c41b916e95e6307102786973ab93a41e8b86d1fc6d3e"
			},
			"imageStatus": "ACTIVATING"
		}
	},
	"requestID": "cf044b7d-EXAMPLE",
	"eventID": "2bfd4ee2-EXAMPLE",
	"readOnly": false,
	"resources": [{
		"ARN": "arn:aws:ecr:us-east-2:123456789012:repository/testrepo",
		"accountId": "123456789012"
	}],
	"eventType": "AwsApiCall",
	"managementEvent": true,
	"recipientAccountId": "123456789012",
	"eventCategory": "Management"
}
```

**Service event (restore completion)**

The following example shows the service event generated when the asynchronous restore operation completes. This event type can be located by filtering for `ImageActivationEvent` for the event name field. The `serviceEventDetails` section contains the restore result and final image status.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "123456789012",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2020-03-12T20:22:12Z",
    "eventSource": "ecr.amazonaws.com",
    "eventName": "ImageActivationEvent",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "9354dd7f-EXAMPLE",
    "readOnly": true,
    "resources": [
        {
            "ARN": "arn:aws:ecr:us-west-2:123456789012:repository/testrepo",
            "accountId": "123456789012",
            "type": "AWS::ECR::Repository"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "repositoryName": "testrepo",
        "imageDigest": "sha256:98c8b060c21d9adbb6b8c41b916e95e6307102786973ab93a41e8b86d1fc6d3e",
        "targetStorageClass": "STANDARD",
        "result": "SUCCESS",
        "imageStatus": "ACTIVE"
    },
    "eventCategory": "Management"
}
```

##### Example: Image referrers action
<a name="cloudtrail-examples-image-referrers-action"></a>

The following example shows a AWS CloudTrail log entry that demonstrates when an OCI 1.1 compliant client fetches a list of referrers, or reference artifacts, for an image using the `Referrers` API.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:account_name",
        "arn": "arn:aws:sts::123456789012:user/Mary_Major",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2024-10-08T16:38:39Z",
                "mfaAuthenticated": "false"
            },
            "ec2RoleDelivery": "2.0"
        },
        "invokedBy": "ecr.amazonaws.com"
    },
    "eventTime": "2024-10-08T17:22:51Z",
    "eventSource": "ecr.amazonaws.com",
    "eventName": "ListImageReferrers",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "ecr.amazonaws.com",
    "userAgent": "ecr.amazonaws.com",
    "requestParameters": {
        "registryId": "123456789012",
        "repositoryName": "testrepo",
        "subjectId": {
            "imageDigest": "sha256:000b9b805af1cdb60628898c9f411996301a1c13afd3dbef1d8a16ac6dbf503a"
        },
        "nextToken": "urD72mdD/mC8b5-EXAMPLE"
    },
    "responseElements": null,
    "requestID": "cb8c167e-EXAMPLE",
    "eventID": "e3c6f4ce-EXAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123456789012",
            "ARN": "arn:aws:ecr:us-east-2:123456789012:repository/testrepo"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

# Using Amazon ECR with an AWS SDK
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

For examples specific to Amazon ECR, see [Code examples for Amazon ECR using AWS SDKs](#service_code_examples).

**Example availability**  
Can't find what you need? Request a code example by using the **Provide feedback** link at the bottom of this page.

# Code examples for Amazon ECR using AWS SDKs
<a name="service_code_examples"></a>

The following code examples show how to use Amazon ECR with an AWS software development kit (SDK). 

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

**Contents**
+ [Basics](#service_code_examples_basics)
  + [Hello Amazon ECR](#example_ecr_Hello_section)
  + [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section)
  + [Actions](#service_code_examples_actions)
    + [`CreateRepository`](#example_ecr_CreateRepository_section)
    + [`DeleteRepository`](#example_ecr_DeleteRepository_section)
    + [`DescribeImages`](#example_ecr_DescribeImages_section)
    + [`DescribeRepositories`](#example_ecr_DescribeRepositories_section)
    + [`GetAuthorizationToken`](#example_ecr_GetAuthorizationToken_section)
    + [`GetRepositoryPolicy`](#example_ecr_GetRepositoryPolicy_section)
    + [`ListImages`](#example_ecr_ListImages_section)
    + [`PushImageCmd`](#example_ecr_PushImageCmd_section)
    + [`PutLifeCyclePolicy`](#example_ecr_PutLifeCyclePolicy_section)
    + [`SetRepositoryPolicy`](#example_ecr_SetRepositoryPolicy_section)
    + [`StartLifecyclePolicyPreview`](#example_ecr_StartLifecyclePolicyPreview_section)
+ [Scenarios](#service_code_examples_scenarios)
  + [Getting started with container registries](#example_ecr_GettingStarted_078_section)

## Basic examples for Amazon ECR using AWS SDKs
<a name="service_code_examples_basics"></a>

The following code examples show how to use the basics of Amazon Elastic Container Registry with AWS SDKs. 

**Contents**
+ [Hello Amazon ECR](#example_ecr_Hello_section)
+ [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section)
+ [Actions](#service_code_examples_actions)
  + [`CreateRepository`](#example_ecr_CreateRepository_section)
  + [`DeleteRepository`](#example_ecr_DeleteRepository_section)
  + [`DescribeImages`](#example_ecr_DescribeImages_section)
  + [`DescribeRepositories`](#example_ecr_DescribeRepositories_section)
  + [`GetAuthorizationToken`](#example_ecr_GetAuthorizationToken_section)
  + [`GetRepositoryPolicy`](#example_ecr_GetRepositoryPolicy_section)
  + [`ListImages`](#example_ecr_ListImages_section)
  + [`PushImageCmd`](#example_ecr_PushImageCmd_section)
  + [`PutLifeCyclePolicy`](#example_ecr_PutLifeCyclePolicy_section)
  + [`SetRepositoryPolicy`](#example_ecr_SetRepositoryPolicy_section)
  + [`StartLifecyclePolicyPreview`](#example_ecr_StartLifecyclePolicyPreview_section)

### Hello Amazon ECR
<a name="example_ecr_Hello_section"></a>

The following code examples show how to get started using Amazon ECR.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ecr.EcrClient;
import software.amazon.awssdk.services.ecr.model.EcrException;
import software.amazon.awssdk.services.ecr.model.ListImagesRequest;
import software.amazon.awssdk.services.ecr.paginators.ListImagesIterable;

public class HelloECR {

    public static void main(String[] args) {
        final String usage = """
            Usage:    <repositoryName> 

            Where:
               repositoryName - The name of the Amazon ECR repository. 
            """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String repoName = args[0];
        EcrClient ecrClient = EcrClient.builder()
            .region(Region.US_EAST_1)
            .build();

        listImageTags(ecrClient, repoName);
    }
    public static void listImageTags(EcrClient ecrClient, String repoName){
        ListImagesRequest listImagesPaginator = ListImagesRequest.builder()
            .repositoryName(repoName)
            .build();

        ListImagesIterable imagesIterable = ecrClient.listImagesPaginator(listImagesPaginator);
        imagesIterable.stream()
            .flatMap(r -> r.imageIds().stream())
            .forEach(image -> System.out.println("The docker image tag is: " +image.imageTag()));
    }
}
```
+  For API details, see [listImages](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/listImages) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
import aws.sdk.kotlin.services.ecr.EcrClient
import aws.sdk.kotlin.services.ecr.model.ListImagesRequest
import kotlin.system.exitProcess

suspend fun main(args: Array<String>) {
    val usage = """
            Usage: <repositoryName> 

            Where:
               repositoryName - The name of the Amazon ECR repository. 
            
    """.trimIndent()

    if (args.size != 1) {
        println(usage)
        exitProcess(1)
    }

    val repoName = args[0]
    listImageTags(repoName)
}

suspend fun listImageTags(repoName: String?) {
    val listImages =
        ListImagesRequest {
            repositoryName = repoName
        }

    EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
        val imageResponse = ecrClient.listImages(listImages)
        imageResponse.imageIds?.forEach { imageId ->
            println("Image tag: ${imageId.imageTag}")
        }
    }
}
```
+  For API details, see [listImages](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
import boto3
import argparse
from boto3 import client


def hello_ecr(ecr_client: client, repository_name: str) -> None:
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Elastic Container Registry (Amazon ECR)
    client and list the images in a repository.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param ecr_client: A Boto3 Amazon ECR Client object. This object wraps
                             the low-level Amazon ECR service API.
    :param repository_name: The name of an Amazon ECR repository in your account.
    """
    print(
        f"Hello, Amazon ECR! Let's list some images in the repository '{repository_name}':\n"
    )
    paginator = ecr_client.get_paginator("list_images")
    page_iterator = paginator.paginate(
        repositoryName=repository_name, PaginationConfig={"MaxItems": 10}
    )

    image_names: [str] = []
    for page in page_iterator:
        for schedule in page["imageIds"]:
            image_names.append(schedule["imageTag"])

    print(f"{len(image_names)} image(s) retrieved.")
    for schedule_name in image_names:
        print(f"\t{schedule_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run hello Amazon ECR.")
    parser.add_argument(
        "--repository-name",
        type=str,
        help="the name of an Amazon ECR repository in your account.",
        required=True,
    )
    args = parser.parse_args()

    hello_ecr(boto3.client("ecr"), args.repository_name)
```
+  For API details, see [listImages](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/listImages) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

### Learn the basics of Amazon ECR with an AWS SDK
<a name="example_ecr_Scenario_RepositoryManagement_section"></a>

The following code examples show how to:
+ Create an Amazon ECR repository.
+ Set repository policies.
+ Retrieve repository URIs.
+ Get Amazon ECR authorization tokens.
+ Set lifecycle policies for Amazon ECR repositories.
+ Push a Docker image to an Amazon ECR repository.
+ Verify the existence of an image in an Amazon ECR repository.
+ List Amazon ECR repositories for your account and get details about them.
+ Delete Amazon ECR repositories.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 
Run an interactive scenario demonstrating Amazon ECR features.  

```
import software.amazon.awssdk.services.ecr.model.EcrException;
import software.amazon.awssdk.services.ecr.model.RepositoryPolicyNotFoundException;

import java.util.Scanner;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * This Java code example requires an IAM Role that has permissions to interact with the Amazon ECR service.
 *
 * To create an IAM role, see:
 *
 * https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html
 *
 * This Java scenario example requires a local docker image named echo-text. Without a local image,
 * this Java program will not successfully run. For more information including how to create the local
 * image, see:
 *
 * /scenarios/basics/ecr/README
 *
 */
public class ECRScenario {
    public static final String DASHES = new String(new char[80]).replace("\0", "-");
    public static void main(String[] args) {
        final String usage = """
            Usage: <iamRoleARN> <accountId>

            Where:
               iamRoleARN - The IAM role ARN that has the necessary permissions to access and manage the Amazon ECR repository.
               accountId - Your AWS account number. 
            """;

        if (args.length != 2) {
            System.out.println(usage);
            return;
        }

        ECRActions ecrActions = new ECRActions();
        String iamRole = args[0];
        String accountId = args[1];
        String localImageName;

        Scanner scanner = new Scanner(System.in);
        System.out.println("""
             The Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry 
             service provided by AWS. It allows developers and organizations to securely 
             store, manage, and deploy Docker container images. 
             ECR provides a simple and scalable way to manage container images throughout their lifecycle, 
             from building and testing to production deployment.\s
                         
             The `EcrAsyncClient` interface in the AWS SDK for Java 2.x provides a set of methods to 
             programmatically interact with the Amazon ECR service. This allows developers to 
             automate the storage, retrieval, and management of container images as part of their application 
             deployment pipelines. With ECR, teams can focus on building and deploying their 
             applications without having to worry about the underlying infrastructure required to 
             host and manage a container registry.
             
            This scenario walks you through how to perform key operations for this service.  
            Let's get started...
                       
            You have two choices:
            1 - Run the entire program.
            2 - Delete an existing Amazon ECR repository named echo-text (created from a previous execution of 
            this program that did not complete).
            """);

        while (true) {
            String input = scanner.nextLine();
            if (input.trim().equalsIgnoreCase("1")) {
                System.out.println("Continuing with the program...");
                System.out.println("");
                break;
            } else if (input.trim().equalsIgnoreCase("2")) {
                String repoName = "echo-text";
                ecrActions.deleteECRRepository(repoName);
                return;
            } else {
                // Handle invalid input.
                System.out.println("Invalid input. Please try again.");
            }
        }

        waitForInputToContinue(scanner);
        System.out.println(DASHES);

        System.out.println("""
           1. Create an ECR repository.
            
           The first task is to ensure we have a local Docker image named echo-text. 
           If this image exists, then an Amazon ECR repository is created. 
           
           An ECR repository is a private Docker container repository provided 
           by Amazon Web Services (AWS). It is a managed service that makes it easy 
           to store, manage, and deploy Docker container images.\s
           """ );

        // Ensure that a local docker image named echo-text exists.
        boolean doesExist = ecrActions.isEchoTextImagePresent();
        String repoName;
        if (!doesExist){
            System.out.println("The local image named echo-text does not exist");
            return;
        } else {
            localImageName = "echo-text";
            repoName = "echo-text";
        }

        try {
            String repoArn = ecrActions.createECRRepository(repoName);
            System.out.println("The ARN of the ECR repository is " + repoArn);

        } catch (IllegalArgumentException e) {
            System.err.println("Invalid repository name: " + e.getMessage());
            return;
        } catch (RuntimeException e) {
            System.err.println("An error occurred while creating the ECR repository: " + e.getMessage());
            e.printStackTrace();
            return;
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("""
        2. Set an ECR repository policy.
        
        Setting an ECR repository policy using the `setRepositoryPolicy` function is crucial for maintaining
        the security and integrity of your container images. The repository policy allows you to 
        define specific rules and restrictions for accessing and managing the images stored within your ECR 
        repository.    
        """);
        waitForInputToContinue(scanner);
        try {
            ecrActions.setRepoPolicy(repoName, iamRole);

        } catch (RepositoryPolicyNotFoundException e) {
            System.err.println("Invalid repository name: " + e.getMessage());
            return;
        } catch (EcrException e) {
            System.err.println("An ECR exception occurred: " + e.getMessage());
            return;
        } catch (RuntimeException e) {
            System.err.println("An error occurred while creating the ECR repository: " + e.getMessage());
            return;
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("""
        3. Display ECR repository policy.
       
        Now we will retrieve the ECR policy to ensure it was successfully set.   
        """);
        waitForInputToContinue(scanner);
        try {
            String policyText = ecrActions.getRepoPolicy(repoName);
            System.out.println("Policy Text:");
            System.out.println(policyText);

        } catch (EcrException e) {
            System.err.println("An ECR exception occurred: " + e.getMessage());
            return;
        } catch (RuntimeException e) {
            System.err.println("An error occurred while creating the ECR repository: " + e.getMessage());
            return;
        }

        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("""
        4. Retrieve an ECR authorization token.
       
        You need an authorization token to securely access and interact with the Amazon ECR registry. 
        The `getAuthorizationToken` method of the `EcrAsyncClient` is responsible for securely accessing 
        and interacting with an Amazon ECR repository. This operation is responsible for obtaining a 
        valid authorization token, which is required to authenticate your requests to the ECR service. 
        
        Without a valid authorization token, you would not be able to perform any operations on the 
        ECR repository, such as pushing, pulling, or managing your Docker images.    
        """);
        waitForInputToContinue(scanner);
        try {
             ecrActions.getAuthToken();

        } catch (EcrException e) {
            System.err.println("An ECR exception occurred: " + e.getMessage());
            return;
        } catch (RuntimeException e) {
            System.err.println("An error occurred while retrieving the authorization token: " + e.getMessage());
            return;
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("""
        5. Get the ECR Repository URI.
                    
        The URI  of an Amazon ECR repository is important. When you want to deploy a container image to 
        a container orchestration platform like Amazon Elastic Kubernetes Service (EKS) 
        or Amazon Elastic Container Service (ECS), you need to specify the full image URI, 
        which includes the ECR repository URI. This allows the container runtime to pull the 
        correct container image from the ECR repository.    
       """);
        waitForInputToContinue(scanner);

        try {
            ecrActions.getRepositoryURI(repoName);

        } catch (EcrException e) {
            System.err.println("An ECR exception occurred: " + e.getMessage());
            return;

        } catch (RuntimeException e) {
            System.err.println("An error occurred while retrieving the URI: " + e.getMessage());
            return;
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("""
            6. Set an ECR Lifecycle Policy.
                        
            An ECR Lifecycle Policy is used to manage the lifecycle of Docker images stored in your ECR repositories. 
            These policies allow you to automatically remove old or unused Docker images from your repositories, 
            freeing up storage space and reducing costs.    
                    
            This example policy helps to maintain the size and efficiency of the container registry
            by automatically removing older and potentially unused images, ensuring that the 
            storage is optimized and the registry remains up-to-date.
            """);
        waitForInputToContinue(scanner);
        try {
            ecrActions.setLifeCyclePolicy(repoName);

        } catch (RuntimeException e) {
            System.err.println("An error occurred while setting the lifecycle policy: " + e.getMessage());
            e.printStackTrace();
            return;
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("""
        7. Push a docker image to the Amazon ECR Repository.
            
        The `pushImageCmd()` method pushes a local Docker image to an Amazon ECR repository.
        It sets up the Docker client by connecting to the local Docker host using the default port.
        It then retrieves the authorization token for the ECR repository by making a call to the AWS SDK.
            
        The method uses the authorization token to create an `AuthConfig` object, which is used to authenticate
        the Docker client when pushing the image. Finally, the method tags the Docker image with the specified
        repository name and image tag, and then pushes the image to the ECR repository using the Docker client.
        If the push operation is successful, the method prints a message indicating that the image was pushed to ECR.
        """);
        waitForInputToContinue(scanner);

        try {
            ecrActions.pushDockerImage(repoName, localImageName);

        } catch (RuntimeException e) {
            System.err.println("An error occurred while pushing a local Docker image to Amazon ECR: " + e.getMessage());
            e.printStackTrace();
            return;
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("8. Verify if the image is in the ECR Repository.");
        waitForInputToContinue(scanner);
        try {
            ecrActions.verifyImage(repoName, localImageName);

        } catch (EcrException e) {
            System.err.println("An ECR exception occurred: " + e.getMessage());
            return;
        } catch (RuntimeException e) {
            System.err.println("An error occurred " + e.getMessage());
            e.printStackTrace();
            return;
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("9. As an optional step, you can interact with the image in Amazon ECR by using the CLI.");
        System.out.println("Would you like to view instructions on how to use the CLI to run the image? (y/n)");
        String ans = scanner.nextLine().trim();
        if (ans.equalsIgnoreCase("y")) {
            String instructions = """
            1. Authenticate with ECR - Before you can pull the image from Amazon ECR, you need to authenticate with the registry. You can do this using the AWS CLI:

                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin %s.dkr.ecr.us-east-1.amazonaws.com

            2. Describe the image using this command:

               aws ecr describe-images --repository-name %s --image-ids imageTag=%s

            3. Run the Docker container and view the output using this command:

               docker run --rm %s.dkr.ecr.us-east-1.amazonaws.com/%s:%s
            """;

            instructions = String.format(instructions, accountId, repoName, localImageName, accountId, repoName, localImageName);
            System.out.println(instructions);
        }
        waitForInputToContinue(scanner);

        System.out.println(DASHES);
        System.out.println("10. Delete the ECR Repository.");
        System.out.println(
        """
        If the repository isn't empty, you must either delete the contents of the repository 
        or use the force option (used in this scenario) to delete the repository and have Amazon ECR delete all of its contents 
        on your behalf.
        """);
        System.out.println("Would you like to delete the Amazon ECR Repository? (y/n)");
        String delAns = scanner.nextLine().trim();
        if (delAns.equalsIgnoreCase("y")) {
            System.out.println("You selected to delete the AWS ECR resources.");

            try {
                ecrActions.deleteECRRepository(repoName);

            } catch (EcrException e) {
                System.err.println("An ECR exception occurred: " + e.getMessage());
                return;
            } catch (RuntimeException e) {
                System.err.println("An error occurred while deleting the Docker image: " + e.getMessage());
                e.printStackTrace();
                return;
            }
        }

        System.out.println(DASHES);
        System.out.println("This concludes the Amazon ECR SDK scenario");
        System.out.println(DASHES);
    }

   private static void waitForInputToContinue(Scanner scanner) {
       while (true) {
           System.out.println("");
           System.out.println("Enter 'c' followed by <ENTER> to continue:");
           String input = scanner.nextLine();

           if (input.trim().equalsIgnoreCase("c")) {
               System.out.println("Continuing with the program...");
               System.out.println("");
               break;
           } else {
               // Handle invalid input.
               System.out.println("Invalid input. Please try again.");
          }
       }
   }
}
```
A wrapper class for Amazon ECR SDK methods.  

```
import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.api.exception.DockerClientException;
import com.github.dockerjava.api.model.AuthConfig;
import com.github.dockerjava.api.model.Image;
import com.github.dockerjava.core.DockerClientBuilder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
import software.amazon.awssdk.http.async.SdkAsyncHttpClient;
import software.amazon.awssdk.http.nio.netty.NettyNioAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ecr.EcrAsyncClient;
import software.amazon.awssdk.services.ecr.model.AuthorizationData;
import software.amazon.awssdk.services.ecr.model.CreateRepositoryRequest;
import software.amazon.awssdk.services.ecr.model.CreateRepositoryResponse;
import software.amazon.awssdk.services.ecr.model.DeleteRepositoryRequest;
import software.amazon.awssdk.services.ecr.model.DeleteRepositoryResponse;
import software.amazon.awssdk.services.ecr.model.DescribeImagesRequest;
import software.amazon.awssdk.services.ecr.model.DescribeImagesResponse;
import software.amazon.awssdk.services.ecr.model.DescribeRepositoriesRequest;
import software.amazon.awssdk.services.ecr.model.DescribeRepositoriesResponse;
import software.amazon.awssdk.services.ecr.model.EcrException;
import software.amazon.awssdk.services.ecr.model.GetAuthorizationTokenResponse;
import software.amazon.awssdk.services.ecr.model.GetRepositoryPolicyRequest;
import software.amazon.awssdk.services.ecr.model.GetRepositoryPolicyResponse;
import software.amazon.awssdk.services.ecr.model.ImageIdentifier;
import software.amazon.awssdk.services.ecr.model.Repository;
import software.amazon.awssdk.services.ecr.model.RepositoryPolicyNotFoundException;
import software.amazon.awssdk.services.ecr.model.SetRepositoryPolicyRequest;
import software.amazon.awssdk.services.ecr.model.SetRepositoryPolicyResponse;
import software.amazon.awssdk.services.ecr.model.StartLifecyclePolicyPreviewRequest;
import software.amazon.awssdk.services.ecr.model.StartLifecyclePolicyPreviewResponse;
import com.github.dockerjava.api.command.DockerCmdExecFactory;
import com.github.dockerjava.netty.NettyDockerCmdExecFactory;
import java.time.Duration;
import java.util.Base64;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionException;

public class ECRActions {
    private static EcrAsyncClient ecrClient;

    private static DockerClient dockerClient;

    private static Logger logger = LoggerFactory.getLogger(ECRActions.class);

    /**
     * Creates an Amazon Elastic Container Registry (Amazon ECR) repository.
     *
     * @param repoName the name of the repository to create.
     * @return the Amazon Resource Name (ARN) of the created repository, or an empty string if the operation failed.
     * @throws IllegalArgumentException     If repository name is invalid.
     * @throws RuntimeException             if an error occurs while creating the repository.
     */
    public String createECRRepository(String repoName) {
        if (repoName == null || repoName.isEmpty()) {
            throw new IllegalArgumentException("Repository name cannot be null or empty");
        }

        CreateRepositoryRequest request = CreateRepositoryRequest.builder()
            .repositoryName(repoName)
            .build();

        CompletableFuture<CreateRepositoryResponse> response = getAsyncClient().createRepository(request);
        try {
            CreateRepositoryResponse result = response.join();
            if (result != null) {
                System.out.println("The " + repoName + " repository was created successfully.");
                return result.repository().repositoryArn();
            } else {
                throw new RuntimeException("Unexpected response type");
            }
        } catch (CompletionException e) {
            Throwable cause = e.getCause();
            if (cause instanceof EcrException ex) {
                if ("RepositoryAlreadyExistsException".equals(ex.awsErrorDetails().errorCode())) {
                    System.out.println("The Amazon ECR repository already exists, moving on...");
                    DescribeRepositoriesRequest describeRequest = DescribeRepositoriesRequest.builder()
                        .repositoryNames(repoName)
                        .build();
                    DescribeRepositoriesResponse describeResponse = getAsyncClient().describeRepositories(describeRequest).join();
                    return describeResponse.repositories().get(0).repositoryArn();
                } else {
                    throw new RuntimeException(ex);
                }
            } else {
                throw new RuntimeException(e);
            }
        }
    }

    /**
     * Deletes an ECR (Elastic Container Registry) repository.
     *
     * @param repoName the name of the repository to delete.
     * @throws IllegalArgumentException if the repository name is null or empty.
     * @throws EcrException if there is an error deleting the repository.
     * @throws RuntimeException if an unexpected error occurs during the deletion process.
     */
    public void deleteECRRepository(String repoName) {
        if (repoName == null || repoName.isEmpty()) {
            throw new IllegalArgumentException("Repository name cannot be null or empty");
        }

        DeleteRepositoryRequest repositoryRequest = DeleteRepositoryRequest.builder()
            .force(true)
            .repositoryName(repoName)
            .build();

        CompletableFuture<DeleteRepositoryResponse> response = getAsyncClient().deleteRepository(repositoryRequest);
        response.whenComplete((deleteRepositoryResponse, ex) -> {
            if (deleteRepositoryResponse != null) {
                System.out.println("You have successfully deleted the " + repoName + " repository");
            } else {
                Throwable cause = ex.getCause();
                if (cause instanceof EcrException) {
                    throw (EcrException) cause;
                } else {
                    throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                }
            }
        });

        // Wait for the CompletableFuture to complete
        response.join();
    }



    private static DockerClient getDockerClient() {
        String osName = System.getProperty("os.name");
        if (osName.startsWith("Windows")) {
            // Make sure Docker Desktop is running.
            String dockerHost = "tcp://localhost:2375"; // Use the Docker Desktop default port.
            DockerCmdExecFactory dockerCmdExecFactory = new NettyDockerCmdExecFactory().withReadTimeout(20000).withConnectTimeout(20000);
            dockerClient = DockerClientBuilder.getInstance(dockerHost).withDockerCmdExecFactory(dockerCmdExecFactory).build();
        } else {
            dockerClient = DockerClientBuilder.getInstance().build();
        }
        return dockerClient;
    }

    /**
     * Retrieves an asynchronous Amazon Elastic Container Registry (ECR) client.
     *
     * @return the configured ECR asynchronous client.
     */
    private static EcrAsyncClient getAsyncClient() {

        /*
         The `NettyNioAsyncHttpClient` class is part of the AWS SDK for Java, version 2,
         and it is designed to provide a high-performance, asynchronous HTTP client for interacting with AWS services.
         It uses the Netty framework to handle the underlying network communication and the Java NIO API to
         provide a non-blocking, event-driven approach to HTTP requests and responses.
         */
        SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
            .maxConcurrency(50)  // Adjust as needed.
            .connectionTimeout(Duration.ofSeconds(60))  // Set the connection timeout.
            .readTimeout(Duration.ofSeconds(60))  // Set the read timeout.
            .writeTimeout(Duration.ofSeconds(60))  // Set the write timeout.
            .build();

        ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
            .apiCallTimeout(Duration.ofMinutes(2))  // Set the overall API call timeout.
            .apiCallAttemptTimeout(Duration.ofSeconds(90))  // Set the individual call attempt timeout.
            .build();

        if (ecrClient == null) {
            ecrClient = EcrAsyncClient.builder()
                .region(Region.US_EAST_1)
                .httpClient(httpClient)
                .overrideConfiguration(overrideConfig)
                .build();
        }
        return ecrClient;
    }

    /**
     * Sets the lifecycle policy for the specified repository.
     *
     * @param repoName the name of the repository for which to set the lifecycle policy.
     */
    public void setLifeCyclePolicy(String repoName) {
        /*
           This policy helps to maintain the size and efficiency of the container registry
           by automatically removing older and potentially unused images,
           ensuring that the storage is optimized and the registry remains up-to-date.
         */
        String polText = """
             {
             "rules": [
                 {
                     "rulePriority": 1,
                     "description": "Expire images older than 14 days",
                     "selection": {
                         "tagStatus": "any",
                         "countType": "sinceImagePushed",
                         "countUnit": "days",
                         "countNumber": 14
                     },
                     "action": {
                         "type": "expire"
                     }
                 }
            ]
            }
            """;

        StartLifecyclePolicyPreviewRequest lifecyclePolicyPreviewRequest = StartLifecyclePolicyPreviewRequest.builder()
            .lifecyclePolicyText(polText)
            .repositoryName(repoName)
            .build();

        CompletableFuture<StartLifecyclePolicyPreviewResponse> response = getAsyncClient().startLifecyclePolicyPreview(lifecyclePolicyPreviewRequest);
        response.whenComplete((lifecyclePolicyPreviewResponse, ex) -> {
            if (lifecyclePolicyPreviewResponse != null) {
                System.out.println("Lifecycle policy preview started successfully.");
            } else {
                if (ex.getCause() instanceof EcrException) {
                    throw (EcrException) ex.getCause();
                } else {
                    String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                    throw new RuntimeException(errorMessage, ex);
                }
            }
        });
        // Wait for the CompletableFuture to complete.
        response.join();
    }

    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     * @throws EcrException             if there is an error retrieving the image information from Amazon ECR.
     * @throws CompletionException      if the asynchronous operation completes exceptionally.
     */
    public void verifyImage(String repositoryName, String imageTag) {
        DescribeImagesRequest request = DescribeImagesRequest.builder()
            .repositoryName(repositoryName)
            .imageIds(ImageIdentifier.builder().imageTag(imageTag).build())
            .build();

        CompletableFuture<DescribeImagesResponse> response = getAsyncClient().describeImages(request);
        response.whenComplete((describeImagesResponse, ex) -> {
            if (ex != null) {
                if (ex instanceof CompletionException) {
                    Throwable cause = ex.getCause();
                    if (cause instanceof EcrException) {
                        throw (EcrException) cause;
                    } else {
                        throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                    }
                } else {
                    throw new RuntimeException("Unexpected error: " + ex.getCause());
                }
            } else if (describeImagesResponse != null && !describeImagesResponse.imageDetails().isEmpty()) {
                System.out.println("Image is present in the repository.");
            } else {
                System.out.println("Image is not present in the repository.");
            }
        });

        // Wait for the CompletableFuture to complete.
        response.join();
    }

    /**
     * Retrieves the repository URI for the specified repository name.
     *
     * @param repoName the name of the repository to retrieve the URI for.
     * @return the repository URI for the specified repository name.
     * @throws EcrException        if there is an error retrieving the repository information.
     * @throws CompletionException if the asynchronous operation completes exceptionally.
     */
    public void getRepositoryURI(String repoName) {
        DescribeRepositoriesRequest request = DescribeRepositoriesRequest.builder()
            .repositoryNames(repoName)
            .build();

        CompletableFuture<DescribeRepositoriesResponse> response = getAsyncClient().describeRepositories(request);
        response.whenComplete((describeRepositoriesResponse, ex) -> {
            if (ex != null) {
                Throwable cause = ex.getCause();
                if (cause instanceof InterruptedException) {
                    Thread.currentThread().interrupt();
                    String errorMessage = "Thread interrupted while waiting for asynchronous operation: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                } else if (cause instanceof EcrException) {
                    throw (EcrException) cause;
                } else {
                    String errorMessage = "Unexpected error: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                }
            } else {
                if (describeRepositoriesResponse != null) {
                    if (!describeRepositoriesResponse.repositories().isEmpty()) {
                        String repositoryUri = describeRepositoriesResponse.repositories().get(0).repositoryUri();
                        System.out.println("Repository URI found: " + repositoryUri);
                    } else {
                        System.out.println("No repositories found for the given name.");
                    }
                } else {
                    System.err.println("No response received from describeRepositories.");
                }
            }
        });
        response.join();
    }

    /**
     * Retrieves the authorization token for Amazon Elastic Container Registry (ECR).
     * This method makes an asynchronous call to the ECR client to retrieve the authorization token.
     * If the operation is successful, the method prints the token to the console.
     * If an exception occurs, the method handles the exception and prints the error message.
     *
     * @throws EcrException     if there is an error retrieving the authorization token from ECR.
     * @throws RuntimeException if there is an unexpected error during the operation.
     */
    public void getAuthToken() {
        CompletableFuture<GetAuthorizationTokenResponse> response = getAsyncClient().getAuthorizationToken();
        response.whenComplete((authorizationTokenResponse, ex) -> {
            if (authorizationTokenResponse != null) {
                AuthorizationData authorizationData = authorizationTokenResponse.authorizationData().get(0);
                String token = authorizationData.authorizationToken();
                if (!token.isEmpty()) {
                    System.out.println("The token was successfully retrieved.");
                }
            } else {
                if (ex.getCause() instanceof EcrException) {
                    throw (EcrException) ex.getCause();
                } else {
                    String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                    throw new RuntimeException(errorMessage, ex); // Rethrow the exception
                }
            }
        });
        response.join();
    }

    /**
     * Gets the repository policy for the specified repository.
     *
     * @param repoName the name of the repository.
     * @throws EcrException if an AWS error occurs while getting the repository policy.
     */
    public String getRepoPolicy(String repoName) {
        if (repoName == null || repoName.isEmpty()) {
            throw new IllegalArgumentException("Repository name cannot be null or empty");
        }

        GetRepositoryPolicyRequest getRepositoryPolicyRequest = GetRepositoryPolicyRequest.builder()
            .repositoryName(repoName)
            .build();

        CompletableFuture<GetRepositoryPolicyResponse> response = getAsyncClient().getRepositoryPolicy(getRepositoryPolicyRequest);
        response.whenComplete((resp, ex) -> {
            if (resp != null) {
                System.out.println("Repository policy retrieved successfully.");
            } else {
                if (ex.getCause() instanceof EcrException) {
                    throw (EcrException) ex.getCause();
                } else {
                    String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                    throw new RuntimeException(errorMessage, ex);
                }
            }
        });

        GetRepositoryPolicyResponse result = response.join();
        return result != null ? result.policyText() : null;
    }

    /**
     * Sets the repository policy for the specified ECR repository.
     *
     * @param repoName the name of the ECR repository.
     * @param iamRole  the IAM role to be granted access to the repository.
     * @throws RepositoryPolicyNotFoundException if the repository policy does not exist.
     * @throws EcrException                      if there is an unexpected error setting the repository policy.
     */
    public void setRepoPolicy(String repoName, String iamRole) {
        /*
          This example policy document grants the specified AWS principal the permission to perform the
          `ecr:BatchGetImage` action. This policy is designed to allow the specified principal
          to retrieve Docker images from the ECR repository.
         */
        String policyDocumentTemplate = """
             {
              "Version":"2012-10-17",		 	 	 
              "Statement" : [ {
                "Sid" : "new statement",
                "Effect" : "Allow",
                "Principal" : {
                  "AWS" : "%s"
                },
                "Action" : "ecr:BatchGetImage"
              } ]
            }
             """;

        String policyDocument = String.format(policyDocumentTemplate, iamRole);
        SetRepositoryPolicyRequest setRepositoryPolicyRequest = SetRepositoryPolicyRequest.builder()
            .repositoryName(repoName)
            .policyText(policyDocument)
            .build();

        CompletableFuture<SetRepositoryPolicyResponse> response = getAsyncClient().setRepositoryPolicy(setRepositoryPolicyRequest);
        response.whenComplete((resp, ex) -> {
            if (resp != null) {
                System.out.println("Repository policy set successfully.");
            } else {
                Throwable cause = ex.getCause();
                if (cause instanceof RepositoryPolicyNotFoundException) {
                    throw (RepositoryPolicyNotFoundException) cause;
                } else if (cause instanceof EcrException) {
                    throw (EcrException) cause;
                } else {
                    String errorMessage = "Unexpected error: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                }
            }
        });
        response.join();
    }

    /**
     * Pushes a Docker image to an Amazon Elastic Container Registry (ECR) repository.
     *
     * @param repoName  the name of the ECR repository to push the image to.
     * @param imageName the name of the Docker image.
     */
    public void pushDockerImage(String repoName, String imageName) {
        System.out.println("Pushing " + imageName + " to Amazon ECR will take a few seconds.");
        CompletableFuture<AuthConfig> authResponseFuture = getAsyncClient().getAuthorizationToken()
            .thenApply(response -> {
                String token = response.authorizationData().get(0).authorizationToken();
                String decodedToken = new String(Base64.getDecoder().decode(token));
                String password = decodedToken.substring(4);

                DescribeRepositoriesResponse descrRepoResponse = getAsyncClient().describeRepositories(b -> b.repositoryNames(repoName)).join();
                Repository repoData = descrRepoResponse.repositories().stream().filter(r -> r.repositoryName().equals(repoName)).findFirst().orElse(null);
                assert repoData != null;
                String registryURL = repoData.repositoryUri().split("/")[0];

                AuthConfig authConfig = new AuthConfig()
                    .withUsername("AWS")
                    .withPassword(password)
                    .withRegistryAddress(registryURL);
                return authConfig;
            })
            .thenCompose(authConfig -> {
                DescribeRepositoriesResponse descrRepoResponse = getAsyncClient().describeRepositories(b -> b.repositoryNames(repoName)).join();
                Repository repoData = descrRepoResponse.repositories().stream().filter(r -> r.repositoryName().equals(repoName)).findFirst().orElse(null);
                getDockerClient().tagImageCmd(imageName + ":latest", repoData.repositoryUri() + ":latest", imageName).exec();
                try {
                    getDockerClient().pushImageCmd(repoData.repositoryUri()).withTag("echo-text").withAuthConfig(authConfig).start().awaitCompletion();
                    System.out.println("The " + imageName + " was pushed to ECR");

                } catch (InterruptedException e) {
                    throw (RuntimeException) e.getCause();
                }
                return CompletableFuture.completedFuture(authConfig);
            });

        authResponseFuture.join();
    }

    // Make sure local image echo-text exists.
    public boolean isEchoTextImagePresent() {
        try {
            List<Image> images = getDockerClient().listImagesCmd().exec();
            boolean helloWorldFound = false;
            for (Image image : images) {
                String[] repoTags = image.getRepoTags();
                if (repoTags != null) {
                    for (String tag : repoTags) {
                        if (tag.startsWith("echo-text")) {
                            System.out.println(tag);
                            helloWorldFound = true;
                        }
                    }
                }
            }
            if (helloWorldFound) {
                System.out.println("The local image named echo-text exists.");
                return true;
            } else {
                System.out.println("The local image named echo-text does not exist.");
                return false;
            }
        } catch (DockerClientException ex) {
            logger.error("ERROR: " + ex.getMessage());
            return false;
        }
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [CreateRepository](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/CreateRepository)
  + [DeleteRepository](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeleteRepository)
  + [DescribeImages](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeImages)
  + [DescribeRepositories](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeRepositories)
  + [GetAuthorizationToken](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetAuthorizationToken)
  + [GetRepositoryPolicy](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetRepositoryPolicy)
  + [SetRepositoryPolicy](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/SetRepositoryPolicy)
  + [StartLifecyclePolicyPreview](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/StartLifecyclePolicyPreview)

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 
Run an interactive scenario demonstrating Amazon ECR features.  

```
import java.util.Scanner

/**
 * Before running this Kotlin code example, set up your development environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html
 *
 * This code example requires an IAM Role that has permissions to interact with the Amazon ECR service.
 *
 * To create an IAM role, see:
 *
 * https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html
 *
 * This code example requires a local docker image named echo-text. Without a local image,
 * this program will not successfully run. For more information including how to create the local
 * image, see:
 *
 * /scenarios/basics/ecr/README
 *
 */

val DASHES = String(CharArray(80)).replace("\u0000", "-")

suspend fun main(args: Array<String>) {
    val usage =
        """
        Usage: <iamRoleARN> <accountId>

        Where:
           iamRoleARN - The IAM role ARN that has the necessary permissions to access and manage the Amazon ECR repository.
           accountId - Your AWS account number. 
        
        """.trimIndent()

    if (args.size != 2) {
        println(usage)
        return
    }

    var iamRole = args[0]
    var localImageName: String
    var accountId = args[1]
    val ecrActions = ECRActions()
    val scanner = Scanner(System.`in`)

    println(
        """
        The Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry 
        service provided by AWS. It allows developers and organizations to securely 
        store, manage, and deploy Docker container images. 
        ECR provides a simple and scalable way to manage container images throughout their lifecycle, 
        from building and testing to production deployment. 
                        
        The `EcrClient` service client that is part of the AWS SDK for Kotlin provides a set of methods to 
        programmatically interact with the Amazon ECR service. This allows developers to 
        automate the storage, retrieval, and management of container images as part of their application 
        deployment pipelines. With ECR, teams can focus on building and deploying their 
        applications without having to worry about the underlying infrastructure required to 
        host and manage a container registry.
            
        This scenario walks you through how to perform key operations for this service.  
        Let's get started...
        
         You have two choices:
            1 - Run the entire program.
            2 - Delete an existing Amazon ECR repository named echo-text (created from a previous execution of 
            this program that did not complete).
          
        """.trimIndent(),
    )

    while (true) {
        val input = scanner.nextLine()
        if (input.trim { it <= ' ' }.equals("1", ignoreCase = true)) {
            println("Continuing with the program...")
            println("")
            break
        } else if (input.trim { it <= ' ' }.equals("2", ignoreCase = true)) {
            val repoName = "echo-text"
            ecrActions.deleteECRRepository(repoName)
            return
        } else {
            // Handle invalid input.
            println("Invalid input. Please try again.")
        }
    }

    waitForInputToContinue(scanner)
    println(DASHES)
    println(
        """
        1. Create an ECR repository.
         
        The first task is to ensure we have a local Docker image named echo-text. 
        If this image exists, then an Amazon ECR repository is created. 
        
        An ECR repository is a private Docker container repository provided 
        by Amazon Web Services (AWS). It is a managed service that makes it easy 
        to store, manage, and deploy Docker container images. 
        
        """.trimIndent(),
    )

    // Ensure that a local docker image named echo-text exists.
    val doesExist = ecrActions.listLocalImages()
    val repoName: String
    if (!doesExist) {
        println("The local image named echo-text does not exist")
        return
    } else {
        localImageName = "echo-text"
        repoName = "echo-text"
    }

    val repoArn = ecrActions.createECRRepository(repoName).toString()
    println("The ARN of the ECR repository is $repoArn")
    waitForInputToContinue(scanner)

    println(DASHES)
    println(
        """
        2. Set an ECR repository policy.
        
        Setting an ECR repository policy using the `setRepositoryPolicy` function is crucial for maintaining
        the security and integrity of your container images. The repository policy allows you to 
        define specific rules and restrictions for accessing and managing the images stored within your ECR 
        repository.    
        
        """.trimIndent(),
    )
    waitForInputToContinue(scanner)
    ecrActions.setRepoPolicy(repoName, iamRole)
    waitForInputToContinue(scanner)

    println(DASHES)
    println(
        """
        3. Display ECR repository policy.
        
        Now we will retrieve the ECR policy to ensure it was successfully set.   
        """.trimIndent(),
    )
    waitForInputToContinue(scanner)
    val policyText = ecrActions.getRepoPolicy(repoName)
    println("Policy Text:")
    println(policyText)
    waitForInputToContinue(scanner)

    println(DASHES)
    println(
        """
        4. Retrieve an ECR authorization token.
        
        You need an authorization token to securely access and interact with the Amazon ECR registry. 
        The `getAuthorizationToken` method of the `EcrAsyncClient` is responsible for securely accessing 
        and interacting with an Amazon ECR repository. This operation is responsible for obtaining a 
        valid authorization token, which is required to authenticate your requests to the ECR service. 
        
        Without a valid authorization token, you would not be able to perform any operations on the 
        ECR repository, such as pushing, pulling, or managing your Docker images.    
        
        """.trimIndent(),
    )
    waitForInputToContinue(scanner)
    ecrActions.getAuthToken()
    waitForInputToContinue(scanner)

    println(DASHES)
    println(
        """
        5. Get the ECR Repository URI.
                    
        The URI  of an Amazon ECR repository is important. When you want to deploy a container image to 
        a container orchestration platform like Amazon Elastic Kubernetes Service (EKS) 
        or Amazon Elastic Container Service (ECS), you need to specify the full image URI, 
        which includes the ECR repository URI. This allows the container runtime to pull the 
        correct container image from the ECR repository.    
        
        """.trimIndent(),
    )
    waitForInputToContinue(scanner)
    val repositoryURI: String? = ecrActions.getRepositoryURI(repoName)
    println("The repository URI is $repositoryURI")
    waitForInputToContinue(scanner)

    println(DASHES)
    println(
        """
        6. Set an ECR Lifecycle Policy.
                    
        An ECR Lifecycle Policy is used to manage the lifecycle of Docker images stored in your ECR repositories. 
        These policies allow you to automatically remove old or unused Docker images from your repositories, 
        freeing up storage space and reducing costs.    
        
        """.trimIndent(),
    )
    waitForInputToContinue(scanner)
    val pol = ecrActions.setLifeCyclePolicy(repoName)
    println(pol)
    waitForInputToContinue(scanner)

    println(DASHES)
    println(
        """
        7. Push a docker image to the Amazon ECR Repository.
            
        The `pushImageCmd()` method pushes a local Docker image to an Amazon ECR repository.
        It sets up the Docker client by connecting to the local Docker host using the default port.
        It then retrieves the authorization token for the ECR repository by making a call to the AWS SDK.
            
        The method uses the authorization token to create an `AuthConfig` object, which is used to authenticate
        the Docker client when pushing the image. Finally, the method tags the Docker image with the specified
        repository name and image tag, and then pushes the image to the ECR repository using the Docker client.
        If the push operation is successful, the method prints a message indicating that the image was pushed to ECR.
        
        """.trimIndent(),
    )

    waitForInputToContinue(scanner)
    ecrActions.pushDockerImage(repoName, localImageName)
    waitForInputToContinue(scanner)

    println(DASHES)
    println("8. Verify if the image is in the ECR Repository.")
    waitForInputToContinue(scanner)
    ecrActions.verifyImage(repoName, localImageName)
    waitForInputToContinue(scanner)

    println(DASHES)
    println("9. As an optional step, you can interact with the image in Amazon ECR by using the CLI.")
    println("Would you like to view instructions on how to use the CLI to run the image? (y/n)")
    val ans = scanner.nextLine().trim()
    if (ans.equals("y", true)) {
        val instructions = """
        1. Authenticate with ECR - Before you can pull the image from Amazon ECR, you need to authenticate with the registry. You can do this using the AWS CLI:
        
            aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $accountId.dkr.ecr.us-east-1.amazonaws.com
        
        2. Describe the image using this command:
        
           aws ecr describe-images --repository-name $repoName --image-ids imageTag=$localImageName
        
        3. Run the Docker container and view the output using this command:
        
           docker run --rm $accountId.dkr.ecr.us-east-1.amazonaws.com/$repoName:$localImageName
        """
        println(instructions)
    }
    waitForInputToContinue(scanner)

    println(DASHES)
    println("10. Delete the ECR Repository.")
    println(
        """
        If the repository isn't empty, you must either delete the contents of the repository 
        or use the force option (used in this scenario) to delete the repository and have Amazon ECR delete all of its contents 
        on your behalf.
        
        """.trimIndent(),
    )
    println("Would you like to delete the Amazon ECR Repository? (y/n)")
    val delAns = scanner.nextLine().trim { it <= ' ' }
    if (delAns.equals("y", ignoreCase = true)) {
        println("You selected to delete the AWS ECR resources.")
        waitForInputToContinue(scanner)
        ecrActions.deleteECRRepository(repoName)
    }

    println(DASHES)
    println("This concludes the Amazon ECR SDK scenario")
    println(DASHES)
}

private fun waitForInputToContinue(scanner: Scanner) {
    while (true) {
        println("")
        println("Enter 'c' followed by <ENTER> to continue:")
        val input = scanner.nextLine()
        if (input.trim { it <= ' ' }.equals("c", ignoreCase = true)) {
            println("Continuing with the program...")
            println("")
            break
        } else {
            // Handle invalid input.
            println("Invalid input. Please try again.")
        }
    }
}
```
A wrapper class for Amazon ECR SDK methods.  

```
import aws.sdk.kotlin.services.ecr.EcrClient
import aws.sdk.kotlin.services.ecr.model.CreateRepositoryRequest
import aws.sdk.kotlin.services.ecr.model.DeleteRepositoryRequest
import aws.sdk.kotlin.services.ecr.model.DescribeImagesRequest
import aws.sdk.kotlin.services.ecr.model.DescribeRepositoriesRequest
import aws.sdk.kotlin.services.ecr.model.EcrException
import aws.sdk.kotlin.services.ecr.model.GetRepositoryPolicyRequest
import aws.sdk.kotlin.services.ecr.model.ImageIdentifier
import aws.sdk.kotlin.services.ecr.model.RepositoryAlreadyExistsException
import aws.sdk.kotlin.services.ecr.model.SetRepositoryPolicyRequest
import aws.sdk.kotlin.services.ecr.model.StartLifecyclePolicyPreviewRequest
import com.github.dockerjava.api.DockerClient
import com.github.dockerjava.api.command.DockerCmdExecFactory
import com.github.dockerjava.api.model.AuthConfig
import com.github.dockerjava.core.DockerClientBuilder
import com.github.dockerjava.netty.NettyDockerCmdExecFactory
import java.io.IOException
import java.util.Base64

class ECRActions {
    private var dockerClient: DockerClient? = null

    private fun getDockerClient(): DockerClient? {
        val osName = System.getProperty("os.name")
        if (osName.startsWith("Windows")) {
            // Make sure Docker Desktop is running.
            val dockerHost = "tcp://localhost:2375" // Use the Docker Desktop default port.
            val dockerCmdExecFactory: DockerCmdExecFactory =
                NettyDockerCmdExecFactory().withReadTimeout(20000).withConnectTimeout(20000)
            dockerClient = DockerClientBuilder.getInstance(dockerHost).withDockerCmdExecFactory(dockerCmdExecFactory).build()
        } else {
            dockerClient = DockerClientBuilder.getInstance().build()
        }
        return dockerClient
    }


    /**
     * Sets the lifecycle policy for the specified repository.
     *
     * @param repoName the name of the repository for which to set the lifecycle policy.
     */
    suspend fun setLifeCyclePolicy(repoName: String): String? {
        val polText =
            """
             {
             "rules": [
                 {
                     "rulePriority": 1,
                     "description": "Expire images older than 14 days",
                     "selection": {
                         "tagStatus": "any",
                         "countType": "sinceImagePushed",
                         "countUnit": "days",
                         "countNumber": 14
                     },
                     "action": {
                         "type": "expire"
                     }
                 }
            ]
            }
            
            """.trimIndent()
        val lifecyclePolicyPreviewRequest =
            StartLifecyclePolicyPreviewRequest {
                lifecyclePolicyText = polText
                repositoryName = repoName
            }

        // Execute the request asynchronously.
        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val response = ecrClient.startLifecyclePolicyPreview(lifecyclePolicyPreviewRequest)
            return response.lifecyclePolicyText
        }
    }


    /**
     * Retrieves the repository URI for the specified repository name.
     *
     * @param repoName the name of the repository to retrieve the URI for.
     * @return the repository URI for the specified repository name.
     */
    suspend fun getRepositoryURI(repoName: String?): String? {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }
        val request =
            DescribeRepositoriesRequest {
                repositoryNames = listOf(repoName)
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeRepositoriesResponse = ecrClient.describeRepositories(request)
            if (!describeRepositoriesResponse.repositories?.isEmpty()!!) {
                return describeRepositoriesResponse?.repositories?.get(0)?.repositoryUri
            } else {
                println("No repositories found for the given name.")
                return ""
            }
        }
    }


    /**
     * Retrieves the authorization token for Amazon Elastic Container Registry (ECR).
     *
     */
    suspend fun getAuthToken() {
        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            // Retrieve the authorization token for ECR.
            val response = ecrClient.getAuthorizationToken()
            val authorizationData = response.authorizationData?.get(0)
            val token = authorizationData?.authorizationToken
            if (token != null) {
                println("The token was successfully retrieved.")
            }
        }
    }


    /**
     * Gets the repository policy for the specified repository.
     *
     * @param repoName the name of the repository.
     */
    suspend fun getRepoPolicy(repoName: String?): String? {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }

        // Create the request
        val getRepositoryPolicyRequest =
            GetRepositoryPolicyRequest {
                repositoryName = repoName
            }
        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val response = ecrClient.getRepositoryPolicy(getRepositoryPolicyRequest)
            val responseText = response.policyText
            return responseText
        }
    }


    /**
     * Sets the repository policy for the specified ECR repository.
     *
     * @param repoName the name of the ECR repository.
     * @param iamRole the IAM role to be granted access to the repository.
     */
    suspend fun setRepoPolicy(
        repoName: String?,
        iamRole: String?,
    ) {
        val policyDocumentTemplate =
            """
             {
              "Version":"2012-10-17",		 	 	 
              "Statement" : [ {
                "Sid" : "new statement",
                "Effect" : "Allow",
                "Principal" : {
                  "AWS" : "$iamRole"
                },
                "Action" : "ecr:BatchGetImage"
              } ]
            }
             
            """.trimIndent()
        val setRepositoryPolicyRequest =
            SetRepositoryPolicyRequest {
                repositoryName = repoName
                policyText = policyDocumentTemplate
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val response = ecrClient.setRepositoryPolicy(setRepositoryPolicyRequest)
            if (response != null) {
                println("Repository policy set successfully.")
            }
        }
    }


    /**
     * Creates an Amazon Elastic Container Registry (Amazon ECR) repository.
     *
     * @param repoName the name of the repository to create.
     * @return the Amazon Resource Name (ARN) of the created repository, or an empty string if the operation failed.
     * @throws RepositoryAlreadyExistsException if the repository exists.
     * @throws EcrException         if an error occurs while creating the repository.
     */
    suspend fun createECRRepository(repoName: String?): String? {
        val request =
            CreateRepositoryRequest {
                repositoryName = repoName
            }

        return try {
            EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
                val response = ecrClient.createRepository(request)
                response.repository?.repositoryArn
            }
        } catch (e: RepositoryAlreadyExistsException) {
            println("Repository already exists: $repoName")
            repoName?.let { getRepoARN(it) }
        } catch (e: EcrException) {
            println("An error occurred: ${e.message}")
            null
        }
    }

    suspend fun getRepoARN(repoName: String): String? {
        // Fetch the existing repository's ARN.
        val describeRequest =
            DescribeRepositoriesRequest {
                repositoryNames = listOf(repoName)
            }
        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeResponse = ecrClient.describeRepositories(describeRequest)
            return describeResponse.repositories?.get(0)?.repositoryArn
        }
    }

    fun listLocalImages(): Boolean = try {
        val images = getDockerClient()?.listImagesCmd()?.exec()
        images?.any { image ->
            image.repoTags?.any { tag -> tag.startsWith("echo-text") } ?: false
        } ?: false
    } catch (ex: Exception) {
        println("ERROR: ${ex.message}")
        false
    }


    /**
     * Pushes a Docker image to an Amazon Elastic Container Registry (ECR) repository.
     *
     * @param repoName the name of the ECR repository to push the image to.
     * @param imageName the name of the Docker image.
     */
    suspend fun pushDockerImage(
        repoName: String,
        imageName: String,
    ) {
        println("Pushing $imageName to $repoName will take a few seconds")
        val authConfig = getAuthConfig(repoName)

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val desRequest =
                DescribeRepositoriesRequest {
                    repositoryNames = listOf(repoName)
                }

            val describeRepoResponse = ecrClient.describeRepositories(desRequest)
            val repoData =
                describeRepoResponse.repositories?.firstOrNull { it.repositoryName == repoName }
                    ?: throw RuntimeException("Repository not found: $repoName")

            val tagImageCmd = getDockerClient()?.tagImageCmd("$imageName", "${repoData.repositoryUri}", imageName)
            if (tagImageCmd != null) {
                tagImageCmd.exec()
            }
            val pushImageCmd =
                repoData.repositoryUri?.let {
                    dockerClient?.pushImageCmd(it)
                        // ?.withTag("latest")
                        ?.withAuthConfig(authConfig)
                }

            try {
                if (pushImageCmd != null) {
                    pushImageCmd.start().awaitCompletion()
                }
                println("The $imageName was pushed to Amazon ECR")
            } catch (e: IOException) {
                throw RuntimeException(e)
            }
        }
    }


    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     */
    suspend fun verifyImage(
        repoName: String?,
        imageTagVal: String?,
    ) {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }
        require(!(imageTagVal == null || imageTagVal.isEmpty())) { "Image tag cannot be null or empty" }

        val imageId =
            ImageIdentifier {
                imageTag = imageTagVal
            }
        val request =
            DescribeImagesRequest {
                repositoryName = repoName
                imageIds = listOf(imageId)
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeImagesResponse = ecrClient.describeImages(request)
            if (describeImagesResponse != null && !describeImagesResponse.imageDetails?.isEmpty()!!) {
                println("Image is present in the repository.")
            } else {
                println("Image is not present in the repository.")
            }
        }
    }


    /**
     * Deletes an ECR (Elastic Container Registry) repository.
     *
     * @param repoName the name of the repository to delete.
     */
    suspend fun deleteECRRepository(repoName: String) {
        if (repoName.isNullOrEmpty()) {
            throw IllegalArgumentException("Repository name cannot be null or empty")
        }

        val repositoryRequest =
            DeleteRepositoryRequest {
                force = true
                repositoryName = repoName
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            ecrClient.deleteRepository(repositoryRequest)
            println("You have successfully deleted the $repoName repository")
        }
    }

    // Return an AuthConfig.
    private suspend fun getAuthConfig(repoName: String): AuthConfig {
        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            // Retrieve the authorization token for ECR.
            val response = ecrClient.getAuthorizationToken()
            val authorizationData = response.authorizationData?.get(0)
            val token = authorizationData?.authorizationToken
            val decodedToken = String(Base64.getDecoder().decode(token))
            val password = decodedToken.substring(4)

            val request =
                DescribeRepositoriesRequest {
                    repositoryNames = listOf(repoName)
                }

            val descrRepoResponse = ecrClient.describeRepositories(request)
            val repoData = descrRepoResponse.repositories?.firstOrNull { it.repositoryName == repoName }
            val registryURL: String = repoData?.repositoryUri?.split("/")?.get(0) ?: ""

            return AuthConfig()
                .withUsername("AWS")
                .withPassword(password)
                .withRegistryAddress(registryURL)
        }
    }
}
```
+ For API details, see the following topics in *AWS SDK for Kotlin API reference*.
  + [CreateRepository](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DeleteRepository](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DescribeImages](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DescribeRepositories](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetAuthorizationToken](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetRepositoryPolicy](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [SetRepositoryPolicy](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [StartLifecyclePolicyPreview](https://sdk.amazonaws.com/kotlin/api/latest/index.html)

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 
Run an interactive scenario at a command prompt.  

```
class ECRGettingStarted:
    """
    A scenario that demonstrates how to use Boto3 to perform basic operations using
    Amazon ECR.
    """

    def __init__(
        self,
        ecr_wrapper: ECRWrapper,
        docker_client: docker.DockerClient,
    ):
        self.ecr_wrapper = ecr_wrapper
        self.docker_client = docker_client
        self.tag = "echo-text"
        self.repository_name = "ecr-basics"
        self.docker_image = None
        self.full_tag_name = None
        self.repository = None

    def run(self, role_arn: str) -> None:
        """
        Runs the scenario.
        """
        print(
            """
The Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry
service provided by AWS. It allows developers and organizations to securely
store, manage, and deploy Docker container images.
ECR provides a simple and scalable way to manage container images throughout their lifecycle,
from building and testing to production deployment.

The `ECRWrapper' class is a wrapper for the Boto3 'ecr' client. The 'ecr' client provides a set of methods to
programmatically interact with the Amazon ECR service. This allows developers to
automate the storage, retrieval, and management of container images as part of their application
deployment pipelines. With ECR, teams can focus on building and deploying their
applications without having to worry about the underlying infrastructure required to
host and manage a container registry.

This scenario walks you through how to perform key operations for this service.
Let's get started...
        """
        )
        press_enter_to_continue()
        print_dashes()
        print(
            f"""
* Create an ECR repository.

An ECR repository is a private Docker container repository provided
by Amazon Web Services (AWS). It is a managed service that makes it easy
to store, manage, and deploy Docker container images.
        """
        )
        print(f"Creating a repository named {self.repository_name}")
        self.repository = self.ecr_wrapper.create_repository(self.repository_name)
        print(f"The ARN of the ECR repository is {self.repository['repositoryArn']}")
        repository_uri = self.repository["repositoryUri"]
        press_enter_to_continue()
        print_dashes()

        print(
            f"""
* Build a Docker image.

Create a local Docker image if it does not already exist.
A Python Docker client is used to execute Docker commands.
You must have Docker installed and running.
            """
        )
        print(f"Building a docker image from 'docker_files/Dockerfile'")
        self.full_tag_name = f"{repository_uri}:{self.tag}"
        self.docker_image = self.docker_client.images.build(
            path="docker_files", tag=self.full_tag_name
        )[0]
        print(f"Docker image {self.full_tag_name} successfully built.")
        press_enter_to_continue()
        print_dashes()

        if role_arn is None:
            print(
                """
* Because an IAM role ARN was not provided, a role policy will not be set for this repository.
            """
            )
        else:
            print(
                """
* Set an ECR repository policy.

Setting an ECR repository policy using the `setRepositoryPolicy` function is crucial for maintaining
the security and integrity of your container images. The repository policy allows you to
define specific rules and restrictions for accessing and managing the images stored within your ECR
repository.
        """
            )

            self.grant_role_download_access(role_arn)
            print(f"Download access granted to the IAM role ARN {role_arn}")
            press_enter_to_continue()
            print_dashes()

            print(
                """
* Display ECR repository policy.

Now we will retrieve the ECR policy to ensure it was successfully set.
            """
            )

            policy_text = self.ecr_wrapper.get_repository_policy(self.repository_name)
            print("Policy Text:")
            print(f"{policy_text}")
            press_enter_to_continue()
            print_dashes()

        print(
            """
* Retrieve an ECR authorization token.

You need an authorization token to securely access and interact with the Amazon ECR registry.
The `get_authorization_token` method of the `ecr` client is responsible for securely accessing
and interacting with an Amazon ECR repository. This operation is responsible for obtaining a
valid authorization token, which is required to authenticate your requests to the ECR service.

Without a valid authorization token, you would not be able to perform any operations on the
ECR repository, such as pushing, pulling, or managing your Docker images.
        """
        )

        authorization_token = self.ecr_wrapper.get_authorization_token()
        print("Authorization token retrieved.")
        press_enter_to_continue()
        print_dashes()
        print(
            """
* Get the ECR Repository URI.

The URI  of an Amazon ECR repository is important. When you want to deploy a container image to
a container orchestration platform like Amazon Elastic Kubernetes Service (EKS)
or Amazon Elastic Container Service (ECS), you need to specify the full image URI,
which includes the ECR repository URI. This allows the container runtime to pull the
correct container image from the ECR repository.
        """
        )
        repository_descriptions = self.ecr_wrapper.describe_repositories(
            [self.repository_name]
        )
        repository_uri = repository_descriptions[0]["repositoryUri"]
        print(f"Repository URI found: {repository_uri}")
        press_enter_to_continue()
        print_dashes()

        print(
            """
* Set an ECR Lifecycle Policy.

An ECR Lifecycle Policy is used to manage the lifecycle of Docker images stored in your ECR repositories.
These policies allow you to automatically remove old or unused Docker images from your repositories,
freeing up storage space and reducing costs.

This example policy helps to maintain the size and efficiency of the container registry
by automatically removing older and potentially unused images, ensuring that the
storage is optimized and the registry remains up-to-date.
            """
        )
        press_enter_to_continue()
        self.put_expiration_policy()
        print(f"An expiration policy was added to the repository.")
        print_dashes()

        print(
            """
* Push a docker image to the Amazon ECR Repository.

The Docker client uses the authorization token is used to authenticate the when pushing the image to the 
ECR repository.
        """
        )
        decoded_authorization = base64.b64decode(authorization_token).decode("utf-8")
        username, password = decoded_authorization.split(":")

        resp = self.docker_client.api.push(
            repository=repository_uri,
            auth_config={"username": username, "password": password},
            tag=self.tag,
            stream=True,
            decode=True,
        )
        for line in resp:
            print(line)

        print_dashes()

        print("* Verify if the image is in the ECR Repository.")
        image_descriptions = self.ecr_wrapper.describe_images(
            self.repository_name, [self.tag]
        )
        if len(image_descriptions) > 0:
            print("Image found in ECR Repository.")
        else:
            print("Image not found in ECR Repository.")
        press_enter_to_continue()
        print_dashes()

        print(
            "* As an optional step, you can interact with the image in Amazon ECR by using the CLI."
        )
        if q.ask(
            "Would you like to view instructions on how to use the CLI to run the image? (y/n)",
            q.is_yesno,
        ):
            print(
                f"""
1. Authenticate with ECR - Before you can pull the image from Amazon ECR, you need to authenticate with the registry. You can do this using the AWS CLI:

    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin {repository_uri.split("/")[0]}

2. Describe the image using this command:

   aws ecr describe-images --repository-name {self.repository_name} --image-ids imageTag={self.tag}

3. Run the Docker container and view the output using this command:

   docker run --rm {self.full_tag_name}
"""
            )

        self.cleanup(True)

    def cleanup(self, ask: bool):
        """
        Deletes the resources created in this scenario.
        :param ask: If True, prompts the user to confirm before deleting the resources.
        """
        if self.repository is not None and (
            not ask
            or q.ask(
                f"Would you like to delete the ECR repository '{self.repository_name}? (y/n) "
            )
        ):
            print(f"Deleting the ECR repository '{self.repository_name}'.")
            self.ecr_wrapper.delete_repository(self.repository_name)

        if self.full_tag_name is not None and (
            not ask
            or q.ask(
                f"Would you like to delete the local Docker image '{self.full_tag_name}? (y/n) "
            )
        ):
            print(f"Deleting the docker image '{self.full_tag_name}'.")
            self.docker_client.images.remove(self.full_tag_name)

    def grant_role_download_access(self, role_arn: str):
        """
        Grants the specified role access to download images from the ECR repository.

        :param role_arn: The ARN of the role to grant access to.
        """
        policy_json = {
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Sid": "AllowDownload",
                    "Effect": "Allow",
                    "Principal": {"AWS": role_arn},
                    "Action": ["ecr:BatchGetImage"],
                }
            ],
        }

        self.ecr_wrapper.set_repository_policy(
            self.repository_name, json.dumps(policy_json)
        )


    def put_expiration_policy(self):
        """
        Puts an expiration policy on the ECR repository.
        """
        policy_json = {
            "rules": [
                {
                    "rulePriority": 1,
                    "description": "Expire images older than 14 days",
                    "selection": {
                        "tagStatus": "any",
                        "countType": "sinceImagePushed",
                        "countUnit": "days",
                        "countNumber": 14,
                    },
                    "action": {"type": "expire"},
                }
            ]
        }

        self.ecr_wrapper.put_lifecycle_policy(
            self.repository_name, json.dumps(policy_json)
        )



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Amazon ECR getting started scenario."
    )
    parser.add_argument(
        "--iam-role-arn",
        type=str,
        default=None,
        help="an optional IAM role ARN that will be granted access to download images from a repository.",
        required=False,
    )
    parser.add_argument(
        "--no-art",
        action="store_true",
        help="accessibility setting that suppresses art in the console output.",
    )
    args = parser.parse_args()
    no_art = args.no_art
    iam_role_arn = args.iam_role_arn
    demo = None
    a_docker_client = None
    try:
        a_docker_client = docker.from_env()
        if not a_docker_client.ping():
            raise docker.errors.DockerException("Docker is not running.")
    except docker.errors.DockerException as err:
        logging.error(
            """
        The Python Docker client could not be created. 
        Do you have Docker installed and running?
        Here is the error message:
        %s
        """,
            err,
        )
        sys.exit("Error with Docker.")
    try:
        an_ecr_wrapper = ECRWrapper.from_client()
        demo = ECRGettingStarted(an_ecr_wrapper, a_docker_client)
        demo.run(iam_role_arn)

    except Exception as exception:
        logging.exception("Something went wrong with the demo!")
        if demo is not None:
            demo.cleanup(False)
```
ECRWrapper class that wraps Amazon ECR actions.  

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def create_repository(self, repository_name: str) -> dict[str, any]:
        """
        Creates an ECR repository.

        :param repository_name: The name of the repository to create.
        :return: A dictionary of the created repository.
        """
        try:
            response = self.ecr_client.create_repository(repositoryName=repository_name)
            return response["repository"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "RepositoryAlreadyExistsException":
                print(f"Repository {repository_name} already exists.")
                response = self.ecr_client.describe_repositories(
                    repositoryNames=[repository_name]
                )
                return self.describe_repositories([repository_name])[0]
            else:
                logger.error(
                    "Error creating repository %s. Here's why %s",
                    repository_name,
                    err.response["Error"]["Message"],
                )
                raise


    def delete_repository(self, repository_name: str):
        """
        Deletes an ECR repository.

        :param repository_name: The name of the repository to delete.
        """
        try:
            self.ecr_client.delete_repository(
                repositoryName=repository_name, force=True
            )
            print(f"Deleted repository {repository_name}.")
        except ClientError as err:
            logger.error(
                "Couldn't delete repository %s.. Here's why %s",
                repository_name,
                err.response["Error"]["Message"],
            )
            raise


    def set_repository_policy(self, repository_name: str, policy_text: str):
        """
        Sets the policy for an ECR repository.

        :param repository_name: The name of the repository to set the policy for.
        :param policy_text: The policy text to set.
        """
        try:
            self.ecr_client.set_repository_policy(
                repositoryName=repository_name, policyText=policy_text
            )
            print(f"Set repository policy for repository {repository_name}.")
        except ClientError as err:
            if err.response["Error"]["Code"] == "RepositoryPolicyNotFoundException":
                logger.error("Repository does not exist. %s.", repository_name)
                raise
            else:
                logger.error(
                    "Couldn't set repository policy for repository %s. Here's why %s",
                    repository_name,
                    err.response["Error"]["Message"],
                )
                raise


    def get_repository_policy(self, repository_name: str) -> str:
        """
        Gets the policy for an ECR repository.

        :param repository_name: The name of the repository to get the policy for.
        :return: The policy text.
        """
        try:
            response = self.ecr_client.get_repository_policy(
                repositoryName=repository_name
            )
            return response["policyText"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "RepositoryPolicyNotFoundException":
                logger.error("Repository does not exist. %s.", repository_name)
                raise
            else:
                logger.error(
                    "Couldn't get repository policy for repository %s. Here's why %s",
                    repository_name,
                    err.response["Error"]["Message"],
                )
                raise


    def get_authorization_token(self) -> str:
        """
        Gets an authorization token for an ECR repository.

        :return: The authorization token.
        """
        try:
            response = self.ecr_client.get_authorization_token()
            return response["authorizationData"][0]["authorizationToken"]
        except ClientError as err:
            logger.error(
                "Couldn't get authorization token. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise


    def describe_repositories(self, repository_names: list[str]) -> list[dict]:
        """
        Describes ECR repositories.

        :param repository_names: The names of the repositories to describe.
        :return: The list of repository descriptions.
        """
        try:
            response = self.ecr_client.describe_repositories(
                repositoryNames=repository_names
            )
            return response["repositories"]
        except ClientError as err:
            logger.error(
                "Couldn't describe repositories. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise


    def put_lifecycle_policy(self, repository_name: str, lifecycle_policy_text: str):
        """
        Puts a lifecycle policy for an ECR repository.

        :param repository_name: The name of the repository to put the lifecycle policy for.
        :param lifecycle_policy_text: The lifecycle policy text to put.
        """
        try:
            self.ecr_client.put_lifecycle_policy(
                repositoryName=repository_name,
                lifecyclePolicyText=lifecycle_policy_text,
            )
            print(f"Put lifecycle policy for repository {repository_name}.")
        except ClientError as err:
            logger.error(
                "Couldn't put lifecycle policy for repository %s. Here's why %s",
                repository_name,
                err.response["Error"]["Message"],
            )
            raise


    def describe_images(
        self, repository_name: str, image_ids: list[str] = None
    ) -> list[dict]:
        """
        Describes ECR images.

        :param repository_name: The name of the repository to describe images for.
        :param image_ids: The optional IDs of images to describe.
        :return: The list of image descriptions.
        """
        try:
            params = {
                "repositoryName": repository_name,
            }
            if image_ids is not None:
                params["imageIds"] = [{"imageTag": tag} for tag in image_ids]

            paginator = self.ecr_client.get_paginator("describe_images")
            image_descriptions = []
            for page in paginator.paginate(**params):
                image_descriptions.extend(page["imageDetails"])
            return image_descriptions
        except ClientError as err:
            logger.error(
                "Couldn't describe images. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateRepository](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/CreateRepository)
  + [DeleteRepository](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeleteRepository)
  + [DescribeImages](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeImages)
  + [DescribeRepositories](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeRepositories)
  + [GetAuthorizationToken](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetAuthorizationToken)
  + [GetRepositoryPolicy](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetRepositoryPolicy)
  + [SetRepositoryPolicy](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/SetRepositoryPolicy)
  + [StartLifecyclePolicyPreview](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/StartLifecyclePolicyPreview)

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

### Actions for Amazon ECR using AWS SDKs
<a name="service_code_examples_actions"></a>

The following code examples demonstrate how to perform individual Amazon ECR actions with AWS SDKs. Each example includes a link to GitHub, where you can find instructions for setting up and running the code. 

These excerpts call the Amazon ECR API and are code excerpts from larger programs that must be run in context. You can see actions in context in [Scenarios for Amazon ECR using AWS SDKs](#service_code_examples_scenarios). 

 The following examples include only the most commonly used actions. For a complete list, see the [Amazon Elastic Container Registry API Reference](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/Welcome.html). 

**Topics**
+ [`CreateRepository`](#example_ecr_CreateRepository_section)
+ [`DeleteRepository`](#example_ecr_DeleteRepository_section)
+ [`DescribeImages`](#example_ecr_DescribeImages_section)
+ [`DescribeRepositories`](#example_ecr_DescribeRepositories_section)
+ [`GetAuthorizationToken`](#example_ecr_GetAuthorizationToken_section)
+ [`GetRepositoryPolicy`](#example_ecr_GetRepositoryPolicy_section)
+ [`ListImages`](#example_ecr_ListImages_section)
+ [`PushImageCmd`](#example_ecr_PushImageCmd_section)
+ [`PutLifeCyclePolicy`](#example_ecr_PutLifeCyclePolicy_section)
+ [`SetRepositoryPolicy`](#example_ecr_SetRepositoryPolicy_section)
+ [`StartLifecyclePolicyPreview`](#example_ecr_StartLifecyclePolicyPreview_section)

#### Use `CreateRepository` with an AWS SDK or CLI
<a name="example_ecr_CreateRepository_section"></a>

The following code examples show how to use `CreateRepository`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 
+  [Getting started with container registries](#example_ecr_GettingStarted_078_section) 

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To create a repository**  
The following `create-repository` example creates a repository inside the specified namespace in the default registry for an account.  

```
aws ecr create-repository \
    --repository-name {{project-a/sample-repo}}
```
Output:  

```
{
    "repository": {
        "registryId": "123456789012",
        "repositoryName": "project-a/sample-repo",
        "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo"
    }
}
```
For more information, see [Creating a Repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the *Amazon ECR User Guide*.  
**Example 2: To create a repository configured with image tag immutability**  
The following `create-repository` example creates a repository configured for tag immutability in the default registry for an account.  

```
aws ecr create-repository \
    --repository-name {{project-a/sample-repo}} \
    --image-tag-mutability {{IMMUTABLE}}
```
Output:  

```
{
    "repository": {
        "registryId": "123456789012",
        "repositoryName": "project-a/sample-repo",
        "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo",
        "imageTagMutability": "IMMUTABLE"
    }
}
```
For more information, see [Image Tag Mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html) in the *Amazon ECR User Guide*.  
**Example 3: To create a repository configured with a scanning configuration**  
The following `create-repository` example creates a repository configured to perform a vulnerability scan on image push in the default registry for an account.  

```
aws ecr create-repository \
    --repository-name {{project-a/sample-repo}} \
    --image-scanning-configuration {{scanOnPush=true}}
```
Output:  

```
{
    "repository": {
        "registryId": "123456789012",
        "repositoryName": "project-a/sample-repo",
        "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo",
        "imageScanningConfiguration": {
            "scanOnPush": true
        }
    }
}
```
For more information, see [Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in the *Amazon ECR User Guide*.  
+  For API details, see [CreateRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Creates an Amazon Elastic Container Registry (Amazon ECR) repository.
     *
     * @param repoName the name of the repository to create.
     * @return the Amazon Resource Name (ARN) of the created repository, or an empty string if the operation failed.
     * @throws IllegalArgumentException     If repository name is invalid.
     * @throws RuntimeException             if an error occurs while creating the repository.
     */
    public String createECRRepository(String repoName) {
        if (repoName == null || repoName.isEmpty()) {
            throw new IllegalArgumentException("Repository name cannot be null or empty");
        }

        CreateRepositoryRequest request = CreateRepositoryRequest.builder()
            .repositoryName(repoName)
            .build();

        CompletableFuture<CreateRepositoryResponse> response = getAsyncClient().createRepository(request);
        try {
            CreateRepositoryResponse result = response.join();
            if (result != null) {
                System.out.println("The " + repoName + " repository was created successfully.");
                return result.repository().repositoryArn();
            } else {
                throw new RuntimeException("Unexpected response type");
            }
        } catch (CompletionException e) {
            Throwable cause = e.getCause();
            if (cause instanceof EcrException ex) {
                if ("RepositoryAlreadyExistsException".equals(ex.awsErrorDetails().errorCode())) {
                    System.out.println("The Amazon ECR repository already exists, moving on...");
                    DescribeRepositoriesRequest describeRequest = DescribeRepositoriesRequest.builder()
                        .repositoryNames(repoName)
                        .build();
                    DescribeRepositoriesResponse describeResponse = getAsyncClient().describeRepositories(describeRequest).join();
                    return describeResponse.repositories().get(0).repositoryArn();
                } else {
                    throw new RuntimeException(ex);
                }
            } else {
                throw new RuntimeException(e);
            }
        }
    }
```
+  For API details, see [CreateRepository](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/CreateRepository) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Creates an Amazon Elastic Container Registry (Amazon ECR) repository.
     *
     * @param repoName the name of the repository to create.
     * @return the Amazon Resource Name (ARN) of the created repository, or an empty string if the operation failed.
     * @throws RepositoryAlreadyExistsException if the repository exists.
     * @throws EcrException         if an error occurs while creating the repository.
     */
    suspend fun createECRRepository(repoName: String?): String? {
        val request =
            CreateRepositoryRequest {
                repositoryName = repoName
            }

        return try {
            EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
                val response = ecrClient.createRepository(request)
                response.repository?.repositoryArn
            }
        } catch (e: RepositoryAlreadyExistsException) {
            println("Repository already exists: $repoName")
            repoName?.let { getRepoARN(it) }
        } catch (e: EcrException) {
            println("An error occurred: ${e.message}")
            null
        }
    }
```
+  For API details, see [CreateRepository](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def create_repository(self, repository_name: str) -> dict[str, any]:
        """
        Creates an ECR repository.

        :param repository_name: The name of the repository to create.
        :return: A dictionary of the created repository.
        """
        try:
            response = self.ecr_client.create_repository(repositoryName=repository_name)
            return response["repository"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "RepositoryAlreadyExistsException":
                print(f"Repository {repository_name} already exists.")
                response = self.ecr_client.describe_repositories(
                    repositoryNames=[repository_name]
                )
                return self.describe_repositories([repository_name])[0]
            else:
                logger.error(
                    "Error creating repository %s. Here's why %s",
                    repository_name,
                    err.response["Error"]["Message"],
                )
                raise
```
+  For API details, see [CreateRepository](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/CreateRepository) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        " iv_repository_name = 'my-repository'
        oo_result = lo_ecr->createrepository(
          iv_repositoryname = iv_repository_name ).
        DATA(lv_repository_uri) = oo_result->get_repository( )->get_repositoryuri( ).
        MESSAGE |Repository created with URI: { lv_repository_uri }| TYPE 'I'.
      CATCH /aws1/cx_ecrrepositoryalrexex.
        " If repository already exists, retrieve it
        DATA lt_repo_names TYPE /aws1/cl_ecrrepositorynamels00=>tt_repositorynamelist.
        APPEND NEW /aws1/cl_ecrrepositorynamels00( iv_value = iv_repository_name ) TO lt_repo_names.
        DATA(lo_describe_result) = lo_ecr->describerepositories( it_repositorynames = lt_repo_names ).
        DATA(lt_repos) = lo_describe_result->get_repositories( ).
        IF lines( lt_repos ) > 0.
          READ TABLE lt_repos INDEX 1 INTO DATA(lo_repo).
          oo_result = NEW /aws1/cl_ecrcrerepositoryrsp( io_repository = lo_repo ).
          MESSAGE |Repository { iv_repository_name } already exists.| TYPE 'I'.
        ENDIF.
    ENDTRY.
```
+  For API details, see [CreateRepository](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `DeleteRepository` with an AWS SDK or CLI
<a name="example_ecr_DeleteRepository_section"></a>

The following code examples show how to use `DeleteRepository`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 
+  [Getting started with container registries](#example_ecr_GettingStarted_078_section) 

------
#### [ CLI ]

**AWS CLI**  
**To delete a repository**  
The following `delete-repository` example command force deletes the specified repository in the default registry for an account. The `--force` flag is required if the repository contains images.  

```
aws ecr delete-repository \
    --repository-name {{ubuntu}} \
    --force
```
Output:  

```
{
    "repository": {
        "registryId": "123456789012",
        "repositoryName": "ubuntu",
        "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/ubuntu"
    }
}
```
For more information, see [Deleting a Repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-delete.html) in the *Amazon ECR User Guide*.  
+  For API details, see [DeleteRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Deletes an ECR (Elastic Container Registry) repository.
     *
     * @param repoName the name of the repository to delete.
     * @throws IllegalArgumentException if the repository name is null or empty.
     * @throws EcrException if there is an error deleting the repository.
     * @throws RuntimeException if an unexpected error occurs during the deletion process.
     */
    public void deleteECRRepository(String repoName) {
        if (repoName == null || repoName.isEmpty()) {
            throw new IllegalArgumentException("Repository name cannot be null or empty");
        }

        DeleteRepositoryRequest repositoryRequest = DeleteRepositoryRequest.builder()
            .force(true)
            .repositoryName(repoName)
            .build();

        CompletableFuture<DeleteRepositoryResponse> response = getAsyncClient().deleteRepository(repositoryRequest);
        response.whenComplete((deleteRepositoryResponse, ex) -> {
            if (deleteRepositoryResponse != null) {
                System.out.println("You have successfully deleted the " + repoName + " repository");
            } else {
                Throwable cause = ex.getCause();
                if (cause instanceof EcrException) {
                    throw (EcrException) cause;
                } else {
                    throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                }
            }
        });

        // Wait for the CompletableFuture to complete
        response.join();
    }
```
+  For API details, see [DeleteRepository](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeleteRepository) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Deletes an ECR (Elastic Container Registry) repository.
     *
     * @param repoName the name of the repository to delete.
     */
    suspend fun deleteECRRepository(repoName: String) {
        if (repoName.isNullOrEmpty()) {
            throw IllegalArgumentException("Repository name cannot be null or empty")
        }

        val repositoryRequest =
            DeleteRepositoryRequest {
                force = true
                repositoryName = repoName
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            ecrClient.deleteRepository(repositoryRequest)
            println("You have successfully deleted the $repoName repository")
        }
    }
```
+  For API details, see [DeleteRepository](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def delete_repository(self, repository_name: str):
        """
        Deletes an ECR repository.

        :param repository_name: The name of the repository to delete.
        """
        try:
            self.ecr_client.delete_repository(
                repositoryName=repository_name, force=True
            )
            print(f"Deleted repository {repository_name}.")
        except ClientError as err:
            logger.error(
                "Couldn't delete repository %s.. Here's why %s",
                repository_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteRepository](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeleteRepository) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        " iv_repository_name = 'my-repository'
        lo_ecr->deleterepository(
          iv_repositoryname = iv_repository_name
          iv_force = abap_true ).
        MESSAGE |Repository { iv_repository_name } deleted.| TYPE 'I'.
      CATCH /aws1/cx_ecrrepositorynotfndex.
        MESSAGE 'Repository not found.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DeleteRepository](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `DescribeImages` with an AWS SDK or CLI
<a name="example_ecr_DescribeImages_section"></a>

The following code examples show how to use `DescribeImages`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 

------
#### [ CLI ]

**AWS CLI**  
**To describe an image in a repository**  
The following `describe-images` example displays details about an image in the `cluster-autoscaler` repository with the tag `v1.13.6`.  

```
aws ecr describe-images \
    --repository-name {{cluster-autoscaler}} \
    --image-ids {{imageTag=v1.13.6}}
```
Output:  

```
{
    "imageDetails": [
        {
            "registryId": "012345678910",
            "repositoryName": "cluster-autoscaler",
            "imageDigest": "sha256:4a1c6567c38904384ebc64e35b7eeddd8451110c299e3368d2210066487d97e5",
            "imageTags": [
                "v1.13.6"
            ],
            "imageSizeInBytes": 48318255,
            "imagePushedAt": 1565128275.0
        }
    ]
}
```
+  For API details, see [DescribeImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-images.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     * @throws EcrException             if there is an error retrieving the image information from Amazon ECR.
     * @throws CompletionException      if the asynchronous operation completes exceptionally.
     */
    public void verifyImage(String repositoryName, String imageTag) {
        DescribeImagesRequest request = DescribeImagesRequest.builder()
            .repositoryName(repositoryName)
            .imageIds(ImageIdentifier.builder().imageTag(imageTag).build())
            .build();

        CompletableFuture<DescribeImagesResponse> response = getAsyncClient().describeImages(request);
        response.whenComplete((describeImagesResponse, ex) -> {
            if (ex != null) {
                if (ex instanceof CompletionException) {
                    Throwable cause = ex.getCause();
                    if (cause instanceof EcrException) {
                        throw (EcrException) cause;
                    } else {
                        throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                    }
                } else {
                    throw new RuntimeException("Unexpected error: " + ex.getCause());
                }
            } else if (describeImagesResponse != null && !describeImagesResponse.imageDetails().isEmpty()) {
                System.out.println("Image is present in the repository.");
            } else {
                System.out.println("Image is not present in the repository.");
            }
        });

        // Wait for the CompletableFuture to complete.
        response.join();
    }
```
+  For API details, see [DescribeImages](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeImages) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     */
    suspend fun verifyImage(
        repoName: String?,
        imageTagVal: String?,
    ) {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }
        require(!(imageTagVal == null || imageTagVal.isEmpty())) { "Image tag cannot be null or empty" }

        val imageId =
            ImageIdentifier {
                imageTag = imageTagVal
            }
        val request =
            DescribeImagesRequest {
                repositoryName = repoName
                imageIds = listOf(imageId)
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeImagesResponse = ecrClient.describeImages(request)
            if (describeImagesResponse != null && !describeImagesResponse.imageDetails?.isEmpty()!!) {
                println("Image is present in the repository.")
            } else {
                println("Image is not present in the repository.")
            }
        }
    }
```
+  For API details, see [DescribeImages](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def describe_images(
        self, repository_name: str, image_ids: list[str] = None
    ) -> list[dict]:
        """
        Describes ECR images.

        :param repository_name: The name of the repository to describe images for.
        :param image_ids: The optional IDs of images to describe.
        :return: The list of image descriptions.
        """
        try:
            params = {
                "repositoryName": repository_name,
            }
            if image_ids is not None:
                params["imageIds"] = [{"imageTag": tag} for tag in image_ids]

            paginator = self.ecr_client.get_paginator("describe_images")
            image_descriptions = []
            for page in paginator.paginate(**params):
                image_descriptions.extend(page["imageDetails"])
            return image_descriptions
        except ClientError as err:
            logger.error(
                "Couldn't describe images. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeImages](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeImages) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        " iv_repository_name = 'my-repository'
        " it_image_ids = VALUE #( ( NEW /aws1/cl_ecrimageidentifier( iv_imagetag = 'latest' ) ) )
        IF it_image_ids IS NOT INITIAL.
          oo_result = lo_ecr->describeimages(
            iv_repositoryname = iv_repository_name
            it_imageids = it_image_ids ).
        ELSE.
          oo_result = lo_ecr->describeimages(
            iv_repositoryname = iv_repository_name ).
        ENDIF.
        DATA(lt_image_details) = oo_result->get_imagedetails( ).
        MESSAGE |Found { lines( lt_image_details ) } images in repository.| TYPE 'I'.
      CATCH /aws1/cx_ecrrepositorynotfndex.
        MESSAGE 'Repository not found.' TYPE 'I'.
      CATCH /aws1/cx_ecrimagenotfoundex.
        MESSAGE 'Image not found.' TYPE 'I'.
      CATCH /aws1/cx_ecrinvalidparameterex.
        MESSAGE 'Invalid parameter provided.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DescribeImages](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `DescribeRepositories` with an AWS SDK or CLI
<a name="example_ecr_DescribeRepositories_section"></a>

The following code examples show how to use `DescribeRepositories`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 

------
#### [ CLI ]

**AWS CLI**  
**To describe the repositories in a registry**  
This example describes the repositories in the default registry for an account.  
Command:  

```
aws ecr describe-repositories
```
Output:  

```
{
    "repositories": [
        {
            "registryId": "012345678910",
            "repositoryName": "ubuntu",
            "repositoryArn": "arn:aws:ecr:us-west-2:012345678910:repository/ubuntu"
        },
        {
            "registryId": "012345678910",
            "repositoryName": "test",
            "repositoryArn": "arn:aws:ecr:us-west-2:012345678910:repository/test"
        }
    ]
}
```
+  For API details, see [DescribeRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-repositories.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Retrieves the repository URI for the specified repository name.
     *
     * @param repoName the name of the repository to retrieve the URI for.
     * @return the repository URI for the specified repository name.
     * @throws EcrException        if there is an error retrieving the repository information.
     * @throws CompletionException if the asynchronous operation completes exceptionally.
     */
    public void getRepositoryURI(String repoName) {
        DescribeRepositoriesRequest request = DescribeRepositoriesRequest.builder()
            .repositoryNames(repoName)
            .build();

        CompletableFuture<DescribeRepositoriesResponse> response = getAsyncClient().describeRepositories(request);
        response.whenComplete((describeRepositoriesResponse, ex) -> {
            if (ex != null) {
                Throwable cause = ex.getCause();
                if (cause instanceof InterruptedException) {
                    Thread.currentThread().interrupt();
                    String errorMessage = "Thread interrupted while waiting for asynchronous operation: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                } else if (cause instanceof EcrException) {
                    throw (EcrException) cause;
                } else {
                    String errorMessage = "Unexpected error: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                }
            } else {
                if (describeRepositoriesResponse != null) {
                    if (!describeRepositoriesResponse.repositories().isEmpty()) {
                        String repositoryUri = describeRepositoriesResponse.repositories().get(0).repositoryUri();
                        System.out.println("Repository URI found: " + repositoryUri);
                    } else {
                        System.out.println("No repositories found for the given name.");
                    }
                } else {
                    System.err.println("No response received from describeRepositories.");
                }
            }
        });
        response.join();
    }
```
+  For API details, see [DescribeRepositories](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeRepositories) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Retrieves the repository URI for the specified repository name.
     *
     * @param repoName the name of the repository to retrieve the URI for.
     * @return the repository URI for the specified repository name.
     */
    suspend fun getRepositoryURI(repoName: String?): String? {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }
        val request =
            DescribeRepositoriesRequest {
                repositoryNames = listOf(repoName)
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeRepositoriesResponse = ecrClient.describeRepositories(request)
            if (!describeRepositoriesResponse.repositories?.isEmpty()!!) {
                return describeRepositoriesResponse?.repositories?.get(0)?.repositoryUri
            } else {
                println("No repositories found for the given name.")
                return ""
            }
        }
    }
```
+  For API details, see [DescribeRepositories](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def describe_repositories(self, repository_names: list[str]) -> list[dict]:
        """
        Describes ECR repositories.

        :param repository_names: The names of the repositories to describe.
        :return: The list of repository descriptions.
        """
        try:
            response = self.ecr_client.describe_repositories(
                repositoryNames=repository_names
            )
            return response["repositories"]
        except ClientError as err:
            logger.error(
                "Couldn't describe repositories. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeRepositories](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeRepositories) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ Rust ]

**SDK for Rust**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecr#code-examples). 

```
async fn show_repos(client: &aws_sdk_ecr::Client) -> Result<(), aws_sdk_ecr::Error> {
    let rsp = client.describe_repositories().send().await?;

    let repos = rsp.repositories();

    println!("Found {} repositories:", repos.len());

    for repo in repos {
        println!("  ARN:  {}", repo.repository_arn().unwrap());
        println!("  Name: {}", repo.repository_name().unwrap());
    }

    Ok(())
}
```
+  For API details, see [DescribeRepositories](https://docs.rs/aws-sdk-ecr/latest/aws_sdk_ecr/client/struct.Client.html#method.describe_repositories) in *AWS SDK for Rust API reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        " it_repository_names = VALUE #( ( NEW /aws1/cl_ecrrepositorynamels00( iv_value = 'my-repository' ) ) )
        oo_result = lo_ecr->describerepositories(
          it_repositorynames = it_repository_names ).
        DATA(lt_repositories) = oo_result->get_repositories( ).
        MESSAGE |Found { lines( lt_repositories ) } repositories.| TYPE 'I'.
      CATCH /aws1/cx_ecrrepositorynotfndex.
        MESSAGE 'Repository not found.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DescribeRepositories](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `GetAuthorizationToken` with an AWS SDK or CLI
<a name="example_ecr_GetAuthorizationToken_section"></a>

The following code examples show how to use `GetAuthorizationToken`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 

------
#### [ CLI ]

**AWS CLI**  
**To get an authorization token for your default registry**  
The following `get-authorization-token` example command gets an authorization token for your default registry.  

```
aws ecr get-authorization-token
```
Output:  

```
{
    "authorizationData": [
        {
            "authorizationToken": "QVdTOkN...",
            "expiresAt": 1448875853.241,
            "proxyEndpoint": "https://123456789012.dkr.ecr.us-west-2.amazonaws.com"
        }
    ]
}
```
+  For API details, see [GetAuthorizationToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-authorization-token.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Retrieves the authorization token for Amazon Elastic Container Registry (ECR).
     * This method makes an asynchronous call to the ECR client to retrieve the authorization token.
     * If the operation is successful, the method prints the token to the console.
     * If an exception occurs, the method handles the exception and prints the error message.
     *
     * @throws EcrException     if there is an error retrieving the authorization token from ECR.
     * @throws RuntimeException if there is an unexpected error during the operation.
     */
    public void getAuthToken() {
        CompletableFuture<GetAuthorizationTokenResponse> response = getAsyncClient().getAuthorizationToken();
        response.whenComplete((authorizationTokenResponse, ex) -> {
            if (authorizationTokenResponse != null) {
                AuthorizationData authorizationData = authorizationTokenResponse.authorizationData().get(0);
                String token = authorizationData.authorizationToken();
                if (!token.isEmpty()) {
                    System.out.println("The token was successfully retrieved.");
                }
            } else {
                if (ex.getCause() instanceof EcrException) {
                    throw (EcrException) ex.getCause();
                } else {
                    String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                    throw new RuntimeException(errorMessage, ex); // Rethrow the exception
                }
            }
        });
        response.join();
    }
```
+  For API details, see [GetAuthorizationToken](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetAuthorizationToken) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Retrieves the authorization token for Amazon Elastic Container Registry (ECR).
     *
     */
    suspend fun getAuthToken() {
        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            // Retrieve the authorization token for ECR.
            val response = ecrClient.getAuthorizationToken()
            val authorizationData = response.authorizationData?.get(0)
            val token = authorizationData?.authorizationToken
            if (token != null) {
                println("The token was successfully retrieved.")
            }
        }
    }
```
+  For API details, see [GetAuthorizationToken](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def get_authorization_token(self) -> str:
        """
        Gets an authorization token for an ECR repository.

        :return: The authorization token.
        """
        try:
            response = self.ecr_client.get_authorization_token()
            return response["authorizationData"][0]["authorizationToken"]
        except ClientError as err:
            logger.error(
                "Couldn't get authorization token. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [GetAuthorizationToken](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetAuthorizationToken) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        oo_result = lo_ecr->getauthorizationtoken( ).
        DATA(lt_auth_data) = oo_result->get_authorizationdata( ).
        IF lines( lt_auth_data ) > 0.
          READ TABLE lt_auth_data INDEX 1 INTO DATA(lo_auth_data).
          DATA(lv_token) = lo_auth_data->get_authorizationtoken( ).
          MESSAGE 'Authorization token retrieved.' TYPE 'I'.
        ENDIF.
      CATCH /aws1/cx_ecrserverexception.
        MESSAGE 'Server exception occurred.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [GetAuthorizationToken](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `GetRepositoryPolicy` with an AWS SDK or CLI
<a name="example_ecr_GetRepositoryPolicy_section"></a>

The following code examples show how to use `GetRepositoryPolicy`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 

------
#### [ CLI ]

**AWS CLI**  
**To retrieve the repository policy for a repository**  
The following `get-repository-policy` example displays details about the repository policy for the `cluster-autoscaler` repository.  

```
aws ecr get-repository-policy \
    --repository-name {{cluster-autoscaler}}
```
Output:  

```
{
    "registryId": "012345678910",
    "repositoryName": "cluster-autoscaler",
    "policyText": "{\n  \"Version\" : \"2008-10-17\",\n  \"Statement\" : [ {\n    \"Sid\" : \"allow public pull\",\n    \"Effect\" : \"Allow\",\n    \"Principal\" : \"*\",\n    \"Action\" : [ \"ecr:BatchCheckLayerAvailability\", \"ecr:BatchGetImage\", \"ecr:GetDownloadUrlForLayer\" ]\n  } ]\n}"
}
```
+  For API details, see [GetRepositoryPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-repository-policy.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Gets the repository policy for the specified repository.
     *
     * @param repoName the name of the repository.
     * @throws EcrException if an AWS error occurs while getting the repository policy.
     */
    public String getRepoPolicy(String repoName) {
        if (repoName == null || repoName.isEmpty()) {
            throw new IllegalArgumentException("Repository name cannot be null or empty");
        }

        GetRepositoryPolicyRequest getRepositoryPolicyRequest = GetRepositoryPolicyRequest.builder()
            .repositoryName(repoName)
            .build();

        CompletableFuture<GetRepositoryPolicyResponse> response = getAsyncClient().getRepositoryPolicy(getRepositoryPolicyRequest);
        response.whenComplete((resp, ex) -> {
            if (resp != null) {
                System.out.println("Repository policy retrieved successfully.");
            } else {
                if (ex.getCause() instanceof EcrException) {
                    throw (EcrException) ex.getCause();
                } else {
                    String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                    throw new RuntimeException(errorMessage, ex);
                }
            }
        });

        GetRepositoryPolicyResponse result = response.join();
        return result != null ? result.policyText() : null;
    }
```
+  For API details, see [GetRepositoryPolicy](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetRepositoryPolicy) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Gets the repository policy for the specified repository.
     *
     * @param repoName the name of the repository.
     */
    suspend fun getRepoPolicy(repoName: String?): String? {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }

        // Create the request
        val getRepositoryPolicyRequest =
            GetRepositoryPolicyRequest {
                repositoryName = repoName
            }
        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val response = ecrClient.getRepositoryPolicy(getRepositoryPolicyRequest)
            val responseText = response.policyText
            return responseText
        }
    }
```
+  For API details, see [GetRepositoryPolicy](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def get_repository_policy(self, repository_name: str) -> str:
        """
        Gets the policy for an ECR repository.

        :param repository_name: The name of the repository to get the policy for.
        :return: The policy text.
        """
        try:
            response = self.ecr_client.get_repository_policy(
                repositoryName=repository_name
            )
            return response["policyText"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "RepositoryPolicyNotFoundException":
                logger.error("Repository does not exist. %s.", repository_name)
                raise
            else:
                logger.error(
                    "Couldn't get repository policy for repository %s. Here's why %s",
                    repository_name,
                    err.response["Error"]["Message"],
                )
                raise
```
+  For API details, see [GetRepositoryPolicy](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetRepositoryPolicy) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        " iv_repository_name = 'my-repository'
        oo_result = lo_ecr->getrepositorypolicy(
          iv_repositoryname = iv_repository_name ).
        DATA(lv_policy_text) = oo_result->get_policytext( ).
        MESSAGE 'Repository policy retrieved.' TYPE 'I'.
      CATCH /aws1/cx_ecrrepositorynotfndex.
        MESSAGE 'Repository not found.' TYPE 'I'.
      CATCH /aws1/cx_ecrrepositoryplynot00.
        MESSAGE 'Repository policy not found.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [GetRepositoryPolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `ListImages` with an AWS SDK or CLI
<a name="example_ecr_ListImages_section"></a>

The following code examples show how to use `ListImages`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ CLI ]

**AWS CLI**  
**To list the images in a repository**  
The following `list-images` example displays a list of the images in the `cluster-autoscaler` repository.  

```
aws ecr list-images \
    --repository-name {{cluster-autoscaler}}
```
Output:  

```
{
    "imageIds": [
        {
            "imageDigest": "sha256:99c6fb4377e9a420a1eb3b410a951c9f464eff3b7dbc76c65e434e39b94b6570",
            "imageTag": "v1.13.8"
        },
        {
            "imageDigest": "sha256:99c6fb4377e9a420a1eb3b410a951c9f464eff3b7dbc76c65e434e39b94b6570",
            "imageTag": "v1.13.7"
        },
        {
            "imageDigest": "sha256:4a1c6567c38904384ebc64e35b7eeddd8451110c299e3368d2210066487d97e5",
            "imageTag": "v1.13.6"
        }
    ]
}
```
+  For API details, see [ListImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-images.html) in *AWS CLI Command Reference*. 

------
#### [ Rust ]

**SDK for Rust**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecr#code-examples). 

```
async fn show_images(
    client: &aws_sdk_ecr::Client,
    repository: &str,
) -> Result<(), aws_sdk_ecr::Error> {
    let rsp = client
        .list_images()
        .repository_name(repository)
        .send()
        .await?;

    let images = rsp.image_ids();

    println!("found {} images", images.len());

    for image in images {
        println!(
            "image: {}:{}",
            image.image_tag().unwrap(),
            image.image_digest().unwrap()
        );
    }

    Ok(())
}
```
+  For API details, see [ListImages](https://docs.rs/aws-sdk-ecr/latest/aws_sdk_ecr/client/struct.Client.html#method.list_images) in *AWS SDK for Rust API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `PushImageCmd` with an AWS SDK
<a name="example_ecr_PushImageCmd_section"></a>

The following code examples show how to use `PushImageCmd`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Pushes a Docker image to an Amazon Elastic Container Registry (ECR) repository.
     *
     * @param repoName  the name of the ECR repository to push the image to.
     * @param imageName the name of the Docker image.
     */
    public void pushDockerImage(String repoName, String imageName) {
        System.out.println("Pushing " + imageName + " to Amazon ECR will take a few seconds.");
        CompletableFuture<AuthConfig> authResponseFuture = getAsyncClient().getAuthorizationToken()
            .thenApply(response -> {
                String token = response.authorizationData().get(0).authorizationToken();
                String decodedToken = new String(Base64.getDecoder().decode(token));
                String password = decodedToken.substring(4);

                DescribeRepositoriesResponse descrRepoResponse = getAsyncClient().describeRepositories(b -> b.repositoryNames(repoName)).join();
                Repository repoData = descrRepoResponse.repositories().stream().filter(r -> r.repositoryName().equals(repoName)).findFirst().orElse(null);
                assert repoData != null;
                String registryURL = repoData.repositoryUri().split("/")[0];

                AuthConfig authConfig = new AuthConfig()
                    .withUsername("AWS")
                    .withPassword(password)
                    .withRegistryAddress(registryURL);
                return authConfig;
            })
            .thenCompose(authConfig -> {
                DescribeRepositoriesResponse descrRepoResponse = getAsyncClient().describeRepositories(b -> b.repositoryNames(repoName)).join();
                Repository repoData = descrRepoResponse.repositories().stream().filter(r -> r.repositoryName().equals(repoName)).findFirst().orElse(null);
                getDockerClient().tagImageCmd(imageName + ":latest", repoData.repositoryUri() + ":latest", imageName).exec();
                try {
                    getDockerClient().pushImageCmd(repoData.repositoryUri()).withTag("echo-text").withAuthConfig(authConfig).start().awaitCompletion();
                    System.out.println("The " + imageName + " was pushed to ECR");

                } catch (InterruptedException e) {
                    throw (RuntimeException) e.getCause();
                }
                return CompletableFuture.completedFuture(authConfig);
            });

        authResponseFuture.join();
    }
```
+  For API details, see [PushImageCmd](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/PushImageCmd) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Pushes a Docker image to an Amazon Elastic Container Registry (ECR) repository.
     *
     * @param repoName the name of the ECR repository to push the image to.
     * @param imageName the name of the Docker image.
     */
    suspend fun pushDockerImage(
        repoName: String,
        imageName: String,
    ) {
        println("Pushing $imageName to $repoName will take a few seconds")
        val authConfig = getAuthConfig(repoName)

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val desRequest =
                DescribeRepositoriesRequest {
                    repositoryNames = listOf(repoName)
                }

            val describeRepoResponse = ecrClient.describeRepositories(desRequest)
            val repoData =
                describeRepoResponse.repositories?.firstOrNull { it.repositoryName == repoName }
                    ?: throw RuntimeException("Repository not found: $repoName")

            val tagImageCmd = getDockerClient()?.tagImageCmd("$imageName", "${repoData.repositoryUri}", imageName)
            if (tagImageCmd != null) {
                tagImageCmd.exec()
            }
            val pushImageCmd =
                repoData.repositoryUri?.let {
                    dockerClient?.pushImageCmd(it)
                        // ?.withTag("latest")
                        ?.withAuthConfig(authConfig)
                }

            try {
                if (pushImageCmd != null) {
                    pushImageCmd.start().awaitCompletion()
                }
                println("The $imageName was pushed to Amazon ECR")
            } catch (e: IOException) {
                throw RuntimeException(e)
            }
        }
    }
```
+  For API details, see [PushImageCmd](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `PutLifeCyclePolicy` with an AWS SDK or CLI
<a name="example_ecr_PutLifeCyclePolicy_section"></a>

The following code examples show how to use `PutLifeCyclePolicy`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ CLI ]

**AWS CLI**  
**To create a lifecycle policy**  
The following `put-lifecycle-policy` example creates a lifecycle policy for the specified repository in the default registry for an account.  

```
aws ecr put-lifecycle-policy \
    --repository-name {{"project-a/amazon-ecs-sample"}} \
    --lifecycle-policy-text {{"file://policy.json"}}
```
Contents of `policy.json`:  

```
{
   "rules": [
       {
           "rulePriority": 1,
           "description": "Expire images older than 14 days",
           "selection": {
               "tagStatus": "untagged",
               "countType": "sinceImagePushed",
               "countUnit": "days",
               "countNumber": 14
           },
           "action": {
               "type": "expire"
           }
       }
   ]
}
```
Output:  

```
{
   "registryId": "<aws_account_id>",
   "repositoryName": "project-a/amazon-ecs-sample",
   "lifecyclePolicyText": "{\"rules\":[{\"rulePriority\":1,\"description\":\"Expire images older than 14 days\",\"selection\":{\"tagStatus\":\"untagged\",\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":14},\"action\":{\"type\":\"expire\"}}]}"
}
```
For more information, see [Lifecycle Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) in the *Amazon ECR User Guide*.  
+  For API details, see [PutLifeCyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-life-cycle-policy.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def put_lifecycle_policy(self, repository_name: str, lifecycle_policy_text: str):
        """
        Puts a lifecycle policy for an ECR repository.

        :param repository_name: The name of the repository to put the lifecycle policy for.
        :param lifecycle_policy_text: The lifecycle policy text to put.
        """
        try:
            self.ecr_client.put_lifecycle_policy(
                repositoryName=repository_name,
                lifecyclePolicyText=lifecycle_policy_text,
            )
            print(f"Put lifecycle policy for repository {repository_name}.")
        except ClientError as err:
            logger.error(
                "Couldn't put lifecycle policy for repository %s. Here's why %s",
                repository_name,
                err.response["Error"]["Message"],
            )
            raise
```
Example that puts an expiration date policy.  

```
    def put_expiration_policy(self):
        """
        Puts an expiration policy on the ECR repository.
        """
        policy_json = {
            "rules": [
                {
                    "rulePriority": 1,
                    "description": "Expire images older than 14 days",
                    "selection": {
                        "tagStatus": "any",
                        "countType": "sinceImagePushed",
                        "countUnit": "days",
                        "countNumber": 14,
                    },
                    "action": {"type": "expire"},
                }
            ]
        }

        self.ecr_wrapper.put_lifecycle_policy(
            self.repository_name, json.dumps(policy_json)
        )
```
+  For API details, see [PutLifeCyclePolicy](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/PutLifeCyclePolicy) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        " iv_repository_name = 'my-repository'
        " iv_lifecycle_policy_text = '{"rules":[{"rulePriority":1,"description":"Expire images older than 14 days",...}]}'
        lo_ecr->putlifecyclepolicy(
          iv_repositoryname = iv_repository_name
          iv_lifecyclepolicytext = iv_lifecycle_policy_text ).
        MESSAGE |Lifecycle policy set for repository { iv_repository_name }.| TYPE 'I'.
      CATCH /aws1/cx_ecrrepositorynotfndex.
        MESSAGE 'Repository not found.' TYPE 'I'.
      CATCH /aws1/cx_ecrvalidationex.
        MESSAGE 'Invalid lifecycle policy format.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [PutLifeCyclePolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `SetRepositoryPolicy` with an AWS SDK or CLI
<a name="example_ecr_SetRepositoryPolicy_section"></a>

The following code examples show how to use `SetRepositoryPolicy`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 

------
#### [ CLI ]

**AWS CLI**  
**To set the repository policy for a repository**  
The following `set-repository-policy` example attaches a repository policy contained in a file to the `cluster-autoscaler` repository.  

```
aws ecr set-repository-policy \
    --repository-name {{cluster-autoscaler}} \
    --policy-text {{file://my-policy.json}}
```
Contents of `my-policy.json`:  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement" : [
        {
            "Sid" : "allow public pull",
            "Effect" : "Allow",
            "Principal" : "*",
            "Action" : [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ]
        }
    ]
}
```
Output:  

```
{
    "registryId": "012345678910",
    "repositoryName": "cluster-autoscaler",
    "policyText": "{\n  \"Version\" : \"2008-10-17\",\n  \"Statement\" : [ {\n    \"Sid\" : \"allow public pull\",\n    \"Effect\" : \"Allow\",\n    \"Principal\" : \"*\",\n    \"Action\" : [ \"ecr:BatchCheckLayerAvailability\", \"ecr:BatchGetImage\", \"ecr:GetDownloadUrlForLayer\" ]\n  } ]\n}"
}
```
+  For API details, see [SetRepositoryPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/set-repository-policy.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Sets the repository policy for the specified ECR repository.
     *
     * @param repoName the name of the ECR repository.
     * @param iamRole  the IAM role to be granted access to the repository.
     * @throws RepositoryPolicyNotFoundException if the repository policy does not exist.
     * @throws EcrException                      if there is an unexpected error setting the repository policy.
     */
    public void setRepoPolicy(String repoName, String iamRole) {
        /*
          This example policy document grants the specified AWS principal the permission to perform the
          `ecr:BatchGetImage` action. This policy is designed to allow the specified principal
          to retrieve Docker images from the ECR repository.
         */
        String policyDocumentTemplate = """
             {
              "Version":"2012-10-17",		 	 	 
              "Statement" : [ {
                "Sid" : "new statement",
                "Effect" : "Allow",
                "Principal" : {
                  "AWS" : "%s"
                },
                "Action" : "ecr:BatchGetImage"
              } ]
            }
             """;

        String policyDocument = String.format(policyDocumentTemplate, iamRole);
        SetRepositoryPolicyRequest setRepositoryPolicyRequest = SetRepositoryPolicyRequest.builder()
            .repositoryName(repoName)
            .policyText(policyDocument)
            .build();

        CompletableFuture<SetRepositoryPolicyResponse> response = getAsyncClient().setRepositoryPolicy(setRepositoryPolicyRequest);
        response.whenComplete((resp, ex) -> {
            if (resp != null) {
                System.out.println("Repository policy set successfully.");
            } else {
                Throwable cause = ex.getCause();
                if (cause instanceof RepositoryPolicyNotFoundException) {
                    throw (RepositoryPolicyNotFoundException) cause;
                } else if (cause instanceof EcrException) {
                    throw (EcrException) cause;
                } else {
                    String errorMessage = "Unexpected error: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                }
            }
        });
        response.join();
    }
```
+  For API details, see [SetRepositoryPolicy](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/SetRepositoryPolicy) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Sets the repository policy for the specified ECR repository.
     *
     * @param repoName the name of the ECR repository.
     * @param iamRole the IAM role to be granted access to the repository.
     */
    suspend fun setRepoPolicy(
        repoName: String?,
        iamRole: String?,
    ) {
        val policyDocumentTemplate =
            """
             {
              "Version":"2012-10-17",		 	 	 
              "Statement" : [ {
                "Sid" : "new statement",
                "Effect" : "Allow",
                "Principal" : {
                  "AWS" : "$iamRole"
                },
                "Action" : "ecr:BatchGetImage"
              } ]
            }
             
            """.trimIndent()
        val setRepositoryPolicyRequest =
            SetRepositoryPolicyRequest {
                repositoryName = repoName
                policyText = policyDocumentTemplate
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val response = ecrClient.setRepositoryPolicy(setRepositoryPolicyRequest)
            if (response != null) {
                println("Repository policy set successfully.")
            }
        }
    }
```
+  For API details, see [SetRepositoryPolicy](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples). 

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def set_repository_policy(self, repository_name: str, policy_text: str):
        """
        Sets the policy for an ECR repository.

        :param repository_name: The name of the repository to set the policy for.
        :param policy_text: The policy text to set.
        """
        try:
            self.ecr_client.set_repository_policy(
                repositoryName=repository_name, policyText=policy_text
            )
            print(f"Set repository policy for repository {repository_name}.")
        except ClientError as err:
            if err.response["Error"]["Code"] == "RepositoryPolicyNotFoundException":
                logger.error("Repository does not exist. %s.", repository_name)
                raise
            else:
                logger.error(
                    "Couldn't set repository policy for repository %s. Here's why %s",
                    repository_name,
                    err.response["Error"]["Message"],
                )
                raise
```
Example that grants an IAM role download access.  

```
    def grant_role_download_access(self, role_arn: str):
        """
        Grants the specified role access to download images from the ECR repository.

        :param role_arn: The ARN of the role to grant access to.
        """
        policy_json = {
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Sid": "AllowDownload",
                    "Effect": "Allow",
                    "Principal": {"AWS": role_arn},
                    "Action": ["ecr:BatchGetImage"],
                }
            ],
        }

        self.ecr_wrapper.set_repository_policy(
            self.repository_name, json.dumps(policy_json)
        )
```
+  For API details, see [SetRepositoryPolicy](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/SetRepositoryPolicy) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples). 

```
    TRY.
        " iv_repository_name = 'my-repository'
        " iv_policy_text = '{"Version":"2012-10-17",		 	 	 "Statement":[...]}'
        lo_ecr->setrepositorypolicy(
          iv_repositoryname = iv_repository_name
          iv_policytext = iv_policy_text ).
        MESSAGE |Policy set for repository { iv_repository_name }.| TYPE 'I'.
      CATCH /aws1/cx_ecrrepositorynotfndex.
        MESSAGE 'Repository not found.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [SetRepositoryPolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

#### Use `StartLifecyclePolicyPreview` with an AWS SDK or CLI
<a name="example_ecr_StartLifecyclePolicyPreview_section"></a>

The following code examples show how to use `StartLifecyclePolicyPreview`.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](#example_ecr_Scenario_RepositoryManagement_section) 

------
#### [ CLI ]

**AWS CLI**  
**To create a lifecycle policy preview**  
The following `start-lifecycle-policy-preview` example creates a lifecycle policy preview defined by a JSON file for the specified repository.  

```
aws ecr start-lifecycle-policy-preview \
    --repository-name {{"project-a/amazon-ecs-sample"}} \
    --lifecycle-policy-text {{"file://policy.json"}}
```
Contents of `policy.json`:  

```
{
   "rules": [
       {
           "rulePriority": 1,
           "description": "Expire images older than 14 days",
           "selection": {
               "tagStatus": "untagged",
               "countType": "sinceImagePushed",
               "countUnit": "days",
               "countNumber": 14
           },
           "action": {
               "type": "expire"
           }
       }
   ]
}
```
Output:  

```
{
   "registryId": "012345678910",
   "repositoryName": "project-a/amazon-ecs-sample",
   "lifecyclePolicyText": "{\n    \"rules\": [\n        {\n            \"rulePriority\": 1,\n            \"description\": \"Expire images older than 14 days\",\n            \"selection\": {\n                \"tagStatus\": \"untagged\",\n                \"countType\": \"sinceImagePushed\",\n                \"countUnit\": \"days\",\n                \"countNumber\": 14\n            },\n            \"action\": {\n                \"type\": \"expire\"\n            }\n        }\n    ]\n}\n",
   "status": "IN_PROGRESS"
}
```
+  For API details, see [StartLifecyclePolicyPreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/start-lifecycle-policy-preview.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples). 

```
    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     * @throws EcrException             if there is an error retrieving the image information from Amazon ECR.
     * @throws CompletionException      if the asynchronous operation completes exceptionally.
     */
    public void verifyImage(String repositoryName, String imageTag) {
        DescribeImagesRequest request = DescribeImagesRequest.builder()
            .repositoryName(repositoryName)
            .imageIds(ImageIdentifier.builder().imageTag(imageTag).build())
            .build();

        CompletableFuture<DescribeImagesResponse> response = getAsyncClient().describeImages(request);
        response.whenComplete((describeImagesResponse, ex) -> {
            if (ex != null) {
                if (ex instanceof CompletionException) {
                    Throwable cause = ex.getCause();
                    if (cause instanceof EcrException) {
                        throw (EcrException) cause;
                    } else {
                        throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                    }
                } else {
                    throw new RuntimeException("Unexpected error: " + ex.getCause());
                }
            } else if (describeImagesResponse != null && !describeImagesResponse.imageDetails().isEmpty()) {
                System.out.println("Image is present in the repository.");
            } else {
                System.out.println("Image is not present in the repository.");
            }
        });

        // Wait for the CompletableFuture to complete.
        response.join();
    }
```
+  For API details, see [StartLifecyclePolicyPreview](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/StartLifecyclePolicyPreview) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples). 

```
    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     */
    suspend fun verifyImage(
        repoName: String?,
        imageTagVal: String?,
    ) {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }
        require(!(imageTagVal == null || imageTagVal.isEmpty())) { "Image tag cannot be null or empty" }

        val imageId =
            ImageIdentifier {
                imageTag = imageTagVal
            }
        val request =
            DescribeImagesRequest {
                repositoryName = repoName
                imageIds = listOf(imageId)
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeImagesResponse = ecrClient.describeImages(request)
            if (describeImagesResponse != null && !describeImagesResponse.imageDetails?.isEmpty()!!) {
                println("Image is present in the repository.")
            } else {
                println("Image is not present in the repository.")
            }
        }
    }
```
+  For API details, see [StartLifecyclePolicyPreview](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

## Scenarios for Amazon ECR using AWS SDKs
<a name="service_code_examples_scenarios"></a>

The following code examples show you how to implement common scenarios in Amazon ECR with AWS SDKs. These scenarios show you how to accomplish specific tasks by calling multiple functions within Amazon ECR or combined with other AWS services. Each scenario includes a link to the complete source code, where you can find instructions on how to set up and run the code. 

Scenarios target an intermediate level of experience to help you understand service actions in context.

**Topics**
+ [Getting started with container registries](#example_ecr_GettingStarted_078_section)

### Getting started with container registries
<a name="example_ecr_GettingStarted_078_section"></a>

The following code example shows how to:
+ Create a Docker image
+ Create an Amazon ECR repository
+ Delete resources

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples). Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo. 

------
#### [ Bash ]

**AWS CLI with Bash script**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Sample developer tutorials](https://github.com/aws-samples/sample-developer-tutorials/tree/main/tuts/078-amazon-elastic-container-registry-gs) repository. 

```
#!/bin/bash

# Amazon ECR Getting Started Script
# This script demonstrates the lifecycle of a Docker image in Amazon ECR

# Set up logging
LOG_FILE="ecr-tutorial.log"
exec > >(tee -a "$LOG_FILE") 2>&1

echo "==================================================="
echo "Amazon ECR Getting Started Tutorial"
echo "==================================================="
echo "This script will:"
echo "1. Create a Docker image"
echo "2. Create an Amazon ECR repository"
echo "3. Authenticate to Amazon ECR"
echo "4. Push the image to Amazon ECR"
echo "5. Pull the image from Amazon ECR"
echo "6. Clean up resources (optional)"
echo "==================================================="

# Check prerequisites
echo "Checking prerequisites..."

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "ERROR: AWS CLI is not installed. Please install it before running this script."
    echo "Visit https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html for installation instructions."
    exit 1
fi

# Check if AWS CLI is configured
if ! aws sts get-caller-identity &> /dev/null; then
    echo "ERROR: AWS CLI is not configured properly. Please run 'aws configure' to set up your credentials."
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed. Please install Docker before running this script."
    echo "Visit https://docs.docker.com/get-docker/ for installation instructions."
    exit 1
fi

# Check if Docker daemon is running
if ! docker info &> /dev/null; then
    echo "ERROR: Docker daemon is not running. Please start Docker and try again."
    exit 1
fi

echo "All prerequisites met."

# Initialize variables
REPO_URI=""
TIMEOUT_CMD="timeout 300"  # 5-minute timeout for long-running commands

# Function to handle errors
handle_error() {
    echo "ERROR: $1"
    echo "Check the log file for details: $LOG_FILE"
    
    echo "==================================================="
    echo "Resources created:"
    echo "- Docker image: hello-world (local)"
    if [ -n "$REPO_URI" ]; then
        echo "- ECR Repository: hello-repository"
        echo "- ECR Image: $REPO_URI:latest"
    fi
    echo "==================================================="
    
    echo "Attempting to clean up resources..."
    cleanup
    exit 1
}

# Function to clean up resources
cleanup() {
    echo "==================================================="
    echo "Cleaning up resources..."
    
    # Delete the image from ECR if it exists
    if [ -n "$REPO_URI" ]; then
        echo "Deleting image from ECR repository..."
        aws ecr batch-delete-image --repository-name hello-repository --image-ids imageTag=latest || echo "Failed to delete image, it may not exist or may have already been deleted."
    fi
    
    # Delete the ECR repository if it exists
    if [ -n "$REPO_URI" ]; then
        echo "Deleting ECR repository..."
        aws ecr delete-repository --repository-name hello-repository --force || echo "Failed to delete repository, it may not exist or may have already been deleted."
    fi
    
    # Remove local Docker image
    echo "Removing local Docker image..."
    docker rmi hello-world:latest 2>/dev/null || echo "Failed to remove local image, it may not exist or may have already been deleted."
    if [ -n "$REPO_URI" ]; then
        docker rmi "$REPO_URI:latest" 2>/dev/null || echo "Failed to remove tagged image, it may not exist or may have already been deleted."
    fi
    
    echo "Cleanup completed."
    echo "==================================================="
}

# Step 1: Create a Docker image
echo "Step 1: Creating a Docker image"

# Create Dockerfile
echo "Creating Dockerfile..."
cat > Dockerfile << 'EOF'
FROM public.ecr.aws/amazonlinux/amazonlinux:latest

# Install dependencies
RUN yum update -y && \
 yum install -y httpd

# Install apache and write hello world message
RUN echo 'Hello World!' > /var/www/html/index.html

# Configure apache
RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
 echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
 echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
 chmod 755 /root/run_apache.sh

EXPOSE 80

CMD /root/run_apache.sh
EOF

# Build Docker image
echo "Building Docker image..."
$TIMEOUT_CMD docker build -t hello-world . || handle_error "Failed to build Docker image or operation timed out after 5 minutes"

# Verify image was created
echo "Verifying Docker image..."
docker images --filter reference=hello-world || handle_error "Failed to list Docker images"

echo "Docker image created successfully."

# Step 2: Create an Amazon ECR repository
echo "Step 2: Creating an Amazon ECR repository"

# Get AWS account ID
echo "Getting AWS account ID..."
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
if [[ -z "$AWS_ACCOUNT_ID" || "$AWS_ACCOUNT_ID" == *"error"* ]]; then
    handle_error "Failed to get AWS account ID. Make sure your AWS credentials are configured correctly."
fi
echo "AWS Account ID: $AWS_ACCOUNT_ID"

# Get current region
AWS_REGION=$(aws configure get region)
if [[ -z "$AWS_REGION" ]]; then
    AWS_REGION="us-east-1"  # Default to us-east-1 if no region is configured
    echo "No AWS region configured, defaulting to $AWS_REGION"
else
    echo "Using AWS region: $AWS_REGION"
fi

# Create ECR repository
echo "Creating ECR repository..."
REPO_RESULT=$(aws ecr create-repository --repository-name hello-repository --tags key=project,value=doc-smith key=tutorial,value=amazon-elastic-container-registry-gs)
if [[ -z "$REPO_RESULT" || "$REPO_RESULT" == *"error"* ]]; then
    handle_error "Failed to create ECR repository"
fi

# Extract repository URI
REPO_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-repository"
echo "Repository URI: $REPO_URI"

# Step 3: Authenticate to Amazon ECR
echo "Step 3: Authenticating to Amazon ECR"

echo "Getting ECR login password..."
aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com" || handle_error "Failed to authenticate to ECR"

echo "Successfully authenticated to ECR."

# Step 4: Push the image to Amazon ECR
echo "Step 4: Pushing the image to Amazon ECR"

# Tag the image
echo "Tagging Docker image..."
docker tag hello-world:latest "$REPO_URI:latest" || handle_error "Failed to tag Docker image"

# Push the image with timeout
echo "Pushing image to ECR..."
$TIMEOUT_CMD docker push "$REPO_URI:latest" || handle_error "Failed to push image to ECR or operation timed out after 5 minutes"

echo "Successfully pushed image to ECR."

# Step 5: Pull the image from Amazon ECR
echo "Step 5: Pulling the image from Amazon ECR"

# Remove local image to ensure we're pulling from ECR
echo "Removing local tagged image..."
docker rmi "$REPO_URI:latest" || echo "Warning: Failed to remove local tagged image"

# Pull the image with timeout
echo "Pulling image from ECR..."
$TIMEOUT_CMD docker pull "$REPO_URI:latest" || handle_error "Failed to pull image from ECR or operation timed out after 5 minutes"

echo "Successfully pulled image from ECR."

# List resources created
echo "==================================================="
echo "Resources created:"
echo "- Docker image: hello-world (local)"
echo "- ECR Repository: hello-repository"
echo "- ECR Image: $REPO_URI:latest"
echo "==================================================="

# Ask user if they want to clean up resources
echo ""
echo "==========================================="
echo "CLEANUP CONFIRMATION"
echo "==========================================="
echo "Do you want to clean up all created resources? (y/n): "
read -r CLEANUP_CHOICE

if [[ "$CLEANUP_CHOICE" =~ ^[Yy]$ ]]; then
    # Step 6: Delete the image from ECR
    echo "Step 6: Deleting the image from ECR"
    
    DELETE_IMAGE_RESULT=$(aws ecr batch-delete-image --repository-name hello-repository --image-ids imageTag=latest)
    if [[ -z "$DELETE_IMAGE_RESULT" || "$DELETE_IMAGE_RESULT" == *"error"* ]]; then
        echo "Warning: Failed to delete image from ECR"
    else
        echo "Successfully deleted image from ECR."
    fi
    
    # Step 7: Delete the ECR repository
    echo "Step 7: Deleting the ECR repository"
    
    DELETE_REPO_RESULT=$(aws ecr delete-repository --repository-name hello-repository --force)
    if [[ -z "$DELETE_REPO_RESULT" || "$DELETE_REPO_RESULT" == *"error"* ]]; then
        echo "Warning: Failed to delete ECR repository"
    else
        echo "Successfully deleted ECR repository."
    fi
    
    # Remove local Docker images
    echo "Removing local Docker images..."
    docker rmi hello-world:latest 2>/dev/null || echo "Warning: Failed to remove local image"
    
    echo "All resources have been cleaned up."
else
    echo "Resources were not cleaned up. You can manually clean up later with:"
    echo "aws ecr batch-delete-image --repository-name hello-repository --image-ids imageTag=latest"
    echo "aws ecr delete-repository --repository-name hello-repository --force"
    echo "docker rmi hello-world:latest"
    echo "docker rmi $REPO_URI:latest"
fi

echo "==================================================="
echo "Tutorial completed!"
echo "Log file: $LOG_FILE"
echo "==================================================="
```
+ For API details, see the following topics in *AWS CLI Command Reference*.
  + [BatchDeleteImage](https://docs.aws.amazon.com/goto/aws-cli/ecr-2015-09-21/BatchDeleteImage)
  + [CreateRepository](https://docs.aws.amazon.com/goto/aws-cli/ecr-2015-09-21/CreateRepository)
  + [DeleteRepository](https://docs.aws.amazon.com/goto/aws-cli/ecr-2015-09-21/DeleteRepository)
  + [GetCallerIdentity](https://docs.aws.amazon.com/goto/aws-cli/sts-2011-06-15/GetCallerIdentity)
  + [GetLoginPassword](https://docs.aws.amazon.com/goto/aws-cli/ecr-2015-09-21/GetLoginPassword)

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon ECR with an AWS SDK](#sdk-general-information-section). This topic also includes information about getting started and details about previous SDK versions.

# Amazon ECR service quotas
<a name="service-quotas"></a>

The following table provides the default service quotas for Amazon Elastic Container Registry (Amazon ECR).


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Basic image scans per 24 hours | Each supported Region: 100,000 | No | The maximum number of images that can be scanned within a 24 hour period in the current account and region using basic scanning. This limit includes both scan on push and manual scans. | 
| Filters per rule in a replication configuration | Each supported Region: 100 | No | The maximum number of filters per rule in a replication configuration. | 
| Images per repository | Each supported Region: 100,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-03A36CE1)  | The maximum number of images per repository. | 
| Layer parts | Each supported Region: 4,200 | No | The maximum number of layer parts. This is only applicable if you are using Amazon ECR API actions directly to initiate multipart uploads for image push operations. | 
| Lifecycle policy length | Each supported Region: 30,720 | No | The maximum number of characters in a lifecycle policy. | 
| Maximum layer part size | Each supported Region: 10 | No | The maximum size (MiB) of a layer part. This is only applicable if you are using Amazon ECR API actions directly to initiate multipart uploads for image push operations. | 
| Maximum layer size | Each supported Region: 52,000 | No | The maximum size (MiB) of a layer. | 
| Minimum layer part size | Each supported Region: 5 | No | The minimum size (MiB) of a layer part. This is only applicable if you are using Amazon ECR API actions directly to initiate multipart uploads for image push operations. | 
| Pull through cache rules per registry | Each supported Region: 50 | No | The maximum number of pull-through cache rules. | 
| Rate of BatchCheckLayerAvailability requests | Each supported Region: 1,000 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-B9173138)  | The maximum number of BatchCheckLayerAvailability requests that you can make per second in the current Region. When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped. | 
| Rate of BatchGetImage requests | Each supported Region: 2,000 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-16E70933)  | The maximum number of BatchGetImage requests that you can make per second in the current Region. When an image is pulled, the BatchGetImage API is called once to retrieve the image manifest. If you request a quota increase for this API, review your GetDownloadUrlForLayer usage as well. | 
| Rate of CompleteLayerUpload requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-44194860)  | The maximum number of CompleteLayerUpload requests that you can make per second in the current Region. When an image is pushed, the CompleteLayerUpload API is called once per each new image layer to verify that the upload has completed. | 
| Rate of GetAuthorizationToken requests | Each supported Region: 500 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-55A41110)  | The maximum number of GetAuthorizationToken requests that you can make per second in the current Region. | 
| Rate of GetDownloadUrlForLayer requests | Each supported Region: 3,000 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-A60A366D)  | The maximum number of GetDownloadUrlForLayer requests that you can make per second in the current Region. When an image is pulled, the GetDownloadUrlForLayer API is called once per image layer that is not already cached. If you request a quota increase for this API, review your BatchGetImage usage as well. | 
| Rate of InitiateLayerUpload requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-95B28F8D)  | The maximum number of InitiateLayerUpload requests that you can make per second in the current Region. When an image is pushed, the InitiateLayerUpload API is called once per image layer that has not already been uploaded. Whether or not an image layer has been uploaded is determined by the BatchCheckLayerAvailability API action. | 
| Rate of PutImage requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-AD52DFB2)  | The maximum number of PutImage requests that you can make per second in the current Region. When an image is pushed and all new image layers have been uploaded, the PutImage API is called once to create or update the image manifest and the tags associated with the image. | 
| Rate of UploadLayerPart requests | Each supported Region: 500 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-A1670B10)  | The maximum number of UploadLayerPart requests that you can make per second in the current Region. When an image is pushed, each new image layer is uploaded in parts and the UploadLayerPart API is called once per each new image layer part. | 
| Rate of image scans | Each supported Region: 1 | No | The maximum number of image scans per image, per 24 hours. | 
| Registered repositories | Each supported Region: 100,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/ecr/quotas/L-CFEB8E8D)  | The maximum number of repositories that you can create in this account in the current Region. | 
| Rules per lifecycle policy | Each supported Region: 50 | No | The maximum number of rules in a lifecycle policy | 
| Rules per replication configuration | Each supported Region: 25 | No | The maximum number of rules in a replication configuration. | 
| Tags per image | Each supported Region: 1,000 | No | The maximum number of tags per image. | 
| Unique destinations across all rules in a replication configuration | Each supported Region: 25 | No | The maximum number of unique destinations across all rules in a replication configuration. | 

## Managing your Amazon ECR service quotas in the AWS Management Console
<a name="service-quotas-console"></a>

Amazon ECR has integrated with Service Quotas, an AWS service that enables you to view and manage your quotas from a central location. For more information, see [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in the *Service Quotas User Guide*.

Service Quotas makes it easy to look up the value of all Amazon ECR service quotas.

**To view Amazon ECR service quotas (AWS Management Console)**

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS services**.

1. From the **AWS services** list, search for and select **Amazon Elastic Container Registry (Amazon ECR)**.

   In the **Service quotas** list, you can see the service quota name, applied value (if it is available), AWS default quota, and whether the quota value is adjustable.

1. To view additional information about a service quota, such as the description, choose the quota name.

To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-increase.html) in the *Service Quotas User Guide*.

### Creating a CloudWatch alarm to monitor API usage metrics
<a name="service-quota-alarm"></a>

Amazon ECR provides CloudWatch usage metrics that correspond to the AWS service quotas for each of the APIs involved with the registry authentication, image push, and image pull actions. In the Service Quotas console, you can visualize your usage on a graph and configure alarms that alert you when your usage approaches a service quota. For more information, see [Amazon ECR usage metrics](#monitoring-usage).

Use the following steps to create a CloudWatch alarm based on one of the Amazon ECR API usage metrics.

**To create an alarm based on your Amazon ECR usage quotas (AWS Management Console)**

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS services**.

1. From the **AWS services** list, search for and select **Amazon Elastic Container Registry (Amazon ECR)**.

1. In the **Service quotas** list, select the Amazon ECR usage quota you want to create an alarm for.

1. In the Amazon CloudWatch Events alarms section, choose **Create**.

1. For **Alarm threshold**, choose the percentage of your applied quota value that you want to set as the alarm value.

1. For **Alarm name**, enter a name for the alarm and then choose **Create**.

# Amazon ECR troubleshooting
<a name="troubleshooting"></a>

This chapter helps you find diagnostic information for Amazon ECR, and provides troubleshooting steps for common issues and error messages.

**Topics**
+ [Troubleshooting Docker commands and issues when using Amazon ECR](#common-errors-docker)
+ [Troubleshooting Amazon ECR error messages](#common-errors)

## Troubleshooting Docker commands and issues when using Amazon ECR
<a name="common-errors-docker"></a>

In some cases, running a Docker command against Amazon ECR might result in an error message. Some common error messages and potential solutions are explained below.

**Topics**
+ [Docker logs do not contain expected error messages](#debug)
+ [Error: "Filesystem Verification Failed" or "404: Image Not Found" when pulling an image from an Amazon ECR repository](#error-filesystem-verification-failed)
+ [Error: "Filesystem Layer Verification Failed" when pulling images from Amazon ECR](#error-filesystem-layer-verification)
+ [HTTP 403 Errors or "no basic auth credentials" error when pushing to repository](#error-403)

### Docker logs do not contain expected error messages
<a name="debug"></a>

To begin debugging any Docker-related issue, start by turning on Docker debugging output on the Docker daemon running on your host instances. If you are using images pulled from Amazon ECR on Amazon ECS container instances, see [Configuring verbose output from the Docker daemon](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-debug-mode.html) in the *Amazon Elastic Container Service Developer Guide*. 

### Error: "Filesystem Verification Failed" or "404: Image Not Found" when pulling an image from an Amazon ECR repository
<a name="error-filesystem-verification-failed"></a>

You may receive the error `Filesystem verification failed` when using the **docker pull** command to pull an image from an Amazon ECR repository with Docker 1.9 or above. You may receive the error `404: Image not found` when you are using Docker versions before 1.9. 

Some possible reasons and their explanations are given below.

The local disk is full  
If the local disk on which you're running **docker pull** is full, then the SHA-1 hash calculated on the local file may be different than the one calculated by Amazon ECR. Check that your local disk has enough remaining free space to store the Docker image you are pulling. You can also delete old images to make room for new ones. Use the **Docker images** command to see a list of all locally downloaded Docker images, along with their sizes. 

Client cannot connect to the remote repository due to network error  
Calls to an Amazon ECR repository require a functioning connection to the internet. Verify your network settings, and verify that other tools and applications can access resources on the internet. If you are running **docker pull** on an Amazon EC2 instance in a private subnet, verify that the subnet has a route to the internet. Use a network address translation (NAT) server or a managed NAT gateway.  
Currently, calls to an Amazon ECR repository also require network access through your corporate firewall to Amazon Simple Storage Service (Amazon S3). If your organization uses firewall software or a NAT device that allows service endpoints, ensure that the Amazon S3 service endpoints for your current Region are allowed.   
If you are using Docker behind an HTTP proxy, you can configure Docker with the appropriate proxy settings. For more information, see [HTTP proxy](https://docs.docker.com/engine/admin/systemd/#/http-proxy) in the Docker documentation. 

### Error: "Filesystem Layer Verification Failed" when pulling images from Amazon ECR
<a name="error-filesystem-layer-verification"></a>

You may receive the error `image image-name not found` when pulling images using the **docker pull** command. If you inspect the Docker logs, you may see an error like the following:

```
filesystem layer verification failed for digest sha256:2b96f...
```

This error indicates that one or more of the layers for your image has failed to download. Some possible reasons and their explanations are given below.

You are using an older version of Docker  
This error can occur in a small percentage of cases when using a Docker version less than 1.10. Upgrade your Docker client to 1.10 or greater.

Your client has encountered a network or disk error  
 A full disk or a network issue may prevent one or more layers from downloading, as discussed earlier about the `Filesystem verification failed` message. Follow the recommendations above to ensure that your filesystem is not full, and that you have enabled access to Amazon S3 from within your network.

### HTTP 403 Errors or "no basic auth credentials" error when pushing to repository
<a name="error-403"></a>

There are times when you may receive an `HTTP 403 (Forbidden)` error, or the error message `no basic auth credentials` from the **docker push** or **docker pull** commands, even if you have successfully authenticated to Docker using the **aws ecr get-login-password** command. The following are some known causes of this issue:

You have authenticated to a different region  
Authentication requests are tied to specific regions, and cannot be used across regions. For example, if you obtain an authorization token from US West (Oregon), you cannot use it to authenticate against your repositories in US East (N. Virginia). To resolve the issue, ensure that you have retrieved an authentication token from the same Region your repository exists in. For more information, see [Private registry authentication in Amazon ECR](#registry_auth).

You have authenticated to push to a repository you don't have permissions for  
You do not have the necessary permissions to push to the repository. For more information, see [Private repository policies in Amazon ECR](#repository-policies).

Your token has expired  
The default authorization token expiration period for tokens obtained using the `GetAuthorizationToken` operation is 12 hours.

Bug in `wincred` credential manager  
Some versions of Docker for Windows use a credential manager called `wincred`, which does not properly handle the Docker login command produced by **aws ecr get-login-password** (for more information, see [`CredsStore` fails with private repositories](https://github.com/moby/moby/issues/22910)). You can run the Docker login command that is output, but when you try to push or pull images, those commands fail. You can work around this bug by removing the `https://` scheme from the registry argument in the Docker login command that is output from **aws ecr get-login-password**. An example Docker login command without the HTTPS scheme is shown below.  

```
docker login -u AWS -p {{<password>}} {{<aws_account_id>}}.dkr.ecr.{{<region>}}.amazonaws.com
```

## Troubleshooting Amazon ECR error messages
<a name="common-errors"></a>

In some cases, an API call that you have initiated through the Amazon ECR console or the AWS CLI exits with an error message. Some common error messages and potential solutions are explained below. 

### HTTP 429: Too Many Requests or ThrottleException
<a name="error-429-too-many-requests"></a>

You may receive a `429: Too Many Requests` error or a `ThrottleException` error from one or more Amazon ECR actions or API calls. This indicates that you are calling a single endpoint in Amazon ECR repeatedly over a short interval, and that your requests are getting throttled. Throttling occurs when calls to a single endpoint from a single user exceed a certain threshold over a period of time.

Each API operations in Amazon ECR has a rate throttles associated with it. For example, the throttle for the [`GetAuthorizationToken`](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html) action is 20 transaction per second (TPS), with up to a 200 TPS burst allowed. In each region, each account receives a bucket that can store up to 200 `GetAuthorizationToken` credits. These credits are replenished at a rate of 20 per second. If your bucket has 200 credits, you could achieve 200 `GetAuthorizationToken` API transactions per second for one second, and then sustain 20 transactions per second indefinitely. For more information on the rate limits for Amazon ECR APIs, see [Amazon ECR service quotas](#service-quotas).

To handle throttling errors, implement a retry function with incremental backoff into your code. For more information, see [Retry behavior](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) in the *AWS SDKs and Tools Reference Guide*. Another option is to request a rate limit increase, which you can do using the Service Quotas console.  For more information, see [Managing your Amazon ECR service quotas in the AWS Management Console](#service-quotas-console)..

### HTTP 403: "User [arn] is not authorized to perform [operation]"
<a name="error-unauthorized"></a>

You may receive the following error when attempting to perform an action with Amazon ECR:

```
$ aws ecr get-login-password 
A client error (AccessDeniedException) occurred when calling the GetAuthorizationToken operation: 
    User: arn:aws:iam::{{account-number}}:user/{{username}} is not authorized to perform: 
    ecr:GetAuthorizationToken on resource: *
```

This indicates that your user does not have permissions granted to use Amazon ECR, or that those permissions are not set up correctly. In particular, if you are performing actions against an Amazon ECR repository, verify that the user has been granted permissions to access that repository. For more information about creating and verifying permissions for Amazon ECR, see [Identity and Access Management for Amazon Elastic Container Registry](#security-iam).

### HTTP 404: "Repository Does Not Exist" error
<a name="repo-does-not-exist-error"></a>

If you specify a Docker Hub repository that does not currently exist, Docker Hub creates it automatically. With Amazon ECR, new repositories must be explicitly created before they can be used. This prevents new repositories from being created accidentally (for example, due to typos), and it also ensures that an appropriate security access policy is explicitly assigned to any new repositories. For more information about creating repositories, see [Amazon ECR private repositories](#Repositories).

### Error: Cannot perform an interactive login from a non TTY device
<a name="cannot-perform-interactive-login"></a>

If you receive the error `Cannot perform an interactive login from a non TTY device`, the following troubleshooting steps should help.
+ Verify that you're using AWS CLI version 2 and that you don't have a conflicting version of AWS CLI version 1 on your system. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ Verify that you've configured your AWS CLI with valid credentials. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+ Verify that the syntax of your AWS CLI command is correct.

# Using Podman with Amazon ECR
<a name="Podman"></a>

Using Podman with Amazon ECR enables organizations to leverage the security and simplicity of Podman while benefiting from the scalability and reliability of Amazon ECR for container image management. By following the outlined steps and commands, developers and administrators can streamline their container workflows, enhance security, and optimize resource utilization. As containerization continues to gain momentum, using Podman and Amazon ECR provides a robust and flexible solution for managing and deploying containerized applications.

## Using Podman to authenticate with Amazon ECR
<a name="authentication-with-ecr"></a>

Before interacting with Amazon ECR using Podman, authentication is required. This can be achieved by running the ``aws ecr get-login-password`` command to retrieve an authentication token, and then using that token with the ``podman login`` command to authenticate with Amazon ECR.

```
aws ecr get-login-password --region {{<region>}} | podman login --username AWS --password-stdin {{<aws_account_id>}}.dkr.ecr.{{<region>}}.amazonaws.com
```

## Using the Amazon ECR credential helper with Podman
<a name="registry-auth-credential-helper-pod"></a>

Amazon ECR provides a Docker credential helper that works with Podman. The credential helper makes it easier to store and use Docker credentials when pushing and pulling images to Amazon ECR. For installation and configuration steps, see [Amazon ECR Docker Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper).

**Important**  
Podman only partially supports the Docker-creds-helper specification. Podman supports the `credHelpers` keyword in Docker configuration but does not support the `credsStore` keyword.  
To use the Amazon ECR credential helper with Podman, configure your Docker configuration file with the `credHelpers` format:  

```
{
    "credHelpers": {
        "public.ecr.aws": "ecr-login",
        "<aws_account_id>.dkr.ecr.<region>.amazonaws.com": "ecr-login"
    }
}
```
The following `credsStore` configuration is not supported by Podman:  

```
{
    "credsStore": "ecr-login"
}
```

**Note**  
The Amazon ECR Docker credential helper does not support multi-factor authentication (MFA) currently.

## Pulling images from Amazon ECR with Podman
<a name="pulling-images-from-ecr"></a>

After successful authentication, container images can be pulled from Amazon ECR using the ``podman pull`` command with the full Amazon ECR repository URI.

```
podman pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{repository_name}}:{{tag}}
```

## Running containers for Amazon ECR with Podman
<a name="running-containers-ecr"></a>

Once the desired image has been pulled, a container can be instantiated using the ``podman run`` command. 

```
podman run -d {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{repository_name}}:{{tag}}
```

## Pushing images to Amazon ECR with Podman
<a name="pushing-images-to-ecr"></a>

To push a local image to Amazon ECR, the image must first be tagged with the Amazon ECR repository URI using ``podman tag``, and then the ``podman push`` command can be used to upload the image to Amazon ECR. 

```
podman tag {{local_image}}:{{tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{repository_name}}:{{tag}} 
podman push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{repository_name}}:{{tag}}
```

# Document history
<a name="doc-history"></a>

The following table describes the important changes to the documentation since the last release of Amazon ECR. We also update the documentation frequently to address the feedback that you send us.


| Change | Description | Date | 
| --- | --- | --- | 
| Added migration guide for third-party registries | Amazon ECR added documentation describing how to identify, copy, and verify container images from third-party registries such as Docker Hub, GitHub Container Registry, and self-hosted registries into your Amazon ECR private registry. For more information, see [Migrate container images from a third-party registry](#migrate-from-third-party). | 15 June 2026 | 
| Clair-based scanning deprecation completed | As of February 2, 2026, Clair-based image scanning has been deprecated and all ECR accounts have been migrated to AWS native basic scanning. Documentation has been updated to remove Clair-specific content and reflect that AWS native is now the only implementation of basic scanning. | 2 February 2026 | 
| ECR managed signing | Amazon ECR now supports managed container image signing to enhance your security posture and eliminate the operational overhead of setting up signing. Container image signing allows you to verify that images are from trusted sources. For more information, see [Managed signing](#managed-signing). | 21 November 2025 | 
| IPv6 support for AWS PrivateLink (VPC endpoints) | Added support for dual-stack (IPv4 and IPv6) connectivity for Amazon ECR VPC endpoints powered by AWS PrivateLink. You can now create dual-stack VPC endpoints that handle traffic over both IPv4 and IPv6 private IP addresses. For more information, see [Amazon ECR interface VPC endpoints (AWS PrivateLink)](#vpc-endpoints). | 21 November 2025 | 
| ECR Archive feature | Amazon ECR has added support for archiving images for long-term retention. For more information, see [Archiving an image in Amazon ECR](#archive_restore_image). | 19 November 2025 | 
| Updated to include support for image tag immutability exclusion patterns | Amazon ECR has updated updated image tagging abilities to include image tag immutability exclusion patterns while creating and updating repositories. You can now to specify tags that can be updated even when tag immutability is enabled on a repository by defining wildcard patterns (such as, `latest`", `v*.beta`, ` dev-*`) to exclude specific tags from immutability rules while maintaining immutability for all other tags. For more information, see [Creating an Amazon ECR private repository to store images](#repository-create). | 23 July 2025 | 
| Updated Enhanced Image Scanning to provide image usage insights | Amazon ECR has updated updated Enhanced Image Scanning abilities to include visibility into how images are used on Amazon EKS and Amazon ECS. For more information, see [Scan images for OS and programming language package vulnerabilities in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-enhanced.html) . | 16 June 2025 | 
| IPv6 support | Added support for making requests to Amazon ECR registries using both IPv4-only and dual-stack (IPv4 and IPv6) endpoints. For more information, see [Making requests to Amazon ECR registries](#ecr-requests). | 30 April 2025 | 
| Added Amazon ECR private registry support to pull through cache | Amazon ECR added support for creating pull through cache rules for the Amazon ECR private registry. For more information, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache) and [Amazon ECR service-linked role for pull through cache](#slr-pullthroughcache). | 12 March 2025 | 
| Added support for setting registry policy scope | Amazon ECR added support for configuring registry policy scope for your private registry. For more information, see [Private registry permissions in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) and [Amazon ECR private registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry-permissions-account-settings). | 23 December 2024 | 
| [ AmazonEC2ContainerRegistryPullOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly) – New policy | Amazon ECR added a new policy that grants pull-only permissions to Amazon ECR. | 10 October 2024 | 
| Docker/OCI Client-proxied operations in CloudTrail events now point to  ecr.amazonaws.com | The value ecr.amazonaws.com replaces AWS Internal in User Agent (userAgent) and Source IP Address (sourceIPAddress) fields for CloudTrail events associated with Docker/OCI Client endpoints. For examples, see [Example: Image pull action](#cloudtrail-examples-image-pull) and [Example: Image push action](#cloudtrail-examples-image-pull). | 1 July 2024 | 
| Added description of new Amazon ECR service-linked role for repository creation templates. | Amazon ECR uses a service-linked role named ** AWSServiceRoleForECRTemplate** which gives permission for Amazon ECR to perform actions on your behalf to complete repository creation template actions. For more information, see [Amazon ECR service-linked role for repository creation templates](#slr-rct). | 20 June 2024 | 
| Added the ECRTemplateServiceRolePolicy service-linked role. | Added the ECRTemplateServiceRolePolicy service-linked role. For more information, see [`ECRTemplateServiceRolePolicy`](#security-iam-awsmanpol-ECRTemplateServiceRolePolicy) | 20 June 2024 | 
| Added cross-Region and cross-account replication to China Regions. | Amazon ECR added support to China Region for filtering which repositories are replicated. For more information, see [Private image replication in Amazon ECR](#replication) | 15 May 2024 | 
| Added GitLab container registry to pull through cache rules | Amazon ECR added support for creating pull through cache rules for the GitLab container registry. For more information, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache). | 8 May 2024 | 
| Amazon ECR lifecycle policy update to add support for using wildcards | Amazon ECR added support for wildcards in a lifecycle policy through the use of the `tagPatternList` parameter in a lifecycle policy rule. For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies). | 18 December 2023 | 
| Amazon ECR repository creation templates | Amazon ECR added support for repository creation templates. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](#repository-creation-templates). | 15 November 2023 | 
| Amazon ECR pull through cache added supported for authenticated upstream registries | Amazon ECR added support for using upstream registries that require authentication for your pull through cache rules. For more information, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache). | 15 November 2023 | 
| [ AWSECRPullThroughCache\_ServiceRolePolicy](#slr-pullthroughcache) – Update to an existing policy | Amazon ECR added new permissions to the ` AWSECRPullThroughCache_ServiceRolePolicy` policy. These permissions allow Amazon ECR to retrieve the encrypted contents of a Secrets Manager secret. This is required when using a pull through cache rule to cache images from an upstream registry that requires authentication. | November 15, 2023 | 
| Amazon ECR image signing | Amazon ECR and AWS Signer added support for creating and pushing container image signatures using the Notary client. For more information, see [Sign images in Amazon ECR](#image-signing). | 6 June 2023 | 
| Added Kubernetes container registry to pull through cache rules | Amazon ECR added support for creating pull through cache rules for the Kubernetes container registry. For more information, see [Sync an upstream registry with an Amazon ECR private registry](#pull-through-cache). | 1 June 2023 | 
| Amazon ECR enhanced scanning duration support | Amazon Inspector added support for setting the duration that your repositories are monitored for when enhanced scanning is enabled. For more information, see [Changing the enhanced scanning duration for images in Amazon Inspector](#image-scanning-enhanced-duration). | 28 June 2022 | 
| Amazon ECR sends repository pull count metrics to Amazon CloudWatch | Amazon ECR sends repository pull count metrics to Amazon CloudWatch. For more information, see [Amazon ECR repository metrics](#ecr-repository-metrics). | 6 January 2022 | 
| Expanded replication support | Amazon ECR added support for filtering which repositories are replicated. For more information, see [Private image replication in Amazon ECR](#replication). | 21 September 2021 | 
| AWS managed policies for Amazon ECR | Amazon ECR added documentation of AWS managed policies. For more information, see [AWS managed policies for Amazon Elastic Container Registry](#security-iam-awsmanpol). | 24 June 2021 | 
| Cross-Region and cross-account replication | Amazon ECR added support for configuring replication settings for your private registry. For more information, see [Private registry settings in Amazon ECR](#registry-settings). | 8 December 2020 | 
| OCI artifact support | Amazon ECR added support for pushing and pulling Open Container Initiative (OCI) artifacts. A new parameter `artifactMediaType` was added to the `DescribeImages` API response to indicate the type of artifact.<br />For more information, see [Pushing a Helm chart to an Amazon ECR private repository](#push-oci-artifact). | 24 August 2020 | 
| Encryption at rest | Amazon ECR added support for configuring encryption for your repositories using server-side encryption with customer managed keys stored in AWS Key Management Service (AWS KMS).<br />For more information, see [Encryption at rest](#encryption-at-rest). | 29 July 2020 | 
| Multi-architecture images | Amazon ECR added support for creating and pushing Docker manifest lists which are used for multi-architecture images.<br />For more information, see [Pushing a multi-architecture image to an Amazon ECR private repository](#docker-push-multi-architecture-image). | 28 April 2020 | 
| Amazon ECR Usage Metrics | Amazon ECR added CloudWatch usage metrics which provides visibility into your account's resource usage. You also have the ability to create CloudWatch alarms from both the CloudWatch and Service Quotas consoles to get alerts when your usage approaches your applied service quota.<br />For more information, see [Amazon ECR usage metrics](#monitoring-usage). | 28 Feb 2020 | 
| Updated Amazon ECR service quotas | Updated the Amazon ECR service quotas to include per-API quotas.<br />For more information, see [Amazon ECR service quotas](#service-quotas). | 19 Feb 2020 | 
| Added `get-login-password` command | Added support for **get-login-password**, which provides a simple and secure method for retrieving an authorization token.<br />For more information, see [Using an authorization token](#registry-auth-token). | 4 Feb 2020 | 
| Image Scanning | Added support for image scanning, which helps in identifying software vulnerabilities in your container images. Amazon ECR uses the Common Vulnerabilities and Exposures (CVEs) database from the open source CoreOS Clair project and provides you with a list of scan findings.<br />For more information, see [Scan images for software vulnerabilities in Amazon ECR](#image-scanning). | 24 Oct 2019 | 
| VPC Endpoint Policy | Added support for setting an IAM policy on the Amazon ECR interface VPC endpoints.<br />For more information, see [Create an endpoint policy for your Amazon ECR VPC endpoints](#ecr-vpc-endpoint-policy). | 26 Sept 2019 | 
| Image Tag Mutability | Added support for configuring a repository to be immutable to prevent image tags from being overwritten.<br />For more information, see [Preventing image tags from being overwritten in Amazon ECR](#image-tag-mutability). | 25 July 2019 | 
| Interface VPC Endpoints (AWS PrivateLink) | Added support for configuring interface VPC endpoints powered by AWS PrivateLink. This allows you to create a private connection between your VPC and Amazon ECR without requiring access over the internet, through a NAT instance, a VPN connection, or Direct Connect.<br />For more information, see [Amazon ECR interface VPC endpoints (AWS PrivateLink)](#vpc-endpoints). | 25 Jan 2019 | 
| Resource tagging | Amazon ECR added support for adding metadata tags to your repositories.<br />For more information, see [Tagging a private repository in Amazon ECR](#ecr-using-tags). | 18 Dec 2018 | 
| Amazon ECR Name Change | Amazon Elastic Container Registry is renamed (previously Amazon EC2 Container Registry). | 21 Nov 2017 | 
| Lifecycle Policies | Amazon ECR lifecycle policies enable you to specify the lifecycle management of images in a repository.<br />For more information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](#LifecyclePolicies). | 11 Oct 2017 | 
| Amazon ECR support for Docker image manifest 2, schema 2 | Amazon ECR now supports Docker Image Manifest V2 Schema 2 (used with Docker version 1.10 and newer).<br />For more information, see [Container image manifest format support in Amazon ECR](#image-manifest-formats). | 27 Jan 2017 | 
| Amazon ECR General Availability | Amazon Elastic Container Registry (Amazon ECR) is a managed AWS Docker registry service that is secure, scalable, and reliable. | 21 Dec 2015 | 