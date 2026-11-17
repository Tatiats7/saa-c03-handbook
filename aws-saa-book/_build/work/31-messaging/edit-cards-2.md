facts card: 5 facts
sns-quota-subscriptions-per-topic
  claim: The default quota is 12,500,000 subscriptions per standard topic and 100 subscriptions per FIFO topic; for Firehose delivery streams the quota is 5 per topic, per subscription owner.
  scope: per topic (standard; FIFO); Firehose: per topic, per subscription owner; default; adjustable.
  link: [12,500,000 per topic](../facts/sns.md#sns-quota-subscriptions-per-topic)
  link: [100 per topic](../facts/sns.md#sns-quota-subscriptions-per-topic)
  link: [5 per topic, per subscription owner](../facts/sns.md#sns-quota-subscriptions-per-topic)
sqs-message-size-range
  claim: An SQS message can be from a minimum of 1 byte (1 character) to a maximum of 1,048,576 bytes (1 MiB).
  scope: per message; maximum; not adjustable.
  link: [1 MiB](../facts/sqs.md#sqs-message-size-range)
  link: [1,048,576 bytes](../facts/sqs.md#sqs-message-size-range)
  link: [1 byte](../facts/sqs.md#sqs-message-size-range)
  say: one mebibyte | one byte
eventbridge-quota-targets-per-rule
  claim: A Custom Event Bus - Classic rule can have a maximum of 5 targets; this quota is not adjustable.
  scope: per rule, per Region; maximum; not adjustable; Custom Event Bus - Classic (rules and targets)..
  link: [5](../facts/eventbridge.md#eventbridge-quota-targets-per-rule)
  link: [Each supported Region: 5](../facts/eventbridge.md#eventbridge-quota-targets-per-rule)
  say: five targets
sns-retry-aws-managed-total-attempts
  claim: For AWS managed endpoints (AWS Lambda and Amazon SQS), the SNS delivery policy makes 100,015 attempts in total, over 23 days: 3 immediate retries, 2 pre-backoff retries 1 second apart, 10 backoff retries from 1 second to 20 seconds, and 100,000 post-backoff retries 20 seconds apart.
  scope: per message delivery to an AWS managed endpoint (Lambda, SQS); default; not adjustable; Only HTTP/S delivery policies can be changed..
  link: [100,015 times](../facts/sns.md#sns-retry-aws-managed-total-attempts)
  link: [over 23 days](../facts/sns.md#sns-retry-aws-managed-total-attempts)
sqs-wa-loose-coupling-via-intermediate-durable-layer
  claim: To further improve resiliency through loose coupling, make component interactions asynchronous where possible: one component generates events and another consumes them, and the two components do not integrate through direct point-to-point interaction but usually through an intermediate durable storage layer, such as an SQS queue, a streaming data platform such as Kinesis, or Step Functions.
  scope: Well-Architected reliability pillar, REL04-BP02 loosely coupled dependencies.
  link: [an intermediate durable storage layer](../facts/sqs.md#sqs-wa-loose-coupling-via-intermediate-durable-layer)
  link: [such as an Amazon SQS queue](../facts/sqs.md#sqs-wa-loose-coupling-via-intermediate-durable-layer)
