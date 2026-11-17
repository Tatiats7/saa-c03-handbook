---
id: "31"
slug: messaging
title: SQS, SNS and EventBridge
file: fast
tier: deep
domains: [1, 2, 3]
tasks: ["2.1", "3.2", "1.1"]
services: [sqs, sns, eventbridge]
minutes: {fast: 20, pass: 72, full: 165}
status: ready
updated: 2026-10-14
---

# SQS, SNS and EventBridge

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** A worker receives a message from a queue and then crashes before it finishes the work. Is the message lost? <!-- gist-trap -->

**Predict 2.** Three services poll the same queue. Does each service get every message?

**Predict 3.** The target of an event rule is down for an hour. Does the event wait for it?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

In AWS CloudShell, list the Amazon Simple Queue Service (Amazon SQS) queues, Amazon Simple Notification Service (Amazon SNS) topics and Amazon EventBridge event buses. Every account has a [default event bus](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events), so the last list is not empty.

<!-- task:start id=messaging-t01 -->

Look

**It kills the belief.** "An account has no event bus until you create one."

> **Cost:** $0.

**Permissions.** `sqs:ListQueues`, `sns:ListTopics`, `events:ListEventBuses`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. List the Amazon SQS queues of the current Region.

   ```bash
   aws sqs list-queues
   ```

   Expect: The URLs of your queues under QueueUrls, or no output when this Region has no queue.

2. List the Amazon SNS topics of the same Region.

   ```bash
   aws sns list-topics --query "Topics[].TopicArn"
   ```

   Expect: A list of topic ARNs, or an empty list.

3. Predict first: you never created an event bus, so how many buses does the list hold? Then list the Amazon EventBridge event buses of the same Region.

   ```bash
   aws events list-event-buses --query "EventBuses[].Name"
   ```

   Expect: A list that holds at least one bus, named default, although you never created it. AWS services send their events to this bus.

**Label.** checked against docs, not run in a real account. Checked 2026-10-15.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon SQS holds messages until a consumer deletes them. Amazon SNS pushes a copy to every subscriber. Amazon EventBridge sends events to targets by rules.

**The problem it solves.** A direct call makes the caller wait, and one failure loses the request. A queue between the producer (sender) and the consumer (receiver) lets you **decouple** (dee-KUP-ul) them, so the work is **asynchronous** (ay-SING-kruh-nus).

**Predict the picture.** Where does a sent message wait, and when does it leave?

<details>
<summary>Show the picture</summary>

![A sequence with three participants: a producer, an SQS queue and a consumer. The producer sends a message, and the queue confirms it. The consumer receives the message, which stays in the queue but hidden. The consumer deletes it. A second path shows a message that is not deleted becoming visible again.](../diagrams/svg/messaging-hero.svg)

**Figure.** A message waits in the queue, hidden while one consumer works on it, until that consumer deletes it.

1. The producer sends a message, and SQS [stores the message in multiple availability zones](../facts/sqs.md#sqs-send-stored-multi-az-before-ack) before it confirms.
2. A consumer polls the queue and receives the message.
3. After the receive, [it remains in the queue](../facts/sqs.md#sqs-receive-keeps-message-hidden) but is [temporarily invisible to other consumers](../facts/sqs.md#sqs-receive-keeps-message-hidden).
4. The consumer processes the message and deletes it [using the DeleteMessage action](../facts/sqs.md#sqs-manual-delete-after-processing).
5. If the consumer does not delete it in time, the message [becomes visible again in the queue](../facts/sqs.md#sqs-undeleted-message-visible-again).

</details>

> **Startup example:** After each upload, Callvale's web application calls the worker and waits. On launch day, the worker was overloaded and 1,900 uploads failed. No upload can be lost again, and one failed recording must not block the others. Several systems must learn when a transcript is ready.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| queue (KYOO) | **poll** a queue | A store that holds messages until a consumer processes them | topic |
| topic | **subscribe** a queue to a topic | A named point that sends each message to all its subscribers | queue |
| visibility timeout | **set** the visibility timeout of the queue | The time a received message stays hidden from other consumers | delay queue |
| dead-letter queue | **configure** a dead-letter queue | The queue that gets a message after too many failed receives | visibility timeout |
| idempotent (eye-dem-POH-tent) | **make** the consumer idempotent | Gives the same result when the same message comes twice | exactly-once processing |
| message group ID | **set** a message group ID | Puts a FIFO message in a group that keeps its order | message deduplication ID |
| fan-out | the fan-out **pattern** | One message sent to many receivers at the same time | filter policy |
| event bus | **send** events to an event bus | Receives events and routes them with rules | topic |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### SQS SNS or EventBridge

<!-- table: compare -->
| Question | SQS | SNS | EventBridge |
|---|---|---|---|
| How does a message move? | Consumers poll: a [pull-based model](../facts/sqs.md#sqs-decision-pull-model) | SNS sends it to every subscriber: a [push-based model](../facts/sns.md#sns-decision-push-model) | EventBridge [matches events against rules](../facts/eventbridge.md#eventbridge-decision-rule-routing) and sends them to targets |
| What does it keep? | The message, [until successfully processed or expired](../facts/sqs.md#sqs-decision-keeps-until-processed) | A standard topic, nothing: [messages are not persisted](../facts/sns.md#sns-decision-no-persistence) | A Classic bus, nothing: events are [not retained. To keep events, add an archive.](../facts/eventbridge.md#eventbridge-classic-bus-does-not-retain-events) |
| Typical use? | [Buffering requests](../facts/sqs.md#sqs-decision-typical-use) between tiers | [Fanout notifications](../facts/sns.md#sns-decision-typical-use) to many subscribers | AWS and partner events, [cross-account event sharing](../facts/eventbridge.md#eventbridge-decision-typical-use) |

**Deciding question:** Does one consumer pull at its own pace, must every subscriber get a copy now, or do the events come from AWS services or SaaS partners?

> **Exam trap:** Do not build a function that polls AWS for changes. The [default event bus](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events) [automatically receives events from AWS services](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events). For software as a service (SaaS) events, choose EventBridge, not SNS. It is the [only event-based service](../facts/eventbridge.md#eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners) that integrates directly with [third-party SaaS partners](../facts/eventbridge.md#eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners). <!-- trap: messaging-trap-build-own-change-detection --> <!-- trap: messaging-trap-topic-receives-saas-events -->

### Standard or FIFO queue

<!-- table: compare -->
| Question | Standard queue | FIFO queue |
|---|---|---|
| How many copies arrive? | [At-least-once message delivery](../facts/sqs.md#sqs-standard-at-least-once-duplicates) | [Exactly-once processing](../facts/sqs.md#sqs-faq-fifo-exactly-once-processing) |
| What order? | A [best-effort attempt](../facts/sqs.md#sqs-standard-best-effort-ordering) | [Sent and received in strict order](../facts/sqs.md#sqs-fifo-order-strict-within-group), within each message group |
| How much throughput? | [Nearly unlimited](../facts/sqs.md#sqs-standard-throughput-nearly-unlimited) | By default, up to [3,000 messages per second with batching](../facts/sqs.md#sqs-faq-fifo-default-throughput-3000-with-batching-300-without); more with high throughput mode |

**Deciding question:** Must order within a group and no duplicates be guaranteed, or can idempotent consumers accept repeats in any order?

### Hide a message or schedule the work

<!-- table: compare -->
| Question | Delay queue | Visibility timeout | Amazon EventBridge Scheduler |
|---|---|---|---|
| What does it do? | A message is [hidden when it is first added to queue](../facts/sqs.md#sqs-delay-queue-hidden-at-add-visibility-after-receive) | A message is hidden [only after it is consumed from the queue](../facts/sqs.md#sqs-delay-queue-hidden-at-add-visibility-after-receive) | Starts a task on [rate-based, cron-based, and one-time schedules](../facts/eventbridge.md#eventbridge-scheduler-three-schedule-types) |
| Longest wait? | [15 minutes](../facts/sqs.md#sqs-delay-queue-range) | [12 hours](../facts/sqs.md#sqs-visibility-timeout-range) | Any later time: [EventBridge Scheduler is the recommended solution](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling) |

**Deciding question:** Must a new message wait unseen, must a received one stay hidden during the work, or must work start at a set time?

> **Exam trap:** A delay queue or a **message timer** does not hold a message for hours or days. Both delay it [up to 15 minutes in the future](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling). For a later start, [EventBridge Scheduler is the recommended solution](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling). <!-- trap: messaging-trap-delay-queue-days -->

### SQS Amazon MQ or Kinesis Data Streams

<!-- table: compare -->
| Question | SQS | Amazon MQ | Amazon Kinesis Data Streams |
|---|---|---|---|
| Made for? | [Recommended for new applications](../facts/sqs.md#sqs-sns-recommended-for-new-applications) | Moving [existing applications](../facts/sns.md#sns-faq-mq-for-existing-apps-standards-based-brokers) off their message brokers | [Real-time processing of streaming big data](../facts/sqs.md#sqs-faq-kinesis-streams-realtime-and-replay) |
| What about the code? | The SQS API | Moves [without rewriting the messaging code](../facts/sns.md#sns-faq-mq-for-existing-apps-standards-based-brokers) | Several applications [read and replay records](../facts/sqs.md#sqs-faq-kinesis-streams-realtime-and-replay) |

**Deciding question:** Is it a new application, an existing broker application that must move without code changes, or a stream that several readers replay?

<!-- xref: 32 Amazon MQ --> <!-- xref: 34 Kinesis Data Streams -->

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "decouple; the database cannot keep up at peak" | an SQS queue between the tiers | it keeps each message [until successfully processed or expired](../facts/sqs.md#sqs-decision-keeps-until-processed) | every service needs each message: SNS fan-out to queues |
| "every service must receive every message" | an SNS topic with one SQS queue per service | SNS [sends the message to each subscribed queue](../facts/sns.md#sns-publish-sends-message-to-each-subscribed-queue) | services pick AWS or partner events by content: EventBridge rules |
| "process in order; no duplicates" | an SQS FIFO queue, one message group ID per entity | a group's messages are [sent and received in strict order](../facts/sqs.md#sqs-fifo-order-strict-within-group) | repeats come hours later: an idempotent consumer |
| "react to an AWS service event or a SaaS event" | an **EventBridge rule** | the default bus [automatically receives events from AWS services](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events) | your own events go to thousands of phones: SNS |
| "run a job every night; send a reminder in three days" | EventBridge Scheduler | it runs [rate-based, cron-based, and one-time schedules](../facts/eventbridge.md#eventbridge-scheduler-three-schedule-types) | a short delay per message: an SQS delay queue, up to [15 minutes](../facts/sqs.md#sqs-delay-queue-range) |
| "a message fails again and again; poison message" | a dead-letter queue with a **redrive policy** | `maxReceiveCount` is the [number of times a consumer can receive](../facts/sqs.md#sqs-dlq-max-receive-count-meaning) it | the job outlasts the visibility timeout: raise the timeout |
| "scale the workers on the queue" | target tracking on **backlog per instance** | queue length alone [might not change proportionally](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-queue-length-not-proportional) | Lambda reads the queue: [Lambda handles the polling](../facts/lambda.md#lambda-esm-lambda-polls-source) |

### Traps

- **Wrong belief:** Receiving a message removes it from the queue. **Truth:** The message stays, [temporarily invisible to other consumers](../facts/sqs.md#sqs-receive-keeps-message-hidden). Without a delete, it comes back. <!-- trap: messaging-trap-receive-deletes -->
- **Wrong belief:** Several services that poll one queue each get every message. **Truth:** For a copy per service, subscribe [multiple SQS standard queues to the SNS topic](../facts/sns.md#sns-faq-fanout-identical-messages-to-multiple-sqs-queues). <!-- trap: messaging-trap-queue-broadcasts -->
- **Wrong belief:** An SNS topic keeps messages until an offline subscriber comes back. **Truth:** In a standard topic, [messages are not persisted](../facts/sns.md#sns-decision-no-persistence). A subscribed SQS queue keeps its copy [until successfully processed or expired](../facts/sqs.md#sqs-decision-keeps-until-processed). A FIFO topic can archive messages for [up to 365 days](../facts/sns.md#sns-change-fifo-archiving-replay-2023). <!-- trap: messaging-trap-topic-stores-messages -->
- **Wrong belief:** A standard queue delivers each message one time, in order. **Truth:** It can deliver [more than one copy of a message](../facts/sqs.md#sqs-standard-at-least-once-duplicates), and order is a [best-effort attempt](../facts/sqs.md#sqs-standard-best-effort-ordering). Make each consumer idempotent. <!-- trap: messaging-trap-standard-exactly-once -->
- **Wrong belief:** An event bus keeps its events for later reads. **Truth:** On a Classic bus, events are [not retained. To keep events, add an archive.](../facts/eventbridge.md#eventbridge-classic-bus-does-not-retain-events) A replay can then [reprocess past events](../facts/eventbridge.md#eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule). <!-- trap: messaging-trap-bus-stores-events -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-08-04) Largest SQS message.<br>
> **Old:** [256 KiB](../facts/sqs.md#sqs-change-max-message-size-1mib-2025).<br>
> **Now:** [1,048,576 bytes (1 MiB)](../facts/sqs.md#sqs-change-max-message-size-1mib-2025).<br>
> **The exam probably expects:** the old limit, with large payloads in Amazon S3. Prefer an option that is right under both values.<br>
> **Status:** examinable.

> **Changed recently:** (2026-01-29) Largest EventBridge request.<br>
> **Old:** [256 KB](../facts/eventbridge.md#eventbridge-change-event-size-1mb-2026).<br>
> **Now:** [1 MB (1,048,576 bytes)](../facts/eventbridge.md#eventbridge-change-event-size-1mb-2026), in most commercial Regions.<br>
> **The exam probably expects:** the old value, if any. Do not let this number decide an answer.<br>
> **Status:** examinable.

> **Changed recently:** (2023-11-27) Redrive from a FIFO dead-letter queue.<br>
> **Old:** not available.<br>
> **Now:** a FIFO dead-letter queue can be redriven, and the destination [must be a FIFO queue as well](../facts/sqs.md#sqs-change-fifo-dlq-redrive-2023).<br>
> **The exam probably expects:** the old value, if any.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** A consumer receives a message, then loses its network before the delete. What happens to the message?

<details>
<summary>Answer</summary>

After the visibility timeout ends, it [becomes visible again in the queue](../facts/sqs.md#sqs-undeleted-message-visible-again).

**Predict 1:** No. It can be [retrieved by the same or a different consumer](../facts/sqs.md#sqs-failed-processing-message-not-lost).

</details>

**Check 2.** Billing and email services must each get every order event, even after an outage. What do you build?

<details>
<summary>Answer</summary>

Subscribe [multiple SQS standard queues to the SNS topic](../facts/sns.md#sns-faq-fanout-identical-messages-to-multiple-sqs-queues), one per service.

**Predict 2:** No: [a single subscriber typically](../facts/sqs.md#sqs-typically-single-subscriber-order-and-loss) processes each message.

</details>

**Check 3.** A topic delivers to a partner's HTTPS endpoint that is down for a day. Does SNS keep it?

<details>
<summary>Answer</summary>

No. SNS [stops retrying the delivery and discards the message](../facts/sns.md#sns-retry-exhausted-discards-unless-dlq), unless [a dead-letter queue is attached to the subscription](../facts/sns.md#sns-retry-exhausted-discards-unless-dlq).

**Predict 3:** Yes: EventBridge retries for [24 hours](../facts/eventbridge.md#eventbridge-retry-default-24h-185-attempts) by default. Then [the event is dropped](../facts/eventbridge.md#eventbridge-retry-exhausted-event-dropped), unless a dead-letter queue catches it.

</details>

## Recap from memory (2 min)
<!-- section: role=recap; route=fast; minutes=2 -->

**Recap 1.** What do SQS, SNS and EventBridge each keep after a message arrives?

<details>
<summary>Answer</summary>

SQS keeps the message [until successfully processed or expired](../facts/sqs.md#sqs-decision-keeps-until-processed). A standard SNS topic: [messages are not persisted](../facts/sns.md#sns-decision-no-persistence). A Classic event bus: [not retained. To keep events, add an archive.](../facts/eventbridge.md#eventbridge-classic-bus-does-not-retain-events)

</details>

**Recap 2.** What fits "a message fails again and again", and what is its "But not if"?

<details>
<summary>Answer</summary>

A dead-letter queue with a redrive policy. Not if the job outlasts the visibility timeout: then raise the timeout.

</details>

**Recap 3.** Which service takes events from SaaS partners directly?

<details>
<summary>Answer</summary>

EventBridge, the [only event-based service](../facts/eventbridge.md#eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners) with direct SaaS integration.

</details>
