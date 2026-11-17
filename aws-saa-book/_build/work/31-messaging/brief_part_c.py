# brief-31, part C: How-it-works subsections 8 to 14 (Lambda, SNS, EventBridge, policies) and the closing sections.

# 8 ---------------------------------------------------------------------------------------------
sub("Lambda polls the queue for you and the queue decides the retries", 4, 210, ["3.2.S1", "2.1.S1", "2.1.K5"],
    ["lambda-esm-at-least-once", "lambda-filter-sqs-removes-unmatched", "lambda-sqs-max-concurrency-vs-reserved",
     "lambda-sqs-fifo-concurrency-message-groups", "lambda-faq-sqs-poll-role-or-queue-policy",
     "lambda-chaining-anti-pattern-sqs-or-step-functions"],
    {
        "problem": "With Lambda as the consumer you write no polling code. The retry rules still belong to the queue.",
        "trace": [
            "**Lambda polls.** SQS reaches Lambda through an [Event source mapping] (lambda-trigger-sqs-esm): [Lambda handles the polling] (lambda-esm-lambda-polls-source) and invokes the function.",
            "**Batch the messages.** The batch size defaults to [10] (lambda-sqs-batch-size): [For standard queues, the maximum is 10,000] (lambda-sqs-batch-size); [For FIFO queues, the maximum is 10] (lambda-sqs-batch-size).",
            "**Scale with the backlog.** Lambda starts with [five batches at a time with five concurrent invocations] (lambda-sqs-scaling-5-batches-300-per-minute-1250) and adds [up to 300 more concurrent invokes per minute] (lambda-sqs-scaling-5-batches-300-per-minute-1250); maximum concurrency caps one source [between 2 and 1,000] (lambda-sqs-max-concurrency-range).",
            "**Fail through the queue.** A failed batch returns by the queue's [visibility timeout and redrive policy] (lambda-queue-esm-retry-set-on-queue). With a [partial batch response] (lambda-sqs-partial-batch-response), Lambda can [make only the failed messages visible again] (lambda-sqs-partial-batch-response).",
            "**Size the timeout.** Give the queue a visibility timeout of [at least six times] (lambda-sqs-visibility-six-times-timeout) the function timeout; the function timeout [must be less than or equal to] (lambda-sqs-timeout-not-above-visibility) the visibility timeout.",
        ],
        "table": ("Where each setting lives (columns: Setting | Where you set it): retries and failed messages | on the source "
                  "queue: its [visibility timeout and redrive policy] (lambda-queue-esm-retry-set-on-queue); batch size and "
                  "maximum concurrency | on the event source mapping; permission to read | the execution role, with "
                  "[sqs:ReceiveMessage] (lambda-sqs-execution-role-read-permissions)."),
        "why": ("Why does AWS work this way? The queue already hides, counts and sets aside messages; Lambda reuses those rules "
                "instead of adding its own."),
        "exam_signal": ("\"process queue messages without managing servers\" points to a Lambda function with an SQS event "
                        "source mapping, where [Lambda handles the polling] (lambda-esm-lambda-polls-source)."),
        "exam_trap": "messaging-trap-lambda-retries-failed-only",
        "exam_trap_text": ("> **Exam trap:** One failed message does not mean one retried message. Without [ReportBatchItemFailures] "
                           "(lambda-sqs-partial-batch-response), the whole batch returns to the queue; with it, Lambda can [make "
                           "only the failed messages visible again] (lambda-sqs-partial-batch-response). "
                           "<!-- trap: messaging-trap-lambda-retries-failed-only -->"),
        "body_extras": ("Only if words remain: event source mappings [process each event at least once] "
                        "(lambda-esm-at-least-once), so the function must be idempotent, as in subsection 4. Chapter 18 owns "
                        "the details (<!-- xref: 18 event source mappings and partial batch responses -->); this subsection names "
                        "no concurrency quota beyond the trace."),
        "say_it": "The short answer is: Lambda polls, and the queue keeps the retry rules. The thing to watch is the visibility timeout.",
        "stop_and_answer": ("A function has a timeout longer than the visibility timeout of its SQS queue. What happens when you "
                            "create the event source mapping? Answer: Lambda [returns an error] "
                            "(lambda-sqs-timeout-not-above-visibility): the function timeout [must be less than or equal to] "
                            "(lambda-sqs-timeout-not-above-visibility) the visibility timeout."),
    })

# 9 ---------------------------------------------------------------------------------------------
sub("An SNS topic pushes each published message to all its subscribers", 3, 200, ["3.2.K3", "2.1.K11", "2.1.K5"],
    ["sns-supports-a2a-and-a2p", "sns-decision-subscriber-types", "sns-faq-topic-is-access-point-for-publish-and-subscribe",
     "sns-faq-topic-supports-multiple-transports", "sns-faq-each-notification-contains-single-message",
     "sns-faq-raw-message-delivery-default-json-envelope", "sns-quota-subscriptions-per-topic",
     "sns-published-messages-stored-across-servers-data-centers", "sns-faq-subscriber-may-receive-duplicates",
     "sns-faq-order-attempted-but-network-issues-can-reorder", "sns-wa-high-throughput-push-many-to-many-fan-out"],
    {
        "problem": ("A queue gives each message to one consumer. When many systems need the same message now, the sender would "
                    "have to call each one. A topic does that for the sender."),
        "trace": [
            "**Publish once.** [Publishers communicate asynchronously with subscribers] (sns-publishers-send-to-topic-asynchronously) through a topic.",
            "**Store before the answer.** SNS keeps [multiple copies (to disk)] (sns-faq-durable-storage-multiple-copies-multiple-azs) in [multiple Availability Zones before acknowledging receipt] (sns-faq-durable-storage-multiple-copies-multiple-azs).",
            "**Push to every subscriber.** SNS delivers to [all applicable subscribers] (sns-faq-publish-triggers-delivery-to-all-subscribers) with a [Push-based model] (sns-decision-push-model), which [removes the need to check or “poll”] (sns-push-mechanism-no-polling).",
            "**Reach applications and people.** Subscribers include [delivery streams, Lambda functions, Amazon SQS queues] (sns-a2a-subscriber-types) and [mobile applications, mobile phone numbers, and email addresses] (sns-a2p-subscriber-types); SNS [invokes AWS Lambda functions asynchronously] (sns-lambda-invoked-asynchronously).",
            "**Keep nothing afterwards.** [Messages are not persisted] (sns-decision-no-persistence), and a published message [cannot be recalled] (sns-faq-published-message-cannot-be-recalled).",
        ],
        "table": ("Queue or topic (columns: Question | SQS queue | SNS topic): who gets a message | one consumer: SQS has [a "
                  "single subscriber typically] (sqs-typically-single-subscriber-order-and-loss) | every subscriber; how it "
                  "arrives | consumers poll | it is pushed; a receiver is offline | the message waits | delivery is retried, "
                  "then [Messages are not persisted] (sns-decision-no-persistence) means it is gone."),
        "why": ("Why does AWS work this way? Push removes polling from many receivers and keeps the delay short: SNS [typical "
                "latency] (sns-faq-sns-typical-latency-under-30-milliseconds) is [under 30 milliseconds] "
                "(sns-faq-sns-typical-latency-under-30-milliseconds)."),
        "exam_signal": ("\"notify several systems at the same time\" or \"fanout\" points to an SNS topic, often used for "
                        "[fanout notifications] (sns-decision-typical-use)."),
        "exam_trap": None,
        "body_extras": ("Only if words remain: subscribers can see [occasional, duplicate messages] "
                        "(sns-faq-subscriber-may-receive-duplicates) and [out-of-order messages at the subscriber end] "
                        "(sns-faq-order-attempted-but-network-issues-can-reorder) on a standard topic. Reference only: a "
                        "standard topic takes [12,500,000 per topic] (sns-quota-subscriptions-per-topic) subscriptions by "
                        "default; the default message size [256 KiB] (sns-message-size-default-256kib) is volatile."),
        "say_it": "The short answer is: a topic pushes one message to every subscriber. The thing to watch is a subscriber that is offline.",
        "stop_and_answer": ("A topic has an email subscription and a Lambda subscription. The function is deleted by mistake for "
                            "a week. Does the email subscriber still get each message? Answer: yes; SNS delivers to [all "
                            "applicable subscribers] (sns-faq-publish-triggers-delivery-to-all-subscribers) one by one. The "
                            "messages for the deleted function are not kept, because [Messages are not persisted] "
                            "(sns-decision-no-persistence)."),
    })

# 10 --------------------------------------------------------------------------------------------
sub("Queues subscribed to a topic give each consumer its own durable copy", 4, 220, ["2.1.S3", "3.2.S1", "2.1.S1", "1.1.S5"],
    ["sns-faq-common-pattern-sns-publishes-to-sqs-queues", "sns-fanout-replicates-message-to-many-endpoints",
     "sns-cross-account-queue-owner-subscription-needs-no-confirmation", "sns-uses-https-to-forward-to-sqs",
     "sns-pricing-sqs-lambda-no-delivery-charge", "sns-fifo-topic-delivers-to-sqs-standard-and-fifo",
     "sns-fifo-topic-cannot-deliver-to-customer-managed-endpoints", "sns-lambda-triggers-standard-topics-only",
     "sns-fifo-to-lambda-needs-sqs-in-between", "sns-faq-fifo-vs-kinesis-fanout-100-vs-5", "sqs-decision-combine-buffer-for-consumers"],
    {
        "problem": ("SNS alone loses a message when a subscriber is offline; SQS alone gives each message to one consumer. "
                    "Together they give every consumer its own copy that waits."),
        "trace": [
            "**Subscribe one queue per consumer.** Subscribe [multiple SQS standard queues to the SNS topic] (sns-faq-fanout-identical-messages-to-multiple-sqs-queues); SNS then [sends the message to each subscribed queue] (sns-publish-sends-message-to-each-subscribed-queue).",
            "**Let the queue accept the topic.** You must [set a policy on the Amazon SQS queue] (sns-sqs-queue-needs-policy-allowing-topic) that allows messages [sent from the Amazon SNS topic] (sns-sqs-queue-needs-policy-allowing-topic); the [aws:SourceArn condition] (sns-queue-policy-sourcearn-limits-to-one-topic) admits that one topic.",
            "**Confirm only across accounts.** A queue and topic of the [same AWS account] (sns-faq-same-account-sqs-subscription-needs-no-opt-in) need no [opt-in] (sns-faq-same-account-sqs-subscription-needs-no-opt-in); a subscriber who does not own the queue [must confirm the subscription] (sns-cross-account-non-owner-must-confirm-subscription).",
            "**Each queue keeps its copy.** The messages [persist in an Amazon SQS queue] (sns-sqs-together-instant-notice-and-later-processing), which prevents loss [when subscribers are offline] (sns-with-sqs-prevents-loss-for-offline-subscribers).",
            "**Unwrap if you want.** Each copy holds [metadata about the message in a JSON document] (sns-sqs-envelope-contains-subject-message-metadata); with raw message delivery, [any Amazon SNS metadata is stripped] (sns-raw-delivery-sqs-strips-sns-metadata).",
        ],
        "table": ("Pairing topic and queue types (columns: Need | Topic | Queues): every consumer, any order | standard topic | "
                  "standard queues; ordered fan-out | FIFO topic, for [consistent end-to-end message ordering] "
                  "(sns-faq-fifo-topic-to-sqs-fifo-queue-end-to-end-ordering) | FIFO queues; ordered topic, consumers that "
                  "accept duplicates | FIFO topic | standard queues, which [lets you lower costs] "
                  "(sns-fifo-standard-queue-subscriber-lowers-cost). Truth table."),
        "why": ("Why does AWS work this way? Each queue decouples one consumer from the publisher and from the other consumers: "
                "a slow indexer no longer slows the webhooks. The integration guide names this combination: events go to a "
                "queue [as a buffer for downstream consumers] (sqs-decision-combine-buffer-for-consumers)."),
        "exam_signal": ("\"every service must get every message, even while it is down\" points to SNS fan-out to SQS queues; a "
                        "common pattern is to [publish messages to Amazon SQS queues] "
                        "(sns-faq-common-pattern-sns-publishes-to-sqs-queues)."),
        "exam_trap": "messaging-trap-subscribe-without-queue-policy",
        "exam_trap_text": ("> **Exam trap:** A subscription alone does not let SNS write to the queue. You must [set a policy on "
                           "the Amazon SQS queue] (sns-sqs-queue-needs-policy-allowing-topic) that allows the topic. "
                           "<!-- trap: messaging-trap-subscribe-without-queue-policy -->"),
        "try_it": "messaging-t03: one sentence ('Send one message to two queues through a topic, and see what a missing queue policy does.'), then See [3-do.md](3-do.md). <!-- task: messaging-t03 -->",
        "diagram": "messaging-fanout after the trace (text fixed in diagrams); its alt and caption count toward words_all_in.",
        "body_extras": ("Reference only, no sentence: an SNS FIFO topic [can't deliver messages to customer managed endpoints] "
                        "(sns-fifo-topic-cannot-deliver-to-customer-managed-endpoints); Lambda triggers take [standard SNS topics "
                        "only] (sns-lambda-triggers-standard-topics-only), so FIFO fan-out to functions goes through queues: "
                        "[subscribe Amazon SQS FIFO or standard queues] (sns-fifo-to-lambda-needs-sqs-in-between)."),
        "say_it": "The short answer is: one topic, and one queue for each consumer. The thing to watch is each queue's access policy.",
        "stop_and_answer": ("A company adds a third queue to its order topic for a new audit service. The audit service is down "
                            "for a day after launch. Are that day's orders lost for the audit service? Answer: no; its subscribed "
                            "queue keeps them: the messages [persist in an Amazon SQS queue] "
                            "(sns-sqs-together-instant-notice-and-later-processing) until the service reads them, within the "
                            "queue's retention period."),
    }, route="pass")

# 11 --------------------------------------------------------------------------------------------
sub("A filter policy decides which messages reach each subscription", 3, 200, ["2.1.S3", "3.2.K3"],
    ["sns-decision-filter-policies", "sns-filter-policy-max-keys", "sns-filter-policy-complexity-150",
     "sns-filter-policy-quota-200-per-topic-10000-per-account", "sns-fifo-same-filtering-as-standard",
     "sns-fifo-exactly-once-lost-with-filtering", "sns-change-payload-based-filtering-2022"],
    {
        "problem": ("Not every subscriber needs every message. Without a filter, each consumer receives everything and throws "
                    "most of it away."),
        "trace": [
            "**Everything by default.** A subscriber [receives every message that's published to the topic] (sns-filter-default-every-message).",
            "**Add a filter policy.** For a subset, [assign a filter policy to the topic subscription] (sns-filter-default-every-message).",
            "**Choose what it reads.** The policy reads [message attributes (default setting)] (sns-filter-scope-attributes-default-or-body), or the body: [Applies the filter policy to the message body] (sns-filter-scope-attributes-default-or-body), which must be a [well-formed JSON object] (sns-filter-body-scope-needs-json-payload).",
            "**Match or skip.** SNS sends a message when its attributes or body [satisfy the conditions specified in the filter policy] (sns-filter-nonmatching-message-not-sent); otherwise it [doesn't send the message to that subscriber] (sns-filter-nonmatching-message-not-sent).",
            "**Allow time for a change.** A new or changed policy needs [up to 15 minutes] (sns-filter-policy-change-up-to-15-minutes) to take full effect.",
        ],
        "table": ("Where to filter (columns: Option | Effort and cost): no filter, the consumer discards | every consumer "
                  "receives and pays for every message; filter policy on attributes | [Attribute-based message filtering is "
                  "free] (sns-pricing-attribute-filtering-free); filter policy on the body | billed by the [total amount of "
                  "outbound payload data scanned] (sns-pricing-attribute-filtering-free); a function between topic and queue | "
                  "code to write, run and pay for. The two pricing links point to a volatile fact: allowed in prose, never a "
                  "question key."),
        "why": ("Why does AWS work this way? Filtering at the subscription keeps publishers simple: they publish once, and each "
                "subscription states what it wants."),
        "exam_signal": ("\"each subscriber should receive only the messages it needs\" points to subscription filter policies, "
                        "with which subscribers [selectively receive only a subset] "
                        "(sns-faq-message-filtering-subscribers-receive-subset)."),
        "exam_trap": "messaging-trap-filter-needs-function",
        "exam_trap_text": ("> **Exam trap:** You need no function to filter a topic's messages. The subscriber can [assign a "
                           "filter policy to the topic subscription] (sns-filter-default-every-message). "
                           "<!-- trap: messaging-trap-filter-needs-function -->"),
        "body_extras": ("Reference only, no sentence: a policy has a [maximum of five keys] (sns-filter-policy-max-keys); with "
                        "filtering, a FIFO topic gives [at-most-once delivery] (sns-fifo-exactly-once-lost-with-filtering)."),
        "say_it": "The short answer is: each subscription can filter its own messages. The thing to watch is the delay after a change.",
        "stop_and_answer": ("A team adds a filter policy so that the EU queue gets only EU orders. A minute later the queue still "
                            "receives US orders. Is the policy wrong? Answer: not yet a sign of an error; a change needs [up to "
                            "15 minutes] (sns-filter-policy-change-up-to-15-minutes) to take full effect."),
    })

# 12 --------------------------------------------------------------------------------------------
sub("An EventBridge rule matches event content and sends each match to its targets", 4, 225, ["2.1.K5", "2.1.S3", "2.1.S1"],
    ["eventbridge-aws-service-events-go-to-default-bus", "eventbridge-rule-applies-to-one-bus",
     "eventbridge-two-rule-types-pattern-and-schedule", "eventbridge-decision-content-filtering",
     "eventbridge-decision-no-ordering", "eventbridge-faq-typical-latency-about-half-a-second",
     "eventbridge-rule-infinite-loop-risk", "eventbridge-pipe-single-source-single-target",
     "eventbridge-faq-event-bus-many-to-many-pipes-point-to-point", "eventbridge-faq-customers-use-sns-as-rule-target-to-filter-and-fan-out",
     "eventbridge-cloudtrail-events-default-bus-only", "eventbridge-schema-registry-schemas-for-aws-service-events",
     "eventbridge-faq-scheduled-rules-remain-scheduler-richer-feature-set", "eventbridge-scheduler-at-least-once-with-retries",
     "eventbridge-scheduler-flexible-time-window-disperses-triggers", "eventbridge-decision-scheduling-category"],
    {
        "problem": ("Many events come from AWS services and SaaS applications, not from your code, and consumers want them by "
                    "content. EventBridge routes events with rules instead of subscriptions."),
        "trace": [
            "**Land on a bus.** Every account has a [default event bus] (eventbridge-default-bus-receives-aws-service-events) that [automatically receives events from AWS services] (eventbridge-default-bus-receives-aws-service-events). Your own events can go to buses [called custom event buses] (eventbridge-custom-bus-your-own-events); [partner event buses] (eventbridge-partner-bus-receives-saas-events) [receive events from SaaS partners] (eventbridge-partner-bus-receives-saas-events).",
            "**Share one shape.** Events are [represented as JSON objects] (eventbridge-events-are-json-with-same-top-level-fields) with [the same top-level fields] (eventbridge-events-are-json-with-same-top-level-fields).",
            "**Match a pattern.** A rule [matches incoming events for a given event bus] (eventbridge-faq-rule-matches-events-on-a-bus-and-routes-to-targets). Its pattern can test the event source, [event metadata, and/or event detail values] (eventbridge-pattern-matches-metadata-data-content), and it [either matches an event or it doesn't] (eventbridge-event-pattern-matches-or-not).",
            "**Send to targets.** A rule has at most [5] (eventbridge-quota-targets-per-rule) targets, all [processed in parallel] (eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel), for example a [Lambda function (ASYNC)] (eventbridge-target-types-list) or [Amazon SQS standard, fair, and FIFO queues] (eventbridge-target-types-list). To reshape an event first, [use the input transformer] (eventbridge-input-transformer-edits-event-before-target).",
            "**No match, no action.** [An event might match multiple rules] (eventbridge-event-can-match-several-rules-or-none); if it matches none, [EventBridge takes no action] (eventbridge-event-can-match-several-rules-or-none).",
        ],
        "table": ("SNS filter policy or EventBridge rule (columns: Question | SNS topic with filter policy | EventBridge rule): "
                  "where events come from | your publishers | AWS services, your apps and SaaS: [SaaS applications, and AWS "
                  "services] (eventbridge-faq-eventbridge-recommended-for-app-saas-aws-events); what the match reads | "
                  "attributes or the body | it is [applied across the entire event body] "
                  "(eventbridge-faq-eventbridge-json-events-rules-apply-to-entire-event-body); how many receivers | [thousands "
                  "or millions of endpoints] (sns-faq-sns-recommended-for-high-fan-out-thousands-or-millions) | [5] "
                  "(eventbridge-quota-targets-per-rule) targets per rule."),
        "diagram": "messaging-eventbridge-routing after the trace (text fixed in diagrams); its alt and caption count toward words_all_in.",
        "why": ("Why does AWS work this way? Routing by content keeps producers unaware of consumers: EventBridge can [abstract "
                "clients (event producers) from the services] (eventbridge-wa-abstracts-producers-from-consumers) they rely on."),
        "exam_signal": ("\"react to events from AWS services or a SaaS partner\" points to EventBridge, the [only event-based "
                        "service] (eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners) that "
                        "integrates directly with [third-party SaaS partners] "
                        "(eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners)."),
        "exam_trap": None,
        "go_deeper": ("Go deeper: schedules. Scheduled rules are a [legacy feature of EventBridge] "
                      "(eventbridge-scheduled-rules-are-legacy) and run in the [UTC+0 time zone] "
                      "(eventbridge-scheduled-rule-utc-and-one-minute-precision). EventBridge Scheduler offers [rate-based, "
                      "cron-based, and one-time schedules] (eventbridge-scheduler-three-schedule-types), cron [in the time zone "
                      "that you specify] (eventbridge-scheduler-cron-supports-time-zones), with schedules [created independently] "
                      "(eventbridge-faq-schedules-created-without-event-bus) of a bus. It runs as [an IAM role that EventBridge "
                      "Scheduler assumes] (eventbridge-scheduler-execution-role-assumed). At most 60 words."),
        "body_extras": ("Only if words remain, one sentence: EventBridge [does not provide message ordering guarantees] "
                        "(eventbridge-decision-no-ordering). Reference only: typical latency [about half a second] "
                        "(eventbridge-faq-typical-latency-about-half-a-second); a rule that triggers itself can loop: [where a "
                        "rule is fired recursively] (eventbridge-rule-infinite-loop-risk); a pipe goes [from a single source to "
                        "a single target] (eventbridge-pipe-single-source-single-target); CloudTrail events are [delivered to the "
                        "default event bus only] (eventbridge-cloudtrail-events-default-bus-only)."),
        "say_it": "The short answer is: a rule picks events by content and sends them on. The thing to watch is the target limit of each rule.",
        "stop_and_answer": ("A team wants a Lambda function to run and a team topic to be notified each time any EC2 instance in "
                            "the account stops. Must it change the instances or write a poller? Answer: no; AWS service events "
                            "reach the [default event bus] (eventbridge-default-bus-receives-aws-service-events), so one rule "
                            "with two targets does the work: a rule can [route to multiple targets] "
                            "(eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel)."),
    }, route="pass")

# 13 --------------------------------------------------------------------------------------------
sub("Failed deliveries are retried and then dropped unless a dead-letter queue catches them", 4, 215,
    ["2.1.K5", "3.2.K3", "2.1.S1"],
    ["sns-durability-retry-policy-and-dlq-preserve-messages", "sns-dlq-is-sqs-queue-for-subscription",
     "sns-dlq-same-account-and-region-as-subscription", "sns-dlq-queue-type-matches-topic-type", "sns-client-side-error-not-retried",
     "sns-retry-only-http-policy-customizable", "sns-retry-retryable-errors-5xx-429", "sns-retry-http-total-retry-time-max",
     "sns-faq-lambda-throttled-delivery-is-retried", "sns-failed-delivery-does-not-change-subscription-status",
     "eventbridge-dlq-queue-same-region-as-rule", "eventbridge-dlq-api-needs-manual-queue-policy",
     "eventbridge-putevents-partial-failure-caller-retries", "eventbridge-putevents-to-missing-bus-drops-event-with-200",
     "eventbridge-decision-no-persistence-at-least-once", "eventbridge-faq-event-replay-debug-hydrate-targets-recover-from-errors",
     "eventbridge-replay-adds-replay-name-field", "eventbridge-archive-single-source-bus-fixed"],
    {
        "problem": ("SNS and EventBridge push. When the receiver is down they cannot wait forever, so each has a retry rule and "
                    "an optional dead-letter queue."),
        "trace": [
            "**SNS retries in phases.** SNS runs a [4-phase retry policy] (sns-faq-four-phase-delivery-retry-policy). To SQS and Lambda it tries [100,015 times] (sns-retry-aws-managed-total-attempts) [over 23 days] (sns-retry-aws-managed-total-attempts); to email, SMS and mobile push, [50 attempts] (sns-retry-customer-managed-total-attempts) [over 6 hours] (sns-retry-customer-managed-total-attempts).",
            "**SNS then drops.** When the policy ends, SNS [stops retrying the delivery and discards the message] (sns-retry-exhausted-discards-unless-dlq), unless [a dead-letter queue is attached to the subscription] (sns-retry-exhausted-discards-unless-dlq).",
            "**EventBridge retries for a day.** By default it retries for [24 hours] (eventbridge-retry-default-24h-185-attempts) and [up to 185 times] (eventbridge-retry-default-24h-185-attempts); you can change the [length of time it tries] (eventbridge-retry-length-and-attempts-set-per-target) for each target.",
            "**Some errors skip the retries.** A missing permission or a deleted target sends the event on [without any retry attempts] (eventbridge-some-errors-skip-retries).",
            "**EventBridge then drops.** After the last attempt [the event is dropped] (eventbridge-retry-exhausted-event-dropped), unless you [configure a dead-letter queue (DLQ)] (eventbridge-retry-exhausted-event-dropped); it is one of the [standard Amazon SQS queues] (eventbridge-dlq-is-standard-sqs-queue).",
        ],
        "table": ("Retries and dead-letter queues (columns: Service | Default retry | Where the dead-letter queue goes): SQS | the "
                  "message returns after each visibility timeout | on the source queue, after the [number of times a consumer "
                  "can receive] (sqs-dlq-max-receive-count-meaning); SNS | phases that depend on the endpoint type | on each "
                  "subscription: [attached to an Amazon SNS subscription] (sns-dlq-attached-to-subscription-not-topic); "
                  "EventBridge | [24 hours] (eventbridge-retry-default-24h-185-attempts) | on each target, and you [can't use a "
                  "FIFO queue for a DLQ] (eventbridge-dlq-fifo-not-supported). Truth table."),
        "why": ("Why does AWS work this way? A push service that kept every message forever would be a queue. It hands long-term "
                "keeping to SQS, through the dead-letter queue."),
        "exam_signal": ("\"keep the messages that could not be delivered\" points to a dead-letter queue on the subscription or "
                        "the target; SNS discards a message unless [a dead-letter queue is attached to the subscription] "
                        "(sns-retry-exhausted-discards-unless-dlq)."),
        "exam_trap": "messaging-trap-dlq-on-topic",
        "exam_trap_text": ("> **Exam trap:** An SNS dead-letter queue does not go on the topic. It is [attached to an Amazon SNS "
                           "subscription] (sns-dlq-attached-to-subscription-not-topic), because [message deliveries happen at "
                           "the subscription level] (sns-dlq-attached-to-subscription-not-topic). "
                           "<!-- trap: messaging-trap-dlq-on-topic -->"),
        "go_deeper": ("Go deeper: archive and replay. A Classic bus keeps nothing: [Not retained. To keep events, add an "
                      "archive.] (eventbridge-classic-bus-does-not-retain-events) An archive [stores events in an archive "
                      "indefinitely] (eventbridge-archive-retention-indefinite-by-default) unless you set days. Replay can "
                      "[reprocess past events] (eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule), which can "
                      "[only be replayed to the source event bus] (eventbridge-replay-to-source-bus-only), and they [aren't "
                      "necessarily replayed in the same order] (eventbridge-replay-order-not-guaranteed). At most 60 words."),
        "body_extras": ("Reference only, no sentence: an SNS dead-letter queue is in the [same AWS account and Region] "
                        "(sns-dlq-same-account-and-region-as-subscription) as its subscription; HTTP/S retry time cannot exceed "
                        "[3,600 seconds] (sns-retry-http-total-retry-time-max); an archive can [specify an event pattern for "
                        "EventBridge] (eventbridge-archive-filter-by-event-pattern); replaying [does not remove them from the "
                        "archive] (eventbridge-replay-keeps-archive-events)."),
        "say_it": "The short answer is: push services retry, then drop the message. The thing to watch is where you attach the dead-letter queue.",
        "stop_and_answer": ("The Lambda target of an EventBridge rule was deleted by mistake, and the target has a dead-letter "
                            "queue. How many retries happen before an event reaches that queue? Answer: none; for such errors "
                            "EventBridge [sends these events directly to the target DLQ] (eventbridge-some-errors-skip-retries)."),
    })

# 14 --------------------------------------------------------------------------------------------
sub("Resource-based policies decide which accounts and services may send to a queue", 4, 220, ["1.1.S5", "2.1.S3"],
    ["sqs-faq-sqs-resource-based-permissions-iam-policy-language", "sqs-faq-only-account-owner-or-delegate-can-operate-queue",
     "sqs-faq-anonymous-access-via-access-policy", "sqs-sse-anonymous-requests-rejected", "sqs-batch-actions-permissions-follow-single-actions",
     "sns-faq-default-only-topic-owner-can-publish", "sns-faq-only-topic-owner-can-change-permissions",
     "sns-addpermission-adds-policy-statement", "sns-faq-add-permission-simple-access-policy-for-conditions",
     "sns-protocol-restriction-needs-custom-policy", "eventbridge-bus-as-target-same-or-different-account",
     "eventbridge-cross-account-new-bus-targets-need-iam-role", "eventbridge-cross-account-sender-pays-as-custom-events",
     "eventbridge-target-needs-permission-to-access", "eventbridge-cross-region-send-and-receive", "sqs-faq-queues-are-independent-per-region",
     "sqs-sse-does-not-encrypt-metadata", "sqs-sse-backlogged-messages-not-encrypted", "sqs-sse-default-key-no-cross-account-lambda",
     "sqs-kms-aws-managed-key-unique-per-account-region", "sqs-faq-sse-no-extra-sqs-charge-kms-calls-charged",
     "sqs-change-sendmessage-needs-only-generatedatakey-2024", "sns-sse-topic-to-encrypted-queue-needs-cmk-policy",
     "sns-dlq-encrypted-queue-needs-custom-kms-key", "sqs-vpc-interface-endpoint-no-gateway-or-nat", "sns-vpc-interface-endpoint-no-igw-nat-vpn",
     "sqs-faq-sse-services-need-compatibility-with-encrypted-queues"],
    {
        "problem": ("A queue, a topic or a bus belongs to one account. Another account, or an AWS service such as Amazon S3, can "
                    "send to it only if its own policy lets that sender in."),
        "trace": [
            "**Start private.** A new queue's policy [allows only the queue owner] (sqs-default-access-policy-owner-only) to send and receive; a new topic is [created with no permissions] (sns-topic-private-by-default); the default bus [only allows events from one account] (eventbridge-default-bus-accepts-one-account-only).",
            "**Write a resource policy.** SQS has its own [resource-based permissions system] (sqs-faq-sqs-resource-based-permissions-iam-policy-language) in the [same language as AWS Identity and Access Management] (sqs-faq-sqs-resource-based-permissions-iam-policy-language); in SQS [the only resource is the queue] (sqs-queue-is-the-only-resource).",
            "**Open it to another account.** For a principal of another account you [configure the queue's access policy] (sqs-cross-account-needs-queue-access-policy); for a bus you [edit the permissions on the event bus] (eventbridge-cross-account-receiver-edits-bus-permissions) that receives.",
            "**Open it to a service.** For S3 event notifications, the topic policy must [grant the Amazon S3 service (s3.amazonaws.com)] (sns-s3-publish-needs-topic-policy-for-s3-principal), with a [SourceAccount condition] (sns-s3-publish-needs-topic-policy-for-s3-principal). For SQS and SNS targets EventBridge uses [an IAM execution role or a resource-based policy] (eventbridge-target-permission-model-by-target-type).",
            "**Use the full policy language.** The permissions API [cannot allow conditional access] (sqs-faq-permissions-api-no-conditional-access); SetQueueAttributes [supports the full access policy language] (sqs-faq-set-queue-attributes-full-policy-language-ip-and-time).",
        ],
        "table": ("Who must allow a sender (columns: Sender | Queue, topic or bus policy | Sender side): a role in another account "
                  "| [configure the queue's access policy] (sqs-cross-account-needs-queue-access-policy) | its own IAM policy "
                  "too; an SNS topic | allow the topic, with the [aws:SourceArn condition] "
                  "(sns-queue-policy-sourcearn-limits-to-one-topic) | nothing; S3 in another account, to a topic | [grant the "
                  "Amazon S3 service (s3.amazonaws.com)] (sns-s3-publish-needs-topic-policy-for-s3-principal) | the event "
                  "notification on the bucket. Three rows."),
        "why": ("Why does AWS work this way? The owner pays and the owner decides: the [queue owner pays] "
                "(sqs-faq-queue-owner-pays-for-shared-access) for [shared message queue access] "
                "(sqs-faq-queue-owner-pays-for-shared-access)."),
        "exam_signal": ("\"an application in another AWS account must send messages to the queue\" points to a statement in the "
                        "queue's access policy: [configure the queue's access policy] "
                        "(sqs-cross-account-needs-queue-access-policy)."),
        "exam_trap": "messaging-trap-iam-policy-enough-cross-account",
        "exam_trap_text": ("> **Exam trap:** An IAM policy in the sender's account is not enough for another account's queue. "
                           "Identity-based policies [aren't sufficient for cross-account access] "
                           "(sqs-cross-account-needs-queue-access-policy). <!-- trap: messaging-trap-iam-policy-enough-cross-account -->"),
        "go_deeper": ("Go deeper: encrypted queues and their senders. SQS gives [managed server-side encryption by default] "
                      "(sqs-sse-managed-encryption-on-by-default), with [SQS-managed encryption keys (SSE-SQS)] "
                      "(sqs-sse-two-key-types) or [AWS Key Management Service (SSE-KMS)] (sqs-sse-two-key-types). For an AWS "
                      "service sender you must [create a customer managed KMS key] "
                      "(sqs-kms-service-senders-need-customer-managed-key); you [cannot modify the key policy] "
                      "(sqs-kms-aws-managed-key-policy-not-modifiable) of the AWS managed key. Grant producers both [kms:GenerateDataKey "
                      "and kms:Decrypt permissions] (sqs-faq-sse-producer-needs-generatedatakey-and-decrypt). At most 60 words."),
        "spot_the_bug": ("Spot the bug (example block, story names allowed): 'Callvale encrypts the uploads queue with SSE-KMS and "
                         "the AWS managed key for Amazon SQS. From that moment, S3 event notifications no longer arrive in the "
                         "queue. What is wrong?' Reveal: Amazon S3 is a service sender; it needs a key whose policy lets it use "
                         "the key, so [create a customer managed KMS key] (sqs-kms-service-senders-need-customer-managed-key) and "
                         "add [permissions in the key policy] (sqs-kms-service-senders-need-customer-managed-key); you [cannot "
                         "modify the key policy] (sqs-kms-aws-managed-key-policy-not-modifiable) of the AWS managed key."),
        "body_extras": ("Reference only, no sentence: private access from a VPC uses an interface endpoint: [you must first define "
                        "an interface VPC endpoint] (sqs-vpc-interface-endpoint-no-gateway-or-nat) (chapter 11 owns it, "
                        "<!-- xref: 11 interface endpoints -->); the producer permission conflict "
                        "(sqs-change-sendmessage-needs-only-generatedatakey-2024) stays out of prose: grant both."),
        "say_it": "The short answer is: the queue's own policy must let the sender in. The thing to watch is the key policy of an encrypted queue.",
        "stop_and_answer": ("An SNS topic in account A must deliver to an SQS queue in account B. Which policy in account B must "
                            "change? Answer: the queue's access policy: allow the topic, limited by the [aws:SourceArn condition] "
                            "(sns-queue-policy-sourcearn-limits-to-one-topic). Without it nothing arrives: you must [set a policy "
                            "on the Amazon SQS queue] (sns-sqs-queue-needs-policy-allowing-topic)."),
    })

# Closing sections of 2-deep.md --------------------------------------------------------------------
S.append({
    "file": "2-deep.md", "section": "numbers-that-decide-answers", "heading": "Numbers that decide answers",
    "bullets": ["2.1.K11", "3.2.K3"], "facts": [], "status": "write", "minutes": 3,
    "plan": ("Fixed H3 'A-list' (8 rows, columns Number | What it is | Why it decides an answer) and 'B-list' (12 rows, columns "
             "Number | What it is), from numbers below; column 1 is always a fact link. Directly under the B-list: the one "
             "not-examinable Changed recently entry (changed_recently.deep, U3). At most 300 words (aim 285; the U3 entry "
             "counts)."),
})
S.append({
    "file": "2-deep.md", "section": "decision-record", "heading": "Decision record", "bullets": ["3.2.S1", "2.1.S3", "2.1.S1"],
    "facts": [], "status": "write", "minutes": 3,
    "plan": ("Five bold fields of D11 from decision_record below, with the diagrams messaging-before (after Context) and "
             "messaging-after (after Decision). Role example: the lint asks for no link, but every AWS behaviour in a reason "
             "carries its fact link (the plan gives them). At most 280 words (aim 260), diagrams' alt and steps included."),
})
S.append({
    "file": "2-deep.md", "section": "faq-quick-fire", "heading": "FAQ quick-fire", "bullets": ["2.1.K2", "1.1.S5"],
    "facts": [], "status": "write", "minutes": 4,
    "plan": ("Ten items of D12 from faq below: '**FAQ <n>.** <question>?', then a reveal with the short answer (with its link) "
             "and the AWS quote block (the quote field, copied exactly, then the link line). At most 450 words (aim 430)."),
})
