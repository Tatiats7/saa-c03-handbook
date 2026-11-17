facts card: 10 facts
ecs-sqs-scale-in-protection-task-processing
  claim: When an ECS service scales in, Service Auto Scaling can stop a task that is still processing a message, which for long-running or non-idempotent work can cause the message to be reprocessed or its progress to be lost; to prevent this, use task scale-in protection to mark a task as protected while it is doing active work.
  scope: Amazon ECS service auto scaling with Amazon SQS.
  link: [stop a task that is still processing](../facts/ecs.md#ecs-sqs-scale-in-protection-task-processing)
  link: [use task scale-in protection](../facts/ecs.md#ecs-sqs-scale-in-protection-task-processing)
ecs-sqs-scale-on-backlog-per-task
  claim: To scale an ECS service on an Amazon SQS queue, AWS recommends scaling on the backlog per task, which is the queue depth divided by the number of running tasks, rather than on queue depth directly.
  scope: Amazon ECS service auto scaling with Amazon SQS.
  link: [scale on the *backlog per task*](../facts/ecs.md#ecs-sqs-scale-on-backlog-per-task)
  link: [not a reliable metric to scale on directly](../facts/ecs.md#ecs-sqs-scale-on-backlog-per-task)
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
ec2-auto-scaling-wa-queue-depth-metric-for-batch-work
  claim: For a video transcoding application, 100% CPU utilization is expected and should not be the primary scaling metric; use the depth of the transcoding job queue instead, and the metric value must increase or decrease proportionally to the number of instances in the group.
  scope: AWS Well-Architected guidance.
  link: [100% CPU utilization is expected and should not be your primary metric](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-queue-depth-metric-for-batch-work)
  link: [depth of the transcoding job queue](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-queue-depth-metric-for-batch-work)
