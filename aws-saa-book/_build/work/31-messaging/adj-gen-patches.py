"""adjudicate-31: write repair patches for disputed chapter 31 facts into adj-patches/.
Each spec changes only what the quote cannot carry; new evidence items are verbatim snapshot text."""
import json, os, copy
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "adj-patches")
os.makedirs(OUT, exist_ok=True)
facts = {}
for s in ["sqs", "sns", "eventbridge"]:
    for line in open(os.path.join(ROOT, "data", "facts", s + ".jsonl")):
        if line.strip():
            d = json.loads(line)
            facts[d["id"]] = d

D = "https://docs.aws.amazon.com/"
SQSG = "docs/AWSSimpleQueueService/latest/SQSDeveloperGuide/"
def sqsg(page):
    return {"source_id": SQSG + page, "url": D + "AWSSimpleQueueService/latest/SQSDeveloperGuide/" + page + ".html"}
def ebg(page):
    return {"source_id": "docs/eventbridge/latest/userguide/" + page, "url": D + "eventbridge/latest/userguide/" + page + ".html"}

def ev(fid, i, quote=None, heading=None):
    e = facts[fid]["evidence"][i]
    o = {"source_id": e["source_id"], "url": e["url"], "quote": quote if quote is not None else e["quote"], "table_header": e.get("table_header")}
    if heading is not None:
        o["heading"] = heading
    elif e.get("heading"):
        o["heading"] = e["heading"]
    return o

def new(src, quote, table_header=None, heading=None):
    o = dict(src); o["quote"] = quote; o["table_header"] = table_header
    if heading:
        o["heading"] = heading
    return o

def same(fid, quote, i=0, table_header=None, heading=None):
    e = facts[fid]["evidence"][i]
    return new({"source_id": e["source_id"], "url": e["url"]}, quote, table_header, heading)

def q(fid, **kw):
    base = dict(facts[fid]["qualifiers"])
    base.update(kw)
    return base

def vals(*pairs):
    return [{"key": k, "display": v} for k, v in pairs]

P = {}

# --- EventBridge ---
f = "eventbridge-case-legendary-play-fine-grained-rules"
P[f] = {"claim": "At Legendary Play, a blockchain service consumes all the events in the system to update the chain, and each of its services exists on its own AWS account within the organization (customer case study)."}

f = "eventbridge-change-direct-delivery-cross-account-targets-2025"
P[f] = {"claim": "On 2025-01-21 EventBridge Event Bus began to deliver events directly to AWS services in another account, without the need for an intermediary EventBridge event bus or Lambda function. It delivers cross-account to targets that support resource-based IAM policies, such as SQS, Lambda, Kinesis Data Streams, SNS and API Gateway.",
        "qualifiers": q(f, condition=""),
        "evidence": [ev(f, 0), ev(f, 1), ev(f, 2), same(f, "This launch allows you to directly target services in another account, without the need for additional infrastructure such as an intermediary EventBridge Event Bus or Lambda function, simplifying your architecture and reducing cost.")]}

f = "eventbridge-change-scheduler-launch-2022"
P[f] = {"claim": "The EventBridge Scheduler User Guide had its initial release on November 10, 2022, and the EventBridge Pipes documentation was launched on December 1, 2022."}

f = "eventbridge-classic-bus-no-ordered-delivery"
P[f] = {"claim": "Ordering is not available on Custom Event Bus - Classic, the bus type that uses rules and targets; on the Custom Event Bus, ordering is FIFO delivery within an event group, per subscriber.",
        "evidence": [ev(f, 0), same(f, "In the EventBridge console, the bus type is shown as Custom Event Bus for this bus and Custom Event Bus - Classic for the buses that use rules and targets.")]}

f = "eventbridge-cloudtrail-events-need-trail-logging"
P[f] = {"claim": "To record EventBridge events with one of the CloudTrail detail-type values, you must enable a CloudTrail trail with logging.",
        "values": vals(("trail", "you must enable a CloudTrail trail with logging")),
        "evidence": [ev(f, 0)]}

f = "eventbridge-decision-events-category-decouple-publishers-subscribers"
P[f] = {"claim": "In the integration decision guide's Choose table, the row whose associated services are Amazon EventBridge and Amazon SNS is for when you need to decouple publishers and subscribers and send events to multiple subscribers simultaneously, and it is optimized for asynchronous, loosely coupled communication between publishers and subscribers."}

f = "eventbridge-dlq-api-needs-manual-queue-policy"
P[f] = {"claim": "For a dead-letter queue (DLQ) of an EventBridge rule target: if you add a target to a rule using the console and choose an SQS queue in the same account, a resource-based policy that grants EventBridge access to the queue is attached to the queue for you; if you use the PutTargets operation of the EventBridge API and choose an SQS queue in the same account, you must manually grant permissions to the queue.",
        "qualifiers": q(f, scope="EventBridge dead-letter queue (SQS queue in the same account)"),
        "evidence": [same(f, "Consider the following when configuring a DLQ for EventBridge."), ev(f, 0),
                     same(f, "If you use the PutTargets operation of the EventBridge API to add or update a target for a rule, and you choose an Amazon SQS queue in the same account, you must manually grant permissions to the queue selected. To learn more, see Granting permissions to the dead-letter queue.")]}

f = "eventbridge-pattern-matches-metadata-data-content"
P[f] = {"claim": "Event patterns for event buses can match against the event source, event metadata, and/or event detail values. Event metadata is data about the event, such as the event source, or the account or Region in which the event originated; event content is the actual property values of the event data.",
        "values": vals(("match", "event metadata, and/or event detail values"), ("metadata", "such as the event source"), ("content", "The actual property values of the event data")),
        "evidence": [new(ebg("eb-event-patterns"), "Event patterns for event buses can match against the event source, event metadata, and/or event detail values."), ev(f, 0)]}

f = "eventbridge-pattern-prefix-and-suffix-matching"
P[f] = {"claim": "You can match an EventBridge event depending on the prefix or the suffix of a value in the event source; prefix matching and suffix matching work for string values."}

f = "eventbridge-pricing-aws-management-events-free"
P[f] = {"claim": "On Custom event buses - classic, AWS management events are ingested by the event bus for free (AWS Free Tier).",
        "qualifiers": q(f, scope="Custom event buses - classic; AWS management events ingested by the event bus"),
        "evidence": [ev(f, 0, quote="AWS Free Tier: AWS management events are ingested by the event bus for free.", heading="Custom event buses - classic")]}

f = "eventbridge-pricing-custom-events-per-million"
P[f] = {"claim": "In the Custom event buses - classic pricing example, the monthly ingestion charge for 10M custom events of 64 KB or less each is 10M * $1.00/M = $10.00 per month.",
        "qualifiers": q(f, scope="Custom event buses - classic; per M (million) custom events ingested, events of 64 KB or less", condition="Worked example in the Custom event buses - classic section of the pricing page.")}

f = "eventbridge-pricing-delivery-to-bus-vs-same-account-service"
P[f] = {"claim": "In the Custom event buses - classic pricing example, where custom events published to an event bus in Account A are sent to another event bus in Account B and then to another service in Account B, custom events delivered to another event bus are charged at $1.00/M, and custom events delivered to a service in the same account are charged at $0.00/M.",
        "qualifiers": q(f, scope="Custom event buses - classic; per M (million) custom events delivered, events of 64 KB or less", condition="Worked example: Account A bus to Account B bus, then to a service in Account B."),
        "evidence": [same(f, "If you publish 10 million of your own events to an event bus in Account A in one month, send 5 million of those events to another event bus in Account B, and then send those events to another service in Account B, your charges would be calculated as follows:"), ev(f, 0)]}

f = "eventbridge-pricing-global-endpoints-no-charge"
P[f] = {"claim": "On Custom event buses - classic, there is no additional charge for global endpoints; custom events published to the global endpoint are billed according to the custom events pricing.",
        "qualifiers": q(f, scope="Custom event buses - classic; EventBridge global endpoints"),
        "evidence": [ev(f, 0, heading="Custom event buses - classic")]}

f = "eventbridge-putevents-up-to-10-entries"
P[f] = {"claim": "When you send custom events to EventBridge using the PutEvents action, you can batch up to 10 event entries into one request.",
        "qualifiers": q(f, scope="per PutEvents request (custom events)", condition="")}

f = "eventbridge-scheduler-flexible-window-max-1440-minutes"
P[f] = {"claim": "In the EventBridge Scheduler API, the maximum time window during which a schedule can be invoked has a valid range from a minimum value of 1 to a maximum value of 1440. The user guide sets a flexible time window in minutes, for example a 15 minute window within which the target is invoked after the scheduled time.",
        "qualifiers": q(f, scope="per schedule; flexible time window"),
        "evidence": [ev(f, 0), new({"source_id": "docs/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows", "url": D + "scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html"},
                                   "For example, if you configure a 15 minute flexible time window for a schedule that runs every hour, it invokes the target within 15 minutes after the scheduled time.")]}

f = "eventbridge-some-errors-skip-retries"
P[f] = {"claim": "Some EventBridge events are dropped or sent to a DLQ without any retry attempts. For errors that result from missing permissions to a target, a target resource that no longer exists, or a target that cannot be found because of an invalid address or DNS lookup failure, no retry attempts happen until action is taken to resolve the underlying issue. EventBridge sends these events directly to the target DLQ, if you have specified one.",
        "qualifiers": q(f, condition="until action is taken to resolve the underlying issue")}

f = "eventbridge-sqs-fair-fifo-target-needs-sqsparameters"
P[f] = {"claim": "EventBridge uses the Target parameters to determine what happens with some targets; you use SqsParameters to specify the message group to use as the target.",
        "qualifiers": q(f, scope="EventBridge rule target parameters"),
        "evidence": [same(f, "EventBridge uses the Target parameters to determine what happens with that target."), ev(f, 0)]}

f = "eventbridge-target-types-list"
P[f] = {"claim": "For Custom Event Bus - Classic rules, you can have EventBridge send events to a number of AWS service resources, including an ECS task, a Firehose delivery stream, a Kinesis stream, a Lambda function (ASYNC), an SNS topic, Amazon SQS standard, fair, and FIFO queues, and a Step Functions state machine (ASYNC).",
        "evidence": [same(f, "This topic describes targets for Custom Event Bus - Classic rules."), same(f, "You can have EventBridge send events to a number of AWS service resources."), ev(f, 0)]}

f = "eventbridge-two-rule-types-pattern-and-schedule"
P[f] = {"claim": "You can create two types of EventBridge rules: rules that match on event data as events are delivered, and rules that run on a defined schedule."}

f = "eventbridge-wa-deployed-multi-az-by-aws"
P[f] = {"qualifiers": q(f, scope="Regional AWS services named in REL11-BP02 (including SQS, SNS and EventBridge)")}

# --- SNS ---
for f in ["sns-a2a-subscriber-types", "sns-a2p-subscriber-types"]:
    P[f] = {"qualifiers": q(f, scope="Amazon SNS subscribers")}

f = "sns-addpermission-adds-policy-statement"
P[f] = {"claim": "To allow one or more AWS accounts to perform a specific action on an SNS topic, such as publishing messages, you can use the SNS API action AddPermission. You specify a topic, a list of AWS account IDs, a list of actions and a label, and SNS automatically generates and adds a new policy statement to the topic's access control policy.",
        "evidence": [same(f, "Let's say you have a topic in Amazon SNS, and you want to allow one or more AWS accounts to perform a specific action on that topic, such as publishing messages. You can accomplish this by using the Amazon SNS API action AddPermission."),
                     same(f, "The AddPermission action allows you to specify a topic, a list of AWS account IDs, a list of actions, and a label. Amazon SNS then automatically generates and adds a new policy statement to the topic's access control policy.")]}

f = "sns-change-fifo-throughput-scope-high-throughput-2025"
P[f] = {"qualifiers": q(f, condition="To get higher throughput, enable high-throughput mode by setting the FifoThroughputScope topic attribute to MessageGroup.")}

f = "sns-change-max-message-size-1mib-opt-in-2026"
P[f] = {"qualifiers": q(f, scope="per message, per topic", condition=""),
        "note": "Not examinable yet: posted 2026-09-18, after the 2026-07-15 cut-off (RULINGS rule 7). The General Reference quota page still lists 256 KiB."}

f = "sns-client-side-error-not-retried"
P[f] = {"claim": "Amazon SNS doesn't retry a message delivery that fails because of a client-side error.",
        "qualifiers": q(f, condition="")}

f = "sns-cross-region-delivery-to-sqs-and-lambda"
P[f] = {"evidence": [same(f, "Amazon SNS supports cross-Region deliveries, both for Regions that are enabled by default and for opt-in Regions."), ev(f, 0)]}

f = "sns-faq-default-only-topic-owner-can-publish"
P[f] = {"claim": "By default, only topic owners have permissions to publish to an SNS topic. A topic owner can set explicit permissions to allow more than one user (with a valid AWS ID) to publish to a topic."}

for f in ["sns-faq-order-attempted-but-network-issues-can-reorder", "sns-faq-subscriber-may-receive-duplicates"]:
    P[f] = {"qualifiers": q(f, scope="Amazon SNS message delivery")}

f = "sns-fifo-content-hash-excludes-attributes"
P[f] = {"claim": "With content-based deduplication on an SNS FIFO topic, SNS uses the message body to generate a unique hash value to use as the deduplication ID for each message; message attributes are not included in the hash calculation.",
        "evidence": [same(f, "If the message body is guaranteed to be unique for each published message, you can enable content-based deduplication for an Amazon SNS FIFO topic and the subscribed Amazon SQS FIFO queues. Amazon SNS uses the message body to generate a unique hash value to use as the deduplication ID for each message, so you don't need to set a deduplication ID when you send each message."), ev(f, 0)]}

f = "sns-fifo-deduplication-interval-5-minutes"
P[f] = {"claim": "If a message with a particular deduplication ID is successfully published to an SNS FIFO topic, any message published with the same deduplication ID within the five minute deduplication interval is accepted but not delivered. Deduplication applies to the entire topic when FifoThroughputScope is set to Topic, and to each individual message group when it is set to MessageGroup.",
        "qualifiers": q(f, scope="per SNS FIFO topic (FifoThroughputScope Topic) or per message group (MessageGroup); per deduplication ID"),
        "evidence": [ev(f, 0), same(f, "Message deduplication applies to an entire Amazon SNS FIFO topic when the topic attribute FifoThroughputScope is set to Topic. When the topic attribute FifoThroughputScope is set to MessageGroup, message deduplication applies to each individual message group.")]}

LEAD = "Amazon SNS FIFO topics and Amazon SQS FIFO queues support message deduplication, which provides exactly-once message delivery and processing as long as the following conditions are met:"
f = "sns-fifo-exactly-once-lost-with-filtering"
P[f] = {"claim": "SNS FIFO topics and SQS FIFO queues provide exactly-once message delivery and processing as long as listed conditions are met; one condition is that the SNS subscription has no message filtering. When you configure message filtering, SNS FIFO topics support at-most-once delivery, as messages can be filtered out based on your subscription filter policies.",
        "evidence": [same(f, LEAD), ev(f, 0)]}
f = "sns-fifo-exactly-once-needs-consumer-delete-before-timeout"
P[f] = {"claim": "SNS FIFO topics and SQS FIFO queues provide exactly-once message delivery and processing only as long as listed conditions are met; one condition is that the SQS FIFO queue consumer processes the message and deletes it from the queue before the visibility timeout expires.",
        "evidence": [same(f, LEAD), ev(f, 0)]}

f = "sns-fifo-high-throughput-enable-messagegroup"
P[f] = {"evidence": [ev(f, 0, quote="To enable high throughput for your Amazon SNS FIFO topic, update the FifoThroughputScope attribute to MessageGroup. This change can be done through the console or using the AWS CLI and SDK, and can also be set during topic creation, which Amazon SNS recommends for the best customer experience and to reduce the chances of your topic being throttled.")]}

f = "sns-fifo-sqs-server-error-retries-100015"
P[f] = {"claim": "When server-side errors occur, SNS FIFO topics retry the failed deliveries up to 100,015 times over 23 days.",
        "qualifiers": q(f, scope="per failed delivery from an SNS FIFO topic; server-side errors", condition="")}

f = "sns-pricing-fifo-min-1kb-message"
P[f] = {"claim": "For SNS FIFO topics, each message up to 1 MiB is billed as one message with a minimum of 1 KB, in addition to the charge per GB of payload data; any message smaller than 1KB is rounded up to 1KB.",
        "values": vals(("min", "rounded up to 1KB"), ("smaller", "Any message smaller than 1KB"), ("fifo-min", "a minimum of 1 KB")),
        "evidence": [same(f, "For FIFO topics, each message up to 1 MiB is billed as one message with a minimum of 1 KB, in addition to the charge per GB of payload data."), ev(f, 0)]}

FOOT = "Amazon SNS FIFO per topic limits exceed the default per account limit when FifoThroughputScope is set to MessageGroup."
f = "sns-publish-throttle-all-other-regions"
P[f] = {"claim": "In the SNS Publish API throttling table, all other supported Regions have 300 messages per second for standard topics and 3,000 messages per second for FIFO topics; SNS FIFO per-topic limits exceed this default per-account limit when FifoThroughputScope is set to MessageGroup.",
        "qualifiers": q(f, scope="per account, per Region (all other supported Regions)"),
        "evidence": [ev(f, 0), same(f, FOOT)]}
f = "sns-publish-throttle-us-east-1"
P[f] = {"claim": "In the SNS Publish API throttling table, US East (N. Virginia) has 30,000 messages per second for standard topics and 30,000 messages per second for FIFO topics; SNS FIFO per-topic limits exceed this default per-account limit when FifoThroughputScope is set to MessageGroup.",
        "qualifiers": q(f, scope="per account, per Region (US East (N. Virginia))"),
        "evidence": [ev(f, 0), same(f, FOOT)]}

f = "sns-queue-policy-sourcearn-limits-to-one-topic"
P[f] = {"claim": "An SQS queue policy that uses the aws:SourceArn condition restricts access to the queue based on the source of the messages, so that only messages originating from the specified SNS topic are allowed to be delivered to the queue.",
        "evidence": [ev(f, 0, quote="This policy uses the aws:SourceArn condition to restrict access to the SQS queue based on the source of the messages being sent. This ensures that only messages originating from the specified SNS topic (in this case, arn:aws:sns:us-east-2:444455556666:MyTopic) are allowed to be delivered to the queue.")]}

f = "sns-s3-publish-needs-topic-policy-for-s3-principal"
P[f] = {"claim": "To allow an S3 bucket from another AWS account to publish event notifications to your SNS topic, you configure the topic's access policy: the policy should grant the Amazon S3 service (s3.amazonaws.com) the permissions to publish to the topic, and the SourceAccount condition ensures that only the specified AWS account, which owns the bucket, can publish notifications to the topic.",
        "qualifiers": q(f, scope="SNS topic access policy, S3 event notifications from a bucket in another account"),
        "evidence": [same(f, "To allow an Amazon S3 bucket from another AWS account to publish event notifications to your Amazon SNS topic, you need to configure the topic's access policy accordingly."), ev(f, 0)]}

f = "sns-vpc-endpoint-publish-without-public-internet"
P[f] = {"claim": "If you use Amazon VPC to host your AWS resources, you can create a private connection between your VPC and SNS, and with this connection you can publish messages to SNS topics without sending them through the public internet.",
        "evidence": [ev(f, 0, quote="If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can create a private connection between your VPC and Amazon SNS. With this connection, you can publish messages to your Amazon SNS topics without sending them through the public internet.")]}

f = "sns-vpc-interface-endpoint-no-igw-nat-vpn"
P[f] = {"evidence": [ev(f, 0, quote="To connect your VPC to Amazon SNS, you define an interface VPC endpoint. This type of endpoint connects your VPC to AWS services. The endpoint provides reliable, scalable connectivity to Amazon SNS. It doesn't require an internet gateway, network address translation (NAT) instance, or VPN connection.")]}

# --- SQS ---
f = "sqs-buffered-client-with-long-polling-minimizes-requests"
P[f] = {"evidence": [ev(f, 0, quote="Client-Side Buffering and Long Polling: Combine client-side buffering with request batching by using long polling together with the buffered asynchronous client included with the AWS SDK for Java. This approach helps to minimize the number of requests and optimizes the handling of large volumes of messages."), ev(f, 1)]}

f = "sqs-case-migros-one-eks-microservices"
P[f] = {"claim": "Migros One's microservices architecture is deployed on Amazon EKS, and it uses Amazon SQS, fully managed message queuing for microservices, distributed systems and serverless applications (customer case study)."}

f = "sqs-change-dlq-redrive-api-2023"
P[f] = {"claim": "On June 7, 2023 SQS added dead-letter queue redrive using the SQS APIs: the StartMessageMoveTask, ListMessageMoveTasks and CancelMessageMoveTask actions configure a redrive. The documentation history row of November 10, 2021 says SQS supports dead-letter queue redrive for standard queues."}

f = "sqs-change-fifo-dlq-redrive-2023"
P[f] = {"claim": "SQS added dead-letter queue redrive for FIFO queues. Before, SQS supported redriving messages from a standard dead-letter queue to standard source queues or a standard custom destination queue; now customers can also redrive messages from a FIFO dead-letter queue to FIFO source queues or FIFO custom destination queues. If the dead-letter queue is a FIFO queue, the redrive destination queue must be a FIFO queue as well.",
        "values": vals(("fifo", "must be a FIFO queue as well"), ("now", "FIFO custom destination queues")),
        "evidence": [ev(f, 0), same(f, "Now SQS customers can also redrive messages from a FIFO dead-letter queue to FIFO source queues or FIFO custom destination queues."), ev(f, 1)]}

f = "sqs-change-sendmessage-needs-only-generatedatakey-2024"
P[f] = {"claim": "The SQS documentation history row of July 24, 2024 says that SQS no longer requires the kms:Decrypt permission for the SendMessage API and that customers only need kms:GenerateDataKey on the KMS key (but still need kms:Decrypt to call ReceiveMessage). The current key-management page still says that the producer must have the kms:Decrypt and kms:GenerateDataKey permissions for the KMS key.",
        "values": vals(("date", "July 24, 2024"), ("send", "only need the kms:GenerateDataKey permission"), ("receive", "still need kms:Decrypt permission to call ReceiveMessage"), ("current", "the producer must have the kms:Decrypt and kms:GenerateDataKey permissions")),
        "qualifiers": q(f, condition=""),
        "note": "AWS pages disagree: the 2024 history row versus the current producer section of sqs-key-management. Teach: grant a producer both kms:GenerateDataKey and kms:Decrypt (see sqs-faq-sse-producer-needs-generatedatakey-and-decrypt).",
        "evidence": [ev(f, 0), new(sqsg("sqs-key-management"), "When the data key reuse period expires, the producer's next call to SendMessage or SendMessageBatch also triggers calls to kms:Decrypt and kms:GenerateDataKey. The call to kms:Decrypt is to verify the integrity of the new data key before using it. Therefore, the producer must have the kms:Decrypt and kms:GenerateDataKey permissions for the KMS key.")]}

f = "sqs-copies-on-multiple-servers-cause-duplicates"
P[f] = {"evidence": [same(f, "Amazon SQS stores copies of your messages on multiple servers for redundancy and high availability. On rare occasions, one of the servers that stores a copy of a message might be unavailable when you receive or delete a message."), ev(f, 0)]}

f = "sqs-decision-combine-buffer-for-consumers"
P[f] = {"claim": "The integration decision guide lists, among a few common ways AWS customers use a combination of services, routing EventBridge or SNS events to an SQS queue as a buffer for downstream consumers.",
        "evidence": [same(f, "If you are using purpose-built services, a combination of services might be the best fit for your use case. The following lists out a few common ways AWS customers are using a combination of services."), ev(f, 0)]}

f = "sqs-delay-queue-range"
P[f] = {"claim": "If you create an SQS delay queue, messages that you send to the queue remain invisible to consumers for the delay period; the default (minimum) delay for a queue is 0 seconds and the maximum is 15 minutes.",
        "qualifiers": q(f, condition=""),
        "evidence": [new(sqsg("sqs-delay-queues"), "If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period. The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes.")]}

RAP = "The redrive allow policy specifies which source queues can access the dead-letter queue. You can choose whether to allow all source queues, allow specific source queues, or deny all source queues use of the dead-letter queue."
f = "sqs-dlq-denyall-blocks-use-as-dlq"
P[f] = {"claim": "The redrive allow policy specifies which source queues can access a dead-letter queue; if you specify denyAll, the queue cannot be used as a dead-letter queue.",
        "evidence": [same(f, RAP), ev(f, 0)]}
f = "sqs-dlq-redrive-allow-by-queue-max-10"
P[f] = {"claim": "In a redrive allow policy, which specifies which source queues can access the dead-letter queue, the byQueue option can specify up to 10 source queues, each by its Amazon Resource Name (ARN).",
        "qualifiers": q(f, condition=""),
        "evidence": [same(f, RAP), ev(f, 0)]}
f = "sqs-dlq-redrive-allow-policy-default-allow-all"
P[f] = {"evidence": [ev(f, 0, quote=RAP + " The default allows all source queues to use the dead-letter queue.")]}

f = "sqs-eventbridge-scheduler-for-advanced-scheduling"
P[f] = {"claim": "SQS delay queues and message timers allow scheduling of message delivery up to 15 minutes in the future. For more flexible scheduling, EventBridge Scheduler, which can schedule one-time or recurring API actions without time limitations, is the recommended solution for advanced message scheduling use cases.",
        "hard": True, "question": "What does AWS recommend when SQS delay queues and message timers (up to 15 minutes) are not enough for scheduling?",
        "values": vals(("service", "EventBridge Scheduler is the recommended solution"), ("use-case", "advanced message scheduling use cases"), ("limit", "up to 15 minutes in the future")),
        "qualifiers": q(f, condition=""),
        "evidence": [ev(f, 0, quote="While Amazon SQS delay queues and message timers allow scheduling of message delivery up to 15 minutes in the future, you may require more flexible scheduling capabilities. In such cases, consider using EventBridge Scheduler, which enables you to schedule billions of one-time or recurring API actions without time limitations. EventBridge Scheduler is the recommended solution for advanced message scheduling use cases.")]}

f = "sqs-faq-dlq-redrive-policy-max-receive-count"
P[f] = {"evidence": [ev(f, 0, quote="When you create your source queue, Amazon SQS allows you to specify a dead-letter queue (DLQ) and the condition under which SQS should move messages to the DLQ. The condition is the number of times a consumer can receive a message from the queue, defined as maxReceiveCount. This configuration of a dead-letter queue with a source queue and the maxReceiveCount is known as the redrive policy.")]}

f = "sqs-faq-maximum-message-size-attribute-range"
P[f] = {"evidence": [ev(f, 0, quote="To configure the maximum message size, use the console or the SetQueueAttributes method to set the MaximumMessageSize attribute. This attribute specifies the number of bytes that an Amazon SQS message can contain. Set this attribute to a value between 1,024 bytes (1 KiB), and 1,048,576 bytes (1 MiB).")]}

f = "sqs-faq-only-account-owner-or-delegate-can-operate-queue"
P[f] = {"claim": "Only an AWS account owner, or an AWS account that the owner has delegated rights to, can perform operations on an Amazon SQS message queue. An access policy can also be configured to allow anonymous users to access a message queue.",
        "values": vals(("v1", "Only an AWS account owner"), ("v2", "delegated rights"), ("anon", "allows anonymous users to access a message queue")),
        "evidence": [ev(f, 0), same(f, "Yes. You can configure an access policy that allows anonymous users to access a message queue.")]}

f = "sqs-faq-permissions-api-no-conditional-access"
P[f] = {"claim": "The SQS permissions API provides an interface for sharing access to a message queue with developers, but it cannot allow conditional access or more advanced use cases.",
        "values": vals(("v1", "cannot allow conditional access")),
        "qualifiers": q(f, scope="SQS permissions API"),
        "evidence": [ev(f, 0, quote="The permissions API provides an interface for sharing access to a message queue to developers. However, this API cannot allow conditional access or more advanced use cases.")]}

f = "sqs-faq-queues-are-independent-per-region"
P[f] = {"evidence": [ev(f, 0, heading="Can I share messages between queues in different regions?")]}

f = "sqs-faq-retention-default-4-days"
P[f] = {"claim": "The default Amazon SQS message retention period is 4 days; you can configure it to a value from 1 minute to 14 days.",
        "evidence": [ev(f, 0, quote="You can configure the Amazon SQS message retention period to a value from 1 minute to 14 days. The default is 4 days.")]}

f = "sqs-faq-sdk-default-20-second-long-poll"
P[f] = {"claim": "All AWS SDKs work with 20-second long polls by default. If you don't use an AWS SDK, or if you configured your SDK to have a shorter timeout, you might need to modify your SQS client to allow longer requests or to use a shorter long-poll timeout.",
        "kind": "behavior",
        "qualifiers": {"scope": "SQS clients (AWS SDKs and other clients)", "default_or_max": "", "adjustable": False, "condition": ""},
        "evidence": [ev(f, 0, quote="All AWS SDKs work with 20-second long polls by default. If you don't use an AWS SDK to access Amazon SQS, or if you configured your AWS SDK to specifically have a shorter timeout, you might need to modify your Amazon SQS client to allow longer requests or to use a shorter long-poll timeout.")]}

f = "sqs-fifo-3000-is-300-calls-of-10"
P[f] = {"claim": "If you use batching, non-high throughput FIFO queues support up to 3,000 messages per second, per API action; the 3,000 messages per second represent 300 API calls, each with a batch of 10 messages.",
        "evidence": [ev(f, 0, quote="If you use batching, non-high throughput FIFO queues support up to 3,000 messages per second, per API action (SendMessage, ReceiveMessage, and DeleteMessage). The 3,000 messages per second represent 300 API calls, each with a batch of 10 messages.")]}

f = "sqs-fifo-ht-other-regions-2400-tps"
P[f] = {"claim": "For SQS FIFO queues in high throughput mode, with non-batched API calls, all other AWS Regions have a default throughput of 2,400 TPS.",
        "evidence": [ev(f, 0, quote="All other AWS Regions: Default throughput of 2,400 TPS."), same(f, "Amazon SQS FIFO limits are based on the number of API requests, not message limits. For high throughput mode, these API request limits are as follows:")]}

f = "sqs-fifo-ht-top-regions-70000-tps"
P[f] = {"claim": "For SQS FIFO queues in high throughput mode, with non-batched API calls, US East (N. Virginia), US West (Oregon) and Europe (Ireland) support up to 70,000 transactions per second (TPS).",
        "evidence": [ev(f, 0, quote="US East (N. Virginia), US West (Oregon), and Europe (Ireland): Up to 70,000 transactions per second (TPS)."), same(f, "Amazon SQS FIFO limits are based on the number of API requests, not message limits. For high throughput mode, these API request limits are as follows:")]}

f = "sqs-fifo-ht-top-regions-batched-700000"
P[f] = {"claim": "For SQS FIFO queues in high throughput mode, with batched API calls, US East (N. Virginia), US West (Oregon) and Europe (Ireland) support up to 700,000 messages per second, which is 10x the non-batch limit of 70,000 TPS.",
        "evidence": [ev(f, 0, quote="US East (N. Virginia), US West (Oregon), and Europe (Ireland): Up to 700,000 messages per second (10x the non-batch limit of 70,000 TPS)."), same(f, "Amazon SQS FIFO limits are based on the number of API requests, not message limits. For high throughput mode, these API request limits are as follows:")]}

f = "sqs-fifo-partition-throughput-3000-batched-300-single"
P[f] = {"qualifiers": q(f, condition="")}

f = "sqs-horizontal-scaling-linear-gain"
P[f] = {"claim": "Scale SQS producers and consumers horizontally by adding more instances of each, and use action batching to send or receive multiple messages in a single request, reducing API call overhead. When you add more clients, you achieve essentially linear gains in queue throughput."}

f = "sqs-in-flight-fifo-limit"
P[f] = {"qualifiers": q(f, condition="You can request an increase beyond this limit by contacting AWS Support."),
        "evidence": [ev(f, 0, quote="FIFO queues support a maximum of 120,000 in-flight messages (messages received by a consumer but not yet deleted). If this limit is reached, Amazon SQS does not return an error, but processing may be impacted. You can request an increase beyond this limit by contacting AWS Support.")]}

f = "sqs-in-flight-standard-limit"
P[f] = {"qualifiers": q(f, condition="Depends on queue traffic and message backlog; to request a quota increase, submit a support request."),
        "evidence": [ev(f, 0), same(f, "To request a quota increase, submit a support request.")]}

f = "sqs-kms-aws-managed-key-unique-per-account-region"
P[f] = {"claim": "You can use the AWS managed KMS key for Amazon SQS, which is unique for each account and Region."}

f = "sqs-kms-service-senders-need-customer-managed-key"
P[f] = {"claim": "Several AWS services act as event sources that can send events to SQS queues. To allow these event sources to work with encrypted queues, you must create a customer managed KMS key and add permissions in the key policy for the service to use the required AWS KMS API methods.",
        "evidence": [ev(f, 0, quote="Several AWS services act as event sources that can send events to Amazon SQS queues. To allow these event sources to work with encrypted queues, you must create a customer managed KMS key and add permissions in the key policy for the service to use the required AWS KMS API methods.")]}

f = "sqs-long-polling-max-wait"
P[f] = {"claim": "When the wait time for the ReceiveMessage API action is greater than 0, long polling is in effect; the maximum long polling wait time is 20 seconds.",
        "evidence": [new(sqsg("sqs-short-and-long-polling"), "When the wait time for the ReceiveMessage API action is greater than 0, long polling is in effect. The maximum long polling wait time is 20 seconds.")]}

f = "sqs-long-polling-min-wait-1-second"
P[f] = {"qualifiers": q(f, condition="")}

f = "sqs-policy-quota-bytes"
P[f] = {"claim": "The maximum size of an Amazon SQS policy is 8,192 bytes.",
        "qualifiers": q(f, scope="per SQS policy", condition=""),
        "evidence": [new(sqsg("quotas-policies"), "The following table lists quotas related to policies."),
                     new(sqsg("quotas-policies"), "| Bytes | 8,192 |", table_header="| Name | Maximum |"), ev(f, 0)]}

f = "sqs-pricing-free-tier-1-million-requests"
P[f] = {"qualifiers": q(f, scope="per month, all customers", condition="")}

f = "sqs-pricing-free-tier-no-rollover"
P[f] = {"evidence": [ev(f, 0, quote="Your usage of the free tier is calculated each month across all regions (except the GovCloud region) and is applied to your bill automatically. Unused free usage does not roll over to the next month.")]}

f = "sqs-queue-name-max-length"
P[f] = {"claim": "An SQS queue name can have up to 80 characters; alphanumeric characters, hyphens and underscores are accepted. The name of a FIFO queue must end with the .fifo suffix, and the suffix counts towards the 80-character queue name quota.",
        "qualifiers": q(f, condition="Queue names are case-sensitive."),
        "evidence": [ev(f, 0), new(sqsg("quotas-fifo"), "The name of a FIFO queue must end with the .fifo suffix. The suffix counts towards the 80-character queue name quota.")]}

f = "sqs-short-polling-is-default-immediate-response"
P[f] = {"qualifiers": q(f, condition="")}

f = "sqs-sse-managed-encryption-on-by-default"
P[f] = {"qualifiers": q(f, condition="")}

f = "sqs-visibility-timeout-default"
P[f] = {"qualifiers": q(f, scope="per message", condition="")}

f = "sqs-wa-back-pressure-slow-down-or-stop-incoming-data"
P[f] = {"claim": "Ignoring back pressure: a workload should have the ability to slow down or stop incoming data when a component cannot process it at the same rate.",
        "qualifiers": q(f, scope="Well-Architected reliability pillar, REL04-BP02")}

f = "sqs-wa-loose-coupling-via-intermediate-durable-layer"
P[f] = {"claim": "To further improve resiliency through loose coupling, make component interactions asynchronous where possible: one component generates events and another consumes them, and the two components do not integrate through direct point-to-point interaction but usually through an intermediate durable storage layer, such as an SQS queue, a streaming data platform such as Kinesis, or Step Functions.",
        "evidence": [same(f, "To further improve resiliency through loose coupling, make component interactions asynchronous where possible."),
                     ev(f, 0, quote="It involves one component that generates events and another that consumes them. The two components do not integrate through direct point-to-point interaction but usually through an intermediate durable storage layer, such as an Amazon SQS queue, a streaming data platform such as Amazon Kinesis, or AWS Step Functions.")]}

for fid, p in P.items():
    assert fid in facts, fid
    assert facts[fid]["status"] == "disputed", (fid, facts[fid]["status"])
    with open(os.path.join(OUT, fid + ".json"), "w") as fh:
        json.dump(p, fh, indent=1, ensure_ascii=False)
print(len(P), "patches written")
