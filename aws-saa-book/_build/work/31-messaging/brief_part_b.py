# brief-31, part B: How-it-works subsections 1 to 7 (the queue).


def sub(heading, minutes, words, bullets, facts, plan, route=None):
    d = {"file": "2-deep.md", "section": anchor(heading), "heading": heading, "bullets": bullets, "facts": facts,
         "status": "write", "minutes": minutes, "words_all_in": words}
    if route:
        d["route"] = route
    d["plan"] = plan
    BRIEF["sections"].append(d)


# 1 ---------------------------------------------------------------------------------------------
sub("SQS stores each message in several Availability Zones before the sender moves on", 3, 210,
    ["3.2.S1", "2.1.S3", "2.1.K2", "2.1.K11"],
    ["sqs-faq-storage-multi-az-region", "sqs-faq-no-admin-overhead", "sqs-faq-scale-without-configuration",
     "sqs-wa-queue-or-stream-lets-you-burst-to-higher-throttle-rates", "sqs-wa-back-pressure-slow-down-or-stop-incoming-data",
     "sqs-wa-queues-in-hard-real-time-systems-stale-requests", "sqs-extended-client-sync-only", "sqs-message-attributes-max"],
    {
        "problem": ("A direct call makes the caller wait for the slowest part, and a failure on either side loses the request. "
                    "A queue lets the sender finish before the receiver even starts."),
        "trace": [
            "**Send and move on.** The producer sends a message, and SQS [stores the message in multiple availability zones] (sqs-send-stored-multi-az-before-ack) before it acknowledges it, so [no single computer, network, or AZ failure] (sqs-send-stored-multi-az-before-ack) makes the message inaccessible.",
            "**Wait in the queue.** Producer and consumer exchange messages [without requiring each component to be concurrently available] (sns-faq-sqs-components-need-not-be-available-at-same-time); the number of messages a queue can store [is unlimited] (sqs-queue-backlog-unlimited).",
            "**Absorb the spike.** SQS keeps [scaling transparently to handle any load increases] (sqs-scales-transparently-for-spikes) [without any provisioning instructions] (sqs-scales-transparently-for-spikes), so a burst makes the queue longer instead of failing requests.",
            "**Expire if nobody processes it.** A queue keeps a message [4 days] (sqs-message-retention-default) by default; you can set [60 seconds] (sqs-message-retention-range) to [14 days] (sqs-message-retention-range). SQS [automatically deletes messages] (sqs-auto-deletes-after-retention-period) older than the [maximum message retention period] (sqs-auto-deletes-after-retention-period).",
        ],
        "table": ("Direct call or queue (columns: Question | Direct call | Through a queue): Receiver is down | the request fails | "
                  "the message waits [until successfully processed or expired] (sqs-decision-keeps-until-processed); Traffic "
                  "spike | the receiver is overloaded | the queue grows and consumers keep their pace: [fine-grained control over "
                  "message processing rates] (sqs-decision-pull-model); What the caller gets back | the result | [an "
                  "acknowledgment that a request has been registered] (sqs-wa-make-component-interactions-asynchronous). One "
                  "link per fact per cell; cells at most 15 words."),
        "why": ("Why does AWS work this way? Well-Architected asks for components that do not call each other directly but meet "
                "[through an intermediate durable storage layer]: write the link as [an intermediate durable storage layer] "
                "(sqs-wa-loose-coupling-via-intermediate-durable-layer), [such as an Amazon SQS queue] "
                "(sqs-wa-loose-coupling-via-intermediate-durable-layer). The durable middle lets each side fail or slow down "
                "alone."),
        "exam_signal": ("\"the database cannot keep up during peaks\" or \"decouple the tiers\" points to an SQS queue between "
                        "the tiers; [buffering requests] (sqs-decision-typical-use) is a typical use."),
        "exam_trap": None,
        "body_extras": ("Only if words remain, one sentence: a message is at most [1 MiB] (sqs-message-size-range) (volatile: "
                        "changed 2025-08-04, see Changed recently; never a question key), and the Extended Client Library "
                        "keeps a larger payload in Amazon S3, up to [2 GB] (sqs-extended-client-max-payload). Reference only, no "
                        "sentence: up to [10 metadata attributes] (sqs-message-attributes-max); the library [works only for "
                        "synchronous clients] (sqs-extended-client-sync-only); in hard real-time systems old requests [should be "
                        "considered stale] (sqs-wa-queues-in-hard-real-time-systems-stale-requests)."),
        "say_it": "The short answer is: the queue holds the message, so the sender does not wait. The thing to watch is the retention period.",
        "stop_and_answer": ("A bad release stops all consumers for six days. The queue keeps its default settings. Are the "
                            "messages from the first day still in the queue when the consumers return? Answer: no; the default "
                            "retention is [4 days] (sqs-message-retention-default), and SQS [automatically deletes messages] "
                            "(sqs-auto-deletes-after-retention-period) older than that; a retention of up to [14 days] "
                            "(sqs-message-retention-range) would have kept them. 'six days' is the prompt's example value; the "
                            "reveal does not repeat it."),
    })

# 2 ---------------------------------------------------------------------------------------------
sub("Consumers poll the queue and long polling waits for messages to arrive", 3, 205, ["2.1.K11", "3.2.K3"],
    ["sqs-faq-sdk-default-20-second-long-poll", "sqs-long-polling-http-timeout-longer-than-wait",
     "sqs-faq-long-poll-timeout-min-1-second", "sqs-batch-up-to-10-messages-cost", "sqs-faq-batch-operations-cost-same-as-other-requests"],
    {
        "problem": "SQS does not push a message to anyone: consumers ask for messages. How they ask decides the cost and how soon they see a message.",
        "trace": [
            "**Pull.** SQS uses a [Pull-based model] (sqs-decision-pull-model): consumers poll the queue.",
            "**Short polling answers at once.** [Short polling (default)] (sqs-short-polling-is-default-immediate-response) [samples a subset of its servers] (sqs-short-polling-samples-subset-of-servers) and answers [even if no messages are found] (sqs-short-polling-is-default-immediate-response), so one call [might not return all of your messages] (sqs-short-polling-request-may-miss-messages).",
            "**Long polling waits.** With a wait time [greater than 0, long polling is in effect] (sqs-long-polling-wait-greater-than-zero): the call [queries all servers for messages] (sqs-long-polling-queries-all-servers) and waits up to [20 seconds] (sqs-long-polling-max-wait) for one to arrive.",
            "**Fewer empty answers.** Long polling lowers cost by [reducing the number of empty responses] (sqs-long-polling-reduces-empty-and-false-empty) and of [false empty responses] (sqs-long-polling-reduces-empty-and-false-empty).",
            "**Take several at once.** One ReceiveMessage call [can process 10 messages at a time] (sqs-no-receive-message-batch-action).",
        ],
        "table": ("Short or long polling (columns: Question | Short polling | Long polling): Which servers it asks | a subset | "
                  "all of them; Empty queue | it [returns immediately] (sqs-faq-long-polling-waits-for-message) | it waits "
                  "[until a message arrives in the message queue] (sqs-faq-long-polling-waits-for-message) or the wait ends; "
                  "Price of one call | the same: long polls are [billed exactly the same] "
                  "(sqs-faq-long-polling-no-extra-charge)."),
        "why": ("Why does AWS work this way? Asking a few servers is fast but can miss a message on the others; waiting lets SQS "
                "look on every server at no extra price per call."),
        "exam_signal": ("\"reduce the number of empty receives\" or \"lower the cost of polling\" points to long polling, which "
                        "can [reduce the number of empty receives] (sqs-faq-long-polling-fewer-empty-receives-lower-cost)."),
        "exam_trap": None,
        "body_extras": ("Only if words remain, one sentence: [long polling is preferable to short polling] "
                        "(sqs-faq-long-polling-preferable-almost-all-cases) in [almost all cases] "
                        "(sqs-faq-long-polling-preferable-almost-all-cases); the console default of [0 seconds] "
                        "(sqs-console-receive-wait-time-default) [sets short polling] (sqs-console-receive-wait-time-default). "
                        "Reference only, no sentence: [All AWS SDKs] (sqs-faq-sdk-default-20-second-long-poll) use [20-second "
                        "long polls] (sqs-faq-sdk-default-20-second-long-poll); the HTTP timeout must be [longer than the "
                        "WaitTimeSeconds parameter] (sqs-long-polling-http-timeout-longer-than-wait); batch actions handle [up "
                        "to 10 messages at a time] (sqs-batch-up-to-10-messages-cost) and [cost the same as other Amazon SQS "
                        "requests] (sqs-faq-batch-operations-cost-same-as-other-requests)."),
        "say_it": "The short answer is: use long polling, it waits for a message. The thing to watch is the client's HTTP timeout.",
        "stop_and_answer": ("A consumer calls ReceiveMessage in a tight loop on a queue that is often empty, and the bill shows "
                            "millions of empty receives. Which queue setting lowers that, and does each call then cost more? "
                            "Answer: set the receive message wait time above zero: [Any non-zero value sets long polling] "
                            "(sqs-console-receive-wait-time-default). Each long poll is [billed exactly the same] "
                            "(sqs-faq-long-polling-no-extra-charge) as a short poll, and there are far fewer of them."),
    })

# 3 ---------------------------------------------------------------------------------------------
sub("A received message stays hidden until it is deleted or the timeout ends", 4, 225, ["2.1.K11", "3.2.K3", "3.2.S1"],
    ["sqs-faq-visibility-timeout-definition", "sqs-locks-messages-multiple-producers-consumers",
     "sqs-faq-receive-then-delete-acknowledges-processing", "sqs-faq-delete-already-deleted-returns-success"],
    {
        "problem": ("Receiving a message does not remove it. SQS must keep other consumers away while one consumer works, and "
                    "bring the message back if that consumer fails."),
        "trace": [
            "**Receive.** After a receive, [it remains in the queue] (sqs-receive-keeps-message-hidden) but is [temporarily invisible to other consumers] (sqs-receive-keeps-message-hidden).",
            "**Hide for the visibility timeout.** The timeout is [30 seconds] (sqs-visibility-timeout-default) by default; you can set it from [0 seconds] (sqs-visibility-timeout-range) to [12 hours] (sqs-visibility-timeout-range).",
            "**Delete when done.** The consumer deletes the message with the [receipt handle] (sqs-faq-receipt-handle-required-to-delete) of the receive, which you [must provide when deleting the message] (sqs-faq-receipt-handle-required-to-delete): [You explicitly delete messages] (sqs-manual-delete-after-processing).",
            "**Come back on failure.** Without a delete, the message [becomes visible again in the queue] (sqs-undeleted-message-visible-again) and can be [retrieved by another consumer] (sqs-undeleted-message-visible-again), so messages [aren't lost even if the initial processing fails] (sqs-failed-processing-message-not-lost).",
            "**Extend long work.** The [ChangeMessageVisibility action] (sqs-change-message-visibility-extend-shorten) can [extend or shorten the timeout as needed] (sqs-change-message-visibility-extend-shorten) for one message.",
        ],
        "table": ("Visibility timeout compared with the processing time (columns: Timeout | What happens): shorter than the "
                  "processing | [a duplicate message is received by another consumer] "
                  "(sqs-visibility-timeout-too-short-gives-duplicate); a little longer | one consumer finishes, and a failed "
                  "message returns soon; far longer | after a failure you [wait for a relatively long time] "
                  "(sqs-visibility-timeout-too-long-delays-retry). Truth table: one row per case, the result in the last "
                  "column."),
        "why": ("Why does AWS work this way? SQS cannot tell a crashed consumer from a slow one. A timer is the only signal it "
                "has, so the timer must fit the work."),
        "exam_signal": ("\"some messages are processed twice\" together with long processing points to a visibility timeout "
                        "that ends while the [original consumer is still working on the message] "
                        "(sqs-visibility-timeout-too-short-gives-duplicate)."),
        "exam_trap": "messaging-trap-short-visibility-safer",
        "exam_trap_text": ("> **Exam trap:** A short visibility timeout is not the safe choice. If it ends while the consumer "
                           "still works, [a duplicate message is received by another consumer] "
                           "(sqs-visibility-timeout-too-short-gives-duplicate). <!-- trap: messaging-trap-short-visibility-safer -->"),
        "go_deeper": ("Go deeper: the 12-hour ceiling. Extending the timeout [does not reset the 12 hour maximum] "
                      "(sqs-visibility-timeout-extend-no-reset), which counts from the receive. Set the timeout [longer than the "
                      "AWS SDK read timeout] (sqs-visibility-timeout-longer-than-sdk-read-timeout). Contrast: a delay queue hides "
                      "a message [hidden when it is first added to queue] (sqs-delay-queue-hidden-at-add-visibility-after-receive), "
                      "the visibility timeout [only after it is consumed from the queue] "
                      "(sqs-delay-queue-hidden-at-add-visibility-after-receive). At most 60 words."),
        "try_it": "messaging-t02: one sentence ('Watch a message that you do not delete come back.'), then See [3-do.md](3-do.md). <!-- task: messaging-t02 -->",
        "spot_the_bug": ("Spot the bug (example block, story values allowed): 'Callvale's convert queue keeps the default visibility "
                         "timeout. A conversion takes 90 seconds on average and up to 25 minutes. Support sees some recordings "
                         "converted twice. What is wrong?' Reveal: the default [30 seconds] (sqs-visibility-timeout-default) ends "
                         "long before a conversion finishes, so [a duplicate message is received by another consumer] "
                         "(sqs-visibility-timeout-too-short-gives-duplicate); set the timeout above the longest conversion, or "
                         "let the worker extend it with the [ChangeMessageVisibility action] "
                         "(sqs-change-message-visibility-extend-shorten). The reveal does not repeat the minutes."),
        "say_it": "The short answer is: receiving hides a message, deleting removes it. The thing to watch is a timeout shorter than the work.",
        "stop_and_answer": ("A consumer receives a message, and its instance is terminated before it calls DeleteMessage. When "
                            "can another consumer get that message? Answer: when the visibility timeout of that receive ends; "
                            "the message then [becomes visible again in the queue] (sqs-undeleted-message-visible-again). Do not "
                            "write example minutes in the reveal."),
    }, route="pass")

# 4 ---------------------------------------------------------------------------------------------
sub("A standard queue can deliver a message twice so consumers must be idempotent", 3, 195, ["2.1.K11", "2.1.S1", "3.2.S1"],
    ["sqs-faq-standard-at-least-once-delivery", "sqs-faq-standard-loose-fifo-order-not-guaranteed",
     "sqs-wa-idempotency-token-lets-client-retry", "sqs-faq-deleted-message-standard-may-repeat-fifo-never"],
    {
        "problem": ("A standard queue scales by keeping copies of each message on several servers. The price is that a copy can "
                    "come back."),
        "trace": [
            "**Keep copies.** If a server that holds a copy is down at delete time, the copy [isn't deleted on the server that is unavailable] (sqs-copies-on-multiple-servers-cause-duplicates), and [you might get that message copy again] (sqs-copies-on-multiple-servers-cause-duplicates).",
            "**Deliver at least once.** A standard queue gives [at-least-once message delivery] (sqs-standard-at-least-once-duplicates): [more than one copy of a message] (sqs-standard-at-least-once-duplicates) can arrive, and [messages may occasionally arrive out of order] (sqs-standard-at-least-once-duplicates).",
            "**Try to keep order.** It makes a [best-effort attempt to maintain the order] (sqs-standard-best-effort-ordering), nothing more.",
            "**Scale almost without limit.** In return it supports a [nearly unlimited number of API calls per second] (sqs-standard-throughput-nearly-unlimited).",
            "**Make the consumer idempotent.** [Design your applications to be idempotent] (sqs-copies-on-multiple-servers-cause-duplicates): consumers [keep track of each token received] (sqs-consumers-keep-idempotency-tokens-ignore-duplicates) and skip a token they have seen.",
        ],
        "table": ("What a duplicate does (columns: Consumer action | Not idempotent | Idempotent): set status to done | same "
                  "result | same result; add a credit to a balance | the balance is wrong | it skips a message ID it already "
                  "processed; send an email | the customer gets two | it checks a record of sent messages. Plain words, no "
                  "links (example rows)."),
        "why": ("Why does AWS work this way? Copies on several servers keep the queue available and fast. An idempotent service "
                "makes [multiple identical requests has the same effect] (sqs-idempotent-service-same-effect-as-single-request) "
                "[as making a single request] (sqs-idempotent-service-same-effect-as-single-request): write it as one sentence "
                "that reads naturally around the two links, or link only the second display."),
        "exam_signal": ("\"nearly unlimited throughput\" and \"order does not matter\" point to a standard queue with idempotent "
                        "consumers; it supports a [nearly unlimited number of API calls per second] "
                        "(sqs-standard-throughput-nearly-unlimited)."),
        "exam_trap": None,
        "say_it": "The short answer is: a standard queue may repeat a message. The thing to watch is code that charges twice.",
        "stop_and_answer": ("A consumer adds a credit to a customer account for each message. One message produced two credits. "
                            "Is the queue broken? Answer: no; a standard queue gives [at-least-once message delivery] "
                            "(sqs-standard-at-least-once-duplicates). The consumer must record each message's ID and skip IDs "
                            "it has seen: consumers [keep track of each token received] "
                            "(sqs-consumers-keep-idempotency-tokens-ignore-duplicates)."),
    })

# 5 ---------------------------------------------------------------------------------------------
sub("A FIFO queue keeps order inside each message group and drops duplicates", 4, 220, ["2.1.K11", "3.2.K3", "2.1.S1"],
    ["sqs-faq-fifo-preserves-exact-order", "sqs-fifo-no-duplicates-introduced", "sqs-fifo-generated-dedup-id-from-body-hash",
     "sqs-faq-fifo-parallel-producers-order-might-not-be-preserved", "sqs-fifo-cannot-request-specific-group",
     "sqs-fifo-message-groups-no-quota", "sqs-faq-cannot-convert-standard-to-fifo", "sqs-change-fair-queues-standard-2025",
     "sqs-faq-fair-queues-versus-fifo-noisy-neighbor", "sqs-faq-fair-queues-same-throughput-as-standard"],
    {
        "problem": ("Some work must happen once and in order: a debit before the refund of the same account. A FIFO queue gives "
                    "order and no duplicates, but per message group and at a lower rate."),
        "trace": [
            "**Name the group.** Every message carries a group ID: you [associate a message group ID with each message] (sqs-fifo-message-group-id-required); a message [sent without a group ID, the action fails] (sqs-fifo-message-group-id-required).",
            "**Keep order in the group.** [Within a message group ID] (sqs-fifo-order-strict-within-group) messages are [sent and received in strict order] (sqs-fifo-order-strict-within-group); while one is in flight, no other message comes [from the same message group ID] (sqs-fifo-in-flight-blocks-same-group) [until the first message is deleted] (sqs-fifo-in-flight-blocks-same-group).",
            "**Run groups in parallel.** A FIFO queue allows [parallel processing of messages] (sqs-fifo-groups-processed-in-parallel) [across different message group IDs] (sqs-fifo-groups-processed-in-parallel).",
            "**Drop duplicates.** A second message with the same deduplication ID within the [5 minute deduplication interval] (sqs-fifo-deduplication-interval-5-minutes) is a duplicate, and [only one copy is delivered] (sqs-fifo-deduplication-interval-5-minutes). Content-based deduplication uses a [SHA-256 hash] (sqs-fifo-content-based-dedup-hash-body-only) of the body, [but not the attributes of the message] (sqs-fifo-content-based-dedup-hash-body-only).",
            "**Accept a rate.** By default a FIFO queue supports up to [300 messages per second] (sqs-faq-fifo-default-throughput-3000-with-batching-300-without), or [3,000 messages per second with batching] (sqs-faq-fifo-default-throughput-3000-with-batching-300-without).",
        ],
        "table": ("Which message group ID (columns: Group ID | Order | Parallel work): one ID for every message | one order for "
                  "the whole queue: [use a single message group ID] (sqs-fifo-single-group-for-strict-order) | one consumer at "
                  "a time; the customer ID | order for each customer | many customers at once; a new ID for each message | no "
                  "useful order | as much as the queue allows. Truth table."),
        "why": ("Why does AWS work this way? Order needs one consumer at a time for a group: FIFO queues do not serve a group to "
                "[more than one consumer at a time] (sqs-faq-fifo-same-group-one-consumer-at-a-time). Small groups keep that "
                "limit small."),
        "exam_signal": ("\"in the order they were sent\" with \"exactly once\" points to a FIFO queue, which gives [exactly-once "
                        "processing] (sqs-faq-fifo-exactly-once-processing)."),
        "exam_trap": "messaging-trap-fifo-global-order",
        "exam_trap_text": ("> **Exam trap:** A FIFO queue does not keep one order across all groups. [Messages with different "
                           "message group IDs] (sqs-fifo-no-order-across-groups) [may arrive or be processed out of order] "
                           "(sqs-fifo-no-order-across-groups). <!-- trap: messaging-trap-fifo-global-order -->"),
        "go_deeper": ("Go deeper: fair queues in a standard queue. Since July 2025, fairness is [applied automatically in all "
                      "Amazon SQS standard queues] (sqs-fair-queues-automatic-no-consumer-change) to messages that carry a group "
                      "ID; it [mitigates the noisy-neighbor impact] (sqs-fair-queues-noisy-neighbor-mitigation) of one busy "
                      "tenant. There the group ID is [used only as a tenant identifier] "
                      "(sqs-fair-queues-groupid-is-tenant-id-no-ordering) and [does not enforce message ordering] "
                      "(sqs-fair-queues-groupid-is-tenant-id-no-ordering). At most 60 words; 'July 2025' may link [July 21, "
                      "2025] (sqs-change-fair-queues-standard-2025) instead."),
        "body_extras": ("Only if words remain, one sentence: the name [must end with the .fifo suffix] "
                        "(sqs-fifo-queue-name-suffix), and you [cannot convert an existing standard queue] "
                        "(sqs-cannot-convert-standard-queue-to-fifo) to FIFO. Reference only: high throughput mode quotas are "
                        "volatile (sqs-fifo-ht-top-regions-70000-tps); no sentence."),
        "say_it": "The short answer is: FIFO keeps order per group, with no duplicates. The thing to watch is the group ID you choose.",
        "stop_and_answer": ("A FIFO queue holds payment events. The group ID is the payment type, card or bank, so one slow card "
                            "payment holds up every card payment. Which group ID keeps each customer's events in order and lets "
                            "customers run in parallel? Answer: the customer ID. Order holds [within a message group ID] "
                            "(sqs-fifo-order-strict-within-group), and different groups allow [parallel processing of messages] "
                            "(sqs-fifo-groups-processed-in-parallel)."),
    }, route="pass")

# 6 ---------------------------------------------------------------------------------------------
sub("After too many failed receives SQS moves a message to a dead-letter queue", 4, 215, ["2.1.K11", "2.1.K2", "3.2.S1"],
    ["sqs-faq-dlq-redrive-policy-max-receive-count", "sqs-dlq-create-queue-first", "sqs-faq-dlq-redrive-allow-policy-required",
     "sqs-dlq-redrive-allow-policy-default-allow-all", "sqs-dlq-denyall-blocks-use-as-dlq", "sqs-faq-dlq-redrive-velocity-selectable",
     "sqs-redrive-defaults-to-source-queue-same-type", "sns-dlq-alarm-on-visible-messages-not-messages-sent"],
    {
        "problem": ("A poison-pill message fails every time. Without a limit it comes back again and again, uses consumers and "
                    "hides real failures."),
        "trace": [
            "**Count the receives.** A redrive policy sets maxReceiveCount: the [number of times a consumer can receive] (sqs-dlq-max-receive-count-meaning) a message [before it is moved to a dead-letter queue] (sqs-dlq-max-receive-count-meaning).",
            "**Move it aside.** When the receive count [exceeds the maxReceiveCount] (sqs-faq-dlq-message-moved-when-receive-count-exceeds-max), SQS moves the message [with its original message ID] (sqs-faq-dlq-message-moved-when-receive-count-exceeds-max).",
            "**Match type and place.** The dead-letter queue of a FIFO queue [must also be a FIFO queue] (sqs-dlq-type-must-match-source-queue-type), and that of a standard queue [must also be a standard queue] (sqs-dlq-type-must-match-source-queue-type). It is in the [same AWS account and Region] (sqs-dlq-same-account-and-region).",
            "**Mind the clock.** In a standard queue [the enqueue timestamp is unchanged] (sqs-dlq-standard-enqueue-timestamp-unchanged) by the move, so set the dead-letter queue's retention [longer than the retention period] (sqs-dlq-retention-longer-than-source-queue) of the source. In a FIFO queue [the enqueue timestamp resets] (sqs-dlq-fifo-enqueue-timestamp-resets).",
            "**Fix, then redrive.** After you fix the consumer, you can [redrive the messages from your dead-letter queue] (sqs-faq-dlq-redrive-back-to-source-queue) [to the source queue] (sqs-faq-dlq-redrive-back-to-source-queue).",
        ],
        "table": ("Choosing maxReceiveCount (columns: Setting | Effect): a low count | a short glitch can send a good message "
                  "aside; a few receives | short glitches retry, a poison-pill message leaves soon; a queue that Lambda reads | "
                  "AWS advises [at least 5] (lambda-sqs-dlq-maxreceivecount-5); no redrive policy | the message returns until the "
                  "retention period deletes it. Four rows; cut row 1 first if over budget."),
        "why": ("Why does AWS work this way? Setting failures aside keeps the main queue moving. SQS offers [dead-letter queues and "
                "poison-pill management] (sqs-faq-hosted-queue-between-microservices-dlq-poison-pill) as common middleware."),
        "exam_signal": ("\"isolate messages that cannot be processed\" points to a dead-letter queue, which receives messages "
                        "when the consumer is [unable to consume the messages successfully] "
                        "(sqs-faq-dlq-definition-isolate-unprocessable-messages)."),
        "exam_trap": "messaging-trap-dlq-fresh-retention",
        "exam_trap_text": ("> **Exam trap:** A moved message does not start a fresh retention period in a standard queue: [the "
                           "enqueue timestamp is unchanged] (sqs-dlq-standard-enqueue-timestamp-unchanged). Set the dead-letter "
                           "queue's retention [longer than the retention period] (sqs-dlq-retention-longer-than-source-queue) of "
                           "the source queue. <!-- trap: messaging-trap-dlq-fresh-retention -->"),
        "go_deeper": ("Go deeper: the rules of a redrive. A [redrive task resets the retention period] "
                      "(sqs-redrive-resets-retention-and-assigns-new-id), and redriven messages are [considered new messages] "
                      "(sqs-redrive-resets-retention-and-assigns-new-id). It moves them [starting with the oldest message] "
                      "(sqs-redrive-oldest-first-order); SQS [doesn't support filtering and modifying messages] "
                      "(sqs-redrive-no-filter-or-modify) on the way. A FIFO queue with a dead-letter queue can [break the exact "
                      "order of messages or operations] (sqs-dlq-with-fifo-can-break-order). At most 60 words."),
        "body_extras": ("Reference only, no sentence: alarm on [use the ApproximateNumberOfMessagesVisible metric] "
                        "(sns-dlq-alarm-on-visible-messages-not-messages-sent) of the dead-letter queue, because the "
                        "[NumberOfMessagesSent metric is not suitable] (sns-dlq-alarm-on-visible-messages-not-messages-sent); a "
                        "redrive allow policy can deny use: [If you specify denyAll] (sqs-dlq-denyall-blocks-use-as-dlq)."),
        "say_it": "The short answer is: after a few failed tries, the message moves aside. The thing to watch is the dead-letter queue's retention.",
        "stop_and_answer": ("A FIFO queue named orders.fifo gets a redrive policy that points to a standard queue named "
                            "orders-dlq. Will SQS accept it? Answer: no; the dead-letter queue of a FIFO queue [must also be a "
                            "FIFO queue] (sqs-dlq-type-must-match-source-queue-type)."),
    })

# 7 ---------------------------------------------------------------------------------------------
sub("Workers scale on the backlog per instance and not on queue length", 4, 215, ["3.2.S2", "3.2.S1"],
    ["ec2-auto-scaling-sqs-dynamic-scaling-when-load-varies", "ecs-sqs-scale-on-backlog-per-task",
     "ecs-sqs-scale-in-protection-task-processing", "sqs-in-flight-standard-limit", "sqs-in-flight-standard-limit-short-vs-long-polling",
     "sqs-in-flight-limit-long-polling-no-error", "sqs-faq-fifo-supports-same-cloudwatch-metrics"],
    {
        "problem": ("Workers behind a queue must grow when messages wait too long and shrink when the queue drains. CPU and the "
                    "raw queue length both give the wrong signal."),
        "trace": [
            "**Read the queue.** [ApproximateNumberOfMessagesVisible] (sqs-metric-visible-messages-is-backlog) counts messages [available for retrieval and processing] (sqs-metric-visible-messages-is-backlog): the backlog. [ApproximateNumberOfMessagesNotVisible] (sqs-metric-not-visible-messages-is-in-flight) counts in-flight messages. [ApproximateAgeOfOldestMessage] (sqs-metric-age-of-oldest-message-measures-lag) gives the age of the [oldest unprocessed message in the queue] (sqs-metric-age-of-oldest-message-measures-lag).",
            "**Divide by the fleet.** The queue length [might not change proportionally] (ec2-auto-scaling-sqs-queue-length-not-proportional) to the group size, so use the [backlog per instance] (ec2-auto-scaling-sqs-backlog-per-instance): visible messages divided by [GroupInServiceInstances] (ec2-auto-scaling-sqs-backlog-per-instance-metric-math), built with [metric math] (ec2-auto-scaling-sqs-metric-math-instead-of-custom).",
            "**Set the target.** The target tracking target is the [acceptable backlog per instance] (ec2-auto-scaling-sqs-backlog-per-instance): take the acceptable wait and [divide it by the average time] (ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target) one message takes.",
            "**Protect long jobs.** A message that is not finished when its instance ends is [returned to the SQS queue] (ec2-auto-scaling-sqs-unprocessed-messages-return); [use instance scale-in protection] (ec2-auto-scaling-sqs-unprocessed-messages-return) for long work.",
            "**Add consumers.** More consumers give [essentially linear gains in queue throughput] (sqs-horizontal-scaling-linear-gain).",
        ],
        "table": ("Scaling metric for queue workers (columns: Metric | Result): average CPU | for batch work [100% CPU utilization "
                  "is expected and should not be your primary metric] (ec2-auto-scaling-wa-queue-depth-metric-for-batch-work); "
                  "visible messages alone | it [might not change proportionally] "
                  "(ec2-auto-scaling-sqs-queue-length-not-proportional) to the group size; backlog per instance | moves with the "
                  "group size, so target tracking can hold it (plain words). Cells at most 15 words: the CPU cell is the display "
                  "plus 'for batch work' (14 words)."),
        "why": ("Why does AWS work this way? What one worker faces is the backlog divided by the workers. That number falls when "
                "the group grows, so a target tracking policy can steer it."),
        "exam_signal": ("\"scale the workers on the number of messages in the queue\" points to target tracking on backlog per "
                        "instance, which uses the [acceptable backlog per instance] (ec2-auto-scaling-sqs-backlog-per-instance) "
                        "as its target."),
        "exam_trap": None,
        "startup_example": ("> **Startup example:** Callvale's convert queue feeds conversion workers in an Auto Scaling group "
                            "that runs from zero to 40 instances. The group tracks the backlog per instance, so it grows in "
                            "the morning and empties at night. (at most 30 words; 40 is worker_group_max of stage 2; write "
                            "'zero' as a word)"),
        "go_deeper": None,
        "body_extras": ("Reference only (B-list): a standard queue holds [approximately 120,000 in flight messages] "
                        "(sqs-in-flight-standard-limit); at that point short polling [returns the OverLimit error message] "
                        "(sqs-in-flight-standard-limit-short-vs-long-polling). Amazon ECS services scale the same way, on the "
                        "[scale on the *backlog per task*] (ecs-sqs-scale-on-backlog-per-task): copy that display exactly with its "
                        "asterisks only if a writer needs it; it is not planned in prose."),
        "say_it": "The short answer is: scale workers on the messages waiting per worker. The thing to watch is long jobs during scale-in.",
        "stop_and_answer": ("A group of four workers faces two thousand visible messages, and the target is a backlog of one "
                            "hundred per instance. Will target tracking add workers? Answer: yes; the backlog per instance is "
                            "visible messages divided by [GroupInServiceInstances] "
                            "(ec2-auto-scaling-sqs-backlog-per-instance-metric-math), which is five times the target here. "
                            "Numbers in the prompt are words, so the reveal needs no number with a unit."),
    })
