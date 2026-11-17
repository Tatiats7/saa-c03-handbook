# brief-31, part E: question slots and the question plan.


def slot(qid, bullet, concept, difficulty, typ, layer, ee, sec, trap, dtraps, key_facts, note, **extra):
    d = {"bullet": bullet, "concept": concept, "difficulty": difficulty, "type": typ, "layer": layer, "exam_english": ee,
         "section": "2-deep.md#" + SID[sec], "trap": trap, "distractor_traps": dtraps}
    d.update(extra)
    d["key_facts"] = key_facts
    d["note"] = note
    d["id"] = qid
    BRIEF["question_slots"].append(d)


BRIEF["question_slots"] = []

SHARED_A = ("Shared stem of twin pair A (q01, q07): 'A company runs an order API on Amazon EC2 instances. The API writes each order "
            "directly to a relational database. During sales, the database cannot keep up, requests time out, and orders are "
            "lost.' Ask: 'Which solution meets these requirements with the LEAST operational overhead?' Options identical in "
            "q01 and q07, in neutral words: (A) Send each order to an Amazon SQS queue. Have the order service poll the queue "
            "and write each order to the database. (B) Publish each order to an Amazon SNS topic. Subscribe one Amazon SQS "
            "queue for each service that processes orders. (C) Publish each order to an Amazon SNS topic. Subscribe the HTTPS "
            "endpoint of each service that processes orders. (D) Move the database to a larger instance class and add a read "
            "replica.")
SHARED_B = ("Shared stem of twin pair B (q02, q09): 'A company runs workers in an Auto Scaling group. The workers poll an Amazon "
            "SQS standard queue and delete each message after they process it.' Ask: 'Which change will resolve this issue "
            "with the LEAST operational overhead?' Options identical: (A) Increase the visibility timeout of the queue to "
            "longer than the longest processing time. (B) Configure a dead-letter queue and a redrive policy for the queue. (C) "
            "Set the receive message wait time of the queue to 20 seconds. (D) Create a FIFO queue and move the producers and "
            "the workers to it.")
SHARED_C = ("Shared stem of twin pair C (q13, q18): 'A company is building an event-driven platform. Several teams' services "
            "must react to events, and each service needs only some of the events.' Ask: 'Which solution meets these "
            "requirements with the LEAST operational overhead?' Options identical: (A) An Amazon EventBridge event bus with one "
            "rule for each service. (B) An Amazon SNS topic with a filter policy on each subscription. (C) One Amazon SQS queue "
            "that every service polls. (D) An Amazon Kinesis data stream that every service reads.")

slot("q01", "3.2.S1", "sqs-buffer-for-overloaded-database", 2, "single", "core",
     ["ee-least-operational-overhead"], 1, "messaging-trap-topic-stores-messages", [],
     ["sqs-decision-keeps-until-processed", "sqs-decision-typical-use", "sns-decision-no-persistence",
      "sns-retry-http-total-retry-time-max"],
     SHARED_A + " Changed phrase of q01: 'Only the company's order service processes the orders. The order service must "
     "process every order, even after it has been offline for a few hours.' Key (A): the queue keeps each order [until "
     "successfully processed or expired] (sqs-decision-keeps-until-processed); [buffering requests] (sqs-decision-typical-use). "
     "(B) violates-qualifier: a topic adds a part when only one service consumes. (C) carries "
     "messaging-trap-topic-stores-messages: [Messages are not persisted] (sns-decision-no-persistence), and HTTP/S retries end "
     "after at most [3,600 seconds] (sns-retry-http-total-retry-time-max). (D) misconception: a larger database does not keep "
     "orders while the order service is offline and still takes every write at the peak. Bullets also 2.1.S3, 2.1.K2.",
     twin="first of strict twin pair A (twin q07)")
slot("q02", "2.1.K11", "visibility-timeout-shorter-than-processing", 2, "single", "core",
     ["ee-least-operational-overhead"], 3, "messaging-trap-short-visibility-safer", [],
     ["sqs-visibility-timeout-default", "sqs-visibility-timeout-too-short-gives-duplicate", "sqs-undeleted-message-visible-again"],
     SHARED_B + " Changed phrase of q02: 'Processing a message takes up to 4 minutes. The queue uses the default visibility "
     "timeout, and many messages are processed by two different workers.' Key (A): the default [30 seconds] "
     "(sqs-visibility-timeout-default) ends while the first worker still works, so [a duplicate message is received by another "
     "consumer] (sqs-visibility-timeout-too-short-gives-duplicate). (B) misconception: a dead-letter queue sets failing messages "
     "aside; it does not stop a second receive. (C) misconception: long polling only waits for messages: [reduce the number of "
     "empty receives] (sqs-faq-long-polling-fewer-empty-receives-lower-cost). (D) violates-qualifier: you [cannot convert an "
     "existing standard queue] (sqs-cannot-convert-standard-queue-to-fifo), so it is a new queue and a migration, and a FIFO "
     "queue also returns a message whose visibility timeout ends. Bullets also 3.2.K3.",
     twin="first of strict twin pair B (twin q09)")
slot("q03", "2.1.K11", "receive-does-not-delete", 1, "single", "core", [], 3, "messaging-trap-receive-deletes", [],
     ["sqs-receive-keeps-message-hidden", "sqs-undeleted-message-visible-again", "sqs-manual-delete-after-processing"],
     "Difficulty 1, qualifier none (no violates-qualifier option). 'A consumer application receives a message from an Amazon "
     "SQS standard queue and processes it successfully. The application does not call DeleteMessage. The queue uses its "
     "default settings. What happens to the message?' Key: it becomes visible again when the visibility timeout ends, and a "
     "consumer receives it again ([becomes visible again in the queue] (sqs-undeleted-message-visible-again)). Distractors: SQS "
     "deleted it when the consumer received it (trap messaging-trap-receive-deletes; why links [temporarily invisible to other "
     "consumers] (sqs-receive-keeps-message-hidden)); SQS moves it to a dead-letter queue at once (misconception: only a "
     "redrive policy moves messages, after the [number of times a consumer can receive] (sqs-dlq-max-receive-count-meaning)); it "
     "stays hidden until the retention period ends (misconception: it is hidden only for the visibility timeout). Bullets also "
     "3.2.K3.")
slot("q04", "2.1.S1", "idempotent-consumer-for-duplicates", 2, "single", "core", ["ee-best"], 4,
     "messaging-trap-standard-exactly-once", [],
     ["sqs-standard-at-least-once-duplicates", "sqs-faq-standard-queue-design-idempotent-consumers",
      "sqs-consumers-keep-idempotency-tokens-ignore-duplicates", "sqs-fifo-deduplication-interval-5-minutes"],
     "'A payment service reads orders from an Amazon SQS standard queue and charges the customer for each order. Sometimes a "
     "customer is charged twice for one order. The payment provider also retries some requests, and its duplicates can arrive "
     "hours apart. Which solution will BEST prevent duplicate charges?' Key: make the consumer idempotent: record each order "
     "ID with a conditional write and skip an ID that is already recorded ([keep track of each token received] "
     "(sqs-consumers-keep-idempotency-tokens-ignore-duplicates); [design your applications to be idempotent] "
     "(sqs-faq-standard-queue-design-idempotent-consumers)). Distractors: increase the visibility timeout to its maximum "
     "(misconception: copies on several servers also repeat a message: [more than one copy of a message] "
     "(sqs-standard-at-least-once-duplicates)); replace the queue with a FIFO queue with content-based deduplication "
     "(misconception: deduplication covers only the [5 minute deduplication interval] (sqs-fifo-deduplication-interval-5-minutes), "
     "and the provider's duplicates arrive later); keep the queue and only fix the provider integration, because a standard "
     "queue delivers each message once (trap messaging-trap-standard-exactly-once). The BEST qualifier: the key is the only "
     "option that covers both sources of duplicates. Bullets also 2.1.K11, 3.2.S1.")
slot("q05", "3.2.K3", "pub-sub-topic-basics", 1, "single", "core", [], 9, "messaging-trap-queue-broadcasts", [],
     ["sns-faq-publish-triggers-delivery-to-all-subscribers", "sns-decision-typical-use", "sqs-typically-single-subscriber-order-and-loss"],
     "Difficulty 1, qualifier none. 'An order service must send each order event to three other microservices at the same "
     "time. Each microservice must receive every event. Which AWS service provides this publish/subscribe model?' Key: an "
     "Amazon SNS topic with one subscription for each microservice ([all applicable subscribers] "
     "(sns-faq-publish-triggers-delivery-to-all-subscribers)). Distractors: one Amazon SQS standard queue that the three "
     "microservices poll (trap messaging-trap-queue-broadcasts; why links [a single subscriber typically] "
     "(sqs-typically-single-subscriber-order-and-loss)); an SQS FIFO queue with one message group for each microservice "
     "(misconception: each message still goes to one consumer); Amazon EventBridge Scheduler with one schedule for each "
     "microservice (misconception: a schedule starts work at set times; it does not forward events). Do not offer an "
     "EventBridge event bus as an option: a rule with several targets would also be right. Bullets also 2.1.K11.")
slot("q06", "2.1.K5", "eventbridge-rule-for-aws-service-events", 2, "single", "core",
     ["ee-least-operational-overhead"], 12, None, ["how-the-exam-asks-trap-keyword-bait"],
     ["eventbridge-default-bus-receives-aws-service-events", "eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel",
      "eventbridge-target-types-list"],
     "'Whenever an Amazon EC2 instance in the account changes to the stopped state, the operations team must receive an "
     "email, and an existing AWS Lambda function must create a ticket. Which solution meets these requirements with the LEAST "
     "operational overhead?' Key: an EventBridge rule on the default event bus that matches EC2 state-change events with the "
     "state stopped, with two targets: an SNS topic that has an email subscription, and the Lambda function (the default bus "
     "[automatically receives events from AWS services] (eventbridge-default-bus-receives-aws-service-events); a rule can "
     "[route to multiple targets] (eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel)). Distractors: a Lambda "
     "function that runs every minute, calls DescribeInstances and compares states (violates-qualifier); an AWS CloudTrail "
     "trail to an S3 bucket with an S3 event notification that invokes a function that reads the logs (violates-qualifier); a "
     "shutdown script on every instance that publishes to an SNS topic (violates-requirement: it misses stops that the script "
     "does not see; keyword bait for 'event-driven': how-the-exam-asks-trap-keyword-bait only if the option text repeats a stem "
     "keyword). Bullets also 2.1.S3, 2.1.S1.")
slot("q07", "2.1.S3", "fan-out-every-service-gets-every-message", 2, "single", "core",
     ["ee-least-operational-overhead"], 10, "messaging-trap-queue-broadcasts", ["messaging-trap-topic-stores-messages"],
     ["sns-faq-fanout-identical-messages-to-multiple-sqs-queues", "sns-with-sqs-prevents-loss-for-offline-subscribers",
      "sqs-typically-single-subscriber-order-and-loss"],
     SHARED_A + " Changed phrase of q07: 'The order service, the shipping service and the analytics service must each process "
     "every order. Each service must process every order, even after it has been offline for a few hours.' Key (B): subscribe "
     "[multiple SQS standard queues to the SNS topic] (sns-faq-fanout-identical-messages-to-multiple-sqs-queues), which prevents "
     "loss [when subscribers are offline] (sns-with-sqs-prevents-loss-for-offline-subscribers). (A) carries "
     "messaging-trap-queue-broadcasts: a queue has [a single subscriber typically] (sqs-typically-single-subscriber-order-and-loss). "
     "(C) carries messaging-trap-topic-stores-messages. (D) misconception as in q01. Bullets also 3.2.S1, 2.1.S1.",
     twin_of="q01")
slot("q08", "3.2.S2", "scale-workers-on-backlog-per-instance", 2, "single", "core", ["ee-best"], 7,
     "auto-scaling-trap-queue-length-metric", [],
     ["ec2-auto-scaling-sqs-backlog-per-instance", "ec2-auto-scaling-sqs-backlog-per-instance-metric-math",
      "ec2-auto-scaling-sqs-queue-length-not-proportional", "ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target"],
     "'A company processes images from an Amazon SQS queue with EC2 instances in an Auto Scaling group. Every message takes "
     "about the same time to process. The number of uploads changes during the day, and each image must be processed within a "
     "set time. The group uses target tracking on average CPU utilization, and messages often wait too long. Which metric "
     "should the target tracking policy use to BEST meet the processing-time goal?' Key: the backlog per instance, the "
     "ApproximateNumberOfMessagesVisible metric divided by GroupInServiceInstances with metric math, with the acceptable "
     "backlog per instance as the target ([backlog per instance] (ec2-auto-scaling-sqs-backlog-per-instance); "
     "[GroupInServiceInstances] (ec2-auto-scaling-sqs-backlog-per-instance-metric-math)). Distractors: "
     "ApproximateNumberOfMessagesVisible alone (trap auto-scaling-trap-queue-length-metric; why links [might not change "
     "proportionally] (ec2-auto-scaling-sqs-queue-length-not-proportional)); ApproximateNumberOfMessagesNotVisible "
     "(misconception: it counts in-flight messages: [received but not yet deleted or expired] "
     "(sqs-metric-not-visible-messages-is-in-flight)); NumberOfMessagesSent (misconception: it counts arrivals, not the wait). "
     "Worked think-aloud: find the constraint (the processing-time goal; load that changes), predict, eliminate, choose. "
     "Bullets also 3.2.S1.",
     worked="worked think-aloud, no wrong path")
slot("q09", "2.1.K11", "poison-message-dead-letter-queue", 2, "single", "core", ["ee-least-operational-overhead"], 6, None, [],
     ["sqs-dlq-max-receive-count-meaning", "sqs-faq-dlq-definition-isolate-unprocessable-messages",
      "sqs-visibility-timeout-too-long-delays-retry"],
     SHARED_B + " Changed phrase of q09: 'Processing a message takes a few seconds. A few malformed messages fail every time, "
     "and the workers receive them again and again for days.' Key (B): a redrive policy moves a message after the [number of "
     "times a consumer can receive] (sqs-dlq-max-receive-count-meaning) it; the dead-letter queue keeps messages the consumer "
     "is [unable to consume the messages successfully] (sqs-faq-dlq-definition-isolate-unprocessable-messages). (A) "
     "misconception: a longer timeout only spaces out the failures: [wait for a relatively long time] "
     "(sqs-visibility-timeout-too-long-delays-retry). (C) misconception. (D) violates-qualifier. Bullets also 2.1.K2, 3.2.S1.",
     twin_of="q02")
slot("q10", "3.2.S2", "age-of-oldest-message-alarm", 1, "single", "core", ["ee-monitor"], 7, None, [],
     ["sqs-metric-age-of-oldest-message-measures-lag", "sqs-metric-not-visible-messages-is-in-flight"],
     "Difficulty 1, qualifier none. 'A company wants to monitor an Amazon SQS queue and receive an alarm when messages wait too "
     "long before a consumer processes them. Which Amazon CloudWatch metric should the alarm use?' Key: "
     "ApproximateAgeOfOldestMessage ([oldest unprocessed message in the queue] "
     "(sqs-metric-age-of-oldest-message-measures-lag)). Distractors: ApproximateNumberOfMessagesNotVisible (misconception: "
     "in-flight messages); NumberOfMessagesSent (misconception: arrivals); CPUUtilization of the consumer instances "
     "(misconception: [100% CPU utilization is expected and should not be your primary metric] "
     "(ec2-auto-scaling-wa-queue-depth-metric-for-batch-work) for batch work). Bullets also 3.2.S1.")
slot("q11", "3.2.K3", "fifo-group-id-per-customer", 2, "multi", "core", ["ee-select-two", "ee-least-operational-overhead"], 5,
     "messaging-trap-fifo-global-order", ["messaging-trap-standard-exactly-once"],
     ["sqs-fifo-order-strict-within-group", "sqs-fifo-groups-processed-in-parallel", "sqs-faq-fifo-exactly-once-processing",
      "sqs-fifo-no-order-across-groups"],
     "Select TWO, five options. 'A company sends account events for many customers to Amazon SQS. The events of each customer "
     "must be processed exactly once and in the order they were sent. Events of different customers must be processed in "
     "parallel by many consumers. Which TWO actions should a solutions architect take to meet these requirements with the "
     "LEAST operational overhead? (Select TWO.)' Keys: use an SQS FIFO queue ([exactly-once processing] "
     "(sqs-faq-fifo-exactly-once-processing)); set the message group ID to the customer ID (order [within a message group ID] "
     "(sqs-fifo-order-strict-within-group); [parallel processing of messages] (sqs-fifo-groups-processed-in-parallel)). "
     "Distractors: give each event a random message group ID, because a FIFO queue keeps the order of all events (trap "
     "messaging-trap-fifo-global-order; why links [may arrive or be processed out of order] (sqs-fifo-no-order-across-groups)); "
     "use one message group ID for all events (violates-requirement: no parallel work, because FIFO queues do not serve "
     "one group to [more than one consumer at a time] (sqs-faq-fifo-same-group-one-consumer-at-a-time)); use an SQS standard queue, which delivers each message once "
     "and in order (trap messaging-trap-standard-exactly-once). Bullets also 2.1.K11.")
slot("q12", "2.1.S3", "sns-filter-policy-per-subscription", 2, "single", "extended", ["ee-least-development-effort"], 11,
     "messaging-trap-filter-needs-function", [],
     ["sns-filter-default-every-message", "sns-filter-nonmatching-message-not-sent", "sns-faq-message-filtering-subscribers-receive-subset"],
     "'An Amazon SNS topic receives every order event of a company, with a message attribute that holds the order type. Three "
     "Amazon SQS queues are subscribed. A Lambda function between the topic and the returns queue copies only return events "
     "into that queue. The company wants to remove the function with the LEAST development effort.' Key: subscribe the returns "
     "queue to the topic directly with a filter policy that matches the order type 'return' ([assign a filter policy to the "
     "topic subscription] (sns-filter-default-every-message)). Distractors: keep a function for filtering, because SNS sends "
     "every message to every subscriber (trap messaging-trap-filter-needs-function); create one topic for each order type and "
     "change the publishers (violates-qualifier); replace the topic with an EventBridge event bus and rules (violates-qualifier: "
     "publishers and consumers change). Bullets also 3.2.K3.")
slot("q13", "2.1.S3", "eventbridge-vs-sns-routing", 2, "single", "extended", ["ee-least-operational-overhead"], 12, None,
     ["messaging-trap-queue-broadcasts"],
     ["eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners",
      "eventbridge-faq-eventbridge-recommended-for-app-saas-aws-events", "eventbridge-default-bus-receives-aws-service-events",
      "eventbridge-pattern-matches-metadata-data-content"],
     SHARED_C + " Changed phrase of q13: 'The events come from AWS services, from the company's own applications and from a "
     "SaaS partner's application. Each service selects events by fields inside the event detail.' Key (A): EventBridge is the "
     "[only event-based service] (eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners) that "
     "integrates with [third-party SaaS partners] (eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners), "
     "and patterns test [event metadata, and/or event detail values] (eventbridge-pattern-matches-metadata-data-content). (B) "
     "violates-qualifier: AWS service and SaaS events would need EventBridge in front of the topic. (C) carries "
     "messaging-trap-queue-broadcasts. (D) misconception: a stream for [real-time processing of streaming big data] "
     "(sqs-faq-kinesis-streams-realtime-and-replay), with code in every reader. Bullets also 2.1.K5.",
     twin="first of strict twin pair C (twin q18)")
slot("q14", "3.2.S1", "lambda-partial-batch-response", 3, "single", "extended", ["ee-most-operationally-efficient"], 8,
     "messaging-trap-lambda-retries-failed-only", ["lambda-trap-function-dlq-for-sqs", "messaging-trap-short-visibility-safer"],
     ["lambda-sqs-partial-batch-response", "lambda-queue-esm-retry-set-on-queue"],
     "'A Lambda function reads an Amazon SQS standard queue with a batch size of 10. When one message of a batch is "
     "malformed, the function returns an error. The other nine messages are processed again and again, and at last all ten "
     "move to the dead-letter queue. Which solution will retry only the malformed message in the MOST operationally efficient "
     "way?' Key: turn on ReportBatchItemFailures and have the function return the IDs of the failed messages ([make only the "
     "failed messages visible again] (lambda-sqs-partial-batch-response)). Distractors: set the batch size to 1 "
     "(violates-qualifier: many more invocations); configure an on-failure destination or a dead-letter queue on the function "
     "(trap lambda-trap-function-dlq-for-sqs; why links [visibility timeout and redrive policy] "
     "(lambda-queue-esm-retry-set-on-queue)); lower the visibility timeout of the queue so that failures come back sooner "
     "(trap messaging-trap-short-visibility-safer). Bullets also 2.1.S1, 2.1.K5.")
slot("q15", "2.1.K2", "dlq-retention-longer-than-source", 3, "single", "extended", ["ee-retain", "ee-least-operational-overhead"],
     6, "messaging-trap-dlq-fresh-retention", [],
     ["sqs-dlq-standard-enqueue-timestamp-unchanged", "sqs-dlq-retention-longer-than-source-queue", "sqs-message-retention-range"],
     "'An Amazon SQS standard queue and its dead-letter queue both keep the default retention period. Failed messages "
     "disappear from the dead-letter queue before the support team reviews them. The company must retain each failed message "
     "for at least 10 days after it was first sent. Which solution meets this requirement with the LEAST operational "
     "overhead?' Key: set the retention period of the dead-letter queue to 14 days ([14 days] (sqs-message-retention-range)), "
     "because [the enqueue timestamp is unchanged] (sqs-dlq-standard-enqueue-timestamp-unchanged) when a message moves. "
     "Distractors: set only the source queue's retention to 14 days (misconception: the dead-letter queue's own retention "
     "deletes the message; why links [longer than the retention period] (sqs-dlq-retention-longer-than-source-queue)); raise "
     "maxReceiveCount (misconception: the message stays longer in the source queue, but the clock still runs from the first "
     "send); have a scheduled Lambda function copy the dead-letter messages to Amazon S3 every day (violates-qualifier). Write "
     "the belief of the trap into the stem's situation, not into an option: the team assumed the move restarted the clock. "
     "Bullets also 2.1.K11.")
slot("q16", "1.1.S5", "sns-to-sqs-queue-policy", 2, "single", "extended", ["ee-most-secure"], 10,
     "messaging-trap-subscribe-without-queue-policy", [],
     ["sns-sqs-queue-needs-policy-allowing-topic", "sns-queue-policy-sourcearn-limits-to-one-topic", "sqs-default-access-policy-owner-only"],
     "'An Amazon SNS topic and an Amazon SQS queue are in the same AWS account. A developer subscribed the queue to the topic, "
     "and the subscription is active. Messages published to the topic never arrive in the queue. The queue has its default "
     "access policy. Which change will deliver the messages in the MOST secure way?' Key: add a statement to the queue's "
     "access policy that allows the SNS service principal to call sqs:SendMessage, with an aws:SourceArn condition that names "
     "the topic ARN ([set a policy on the Amazon SQS queue] (sns-sqs-queue-needs-policy-allowing-topic); [aws:SourceArn "
     "condition] (sns-queue-policy-sourcearn-limits-to-one-topic)). Distractors: allow every principal (*) to call "
     "sqs:SendMessage with no condition (violates-qualifier); confirm the subscription with ConfirmSubscription (misconception: "
     "a same-account queue subscription needs no [opt-in] (sns-faq-same-account-sqs-subscription-needs-no-opt-in)); keep the "
     "subscription and wait, because a subscription is all SNS needs (trap messaging-trap-subscribe-without-queue-policy). "
     "Bullets also 2.1.S3.")
slot("q17", "2.1.K5", "eventbridge-archive-and-replay", 3, "single", "extended", ["ee-least-operational-overhead"], 13,
     "messaging-trap-bus-stores-events", [],
     ["eventbridge-classic-bus-does-not-retain-events", "eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule",
      "eventbridge-replay-to-source-bus-only"],
     "'A company publishes orders to a custom Amazon EventBridge event bus. A rule sends them to a Lambda function. Last week "
     "a bug made the function process orders wrongly for several hours, and the company could not process those events again. "
     "After any future bug, the company must be able to process the events of the last 30 days again. Which solution meets "
     "this requirement with the LEAST operational overhead?' Key: create an archive of the bus that keeps events for 30 days, "
     "and after a fix start a replay of the affected time window ([reprocess past events] "
     "(eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule)). Distractors: read the past events again from the "
     "event bus (trap messaging-trap-bus-stores-events; why links [Not retained. To keep events, add an archive.] "
     "(eventbridge-classic-bus-does-not-retain-events)); add a dead-letter queue to the target (misconception: a dead-letter "
     "queue holds only events that could not be delivered, and these were delivered); add a rule that sends every event "
     "through Amazon Data Firehose to Amazon S3 and write a tool that publishes them again (violates-qualifier). Bullets also "
     "2.1.S1.")
slot("q18", "2.1.S1", "eventbridge-vs-sns-routing", 2, "single", "extended", ["ee-least-operational-overhead"], 9, None,
     ["messaging-trap-queue-broadcasts"],
     ["sns-a2p-subscriber-types", "sns-faq-sns-recommended-for-high-fan-out-thousands-or-millions", "sns-decision-filter-policies",
      "eventbridge-target-types-list"],
     SHARED_C + " Changed phrase of q18: 'All events come from the company's own order application. Every event must also "
     "reach the customers' mobile phones by SMS within seconds.' Key (B): SNS reaches [mobile applications, mobile phone "
     "numbers, and email addresses] (sns-a2p-subscriber-types) and suits [thousands or millions of endpoints] "
     "(sns-faq-sns-recommended-for-high-fan-out-thousands-or-millions); each service filters with [subscription filter "
     "policies] (sns-decision-filter-policies). (A) violates-qualifier: EventBridge targets do not include phone numbers, so a "
     "topic would be needed behind the rules (link the target list: [Lambda function (ASYNC)] (eventbridge-target-types-list) "
     "only if the why names targets). (C) carries messaging-trap-queue-broadcasts. (D) misconception. Bullets also 3.2.K3.",
     twin_of="q13")
slot("q19", "3.2.K3", "sns-subscription-dead-letter-queue", 3, "multi", "extended", ["ee-select-two", "ee-least-operational-overhead"],
     13, "messaging-trap-dlq-on-topic", ["messaging-trap-topic-stores-messages"],
     ["sns-dlq-attached-to-subscription-not-topic", "sns-dlq-same-account-and-region-as-subscription",
      "sns-retry-exhausted-discards-unless-dlq", "sns-dlq-queue-type-matches-topic-type"],
     "Select TWO, five options. 'An Amazon SNS standard topic delivers order events to a partner's HTTPS endpoint and to an "
     "Amazon SQS queue. The partner endpoint is sometimes down for several hours, and the events for the partner are lost. "
     "The company must keep the undelivered events so that it can send them again later. Which TWO actions meet these "
     "requirements with the LEAST operational overhead? (Select TWO.)' Keys: create an SQS standard queue in the same AWS "
     "account and Region as the subscription ([same AWS account and Region] (sns-dlq-same-account-and-region-as-subscription)); "
     "set that queue as the dead-letter queue (redrive policy) of the HTTPS subscription ([attached to an Amazon SNS "
     "subscription] (sns-dlq-attached-to-subscription-not-topic)). Distractors: attach the dead-letter queue to the topic (trap "
     "messaging-trap-dlq-on-topic); use an SQS FIFO queue as the dead-letter queue ([standard topic subscriptions use standard "
     "queues] (sns-dlq-queue-type-matches-topic-type)); raise the HTTPS delivery retry policy to keep trying for 24 hours "
     "(impossible-feature: at most [3,600 seconds] (sns-retry-http-total-retry-time-max); the one impossible-feature option of "
     "the question). The topic keeps nothing itself: messaging-trap-topic-stores-messages may tag a fifth option 'rely on the "
     "topic to hold the events until the endpoint returns' if the writer uses it. Bullets also 2.1.S1, 2.1.K5.")
slot("q20", "1.1.S5", "cross-account-queue-access-policy", 3, "single", "extended", ["ee-least-privilege", "ee-most-secure"], 14,
     "messaging-trap-iam-policy-enough-cross-account", ["iam-trap-cross-account-one-policy"],
     ["sqs-cross-account-needs-queue-access-policy", "sqs-default-access-policy-owner-only"],
     "'An application in account B runs with an IAM role. The role's policy allows sqs:SendMessage on an Amazon SQS queue in "
     "account A. Every call fails with an access denied error. The queue uses SSE-SQS. Which solution grants access MOST "
     "securely and follows the principle of least privilege?' Key: add a statement to the queue's access policy in account A "
     "that allows the role's ARN to call sqs:SendMessage on that queue ([configure the queue's access policy] "
     "(sqs-cross-account-needs-queue-access-policy)). Distractors: grant the role sqs:* on all resources in account B (trap "
     "messaging-trap-iam-policy-enough-cross-account; why links [aren't sufficient for cross-account access] "
     "(sqs-cross-account-needs-queue-access-policy)); allow every principal (*) in the queue policy (violates-qualifier); add "
     "the queue policy statement and remove the role's own policy (trap iam-trap-cross-account-one-policy; the why may link a "
     "chapter 03 fact on cross-account evaluation). The stem states SSE-SQS so that no key policy question arises. Bullets "
     "also 2.1.S3.")
slot("q21", "2.1.K2", "scheduler-vs-delay-queue", 2, "single", "extended", ["ee-least-operational-overhead", "ee-one-time"], 12,
     None, ["how-the-exam-asks-trap-keyword-bait"],
     ["sqs-delay-queue-range", "sqs-message-timer-range", "sqs-eventbridge-scheduler-for-advanced-scheduling",
      "eventbridge-scheduler-one-time-schedule-invokes-once"],
     "'A company must send a reminder email to each new user 3 days after the user signs up. Each reminder is a one-time "
     "action. The company wants a serverless solution with the LEAST operational overhead.' Key: when a user signs up, create "
     "an EventBridge Scheduler one-time schedule that invokes a Lambda function at the reminder time ([EventBridge Scheduler is "
     "the recommended solution] (sqs-eventbridge-scheduler-for-advanced-scheduling); a one-time schedule [invokes a target "
     "only once] (eventbridge-scheduler-one-time-schedule-invokes-once)). Distractors: send each reminder to an SQS delay "
     "queue with a 3-day delay (impossible-feature: at most [15 minutes] (sqs-delay-queue-range)); give each message a message "
     "timer of 3 days (misconception, same limit: [15 minutes] (sqs-message-timer-range); keep only one impossible-feature "
     "option, so label this one misconception); a cron job on an EC2 instance that checks the user table every hour "
     "(violates-qualifier). Bullets also 2.1.K5.")
slot("q22", "1.1.S5", "encrypted-queue-for-service-sender", 3, "multi", "extended", ["ee-select-two", "ee-at-rest"], 14,
     "kms-trap-aws-managed-key-controllable", ["messaging-trap-subscribe-without-queue-policy"],
     ["sns-sse-topic-to-encrypted-queue-needs-cmk-policy", "sqs-kms-aws-managed-key-policy-not-modifiable",
      "sqs-kms-service-senders-need-customer-managed-key"],
     "Select TWO, five options. 'An Amazon SNS topic delivers messages to an Amazon SQS queue. A new rule requires the queue "
     "to be encrypted at rest with an AWS KMS key whose key policy the company controls. After the team turned on SSE-KMS "
     "with the AWS managed key for Amazon SQS, no messages arrive. Which TWO actions will restore delivery and meet the rule "
     "with the LEAST operational overhead? (Select TWO.)' Keys: encrypt the queue with a customer managed key ([create a "
     "customer managed KMS key] (sqs-kms-service-senders-need-customer-managed-key)); add a key policy statement that allows "
     "the SNS service principal kms:GenerateDataKey and kms:Decrypt ([API actions GenerateDataKey and Decrypt] "
     "(sns-sse-topic-to-encrypted-queue-needs-cmk-policy)). Distractors: edit the key policy of the AWS managed key to allow "
     "SNS (trap kms-trap-aws-managed-key-controllable; why links [cannot modify the key policy] "
     "(sqs-kms-aws-managed-key-policy-not-modifiable)); switch the queue to SSE-SQS (violates-requirement: the company must "
     "control the key policy); delete the queue's access policy statement for the topic, because encryption replaces it "
     "(trap messaging-trap-subscribe-without-queue-policy). Worked think-aloud with a wrong path: step 3 predicts 'edit the "
     "AWS managed key's policy'; step 5 says 'My first idea breaks because the key policy of the AWS managed key for Amazon "
     "SQS cannot be modified.' Bullets also 2.1.S3.",
     worked="worked think-aloud with a wrong path")

BRIEF["question_plan"] = {
    "write": 22,
    "difficulty": {"1": 3, "2": 13, "3": 6},
    "difficulty_note": ("3/22 = 14% (target 20% +- 10), 13/22 = 59% (55% +- 10), 6/22 = 27% (25% +- 10). When the weakest four "
                        "are cut, cut at least one difficulty-2 question for each cut of a 1 or a 3."),
    "layer": {"core": 11, "extended": 11},
    "multi": 3,
    "multi_slots": ["q11 (core, difficulty 2)", "q19 (extended, difficulty 3)", "q22 (extended, difficulty 3, worked, wrong path)"],
    "twin_pairs": [
        "q01 / q07 (strict, core, difficulty 2, LEAST operational overhead: 'Only the company's order service processes the orders. The order service must process every order, even after it has been offline for a few hours.' / 'The order service, the shipping service and the analytics service must each process every order. Each service must process every order, even after it has been offline for a few hours.'; same four options; key A / key B)",
        "q02 / q09 (strict, core, difficulty 2, LEAST operational overhead: 'Processing a message takes up to 4 minutes. The queue uses the default visibility timeout, and many messages are processed by two different workers.' / 'Processing a message takes a few seconds. A few malformed messages fail every time, and the workers receive them again and again for days.'; same four options; key A / key B)",
        "q13 / q18 (strict, extended, difficulty 2, LEAST operational overhead: 'The events come from AWS services, from the company's own applications and from a SaaS partner's application. Each service selects events by fields inside the event detail.' / 'All events come from the company's own order application. Every event must also reach the customers' mobile phones by SMS within seconds.'; same four options; key A / key B)",
    ],
    "twin_pairs_note": ("Three strict pairs are written so that one rejection still ships two whole pairs (orchestrator note). "
                        "Each pair turns on stable facts; none on a volatile one. The later question of each pair carries "
                        "twin_of; at least 3 questions stand between the two of a pair."),
    "worked": ["q08 (no wrong path)", "q22 (wrong path)"],
    "slots_on_a_trap": 16,
    "every_trap_cited": ("All 13 trap ids of this brief are the slot trap or a planned distractor trap of at least one slot: "
                         "receive-deletes q03; queue-broadcasts q05 q07 (and q13 q18 distractors); topic-stores-messages q01 "
                         "(and q07 q19); standard-exactly-once q04 (and q11); bus-stores-events q17; short-visibility-safer q02 "
                         "(and q14); fifo-global-order q11; dlq-fresh-retention q15; lambda-retries-failed-only q14; "
                         "subscribe-without-queue-policy q16 (and q22); filter-needs-function q12; dlq-on-topic q19; "
                         "iam-policy-enough-cross-account q20."),
    "bullets_covered": ("all 9 bullets of the registry entry are the primary bullet of at least two slots: 2.1.K2 q15 q21; "
                        "2.1.K5 q06 q17; 2.1.K11 q02 q03 q09; 2.1.S1 q04 q18; 2.1.S3 q07 q12 q13; 3.2.K3 q05 q11 q19; 3.2.S1 "
                        "q01 q14; 3.2.S2 q08 q10; 1.1.S5 q16 q20 q22. Secondary bullets are named in each note ('Bullets also "
                        "...'); list them in the item's bullets field after the primary one."),
    "q205_rule": ("Q205 is a chapter rule: at least half of all wrong options of the chapter carry a trap id (this brief's 13, "
                  "or traps_from_other_chapters). A distractor gets a trap id only when its text states exactly that trap's "
                  "belief; otherwise it carries a misconception and a distractor_type. Aim for two tagged wrong options in most "
                  "questions; the notes name the planned tags."),
    "rule": ("Question ids are messaging-q001 to messaging-q022 in slot order (q01 = messaging-q001). Protect the three twin "
             "pairs, the three multiple-response questions and both worked questions when the weakest four are cut. At most 2 "
             "questions per concept; a unique (concept, trap) pair per question (twins exempt). Stems never name Callvale; they "
             "may reuse its situation. Keep at most one impossible-feature distractor per question, and give it a fact. Never "
             "let a volatile fact decide a key (list below). Never state a price. Within a twin pair, the qualifier, the "
             "options and every sentence but the changed phrase are identical. Stems may hold numbers of the scenario (4 "
             "minutes, 3 days, 10 days); an option's why that states an AWS number links its fact."),
    "qualifier_rule": ("Difficulty 1 questions (q03, q05, q10) have qualifier none and no violates-qualifier option; every other "
                       "question has one qualifier word of SPEC questions.qualifier_words (MOST, LEAST, BEST, LOWEST, HIGHEST, "
                       "FASTEST) and at least one violates-qualifier option. 3 of 22 without a qualifier stays under the 25% cap "
                       "of Q204."),
    "key_facts_note": "key_facts of each slot are the stable facts that decide its key; build_brief.py checked that none is volatile.",
}
