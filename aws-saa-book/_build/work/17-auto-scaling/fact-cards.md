facts card: 522 facts
aws-auto-scaling-aas-cooldown-larger-scale-out
  claim: Application Auto Scaling keeps evaluating metrics during a cooldown period, and if a larger scale-out is needed during the cooldown the policy scales out immediately.
  scope: per Application Auto Scaling scalable target.
  link: [continues to evaluate metrics during the cooldown](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-cooldown-larger-scale-out)
  link: [the scaling policy scales out immediately](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-cooldown-larger-scale-out)
aws-auto-scaling-aas-off-by-default
  claim: For the services that integrate with Application Auto Scaling, auto scaling is an optional feature that is disabled by default in almost all cases.
  scope: per integrated AWS service; default; adjustable.
  link: [disabled by default in almost all cases](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-off-by-default)
  link: [an optional feature of the service](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-off-by-default)
aws-auto-scaling-aas-out-of-band-corrected
  claim: Capacity changed out of band outside a scalable target's minimum-maximum range is brought back into that range the next time a scaling policy is invoked or RegisterScalableTarget is called.
  scope: per Application Auto Scaling scalable target.
  link: [out-of-band changes](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-out-of-band-corrected)
  link: [updated to comply with the set minimum](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-out-of-band-corrected)
aws-auto-scaling-aas-policy-types
  claim: Application Auto Scaling scales its resources with target tracking scaling, step scaling, scheduled scaling and predictive scaling.
  scope: Application Auto Scaling scalable targets.
  link: [Target tracking scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
  link: [Step scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
  link: [Scheduled scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
  link: [Predictive scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types)
aws-auto-scaling-aas-predictive-history-and-horizon
  claim: Application Auto Scaling predictive scaling analyzes metric data from up to the past 14 days, makes an hourly forecast for the next 48 hours, and updates the forecast every 6 hours.
  scope: per Application Auto Scaling predictive scaling policy.
  link: [up to the past 14 days](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-history-and-horizon)
  link: [next 48 hours](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-history-and-horizon)
  link: [every 6 hours](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-history-and-horizon)
aws-auto-scaling-aas-predictive-max-capacity-breach
  claim: By default Application Auto Scaling scaling policies cannot raise capacity above the maximum capacity; if you let predictive scaling raise the maximum automatically, the maximum does not automatically go back down to the original value.
  scope: per Application Auto Scaling scalable target; MaxCapacityBreachBehavior set to increase the maximum.
  link: [cannot increase capacity higher than its maximum capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-max-capacity-breach)
  link: [does not automatically decrease back](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-max-capacity-breach)
aws-auto-scaling-aas-predictive-min-24-hours
  claim: Application Auto Scaling predictive scaling needs at least 24 hours of historical metric data to start forecasting, and forecasts are more effective when the history spans two full weeks.
  scope: per Application Auto Scaling predictive scaling policy; minimum; not adjustable.
  link: [at least 24 hours of historical data](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-min-24-hours)
  link: [two full weeks](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-min-24-hours)
aws-auto-scaling-aas-predictive-no-scale-in
  claim: Application Auto Scaling predictive scaling does not scale in when the forecast expects less load; to remove capacity that is no longer needed, you must also create a target tracking or step scaling policy.
  scope: per Application Auto Scaling predictive scaling policy in forecast and scale mode; forecast expects a decrease in load.
  link: [predictive scaling will not scale in](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-no-scale-in)
  link: [create a Target Tracking or Step Scaling policy](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-predictive-no-scale-in)
aws-auto-scaling-aas-scalable-dimension-examples
  claim: Examples of scalable dimensions: an ECS service scales its task count, a DynamoDB table scales its read and write capacity (and that of its global secondary indexes), and an Aurora cluster scales its replica count.
  scope: per Application Auto Scaling scalable target.
  link: [auto scaling of its task count](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-dimension-examples)
  link: [the read and write capacity of the table](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-dimension-examples)
  link: [scaling of its replica count](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-dimension-examples)
aws-auto-scaling-aas-scalable-target-identity
  claim: In Application Auto Scaling, a scalable target is the resource you want to scale, identified by a service namespace, a resource ID and a scalable dimension.
  scope: per Application Auto Scaling scalable target.
  link: [service namespace, resource ID, and scalable dimension](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-target-identity)
  link: [specify the resource that you want to scale](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scalable-target-identity)
aws-auto-scaling-aas-scaling-out-in-limits
  claim: With scaling policies set, Application Auto Scaling cannot scale a scalable target in below its minimum capacity or out above its maximum capacity.
  scope: per Application Auto Scaling scalable target.
  link: [lower than its minimum capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scaling-out-in-limits)
  link: [higher than its maximum capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scaling-out-in-limits)
aws-auto-scaling-aas-scheduled-modifies-min-max
  claim: Application Auto Scaling scheduled actions work by changing the scalable target's minimum and maximum capacity at a specific date and time.
  scope: per Application Auto Scaling scalable target.
  link: [modifying the minimum and maximum capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-scheduled-modifies-min-max)
aws-auto-scaling-change-aas-memcached-2025
  claim: Since April 10, 2025 Application Auto Scaling can horizontally scale the number of nodes of an ElastiCache Memcached cluster.
  scope: per ElastiCache Memcached cluster.
  link: [April 10, 2025](../facts/aws-auto-scaling.md#aws-auto-scaling-change-aas-memcached-2025)
  link: [horizontally scale the number of nodes](../facts/aws-auto-scaling.md#aws-auto-scaling-change-aas-memcached-2025)
aws-auto-scaling-change-aas-metric-math-2023
  claim: Since March 14, 2023 Application Auto Scaling target tracking policies can use CloudWatch metric math to combine several metrics into a new time series.
  scope: per Application Auto Scaling target tracking policy.
  link: [March 14, 2023](../facts/aws-auto-scaling.md#aws-auto-scaling-change-aas-metric-math-2023)
  link: [use metric math](../facts/aws-auto-scaling.md#aws-auto-scaling-change-aas-metric-math-2023)
aws-auto-scaling-change-aas-predictive-guide-2024
  claim: On November 21, 2024 the Application Auto Scaling User Guide added a new topic on getting started with predictive scaling in Application Auto Scaling.
  scope: Application Auto Scaling User Guide.
  link: [November 21, 2024](../facts/aws-auto-scaling.md#aws-auto-scaling-change-aas-predictive-guide-2024)
  link: [get started using predictive scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-change-aas-predictive-guide-2024)
aws-auto-scaling-change-scaling-plan-migration-2024
  claim: On April 5, 2024 AWS added guidance to migrate from AWS Auto Scaling scaling plans to Amazon EC2 Auto Scaling predictive scaling, which offers more functionality; the migration moves a plan to EC2 Auto Scaling and Application Auto Scaling scaling policies.
  scope: AWS Auto Scaling scaling plans.
  link: [April 5, 2024](../facts/aws-auto-scaling.md#aws-auto-scaling-change-scaling-plan-migration-2024)
  link: [migrate from AWS Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-change-scaling-plan-migration-2024)
aws-auto-scaling-faq-application-auto-scaling-for-non-ec2
  claim: To scale a resource other than EC2, use the Application Auto Scaling API, which defines scaling policies or scheduled one-time or recurring actions for resources such as ECS services, EC2 Spot fleets, EMR clusters, AppStream 2.0 fleets, DynamoDB provisioned capacity, Aurora Replicas and SageMaker endpoint variants.
  scope: Application Auto Scaling (resources other than EC2).
  link: [you can use the Application Auto Scaling API](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2)
  link: [Amazon ECS services, Amazon EC2 Spot fleets](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2)
  link: [provisioned read and write capacity for Amazon DynamoDB](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2)
aws-auto-scaling-faq-creates-target-tracking-only
  claim: AWS Auto Scaling creates target tracking scaling policies only; for step scaling policies or scheduled scaling, use the individual service consoles or APIs.
  scope: per scaling plan.
  link: [target tracking scaling policies only](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-creates-target-tracking-only)
  link: [step scaling policies or scheduled scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-creates-target-tracking-only)
aws-auto-scaling-faq-definition
  claim: AWS Auto Scaling scales collections of related resources that support one application and configures consistent scaling policies across the full infrastructure stack behind it.
  scope: AWS Auto Scaling (service definition).
  link: [across the full infrastructure stack](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-definition)
  link: [scale collections of related resources](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-definition)
aws-auto-scaling-faq-discovery-scans-stack-or-tags
  claim: AWS Auto Scaling scans the selected CloudFormation stack, or the resources with the specified tags, to identify the supported resource types that can be scaled; ECS services cannot currently be discovered using tags.
  scope: per scaling plan; the tag limitation is stated as current ('currently').
  link: [scan your selected AWS CloudFormation stack](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-discovery-scans-stack-or-tags)
  link: [ECS services cannot be discovered using tags](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-discovery-scans-stack-or-tags)
  say: it scans your stack or your tagged resources | ECS services are not found by tags
aws-auto-scaling-faq-faster-than-per-service-consoles
  claim: Configuring scaling policies for all scalable resources of an application with AWS Auto Scaling is faster than managing each resource's policies in its own service console, and easier because AWS Auto Scaling includes predefined scaling strategies.
  scope: per application (scaling plan).
  link: [predefined scaling strategies](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-faster-than-per-service-consoles)
  say: it is faster and has predefined strategies
aws-auto-scaling-faq-free-cloudwatch-fees-apply
  claim: AWS Auto Scaling is free to use; because it is enabled by Amazon CloudWatch, service fees apply for CloudWatch and for your application resources, such as EC2 instances and Elastic Load Balancing load balancers.
  scope: per account; fixed.
  link: [free to use](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-free-cloudwatch-fees-apply)
  say: free to use
aws-auto-scaling-faq-plan-creates-target-tracking-per-resource
  claim: For each resource in a scaling plan, AWS Auto Scaling creates a target tracking scaling policy with the most popular metric for that resource type and automatically sets the resource's min and max values.
  scope: per resource in a scaling plan.
  link: [creates a target tracking scaling policy](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-plan-creates-target-tracking-per-resource)
  link: [automatically sets the min/max values](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-plan-creates-target-tracking-per-resource)
aws-auto-scaling-faq-plan-dynamic-or-predictive-alone
  claim: A scaling plan can use only Dynamic Scaling and opt out of Predictive Scaling, or enable only Predictive Scaling without Dynamic Scaling.
  scope: per scaling plan.
  link: [only Dynamic Scaling and opt-out of Predictive Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-plan-dynamic-or-predictive-alone)
  link: [just Predictive Scaling without configuring Dynamic Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-plan-dynamic-or-predictive-alone)
aws-auto-scaling-faq-predictive-and-target-tracking-together
  claim: In AWS Auto Scaling, Predictive Scaling and target tracking are configured together by a user to generate a scaling plan.
  scope: per scaling plan.
  link: [configured together by a user](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-and-target-tracking-together)
  say: you configure them together in one scaling plan
aws-auto-scaling-faq-predictive-buffer-time
  claim: Predictive Scaling can be given a buffer time so instances are provisioned some time before a predicted traffic change, which helps instances that need warm-up time before they can serve traffic.
  scope: per AWS Auto Scaling scaling plan.
  link: [configure buffer time to provision instances](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-buffer-time)
aws-auto-scaling-faq-predictive-ec2-only-in-plans
  claim: In an AWS Auto Scaling scaling plan, Predictive Scaling only generates schedules for EC2 instances.
  scope: per scaling plan.
  link: [only generates schedules for EC2 instances](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-ec2-only-in-plans)
aws-auto-scaling-faq-predictive-forecast-horizon
  claim: Every 24 hours, Predictive Scaling forecasts traffic 48 hours into the future and schedules capacity changes for those 48 hours.
  scope: per scaling plan; fixed.
  link: [Every 24 hours](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-forecast-horizon)
  link: [48 hours into the future](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-forecast-horizon)
  say: every twenty-four hours | forty-eight hours ahead
aws-auto-scaling-faq-predictive-free
  claim: Predictive Scaling is free to use; you pay for the resources that run your application.
  scope: per account; fixed.
  link: [free to use](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-free)
  say: free to use
aws-auto-scaling-faq-predictive-history-needed
  claim: Predictive Scaling needs up to two weeks of historical data, but it can generate a schedule with as little as a day's worth of data.
  scope: per scaling plan; minimum; not adjustable; a schedule can be generated after a day; the forecast uses up to two weeks.
  link: [up to two weeks of historical data](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-history-needed)
  link: [as little as a day's worth of data](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-history-needed)
  say: up to two weeks of history | as little as a single day of data
aws-auto-scaling-faq-predictive-min-dynamic-utilization
  claim: In a scaling plan, Predictive Scaling schedules future scaling actions that configure minimum capacity, and Dynamic Scaling uses the resource utilization metric and its target value to change EC2 capacity over time as traffic varies.
  scope: per scaling plan.
  link: [schedules future scaling actions to configure minimum capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-min-dynamic-utilization)
  say: predictive sets the minimum; dynamic follows the utilization target
aws-auto-scaling-faq-predictive-provisions-in-advance
  claim: By predicting traffic changes, Predictive Scaling provisions EC2 instances in advance of changing traffic, which makes Auto Scaling faster and more accurate.
  scope: per scaling plan.
  link: [in advance of changing traffic](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-provisions-in-advance)
  say: before the traffic changes
aws-auto-scaling-faq-predictive-scaling-definition
  claim: Predictive Scaling looks at historic traffic patterns and forecasts them into the future to schedule changes in the number of EC2 instances; it uses machine learning models to forecast daily and weekly patterns.
  scope: per AWS Auto Scaling scaling plan.
  link: [uses machine learning models](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-scaling-definition)
  link: [schedule changes in the number of EC2 instances](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-scaling-definition)
aws-auto-scaling-faq-predictive-sets-minimum-target-tracking-actual
  claim: In a scaling plan, Predictive Scaling sets the minimum capacity from forecasted traffic, while target tracking changes the actual capacity based on the actual traffic at the moment; the two are configured together.
  scope: per scaling plan.
  link: [sets up the minimum capacity for your application](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-sets-minimum-target-tracking-actual)
  link: [target tracking changes the actual capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-sets-minimum-target-tracking-actual)
aws-auto-scaling-faq-recommendations-and-guardrails
  claim: AWS Auto Scaling bases its scaling recommendations on the most popular scaling metrics and thresholds, and recommends minimum and maximum sizes as safe guardrails.
  scope: per AWS Auto Scaling scaling plan.
  link: [most popular scaling metrics and thresholds](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-recommendations-and-guardrails)
  link: [recommends safe guardrails for scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-recommendations-and-guardrails)
aws-auto-scaling-faq-scalable-resource-list
  claim: Through one unified interface, AWS Auto Scaling can scale EC2 Auto Scaling groups, ECS services, EC2 Spot Fleets, DynamoDB throughput capacity and Aurora replicas.
  scope: per scaling plan.
  link: [Amazon EC2 Auto Scaling groups](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scalable-resource-list)
  link: [Amazon DynamoDB throughput capacity](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scalable-resource-list)
  link: [Aurora replicas for Amazon Aurora](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scalable-resource-list)
aws-auto-scaling-faq-scaling-plan-definition
  claim: A scaling plan is a collection of scaling instructions for multiple AWS resources; its key parameters are a resource utilization metric with a target value and an incoming traffic metric that Predictive Scaling uses for forecasts.
  scope: per AWS Auto Scaling scaling plan.
  link: [collection of scaling instructions for multiple AWS resources](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scaling-plan-definition)
  link: [resource utilization metric and the incoming traffic metric](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-scaling-plan-definition)
aws-auto-scaling-faq-target-tracking-handles-unpredicted-spikes
  claim: Used with Predictive Scaling, target tracking tracks the desired capacity utilization levels as traffic varies and addresses unpredicted traffic spikes and other fluctuations.
  scope: per scaling plan; target tracking used in conjunction with Predictive Scaling.
  link: [addresses unpredicted traffic spikes and other fluctuations](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-target-tracking-handles-unpredicted-spikes)
  say: target tracking handles the surprises
aws-auto-scaling-faq-three-scaling-strategies
  claim: A scaling plan sets target values from three predefined scaling recommendations (optimize availability, optimize costs, or balance the two), or from target values you define yourself.
  scope: per scaling plan.
  link: [optimize availability, optimize costs, or balance the two](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-three-scaling-strategies)
  say: optimize availability, optimize costs, or balance the two
aws-auto-scaling-faq-when-to-use
  claim: Use AWS Auto Scaling for an application that uses one or more scalable resources and experiences variable load, for example a three-tier web application with EC2 Auto Scaling groups and DynamoDB tables scaled together.
  scope: choice of AWS Auto Scaling for an application.
  link: [experiences variable load](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-when-to-use)
aws-auto-scaling-plans-detailed-monitoring-best-practice
  claim: EC2 instances use basic monitoring by default, with metric data at five-minute intervals; for an additional charge, detailed monitoring gives one-minute data, which AWS recommends for scaling because stale five-minute data slows the response.
  scope: per EC2 instance.
  link: [five-minute intervals](../facts/aws-auto-scaling.md#aws-auto-scaling-plans-detailed-monitoring-best-practice)
  link: [For an additional charge](../facts/aws-auto-scaling.md#aws-auto-scaling-plans-detailed-monitoring-best-practice)
aws-auto-scaling-plans-one-plan-per-resource
  claim: A scaling plan can contain resources from multiple services, but each resource can be in only one scaling plan at a time.
  scope: per scalable resource.
  link: [only one scaling plan at a time](../facts/aws-auto-scaling.md#aws-auto-scaling-plans-one-plan-per-resource)
aws-auto-scaling-plans-prefer-native-predictive-policies
  claim: If you use AWS Auto Scaling scaling plans only for predictive scaling, AWS strongly recommends setting predictive scaling policies directly on the Auto Scaling resources instead, because that option has more features.
  scope: per AWS Auto Scaling scaling plan; scaling plan used only for predictive scaling.
  link: [directly on your Auto Scaling resources instead](../facts/aws-auto-scaling.md#aws-auto-scaling-plans-prefer-native-predictive-policies)
aws-auto-scaling-pricing-page-no-additional-charge
  claim: AWS Auto Scaling has no additional charge; you pay only for the AWS resources that run your applications and the Amazon CloudWatch monitoring fees.
  scope: per account.
  link: [no additional charge](../facts/aws-auto-scaling.md#aws-auto-scaling-pricing-page-no-additional-charge)
  say: no additional charge
aws-auto-scaling-quota-scalable-resources-per-scaling-plan-type
  claim: Scaling plans can manage by default 3,000 scalable resources for Amazon DynamoDB, 200 Auto Scaling groups for Amazon EC2 Auto Scaling and 500 scalable resources of any other type; the quota is adjustable.
  scope: per resource type, per Region, per account; default; adjustable.
  link: [3,000 scalable resources](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scalable-resources-per-scaling-plan-type)
  link: [200 Auto Scaling groups](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scalable-resources-per-scaling-plan-type)
  link: [500 scalable resources](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scalable-resources-per-scaling-plan-type)
  say: three thousand scalable resources | two hundred Auto Scaling groups | five hundred scalable resources
aws-auto-scaling-quota-scalable-targets-per-resource-type
  claim: Application Auto Scaling allows by default 5,000 scalable targets for Amazon DynamoDB, 3,000 scalable targets for Amazon ECS, 1,500 scalable targets for Amazon Keyspaces and 500 scalable targets for other resource types; the quota is adjustable.
  scope: per resource type, per Region, per account; default; adjustable.
  link: [5,000 scalable targets](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scalable-targets-per-resource-type)
  link: [3,000 scalable targets](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scalable-targets-per-resource-type)
  link: [500 scalable targets](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scalable-targets-per-resource-type)
  say: five thousand scalable targets | three thousand scalable targets | five hundred scalable targets
aws-auto-scaling-quota-scaling-instructions-per-plan
  claim: A scaling plan can have 500 scaling instructions; the quota is not adjustable.
  scope: per scaling plan; maximum; not adjustable.
  link: [500 scaling instructions](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scaling-instructions-per-plan)
  say: five hundred scaling instructions
aws-auto-scaling-quota-scaling-plans-per-account
  claim: An account can have 100 scaling plans by default; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [100 scaling plans](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scaling-plans-per-account)
  say: one hundred scaling plans
aws-auto-scaling-quota-scaling-policies-per-scalable-target
  claim: A scalable target in Application Auto Scaling can have 50 scaling policies, counting step scaling and target tracking policies together; the quota is not adjustable.
  scope: per scalable target; maximum; not adjustable.
  link: [50 scaling policies](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scaling-policies-per-scalable-target)
  say: fifty scaling policies
aws-auto-scaling-quota-scheduled-actions-per-scalable-target
  claim: Application Auto Scaling allows 200 scheduled actions for each scalable target, with no quota increase possible.
  scope: per scalable target; maximum; not adjustable.
  link: [200 scheduled actions](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-scheduled-actions-per-scalable-target)
  say: two hundred scheduled actions
aws-auto-scaling-quota-step-adjustments-per-policy
  claim: Each Application Auto Scaling step scaling policy starts with a default of 20 step adjustments, which you can raise.
  scope: per step scaling policy; default; adjustable.
  link: [20 step adjustments](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-step-adjustments-per-policy)
  say: twenty step adjustments
aws-auto-scaling-quota-target-tracking-configurations-per-instruction
  claim: Each scaling instruction holds at most 10 target tracking configurations, a fixed limit of scaling plans.
  scope: per scaling instruction; maximum; not adjustable.
  link: [10 target tracking configurations](../facts/aws-auto-scaling.md#aws-auto-scaling-quota-target-tracking-configurations-per-instruction)
  say: ten target tracking configurations
aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services
  claim: Well-Architected rule of thumb: use Amazon EC2 Auto Scaling for EC2 instances and Application Auto Scaling for other AWS services, such as AWS Lambda functions or Amazon ECS services.
  scope: AWS Well-Architected guidance.
  link: [use Amazon EC2 Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services)
  link: [For other AWS services, use Application Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services)
aws-auto-scaling-wa-free-managed-service
  claim: AWS Auto Scaling is a fully managed and free service to scale application capacity; it integrates with EC2 instances and Spot Fleets, Amazon ECS, Amazon DynamoDB and Amazon Aurora.
  scope: AWS Well-Architected guidance.
  link: [fully managed and free service](../facts/aws-auto-scaling.md#aws-auto-scaling-wa-free-managed-service)
ec2-auto-scaling-add-az-group-and-load-balancer
  claim: To expand to another Availability Zone you add that zone to the Auto Scaling group and also enable the zone for the load balancer (if it supports it).
  scope: per Auto Scaling group across Availability Zones.
  link: [adding an Availability Zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-add-az-group-and-load-balancer)
  link: [enabling that Availability Zone for your load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-add-az-group-and-load-balancer)
ec2-auto-scaling-administrative-suspension
  claim: EC2 Auto Scaling can itself suspend processes (an administrative suspension), most commonly for groups that have tried to launch instances for over 24 hours without launching any; you can resume them.
  scope: per Auto Scaling group (scaling processes).
  link: [over 24 hours](../facts/ec2-auto-scaling.md#ec2-auto-scaling-administrative-suspension)
  link: [administrative suspension](../facts/ec2-auto-scaling.md#ec2-auto-scaling-administrative-suspension)
ec2-auto-scaling-alb-minimum-two-azs
  claim: An Application Load Balancer must have at least two Availability Zones enabled.
  scope: per Application Load Balancer; minimum.
  link: [at least two Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-alb-minimum-two-azs)
ec2-auto-scaling-attach-criteria
  claim: To attach an existing instance to a group it must be running, its AMI must still exist, it must not belong to another Auto Scaling group, and it must be in one of the group's Availability Zones.
  scope: per instance attached to an Auto Scaling group.
  link: [not a member of another Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-attach-criteria)
  link: [launched into one of the Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-attach-criteria)
ec2-auto-scaling-attach-raises-desired
  claim: Attaching instances raises the group's desired capacity by that number; the request fails if the new desired capacity would exceed the group's maximum size.
  scope: per Auto Scaling group (attach instances).
  link: [desired capacity of the group increases](../facts/ec2-auto-scaling.md#ec2-auto-scaling-attach-raises-desired)
  link: [the request to attach more instances fails](../facts/ec2-auto-scaling.md#ec2-auto-scaling-attach-raises-desired)
ec2-auto-scaling-attached-treated-same
  claim: EC2 Auto Scaling treats attached instances like instances it launched itself, so an attached instance can be terminated during scale in if it is selected.
  scope: per attached instance.
  link: [treats attached instances the same](../facts/ec2-auto-scaling.md#ec2-auto-scaling-attached-treated-same)
  link: [can be terminated during scale-in events](../facts/ec2-auto-scaling.md#ec2-auto-scaling-attached-treated-same)
ec2-auto-scaling-aws-managed-key-no-extra-authorization
  claim: EC2 Auto Scaling needs no additional authorization to use the default AWS managed key for encrypted volumes.
  scope: per account (KMS keys); default AWS managed key.
  link: [does not need additional authorization](../facts/ec2-auto-scaling.md#ec2-auto-scaling-aws-managed-key-no-extra-authorization)
ec2-auto-scaling-az-distribution-balanced-only
  claim: With the balanced only Availability Zone distribution, the group keeps trying to launch in the zone where launches fail instead of moving to another zone; it suits quorum-based workloads and groups that can tolerate losing a zone.
  scope: per Auto Scaling group across Availability Zones.
  link: [continue to attempt to launch instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-distribution-balanced-only)
  link: [quorum-based workloads](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-distribution-balanced-only)
ec2-auto-scaling-az-distribution-reservations-then-balanced
  claim: Since June 30, 2026, the reservations then balanced strategy launches instances into the group's Capacity Reservations first and spreads only the remaining capacity evenly across the enabled Availability Zones.
  scope: per Auto Scaling group across Availability Zones.
  link: [Reservations then balanced](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-distribution-reservations-then-balanced)
  link: [June 30, 2026](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-distribution-reservations-then-balanced)
ec2-auto-scaling-az-recovery-rebalance
  claim: When an unhealthy or unavailable Availability Zone recovers, EC2 Auto Scaling rebalances the group by launching in the zones with the fewest instances and terminating instances elsewhere.
  scope: per Auto Scaling group across Availability Zones.
  link: [automatically rebalances the Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-recovery-rebalance)
  link: [the enabled Availability Zones with the fewest instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-recovery-rebalance)
ec2-auto-scaling-az-strategy-balanced-best-effort
  claim: With the balanced best effort AZ strategy, EC2 Auto Scaling keeps equal counts across zones but, if launches fail in one zone, launches into another healthy zone instead.
  scope: per Auto Scaling group across Availability Zones.
  link: [Balanced best effort](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-strategy-balanced-best-effort)
  link: [in another healthy Availability Zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-strategy-balanced-best-effort)
ec2-auto-scaling-az-unavailable-launch-elsewhere
  claim: If one Availability Zone becomes unavailable, EC2 Auto Scaling can launch instances in another zone of the group to compensate.
  scope: per Auto Scaling group across Availability Zones.
  link: [launch instances in another one to compensate](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-unavailable-launch-elsewhere)
  link: [If one Availability Zone becomes unavailable](../facts/ec2-auto-scaling.md#ec2-auto-scaling-az-unavailable-launch-elsewhere)
ec2-auto-scaling-billed-from-launch
  claim: You are billed for Auto Scaling instances as soon as they launch, including the time before they are in service.
  scope: per instance in an Auto Scaling group.
  link: [as soon as they are launched](../facts/ec2-auto-scaling.md#ec2-auto-scaling-billed-from-launch)
  link: [not yet in service](../facts/ec2-auto-scaling.md#ec2-auto-scaling-billed-from-launch)
ec2-auto-scaling-cannot-hibernate-group-instance
  claim: You cannot hibernate an instance that is in an Auto Scaling group: if you try, Auto Scaling marks the stopped instance unhealthy and might terminate it and launch a replacement.
  scope: per instance in an Auto Scaling group.
  link: [You can't hibernate an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance)
  link: [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance)
ec2-auto-scaling-capacity-rebalancing-exceeds-max-10-percent
  claim: During Capacity Rebalancing, Amazon EC2 Auto Scaling can temporarily exceed the group's maximum size by up to 10 percent of the desired capacity.
  scope: per Auto Scaling group with Capacity Rebalancing; maximum; not adjustable.
  link: [up to 10 percent of the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-rebalancing-exceeds-max-10-percent)
  say: up to ten percent of the desired capacity
ec2-auto-scaling-capacity-rebalancing-hook-under-two-minutes
  claim: A custom lifecycle hook action for Capacity Rebalancing should finish in under two minutes so tasks complete before termination.
  scope: per Auto Scaling group with Capacity Rebalancing.
  link: [finish in under two minutes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-rebalancing-hook-under-two-minutes)
  say: finish in under two minutes
ec2-auto-scaling-capacity-rebalancing-spot
  claim: Capacity Rebalancing, for groups with Spot Instances, makes EC2 Auto Scaling try to launch a new Spot Instance when EC2 reports elevated interruption risk, and terminate the old one after the new one launches.
  scope: per Auto Scaling group with Spot Instances.
  link: [at an elevated risk of interruption](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-rebalancing-spot)
  link: [then terminates an earlier instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-rebalancing-spot)
ec2-auto-scaling-capacity-reservation-az-balance-by-default
  claim: By default, Auto Scaling puts Availability Zone balance first when it consumes Capacity Reservations; with On-Demand fallback, instances launch as On-Demand in a zone without reserved capacity to keep the balance.
  scope: per Auto Scaling group that consumes Capacity Reservations; default; adjustable; On-Demand fallback enabled for the On-Demand part of the claim.
  link: [prioritizes Availability Zone balance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-az-balance-by-default)
  link: [instances launch as On-Demand to maintain the balance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-az-balance-by-default)
ec2-auto-scaling-capacity-reservation-none-and-default
  claim: With the Capacity Reservation preference none, Auto Scaling does not launch instances into a Capacity Reservation and instances run as On-Demand capacity; with default, it uses the Capacity Reservation specification from the launch template, unless the group uses distribution segments, in which case it consumes reservations in the priority order of the segments.
  scope: per Auto Scaling group.
  link: [Instances run as On-Demand capacity.](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-none-and-default)
  link: [uses the Capacity Reservation specification](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-none-and-default)
ec2-auto-scaling-capacity-reservation-preference-values
  claim: The group's Capacity Reservation preference decides how reserved capacity is used: with capacity-reservations-only, instances fail to launch when no reserved capacity is available; with capacity-reservations-first, they launch as On-Demand instead.
  scope: per Auto Scaling group; no reserved capacity is available.
  link: [instances fail to launch](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-preference-values)
  link: [instances launch as On-Demand](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-preference-values)
ec2-auto-scaling-capacity-reservation-single-target
  claim: An Auto Scaling group's Capacity Reservation target can name only a single Capacity Reservation ID or a single Capacity Reservation Resource Group ARN.
  scope: per Auto Scaling group Capacity Reservation target.
  link: [Only a single Capacity Reservation ID](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-single-target)
ec2-auto-scaling-capacity-reservation-types-supported
  claim: A Capacity Reservation reserves EC2 compute capacity in a specific Availability Zone so that it is available when the Auto Scaling group needs to launch instances; when a Capacity Block expires, Amazon EC2 terminates the instances running in it.
  scope: per Availability Zone.
  link: [in a specific Availability Zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-types-supported)
  link: [Amazon EC2 terminates the instances running in it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-capacity-reservation-types-supported)
ec2-auto-scaling-case-canva-46-percent-purchase-mix
  claim: Canva reduced compute costs by 46 percent with a combination of purchase options; for example, projects of free-plan users run on Spot Instances.
  scope: customer case study.
  link: [reduced compute costs by 46 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-canva-46-percent-purchase-mix)
  link: [run on Spot Instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-canva-46-percent-purchase-mix)
ec2-auto-scaling-case-canva-ecs-spot-capacity-provider
  claim: Canva runs its video and streaming functions as containerized workloads on Amazon ECS that use ECS cluster auto scaling, which manages the scaling of the EC2 instances registered to the cluster, with a dedicated capacity provider on EC2 Spot Instances.
  scope: customer case study.
  link: [Amazon ECS cluster auto scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-canva-ecs-spot-capacity-provider)
  link: [runs on Amazon EC2 Spot Instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-canva-ecs-spot-capacity-provider)
ec2-auto-scaling-case-nasa-jpl-spot-fleets
  claim: NASA JPL processes about 4.4 TB of downlinked satellite data a day into up to 70 TB of data products on automatic scaling fleets: Spot Instances for the fault-tolerant processing and On-Demand with Capacity Reservations for critical processing.
  scope: customer case study.
  link: [up to 70 TB of final data products](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-nasa-jpl-spot-fleets)
  link: [automatic scaling fleets](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-nasa-jpl-spot-fleets)
ec2-auto-scaling-change-az-distribution-2024
  claim: Since November 7, 2024 you can choose an Availability Zone distribution strategy for an Auto Scaling group.
  scope: per Auto Scaling group.
  link: [November 7, 2024](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-az-distribution-2024)
  link: [choose an Availability Zone distribution](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-az-distribution-2024)
ec2-auto-scaling-change-batch-termination-2026
  claim: The TerminateInstanceInAutoScalingGroup API now accepts up to 100 instance IDs in one call (batch termination); lifecycle hooks and load balancer connection draining still apply to each instance, at no additional cost.
  scope: per TerminateInstanceInAutoScalingGroup API call; maximum.
  link: [up to 100 instance IDs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-batch-termination-2026)
  link: [no additional cost](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-batch-termination-2026)
ec2-auto-scaling-change-capacity-blocks-2023
  claim: Since October 31, 2023 an Auto Scaling group can launch instances into a Capacity Block for ML, which reserves GPU instances on a future date for short-duration machine learning workloads, by giving the Capacity Block reservation ID in the launch template.
  scope: per launch template.
  link: [October 31, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-capacity-blocks-2023)
  link: [reserve GPU instances on a future date](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-capacity-blocks-2023)
ec2-auto-scaling-change-capacity-reservation-preference-2024
  claim: Since November 20, 2024 an Auto Scaling group can prioritize launching instances into Capacity Reservations through a Capacity Reservation preference set on the group.
  scope: per Auto Scaling group.
  link: [November 20, 2024](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-capacity-reservation-preference-2024)
  link: [prioritize launching instances into Capacity Reservations](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-capacity-reservation-preference-2024)
ec2-auto-scaling-change-instance-maintenance-policy-2023
  claim: Since November 15, 2023 an instance maintenance policy lets you choose whether replacement instances launch before or after existing instances are terminated, for events such as an instance refresh or a health check replacement.
  scope: per Auto Scaling group.
  link: [November 15, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-instance-maintenance-policy-2023)
  link: [launched before or after existing instances are terminated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-instance-maintenance-policy-2023)
ec2-auto-scaling-change-instance-refresh-alarm-rollback-2023
  claim: Since July 31, 2023, an instance refresh can be set to fail and optionally roll back when a chosen CloudWatch alarm goes into the ALARM state.
  scope: per instance refresh.
  link: [July 31, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-instance-refresh-alarm-rollback-2023)
ec2-auto-scaling-change-instance-refresh-cloudformation-2026
  claim: CloudFormation now has an AutoScalingInstanceRefresh update policy: when a stack update changes properties that need instance replacement, CloudFormation starts an instance refresh, and rollback goes through the stack rollback.
  scope: per CloudFormation stack that updates an Auto Scaling group.
  link: [AutoScalingInstanceRefresh update policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-instance-refresh-cloudformation-2026)
  link: [Rollback is handled through CloudFormation stack rollback](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-instance-refresh-cloudformation-2026)
ec2-auto-scaling-change-instance-refresh-rollback-2023
  claim: On February 10, 2023 instance refresh gained rollback of changes from a failed refresh, and the choice to terminate or ignore standby instances and to replace or ignore scale-in protected instances instead of waiting for them.
  scope: per instance refresh.
  link: [February 10, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-instance-refresh-rollback-2023)
  link: [roll back changes from a failed instance refresh](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-instance-refresh-rollback-2023)
ec2-auto-scaling-change-predictive-forecasts-every-six-hours
  claim: Since January 6, 2023, predictive scaling forecasts update every six hours instead of daily.
  scope: per predictive scaling policy.
  link: [update every six hours](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-predictive-forecasts-every-six-hours)
  link: [daily](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-predictive-forecasts-every-six-hours)
  changed: 2023-01-06: was daily
ec2-auto-scaling-change-price-capacity-optimized-2022
  claim: The price-capacity-optimized Spot allocation strategy was added on November 10, 2022; it requests Spot Instances from the pools least likely to be interrupted that also have the lowest possible price, and AWS now recommends it when you are getting started.
  scope: per Auto Scaling group with Spot Instances.
  link: [November 10, 2022](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-price-capacity-optimized-2022)
  link: [price and capacity optimized allocation strategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-price-capacity-optimized-2022)
ec2-auto-scaling-change-ssm-parameter-ami-2023
  claim: Since January 19, 2023 a launch template for an Auto Scaling group can name a Systems Manager parameter instead of an AMI ID, so the group can use new AMI IDs without new launch templates or versions.
  scope: per launch template used by an Auto Scaling group.
  link: [January 19, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-ssm-parameter-ami-2023)
  link: [Systems Manager parameter instead of an AMI ID](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-ssm-parameter-ami-2023)
ec2-auto-scaling-change-target-tracking-metric-math-2022
  claim: Since December 8, 2022, a target tracking scaling policy can use CloudWatch metric math to combine several metrics into one scaling metric.
  scope: per target tracking scaling policy.
  link: [December 8, 2022](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-target-tracking-metric-math-2022)
  link: [use metric math](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-target-tracking-metric-math-2022)
ec2-auto-scaling-change-warm-pool-mixed-instances-2025
  claim: Since November 4, 2025 you can add a warm pool to an Auto Scaling group that has a mixed instances policy, when the policy is configured for On-Demand Instances only and the group does not use instance weighting (warm pools support neither Spot Instances in mixed instance groups nor weighted mixed instance groups).
  scope: per Auto Scaling group with a mixed instances policy; the mixed instances policy is On-Demand only and the group does not use instance weighting.
  link: [Nov 4, 2025](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-warm-pool-mixed-instances-2025)
  link: [add warm pools to Auto Scaling groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-warm-pool-mixed-instances-2025)
  link: [configured for On-Demand instances only](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-warm-pool-mixed-instances-2025)
  link: [you can’t add a warm pool](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-warm-pool-mixed-instances-2025)
ec2-auto-scaling-combine-policy-types-predictive-plus-dynamic
  claim: A group can use several policy types together: dynamic scaling policies can be combined, and predictive scaling (proactive) can be combined with dynamic scaling (reactive) to add instances ahead of daily and weekly patterns.
  scope: per Auto Scaling group.
  link: [multiple policy types (or a combination of them)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-combine-policy-types-predictive-plus-dynamic)
  link: [combine predictive scaling and dynamic scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-combine-policy-types-predictive-plus-dynamic)
ec2-auto-scaling-console-desired-above-max-raises-max
  claim: In the console, a desired capacity above the maximum automatically raises the maximum to the new desired capacity.
  scope: per Auto Scaling group, edited in the console.
  link: [automatically increased to the new desired capacity value](../facts/ec2-auto-scaling.md#ec2-auto-scaling-console-desired-above-max-raises-max)
  say: raised to the new desired capacity
ec2-auto-scaling-control-plane-outage-no-effect
  claim: A control plane outage of the EC2 Auto Scaling service APIs does not affect the scaling of existing Auto Scaling groups.
  scope: per existing Auto Scaling group.
  link: [will not affect the scaling of existing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-control-plane-outage-no-effect)
ec2-auto-scaling-cooldown-applies-to-simple-scaling
  claim: After a group launches or terminates instances, further scaling activities started by simple scaling policies wait for the cooldown period to end.
  scope: per simple scaling policy.
  link: [scaling activities initiated by simple scaling policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-applies-to-simple-scaling)
  say: scaling activities started by simple scaling policies
ec2-auto-scaling-cooldown-elb-deregistration-300-seconds
  claim: By default, Elastic Load Balancing waits 300 seconds to complete deregistration (connection draining).
  scope: per load balancer deregistration; default; adjustable.
  link: [300 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-elb-deregistration-300-seconds)
  say: three hundred seconds
ec2-auto-scaling-cooldown-manual-scaling-default-no-wait
  claim: Manual scaling does not wait for a cooldown by default; with the AWS CLI or an SDK you can choose to honor the default cooldown.
  scope: per manual scaling action; default; adjustable.
  link: [the default is not to wait](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-manual-scaling-default-no-wait)
  say: the default is not to wait
ec2-auto-scaling-cooldown-not-settable-at-console-create
  claim: In the Amazon EC2 Auto Scaling console, you cannot set the default cooldown when you first create a group; you can update it after the group exists.
  scope: per Auto Scaling group (scaling cooldown).
  link: [can't set the default cooldown](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-not-settable-at-console-create)
  say: can't set the default cooldown
ec2-auto-scaling-cooldown-policy-specific-overrides-default
  claim: Simple scaling policies use the group's default cooldown unless a cooldown is set on the policy, which then overrides the default cooldown.
  scope: per Auto Scaling group (scaling cooldown).
  link: [it overrides the default cooldown](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-policy-specific-overrides-default)
  say: it overrides the default cooldown
ec2-auto-scaling-cooldown-scale-in-starts-at-draining
  claim: With Elastic Load Balancing, for scale in, the cooldown period starts when the instance selected for termination starts connection draining; it does not wait for draining or a lifecycle hook to finish.
  scope: per Auto Scaling group (scaling cooldown).
  link: [starts connection draining (deregistration delay)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-scale-in-starts-at-draining)
  say: starts connection draining
ec2-auto-scaling-cooldown-scheduled-action-does-not-wait
  claim: A scheduled action can start a scaling activity at its scheduled time without waiting for the cooldown period to end.
  scope: per Auto Scaling group (scaling cooldown).
  link: [initiate a scaling activity immediately](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-scheduled-action-does-not-wait)
  say: start a scaling activity immediately
ec2-auto-scaling-cooldown-starts-after-last-instance
  claim: When several instances launch or terminate, the cooldown period starts when the last instance finishes launching or terminating.
  scope: per Auto Scaling group (scaling cooldown).
  link: [when the last instance finishes launching or terminating](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-starts-after-last-instance)
  say: when the last instance finishes launching or terminating
ec2-auto-scaling-cooldown-target-tracking-step-do-not-wait
  claim: Target tracking and step scaling policies can start a scale-out immediately without waiting for the cooldown period to end; new instances have a warmup period instead.
  scope: per Auto Scaling group (scaling cooldown).
  link: [without waiting for the cooldown period to end](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-target-tracking-step-do-not-wait)
  say: without waiting for the cooldown to end
ec2-auto-scaling-cooldown-unhealthy-replacement-does-not-wait
  claim: Amazon EC2 Auto Scaling does not wait for the cooldown period to end before it replaces an unhealthy instance.
  scope: per Auto Scaling group (scaling cooldown).
  link: [does not wait for the cooldown period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-unhealthy-replacement-does-not-wait)
  say: does not wait for the cooldown period
ec2-auto-scaling-custom-health-check-immediate-replace
  claim: A custom health check can mark an instance Unhealthy (for example with set-instance-health), which makes EC2 Auto Scaling replace it immediately.
  scope: per Auto Scaling group (health checks).
  link: [mark that particular instance as](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-health-check-immediate-replace)
  link: [immediately replace it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-health-check-immediate-replace)
ec2-auto-scaling-custom-suffix-slr-for-granular-key-access
  claim: To give granular access to one specific customer managed key, AWS says to use a custom suffix service-linked role (for example AWSServiceRoleForAutoScaling_suffix) rather than the default role.
  scope: per account (service-linked role); granular access to a specific customer managed key.
  link: [custom suffix service-linked role](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-suffix-slr-for-granular-key-access)
ec2-auto-scaling-custom-termination-policy-failure-no-termination
  claim: If the custom termination Lambda function errors, times out or returns an empty list, Auto Scaling terminates no instances, except unhealthy ones.
  scope: per Auto Scaling group during scale in.
  link: [doesn't terminate any instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-termination-policy-failure-no-termination)
  link: [returns an empty list](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-termination-policy-failure-no-termination)
ec2-auto-scaling-custom-termination-policy-lambda
  claim: A custom termination policy is a Lambda function that Auto Scaling calls whenever it must select an instance for termination; it terminates only instances that the function returns.
  scope: per Auto Scaling group during scale in.
  link: [custom termination policy using a Lambda function](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-termination-policy-lambda)
  link: [only terminate instances that the function returns](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-termination-policy-lambda)
ec2-auto-scaling-customer-managed-key-needs-launch-template
  claim: A launch configuration cannot specify a customer managed KMS key (KmsKeyId) for EBS encryption; use a launch template to specify it.
  scope: per launch configuration.
  link: [not available when you use a launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-customer-managed-key-needs-launch-template)
  link: [use a launch template instead](../facts/ec2-auto-scaling.md#ec2-auto-scaling-customer-managed-key-needs-launch-template)
ec2-auto-scaling-decision-guide-definition
  claim: The AWS compute decision guide defines EC2 Auto Scaling as the service that maintains application availability and adds or removes EC2 instances automatically using scaling policies you define.
  scope: AWS compute decision guide.
  link: [automatically add or remove EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-decision-guide-definition)
ec2-auto-scaling-decision-guide-horizontal-for-fluctuating
  claim: The AWS compute decision guide calls horizontal scalability (adding instances) essential for dynamic workloads with fluctuating demand.
  scope: AWS compute decision guide.
  link: [essential for dynamic workloads with fluctuating demands](../facts/ec2-auto-scaling.md#ec2-auto-scaling-decision-guide-horizontal-for-fluctuating)
ec2-auto-scaling-decision-guide-pay-for-what-you-use
  claim: The compute decision guide says a service that adjusts its own scale, such as Auto Scaling or serverless, handles spikes and lulls and optimizes cost because you pay only for the resources you use.
  scope: AWS compute decision guide.
  link: [you only pay for the resources you use](../facts/ec2-auto-scaling.md#ec2-auto-scaling-decision-guide-pay-for-what-you-use)
ec2-auto-scaling-default-cooldown-300-seconds
  claim: The default cooldown of an Auto Scaling group is 300 seconds (5 minutes).
  scope: per Auto Scaling group; default; adjustable.
  link: [300 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-cooldown-300-seconds)
  link: [5 minutes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-cooldown-300-seconds)
  say: three hundred seconds | five minutes
ec2-auto-scaling-default-instance-warmup-not-on-by-default
  claim: The default instance warmup is not enabled by default; AWS strongly recommends enabling and configuring it to optimize target tracking and step scaling policies.
  scope: per Auto Scaling group; default; adjustable.
  link: [It is not enabled or configured by default.](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-instance-warmup-not-on-by-default)
  link: [strongly recommend that you enable and configure](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-instance-warmup-not-on-by-default)
ec2-auto-scaling-default-instance-warmup-purpose
  claim: The default instance warmup is how long an instance waits after reaching InService before its usage data counts in the aggregated metrics, so new instances with temporarily high startup usage do not distort dynamic scaling.
  scope: per Auto Scaling group.
  link: [waits before contributing usage data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-instance-warmup-purpose)
ec2-auto-scaling-default-instance-warmup-start-300-seconds
  claim: If you are unsure of the warmup time, AWS suggests starting with 300 seconds and then adjusting it.
  scope: per Auto Scaling group (instance warmup).
  link: [300 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-instance-warmup-start-300-seconds)
  say: three hundred seconds
ec2-auto-scaling-default-no-policies-fixed-size
  claim: By default an Auto Scaling group has no scaling policy or scheduled action, so it keeps a fixed size: it maintains its desired capacity and replaces an instance that becomes unhealthy.
  scope: per Auto Scaling group; default; adjustable.
  link: [maintain a fixed size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-no-policies-fixed-size)
  link: [continues to maintain its desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-no-policies-fixed-size)
ec2-auto-scaling-deregisters-on-scale-in
  claim: On scale in, EC2 Auto Scaling deregisters the terminating instance from the load balancer; new requests go to other targets while existing connections continue until the deregistration delay expires.
  scope: per Auto Scaling group with a load balancer.
  link: [automatically deregisters the terminating instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-deregisters-on-scale-in)
  link: [until the deregistration delay expires](../facts/ec2-auto-scaling.md#ec2-auto-scaling-deregisters-on-scale-in)
ec2-auto-scaling-desired-capacity-maintained
  claim: If you set a desired capacity, EC2 Auto Scaling ensures the group has that many instances; scaling policies then launch or terminate instances as demand changes.
  scope: per Auto Scaling group.
  link: [ensures that your group has this many instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-capacity-maintained)
  link: [as demand on your application increases or decreases](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-capacity-maintained)
ec2-auto-scaling-desired-spread-across-azs
  claim: With several Availability Zones, the desired capacity is distributed across those zones, and EC2 Auto Scaling keeps the balance across all of them when a scaling action occurs.
  scope: per Auto Scaling group across Availability Zones.
  link: [desired capacity is distributed across these Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-spread-across-azs)
  link: [maintains balance across all of the Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-spread-across-azs)
ec2-auto-scaling-desired-within-min-max
  claim: The desired capacity must be equal to or greater than the minimum size and equal to or less than the maximum size of the group.
  scope: per Auto Scaling group.
  link: [within the range of your minimum and maximum](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-within-min-max)
  say: within the minimum and maximum
ec2-auto-scaling-detach-replace-or-decrement
  claim: When you detach instances you can decrement desired capacity by that number; if you do not, EC2 Auto Scaling launches new instances to replace the detached ones.
  scope: per Auto Scaling group (detach instances).
  link: [launches new instances to replace the detached ones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-detach-replace-or-decrement)
  link: [decrement the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-detach-replace-or-decrement)
ec2-auto-scaling-detached-keeps-running
  claim: A detached instance keeps running and keeps incurring charges; it can be managed on its own or attached to a different Auto Scaling group.
  scope: per detached instance.
  link: [continues running and incurring charges](../facts/ec2-auto-scaling.md#ec2-auto-scaling-detached-keeps-running)
  link: [attached to a different Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-detached-keeps-running)
ec2-auto-scaling-dynamic-capacity-kept-within-min-max
  claim: When a dynamic scaling policy calculates a capacity outside the group's minimum and maximum, EC2 Auto Scaling keeps the new capacity within those limits.
  scope: per dynamic scaling policy.
  link: [never goes outside of the minimum and maximum](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-capacity-kept-within-min-max)
ec2-auto-scaling-dynamic-largest-capacity-wins
  claim: When several dynamic scaling policies fire at the same time, EC2 Auto Scaling chooses the policy that gives the largest capacity, for both scale out and scale in.
  scope: per Auto Scaling group with several dynamic scaling policies.
  link: [the policy that provides the largest capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-largest-capacity-wins)
  link: [for both scale out and scale in](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-largest-capacity-wins)
ec2-auto-scaling-dynamic-simple-definition
  claim: Simple scaling increases and decreases the group's current capacity using a single scaling adjustment, with a cooldown period between scaling activities.
  scope: per simple scaling policy.
  link: [Simple scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-simple-definition)
  link: [a single scaling adjustment](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-simple-definition)
  link: [a cooldown period between each scaling activity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-simple-definition)
ec2-auto-scaling-dynamic-step-definition
  claim: Step scaling increases and decreases the group's current capacity using a set of step adjustments that vary with the size of the alarm breach.
  scope: per step scaling policy.
  link: [Step scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-step-definition)
  link: [the size of the alarm breach](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-step-definition)
ec2-auto-scaling-dynamic-target-tracking-definition
  claim: Target tracking scaling increases and decreases the group's current capacity based on a CloudWatch metric and a target value; it works similar to a thermostat: you select a temperature and the thermostat does the rest.
  scope: per target tracking scaling policy.
  link: [Target tracking scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-target-tracking-definition)
  link: [a Amazon CloudWatch metric and a target value](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-target-tracking-definition)
ec2-auto-scaling-dynamic-target-tracking-with-step-caution
  claim: Combining target tracking and step scaling policies needs caution: if a step scaling policy starts a scale-in before the target tracking policy is ready to scale in, the scale-in is not blocked, and after it completes the target tracking policy could instruct the group to scale out again.
  scope: per Auto Scaling group with target tracking and step scaling policies.
  link: [the scale in activity will not be blocked](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-target-tracking-with-step-caution)
  link: [conflicts between these policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-target-tracking-with-step-caution)
ec2-auto-scaling-ec2-metrics-five-minute-default
  claim: Amazon EC2 metrics are published in five-minute intervals by default, and detailed monitoring lowers the interval to one minute.
  scope: per EC2 metric; default; adjustable.
  link: [five-minute intervals](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ec2-metrics-five-minute-default)
  link: [one minute](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ec2-metrics-five-minute-default)
  say: five-minute intervals | one minute
ec2-auto-scaling-ec2-status-checks-always-enabled
  claim: The Amazon EC2 status checks need no special configuration and are always enabled for an Auto Scaling group.
  scope: per Auto Scaling group (health checks).
  link: [always enabled](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ec2-status-checks-always-enabled)
  say: always enabled
ec2-auto-scaling-elastic-ip-not-moved-to-replacement
  claim: When an instance is terminated, its Elastic IP addresses are disassociated and are not automatically associated with the replacement instance.
  scope: per replaced instance.
  link: [not automatically associated with the new instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elastic-ip-not-moved-to-replacement)
  say: not moved to the new instance
ec2-auto-scaling-elb-checks-reroute-and-replace
  claim: When ELB health checks are enabled on the group and an instance fails them, Elastic Load Balancing stops sending it traffic while EC2 Auto Scaling replaces the instance.
  scope: per Auto Scaling group with a load balancer.
  link: [Elastic Load Balancing stops sending traffic to it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace)
  link: [Amazon EC2 Auto Scaling replaces the unhealthy instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace)
ec2-auto-scaling-elb-health-checks-ignored-by-default
  claim: By default, Amazon EC2 Auto Scaling ignores the results of Elastic Load Balancing health checks.
  scope: per Auto Scaling group; default; adjustable.
  link: [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default)
  say: ignores the load balancer health checks
ec2-auto-scaling-eventbridge-near-real-time
  claim: EC2 Auto Scaling events reach EventBridge in near real time, and EventBridge rules can start actions such as an AWS Lambda function while instances launch or terminate.
  scope: per Auto Scaling group (notifications).
  link: [delivered to EventBridge in near real time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-eventbridge-near-real-time)
  link: [invoke an AWS Lambda function](../facts/ec2-auto-scaling.md#ec2-auto-scaling-eventbridge-near-real-time)
ec2-auto-scaling-faq-all-spot-or-all-on-demand
  claim: A group can be configured so that all of its capacity is only Spot Instances, or all of its capacity is only On-Demand Instances and RIs.
  scope: per Auto Scaling group.
  link: [all capacity to be only Spot instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-all-spot-or-all-on-demand)
  link: [only On-Demand instances and RIs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-all-spot-or-all-on-demand)
ec2-auto-scaling-faq-balances-across-azs
  claim: EC2 Auto Scaling always launches new instances so that they are balanced between zones as evenly as possible across the whole fleet, and it only launches into Availability Zones that have available capacity for the requested instance type.
  scope: per Auto Scaling group; the group is configured with multiple Availability Zones.
  link: [balanced between zones as evenly as possible](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-balances-across-azs)
  link: [only launches into Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-balances-across-azs)
ec2-auto-scaling-faq-cannot-scale-past-ec2-limit
  claim: EC2 Auto Scaling cannot scale past the EC2 limit on the number of instances the account can run; to get more, submit an EC2 instance limit request.
  scope: per account.
  link: [cannot scale past the Amazon EC2 limit](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-cannot-scale-past-ec2-limit)
ec2-auto-scaling-faq-cloudwatch-agent-from-ami
  claim: If the AMI contains a CloudWatch agent, the agent is present on the instances the group launches; with the stock Amazon Linux AMI you need to install it yourself.
  scope: per instance launched from the group's AMI.
  link: [If your AMI contains a CloudWatch agent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-cloudwatch-agent-from-ami)
  link: [you need to install it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-cloudwatch-agent-from-ami)
ec2-auto-scaling-faq-cloudwatch-alarms-and-elb
  claim: Amazon CloudWatch can send alarms that trigger scaling activities, and Elastic Load Balancing can distribute traffic to the instances in the Auto Scaling group.
  scope: per EC2 Auto Scaling group.
  link: [send alarms to trigger scaling activities](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-cloudwatch-alarms-and-elb)
  say: CloudWatch alarms trigger scaling
ec2-auto-scaling-faq-codedeploy-cloudformation-for-changes
  claim: To roll out code changes to multiple instances in a group, use AWS CodeDeploy or CloudFormation.
  scope: per Auto Scaling group (code deployment).
  link: [AWS CodeDeploy or CloudFormation](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-codedeploy-cloudformation-for-changes)
ec2-auto-scaling-faq-data-not-copied-to-new-instances
  claim: Data is not automatically copied from existing instances to new instances the group launches; use lifecycle hooks to copy data, or an Amazon RDS database with replicas.
  scope: per newly launched instance.
  link: [Data is not automatically copied](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-data-not-copied-to-new-instances)
  link: [lifecycle hooks to copy the data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-data-not-copied-to-new-instances)
ec2-auto-scaling-faq-definition
  claim: Amazon EC2 Auto Scaling is a fully managed service that launches or terminates EC2 instances automatically to keep the correct number of instances available for the application load.
  scope: Amazon EC2 Auto Scaling (service definition).
  link: [fully managed service](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-definition)
  say: a fully managed service that launches or terminates instances automatically
ec2-auto-scaling-faq-delete-group-terminates-instances
  claim: If you delete an Auto Scaling group that has running instances, the instances are terminated and the group is deleted.
  scope: per Auto Scaling group (deletion).
  link: [the instances will be terminated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-delete-group-terminates-instances)
ec2-auto-scaling-faq-does-not-add-volumes
  claim: EC2 Auto Scaling does not automatically add a volume when an existing volume approaches capacity; a volume is attached to a new instance when that instance is added, and the EC2 API adds a volume to an existing instance.
  scope: per instance EBS volumes.
  link: [doesn't automatically add a volume](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-does-not-add-volumes)
ec2-auto-scaling-faq-dynamic-scaling-alarm-example
  claim: In the FAQ example of dynamic scaling, if CPU spikes above 80% and an alarm is set up, EC2 Auto Scaling can add a new instance dynamically.
  scope: per EC2 Auto Scaling group; an alarm must be set up; 80% is an example threshold.
  link: [above 80%](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-dynamic-scaling-alarm-example)
  say: above eighty percent
ec2-auto-scaling-faq-elb-requests-before-detection-fail
  claim: When ELB notices that an instance is unhealthy it stops routing requests to it, but before it discovers that the instance is unhealthy, some requests to that instance fail.
  scope: per Auto Scaling group with a load balancer.
  link: [some requests to that instance will fail](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-elb-requests-before-detection-fail)
  link: [stop routing requests to it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-elb-requests-before-detection-fail)
ec2-auto-scaling-faq-fleet-management-vs-dynamic-scaling
  claim: Fleet management is the function that automatically replaces unhealthy instances and keeps the fleet at the desired capacity; dynamic scaling is the function that automatically increases or decreases capacity based on load or other metrics.
  scope: Amazon EC2 Auto Scaling functions.
  link: [automatically replaces unhealthy instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-fleet-management-vs-dynamic-scaling)
  link: [automatically increases or decreases capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-fleet-management-vs-dynamic-scaling)
ec2-auto-scaling-faq-group-definition
  claim: An Auto Scaling group is a collection of EC2 instances with similar characteristics, treated as a logical grouping for fleet management and dynamic scaling; the group adjusts the number of instances to keep a fixed count even if an instance becomes unhealthy.
  scope: per Auto Scaling group.
  link: [treated as a logical grouping](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-group-definition)
  link: [maintain a fixed number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-group-definition)
ec2-auto-scaling-faq-group-from-instance-no-new-ami
  claim: Creating an Auto Scaling group from an existing instance does not create a new AMI.
  scope: per Auto Scaling group created from an existing instance.
  link: [does not create a new AMI](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-group-from-instance-no-new-ami)
ec2-auto-scaling-faq-group-size-bounded-by-ec2-quota
  claim: A group can have as many instances as the account's EC2 quota allows.
  scope: per Auto Scaling group; maximum; adjustable; bounded by the account's EC2 instance quota.
  link: [as your EC2 quota allows](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-group-size-bounded-by-ec2-quota)
  say: as many instances as your EC2 quota allows
ec2-auto-scaling-faq-groups-created-outside-aws-auto-scaling
  claim: EC2 Auto Scaling groups must be created and configured outside of AWS Auto Scaling, for example through the EC2 console, the Auto Scaling API or CloudFormation; AWS Auto Scaling can help you configure dynamic scaling policies for existing groups.
  scope: per Auto Scaling group used in a scaling plan.
  link: [created and configured outside of AWS Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-groups-created-outside-aws-auto-scaling)
ec2-auto-scaling-faq-iam-resource-level-permissions
  claim: With Amazon EC2 Auto Scaling resource-level permissions, you can restrict access to a particular Auto Scaling group or launch configuration.
  scope: per IAM policy.
  link: [resource-level permissions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-iam-resource-level-permissions)
ec2-auto-scaling-faq-instance-type-weights
  claim: A group can use any instance type available in the Region, and each instance type can carry an optional weight that defines how many capacity units an instance of that type contributes.
  scope: per instance type in a group.
  link: [optional weight for each instance type](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-instance-type-weights)
  link: [capacity units that each instance would contribute](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-instance-type-weights)
ec2-auto-scaling-faq-launch-configuration-change-existing-unaffected
  claim: When you change a group's launch configuration, new instances launch with the new configuration, but existing instances are not affected.
  scope: per Auto Scaling group that uses a launch configuration.
  link: [existing instances are not affected](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-launch-configuration-change-existing-unaffected)
ec2-auto-scaling-faq-launch-configuration-multiple-groups
  claim: The same launch configuration can be specified with multiple EC2 Auto Scaling groups.
  scope: per launch configuration; a group still uses only one launch configuration at a time.
  link: [with multiple EC2 Auto Scaling groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-launch-configuration-multiple-groups)
  say: you can reuse a launch configuration across groups
ec2-auto-scaling-faq-launch-configuration-one-and-immutable
  claim: A group can have only one launch configuration at a time, and a launch configuration cannot be modified after it is created; to change it, create a new launch configuration and update the group.
  scope: per Auto Scaling group.
  link: [only specify one launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-launch-configuration-one-and-immutable)
  link: [can't modify a launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-launch-configuration-one-and-immutable)
ec2-auto-scaling-faq-launch-configuration-template
  claim: A launch configuration is a template that an EC2 Auto Scaling group uses to launch EC2 instances.
  scope: per EC2 Auto Scaling group.
  link: [A launch configuration is a template](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-launch-configuration-template)
  say: a launch configuration is a template
ec2-auto-scaling-faq-lifecycle-hooks-definition
  claim: Lifecycle hooks let you take action before an instance goes into service or before it is terminated; a launch hook can configure software before the instance is connected to the load balancer, and a terminate hook can collect data before the instance goes away.
  scope: per lifecycle hook.
  link: [before an instance goes into service](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-lifecycle-hooks-definition)
  link: [launch hooks can perform software configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-lifecycle-hooks-definition)
ec2-auto-scaling-faq-no-additional-fees
  claim: EC2 Auto Scaling fleet management and dynamic scaling carry no additional fees; EC2 and CloudWatch service fees apply and are billed separately.
  scope: per account; fixed.
  link: [no additional fees](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-no-additional-fees)
  link: [service fees apply and are billed separately](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-no-additional-fees)
  say: no additional fees
ec2-auto-scaling-faq-no-elb-required-ec2-health-check
  claim: You do not have to use ELB to use Auto Scaling: the EC2 health check can identify and replace unhealthy instances on its own.
  scope: per Auto Scaling group (health checks).
  link: [don't have to use ELB](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-no-elb-required-ec2-health-check)
  link: [use the EC2 health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-no-elb-required-ec2-health-check)
ec2-auto-scaling-faq-on-demand-base-spot-above
  claim: When combining purchase models, you can set the group's base capacity to be fulfilled by On-Demand Instances; as the group scales, anything beyond the base is fulfilled with only Spot Instances or with a specified percentage mix of On-Demand and Spot.
  scope: per Auto Scaling group.
  link: [base capacity be fulfilled with On-Demand instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-on-demand-base-spot-above)
  link: [specified percentage mix of On-Demand or Spot instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-on-demand-base-spot-above)
ec2-auto-scaling-faq-persist-data-off-instance
  claim: If data on an instance must survive scale-in, store it off the instance in a service such as S3, RDS or DynamoDB.
  scope: per instance data that must survive scale in.
  link: [S3, RDS, or DynamoDB](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-persist-data-off-instance)
  link: [stored off the instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-persist-data-off-instance)
ec2-auto-scaling-faq-predictive-ahead-of-demand
  claim: For predictable load changes, a predictive scaling policy proactively increases capacity ahead of upcoming demand.
  scope: per predictive scaling policy.
  link: [proactively increase capacity ahead of upcoming demand](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-ahead-of-demand)
ec2-auto-scaling-faq-predictive-policy-cli-console-sdk
  claim: Predictive scaling can be used directly through the AWS CLI, the EC2 Auto Scaling console and the AWS SDKs, in the same way as other scaling policies such as simple scaling or target tracking.
  scope: per EC2 Auto Scaling group.
  link: [similar to how you use other scaling policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-policy-cli-console-sdk)
  say: like any other scaling policy
ec2-auto-scaling-faq-predictive-policy-vs-scaling-plan
  claim: A predictive scaling policy brings a prediction algorithm similar to the one offered through an AWS Auto Scaling plan into EC2 Auto Scaling as a native scaling policy, so you do not have to create a scaling plan just to use predictive scaling.
  scope: per predictive scaling policy.
  link: [native scaling policy in EC2 Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-policy-vs-scaling-plan)
  link: [create an AWS Auto Scaling plan](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-policy-vs-scaling-plan)
ec2-auto-scaling-faq-regional-spans-azs-not-regions
  claim: An Auto Scaling group is a Regional construct: it can span Availability Zones, but not Regions.
  scope: per Auto Scaling group.
  link: [regional constructs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-regional-spans-azs-not-regions)
  link: [can span Availability Zones, but not AWS regions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-regional-spans-azs-not-regions)
ec2-auto-scaling-faq-replacement-time-minutes
  claim: Replacing an unhealthy instance with a new InService instance takes minutes: most replacements happen in less than 5 minutes, and the time depends on factors such as how long the AMI takes to boot.
  scope: per replacement; depends on factors such as AMI boot time.
  link: [less than 5 minutes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-replacement-time-minutes)
  link: [within minutes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-replacement-time-minutes)
  say: less than five minutes
ec2-auto-scaling-faq-replaces-impaired-instance
  claim: When an impaired instance fails a health check, EC2 Auto Scaling automatically terminates it and replaces it with a new one; with an Elastic Load Balancing load balancer it detaches the impaired instance from the load balancer before provisioning the replacement.
  scope: per Auto Scaling group (health checks).
  link: [automatically terminates it and replaces it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-replaces-impaired-instance)
  link: [gracefully detaches the impaired instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-replaces-impaired-instance)
ec2-auto-scaling-faq-retarget-other-azs
  claim: If none of the specified instance types are available in an Availability Zone, Auto Scaling retargets the launches to the group's other Availability Zones; it always prefers to keep compute balanced across zones.
  scope: per Auto Scaling group; none of the specified instance types is available in that zone.
  link: [retarget the launches in other Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-retarget-other-azs)
  link: [keeping your compute balanced across Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-retarget-other-azs)
ec2-auto-scaling-faq-ri-discount-applies-to-on-demand
  claim: Reserved Instance discounts apply to On-Demand Instances that a group launches: if you hold RIs for an instance family and EC2 Auto Scaling launches a matching instance, you receive RI pricing.
  scope: per account; the launched instance matches the Reserved Instance.
  link: [receive your RI pricing for On-Demand Instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-ri-discount-applies-to-on-demand)
ec2-auto-scaling-faq-set-instance-health-custom-check
  claim: The SetInstanceHealth API lets you mark an instance UNHEALTHY yourself, which results in its termination and replacement; this is how a custom health check reports to the group.
  scope: per Auto Scaling group (health checks).
  link: [SetInstanceHealth](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-set-instance-health-custom-check)
  link: [result in a termination and replacement](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-set-instance-health-custom-check)
ec2-auto-scaling-faq-single-group-mixed-purchase-options
  claim: A single Auto Scaling group can provision and scale EC2 capacity across different instance types, Availability Zones, and On-Demand, RI and Spot purchase options, with a chosen split between On-Demand and Spot capacity.
  scope: per Auto Scaling group.
  link: [On-Demand, RIs and Spot purchase options](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-single-group-mixed-purchase-options)
  link: [desired split between On-Demand and Spot capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-single-group-mixed-purchase-options)
ec2-auto-scaling-faq-sns-notification-on-scale
  claim: You can configure a group to send an Amazon SNS notification whenever it scales; SNS delivers it as HTTP or HTTPS POST, email, or a message to an SQS queue.
  scope: per Auto Scaling group (notifications).
  link: [send an SNS notification](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-sns-notification-on-scale)
ec2-auto-scaling-faq-sns-terminate-notification-example
  claim: If the group uses the autoscaling: EC2_INSTANCE_TERMINATE notification type and terminates an instance, it sends an email notification with details such as the instance ID and the reason for the termination.
  scope: per EC2 Auto Scaling group; the notification type is configured and the SNS subscription is email (FAQ example).
  link: [it sends an email notification](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-sns-terminate-notification-example)
  say: it sends an email with the instance ID and the reason
ec2-auto-scaling-faq-stateful-instance
  claim: A stateful instance holds data that exists only on that instance, so terminating it loses that data; use lifecycle hooks to copy the data off before termination, or enable instance protection so EC2 Auto Scaling does not terminate it.
  scope: per stateful instance.
  link: [exists only on that instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-stateful-instance)
  link: [lifecycle hooks to copy the data off](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-stateful-instance)
  link: [enable instance protection](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-stateful-instance)
ec2-auto-scaling-faq-suspend-health-checks
  claim: You can temporarily suspend EC2 Auto Scaling health checks with the SuspendProcesses API, for example to inspect an unhealthy instance, and resume them with ResumeProcesses.
  scope: per Auto Scaling group (scaling processes).
  link: [SuspendProcesses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-suspend-health-checks)
  link: [ResumeProcesses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-suspend-health-checks)
ec2-auto-scaling-faq-target-tracking-average-cpu-example
  claim: With target tracking set to keep CPU utilization of a web server fleet at 50%, EC2 Auto Scaling launches or terminates instances as required to keep the average CPU utilization at 50%.
  scope: per EC2 Auto Scaling group with a target tracking policy; FAQ example value; the target is chosen by the user.
  link: [average CPU utilization at 50%](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-target-tracking-average-cpu-example)
  say: keeps the average CPU at fifty percent
ec2-auto-scaling-faq-target-tracking-definition
  claim: With target tracking you select a load metric such as CPU utilization or request count and set a target value; EC2 Auto Scaling then adjusts the number of instances to maintain that target, like a home thermostat.
  scope: per target tracking scaling policy.
  link: [adjusts the number of EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-target-tracking-definition)
  link: [home thermostat](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-target-tracking-definition)
ec2-auto-scaling-faq-termination-policy-and-instance-protection
  claim: A termination policy decides which instances EC2 Auto Scaling terminates first when it scales in; instance protection prevents EC2 Auto Scaling from selecting specific instances for termination when scaling in.
  scope: per Auto Scaling group during scale in.
  link: [termination policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-termination-policy-and-instance-protection)
  link: [use instance protection to prevent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-termination-policy-and-instance-protection)
ec2-auto-scaling-faq-unhealthy-instance-definition
  claim: An unhealthy instance is one whose hardware has become impaired, or one that is not passing a user-configured ELB health check; EC2 Auto Scaling checks each instance at regular intervals and can also run ELB health checks when the instance is connected to a load balancer.
  scope: per Auto Scaling group (health checks).
  link: [hardware has become impaired](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-unhealthy-instance-definition)
  link: [not passing a user-configured ELB health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-unhealthy-instance-definition)
ec2-auto-scaling-faq-update-mixed-instances-settings
  claim: An existing group can be updated to change its mixed-instances settings: instance types, the prioritization order for On-Demand Instances, the percentage split between On-Demand and Spot, and the allocation strategy.
  scope: per Auto Scaling group.
  link: [update an existing ASG](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-update-mixed-instances-settings)
  link: [percentage split between On-Demand and Spot instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-update-mixed-instances-settings)
ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling
  claim: Use AWS Auto Scaling to manage scaling for multiple resources across multiple services; use EC2 Auto Scaling if you only need to scale Auto Scaling groups or only want to maintain the health of the EC2 fleet.
  scope: choice between EC2 Auto Scaling and AWS Auto Scaling.
  link: [multiple resources across multiple services](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling)
  link: [only need to scale Amazon EC2 Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling)
ec2-auto-scaling-faq-which-health-check-type
  claim: If the group uses Elastic Load Balancing, select the ELB health check; if it does not, select the EC2 health check.
  scope: per Auto Scaling group (health checks).
  link: [select an ELB health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-which-health-check-type)
  link: [select the EC2 health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-which-health-check-type)
ec2-auto-scaling-faq-without-elb-route53-or-proxy
  claim: Without ELB, users can be directed to the other instances by integrating with Route53 (not supported natively by EC2 Auto Scaling, but used by many customers), by your own reverse proxy, or, for internal microservices, by a service discovery solution.
  scope: per Auto Scaling group without a load balancer.
  link: [integrate with Route53](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-without-elb-route53-or-proxy)
  link: [your own reverse proxy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-without-elb-route53-or-proxy)
  link: [service discovery solutions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-without-elb-route53-or-proxy)
ec2-auto-scaling-faq-works-with-alb-nlb-health-checks
  claim: EC2 Auto Scaling works with Application Load Balancers and Network Load Balancers, including their health check feature.
  scope: per Auto Scaling group with a load balancer.
  link: [including their health check feature](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-works-with-alb-nlb-health-checks)
ec2-auto-scaling-grace-period-console-300-cli-0
  claim: The default health check grace period is 300 seconds when you create a group in the console, and 0 seconds when you create it with the AWS CLI or an SDK.
  scope: per Auto Scaling group; default; adjustable; 300 seconds in the console; 0 seconds with the AWS CLI or an SDK.
  link: [300 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-console-300-cli-0)
  link: [0 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-console-300-cli-0)
  say: three hundred seconds | zero seconds
ec2-auto-scaling-grace-period-definition
  claim: The health check grace period is the minimum time, in seconds, that a new instance stays in service before Amazon EC2 Auto Scaling terminates it for being unhealthy.
  scope: per Auto Scaling group (health checks).
  link: [minimum amount of time (in seconds)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-definition)
  say: minimum amount of time in seconds
ec2-auto-scaling-grace-period-zero-turns-off
  claim: A health check grace period of 0 turns the grace period off.
  scope: per Auto Scaling group (health checks).
  link: [A value of 0 turns off](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-zero-turns-off)
  say: a value of zero turns it off
ec2-auto-scaling-grace-period-zero-with-launch-hooks
  claim: If you use lifecycle hooks for instance launch, you can set the health check grace period to 0, and a value set too high reduces the effectiveness of health checks.
  scope: per Auto Scaling group (health checks).
  link: [set the health check grace period to 0](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-zero-with-launch-hooks)
  say: set the grace period to zero
ec2-auto-scaling-group-metric-names
  claim: Group metrics in the AWS/AutoScaling namespace include GroupDesiredCapacity (instances the group tries to keep) and GroupInServiceInstances (running instances, not pending or terminating).
  scope: per Auto Scaling group (group metrics).
  link: [GroupDesiredCapacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-group-metric-names)
  link: [GroupInServiceInstances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-group-metric-names)
  link: [AWS/AutoScaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-group-metric-names)
ec2-auto-scaling-group-metrics-best-effort
  claim: With group metrics enabled, EC2 Auto Scaling sends sampled data to CloudWatch every minute on a best-effort basis, and gaps from a CloudWatch disruption are not backfilled.
  scope: per Auto Scaling group (group metrics).
  link: [every minute on a best-effort basis](../facts/ec2-auto-scaling.md#ec2-auto-scaling-group-metrics-best-effort)
  link: [data isn't backfilled](../facts/ec2-auto-scaling.md#ec2-auto-scaling-group-metrics-best-effort)
ec2-auto-scaling-group-metrics-must-enable
  claim: Auto Scaling group metrics are available at one-minute granularity at no additional charge, but you must enable them.
  scope: per Auto Scaling group; default; adjustable.
  link: [one-minute granularity at no additional charge](../facts/ec2-auto-scaling.md#ec2-auto-scaling-group-metrics-must-enable)
  link: [you must enable them](../facts/ec2-auto-scaling.md#ec2-auto-scaling-group-metrics-must-enable)
ec2-auto-scaling-health-assumed-healthy
  claim: Every instance in a group starts with a Healthy status and is assumed healthy unless EC2 Auto Scaling receives a notification that it is unhealthy.
  scope: per Auto Scaling group (health checks).
  link: [start with a `Healthy` status](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-assumed-healthy)
  link: [Instances are assumed to be healthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-assumed-healthy)
ec2-auto-scaling-health-cannot-remove-ec2-checks
  claim: The EC2 status checks and scheduled events cannot be removed from a group's health checks; to stop replacements, AWS recommends suspending the ReplaceUnhealthy and HealthCheck processes.
  scope: per Auto Scaling group (health checks).
  link: [does not provide a way of removing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-cannot-remove-ec2-checks)
  link: [suspend the `ReplaceUnhealthy` and `HealthCheck` process](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-cannot-remove-ec2-checks)
ec2-auto-scaling-health-check-type-ec2-default
  claim: Amazon EC2 status checks and scheduled events are the default health check type of an Auto Scaling group.
  scope: per Auto Scaling group; default; adjustable.
  link: [default health check type](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-check-type-ec2-default)
  say: default health check type
ec2-auto-scaling-health-draining-before-terminating-unhealthy
  claim: With connection draining (deregistration delay) on the load balancer, EC2 Auto Scaling waits for in-flight requests to complete or the maximum timeout to expire before it terminates unhealthy instances.
  scope: per Auto Scaling group with a load balancer.
  link: [waits for either in-flight requests to complete](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-draining-before-terminating-unhealthy)
  link: [connection draining (deregistration delay)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-draining-before-terminating-unhealthy)
ec2-auto-scaling-health-ebs-check-must-be-turned-on
  claim: The Amazon EBS health check type checks whether EBS volumes are reachable and pass I/O status checks; you must turn it on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [Amazon EBS health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-check-must-be-turned-on)
  link: [passing I/O status checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-check-must-be-turned-on)
ec2-auto-scaling-health-ebs-volumes-detached-on-terminate
  claim: When an instance is terminated, its EBS volumes are detached (or deleted, depending on DeleteOnTermination) and are not attached to the replacement; you attach them yourself or with a lifecycle hook.
  scope: per replaced instance.
  link: [attached EBS volumes are detached](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-volumes-detached-on-terminate)
  link: [lifecycle hook-based solution](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-volumes-detached-on-terminate)
ec2-auto-scaling-health-elb-check-must-be-turned-on
  claim: The Elastic Load Balancing health check type checks whether the load balancer reports the instance as healthy and able to handle requests; you must turn it on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [you must turn it on](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on)
  link: [Elastic Load Balancing health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on)
ec2-auto-scaling-health-elb-unhealthy-replaced
  claim: Once ELB health checks are turned on for the group, an instance that Elastic Load Balancing reports as Unhealthy is marked Unhealthy at the next periodic health check and replaced.
  scope: per Auto Scaling group (health checks).
  link: [on its next periodic health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-unhealthy-replaced)
  link: [replaces it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-unhealthy-replaced)
ec2-auto-scaling-health-not-running-immediate
  claim: If EC2 Auto Scaling detects that an instance is no longer in the running state, it treats this as an immediate failure, marks the instance Unhealthy at once and replaces it.
  scope: per Auto Scaling group (health checks).
  link: [treated as an immediate failure](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-not-running-immediate)
  link: [immediately marks the instance as `Unhealthy`](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-not-running-immediate)
ec2-auto-scaling-health-optional-checks-after-grace-period
  claim: EC2 Auto Scaling checks a new instance with the built-in EC2 status checks, and only after a grace period with the optional health checks enabled for the group.
  scope: per Auto Scaling group (health checks).
  link: [after a grace period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-optional-checks-after-grace-period)
  link: [any optional health checks that you enabled](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-optional-checks-after-grace-period)
ec2-auto-scaling-health-replace-at-same-time-default
  claim: By default, new instances are provisioned at the same time as unhealthy existing instances are terminated, which might stop new requests being accepted until the new instances are fully operational.
  scope: per Auto Scaling group; default; adjustable.
  link: [new instances are provisioned at the same time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-replace-at-same-time-default)
ec2-auto-scaling-health-replacement-uses-current-settings
  claim: When an InService instance is unhealthy, EC2 Auto Scaling replaces it to keep the desired capacity, and the new instance launches with the group's current settings and its current launch template or launch configuration.
  scope: per Auto Scaling group (health checks).
  link: [current settings of the Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-replacement-uses-current-settings)
  link: [replaces it with a new instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-replacement-uses-current-settings)
ec2-auto-scaling-health-scheduled-event-replaced
  claim: An instance affected by an EC2 scheduled event is considered unhealthy and replaced; it does not start shutting down until the time in the event timestamp.
  scope: per instance affected by an EC2 scheduled event.
  link: [affected by a scheduled event](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-scheduled-event-replaced)
  link: [considers the instance to be unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-scheduled-event-replaced)
ec2-auto-scaling-health-unexpected-termination-replaced
  claim: When an instance terminates unexpectedly, for example from a Spot interruption or a manual termination, EC2 Auto Scaling launches a replacement to keep the desired capacity.
  scope: per Auto Scaling group (health checks).
  link: [terminates unexpectedly](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-unexpected-termination-replaced)
  link: [automatically launch a replacement instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-unexpected-termination-replaced)
ec2-auto-scaling-health-vpc-lattice-check-must-be-turned-on
  claim: The VPC Lattice health check type checks whether VPC Lattice reports the instance as healthy; like the ELB check, you must turn it on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [you must turn it on](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-vpc-lattice-check-must-be-turned-on)
  link: [VPC Lattice health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-vpc-lattice-check-must-be-turned-on)
ec2-auto-scaling-health-vpc-lattice-ignored-by-default
  claim: By default EC2 Auto Scaling ignores the results of VPC Lattice health checks; you can turn them on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [ignores the results of the VPC Lattice](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-vpc-lattice-ignored-by-default)
ec2-auto-scaling-high-resolution-not-in-govcloud
  claim: Target tracking with high-resolution metrics is available in all AWS Regions except the AWS GovCloud (US) Regions.
  scope: per Region.
  link: [except the AWS GovCloud (US) Regions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-high-resolution-not-in-govcloud)
ec2-auto-scaling-high-resolution-target-tracking
  claim: Since November 22, 2024, a target tracking policy can scale on a high-resolution CloudWatch metric with a period lower than 60 seconds; the lowest supported period is 10 seconds.
  scope: per target tracking scaling policy.
  link: [lower than 60 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-high-resolution-target-tracking)
  link: [lowest supported interval is 10 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-high-resolution-target-tracking)
  link: [November 22, 2024](../facts/ec2-auto-scaling.md#ec2-auto-scaling-high-resolution-target-tracking)
ec2-auto-scaling-imds-target-lifecycle-state
  claim: Code on an instance can detect an upcoming termination by polling the instance metadata item autoscaling/target-lifecycle-state, which EC2 Auto Scaling updates before the instance moves to a new steady state; the current lifecycle state cannot be read from instance metadata.
  scope: per Auto Scaling instance, read through the Instance Metadata Service.
  link: [autoscaling/target-lifecycle-state](../facts/ec2-auto-scaling.md#ec2-auto-scaling-imds-target-lifecycle-state)
  link: [polls for the lifecycle state of an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-imds-target-lifecycle-state)
  link: [You cannot retrieve the current lifecycle state](../facts/ec2-auto-scaling.md#ec2-auto-scaling-imds-target-lifecycle-state)
ec2-auto-scaling-inservice-counts-toward-desired
  claim: A new instance enters the InService state after it is fully configured and passes the EC2 health checks; from then it counts against the group's desired capacity.
  scope: per instance in an Auto Scaling group.
  link: [passes the Amazon EC2 health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-inservice-counts-toward-desired)
  link: [counted against the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-inservice-counts-toward-desired)
  link: [InService](../facts/ec2-auto-scaling.md#ec2-auto-scaling-inservice-counts-toward-desired)
ec2-auto-scaling-instance-lifecycle-policy-retains-on-abandon
  claim: Since November 20, 2025, an instance lifecycle policy can keep an instance in a retained state when its termination lifecycle hook ends with ABANDON; without the policy the instance is terminated at once even after ABANDON.
  scope: per Auto Scaling group with an instance lifecycle policy.
  link: [moves to a retained state](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-lifecycle-policy-retains-on-abandon)
  link: [proceeds to termination immediately](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-lifecycle-policy-retains-on-abandon)
  link: [November 20, 2025](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-lifecycle-policy-retains-on-abandon)
ec2-auto-scaling-instance-maintenance-policy-launch-before-terminate
  claim: An instance maintenance policy (added November 15, 2023) sets a minimum and maximum healthy percentage; the group replaces instances only within that range, so it can launch a new instance and wait for it to be ready before terminating the unhealthy one.
  scope: per Auto Scaling group with an instance maintenance policy.
  link: [minimum and maximum healthy percentage](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-maintenance-policy-launch-before-terminate)
  link: [November 15, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-maintenance-policy-launch-before-terminate)
ec2-auto-scaling-instance-profile-for-app-credentials
  claim: Applications on Auto Scaling instances get credentials from an IAM role: you choose an instance profile in the launch template (or launch configuration), and EC2 passes the role to each instance at launch.
  scope: per launch template used by an Auto Scaling group.
  link: [choose an instance profile](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-profile-for-app-credentials)
  link: [a container for an IAM role](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-profile-for-app-credentials)
ec2-auto-scaling-instance-refresh-all-at-once
  claim: To replace all instances of the group at once, set the instance refresh minimum healthy percentage to 0 percent.
  scope: per instance refresh.
  link: [0 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-all-at-once)
  say: zero percent
ec2-auto-scaling-instance-refresh-auto-rollback-alarm
  claim: An instance refresh can roll back automatically if it fails or if a CloudWatch alarm you specify goes into the ALARM state; a rollback restores the group's previous configuration.
  scope: per instance refresh.
  link: [Automatically roll back if the instance refresh fails](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-auto-rollback-alarm)
  link: [configuration it was previously using](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-auto-rollback-alarm)
ec2-auto-scaling-instance-refresh-auto-rollback-default
  claim: Auto rollback for an instance refresh is disabled by default, both from the AWS CLI or an SDK and in the console.
  scope: per instance refresh; default; adjustable.
  link: [Disabled (false)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-auto-rollback-default)
  say: disabled
ec2-auto-scaling-instance-refresh-bake-time-default
  claim: The bake time of an instance refresh is zero by default.
  scope: per instance refresh; default; adjustable.
  link: [Zero](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-bake-time-default)
  say: zero
ec2-auto-scaling-instance-refresh-checkpoint-delay-default
  claim: The checkpoint delay of an instance refresh is 1 hour (3600 seconds) by default.
  scope: per instance refresh checkpoint; default; adjustable.
  link: [1 hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-checkpoint-delay-default)
  link: [3600 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-checkpoint-delay-default)
  say: one hour | thirty-six hundred seconds
ec2-auto-scaling-instance-refresh-checkpoints
  claim: A checkpoint is a point in time where the instance refresh pauses for a specified amount of time, which lets you deploy updates in phases; without checkpoints, rolling replacements are performed continuously.
  scope: per instance refresh.
  link: [pauses for a specified amount of time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-checkpoints)
  link: [rolling replacements are performed continuously](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-checkpoints)
ec2-auto-scaling-instance-refresh-checkpoints-default
  claim: Checkpoints for an instance refresh are disabled by default, both from the AWS CLI or an SDK and in the console.
  scope: per instance refresh; default; adjustable.
  link: [Disabled (false)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-checkpoints-default)
  say: disabled
ec2-auto-scaling-instance-refresh-cloudwatch-alarm-default
  claim: The CloudWatch alarm setting for an instance refresh is disabled by default, both from the AWS CLI or an SDK and in the console.
  scope: per instance refresh; default; adjustable.
  link: [Disabled (null)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-cloudwatch-alarm-default)
  say: disabled
ec2-auto-scaling-instance-refresh-healthy-percentage-difference
  claim: The difference between the minimum healthy percentage and the maximum healthy percentage of an instance refresh cannot be greater than 100.
  scope: per instance refresh; maximum.
  link: [greater than 100](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-healthy-percentage-difference)
  say: greater than one hundred
ec2-auto-scaling-instance-refresh-launch-before-terminate
  claim: During an instance refresh, if the minimum healthy percentage is 100 percent, EC2 Auto Scaling launches the new instances before terminating the old ones, so desired capacity is kept at all times.
  scope: per instance refresh.
  link: [Launch the new instances first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-launch-before-terminate)
  link: [minimum healthy percentage](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-launch-before-terminate)
  link: [100 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-launch-before-terminate)
ec2-auto-scaling-instance-refresh-max-duration
  claim: An instance refresh can actively replace instances for at most 14 days.
  scope: per instance refresh; maximum; not adjustable.
  link: [14 days](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-max-duration)
  say: fourteen days
ec2-auto-scaling-instance-refresh-max-healthy-percentage-default
  claim: Without an instance maintenance policy, the maximum healthy percentage of an instance refresh defaults to 100 percent.
  scope: per instance refresh; default; adjustable; no instance maintenance policy is set.
  link: [100 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-max-healthy-percentage-default)
  say: one hundred percent
ec2-auto-scaling-instance-refresh-min-healthy-percentage-default
  claim: Without an instance maintenance policy, the minimum healthy percentage of an instance refresh defaults to 90 percent.
  scope: per instance refresh; default; adjustable; no instance maintenance policy is set.
  link: [90 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-min-healthy-percentage-default)
  say: ninety percent
ec2-auto-scaling-instance-refresh-min-max-healthy
  claim: The minimum healthy percentage is the share of desired capacity kept in service, healthy and ready to use during an instance refresh; the maximum healthy percentage is the share of desired capacity that the group can increase to when it replaces instances.
  scope: per instance refresh.
  link: [the desired capacity to keep in service](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-min-max-healthy)
ec2-auto-scaling-instance-refresh-one-at-a-time
  claim: To replace one instance at a time, set both the minimum and maximum healthy percentage of the instance refresh to 100 percent; the refresh then launches a new instance before terminating an old one.
  scope: per instance refresh.
  link: [100 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-one-at-a-time)
  say: one hundred percent
ec2-auto-scaling-instance-refresh-retry-timeout
  claim: When an instance refresh cannot continue making replacements, because it is waiting to replace instances on standby or protected from scale in, or because the new instances do not pass their health checks, Amazon EC2 Auto Scaling keeps retrying for an hour; if the problem persists, the operation fails.
  scope: per instance refresh; maximum; not adjustable.
  link: [an hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-retry-timeout)
  say: an hour
ec2-auto-scaling-instance-refresh-rolling-default
  claim: An instance refresh uses the rolling strategy by default: it terminates instances and launches new ones in batches while keeping desired capacity; the replace root volume strategy instead swaps only the root volume without terminating the instance.
  scope: per instance refresh; default; adjustable.
  link: [Rolling strategy (default)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-rolling-default)
  link: [replacing only the root volume](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-rolling-default)
ec2-auto-scaling-instance-refresh-scale-in-protected-default
  claim: By default, an instance refresh waits when it finds instances protected from scale in if started from the AWS CLI or an SDK, and ignores them if started from the console.
  scope: per instance refresh; default; adjustable; differs between the AWS CLI or SDK and the console.
  link: [Wait](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-scale-in-protected-default)
  link: [Ignore](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-scale-in-protected-default)
  say: wait | ignore
ec2-auto-scaling-instance-refresh-scale-out-uses-desired-config
  claim: If a scale-out event happens during an instance refresh, new instances use the desired configuration, and after the refresh succeeds the group settings are updated to it.
  scope: per instance refresh.
  link: [launches new instances with the desired configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-scale-out-uses-desired-config)
  link: [updates the Auto Scaling group settings](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-scale-out-uses-desired-config)
ec2-auto-scaling-instance-refresh-skip-matching-default
  claim: Skip matching for an instance refresh is disabled by default from the AWS CLI or an SDK and enabled by default in the console.
  scope: per instance refresh; default; adjustable; differs between the AWS CLI or SDK and the console.
  link: [Disabled (false)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-skip-matching-default)
  link: [Enabled](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-skip-matching-default)
  say: disabled | enabled
ec2-auto-scaling-instance-refresh-skip-matching-user-data-gap
  claim: Skip matching does not check for code changes deployed from a user data script, so turn it off when user data pulls new code.
  scope: per instance refresh.
  link: [doesn't check for code changes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-skip-matching-user-data-gap)
  link: [turn off skip matching](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-skip-matching-user-data-gap)
ec2-auto-scaling-instance-refresh-standby-default
  claim: By default, an instance refresh waits when it finds instances in Standby if started from the AWS CLI or an SDK, and ignores them if started from the console.
  scope: per instance refresh; default; adjustable; differs between the AWS CLI or SDK and the console.
  link: [Wait](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-standby-default)
  link: [Ignore](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-standby-default)
  say: wait | ignore
ec2-auto-scaling-instance-refresh-ten-percent-at-a-time
  claim: With a minimum healthy percentage of 90 percent and a maximum healthy percentage of 100 percent, an instance refresh replaces 10 percent of capacity at a time.
  scope: per instance refresh.
  link: [10 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-ten-percent-at-a-time)
  say: ten percent
ec2-auto-scaling-instance-refresh-use-cases
  claim: An instance refresh can help you deploy a new AMI or user data script across the group, migrate instances to new instance types, or switch a group from a launch configuration to a launch template.
  scope: per instance refresh.
  link: [Deploying a new Amazon Machine Image (AMI)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-use-cases)
  link: [roll out the updates immediately](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-use-cases)
ec2-auto-scaling-instance-refresh-warm-pool-order
  claim: An instance refresh replaces InService instances first and then the instances in the warm pool.
  scope: per instance refresh.
  link: [Then it replaces instances in the warm pool](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-warm-pool-order)
  link: [before instances that are in a warm pool](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-warm-pool-order)
ec2-auto-scaling-instance-refresh-warmup-default
  claim: An instance refresh uses the group's default instance warmup, if defined, or otherwise its health check grace period, as the instance warmup.
  scope: per instance refresh; default; adjustable.
  link: [default instance warmup](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-warmup-default)
  link: [health check grace period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-warmup-default)
  say: default instance warmup | health check grace period
ec2-auto-scaling-interface-endpoint-privatelink
  claim: An interface VPC endpoint (AWS PrivateLink) lets you call the EC2 Auto Scaling APIs privately, keeping traffic between the VPC and the service on the AWS network, with no internet gateway, NAT device or virtual private gateway needed.
  scope: per VPC.
  link: [interface VPC endpoint](../facts/ec2-auto-scaling.md#ec2-auto-scaling-interface-endpoint-privatelink)
  link: [don't need an internet gateway, a NAT device](../facts/ec2-auto-scaling.md#ec2-auto-scaling-interface-endpoint-privatelink)
ec2-auto-scaling-interruptible-capacity-reservation-notice
  claim: An Auto Scaling group can use Interruptible Capacity Reservations: unused reserved capacity from On-Demand Capacity Reservations, or interruptible reservations shared through AWS Resource Access Manager, in exchange for accepting a 2-minute reclamation notice.
  scope: per instance in an Interruptible Capacity Reservation.
  link: [2-minute reclamation notice](../facts/ec2-auto-scaling.md#ec2-auto-scaling-interruptible-capacity-reservation-notice)
ec2-auto-scaling-launch-config-immutable
  claim: A launch configuration cannot be modified after it is created; to change it you create a new launch configuration and update the group, and a group uses only one launch configuration at a time.
  scope: per launch configuration.
  link: [can't modify a launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-immutable)
  link: [only specify one launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-immutable)
  link: [must create a launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-immutable)
ec2-auto-scaling-launch-config-no-mixed-types
  claim: With a launch configuration you cannot create a group that launches both Spot and On-Demand Instances or that uses multiple instance types; a launch template is required for these features.
  scope: per launch configuration.
  link: [launches both Spot and On-Demand Instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-no-mixed-types)
  link: [must use a launch template](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-no-mixed-types)
ec2-auto-scaling-launch-configurations-blocked-for-new-accounts
  claim: An account created on or after October 1, 2024 cannot create a launch configuration by any method (console, API, AWS CLI, or CloudFormation).
  scope: per account, by account creation date.
  link: [October 1, 2024](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-blocked-for-new-accounts)
  link: [cannot create new launch configurations using any method](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-blocked-for-new-accounts)
ec2-auto-scaling-launch-configurations-console-blocked-2023
  claim: An account created on or after June 1, 2023 cannot create a launch configuration in the console.
  scope: per account, by account creation date.
  link: [June 1, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-console-blocked-2023)
ec2-auto-scaling-launch-configurations-no-new-instance-types
  claim: As of January 1, 2023, new EC2 instance types are not supported in launch configurations.
  scope: per launch configuration.
  link: [January 1, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-no-new-instance-types)
  link: [no longer supported in launch configurations](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-no-new-instance-types)
ec2-auto-scaling-launch-hook-states
  claim: With an EC2_INSTANCE_LAUNCHING lifecycle hook, a new instance moves from Pending to Pending:Wait, then to Pending:Proceed after you complete the lifecycle action, and then to InService.
  scope: per instance with a launch lifecycle hook.
  link: [Pending:Wait](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-hook-states)
  link: [Pending:Proceed](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-hook-states)
  link: [EC2_INSTANCE_LAUNCHING](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-hook-states)
ec2-auto-scaling-launch-in-az-with-fewest
  claim: EC2 Auto Scaling tries to maintain equivalent numbers of instances in each enabled Availability Zone by attempting to launch new instances in the zone with the fewest instances.
  scope: per Auto Scaling group across Availability Zones.
  link: [the Availability Zone with the fewest instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-in-az-with-fewest)
  link: [maintain equivalent numbers of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-in-az-with-fewest)
ec2-auto-scaling-launch-retries-other-az
  claim: If a launch in one Availability Zone fails, EC2 Auto Scaling tries another Availability Zone until a launch succeeds; with several subnets in a zone it prefers the subnet with the most free IP addresses.
  scope: per Auto Scaling group across Availability Zones.
  link: [in another Availability Zone until it succeeds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-retries-other-az)
  link: [the highest number of available IP addresses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-retries-other-az)
ec2-auto-scaling-launch-template-ami-rule
  claim: All launch template parameters are optional, but if the template does not specify an AMI you cannot add the AMI when you create the Auto Scaling group.
  scope: per launch template used by an Auto Scaling group.
  link: [you cannot add the AMI](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-ami-rule)
  link: [all parameters are optional](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-ami-rule)
ec2-auto-scaling-launch-template-latest-version-passrole-risk
  claim: When a group uses the $Latest or $Default launch template version, later launches use that version, even if it has changed, with the permissions of the service-linked role, so a user who can update the template could pass an IAM role to instances without iam:PassRole; the autoscaling:LaunchTemplateVersionSpecified condition key limits who can configure groups to use $Latest or $Default.
  scope: per launch template used by an Auto Scaling group; group uses $Latest or $Default.
  link: [even if they don't have the `iam:PassRole` permission](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-latest-version-passrole-risk)
  link: [autoscaling:LaunchTemplateVersionSpecified](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-latest-version-passrole-risk)
ec2-auto-scaling-launch-template-newer-features
  claim: Launch templates give access to newer EC2 features such as Systems Manager parameters for the AMI ID, Capacity Reservations, Capacity Blocks and Dedicated Hosts.
  scope: per launch template used by an Auto Scaling group.
  link: [Systems Manager parameters (AMI ID)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-newer-features)
  link: [Capacity Reservations, Capacity Blocks, and Dedicated Hosts](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-newer-features)
ec2-auto-scaling-launch-template-passrole-needed
  claim: Instances in an Auto Scaling group get an IAM role through an instance profile chosen in the launch template; the IAM identity that creates or updates a group with a launch template that specifies an instance profile needs the iam:PassRole permission.
  scope: per launch template used by an Auto Scaling group; the launch template specifies an instance profile.
  link: [iam:PassRole](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-passrole-needed)
  link: [choose an instance profile](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-passrole-needed)
ec2-auto-scaling-launch-template-versions
  claim: A launch template, unlike a launch configuration, can have multiple versions.
  scope: per launch template used by an Auto Scaling group.
  link: [multiple versions of a launch template](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-versions)
  link: [launch template instead of a launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-template-versions)
ec2-auto-scaling-launchinstances-needs-launch-template
  claim: The LaunchInstances API works only with groups that use launch templates; groups with launch configurations are not supported.
  scope: per Auto Scaling group.
  link: [only works with Auto Scaling groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launchinstances-needs-launch-template)
  link: [launch configurations are not supported](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launchinstances-needs-launch-template)
ec2-auto-scaling-launchinstances-one-az-and-single-purchase-option
  claim: A LaunchInstances call targets only one Availability Zone, and the API supports mixed instances policies that are fully On-Demand or fully Spot, not a mix of both.
  scope: per LaunchInstances API call.
  link: [can only target one Availability Zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launchinstances-one-az-and-single-purchase-option)
  link: [fully On-Demand or fully Spot purchasing options only](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launchinstances-one-az-and-single-purchase-option)
ec2-auto-scaling-lb-attach-target-group
  claim: For an Application, Network or Gateway Load Balancer you attach a target group to the Auto Scaling group, not the load balancer itself; a Classic Load Balancer is attached directly.
  scope: per Auto Scaling group with a load balancer.
  link: [attach a target group rather than](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-attach-target-group)
  link: [registered directly with the load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-attach-target-group)
ec2-auto-scaling-lb-auto-register-deregister
  claim: With a load balancer attached, instances that the group launches are registered with the load balancer automatically, and instances it terminates are deregistered automatically; you do not register instances one by one.
  scope: per Auto Scaling group with a load balancer.
  link: [automatically registered with the load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-auto-register-deregister)
  link: [automatically deregistered from the load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-auto-register-deregister)
ec2-auto-scaling-lb-default-ec2-checks-only
  claim: By default EC2 Auto Scaling replaces only instances that are unhealthy or unreachable by the Amazon EC2 health checks; with Elastic Load Balancing health checks turned on it can also replace a running instance that an attached load balancer reports as unhealthy.
  scope: per Auto Scaling group; default; adjustable.
  link: [only replaces instances that are unhealthy or unreachable](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
  link: [report it as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
ec2-auto-scaling-lb-four-types
  claim: An Auto Scaling group can be used with all four Elastic Load Balancing types: Application, Network, Gateway and Classic Load Balancers.
  scope: per Auto Scaling group with a load balancer.
  link: [four types of load balancers](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-four-types)
  link: [Gateway Load Balancers](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-four-types)
  link: [Classic Load Balancers](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-four-types)
ec2-auto-scaling-lb-no-traffic-to-disabled-az
  claim: A load balancer does not route traffic to registered targets in Availability Zones that are not enabled for the load balancer.
  scope: per Auto Scaling group with a load balancer.
  link: [does not route traffic to them](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-no-traffic-to-disabled-az)
ec2-auto-scaling-lifecycle-hook-abandon-continue
  claim: A lifecycle action ends with continue or abandon: at launch, continue puts the instance in service and abandon lets the group terminate and replace it; at termination both let the instance terminate, and abandon skips remaining hooks.
  scope: per lifecycle hook.
  link: [abandon indicates that your custom actions were unsuccessful](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-abandon-continue)
  link: [both abandon and continue allow the instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-abandon-continue)
ec2-auto-scaling-lifecycle-hook-default-result
  claim: When a lifecycle hook's timeout elapses or an unexpected failure occurs, the Auto Scaling group takes the hook's default result, and that default value is ABANDON.
  scope: per lifecycle hook; default; adjustable.
  link: [ABANDON](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-default-result)
  say: abandon
ec2-auto-scaling-lifecycle-hook-eventbridge-default
  claim: By default a lifecycle hook added in the console sends its notifications to EventBridge; to send them directly to SNS, SQS or Lambda you add the hook with the CLI, CloudFormation or an SDK.
  scope: per lifecycle hook created in the console; default; adjustable.
  link: [sends lifecycle event notifications to Amazon EventBridge](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-eventbridge-default)
  link: [sends notifications directly to Amazon SNS](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-eventbridge-default)
ec2-auto-scaling-lifecycle-hook-eventbridge-recommended-target
  claim: AWS recommends EventBridge over Amazon SNS or Amazon SQS as the notification target of a lifecycle hook; the SNS and SQS notifications carry the same information.
  scope: per lifecycle hook.
  link: [use EventBridge instead of Amazon SNS](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-eventbridge-recommended-target)
ec2-auto-scaling-lifecycle-hook-four-targets
  claim: A lifecycle hook notification can target Amazon EventBridge, Amazon SNS, Amazon SQS, or AWS Lambda directly.
  scope: per lifecycle hook.
  link: [four different approaches for implementing notification targets](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-four-targets)
  link: [Invoke a Lambda function](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-four-targets)
ec2-auto-scaling-lifecycle-hook-global-timeout
  claim: An instance cannot stay in a lifecycle hook wait state longer than the global timeout of 48 hours or 100 times the heartbeat timeout, whichever is smaller.
  scope: per lifecycle action; maximum; not adjustable.
  link: [48 hours](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-global-timeout)
  link: [100 times the heartbeat timeout](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-global-timeout)
  say: forty-eight hours | one hundred times the heartbeat timeout
ec2-auto-scaling-lifecycle-hook-heartbeat-timeout-default
  claim: A lifecycle hook's heartbeat timeout is 3600 seconds (1 hour) by default.
  scope: per lifecycle hook; default; adjustable.
  link: [3600 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-heartbeat-timeout-default)
  link: [1 hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-heartbeat-timeout-default)
  say: thirty-six hundred seconds | one hour
ec2-auto-scaling-lifecycle-hook-heartbeat-timeout-range
  claim: The heartbeat timeout of a lifecycle hook can be set between 30 and 7200 seconds.
  scope: per lifecycle hook; maximum; not adjustable.
  link: [30 to 7200 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-heartbeat-timeout-range)
  say: thirty to seventy-two hundred seconds
ec2-auto-scaling-lifecycle-hook-lambda-direct-target
  claim: Since July 28, 2025, a lifecycle hook can send its notification directly to a Lambda function; a direct SNS, SQS or Lambda target is set with the AWS CLI, CloudFormation or an SDK, while the console sends lifecycle events to EventBridge by default.
  scope: per lifecycle hook.
  link: [July 28, 2025](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-lambda-direct-target)
  link: [sends lifecycle event notifications to Amazon EventBridge](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-lambda-direct-target)
ec2-auto-scaling-lifecycle-hook-lb-registration
  claim: A launch lifecycle hook is commonly used to make sure bootstrap scripts have finished and the application is ready before the instance is registered with the load balancer at the end of the hook.
  scope: per lifecycle hook.
  link: [ready to accept traffic](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-lb-registration)
  link: [control when instances are registered](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-lb-registration)
ec2-auto-scaling-lifecycle-hook-not-for-attach-detach-standby
  claim: Lifecycle hooks do not run when you attach or detach instances, move instances in or out of standby, or delete the group with the force delete option.
  scope: per lifecycle hook.
  link: [move instances in and out of standby mode](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-not-for-attach-detach-standby)
  link: [attach or detach instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-not-for-attach-detach-standby)
ec2-auto-scaling-lifecycle-hook-purpose
  claim: A lifecycle hook lets you run a custom action when an instance launches or terminates, and gives a set time, one hour by default, for the action before the instance moves to the next state.
  scope: per lifecycle hook.
  link: [one hour by default](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-purpose)
  link: [perform a custom action on instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-purpose)
ec2-auto-scaling-lifecycle-hook-scale-in-use
  claim: An example use of a lifecycle hook on scale in: the hook pauses the instance before it is terminated and sends a notification using Amazon EventBridge; while the instance is in the wait state, you can invoke a Lambda function or connect to the instance to download logs or other data.
  scope: per lifecycle hook.
  link: [pauses the instance before it is terminated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-scale-in-use)
  link: [download logs or other data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-scale-in-use)
ec2-auto-scaling-lifecycle-hook-scale-out-metrics-wait
  claim: On scale out, EC2 Auto Scaling does not count a new instance toward the group's aggregated metrics until it is InService and its instance warmup has finished.
  scope: per lifecycle hook.
  link: [doesn't immediately count a new instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-scale-out-metrics-wait)
  link: [the instance warmup has finished](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-scale-out-metrics-wait)
ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice
  claim: A lifecycle hook does not prevent a Spot Instance from terminating when capacity is no longer available, which can happen at any time with a two-minute interruption notice.
  scope: per Spot Instance in an Auto Scaling group.
  link: [two-minute interruption notice](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice)
  link: [does not prevent an instance from terminating](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice)
  say: two-minute interruption notice
ec2-auto-scaling-lifecycle-hook-target-same-region
  claim: The EventBridge rule, Lambda function, SNS topic or SQS queue used with a lifecycle hook must be in the same Region as the Auto Scaling group.
  scope: per lifecycle hook.
  link: [must always be in the same Region](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-target-same-region)
  link: [same Region](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-target-same-region)
ec2-auto-scaling-lifecycle-hook-user-data-complete
  claim: A user data script can perform custom actions on instances as they launch without a notification target; to signal that the lifecycle action is complete, the script must call CompleteLifecycleAction, and you must create an IAM role with a policy that allows the instances to call this API.
  scope: per lifecycle hook.
  link: [do not need to configure a notification target](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-user-data-complete)
  link: [add the CompleteLifecycleAction API call](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-user-data-complete)
ec2-auto-scaling-lifecycle-matching-scale-in
  claim: AWS advises creating a matching scale-in event for each scale-out event, so resources follow demand closely.
  scope: per Auto Scaling group.
  link: [a corresponding scale-in event for each scale-out event](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-matching-scale-in)
ec2-auto-scaling-lifecycle-pending-then-inservice
  claim: Instances launched in a scale-out start in the Pending state; when fully configured and passing the EC2 health checks they enter InService.
  scope: per instance in an Auto Scaling group.
  link: [start in the `Pending` state](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-pending-then-inservice)
  link: [it enters the `InService` state](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-pending-then-inservice)
ec2-auto-scaling-maintenance-policy-custom
  claim: A custom instance maintenance policy sets your own minimum and maximum range of capacity to keep available while instances are replaced, to balance cost and availability.
  scope: per Auto Scaling group with an instance maintenance policy.
  link: [Custom policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-custom)
  link: [a custom minimum and maximum range](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-custom)
ec2-auto-scaling-maintenance-policy-does-not-block-scaling
  claim: An instance maintenance policy applies only to instance maintenance events and does not prevent the group from being scaled manually or automatically.
  scope: per Auto Scaling group with an instance maintenance policy.
  link: [only applies to instance maintenance events](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-does-not-block-scaling)
  link: [doesn't prevent the group from being manually](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-does-not-block-scaling)
ec2-auto-scaling-maintenance-policy-launch-before-terminating-option
  claim: The Launch before terminating option provisions a new instance before an existing one can be terminated; it favors availability over cost savings.
  scope: per Auto Scaling group with an instance maintenance policy.
  link: [Launch before terminating](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-launch-before-terminating-option)
  link: [favor availability over cost savings](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-launch-before-terminating-option)
ec2-auto-scaling-maintenance-policy-low-min-healthy-faster
  claim: A low minimum healthy percentage replaces instances faster, but can reduce availability if not enough healthy instances are running.
  scope: per Auto Scaling group with an instance maintenance policy.
  link: [replace instances faster](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-low-min-healthy-faster)
  link: [it can reduce availability](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-low-min-healthy-faster)
ec2-auto-scaling-maintenance-policy-none-by-default
  claim: By default an Auto Scaling group has no instance maintenance policy, so it handles instance maintenance events with the default behaviors.
  scope: per Auto Scaling group; default; adjustable.
  link: [to not have an instance maintenance policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-none-by-default)
  link: [the default behaviors](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-none-by-default)
ec2-auto-scaling-maintenance-policy-terminate-and-launch
  claim: The Terminate and launch option of an instance maintenance policy provisions new instances at the same time existing ones are terminated; it favors cost savings over availability.
  scope: per Auto Scaling group with an instance maintenance policy.
  link: [Terminate and launch](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-terminate-and-launch)
  link: [favor cost savings over availability](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-terminate-and-launch)
ec2-auto-scaling-maintenance-policy-unexpected-termination-exception
  claim: Even with an instance maintenance policy, EC2 Auto Scaling still terminates and launches in some situations (unexpected termination, EC2 scheduled events, Spot interruptions), so capacity can fall below the policy's lower threshold.
  scope: per Auto Scaling group with an instance maintenance policy.
  link: [continue to default to terminate and launch](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-unexpected-termination-exception)
  link: [less than the lower threshold](../facts/ec2-auto-scaling.md#ec2-auto-scaling-maintenance-policy-unexpected-termination-exception)
ec2-auto-scaling-manual-scaling-definition
  claim: Manual scaling is the most basic method: you update the desired capacity of the group or terminate instances in it.
  scope: per Auto Scaling group (manual scaling).
  link: [update the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-manual-scaling-definition)
  link: [terminate instances in the Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-manual-scaling-definition)
ec2-auto-scaling-max-instance-lifetime-batch-replacement
  claim: EC2 Auto Scaling usually replaces lifetime-expired instances one at a time, but if the lifetime is too short it may replace several at once, up to 10 percent of current capacity.
  scope: per Auto Scaling group with a maximum instance lifetime.
  link: [up to 10 percent of the current capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-batch-replacement)
  link: [usually replace instances one at a time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-batch-replacement)
ec2-auto-scaling-max-instance-lifetime-clear-with-0
  claim: To clear a maximum instance lifetime, you set it to 0; the setting applies to all current and future instances in the group.
  scope: per Auto Scaling group with a maximum instance lifetime.
  link: [specify a new value of 0](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-clear-with-0)
  say: set it to zero
ec2-auto-scaling-max-instance-lifetime-honors-scale-in-protection
  claim: An instance with scale-in protection is not terminated even when it has reached its maximum instance lifetime.
  scope: per Auto Scaling group with a maximum instance lifetime.
  link: [will not terminate the instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-honors-scale-in-protection)
  say: will not terminate the instance
ec2-auto-scaling-max-instance-lifetime-min-one-day
  claim: The maximum instance lifetime must be at least 86,400 seconds (one day).
  scope: per Auto Scaling group; minimum; not adjustable; 0 clears a previously set value.
  link: [86,400 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-min-one-day)
  link: [at least 86,400 seconds (one day)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-min-one-day)
ec2-auto-scaling-max-instance-lifetime-not-at-console-create
  claim: You cannot set the maximum instance lifetime when you create a group in the console; you can edit the group afterwards.
  scope: per Auto Scaling group with a maximum instance lifetime.
  link: [you cannot set the maximum instance lifetime](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-not-at-console-create)
  say: you cannot set it at creation
ec2-auto-scaling-max-instance-lifetime-purpose
  claim: Maximum instance lifetime is the longest time, in seconds, an instance may be in service before it is terminated and replaced; it is used to replace instances on a schedule for security or compliance.
  scope: per Auto Scaling group with a maximum instance lifetime.
  link: [can be in service before it is terminated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-purpose)
  link: [replace your instances on a schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-purpose)
ec2-auto-scaling-max-instance-lifetime-replacement-uses-current-template
  claim: When maximum instance lifetime replaces an instance, the new instance uses the launch template or configuration currently attached to the group, so a newer AMI version is deployed automatically.
  scope: per Auto Scaling group with a maximum instance lifetime.
  link: [uses the launch template or launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-replacement-uses-current-template)
  link: [will be deployed automatically](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-replacement-uses-current-template)
ec2-auto-scaling-max-instance-lifetime-terminate-then-launch
  claim: By default a lifetime replacement terminates the instance first and launches the new one while it is terminating; an instance maintenance policy can change this to launch before terminate.
  scope: per Auto Scaling group; default; adjustable; an instance maintenance policy changes it.
  link: [another scaling activity launches a new instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-terminate-then-launch)
  link: [launch before terminating](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-terminate-then-launch)
ec2-auto-scaling-metric-math-single-time-series
  claim: A target tracking metric math expression may combine any CloudWatch metrics and functions, but it must return a single time series.
  scope: per target tracking scaling policy.
  link: [must eventually return a single time series](../facts/ec2-auto-scaling.md#ec2-auto-scaling-metric-math-single-time-series)
  link: [single time series](../facts/ec2-auto-scaling.md#ec2-auto-scaling-metric-math-single-time-series)
ec2-auto-scaling-min-max-never-crossed
  claim: An Auto Scaling group has a minimum size and a maximum size; EC2 Auto Scaling ensures the group never goes below the minimum and never goes above the maximum.
  scope: per Auto Scaling group.
  link: [never goes below this size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
  link: [never goes above this size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
  link: [minimum number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
  link: [maximum number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
ec2-auto-scaling-multiple-policies-largest-desired-wins
  claim: When several scaling policies are active, each computes desired capacity independently and the group uses the largest value; for example 10 instances from target tracking and 8 from predictive scaling gives 10.
  scope: per Auto Scaling group with several scaling policies.
  link: [set to the maximum of those](../facts/ec2-auto-scaling.md#ec2-auto-scaling-multiple-policies-largest-desired-wins)
  say: set to the largest of those
ec2-auto-scaling-no-capacity-rebalancing-replace-after-interruption
  claim: Without Capacity Rebalancing, Auto Scaling replaces a Spot Instance only after the Spot service interrupts it and its health check fails.
  scope: per Auto Scaling group with Spot Instances.
  link: [until after the Amazon EC2 Spot service interrupts](../facts/ec2-auto-scaling.md#ec2-auto-scaling-no-capacity-rebalancing-replace-after-interruption)
  say: after the instance is interrupted
ec2-auto-scaling-no-secrets-in-user-data
  claim: AWS recommends never putting confidential or sensitive information in the user data passed to an instance, or in tags and free-form name fields.
  scope: per launch template used by an Auto Scaling group.
  link: [never put confidential or sensitive information](../facts/ec2-auto-scaling.md#ec2-auto-scaling-no-secrets-in-user-data)
ec2-auto-scaling-no-visibility-into-applications
  claim: By default EC2 Auto Scaling has no visibility into the applications on its instances, so it can terminate an instance before the application shuts down gracefully or finishes its jobs.
  scope: per Auto Scaling group during scale in.
  link: [no visibility into the applications](../facts/ec2-auto-scaling.md#ec2-auto-scaling-no-visibility-into-applications)
  link: [able to gracefully shut down](../facts/ec2-auto-scaling.md#ec2-auto-scaling-no-visibility-into-applications)
ec2-auto-scaling-odcr-no-term-commitment
  claim: An On-Demand Capacity Reservation used by an Auto Scaling group reserves compute capacity in a specific Availability Zone with no term commitment.
  scope: per On-Demand Capacity Reservation.
  link: [with no term commitment](../facts/ec2-auto-scaling.md#ec2-auto-scaling-odcr-no-term-commitment)
ec2-auto-scaling-on-demand-prioritized-uses-reserved-instances
  claim: With the prioritized On-Demand allocation strategy, put the instance type of your unused Reserved Instances first in the override list so the group launches it first and gets the Reserved Instance rate.
  scope: per mixed instances group.
  link: [discounted rate of the regular On-Demand Instance pricing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-on-demand-prioritized-uses-reserved-instances)
ec2-auto-scaling-pauses-scale-in-unreliable-metrics
  claim: EC2 Auto Scaling detects unreliable CloudWatch metrics behind scaling policies and pauses scale-in when reliable metrics are not available, for example when data points are missing.
  scope: per Auto Scaling group with scaling policies.
  link: [pauses scale-in activities](../facts/ec2-auto-scaling.md#ec2-auto-scaling-pauses-scale-in-unreliable-metrics)
ec2-auto-scaling-predictive-analyzes-up-to-14-days
  claim: Predictive scaling analyzes metric data from up to the past 14 days to find patterns.
  scope: per predictive scaling policy; maximum; not adjustable.
  link: [14 days](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-analyzes-up-to-14-days)
  say: fourteen days
ec2-auto-scaling-predictive-assumes-homogeneous
  claim: Predictive scaling assumes the group is homogeneous with instances of equal capacity, so forecasts for mixed instances groups can be inaccurate.
  scope: per predictive scaling policy.
  link: [homogenous and all instances are of equal capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-assumes-homogeneous)
  link: [forecasted capacity can be inaccurate](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-assumes-homogeneous)
ec2-auto-scaling-predictive-does-not-scale-in
  claim: Predictive scaling does not scale in when the forecast expects less load; you need dynamic scaling policies to remove capacity.
  scope: per predictive scaling policy.
  link: [it will not scale in to remove capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-does-not-scale-in)
  say: it will not scale in
ec2-auto-scaling-predictive-forecast-next-48-hours
  claim: Predictive scaling generates an hourly capacity forecast for the next 48 hours.
  scope: per predictive scaling policy.
  link: [48 hours](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-forecast-next-48-hours)
  say: forty-eight hours
ec2-auto-scaling-predictive-forecast-only-mode-first
  claim: When you first enable predictive scaling, it runs in forecast only mode, which forecasts capacity but does not scale the group.
  scope: per predictive scaling policy; default; adjustable.
  link: [forecast only](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-forecast-only-mode-first)
  say: forecast only
ec2-auto-scaling-predictive-forecast-updated-every-6-hours
  claim: The predictive scaling forecast is updated every 6 hours using the latest CloudWatch data.
  scope: per predictive scaling policy.
  link: [every 6 hours](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-forecast-updated-every-6-hours)
  say: every six hours
ec2-auto-scaling-predictive-long-initialization-fit
  claim: Predictive scaling suits regular traffic patterns and applications that take a long time to initialize, because it launches capacity before forecasted load while dynamic scaling is reactive.
  scope: per predictive scaling policy.
  link: [take a long time to initialize](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-long-initialization-fit)
  link: [launching capacity in advance of forecasted load](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-long-initialization-fit)
  link: [which is reactive in nature](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-long-initialization-fit)
ec2-auto-scaling-predictive-max-capacity-breach
  claim: You can let predictive scaling raise the group's maximum capacity automatically when the forecast approaches or exceeds it, using MaxCapacityBreachBehavior and MaxCapacityBuffer.
  scope: per predictive scaling policy.
  link: [MaxCapacityBreachBehavior](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-max-capacity-breach)
  link: [MaxCapacityBuffer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-max-capacity-breach)
  link: [automatically increased](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-max-capacity-breach)
ec2-auto-scaling-predictive-needs-24-hours-of-data
  claim: A predictive scaling policy needs at least 24 hours of metric data before it can start forecasting.
  scope: per predictive scaling policy; minimum; not adjustable.
  link: [at least 24 hours of data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-needs-24-hours-of-data)
  say: at least twenty-four hours of data
ec2-auto-scaling-predictive-new-group-needs-24-hours
  claim: A new Auto Scaling group that replaces an old one needs 24 hours of historical load data before predictive scaling can generate forecasts again.
  scope: per predictive scaling policy.
  link: [24 hours of historical load data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-new-group-needs-24-hours)
  say: twenty-four hours of historical load data
ec2-auto-scaling-predictive-pre-launch-buffer
  claim: Predictive scaling can launch instances earlier than the start of the hour with the SchedulingBufferTime property (Pre-launch instances in the console), so instances have time to boot before forecasted demand.
  scope: per predictive scaling policy.
  link: [SchedulingBufferTime](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-pre-launch-buffer)
  link: [Pre-launch instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-pre-launch-buffer)
  link: [ahead of the forecasted demand](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-pre-launch-buffer)
ec2-auto-scaling-predictive-raised-max-stays
  claim: A maximum capacity that predictive scaling raised does not automatically decrease back to the original maximum.
  scope: per predictive scaling policy.
  link: [does not automatically decrease back](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-raised-max-stays)
  say: does not go back down automatically
ec2-auto-scaling-predictive-scales-at-start-of-hour
  claim: By default, predictive scaling scales the group at the start of each hour based on the forecast for that hour.
  scope: per predictive scaling policy; default; adjustable.
  link: [at the start of each hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-scales-at-start-of-hour)
  say: at the start of each hour
ec2-auto-scaling-predictive-two-full-weeks-best
  claim: Predictive scaling forecasts are more effective when the historical data spans two full weeks.
  scope: per predictive scaling policy.
  link: [two full weeks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-two-full-weeks-best)
  say: two full weeks
ec2-auto-scaling-pricing-page-no-additional-fees
  claim: Amazon EC2 Auto Scaling features have no additional fees beyond the fees for Amazon EC2, CloudWatch (for scaling policies) and the other AWS resources you use.
  scope: per account.
  link: [no additional fees](../facts/ec2-auto-scaling.md#ec2-auto-scaling-pricing-page-no-additional-fees)
  say: no additional fees
ec2-auto-scaling-process-add-to-load-balancer
  claim: The AddToLoadBalancer process adds instances to the attached load balancer target group or Classic Load Balancer when they launch.
  scope: per Auto Scaling group (scaling processes).
  link: [AddToLoadBalancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-add-to-load-balancer)
  link: [Adds instances to the attached load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-add-to-load-balancer)
ec2-auto-scaling-process-alarm-notification
  claim: The AlarmNotification process accepts notifications from the CloudWatch alarms that are associated with the group's dynamic scaling policies.
  scope: per Auto Scaling group (scaling processes).
  link: [AlarmNotification](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-alarm-notification)
  link: [Accepts notifications from CloudWatch alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-alarm-notification)
ec2-auto-scaling-process-az-rebalance
  claim: The AZRebalance process balances the number of instances evenly across the group's Availability Zones when the group becomes unbalanced, for example when an unavailable zone becomes healthy again.
  scope: per Auto Scaling group (scaling processes).
  link: [AZRebalance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-az-rebalance)
  link: [Balances the number of EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-az-rebalance)
ec2-auto-scaling-process-health-check
  claim: The HealthCheck process checks instance health and marks an instance unhealthy when Amazon EC2 or Elastic Load Balancing reports it unhealthy; it can override a health status you set manually.
  scope: per Auto Scaling group (scaling processes).
  link: [HealthCheck](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-health-check)
  link: [marks an instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-health-check)
ec2-auto-scaling-process-launch
  claim: The Launch process adds instances to the group when it scales out or when EC2 Auto Scaling launches instances for other reasons, such as adding instances to a warm pool.
  scope: per Auto Scaling group (scaling processes).
  link: [Adds instances to the Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-launch)
  link: [Launch](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-launch)
ec2-auto-scaling-process-replace-unhealthy
  claim: The ReplaceUnhealthy process terminates instances marked unhealthy and launches new instances to replace them.
  scope: per Auto Scaling group (scaling processes).
  link: [ReplaceUnhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-replace-unhealthy)
  link: [Terminates instances that are marked as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-replace-unhealthy)
ec2-auto-scaling-process-scheduled-actions
  claim: The ScheduledActions process performs scheduled scaling actions, including those created by an AWS Auto Scaling scaling plan with predictive scaling turned on.
  scope: per Auto Scaling group (scaling processes).
  link: [ScheduledActions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-scheduled-actions)
  link: [Performs the scheduled scaling actions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-scheduled-actions)
ec2-auto-scaling-process-terminate
  claim: The Terminate process removes instances when the group scales in or for other reasons, such as exceeding the maximum instance lifetime or failing a health check.
  scope: per Auto Scaling group (scaling processes).
  link: [Removes instances from the Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-terminate)
  link: [failing a health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-terminate)
ec2-auto-scaling-purchase-options-need-launch-template
  claim: You can specify multiple purchase options (On-Demand and Spot) for an Auto Scaling group only when the group uses a launch template.
  scope: per Auto Scaling group.
  link: [only when you use a launch template](../facts/ec2-auto-scaling.md#ec2-auto-scaling-purchase-options-need-launch-template)
  link: [multiple purchase options](../facts/ec2-auto-scaling.md#ec2-auto-scaling-purchase-options-need-launch-template)
ec2-auto-scaling-quota-attach-instances-per-call
  claim: One AttachInstances API call can name at most 20 instance IDs; this limit cannot be changed.
  scope: per AttachInstances API call; maximum; not adjustable.
  link: [20 instance IDs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-attach-instances-per-call)
  say: twenty instance IDs
ec2-auto-scaling-quota-attach-load-balancers-per-call
  claim: One AttachLoadBalancers call can include at most 10 load balancers; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [10 load balancers](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-attach-load-balancers-per-call)
  say: ten load balancers
ec2-auto-scaling-quota-attach-target-groups-per-call
  claim: One AttachLoadBalancerTargetGroups call can include at most 10 target groups; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [10 target groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-attach-target-groups-per-call)
  say: ten target groups
ec2-auto-scaling-quota-batch-delete-scheduled-actions-per-call
  claim: One BatchDeleteScheduledAction call can include at most 50 scheduled actions; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [50 scheduled actions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-batch-delete-scheduled-actions-per-call)
  say: fifty scheduled actions
ec2-auto-scaling-quota-batch-put-scheduled-actions-per-call
  claim: One BatchPutScheduledUpdateGroupAction call can include at most 50 scheduled actions; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [50 scheduled actions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-batch-put-scheduled-actions-per-call)
  say: fifty scheduled actions
ec2-auto-scaling-quota-classic-load-balancers-per-group
  claim: At most 50 Classic Load Balancers may be attached to a single Auto Scaling group, and the number is not adjustable.
  scope: per Auto Scaling group; maximum; not adjustable.
  link: [50 Classic Load Balancers](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-classic-load-balancers-per-group)
  say: fifty Classic Load Balancers
ec2-auto-scaling-quota-detach-instances-per-call
  claim: One DetachInstances call can include at most 20 instance IDs; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [20 instance IDs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-detach-instances-per-call)
  say: twenty instance IDs
ec2-auto-scaling-quota-detach-load-balancers-per-call
  claim: One DetachLoadBalancers call can include at most 10 load balancers; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [10 load balancers](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-detach-load-balancers-per-call)
  say: ten load balancers
ec2-auto-scaling-quota-detach-target-groups-per-call
  claim: One DetachLoadBalancerTargetGroups call can include at most 10 target groups; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [10 target groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-detach-target-groups-per-call)
  say: ten target groups
ec2-auto-scaling-quota-enter-standby-per-call
  claim: One EnterStandby call can include at most 20 instance IDs; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [20 instance IDs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-enter-standby-per-call)
  say: twenty instance IDs
ec2-auto-scaling-quota-exit-standby-per-call
  claim: One ExitStandby call can include at most 20 instance IDs; this limit cannot be changed.
  scope: per API call; maximum; not adjustable.
  link: [20 instance IDs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-exit-standby-per-call)
  say: twenty instance IDs
ec2-auto-scaling-quota-groups-per-region
  claim: An account can have 500 Auto Scaling groups per Region by default.
  scope: per Region, per account; default; adjustable.
  link: [500 Auto Scaling groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-groups-per-region)
  say: five hundred Auto Scaling groups
ec2-auto-scaling-quota-launch-configurations-per-region
  claim: An account can have 200 launch configurations per Region by default.
  scope: per Region, per account; default; adjustable.
  link: [200 launch configurations](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-launch-configurations-per-region)
  say: two hundred launch configurations
ec2-auto-scaling-quota-lifecycle-hooks-per-group
  claim: A fixed quota allows 50 lifecycle hooks on each Auto Scaling group.
  scope: per Auto Scaling group; maximum; not adjustable.
  link: [50 lifecycle hooks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-lifecycle-hooks-per-group)
  say: fifty lifecycle hooks
ec2-auto-scaling-quota-scaling-policies-per-group
  claim: An Auto Scaling group can have 50 scaling policies; this quota cannot be changed.
  scope: per Auto Scaling group; maximum; not adjustable.
  link: [50 scaling policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-scaling-policies-per-group)
  say: fifty scaling policies
ec2-auto-scaling-quota-scheduled-actions-per-group
  claim: An Auto Scaling group can have 125 scheduled actions; this quota cannot be changed.
  scope: per Auto Scaling group; maximum; not adjustable.
  link: [125 scheduled actions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-scheduled-actions-per-group)
  say: one hundred twenty-five scheduled actions
ec2-auto-scaling-quota-set-instance-protection-per-call
  claim: SetInstanceProtection accepts up to 50 instance IDs in a single API request, a limit that is fixed.
  scope: per SetInstanceProtection API call; maximum; not adjustable.
  link: [50 instance IDs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-set-instance-protection-per-call)
  say: fifty instance IDs
ec2-auto-scaling-quota-sns-topics-per-group
  claim: Notifications from one Auto Scaling group go to no more than 10 SNS topics, a fixed quota.
  scope: per Auto Scaling group; maximum; not adjustable.
  link: [10 SNS topics](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-sns-topics-per-group)
  say: ten SNS topics
ec2-auto-scaling-quota-step-adjustments-per-policy
  claim: Each step scaling policy holds up to 20 step adjustments, and this quota is not adjustable.
  scope: per step scaling policy; maximum; not adjustable.
  link: [20 step adjustments](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-step-adjustments-per-policy)
  say: twenty step adjustments
ec2-auto-scaling-quota-target-groups-per-group
  claim: A fixed cap allows 50 Elastic Load Balancing target groups on one Auto Scaling group.
  scope: per Auto Scaling group; maximum; not adjustable.
  link: [50 Elastic Load Balancing target groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-target-groups-per-group)
  say: fifty target groups
ec2-auto-scaling-quota-vpc-lattice-target-groups-per-group
  claim: One Auto Scaling group takes at most 5 VPC Lattice target groups; the quota is fixed.
  scope: per Auto Scaling group; maximum; not adjustable.
  link: [5 VPC Lattice target groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-vpc-lattice-target-groups-per-group)
  say: five VPC Lattice target groups
ec2-auto-scaling-rebalance-exceed-max-margin
  claim: During a rebalancing activity the group can temporarily exceed its maximum capacity, by default by 10 percent or one instance, whichever is greater; the margin is extended only if the group is at or near maximum capacity and needs rebalancing, and the extension lasts only as long as needed to rebalance (typically a few minutes).
  scope: per Auto Scaling group, during a rebalancing activity; default; adjustable; only if the group is at or near maximum capacity and needs rebalancing.
  link: [10 percent or one instance, whichever is greater](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-exceed-max-margin)
  link: [temporarily exceed the specified maximum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-exceed-max-margin)
ec2-auto-scaling-rebalance-launch-before-terminate
  claim: When rebalancing Availability Zones, EC2 Auto Scaling launches new instances before it terminates the old ones, so rebalancing does not reduce availability.
  scope: per Auto Scaling group across Availability Zones.
  link: [launches new instances before terminating the earlier ones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-launch-before-terminate)
  link: [rebalancing does not compromise the performance or availability](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-launch-before-terminate)
ec2-auto-scaling-rebalance-on-az-change
  claim: When you change the group's Availability Zones, EC2 Auto Scaling rebalances the group, which replaces and redistributes some instances.
  scope: per Auto Scaling group across Availability Zones.
  link: [rebalances your group when you change Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-on-az-change)
  link: [replacing and redistributing some instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-on-az-change)
ec2-auto-scaling-rebalance-triggers
  claim: A group can become unbalanced and Availability Zone rebalancing can follow when you change its Availability Zones, when you explicitly terminate or detach instances or place them in standby, when a zone that lacked capacity recovers, or when a zone's Spot price falls from above to below your maximum price.
  scope: per Auto Scaling group across Availability Zones.
  link: [You change the Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-triggers)
  link: [explicitly terminate or detach instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-rebalance-triggers)
ec2-auto-scaling-registers-with-lb-before-inservice
  claim: When the group receives traffic from an Elastic Load Balancing load balancer, EC2 Auto Scaling registers a new instance with the load balancer before marking it InService.
  scope: per Auto Scaling group with a load balancer.
  link: [before it marks the instance as](../facts/ec2-auto-scaling.md#ec2-auto-scaling-registers-with-lb-before-inservice)
  link: [registers your instance with the load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-registers-with-lb-before-inservice)
ec2-auto-scaling-replace-root-volume-preserves
  claim: Root volume replacement updates an instance by swapping only its root EBS volume while it keeps running, preserving network interfaces and IP addresses, non-root EBS volumes, instance store data, security groups and IAM roles.
  scope: per instance refresh with the replace root volume strategy.
  link: [replacing only the root EBS volume](../facts/ec2-auto-scaling.md#ec2-auto-scaling-replace-root-volume-preserves)
  link: [Network interfaces and IP addresses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-replace-root-volume-preserves)
ec2-auto-scaling-replace-root-volume-requirements
  claim: The replace root volume strategy requires a mixed instances policy whose overrides each specify an ImageId and AMIs that contain only a single root volume, and root volume replacement does not support Elastic Load Balancing.
  scope: per instance refresh with the replace root volume strategy.
  link: [must use a mixed instances policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-replace-root-volume-requirements)
  link: [Root volume replacement doesn’t support Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-replace-root-volume-requirements)
ec2-auto-scaling-require-imdsv2-launch-template
  claim: For extra security, you can set your users' permissions to require the use of a launch template that requires IMDSv2.
  scope: per launch template used by an Auto Scaling group.
  link: [a launch template that requires IMDSv2](../facts/ec2-auto-scaling.md#ec2-auto-scaling-require-imdsv2-launch-template)
ec2-auto-scaling-resilience-practices
  claim: AWS recommends spanning the group across multiple Availability Zones, keeping at least one instance in each zone, and attaching a load balancer across the same zones.
  scope: per Auto Scaling group across Availability Zones.
  link: [across multiple Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-resilience-practices)
  link: [at least one instance in each Availability Zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-resilience-practices)
ec2-auto-scaling-retained-instances-charged-and-replaced
  claim: A retained instance still incurs standard EC2 charges, does not count toward desired capacity (so the group launches a replacement), and must be terminated manually with TerminateInstanceInAutoScalingGroup.
  scope: per Auto Scaling group with an instance lifecycle policy.
  link: [continue to incur standard Amazon EC2 charges](../facts/ec2-auto-scaling.md#ec2-auto-scaling-retained-instances-charged-and-replaced)
  link: [launches replacement instances to maintain the desired size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-retained-instances-charged-and-replaced)
ec2-auto-scaling-root-volume-replacement-keeps-instance-running
  claim: Since November 20, 2025, an instance refresh can use the ReplaceRootVolume strategy: it replaces only the root EBS volume while the instance keeps running, so no new instance is launched and network interfaces, IP addresses, non-root volumes, security groups and IAM roles are preserved.
  scope: per instance refresh with the replace root volume strategy.
  link: [replacing only the root EBS volume](../facts/ec2-auto-scaling.md#ec2-auto-scaling-root-volume-replacement-keeps-instance-running)
  link: [November 20, 2025](../facts/ec2-auto-scaling.md#ec2-auto-scaling-root-volume-replacement-keeps-instance-running)
ec2-auto-scaling-root-volume-replacement-limits
  claim: Replace Root Volume cannot be used when the group or the desired configuration uses the $Latest or $Default launch template version, or when the group has a warm pool; if the replacement fails on an instance, the instance is terminated and replaced.
  scope: per instance refresh with the ReplaceRootVolume strategy.
  link: [uses the `$Latest` or `$Default` launch template version](../facts/ec2-auto-scaling.md#ec2-auto-scaling-root-volume-replacement-limits)
  link: [has a warm pool](../facts/ec2-auto-scaling.md#ec2-auto-scaling-root-volume-replacement-limits)
  link: [marks that instance for termination](../facts/ec2-auto-scaling.md#ec2-auto-scaling-root-volume-replacement-limits)
ec2-auto-scaling-scale-in-protection-all-protected
  claim: If every instance in the group is protected from scale in when a scale-in event occurs, the desired capacity is still decremented, but the group cannot terminate instances until their protection is removed.
  scope: per instance with scale-in protection.
  link: [its desired capacity is decremented](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-all-protected)
  link: [can't terminate the required number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-all-protected)
ec2-auto-scaling-scale-in-protection-ec2-termination-protection-for-manual
  claim: Scale-in protection does not stop manual termination through the EC2 console, CLI or API; to protect group instances from manual termination, enable EC2 termination protection.
  scope: per instance with scale-in protection.
  link: [enable Amazon EC2 termination protection](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-ec2-termination-protection-for-manual)
  link: [To protect Auto Scaling instances from manual termination](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-ec2-termination-protection-for-manual)
ec2-auto-scaling-scale-in-protection-group-setting-new-only
  claim: When you enable the group's scale-in protection setting, all new instances launched by the group have scale-in protection; enabling or disabling the setting does not affect existing instances.
  scope: per Auto Scaling group (scale-in protection setting).
  link: [does not affect existing instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-group-setting-new-only)
ec2-auto-scaling-scale-in-protection-lost-on-detach
  claim: Detaching a protected instance loses its scale-in protection setting; when it is attached again it inherits the group's current setting.
  scope: per instance with scale-in protection.
  link: [instance scale in protection setting is lost](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-lost-on-detach)
  link: [inherits the current instance scale in protection setting](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-lost-on-detach)
ec2-auto-scaling-scale-in-protection-not-health-replacement
  claim: Instance scale-in protection does not protect an instance from health check replacement when it fails health checks.
  scope: per instance with scale-in protection.
  link: [Health check replacement](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-not-health-replacement)
  link: [does not protect Auto Scaling instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-not-health-replacement)
ec2-auto-scaling-scale-in-protection-off-by-default
  claim: Instance scale-in protection is disabled by default when you create an Auto Scaling group, so EC2 Auto Scaling can terminate any instance in the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [instance scale-in protection is disabled](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-off-by-default)
  link: [can terminate any instance in the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-off-by-default)
ec2-auto-scaling-scaling-methods
  claim: EC2 Auto Scaling can scale by schedule, as a function of date and time; dynamically, with a scaling policy that resizes the group to meet changes in demand; and predictively, combined with dynamic scaling, to add instances in advance of daily and weekly traffic patterns.
  scope: per Auto Scaling group.
  link: [as a function of date and time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-methods)
  link: [dynamically resizes your Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-methods)
  link: [combine predictive scaling and dynamic scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-methods)
ec2-auto-scaling-scaling-policies-capped-at-max-capacity
  claim: By default, scaling policies cannot increase capacity above the group's maximum capacity; predictive scaling can optionally raise the maximum when the forecast approaches or exceeds it.
  scope: per Auto Scaling group; default; adjustable.
  link: [cannot increase capacity higher than its maximum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-policies-capped-at-max-capacity)
  say: cannot go above the maximum capacity
ec2-auto-scaling-scaling-policy-adjusts-desired
  claim: A scaling policy changes the group's desired capacity between the minimum and maximum you set, and the group launches or terminates instances to match.
  scope: per Auto Scaling group with a scaling policy.
  link: [adjusts the desired capacity of the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-policy-adjusts-desired)
  link: [launches or terminates the instances as needed](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-policy-adjusts-desired)
ec2-auto-scaling-scheduled-action-keeps-current-limits
  claim: A scheduled action that does not set new minimum and maximum sizes keeps the group's current minimum and maximum limits.
  scope: per scheduled action.
  link: [current minimum and maximum size limits apply](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-keeps-current-limits)
  say: the current limits apply
ec2-auto-scaling-scheduled-action-sets-capacities
  claim: A scheduled action sets the group's desired, minimum and maximum capacity at a specified date and time; you give a new desired capacity and optionally a new minimum and maximum.
  scope: per scheduled action.
  link: [desired, minimum, and maximum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-sets-capacities)
  link: [optionally a new minimum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-sets-capacities)
ec2-auto-scaling-scheduled-dst-location-time-zones
  claim: Location-based time zones such as America/New_York adjust automatically for Daylight Saving Time; a UTC-based time zone such as Etc/UTC does not.
  scope: per scheduled action.
  link: [automatically adjust for DST](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-dst-location-time-zones)
  link: [will not adjust for DST](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-dst-location-time-zones)
ec2-auto-scaling-scheduled-one-time-or-recurring
  claim: Scheduled actions can run one time only or on a recurring schedule described by a cron expression and a time zone.
  scope: per scheduled action.
  link: [scale one time only](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-one-time-or-recurring)
  link: [on a recurring schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-one-time-or-recurring)
  link: [specify a cron expression and a time zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-one-time-or-recurring)
ec2-auto-scaling-scheduled-order-within-group-only
  claim: The order in which scheduled actions run is guaranteed within one group, but not across groups.
  scope: per scheduled action.
  link: [guaranteed within the same group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-order-within-group-only)
  link: [not for scheduled actions across groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-order-within-group-only)
ec2-auto-scaling-scheduled-plus-policies-together
  claim: Scheduled scaling and scaling policies can be used together on one group: after a scheduled action runs, the scaling policy keeps deciding whether to scale further, while capacity must stay within the minimum and maximum set by the scheduled action.
  scope: per Auto Scaling group.
  link: [use scheduled scaling and scaling policies together](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-plus-policies-together)
  link: [must fall within the minimum and maximum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-plus-policies-together)
ec2-auto-scaling-scheduled-suspend-to-turn-off
  claim: You can turn off scheduled scaling temporarily by suspending the ScheduledActions process, without deleting the actions, and resume it later.
  scope: per scheduled action.
  link: [suspending the `ScheduledActions` process](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-suspend-to-turn-off)
  link: [without having to delete them](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-suspend-to-turn-off)
ec2-auto-scaling-scheduled-unique-start-time
  claim: Each scheduled action in a group needs a unique time value; a call that schedules an action at a time already taken is rejected with an error.
  scope: per scheduled action.
  link: [must have a unique time value](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-unique-start-time)
  link: [the call is rejected](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-unique-start-time)
ec2-auto-scaling-scheduled-utc-default-time-zone
  claim: Recurring scheduled actions use UTC by default; you can set a local IANA time zone, and a location-based time zone adjusts automatically for Daylight Saving Time.
  scope: per recurring scheduled action; default; adjustable.
  link: [Coordinated Universal Time (UTC)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-utc-default-time-zone)
  link: [the action automatically adjusts for DST](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-utc-default-time-zone)
ec2-auto-scaling-scheduled-vs-dynamic-when-to-use
  claim: Choose scheduled scaling when you know exactly when capacity must change because demand follows a predictable schedule; choose dynamic scaling when traffic changes at times you cannot predict.
  scope: per Auto Scaling group.
  link: [the need arises on a predictable schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-vs-dynamic-when-to-use)
  link: [you don't know when the traffic will change](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-vs-dynamic-when-to-use)
ec2-auto-scaling-set-instance-health-respects-grace-period
  claim: By default, set-instance-health respects the health check grace period; the --no-should-respect-grace-period option overrides this.
  scope: per set-instance-health call; default; adjustable.
  link: [respects the health check grace period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-set-instance-health-respects-grace-period)
  link: [--no-should-respect-grace-period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-set-instance-health-respects-grace-period)
ec2-auto-scaling-simple-scaling-not-recommended
  claim: AWS recommends as a best practice not to use simple scaling policies and scaling cooldowns; target tracking or step scaling performs better.
  scope: per simple scaling policy.
  link: [do not use simple scaling policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-simple-scaling-not-recommended)
  say: do not use simple scaling policies
ec2-auto-scaling-simple-scaling-paused-by-hooks
  claim: When lifecycle hooks run, simple scaling activities are usually paused until the lifecycle actions finish and the cooldown expires; AWS recommends step or target tracking scaling instead of simple scaling.
  scope: per simple scaling policy.
  link: [paused until the lifecycle actions have completed](../facts/ec2-auto-scaling.md#ec2-auto-scaling-simple-scaling-paused-by-hooks)
  link: [recommend against using simple scaling policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-simple-scaling-paused-by-hooks)
ec2-auto-scaling-simple-single-adjustment-cooldown
  claim: Simple scaling policies are like step scaling policies but use a single scaling adjustment, with a cooldown period between scaling activities.
  scope: per simple scaling policy.
  link: [based on a single scaling adjustment](../facts/ec2-auto-scaling.md#ec2-auto-scaling-simple-single-adjustment-cooldown)
  link: [with a cooldown period between each scaling activity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-simple-single-adjustment-cooldown)
ec2-auto-scaling-slr-created-on-first-group
  claim: Amazon EC2 Auto Scaling calls other AWS services through a service-linked role named AWSServiceRoleForAutoScaling, which it creates the first time you create an Auto Scaling group unless you create and specify a custom suffix role.
  scope: per account; unless a custom suffix service-linked role is specified.
  link: [AWSServiceRoleForAutoScaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-slr-created-on-first-group)
ec2-auto-scaling-slr-no-customer-managed-key-access
  claim: The EC2 Auto Scaling service-linked role can use AWS managed keys but has no access to customer managed KMS keys; to launch instances with EBS volumes encrypted by a customer managed key, you must set up the key policy to allow the role.
  scope: per account (service-linked role); EBS encryption with a customer managed key.
  link: [do not include access](../facts/ec2-auto-scaling.md#ec2-auto-scaling-slr-no-customer-managed-key-access)
  link: [set up the key policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-slr-no-customer-managed-key-access)
ec2-auto-scaling-slr-only-linked-service-assumes
  claim: A service-linked role is a secure way to delegate permissions because only the linked service can assume it, and it makes the API calls the service makes for you visible in AWS CloudTrail.
  scope: per account (service-linked role).
  link: [only the linked service can assume](../facts/ec2-auto-scaling.md#ec2-auto-scaling-slr-only-linked-service-assumes)
ec2-auto-scaling-sns-four-event-types
  claim: Amazon SNS notifications cover four events: EC2_INSTANCE_LAUNCH, EC2_INSTANCE_LAUNCH_ERROR, EC2_INSTANCE_TERMINATE and EC2_INSTANCE_TERMINATE_ERROR.
  scope: per Auto Scaling group (notifications).
  link: [autoscaling:EC2_INSTANCE_LAUNCH](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sns-four-event-types)
  link: [autoscaling:EC2_INSTANCE_LAUNCH_ERROR](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sns-four-event-types)
  link: [autoscaling:EC2_INSTANCE_TERMINATE](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sns-four-event-types)
  link: [autoscaling:EC2_INSTANCE_TERMINATE_ERROR](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sns-four-event-types)
ec2-auto-scaling-sns-one-per-instance-best-effort
  claim: SNS notifications are sent one per instance added or removed, on a best-effort basis; an instance can still fail after its first notification.
  scope: per Auto Scaling group (notifications).
  link: [one notification sent per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sns-one-per-instance-best-effort)
  link: [on a best-effort basis](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sns-one-per-instance-best-effort)
ec2-auto-scaling-spot-capacity-optimized-pools
  claim: The capacity-optimized Spot allocation strategy launches into the pools with the most available capacity, using real-time capacity data, to reduce interruptions for workloads where restarting is expensive.
  scope: per Auto Scaling group with Spot Instances.
  link: [capacity-optimized](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-capacity-optimized-pools)
  link: [most available pools](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-capacity-optimized-pools)
ec2-auto-scaling-spot-interruption-bypasses-all-protection
  claim: Amazon EC2 can interrupt Spot Instances and interruptible capacity reservations in a group at any time, and these interruptions bypass every EC2 Auto Scaling protection mechanism.
  scope: per Auto Scaling group with Spot Instances.
  link: [bypass all Amazon EC2 Auto Scaling protection mechanisms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-interruption-bypasses-all-protection)
  link: [can interrupt and reclaim your instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-interruption-bypasses-all-protection)
ec2-auto-scaling-spot-lowest-price-not-recommended
  claim: AWS does not recommend the lowest-price Spot allocation strategy because it has the highest risk of interruption, and it is only available from the AWS CLI.
  scope: Spot allocation strategy of a mixed instances group.
  link: [lowest-price](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-lowest-price-not-recommended)
  link: [highest risk of interruption](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-lowest-price-not-recommended)
  link: [only available when using the AWS CLI](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-lowest-price-not-recommended)
ec2-auto-scaling-spot-price-capacity-optimized-recommended
  claim: For Spot Instances in a mixed instances group, AWS recommends the price-capacity-optimized allocation strategy: it chooses the Spot pools that are least likely to be interrupted and have the lowest possible price.
  scope: per Auto Scaling group with Spot Instances.
  link: [price and capacity optimized allocation strategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-price-capacity-optimized-recommended)
  link: [least likely to be interrupted](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-price-capacity-optimized-recommended)
ec2-auto-scaling-spot-rebalance-recommendation-and-two-minute-notice
  claim: Before interrupting a Spot Instance, Amazon EC2 always gives both an instance rebalance recommendation and a two-minute interruption notice.
  scope: per Auto Scaling group with Spot Instances.
  link: [Spot two-minute instance interruption notice](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-rebalance-recommendation-and-two-minute-notice)
  say: two-minute interruption notice
ec2-auto-scaling-spot-terminated-replacement
  claim: When a Spot Instance in the group is terminated, the Auto Scaling group attempts to launch a replacement to keep the desired capacity.
  scope: per Auto Scaling group with Spot Instances.
  link: [attempts to launch a replacement instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-terminated-replacement)
  link: [Spot Instance is terminated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-terminated-replacement)
ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target
  claim: For queue workers, the target tracking target is the acceptable backlog per instance: the acceptable latency divided by the average time one instance needs to process a message; for example 10 seconds of latency and 0.1 seconds per message give a target of 100 messages.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [divide it by the average time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target)
  link: [10 / 0.1, which equals 100 messages](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target)
ec2-auto-scaling-sqs-backlog-per-instance
  claim: Backlog per instance is the queue length (ApproximateNumberOfMessages) divided by the number of InService instances; the target tracking target is the acceptable backlog per instance.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [Divide that number by the fleet's running capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [acceptable backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
ec2-auto-scaling-sqs-backlog-per-instance-metric-math
  claim: The SQS backlog per instance is the approximate number of visible messages in the queue divided by the group's running capacity (the InService instances); with metric math this is ApproximateNumberOfMessagesVisible divided by GroupInServiceInstances, and a target tracking policy keeps it at the target value.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [ApproximateNumberOfMessagesVisible](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance-metric-math)
  link: [GroupInServiceInstances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance-metric-math)
ec2-auto-scaling-sqs-dynamic-scaling-when-load-varies
  claim: In the AWS example of an Auto Scaling group that processes images from an SQS queue, a fixed-size group works if the upload rate does not vary; if the number of uploads changes over time, AWS suggests dynamic scaling of the group.
  scope: per Auto Scaling group that processes an SQS queue; the number of uploads changes over time.
  link: [you might consider using dynamic scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-dynamic-scaling-when-load-varies)
ec2-auto-scaling-sqs-metric-math-instead-of-custom
  claim: Instead of publishing a custom backlog-per-instance metric, you can calculate it with CloudWatch metric math (the approximate number of messages available for retrieval divided by the number of InService instances), which saves the cost and effort of publishing your own metric.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [save the cost and effort](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-metric-math-instead-of-custom)
  link: [metric math](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-metric-math-instead-of-custom)
ec2-auto-scaling-sqs-queue-length-not-proportional
  claim: The issue with target tracking on ApproximateNumberOfMessagesVisible is that the number of messages in the queue might not change proportionally to the size of the group that processes them.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [might not change proportionally](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-queue-length-not-proportional)
  link: [ApproximateNumberOfMessagesVisible](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-queue-length-not-proportional)
ec2-auto-scaling-sqs-unprocessed-messages-return
  claim: Messages not yet processed when a worker instance is terminated return to the SQS queue for another instance; scale-in protection can keep long-running workers from being terminated.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [returned to the SQS queue](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-unprocessed-messages-return)
  link: [use instance scale-in protection](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-unprocessed-messages-return)
ec2-auto-scaling-ssm-parameter-api-cost
  claim: Auto Scaling resolves the Systems Manager parameter on each create or update call for the group; with advanced parameters or higher throughput limits, these GetParameters calls can raise Systems Manager cost, which is charged per Parameter Store API interaction.
  scope: per launch template used by an Auto Scaling group; advanced parameters or higher throughput limits.
  link: [charges are incurred per Parameter Store API interaction](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-api-cost)
ec2-auto-scaling-ssm-parameter-for-ami
  claim: A launch template can reference an AMI through a Systems Manager parameter, so the group picks up new AMI IDs without new launch templates or new template versions.
  scope: per launch template used by an Auto Scaling group.
  link: [use new AMI IDs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-for-ami)
  link: [Systems Manager parameters](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-for-ami)
ec2-auto-scaling-ssm-parameter-needs-getparameters
  claim: To specify a Parameter Store parameter in a launch template you need ssm:GetParameters on that parameter, and anyone who uses the launch template also needs it so the value can be validated.
  scope: per launch template used by an Auto Scaling group.
  link: [ssm:GetParameters](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-needs-getparameters)
ec2-auto-scaling-ssm-parameter-no-warm-pools
  claim: If an Auto Scaling group uses a launch template that specifies a Systems Manager parameter for the AMI, warm pools are not supported, and you cannot start an instance refresh with a desired configuration or skip matching.
  scope: per Auto Scaling group; launch template specifies a Systems Manager parameter.
  link: [warm pools are not supported](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-no-warm-pools)
ec2-auto-scaling-ssm-parameter-sources
  claim: The AMI parameter in a launch template can be a parameter in your own account, a parameter shared from another account, or an AWS public parameter for a public AMI.
  scope: per launch template used by an Auto Scaling group.
  link: [a parameter shared from another AWS account](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-sources)
  link: [a public parameter for a public AMI](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-sources)
ec2-auto-scaling-standby-billed
  claim: You are billed for instances that are in a standby state.
  scope: per instance in Standby.
  link: [You are billed for instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-billed)
  link: [standby state](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-billed)
ec2-auto-scaling-standby-decrement-choice
  claim: When you put an instance on standby you choose whether to decrement desired capacity; if you do not, EC2 Auto Scaling launches a replacement instance, and if you do, no replacement is launched.
  scope: per instance in Standby.
  link: [launches an instance to replace the one](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-decrement-choice)
  link: [prevents the launch of an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-decrement-choice)
ec2-auto-scaling-standby-deregistration-delay-default
  claim: When an instance enters standby and connection draining is enabled on the load balancer, Elastic Load Balancing waits 300 seconds by default before it completes deregistration.
  scope: per load balancer (deregistration delay); default; adjustable; connection draining is enabled.
  link: [300 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-deregistration-delay-default)
  say: three hundred seconds
ec2-auto-scaling-standby-no-health-checks
  claim: EC2 Auto Scaling does not perform health checks on an instance in Standby; its health status stays what it was before standby until you return it to service.
  scope: per instance in Standby.
  link: [does not perform health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-health-checks)
  link: [health status reflects the status](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-health-checks)
ec2-auto-scaling-standby-no-lb-traffic
  claim: A Standby instance remains part of the group but does not handle load balancer traffic, and the group will not terminate it through health checks or scale-in events.
  scope: per instance in Standby.
  link: [do not actively handle load balancer traffic](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-lb-traffic)
  link: [during scale-in events](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-lb-traffic)
ec2-auto-scaling-standby-preferred-over-detach
  claim: To take an instance out of a group temporarily, AWS recommends the standby procedure rather than detaching and re-attaching it to the same group.
  scope: per instance in Standby.
  link: [recommend using the standby procedure](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-preferred-over-detach)
  link: [Instead of detaching and re-attaching an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-preferred-over-detach)
ec2-auto-scaling-standby-still-managed
  claim: An instance in Standby is still managed by the Auto Scaling group but is not an active part of the application until you return it to service.
  scope: per instance in Standby.
  link: [continue to be managed](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-still-managed)
  link: [not an active part of your application](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-still-managed)
ec2-auto-scaling-stateful-drain-or-transfer
  claim: To shut down a stateful instance gracefully, its workload should be drained (finish its assigned jobs) or transferred to another active instance.
  scope: per stateful instance.
  link: [either drained (completing all currently assigned jobs)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-stateful-drain-or-transfer)
  link: [transferred (moving jobs, data, or configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-stateful-drain-or-transfer)
ec2-auto-scaling-status-check-failure-waits-few-minutes
  claim: When a status check fails, Amazon EC2 Auto Scaling waits a few minutes for AWS to fix the issue.
  scope: per Auto Scaling group (health checks).
  link: [waits a few minutes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-status-check-failure-waits-few-minutes)
  say: waits a few minutes
ec2-auto-scaling-step-adjustment-types
  claim: Step and simple scaling support three adjustment types: ChangeInCapacity, ExactCapacity and PercentChangeInCapacity.
  scope: per step scaling policy.
  link: [ChangeInCapacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-adjustment-types)
  link: [ExactCapacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-adjustment-types)
  link: [PercentChangeInCapacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-adjustment-types)
ec2-auto-scaling-step-bounds-console-absolute-cli-relative
  claim: Step adjustment bounds are absolute values in the console but relative to the breach threshold in the AWS CLI or an SDK.
  scope: per step scaling policy.
  link: [as absolute values](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-bounds-console-absolute-cli-relative)
  link: [relative to the breach threshold](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-bounds-console-absolute-cli-relative)
  say: as absolute values | relative to the breach threshold
ec2-auto-scaling-step-continues-until-ok
  claim: A step scaling policy applies its step adjustments when the alarm is breached for the set number of evaluation periods, and the adjustments can continue for further breaches until the alarm returns to OK.
  scope: per step scaling policy.
  link: [can continue for additional alarm breaches](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-continues-until-ok)
  link: [until the alarm state returns to](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-continues-until-ok)
ec2-auto-scaling-step-flapping-margin
  claim: Leave an adequate margin between the scale-out and scale-in thresholds to prevent flapping, an infinite loop of scaling in and scaling out.
  scope: per step scaling policy.
  link: [to prevent flapping](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-flapping-margin)
  link: [infinite loop of scaling in and scaling out](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-flapping-margin)
ec2-auto-scaling-step-percent-rounding
  claim: With PercentChangeInCapacity, a result greater than 1 is rounded down, and a result between 0 and 1 is rounded to 1.
  scope: per step scaling policy.
  link: [rounded down](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-percent-rounding)
  link: [rounded to 1](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-percent-rounding)
  say: rounded down | rounded to one
ec2-auto-scaling-step-ranges-no-overlap-or-gap
  claim: The ranges of the step adjustments in a step scaling policy cannot overlap or leave a gap.
  scope: per step scaling policy.
  link: [can't overlap or have a gap](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-ranges-no-overlap-or-gap)
  say: can't overlap or have a gap
ec2-auto-scaling-step-simple-you-manage-alarms
  claim: With step scaling and simple scaling, you create and manage the CloudWatch alarms that start scaling.
  scope: per step scaling policy.
  link: [you create and manage the CloudWatch alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-simple-you-manage-alarms)
ec2-auto-scaling-step-warmup-single-activity
  claim: During step scaling, instances still warming up count toward desired capacity for the next scale-out, so several alarm breaches in the range of the same step adjustment produce a single scaling activity.
  scope: per step scaling policy.
  link: [result in a single scaling activity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-warmup-single-activity)
  link: [counted as part of the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-warmup-single-activity)
ec2-auto-scaling-suspend-processes-purpose
  claim: Suspending processes lets you investigate or troubleshoot without interference from scaling policies or scheduled actions, and stops EC2 Auto Scaling from marking instances unhealthy and replacing them while you change the group.
  scope: per Auto Scaling group (scaling processes).
  link: [investigate or troubleshoot an issue without interference](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
  link: [marking instances unhealthy and replacing them](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
ec2-auto-scaling-suspend-terminate-full-control
  claim: Suspending the Terminate process stops Auto Scaling from attempting any terminations, except a user request through TerminateInstanceInAutoScalingGroup; AWS recommends it only when other options do not give enough control.
  scope: per Auto Scaling group during scale in.
  link: [complete control over all EC2 instance terminations](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-terminate-full-control)
  link: [We only recommend using this option](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-terminate-full-control)
ec2-auto-scaling-synchronous-provisioning-launchinstances
  claim: Since November 18, 2025, the LaunchInstances API lets you request a specific number of instances in one Availability Zone synchronously and get immediate feedback on capacity, instead of waiting for asynchronous scaling.
  scope: per LaunchInstances API call.
  link: [LaunchInstances API](../facts/ec2-auto-scaling.md#ec2-auto-scaling-synchronous-provisioning-launchinstances)
  link: [November 18, 2025](../facts/ec2-auto-scaling.md#ec2-auto-scaling-synchronous-provisioning-launchinstances)
ec2-auto-scaling-target-tracking-alb-resource-label
  claim: To use the ALBRequestCountPerTarget metric you must specify the ResourceLabel parameter, which identifies the load balancer target group of the metric.
  scope: per target tracking scaling policy.
  link: [ResourceLabel](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-alb-resource-label)
  link: [identify the load balancer target group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-alb-resource-label)
ec2-auto-scaling-target-tracking-conservative-rounding
  claim: Target tracking rounds conservatively when it decides how many instances to add or remove, so the metric can sit some distance from the target value, most visibly in small groups.
  scope: per target tracking scaling policy.
  link: [rounding up or down](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-conservative-rounding)
  link: [act conservatively](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-conservative-rounding)
ec2-auto-scaling-target-tracking-creates-two-alarms
  claim: Amazon EC2 Auto Scaling creates and manages the CloudWatch alarms of a target tracking policy; in the AWS SQS walkthrough, creating the policy creates two alarms: one for scaling out and one for scaling in.
  scope: per target tracking scaling policy (AWS SQS CLI example).
  link: [two alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-creates-two-alarms)
  link: [one for scaling in](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-creates-two-alarms)
  say: two alarms
ec2-auto-scaling-target-tracking-disable-scale-in
  claim: You can temporarily disable the scale-in portion of a target tracking policy, for example to keep a minimum number of instances during deployments.
  scope: per target tracking scaling policy.
  link: [disable the scale-in portion](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-disable-scale-in)
  link: [successful deployments](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-disable-scale-in)
ec2-auto-scaling-target-tracking-do-not-edit-alarms
  claim: You should not create, edit or delete the CloudWatch alarms of a target tracking policy; EC2 Auto Scaling manages them and can edit, replace or delete them.
  scope: per target tracking scaling policy.
  link: [Do not create, edit, or delete](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-do-not-edit-alarms)
ec2-auto-scaling-target-tracking-insufficient-data-no-scaling
  claim: When the target tracking metric is missing data points, the alarm goes to INSUFFICIENT_DATA and EC2 Auto Scaling cannot scale the group until new data points arrive.
  scope: per target tracking scaling policy.
  link: [cannot scale your group until new data points](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-insufficient-data-no-scaling)
  link: [INSUFFICIENT_DATA](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-insufficient-data-no-scaling)
ec2-auto-scaling-target-tracking-metric-math-current
  claim: A target tracking policy can track one CloudWatch metric or a metric math expression over several metrics that produces one time series.
  scope: per target tracking scaling policy.
  link: [create new single time series](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-metric-math-current)
ec2-auto-scaling-target-tracking-metric-must-fall-as-capacity-grows
  claim: Target tracking assumes the metric is inversely proportional to group capacity (when capacity increases, the metric should decrease by nearly the same proportion), so converting metrics is essential; metric math is particularly useful to convert existing metrics into average per-instance values.
  scope: per target tracking scaling policy.
  link: [inversely proportional to the capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-metric-must-fall-as-capacity-grows)
  link: [convert existing metrics into average per-instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-metric-must-fall-as-capacity-grows)
ec2-auto-scaling-target-tracking-multiple-policies-different-metrics
  claim: A group can use several target tracking policies together, provided each one uses a different metric.
  scope: per target tracking scaling policy.
  link: [each of them uses a different metric](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-multiple-policies-different-metrics)
ec2-auto-scaling-target-tracking-no-manual-alarms
  claim: Target tracking policies remove the need to define CloudWatch alarms and scaling adjustments by hand; EC2 Auto Scaling handles them from the target you set.
  scope: per target tracking scaling policy.
  link: [remove the need to manually define CloudWatch alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-no-manual-alarms)
ec2-auto-scaling-target-tracking-no-scale-out-below-target
  claim: A target tracking policy cannot scale out the group when the metric is below the target value.
  scope: per target tracking scaling policy.
  link: [metric is below the target value](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-no-scale-out-below-target)
  say: metric below the target value
ec2-auto-scaling-target-tracking-out-any-in-all
  claim: With several target tracking policies, the group scales out if any policy is ready to scale out, and scales in only if all policies with scale in enabled are ready to scale in.
  scope: per target tracking scaling policy.
  link: [any of the target tracking policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-out-any-in-all)
  link: [all of the target tracking policies](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-out-any-in-all)
  say: any of the policies | all of the policies
ec2-auto-scaling-target-tracking-predefined-metrics
  claim: Target tracking offers four predefined metrics: ASGAverageCPUUtilization, ASGAverageNetworkIn, ASGAverageNetworkOut and ALBRequestCountPerTarget; you can also use custom CloudWatch metrics.
  scope: per target tracking scaling policy.
  link: [ASGAverageCPUUtilization](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [ASGAverageNetworkIn](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [ASGAverageNetworkOut](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [ALBRequestCountPerTarget](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [either predefined metrics or custom metrics](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
ec2-auto-scaling-target-tracking-scale-in-gradual
  claim: A target tracking policy prioritizes availability by scaling in more gradually when traffic decreases; a step scaling policy gives more control.
  scope: per target tracking scaling policy.
  link: [scaling in more gradually when traffic is decreasing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-scale-in-gradual)
  link: [prioritizes availability](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-scale-in-gradual)
ec2-auto-scaling-target-tracking-scale-to-zero-needs-min-zero
  claim: For a group to scale in to 0 when no requests arrive, its minimum capacity must be set to 0.
  scope: per target tracking scaling policy.
  link: [minimum capacity must be set to 0](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-scale-to-zero-needs-min-zero)
  say: minimum capacity set to zero
ec2-auto-scaling-target-tracking-service-manages-alarms
  claim: With a target tracking policy, EC2 Auto Scaling creates and manages the CloudWatch alarms that start scaling when the metric moves away from the target.
  scope: per target tracking scaling policy.
  link: [creates and manages the CloudWatch alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-service-manages-alarms)
  link: [when the metric deviates from the target](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-service-manages-alarms)
ec2-auto-scaling-target-tracking-target-value-high-with-buffer
  claim: To use resources cost-efficiently, set the target value as high as possible while keeping a reasonable buffer for unexpected traffic increases.
  scope: per target tracking scaling policy.
  link: [set the target value as high as possible](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-target-value-high-with-buffer)
  link: [reasonable buffer for unexpected traffic increases](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-target-value-high-with-buffer)
ec2-auto-scaling-target-tracking-throughput-per-instance-minute
  claim: For a throughput metric such as ALB request count per target, the target value is the best average throughput of one instance over a one-minute period.
  scope: per target tracking scaling policy.
  link: [for a one-minute period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-throughput-per-instance-minute)
  say: for a one-minute period
ec2-auto-scaling-target-tracking-unsuitable-metrics
  claim: The load balancer RequestCount and Latency metrics do not work for target tracking: the number of requests doesn't change based on the group's utilization, and latency can increase with utilization but doesn't necessarily change proportionally.
  scope: per target tracking scaling policy.
  link: [do not work for target tracking](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-unsuitable-metrics)
  link: [doesn't change based on the utilization](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-unsuitable-metrics)
  link: [doesn't necessarily change proportionally](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-unsuitable-metrics)
ec2-auto-scaling-terminate-hook-states
  claim: With an EC2_INSTANCE_TERMINATING lifecycle hook, an instance moves from Terminating to Terminating:Wait, then to Terminating:Proceed after you complete the lifecycle action, and then to Terminated.
  scope: per instance with a termination lifecycle hook.
  link: [Terminating:Wait](../facts/ec2-auto-scaling.md#ec2-auto-scaling-terminate-hook-states)
  link: [Terminating:Proceed](../facts/ec2-auto-scaling.md#ec2-auto-scaling-terminate-hook-states)
  link: [EC2_INSTANCE_TERMINATING](../facts/ec2-auto-scaling.md#ec2-auto-scaling-terminate-hook-states)
ec2-auto-scaling-terminating-cannot-return
  claim: An instance in the Terminating state cannot be put back into service; the group chose it with its termination policy.
  scope: per terminating instance.
  link: [can't be put back into service](../facts/ec2-auto-scaling.md#ec2-auto-scaling-terminating-cannot-return)
  link: [uses its termination policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-terminating-cannot-return)
ec2-auto-scaling-termination-az-balance-first
  claim: EC2 Auto Scaling always balances instances across Availability Zones first, whatever termination policy is used, so some newer instances can be terminated before older ones.
  scope: per Auto Scaling group during scale in.
  link: [always balances instances across Availability Zones first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
  link: [regardless of which termination policy is used](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
ec2-auto-scaling-termination-default-billing-hour-then-random
  claim: After the outdated-configuration check, the default termination policy picks the instance closest to the next billing hour, and chooses at random among instances that are equally close.
  scope: per Auto Scaling group during scale in.
  link: [closest to the next billing hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-billing-hour-then-random)
  link: [terminate one at random](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-billing-hour-then-random)
ec2-auto-scaling-termination-default-outdated-first
  claim: The default termination policy of an Auto Scaling group is designed to terminate instances that use outdated configurations first; you can change the policy.
  scope: per Auto Scaling group; default; adjustable.
  link: [terminate instances that are using outdated configurations first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-outdated-first)
ec2-auto-scaling-termination-default-zone-with-most
  claim: With the default termination policy, EC2 Auto Scaling first picks the Availability Zone with the most instances that also has at least one instance not protected from scale in.
  scope: per Auto Scaling group during scale in.
  link: [has the most instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-zone-with-most)
  link: [at least one instance that is not protected](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-zone-with-most)
ec2-auto-scaling-termination-hook-best-effort
  claim: By default termination lifecycle hooks are best effort: if the hook times out or is abandoned, EC2 Auto Scaling terminates the instance immediately, unless an instance lifecycle policy retains it.
  scope: per termination lifecycle hook; default; adjustable; an instance lifecycle policy can retain the instance instead.
  link: [termination lifecycle hooks operate on a best-effort basis](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-hook-best-effort)
  link: [proceeds with terminating the instance immediately](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-hook-best-effort)
ec2-auto-scaling-termination-hook-extends-life
  claim: A termination lifecycle hook extends the life of an instance already selected for termination, giving time to finish in-progress work or save it and transfer it to another instance.
  scope: per termination lifecycle hook.
  link: [extends the life of your Amazon EC2 instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-hook-extends-life)
  link: [transfer the work to another instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-hook-extends-life)
ec2-auto-scaling-termination-imbalanced-zone-first
  claim: If one Availability Zone has more instances than the others, EC2 Auto Scaling applies the termination policy to that imbalanced zone first; if the zones are balanced, it applies the policy across all zones.
  scope: per Auto Scaling group during scale in.
  link: [applies the termination policy to the imbalanced zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-imbalanced-zone-first)
  link: [Maintaining Zonal balance takes precedence](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-imbalanced-zone-first)
ec2-auto-scaling-termination-mixed-purchase-option-first
  claim: In a mixed instances group, EC2 Auto Scaling first decides whether to terminate a Spot or an On-Demand Instance, based on the group settings, so the group trends toward its Spot and On-Demand ratio.
  scope: per Auto Scaling group during scale in.
  link: [which purchase option (Spot or On-Demand)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-mixed-purchase-option-first)
  link: [trends toward the specified ratio](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-mixed-purchase-option-first)
ec2-auto-scaling-termination-policy-allocation-strategy
  claim: The AllocationStrategy termination policy terminates instances so that the remaining instances align with the group's allocation strategy for the purchase option that is terminating; it helps when preferred instance types change.
  scope: per Auto Scaling group during scale in.
  link: [AllocationStrategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-allocation-strategy)
  link: [align the remaining instances to the allocation strategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-allocation-strategy)
ec2-auto-scaling-termination-policy-closest-to-next-hour
  claim: The ClosestToNextInstanceHour termination policy terminates the instances closest to the next billing hour, to get the most from instances with an hourly charge.
  scope: per Auto Scaling group during scale in.
  link: [ClosestToNextInstanceHour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-closest-to-next-hour)
  link: [closest to the next billing hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-closest-to-next-hour)
ec2-auto-scaling-termination-policy-newest-instance
  claim: The NewestInstance termination policy terminates the newest instance in the group; it is useful when you test a new launch configuration but do not want to keep it in production.
  scope: per Auto Scaling group during scale in.
  link: [NewestInstance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-newest-instance)
  link: [Terminate the newest instance in the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-newest-instance)
ec2-auto-scaling-termination-policy-oldest-instance
  claim: The OldestInstance termination policy terminates the oldest instance in the group; it is useful when you move the group to a new EC2 instance type.
  scope: per Auto Scaling group during scale in.
  link: [OldestInstance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-instance)
  link: [Terminate the oldest instance in the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-instance)
ec2-auto-scaling-termination-policy-oldest-launch-template
  claim: The OldestLaunchTemplate termination policy terminates first the instances that use a noncurrent launch template, then the instances that use the oldest version of the current launch template.
  scope: per Auto Scaling group during scale in.
  link: [OldestLaunchTemplate](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-launch-template)
  link: [Terminate instances that have the oldest launch template](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-launch-template)
ec2-auto-scaling-termination-policy-skips-unhealthy
  claim: Termination policies apply only to instances the group does not consider unhealthy; instances marked unhealthy by health checks bypass the termination policy.
  scope: per Auto Scaling group during scale in.
  link: [bypass termination policy evaluation](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-skips-unhealthy)
  link: [only to instances that are not considered unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-skips-unhealthy)
ec2-auto-scaling-two-notification-ways
  claim: You can receive Auto Scaling notifications in two ways: Amazon SNS, which notifies when the group launches or terminates instances and can only be turned on or off, and Amazon EventBridge, which matches events to criteria and sends them to many targets.
  scope: per Auto Scaling group (notifications).
  link: [two ways to receive notifications](../facts/ec2-auto-scaling.md#ec2-auto-scaling-two-notification-ways)
  link: [only turn Amazon SNS notifications on or off](../facts/ec2-auto-scaling.md#ec2-auto-scaling-two-notification-ways)
  link: [sent to a variety of targets](../facts/ec2-auto-scaling.md#ec2-auto-scaling-two-notification-ways)
ec2-auto-scaling-unhealthy-bypasses-protection
  claim: An unhealthy instance is terminated even with a custom termination policy or scale-in protection; the only way to stop replacement of unhealthy instances is to suspend the HealthCheck, ReplaceUnhealthy or Terminate process.
  scope: per unhealthy instance.
  link: [only way to prevent replacement of unhealthy instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-bypasses-protection)
  link: [custom termination policies or scale-in protection in place](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-bypasses-protection)
ec2-auto-scaling-unhealthy-replacement-10-percent-at-a-time
  claim: By default, Amazon EC2 Auto Scaling replaces up to 10 percent of the group's desired capacity at a time until all unhealthy instances are replaced; in a group so small that 10 percent is less than one instance it replaces them one at a time, and an instance maintenance policy can modify the 10 percent value.
  scope: per Auto Scaling group; default; adjustable; groups where 10 percent of desired capacity is at least one instance; no instance maintenance policy changes the rate.
  link: [10 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-replacement-10-percent-at-a-time)
  say: ten percent
ec2-auto-scaling-unhealthy-replacement-after-90-percent
  claim: Unhealthy instances are replaced after new instances finish warming up and the group has risen to more than 90 percent of its desired capacity.
  scope: per Auto Scaling group (health checks).
  link: [more than 90 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-replacement-after-90-percent)
  say: more than ninety percent
ec2-auto-scaling-unhealthy-replacement-small-group-one-at-a-time
  claim: In a small group where 10 percent is less than one instance, unhealthy instances are replaced one at a time, which might cause some downtime.
  scope: per Auto Scaling group (health checks).
  link: [one at a time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-replacement-small-group-one-at-a-time)
  say: one at a time
ec2-auto-scaling-unhealthy-replacement-waits-below-10-percent
  claim: If a scaling activity is in progress and the group is short of its desired capacity by 10 percent or more, Amazon EC2 Auto Scaling waits for that activity before it replaces unhealthy instances.
  scope: per Auto Scaling group (health checks).
  link: [10 percent or more](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-replacement-waits-below-10-percent)
  say: ten percent or more
ec2-auto-scaling-unhealthy-terminated-replaced
  claim: An Auto Scaling group keeps a fixed number of instances even when one becomes unhealthy: it terminates the unhealthy instance and launches another to replace it.
  scope: per Auto Scaling group (health checks).
  link: [terminates the unhealthy instance and launches another](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-terminated-replaced)
  link: [maintain a fixed number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-terminated-replaced)
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
ec2-auto-scaling-vertical-stopped-group-instance-unhealthy
  claim: If you stop an instance in an Auto Scaling group to change its type, EC2 Auto Scaling marks it unhealthy and might replace it; suspend the scaling processes to prevent this.
  scope: per instance in an Auto Scaling group.
  link: [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stopped-group-instance-unhealthy)
  link: [suspend the scaling processes for the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stopped-group-instance-unhealthy)
ec2-auto-scaling-wa-attribute-based-selection-newer-types
  claim: Attribute-based instance type selection in an Auto Scaling group lets the group use newer-generation instance types automatically when they are released and reach a broader range of Spot capacity.
  scope: AWS Well-Architected guidance.
  link: [newer generation instance types when they are released](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-attribute-based-selection-newer-types)
ec2-auto-scaling-wa-auto-recovery-when-single-location
  claim: Well-Architected names EC2 automatic recovery for an application that cannot be deployed in multiple locations: it replaces failed hardware and restarts the instance.
  scope: AWS Well-Architected guidance; the application cannot be deployed in multiple locations and can tolerate rebooting.
  link: [not capable of being deployed in multiple locations](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-auto-recovery-when-single-location)
ec2-auto-scaling-wa-auto-scaling-self-heals-stateless
  claim: Well-Architected: Auto Scaling can self-heal stateless applications and add or remove capacity, and making services stateless lets a whole resource be replaced on restart without losing data.
  scope: AWS Well-Architected guidance.
  link: [can perform self-healing on stateless applications](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-auto-scaling-self-heals-stateless)
ec2-auto-scaling-wa-customer-experience-metric
  claim: Well-Architected COST09-BP03 says that, when possible, you should scale on a metric that reflects customer experience, typically a custom metric from the application code, rather than only standard EC2 metrics.
  scope: AWS Well-Architected guidance; when possible.
  link: [indicative of customer experience](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-customer-experience-metric)
ec2-auto-scaling-wa-demand-based-pay-for-use
  claim: Well-Architected COST09-BP03: supplying resources based on demand means you pay only for the resources you use, launching them when needed and terminating them when not.
  scope: AWS Well-Architected guidance.
  link: [pay for the resources you use only](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-demand-based-pay-for-use)
ec2-auto-scaling-wa-immutable-infrastructure-definition
  claim: Well-Architected defines immutable infrastructure as a model where no updates, security patches or configuration changes happen in place on production workloads; a change is built onto new infrastructure and deployed, which also lets remote access such as SSH be disabled.
  scope: AWS Well-Architected guidance.
  link: [no updates, security patches, or configuration changes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-immutable-infrastructure-definition)
  link: [remote access mechanisms (such as SSH)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-immutable-infrastructure-definition)
ec2-auto-scaling-wa-immutable-rollback-benefit
  claim: With immutable deployments the previous working version is not changed, so you can roll back to it when errors are detected; deployments either complete or change nothing.
  scope: AWS Well-Architected guidance.
  link: [the previous working version is not changed](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-immutable-rollback-benefit)
ec2-auto-scaling-wa-instance-scheduler-cannot-stop-group-instances
  claim: AWS Instance Scheduler cannot stop and start instances that are part of an Auto Scaling group; Auto Scaling groups have their own scheduling for the instances in the group.
  scope: per Auto Scaling group instance.
  link: [cannot stop and start instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-instance-scheduler-cannot-stop-group-instances)
ec2-auto-scaling-wa-load-balanced-clusters-use-groups
  claim: The Well-Architected reliability pillar says compute clusters reached through a load balancer should use Auto Scaling groups, with Elastic Load Balancing spreading traffic across targets in one or more Availability Zones.
  scope: AWS Well-Architected guidance.
  link: [should leverage Auto Scaling groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-load-balanced-clusters-use-groups)
ec2-auto-scaling-wa-memory-is-a-poor-scaling-metric
  claim: Well-Architected warns against memory utilization as a scaling metric: it rises as an application warms up and usually stays high when demand falls, so it does not track demand in both directions.
  scope: AWS Well-Architected guidance.
  link: [does not correspond to demand in both directions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-memory-is-a-poor-scaling-metric)
ec2-auto-scaling-wa-offload-session-data
  claim: To make an application stateless, Well-Architected says to offload session data to a database, a cache or external files.
  scope: AWS Well-Architected guidance.
  link: [database, cache, or external files](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-offload-session-data)
ec2-auto-scaling-wa-policies-improve-performance-and-cost
  claim: Well-Architected REL07-BP01: by monitoring key metrics and applying predefined scaling policies, Auto Scaling provisions or deprovisions resources as needed, which improves performance and cost-efficiency and avoids manual errors or delays.
  scope: AWS Well-Architected guidance.
  link: [improves performance and cost-efficiency](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-policies-improve-performance-and-cost)
ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times
  claim: Both scheduled and predictive scaling implement time-based supply; predictive scaling scales out from observed patterns, while scheduled scaling scales out at times you define in advance.
  scope: AWS Well-Architected guidance.
  link: [Predictive scaling uses patterns to scale out](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times)
  link: [scheduled scaling uses pre-defined times to scale out](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times)
ec2-auto-scaling-wa-predictive-scaling-before-projected-load
  claim: Well-Architected cost advice: consider predictive scaling for regular traffic spikes and applications that take a long time to start, because it initializes capacity before projected load, while dynamic scaling alone is reactive.
  scope: AWS Well-Architected guidance.
  link: [applications that take a long time to start](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-predictive-scaling-before-projected-load)
  link: [dynamic scaling alone, which is reactive in nature](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-predictive-scaling-before-projected-load)
ec2-auto-scaling-wa-queue-depth-metric-for-batch-work
  claim: For a video transcoding application, 100% CPU utilization is expected and should not be the primary scaling metric; use the depth of the transcoding job queue instead, and the metric value must increase or decrease proportionally to the number of instances in the group.
  scope: AWS Well-Architected guidance.
  link: [100% CPU utilization is expected and should not be your primary metric](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-queue-depth-metric-for-batch-work)
  link: [depth of the transcoding job queue](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-queue-depth-metric-for-batch-work)
ec2-auto-scaling-wa-replaces-unhealthy-instance
  claim: Well-Architected auto-healing: when an instance is in any state other than running, or its system status is impaired, EC2 Auto Scaling considers the instance unhealthy and launches a replacement instance.
  scope: AWS Well-Architected guidance.
  link: [considers the instance to be unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-replaces-unhealthy-instance)
ec2-auto-scaling-wa-scaling-metric-examples
  claim: Typical scaling metrics include CPU utilization, work queue depth such as an Amazon SQS queue, number of active users and network throughput; a scaling metric is one that corresponds to the workload's demand.
  scope: AWS Well-Architected guidance.
  link: [CPU utilization, work queue depth](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-scaling-metric-examples)
ec2-auto-scaling-wa-stateless-scales-horizontally
  claim: Stateless applications can scale horizontally because any available compute resource, such as an EC2 instance or a Lambda function, can serve any request.
  scope: AWS Well-Architected guidance.
  link: [they can scale horizontally](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-stateless-scales-horizontally)
ec2-auto-scaling-wa-stateless-servers-replaceable
  claim: Well-Architected REL05-BP06: a system that keeps no state on local disk or memory between requests lets servers be replaced at will without an availability impact.
  scope: AWS Well-Architected guidance.
  link: [replaced at will without causing an availability impact](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-stateless-servers-replaceable)
ec2-auto-scaling-wa-static-stability-for-az-loss
  claim: For large-scale replacement such as losing a whole Availability Zone, Well-Architected prefers static stability for high availability.
  scope: AWS Well-Architected guidance; large-scale replacements.
  link: [static stability is preferred for high availability](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-static-stability-for-az-loss)
ec2-auto-scaling-wa-three-scaling-options
  claim: Well-Architected names three major options to scale automatically: metric-based scaling, scheduled scaling (often for predictable demand such as weekday business hours or sales events), and predictive scaling, which uses machine learning to scale resources based on anticipated demand.
  scope: AWS Well-Architected guidance.
  link: [metric-based scaling, scheduled scaling, and predictive scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-three-scaling-options)
  link: [uses machine learning to automatically scale resources](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-three-scaling-options)
ec2-auto-scaling-wa-time-based-supply-no-startup-delay
  claim: A time-based supply approach has resources ready at the time they are needed, without waiting for start-up procedures and system or consistency checks, and it does not depend on resource utilization.
  scope: AWS Well-Architected guidance; demand that is predictable or well-defined by time.
  link: [available at the specific time they are required](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-time-based-supply-no-startup-delay)
ec2-auto-scaling-wa-utilization-target-50-70-percent
  claim: Well-Architected advice: do not set a scaling target close to full utilization such as 90% CPU; typical targets range between 50-70% because metric-based scaling is a latent operation that needs minutes to add capacity.
  scope: AWS Well-Architected guidance.
  link: [range between 50-70%](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-utilization-target-50-70-percent)
  link: [90% CPU utilization](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-utilization-target-50-70-percent)
ec2-auto-scaling-warm-pool-definition
  claim: A warm pool is a pool of pre-initialized EC2 instances beside an Auto Scaling group; on scale out the group draws on the pool, and instances count toward desired capacity only as they leave the pool.
  scope: per warm pool.
  link: [pool of pre-initialized EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-definition)
  link: [count toward the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-definition)
ec2-auto-scaling-warm-pool-depleted-cold-start
  claim: If the warm pool is empty during a scale-out event, instances launch directly into the group (a cold start); a zone that is out of capacity can also cause cold starts.
  scope: per warm pool.
  link: [launch directly into the Auto Scaling group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-depleted-cold-start)
  link: [cold start](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-depleted-cold-start)
ec2-auto-scaling-warm-pool-ebs-root-required
  claim: EC2 Auto Scaling can keep a warm pool instance Stopped or Hibernated only if its root device is an EBS volume; instance store-backed instances cannot be stopped or hibernated.
  scope: per warm pool.
  link: [only if it has an Amazon EBS volume](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-ebs-root-required)
  link: [cannot be stopped or hibernated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-ebs-root-required)
ec2-auto-scaling-warm-pool-hibernated-ram
  claim: A Hibernated warm pool instance saves its RAM contents to the EBS root volume; while hibernated you pay only for EBS volumes (including the RAM storage) and Elastic IP addresses.
  scope: per warm pool.
  link: [save the contents of your RAM](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-hibernated-ram)
  link: [pay only for the EBS volumes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-hibernated-ram)
ec2-auto-scaling-warm-pool-no-spot-no-weights
  claim: A warm pool is not supported with weighted mixed instance groups, and a mixed instances policy must be On-Demand only (no Spot) to use a warm pool.
  scope: per Auto Scaling group with a mixed instances policy.
  link: [aren’t supported with weighted mixed instance groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-no-spot-no-weights)
  link: [don’t support Spot Instances within mixed instance groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-no-spot-no-weights)
ec2-auto-scaling-warm-pool-reuse-policy
  claim: By default EC2 Auto Scaling terminates instances on scale in and launches new ones into the warm pool; an instance reuse policy returns scaled-in instances to the warm pool instead.
  scope: per warm pool; default; adjustable.
  link: [launches new instances into the warm pool](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-reuse-policy)
  link: [specify an instance reuse policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-reuse-policy)
ec2-auto-scaling-warm-pool-size-default
  claim: By default the warm pool size is the group's maximum capacity minus its desired capacity; MaxGroupPreparedCapacity sets a separate cap, and there is no minimum pool size by default.
  scope: per warm pool; default; adjustable; a custom MaxGroupPreparedCapacity changes the calculation.
  link: [maximum capacity and its desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-size-default)
  link: [MaxGroupPreparedCapacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-size-default)
  link: [There is no minimum size set by default](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-size-default)
ec2-auto-scaling-warm-pool-states
  claim: Warm pool instances can be kept in one of three states: Stopped, Running or Hibernated; keeping them Stopped is an effective way to minimize costs, because you pay only for the volumes and the attached Elastic IP addresses.
  scope: per warm pool.
  link: [Stopped, Running, or Hibernated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-states)
  link: [pay only for the volumes that you use](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-states)
  link: [an effective way to minimize costs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-states)
ec2-auto-scaling-warm-pool-stop-ignores-user-data
  claim: Instances entering a warm pool are stopped or hibernated without waiting for user data to finish; to hold an instance until bootstrap completes, use an EC2_INSTANCE_LAUNCHING lifecycle hook.
  scope: per warm pool.
  link: [does not wait for user data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-stop-ignores-user-data)
  link: [hold an instance until your bootstrap script completes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-stop-ignores-user-data)
ec2-auto-scaling-warm-pool-stopped-instances-pay-volumes-only
  claim: For stopped warm pool instances you pay only for the volumes and the attached Elastic IP addresses; keeping warm pool instances Running is possible but strongly discouraged because of the extra charges.
  scope: per warm pool.
  link: [pay only for the volumes that you use](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-stopped-instances-pay-volumes-only)
  link: [highly discouraged](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-stopped-instances-pay-volumes-only)
ec2-auto-scaling-warm-pool-unnecessary-cost
  claim: Creating a warm pool when it is not required can lead to unnecessary costs: if first boot time does not cause noticeable latency issues for the application, you probably do not need a warm pool.
  scope: per warm pool.
  link: [can lead to unnecessary costs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-unnecessary-cost)
ec2-auto-scaling-warmup-blocks-scale-in
  claim: While new instances are warming up, dynamic scaling blocks scale-in activities until they finish warming up, and warming-up instances count as group capacity when it decides how many instances to add.
  scope: per Auto Scaling group (instance warmup); while instances are warming up.
  link: [blocks the scale in activities for dynamic scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warmup-blocks-scale-in)
ec2-auto-scaling-warmup-fallbacks-when-unset
  claim: Without a default instance warmup, instance refresh uses the health check grace period as its warmup, target tracking and step scaling policies use the default cooldown value, and predictive scaling policies have no default warmup.
  scope: per Auto Scaling group; default; adjustable; no default instance warmup set.
  link: [uses the health check grace period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warmup-fallbacks-when-unset)
  link: [value set for the default cooldown](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warmup-fallbacks-when-unset)
  link: [they have no default warmup time](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warmup-fallbacks-when-unset)
ec2-auto-scaling-warmup-instance-not-in-metrics
  claim: Until its warmup time has expired, a new instance is not counted toward the group's aggregated EC2 instance metrics.
  scope: per Auto Scaling group (instance warmup).
  link: [not counted toward the aggregated EC2 instance metrics](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warmup-instance-not-in-metrics)
  say: not counted in the aggregated metrics
ec2-auto-scaling-weights-can-exceed-max
  claim: With instance weights, EC2 Auto Scaling can scale out above the maximum size, but only by up to your largest instance weight.
  scope: per mixed instances group with instance weights.
  link: [only by up to your maximum instance weight](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-can-exceed-max)
  link: [scale out above the maximum size limit](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-can-exceed-max)
ec2-auto-scaling-weights-desired-in-units
  claim: With weights, specify the group's desired capacity (and minimum and maximum) in units, not instances; current capacity can be at or above desired capacity.
  scope: per mixed instances group.
  link: [desired capacity in units, not instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-desired-in-units)
  link: [at the desired capacity or above it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-desired-in-units)
ec2-auto-scaling-weights-equal-by-default
  claim: By default all instance types have equal weight regardless of size, so each instance counts the same toward desired capacity.
  scope: per Auto Scaling group; default; adjustable.
  link: [equal weight regardless of size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-equal-by-default)
  link: [each instance counts the same](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-equal-by-default)
ec2-auto-scaling-weights-units-toward-desired
  claim: With weights, each instance type counts as its assigned number of units toward desired capacity; weights do not choose which instance types launch, the allocation strategies do.
  scope: per mixed instances group.
  link: [how many units to associate](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-units-toward-desired)
  link: [The weights do not change which instance types](../facts/ec2-auto-scaling.md#ec2-auto-scaling-weights-units-toward-desired)
ec2-auto-scaling-whitepaper-group-per-tier
  claim: The web hosting whitepaper, which is marked as a historical reference, describes multiple Auto Scaling groups for different layers of the architecture, so each layer can scale independently, for example on network I/O for web servers and CPU utilization for application servers.
  scope: AWS web hosting whitepaper (historical reference).
  link: [each layer can scale independently](../facts/ec2-auto-scaling.md#ec2-auto-scaling-whitepaper-group-per-tier)
ec2-auto-scaling-zonal-shift-is-arc-feature
  claim: Zonal shift is a capability of Amazon Application Recovery Controller (ARC); enabling it registers the Auto Scaling group with the ARC zonal shift service, and during an active zonal shift the group treats that Availability Zone as impaired.
  scope: per Auto Scaling group with zonal shift.
  link: [Amazon Application Recovery Controller (ARC)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-zonal-shift-is-arc-feature)
ec2-auto-scaling-zonal-shift-launches-only-in-healthy-azs
  claim: Since November 18, 2024, you can start a zonal shift on an Auto Scaling group: the group then launches all new capacity in the healthy Availability Zones and blocks scaling policies from decreasing desired capacity.
  scope: per Auto Scaling group with zonal shift.
  link: [in the healthy Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-zonal-shift-launches-only-in-healthy-azs)
  link: [block scaling policies from decreasing desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-zonal-shift-launches-only-in-healthy-azs)
  link: [November 18, 2024](../facts/ec2-auto-scaling.md#ec2-auto-scaling-zonal-shift-launches-only-in-healthy-azs)
ec2-auto-scaling-zonal-shift-min-healthy-100-best-practice
  claim: For zonal shift, AWS recommends an instance maintenance policy with a minimum healthy percentage of 100, so the group waits for a new instance to be ready before it terminates an unhealthy one.
  scope: per Auto Scaling group with zonal shift.
  link: [minimum healthy percentage of 100](../facts/ec2-auto-scaling.md#ec2-auto-scaling-zonal-shift-min-healthy-100-best-practice)
