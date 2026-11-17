facts card: 20 facts
ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling
  claim: Use AWS Auto Scaling to manage scaling for multiple resources across multiple services; use EC2 Auto Scaling if you only need to scale Auto Scaling groups or only want to maintain the health of the EC2 fleet.
  scope: choice between EC2 Auto Scaling and AWS Auto Scaling.
  link: [multiple resources across multiple services](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling)
  link: [only need to scale Amazon EC2 Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling)
aws-auto-scaling-faq-application-auto-scaling-for-non-ec2
  claim: To scale a resource other than EC2, use the Application Auto Scaling API, which defines scaling policies or scheduled one-time or recurring actions for resources such as ECS services, EC2 Spot fleets, EMR clusters, AppStream 2.0 fleets, DynamoDB provisioned capacity, Aurora Replicas and SageMaker endpoint variants.
  scope: Application Auto Scaling (resources other than EC2).
  link: [you can use the Application Auto Scaling API](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2)
  link: [Amazon ECS services, Amazon EC2 Spot fleets](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2)
  link: [provisioned read and write capacity for Amazon DynamoDB](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2)
aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services
  claim: Well-Architected rule of thumb: use Amazon EC2 Auto Scaling for EC2 instances and Application Auto Scaling for other AWS services, such as AWS Lambda functions or Amazon ECS services.
  scope: AWS Well-Architected guidance.
  link: [use Amazon EC2 Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services)
  link: [For other AWS services, use Application Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services)
aws-auto-scaling-faq-definition
  claim: AWS Auto Scaling scales collections of related resources that support one application and configures consistent scaling policies across the full infrastructure stack behind it.
  scope: AWS Auto Scaling (service definition).
  link: [across the full infrastructure stack](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-definition)
  link: [scale collections of related resources](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-definition)
aws-auto-scaling-faq-creates-target-tracking-only
  claim: AWS Auto Scaling creates target tracking scaling policies only; for step scaling policies or scheduled scaling, use the individual service consoles or APIs.
  scope: per scaling plan.
  link: [target tracking scaling policies only](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-creates-target-tracking-only)
  link: [step scaling policies or scheduled scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-creates-target-tracking-only)
aws-auto-scaling-aas-policy-types
  claim: Application Auto Scaling scales its resources with target tracking scaling, step scaling, scheduled scaling and predictive scaling.
  scope: Application Auto Scaling scalable targets.
  link: [Target tracking scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
  link: [Step scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
  link: [Scheduled scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
  link: [Predictive scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
ec2-auto-scaling-scaling-methods
  claim: EC2 Auto Scaling can scale by schedule, as a function of date and time; dynamically, with a scaling policy that resizes the group to meet changes in demand; and predictively, combined with dynamic scaling, to add instances in advance of daily and weekly traffic patterns.
  scope: per Auto Scaling group.
  link: [as a function of date and time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-methods)
  link: [dynamically resizes your Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-methods)
  link: [combine predictive scaling and dynamic scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-methods)
ec2-auto-scaling-vertical-resize-instance-type
  claim: Vertical scaling (scaling up) adds more power to existing infrastructure, such as more CPU or memory for an instance; you resize an EC2 instance by changing its instance type, and you then pay the rate of the new instance type.
  scope: per EC2 instance.
  link: [resize your instance by changing its instance type](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-resize-instance-type)
  link: [paying the rate of the new instance type](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-resize-instance-type)
ec2-auto-scaling-vertical-stop-required
  claim: You must stop an EBS-backed instance before you can change its instance type, so plan for downtime while the instance is stopped.
  scope: per EBS-backed EC2 instance.
  link: [You must stop your instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stop-required)
  link: [plan for downtime](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stop-required)
ec2-auto-scaling-decision-guide-horizontal-for-fluctuating
  claim: The AWS compute decision guide calls horizontal scalability (adding instances) essential for dynamic workloads with fluctuating demand.
  scope: AWS compute decision guide.
  link: [essential for dynamic workloads with fluctuating demands](../facts/ec2-auto-scaling.md#ec2-auto-scaling-decision-guide-horizontal-for-fluctuating)
ec2-auto-scaling-wa-stateless-scales-horizontally
  claim: Stateless applications can scale horizontally because any available compute resource, such as an EC2 instance or a Lambda function, can serve any request.
  scope: AWS Well-Architected guidance.
  link: [they can scale horizontally](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-stateless-scales-horizontally)
ec2-auto-scaling-wa-stateless-servers-replaceable
  claim: Well-Architected REL05-BP06: a system that keeps no state on local disk or memory between requests lets servers be replaced at will without an availability impact.
  scope: AWS Well-Architected guidance.
  link: [replaced at will without causing an availability impact](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-stateless-servers-replaceable)
ec2-auto-scaling-scheduled-action-sets-capacities
  claim: A scheduled action sets the group's desired, minimum and maximum capacity at a specified date and time; you give a new desired capacity and optionally a new minimum and maximum.
  scope: per scheduled action.
  link: [desired, minimum, and maximum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-sets-capacities)
  link: [optionally a new minimum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-sets-capacities)
ec2-auto-scaling-faq-predictive-ahead-of-demand
  claim: For predictable load changes, a predictive scaling policy proactively increases capacity ahead of upcoming demand.
  scope: per predictive scaling policy.
  link: [proactively increase capacity ahead of upcoming demand](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-ahead-of-demand)
ec2-auto-scaling-scheduled-vs-dynamic-when-to-use
  claim: Choose scheduled scaling when you know exactly when capacity must change because demand follows a predictable schedule; choose dynamic scaling when traffic changes at times you cannot predict.
  scope: per Auto Scaling group.
  link: [the need arises on a predictable schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-vs-dynamic-when-to-use)
  link: [you don't know when the traffic will change](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-vs-dynamic-when-to-use)
ec2-auto-scaling-predictive-long-initialization-fit
  claim: Predictive scaling suits regular traffic patterns and applications that take a long time to initialize, because it launches capacity before forecasted load while dynamic scaling is reactive.
  scope: per predictive scaling policy.
  link: [take a long time to initialize](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-long-initialization-fit)
  link: [launching capacity in advance of forecasted load](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-long-initialization-fit)
  link: [which is reactive in nature](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-long-initialization-fit)
ec2-auto-scaling-target-tracking-scale-in-gradual
  claim: A target tracking policy prioritizes availability by scaling in more gradually when traffic decreases; a step scaling policy gives more control.
  scope: per target tracking scaling policy.
  link: [scaling in more gradually when traffic is decreasing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-scale-in-gradual)
  link: [prioritizes availability](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-scale-in-gradual)
ec2-auto-scaling-predictive-does-not-scale-in
  claim: Predictive scaling does not scale in when the forecast expects less load; you need dynamic scaling policies to remove capacity.
  scope: per predictive scaling policy.
  link: [it will not scale in to remove capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-does-not-scale-in)
  say: it will not scale in
ec2-auto-scaling-predictive-needs-24-hours-of-data
  claim: A predictive scaling policy needs at least 24 hours of metric data before it can start forecasting.
  scope: per predictive scaling policy; minimum; not adjustable.
  link: [at least 24 hours of data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-needs-24-hours-of-data)
  say: at least twenty-four hours of data
ec2-auto-scaling-faq-group-size-bounded-by-ec2-quota
  claim: A group can have as many instances as the account's EC2 quota allows.
  scope: per Auto Scaling group; maximum; adjustable; bounded by the account's EC2 instance quota.
  link: [as your EC2 quota allows](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-group-size-bounded-by-ec2-quota)
  say: as many instances as your EC2 quota allows
