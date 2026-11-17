# brief-31, part D: traps, compare tables, signals, words table, numbers, Changed recently, FAQ, story, decision record,
# real world, devices.
SID = {i + 1: s["section"] for i, s in enumerate(x for x in BRIEF["sections"] if isinstance(x.get("plan"), dict))}
D = "2-deep.md#"

BRIEF["traps"] = [
    {"id": "messaging-trap-receive-deletes",
     "belief": "Receiving a message removes it from the queue.",
     "truth": ("The message stays in the queue, hidden from other consumers, until the consumer deletes it; if it is not "
               "deleted before the visibility timeout ends, it becomes visible again."),
     "facts": ["sqs-receive-keeps-message-hidden", "sqs-manual-delete-after-processing", "sqs-undeleted-message-visible-again"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "messaging-trap-queue-broadcasts",
     "belief": "When several services poll one queue, each service gets every message.",
     "truth": ("A queue typically gives each message to a single consumer; to give every service its own copy, subscribe one "
               "SQS queue per service to an SNS topic."),
     "facts": ["sqs-typically-single-subscriber-order-and-loss", "sns-faq-fanout-identical-messages-to-multiple-sqs-queues"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "messaging-trap-topic-stores-messages",
     "belief": "An SNS topic keeps messages until an offline subscriber comes back.",
     "truth": ("SNS does not persist messages: it retries the delivery, then discards the message unless a dead-letter queue "
               "is attached to the subscription. Subscribe an SQS queue to keep messages for an offline consumer."),
     "facts": ["sns-decision-no-persistence", "sns-retry-exhausted-discards-unless-dlq", "sns-with-sqs-prevents-loss-for-offline-subscribers"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "messaging-trap-standard-exactly-once",
     "belief": "A standard queue delivers each message exactly once and in the order it was sent.",
     "truth": ("A standard queue gives at-least-once delivery: more than one copy of a message can arrive, and messages can "
               "arrive out of order, so consumers must be idempotent."),
     "facts": ["sqs-standard-at-least-once-duplicates", "sqs-faq-standard-queue-design-idempotent-consumers"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "messaging-trap-bus-stores-events",
     "belief": "An EventBridge event bus keeps its events, so a target can read or replay them later.",
     "truth": ("A Classic event bus does not retain events and EventBridge does not persist them; to keep events and send "
               "them again, add an archive and start a replay."),
     "facts": ["eventbridge-classic-bus-does-not-retain-events", "eventbridge-decision-no-persistence-at-least-once",
               "eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "messaging-trap-short-visibility-safer",
     "belief": "A short visibility timeout is the safe choice, because a failed message comes back sooner.",
     "truth": ("If the visibility timeout ends while the consumer still works, another consumer receives a duplicate of the "
               "message; set the timeout longer than the processing time."),
     "facts": ["sqs-visibility-timeout-too-short-gives-duplicate", "sqs-visibility-timeout-too-long-delays-retry"],
     "placed_in": D + SID[3] + " (Exam trap callout)"},
    {"id": "messaging-trap-fifo-global-order",
     "belief": "A FIFO queue keeps one order across all of its messages, whatever their message group IDs.",
     "truth": ("Order is strict only within one message group ID; messages with different group IDs may arrive or be "
               "processed out of order relative to one another."),
     "facts": ["sqs-fifo-order-strict-within-group", "sqs-fifo-no-order-across-groups"],
     "placed_in": D + SID[5] + " (Exam trap callout)"},
    {"id": "messaging-trap-dlq-fresh-retention",
     "belief": "A message that moves to a dead-letter queue starts a new retention period there.",
     "truth": ("In a standard queue the enqueue timestamp does not change when the message moves, so the dead-letter queue "
               "needs a retention period longer than the source queue's."),
     "facts": ["sqs-dlq-standard-enqueue-timestamp-unchanged", "sqs-dlq-retention-longer-than-source-queue"],
     "placed_in": D + SID[6] + " (Exam trap callout)"},
    {"id": "messaging-trap-lambda-retries-failed-only",
     "belief": "When one message of a batch that Lambda reads from SQS fails, Lambda retries only that message.",
     "truth": ("Retries go through the queue: without a partial batch response the failed batch becomes visible again; with "
               "ReportBatchItemFailures, Lambda makes only the failed messages visible again."),
     "facts": ["lambda-sqs-partial-batch-response", "lambda-queue-esm-retry-set-on-queue"],
     "placed_in": D + SID[8] + " (Exam trap callout)"},
    {"id": "messaging-trap-subscribe-without-queue-policy",
     "belief": "Subscribing an SQS queue to an SNS topic is enough for the messages to arrive.",
     "truth": ("The queue's access policy must allow the topic to send messages; the aws:SourceArn condition limits that "
               "permission to the one topic."),
     "facts": ["sns-sqs-queue-needs-policy-allowing-topic", "sns-queue-policy-sourcearn-limits-to-one-topic"],
     "placed_in": D + SID[10] + " (Exam trap callout)"},
    {"id": "messaging-trap-filter-needs-function",
     "belief": "To send only some of a topic's messages to one subscriber, you put a Lambda function between the topic and the subscriber.",
     "truth": ("A subscriber receives every message by default; a filter policy on its subscription makes SNS send it only "
               "the messages that match."),
     "facts": ["sns-filter-default-every-message", "sns-filter-nonmatching-message-not-sent"],
     "placed_in": D + SID[11] + " (Exam trap callout)"},
    {"id": "messaging-trap-dlq-on-topic",
     "belief": "An SNS dead-letter queue is set once on the topic and catches the failed deliveries of every subscriber.",
     "truth": ("An SNS dead-letter queue is attached to a subscription, not to the topic, because deliveries happen at the "
               "subscription level; without one, SNS discards a message when its retries end."),
     "facts": ["sns-dlq-attached-to-subscription-not-topic", "sns-retry-exhausted-discards-unless-dlq"],
     "placed_in": D + SID[13] + " (Exam trap callout)"},
    {"id": "messaging-trap-iam-policy-enough-cross-account",
     "belief": "An IAM policy in the sender's own account is enough to send messages to a queue in another account.",
     "truth": ("The queue's access policy must also allow that principal; identity-based policies alone are not sufficient "
               "for cross-account access to a queue, whose default policy allows only the owner."),
     "facts": ["sqs-cross-account-needs-queue-access-policy", "sqs-default-access-policy-owner-only"],
     "placed_in": D + SID[14] + " (Exam trap callout)"},
]

BRIEF["traps_from_other_chapters"] = {
    "rule": ("Question writers can tag a distractor with a trap id of another chapter when the distractor states exactly that "
             "belief (lint.traps() knows them; build_brief.py confirmed each id below on 2026-10-14). Q205 needs a trap id on "
             "at least half of all wrong options of the chapter; reuse is allowed."),
    "ids": {
        "auto-scaling-trap-queue-length-metric": "target tracking on the visible messages alone scales a worker group correctly (17)",
        "lambda-trap-function-dlq-for-sqs": "the function's dead-letter queue or on-failure destination catches failing SQS messages (18)",
        "lambda-trap-scales-without-limit": "Lambda scales without limit, so a spike is never throttled (18)",
        "s3-trap-event-notification-fifo": "S3 event notifications can go directly to an SQS FIFO queue (21)",
        "kms-trap-aws-managed-key-controllable": "you can edit the key policy of an AWS managed key such as aws/sqs (06)",
        "iam-trap-cross-account-one-policy": "across accounts one side is enough (03); pair it with messaging-trap-iam-policy-enough-cross-account only when the option names a policy on one side",
        "how-the-exam-asks-trap-keyword-bait": "an option that repeats a stem keyword ('decouple', 'event-driven') must be right (01)",
        "how-the-exam-asks-trap-cheapest-wins": "the cheapest option wins even when it misses a requirement (01)",
        "how-the-exam-asks-trap-newest-feature-wins": "the newest feature is the answer when it fits (01)",
        "how-the-exam-asks-trap-eventually-means-maybe": "'eventually' means the data may never arrive (01)",
    },
}

BRIEF["compare_tables"] = [
    {"title": "SQS SNS or EventBridge", "section": "1-fast.md#choose-it-or-not", "h3_section_id": "sqs-sns-or-eventbridge",
     "neighbours": ["Amazon SQS", "Amazon SNS", "Amazon EventBridge"],
     "rows": ("Columns: Question | SQS | SNS | EventBridge (4 columns). How a message moves: consumers poll, a [Pull-based model] "
              "(sqs-decision-pull-model) | a [Push-based model] (sns-decision-push-model) to every subscriber | it "
              "[matches events against rules] (eventbridge-decision-rule-routing) and routes them to targets. What it keeps (Recap 1 asks for this row): the message, [until successfully "
              "processed or expired] (sqs-decision-keeps-until-processed) | nothing: [Messages are not persisted] "
              "(sns-decision-no-persistence) | nothing: it [doesn't persist events] "
              "(eventbridge-decision-no-persistence-at-least-once). Typical use: [buffering requests] (sqs-decision-typical-use) "
              "| [fanout notifications] (sns-decision-typical-use) | AWS and SaaS events, [cross-account event sharing] "
              "(eventbridge-decision-typical-use). Three rows."),
     "deciding_question": ("Does one consumer pull the work at its own pace, must every subscriber get a copy now, or must a "
                           "rule choose the targets by event content?")},
    {"title": "Standard or FIFO queue", "section": "1-fast.md#choose-it-or-not", "h3_section_id": "standard-or-fifo-queue",
     "neighbours": ["SQS standard queue", "SQS FIFO queue"],
     "rows": ("Columns: Question | Standard queue | FIFO queue (3 columns). Copies delivered: [at-least-once message delivery] "
              "(sqs-standard-at-least-once-duplicates) | [exactly-once processing] (sqs-faq-fifo-exactly-once-processing). "
              "Order: a [best-effort attempt] (sqs-standard-best-effort-ordering) | [sent and received in strict order] "
              "(sqs-fifo-order-strict-within-group), within each message group. Throughput (cut first if over budget): "
              "[nearly unlimited] (sqs-standard-throughput-nearly-unlimited) API calls | up to [3,000 messages per second with "
              "batching] (sqs-faq-fifo-default-throughput-3000-with-batching-300-without) by default. Three rows."),
     "deciding_question": "Must order within a group and no duplicates be guaranteed, or is the highest throughput with idempotent consumers enough?"},
    {"title": "Hide a message or schedule the work", "section": "1-fast.md#choose-it-or-not",
     "h3_section_id": "hide-a-message-or-schedule-the-work",
     "neighbours": ["SQS delay queue", "SQS visibility timeout", "Amazon EventBridge Scheduler"],
     "rows": ("Columns: Question | Delay queue | Visibility timeout | EventBridge Scheduler (4 columns). What it does: hides a "
              "new message, [hidden when it is first added to queue] (sqs-delay-queue-hidden-at-add-visibility-after-receive) | "
              "hides a received message, [only after it is consumed from the queue] "
              "(sqs-delay-queue-hidden-at-add-visibility-after-receive) | starts a task: [rate-based, cron-based, and one-time "
              "schedules] (eventbridge-scheduler-three-schedule-types). Longest wait: [15 minutes] (sqs-delay-queue-range) | [12 "
              "hours] (sqs-visibility-timeout-range) | any time later: [EventBridge Scheduler is the recommended solution] "
              "(sqs-eventbridge-scheduler-for-advanced-scheduling). Two rows. A message timer has the same range as a delay "
              "queue: plain words, no extra link."),
     "deciding_question": ("Must a new message wait before anyone sees it, must a received message stay hidden while it is "
                           "processed, or must work start at a set time?")},
    {"title": "SQS Amazon MQ or Kinesis Data Streams", "section": "1-fast.md#choose-it-or-not",
     "h3_section_id": "sqs-amazon-mq-or-kinesis-data-streams",
     "neighbours": ["Amazon SQS", "Amazon MQ", "Amazon Kinesis Data Streams"],
     "rows": ("Columns: Question | SQS | Amazon MQ | Kinesis Data Streams (4 columns). Made for: new cloud applications, "
              "[recommended for new applications] (sqs-sns-recommended-for-new-applications) | moving existing broker "
              "applications: [We recommend Amazon MQ for migrating applications] (sqs-vs-mq-new-apps-vs-broker-migration) | "
              "[real-time processing of streaming big data] (sqs-faq-kinesis-streams-realtime-and-replay). Code: the SQS API | "
              "[without rewriting the messaging code] (sns-faq-mq-for-existing-apps-standards-based-brokers) | the Kinesis API, and several readers can "
              "[read and replay records] (sqs-faq-kinesis-streams-realtime-and-replay). Two rows. Chapters 32 and 34 teach MQ "
              "and Kinesis: <!-- xref: 32 Amazon MQ --> <!-- xref: 34 Kinesis Data Streams -->."),
     "deciding_question": ("Is it a new application, an existing broker application that must move without code changes, or a "
                           "stream that several readers replay?")},
]

BRIEF["signals"] = [
    {"stem": "decouple; the database cannot keep up at peak", "think": "an SQS queue between the tiers",
     "fact": "sqs-decision-keeps-until-processed",
     "because": "it keeps each message [until successfully processed or expired] (sqs-decision-keeps-until-processed)",
     "but_not_if": "every service needs every message: an SNS topic with one queue per service"},
    {"stem": "every service must receive every message", "think": "an SNS topic with one SQS queue per service",
     "fact": "sns-publish-sends-message-to-each-subscribed-queue",
     "because": "SNS [sends the message to each subscribed queue] (sns-publish-sends-message-to-each-subscribed-queue)",
     "but_not_if": "services choose events by content from AWS services or SaaS: EventBridge rules"},
    {"stem": "process in order; no duplicates", "think": "an SQS FIFO queue, one message group ID per entity",
     "fact": "sqs-fifo-order-strict-within-group",
     "because": "a group's messages are [sent and received in strict order] (sqs-fifo-order-strict-within-group)",
     "but_not_if": "order does not matter and throughput must be nearly unlimited: a standard queue"},
    {"stem": "react to an AWS service event or a SaaS event", "think": "an EventBridge rule",
     "fact": "eventbridge-default-bus-receives-aws-service-events",
     "because": "the default bus [automatically receives events from AWS services] (eventbridge-default-bus-receives-aws-service-events)",
     "but_not_if": "the message must reach thousands of phones or email addresses: SNS"},
    {"stem": "run a job every night; send a reminder in three days", "think": "EventBridge Scheduler",
     "fact": "eventbridge-scheduler-three-schedule-types",
     "because": "it runs [rate-based, cron-based, and one-time schedules] (eventbridge-scheduler-three-schedule-types)",
     "but_not_if": "each message only needs a short delay: an SQS delay queue, up to [15 minutes] (sqs-delay-queue-range)"},
    {"stem": "a message fails again and again; poison message", "think": "a dead-letter queue with a redrive policy",
     "fact": "sqs-dlq-max-receive-count-meaning",
     "because": "maxReceiveCount is the [number of times a consumer can receive] (sqs-dlq-max-receive-count-meaning) it",
     "but_not_if": ("the FIFO order must never break: a dead-letter queue can [break the exact order of messages or operations] "
                    "(sqs-dlq-with-fifo-can-break-order)"),
     "note": "Recap 2 asks for this row and its 'But not if'."},
    {"stem": "reduce empty receives; lower the cost of polling", "think": "long polling",
     "fact": "sqs-faq-long-polling-fewer-empty-receives-lower-cost",
     "because": "it can [reduce the number of empty receives] (sqs-faq-long-polling-fewer-empty-receives-lower-cost)",
     "but_not_if": "the call must return at once on an empty queue: short polling [returns immediately] (sqs-faq-long-polling-waits-for-message)"},
    {"stem": "scale the workers on the queue", "think": "target tracking on backlog per instance",
     "fact": "ec2-auto-scaling-sqs-queue-length-not-proportional",
     "because": "queue length alone [might not change proportionally] (ec2-auto-scaling-sqs-queue-length-not-proportional) to the group",
     "but_not_if": "Lambda reads the queue: [Lambda handles the polling] (lambda-esm-lambda-polls-source) and the scaling"},
]

BRIEF["words_table"] = [
    {"term": "queue", "respelling": "KYOO", "collocation": "poll a queue (bold: poll)", "do_not_confuse": "topic",
     "bank": "queue (in the bank)"},
    {"term": "topic", "respelling": None, "collocation": "subscribe a queue to a topic (bold: subscribe)",
     "do_not_confuse": "queue", "bank": "topic (in the bank)"},
    {"term": "visibility timeout", "respelling": None, "collocation": "set the visibility timeout of the queue (bold: set)",
     "do_not_confuse": "delay queue", "bank": "visibility-timeout (in the bank)"},
    {"term": "dead-letter queue", "respelling": None, "collocation": "configure a dead-letter queue (bold: configure)",
     "do_not_confuse": "visibility timeout", "bank": "dead-letter-queue (in the bank)"},
    {"term": "idempotent", "respelling": "eye-dem-POH-tent", "collocation": "make the consumer idempotent (bold: make)",
     "do_not_confuse": "exactly-once processing", "bank": "idempotent (in the bank)"},
    {"term": "message group ID", "respelling": None, "collocation": "set a message group ID (bold: set)",
     "do_not_confuse": "deduplication ID", "bank": "term_request message-group-id"},
    {"term": "fan-out", "respelling": None, "collocation": "the fan-out pattern (bold: pattern)",
     "do_not_confuse": "filter policy", "bank": "term_request fan-out"},
    {"term": "event bus", "respelling": None, "collocation": "send events to an event bus (bold: send)",
     "do_not_confuse": "topic", "bank": "term_request event-bus"},
]

BRIEF["numbers"] = {
    "a_list": [
        {"display": "4 days", "fact": "sqs-message-retention-default", "card": "messaging-c001",
         "what": "Default message retention period", "why": "a message older than the retention period is deleted unread"},
        {"display": "14 days", "fact": "sqs-message-retention-range", "card": "messaging-c002",
         "what": "Longest message retention period", "why": "a longer outage needs another store, such as Amazon S3"},
        {"display": "30 seconds", "fact": "sqs-visibility-timeout-default", "card": "messaging-c003",
         "what": "Default visibility timeout", "why": "longer work at the default gives duplicates"},
        {"display": "12 hours", "fact": "sqs-visibility-timeout-range", "card": "messaging-c004",
         "what": "Longest visibility timeout, counted from the receive", "why": "longer jobs need another design, such as Step Functions"},
        {"display": "20 seconds", "fact": "sqs-long-polling-max-wait", "card": "messaging-c005",
         "what": "Longest long-polling wait", "why": "the answer to 'fewer empty receives'"},
        {"display": "15 minutes", "fact": "sqs-delay-queue-range", "card": "messaging-c006",
         "what": "Longest delay of a delay queue or message timer", "why": "a later start needs EventBridge Scheduler"},
        {"display": "3,000 messages per second with batching", "display2": "300 messages per second",
         "fact": "sqs-faq-fifo-default-throughput-3000-with-batching-300-without", "card": "messaging-c007",
         "what": "FIFO queue throughput by default (link both displays in cell 1)",
         "why": "above it, use a standard queue or high throughput mode"},
        {"display": "5", "fact": "eventbridge-quota-targets-per-rule", "card": "messaging-c008",
         "what": "Targets of one EventBridge rule (not adjustable); write the cell '[5](...) targets'",
         "why": "more receivers need a second rule or an SNS topic as a target"},
    ],
    "b_list": [
        {"display": "1 MiB", "fact": "sqs-message-size-range", "what": "Largest SQS message (volatile: changed 2025-08-04)"},
        {"display": "2 GB", "fact": "sqs-extended-client-max-payload", "what": "Payload through the Extended Client Library and Amazon S3"},
        {"display": "10 messages", "fact": "sqs-batch-max-messages", "what": "Messages in one batch request"},
        {"display": "5 minute deduplication interval", "fact": "sqs-fifo-deduplication-interval-5-minutes",
         "what": "FIFO deduplication window"},
        {"display": "approximately 120,000 in flight messages", "fact": "sqs-in-flight-standard-limit",
         "what": "In-flight messages of most standard queues; FIFO: [120,000 in-flight messages] (sqs-in-flight-fifo-limit)"},
        {"display": "24 hours", "fact": "eventbridge-retry-default-24h-185-attempts",
         "what": "EventBridge retry time per target by default, [up to 185 times] (eventbridge-retry-default-24h-185-attempts)"},
        {"display": "100,015 times", "fact": "sns-retry-aws-managed-total-attempts",
         "what": "SNS delivery attempts to SQS and Lambda, [over 23 days] (sns-retry-aws-managed-total-attempts)"},
        {"display": "3,600 seconds", "fact": "sns-retry-http-total-retry-time-max", "what": "Longest total retry time to an HTTP/S endpoint"},
        {"display": "256 KiB", "fact": "sns-message-size-default-256kib", "what": "Default SNS message size (volatile)"},
        {"display": "100 per topic", "fact": "sns-quota-subscriptions-per-topic",
         "what": "Subscriptions of a FIFO topic; standard: [12,500,000 per topic] (sns-quota-subscriptions-per-topic)"},
        {"display": "up to 15 minutes", "fact": "sns-filter-policy-change-up-to-15-minutes", "what": "Time for a filter policy change"},
        {"display": "1 MB", "fact": "eventbridge-putevents-request-size-under-1mb",
         "what": "Largest PutEvents request (volatile: changed 2026-01-29)"},
    ],
    "not_used": [
        "Prices (SNS $0.50 per million requests, EventBridge $1.00/M custom events, Scheduler free tier 14,000,000 invocations, "
        "SQS free tier 1 million requests): volatile price facts; no row; tasks state about $0 without a price fact.",
        "FIFO high throughput mode quotas (70,000 and 700,000 per second, 2,400 TPS): volatile and Region-dependent; no row.",
        "SNS publish throttles (30,000 messages per second in US East (N. Virginia), 300 elsewhere): Region-dependent; no row.",
        "Lambda scaling numbers (five batches, 300 more per minute, 1,250, maximum concurrency 2 to 1,000): subsection 8 only; chapter 18 owns them.",
        "EventBridge quotas (100 buses, 300 rules per bus, 2,048 characters per pattern, 30 wildcard rules), Scheduler quotas "
        "(10,000,000 schedules, 500 groups, flexible window 1 to 1440, retries 0 to 185, event age 60 to 86400): reference only.",
        "Global endpoints RTO and RPO (360 seconds, at most 420): reference only, chapter 40 owns recovery numbers.",
        "SQS policy quotas (8,192 bytes, 20 statements, 50 principals, 10 conditions), queue name 80 characters: reference only.",
    ],
}

BRIEF["changed_recently"] = {
    "fast": [
        {"date": "2025-08-04", "what": "Largest SQS message", "fact": "sqs-change-max-message-size-1mib-2025",
         "old_display": "256 KiB", "now_display": "1,048,576 bytes (1 MiB)",
         "exam_probably_expects": ("older questions say 256 KB and send larger payloads through Amazon S3 with the Extended "
                                   "Client Library; prefer an option that is right under both values."),
         "status": "examinable",
         "note": "Old: [256 KiB](...), Now: [1,048,576 bytes (1 MiB)](...), both links to sqs-change-max-message-size-1mib-2025. Volatile: never a question key."},
        {"date": "2026-01-29", "what": "Largest EventBridge event (PutEvents request)", "fact": "eventbridge-change-event-size-1mb-2026",
         "old_display": "256 KB", "now_display": "1 MB (1,048,576 bytes)",
         "exam_probably_expects": "the old value, if any. Do not let this number decide an answer.",
         "status": "examinable",
         "note": ("2026-01-29 is before the cut-off 2026-07-15, so the entry is examinable; the fact names five Regions without "
                  "it: do not write 'all Regions'. Volatile: never a question key.")},
        {"date": "2023-11-27", "what": "Redrive from a FIFO dead-letter queue", "fact": "sqs-change-fifo-dlq-redrive-2023",
         "old_display": "not available. (fixed text; before the change only standard dead-letter queues could be redriven)",
         "now_display": "must be a FIFO queue as well",
         "exam_probably_expects": ("older questions may say that only standard dead-letter queues can be redriven; today a FIFO "
                                   "dead-letter queue redrives to a FIFO queue."),
         "status": "examinable",
         "note": ("Write the Now line as: 'a FIFO dead-letter queue can be redriven; the destination [must be a FIFO queue as "
                  "well](...)'. The date comes from changed.date of the fact (L107); the What's New page is robots-blocked, so "
                  "no date display exists: write the date only in the '(2023-11-27)' slot.")},
    ],
    "deep": [
        {"date": "2026-09-18", "what": "Largest SNS message (opt-in per topic)", "fact": "sns-change-max-message-size-1mib-opt-in-2026",
         "old_display": "256 KiB", "now_display": "1 MiB",
         "exam_probably_expects": "the old value, if any. Do not let this number decide an answer.",
         "status": "not examinable yet",
         "placement": "2-deep.md directly under the B-list (U3), last line '**Status:** not examinable yet.'",
         "note": "The default stays 256 KiB; the opt-in needs 100 or fewer subscriptions of supported types. No question uses it."},
    ],
    "considered_not_used": [
        {"fact": "eventbridge-change-custom-event-bus-classic-rename-2026",
         "why": "new Custom Event Bus GA 2026-09-24, after the cut-off, and the fact has no changed record, so an entry cannot pass L107; notes_for_orchestrator"},
        {"fact": "sqs-change-default-sse-all-queues-2022", "why": "no changed record; default SSE is current truth in the subsection 14 Go deeper"},
        {"fact": "sqs-change-fair-queues-standard-2025", "why": "no changed record; current truth in the subsection 5 Go deeper"},
        {"fact": "sqs-change-sendmessage-needs-only-generatedatakey-2024",
         "why": "no changed record and a kept conflict with the current key-management page; the book says 'grant both'"},
        {"fact": "sns-change-fifo-throughput-scope-high-throughput-2025", "why": "no changed record; FIFO topic throughput is reference only"},
        {"fact": "eventbridge-change-direct-delivery-cross-account-targets-2025", "why": "no changed record; reference only"},
        {"fact": "eventbridge-change-targets-sqs-fair-queues-2025", "why": "no changed record; the target list of subsection 12 names fair queues"},
        {"fact": "sns-change-fifo-archiving-replay-2023", "why": "no changed record; SNS FIFO archive is reference only"},
        {"fact": "sns-change-fifo-standard-queue-subscribers-2023", "why": "no changed record; the subsection 10 table carries it"},
        {"fact": "sns-change-payload-based-filtering-2022", "why": "no changed record; the subsection 11 trace carries body filtering"},
        {"fact": "sns-change-message-data-protection-closed-to-new-customers-2026", "why": "message data protection is not taught"},
        {"fact": "sqs-change-fifo-high-throughput-quotas-raised-2022", "why": "no changed record; quotas are volatile"},
        {"fact": "eventbridge-change-scheduler-launch-2022", "why": "documentation history only; Scheduler is current truth"},
    ],
}

BRIEF["faq"] = [
    {"n": 1, "q": "Can you convert an existing standard queue to a FIFO queue?", "fact": "sqs-faq-cannot-convert-standard-to-fifo",
     "answer": "No; you [choose the queue type when you create it] (sqs-faq-cannot-convert-standard-to-fifo), so create a new FIFO queue.",
     "quote": "No. You must choose the queue type when you create it.", "url": "https://aws.amazon.com/sqs/faqs/"},
    {"n": 2, "q": "Does a long-polling ReceiveMessage call cost more than a short-polling one?", "fact": "sqs-faq-long-polling-no-extra-charge",
     "answer": "No; long polls are [billed exactly the same] (sqs-faq-long-polling-no-extra-charge).",
     "quote": "Long-polling ReceiveMessage calls are billed exactly the same as short-polling ReceiveMessage calls.",
     "url": "https://aws.amazon.com/sqs/faqs/"},
    {"n": 3, "q": "Can a deleted message come back from a standard queue?", "fact": "sqs-faq-deleted-message-standard-may-repeat-fifo-never",
     "answer": "Rarely, yes: you might get a [previously-deleted message a second time] (sqs-faq-deleted-message-standard-may-repeat-fifo-never).",
     "quote": "For standard queues, under rare circumstances, you might receive a previously-deleted message a second time.",
     "url": "https://aws.amazon.com/sqs/faqs/"},
    {"n": 4, "q": "Can a queue share its messages with a queue in another Region?", "fact": "sqs-faq-queues-are-independent-per-region",
     "answer": "No; each queue is [independent within each region] (sqs-faq-queues-are-independent-per-region).",
     "quote": "Each Amazon SQS message queue is independent within each region.", "url": "https://aws.amazon.com/sqs/faqs/"},
    {"n": 5, "q": "Can a FIFO queue use a standard queue as its dead-letter queue?", "fact": "sqs-faq-dlq-fifo-needs-fifo-standard-needs-standard",
     "answer": "No; you [must use a FIFO dead letter queue] (sqs-faq-dlq-fifo-needs-fifo-standard-needs-standard) with a FIFO queue.",
     "quote": "However, you must use a FIFO dead letter queue with a FIFO queue.", "url": "https://aws.amazon.com/sqs/faqs/"},
    {"n": 6, "q": "Can you recall a message after you publish it to a topic?", "fact": "sns-faq-published-message-cannot-be-recalled",
     "answer": "No; it [cannot be recalled] (sns-faq-published-message-cannot-be-recalled).",
     "quote": "No, once a message has been successfully published to a topic, it cannot be recalled.",
     "url": "https://aws.amazon.com/sns/faqs/"},
    {"n": 7, "q": "Can any AWS account publish to your topic by default?", "fact": "sns-faq-default-only-topic-owner-can-publish",
     "answer": "No; by default [only topic owners have permissions to publish] (sns-faq-default-only-topic-owner-can-publish).",
     "quote": "By default, only topic owners have permissions to publish to a topic.", "url": "https://aws.amazon.com/sns/faqs/"},
    {"n": 8, "q": "Does a standard SNS topic deliver messages in the order they were published?",
     "fact": "sns-faq-order-attempted-but-network-issues-can-reorder",
     "answer": ("Not always; SNS tries, but subscribers can see [out-of-order messages at the subscriber end] "
                "(sns-faq-order-attempted-but-network-issues-can-reorder). For order, use a FIFO topic."),
     "quote": "However, network issues could potentially result in out-of-order messages at the subscriber end.",
     "url": "https://aws.amazon.com/sns/faqs/"},
    {"n": 9, "q": "Can EventBridge Scheduler call a third-party HTTPS endpoint directly?", "fact": "eventbridge-faq-scheduler-no-direct-non-aws-targets",
     "answer": ("No; it [does not support non-AWS targets directly] (eventbridge-faq-scheduler-no-direct-non-aws-targets). Use "
                "Lambda or the [API destinations feature] (eventbridge-faq-scheduler-no-direct-non-aws-targets)."),
     "quote": "EventBridge Scheduler does not support non-AWS targets directly.", "url": "https://aws.amazon.com/eventbridge/faqs/"},
    {"n": 10, "q": "Can one EventBridge rule send an event to several targets?",
     "fact": "eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel",
     "answer": "Yes; a rule can [route to multiple targets] (eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel), all [processed in parallel] (eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel).",
     "quote": "A single rule can route to multiple targets, all of which are processed in parallel.",
     "url": "https://aws.amazon.com/eventbridge/faqs/"},
]
BRIEF["faq_alternates"] = [
    "sns-faq-same-account-sqs-subscription-needs-no-opt-in",
    "sqs-faq-purge-queue-deletes-all-messages",
    "sqs-faq-delete-already-deleted-returns-success",
    "eventbridge-faq-pipes-do-not-need-an-event-bus",
    "eventbridge-faq-global-endpoints-custom-events-only",
]
BRIEF["faq_note"] = (
    "Each quote block holds whole sentences of the evidence quote of the item's fact, copied exactly (F2, L306); "
    "build_brief.py checked each 'quote' against the stored evidence and its URL. The link line under each quote is '— "
    "[Amazon SQS FAQs](https://aws.amazon.com/sqs/faqs/)', '— [Amazon SNS FAQs](https://aws.amazon.com/sns/faqs/)' or '— "
    "[Amazon EventBridge FAQs](https://aws.amazon.com/eventbridge/faqs/)'. Item 5 and item 8 begin with 'However,': keep it, it "
    "is part of the sentence. Item 1 is two whole sentences ('No.' and the next). If the section runs over 450 words, shorten "
    "the short answers first, never a quote.")

BRIEF["story"] = {
    "stage": 2, "month": 12,
    "trigger": "Launch day, 10:20 Eastern. The web tier scales out, but each upload request waits for the one worker. In 47 minutes, 1,900 uploads fail.",
    "problem": ("After each upload, Callvale's web application calls the worker and waits. On launch day, the worker was "
                "overloaded and 1,900 uploads failed. No upload can be lost again, and one failed recording must not block the "
                "others. Several systems must learn when a transcript is ready."),
    "uses_numbers": ["launch_day_incident", "dead_letter_after_receives", "worker_group_max"],
    "state_at_month_12": ("Stage 2, story order 12 (month 12, the first chapter of launch week, before chapter 18 in the same "
                          "month). Before: pipeline state P1 (the web application calls the one worker directly and waits; "
                          "scheduled jobs on the worker register uploads, save results and send notifications; job status in "
                          "PostgreSQL). After: P2 (S3 event, uploads queue, start-job function, convert queue, conversion "
                          "workers in an Auto Scaling group from zero to 40 that scales on the backlog, a chain of functions for "
                          "Amazon Transcribe and Amazon Comprehend, save-results, the transcript-ready topic that fans out to the "
                          "webhooks and indexing queues; job status still in PostgreSQL through Amazon RDS Proxy). Not yet: the "
                          "state machine (32), DynamoDB (28), ops-alerts (stage 3, 37)."),
    "rules": ("Question stems never name Callvale. The story never teaches a fact. No dollar amounts in story text. Ben's "
              "question is the speak item messaging-s01. W903: in the Startup example callouts and the Decision record, write "
              "digits only for numbers of uses_numbers: 47 (minutes of the failure), 1,900 (failed uploads), 900 (database "
              "connections), 6 (hours the worker was behind), 10:20 (time), 12 (month), 3 (failed receives before the "
              "dead-letter queue), 40 (maximum conversion workers). Write 'zero' as a word."),
}

BRIEF["decision_record"] = {
    "status": "write",
    "context": ("The trigger of data/startup.json chapter 31 plus the incident numbers, at most 80 words, stage 2: 'Launch day, "
                "month 12, 10:20. The web tier scaled out, but each upload request waited for the one worker. In 47 minutes, "
                "1,900 uploads failed. The database reached 900 connections, and the worker was 6 hours behind.' (about 40 "
                "words)."),
    "requirement": ("No upload can be lost, one failed recording must not block the others, and several systems must learn "
                    "when a transcript is ready, with the MOST resilient design (qualifier of the JSON: most resilient)."),
    "requirement_qualifier": "most resilient",
    "options": [
        "more and larger workers behind an internal load balancer",
        "Amazon SQS queues, with an Amazon SNS topic for results (chosen)",
        "one stream for all events",
    ],
    "decision": ("SQS queues between the stages, an SNS topic that fans out results, and EventBridge for AWS events and "
                 "schedules (data/startup.json choice). Name the parts: the uploads and convert queues, each with a dead-letter "
                 "queue; the transcript-ready topic with the webhooks and indexing queues; EventBridge schedules for the nightly "
                 "jobs. The convert queue moves a message to convert-dlq after 3 failed receives (the JSON note); do not attach "
                 "the number 3 to the uploads queue (see notes_for_orchestrator)."),
    "reasons_with_facts": [
        ("Option 1 keeps the direct call: each upload still waits for a worker, and a worker that fails still loses the "
         "request. Well-Architected advises to [make component interactions asynchronous where possible] "
         "(sqs-wa-make-component-interactions-asynchronous)."),
        ("Option 3 fits a different problem: a stream is for [real-time processing of streaming big data] "
         "(sqs-faq-kinesis-streams-realtime-and-replay); each upload here is one job that one worker takes."),
        ("Option 2: SQS [stores the message in multiple availability zones] (sqs-send-stored-multi-az-before-ack) before the "
         "upload request returns; a recording that keeps failing moves aside [before it is moved to a dead-letter queue] "
         "(sqs-dlq-max-receive-count-meaning) blocks nobody; the topic [sends the message to each subscribed queue] "
         "(sns-publish-sends-message-to-each-subscribed-queue), so webhooks and indexing each get every transcript."),
    ],
    "tradeoff": ("Processing is asynchronous: users see 'processing', and workers must handle the same message twice without "
                 "harm (data/startup.json tradeoff, word for word). Optional link on the last clause: [Design your applications "
                 "to be idempotent] (sqs-copies-on-multiple-servers-cause-duplicates)."),
    "later": ("One sentence at most: from stage 3, EventBridge rules route AWS service events to the ops-alerts topic (chapter "
              "37). No new option in the record."),
    "spot_the_bug": None,
    "diagrams": ["messaging-before", "messaging-after"],
}

BRIEF["realworld"] = {
    "status": "skip",
    "why": ("The template's first paragraph needs '**Company, year.**' (bold_fields.realworld_first_paragraph_regex). The "
            "verified case facts (eventbridge-case-hanwha-qcells-scheduling-jobs, eventbridge-case-legendary-play-fine-grained-rules, "
            "sqs-case-migros-one-eks-microservices) state no year, and a year from memory is not allowed. The section is "
            "optional and not in the sections list, so leaving it out is no L905 error. If a later run verifies a year, the "
            "best candidate is Hanwha Qcells with the quote 'Amazon EventBridge streamlined scheduling tasks, reducing the time "
            "needed to set up jobs from weeks to just a few clicks.' (20 words, "
            "https://aws.amazon.com/solutions/case-studies/hanwha-qcells-case-study/)."),
}

BRIEF["devices"] = {
    "exam_trap_callouts_2_deep": {
        SID[3]: "messaging-trap-short-visibility-safer",
        SID[5]: "messaging-trap-fifo-global-order",
        SID[6]: "messaging-trap-dlq-fresh-retention",
        SID[8]: "messaging-trap-lambda-retries-failed-only",
        SID[10]: "messaging-trap-subscribe-without-queue-policy",
        SID[11]: "messaging-trap-filter-needs-function",
        SID[13]: "messaging-trap-dlq-on-topic",
        SID[14]: "messaging-trap-iam-policy-enough-cross-account",
    },
    "exam_trap_form": ("> **Exam trap:** <wrong belief in plain words>. <truth with its fact link>. <!-- trap: <id> -->  Each "
                       "one adds a new case; never restate the table above it. The plans give ready texts (exam_trap_text)."),
    "fast_traps_list": ["messaging-trap-receive-deletes", "messaging-trap-queue-broadcasts", "messaging-trap-topic-stores-messages",
                        "messaging-trap-standard-exactly-once", "messaging-trap-bus-stores-events"],
    "fast_traps_links": (
        "Each fast trap item links one fact in its Truth part: receive-deletes [temporarily invisible to other consumers] "
        "(sqs-receive-keeps-message-hidden); queue-broadcasts [multiple SQS standard queues to the SNS topic] "
        "(sns-faq-fanout-identical-messages-to-multiple-sqs-queues); topic-stores-messages [Messages are not persisted] "
        "(sns-decision-no-persistence); standard-exactly-once [more than one copy of a message] "
        "(sqs-standard-at-least-once-duplicates); bus-stores-events [doesn't persist events] "
        "(eventbridge-decision-no-persistence-at-least-once). The 'Wrong belief' half needs no link."),
    "go_deeper": [
        SID[3] + ": the 12-hour ceiling and the delay queue contrast",
        SID[5] + ": fair queues in a standard queue",
        SID[6] + ": the rules of a redrive",
        SID[12] + ": schedules (scheduled rules and EventBridge Scheduler)",
        SID[13] + ": archive and replay",
        SID[14] + ": encrypted queues and their senders",
    ],
    "spot_the_bug": [
        SID[3] + ": the convert queue keeps the default visibility timeout while a conversion can take up to 25 minutes",
        SID[14] + ": the uploads queue encrypted with the AWS managed key, and S3 event notifications stop",
    ],
    "try_it": [SID[3] + ": messaging-t02", SID[10] + ": messaging-t03"],
    "startup_example_2_deep": [SID[7] + ": the convert queue's workers scale from zero to 40 on the backlog per instance"],
    "predict_the_picture": ("In one breath: 'When a producer sends a message to a queue, where does the message wait, and when "
                            "does it leave the queue?' before the hero messaging-hero (LEARNING device 6)."),
    "route_pass_subsections": [SID[3], SID[5], SID[10], SID[12]],
    "route_pass_note": ("Four of the maximum four (section_flag.h3_pass_route_subsections): the visibility timeout, FIFO, "
                        "fan-out and EventBridge rules carry most exam questions of the chapter."),
    "xref_markers": [
        "11 VPC connectivity (interface endpoints for SQS and SNS)",
        "17 Auto Scaling (target tracking policies)",
        "18 Lambda (event source mappings, partial batch responses, asynchronous invocation destinations)",
        "21 S3 (event notifications, FIFO destinations not supported)",
        "06 KMS (customer managed keys, key policies)",
        "32 Step Functions and Amazon MQ",
        "34 Kinesis Data Streams",
        "37 Monitoring (CloudWatch alarms on queue metrics)",
    ],
}
