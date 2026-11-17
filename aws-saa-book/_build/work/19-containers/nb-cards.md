facts card: 16 facts
ec2-auto-scaling-case-canva-ecs-spot-capacity-provider
  claim: Canva runs its video and streaming functions as containerized workloads on Amazon ECS that use ECS cluster auto scaling, which manages the scaling of the EC2 instances registered to the cluster, with a dedicated capacity provider on EC2 Spot Instances.
  scope: customer case study.
  link: [Amazon ECS cluster auto scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-canva-ecs-spot-capacity-provider)
  link: [runs on Amazon EC2 Spot Instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-case-canva-ecs-spot-capacity-provider)
lambda-choose-fargate-containers-persistent
  claim: The decision guide says to consider Fargate when you need to run containerized applications with specific resource needs or persistent processes.
  scope: Fargate versus Lambda.
  link: [specific resource needs or persistent processes](../facts/lambda.md#lambda-choose-fargate-containers-persistent)
  say: containers with persistent processes
lambda-container-image-10-gb
  claim: A container image for Lambda is limited to 10 GB, measured as the maximum uncompressed image size including all layers.
  scope: per function, container image, uncompressed including all layers; maximum; not adjustable.
  link: [10 GB](../facts/lambda.md#lambda-container-image-10-gb)
lambda-container-image-ecr-same-region
  claim: A container image function is created from an image in an Amazon ECR repository that must be in the same AWS Region as the function; the image can be in a different AWS account if it is in the same Region.
  scope: Lambda function defined as a container image.
  link: [in the same AWS Region](../facts/lambda.md#lambda-container-image-ecr-same-region)
  link: [an image in a different AWS account](../facts/lambda.md#lambda-container-image-ecr-same-region)
  say: an ECR repository in the same Region
lambda-fargate-long-running-lambda-short
  claim: The decision guide positions Fargate as ideal for long-running applications, microservices or batch processing, while Lambda functions are optimized for short-lived, event-driven tasks with a maximum execution time of 15 minutes per invocation.
  scope: Fargate versus Lambda.
  link: [long-running applications, microservices, or batch processing](../facts/lambda.md#lambda-fargate-long-running-lambda-short)
  link: [short-lived, event-driven tasks](../facts/lambda.md#lambda-fargate-long-running-lambda-short)
lambda-fargate-no-execution-time-limit
  claim: Containers in Fargate can run indefinitely because Fargate has no hard limit on execution time, while a Lambda function has a maximum execution time of 15 minutes per invocation.
  scope: per Fargate task container, compared with one Lambda invocation; maximum.
  link: [no hard limit on execution time](../facts/lambda.md#lambda-fargate-no-execution-time-limit)
  link: [15 minutes per invocation](../facts/lambda.md#lambda-fargate-no-execution-time-limit)
lambda-vs-fargate-cost-by-volume
  claim: The decision guide says you typically pay less with Lambda at lower traffic volumes, while Fargate's per-second resource billing tends to be more economical for sustained, high-throughput workloads; Lambda costs scale linearly with request volume.
  scope: Fargate versus Lambda cost.
  link: [pay less with Lambda at lower traffic volumes](../facts/lambda.md#lambda-vs-fargate-cost-by-volume)
  link: [sustained, high-throughput workloads](../facts/lambda.md#lambda-vs-fargate-cost-by-volume)
lambda-vs-fargate-cpu-memory-ceilings
  claim: With Fargate you can select CPU values from 0.25 vCPUs to 32 vCPUs, and memory ranges from 0.5 GB to 244 GB per task, depending on your configuration; with Lambda, CPU scales with memory, up to 6 vCPU.
  scope: per Fargate task, compared with a Lambda function; maximum; not adjustable; Fargate memory range depends on the task configuration.
  link: [0.25 vCPUs to 32 vCPUs](../facts/lambda.md#lambda-vs-fargate-cpu-memory-ceilings)
  link: [0.5 GB to 244 GB per task](../facts/lambda.md#lambda-vs-fargate-cpu-memory-ceilings)
lambda-vs-fargate-state
  claim: For standard Lambda functions each invocation is independent and stateless, so state that must persist between invocations is managed externally, for example in a database or storage service.
  scope: Fargate versus Lambda.
  link: [each invocation is independent and stateless](../facts/lambda.md#lambda-vs-fargate-state)
lambda-durable-vs-fargate-wait-heavy
  claim: For long-running workloads, durable functions are cost-effective for workflows that spend most of their time waiting (human approvals, scheduled delays, external callbacks) because waits incur no compute charges; Fargate fits workloads that need continuous compute.
  scope: Lambda durable functions versus Fargate.
  link: [spend most of their time waiting](../facts/lambda.md#lambda-durable-vs-fargate-wait-heavy)
  link: [require continuous compute](../facts/lambda.md#lambda-durable-vs-fargate-wait-heavy)
ec2-compute-guide-fargate-no-servers-for-containers
  claim: AWS Fargate is a technology you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances.
  scope: AWS Fargate.
  link: [run containers without having to manage servers](../facts/ec2.md#ec2-compute-guide-fargate-no-servers-for-containers)
  say: Fargate runs containers with no servers to manage
ec2-neighbour-batch-runs-on-ec2-fargate
  claim: AWS Batch runs compute-intensive workloads on top of Amazon ECS and Amazon EKS, and can scale compute capacity on Amazon EC2 instances, Fargate resources and Amazon ECS Managed Instances.
  scope: AWS Batch.
  link: [Amazon EC2 instances, Fargate resources](../facts/ec2.md#ec2-neighbour-batch-runs-on-ec2-fargate)
  say: on EC2 instances or Fargate
elb-nlb-faq-ip-targets-container-security-groups-same-port
  claim: Registering containers by IP address instead of instance ID lets each container have its own security group, and lets several containers on one instance use the same port (for example port 80).
  scope: load balancer IP targets for containers.
  link: [can now have its own security group](../facts/elb.md#elb-nlb-faq-ip-targets-container-security-groups-same-port)
  link: [use the same port (say port 80)](../facts/elb.md#elb-nlb-faq-ip-targets-container-security-groups-same-port)
lambda-timeout-max
  claim: The maximum function timeout is 900 seconds (15 minutes); for functions on Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) allow a maximum of 5,400 seconds (90 minutes).
  scope: per function; maximum; not adjustable; 5,400 seconds only for Lambda Managed Instances, asynchronous and event source mapping invocations except Amazon MQ and Amazon DocumentDB.
  link: [900 seconds](../facts/lambda.md#lambda-timeout-max)
  link: [15 minutes](../facts/lambda.md#lambda-timeout-max)
  link: [5,400 seconds (90 minutes)](../facts/lambda.md#lambda-timeout-max)
lambda-choose-functions-event-driven-unpredictable
  claim: The Fargate-or-Lambda decision guide says to consider Lambda functions for event-driven tasks, unpredictable workloads, or wait-heavy orchestration workflows.
  scope: Lambda functions versus Lambda Managed Instances versus Fargate.
  link: [event-driven tasks, unpredictable workloads](../facts/lambda.md#lambda-choose-functions-event-driven-unpredictable)
  say: event-driven, unpredictable work
ec2-compute-guide-ec2-overhead-justified-for-control
  claim: Managing EC2 instances means responsibility for setup, scaling, patching and securing servers, which can need a dedicated operations team; the overhead is often justified where granular control over the compute environment is necessary.
  scope: choosing an AWS compute service.
  link: [granular control over the compute environment](../facts/ec2.md#ec2-compute-guide-ec2-overhead-justified-for-control)
  say: when you need granular control
