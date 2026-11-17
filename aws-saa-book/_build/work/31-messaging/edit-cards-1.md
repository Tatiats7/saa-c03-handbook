facts card: 18 facts
sqs-fifo-deduplication-interval-5-minutes
  claim: In an SQS FIFO queue, messages with the same deduplication ID sent within a 5 minute deduplication interval are treated as duplicates, and only one copy is delivered.
  scope: per FIFO queue, per message deduplication ID; fixed; not adjustable.
  link: [5 minute deduplication interval](../facts/sqs.md#sqs-fifo-deduplication-interval-5-minutes)
  link: [only one copy is delivered](../facts/sqs.md#sqs-fifo-deduplication-interval-5-minutes)
  say: five minutes
sqs-consumers-keep-idempotency-tokens-ignore-duplicates
  claim: A message that was published once may be delivered more than once. A publisher can include idempotency tokens, and consumers should keep track of each token received and ignore messages with duplicate tokens.
  scope: event-driven architectures with message queues.
  link: [may be accidentally delivered more than once](../facts/sqs.md#sqs-consumers-keep-idempotency-tokens-ignore-duplicates)
  link: [keep track of each token received](../facts/sqs.md#sqs-consumers-keep-idempotency-tokens-ignore-duplicates)
sqs-visibility-timeout-too-long-delays-retry
  claim: A visibility timeout that is far longer than the processing time makes you wait a long time before a failed message can be processed again.
  scope: SQS queue; visibility timeout much longer than processing time.
  link: [wait for a relatively long time](../facts/sqs.md#sqs-visibility-timeout-too-long-delays-retry)
  link: [to attempt to process the message again](../facts/sqs.md#sqs-visibility-timeout-too-long-delays-retry)
sqs-dlq-max-receive-count-meaning
  claim: A redrive policy sets maxReceiveCount, the number of times a consumer can receive a message from the source queue before SQS moves it to the dead-letter queue.
  scope: SQS redrive policy, per source queue.
  link: [number of times a consumer can receive](../facts/sqs.md#sqs-dlq-max-receive-count-meaning)
  link: [before it is moved to a dead-letter queue](../facts/sqs.md#sqs-dlq-max-receive-count-meaning)
sqs-undeleted-message-visible-again
  claim: If the consumer does not delete a message before the visibility timeout expires, the message becomes visible again in the queue and another consumer can retrieve it.
  scope: SQS queue; message not deleted before the visibility timeout expires.
  link: [becomes visible again in the queue](../facts/sqs.md#sqs-undeleted-message-visible-again)
  link: [retrieved by another consumer](../facts/sqs.md#sqs-undeleted-message-visible-again)
eventbridge-dlq-is-standard-sqs-queue
  claim: EventBridge dead-letter queues are standard SQS queues that EventBridge uses to store events that could not be delivered to a target.
  scope: EventBridge rule target.
  link: [standard Amazon SQS queues](../facts/eventbridge.md#eventbridge-dlq-is-standard-sqs-queue)
  link: [events that couldn't successfully be delivered](../facts/eventbridge.md#eventbridge-dlq-is-standard-sqs-queue)
eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule
  claim: Event Replay lets you reprocess past events back to an event bus or a specific EventBridge rule.
  scope: per archive.
  link: [reprocess past events](../facts/eventbridge.md#eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule)
  link: [specific EventBridge rule](../facts/eventbridge.md#eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule)
sqs-delay-queue-range
  claim: If you create an SQS delay queue, messages that you send to the queue remain invisible to consumers for the delay period; the default (minimum) delay for a queue is 0 seconds and the maximum is 15 minutes.
  scope: per queue (delay queue); maximum; not adjustable.
  link: [0 seconds](../facts/sqs.md#sqs-delay-queue-range)
  link: [15 minutes](../facts/sqs.md#sqs-delay-queue-range)
  say: zero seconds | fifteen minutes
sqs-message-timer-range
  claim: The delay for an individual SQS message (message timer) is 0 seconds by default, which is also the minimum, and the maximum is 15 minutes.
  scope: per message (message timer); maximum; not adjustable; The default and minimum delay is 0 seconds..
  link: [0 seconds](../facts/sqs.md#sqs-message-timer-range)
  link: [15 minutes](../facts/sqs.md#sqs-message-timer-range)
  say: zero seconds | fifteen minutes
sqs-eventbridge-scheduler-for-advanced-scheduling
  claim: SQS delay queues and message timers allow scheduling of message delivery up to 15 minutes in the future. For more flexible scheduling, EventBridge Scheduler, which can schedule one-time or recurring API actions without time limitations, is the recommended solution for advanced message scheduling use cases.
  scope: message scheduling.
  link: [EventBridge Scheduler is the recommended solution](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling)
  link: [advanced message scheduling use cases](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling)
  link: [up to 15 minutes in the future](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling)
sqs-metric-not-visible-messages-is-in-flight
  claim: The ApproximateNumberOfMessagesNotVisible metric counts in-flight messages: messages that were received but not yet deleted or expired. Use it to track processing delays or stuck consumers.
  scope: SQS queue CloudWatch metric.
  link: [ApproximateNumberOfMessagesNotVisible](../facts/sqs.md#sqs-metric-not-visible-messages-is-in-flight)
  link: [received but not yet deleted or expired](../facts/sqs.md#sqs-metric-not-visible-messages-is-in-flight)
sqs-metric-visible-messages-is-backlog
  claim: The ApproximateNumberOfMessagesVisible metric counts the messages currently available for retrieval and processing. It reflects the current processing backlog in the queue.
  scope: SQS queue CloudWatch metric.
  link: [ApproximateNumberOfMessagesVisible](../facts/sqs.md#sqs-metric-visible-messages-is-backlog)
  link: [available for retrieval and processing](../facts/sqs.md#sqs-metric-visible-messages-is-backlog)
sqs-metric-age-of-oldest-message-measures-lag
  claim: The ApproximateAgeOfOldestMessage metric reports, in seconds, the age of the oldest unprocessed message in the queue. It is reported if the queue contains at least one active message.
  scope: SQS queue CloudWatch metric.
  link: [ApproximateAgeOfOldestMessage](../facts/sqs.md#sqs-metric-age-of-oldest-message-measures-lag)
  link: [oldest unprocessed message in the queue](../facts/sqs.md#sqs-metric-age-of-oldest-message-measures-lag)
eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners
  claim: EventBridge is the only event-based service that integrates directly with third-party SaaS partners.
  scope: EventBridge versus SNS.
  link: [only event-based service](../facts/eventbridge.md#eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners)
  link: [third-party SaaS partners](../facts/eventbridge.md#eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners)
eventbridge-default-bus-receives-aws-service-events
  claim: Every account has a default event bus that automatically receives events from AWS services.
  scope: per account, per Region.
  link: [default event bus](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events)
  link: [automatically receives events from AWS services](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events)
sns-filter-default-every-message
  claim: By default, an SNS topic subscriber receives every message published to the topic. To receive only a subset of the messages, the subscriber must assign a filter policy to the subscription.
  scope: SNS subscription; default; adjustable; no filter policy assigned.
  link: [receives every message that's published to the topic](../facts/sns.md#sns-filter-default-every-message)
  link: [assign a filter policy to the topic subscription](../facts/sns.md#sns-filter-default-every-message)
sns-filter-nonmatching-message-not-sent
  claim: SNS sends a message to a subscriber only if all message attributes or message body properties satisfy the conditions in the filter policy. Otherwise SNS does not send the message to that subscriber.
  scope: SNS subscription with a filter policy.
  link: [satisfy the conditions specified in the filter policy](../facts/sns.md#sns-filter-nonmatching-message-not-sent)
  link: [doesn't send the message to that subscriber](../facts/sns.md#sns-filter-nonmatching-message-not-sent)
sqs-typically-single-subscriber-order-and-loss
  claim: SQS typically processes messages through a single subscriber, which is ideal for workflows where order and loss prevention are critical; to distribute wider, combine SQS with SNS for a fanout pattern.
  scope: SQS developer guide overview (SQS, SNS and Amazon MQ).
  link: [a single subscriber typically](../facts/sqs.md#sqs-typically-single-subscriber-order-and-loss)
  link: [fanout messaging pattern](../facts/sqs.md#sqs-typically-single-subscriber-order-and-loss)
