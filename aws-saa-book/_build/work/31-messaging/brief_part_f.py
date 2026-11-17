# brief-31, part F: terms, term requests, tasks, spoken prompts, cards, diagrams, fact requests and notes.

BRIEF["terms"] = ["queue", "topic", "decouple", "asynchronous", "idempotent", "dead-letter-queue", "visibility-timeout",
                  "event-source-mapping", "backlog-per-instance", "resource-based-policy", "retention-period"]


def term(tid, text, kind, meaning, collocations, do_not_confuse, facts, short=None, respelling=None, banned=None, avoid=None,
         id_note=None):
    d = {"id": tid, "term": text, "kind": kind, "short": short, "banned": banned or [], "banned_case": [], "avoid": avoid or [],
         "respelling": respelling, "meaning": meaning, "collocations": collocations, "do_not_confuse": do_not_confuse,
         "facts": facts}
    if id_note:
        d["id_note"] = id_note
    return d


BRIEF["term_requests"] = [
    term("producer", "producer", "concept", "A component that sends messages to a queue, a topic or an event bus.",
         ["the producer sends a message", "decouple the producer from the consumer"], ["consumer", "publisher"],
         ["sqs-locks-messages-multiple-producers-consumers"]),
    term("consumer", "consumer", "concept", "A component that receives messages from a queue and processes them.",
         ["the consumer polls the queue", "the consumer deletes the message"], ["subscriber", "producer"],
         ["sqs-decision-pull-model"], avoid=["client (for a consumer)"]),
    term("standard-queue", "standard queue", "aws-name",
         "The default SQS queue type: nearly unlimited throughput, at-least-once delivery and best-effort order.",
         ["create a standard queue", "a standard queue delivers at least once"], ["FIFO queue"],
         ["sqs-standard-at-least-once-duplicates"]),
    term("fifo-queue", "FIFO queue", "aws-name",
         "An SQS queue that keeps order inside each message group and does not introduce duplicates.",
         ["create a FIFO queue", "send messages to a FIFO queue"], ["standard queue", "FIFO topic"],
         ["sqs-fifo-order-strict-within-group"], respelling="FY-foh"),
    term("message-group-id", "message group ID", "aws-name",
         "The value that puts a FIFO message in a group; messages of one group keep their order.",
         ["set a message group ID", "one message group ID per customer"], ["message deduplication ID"],
         ["sqs-fifo-message-group-id-required"]),
    term("message-deduplication-id", "message deduplication ID", "aws-name",
         "The value that SQS uses to drop a repeated FIFO message within the deduplication interval.",
         ["send a message deduplication ID", "a duplicate deduplication ID"], ["message group ID"],
         ["sqs-fifo-deduplication-interval-5-minutes"]),
    term("content-based-deduplication", "content-based deduplication", "aws-name",
         "A FIFO setting that makes the deduplication ID from a hash of the message body.",
         ["turn on content-based deduplication"], ["message deduplication ID"],
         ["sqs-fifo-content-based-dedup-hash-body-only"]),
    term("long-polling", "long polling", "concept",
         "A receive call that asks all servers and waits for a message until its wait time ends.",
         ["turn on long polling", "long polling reduces empty receives"], ["short polling"],
         ["sqs-long-polling-queries-all-servers"]),
    term("short-polling", "short polling", "concept",
         "The default receive call: it asks a subset of servers and answers at once, even when it finds nothing.",
         ["short polling returns at once"], ["long polling"], ["sqs-short-polling-is-default-immediate-response"]),
    term("receipt-handle", "receipt handle", "aws-name", "The token of one receive that you give to DeleteMessage.",
         ["delete a message with its receipt handle"], ["message ID"], ["sqs-faq-receipt-handle-required-to-delete"]),
    term("in-flight-message", "in-flight message", "concept", "A message that a consumer received and has not yet deleted.",
         ["count the in-flight messages"], ["visible message"], ["sqs-metric-not-visible-messages-is-in-flight"]),
    term("delay-queue", "delay queue", "aws-name", "An SQS queue that hides every new message for a set delay.",
         ["create a delay queue", "a delay queue hides new messages"], ["visibility timeout", "message timer"],
         ["sqs-delay-queue-hides-new-messages"]),
    term("message-timer", "message timer", "aws-name", "A delay set on one message when it is added to a queue.",
         ["set a message timer"], ["delay queue"], ["sqs-message-timer-initial-invisibility"]),
    term("redrive-policy", "redrive policy", "aws-name",
         "The queue setting that names the dead-letter queue and the maximum number of receives.",
         ["set a redrive policy", "the redrive policy moves the message"], ["dead-letter queue redrive"],
         ["sqs-faq-dlq-redrive-policy-max-receive-count"]),
    term("dead-letter-queue-redrive", "dead-letter queue redrive", "aws-name",
         "Moving messages from a dead-letter queue back to their source queue or to another queue of the same type.",
         ["start a dead-letter queue redrive"], ["redrive policy"], ["sqs-faq-dlq-redrive-back-to-source-queue"]),
    term("poison-pill-message", "poison-pill message", "concept", "A message that fails every time a consumer processes it.",
         ["move a poison-pill message aside"], ["duplicate message"],
         ["sqs-faq-hosted-queue-between-microservices-dlq-poison-pill"]),
    term("at-least-once-delivery", "at-least-once delivery", "concept",
         "Each message is delivered one or more times, so a duplicate can arrive.",
         ["a standard queue gives at-least-once delivery"], ["exactly-once processing"],
         ["sqs-faq-standard-at-least-once-delivery"]),
    term("exactly-once-processing", "exactly-once processing", "concept",
         "Each message is delivered once and stays until a consumer processes and deletes it.",
         ["a FIFO queue gives exactly-once processing"], ["at-least-once delivery"], ["sqs-faq-fifo-exactly-once-processing"]),
    term("message-attribute", "message attribute", "aws-name", "A name, type and value sent with a message, beside its body.",
         ["add a message attribute", "filter on a message attribute"], ["message body"], ["sqs-faq-message-attributes-types"]),
    term("publishsubscribe", "publish/subscribe", "concept",
         "Messaging in which a publisher sends to a topic and every subscriber gets a copy; also called pub/sub.",
         ["publish/subscribe messaging", "the publish/subscribe model"], ["point-to-point messaging"],
         ["sns-decision-typical-use"], short="pub/sub",
         id_note="the GitHub anchor of 'publish/subscribe' drops the slash; the exam guide writes publish/subscribe"),
    term("subscription", "subscription", "aws-name", "The link between a topic and one endpoint that receives its messages.",
         ["create a subscription", "confirm a subscription"], ["topic", "subscriber"],
         ["sns-dlq-attached-to-subscription-not-topic"]),
    term("fan-out", "fan-out", "concept",
         "Sending one message to many receivers at the same time, often an SNS topic to several queues.",
         ["the fan-out pattern", "fan out messages to several queues"], ["filter policy", "load balancing"],
         ["sns-fanout-replicates-message-to-many-endpoints"], avoid=["fanout (in prose; AWS writes both)"]),
    term("filter-policy", "filter policy", "aws-name",
         "A subscription setting that makes SNS send only the messages whose attributes or body match it.",
         ["assign a filter policy to a subscription"], ["event pattern"], ["sns-filter-default-every-message"]),
    term("raw-message-delivery", "raw message delivery", "aws-name",
         "A subscription setting that sends the message as published, without the SNS JSON envelope.",
         ["turn on raw message delivery"], ["message attribute"], ["sns-raw-delivery-sqs-strips-sns-metadata"]),
    term("fifo-topic", "FIFO topic", "aws-name",
         "An SNS topic that keeps message order and removes duplicates, for SQS subscribers.",
         ["subscribe a FIFO queue to a FIFO topic"], ["FIFO queue", "standard topic"],
         ["sns-faq-fifo-topic-to-sqs-fifo-queue-end-to-end-ordering"], respelling="FY-foh"),
    term("event-bus", "event bus", "aws-name", "An EventBridge resource that receives events and routes them with rules.",
         ["send events to an event bus", "a custom event bus"], ["topic", "queue"],
         ["eventbridge-bus-many-sources-to-many-targets"]),
    term("default-event-bus", "default event bus", "aws-name",
         "The event bus of each account and Region that receives events from AWS services.",
         ["a rule on the default event bus"], ["custom event bus"], ["eventbridge-default-bus-receives-aws-service-events"]),
    term("partner-event-bus", "partner event bus", "aws-name", "An event bus that receives events from a SaaS partner.",
         ["create a partner event bus"], ["default event bus"], ["eventbridge-partner-bus-receives-saas-events"]),
    term("eventbridge-rule", "EventBridge rule", "aws-name",
         "A setting on one event bus that matches events with an event pattern and sends them to targets.",
         ["create an EventBridge rule", "the rule matches an event"], ["filter policy", "subscription"],
         ["eventbridge-faq-rule-matches-events-on-a-bus-and-routes-to-targets"]),
    term("event-pattern", "event pattern", "aws-name", "The part of a rule that an event must match, with the same structure as the event.",
         ["write an event pattern", "the event pattern matches"], ["filter policy"], ["eventbridge-event-pattern-matches-or-not"]),
    term("input-transformer", "input transformer", "aws-name",
         "A target setting that changes the shape of an event before EventBridge passes it to the target.",
         ["use the input transformer"], ["event pattern"], ["eventbridge-input-transformer-edits-event-before-target"]),
    term("event-replay", "event replay", "aws-name", "Sending archived events back to the event bus that first received them.",
         ["start an event replay", "replay events from an archive"], ["dead-letter queue redrive"],
         ["eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule"]),
    term("partial-batch-response", "partial batch response", "aws-name",
         "A Lambda response that names only the failed messages of an SQS batch, so only they return.",
         ["return a partial batch response"], ["dead-letter queue"], ["lambda-sqs-partial-batch-response"]),
]

BRIEF["term_amendments"] = [
    {"id": "queue", "add_facts": ["sqs-decision-keeps-until-processed"],
     "why": "The bank entry has no fact; this one grounds 'holds messages until a consumer processes them'."},
    {"id": "topic", "add_facts": ["sns-publish-sends-message-to-each-subscribed-queue"],
     "why": "The bank entry has no fact; this one grounds 'sends each published message to all of its subscribers'."},
    {"id": "dead-letter-queue",
     "add_meaning": "In SQS, the queue to which a source queue moves a message after its maximum number of receives.",
     "add_collocations": ["set the redrive policy to a dead-letter queue"],
     "add_facts": ["sqs-faq-dlq-definition-isolate-unprocessable-messages"],
     "why": "The bank's fact is a Lambda fact; the SQS meaning and collocation are what this chapter uses."},
    {"id": "visibility-timeout", "add_facts": ["sqs-faq-visibility-timeout-definition"],
     "why": "The bank's fact is a Lambda fact; this is the SQS definition."},
    {"id": "retention-period",
     "add_meaning": "In SQS, how long a queue keeps a message before it deletes the message unread.",
     "add_facts": ["sqs-message-retention-default"],
     "why": "The bank's meaning names S3 Object Lock; subsections 1 and 6 use the SQS meaning ('message retention period')."},
]
BRIEF["terms_note"] = (
    "terms lists only bank terms (B11). Per the orchestrator note, term_requests holds every new term that the chapter defines "
    "in bold, as a ready bank entry (id, term, kind, short, meaning, collocations, do_not_confuse, facts); the terms agent adds "
    "them to data/terms.json right after this brief, appends their ids to terms, and applies term_amendments. Writers then "
    "need no needs-term marker. Respell only bank respellings (STYLE 4): queue (KYOO), decouple, asynchronous, idempotent, and "
    "the requested FY-foh for FIFO queue and FIFO topic. 'EventBridge rule' is the term (the plain word 'rule' is too common "
    "in other chapters: lifecycle rule, listener rule); writers bold 'EventBridge rule' at first use and may write 'rule' "
    "afterwards. 'publish/subscribe' has the id publishsubscribe (the anchor drops the slash).")

BRIEF["tasks"] = [
    {"id": "messaging-t01", "type": "look", "title": "List your queues topics and event buses",
     "section": "1-fast.md#look-first", "kills": "\"An account has no event bus until you create one.\"", "trap": None,
     "pass_route": False, "status": "write",
     "plan": ("In AWS CloudShell, read-only, 3 minutes, $0. (1) aws sqs list-queues: expect the queue URLs of this Region, or "
              "no output. (2) aws sns list-topics: expect the topic ARNs, or an empty list. (3) aws events list-event-buses: "
              "expect at least one bus named default, because every account has a [default event bus] "
              "(eventbridge-default-bus-receives-aws-service-events). Creates nothing. The writer confirms the three operations "
              "and their output fields with tasks check-cli --reference."),
     "facts": ["eventbridge-default-bus-receives-aws-service-events"]},
    {"id": "messaging-t02", "type": "try", "title": "Watch an unprocessed message come back",
     "section": "2-deep.md#" + SID[3], "kills": "\"Receiving a message removes it from the queue.\"",
     "trap": "messaging-trap-receive-deletes", "pass_route": True, "status": "write",
     "plan": ("In AWS CloudShell, about 6 minutes. Steps: aws sqs create-queue --queue-name saa-messaging-t02 --attributes "
              "VisibilityTimeout=10 --tags book=saa,task=messaging-t02 with capture QUEUE_URL (query QueueUrl); aws sqs "
              "send-message --queue-url $QUEUE_URL --message-body job-1; aws sqs receive-message --queue-url $QUEUE_URL "
              "--wait-time-seconds 5: expect the message job-1 (do not delete it). Break it: predict 'If you do not delete the "
              "message, will a later receive get it again?'; aws sqs receive-message --queue-url $QUEUE_URL --wait-time-seconds 20 "
              "--attribute-names ApproximateReceiveCount with capture RECEIPT (query Messages[0].ReceiptHandle): expect job-1 "
              "again, with ApproximateReceiveCount 2, after about 10 seconds; explain: after a receive [it remains in the queue] "
              "(sqs-receive-keeps-message-hidden), and without a delete it [becomes visible again in the queue] "
              "(sqs-undeleted-message-visible-again). Fix: aws sqs delete-message --queue-url $QUEUE_URL --receipt-handle "
              "$RECEIPT; then receive-message --wait-time-seconds 20 returns nothing. Cleanup: aws sqs delete-queue --queue-url "
              "$QUEUE_URL. Verify: aws sqs get-queue-url --queue-name saa-messaging-t02, expect the error "
              "AWS.SimpleQueueService.NonExistentQueue (T108 by-name read; the expect line may say 'can take a short time after "
              "the delete' without a number). Cost line: 'about $0: one queue and fewer than 10 requests' with cost_facts [] "
              "(no dollar amount above 0, T109). If forgotten: an empty queue with no requests costs nothing for requests (plain "
              "words; no price fact). The second receive waits for the visibility timeout through long polling, so no sleep "
              "command is needed. Label 'checked against docs, not run in a real account'. The writer confirms the tag syntax "
              "of create-queue and each operation with tasks check-cli --reference."),
     "facts": ["sqs-receive-keeps-message-hidden", "sqs-undeleted-message-visible-again", "sqs-manual-delete-after-processing",
               "sqs-long-polling-max-wait", "sqs-faq-receipt-handle-required-to-delete"]},
    {"id": "messaging-t03", "type": "try", "title": "Send one message to two queues through a topic",
     "section": "2-deep.md#" + SID[10], "kills": "\"Subscribing a queue to a topic is enough for messages to arrive.\"",
     "trap": "messaging-trap-subscribe-without-queue-policy", "pass_route": False, "status": "write",
     "plan": ("In AWS CloudShell, about 10 minutes. Steps: aws sns create-topic --name saa-messaging-t03 --tags "
              "Key=book,Value=saa Key=task,Value=messaging-t03 with capture TOPIC_ARN (query TopicArn); create two queues "
              "saa-messaging-t03-a and saa-messaging-t03-b with --tags book=saa,task=messaging-t03 and captures QUEUE_A and QUEUE_B; "
              "aws sqs get-queue-attributes --attribute-names QueueArn for each, with captures QUEUE_A_ARN and QUEUE_B_ARN; aws "
              "sns subscribe --protocol sqs --notification-endpoint $QUEUE_A_ARN (and B). Break it: predict 'The queues keep "
              "their default access policies. Will a published message reach them?'; aws sns publish --topic-arn $TOPIC_ARN "
              "--message order-1; aws sqs receive-message --queue-url $QUEUE_A --wait-time-seconds 10: expect no message; "
              "explain: you must [set a policy on the Amazon SQS queue] (sns-sqs-queue-needs-policy-allowing-topic) that allows "
              "the topic. Fix: aws sqs set-queue-attributes for each queue with an inline Policy that allows the service principal "
              "sns.amazonaws.com to call sqs:SendMessage on that queue with the [aws:SourceArn condition] "
              "(sns-queue-policy-sourcearn-limits-to-one-topic) equal to $TOPIC_ARN (inline JSON in the attribute value, no "
              "file://, J5); publish order-2; receive from both queues: expect order-2 in each, inside the SNS JSON envelope. "
              "Cleanup: aws sns delete-topic --topic-arn $TOPIC_ARN; aws sqs delete-queue for both queues. Verify: aws sqs "
              "get-queue-url --queue-name saa-messaging-t03-a, expect the error AWS.SimpleQueueService.NonExistentQueue (T108 "
              "by-name read). Cost line: 'about $0: one topic, two queues and fewer than 20 requests' with cost_facts []. Label "
              "'checked against docs, not run in a real account'. The JSON quoting of the inline policy is the hard part: the "
              "writer confirms it, the tag syntaxes and every operation with tasks check-cli --reference."),
     "facts": ["sns-sqs-queue-needs-policy-allowing-topic", "sns-queue-policy-sourcearn-limits-to-one-topic",
               "sns-publish-sends-message-to-each-subscribed-queue", "sns-faq-same-account-sqs-subscription-needs-no-opt-in",
               "sns-sqs-envelope-contains-subject-message-metadata", "sqs-default-access-policy-owner-only"]},
]

BRIEF["speak"] = [
    {"id": "messaging-s01", "kind": "decide", "persona": "Ben, CTO of Callvale",
     "prompt": "SQS, SNS, EventBridge: all three move messages. When do I use which?",
     "section": "1-fast.md#choose-it-or-not", "pass_route": True,
     "facts": ["lambda-trigger-sqs-sns-eventbridge-model", "sqs-decision-keeps-until-processed", "sns-decision-no-persistence",
               "sns-faq-fanout-identical-messages-to-multiple-sqs-queues", "eventbridge-default-bus-receives-aws-service-events",
               "eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners",
               "eventbridge-quota-targets-per-rule", "sqs-lens-sqs-sns-eventbridge-roles-in-event-driven-design"],
     "note": ("Ben talks in short technical sentences and wants the fewest parts. Short answer: a queue when one consumer does "
              "the work at its own pace; a topic when every subscriber needs a copy now; EventBridge when AWS services or SaaS "
              "apps produce the events and rules pick them by content. How it works: SQS keeps a message until a consumer "
              "deletes it; SNS pushes copies and keeps nothing; an EventBridge rule matches events and sends them to up to five "
              "targets. Watch: SNS and EventBridge keep nothing, so put a queue behind them for any consumer that can be down. "
              "In your case: 'Which of your systems must keep working while another one is down?' Must not say: 'SNS stores "
              "messages until the subscriber is back'; 'one queue gives every service a copy'; 'an event bus keeps events for "
              "replay by default'. Numbers as words from the say forms: five targets.")},
    {"id": "messaging-s02", "kind": "explain", "persona": "a startup CTO you advise",
     "prompt": "Our worker crashed in the middle of a job. Did we lose that message?",
     "section": "2-deep.md#" + SID[3], "pass_route": False,
     "facts": ["sqs-receive-keeps-message-hidden", "sqs-failed-processing-message-not-lost", "sqs-visibility-timeout-default",
               "sqs-dlq-max-receive-count-meaning", "sqs-standard-at-least-once-duplicates",
               "sqs-faq-standard-queue-design-idempotent-consumers"],
     "note": ("Short answer: no, as long as the worker had not deleted it; it comes back when the visibility timeout ends. How "
              "it works: a receive hides the message, a delete removes it; the default timeout is thirty seconds; after several "
              "failed receives a redrive policy moves it to a dead-letter queue. Watch: the restart can process it twice, so the "
              "worker must be idempotent, and the timeout must be longer than the longest job. In your case: 'How long does your "
              "longest job take?' Must not say: 'the message is gone'; 'SQS delivers each message exactly once'; 'the "
              "dead-letter queue retries it for you'. Numbers as words from the say forms: thirty seconds.")},
    {"id": "messaging-s03", "kind": "compare", "persona": "a startup founder in office hours",
     "prompt": "Standard queue or FIFO queue: which should we start with?",
     "section": "2-deep.md#" + SID[5], "pass_route": False,
     "facts": ["sqs-standard-throughput-nearly-unlimited", "sqs-standard-at-least-once-duplicates",
               "sqs-faq-fifo-exactly-once-processing", "sqs-fifo-order-strict-within-group", "sqs-fifo-groups-processed-in-parallel",
               "sqs-cannot-convert-standard-queue-to-fifo"],
     "note": ("First sentence starts 'Both': both keep messages safely; the difference is order and duplicates against "
              "throughput. Short answer: a standard queue, unless order per customer or no duplicates is a hard rule; then a "
              "FIFO queue with the customer ID as message group ID. How it works: a standard queue scales almost without limit "
              "but can repeat a message and change the order; a FIFO queue keeps order inside each group and drops duplicates, "
              "at a lower rate. Watch: you cannot turn a standard queue into a FIFO queue later; the type is chosen at "
              "creation. In your case: 'Does anything break if two events of one customer arrive out of order?' Must not say: "
              "'standard queues keep the order'; 'a FIFO queue keeps one order across all customers'; 'you can switch to FIFO "
              "later'. No numbers (the FIFO rate facts have no spoken form).")},
    {"id": "messaging-s04", "kind": "explain", "persona": "Ana, CEO of Callvale",
     "prompt": "On launch day, uploads failed. What did we change so that it cannot happen again?",
     "section": "2-deep.md#decision-record", "pass_route": False,
     "facts": ["sqs-send-stored-multi-az-before-ack", "sns-faq-sqs-components-need-not-be-available-at-same-time",
               "sqs-scales-transparently-for-spikes", "sqs-message-retention-default", "sqs-dlq-max-receive-count-meaning",
               "sns-publish-sends-message-to-each-subscribed-queue"],
     "note": ("Ana uses no AWS terms: explain a queue the first time as 'a waiting line for work that AWS keeps safe'. Short "
              "answer: an upload now waits safely in line instead of failing when the worker is busy. How it works: each upload "
              "is stored in several data centers before we say 'received'; workers take uploads from the line at their own "
              "pace; a recording that keeps failing is moved aside, so it blocks no one; when a transcript is ready, one message "
              "reaches both the customer webhooks and search. Watch: processing is not instant; customers see 'processing' for a "
              "while, and a message waits at most four days by default. In your case: 'How long may a customer wait for a "
              "transcript before we warn them?' Must not say: 'nothing can fail again'; 'transcripts are ready at once'; 'we "
              "fixed it with more servers'. Numbers as words from the say forms: four days.")},
]


def card(cid, typ, deck, sec, fact, front, back, trap=None):
    return {"id": cid, "type": typ, "deck": deck, "section": sec, "facts": [fact], "trap": trap, "front": front, "back": back}


S2 = lambda n: "2-deep.md#" + SID[n]  # noqa: E731
CHOOSE = "1-fast.md#choose-it-or-not"
BRIEF["cards"] = [
    card("messaging-c001", "number", "core", S2(1), "sqs-message-retention-default",
         "In Amazon SQS, how long does a queue keep a message by default?", "4 days."),
    card("messaging-c002", "number", "core", S2(1), "sqs-message-retention-range",
         "In Amazon SQS, what is the longest message retention period?", "14 days."),
    card("messaging-c003", "number", "core", S2(3), "sqs-visibility-timeout-default",
         "In Amazon SQS, what is the default visibility timeout?", "30 seconds."),
    card("messaging-c004", "number", "core", S2(3), "sqs-visibility-timeout-range",
         "In Amazon SQS, what is the longest visibility timeout?", "12 hours."),
    card("messaging-c005", "number", "core", S2(2), "sqs-long-polling-max-wait",
         "In Amazon SQS, how long can one long-polling call wait?", "20 seconds."),
    card("messaging-c006", "number", "core", CHOOSE, "sqs-delay-queue-range",
         "In Amazon SQS, what is the longest delay of a delay queue?", "15 minutes."),
    card("messaging-c007", "number", "core", S2(5), "sqs-faq-fifo-default-throughput-3000-with-batching-300-without",
         "In Amazon SQS, how many messages per second does a FIFO queue support by default?",
         "300 messages per second, or 3,000 messages per second with batching."),
    card("messaging-c008", "number", "core", S2(12), "eventbridge-quota-targets-per-rule",
         "In Amazon EventBridge, how many targets can one rule have?", "5 targets."),
    card("messaging-c009", "cannot", "core", S2(3), "sqs-receive-keeps-message-hidden",
         "In Amazon SQS, does receiving a message delete it?", "No. It stays in the queue, hidden from other consumers.",
         "messaging-trap-receive-deletes"),
    card("messaging-c010", "decide", "core", S2(10), "sns-faq-fanout-identical-messages-to-multiple-sqs-queues",
         "Several services must each get every message. What do you build?", "An SNS topic with one SQS queue per service.",
         "messaging-trap-queue-broadcasts"),
    card("messaging-c011", "cannot", "core", S2(9), "sns-decision-no-persistence",
         "In Amazon SNS, does a topic keep messages for an offline subscriber?",
         "No. Messages are not persisted; subscribe an SQS queue.", "messaging-trap-topic-stores-messages"),
    card("messaging-c012", "cannot", "core", S2(4), "sqs-standard-at-least-once-duplicates",
         "In Amazon SQS, can a standard queue deliver one message twice?",
         "Yes. Delivery is at least once; make consumers idempotent.", "messaging-trap-standard-exactly-once"),
    card("messaging-c013", "decide", "core", S2(7), "ec2-auto-scaling-sqs-backlog-per-instance-metric-math",
         "Workers poll an SQS queue. Which metric should their Auto Scaling group track?",
         "Backlog per instance: visible messages divided by InService instances.", "auto-scaling-trap-queue-length-metric"),
    card("messaging-c014", "cannot", "core", S2(13), "eventbridge-classic-bus-does-not-retain-events",
         "In Amazon EventBridge, does a Classic event bus keep its events?", "No. To keep events, add an archive.",
         "messaging-trap-bus-stores-events"),
    card("messaging-c015", "differ", "extended", CHOOSE, "sqs-delay-queue-hidden-at-add-visibility-after-receive",
         "In Amazon SQS, what does a delay queue hide, and what does the visibility timeout hide?",
         "Delay: new messages. Visibility timeout: received messages."),
    card("messaging-c016", "cannot", "extended", S2(5), "sqs-cannot-convert-standard-queue-to-fifo",
         "In Amazon SQS, can you convert a standard queue to a FIFO queue?", "No. Create a new FIFO queue."),
    card("messaging-c017", "cannot", "extended", S2(5), "sqs-fifo-no-order-across-groups",
         "In an SQS FIFO queue, do messages of different groups keep their order?",
         "No. They may arrive or be processed out of order.", "messaging-trap-fifo-global-order"),
    card("messaging-c018", "decide", "extended", S2(5), "sqs-fifo-groups-processed-in-parallel",
         "Each customer's events must stay in order, and customers must run in parallel. How?",
         "A FIFO queue with the customer ID as message group ID."),
    card("messaging-c019", "cannot", "extended", S2(5), "sqs-fifo-deduplication-interval-5-minutes",
         "In an SQS FIFO queue, what happens to a duplicate sent within the 5 minute deduplication interval?",
         "Only one copy is delivered."),
    card("messaging-c020", "cannot", "extended", S2(6), "sqs-dlq-type-must-match-source-queue-type",
         "In Amazon SQS, can a FIFO queue use a standard dead-letter queue?",
         "No. Its dead-letter queue must also be a FIFO queue."),
    card("messaging-c021", "cannot", "extended", S2(6), "sqs-dlq-same-account-and-region",
         "In Amazon SQS, can a dead-letter queue be in another Region?",
         "No. Same AWS account and Region as the source queue."),
    card("messaging-c022", "decide", "extended", S2(6), "sqs-dlq-retention-longer-than-source-queue",
         "In Amazon SQS, how long should a dead-letter queue keep messages?",
         "Longer than the retention period of the source queue.", "messaging-trap-dlq-fresh-retention"),
    card("messaging-c023", "decide", "extended", S2(8), "lambda-sqs-partial-batch-response",
         "Lambda reads an SQS queue. How do you retry only the failed messages of a batch?",
         "Return a partial batch response with ReportBatchItemFailures.", "messaging-trap-lambda-retries-failed-only"),
    card("messaging-c024", "decide", "extended", S2(8), "lambda-sqs-visibility-six-times-timeout",
         "Lambda reads an SQS queue. How long should the queue's visibility timeout be?",
         "At least six times the function timeout."),
    card("messaging-c025", "decide", "extended", S2(10), "sns-sqs-queue-needs-policy-allowing-topic",
         "An SNS topic delivers nothing to a subscribed SQS queue. What is missing?",
         "A queue policy that allows the topic to send messages.", "messaging-trap-subscribe-without-queue-policy"),
    card("messaging-c026", "decide", "extended", S2(11), "sns-filter-default-every-message",
         "One subscriber needs only some of a topic's messages. What do you add?", "A filter policy on that subscription.",
         "messaging-trap-filter-needs-function"),
    card("messaging-c027", "differ", "extended", S2(13), "sns-dlq-attached-to-subscription-not-topic",
         "In Amazon SNS, where do you attach a dead-letter queue?", "To a subscription, not to the topic.",
         "messaging-trap-dlq-on-topic"),
    card("messaging-c028", "cannot", "extended", S2(14), "sqs-cross-account-needs-queue-access-policy",
         "A role in another account has an IAM policy for sqs:SendMessage. Is that enough?",
         "No. The queue's access policy must also allow it.", "messaging-trap-iam-policy-enough-cross-account"),
    card("messaging-c029", "cannot", "extended", S2(14), "sqs-kms-aws-managed-key-policy-not-modifiable",
         "In Amazon SQS, can you edit the key policy of the AWS managed key?", "No. You cannot modify that key policy.",
         "kms-trap-aws-managed-key-controllable"),
    card("messaging-c030", "differ", "extended", S2(2), "sqs-faq-long-polling-waits-for-message",
         "In Amazon SQS, what is the difference between short polling and long polling?",
         "Short returns at once; long waits until a message arrives."),
    card("messaging-c031", "decide", "extended", S2(12), "sqs-eventbridge-scheduler-for-advanced-scheduling",
         "A task must run once, three days from now. Which service schedules it?",
         "EventBridge Scheduler, with a one-time schedule."),
    card("messaging-c032", "decide", "extended", S2(12), "eventbridge-default-bus-receives-aws-service-events",
         "React to an EC2 state change without polling. What do you use?", "An EventBridge rule on the default event bus."),
]
BRIEF["card_plan"] = {
    "core": 14, "extended": 18, "number_cards_equal_a_list_rows": 8,
    "rule": ("Fronts and backs above are drafts for the card writer: one fact per card, an answer of at most 12 words, a display "
             "of the card fact for any number with a unit (4 days, 14 days, 30 seconds, 12 hours, 20 seconds, 15 minutes, 300 "
             "messages per second, 3,000 messages per second with batching, 5, 5 minute deduplication interval are the "
             "displays; c005's back may be 'Up to 20 seconds.' only if 'up to' is supported: write '20 seconds.'), and the "
             "context named at the start of the front. No front holds a number with a unit that is not a display of a card "
             "fact. No absolute word without a fact of the card that supports it: c019 ('Only one copy is delivered') rests on "
             "sqs-fifo-deduplication-interval-5-minutes; c024 ('At least six times') on lambda-sqs-visibility-six-times-timeout; "
             "c028 ('must') on sqs-cross-account-needs-queue-access-policy; c029 ('cannot') on "
             "sqs-kms-aws-managed-key-policy-not-modifiable. c031's front has 'three days' as a scenario value in words; keep it "
             "a word."),
}

BRIEF["diagrams"] = [
    {"id": "messaging-hero", "kind": "sequence",
     "placement": ("1-fast.md#in-one-breath (behind 'Predict the picture. When a producer sends a message to a queue, where "
                   "does the message wait, and when does it leave the queue?')"),
     "title": "One message through a queue",
     "claim": "A message waits in the queue, hidden while one consumer works on it, until that consumer deletes it.",
     "alt": ("A sequence with three participants: a producer, an SQS queue and a consumer. The producer sends a message, and "
             "the queue confirms it. The consumer receives the message, which stays in the queue but hidden. The consumer "
             "deletes it. A second path shows a message that is not deleted becoming visible again."),
     "say": [
         "The producer sends a message, and SQS stores the message in multiple availability zones before it confirms.",
         "A consumer polls the queue and receives the message.",
         "After the receive, it remains in the queue but is temporarily invisible to other consumers.",
         "The consumer processes the message and deletes it using the DeleteMessage action.",
         "If the consumer does not delete it in time, the message becomes visible again in the queue.",
     ],
     "facts_for_steps": ["sqs-send-stored-multi-az-before-ack", "sqs-receive-keeps-message-hidden",
                         "sqs-manual-delete-after-processing", "sqs-undeleted-message-visible-again"],
     "note": ("Size s. Participants: Producer (users or a generic app icon, label 'Producer'), Queue (sqs icon, label 'SQS "
              "queue'), Consumer (label 'Consumer'). Messages: 1 producer to queue 'send'; 2 queue to producer, dashed, "
              "'stored'; 3 consumer to queue 'receive'; 4 queue to consumer, dashed, 'message (hidden)'; 5 consumer to queue "
              "'delete'; 6 alternative path: queue aside 'timeout ends: visible again'. Labels at most 4 words, no digits. "
              "Markdown step links: 1 [stores the message in multiple availability zones] (sqs-send-stored-multi-az-before-ack); "
              "3 [it remains in the queue] and [temporarily invisible to other consumers] (sqs-receive-keeps-message-hidden); 4 "
              "[using the DeleteMessage action] (sqs-manual-delete-after-processing); 5 [becomes visible again in the queue] "
              "(sqs-undeleted-message-visible-again); step 2 states no AWS rule. If a step changes to fit its link, change say "
              "here and in the spec together (L703). The caption equals the claim; it holds no number and no absolute word.")},
    {"id": "messaging-fanout", "kind": "arch",
     "placement": "2-deep.md#" + SID[10] + " (after the trace)",
     "title": "Fan-out from one topic to two queues",
     "claim": "An SNS topic sends a copy of each message to every subscribed queue, and each queue keeps its copy for its own consumer.",
     "alt": ("A publisher on the left sends to one SNS topic. Arrows go from the topic to two SQS queues; the arrow to the "
             "second queue carries a filter policy label. Each queue has its own consumer on the right, and a dead-letter "
             "queue sits under each queue."),
     "say": [
         "The publisher sends one message to the topic.",
         "SNS sends the message to each subscribed queue.",
         "A subscription with a filter policy gets a message only when the message attributes satisfy the conditions specified in the filter policy.",
         "Each consumer polls its own queue, where the messages persist in an Amazon SQS queue until it reads them.",
     ],
     "facts_for_steps": ["sns-publish-sends-message-to-each-subscribed-queue", "sns-filter-nonmatching-message-not-sent",
                         "sns-sqs-together-instant-notice-and-later-processing"],
     "note": ("Size m, at most 10 nodes: 'Publisher', 'SNS topic' (sns icon), 'Queue A' and 'Queue B' (sqs icon), 'Consumer A', "
              "'Consumer B', 'DLQ A', 'DLQ B'. Edge label on the topic-to-queue-B edge: 'filter policy'. Labels at most 4 words. "
              "Step links: 2 [sends the message to each subscribed queue] (sns-publish-sends-message-to-each-subscribed-queue); 3 "
              "[satisfy the conditions specified in the filter policy] (sns-filter-nonmatching-message-not-sent), which carries "
              "the absolute word 'only'; 4 [persist in an Amazon SQS queue] (sns-sqs-together-instant-notice-and-later-processing). "
              "Step 4 reads awkwardly by design so that the display stands whole: a writer may change it to 'Each consumer "
              "polls its own queue; the messages persist in an Amazon SQS queue until it reads them.' and must then change say "
              "here and in the spec together. Generic names, not Callvale's (this is the How-it-works picture).")},
    {"id": "messaging-eventbridge-routing", "kind": "arch",
     "placement": "2-deep.md#" + SID[12] + " (after the trace)",
     "title": "Event buses, rules and targets",
     "claim": "Events from AWS services, your applications and SaaS partners land on event buses, and rules send matching events to their targets.",
     "alt": ("Three sources on the left: an AWS service, an application and a SaaS partner. The AWS service and the application "
             "send to the default event bus and a custom event bus; the SaaS partner sends to a partner event bus. Each bus has "
             "rules, and each rule points to targets such as a Lambda function, an SQS queue and an SNS topic."),
     "say": [
         "When an AWS service sends an event, it goes to your account's default event bus.",
         "Your applications can send custom events, and SaaS partners send events to partner event buses.",
         "Each rule matches incoming events for a given event bus.",
         "A matching event goes to every target of the rule, processed in parallel.",
         "If an event matches no rule, EventBridge takes no action.",
     ],
     "facts_for_steps": ["eventbridge-aws-service-events-go-to-default-bus", "eventbridge-partner-bus-receives-saas-events",
                         "eventbridge-faq-rule-matches-events-on-a-bus-and-routes-to-targets",
                         "eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel",
                         "eventbridge-event-can-match-several-rules-or-none"],
     "note": ("Size m, at most 12 nodes: 'AWS service', 'Your app', 'SaaS partner', 'Default bus', 'Custom bus', 'Partner "
              "bus' (eventbridge icon), 'Rule' nodes as small boxes, targets 'Lambda function', 'SQS queue', 'SNS topic'. Labels "
              "at most 4 words, no digits (do not draw five targets). Step links: 1 [it goes to your account's default event "
              "bus] (eventbridge-aws-service-events-go-to-default-bus); 2 [partner event buses] "
              "(eventbridge-partner-bus-receives-saas-events); 3 [matches incoming events for a given event bus] "
              "(eventbridge-faq-rule-matches-events-on-a-bus-and-routes-to-targets); 4 [processed in parallel] "
              "(eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel); 5 [EventBridge takes no action] "
              "(eventbridge-event-can-match-several-rules-or-none). Keep spec say and Markdown steps equal (L703).")},
    {"id": "messaging-before", "kind": "arch",
     "placement": "2-deep.md#decision-record (after Context)",
     "title": "Callvale before: the upload waits for the worker",
     "claim": "The web application calls the one worker and waits, so when the worker is busy, the upload fails.",
     "alt": ("Before: customers upload recordings to the web tier. The web application calls the single worker directly and "
             "waits. Scheduled jobs on the same worker save results and send notifications. Job status is in the PostgreSQL "
             "database."),
     "say": [
         "A customer uploads a recording to the web application.",
         "The web application calls the worker and waits for it to finish.",
         "Scheduled jobs on the same worker save results and send notifications.",
         "When the worker is overloaded, the upload request fails.",
     ],
     "facts_for_steps": [],
     "note": ("Story picture (pipeline state P1 of STARTUP.md B1, shared with chapter 18; this chapter highlights the direct "
              "call). Steps are story, not AWS rules: no fact link, no number, no absolute word. At most 8 nodes: 'Customers', "
              "'Web tier' (ALB and instances as one group), 'Worker' (ec2 icon, emph: the bottleneck), 'Scheduled jobs' (inside "
              "or next to the worker), 'PostgreSQL' (rds icon), 'Uploads' (S3 icon). Flow left to right (A7 rule 13). Keep spec "
              "say and Markdown steps equal (L703).")},
    {"id": "messaging-after", "kind": "arch",
     "placement": "2-deep.md#decision-record (after Decision)",
     "title": "Callvale after: queues between the steps and a topic for results",
     "claim": "Uploads wait in queues between the steps, and the transcript-ready topic sends each finished transcript to two queues.",
     "alt": ("After: an upload to Amazon S3 sends an event to the uploads queue. The start-job function reads it and sends work "
             "to the convert queue. Conversion workers in an Auto Scaling group read the convert queue. The save-results "
             "function publishes to the transcript-ready topic, which sends a copy to the webhooks queue and the indexing "
             "queue. Each queue has a dead-letter queue."),
     "say": [
         "An upload to Amazon S3 sends an event to the uploads queue.",
         "The start-job function reads the uploads queue and sends conversion work to the convert queue.",
         "Conversion workers scale on the convert backlog and process each message.",
         "The save-results function publishes to the transcript-ready topic, which sends the message to each subscribed queue.",
         "A consumer can receive a message a set number of times before it is moved to a dead-letter queue.",
     ],
     "facts_for_steps": ["sns-publish-sends-message-to-each-subscribed-queue", "sqs-dlq-max-receive-count-meaning"],
     "note": ("Pipeline state P2 (shared with chapter 18; this chapter highlights the queues and the topic). At most 12 nodes: "
              "'Uploads' (S3), 'uploads' queue, 'start-job' (Lambda function icon), 'convert' queue, 'Conversion workers' "
              "(Auto Scaling group), 'Transcribe and Comprehend' (one group, functions), 'save-results' (Lambda function icon), "
              "'transcript-ready' (sns), 'webhooks' queue, 'indexing' queue, DLQ marks under the queues as small nodes or a "
              "legend. Same cells as messaging-before where possible (A7 rule 13). No numbers in labels (40 workers is "
              "prose only). Step links: 4 [sends the message to each subscribed queue] "
              "(sns-publish-sends-message-to-each-subscribed-queue); 5 [before it is moved to a dead-letter queue] "
              "(sqs-dlq-max-receive-count-meaning); steps 1 to 3 are story. Keep spec say and Markdown steps equal (L703).")},
]

BRIEF["fact_requests"] = []

BRIEF["notes_for_orchestrator"] = [
    ("Only verified facts are named: chapter-31 sqs-, sns- and eventbridge- facts from fact-cards.md (550 verified, "
     "2026-10-14), plus verified facts of chapters 18 (lambda-), 17 (ec2-auto-scaling-), 19 (ecs-) and 21 (s3-). "
     "build_brief.py checked every fact id and every display-and-id pair against data/facts/*.jsonl before stage end; the "
     "generator and its six data parts stay in _build/work/31-messaging/ (brief_part_a.py to brief_part_f.py)."),
    ("Terms (orchestrator note): term_requests holds 33 complete bank entries for every new term the chapter defines in "
     "bold, plus 5 term_amendments (queue, topic, dead-letter-queue, visibility-timeout, retention-period). The terms agent "
     "adds them to data/terms.json and appends their ids to brief.json terms, so that no writer needs a needs-term marker. "
     "The words table (8 rows) uses three of them (message-group-id, fan-out, event-bus). Check two ids: publishsubscribe "
     "(the anchor of 'publish/subscribe') and eventbridge-rule (term 'EventBridge rule')."),
    ("Traps: 13 (the U5 cap): 5 in the fast list, 8 as Exam trap callouts in 2-deep.md. 2-deep.md callouts: 8 Exam trap + 2 "
     "Try it + 1 Startup example = 11 of 12. Subsections without an Exam trap: 1, 2, 4, 7, 9, 12 (3 and 14 carry the two "
     "Spot the bug prompts). 16 of 22 slots are built on a trap; all 13 trap ids are cited by a slot."),
    ("Twin pairs: three strict pairs (q01/q07 queue or fan-out, q02/q09 visibility timeout or dead-letter queue, q13/q18 "
     "EventBridge or SNS), so that the chapter still ships two whole pairs after one rejection. Each pair has identical "
     "options and qualifiers and turns on stable facts."),
    ("Changed recently: three examinable fast entries with changed records (2025-08-04 SQS message size, 2026-01-29 "
     "EventBridge event size, 2023-11-27 FIFO dead-letter queue redrive) and one not-examinable entry under the B-list "
     "(2026-09-18 SNS 1 MiB opt-in). Not in the book: the new EventBridge 'Custom Event Bus' of 2026-09-24 (after the cut-off; "
     "its fact has no changed record, and the book teaches the Classic bus with rules and targets, which AWS keeps)."),
    ("STARTUP difference to report (A7 rule 6): data/startup.json sets dead_letter_after_receives = 3 for Callvale's queues, "
     "but the uploads queue is read by the start-job Lambda function (chapter 18), and AWS recommends a maxReceiveCount of "
     "[at least 5] (lambda-sqs-dlq-maxreceivecount-5) for a Lambda event source. This brief attaches the 3 only to the convert "
     "queue (read by EC2 workers) and leaves the uploads queue's count unnamed. Proposed story fix: 'convert: 3 receives; "
     "uploads: 5 receives' in data/startup.json (chapter 18 should agree)."),
    ("Story numbers: the Spot the bug prompt of subsection 3 uses Callvale's conversion times (90 seconds on average, up to "
     "25 minutes; fact sheet A4), which are not in the uses_numbers of chapter 31; W903 checks only Startup example callouts "
     "and the Decision record, so the prompt passes. If the orchestrator prefers, add conversion_seconds_average and "
     "conversion_minutes_longest to uses_numbers of chapter 31."),
    ("Real world: not written. The three verified case facts (Hanwha Qcells, Legendary Play, Migros One) give no year, and "
     "the first paragraph needs '**Company, year.**'. No fact request filed (an open request blocks the counts gate)."),
    ("Neighbour facts that are NOT verified and are not named here (they need votes outside chapter 31): "
     "s3-event-notification-must-grant-s3-permission-to-destination, s3-event-notification-destination-types, "
     "s3-event-notification-sns-destination-standard-only, s3-event-notification-sqs-fifo-via-eventbridge, "
     "s3-event-notification-sqs-message-size-recommendation, s3-eventbridge-destination-enable-per-bucket-all-events, "
     "s3-eventbridge-enable-takes-about-five-minutes, s3-event-notification-destination-same-region-as-bucket, "
     "mq-welcome-migrate-without-rewriting-messaging-code, step-functions-decision-workflows-category, "
     "kinesis-data-streams-decision-streaming-category, kinesis-data-streams-multiple-independent-consumer-applications. The "
     "brief uses the verified sqs- and sns- equivalents (sqs-vs-mq-new-apps-vs-broker-migration, "
     "sqs-faq-kinesis-streams-realtime-and-replay, sns-faq-fifo-vs-kinesis-fanout-100-vs-5)."),
    ("Kept conflict: sqs-faq-sse-producer-needs-generatedatakey-and-decrypt against "
     "sqs-change-sendmessage-needs-only-generatedatakey-2024 (register-31, adjudicate-31). The book says 'grant producers both "
     "permissions', which works under either reading; no Changed recently entry (no changed record)."),
    ("Volatile facts: 56 chapter-31 facts are volatile (prices, the message-size changes, FIFO high throughput quotas, SNS "
     "FIFO throughput, PutEvents limits); question_plan lists them. Prose, cards and Changed recently may link them where a "
     "plan names them; every key rests on the stable key_facts of its slot."),
    ("Displays to copy exactly (F2): sns-push-mechanism-no-polling 'removes the need to check or “poll”' (curly quotes); "
     "eventbridge-classic-bus-does-not-retain-events 'Not retained. To keep events, add an archive.' (two sentences, in the "
     "fast Truth line and the subsection 13 Go deeper); sqs-send-stored-multi-az-before-ack 'stores the message in multiple "
     "availability zones' (lowercase a and z, AWS's text); ecs-sqs-scale-on-backlog-per-task has asterisks in its display "
     "and is not planned in prose."),
    ("Section count for stage end: 9 sections of 1-fast.md + the How it works H2 + 14 subsections + Numbers + Decision "
     "record + FAQ = 27 brief sections; the skipped real-world box is not a brief section."),
]
