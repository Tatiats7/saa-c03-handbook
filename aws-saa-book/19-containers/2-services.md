---
chapter: "19"
file: services
title: ECS and EKS outside AWS, card by card
status: ready
updated: 2026-10-14
---

# ECS and EKS outside AWS, card by card

## Amazon ECS Anywhere (1 min)
<!-- section: role=card; route=full; minutes=1; service=ecs-anywhere -->

**What it is.** A feature of Amazon ECS that lets you [run and manage container-based applications on-premises](../facts/ecs-anywhere.md#ecs-anywhere-faq-what-it-is), on your own virtual machines and servers.

**Stem signals.**

- "run containers on the company's own servers with the same ECS tools and APIs"
- "manage on-premises and cloud containers from one ECS cluster"
- "move on-premises container workloads to Fargate later"

**Do not confuse with.** Amazon EKS Anywhere runs Kubernetes clusters that you operate yourself, [including in air-gapped environments](../facts/eks-anywhere.md#eks-anywhere-faq-connected-or-air-gapped). ECS Anywhere keeps the control plane in the AWS Region, so each server needs a [stable internet connection](../facts/ecs-anywhere.md#ecs-anywhere-faq-needs-stable-internet-not-air-gapped).

**One fact.** Each server joins an ECS cluster as an external instance, which suits applications that [generate outbound traffic or process data](../facts/ecs-anywhere.md#ecs-anywhere-external-instances-outbound-workloads). Without Elastic Load Balancing support, an application that needs inbound traffic runs less efficiently.

> **Say it:** ECS Anywhere runs ECS tasks on your own servers. The control plane stays in the AWS Region, so the site needs the internet.

**Source.** [Amazon ECS Anywhere FAQs](https://aws.amazon.com/ecs/anywhere/faqs/)

## Amazon EKS Anywhere (1 min)
<!-- section: role=card; route=full; minutes=1; service=eks-anywhere -->

**What it is.** A [customer-managed product](../facts/eks-anywhere.md#eks-anywhere-faq-customer-managed-product) for Kubernetes clusters on your own infrastructure, and you run the cluster lifecycle and maintenance yourself. It uses [the same Kubernetes distribution deployed by Amazon EKS](../facts/eks-anywhere.md#eks-anywhere-faq-uses-eks-distro) and runs connected to an AWS Region or disconnected from it.

**Stem signals.**

- "Kubernetes in a data center with no connection to the internet"
- "Kubernetes on VMware vSphere or bare metal servers on premises"

**Do not confuse with.** Amazon EKS Hybrid Nodes: [AWS manages the AWS-hosted Kubernetes control plane](../facts/eks.md#eks-hybrid-nodes-on-premises-control-plane-aws), your servers join as nodes, and the site [must have a reliable connection](../facts/eks.md#eks-hybrid-nodes-need-reliable-connection). Amazon EKS Distro gives the Kubernetes build, and you prepare the servers and networking yourself.

**One fact.** EKS Anywhere is [not supported on AWS Cloud](../facts/eks-anywhere.md#eks-anywhere-faq-not-supported-on-aws-cloud). For Kubernetes on AWS, use Amazon EKS.

> **Say it:** EKS Anywhere is Kubernetes from AWS that you run in your own data center. It also works with no connection to AWS.

**Source.** [Amazon EKS Anywhere FAQs](https://aws.amazon.com/eks/eks-anywhere/faqs/)

## Amazon EKS Distro (1 min)
<!-- section: role=card; route=full; minutes=1; service=eks-distro -->

**What it is.** The open-source Kubernetes and dependencies that Amazon EKS deploys, packaged so that you can [manually run Kubernetes clusters anywhere](../facts/eks-distro.md#eks-distro-faq-same-kubernetes-as-eks-run-it-yourself). You can create clusters on Amazon EC2, [on premises on your own hardware](../facts/eks-distro.md#eks-distro-faq-clusters-on-ec2-on-premises-other-clouds), or in other clouds.

**Stem signals.**

- "the same Kubernetes versions and builds as Amazon EKS, with the company's own tooling"
- "Kubernetes clusters on premises or in other clouds, run by the company"

**Do not confuse with.** Amazon EKS is a [managed service](../facts/eks.md#eks-faq-managed-kubernetes-no-control-plane-to-run) that runs the control plane for you. Amazon EKS Anywhere packages EKS Distro for [VMware vSphere, bare metal, Nutanix](../facts/eks-anywhere.md#eks-anywhere-faq-built-on-cluster-api-infrastructure) and other platforms. For EKS Distro, AWS reviews the issues that customers submit, but fixes are on a [best effort basis](../facts/eks-distro.md#eks-distro-faq-support-best-effort).

**One fact.** EKS Distro does not include [the official Kubernetes network, storage plugins](../facts/eks-distro.md#eks-distro-faq-does-not-include-iam-authenticator-or-plugins) or the AWS IAM authenticator.

> **Say it:** EKS Distro is the Kubernetes build that EKS uses. You install it, run it and support it yourself.

**Source.** [Amazon EKS Distro FAQs](https://aws.amazon.com/eks/eks-distro/faqs/)
