facts card: 13 facts
aws-auto-scaling-faq-scaling-plan-definition
  claim: A scaling plan is a collection of scaling instructions for multiple AWS resources; its key parameters are a resource utilization metric with a target value and an incoming traffic metric that Predictive Scaling uses for forecasts.
  scope: per AWS Auto Scaling scaling plan.
  link: [collection of scaling instructions for multiple AWS resources](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scaling-plan-definition)
  link: [resource utilization metric and the incoming traffic metric](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scaling-plan-definition)
aws-auto-scaling-faq-scalable-resource-list
  claim: Through one unified interface, AWS Auto Scaling can scale EC2 Auto Scaling groups, ECS services, EC2 Spot Fleets, DynamoDB throughput capacity and Aurora replicas.
  scope: per scaling plan.
  link: [Amazon EC2 Auto Scaling groups](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scalable-resource-list)
  link: [Amazon DynamoDB throughput capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scalable-resource-list)
  link: [Aurora replicas for Amazon Aurora](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scalable-resource-list)
aws-auto-scaling-faq-three-scaling-strategies
  claim: A scaling plan sets target values from three predefined scaling recommendations (optimize availability, optimize costs, or balance the two), or from target values you define yourself.
  scope: per scaling plan.
  link: [optimize availability, optimize costs, or balance the two](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-three-scaling-strategies)
  say: optimize availability, optimize costs, or balance the two
aws-auto-scaling-faq-discovery-scans-stack-or-tags
  claim: AWS Auto Scaling scans the selected CloudFormation stack, or the resources with the specified tags, to identify the supported resource types that can be scaled; ECS services cannot currently be discovered using tags.
  scope: per scaling plan; the tag limitation is stated as current ('currently').
  link: [scan your selected AWS CloudFormation stack](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-discovery-scans-stack-or-tags)
  link: [ECS services cannot be discovered using tags](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-discovery-scans-stack-or-tags)
  say: it scans your stack or your tagged resources | ECS services are not found by tags
aws-auto-scaling-faq-when-to-use
  claim: Use AWS Auto Scaling for an application that uses one or more scalable resources and experiences variable load, for example a three-tier web application with EC2 Auto Scaling groups and DynamoDB tables scaled together.
  scope: choice of AWS Auto Scaling for an application.
  link: [experiences variable load](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-when-to-use)
aws-auto-scaling-plans-prefer-native-predictive-policies
  claim: If you use AWS Auto Scaling scaling plans only for predictive scaling, AWS strongly recommends setting predictive scaling policies directly on the Auto Scaling resources instead, because that option has more features.
  scope: per AWS Auto Scaling scaling plan; scaling plan used only for predictive scaling.
  link: [directly on your Auto Scaling resources instead](../facts/aws-auto-scaling.md#aws-auto-scaling-plans-prefer-native-predictive-policies)
aws-auto-scaling-faq-free-cloudwatch-fees-apply
  claim: AWS Auto Scaling is free to use; because it is enabled by Amazon CloudWatch, service fees apply for CloudWatch and for your application resources, such as EC2 instances and Elastic Load Balancing load balancers.
  scope: per account; fixed.
  link: [free to use](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-free-cloudwatch-fees-apply)
  say: free to use
aws-auto-scaling-plans-one-plan-per-resource
  claim: A scaling plan can contain resources from multiple services, but each resource can be in only one scaling plan at a time.
  scope: per scalable resource.
  link: [only one scaling plan at a time](../facts/aws-auto-scaling.md#aws-auto-scaling-plans-one-plan-per-resource)
ec2-auto-scaling-faq-groups-created-outside-aws-auto-scaling
  claim: EC2 Auto Scaling groups must be created and configured outside of AWS Auto Scaling, for example through the EC2 console, the Auto Scaling API or CloudFormation; AWS Auto Scaling can help you configure dynamic scaling policies for existing groups.
  scope: per Auto Scaling group used in a scaling plan.
  link: [created and configured outside of AWS Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-groups-created-outside-aws-auto-scaling)
aws-auto-scaling-aas-scalable-target-identity
  claim: In Application Auto Scaling, a scalable target is the resource you want to scale, identified by a service namespace, a resource ID and a scalable dimension.
  scope: per Application Auto Scaling scalable target.
  link: [service namespace, resource ID, and scalable dimension](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-target-identity)
  link: [specify the resource that you want to scale](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-target-identity)
aws-auto-scaling-aas-scalable-dimension-examples
  claim: Examples of scalable dimensions: an ECS service scales its task count, a DynamoDB table scales its read and write capacity (and that of its global secondary indexes), and an Aurora cluster scales its replica count.
  scope: per Application Auto Scaling scalable target.
  link: [auto scaling of its task count](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-dimension-examples)
  link: [the read and write capacity of the table](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-dimension-examples)
  link: [scaling of its replica count](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-dimension-examples)
ec2-auto-scaling-faq-predictive-policy-vs-scaling-plan
  claim: A predictive scaling policy brings a prediction algorithm similar to the one offered through an AWS Auto Scaling plan into EC2 Auto Scaling as a native scaling policy, so you do not have to create a scaling plan just to use predictive scaling.
  scope: per predictive scaling policy.
  link: [native scaling policy in EC2 Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-policy-vs-scaling-plan)
  link: [create an AWS Auto Scaling plan](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-policy-vs-scaling-plan)
aws-auto-scaling-change-scaling-plan-migration-2024
  claim: On April 5, 2024 AWS added guidance to migrate from AWS Auto Scaling scaling plans to Amazon EC2 Auto Scaling predictive scaling, which offers more functionality; the migration moves a plan to EC2 Auto Scaling and Application Auto Scaling scaling policies.
  scope: AWS Auto Scaling scaling plans.
  link: [April 5, 2024](../facts/aws-auto-scaling.md#aws-auto-scaling-change-scaling-plan-migration-2024)
  link: [migrate from AWS Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-change-scaling-plan-migration-2024)
