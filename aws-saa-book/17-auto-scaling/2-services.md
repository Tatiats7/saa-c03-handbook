---
chapter: "17"
file: services
title: AWS Auto Scaling in one card
status: ready
updated: 2026-10-13
---

# AWS Auto Scaling in one card

## AWS Auto Scaling (1 min)
<!-- section: role=card; route=full; minutes=1; service=aws-auto-scaling -->

**What it is.** A service that lets you [scale collections of related resources](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-definition) that support one application. You create a scaling plan: a [collection of scaling instructions for multiple AWS resources](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scaling-plan-definition).

**Stem signals.**

- "scale the EC2 instances, DynamoDB tables and Aurora replicas of one application together"
- "optimize availability, optimize costs, or balance the two"

**Do not confuse with.**

- **Wrong belief:** Application Auto Scaling scales the instances of an EC2 Auto Scaling group. **Truth:** For EC2 instances, [use Amazon EC2 Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services). <!-- trap: auto-scaling-trap-application-auto-scaling-for-ec2 -->
- **Wrong belief:** EC2 Auto Scaling also scales an ECS service or a DynamoDB table. **Truth:** It is the choice when you [only need to scale Amazon EC2 Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling) groups. For other resources, [you can use the Application Auto Scaling API](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2). <!-- trap: auto-scaling-trap-ec2-auto-scaling-for-any-resource -->

**One fact.** A scaling plan creates [target tracking scaling policies only](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-creates-target-tracking-only); for [step scaling policies or scheduled scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-creates-target-tracking-only), use each service. A plan can add predictive scaling, which [only generates schedules for EC2 instances](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-ec2-only-in-plans). For predictive scaling alone, AWS recommends predictive scaling policies [directly on your Auto Scaling resources instead](../facts/aws-auto-scaling.md#aws-auto-scaling-plans-prefer-native-predictive-policies).

> **Say it:** AWS Auto Scaling builds one scaling plan for the resources of one application. For a single EC2 group, use EC2 Auto Scaling.

**Source.** [What is a scaling plan?](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html)
