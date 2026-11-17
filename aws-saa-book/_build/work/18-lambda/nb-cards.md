facts card: 25 facts
rds-proxy-lambda-connection-pooling
  claim: AWS Lambda functions are good candidates for RDS Proxy because they make frequent short database connections that benefit from its connection pooling, and they can use IAM authentication instead of database credentials in the function code.
  scope: Amazon RDS Proxy.
  link: [connection pooling offered by RDS Proxy](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling)
  link: [frequent short database connections](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling)
rds-proxy-faq-use-case-open-close
  claim: Applications that open and close database connections often, such as serverless, PHP or Ruby on Rails apps, benefit from the connection pool that RDS Proxy keeps.
  scope: Amazon RDS Proxy.
  link: [Serverless, PHP, or Ruby on Rails](../facts/rds-proxy.md#rds-proxy-faq-use-case-open-close)
rds-proxy-faq-lambda-iam-execution-role
  claim: With RDS Proxy, a Lambda function no longer handles database credentials in code: it can authenticate to RDS Proxy and the database with its IAM execution role.
  scope: Amazon RDS Proxy.
  link: [IAM execution role](../facts/rds-proxy.md#rds-proxy-faq-lambda-iam-execution-role)
rds-proxy-definition-pool-share
  claim: Amazon RDS Proxy lets applications pool and share database connections to improve their ability to scale, and makes them more resilient to database failures by connecting to a standby while preserving application connections.
  scope: Amazon RDS Proxy.
  link: [pool and share database connections](../facts/rds-proxy.md#rds-proxy-definition-pool-share)
  link: [preserving application connections](../facts/rds-proxy.md#rds-proxy-definition-pool-share)
rds-proxy-surges-queue-throttle
  claim: RDS Proxy queues or throttles application connections that cannot be served at once from the pool, so latency may rise but the application keeps scaling; requests beyond your limits are rejected (load shedding).
  scope: Amazon RDS Proxy.
  link: [queues or throttles application connections](../facts/rds-proxy.md#rds-proxy-surges-queue-throttle)
  link: [it sheds load](../facts/rds-proxy.md#rds-proxy-surges-queue-throttle)
rds-proxy-same-vpc-not-public
  claim: RDS Proxy must be in the same VPC as the database and cannot be publicly accessible, even if the database is.
  scope: Amazon RDS Proxy.
  link: [The proxy can't be publicly accessible](../facts/rds-proxy.md#rds-proxy-same-vpc-not-public)
  link: [same virtual private cloud (VPC) as the database](../facts/rds-proxy.md#rds-proxy-same-vpc-not-public)
rds-proxy-faq-secrets-manager-credentials
  claim: RDS Proxy lets you manage database credentials centrally in AWS Secrets Manager.
  scope: Amazon RDS Proxy.
  link: [AWS Secrets Manager](../facts/rds-proxy.md#rds-proxy-faq-secrets-manager-credentials)
rds-proxy-pricing-per-vcpu
  claim: For provisioned instances, RDS Proxy is priced per vCPU per hour of the underlying database; partial hours are billed in 1-second increments, with a 10-minute minimum charge following a billable status change such as creating, starting, or modifying.
  scope: per proxy; Aurora Serverless is priced per ACU per hour instead; the default proxy endpoint has no extra charge, additional endpoints incur PrivateLink charges.
  link: [priced per vCPU per hour](../facts/rds-proxy.md#rds-proxy-pricing-per-vcpu)
  link: [a 10-minute minimum charge](../facts/rds-proxy.md#rds-proxy-pricing-per-vcpu)
  say: per vCPU of the database per hour | ten-minute minimum
rds-proxy-lambda-console-connect
  claim: When you connect a Lambda function to a DB instance in the RDS console, you can route the connection through RDS Proxy; RDS then configures the VPC security groups for the function, the DB instance and the proxy.
  scope: Amazon RDS Proxy.
  link: [configures the VPC security group for the proxy](../facts/rds-proxy.md#rds-proxy-lambda-console-connect)
elb-lambda-target-alb-only
  claim: Network Load Balancers do not support the lambda target type; Application Load Balancers are the only load balancers that support it.
  scope: lambda target type.
  link: [do not support the `lambda` target type](../facts/elb.md#elb-lambda-target-alb-only)
  link: [the only load balancers that support](../facts/elb.md#elb-lambda-target-alb-only)
elb-lambda-target-body-max-1-mb
  claim: With a Lambda function as an Application Load Balancer target, the request body sent to the function and the response JSON from the function can each be at most 1 MB.
  scope: per request and per response, Lambda target of an Application Load Balancer; maximum; not adjustable.
  link: [1 MB](../facts/elb.md#elb-lambda-target-body-max-1-mb)
  say: one megabyte
elb-alb-lambda-request-as-json
  claim: When an ALB forwards a request to a target group with a Lambda function target, it invokes the function directly (not over a network connection) and passes the request content to it in JSON format.
  scope: Application Load Balancer Lambda target.
  link: [in JSON format](../facts/elb.md#elb-alb-lambda-request-as-json)
  link: [invokes the Lambda function directly](../facts/elb.md#elb-alb-lambda-request-as-json)
elb-alb-lambda-same-account-region
  claim: A Lambda function target and its target group must be in the same account and the same Region, and WebSockets are not supported for Lambda targets.
  scope: Application Load Balancer Lambda target.
  link: [in the same Region](../facts/elb.md#elb-alb-lambda-same-account-region)
  link: [WebSockets are not supported](../facts/elb.md#elb-alb-lambda-same-account-region)
elb-alb-target-types-instance-ip-lambda
  claim: An Application Load Balancer target group has the target type instance (targets by instance ID), ip (targets by IP address) or lambda (a Lambda function), and the target type cannot be changed after the target group is created.
  scope: Application Load Balancer target group; target type fixed at creation.
  link: [The target is a Lambda function](../facts/elb.md#elb-alb-target-types-instance-ip-lambda)
  link: [you can't change its target type](../facts/elb.md#elb-alb-target-types-instance-ip-lambda)
ec2-compute-guide-lambda-no-servers
  claim: Serverless computing options like AWS Lambda run code in response to events without the need to manage servers, reducing the operational burden.
  scope: AWS Lambda compared with EC2.
  link: [without the need to manage servers](../facts/ec2.md#ec2-compute-guide-lambda-no-servers)
  say: Lambda runs code on events, with no servers to manage
ec2-on-demand-billing-per-second-60s-minimum
  claim: On-Demand Instances are billed only for the seconds they are in the running state, with a 60-second minimum.
  scope: per On-Demand Instance; minimum.
  link: [60-second minimum](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [You pay only for the seconds](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [are in the running state](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  say: a sixty-second minimum | only for the seconds the instance is running | while running
ec2-spot-recommended-stateless-fault-tolerant-flexible
  claim: AWS recommends Spot Instances for stateless, fault-tolerant, flexible applications, such as big data, containerized workloads, CI/CD, stateless web servers, high performance computing (HPC) and rendering.
  scope: Spot Instances.
  link: [stateless, fault-tolerant, flexible applications](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible)
  link: [big data, containerized workloads, CI/CD](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible)
  say: Spot is for stateless, fault-tolerant, flexible applications
ec2-spot-interruption-notice-two-minutes
  claim: A Spot Instance interruption notice is a warning issued two minutes before Amazon EC2 stops or terminates the Spot Instance; with hibernation as the interruption behavior you get the notice but not a two-minute warning, because hibernation begins immediately.
  scope: per Spot Instance; fixed; interruption notices are emitted on a best effort basis.
  link: [two minutes before Amazon EC2 stops or terminates your Spot Instance](../facts/ec2.md#ec2-spot-interruption-notice-two-minutes)
  link: [you do not receive a two-minute warning](../facts/ec2.md#ec2-spot-interruption-notice-two-minutes)
  say: a two-minute warning | no two-minute warning for hibernation
ec2-spot-discount-up-to-90-percent
  claim: Spot Instances use spare EC2 capacity at a discount of up to 90% compared with On-Demand prices.
  scope: per Spot Instance; maximum; spare EC2 capacity; the Spot price varies with supply and demand.
  link: [up to 90%](../facts/ec2.md#ec2-spot-discount-up-to-90-percent)
  say: up to ninety percent off On-Demand
ec2-compute-guide-fargate-no-servers-for-containers
  claim: AWS Fargate is a technology you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances.
  scope: AWS Fargate.
  link: [run containers without having to manage servers](../facts/ec2.md#ec2-compute-guide-fargate-no-servers-for-containers)
  say: Fargate runs containers with no servers to manage
ec2-auto-scaling-sqs-backlog-per-instance
  claim: Backlog per instance is the queue length (ApproximateNumberOfMessages) divided by the number of InService instances; the target tracking target is the acceptable backlog per instance.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [Divide that number by the fleet's running capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [acceptable backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
ec2-auto-scaling-wa-queue-depth-metric-for-batch-work
  claim: For a video transcoding application, 100% CPU utilization is expected and should not be the primary scaling metric; use the depth of the transcoding job queue instead, and the metric value must increase or decrease proportionally to the number of instances in the group.
  scope: AWS Well-Architected guidance.
  link: [100% CPU utilization is expected and should not be your primary metric](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-queue-depth-metric-for-batch-work)
  link: [depth of the transcoding job queue](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-queue-depth-metric-for-batch-work)
ec2-neighbour-batch-provisions-for-jobs
  claim: AWS Batch runs batch computing workloads of any scale as a fully managed service: it automatically provisions compute resources and optimizes the workload distribution, with no batch computing software to install or manage.
  scope: AWS Batch.
  link: [automatically provisions compute resources](../facts/ec2.md#ec2-neighbour-batch-provisions-for-jobs)
  say: Batch runs batch jobs and provisions the compute for you
ec2-auto-scaling-faq-replacement-time-minutes
  claim: Replacing an unhealthy instance with a new InService instance takes minutes: most replacements happen in less than 5 minutes, and the time depends on factors such as how long the AMI takes to boot.
  scope: per replacement; depends on factors such as AMI boot time.
  link: [less than 5 minutes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-replacement-time-minutes)
  link: [within minutes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-replacement-time-minutes)
  say: less than five minutes
ec2-auto-scaling-custom-termination-policy-lambda
  claim: A custom termination policy is a Lambda function that Auto Scaling calls whenever it must select an instance for termination; it terminates only instances that the function returns.
  scope: per Auto Scaling group during scale in.
  link: [custom termination policy using a Lambda function](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-termination-policy-lambda)
  link: [only terminate instances that the function returns](../facts/ec2-auto-scaling.md#ec2-auto-scaling-custom-termination-policy-lambda)
