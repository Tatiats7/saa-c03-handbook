facts card: 24 facts
lambda-chaining-anti-pattern-sqs-or-step-functions
  claim: Lambda functions directly calling other Lambda functions is generally an anti-pattern because of cost and complexity (except for durable functions); the two common alternatives are an Amazon SQS queue between the functions or AWS Step Functions.
  scope: Lambda application design; does not apply to durable functions.
  link: [generally an anti-pattern](../facts/lambda.md#lambda-chaining-anti-pattern-sqs-or-step-functions)
  link: [use an Amazon SQS queue between Lambda functions](../facts/lambda.md#lambda-chaining-anti-pattern-sqs-or-step-functions)
  link: [use AWS Step Functions](../facts/lambda.md#lambda-chaining-anti-pattern-sqs-or-step-functions)
  say: function chaining is an anti-pattern
lambda-esm-at-least-once
  claim: Event source mappings process each event at least once, so duplicates can occur and function code should be idempotent.
  scope: event source mappings.
  link: [process each event at least once](../facts/lambda.md#lambda-esm-at-least-once)
  link: [duplicate processing of records can occur](../facts/lambda.md#lambda-esm-at-least-once)
lambda-esm-lambda-polls-source
  claim: With an event source mapping, Lambda itself fetches events from a queue or stream: Lambda handles the polling and invokes your function, so the source service does not push events.
  scope: event source mappings.
  link: [Lambda handles the polling](../facts/lambda.md#lambda-esm-lambda-polls-source)
  link: [Lambda actively fetches](../facts/lambda.md#lambda-esm-lambda-polls-source)
  say: Lambda does the polling for you
lambda-filter-sqs-removes-unmatched
  claim: For an Amazon SQS event source, if a message does not satisfy the filter criteria, Lambda automatically removes the message from the queue, so you do not delete it manually.
  scope: Amazon SQS event source mapping with filters.
  link: [automatically removes the message from the queue](../facts/lambda.md#lambda-filter-sqs-removes-unmatched)
  link: [You don't have to manually delete these messages](../facts/lambda.md#lambda-filter-sqs-removes-unmatched)
  say: Lambda deletes it from the queue for you
lambda-queue-esm-retry-set-on-queue
  claim: For an event source mapping that reads from a queue, the visibility timeout and redrive policy on the source queue determine the time between retries and the destination for failed events.
  scope: event source mapping that reads from a queue.
  link: [visibility timeout and redrive policy](../facts/lambda.md#lambda-queue-esm-retry-set-on-queue)
  link: [on the source queue](../facts/lambda.md#lambda-queue-esm-retry-set-on-queue)
  say: the queue's visibility timeout and redrive policy
lambda-sqs-batch-size
  claim: The SQS event source batch size defaults to 10; the maximum is 10,000 for standard queues and 10 for FIFO queues.
  scope: per SQS event source mapping; default; adjustable.
  link: [10](../facts/lambda.md#lambda-sqs-batch-size)
  link: [For standard queues, the maximum is 10,000](../facts/lambda.md#lambda-sqs-batch-size)
  link: [For FIFO queues, the maximum is 10](../facts/lambda.md#lambda-sqs-batch-size)
lambda-sqs-dlq-maxreceivecount-5
  claim: If the function fails to process a message multiple times, Amazon SQS can send it to a dead-letter queue; AWS recommends setting maxReceiveCount on the source queue's redrive policy to at least 5 so Lambda gets a few retries first.
  scope: Amazon SQS queue used as a Lambda event source; minimum; a recommendation for the redrive policy.
  link: [send it to a dead-letter queue](../facts/lambda.md#lambda-sqs-dlq-maxreceivecount-5)
  link: [at least 5](../facts/lambda.md#lambda-sqs-dlq-maxreceivecount-5)
  say: SQS moves it to the queue's dead-letter queue | at least five
lambda-sqs-partial-batch-response
  claim: With a partial batch response, turned on by specifying ReportBatchItemFailures in FunctionResponseTypes, an SQS event source mapping makes only the failed messages of a batch visible again instead of reprocessing the successful ones.
  scope: Amazon SQS event source mapping; ReportBatchItemFailures is specified.
  link: [partial batch response](../facts/lambda.md#lambda-sqs-partial-batch-response)
  link: [ReportBatchItemFailures](../facts/lambda.md#lambda-sqs-partial-batch-response)
  link: [make only the failed messages visible again](../facts/lambda.md#lambda-sqs-partial-batch-response)
  say: a partial batch response
lambda-sqs-visibility-six-times-timeout
  claim: AWS recommends setting the source queue's visibility timeout to at least six times the function's configured timeout, so that Lambda has time to retry if the function is throttled while processing a previous batch.
  scope: Amazon SQS queue used as a Lambda event source; minimum; a recommendation, not an enforced value.
  link: [at least six times](../facts/lambda.md#lambda-sqs-visibility-six-times-timeout)
  link: [visibility timeout](../facts/lambda.md#lambda-sqs-visibility-six-times-timeout)
  say: at least six times the function timeout
lambda-sqs-max-concurrency-range
  claim: The maximum concurrency setting of an SQS event source accepts a number between 2 and 1,000; leaving it empty turns it off.
  scope: per SQS event source mapping; maximum; not adjustable; an empty value turns maximum concurrency off.
  link: [between 2 and 1,000](../facts/lambda.md#lambda-sqs-max-concurrency-range)
lambda-sqs-max-concurrency-vs-reserved
  claim: Maximum concurrency and reserved concurrency are two independent settings; do not set maximum concurrency higher than the function's reserved concurrency, and if you configure maximum concurrency, keep reserved concurrency greater than or equal to the total maximum concurrency for all SQS event sources on the function, or Lambda might throttle messages.
  scope: per function with SQS event sources.
  link: [reserved concurrency is greater than or equal to](../facts/lambda.md#lambda-sqs-max-concurrency-vs-reserved)
lambda-sqs-fifo-concurrency-message-groups
  claim: For a FIFO queue, concurrent invocations are capped by the number of message group IDs or the maximum concurrency setting, whichever is lower: six message groups with maximum concurrency 10 give at most six concurrent invocations.
  scope: per SQS FIFO event source mapping; maximum.
  link: [six message group IDs and maximum concurrency is set to 10, your function can have a maximum of six concurrent invocations](../facts/lambda.md#lambda-sqs-fifo-concurrency-message-groups)
lambda-trigger-sqs-sns-eventbridge-model
  claim: In their communication model, Amazon SQS is pull-based (consumers poll messages from the queue), Amazon SNS is push-based (subscribers receive messages when published), and EventBridge is event-driven (rules match events and route them to targets).
  scope: Amazon SQS versus Amazon SNS versus Amazon EventBridge.
  link: [Pull-based (consumers poll messages from the queue)](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-model)
  link: [Push-based (subscribers receive messages when published)](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-model)
  link: [rules match events and route to targets](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-model)
lambda-trigger-sqs-sns-eventbridge-use-cases
  claim: Typical uses: SQS for decoupling microservices, buffering requests and processing tasks asynchronously; SNS for fanout notifications and pub/sub messaging; EventBridge for event-driven architectures, real-time stream processing and cross-account event sharing.
  scope: Amazon SQS versus Amazon SNS versus Amazon EventBridge.
  link: [buffering requests](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-use-cases)
  link: [Fanout notifications](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-use-cases)
  link: [cross-account event sharing](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-use-cases)
lambda-trigger-sns-async
  claim: Amazon SNS is an event-driven trigger that invokes a Lambda function asynchronously.
  scope: Amazon SNS as a Lambda trigger.
  link: [Event-driven; asynchronous invocation](../facts/lambda.md#lambda-trigger-sns-async)
  link: [Amazon Simple Notification Service](../facts/lambda.md#lambda-trigger-sns-async)
  say: event-driven, asynchronous invocation
lambda-trigger-eventbridge-async-rules
  claim: EventBridge invokes a Lambda function asynchronously from event buses and rules, and synchronously or asynchronously from pipes.
  scope: Amazon EventBridge as a Lambda trigger.
  link: [asynchronous invocation (event buses and rules)](../facts/lambda.md#lambda-trigger-eventbridge-async-rules)
  link: [synchronous or asynchronous invocation (pipes)](../facts/lambda.md#lambda-trigger-eventbridge-async-rules)
  say: asynchronous for event buses and rules
lambda-trigger-sqs-esm
  claim: Amazon SQS invokes Lambda through an event source mapping.
  scope: Amazon SQS as a Lambda event source.
  link: [Event source mapping](../facts/lambda.md#lambda-trigger-sqs-esm)
  link: [Amazon Simple Queue Service](../facts/lambda.md#lambda-trigger-sqs-esm)
  say: an event source mapping
lambda-sqs-execution-role-read-permissions
  claim: The Lambda testing guide lists, as an example of a configuration problem with Amazon SQS and Lambda, a function execution role that doesn't allow reading messages from the queue (through sqs:ReceiveMessage, sqs:DeleteMessage or sqs:GetQueueAttributes).
  scope: execution role of a function with an SQS event source mapping.
  link: [sqs:ReceiveMessage](../facts/lambda.md#lambda-sqs-execution-role-read-permissions)
  link: [doesn't allow reading messages from the queue](../facts/lambda.md#lambda-sqs-execution-role-read-permissions)
lambda-sqs-scaling-5-batches-300-per-minute-1250
  claim: For a standard SQS queue, Lambda starts with five batches and five concurrent invocations, adds up to 300 more concurrent invokes per minute while messages remain, and one event source mapping can process at most 1,250 invokes simultaneously.
  scope: per SQS event source mapping, standard queue; maximum; not adjustable.
  link: [five batches at a time with five concurrent invocations](../facts/lambda.md#lambda-sqs-scaling-5-batches-300-per-minute-1250)
  link: [up to 300 more concurrent invokes per minute](../facts/lambda.md#lambda-sqs-scaling-5-batches-300-per-minute-1250)
  link: [1,250](../facts/lambda.md#lambda-sqs-scaling-5-batches-300-per-minute-1250)
lambda-sqs-timeout-not-above-visibility
  claim: A function's timeout must be less than or equal to the queue's visibility timeout; Lambda validates this when you create or update an SQS event source mapping and returns an error if the function timeout exceeds the visibility timeout.
  scope: Amazon SQS event source mapping.
  link: [must be less than or equal to](../facts/lambda.md#lambda-sqs-timeout-not-above-visibility)
  link: [returns an error](../facts/lambda.md#lambda-sqs-timeout-not-above-visibility)
  say: the function timeout must not exceed the visibility timeout
lambda-faq-sqs-poll-role-or-queue-policy
  claim: Which SQS queue a function can poll is controlled by the function role or by a resource policy on the queue; when both are present, the more restrictive one applies.
  scope: SQS event sources.
  link: [more restrictive of the two](../facts/lambda.md#lambda-faq-sqs-poll-role-or-queue-policy)
lambda-destination-fifo-unsupported
  claim: An Amazon SQS FIFO queue or an Amazon SNS FIFO topic is an unsupported destination type for asynchronous invocation records; when Lambda cannot send a record to a configured destination, it sends a DestinationDeliveryFailures metric to Amazon CloudWatch.
  scope: asynchronous invocation destinations.
  link: [unsupported destination type](../facts/lambda.md#lambda-destination-fifo-unsupported)
  link: [an Amazon SQS FIFO queue](../facts/lambda.md#lambda-destination-fifo-unsupported)
  link: [DestinationDeliveryFailures metric](../facts/lambda.md#lambda-destination-fifo-unsupported)
  say: FIFO queues and FIFO topics are not supported
lambda-async-destination-targets
  claim: Lambda can send records of asynchronous invocations to a standard SQS queue, a standard SNS topic, an Amazon S3 bucket (on failure only), a Lambda function, or an EventBridge event bus.
  scope: asynchronous invocation destinations; an S3 bucket only for failed invocations.
  link: [A standard SQS queue](../facts/lambda.md#lambda-async-destination-targets)
  link: [A standard SNS topic](../facts/lambda.md#lambda-async-destination-targets)
  link: [An Amazon S3 bucket (on failure only)](../facts/lambda.md#lambda-async-destination-targets)
  link: [A Lambda function](../facts/lambda.md#lambda-async-destination-targets)
  link: [An EventBridge event bus](../facts/lambda.md#lambda-async-destination-targets)
  say: a standard SQS queue
lambda-case-doordash-sqs-buffer
  claim: DoorDash connected Amazon API Gateway to Amazon SQS to decouple submission processing, and ran a Lambda function that retrieved data from SQS and sent it to Amazon Data Firehose (named Kinesis Data Firehose in the case study).
  scope: DoorDash case study.
  link: [to decouple submission processing](../facts/lambda.md#lambda-case-doordash-sqs-buffer)
