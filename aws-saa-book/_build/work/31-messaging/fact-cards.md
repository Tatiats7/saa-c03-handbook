facts card: 550 facts
eventbridge-api-destination-https-endpoint-target
  claim: API destinations are HTTPS endpoints that you can invoke as the target of an event bus rule or a pipe. You can use any HTTP method except CONNECT and TRACE.
  scope: EventBridge API destination.
  link: [HTTPS endpoints that you can invoke](../facts/eventbridge.md#eventbridge-api-destination-https-endpoint-target)
  link: [any HTTP method except CONNECT and TRACE](../facts/eventbridge.md#eventbridge-api-destination-https-endpoint-target)
eventbridge-api-destination-no-mtls
  claim: API destinations do not support mutual TLS (mTLS).
  scope: EventBridge API destination.
  link: [do not support mutual TLS (mTLS)](../facts/eventbridge.md#eventbridge-api-destination-no-mtls)
  link: [API destinations](../facts/eventbridge.md#eventbridge-api-destination-no-mtls)
eventbridge-archive-filter-by-event-pattern
  claim: You can give an archive an event pattern so that only matching events are sent to the archive.
  scope: EventBridge archive.
  link: [specify an event pattern for EventBridge](../facts/eventbridge.md#eventbridge-archive-filter-by-event-pattern)
  link: [filtering the events it sends to the archive](../facts/eventbridge.md#eventbridge-archive-filter-by-event-pattern)
eventbridge-archive-retention-indefinite-by-default
  claim: You can set the number of days to keep events in an archive. By default, EventBridge stores events in an archive indefinitely.
  scope: EventBridge archive; default; adjustable.
  link: [stores events in an archive indefinitely](../facts/eventbridge.md#eventbridge-archive-retention-indefinite-by-default)
  link: [days to retain events in the archive](../facts/eventbridge.md#eventbridge-archive-retention-indefinite-by-default)
eventbridge-archive-single-source-bus-fixed
  claim: Each archive receives events from a single source event bus. You cannot change the source event bus after the archive is created.
  scope: EventBridge archive.
  link: [events from a single source event bus](../facts/eventbridge.md#eventbridge-archive-single-source-bus-fixed)
  link: [cannot change the source event bus](../facts/eventbridge.md#eventbridge-archive-single-source-bus-fixed)
eventbridge-aws-service-events-go-to-default-bus
  claim: When an AWS service in your account sends an event to EventBridge, the event goes to your account's default event bus. AWS services send events on a durable or best-effort basis.
  scope: EventBridge default event bus.
  link: [it goes to your account's default event bus](../facts/eventbridge.md#eventbridge-aws-service-events-go-to-default-bus)
  link: [AWS services send events to EventBridge](../facts/eventbridge.md#eventbridge-aws-service-events-go-to-default-bus)
eventbridge-bus-as-target-same-or-different-account
  claim: A rule can specify another event bus as its target, in the same or a different AWS account.
  scope: EventBridge rule target.
  link: [other event buses as targets for rules](../facts/eventbridge.md#eventbridge-bus-as-target-same-or-different-account)
  link: [in the same or different AWS accounts](../facts/eventbridge.md#eventbridge-bus-as-target-same-or-different-account)
eventbridge-bus-many-sources-to-many-targets
  claim: Event buses route events from multiple sources to multiple destinations, called targets.
  scope: EventBridge event bus.
  link: [route events from multiple sources](../facts/eventbridge.md#eventbridge-bus-many-sources-to-many-targets)
  link: [multiple destinations, or targets](../facts/eventbridge.md#eventbridge-bus-many-sources-to-many-targets)
eventbridge-case-hanwha-qcells-scheduling-jobs
  claim: Hanwha Qcells used Amazon EventBridge for scheduling tasks in its Virtual Power Plant platform, which cut the time to set up jobs from weeks to just a few clicks (customer case study).
  scope: Hanwha Qcells case study.
  link: [streamlined scheduling tasks](../facts/eventbridge.md#eventbridge-case-hanwha-qcells-scheduling-jobs)
  link: [from weeks to just a few clicks](../facts/eventbridge.md#eventbridge-case-hanwha-qcells-scheduling-jobs)
eventbridge-case-legendary-play-fine-grained-rules
  claim: At Legendary Play, a blockchain service consumes all the events in the system to update the chain, and each of its services exists on its own AWS account within the organization (customer case study).
  scope: Legendary Play case study.
  link: [consumes all the events in the system](../facts/eventbridge.md#eventbridge-case-legendary-play-fine-grained-rules)
  link: [its own AWS account within the organization](../facts/eventbridge.md#eventbridge-case-legendary-play-fine-grained-rules)
eventbridge-change-custom-event-bus-classic-rename-2026
  claim: On 2026-09-24 EventBridge relaunched event buses with a new enhanced Custom event bus and renamed the existing bus to Custom event bus - classic. The new bus keeps every event for a retention period of 1 to 365 days and delivers in FIFO order within an event group, per subscriber. Custom Event Bus - Classic remains available, and you can run both products side by side.
  scope: EventBridge custom event buses; not examinable yet: general availability on 2026-09-24 is after 2026-07-15; the exam model is the default bus with rules and up to five targets (Custom Event Bus - Classic).
  link: [2026-09-24](../facts/eventbridge.md#eventbridge-change-custom-event-bus-classic-rename-2026)
  link: [1 to 365 days](../facts/eventbridge.md#eventbridge-change-custom-event-bus-classic-rename-2026)
  link: [Custom event bus - classic](../facts/eventbridge.md#eventbridge-change-custom-event-bus-classic-rename-2026)
eventbridge-change-direct-delivery-cross-account-targets-2025
  claim: On 2025-01-21 EventBridge Event Bus began to deliver events directly to AWS services in another account, without the need for an intermediary EventBridge event bus or Lambda function. It delivers cross-account to targets that support resource-based IAM policies, such as SQS, Lambda, Kinesis Data Streams, SNS and API Gateway.
  scope: EventBridge event bus rules, cross-account targets.
  link: [2025-01-21](../facts/eventbridge.md#eventbridge-change-direct-delivery-cross-account-targets-2025)
  link: [targets that support resource-based IAM policies](../facts/eventbridge.md#eventbridge-change-direct-delivery-cross-account-targets-2025)
eventbridge-change-event-size-1mb-2026
  claim: On 2026-01-29 EventBridge increased the event payload size from 256 KB to 1 MB. The PutEvents page now says the total request size must be less than 1 MB (1,048,576 bytes). The announcement says the feature is available in all commercial Regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Taipei) and Mexico (Central).
  scope: per PutEvents request (sum of all entries); maximum; event buses; not available in five listed Regions.
  link: [1 MB (1,048,576 bytes)](../facts/eventbridge.md#eventbridge-change-event-size-1mb-2026)
  link: [256 KB](../facts/eventbridge.md#eventbridge-change-event-size-1mb-2026)
  link: [2026-01-29](../facts/eventbridge.md#eventbridge-change-event-size-1mb-2026)
  changed: 2026-01-29: was 256 KB
eventbridge-change-scheduler-launch-2022
  claim: The EventBridge Scheduler User Guide had its initial release on November 10, 2022, and the EventBridge Pipes documentation was launched on December 1, 2022.
  scope: EventBridge Scheduler and Pipes documentation history.
  link: [November 10, 2022](../facts/eventbridge.md#eventbridge-change-scheduler-launch-2022)
  link: [December 1, 2022](../facts/eventbridge.md#eventbridge-change-scheduler-launch-2022)
eventbridge-change-targets-sqs-fair-queues-2025
  claim: On 2025-11-13 EventBridge began to support SQS fair queues as targets. The post says to be sure to include a MessageGroupID parameter, which can be specified with either a static value or JSON path expression.
  scope: EventBridge rule targets; the post says support for fair queue and FIFO targets is available in all AWS commercial and AWS GovCloud (US) Regions.
  link: [2025-11-13](../facts/eventbridge.md#eventbridge-change-targets-sqs-fair-queues-2025)
  link: [include a MessageGroupID parameter](../facts/eventbridge.md#eventbridge-change-targets-sqs-fair-queues-2025)
eventbridge-classic-bus-does-not-retain-events
  claim: Custom Event Bus - Classic does not retain events. To keep events you add an archive.
  scope: EventBridge Custom Event Bus - Classic.
  link: [Not retained. To keep events, add an archive.](../facts/eventbridge.md#eventbridge-classic-bus-does-not-retain-events)
  link: [Retention](../facts/eventbridge.md#eventbridge-classic-bus-does-not-retain-events)
eventbridge-classic-bus-no-ordered-delivery
  claim: Ordering is not available on Custom Event Bus - Classic, the bus type that uses rules and targets; on the Custom Event Bus, ordering is FIFO delivery within an event group, per subscriber.
  scope: EventBridge Custom Event Bus - Classic.
  link: [Ordering](../facts/eventbridge.md#eventbridge-classic-bus-no-ordered-delivery)
  link: [Not available.](../facts/eventbridge.md#eventbridge-classic-bus-no-ordered-delivery)
eventbridge-cloudtrail-events-default-bus-only
  claim: All CloudTrail events are delivered to the default event bus only. To process them on a Classic custom bus, create a rule on the default bus that forwards matching events to it.
  scope: EventBridge, CloudTrail events.
  link: [delivered to the default event bus only](../facts/eventbridge.md#eventbridge-cloudtrail-events-default-bus-only)
  link: [forwards matching events to your Classic custom bus](../facts/eventbridge.md#eventbridge-cloudtrail-events-default-bus-only)
eventbridge-cloudtrail-events-need-trail-logging
  claim: To record EventBridge events with one of the CloudTrail detail-type values, you must enable a CloudTrail trail with logging.
  scope: EventBridge, CloudTrail events.
  link: [you must enable a CloudTrail trail with logging](../facts/eventbridge.md#eventbridge-cloudtrail-events-need-trail-logging)
eventbridge-cloudwatch-logs-target-no-rolearn
  claim: For CloudWatch Logs targets, do not specify a RoleArn in the target configuration.
  scope: EventBridge rule target.
  link: [do not specify a RoleArn](../facts/eventbridge.md#eventbridge-cloudwatch-logs-target-no-rolearn)
  link: [Amazon CloudWatch Logs targets](../facts/eventbridge.md#eventbridge-cloudwatch-logs-target-no-rolearn)
eventbridge-comparison-operators-leaf-nodes-only
  claim: EventBridge comparison operators only work on leaf nodes of the event, except $or and anything-but.
  scope: EventBridge event pattern.
  link: [only work on leaf nodes](../facts/eventbridge.md#eventbridge-comparison-operators-leaf-nodes-only)
  link: [with the exception of $or and anything-but](../facts/eventbridge.md#eventbridge-comparison-operators-leaf-nodes-only)
eventbridge-cross-account-events-not-forwarded-again
  claim: A receiver account cannot forward events it received from a sender account on to a third account: those events are not sent to the third account. The same holds for chaining three event buses inside one account.
  scope: EventBridge event bus to event bus delivery.
  link: [events are not sent to the third account](../facts/eventbridge.md#eventbridge-cross-account-events-not-forwarded-again)
  link: [are not sent to the third event bus](../facts/eventbridge.md#eventbridge-cross-account-events-not-forwarded-again)
eventbridge-cross-account-new-bus-targets-need-iam-role
  claim: EventBridge requires all new cross-account event bus targets to add IAM roles. This applies to event bus targets created after March 2, 2023.
  scope: EventBridge cross-account event bus target; targets created after March 2, 2023.
  link: [all new cross account event bus targets](../facts/eventbridge.md#eventbridge-cross-account-new-bus-targets-need-iam-role)
  link: [created after March 2, 2023](../facts/eventbridge.md#eventbridge-cross-account-new-bus-targets-need-iam-role)
eventbridge-cross-account-receiver-edits-bus-permissions
  claim: To receive events from other accounts or organizations, you must first edit the permissions on the event bus that receives them. With AWS Organizations you can name an organization and grant access to all its accounts.
  scope: EventBridge event bus, cross-account.
  link: [edit the permissions on the event bus](../facts/eventbridge.md#eventbridge-cross-account-receiver-edits-bus-permissions)
  link: [grant access to all accounts](../facts/eventbridge.md#eventbridge-cross-account-receiver-edits-bus-permissions)
eventbridge-cross-account-sender-pays-as-custom-events
  claim: Events sent from one account to another are charged to the sending account as custom events. The receiving account is not charged.
  scope: EventBridge cross-account delivery.
  link: [charged to the sending account as custom events](../facts/eventbridge.md#eventbridge-cross-account-sender-pays-as-custom-events)
  link: [The receiving account is not charged](../facts/eventbridge.md#eventbridge-cross-account-sender-pays-as-custom-events)
eventbridge-cross-region-send-and-receive
  claim: You can configure EventBridge to send and receive events between AWS Regions, by making an event bus in another Region the target of a rule.
  scope: EventBridge event bus, cross-Region.
  link: [send and receive events between AWS Regions](../facts/eventbridge.md#eventbridge-cross-region-send-and-receive)
  link: [bus in another AWS Region as a target](../facts/eventbridge.md#eventbridge-cross-region-send-and-receive)
eventbridge-custom-bus-your-own-events
  claim: You can create additional event buses, called custom event buses, and specify which events they receive. This page describes the Classic custom event bus.
  scope: EventBridge, Custom Event Bus - Classic.
  link: [called custom event buses](../facts/eventbridge.md#eventbridge-custom-bus-your-own-events)
  link: [specify which events they receive](../facts/eventbridge.md#eventbridge-custom-bus-your-own-events)
eventbridge-decision-content-filtering
  claim: EventBridge supports advanced event pattern matching and content-based filtering, so events can be processed and routed in a fine-grained way based on event content.
  scope: Amazon EventBridge, in the SNS, SQS or EventBridge decision guide.
  link: [advanced event pattern matching](../facts/eventbridge.md#eventbridge-decision-content-filtering)
  link: [content-based filtering](../facts/eventbridge.md#eventbridge-decision-content-filtering)
eventbridge-decision-events-category-decouple-publishers-subscribers
  claim: In the integration decision guide's Choose table, the row whose associated services are Amazon EventBridge and Amazon SNS is for when you need to decouple publishers and subscribers and send events to multiple subscribers simultaneously, and it is optimized for asynchronous, loosely coupled communication between publishers and subscribers.
  scope: application integration decision guide.
  link: [decouple publishers and subscribers](../facts/eventbridge.md#eventbridge-decision-events-category-decouple-publishers-subscribers)
  link: [asynchronous, loosely coupled communication](../facts/eventbridge.md#eventbridge-decision-events-category-decouple-publishers-subscribers)
eventbridge-decision-no-ordering
  claim: EventBridge gives no message ordering guarantee: it delivers events to targets in an arbitrary order.
  scope: Amazon EventBridge, in the SNS, SQS or EventBridge decision guide.
  link: [does not provide message ordering guarantees](../facts/eventbridge.md#eventbridge-decision-no-ordering)
  link: [arbitrary order](../facts/eventbridge.md#eventbridge-decision-no-ordering)
eventbridge-decision-no-persistence-at-least-once
  claim: EventBridge processes events in real time and does not persist them. It guarantees at-least-once delivery to targets, so events may be delivered more than once.
  scope: Amazon EventBridge, in the SNS, SQS or EventBridge decision guide.
  link: [doesn't persist events](../facts/eventbridge.md#eventbridge-decision-no-persistence-at-least-once)
  link: [At-least-once delivery is guaranteed to targets](../facts/eventbridge.md#eventbridge-decision-no-persistence-at-least-once)
eventbridge-decision-pipes-stream-or-queue-to-bus
  claim: A common combination is to pull events straight from a stream (Kinesis Data Streams or Amazon MSK) or a queue (SQS or Amazon MQ) with EventBridge Pipes and send them to an EventBridge bus that pushes them out to consumers.
  scope: application integration decision guide.
  link: [with EventBridge Pipes](../facts/eventbridge.md#eventbridge-decision-pipes-stream-or-queue-to-bus)
  link: [sending events to an EventBridge bus](../facts/eventbridge.md#eventbridge-decision-pipes-stream-or-queue-to-bus)
eventbridge-decision-rule-routing
  claim: EventBridge uses an event-driven model: it matches events against rules and delivers them to targets such as AWS services, integrated SaaS applications and custom applications.
  scope: Amazon EventBridge, in the SNS, SQS or EventBridge decision guide.
  link: [matches events against rules](../facts/eventbridge.md#eventbridge-decision-rule-routing)
  link: [integrated SaaS applications](../facts/eventbridge.md#eventbridge-decision-rule-routing)
  say: matches events against rules
eventbridge-decision-scheduling-category
  claim: For scheduling, the integration decision guide names Amazon EventBridge: use scheduling to automate routine tasks that run at specific times or intervals, with built-in retry logic.
  scope: application integration decision guide.
  link: [automate routine tasks](../facts/eventbridge.md#eventbridge-decision-scheduling-category)
  link: [reliable, time-based tasks with built-in retry logic](../facts/eventbridge.md#eventbridge-decision-scheduling-category)
eventbridge-decision-typical-use
  claim: EventBridge suits event-driven architectures, real-time stream processing and cross-account event sharing.
  scope: Amazon EventBridge, in the SNS, SQS or EventBridge decision guide.
  link: [building event-driven architectures](../facts/eventbridge.md#eventbridge-decision-typical-use)
  link: [cross-account event sharing](../facts/eventbridge.md#eventbridge-decision-typical-use)
eventbridge-default-bus-accepts-one-account-only
  claim: By default, the default event bus in your account only allows events from one account. A resource-based policy attached to the bus can allow other accounts to call PutEvents, PutRule and PutTargets.
  scope: EventBridge default event bus; default; adjustable.
  link: [only allows events from one account](../facts/eventbridge.md#eventbridge-default-bus-accepts-one-account-only)
  link: [attaching a resource-based policy to it](../facts/eventbridge.md#eventbridge-default-bus-accepts-one-account-only)
eventbridge-default-bus-receives-aws-service-events
  claim: Every account has a default event bus that automatically receives events from AWS services.
  scope: per account, per Region.
  link: [default event bus](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events)
  link: [automatically receives events from AWS services](../facts/eventbridge.md#eventbridge-default-bus-receives-aws-service-events)
eventbridge-dlq-api-needs-manual-queue-policy
  claim: For a dead-letter queue (DLQ) of an EventBridge rule target: if you add a target to a rule using the console and choose an SQS queue in the same account, a resource-based policy that grants EventBridge access to the queue is attached to the queue for you; if you use the PutTargets operation of the EventBridge API and choose an SQS queue in the same account, you must manually grant permissions to the queue.
  scope: EventBridge dead-letter queue (SQS queue in the same account).
  link: [is attached to the queue for you](../facts/eventbridge.md#eventbridge-dlq-api-needs-manual-queue-policy)
  link: [you must manually grant permissions to the queue](../facts/eventbridge.md#eventbridge-dlq-api-needs-manual-queue-policy)
eventbridge-dlq-fifo-not-supported
  claim: Only standard SQS queues are supported as an EventBridge dead-letter queue. You cannot use a FIFO queue.
  scope: EventBridge rule target dead-letter queue.
  link: [Only standard queues are supported](../facts/eventbridge.md#eventbridge-dlq-fifo-not-supported)
  link: [can't use a FIFO queue for a DLQ](../facts/eventbridge.md#eventbridge-dlq-fifo-not-supported)
eventbridge-dlq-is-standard-sqs-queue
  claim: EventBridge dead-letter queues are standard SQS queues that EventBridge uses to store events that could not be delivered to a target.
  scope: EventBridge rule target.
  link: [standard Amazon SQS queues](../facts/eventbridge.md#eventbridge-dlq-is-standard-sqs-queue)
  link: [events that couldn't successfully be delivered](../facts/eventbridge.md#eventbridge-dlq-is-standard-sqs-queue)
eventbridge-dlq-queue-same-region-as-rule
  claim: The SQS queue used as a dead-letter queue must be in the same Region in which you create the rule.
  scope: EventBridge rule target dead-letter queue.
  link: [must be in the same Region](../facts/eventbridge.md#eventbridge-dlq-queue-same-region-as-rule)
  link: [in which you create the rule](../facts/eventbridge.md#eventbridge-dlq-queue-same-region-as-rule)
eventbridge-event-can-match-several-rules-or-none
  claim: An event might match several rules, and each rule can specify up to five targets. If an event matches no rule, EventBridge takes no action.
  scope: EventBridge event bus.
  link: [An event might match multiple rules](../facts/eventbridge.md#eventbridge-event-can-match-several-rules-or-none)
  link: [EventBridge takes no action](../facts/eventbridge.md#eventbridge-event-can-match-several-rules-or-none)
eventbridge-event-pattern-matches-or-not
  claim: An event pattern has the same structure as the events it matches. An event pattern either matches an event or it does not.
  scope: EventBridge event pattern.
  link: [same structure as the events they match](../facts/eventbridge.md#eventbridge-event-pattern-matches-or-not)
  link: [either matches an event or it doesn't](../facts/eventbridge.md#eventbridge-event-pattern-matches-or-not)
eventbridge-events-are-json-with-same-top-level-fields
  claim: EventBridge events are JSON objects. They all have a similar structure and the same top-level fields.
  scope: EventBridge event.
  link: [represented as JSON objects](../facts/eventbridge.md#eventbridge-events-are-json-with-same-top-level-fields)
  link: [the same top-level fields](../facts/eventbridge.md#eventbridge-events-are-json-with-same-top-level-fields)
eventbridge-faq-api-destination-connection-stores-secret-in-secrets-manager
  claim: Each API destination uses a Connection that defines the authorization method and credentials. Creating a connection creates a secret in AWS Secrets Manager to store the authorization information securely.
  scope: per connection.
  link: [authorization method and credentials](../facts/eventbridge.md#eventbridge-faq-api-destination-connection-stores-secret-in-secrets-manager)
  link: [secret on AWS Secrets Manager](../facts/eventbridge.md#eventbridge-faq-api-destination-connection-stores-secret-in-secrets-manager)
eventbridge-faq-api-destination-optional-invocation-rate-limit
  claim: For an API destination you can optionally define the invocation rate limit, which is the maximum number of invocations per second to send to the endpoint.
  scope: per API destination.
  link: [invocation rate limit](../facts/eventbridge.md#eventbridge-faq-api-destination-optional-invocation-rate-limit)
  link: [maximum number of invocations per second](../facts/eventbridge.md#eventbridge-faq-api-destination-optional-invocation-rate-limit)
eventbridge-faq-api-destinations-send-events-to-on-premises-or-saas-apps
  claim: API destinations help developers send events back to any on-premises or SaaS application, with control over throughput and authentication.
  scope: per API destination.
  link: [on-premises or SaaS applications](../facts/eventbridge.md#eventbridge-faq-api-destinations-send-events-to-on-premises-or-saas-apps)
  link: [control throughput and authentication](../facts/eventbridge.md#eventbridge-faq-api-destinations-send-events-to-on-premises-or-saas-apps)
eventbridge-faq-can-tag-rules-and-event-buses
  claim: You can tag EventBridge rules and event buses.
  scope: EventBridge resources.
  link: [tag rules and event buses](../facts/eventbridge.md#eventbridge-faq-can-tag-rules-and-event-buses)
  link: [you can tag rules](../facts/eventbridge.md#eventbridge-faq-can-tag-rules-and-event-buses)
eventbridge-faq-cross-account-centralize-events-into-single-bus
  claim: Cross-account events can centralize events from multiple accounts into a single event bus to monitor and audit them, and to keep data in sync between accounts.
  scope: per event bus.
  link: [centralize events from multiple accounts](../facts/eventbridge.md#eventbridge-faq-cross-account-centralize-events-into-single-bus)
  link: [single event bus](../facts/eventbridge.md#eventbridge-faq-cross-account-centralize-events-into-single-bus)
eventbridge-faq-cross-account-target-default-or-other-event-bus
  claim: A target can send events to another account. The target can be the default event bus or any other event bus in that account. These are called cross-account events.
  scope: per rule target.
  link: [cross-account events](../facts/eventbridge.md#eventbridge-faq-cross-account-target-default-or-other-event-bus)
  link: [default event bus or any other event bus](../facts/eventbridge.md#eventbridge-faq-cross-account-target-default-or-other-event-bus)
eventbridge-faq-customers-use-sns-as-rule-target-to-filter-and-fan-out
  claim: A common pattern is to use SNS as a target for an EventBridge rule: the rule filters the events you need and SNS fans them out to multiple endpoints.
  scope: EventBridge and SNS.
  link: [use SNS as a target for their rule](../facts/eventbridge.md#eventbridge-faq-customers-use-sns-as-rule-target-to-filter-and-fan-out)
  link: [fan out to multiple endpoints](../facts/eventbridge.md#eventbridge-faq-customers-use-sns-as-rule-target-to-filter-and-fan-out)
eventbridge-faq-default-quotas-can-be-raised-to-hundreds-of-thousands-events-per-second
  claim: Default EventBridge quotas can be increased to process hundreds of thousands of events per second.
  scope: per Region.
  link: [hundreds of thousands of events per second](../facts/eventbridge.md#eventbridge-faq-default-quotas-can-be-raised-to-hundreds-of-thousands-events-per-second)
  link: [Default EventBridge quotas can be increased](../facts/eventbridge.md#eventbridge-faq-default-quotas-can-be-raised-to-hundreds-of-thousands-events-per-second)
eventbridge-faq-event-bus-many-to-many-pipes-point-to-point
  claim: EventBridge event buses are well suited for many-to-many routing of events between event-driven services. EventBridge Pipes is intended for point-to-point integrations between event publishers and consumers, with support for advanced transformations and enrichments.
  scope: event bus versus Pipes.
  link: [many-to-many routing of events](../facts/eventbridge.md#eventbridge-faq-event-bus-many-to-many-pipes-point-to-point)
  link: [point-to-point integrations](../facts/eventbridge.md#eventbridge-faq-event-bus-many-to-many-pipes-point-to-point)
eventbridge-faq-event-replay-debug-hydrate-targets-recover-from-errors
  claim: Event Replay helps developers debug applications, extend them by hydrating targets with historic events, and recover from errors.
  scope: per archive.
  link: [extend them by hydrating targets with historic events](../facts/eventbridge.md#eventbridge-faq-event-replay-debug-hydrate-targets-recover-from-errors)
  link: [recover from errors](../facts/eventbridge.md#eventbridge-faq-event-replay-debug-hydrate-targets-recover-from-errors)
eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule
  claim: Event Replay lets you reprocess past events back to an event bus or a specific EventBridge rule.
  scope: per archive.
  link: [reprocess past events](../facts/eventbridge.md#eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule)
  link: [specific EventBridge rule](../facts/eventbridge.md#eventbridge-faq-event-replay-reprocesses-past-events-to-bus-or-rule)
eventbridge-faq-eventbridge-json-events-rules-apply-to-entire-event-body
  claim: EventBridge uses a defined JSON-based structure for events, and rules are applied across the entire event body to select events to forward to a target.
  scope: EventBridge versus SNS.
  link: [defined JSON-based structure for events](../facts/eventbridge.md#eventbridge-faq-eventbridge-json-events-rules-apply-to-entire-event-body)
  link: [applied across the entire event body](../facts/eventbridge.md#eventbridge-faq-eventbridge-json-events-rules-apply-to-entire-event-body)
eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners
  claim: EventBridge is the only event-based service that integrates directly with third-party SaaS partners.
  scope: EventBridge versus SNS.
  link: [only event-based service](../facts/eventbridge.md#eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners)
  link: [third-party SaaS partners](../facts/eventbridge.md#eventbridge-faq-eventbridge-only-service-integrating-directly-with-saas-partners)
eventbridge-faq-eventbridge-recommended-for-app-saas-aws-events
  claim: Amazon EventBridge is recommended when you want to build an application that reacts to events from your own applications, SaaS applications, and AWS services.
  scope: EventBridge versus SNS.
  link: [reacts to events from your own applications](../facts/eventbridge.md#eventbridge-faq-eventbridge-recommended-for-app-saas-aws-events)
  link: [SaaS applications, and AWS services](../facts/eventbridge.md#eventbridge-faq-eventbridge-recommended-for-app-saas-aws-events)
eventbridge-faq-global-endpoints-custom-events-only
  claim: Global endpoints are available for custom events only.
  scope: global endpoints.
  link: [available for custom events only](../facts/eventbridge.md#eventbridge-faq-global-endpoints-custom-events-only)
  link: [Global endpoints](../facts/eventbridge.md#eventbridge-faq-global-endpoints-custom-events-only)
eventbridge-faq-global-endpoints-do-not-use-subscriber-metrics-in-health-check
  claim: AWS recommends against including subscriber metrics in the health check of a global endpoint, because one failing subscriber could cause failover although all other subscribers are healthy.
  scope: global endpoints.
  link: [recommend against including subscriber metrics](../facts/eventbridge.md#eventbridge-faq-global-endpoints-do-not-use-subscriber-metrics-in-health-check)
  link: [single subscriber encounters an issue](../facts/eventbridge.md#eventbridge-faq-global-endpoints-do-not-use-subscriber-metrics-in-health-check)
eventbridge-faq-global-endpoints-failover-uses-cloudwatch-alarms-route-53-health-checks
  claim: You configure failover criteria for a global endpoint with Amazon CloudWatch alarms, through Amazon Route 53 health checks, to decide when to fail over and when to route events back to the primary Region.
  scope: global endpoints.
  link: [CloudWatch Alarms (through Amazon Route 53 health checks)](../facts/eventbridge.md#eventbridge-faq-global-endpoints-failover-uses-cloudwatch-alarms-route-53-health-checks)
  link: [route events back to the primary Region](../facts/eventbridge.md#eventbridge-faq-global-endpoints-failover-uses-cloudwatch-alarms-route-53-health-checks)
eventbridge-faq-global-endpoints-no-latency-based-routing
  claim: Global endpoints do not support latency-based routing in the first iteration of the launch.
  scope: global endpoints.
  link: [not supporting latency-based routing](../facts/eventbridge.md#eventbridge-faq-global-endpoints-no-latency-based-routing)
  link: [first iteration of the launch](../facts/eventbridge.md#eventbridge-faq-global-endpoints-no-latency-based-routing)
eventbridge-faq-global-endpoints-replicate-events-across-regions-for-failover
  claim: Global endpoints let you replicate events across primary and secondary Regions to implement failover with minimum data loss, and to fail over automatically to a backup Region during service disruptions.
  scope: global endpoints.
  link: [replicate your events across primary and secondary Regions](../facts/eventbridge.md#eventbridge-faq-global-endpoints-replicate-events-across-regions-for-failover)
  link: [failover automatically to a backup Region](../facts/eventbridge.md#eventbridge-faq-global-endpoints-replicate-events-across-regions-for-failover)
eventbridge-faq-global-endpoints-replication-1-dollar-per-million-events
  claim: Replication for global endpoints costs $1 per million events, which EventBridge charges for cross Region events.
  scope: global endpoints.
  link: [$1 per million events](../facts/eventbridge.md#eventbridge-faq-global-endpoints-replication-1-dollar-per-million-events)
  link: [cross Region events](../facts/eventbridge.md#eventbridge-faq-global-endpoints-replication-1-dollar-per-million-events)
eventbridge-faq-global-endpoints-rto-rpo-360-seconds-max-420
  claim: With global endpoints, if you follow the prescriptive guidance for alarm configuration, the RTO and RPO will be 360 seconds, with a maximum of 420.
  scope: global endpoints; maximum.
  link: [360 seconds](../facts/eventbridge.md#eventbridge-faq-global-endpoints-rto-rpo-360-seconds-max-420)
  link: [maximum of 420](../facts/eventbridge.md#eventbridge-faq-global-endpoints-rto-rpo-360-seconds-max-420)
eventbridge-faq-global-endpoints-suit-idempotent-or-tolerant-applications
  claim: Global endpoints are well suited for applications that do not require idempotency or can handle idempotency across Regions, and for applications that tolerate up to 420 seconds of events not being replicated.
  scope: global endpoints.
  link: [do not require idempotency](../facts/eventbridge.md#eventbridge-faq-global-endpoints-suit-idempotent-or-tolerant-applications)
  link: [up to 420 seconds of events not being replicated](../facts/eventbridge.md#eventbridge-faq-global-endpoints-suit-idempotent-or-tolerant-applications)
eventbridge-faq-global-endpoints-turn-on-replication
  claim: Turn on replication to minimize the data at risk during a service disruption.
  scope: global endpoints.
  link: [Turn on replication](../facts/eventbridge.md#eventbridge-faq-global-endpoints-turn-on-replication)
  link: [data at risk during a service disruption](../facts/eventbridge.md#eventbridge-faq-global-endpoints-turn-on-replication)
eventbridge-faq-lambda-esm-and-pipes-share-polling-infrastructure
  claim: AWS Lambda's event source mapping (ESM) and EventBridge Pipes use the same polling infrastructure to select and send events.
  scope: Lambda ESM versus Pipes.
  link: [same polling infrastructure](../facts/eventbridge.md#eventbridge-faq-lambda-esm-and-pipes-share-polling-infrastructure)
  link: [select and send events](../facts/eventbridge.md#eventbridge-faq-lambda-esm-and-pipes-share-polling-infrastructure)
eventbridge-faq-pipes-can-use-event-bus-as-target
  claim: EventBridge Pipes can use an EventBridge event bus as a target.
  scope: per pipe.
  link: [use an EventBridge event bus as a target](../facts/eventbridge.md#eventbridge-faq-pipes-can-use-event-bus-as-target)
  link: [EventBridge Pipes](../facts/eventbridge.md#eventbridge-faq-pipes-can-use-event-bus-as-target)
eventbridge-faq-pipes-do-not-need-an-event-bus
  claim: EventBridge Pipes can be used independently of existing EventBridge features, so you can receive events from producers such as Kinesis, SQS, or Amazon MSK without using an event bus.
  scope: per pipe.
  link: [used independently of existing EventBridge features](../facts/eventbridge.md#eventbridge-faq-pipes-do-not-need-an-event-bus)
  link: [without needing to use an EventBridge event bus](../facts/eventbridge.md#eventbridge-faq-pipes-do-not-need-an-event-bus)
eventbridge-faq-pipes-maintain-event-order-from-source
  claim: EventBridge Pipes maintains the order of events received from an event source when it sends those events to a destination service.
  scope: per pipe.
  link: [maintain the order of events](../facts/eventbridge.md#eventbridge-faq-pipes-maintain-event-order-from-source)
  link: [destination service](../facts/eventbridge.md#eventbridge-faq-pipes-maintain-event-order-from-source)
eventbridge-faq-pipes-optional-filter-and-enrichment-step
  claim: A pipe can have an optional filtering step that lets only specific source events flow in, and an optional enrichment step that uses AWS Lambda, AWS Step Functions, API destinations, or Amazon API Gateway.
  scope: per pipe.
  link: [optional filtering step](../facts/eventbridge.md#eventbridge-faq-pipes-optional-filter-and-enrichment-step)
  link: [optional enrichment step](../facts/eventbridge.md#eventbridge-faq-pipes-optional-filter-and-enrichment-step)
eventbridge-faq-pipes-point-to-point-with-filtering-and-enrichment
  claim: EventBridge Pipes gives a simpler, consistent, and cost-effective way to create point-to-point integration between event producers and consumers.
  scope: EventBridge Pipes.
  link: [point-to-point integration](../facts/eventbridge.md#eventbridge-faq-pipes-point-to-point-with-filtering-and-enrichment)
  link: [event producers and consumers](../facts/eventbridge.md#eventbridge-faq-pipes-point-to-point-with-filtering-and-enrichment)
eventbridge-faq-pipes-sources-sqs-kinesis-dynamodb-kafka-mq
  claim: EventBridge Pipes supports Amazon SQS, Amazon Kinesis, Amazon DynamoDB, Amazon Managed Streaming Kafka, self-managed Kafka, and Amazon MQ as sources.
  scope: per pipe.
  link: [Amazon SQS, Amazon Kinesis, Amazon DynamoDB](../facts/eventbridge.md#eventbridge-faq-pipes-sources-sqs-kinesis-dynamodb-kafka-mq)
  link: [self-managed Kafka, and Amazon MQ](../facts/eventbridge.md#eventbridge-faq-pipes-sources-sqs-kinesis-dynamodb-kafka-mq)
eventbridge-faq-pipes-vs-lambda-esm
  claim: Lambda event source mapping suits customers who want Lambda as the target to process the events; Pipes suits customers who prefer a managed resource that connects a source to a target without creating, maintaining and scaling Lambda code.
  scope: EventBridge FAQ comparison.
  link: [use Lambda as a target](../facts/eventbridge.md#eventbridge-faq-pipes-vs-lambda-esm)
  link: [creating, maintaining, and scaling Lambda code](../facts/eventbridge.md#eventbridge-faq-pipes-vs-lambda-esm)
eventbridge-faq-publish-custom-application-events-through-api
  claim: You can generate custom application-level events and publish them to EventBridge through the service's API operations.
  scope: Amazon EventBridge.
  link: [custom application-level events](../facts/eventbridge.md#eventbridge-faq-publish-custom-application-events-through-api)
  link: [through the service’s API operations](../facts/eventbridge.md#eventbridge-faq-publish-custom-application-events-through-api)
eventbridge-faq-rule-can-customize-event-before-target
  claim: A rule can customize an event before it is sent to the target, by passing only certain parts or by overwriting it with a constant.
  scope: per rule target.
  link: [customize an event before it is sent](../facts/eventbridge.md#eventbridge-faq-rule-can-customize-event-before-target)
  link: [overwriting it with a constant](../facts/eventbridge.md#eventbridge-faq-rule-can-customize-event-before-target)
eventbridge-faq-rule-matches-events-on-a-bus-and-routes-to-targets
  claim: A rule matches incoming events for a given event bus and routes them to targets for processing.
  scope: per rule.
  link: [matches incoming events for a given event bus](../facts/eventbridge.md#eventbridge-faq-rule-matches-events-on-a-bus-and-routes-to-targets)
  link: [routes them to targets](../facts/eventbridge.md#eventbridge-faq-rule-matches-events-on-a-bus-and-routes-to-targets)
eventbridge-faq-scheduled-rules-remain-scheduler-richer-feature-set
  claim: Scheduled rules will continue to be available, but EventBridge Scheduler offers a richer feature set with more flexibility for creating, executing, and managing schedules.
  scope: Scheduler versus scheduled rules.
  link: [Scheduled rules will continue to be available](../facts/eventbridge.md#eventbridge-faq-scheduled-rules-remain-scheduler-richer-feature-set)
  link: [richer feature set](../facts/eventbridge.md#eventbridge-faq-scheduled-rules-remain-scheduler-richer-feature-set)
eventbridge-faq-scheduler-builds-on-scheduled-rules-adds-time-zones-scale-payloads
  claim: EventBridge Scheduler builds upon the scheduling functionality of Scheduled Rules. It adds support for time zones, increased scale, customized target payloads, added time expressions, and a dashboard for monitoring schedules.
  scope: Scheduler versus scheduled rules.
  link: [support for time zones, increased scale](../facts/eventbridge.md#eventbridge-faq-scheduler-builds-on-scheduled-rules-adds-time-zones-scale-payloads)
  link: [customized target payloads](../facts/eventbridge.md#eventbridge-faq-scheduler-builds-on-scheduled-rules-adds-time-zones-scale-payloads)
eventbridge-faq-scheduler-delete-after-completion-cron-rate-one-time
  claim: Delete upon completion is available for all currently supported scheduling patterns: cron, rate, and one-time schedules.
  scope: per schedule.
  link: [Delete upon completion](../facts/eventbridge.md#eventbridge-faq-scheduler-delete-after-completion-cron-rate-one-time)
  link: [cron, rate, and one-time schedules](../facts/eventbridge.md#eventbridge-faq-scheduler-delete-after-completion-cron-rate-one-time)
eventbridge-faq-scheduler-no-direct-non-aws-targets
  claim: EventBridge Scheduler does not support non-AWS targets directly. You can invoke non-AWS targets using Lambda, ECS and Fargate, or EventBridge API destinations.
  scope: per schedule.
  link: [does not support non-AWS targets directly](../facts/eventbridge.md#eventbridge-faq-scheduler-no-direct-non-aws-targets)
  link: [API destinations feature](../facts/eventbridge.md#eventbridge-faq-scheduler-no-direct-non-aws-targets)
eventbridge-faq-scheduler-schedules-for-any-service-with-api-action
  claim: EventBridge Scheduler can create schedules for any service with an AWS API action.
  scope: EventBridge Scheduler.
  link: [any service with an AWS API action](../facts/eventbridge.md#eventbridge-faq-scheduler-schedules-for-any-service-with-api-action)
  link: [deep integrations with AWS services](../facts/eventbridge.md#eventbridge-faq-scheduler-schedules-for-any-service-with-api-action)
eventbridge-faq-scheduler-serverless-task-scheduler-millions-of-schedules
  claim: Amazon EventBridge Scheduler is a serverless task scheduler that simplifies creating, executing, and managing millions of schedules across AWS services without provisioning or managing underlying infrastructure.
  scope: EventBridge Scheduler.
  link: [serverless task scheduler](../facts/eventbridge.md#eventbridge-faq-scheduler-serverless-task-scheduler-millions-of-schedules)
  link: [millions of schedules across AWS services](../facts/eventbridge.md#eventbridge-faq-scheduler-serverless-task-scheduler-millions-of-schedules)
eventbridge-faq-scheduler-time-zones-adjust-for-daylight-saving
  claim: With EventBridge Scheduler you can choose the time zone a schedule operates in, and the schedule adjusts automatically to Daylight Savings Time and back to standard time.
  scope: per schedule.
  link: [select what time zone a schedule will operate](../facts/eventbridge.md#eventbridge-faq-scheduler-time-zones-adjust-for-daylight-saving)
  link: [automatically adjust to Daylight Savings Time](../facts/eventbridge.md#eventbridge-faq-scheduler-time-zones-adjust-for-daylight-saving)
eventbridge-faq-schedules-created-without-event-bus
  claim: Schedules can be created independently, without the need to create an event bus with a scheduled rule.
  scope: EventBridge Scheduler.
  link: [created independently](../facts/eventbridge.md#eventbridge-faq-schedules-created-without-event-bus)
  link: [without the need to create an event bus](../facts/eventbridge.md#eventbridge-faq-schedules-created-without-event-bus)
eventbridge-faq-schema-discovery-adds-schemas-of-bus-events-automatically
  claim: When schema discovery is enabled for an event bus, the schema of each event sent to the bus is automatically added to the schema registry. If an event's schema changes, a new schema version is created.
  scope: per event bus.
  link: [automatically added to the registry](../facts/eventbridge.md#eventbridge-faq-schema-discovery-adds-schemas-of-bus-events-automatically)
  link: [new version of the schema](../facts/eventbridge.md#eventbridge-faq-schema-discovery-adds-schemas-of-bus-events-automatically)
eventbridge-faq-schema-discovery-free-tier-5m-events-then-10-cents-per-million
  claim: Schema discovery has a free tier of 5 M ingested events per month. Additional usage costs $0.10 per million ingested events.
  scope: schema discovery.
  link: [5 M ingested events per month](../facts/eventbridge.md#eventbridge-faq-schema-discovery-free-tier-5m-events-then-10-cents-per-million)
  link: [$0.10 per million ingested events](../facts/eventbridge.md#eventbridge-faq-schema-discovery-free-tier-5m-events-then-10-cents-per-million)
eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel
  claim: A single rule can route to multiple targets, all of which are processed in parallel.
  scope: per rule.
  link: [route to multiple targets](../facts/eventbridge.md#eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel)
  link: [processed in parallel](../facts/eventbridge.md#eventbridge-faq-single-rule-routes-to-multiple-targets-in-parallel)
eventbridge-faq-sla-monthly-uptime-at-least-99-99-percent
  claim: AWS will use commercially reasonable efforts to make EventBridge available with a Monthly Uptime Percentage for each AWS Region, during any monthly billing cycle, of at least 99.99%.
  scope: per Region, per month; minimum.
  link: [99.99%](../facts/eventbridge.md#eventbridge-faq-sla-monthly-uptime-at-least-99-99-percent)
  link: [Monthly Uptime Percentage](../facts/eventbridge.md#eventbridge-faq-sla-monthly-uptime-at-least-99-99-percent)
eventbridge-faq-typical-latency-about-half-a-second
  claim: The typical latency between sending and receiving an event in EventBridge is about half a second, and it can vary.
  scope: per event.
  link: [about half a second](../facts/eventbridge.md#eventbridge-faq-typical-latency-about-half-a-second)
  link: [Typical latency](../facts/eventbridge.md#eventbridge-faq-typical-latency-about-half-a-second)
eventbridge-faq-what-is-eventbridge-real-time-changes-without-code
  claim: Amazon EventBridge provides real-time access to changes in data in AWS services, your own applications, and software as a service (SaaS) applications without writing code.
  scope: Amazon EventBridge.
  link: [real-time access to changes in data](../facts/eventbridge.md#eventbridge-faq-what-is-eventbridge-real-time-changes-without-code)
  link: [without writing code](../facts/eventbridge.md#eventbridge-faq-what-is-eventbridge-real-time-changes-without-code)
eventbridge-global-endpoints-async-replication-not-simultaneous
  claim: Events are processed in the secondary Region asynchronously, so they are not guaranteed to be processed at the same time in both Regions.
  scope: EventBridge global endpoint.
  link: [processed in the secondary Region asynchronously](../facts/eventbridge.md#eventbridge-global-endpoints-async-replication-not-simultaneous)
  link: [guaranteed to be processed at the same time](../facts/eventbridge.md#eventbridge-global-endpoints-async-replication-not-simultaneous)
eventbridge-global-endpoints-custom-bus-same-name-each-region
  claim: If you use custom buses with global endpoints, you need a custom bus with the same name, in the same account, in each Region for failover to work.
  scope: EventBridge global endpoint with custom buses.
  link: [bus in each Region with the same name](../facts/eventbridge.md#eventbridge-global-endpoints-custom-bus-same-name-each-region)
  link: [same account for failover to work properly](../facts/eventbridge.md#eventbridge-global-endpoints-custom-bus-same-name-each-region)
eventbridge-global-endpoints-failover-to-secondary-region
  claim: With global endpoints you assign a health check to the endpoint. When failover starts, all custom events are routed within minutes to an event bus in the secondary Region. When the health check is healthy again, events are processed by the event bus in the primary Region.
  scope: EventBridge global endpoint; custom events only.
  link: [health check to the endpoint](../facts/eventbridge.md#eventbridge-global-endpoints-failover-to-secondary-region)
  link: [custom events are routed to an event bus](../facts/eventbridge.md#eventbridge-global-endpoints-failover-to-secondary-region)
eventbridge-global-endpoints-replication-needed-for-auto-recovery
  claim: Event replication is required to recover automatically from a failover. Without it, you must manually reset the Route 53 health check to healthy before events go back to the primary Region.
  scope: EventBridge global endpoint; event replication not enabled.
  link: [required to automatically recover from a failover event](../facts/eventbridge.md#eventbridge-global-endpoints-replication-needed-for-auto-recovery)
  link: [manually reset the Route 53 health check](../facts/eventbridge.md#eventbridge-global-endpoints-replication-needed-for-auto-recovery)
eventbridge-input-transformer-edits-event-before-target
  claim: To customize the structure or date of an event before EventBridge passes it to a target, use the input transformer.
  scope: EventBridge rule target.
  link: [use the input transformer](../facts/eventbridge.md#eventbridge-input-transformer-edits-event-before-target)
  link: [before EventBridge passes it to a target](../facts/eventbridge.md#eventbridge-input-transformer-edits-event-before-target)
eventbridge-lens-additional-latency-consider-sns-sqs
  claim: EventBridge can introduce additional latency to the application; if latency is a concern, consider using Amazon SNS and Amazon SQS for event filtering and routing (Serverless Applications Lens).
  scope: Serverless Applications Lens, event-driven architectures.
  link: [EventBridge can introduce additional latency to the application](../facts/eventbridge.md#eventbridge-lens-additional-latency-consider-sns-sqs)
  link: [consider using Amazon SNS and Amazon SQS](../facts/eventbridge.md#eventbridge-lens-additional-latency-consider-sns-sqs)
eventbridge-partner-bus-receives-saas-events
  claim: You can create partner event buses, which receive events from SaaS partners.
  scope: EventBridge partner event bus.
  link: [partner event buses](../facts/eventbridge.md#eventbridge-partner-bus-receives-saas-events)
  link: [receive events from SaaS partners](../facts/eventbridge.md#eventbridge-partner-bus-receives-saas-events)
eventbridge-pattern-anything-but-matching
  claim: Anything-but matching matches anything except what is specified in the rule. It works with strings and numeric values, including lists that contain only strings or only numbers.
  scope: EventBridge event pattern.
  link: [matches anything except what's specified in the rule](../facts/eventbridge.md#eventbridge-pattern-anything-but-matching)
  link: [strings and numeric values](../facts/eventbridge.md#eventbridge-pattern-anything-but-matching)
eventbridge-pattern-exists-matching-leaf-nodes-only
  claim: Exists matching checks for the presence or absence of a field in the event JSON. It only works on leaf nodes, not on intermediate nodes.
  scope: EventBridge event pattern.
  link: [presence or absence of a field](../facts/eventbridge.md#eventbridge-pattern-exists-matching-leaf-nodes-only)
  link: [only works on leaf nodes](../facts/eventbridge.md#eventbridge-pattern-exists-matching-leaf-nodes-only)
eventbridge-pattern-matches-metadata-data-content
  claim: Event patterns for event buses can match against the event source, event metadata, and/or event detail values. Event metadata is data about the event, such as the event source, or the account or Region in which the event originated; event content is the actual property values of the event data.
  scope: EventBridge event pattern.
  link: [event metadata, and/or event detail values](../facts/eventbridge.md#eventbridge-pattern-matches-metadata-data-content)
  link: [such as the event source](../facts/eventbridge.md#eventbridge-pattern-matches-metadata-data-content)
  link: [The actual property values of the event data](../facts/eventbridge.md#eventbridge-pattern-matches-metadata-data-content)
eventbridge-pattern-prefix-and-suffix-matching
  claim: You can match an EventBridge event depending on the prefix or the suffix of a value in the event source; prefix matching and suffix matching work for string values.
  scope: EventBridge event pattern; string values.
  link: [prefix of a value in the event source](../facts/eventbridge.md#eventbridge-pattern-prefix-and-suffix-matching)
  link: [suffix of a value in the event source](../facts/eventbridge.md#eventbridge-pattern-prefix-and-suffix-matching)
eventbridge-pipe-charged-only-for-matching-events
  claim: You are charged only for the events that match the filter of a pipe.
  scope: EventBridge Pipes, per event.
  link: [charged for those events that match the filter](../facts/eventbridge.md#eventbridge-pipe-charged-only-for-matching-events)
  link: [events that match the filter](../facts/eventbridge.md#eventbridge-pipe-charged-only-for-matching-events)
eventbridge-pipe-setup-source-filter-enrichment-target
  claim: To set up a pipe, you choose the source, add optional filtering, define optional enrichment and choose the target.
  scope: EventBridge Pipes.
  link: [choose the source, add optional filtering](../facts/eventbridge.md#eventbridge-pipe-setup-source-filter-enrichment-target)
  link: [define optional enrichment](../facts/eventbridge.md#eventbridge-pipe-setup-source-filter-enrichment-target)
eventbridge-pipe-single-source-single-target
  claim: A pipe routes events from a single source to a single target. It can also filter for specific events and enrich the event data before it is sent to the target.
  scope: EventBridge Pipes.
  link: [from a single source to a single target](../facts/eventbridge.md#eventbridge-pipe-single-source-single-target)
  link: [perform enrichments on the event data](../facts/eventbridge.md#eventbridge-pipe-single-source-single-target)
eventbridge-pipe-to-bus-fans-out-to-many-targets
  claim: To reach multiple targets from one source, create a pipe with an event bus as its target. The pipe sends events to the bus, which sends them on to multiple targets.
  scope: EventBridge Pipes and event buses.
  link: [a pipe with an event bus](../facts/eventbridge.md#eventbridge-pipe-to-bus-fans-out-to-many-targets)
  link: [sends those events on to multiple targets](../facts/eventbridge.md#eventbridge-pipe-to-bus-fans-out-to-many-targets)
eventbridge-pipes-sqs-error-makes-batch-visible-again
  claim: By default, if a pipe has an error while processing a batch from SQS, all messages in that batch become visible in the queue again, so the pipe code must process the same message more than once without side effects.
  scope: EventBridge Pipes with an SQS source; default; batch item failures not reported.
  link: [all messages in that batch become visible](../facts/eventbridge.md#eventbridge-pipes-sqs-error-makes-batch-visible-again)
  link: [process the same message multiple times](../facts/eventbridge.md#eventbridge-pipes-sqs-error-makes-batch-visible-again)
eventbridge-pipes-sqs-polls-and-deletes-on-success
  claim: EventBridge polls the SQS queue and invokes the pipe synchronously with a batch of messages. When the pipe successfully processes the batch, EventBridge deletes the messages from the queue.
  scope: EventBridge Pipes with an SQS source.
  link: [polls the queue and invokes your pipe synchronously](../facts/eventbridge.md#eventbridge-pipes-sqs-polls-and-deletes-on-success)
  link: [EventBridge deletes its messages from the queue](../facts/eventbridge.md#eventbridge-pipes-sqs-polls-and-deletes-on-success)
eventbridge-pipes-sqs-source-standard-and-fifo
  claim: An SQS queue can be a pipe source. EventBridge Pipes support standard queues and first-in, first-out (FIFO) queues.
  scope: EventBridge Pipes source.
  link: [standard queues and first-in, first-out (FIFO) queues](../facts/eventbridge.md#eventbridge-pipes-sqs-source-standard-and-fifo)
  link: [receive records from an Amazon SQS queue](../facts/eventbridge.md#eventbridge-pipes-sqs-source-standard-and-fifo)
eventbridge-pricing-api-destinations-per-million
  claim: In the page's API destinations example, 2M events are charged at $0.20/M, which is $0.40 per month.
  scope: per M (million) API destination invocations, events of 64 KB or less; Worked example on the pricing page..
  link: [$0.20/M](../facts/eventbridge.md#eventbridge-pricing-api-destinations-per-million)
  link: [$0.40 per month](../facts/eventbridge.md#eventbridge-pricing-api-destinations-per-million)
eventbridge-pricing-aws-management-events-free
  claim: On Custom event buses - classic, AWS management events are ingested by the event bus for free (AWS Free Tier).
  scope: Custom event buses - classic; AWS management events ingested by the event bus.
  link: [AWS management events](../facts/eventbridge.md#eventbridge-pricing-aws-management-events-free)
  link: [ingested by the event bus for free](../facts/eventbridge.md#eventbridge-pricing-aws-management-events-free)
eventbridge-pricing-classic-64kb-chunk
  claim: For Custom event buses - Classic, each 64 KB chunk of a payload is billed as one event; for example, an event with a 256 KB payload is billed as 4 events.
  scope: per event payload; Custom event buses - Classic.
  link: [64 KB chunk](../facts/eventbridge.md#eventbridge-pricing-classic-64kb-chunk)
  link: [4 events](../facts/eventbridge.md#eventbridge-pricing-classic-64kb-chunk)
  say: sixty-four kilobyte chunk
eventbridge-pricing-custom-events-per-million
  claim: In the Custom event buses - classic pricing example, the monthly ingestion charge for 10M custom events of 64 KB or less each is 10M * $1.00/M = $10.00 per month.
  scope: Custom event buses - classic; per M (million) custom events ingested, events of 64 KB or less; Worked example in the Custom event buses - classic section of the pricing page..
  link: [$1.00/M](../facts/eventbridge.md#eventbridge-pricing-custom-events-per-million)
  link: [$10.00 per month](../facts/eventbridge.md#eventbridge-pricing-custom-events-per-million)
eventbridge-pricing-delivery-to-bus-vs-same-account-service
  claim: In the Custom event buses - classic pricing example, where custom events published to an event bus in Account A are sent to another event bus in Account B and then to another service in Account B, custom events delivered to another event bus are charged at $1.00/M, and custom events delivered to a service in the same account are charged at $0.00/M.
  scope: Custom event buses - classic; per M (million) custom events delivered, events of 64 KB or less; Worked example: Account A bus to Account B bus, then to a service in Account B..
  link: [$1.00/M](../facts/eventbridge.md#eventbridge-pricing-delivery-to-bus-vs-same-account-service)
  link: [$0.00/M](../facts/eventbridge.md#eventbridge-pricing-delivery-to-bus-vs-same-account-service)
eventbridge-pricing-global-endpoints-no-charge
  claim: On Custom event buses - classic, there is no additional charge for global endpoints; custom events published to the global endpoint are billed according to the custom events pricing.
  scope: Custom event buses - classic; EventBridge global endpoints.
  link: [no additional charge for global endpoints](../facts/eventbridge.md#eventbridge-pricing-global-endpoints-no-charge)
  link: [billed according to the custom events pricing](../facts/eventbridge.md#eventbridge-pricing-global-endpoints-no-charge)
eventbridge-pricing-pipes-64kb-chunk
  claim: For EventBridge Pipes, each 64 KB chunk of payload is billed as one request; for example, a batch of events with a 256 KB payload is billed as four requests.
  scope: per Pipes payload.
  link: [64 KB chunk](../facts/eventbridge.md#eventbridge-pricing-pipes-64kb-chunk)
  link: [billed as four requests](../facts/eventbridge.md#eventbridge-pricing-pipes-64kb-chunk)
  say: sixty-four kilobyte chunk
eventbridge-pricing-pipes-per-million-requests
  claim: In the page's Pipes example, 0.5M requests after filtering are charged at $0.40 for each M, which is $0.20.
  scope: per M (million) Pipes requests after filtering; Worked example on the pricing page..
  link: [$0.40](../facts/eventbridge.md#eventbridge-pricing-pipes-per-million-requests)
  link: [$0.20](../facts/eventbridge.md#eventbridge-pricing-pipes-per-million-requests)
eventbridge-pricing-scheduler-free-tier-14m
  claim: As part of the Free Tier, EventBridge Scheduler allows 14,000,000 invocations per month for free.
  scope: per month, across all Regions except GovCloud; Unused free usage does not roll over to the next month..
  link: [14,000,000 invocations per month](../facts/eventbridge.md#eventbridge-pricing-scheduler-free-tier-14m)
eventbridge-pricing-scheduler-per-million-beyond-free
  claim: In the page's example, EventBridge Scheduler invocations beyond the 14M free tier (20M invocations in the month) are charged at $1.00/M, which is $6.00.
  scope: per M (million) Scheduler invocations beyond the free tier; Worked example on the pricing page..
  link: [$1.00/M](../facts/eventbridge.md#eventbridge-pricing-scheduler-per-million-beyond-free)
  link: [$6.00](../facts/eventbridge.md#eventbridge-pricing-scheduler-per-million-beyond-free)
eventbridge-pricing-schema-registry-free
  claim: Usage of the EventBridge Schema Registry for AWS and custom schemas is free, and Schema Discovery includes a Free Tier of 5 million ingested events per month.
  scope: Schema Registry; Schema Discovery per month.
  link: [free](../facts/eventbridge.md#eventbridge-pricing-schema-registry-free)
  link: [5 million ingested events per month](../facts/eventbridge.md#eventbridge-pricing-schema-registry-free)
eventbridge-putevents-entry-size-calculation
  claim: EventBridge calculates a PutEvents entry size from the Time parameter (14 bytes, if specified), the UTF-8 byte length of Source and DetailType, and, if specified, the UTF-8 byte length of Detail and of each Resources entry.
  scope: per PutEvents entry.
  link: [the Time parameter is 14 bytes](../facts/eventbridge.md#eventbridge-putevents-entry-size-calculation)
  link: [the number of bytes for their UTF-8 encoded forms](../facts/eventbridge.md#eventbridge-putevents-entry-size-calculation)
eventbridge-putevents-over-1mb-use-s3
  claim: If a PutEvents entry is larger than 1 MB (1,048,576 bytes), AWS recommends uploading the event to an Amazon S3 bucket and including the Object URL in the PutEvents entry.
  scope: per PutEvents entry.
  link: [larger than 1 MB (1,048,576 bytes)](../facts/eventbridge.md#eventbridge-putevents-over-1mb-use-s3)
  link: [uploading the event to an Amazon S3 bucket](../facts/eventbridge.md#eventbridge-putevents-over-1mb-use-s3)
eventbridge-putevents-partial-failure-caller-retries
  claim: If one entry of a PutEvents request fails, EventBridge by default continues with the other entries. The response can hold both successful and failed entries, and you must find the failed entries and send them again in a later call.
  scope: EventBridge PutEvents; default.
  link: [EventBridge continues processing the rest of the entries](../facts/eventbridge.md#eventbridge-putevents-partial-failure-caller-retries)
  link: [You must detect unsuccessful entries](../facts/eventbridge.md#eventbridge-putevents-partial-failure-caller-retries)
eventbridge-putevents-request-size-under-1mb
  claim: The total PutEvents request size, which is the sum of all event entries in the request, must be less than 1 MB (1,048,576 bytes); the limit applies to the request as a whole, and a single event can use up to the full 1 MB if it is the only entry.
  scope: per PutEvents request, all entries together; maximum; not adjustable.
  link: [1 MB](../facts/eventbridge.md#eventbridge-putevents-request-size-under-1mb)
  link: [1,048,576 bytes](../facts/eventbridge.md#eventbridge-putevents-request-size-under-1mb)
  say: one megabyte
eventbridge-putevents-sends-many-events-in-one-request
  claim: The PutEvents action sends multiple events to EventBridge in a single request, and each event gets a unique ID.
  scope: EventBridge PutEvents.
  link: [The PutEvents action sends multiple events](../facts/eventbridge.md#eventbridge-putevents-sends-many-events-in-one-request)
  link: [in a single request](../facts/eventbridge.md#eventbridge-putevents-sends-many-events-in-one-request)
eventbridge-putevents-to-missing-bus-drops-event-with-200
  claim: If you use PutEvents to publish an event to an event bus that does not exist, EventBridge does not find a rule and drops the event, yet it still returns a 200 response and does not count the event as a failed entry.
  scope: EventBridge PutEvents; event bus does not exist.
  link: [will not find a corresponding rule](../facts/eventbridge.md#eventbridge-putevents-to-missing-bus-drops-event-with-200)
  link: [EventBridge will send a 200 response](../facts/eventbridge.md#eventbridge-putevents-to-missing-bus-drops-event-with-200)
eventbridge-putevents-up-to-10-entries
  claim: When you send custom events to EventBridge using the PutEvents action, you can batch up to 10 event entries into one request.
  scope: per PutEvents request (custom events); maximum; not adjustable.
  link: [up to 10 event entries](../facts/eventbridge.md#eventbridge-putevents-up-to-10-entries)
  say: ten event entries
eventbridge-quota-event-buses-classic
  claim: The default quota is 100 event buses per account in each supported Region, and it can be raised through Service Quotas.
  scope: per account, per Region; default; adjustable; Custom Event Bus - Classic quotas table..
  link: [Each supported Region: 100](../facts/eventbridge.md#eventbridge-quota-event-buses-classic)
eventbridge-quota-event-pattern-size
  claim: The default maximum size of an event pattern is 2,048 characters, and the quota is adjustable.
  scope: per event pattern, per Region; default; adjustable; Custom Event Bus - Classic quotas table..
  link: [2,048](../facts/eventbridge.md#eventbridge-quota-event-pattern-size)
eventbridge-quota-pipes-per-account
  claim: EventBridge Pipes has a default limit of 1000 pipes per account in all Regions.
  scope: per account, all Regions; default; not adjustable.
  link: [1000](../facts/eventbridge.md#eventbridge-quota-pipes-per-account)
eventbridge-quota-rules-per-bus
  claim: The default quota is 300 rules per event bus in most supported Regions (100 in af-south-1 and eu-south-1), and it is adjustable.
  scope: per event bus, per account, per Region; default; adjustable; 300 in each of the other supported Regions; 100 in af-south-1 and eu-south-1..
  link: [300](../facts/eventbridge.md#eventbridge-quota-rules-per-bus)
  link: [af-south-1: 100](../facts/eventbridge.md#eventbridge-quota-rules-per-bus)
eventbridge-quota-rules-with-wildcards
  claim: Each event bus can have at most 30 rules whose event filters include wildcards; this quota cannot be adjusted.
  scope: per event bus, per account, per Region; maximum; not adjustable.
  link: [30 rules per event bus](../facts/eventbridge.md#eventbridge-quota-rules-with-wildcards)
eventbridge-quota-targets-per-rule
  claim: A Custom Event Bus - Classic rule can have a maximum of 5 targets; this quota is not adjustable.
  scope: per rule, per Region; maximum; not adjustable; Custom Event Bus - Classic (rules and targets)..
  link: [5](../facts/eventbridge.md#eventbridge-quota-targets-per-rule)
  link: [Each supported Region: 5](../facts/eventbridge.md#eventbridge-quota-targets-per-rule)
  say: five targets
eventbridge-replay-adds-replay-name-field
  claim: When EventBridge replays an event from an archive, it adds a replay-name metadata field to the event. EventBridge also uses this field to make sure replayed events are not sent to archives.
  scope: EventBridge replay.
  link: [adds a metadata field to the event](../facts/eventbridge.md#eventbridge-replay-adds-replay-name-field)
  link: [replayed events aren't sent to archives](../facts/eventbridge.md#eventbridge-replay-adds-replay-name-field)
eventbridge-replay-keeps-archive-events
  claim: Replaying events does not remove them from the archive, so you can replay events in multiple replays. EventBridge removes events only when they exceed the archive retention period or you delete the archive.
  scope: EventBridge replay.
  link: [does not remove them from the archive](../facts/eventbridge.md#eventbridge-replay-keeps-archive-events)
  link: [replay events in multiple replays](../facts/eventbridge.md#eventbridge-replay-keeps-archive-events)
eventbridge-replay-order-not-guaranteed
  claim: Events are not necessarily replayed in the same order in which they were added to the archive.
  scope: EventBridge replay.
  link: [aren't necessarily replayed in the same order](../facts/eventbridge.md#eventbridge-replay-order-not-guaranteed)
  link: [added to the archive](../facts/eventbridge.md#eventbridge-replay-order-not-guaranteed)
eventbridge-replay-to-source-bus-only
  claim: Archived events can only be replayed to the source event bus, the bus that originally received them.
  scope: EventBridge replay.
  link: [only be replayed to the source event bus](../facts/eventbridge.md#eventbridge-replay-to-source-bus-only)
  link: [event bus that originally received them](../facts/eventbridge.md#eventbridge-replay-to-source-bus-only)
eventbridge-retry-default-24h-185-attempts
  claim: By default, EventBridge retries sending an event to a target for 24 hours and up to 185 times, with exponential back off and jitter; the retry policy settings of the target set the length of time and the number of retry attempts.
  scope: per target of a rule (retry policy setting); default; adjustable; Retriable errors only; configured in the Retry policy settings of the target..
  link: [24 hours](../facts/eventbridge.md#eventbridge-retry-default-24h-185-attempts)
  link: [up to 185 times](../facts/eventbridge.md#eventbridge-retry-default-24h-185-attempts)
  say: twenty-four hours
eventbridge-retry-exhausted-event-dropped
  claim: If an event is not delivered after all retry attempts are exhausted, the event is dropped and EventBridge does not continue to process it; a dead-letter queue can receive failed events.
  scope: per target delivery.
  link: [the event is dropped](../facts/eventbridge.md#eventbridge-retry-exhausted-event-dropped)
  link: [configure a dead-letter queue (DLQ)](../facts/eventbridge.md#eventbridge-retry-exhausted-event-dropped)
eventbridge-retry-length-and-attempts-set-per-target
  claim: When an event is not delivered because of retriable errors, EventBridge retries. You set the length of time it tries and the number of retry attempts in the Retry policy settings of each target.
  scope: EventBridge rule target; retriable errors.
  link: [number of retry attempts](../facts/eventbridge.md#eventbridge-retry-length-and-attempts-set-per-target)
  link: [length of time it tries](../facts/eventbridge.md#eventbridge-retry-length-and-attempts-set-per-target)
eventbridge-rule-applies-to-one-bus
  claim: Each rule is defined for one specific event bus and applies only to events on that event bus.
  scope: EventBridge rule.
  link: [defined for a specific event bus](../facts/eventbridge.md#eventbridge-rule-applies-to-one-bus)
  link: [only apply to events on that event bus](../facts/eventbridge.md#eventbridge-rule-applies-to-one-bus)
eventbridge-rule-infinite-loop-risk
  claim: A rule can lead to higher-than-expected charges and throttling. For example, you can inadvertently create a rule that leads to an infinite loop, where a rule is fired recursively without end.
  scope: EventBridge rule.
  link: [where a rule is fired recursively](../facts/eventbridge.md#eventbridge-rule-infinite-loop-risk)
  link: [higher-than-expected charges and throttling](../facts/eventbridge.md#eventbridge-rule-infinite-loop-risk)
eventbridge-rule-single-target-best-practice
  claim: A rule can have up to five targets, but managing rules is easier with a single target per rule. To send the same events to several targets, duplicate the rule.
  scope: EventBridge rule.
  link: [specify a single target for each rule](../facts/eventbridge.md#eventbridge-rule-single-target-best-practice)
  link: [duplicating the rule to deliver the same events](../facts/eventbridge.md#eventbridge-rule-single-target-best-practice)
eventbridge-saas-partner-event-source-needs-bus
  claim: To receive events from a SaaS partner, you need a partner event source from the partner. You accept it by creating a Custom Event Bus - Classic and matching it to the partner event source.
  scope: EventBridge SaaS partner integration.
  link: [need a partner event source from the partner](../facts/eventbridge.md#eventbridge-saas-partner-event-source-needs-bus)
  link: [match it to the partner event source](../facts/eventbridge.md#eventbridge-saas-partner-event-source-needs-bus)
eventbridge-scheduled-rule-utc-and-one-minute-precision
  claim: All scheduled rules use the UTC+0 time zone, and the minimum precision for a schedule is one minute.
  scope: EventBridge scheduled rule; fixed.
  link: [UTC+0 time zone](../facts/eventbridge.md#eventbridge-scheduled-rule-utc-and-one-minute-precision)
  link: [minimum precision for a schedule is one minute](../facts/eventbridge.md#eventbridge-scheduled-rule-utc-and-one-minute-precision)
eventbridge-scheduled-rules-are-legacy
  claim: Scheduled rules are a legacy feature of EventBridge. AWS recommends EventBridge Scheduler to invoke targets on a schedule.
  scope: EventBridge scheduled rules.
  link: [legacy feature of EventBridge](../facts/eventbridge.md#eventbridge-scheduled-rules-are-legacy)
  link: [use Scheduler to invoke targets on a schedule](../facts/eventbridge.md#eventbridge-scheduled-rules-are-legacy)
eventbridge-scheduler-at-least-once-with-retries
  claim: EventBridge Scheduler provides at-least-once event delivery to targets, and you can set the number of retries for a failed task.
  scope: EventBridge Scheduler schedule.
  link: [at-least-once event delivery to targets](../facts/eventbridge.md#eventbridge-scheduler-at-least-once-with-retries)
  link: [set the number of retries for your schedule](../facts/eventbridge.md#eventbridge-scheduler-at-least-once-with-retries)
eventbridge-scheduler-cron-supports-time-zones
  claim: EventBridge Scheduler supports cron-based schedules in UTC or in the time zone that you specify when you create the schedule.
  scope: EventBridge Scheduler cron-based schedule.
  link: [in the time zone that you specify](../facts/eventbridge.md#eventbridge-scheduler-cron-supports-time-zones)
  link: [Universal Coordinated Time (UTC)](../facts/eventbridge.md#eventbridge-scheduler-cron-supports-time-zones)
eventbridge-scheduler-dlq-standard-sqs-only
  claim: EventBridge Scheduler supports an SQS standard queue as a schedule's dead-letter queue. It does not support a FIFO queue as the dead-letter queue.
  scope: EventBridge Scheduler schedule.
  link: [an Amazon SQS standard queue that you specify](../facts/eventbridge.md#eventbridge-scheduler-dlq-standard-sqs-only)
  link: [does not support using a FIFO queue](../facts/eventbridge.md#eventbridge-scheduler-dlq-standard-sqs-only)
eventbridge-scheduler-execution-role-assumed
  claim: An execution role is an IAM role that EventBridge Scheduler assumes to interact with other AWS services on your behalf. You attach permission policies to this role to let the schedule invoke its target.
  scope: EventBridge Scheduler schedule.
  link: [an IAM role that EventBridge Scheduler assumes](../facts/eventbridge.md#eventbridge-scheduler-execution-role-assumed)
  link: [attach permission policies to this role](../facts/eventbridge.md#eventbridge-scheduler-execution-role-assumed)
eventbridge-scheduler-flexible-time-window-disperses-triggers
  claim: Flexible time windows let you disperse schedules and improve the reliability of triggers for use cases that do not need precise invocation of targets.
  scope: EventBridge Scheduler schedule.
  link: [allowing you to disperse your schedules](../facts/eventbridge.md#eventbridge-scheduler-flexible-time-window-disperses-triggers)
  link: [do not require precise scheduled invocation of targets](../facts/eventbridge.md#eventbridge-scheduler-flexible-time-window-disperses-triggers)
eventbridge-scheduler-flexible-window-max-1440-minutes
  claim: In the EventBridge Scheduler API, the maximum time window during which a schedule can be invoked has a valid range from a minimum value of 1 to a maximum value of 1440. The user guide sets a flexible time window in minutes, for example a 15 minute window within which the target is invoked after the scheduled time.
  scope: per schedule; flexible time window; maximum; not adjustable.
  link: [Minimum value of 1](../facts/eventbridge.md#eventbridge-scheduler-flexible-window-max-1440-minutes)
  link: [Maximum value of 1440](../facts/eventbridge.md#eventbridge-scheduler-flexible-window-max-1440-minutes)
eventbridge-scheduler-input-payload-256kb
  claim: The maximum size of an EventBridge Scheduler target's Input payload is 256 KB; this is a fixed limit, not an adjustable Service Quotas quota.
  scope: per schedule target Input; maximum; not adjustable; Applies to all target types, templated and universal..
  link: [256 KB](../facts/eventbridge.md#eventbridge-scheduler-input-payload-256kb)
  say: two hundred fifty-six kilobytes
eventbridge-scheduler-one-time-schedule-invokes-once
  claim: A one-time schedule invokes its target only once.
  scope: EventBridge Scheduler.
  link: [invokes a target only once](../facts/eventbridge.md#eventbridge-scheduler-one-time-schedule-invokes-once)
  link: [A one-time schedule is a schedule](../facts/eventbridge.md#eventbridge-scheduler-one-time-schedule-invokes-once)
eventbridge-scheduler-quota-schedule-groups
  claim: The default quota is 500 schedule groups per Region for EventBridge Scheduler, and it is adjustable.
  scope: per Region; default; adjustable.
  link: [500](../facts/eventbridge.md#eventbridge-scheduler-quota-schedule-groups)
eventbridge-scheduler-quota-schedules-per-region
  claim: The default quota for EventBridge Scheduler is 10,000,000 schedules per Region; the quota includes one-time schedules that have completed running, and it is adjustable to billions of schedules.
  scope: per Region; default; adjustable; Includes one-time schedules that have completed running..
  link: [10,000,000](../facts/eventbridge.md#eventbridge-scheduler-quota-schedules-per-region)
eventbridge-scheduler-recurring-schedules-use-time-zone
  claim: Rate-based and cron-based schedules are recurring schedules. You configure each with a schedule expression and a time zone in which EventBridge Scheduler evaluates it.
  scope: EventBridge Scheduler.
  link: [rate-based and cron-based schedules are recurring schedules](../facts/eventbridge.md#eventbridge-scheduler-recurring-schedules-use-time-zone)
  link: [specifying a time zone](../facts/eventbridge.md#eventbridge-scheduler-recurring-schedules-use-time-zone)
eventbridge-scheduler-retry-max-attempts
  claim: In an EventBridge Scheduler retry policy, MaximumRetryAttempts can be set from 0 to 185; retries with exponential backoff continue until the maximum attempts are made or the MaximumEventAgeInSeconds is reached.
  scope: per schedule target retry policy; maximum; not adjustable.
  link: [Minimum value of 0](../facts/eventbridge.md#eventbridge-scheduler-retry-max-attempts)
  link: [Maximum value of 185](../facts/eventbridge.md#eventbridge-scheduler-retry-max-attempts)
eventbridge-scheduler-retry-max-event-age
  claim: In an EventBridge Scheduler retry policy, MaximumEventAgeInSeconds is the maximum amount of time to continue to make retry attempts, with a valid range from a minimum value of 60 to a maximum value of 86400.
  scope: per schedule target retry policy; the parameter counts in seconds; maximum; not adjustable.
  link: [Minimum value of 60](../facts/eventbridge.md#eventbridge-scheduler-retry-max-event-age)
  link: [Maximum value of 86400](../facts/eventbridge.md#eventbridge-scheduler-retry-max-event-age)
eventbridge-scheduler-serverless-central-service
  claim: EventBridge Scheduler is a serverless scheduler that lets you create, run and manage tasks from one central, managed service.
  scope: EventBridge Scheduler.
  link: [a serverless scheduler](../facts/eventbridge.md#eventbridge-scheduler-serverless-central-service)
  link: [from one central, managed service](../facts/eventbridge.md#eventbridge-scheduler-serverless-central-service)
eventbridge-scheduler-templated-targets-core-services
  claim: Templated targets are a set of common API operations across core AWS services such as Amazon SQS, Lambda and Step Functions.
  scope: EventBridge Scheduler targets.
  link: [common API operations across a group of core](../facts/eventbridge.md#eventbridge-scheduler-templated-targets-core-services)
  link: [Amazon SQS, Lambda, and Step Functions](../facts/eventbridge.md#eventbridge-scheduler-templated-targets-core-services)
eventbridge-scheduler-three-schedule-types
  claim: EventBridge Scheduler has three schedule types: rate-based, cron-based and one-time schedules.
  scope: EventBridge Scheduler.
  link: [rate-based, cron-based, and one-time schedules](../facts/eventbridge.md#eventbridge-scheduler-three-schedule-types)
  link: [three schedule types](../facts/eventbridge.md#eventbridge-scheduler-three-schedule-types)
eventbridge-scheduler-universal-target-wider-api-set
  claim: The universal target is a customizable set of parameters that lets a schedule invoke a wider set of API operations for many AWS services.
  scope: EventBridge Scheduler targets.
  link: [customizable set of parameters](../facts/eventbridge.md#eventbridge-scheduler-universal-target-wider-api-set)
  link: [invoke a wider set of API operation](../facts/eventbridge.md#eventbridge-scheduler-universal-target-wider-api-set)
eventbridge-schema-registry-schemas-for-aws-service-events
  claim: EventBridge provides schemas for all events generated by AWS services. You can also create or upload custom schemas or infer schemas from events on an event bus.
  scope: EventBridge schema registry.
  link: [all events that are generated by AWS services](../facts/eventbridge.md#eventbridge-schema-registry-schemas-for-aws-service-events)
  link: [infer schemas directly from events](../facts/eventbridge.md#eventbridge-schema-registry-schemas-for-aws-service-events)
eventbridge-some-errors-skip-retries
  claim: Some EventBridge events are dropped or sent to a DLQ without any retry attempts. For errors that result from missing permissions to a target, a target resource that no longer exists, or a target that cannot be found because of an invalid address or DNS lookup failure, no retry attempts happen until action is taken to resolve the underlying issue. EventBridge sends these events directly to the target DLQ, if you have specified one.
  scope: EventBridge rule target; until action is taken to resolve the underlying issue.
  link: [without any retry attempts](../facts/eventbridge.md#eventbridge-some-errors-skip-retries)
  link: [sends these events directly to the target DLQ](../facts/eventbridge.md#eventbridge-some-errors-skip-retries)
eventbridge-target-needs-permission-to-access
  claim: To deliver event data to a target, EventBridge needs permission to access the target resource.
  scope: EventBridge rule target.
  link: [EventBridge needs permission to access the target resource](../facts/eventbridge.md#eventbridge-target-needs-permission-to-access)
  link: [To deliver event data to a target](../facts/eventbridge.md#eventbridge-target-needs-permission-to-access)
eventbridge-target-permission-model-by-target-type
  claim: For CloudWatch Logs targets EventBridge uses resource-based policies. For Lambda, SNS and SQS targets it can use an IAM execution role or a resource-based policy. For Kinesis streams it uses identity-based policies.
  scope: EventBridge rule target.
  link: [EventBridge uses resource-based policies](../facts/eventbridge.md#eventbridge-target-permission-model-by-target-type)
  link: [an IAM execution role or a resource-based policy](../facts/eventbridge.md#eventbridge-target-permission-model-by-target-type)
  link: [For Kinesis streams, EventBridge uses identity-based](../facts/eventbridge.md#eventbridge-target-permission-model-by-target-type)
eventbridge-target-types-list
  claim: For Custom Event Bus - Classic rules, you can have EventBridge send events to a number of AWS service resources, including an ECS task, a Firehose delivery stream, a Kinesis stream, a Lambda function (ASYNC), an SNS topic, Amazon SQS standard, fair, and FIFO queues, and a Step Functions state machine (ASYNC).
  scope: EventBridge rule target, Custom Event Bus - Classic.
  link: [ECS task](../facts/eventbridge.md#eventbridge-target-types-list)
  link: [Kinesis stream](../facts/eventbridge.md#eventbridge-target-types-list)
  link: [Lambda function (ASYNC)](../facts/eventbridge.md#eventbridge-target-types-list)
  link: [Amazon SQS standard, fair, and FIFO queues](../facts/eventbridge.md#eventbridge-target-types-list)
  link: [Step Functions state machine (ASYNC)](../facts/eventbridge.md#eventbridge-target-types-list)
eventbridge-two-rule-types-pattern-and-schedule
  claim: You can create two types of EventBridge rules: rules that match on event data as events are delivered, and rules that run on a defined schedule.
  scope: EventBridge rule.
  link: [rules that match on event data](../facts/eventbridge.md#eventbridge-two-rule-types-pattern-and-schedule)
  link: [rules that run on a defined schedule](../facts/eventbridge.md#eventbridge-two-rule-types-pattern-and-schedule)
eventbridge-wa-abstracts-producers-from-consumers
  claim: Event-driven architectures can be built with EventBridge, which can abstract clients (event producers) from the services they rely on (event consumers).
  scope: Well-Architected reliability pillar, REL04-BP02 loosely coupled dependencies.
  link: [abstract clients (event producers) from the services](../facts/eventbridge.md#eventbridge-wa-abstracts-producers-from-consumers)
  link: [Event-driven architectures](../facts/eventbridge.md#eventbridge-wa-abstracts-producers-from-consumers)
eventbridge-wa-deployed-multi-az-by-aws
  claim: AWS services such as Amazon S3, Lambda, API Gateway, Amazon SQS, Amazon SNS, EventBridge and Amazon DynamoDB are automatically deployed to multiple Availability Zones by AWS.
  scope: Regional AWS services named in REL11-BP02 (including SQS, SNS and EventBridge).
  link: [automatically deployed to multiple Availability Zones](../facts/eventbridge.md#eventbridge-wa-deployed-multi-az-by-aws)
  link: [by AWS](../facts/eventbridge.md#eventbridge-wa-deployed-multi-az-by-aws)
sns-a2a-subscriber-types
  claim: Application-to-application messaging supports subscribers such as delivery streams, Lambda functions, SQS queues, HTTP/S endpoints and AWS Event Fork Pipelines.
  scope: Amazon SNS subscribers.
  link: [delivery streams, Lambda functions, Amazon SQS queues](../facts/sns.md#sns-a2a-subscriber-types)
  link: [HTTP/S endpoints, and AWS Event Fork Pipelines](../facts/sns.md#sns-a2a-subscriber-types)
sns-a2p-subscriber-types
  claim: Application-to-person notifications go to subscribers such as mobile applications, mobile phone numbers and email addresses.
  scope: Amazon SNS subscribers.
  link: [mobile applications, mobile phone numbers, and email addresses](../facts/sns.md#sns-a2p-subscriber-types)
  link: [Application-to-person notifications](../facts/sns.md#sns-a2p-subscriber-types)
sns-addpermission-adds-policy-statement
  claim: To allow one or more AWS accounts to perform a specific action on an SNS topic, such as publishing messages, you can use the SNS API action AddPermission. You specify a topic, a list of AWS account IDs, a list of actions and a label, and SNS automatically generates and adds a new policy statement to the topic's access control policy.
  scope: SNS topic access policy.
  link: [using the Amazon SNS API action AddPermission](../facts/sns.md#sns-addpermission-adds-policy-statement)
  link: [automatically generates and adds a new policy statement](../facts/sns.md#sns-addpermission-adds-policy-statement)
sns-change-fifo-archiving-replay-2023
  claim: On October 26, 2023 SNS added message archiving and replay for FIFO topics. Topic owners can archive messages to a topic for up to 365 days, and subscribers can replay the archived messages back to a subscribed endpoint.
  scope: SNS FIFO topics only; maximum.
  link: [October 26, 2023](../facts/sns.md#sns-change-fifo-archiving-replay-2023)
  link: [up to 365 days](../facts/sns.md#sns-change-fifo-archiving-replay-2023)
sns-change-fifo-standard-queue-subscribers-2023
  claim: On September 14, 2023 SNS added support for subscribing a standard queue to a FIFO topic. You can subscribe an SQS FIFO queue or a standard queue to an SNS FIFO topic, but only SQS FIFO queues guarantee messages are received in order and with no duplicates.
  scope: SNS FIFO topic subscriptions.
  link: [September 14, 2023](../facts/sns.md#sns-change-fifo-standard-queue-subscribers-2023)
  link: [guarantee messages are received in order](../facts/sns.md#sns-change-fifo-standard-queue-subscribers-2023)
sns-change-fifo-throughput-scope-high-throughput-2025
  claim: On 2025-01-21 SNS added high-throughput mode for FIFO topics, which you enable by setting the FifoThroughputScope topic attribute to MessageGroup. By default, SNS FIFO topics provide 300 MPS per message group ID and 3K MPS per topic, with topic level de-duplication.
  scope: per message group ID and per FIFO topic; default; To get higher throughput, enable high-throughput mode by setting the FifoThroughputScope topic attribute to MessageGroup..
  link: [2025-01-21](../facts/sns.md#sns-change-fifo-throughput-scope-high-throughput-2025)
  link: [300 MPS per message group ID](../facts/sns.md#sns-change-fifo-throughput-scope-high-throughput-2025)
  link: [3K MPS per topic](../facts/sns.md#sns-change-fifo-throughput-scope-high-throughput-2025)
sns-change-max-message-size-1mib-opt-in-2026
  claim: On 2026-09-18 SNS added support for message payloads up to 1 MiB, a 4x increase from the previous 256 KiB limit. Topics still accept messages up to 256 KiB by default.
  scope: per message, per topic; default.
  link: [256 KiB](../facts/sns.md#sns-change-max-message-size-1mib-opt-in-2026)
  link: [1 MiB](../facts/sns.md#sns-change-max-message-size-1mib-opt-in-2026)
  link: [2026-09-18](../facts/sns.md#sns-change-max-message-size-1mib-opt-in-2026)
  changed: 2026-09-18: was 256 KiB
sns-change-message-data-protection-closed-to-new-customers-2026
  claim: SNS message data protection is no longer open to new customers: the documentation history lists April 30, 2026, and existing customers with message data protection policies configured can continue to use the feature in those accounts. AWS recommends a Lambda-based architecture with Amazon Bedrock Guardrails as the alternative.
  scope: SNS message data protection; do not teach it as an exam answer for new designs.
  link: [April 30, 2026](../facts/sns.md#sns-change-message-data-protection-closed-to-new-customers-2026)
  link: [Lambda-based architecture using Amazon Bedrock Guardrails](../facts/sns.md#sns-change-message-data-protection-closed-to-new-customers-2026)
sns-change-payload-based-filtering-2022
  claim: On November 22, 2022 SNS added payload-based message filtering, which lets you filter messages based on the message payload. If no filter policy scope is defined for an existing filter policy, the scope defaults to MessageAttributes.
  scope: per subscription filter policy; default; FilterPolicyScope subscription attribute.
  link: [November 22, 2022](../facts/sns.md#sns-change-payload-based-filtering-2022)
  link: [MessageAttributes](../facts/sns.md#sns-change-payload-based-filtering-2022)
sns-client-side-error-not-retried
  claim: Amazon SNS doesn't retry a message delivery that fails because of a client-side error.
  scope: SNS subscription delivery.
  link: [doesn't retry the message delivery](../facts/sns.md#sns-client-side-error-not-retried)
  link: [fails because of a client-side error](../facts/sns.md#sns-client-side-error-not-retried)
sns-cross-account-non-owner-must-confirm-subscription
  claim: Any user who creates a subscription but is not the owner of the queue must confirm the subscription. Until it is confirmed, no notifications from the topic are sent to the queue.
  scope: SNS topic to SQS queue in another account; subscriber is not the queue owner.
  link: [must confirm the subscription](../facts/sns.md#sns-cross-account-non-owner-must-confirm-subscription)
  link: [Until confirmed, no notifications published to the topic](../facts/sns.md#sns-cross-account-non-owner-must-confirm-subscription)
sns-cross-account-queue-owner-subscription-needs-no-confirmation
  claim: When the queue owner creates the subscription to a topic in another account, the subscription does not need confirmation. The topic owner must first give the queue owner's account permission to call Subscribe on the topic.
  scope: SNS topic to SQS queue in another account; the queue owner creates the subscription.
  link: [the subscription doesn't require confirmation](../facts/sns.md#sns-cross-account-queue-owner-subscription-needs-no-confirmation)
  link: [call the Subscribe action on the topic](../facts/sns.md#sns-cross-account-queue-owner-subscription-needs-no-confirmation)
sns-cross-region-delivery-to-sqs-and-lambda
  claim: SNS supports cross-Region delivery of notifications to SQS queues and to Lambda functions, in Regions that are enabled by default and in opt-in Regions.
  scope: SNS topic to SQS queue or Lambda function in another Region.
  link: [Amazon SQS queues and to AWS Lambda functions](../facts/sns.md#sns-cross-region-delivery-to-sqs-and-lambda)
  link: [cross-Region delivery of notifications](../facts/sns.md#sns-cross-region-delivery-to-sqs-and-lambda)
sns-cross-region-opt-in-region-needs-different-principal
  claim: When one of the Regions is an opt-in Region, you must specify a different SNS service principal in the policy of the subscribed resource.
  scope: SNS cross-Region delivery; one Region is an opt-in Region.
  link: [a different Amazon SNS service principal](../facts/sns.md#sns-cross-region-opt-in-region-needs-different-principal)
  link: [one of the Regions is an opt-in Region](../facts/sns.md#sns-cross-region-opt-in-region-needs-different-principal)
sns-decision-filter-policies
  claim: SNS provides message filtering through subscription filter policies, which let subscribers selectively receive messages based on message attributes.
  scope: Amazon SNS, in the SNS, SQS or EventBridge decision guide.
  link: [subscription filter policies](../facts/sns.md#sns-decision-filter-policies)
  link: [based on message attributes](../facts/sns.md#sns-decision-filter-policies)
sns-decision-no-persistence
  claim: SNS does not persist messages. It delivers them to subscribers in real time.
  scope: Amazon SNS, in the SNS, SQS or EventBridge decision guide.
  link: [Messages are not persisted](../facts/sns.md#sns-decision-no-persistence)
  link: [delivered to subscribers in real-time](../facts/sns.md#sns-decision-no-persistence)
sns-decision-pricing-dimensions-requests-notifications-data
  claim: SNS pricing is based on the number of API requests, notifications delivered and data transferred; SNS SMS messages are billed through AWS End User Messaging.
  scope: Amazon SNS, in the SNS, SQS or EventBridge decision guide.
  link: [API requests, notifications delivered, and data transferred](../facts/sns.md#sns-decision-pricing-dimensions-requests-notifications-data)
  link: [billed through AWS End User Messaging](../facts/sns.md#sns-decision-pricing-dimensions-requests-notifications-data)
sns-decision-push-model
  claim: SNS uses a push-based model: it delivers messages to subscriptions such as HTTP/HTTPS endpoints, email addresses, SMS, SQS queues and Lambda functions.
  scope: Amazon SNS, in the SNS, SQS or EventBridge decision guide.
  link: [Push-based model](../facts/sns.md#sns-decision-push-model)
  link: [HTTP/HTTPS endpoints, email addresses, SMS](../facts/sns.md#sns-decision-push-model)
  say: push-based model
sns-decision-subscriber-types
  claim: SNS supports a wide range of subscribers: HTTP/S endpoints, email, SMS, mobile push notifications, Lambda functions and SQS queues.
  scope: Amazon SNS, in the SNS, SQS or EventBridge decision guide.
  link: [a wide range of subscribers](../facts/sns.md#sns-decision-subscriber-types)
  link: [mobile push notifications, Lambda functions](../facts/sns.md#sns-decision-subscriber-types)
sns-decision-typical-use
  claim: SNS is often used for fanout notifications, pub/sub messaging and mobile push notifications, which broadcast a message to several subscribers at the same time.
  scope: Amazon SNS, in the SNS, SQS or EventBridge decision guide.
  link: [fanout notifications](../facts/sns.md#sns-decision-typical-use)
  link: [pub/sub messaging](../facts/sns.md#sns-decision-typical-use)
sns-dlq-alarm-on-visible-messages-not-messages-sent
  claim: An alarm on NumberOfMessagesSent is not suitable for a dead-letter queue because that metric does not capture messages sent to the DLQ after failed processing. Use ApproximateNumberOfMessagesVisible instead.
  scope: SQS dead-letter queue monitoring.
  link: [use the ApproximateNumberOfMessagesVisible metric](../facts/sns.md#sns-dlq-alarm-on-visible-messages-not-messages-sent)
  link: [NumberOfMessagesSent metric is not suitable](../facts/sns.md#sns-dlq-alarm-on-visible-messages-not-messages-sent)
sns-dlq-attached-to-subscription-not-topic
  claim: An SNS dead-letter queue is attached to a subscription, not to a topic, because message deliveries happen at the subscription level.
  scope: SNS subscription.
  link: [attached to an Amazon SNS subscription](../facts/sns.md#sns-dlq-attached-to-subscription-not-topic)
  link: [message deliveries happen at the subscription level](../facts/sns.md#sns-dlq-attached-to-subscription-not-topic)
sns-dlq-encrypted-queue-needs-custom-kms-key
  claim: To use an encrypted SQS queue as a dead-letter queue for an SNS subscription, you must use a custom KMS key whose key policy grants the SNS service principal access to the AWS KMS API actions.
  scope: SNS subscription dead-letter queue with SSE-KMS.
  link: [you must use a custom KMS](../facts/sns.md#sns-dlq-encrypted-queue-needs-custom-kms-key)
  link: [grants the Amazon SNS service principal access](../facts/sns.md#sns-dlq-encrypted-queue-needs-custom-kms-key)
sns-dlq-is-sqs-queue-for-subscription
  claim: An SNS dead-letter queue is an SQS queue that an SNS subscription can target for messages that cannot be delivered to the subscriber.
  scope: SNS subscription.
  link: [an Amazon SNS subscription can target](../facts/sns.md#sns-dlq-is-sqs-queue-for-subscription)
  link: [messages that can't be delivered to subscribers](../facts/sns.md#sns-dlq-is-sqs-queue-for-subscription)
sns-dlq-queue-type-matches-topic-type
  claim: FIFO topic subscriptions use FIFO queues as dead-letter queues, and standard topic subscriptions use standard queues.
  scope: SNS subscription dead-letter queue.
  link: [FIFO topic subscriptions use FIFO queues](../facts/sns.md#sns-dlq-queue-type-matches-topic-type)
  link: [standard topic subscriptions use standard queues](../facts/sns.md#sns-dlq-queue-type-matches-topic-type)
sns-dlq-same-account-and-region-as-subscription
  claim: The SNS subscription and its SQS dead-letter queue must be under the same AWS account and Region.
  scope: SNS subscription dead-letter queue.
  link: [same AWS account and Region](../facts/sns.md#sns-dlq-same-account-and-region-as-subscription)
  link: [must be under the same AWS account](../facts/sns.md#sns-dlq-same-account-and-region-as-subscription)
sns-durability-retry-policy-and-dlq-preserve-messages
  claim: If a subscribed endpoint is not available, SNS runs a delivery retry policy. To keep messages that are not delivered before the policy ends, you can create a dead-letter queue.
  scope: SNS subscription.
  link: [Amazon SNS runs a delivery retry policy](../facts/sns.md#sns-durability-retry-policy-and-dlq-preserve-messages)
  link: [you can create a dead-letter queue](../facts/sns.md#sns-durability-retry-policy-and-dlq-preserve-messages)
sns-event-destinations-fifo-mostly-sqs-only
  claim: Most AWS services support receiving events from SNS standard topics only. Amazon SQS supports receiving events from both SNS standard and FIFO topics.
  scope: SNS FIFO and standard topics.
  link: [from SNS standard topics only](../facts/sns.md#sns-event-destinations-fifo-mostly-sqs-only)
  link: [Amazon SQS supports receiving events from both](../facts/sns.md#sns-event-destinations-fifo-mostly-sqs-only)
sns-extended-client-library-2gb
  claim: To publish SNS messages larger than 1 MiB, use the Amazon SNS Extended Client Library for Java or for Python to store payloads in Amazon S3; these libraries support messages up to 2 GB and work with Standard and FIFO topics.
  scope: per message payload stored in Amazon S3; maximum; not adjustable; Compatible with Standard and FIFO topics..
  link: [up to 2 GB](../facts/sns.md#sns-extended-client-library-2gb)
  link: [store payloads in Amazon S3](../facts/sns.md#sns-extended-client-library-2gb)
  say: two gigabytes
sns-failed-delivery-does-not-change-subscription-status
  claim: Failed deliveries do not change the status of your SNS subscriptions.
  scope: SNS subscription.
  link: [don't change the status of your subscriptions](../facts/sns.md#sns-failed-delivery-does-not-change-subscription-status)
  link: [Failed deliveries](../facts/sns.md#sns-failed-delivery-does-not-change-subscription-status)
sns-fanout-replicates-message-to-many-endpoints
  claim: In the fanout scenario, a message published to an SNS topic is replicated and pushed to multiple endpoints such as Firehose delivery streams, SQS queues, HTTP(S) endpoints and Lambda functions, which allows parallel asynchronous processing.
  scope: SNS topic.
  link: [replicated and pushed to multiple endpoints](../facts/sns.md#sns-fanout-replicates-message-to-many-endpoints)
  link: [parallel asynchronous processing](../facts/sns.md#sns-fanout-replicates-message-to-many-endpoints)
sns-faq-add-permission-simple-access-policy-for-conditions
  claim: The AddPermission and RemovePermission APIs give a simple way to add and remove topic permissions. For conditional access and more advanced use cases, use access control policies.
  scope: per topic.
  link: [AddPermission and RemovePermission](../facts/sns.md#sns-faq-add-permission-simple-access-policy-for-conditions)
  link: [conditional access and more advanced use cases](../facts/sns.md#sns-faq-add-permission-simple-access-policy-for-conditions)
sns-faq-common-pattern-sns-publishes-to-sqs-queues
  claim: A common pattern is to use SNS to publish messages to Amazon SQS queues to reliably send messages to one or many system components asynchronously.
  scope: SNS and SQS.
  link: [publish messages to Amazon SQS queues](../facts/sns.md#sns-faq-common-pattern-sns-publishes-to-sqs-queues)
  link: [one or many system components asynchronously](../facts/sns.md#sns-faq-common-pattern-sns-publishes-to-sqs-queues)
sns-faq-default-only-topic-owner-can-publish
  claim: By default, only topic owners have permissions to publish to an SNS topic. A topic owner can set explicit permissions to allow more than one user (with a valid AWS ID) to publish to a topic.
  scope: per topic; default; not adjustable.
  link: [only topic owners have permissions to publish](../facts/sns.md#sns-faq-default-only-topic-owner-can-publish)
  link: [explicit permissions](../facts/sns.md#sns-faq-default-only-topic-owner-can-publish)
sns-faq-delivery-guaranteed-while-endpoint-accessible
  claim: Amazon SNS delivers a message to the subscribed endpoint as long as the endpoint is accessible. A delivery fails when SNS cannot access the endpoint because of a client-side or a server-side error.
  scope: per subscription.
  link: [as long as the subscribed endpoint is accessible](../facts/sns.md#sns-faq-delivery-guaranteed-while-endpoint-accessible)
  link: [client-side or a server-side error](../facts/sns.md#sns-faq-delivery-guaranteed-while-endpoint-accessible)
sns-faq-durable-storage-multiple-copies-multiple-azs
  claim: On a publish request, SNS stores multiple copies of the message to disk across multiple Availability Zones before it acknowledges receipt to the sender.
  scope: per published message.
  link: [multiple copies (to disk)](../facts/sns.md#sns-faq-durable-storage-multiple-copies-multiple-azs)
  link: [multiple Availability Zones before acknowledging receipt](../facts/sns.md#sns-faq-durable-storage-multiple-copies-multiple-azs)
sns-faq-each-notification-contains-single-message
  claim: All SNS notification messages contain a single published message.
  scope: per notification.
  link: [single published message](../facts/sns.md#sns-faq-each-notification-contains-single-message)
  link: [notification messages](../facts/sns.md#sns-faq-each-notification-contains-single-message)
sns-faq-fanout-identical-messages-to-multiple-sqs-queues
  claim: To fan out identical messages to multiple SQS queues, create an SNS topic and subscribe multiple SQS standard queues to it. Whenever a message is sent to the topic, SNS delivers it to all the subscribed queues.
  scope: per topic.
  link: [multiple SQS standard queues to the SNS topic](../facts/sns.md#sns-faq-fanout-identical-messages-to-multiple-sqs-queues)
  link: [fanned out to the SQS queues](../facts/sns.md#sns-faq-fanout-identical-messages-to-multiple-sqs-queues)
sns-faq-fifo-topic-to-sqs-fifo-queue-end-to-end-ordering
  claim: Amazon SNS FIFO topics can deliver ordered messages to Amazon SQS FIFO queues to provide consistent end-to-end message ordering for distributed applications.
  scope: FIFO topics.
  link: [deliver ordered messages to Amazon Simple Queue Service](../facts/sns.md#sns-faq-fifo-topic-to-sqs-fifo-queue-end-to-end-ordering)
  link: [consistent end-to-end message ordering](../facts/sns.md#sns-faq-fifo-topic-to-sqs-fifo-queue-end-to-end-ordering)
sns-faq-fifo-topics-ordered-and-once-only-delivery
  claim: When delivery to subscribers must be in order (first-in-first-out) and once only, and you want SNS to handle it, SNS FIFO topics are the way to go.
  scope: FIFO topics.
  link: [in order (first-in-first-out), and once only](../facts/sns.md#sns-faq-fifo-topics-ordered-and-once-only-delivery)
  link: [SNS FIFO topics is the way to go](../facts/sns.md#sns-faq-fifo-topics-ordered-and-once-only-delivery)
sns-faq-fifo-vs-kinesis-fanout-100-vs-5
  claim: Both SNS FIFO topics and Kinesis Streams support strictly ordered, many-to-many messaging. SNS FIFO topics allow ordered fan-out up to 100 subscribers; Kinesis Streams supports ordered fan-out up to 5 subscribers and is often used for analytics and anomaly detection.
  scope: ordered fan-out; maximum; FAQ wording.
  link: [up to 100 subscribers](../facts/sns.md#sns-faq-fifo-vs-kinesis-fanout-100-vs-5)
  link: [up to 5 subscribers](../facts/sns.md#sns-faq-fifo-vs-kinesis-fanout-100-vs-5)
sns-faq-four-phase-delivery-retry-policy
  claim: If a message cannot be delivered on the first attempt, Amazon SNS runs a 4-phase retry policy: retries with no delay, retries with minimum delay, retries according to a back-off model, and retries with maximum delay.
  scope: per delivery attempt.
  link: [4-phase retry policy](../facts/sns.md#sns-faq-four-phase-delivery-retry-policy)
  link: [retries according to a back-off model](../facts/sns.md#sns-faq-four-phase-delivery-retry-policy)
sns-faq-free-tier-1-million-requests-100000-http-1000-email
  claim: Each month, Amazon SNS customers incur no charges for the first 1 million requests, the first 100,000 notifications over HTTP, and the first 1,000 notifications over email.
  scope: per month.
  link: [first 1 million Amazon SNS requests](../facts/sns.md#sns-faq-free-tier-1-million-requests-100000-http-1000-email)
  link: [first 1,000 notifications over email](../facts/sns.md#sns-faq-free-tier-1-million-requests-100000-http-1000-email)
sns-faq-lambda-throttled-delivery-is-retried
  claim: If AWS Lambda throttles an Amazon SNS message, Amazon SNS retries the delivery attempts.
  scope: per delivery.
  link: [Lambda throttles](../facts/sns.md#sns-faq-lambda-throttled-delivery-is-retried)
  link: [retry the delivery](../facts/sns.md#sns-faq-lambda-throttled-delivery-is-retried)
sns-faq-message-filtering-subscribers-receive-subset
  claim: With message filtering, Amazon SNS topic subscribers can selectively receive only a subset of the messages they are interested in, instead of all messages published to the topic.
  scope: per subscription.
  link: [selectively receive only a subset](../facts/sns.md#sns-faq-message-filtering-subscribers-receive-subset)
  link: [receiving all messages published to a topic](../facts/sns.md#sns-faq-message-filtering-subscribers-receive-subset)
sns-faq-mq-for-existing-apps-standards-based-brokers
  claim: AWS recommends Amazon MQ when you move messaging of existing applications to the cloud quickly. Amazon MQ supports industry-standard APIs and protocols, so you can switch from a standards-based message broker without rewriting the messaging code.
  scope: Amazon MQ versus Amazon SNS.
  link: [existing applications](../facts/sns.md#sns-faq-mq-for-existing-apps-standards-based-brokers)
  link: [without rewriting the messaging code](../facts/sns.md#sns-faq-mq-for-existing-apps-standards-based-brokers)
sns-faq-only-topic-owner-can-change-permissions
  claim: Only the owner of the topic can change permissions for that topic.
  scope: per topic.
  link: [Only the owner of the topic](../facts/sns.md#sns-faq-only-topic-owner-can-change-permissions)
  link: [change permissions](../facts/sns.md#sns-faq-only-topic-owner-can-change-permissions)
sns-faq-order-attempted-but-network-issues-can-reorder
  claim: Amazon SNS attempts to deliver messages in the order they were published into the topic, but network issues could result in out-of-order messages at the subscriber end.
  scope: Amazon SNS message delivery.
  link: [attempt to deliver messages from the publisher](../facts/sns.md#sns-faq-order-attempted-but-network-issues-can-reorder)
  link: [out-of-order messages at the subscriber end](../facts/sns.md#sns-faq-order-attempted-but-network-issues-can-reorder)
sns-faq-price-per-million-requests-http-email
  claim: Amazon SNS users pay $0.50 per 1 million requests, $0.06 per 100,000 notification deliveries over HTTP, and $2.00 per 100,000 notification deliveries over email.
  scope: Amazon SNS.
  link: [$0.50 per 1 million](../facts/sns.md#sns-faq-price-per-million-requests-http-email)
  link: [$2.00 per 100,000 notification deliveries over email](../facts/sns.md#sns-faq-price-per-million-requests-http-email)
sns-faq-publish-triggers-delivery-to-all-subscribers
  claim: When a publisher publishes a message to a topic, Amazon SNS immediately delivers the message to all applicable subscribers.
  scope: per topic.
  link: [publish a message to the topic](../facts/sns.md#sns-faq-publish-triggers-delivery-to-all-subscribers)
  link: [all applicable subscribers](../facts/sns.md#sns-faq-publish-triggers-delivery-to-all-subscribers)
sns-faq-published-message-cannot-be-recalled
  claim: Once a message has been successfully published to a topic, it cannot be recalled.
  scope: per published message.
  link: [cannot be recalled](../facts/sns.md#sns-faq-published-message-cannot-be-recalled)
  link: [successfully published to a topic](../facts/sns.md#sns-faq-published-message-cannot-be-recalled)
sns-faq-raw-message-delivery-default-json-envelope
  claim: By default, SNS delivers messages encoded in JSON that provides metadata about the message and topic. You can opt in to raw delivery, where messages arrive exactly as published.
  scope: per subscription; default; not adjustable.
  link: [By default, messages are delivered encoded in JSON](../facts/sns.md#sns-faq-raw-message-delivery-default-json-envelope)
  link: [exactly as you published them](../facts/sns.md#sns-faq-raw-message-delivery-default-json-envelope)
sns-faq-same-account-sqs-subscription-needs-no-opt-in
  claim: The explicit opt-in confirmation steps are not required when you subscribe your Amazon SQS queue to your Amazon SNS topic and both are owned by the same AWS account.
  scope: per subscription.
  link: [opt-in](../facts/sns.md#sns-faq-same-account-sqs-subscription-needs-no-opt-in)
  link: [same AWS account](../facts/sns.md#sns-faq-same-account-sqs-subscription-needs-no-opt-in)
sns-faq-sns-messages-unstructured-six-target-types
  claim: SNS messages are unstructured and can be in any format. SNS forwards messages to six different types of targets: Lambda, SQS, HTTP/S endpoints, SMS, mobile push, and email.
  scope: EventBridge versus SNS.
  link: [unstructured and can be in any format](../facts/sns.md#sns-faq-sns-messages-unstructured-six-target-types)
  link: [six different types of targets](../facts/sns.md#sns-faq-sns-messages-unstructured-six-target-types)
sns-faq-sns-recommended-for-high-fan-out-thousands-or-millions
  claim: Amazon SNS is recommended for applications that need high fan out, which means thousands or millions of endpoints.
  scope: EventBridge versus SNS.
  link: [high fan out](../facts/sns.md#sns-faq-sns-recommended-for-high-fan-out-thousands-or-millions)
  link: [thousands or millions of endpoints](../facts/sns.md#sns-faq-sns-recommended-for-high-fan-out-thousands-or-millions)
sns-faq-sns-typical-latency-under-30-milliseconds
  claim: Amazon SNS typical latency is under 30 milliseconds.
  scope: per message.
  link: [under 30 milliseconds](../facts/sns.md#sns-faq-sns-typical-latency-under-30-milliseconds)
  link: [typical latency](../facts/sns.md#sns-faq-sns-typical-latency-under-30-milliseconds)
sns-faq-sqs-components-need-not-be-available-at-same-time
  claim: Amazon SQS lets distributed components of an application send and receive messages without requiring each component to be concurrently available.
  scope: SNS versus SQS.
  link: [without requiring each component to be concurrently available](../facts/sns.md#sns-faq-sqs-components-need-not-be-available-at-same-time)
  link: [send and receive messages](../facts/sns.md#sns-faq-sqs-components-need-not-be-available-at-same-time)
sns-faq-sqs-sns-decouple-microservices-new-apps
  claim: For brand new applications in the cloud AWS recommends Amazon SQS and Amazon SNS. You can use them to decouple and scale microservices, distributed systems, and serverless applications, and improve reliability.
  scope: Amazon SNS and SQS.
  link: [brand new applications in the cloud](../facts/sns.md#sns-faq-sqs-sns-decouple-microservices-new-apps)
  link: [decouple and scale microservices](../facts/sns.md#sns-faq-sqs-sns-decouple-microservices-new-apps)
sns-faq-subscriber-may-receive-duplicates
  claim: Most of the time each message is delivered to your application exactly once, but the distributed nature of Amazon SNS and transient network conditions could result in occasional duplicate messages at the subscriber end. Applications should be designed so that processing a message more than once does not create errors or inconsistencies.
  scope: Amazon SNS message delivery.
  link: [occasional, duplicate messages](../facts/sns.md#sns-faq-subscriber-may-receive-duplicates)
  link: [processing a message more than once](../facts/sns.md#sns-faq-subscriber-may-receive-duplicates)
sns-faq-subscription-confirmation-token-valid-2-days
  claim: The token in the confirmation message sent to an endpoint on a subscription request is valid for 2 days.
  scope: per subscription request; fixed; not adjustable.
  link: [valid for 2 days](../facts/sns.md#sns-faq-subscription-confirmation-token-valid-2-days)
  link: [confirmation message](../facts/sns.md#sns-faq-subscription-confirmation-token-valid-2-days)
sns-faq-topic-is-access-point-for-publish-and-subscribe
  claim: A topic is an access point that identifies a specific subject or event type, used to publish messages and to let clients subscribe for notifications.
  scope: per topic.
  link: [identifying a specific subject or event type](../facts/sns.md#sns-faq-topic-is-access-point-for-publish-and-subscribe)
  link: [allowing clients to subscribe for notifications](../facts/sns.md#sns-faq-topic-is-access-point-for-publish-and-subscribe)
sns-faq-topic-name-limit-256-characters
  claim: Topic names are limited to 256 characters. Alphanumeric characters plus hyphens (-) and underscores (_) are allowed.
  scope: per topic name; maximum; not adjustable.
  link: [limited to 256 characters](../facts/sns.md#sns-faq-topic-name-limit-256-characters)
  link: [Alphanumeric characters plus hyphens (-) and underscores (_)](../facts/sns.md#sns-faq-topic-name-limit-256-characters)
sns-faq-topic-supports-multiple-transports
  claim: A topic can support subscriptions and notification deliveries over multiple transports.
  scope: per topic.
  link: [multiple transports](../facts/sns.md#sns-faq-topic-supports-multiple-transports)
  link: [subscriptions and notification deliveries](../facts/sns.md#sns-faq-topic-supports-multiple-transports)
sns-fifo-archive-replay-fifo-topics-only
  claim: SNS provides a no-code message archiving and replay feature that is specifically designed for FIFO topics.
  scope: SNS FIFO topic.
  link: [no-code message archiving and replay feature](../facts/sns.md#sns-fifo-archive-replay-fifo-topics-only)
  link: [specifically designed for FIFO (First-In-First-Out) topics](../facts/sns.md#sns-fifo-archive-replay-fifo-topics-only)
sns-fifo-content-based-dedup-hash-of-body
  claim: If every message body is unique, you can enable content-based deduplication on an SNS FIFO topic and the subscribed SQS FIFO queues. SNS then hashes the message body to make the deduplication ID, so you don't need to set one. If a message is published with its own deduplication ID, the published ID overrides the generated one.
  scope: SNS FIFO topic and SQS FIFO queue; message body is unique for each published message.
  link: [enable content-based deduplication](../facts/sns.md#sns-fifo-content-based-dedup-hash-of-body)
  link: [hash value to use as the deduplication ID](../facts/sns.md#sns-fifo-content-based-dedup-hash-of-body)
  link: [the published deduplication ID overrides](../facts/sns.md#sns-fifo-content-based-dedup-hash-of-body)
sns-fifo-content-hash-excludes-attributes
  claim: With content-based deduplication on an SNS FIFO topic, SNS uses the message body to generate a unique hash value to use as the deduplication ID for each message; message attributes are not included in the hash calculation.
  scope: SNS FIFO topic, content-based deduplication.
  link: [not included in the hash calculation](../facts/sns.md#sns-fifo-content-hash-excludes-attributes)
  link: [Message attributes are not included](../facts/sns.md#sns-fifo-content-hash-excludes-attributes)
sns-fifo-deduplication-interval-5-minutes
  claim: If a message with a particular deduplication ID is successfully published to an SNS FIFO topic, any message published with the same deduplication ID within the five minute deduplication interval is accepted but not delivered. Deduplication applies to the entire topic when FifoThroughputScope is set to Topic, and to each individual message group when it is set to MessageGroup.
  scope: per SNS FIFO topic (FifoThroughputScope Topic) or per message group (MessageGroup); per deduplication ID; fixed; not adjustable.
  link: [five minute deduplication interval](../facts/sns.md#sns-fifo-deduplication-interval-5-minutes)
  link: [accepted but not delivered](../facts/sns.md#sns-fifo-deduplication-interval-5-minutes)
  say: five minutes
sns-fifo-exactly-once-lost-with-filtering
  claim: SNS FIFO topics and SQS FIFO queues provide exactly-once message delivery and processing as long as listed conditions are met; one condition is that the SNS subscription has no message filtering. When you configure message filtering, SNS FIFO topics support at-most-once delivery, as messages can be filtered out based on your subscription filter policies.
  scope: SNS FIFO topic to SQS FIFO queue; subscription has a filter policy.
  link: [at-most-once delivery](../facts/sns.md#sns-fifo-exactly-once-lost-with-filtering)
  link: [has no message filtering](../facts/sns.md#sns-fifo-exactly-once-lost-with-filtering)
sns-fifo-high-throughput-enable-messagegroup
  claim: To enable high throughput for an SNS FIFO topic, update the FifoThroughputScope attribute to MessageGroup; this can also be set when the topic is created.
  scope: per SNS FIFO topic.
  link: [update the FifoThroughputScope attribute to MessageGroup](../facts/sns.md#sns-fifo-high-throughput-enable-messagegroup)
  link: [FifoThroughputScope](../facts/sns.md#sns-fifo-high-throughput-enable-messagegroup)
sns-fifo-messagegroup-scope-not-reversible
  claim: Once a topic's FifoThroughputScope is set to MessageGroup, it cannot be reverted back to the Topic throughput.
  scope: per SNS FIFO topic.
  link: [cannot be reverted back to the Topic throughput](../facts/sns.md#sns-fifo-messagegroup-scope-not-reversible)
  link: [Once you've enabled a topic's FifoThroughputScope to MessageGroup](../facts/sns.md#sns-fifo-messagegroup-scope-not-reversible)
sns-fifo-replay-started-by-subscriber
  claim: A subscriber starts a replay and selects the time window of archived messages to be reprocessed to the subscribed endpoint.
  scope: SNS FIFO topic, subscription.
  link: [A subscriber initiates a replay](../facts/sns.md#sns-fifo-replay-started-by-subscriber)
  link: [selecting the time window for the messages](../facts/sns.md#sns-fifo-replay-started-by-subscriber)
sns-fifo-same-filtering-as-standard
  claim: SNS FIFO topics support the same message filtering capabilities as standard topics.
  scope: SNS FIFO topic.
  link: [the same message filtering capabilities](../facts/sns.md#sns-fifo-same-filtering-as-standard)
  link: [as standard topics](../facts/sns.md#sns-fifo-same-filtering-as-standard)
sns-fifo-sqs-both-store-redundantly-multiple-azs
  claim: SNS FIFO topics and SQS queues are durable. Both store messages redundantly across multiple Availability Zones and provide dead-letter queues for exceptional cases.
  scope: SNS FIFO topic and SQS queue.
  link: [store messages redundantly across multiple Availability Zones](../facts/sns.md#sns-fifo-sqs-both-store-redundantly-multiple-azs)
  link: [FIFO topics and Amazon SQS queues are durable](../facts/sns.md#sns-fifo-sqs-both-store-redundantly-multiple-azs)
sns-fifo-sqs-server-error-retries-100015
  claim: When server-side errors occur, SNS FIFO topics retry the failed deliveries up to 100,015 times over 23 days.
  scope: per failed delivery from an SNS FIFO topic; server-side errors; maximum; not adjustable.
  link: [up to 100,015 times](../facts/sns.md#sns-fifo-sqs-server-error-retries-100015)
  link: [over 23 days](../facts/sns.md#sns-fifo-sqs-server-error-retries-100015)
sns-fifo-standard-queue-subscriber-lowers-cost
  claim: For workloads that accept best-effort ordering and at-least-once delivery, subscribing SQS standard queues to an SNS FIFO topic lowers costs and lets you share queues with workloads that do not use FIFO.
  scope: SNS FIFO topic to SQS standard queue; workload tolerates best-effort ordering and at-least-once delivery.
  link: [lets you lower costs](../facts/sns.md#sns-fifo-standard-queue-subscriber-lowers-cost)
  link: [sharing queues across workloads that don't use FIFO](../facts/sns.md#sns-fifo-standard-queue-subscriber-lowers-cost)
sns-fifo-throughput-scope-topic-limits
  claim: SNS FIFO topics have a maximum per message group limit of 300 messages per second; when FifoThroughputScope is set to Topic, per topic throughput defaults to 3,000 messages per second or 20MB per second, whichever comes first.
  scope: per message group (300); per topic when FifoThroughputScope is Topic (3,000 messages or 20MB per second); default; adjustable; Whichever of 3,000 messages or 20MB per second comes first, when FifoThroughputScope is set to Topic..
  link: [300 messages per second](../facts/sns.md#sns-fifo-throughput-scope-topic-limits)
  link: [3,000 messages per second](../facts/sns.md#sns-fifo-throughput-scope-topic-limits)
  link: [20MB per second](../facts/sns.md#sns-fifo-throughput-scope-topic-limits)
sns-fifo-to-lambda-needs-sqs-in-between
  claim: To fan out messages from an SNS FIFO topic to Lambda functions, first subscribe SQS FIFO or standard queues to the topic, then configure the queues to trigger the functions.
  scope: SNS FIFO topic to Lambda.
  link: [subscribe Amazon SQS FIFO or standard queues](../facts/sns.md#sns-fifo-to-lambda-needs-sqs-in-between)
  link: [configure the queues to trigger the functions](../facts/sns.md#sns-fifo-to-lambda-needs-sqs-in-between)
sns-fifo-topic-cannot-deliver-to-customer-managed-endpoints
  claim: An SNS FIFO topic cannot deliver messages to customer managed endpoints such as email addresses, mobile apps, SMS phone numbers or HTTP(S) endpoints. Trying to subscribe them results in errors.
  scope: SNS FIFO topic.
  link: [can't deliver messages to customer managed endpoints](../facts/sns.md#sns-fifo-topic-cannot-deliver-to-customer-managed-endpoints)
  link: [result in errors](../facts/sns.md#sns-fifo-topic-cannot-deliver-to-customer-managed-endpoints)
sns-fifo-topic-delivers-to-sqs-standard-and-fifo
  claim: An SNS FIFO topic supports delivery to both SQS standard queues and SQS FIFO queues.
  scope: SNS FIFO topic.
  link: [both Amazon SQS standard and FIFO queues](../facts/sns.md#sns-fifo-topic-delivers-to-sqs-standard-and-fifo)
  link: [data consistency in near real-time](../facts/sns.md#sns-fifo-topic-delivers-to-sqs-standard-and-fifo)
sns-fifo-topic-name-needs-fifo-suffix
  claim: The name of an SNS FIFO topic must end with .fifo.
  scope: SNS FIFO topic name.
  link: [add .fifo to the end of the name](../facts/sns.md#sns-fifo-topic-name-needs-fifo-suffix)
  link: [For a FIFO topic](../facts/sns.md#sns-fifo-topic-name-needs-fifo-suffix)
sns-filter-body-scope-needs-json-payload
  claim: Filter policies for the message body assume that the message payload is a well-formed JSON object.
  scope: SNS subscription, FilterPolicyScope MessageBody.
  link: [well-formed JSON object](../facts/sns.md#sns-filter-body-scope-needs-json-payload)
  link: [Filter policies for the message body](../facts/sns.md#sns-filter-body-scope-needs-json-payload)
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
sns-filter-policy-change-up-to-15-minutes
  claim: Additions or changes to an SNS subscription filter policy require up to 15 minutes to fully take effect.
  scope: per subscription filter policy change; maximum; not adjustable; Eventual consistency..
  link: [up to 15 minutes](../facts/sns.md#sns-filter-policy-change-up-to-15-minutes)
  say: fifteen minutes
sns-filter-policy-complexity-150
  claim: The total combination of values in an SNS filter policy must not exceed 150; the total is the product of the number of values in each array in the policy.
  scope: per filter policy; product of the number of values in each array; maximum; not adjustable.
  link: [must not exceed 150](../facts/sns.md#sns-filter-policy-complexity-150)
sns-filter-policy-max-keys
  claim: An SNS subscription filter policy can have a maximum of five keys.
  scope: per filter policy; maximum; not adjustable.
  link: [maximum of five keys](../facts/sns.md#sns-filter-policy-max-keys)
  say: five keys
sns-filter-policy-max-size-256kb
  claim: The maximum size of an SNS filter policy is 256 KB.
  scope: per filter policy; maximum; not adjustable.
  link: [256 KB](../facts/sns.md#sns-filter-policy-max-size-256kb)
  say: two hundred fifty-six kilobytes
sns-filter-policy-quota-200-per-topic-10000-per-account
  claim: By default, you can have up to 200 filter policies per SNS topic and 10,000 filter policies per AWS account; the quota can be increased with AWS Service Quotas.
  scope: per topic, and per AWS account; default; adjustable.
  link: [200 filter policies per topic](../facts/sns.md#sns-filter-policy-quota-200-per-topic-10000-per-account)
  link: [10,000 filter policies per AWS account](../facts/sns.md#sns-filter-policy-quota-200-per-topic-10000-per-account)
sns-filter-scope-attributes-default-or-body
  claim: The FilterPolicyScope subscription attribute is MessageAttributes by default, which applies the filter policy to message attributes. MessageBody applies the filter policy to the message body.
  scope: SNS subscription, FilterPolicyScope; default; adjustable.
  link: [message attributes (default setting)](../facts/sns.md#sns-filter-scope-attributes-default-or-body)
  link: [Applies the filter policy to the message body](../facts/sns.md#sns-filter-scope-attributes-default-or-body)
sns-lambda-invoked-asynchronously
  claim: SNS invokes Lambda functions asynchronously.
  scope: SNS subscription to Lambda.
  link: [invokes AWS Lambda functions asynchronously](../facts/sns.md#sns-lambda-invoked-asynchronously)
  link: [Amazon SNS invokes](../facts/sns.md#sns-lambda-invoked-asynchronously)
sns-lambda-subscribe-to-topics-in-other-accounts
  claim: You can subscribe a Lambda function to SNS topics in the same account or in other AWS accounts.
  scope: Lambda subscription to an SNS standard topic.
  link: [same account or in other AWS accounts](../facts/sns.md#sns-lambda-subscribe-to-topics-in-other-accounts)
  link: [subscribe your function to topics](../facts/sns.md#sns-lambda-subscribe-to-topics-in-other-accounts)
sns-lambda-triggers-standard-topics-only
  claim: Lambda supports SNS triggers for standard SNS topics only. FIFO topics are not supported as a direct Lambda trigger.
  scope: Lambda SNS trigger.
  link: [standard SNS topics only](../facts/sns.md#sns-lambda-triggers-standard-topics-only)
  link: [FIFO topics aren't supported](../facts/sns.md#sns-lambda-triggers-standard-topics-only)
sns-message-attributes-sqs-raw-delivery-max-10
  claim: For SQS subscriptions with Raw Message Delivery enabled, a maximum of 10 message attributes can be sent; more than 10 attributes require Raw Message Delivery to be disabled, and a message with more than 10 attributes is discarded as a client side error.
  scope: per message sent to an SQS subscription with Raw Message Delivery enabled; maximum; not adjustable; Applies when Raw Message Delivery is enabled..
  link: [a maximum of 10 message attributes](../facts/sns.md#sns-message-attributes-sqs-raw-delivery-max-10)
  say: ten message attributes
sns-message-size-default-256kib
  claim: By default, all existing and newly created SNS topics have a MaximumMessageSize of 262,144 bytes (256 KiB).
  scope: per topic (MaximumMessageSize topic attribute); default; adjustable; MaximumMessageSize can be set between 1,024 and 1,048,576 bytes..
  link: [256 KiB](../facts/sns.md#sns-message-size-default-256kib)
  link: [262,144 bytes](../facts/sns.md#sns-message-size-default-256kib)
  say: two hundred fifty-six kibibytes
sns-message-size-optin-1mib
  claim: Amazon SNS supports message payloads up to 1 MiB (1,048,576 bytes) when the MaximumMessageSize topic attribute is configured; without that setting topics accept messages up to 256 KiB. To set the attribute above 256 KiB, the topic must have 100 or fewer total subscriptions, all of supported endpoint types (Amazon Data Firehose, Amazon SQS or AWS Lambda).
  scope: per topic (MaximumMessageSize topic attribute); maximum; not adjustable; Opt-in per topic; the default stays 256 KiB. Above 256 KiB only with 100 or fewer subscriptions, all Amazon Data Firehose, Amazon SQS or AWS Lambda..
  link: [1 MiB (1,048,576 bytes)](../facts/sns.md#sns-message-size-optin-1mib)
  link: [1 MiB](../facts/sns.md#sns-message-size-optin-1mib)
  link: [100 or fewer total subscriptions](../facts/sns.md#sns-message-size-optin-1mib)
  say: one mebibyte | one hundred or fewer subscriptions
sns-message-size-optin-endpoints-and-100-subscriptions
  claim: Topics with MaximumMessageSize set above 256 KiB support Amazon Data Firehose, Amazon SQS and AWS Lambda subscriptions, with up to 100 total subscriptions per topic.
  scope: per topic with MaximumMessageSize above 256 KiB; maximum; Applies only when MaximumMessageSize is above 256 KiB..
  link: [up to 100 total subscriptions per topic](../facts/sns.md#sns-message-size-optin-endpoints-and-100-subscriptions)
  link: [Amazon Data Firehose, Amazon SQS, and AWS Lambda subscriptions](../facts/sns.md#sns-message-size-optin-endpoints-and-100-subscriptions)
sns-pricing-archive-min-1-day-storage
  claim: Data archived by Amazon SNS message archiving is billed for a minimum of 1 day of storage, and message replay is billed at the existing FIFO API Requests and Payload data rates.
  scope: per archived data; FIFO topic archiving and replay; minimum.
  link: [a minimum of 1 day of storage](../facts/sns.md#sns-pricing-archive-min-1-day-storage)
  link: [billed at the existing FIFO API Requests and Payload data rates](../facts/sns.md#sns-pricing-archive-min-1-day-storage)
sns-pricing-attribute-filtering-free
  claim: Attribute-based message filtering in Amazon SNS is free, while payload-based message filtering is billed by the total outbound payload data scanned for each subscription with an active filter policy.
  scope: per subscription with an active filter policy.
  link: [Attribute-based message filtering is free](../facts/sns.md#sns-pricing-attribute-filtering-free)
  link: [total amount of outbound payload data scanned](../facts/sns.md#sns-pricing-attribute-filtering-free)
sns-pricing-data-transfer-in-free
  claim: Data transferred into Amazon SNS is free of charge.
  scope: data transfer into Amazon SNS.
  link: [is free of charge](../facts/sns.md#sns-pricing-data-transfer-in-free)
  link: [Data transferred into Amazon SNS](../facts/sns.md#sns-pricing-data-transfer-in-free)
sns-pricing-fifo-min-1kb-message
  claim: SNS FIFO topic pricing is based on the number of published messages, the number of subscribed messages and their payload data; in that part of the pricing page, each message from 1KB to the topic's maximum message size (up to 1 MiB) is billed as one message, and any message smaller than 1KB is rounded up to 1KB.
  scope: per message published to a FIFO topic; minimum.
  link: [rounded up to 1KB](../facts/sns.md#sns-pricing-fifo-min-1kb-message)
  link: [Any message smaller than 1KB](../facts/sns.md#sns-pricing-fifo-min-1kb-message)
sns-pricing-fifo-subscription-messages
  claim: For Amazon SNS FIFO topics, subscription messages are calculated by multiplying the number of published messages by the number of subscriptions, and both filtered and delivered messages count.
  scope: per FIFO topic.
  link: [multiplying the number of published messages](../facts/sns.md#sns-pricing-fifo-subscription-messages)
  link: [Both filtered and delivered messages count](../facts/sns.md#sns-pricing-fifo-subscription-messages)
sns-pricing-free-usage-not-accumulated
  claim: Amazon SNS free usage is calculated each month across all Regions and applied to the bill automatically; free usage does not accumulate.
  scope: per month, across all Regions.
  link: [calculated each month across all regions](../facts/sns.md#sns-pricing-free-usage-not-accumulated)
  link: [free usage does not accumulate](../facts/sns.md#sns-pricing-free-usage-not-accumulated)
sns-pricing-no-upfront-pay-for-use
  claim: With Amazon SNS there are no upfront fees, no required minimum commitments and no long-term contracts.
  scope: Amazon SNS account usage.
  link: [no upfront fees](../facts/sns.md#sns-pricing-no-upfront-pay-for-use)
  link: [no required minimum commitments](../facts/sns.md#sns-pricing-no-upfront-pay-for-use)
sns-pricing-sqs-lambda-no-delivery-charge
  claim: Amazon SNS does not charge for per-message notification delivery when delivering messages to Amazon SQS and AWS Lambda, but it does charge for the amount of data transferred from SNS to SQS or Lambda.
  scope: per delivery to Amazon SQS and AWS Lambda endpoints; Data transfer is charged at Internet Data Transfer rates..
  link: [does not charge for per-message notification delivery](../facts/sns.md#sns-pricing-sqs-lambda-no-delivery-charge)
  link: [does charge for the amount of data transferred](../facts/sns.md#sns-pricing-sqs-lambda-no-delivery-charge)
sns-pricing-standard-delivery-64kb-chunk
  claim: Except for SMS messages, each 64KB chunk of delivered data is billed as 1 delivery; for example, a single notification with a 1 MiB payload is billed as 16 deliveries.
  scope: per notification delivery, Standard topics; SMS excluded; SMS messages are excluded..
  link: [64KB chunk](../facts/sns.md#sns-pricing-standard-delivery-64kb-chunk)
  link: [16 deliveries](../facts/sns.md#sns-pricing-standard-delivery-64kb-chunk)
  say: sixty-four kilobyte chunk
sns-pricing-standard-publish-64kb-chunk
  claim: SNS Standard topic pricing is based on the number of monthly API requests and the number of deliveries. For API requests, each 64KB chunk of published data is billed as 1 request; for example, a single publish with a 1 MiB payload is billed as 16 requests.
  scope: per publish, Standard topics.
  link: [64KB chunk](../facts/sns.md#sns-pricing-standard-publish-64kb-chunk)
  link: [16 requests](../facts/sns.md#sns-pricing-standard-publish-64kb-chunk)
  say: sixty-four kilobyte chunk
sns-protocol-restriction-needs-custom-policy
  claim: To restrict the delivery protocol of a topic to HTTPS you must write a custom policy, because the AddPermission action does not let you specify protocol restrictions.
  scope: SNS topic access policy.
  link: [you must create a custom policy](../facts/sns.md#sns-protocol-restriction-needs-custom-policy)
  link: [does not allow you to specify protocol restrictions](../facts/sns.md#sns-protocol-restriction-needs-custom-policy)
sns-publish-batch-max-10-messages
  claim: With the Amazon SNS PublishBatch API you can publish up to 10 messages in a single API request, to either Standard or FIFO topics.
  scope: per PublishBatch API request; maximum; not adjustable.
  link: [up to 10 messages](../facts/sns.md#sns-publish-batch-max-10-messages)
  say: ten messages
sns-publish-batch-total-size-max-message-size
  claim: The total aggregate size of all messages in a single SNS PublishBatch API request cannot exceed the topic's configured MaximumMessageSize, which is 262,144 bytes by default.
  scope: per PublishBatch API request, all messages together; maximum; adjustable; The limit is the topic's MaximumMessageSize..
  link: [default 262,144 bytes](../facts/sns.md#sns-publish-batch-total-size-max-message-size)
sns-publish-sends-message-to-each-subscribed-queue
  claim: You can subscribe one or more SQS queues to an SNS topic. When you publish a message to the topic, SNS sends the message to each subscribed queue.
  scope: SNS topic and SQS queues.
  link: [subscribe one or more Amazon SQS queues](../facts/sns.md#sns-publish-sends-message-to-each-subscribed-queue)
  link: [sends the message to each subscribed queue](../facts/sns.md#sns-publish-sends-message-to-each-subscribed-queue)
sns-publish-size-counts-body-and-attributes
  claim: When a message is published, Amazon SNS checks the combined size of the message body and message attributes against the topic's MaximumMessageSize, and returns an InvalidParameter error if the size is exceeded.
  scope: per published message.
  link: [message body and message attributes](../facts/sns.md#sns-publish-size-counts-body-and-attributes)
  link: [returns an InvalidParameter error](../facts/sns.md#sns-publish-size-counts-body-and-attributes)
sns-publish-throttle-all-other-regions
  claim: In the SNS Publish API throttling table, all other supported Regions have 300 messages per second for standard topics and 3,000 messages per second for FIFO topics; SNS FIFO per-topic limits exceed this default per-account limit when FifoThroughputScope is set to MessageGroup.
  scope: per account, per Region (all other supported Regions); default; adjustable; A soft limit increase can be requested through an SNS quota increase request..
  link: [300 messages per second](../facts/sns.md#sns-publish-throttle-all-other-regions)
  link: [3,000 messages per second](../facts/sns.md#sns-publish-throttle-all-other-regions)
sns-publish-throttle-us-east-1
  claim: In the SNS Publish API throttling table, US East (N. Virginia) has 30,000 messages per second for standard topics and 30,000 messages per second for FIFO topics; SNS FIFO per-topic limits exceed this default per-account limit when FifoThroughputScope is set to MessageGroup.
  scope: per account, per Region (US East (N. Virginia)); default; adjustable; A soft limit increase can be requested through an SNS quota increase request..
  link: [30,000 messages per second](../facts/sns.md#sns-publish-throttle-us-east-1)
sns-published-messages-stored-across-servers-data-centers
  claim: SNS stores published messages across multiple, geographically separated servers and data centers.
  scope: SNS topic.
  link: [Published messages are stored across](../facts/sns.md#sns-published-messages-stored-across-servers-data-centers)
  link: [geographically separated servers and data centers](../facts/sns.md#sns-published-messages-stored-across-servers-data-centers)
sns-publishers-send-to-topic-asynchronously
  claim: Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical access point and communication channel.
  scope: SNS topic.
  link: [Publishers communicate asynchronously with subscribers](../facts/sns.md#sns-publishers-send-to-topic-asynchronously)
  link: [logical access point and communication channel](../facts/sns.md#sns-publishers-send-to-topic-asynchronously)
sns-push-mechanism-no-polling
  claim: SNS lets applications send time-critical messages to multiple subscribers through a push mechanism, so subscribers do not need to check or poll for updates.
  scope: SNS topic.
  link: [through a “push” mechanism](../facts/sns.md#sns-push-mechanism-no-polling)
  link: [removes the need to check or “poll”](../facts/sns.md#sns-push-mechanism-no-polling)
sns-queue-policy-sourcearn-limits-to-one-topic
  claim: An SQS queue policy that uses the aws:SourceArn condition restricts access to the queue based on the source of the messages, so that only messages originating from the specified SNS topic are allowed to be delivered to the queue.
  scope: SQS queue policy for SNS delivery.
  link: [aws:SourceArn condition](../facts/sns.md#sns-queue-policy-sourcearn-limits-to-one-topic)
  link: [restrict access to the SQS queue](../facts/sns.md#sns-queue-policy-sourcearn-limits-to-one-topic)
sns-quota-subscriptions-per-topic
  claim: The default quota is 12,500,000 subscriptions per standard topic and 100 subscriptions per FIFO topic; for Firehose delivery streams the quota is 5 per topic, per subscription owner.
  scope: per topic (standard; FIFO); Firehose: per topic, per subscription owner; default; adjustable.
  link: [12,500,000 per topic](../facts/sns.md#sns-quota-subscriptions-per-topic)
  link: [100 per topic](../facts/sns.md#sns-quota-subscriptions-per-topic)
  link: [5 per topic, per subscription owner](../facts/sns.md#sns-quota-subscriptions-per-topic)
sns-quota-topics-per-account
  claim: The default quota is 100,000 standard topics per account and 1,000 FIFO topics per account.
  scope: per account (standard topics; FIFO topics); default; adjustable.
  link: [100,000 per account](../facts/sns.md#sns-quota-topics-per-account)
  link: [1,000 per account](../facts/sns.md#sns-quota-topics-per-account)
sns-raw-delivery-firehose-body-only
  claim: With raw message delivery enabled for Firehose endpoints, the message body is delivered; message attributes are not sent.
  scope: SNS subscription to Firehose; RawMessageDelivery is true.
  link: [the message body is delivered](../facts/sns.md#sns-raw-delivery-firehose-body-only)
  link: [message attributes, it won't be sent](../facts/sns.md#sns-raw-delivery-firehose-body-only)
sns-raw-delivery-http-header-added
  claim: With raw message delivery enabled for HTTP/S endpoints, SNS adds the HTTP header x-amz-sns-rawdelivery with the value true, which shows that the message was published without JSON formatting.
  scope: SNS subscription to HTTP/S; RawMessageDelivery is true.
  link: [x-amz-sns-rawdelivery](../facts/sns.md#sns-raw-delivery-http-header-added)
  link: [published without JSON formatting](../facts/sns.md#sns-raw-delivery-http-header-added)
sns-raw-delivery-set-with-subscription-attribute
  claim: To enable raw message delivery with an AWS SDK, call the SetSubscriptionAttribute API action and set the RawMessageDelivery attribute to true.
  scope: SNS subscription.
  link: [SetSubscriptionAttribute API action](../facts/sns.md#sns-raw-delivery-set-with-subscription-attribute)
  link: [RawMessageDelivery attribute to true](../facts/sns.md#sns-raw-delivery-set-with-subscription-attribute)
sns-raw-delivery-sqs-strips-sns-metadata
  claim: With raw message delivery enabled for SQS endpoints, any SNS metadata is stripped from the published message and the message is sent as is.
  scope: SNS subscription to SQS; RawMessageDelivery is true.
  link: [any Amazon SNS metadata is stripped](../facts/sns.md#sns-raw-delivery-sqs-strips-sns-metadata)
  link: [the message is sent as is](../facts/sns.md#sns-raw-delivery-sqs-strips-sns-metadata)
sns-retry-aws-managed-total-attempts
  claim: For AWS managed endpoints (AWS Lambda and Amazon SQS), the SNS delivery policy makes 100,015 attempts in total, over 23 days: 3 immediate retries, 2 pre-backoff retries 1 second apart, 10 backoff retries from 1 second to 20 seconds, and 100,000 post-backoff retries 20 seconds apart.
  scope: per message delivery to an AWS managed endpoint (Lambda, SQS); default; not adjustable; Only HTTP/S delivery policies can be changed..
  link: [100,015 times](../facts/sns.md#sns-retry-aws-managed-total-attempts)
  link: [over 23 days](../facts/sns.md#sns-retry-aws-managed-total-attempts)
sns-retry-customer-managed-total-attempts
  claim: For customer managed endpoints (SMTP, SMS and mobile push), the SNS delivery policy makes 50 attempts in total, over 6 hours.
  scope: per message delivery to a customer managed endpoint (SMTP, SMS, mobile push); default; not adjustable; Only HTTP/S delivery policies can be changed..
  link: [50 attempts](../facts/sns.md#sns-retry-customer-managed-total-attempts)
  link: [over 6 hours](../facts/sns.md#sns-retry-customer-managed-total-attempts)
sns-retry-exhausted-discards-unless-dlq
  claim: When the SNS delivery policy is exhausted, Amazon SNS stops retrying and discards the message, unless a dead-letter queue is attached to the subscription.
  scope: per subscription delivery.
  link: [stops retrying the delivery and discards the message](../facts/sns.md#sns-retry-exhausted-discards-unless-dlq)
  link: [a dead-letter queue is attached to the subscription](../facts/sns.md#sns-retry-exhausted-discards-unless-dlq)
sns-retry-http-total-retry-time-max
  claim: The total policy retry time for an SNS HTTP/S endpoint cannot be greater than 3,600 seconds; this is a hard limit and cannot be increased.
  scope: per HTTP/S endpoint delivery policy; maximum; not adjustable.
  link: [3,600 seconds](../facts/sns.md#sns-retry-http-total-retry-time-max)
  say: thirty-six hundred seconds
sns-retry-only-http-policy-customizable
  claim: Except for HTTP/S, you cannot change the SNS-defined delivery policies; only HTTP/S supports custom delivery policies.
  scope: per delivery protocol.
  link: [Only HTTP/S supports custom policies](../facts/sns.md#sns-retry-only-http-policy-customizable)
  link: [you can't change Amazon SNS-defined delivery policies](../facts/sns.md#sns-retry-only-http-policy-customizable)
sns-retry-retryable-errors-5xx-429
  claim: For HTTP/S delivery, Amazon SNS treats all 5XX errors and 429 errors as retryable; all other errors are permanent failures and are not retried.
  scope: SNS HTTP/S delivery policy.
  link: [all 5XX errors and 429](../facts/sns.md#sns-retry-retryable-errors-5xx-429)
  link: [permanent failures and retries will not be attempted](../facts/sns.md#sns-retry-retryable-errors-5xx-429)
sns-s3-publish-needs-topic-policy-for-s3-principal
  claim: To allow an S3 bucket from another AWS account to publish event notifications to your SNS topic, you configure the topic's access policy: the policy should grant the Amazon S3 service (s3.amazonaws.com) the permissions to publish to the topic, and the SourceAccount condition ensures that only the specified AWS account, which owns the bucket, can publish notifications to the topic.
  scope: SNS topic access policy, S3 event notifications from a bucket in another account.
  link: [grant the Amazon S3 service (s3.amazonaws.com)](../facts/sns.md#sns-s3-publish-needs-topic-policy-for-s3-principal)
  link: [SourceAccount condition](../facts/sns.md#sns-s3-publish-needs-topic-policy-for-s3-principal)
sns-sqs-envelope-contains-subject-message-metadata
  claim: When SNS delivers to a subscribed SQS queue, the SQS message holds the subject and message that were published plus metadata about the message, in a JSON document. If raw message delivery is enabled for the SQS endpoint, any SNS metadata is stripped and the message is sent as is.
  scope: SNS to SQS subscription; the JSON document applies when raw message delivery is not enabled; with raw message delivery the message is sent as is.
  link: [subject and message that were published](../facts/sns.md#sns-sqs-envelope-contains-subject-message-metadata)
  link: [metadata about the message in a JSON document](../facts/sns.md#sns-sqs-envelope-contains-subject-message-metadata)
  link: [any Amazon SNS metadata is stripped](../facts/sns.md#sns-sqs-envelope-contains-subject-message-metadata)
sns-sqs-queue-needs-policy-allowing-topic
  claim: To publish from an SNS topic to an SQS queue you must explicitly set a policy on the SQS queue that allows messages to be sent from the SNS topic.
  scope: SNS topic to SQS queue.
  link: [set a policy on the Amazon SQS queue](../facts/sns.md#sns-sqs-queue-needs-policy-allowing-topic)
  link: [sent from the Amazon SNS topic](../facts/sns.md#sns-sqs-queue-needs-policy-allowing-topic)
sns-sqs-together-instant-notice-and-later-processing
  claim: When SNS and SQS are used together, messages reach applications that need instant notification of an event, and the messages also persist in an SQS queue for other applications to process later.
  scope: SNS topic with SQS queue subscribers.
  link: [applications that need instant notification of an event](../facts/sns.md#sns-sqs-together-instant-notice-and-later-processing)
  link: [persist in an Amazon SQS queue](../facts/sns.md#sns-sqs-together-instant-notice-and-later-processing)
sns-sse-backlogged-messages-not-encrypted
  claim: A message is encrypted only if it is sent after encryption of the topic is enabled. SNS does not encrypt backlogged messages.
  scope: SNS topic when SSE is enabled.
  link: [encrypted only if it is sent after](../facts/sns.md#sns-sse-backlogged-messages-not-encrypted)
  link: [doesn't encrypt backlogged messages](../facts/sns.md#sns-sse-backlogged-messages-not-encrypted)
sns-sse-does-not-encrypt-metadata
  claim: SNS server-side encryption encrypts the body of a message. It does not encrypt topic metadata, message metadata, the data protection policy or per-topic metrics.
  scope: SNS topic with SSE.
  link: [SSE encrypts the body of a message](../facts/sns.md#sns-sse-does-not-encrypt-metadata)
  link: [Topic metadata (topic name and attributes)](../facts/sns.md#sns-sse-does-not-encrypt-metadata)
  link: [Per-topic metrics](../facts/sns.md#sns-sse-does-not-encrypt-metadata)
sns-sse-keys-managed-in-kms
  claim: SNS server-side encryption protects the contents of messages in topics using keys managed in AWS KMS. It encrypts messages as soon as SNS receives them and decrypts them only when they are sent.
  scope: SNS topic.
  link: [using keys managed in AWS Key Management Service](../facts/sns.md#sns-sse-keys-managed-in-kms)
  link: [only decrypted when they are sent](../facts/sns.md#sns-sse-keys-managed-in-kms)
sns-sse-requests-need-https-sigv4
  claim: All requests to SNS topics with SSE enabled must use HTTPS and Signature Version 4.
  scope: SNS topic with SSE.
  link: [must use HTTPS and Signature Version 4](../facts/sns.md#sns-sse-requests-need-https-sigv4)
  link: [All requests to topics with SSE enabled](../facts/sns.md#sns-sse-requests-need-https-sigv4)
sns-sse-symmetric-keys-only
  claim: SNS supports only symmetric encryption KMS keys. You cannot use any other type of KMS key to encrypt SNS resources.
  scope: SNS topic SSE.
  link: [only supports symmetric encryption KMS keys](../facts/sns.md#sns-sse-symmetric-keys-only)
  link: [cannot use any other type of KMS key](../facts/sns.md#sns-sse-symmetric-keys-only)
sns-sse-topic-to-encrypted-queue-needs-cmk-policy
  claim: For SNS to send messages to an encrypted SQS queue, the customer managed key of the queue must have a policy statement that grants the SNS service principal access to the AWS KMS actions GenerateDataKey and Decrypt.
  scope: SNS topic to SQS queue encrypted with a customer managed key.
  link: [grants Amazon SNS service-principal access](../facts/sns.md#sns-sse-topic-to-encrypted-queue-needs-cmk-policy)
  link: [API actions GenerateDataKey and Decrypt](../facts/sns.md#sns-sse-topic-to-encrypted-queue-needs-cmk-policy)
sns-standard-vs-fifo-topic-features
  claim: FIFO topics ensure strict message ordering, message grouping and deduplication, and let FIFO and standard queues subscribe. Standard topics fit cases where ordering and possible duplication are not critical, and they support all delivery protocols.
  scope: SNS topic types.
  link: [strict message ordering, message grouping, and deduplication](../facts/sns.md#sns-standard-vs-fifo-topic-features)
  link: [supporting all delivery protocols](../facts/sns.md#sns-standard-vs-fifo-topic-features)
sns-supports-a2a-and-a2p
  claim: SNS supports application-to-application (A2A) messaging and application-to-person (A2P) messaging, so it can send messages between applications or directly to mobile phones, email addresses and more.
  scope: SNS.
  link: [Application-to-Application (A2A)](../facts/sns.md#sns-supports-a2a-and-a2p)
  link: [Application-to-Person (A2P) messaging](../facts/sns.md#sns-supports-a2a-and-a2p)
sns-topic-private-by-default
  claim: By default, SNS topics are created with no permissions, so they are private and only accessible to the account that created them.
  scope: new SNS topic; default; adjustable.
  link: [created with no permissions](../facts/sns.md#sns-topic-private-by-default)
  link: [private and only accessible to the account](../facts/sns.md#sns-topic-private-by-default)
sns-topic-type-and-name-fixed-after-creation
  claim: After you create an SNS topic you cannot change its type (standard or FIFO) or its name.
  scope: SNS topic.
  link: [you can't change the topic type or name](../facts/sns.md#sns-topic-type-and-name-fixed-after-creation)
  link: [you choose a topic type (standard or FIFO)](../facts/sns.md#sns-topic-type-and-name-fixed-after-creation)
sns-uses-https-to-forward-to-sqs
  claim: When an SQS queue is subscribed to an SNS topic, SNS uses HTTPS to forward messages to SQS.
  scope: SNS to SQS subscription.
  link: [Amazon SNS uses HTTPS to forward messages](../facts/sns.md#sns-uses-https-to-forward-to-sqs)
  link: [forward messages to Amazon SQS](../facts/sns.md#sns-uses-https-to-forward-to-sqs)
sns-vpc-endpoint-publish-without-public-internet
  claim: If you use Amazon VPC to host your AWS resources, you can create a private connection between your VPC and SNS, and with this connection you can publish messages to SNS topics without sending them through the public internet.
  scope: VPC to SNS; interface VPC endpoint for Amazon SNS.
  link: [without sending them through the public internet](../facts/sns.md#sns-vpc-endpoint-publish-without-public-internet)
  link: [publish messages to your Amazon SNS topics](../facts/sns.md#sns-vpc-endpoint-publish-without-public-internet)
sns-vpc-interface-endpoint-no-igw-nat-vpn
  claim: To connect a VPC to SNS you define an interface VPC endpoint. The endpoint does not require an internet gateway, a NAT instance or a VPN connection.
  scope: VPC to SNS.
  link: [It doesn't require an internet gateway](../facts/sns.md#sns-vpc-interface-endpoint-no-igw-nat-vpn)
  link: [reliable, scalable connectivity to Amazon SNS](../facts/sns.md#sns-vpc-interface-endpoint-no-igw-nat-vpn)
sns-wa-high-throughput-push-many-to-many-fan-out
  claim: SNS is an effective solution when you need high-throughput, push-based, many-to-many messaging; publisher systems can fan out messages to a large number of subscriber endpoints for parallel processing.
  scope: Well-Architected reliability pillar, REL04-BP02 loosely coupled dependencies.
  link: [high-throughput, push-based, many-to-many messaging](../facts/sns.md#sns-wa-high-throughput-push-many-to-many-fan-out)
  link: [fan out messages to a large number](../facts/sns.md#sns-wa-high-throughput-push-many-to-many-fan-out)
sns-with-sqs-prevents-loss-for-offline-subscribers
  claim: To prevent message loss when subscribers are offline, integrate SNS with SQS queues, which keeps delivery consistent.
  scope: SQS developer guide overview (SQS, SNS and Amazon MQ).
  link: [when subscribers are offline](../facts/sns.md#sns-with-sqs-prevents-loss-for-offline-subscribers)
  link: [integrating Amazon SNS with Amazon SQS queue messages](../facts/sns.md#sns-with-sqs-prevents-loss-for-offline-subscribers)
sqs-auto-deletes-after-retention-period
  claim: SQS automatically deletes messages that have been in a queue for more than the maximum message retention period.
  scope: SQS queue.
  link: [automatically deletes messages](../facts/sqs.md#sqs-auto-deletes-after-retention-period)
  link: [maximum message retention period](../facts/sqs.md#sqs-auto-deletes-after-retention-period)
sqs-batch-actions-permissions-follow-single-actions
  claim: You cannot set permissions explicitly for the SQS batch actions. Setting permissions for SendMessage, DeleteMessage or ChangeMessageVisibility sets permissions for the matching batch actions.
  scope: SQS batch actions.
  link: [You cannot set permissions explicitly](../facts/sqs.md#sqs-batch-actions-permissions-follow-single-actions)
  link: [corresponding batch versions of the actions](../facts/sqs.md#sqs-batch-actions-permissions-follow-single-actions)
sqs-batch-max-messages
  claim: A single SQS message batch request can include a maximum of 10 messages.
  scope: per message batch request; maximum; not adjustable.
  link: [10 messages](../facts/sqs.md#sqs-batch-max-messages)
  say: ten messages
sqs-batch-total-payload-1mib
  claim: The total size of all messages sent in a single SendMessageBatch call cannot exceed 1,048,576 bytes (1 MiB).
  scope: per SendMessageBatch call, all messages together; maximum; not adjustable.
  link: [1,048,576 bytes](../facts/sqs.md#sqs-batch-total-payload-1mib)
  link: [1 MiB](../facts/sqs.md#sqs-batch-total-payload-1mib)
  say: one mebibyte
sqs-batch-up-to-10-messages-cost
  claim: Batched SQS actions can send, receive or delete up to 10 messages at a time, and because Amazon SQS charges by the request, batching can substantially reduce costs.
  scope: per batch API request; maximum.
  link: [up to 10 messages at a time](../facts/sqs.md#sqs-batch-up-to-10-messages-cost)
  link: [batching can substantially reduce your costs](../facts/sqs.md#sqs-batch-up-to-10-messages-cost)
sqs-buffered-client-with-long-polling-minimizes-requests
  claim: You can combine client-side buffering with request batching by using long polling together with the buffered asynchronous client in the AWS SDK for Java, which minimizes requests. That client does not currently support FIFO queues.
  scope: AWS SDK for Java, SQS Buffered Asynchronous Client.
  link: [combine client-side buffering with request batching](../facts/sqs.md#sqs-buffered-client-with-long-polling-minimizes-requests)
  link: [doesn't currently support FIFO queues](../facts/sqs.md#sqs-buffered-client-with-long-polling-minimizes-requests)
sqs-cannot-convert-standard-queue-to-fifo
  claim: You cannot convert an existing standard queue into a FIFO queue. You must create a new FIFO queue, or delete the standard queue and recreate it as a FIFO queue.
  scope: SQS queue type.
  link: [cannot convert an existing standard queue](../facts/sqs.md#sqs-cannot-convert-standard-queue-to-fifo)
  link: [create a new FIFO queue for your application](../facts/sqs.md#sqs-cannot-convert-standard-queue-to-fifo)
sqs-case-migros-one-eks-microservices
  claim: Migros One's microservices architecture is deployed on Amazon EKS, and it uses Amazon SQS, fully managed message queuing for microservices, distributed systems and serverless applications (customer case study).
  scope: Migros One case study.
  link: [deployed on Amazon Elastic Kubernetes Service](../facts/sqs.md#sqs-case-migros-one-eks-microservices)
  link: [fully managed message queuing for microservices](../facts/sqs.md#sqs-case-migros-one-eks-microservices)
sqs-change-default-sse-all-queues-2022
  claim: The SQS console page says that on August 17, 2022, default server-side encryption (SSE) was applied to all SQS queues. The documentation history lists default SSE with SQS-owned encryption keys (SSE-SQS) on September 26, 2022. The default option applies only when you create a queue without specifying encryption attributes.
  scope: SQS queues; default; the default option is only effective when you create a queue without specifying encryption attributes.
  link: [August 17, 2022](../facts/sqs.md#sqs-change-default-sse-all-queues-2022)
  link: [September 26, 2022](../facts/sqs.md#sqs-change-default-sse-all-queues-2022)
  link: [default server-side encryption (SSE) was applied](../facts/sqs.md#sqs-change-default-sse-all-queues-2022)
sqs-change-fair-queues-standard-2025
  claim: Fair queues support for standard queues was added on July 21, 2025. SQS applies the fairness capability automatically in all standard queues, for messages with the MessageGroupId property, and a standard queue message group ID does not enforce message ordering.
  scope: standard queues; MessageGroupId on a standard queue is only a tenant identifier and does not enforce message ordering.
  link: [July 21, 2025](../facts/sqs.md#sqs-change-fair-queues-standard-2025)
  link: [messages with the MessageGroupId property](../facts/sqs.md#sqs-change-fair-queues-standard-2025)
sqs-change-fifo-dlq-redrive-2023
  claim: A What's New post says that Amazon SQS already supports redriving messages from a standard dead-letter queue to standard source queues or a standard custom destination queue. The current developer guide says that if the dead-letter queue is a FIFO queue, the redrive destination queue must be a FIFO queue as well.
  scope: dead-letter queue redrive; the redrive destination must be the same queue type as the dead-letter queue.
  link: [must be a FIFO queue as well](../facts/sqs.md#sqs-change-fifo-dlq-redrive-2023)
  changed: 2023-11-27: was redriving messages from a standard dead-letter queue to a standard source queues or a standard custom destination queue
sqs-change-fifo-high-throughput-quotas-raised-2022
  claim: On October 20, 2022 the SQS documentation history lists increased default quotas for FIFO high throughput mode in commercial Regions.
  scope: FIFO queues in high throughput mode, per Region; current values are on the quotas-messages page.
  link: [October 20, 2022](../facts/sqs.md#sqs-change-fifo-high-throughput-quotas-raised-2022)
  link: [Increased default quotas for FIFO high throughput mode](../facts/sqs.md#sqs-change-fifo-high-throughput-quotas-raised-2022)
sqs-change-max-message-size-1mib-2025
  claim: On 2025-08-04 SQS raised the maximum message payload size from 256 KiB to 1 MiB for standard and FIFO queues. The message quota page now lists a maximum of 1,048,576 bytes (1 MiB).
  scope: per message, standard and FIFO queues; maximum; the What's New post says the change is available in all AWS commercial Regions and AWS GovCloud (US).
  link: [1,048,576 bytes (1 MiB)](../facts/sqs.md#sqs-change-max-message-size-1mib-2025)
  link: [256 KiB](../facts/sqs.md#sqs-change-max-message-size-1mib-2025)
  link: [2025-08-04](../facts/sqs.md#sqs-change-max-message-size-1mib-2025)
  changed: 2025-08-04: was 256 KiB
sqs-change-message-visibility-extend-shorten
  claim: The ChangeMessageVisibility action can programmatically extend or shorten the visibility timeout. It can also set a specific timeout on individual messages without changing the queue setting.
  scope: SQS message, per message.
  link: [ChangeMessageVisibility action](../facts/sqs.md#sqs-change-message-visibility-extend-shorten)
  link: [extend or shorten the timeout as needed](../facts/sqs.md#sqs-change-message-visibility-extend-shorten)
sqs-change-sendmessage-needs-only-generatedatakey-2024
  claim: The SQS documentation history row of July 24, 2024 says that SQS no longer requires the kms:Decrypt permission for the SendMessage API and that customers only need kms:GenerateDataKey on the KMS key (but still need kms:Decrypt to call ReceiveMessage). The current key-management page still says that the producer must have the kms:Decrypt and kms:GenerateDataKey permissions for the KMS key.
  scope: SSE-KMS queues, per KMS key.
  link: [July 24, 2024](../facts/sqs.md#sqs-change-sendmessage-needs-only-generatedatakey-2024)
  link: [only need the kms:GenerateDataKey permission](../facts/sqs.md#sqs-change-sendmessage-needs-only-generatedatakey-2024)
  link: [still need kms:Decrypt permission to call ReceiveMessage](../facts/sqs.md#sqs-change-sendmessage-needs-only-generatedatakey-2024)
  link: [the producer must have the kms:Decrypt and kms:GenerateDataKey permissions](../facts/sqs.md#sqs-change-sendmessage-needs-only-generatedatakey-2024)
sqs-console-max-message-size-default
  claim: In the SQS console, the maximum message size setting ranges from 1 KiB to 1024 KiB and the default is 1024 KiB.
  scope: per queue (maximum message size setting); default; adjustable; Console setting when creating a standard queue..
  link: [1024 KiB](../facts/sqs.md#sqs-console-max-message-size-default)
  link: [1 KiB](../facts/sqs.md#sqs-console-max-message-size-default)
sqs-console-no-batch-actions
  claim: The SQS console does not support batch actions. You must use the query API or an AWS SDK to run batch operations.
  scope: SQS console.
  link: [console does not support batch actions](../facts/sqs.md#sqs-console-no-batch-actions)
  link: [use the query API or an AWS SDK](../facts/sqs.md#sqs-console-no-batch-actions)
sqs-console-receive-wait-time-default
  claim: In the SQS console, the receive message wait time ranges from 0 to 20 seconds and the default is 0 seconds, which sets short polling; any non-zero value sets long polling.
  scope: per queue (receive message wait time setting); default; adjustable; Console setting when creating a standard queue..
  link: [0 seconds](../facts/sqs.md#sqs-console-receive-wait-time-default)
  link: [0 to 20 seconds](../facts/sqs.md#sqs-console-receive-wait-time-default)
  link: [sets short polling](../facts/sqs.md#sqs-console-receive-wait-time-default)
  link: [Any non-zero value sets long polling](../facts/sqs.md#sqs-console-receive-wait-time-default)
  say: zero seconds
sqs-consumers-keep-idempotency-tokens-ignore-duplicates
  claim: A message that was published once may be delivered more than once. A publisher can include idempotency tokens, and consumers should keep track of each token received and ignore messages with duplicate tokens.
  scope: event-driven architectures with message queues.
  link: [may be accidentally delivered more than once](../facts/sqs.md#sqs-consumers-keep-idempotency-tokens-ignore-duplicates)
  link: [keep track of each token received](../facts/sqs.md#sqs-consumers-keep-idempotency-tokens-ignore-duplicates)
sqs-copies-on-multiple-servers-cause-duplicates
  claim: SQS stores copies of a message on multiple servers. If a server that holds a copy is unavailable when you receive or delete a message, the copy is not deleted there and you might get that message copy again, so applications must be idempotent.
  scope: SQS standard queue; a server holding a copy is unavailable at receive or delete time.
  link: [isn't deleted on the server that is unavailable](../facts/sqs.md#sqs-copies-on-multiple-servers-cause-duplicates)
  link: [you might get that message copy again](../facts/sqs.md#sqs-copies-on-multiple-servers-cause-duplicates)
  link: [Design your applications to be idempotent](../facts/sqs.md#sqs-copies-on-multiple-servers-cause-duplicates)
sqs-cross-account-needs-queue-access-policy
  claim: To let a principal in another account use a queue, you must configure the queue's access policy to allow that principal. IAM identity-based policies alone are not sufficient for cross-account access to SQS queues.
  scope: SQS queue, cross-account access.
  link: [configure the queue's access policy](../facts/sqs.md#sqs-cross-account-needs-queue-access-policy)
  link: [aren't sufficient for cross-account access](../facts/sqs.md#sqs-cross-account-needs-queue-access-policy)
sqs-decision-combine-buffer-for-consumers
  claim: The integration decision guide lists, among a few common ways AWS customers use a combination of services, routing EventBridge or SNS events to an SQS queue as a buffer for downstream consumers.
  scope: application integration decision guide.
  link: [as a buffer for downstream consumers](../facts/sqs.md#sqs-decision-combine-buffer-for-consumers)
  link: [buffer for downstream consumers](../facts/sqs.md#sqs-decision-combine-buffer-for-consumers)
sqs-decision-fifo-ordering-sns-fifo
  claim: SQS FIFO queues and SNS FIFO topics support first-in-first-out guaranteed message ordering, which suits scenarios that need sequential processing.
  scope: Amazon SQS, in the SNS, SQS or EventBridge decision guide.
  link: [First-In-First-Out guaranteed message ordering](../facts/sqs.md#sqs-decision-fifo-ordering-sns-fifo)
  link: [requiring sequential processing](../facts/sqs.md#sqs-decision-fifo-ordering-sns-fifo)
sqs-decision-keeps-until-processed
  claim: SQS keeps a message in the queue until it is successfully processed or it expires.
  scope: Amazon SQS, in the SNS, SQS or EventBridge decision guide.
  link: [Messages are persisted in the queue](../facts/sqs.md#sqs-decision-keeps-until-processed)
  link: [until successfully processed or expired](../facts/sqs.md#sqs-decision-keeps-until-processed)
sqs-decision-messaging-pubsub-or-point-to-point
  claim: The messaging category of the integration decision guide is for pub/sub messaging that broadcasts to many recipients at once, or point-to-point messaging for reliable asynchronous communication between components; its services are SNS, SQS and Amazon MQ.
  scope: application integration decision guide.
  link: [pub/sub messaging to broadcast messages](../facts/sqs.md#sqs-decision-messaging-pubsub-or-point-to-point)
  link: [point-to-point messaging](../facts/sqs.md#sqs-decision-messaging-pubsub-or-point-to-point)
sqs-decision-pricing-dimensions-requests-and-data
  claim: SQS pricing is based on the number of API requests and data transferred, with a free tier that includes a monthly allowance of free API requests and data transfer.
  scope: Amazon SQS, in the SNS, SQS or EventBridge decision guide.
  link: [number of API requests and data transferred](../facts/sqs.md#sqs-decision-pricing-dimensions-requests-and-data)
  link: [a monthly allowance of free API requests](../facts/sqs.md#sqs-decision-pricing-dimensions-requests-and-data)
sqs-decision-pull-model
  claim: SQS uses a pull-based model: consumers actively poll messages from the queue, which gives fine-grained control over the message processing rate and lets consumers scale independently.
  scope: Amazon SQS, in the SNS, SQS or EventBridge decision guide.
  link: [Pull-based model](../facts/sqs.md#sqs-decision-pull-model)
  link: [fine-grained control over message processing rates](../facts/sqs.md#sqs-decision-pull-model)
  say: pull-based model
sqs-decision-pull-vs-push-for-lambda
  claim: The decision guide says a pull based architecture could use services such as SQS or Kinesis Data Streams, where messages are stored on a queue or a stream and then can be retrieved by a consuming system. It also names EventBridge or SNS invoking a Lambda function asynchronously as an example when you consider a pull or push based architecture.
  scope: application integration decision guide.
  link: [A pull based architecture could use services](../facts/sqs.md#sqs-decision-pull-vs-push-for-lambda)
  link: [invoking a Lambda function asynchronously](../facts/sqs.md#sqs-decision-pull-vs-push-for-lambda)
sqs-decision-typical-use
  claim: SQS is commonly used to decouple microservices, buffer requests and process tasks asynchronously, which lets consumers scale independently and handle failures gracefully.
  scope: Amazon SQS, in the SNS, SQS or EventBridge decision guide.
  link: [decoupling microservices](../facts/sqs.md#sqs-decision-typical-use)
  link: [buffering requests](../facts/sqs.md#sqs-decision-typical-use)
sqs-default-access-policy-owner-only
  claim: By default, the access policy of a new queue allows only the queue owner to send and receive messages.
  scope: access policy of a new SQS queue; default; adjustable.
  link: [allows only the queue owner](../facts/sqs.md#sqs-default-access-policy-owner-only)
  link: [to send and receive messages](../facts/sqs.md#sqs-default-access-policy-owner-only)
sqs-delay-queue-hidden-at-add-visibility-after-receive
  claim: A delay queue hides a message when it is first added to the queue. A visibility timeout hides a message only after a consumer receives it from the queue.
  scope: SQS queue.
  link: [hidden when it is first added to queue](../facts/sqs.md#sqs-delay-queue-hidden-at-add-visibility-after-receive)
  link: [only after it is consumed from the queue](../facts/sqs.md#sqs-delay-queue-hidden-at-add-visibility-after-receive)
sqs-delay-queue-hides-new-messages
  claim: In a delay queue, every message sent to the queue stays invisible to consumers for the delay period.
  scope: SQS queue, per queue.
  link: [remain invisible to consumers](../facts/sqs.md#sqs-delay-queue-hides-new-messages)
  link: [for the duration of the delay period](../facts/sqs.md#sqs-delay-queue-hides-new-messages)
sqs-delay-queue-range
  claim: If you create an SQS delay queue, messages that you send to the queue remain invisible to consumers for the delay period; the default (minimum) delay for a queue is 0 seconds and the maximum is 15 minutes.
  scope: per queue (delay queue); maximum; not adjustable.
  link: [0 seconds](../facts/sqs.md#sqs-delay-queue-range)
  link: [15 minutes](../facts/sqs.md#sqs-delay-queue-range)
  say: zero seconds | fifteen minutes
sqs-delay-setting-retroactive-fifo-only
  claim: Changing the per-queue delay setting does not affect messages already in a standard queue. In a FIFO queue the change is retroactive and affects messages already in the queue.
  scope: per-queue delay setting; standard versus FIFO queue.
  link: [is not retroactive](../facts/sqs.md#sqs-delay-setting-retroactive-fifo-only)
  link: [setting is retroactive](../facts/sqs.md#sqs-delay-setting-retroactive-fifo-only)
sqs-dlq-create-queue-first
  claim: You must first create a new queue before you can configure it as a dead-letter queue.
  scope: SQS dead-letter queue.
  link: [must first create a new queue](../facts/sqs.md#sqs-dlq-create-queue-first)
  link: [before configuring it as a dead-letter queue](../facts/sqs.md#sqs-dlq-create-queue-first)
sqs-dlq-denyall-blocks-use-as-dlq
  claim: The redrive allow policy specifies which source queues can access a dead-letter queue; if you specify denyAll, the queue cannot be used as a dead-letter queue.
  scope: SQS redrive allow policy.
  link: [If you specify denyAll](../facts/sqs.md#sqs-dlq-denyall-blocks-use-as-dlq)
  link: [cannot be used as a dead-letter queue](../facts/sqs.md#sqs-dlq-denyall-blocks-use-as-dlq)
sqs-dlq-fifo-enqueue-timestamp-resets
  claim: In a FIFO SQS queue, the enqueue timestamp resets when the message is moved to a dead-letter queue.
  scope: FIFO queues and their dead-letter queues.
  link: [the enqueue timestamp resets](../facts/sqs.md#sqs-dlq-fifo-enqueue-timestamp-resets)
  link: [moved to a dead-letter queue](../facts/sqs.md#sqs-dlq-fifo-enqueue-timestamp-resets)
sqs-dlq-max-receive-count-meaning
  claim: A redrive policy sets maxReceiveCount, the number of times a consumer can receive a message from the source queue before SQS moves it to the dead-letter queue.
  scope: SQS redrive policy, per source queue.
  link: [number of times a consumer can receive](../facts/sqs.md#sqs-dlq-max-receive-count-meaning)
  link: [before it is moved to a dead-letter queue](../facts/sqs.md#sqs-dlq-max-receive-count-meaning)
sqs-dlq-redrive-allow-by-queue-max-10
  claim: In a redrive allow policy, which specifies which source queues can access the dead-letter queue, the byQueue option can specify up to 10 source queues, each by its Amazon Resource Name (ARN).
  scope: per dead-letter queue redrive allow policy; maximum; not adjustable.
  link: [up to 10 source queues](../facts/sqs.md#sqs-dlq-redrive-allow-by-queue-max-10)
  say: ten source queues
sqs-dlq-redrive-allow-policy-default-allow-all
  claim: A redrive allow policy can allow all source queues, allow specific source queues, or deny all source queues. By default, all source queues can use the dead-letter queue.
  scope: redrive allow policy, per dead-letter queue; default; adjustable.
  link: [The default allows all source queues](../facts/sqs.md#sqs-dlq-redrive-allow-policy-default-allow-all)
  link: [deny all source queues](../facts/sqs.md#sqs-dlq-redrive-allow-policy-default-allow-all)
sqs-dlq-retention-longer-than-source-queue
  claim: Best practice is to always set the retention period of a dead-letter queue longer than the retention period of the original queue.
  scope: SQS dead-letter queue.
  link: [longer than the retention period](../facts/sqs.md#sqs-dlq-retention-longer-than-source-queue)
  link: [retention period of a dead-letter queue](../facts/sqs.md#sqs-dlq-retention-longer-than-source-queue)
sqs-dlq-same-account-and-region
  claim: An SQS dead-letter queue must be in the same AWS account and Region as its source queue.
  scope: per dead-letter queue and its source queues.
  link: [same AWS account and Region](../facts/sqs.md#sqs-dlq-same-account-and-region)
  link: [must be in the same AWS account](../facts/sqs.md#sqs-dlq-same-account-and-region)
sqs-dlq-standard-enqueue-timestamp-unchanged
  claim: In a standard SQS queue, message expiration is always based on the original enqueue timestamp, and the enqueue timestamp stays unchanged when the message is moved to a dead-letter queue.
  scope: standard queues and their dead-letter queues.
  link: [the enqueue timestamp is unchanged](../facts/sqs.md#sqs-dlq-standard-enqueue-timestamp-unchanged)
  link: [always based on its original enqueue timestamp](../facts/sqs.md#sqs-dlq-standard-enqueue-timestamp-unchanged)
sqs-dlq-type-must-match-source-queue-type
  claim: The dead-letter queue of a FIFO queue must also be a FIFO queue. The dead-letter queue of a standard queue must also be a standard queue.
  scope: SQS dead-letter queue.
  link: [must also be a FIFO queue](../facts/sqs.md#sqs-dlq-type-must-match-source-queue-type)
  link: [must also be a standard queue](../facts/sqs.md#sqs-dlq-type-must-match-source-queue-type)
sqs-dlq-with-fifo-can-break-order
  claim: Do not use a dead-letter queue with a FIFO queue if you do not want to break the exact order of messages or operations.
  scope: SQS FIFO queue with dead-letter queue; exact order of messages must not break.
  link: [use a dead-letter queue with a FIFO queue](../facts/sqs.md#sqs-dlq-with-fifo-can-break-order)
  link: [break the exact order of messages or operations](../facts/sqs.md#sqs-dlq-with-fifo-can-break-order)
sqs-eventbridge-scheduler-for-advanced-scheduling
  claim: SQS delay queues and message timers allow scheduling of message delivery up to 15 minutes in the future. For more flexible scheduling, EventBridge Scheduler, which can schedule one-time or recurring API actions without time limitations, is the recommended solution for advanced message scheduling use cases.
  scope: message scheduling.
  link: [EventBridge Scheduler is the recommended solution](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling)
  link: [advanced message scheduling use cases](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling)
  link: [up to 15 minutes in the future](../facts/sqs.md#sqs-eventbridge-scheduler-for-advanced-scheduling)
sqs-extended-client-max-payload
  claim: With the SQS Extended Client Library, an SQS message holds a reference to a payload stored in Amazon S3, and the maximum payload size is 2 GB.
  scope: per message payload stored in Amazon S3 by the Extended Client Library; maximum; not adjustable; The library works only for synchronous clients..
  link: [2 GB](../facts/sqs.md#sqs-extended-client-max-payload)
  link: [reference to a message payload in Amazon S3](../facts/sqs.md#sqs-extended-client-max-payload)
  say: two gigabytes
sqs-extended-client-sync-only
  claim: The SQS Extended Client Library works only for synchronous clients.
  scope: SQS Extended Client Library for Java and for Python.
  link: [works only for synchronous clients](../facts/sqs.md#sqs-extended-client-sync-only)
  link: [reference to a message payload in Amazon S3](../facts/sqs.md#sqs-extended-client-sync-only)
sqs-failed-processing-message-not-lost
  claim: If a consumer does not process and delete a message before the visibility timeout expires, for example because of an application error, a crash or a connectivity problem, the message becomes visible again in the queue. The same or a different consumer can then retrieve it for another processing attempt, so the message is not lost.
  scope: SQS queue; the message is not processed and deleted before the visibility timeout expires.
  link: [retrieved by the same or a different consumer](../facts/sqs.md#sqs-failed-processing-message-not-lost)
  link: [aren't lost even if the initial processing fails](../facts/sqs.md#sqs-failed-processing-message-not-lost)
sqs-fair-queues-automatic-no-consumer-change
  claim: Fairness is applied automatically in all SQS standard queues to messages that have a MessageGroupId. It needs no consumer code change, has no impact on API latency and has no throughput limitations.
  scope: SQS standard queue, messages with MessageGroupId.
  link: [applied automatically in all Amazon SQS standard queues](../facts/sqs.md#sqs-fair-queues-automatic-no-consumer-change)
  link: [any change in the consumer code](../facts/sqs.md#sqs-fair-queues-automatic-no-consumer-change)
  link: [any throughput limitations](../facts/sqs.md#sqs-fair-queues-automatic-no-consumer-change)
sqs-fair-queues-groupid-is-tenant-id-no-ordering
  claim: On a standard queue, MessageGroupId is used only as a tenant identifier for fair queues and does not enforce message ordering.
  scope: SQS standard queue.
  link: [used only as a tenant identifier](../facts/sqs.md#sqs-fair-queues-groupid-is-tenant-id-no-ordering)
  link: [does not enforce message ordering](../facts/sqs.md#sqs-fair-queues-groupid-is-tenant-id-no-ordering)
sqs-fair-queues-no-per-tenant-rate-limit
  claim: Fair queues do not limit the consumption rate per tenant. Like standard queues, they allow virtually unlimited throughput and have no limit on the number of tenants.
  scope: SQS standard queue with fair queues.
  link: [does not limit the consumption rate per tenant](../facts/sqs.md#sqs-fair-queues-no-per-tenant-rate-limit)
  link: [virtually unlimited throughput](../facts/sqs.md#sqs-fair-queues-no-per-tenant-rate-limit)
  link: [no limits on the number of tenants](../facts/sqs.md#sqs-fair-queues-no-per-tenant-rate-limit)
sqs-fair-queues-noisy-neighbor-mitigation
  claim: SQS fair queues automatically mitigate the noisy-neighbor impact in multi-tenant queues that hold messages from many customers, client applications or message types.
  scope: SQS standard queue.
  link: [mitigates the noisy-neighbor impact](../facts/sqs.md#sqs-fair-queues-noisy-neighbor-mitigation)
  link: [multi-tenant queues](../facts/sqs.md#sqs-fair-queues-noisy-neighbor-mitigation)
sqs-faq-anonymous-access-via-access-policy
  claim: You can configure an access policy that allows anonymous users to access an Amazon SQS queue.
  scope: per queue.
  link: [allows anonymous users](../facts/sqs.md#sqs-faq-anonymous-access-via-access-policy)
  link: [configure an access policy](../facts/sqs.md#sqs-faq-anonymous-access-via-access-policy)
sqs-faq-any-number-of-queues
  claim: You can create any number of message queues.
  scope: per account; maximum; not adjustable.
  link: [any number of message queues](../facts/sqs.md#sqs-faq-any-number-of-queues)
  link: [create any number](../facts/sqs.md#sqs-faq-any-number-of-queues)
sqs-faq-batch-operations-cost-same-as-other-requests
  claim: Batch operations (SendMessageBatch, DeleteMessageBatch, and ChangeMessageVisibilityBatch) cost the same as other Amazon SQS requests, so grouping messages into batches can reduce your costs.
  scope: per request.
  link: [cost the same as other Amazon SQS requests](../facts/sqs.md#sqs-faq-batch-operations-cost-same-as-other-requests)
  link: [reduce your Amazon SQS costs](../facts/sqs.md#sqs-faq-batch-operations-cost-same-as-other-requests)
sqs-faq-cannot-convert-standard-to-fifo
  claim: You cannot convert an existing standard queue to a FIFO queue, because you must choose the queue type when you create it. It is possible to move to a FIFO queue.
  scope: per queue.
  link: [choose the queue type when you create it](../facts/sqs.md#sqs-faq-cannot-convert-standard-to-fifo)
  link: [move to a FIFO queue](../facts/sqs.md#sqs-faq-cannot-convert-standard-to-fifo)
sqs-faq-data-transfer-free-to-ec2-lambda-same-region
  claim: You can transfer data between Amazon SQS and Amazon EC2 or AWS Lambda free of charge within a single Region.
  scope: per Region.
  link: [free of charge within a single region](../facts/sqs.md#sqs-faq-data-transfer-free-to-ec2-lambda-same-region)
  link: [Amazon EC2 or AWS Lambda](../facts/sqs.md#sqs-faq-data-transfer-free-to-ec2-lambda-same-region)
sqs-faq-delete-already-deleted-returns-success
  claim: When you issue a DeleteMessage request on a previously-deleted message, Amazon SQS returns a success response.
  scope: per message.
  link: [returns a success response](../facts/sqs.md#sqs-faq-delete-already-deleted-returns-success)
  link: [previously-deleted message](../facts/sqs.md#sqs-faq-delete-already-deleted-returns-success)
sqs-faq-deleted-message-standard-may-repeat-fifo-never
  claim: A deleted message is never received again from a FIFO queue. From a standard queue, under rare circumstances, you might receive a previously-deleted message a second time.
  scope: per message.
  link: [FIFO queues never introduce duplicate messages](../facts/sqs.md#sqs-faq-deleted-message-standard-may-repeat-fifo-never)
  link: [previously-deleted message a second time](../facts/sqs.md#sqs-faq-deleted-message-standard-may-repeat-fifo-never)
sqs-faq-dlq-definition-isolate-unprocessable-messages
  claim: A dead-letter queue is an Amazon SQS queue to which a source queue can send messages if the source queue's consumer application cannot consume them successfully.
  scope: per source queue.
  link: [source queue can send messages](../facts/sqs.md#sqs-faq-dlq-definition-isolate-unprocessable-messages)
  link: [unable to consume the messages successfully](../facts/sqs.md#sqs-faq-dlq-definition-isolate-unprocessable-messages)
sqs-faq-dlq-fifo-needs-fifo-standard-needs-standard
  claim: You must use a FIFO dead-letter queue with a FIFO queue, and you can use only a standard dead-letter queue with a standard queue.
  scope: per source queue.
  link: [must use a FIFO dead letter queue](../facts/sqs.md#sqs-faq-dlq-fifo-needs-fifo-standard-needs-standard)
  link: [only a standard dead letter queue](../facts/sqs.md#sqs-faq-dlq-fifo-needs-fifo-standard-needs-standard)
sqs-faq-dlq-message-moved-when-receive-count-exceeds-max
  claim: When the ReceiveCount for a message exceeds the maxReceiveCount for a queue, Amazon SQS is designed to move the message to a dead-letter queue with its original message ID.
  scope: per source queue.
  link: [exceeds the maxReceiveCount](../facts/sqs.md#sqs-faq-dlq-message-moved-when-receive-count-exceeds-max)
  link: [with its original message ID](../facts/sqs.md#sqs-faq-dlq-message-moved-when-receive-count-exceeds-max)
sqs-faq-dlq-redrive-allow-policy-required
  claim: When you configure a dead letter queue, you are required to set appropriate permissions for the dead letter queue redrive using RedriveAllowPolicy.
  scope: per dead-letter queue.
  link: [required to set appropriate permissions](../facts/sqs.md#sqs-faq-dlq-redrive-allow-policy-required)
  link: [RedriveAllowPolicy](../facts/sqs.md#sqs-faq-dlq-redrive-allow-policy-required)
sqs-faq-dlq-redrive-back-to-source-queue
  claim: Once you recover your consumer application, you can redrive the messages from the dead-letter queue to the source queue.
  scope: per dead-letter queue.
  link: [redrive the messages from your dead-letter queue](../facts/sqs.md#sqs-faq-dlq-redrive-back-to-source-queue)
  link: [to the source queue](../facts/sqs.md#sqs-faq-dlq-redrive-back-to-source-queue)
sqs-faq-dlq-redrive-policy-max-receive-count
  claim: The condition for moving a message to a dead-letter queue is the number of times a consumer can receive a message from the queue, defined as maxReceiveCount. A dead-letter queue configured with a source queue and the maxReceiveCount is known as the redrive policy.
  scope: per source queue.
  link: [defined as maxReceiveCount](../facts/sqs.md#sqs-faq-dlq-redrive-policy-max-receive-count)
  link: [known as the redrive policy](../facts/sqs.md#sqs-faq-dlq-redrive-policy-max-receive-count)
sqs-faq-dlq-redrive-velocity-selectable
  claim: You can select the redrive velocity to set the rate at which Amazon SQS moves messages from the dead-letter queue to the source queue.
  scope: per redrive.
  link: [select the redrive velocity](../facts/sqs.md#sqs-faq-dlq-redrive-velocity-selectable)
  link: [the rate at which Amazon SQS will move](../facts/sqs.md#sqs-faq-dlq-redrive-velocity-selectable)
sqs-faq-fair-queues-messages-without-group-id-unique-tenants
  claim: Messages without a message group ID are treated as belonging to unique tenants, so you can apply message group IDs only where you need them.
  scope: fair queues.
  link: [selectively apply message group IDs](../facts/sqs.md#sqs-faq-fair-queues-messages-without-group-id-unique-tenants)
  link: [unique tenants](../facts/sqs.md#sqs-faq-fair-queues-messages-without-group-id-unique-tenants)
sqs-faq-fair-queues-same-throughput-as-standard
  claim: Fair queues maintain the same high throughput capabilities of standard queues.
  scope: fair queues.
  link: [same high throughput capabilities of standard queues](../facts/sqs.md#sqs-faq-fair-queues-same-throughput-as-standard)
  link: [Fair queues](../facts/sqs.md#sqs-faq-fair-queues-same-throughput-as-standard)
sqs-faq-fair-queues-versus-fifo-noisy-neighbor
  claim: FIFO queues maintain strict ordering by limiting the number of in-flight messages from each tenant, which limits throughput for each tenant. Fair queues let multiple consumers process messages from the same tenant at the same time.
  scope: fair queues versus FIFO queues.
  link: [in-flight messages from each tenant](../facts/sqs.md#sqs-faq-fair-queues-versus-fifo-noisy-neighbor)
  link: [process messages from the same tenant concurrently](../facts/sqs.md#sqs-faq-fair-queues-versus-fifo-noisy-neighbor)
sqs-faq-fifo-default-throughput-3000-with-batching-300-without
  claim: By default, FIFO queues support up to 3,000 messages per second with batching, or up to 300 messages per second (300 send, receive, or delete operations per second) without batching.
  scope: per FIFO queue, default mode; default; adjustable.
  link: [3,000 messages per second with batching](../facts/sqs.md#sqs-faq-fifo-default-throughput-3000-with-batching-300-without)
  link: [300 messages per second](../facts/sqs.md#sqs-faq-fifo-default-throughput-3000-with-batching-300-without)
sqs-faq-fifo-exactly-once-processing
  claim: FIFO queues provide exactly-once processing: each message is delivered once and stays available until a consumer processes and deletes it. Duplicates are not introduced into the queue.
  scope: FIFO queues.
  link: [exactly-once processing](../facts/sqs.md#sqs-faq-fifo-exactly-once-processing)
  link: [Duplicates are not introduced into the queue](../facts/sqs.md#sqs-faq-fifo-exactly-once-processing)
sqs-faq-fifo-no-sequencing-info
  claim: With a FIFO queue you do not have to place sequencing information in your messages.
  scope: FIFO queues.
  link: [sequencing information](../facts/sqs.md#sqs-faq-fifo-no-sequencing-info)
  link: [FIFO queue](../facts/sqs.md#sqs-faq-fifo-no-sequencing-info)
sqs-faq-fifo-parallel-producers-order-might-not-be-preserved
  claim: If multiple producers send messages in parallel without waiting for the success response of SendMessage or SendMessageBatch, the order between producers might not be preserved.
  scope: FIFO queues.
  link: [order between producers might not be preserved](../facts/sqs.md#sqs-faq-fifo-parallel-producers-order-might-not-be-preserved)
  link: [without waiting for the success response](../facts/sqs.md#sqs-faq-fifo-parallel-producers-order-might-not-be-preserved)
sqs-faq-fifo-preserves-exact-order
  claim: FIFO queues preserve the exact order in which messages are sent and received.
  scope: FIFO queues.
  link: [preserve the exact order](../facts/sqs.md#sqs-faq-fifo-preserves-exact-order)
  link: [FIFO (first-in-first-out) queues](../facts/sqs.md#sqs-faq-fifo-preserves-exact-order)
sqs-faq-fifo-same-group-one-consumer-at-a-time
  claim: By design, FIFO queues do not serve messages from the same message group to more than one consumer at a time. A FIFO queue with multiple message groups can serve different groups to different consumers in parallel.
  scope: per message group.
  link: [more than one consumer at a time](../facts/sqs.md#sqs-faq-fifo-same-group-one-consumer-at-a-time)
  link: [different message groups to different consumers](../facts/sqs.md#sqs-faq-fifo-same-group-one-consumer-at-a-time)
sqs-faq-fifo-supports-same-cloudwatch-metrics
  claim: FIFO queues support all metrics that standard queues support, and for FIFO queues all approximate metrics return accurate counts.
  scope: FIFO queues.
  link: [all metrics that standard queues support](../facts/sqs.md#sqs-faq-fifo-supports-same-cloudwatch-metrics)
  link: [accurate counts](../facts/sqs.md#sqs-faq-fifo-supports-same-cloudwatch-metrics)
sqs-faq-hipaa-eligible-with-baa
  claim: Amazon SQS is a HIPAA Eligible Service. With an executed Business Associate Agreement with AWS, you can use it to transmit messages that contain protected health information.
  scope: Amazon SQS.
  link: [HIPAA Eligible Service](../facts/sqs.md#sqs-faq-hipaa-eligible-with-baa)
  link: [executed Business Associate Agreement](../facts/sqs.md#sqs-faq-hipaa-eligible-with-baa)
sqs-faq-hosted-queue-between-microservices-dlq-poison-pill
  claim: SQS is a hosted queue that stores messages as they travel between applications or microservices; it provides common middleware constructs such as dead-letter queues and poison-pill management.
  scope: Amazon SQS FAQ comparison.
  link: [reliable, highly-scalable hosted queue for storing messages](../facts/sqs.md#sqs-faq-hosted-queue-between-microservices-dlq-poison-pill)
  link: [dead-letter queues and poison-pill management](../facts/sqs.md#sqs-faq-hosted-queue-between-microservices-dlq-poison-pill)
sqs-faq-jms-library-jms-1-1
  claim: Amazon provides the Amazon SQS Java Messaging Library, which implements the JMS 1.1 specification and uses Amazon SQS as the JMS provider.
  scope: Amazon SQS.
  link: [Amazon SQS Java Messaging Library](../facts/sqs.md#sqs-faq-jms-library-jms-1-1)
  link: [JMS 1.1 specification](../facts/sqs.md#sqs-faq-jms-library-jms-1-1)
sqs-faq-kinesis-streams-realtime-and-replay
  claim: In the SQS FAQ comparison, Amazon Kinesis Streams allows real-time processing of streaming big data and the ability to read and replay records to multiple Amazon Kinesis Applications.
  scope: Kinesis Streams versus SQS.
  link: [real-time processing of streaming big data](../facts/sqs.md#sqs-faq-kinesis-streams-realtime-and-replay)
  link: [read and replay records](../facts/sqs.md#sqs-faq-kinesis-streams-realtime-and-replay)
sqs-faq-long-poll-timeout-max-20-seconds
  claim: In general, you should use a maximum of 20 seconds for a long-poll timeout.
  scope: per ReceiveMessage call; maximum; not adjustable.
  link: [maximum of 20 seconds](../facts/sqs.md#sqs-faq-long-poll-timeout-max-20-seconds)
  link: [long-poll timeout](../facts/sqs.md#sqs-faq-long-poll-timeout-max-20-seconds)
sqs-faq-long-poll-timeout-min-1-second
  claim: If the 20-second maximum does not work for your application, you can set a shorter long-poll timeout, as low as 1 second.
  scope: per ReceiveMessage call; minimum; not adjustable.
  link: [as low as 1 second](../facts/sqs.md#sqs-faq-long-poll-timeout-min-1-second)
  link: [shorter long-poll timeout](../facts/sqs.md#sqs-faq-long-poll-timeout-min-1-second)
sqs-faq-long-polling-fewer-empty-receives-lower-cost
  claim: Using long polling might reduce the cost of using SQS, because you can reduce the number of empty receives.
  scope: per queue consumer.
  link: [reduce the number of empty receives](../facts/sqs.md#sqs-faq-long-polling-fewer-empty-receives-lower-cost)
  link: [reduce the cost of using SQS](../facts/sqs.md#sqs-faq-long-polling-fewer-empty-receives-lower-cost)
sqs-faq-long-polling-no-extra-charge
  claim: Long-polling ReceiveMessage calls are billed exactly the same as short-polling ReceiveMessage calls, so there is no additional charge for long polling.
  scope: per ReceiveMessage call.
  link: [billed exactly the same](../facts/sqs.md#sqs-faq-long-polling-no-extra-charge)
  link: [short-polling ReceiveMessage calls](../facts/sqs.md#sqs-faq-long-polling-no-extra-charge)
sqs-faq-long-polling-preferable-almost-all-cases
  claim: In almost all cases, Amazon SQS long polling is preferable to short polling.
  scope: Amazon SQS consumers.
  link: [long polling is preferable to short polling](../facts/sqs.md#sqs-faq-long-polling-preferable-almost-all-cases)
  link: [almost all cases](../facts/sqs.md#sqs-faq-long-polling-preferable-almost-all-cases)
sqs-faq-long-polling-waits-for-message
  claim: Short polling returns immediately even if the queue is empty. Long polling does not return a response until a message arrives in the queue or the long poll times out.
  scope: per ReceiveMessage call.
  link: [returns immediately](../facts/sqs.md#sqs-faq-long-polling-waits-for-message)
  link: [until a message arrives in the message queue](../facts/sqs.md#sqs-faq-long-polling-waits-for-message)
sqs-faq-maximum-message-size-attribute-range
  claim: The MaximumMessageSize attribute of a queue takes a value between 1,024 bytes (1 KiB) and 1,048,576 bytes (1 MiB).
  scope: per queue; maximum; adjustable.
  link: [1,024 bytes (1 KiB)](../facts/sqs.md#sqs-faq-maximum-message-size-attribute-range)
  link: [1,048,576 bytes (1 MiB)](../facts/sqs.md#sqs-faq-maximum-message-size-attribute-range)
sqs-faq-message-attributes-types
  claim: Amazon SQS message attributes take the form of name-type-value triples. The supported types include string, binary, and number.
  scope: per message attribute.
  link: [name-type-value triples](../facts/sqs.md#sqs-faq-message-attributes-types)
  link: [string, binary, and number](../facts/sqs.md#sqs-faq-message-attributes-types)
sqs-faq-mq-for-existing-apps
  claim: AWS recommends Amazon MQ when you move messaging of existing applications to the cloud quickly. Amazon MQ supports industry-standard APIs and protocols, so you can switch from a standards-based message broker without rewriting the messaging code.
  scope: Amazon MQ versus Amazon SQS.
  link: [existing applications](../facts/sqs.md#sqs-faq-mq-for-existing-apps)
  link: [industry-standard APIs and protocols](../facts/sqs.md#sqs-faq-mq-for-existing-apps)
sqs-faq-new-cloud-applications-sqs-and-sns
  claim: For brand new applications in the cloud, the SQS FAQ recommends SQS and SNS: lightweight, fully managed message queue and topic services that scale almost infinitely and have simple, easy-to-use APIs.
  scope: Amazon SQS FAQ comparison.
  link: [brand new applications in the cloud](../facts/sqs.md#sqs-faq-new-cloud-applications-sqs-and-sns)
  link: [lightweight, fully managed message queue and topic services](../facts/sqs.md#sqs-faq-new-cloud-applications-sqs-and-sns)
sqs-faq-no-admin-overhead
  claim: Amazon SQS needs no administrative overhead and little configuration.
  scope: Amazon SQS.
  link: [no administrative overhead](../facts/sqs.md#sqs-faq-no-admin-overhead)
  link: [little configuration](../facts/sqs.md#sqs-faq-no-admin-overhead)
sqs-faq-only-account-owner-or-delegate-can-operate-queue
  claim: Only an AWS account owner, or an AWS account that the owner has delegated rights to, can perform operations on an Amazon SQS message queue. An access policy can also be configured to allow anonymous users to access a message queue.
  scope: per queue.
  link: [Only an AWS account owner](../facts/sqs.md#sqs-faq-only-account-owner-or-delegate-can-operate-queue)
  link: [delegated rights](../facts/sqs.md#sqs-faq-only-account-owner-or-delegate-can-operate-queue)
  link: [allows anonymous users to access a message queue](../facts/sqs.md#sqs-faq-only-account-owner-or-delegate-can-operate-queue)
sqs-faq-permissions-api-no-conditional-access
  claim: The SQS permissions API provides an interface for sharing access to a message queue with developers, but it cannot allow conditional access or more advanced use cases.
  scope: SQS permissions API.
  link: [cannot allow conditional access](../facts/sqs.md#sqs-faq-permissions-api-no-conditional-access)
sqs-faq-pricing-same-all-regions-except-china-beijing
  claim: Amazon SQS pricing is the same for all Regions, except China (Beijing).
  scope: per Region.
  link: [same for all regions](../facts/sqs.md#sqs-faq-pricing-same-all-regions-except-china-beijing)
  link: [except China (Beijing)](../facts/sqs.md#sqs-faq-pricing-same-all-regions-except-china-beijing)
sqs-faq-purge-queue-deletes-all-messages
  claim: You can delete all messages in an Amazon SQS queue by using the PurgeQueue action.
  scope: per queue.
  link: [PurgeQueue action](../facts/sqs.md#sqs-faq-purge-queue-deletes-all-messages)
  link: [delete all messages](../facts/sqs.md#sqs-faq-purge-queue-deletes-all-messages)
sqs-faq-queue-name-unique-per-account-region-reusable
  claim: A queue name must be unique within an AWS account and Region. You can reuse the name after you delete the queue.
  scope: per account, per Region.
  link: [unique within an AWS account and region](../facts/sqs.md#sqs-faq-queue-name-unique-per-account-region-reusable)
  link: [reuse a message queue's name after you delete](../facts/sqs.md#sqs-faq-queue-name-unique-per-account-region-reusable)
sqs-faq-queue-owner-pays-for-shared-access
  claim: The message queue owner pays for shared message queue access.
  scope: per shared queue.
  link: [queue owner pays](../facts/sqs.md#sqs-faq-queue-owner-pays-for-shared-access)
  link: [shared message queue access](../facts/sqs.md#sqs-faq-queue-owner-pays-for-shared-access)
sqs-faq-queues-are-independent-per-region
  claim: You cannot share messages between queues in different Regions, because each Amazon SQS queue is independent within its Region.
  scope: per Region.
  link: [independent within each region](../facts/sqs.md#sqs-faq-queues-are-independent-per-region)
  link: [Each Amazon SQS message queue](../facts/sqs.md#sqs-faq-queues-are-independent-per-region)
sqs-faq-receipt-handle-required-to-delete
  claim: When you receive a message, the response includes a receipt handle that you must provide when deleting the message.
  scope: per message.
  link: [receipt handle](../facts/sqs.md#sqs-faq-receipt-handle-required-to-delete)
  link: [must provide when deleting the message](../facts/sqs.md#sqs-faq-receipt-handle-required-to-delete)
sqs-faq-receive-then-delete-acknowledges-processing
  claim: You are responsible for deleting the message, and the deletion request acknowledges that you are done processing the message.
  scope: per message.
  link: [responsible for deleting the message](../facts/sqs.md#sqs-faq-receive-then-delete-acknowledges-processing)
  link: [acknowledges](../facts/sqs.md#sqs-faq-receive-then-delete-acknowledges-processing)
sqs-faq-retention-default-4-days
  claim: The default Amazon SQS message retention period is 4 days; you can configure it to a value from 1 minute to 14 days.
  scope: per queue; default; adjustable.
  link: [The default is 4 days](../facts/sqs.md#sqs-faq-retention-default-4-days)
  link: [4 days](../facts/sqs.md#sqs-faq-retention-default-4-days)
sqs-faq-retention-range-1-minute-to-14-days
  claim: You can set the Amazon SQS message retention period to a value from 1 minute to 14 days.
  scope: per queue; maximum; adjustable; configurable between 1 minute and 14 days.
  link: [1 minute to 14 days](../facts/sqs.md#sqs-faq-retention-range-1-minute-to-14-days)
  link: [message retention period](../facts/sqs.md#sqs-faq-retention-range-1-minute-to-14-days)
sqs-faq-scale-without-configuration
  claim: You can scale the amount of traffic you send to Amazon SQS up or down without any configuration.
  scope: Amazon SQS.
  link: [up or down without any configuration](../facts/sqs.md#sqs-faq-scale-without-configuration)
  link: [scale the amount of traffic](../facts/sqs.md#sqs-faq-scale-without-configuration)
sqs-faq-sdk-default-20-second-long-poll
  claim: All AWS SDKs work with 20-second long polls by default. If you don't use an AWS SDK, or if you configured your SDK to have a shorter timeout, you might need to modify your SQS client to allow longer requests or to use a shorter long-poll timeout.
  scope: SQS clients (AWS SDKs and other clients).
  link: [20-second long polls](../facts/sqs.md#sqs-faq-sdk-default-20-second-long-poll)
  link: [All AWS SDKs](../facts/sqs.md#sqs-faq-sdk-default-20-second-long-poll)
sqs-faq-set-queue-attributes-full-policy-language-ip-and-time
  claim: The SetQueueAttributes operation supports the full access policy language, so you can, for example, restrict access to a queue by IP address and time of day.
  scope: per queue.
  link: [supports the full access policy language](../facts/sqs.md#sqs-faq-set-queue-attributes-full-policy-language-ip-and-time)
  link: [IP address and time of day](../facts/sqs.md#sqs-faq-set-queue-attributes-full-policy-language-ip-and-time)
sqs-faq-share-queue-with-access-policy-statement
  claim: You can share an Amazon SQS queue by associating an access policy statement, which specifies the permissions granted, with the queue.
  scope: per queue.
  link: [access policy statement](../facts/sqs.md#sqs-faq-share-queue-with-access-policy-statement)
  link: [message queue to be shared](../facts/sqs.md#sqs-faq-share-queue-with-access-policy-statement)
sqs-faq-sns-push-sqs-poll
  claim: Amazon SNS pushes time-critical messages to multiple subscribers, so receivers do not need to poll. Amazon SQS is a message queue that applications poll to exchange messages, and it decouples sending and receiving components.
  scope: SQS versus SNS.
  link: [multiple subscribers](../facts/sqs.md#sqs-faq-sns-push-sqs-poll)
  link: [through a polling model](../facts/sqs.md#sqs-faq-sns-push-sqs-poll)
sqs-faq-some-services-not-compatible-with-fifo-targets
  claim: Some AWS or external services that send notifications to Amazon SQS might not be compatible with FIFO queues, even though they let you set a FIFO queue as a target.
  scope: FIFO queues.
  link: [might not be compatible with FIFO queues](../facts/sqs.md#sqs-faq-some-services-not-compatible-with-fifo-targets)
  link: [set a FIFO queue as a target](../facts/sqs.md#sqs-faq-some-services-not-compatible-with-fifo-targets)
sqs-faq-sqs-resource-based-permissions-iam-policy-language
  claim: Amazon SQS has its own resource-based permissions system that uses policies written in the same language as IAM policies.
  scope: per queue.
  link: [resource-based permissions system](../facts/sqs.md#sqs-faq-sqs-resource-based-permissions-iam-policy-language)
  link: [same language as AWS Identity and Access Management](../facts/sqs.md#sqs-faq-sqs-resource-based-permissions-iam-policy-language)
sqs-faq-sqs-supports-standard-and-fifo
  claim: Amazon SQS supports both standard and FIFO queues.
  scope: Amazon SQS.
  link: [standard and FIFO queues](../facts/sqs.md#sqs-faq-sqs-supports-standard-and-fifo)
  link: [supports both](../facts/sqs.md#sqs-faq-sqs-supports-standard-and-fifo)
sqs-faq-sse-algorithm-aes-gcm-256
  claim: SSE for Amazon SQS uses the AES-GCM 256 algorithm.
  scope: Amazon SQS queues.
  link: [AES-GCM 256 algorithm](../facts/sqs.md#sqs-faq-sse-algorithm-aes-gcm-256)
  link: [SSE uses](../facts/sqs.md#sqs-faq-sse-algorithm-aes-gcm-256)
sqs-faq-sse-both-queue-types
  claim: Both standard and FIFO queues support server-side encryption (SSE).
  scope: Amazon SQS queues.
  link: [Both standard and FIFO queues support SSE](../facts/sqs.md#sqs-faq-sse-both-queue-types)
  link: [standard and FIFO queues](../facts/sqs.md#sqs-faq-sse-both-queue-types)
sqs-faq-sse-data-key-reuse-1-minute-to-24-hours
  claim: Amazon SQS generates data keys from the KMS key for envelope encryption and decryption of messages for a configurable time period from 1 minute to 24 hours.
  scope: per queue; maximum; adjustable.
  link: [from 1 minute to 24 hours](../facts/sqs.md#sqs-faq-sse-data-key-reuse-1-minute-to-24-hours)
  link: [configurable time period](../facts/sqs.md#sqs-faq-sse-data-key-reuse-1-minute-to-24-hours)
sqs-faq-sse-key-policy-must-allow-queue-encryption
  claim: Before you can use SSE, you must configure AWS KMS key policies to allow encryption of queues and encryption and decryption of messages.
  scope: per KMS key.
  link: [configure AWS KMS key policies](../facts/sqs.md#sqs-faq-sse-key-policy-must-allow-queue-encryption)
  link: [encryption and decryption of messages](../facts/sqs.md#sqs-faq-sse-key-policy-must-allow-queue-encryption)
sqs-faq-sse-no-extra-sqs-charge-kms-calls-charged
  claim: There are no additional Amazon SQS charges for SSE, but there are charges for calls from Amazon SQS to AWS KMS.
  scope: per queue.
  link: [no additional Amazon SQS charges](../facts/sqs.md#sqs-faq-sse-no-extra-sqs-charge-kms-calls-charged)
  link: [calls from Amazon SQS to AWS KMS](../facts/sqs.md#sqs-faq-sse-no-extra-sqs-charge-kms-calls-charged)
sqs-faq-sse-producer-needs-generatedatakey-and-decrypt
  claim: To send messages to an encrypted queue, the producer must have the kms:GenerateDataKey and kms:Decrypt permissions for the KMS key.
  scope: producer of an SSE-KMS queue, per KMS key; CONFLICT kept open on purpose: the SQS documentation history row of July 24, 2024 (sqs-change-sendmessage-needs-only-generatedatakey-2024) says SendMessage no longer requires kms:Decrypt; the FAQ and the current key-management page still say a producer needs both. Granting both permissions to a producer is the design that works under either reading..
  link: [kms:GenerateDataKey and kms:Decrypt permissions](../facts/sqs.md#sqs-faq-sse-producer-needs-generatedatakey-and-decrypt)
  link: [the producer must have](../facts/sqs.md#sqs-faq-sse-producer-needs-generatedatakey-and-decrypt)
sqs-faq-sse-services-need-compatibility-with-encrypted-queues
  claim: To use SNS, CloudWatch Events and S3 events with encrypted queues, you need to enable compatibility between those AWS services and queues with SSE.
  scope: per encrypted queue.
  link: [enable compatibility between AWS services](../facts/sqs.md#sqs-faq-sse-services-need-compatibility-with-encrypted-queues)
  link: [Queues with SSE](../facts/sqs.md#sqs-faq-sse-services-need-compatibility-with-encrypted-queues)
sqs-faq-sse-uses-kms-keys
  claim: SSE protects the contents of messages in Amazon SQS queues using keys managed in AWS KMS. SSE encrypts messages as soon as Amazon SQS receives them, and Amazon SQS decrypts messages only when they are sent to an authorized consumer.
  scope: Amazon SQS queues.
  link: [keys managed in the AWS Key Management Service](../facts/sqs.md#sqs-faq-sse-uses-kms-keys)
  link: [sent to an authorized consumer](../facts/sqs.md#sqs-faq-sse-uses-kms-keys)
sqs-faq-standard-at-least-once-delivery
  claim: Standard queues provide at-least-once delivery, which means that each message is delivered at least once.
  scope: standard queues.
  link: [at-least-once delivery](../facts/sqs.md#sqs-faq-standard-at-least-once-delivery)
  link: [delivered at least once](../facts/sqs.md#sqs-faq-standard-at-least-once-delivery)
sqs-faq-standard-loose-fifo-order-not-guaranteed
  claim: Standard queues provide a loose-FIFO capability that attempts to preserve message order. Receiving messages in the exact order they are sent is not guaranteed.
  scope: standard queues.
  link: [loose-FIFO capability](../facts/sqs.md#sqs-faq-standard-loose-fifo-order-not-guaranteed)
  link: [not guaranteed](../facts/sqs.md#sqs-faq-standard-loose-fifo-order-not-guaranteed)
sqs-faq-standard-queue-design-idempotent-consumers
  claim: If you use a standard queue, you must design your applications to be idempotent, so processing the same message more than once does not affect them adversely.
  scope: standard queues.
  link: [design your applications to be idempotent](../facts/sqs.md#sqs-faq-standard-queue-design-idempotent-consumers)
  link: [same message more than once](../facts/sqs.md#sqs-faq-standard-queue-design-idempotent-consumers)
sqs-faq-storage-multi-az-region
  claim: Amazon SQS stores all message queues and messages within a single AWS Region, across multiple redundant Availability Zones, so that no single computer, network, or Availability Zone failure can make messages inaccessible.
  scope: per Region.
  link: [multiple redundant Availability Zones](../facts/sqs.md#sqs-faq-storage-multi-az-region)
  link: [highly-available AWS region](../facts/sqs.md#sqs-faq-storage-multi-az-region)
sqs-faq-typical-latency-tens-to-low-hundreds-ms
  claim: Typical latencies for SendMessage, ReceiveMessage, and DeleteMessage API requests are in the tens or low hundreds of milliseconds.
  scope: per API request.
  link: [tens or low hundreds of milliseconds](../facts/sqs.md#sqs-faq-typical-latency-tens-to-low-hundreds-ms)
  link: [SendMessage, ReceiveMessage, and DeleteMessage](../facts/sqs.md#sqs-faq-typical-latency-tens-to-low-hundreds-ms)
sqs-faq-visibility-timeout-definition
  claim: The visibility timeout is a period of time during which Amazon SQS prevents other consuming components from receiving and processing a message.
  scope: per message.
  link: [prevents other consuming components](../facts/sqs.md#sqs-faq-visibility-timeout-definition)
  link: [period of time](../facts/sqs.md#sqs-faq-visibility-timeout-definition)
sqs-fifo-3000-is-300-calls-of-10
  claim: If you use batching, non-high throughput FIFO queues support up to 3,000 messages per second, per API action; the 3,000 messages per second represent 300 API calls, each with a batch of 10 messages.
  scope: per API action; non-high throughput FIFO queue; with batching; maximum; not adjustable.
  link: [300 API calls](../facts/sqs.md#sqs-fifo-3000-is-300-calls-of-10)
  link: [a batch of 10 messages](../facts/sqs.md#sqs-fifo-3000-is-300-calls-of-10)
sqs-fifo-cannot-request-specific-group
  claim: A consumer cannot explicitly ask to receive messages from a specific message group ID in a FIFO queue.
  scope: SQS FIFO queue, ReceiveMessage.
  link: [cannot explicitly request to receive messages](../facts/sqs.md#sqs-fifo-cannot-request-specific-group)
  link: [from a specific message group ID](../facts/sqs.md#sqs-fifo-cannot-request-specific-group)
sqs-fifo-content-based-dedup-hash-body-only
  claim: With content-based deduplication, Amazon SQS uses a SHA-256 hash of the message body, but not of the message attributes, to generate the message deduplication ID.
  scope: SQS FIFO queues with content-based deduplication enabled.
  link: [SHA-256 hash](../facts/sqs.md#sqs-fifo-content-based-dedup-hash-body-only)
  link: [but not the attributes of the message](../facts/sqs.md#sqs-fifo-content-based-dedup-hash-body-only)
sqs-fifo-dedup-id-tracked-after-delete
  claim: SQS continues to track a FIFO deduplication ID even after the message has been received and deleted.
  scope: SQS FIFO queue.
  link: [continues tracking the deduplication ID](../facts/sqs.md#sqs-fifo-dedup-id-tracked-after-delete)
  link: [received and deleted](../facts/sqs.md#sqs-fifo-dedup-id-tracked-after-delete)
sqs-fifo-deduplication-interval-5-minutes
  claim: In an SQS FIFO queue, messages with the same deduplication ID sent within a 5 minute deduplication interval are treated as duplicates, and only one copy is delivered.
  scope: per FIFO queue, per message deduplication ID; fixed; not adjustable.
  link: [5 minute deduplication interval](../facts/sqs.md#sqs-fifo-deduplication-interval-5-minutes)
  link: [only one copy is delivered](../facts/sqs.md#sqs-fifo-deduplication-interval-5-minutes)
  say: five minutes
sqs-fifo-generated-dedup-id-from-body-hash
  claim: If you do not specify a deduplication ID and content-based deduplication is enabled, SQS generates the deduplication ID by hashing the message body.
  scope: SQS FIFO queue; content-based deduplication is enabled and no deduplication ID is sent.
  link: [by hashing the message body](../facts/sqs.md#sqs-fifo-generated-dedup-id-from-body-hash)
  link: [content-based deduplication is enabled](../facts/sqs.md#sqs-fifo-generated-dedup-id-from-body-hash)
sqs-fifo-groups-processed-in-parallel
  claim: A FIFO queue allows parallel processing of messages across different message group IDs. To get more concurrency, design the system with several message group IDs for independent workflows.
  scope: SQS FIFO queue.
  link: [parallel processing of messages](../facts/sqs.md#sqs-fifo-groups-processed-in-parallel)
  link: [across different message group IDs](../facts/sqs.md#sqs-fifo-groups-processed-in-parallel)
  link: [multiple message group IDs for independent workflows](../facts/sqs.md#sqs-fifo-groups-processed-in-parallel)
sqs-fifo-ht-other-regions-2400-tps
  claim: For SQS FIFO queues in high throughput mode, with non-batched API calls, all other AWS Regions have a default throughput of 2,400 TPS.
  scope: per queue; non-batched API calls; all other AWS Regions; high throughput mode; default; adjustable.
  link: [2,400 TPS](../facts/sqs.md#sqs-fifo-ht-other-regions-2400-tps)
  say: two thousand four hundred transactions per second
sqs-fifo-ht-top-regions-70000-tps
  claim: For SQS FIFO queues in high throughput mode, with non-batched API calls, US East (N. Virginia), US West (Oregon) and Europe (Ireland) support up to 70,000 transactions per second (TPS).
  scope: per queue; non-batched API calls; US East (N. Virginia), US West (Oregon), Europe (Ireland); high throughput mode; maximum; adjustable.
  link: [70,000 transactions per second](../facts/sqs.md#sqs-fifo-ht-top-regions-70000-tps)
  say: seventy thousand transactions per second
sqs-fifo-ht-top-regions-batched-700000
  claim: For SQS FIFO queues in high throughput mode, with batched API calls, US East (N. Virginia), US West (Oregon) and Europe (Ireland) support up to 700,000 messages per second, which is 10x the non-batch limit of 70,000 TPS.
  scope: per queue; batched API calls; US East (N. Virginia), US West (Oregon), Europe (Ireland); high throughput mode; maximum; adjustable.
  link: [700,000 messages per second](../facts/sqs.md#sqs-fifo-ht-top-regions-batched-700000)
  say: seven hundred thousand messages per second
sqs-fifo-in-flight-blocks-same-group
  claim: While a message of a message group is in flight, a FIFO queue returns no additional messages from the same message group until that message is deleted or becomes visible again.
  scope: per message group ID, SQS FIFO queue; an earlier message of the group is received and not deleted.
  link: [from the same message group ID](../facts/sqs.md#sqs-fifo-in-flight-blocks-same-group)
  link: [until the first message is deleted](../facts/sqs.md#sqs-fifo-in-flight-blocks-same-group)
sqs-fifo-message-group-id-required
  claim: You must give every message sent to a FIFO queue a message group ID. If a message is sent without a group ID, the action fails.
  scope: per message, SQS FIFO queue.
  link: [associate a message group ID with each message](../facts/sqs.md#sqs-fifo-message-group-id-required)
  link: [sent without a group ID, the action fails](../facts/sqs.md#sqs-fifo-message-group-id-required)
sqs-fifo-message-groups-no-quota
  claim: There is no quota to the number of message groups within an SQS FIFO queue.
  scope: per FIFO queue; maximum; not adjustable.
  link: [no quota to the number of message groups](../facts/sqs.md#sqs-fifo-message-groups-no-quota)
  link: [There is no quota](../facts/sqs.md#sqs-fifo-message-groups-no-quota)
sqs-fifo-no-duplicates-introduced
  claim: Unlike standard queues, FIFO queues do not introduce duplicate messages.
  scope: SQS FIFO queue.
  link: [FIFO queues don't introduce duplicate messages](../facts/sqs.md#sqs-fifo-no-duplicates-introduced)
  link: [Unlike standard queues](../facts/sqs.md#sqs-fifo-no-duplicates-introduced)
sqs-fifo-no-order-across-groups
  claim: In a FIFO queue, messages that have different message group IDs may arrive or be processed out of order relative to one another.
  scope: across message group IDs, SQS FIFO queue.
  link: [Messages with different message group IDs](../facts/sqs.md#sqs-fifo-no-order-across-groups)
  link: [may arrive or be processed out of order](../facts/sqs.md#sqs-fifo-no-order-across-groups)
sqs-fifo-no-per-message-timers
  claim: SQS FIFO queues do not support timers on individual messages.
  scope: FIFO queues, per-message timers.
  link: [don't support timers on individual messages](../facts/sqs.md#sqs-fifo-no-per-message-timers)
  link: [FIFO queues don't support timers](../facts/sqs.md#sqs-fifo-no-per-message-timers)
sqs-fifo-order-strict-within-group
  claim: In a FIFO queue, within one message group ID all messages are sent and received in strict order.
  scope: per message group ID, SQS FIFO queue.
  link: [Within a message group ID](../facts/sqs.md#sqs-fifo-order-strict-within-group)
  link: [sent and received in strict order](../facts/sqs.md#sqs-fifo-order-strict-within-group)
sqs-fifo-partition-throughput-3000-batched-300-single
  claim: Each partition of an SQS FIFO queue supports up to 3,000 messages per second with batching, or up to 300 messages per second for send, receive and delete operations, in supported Regions.
  scope: per partition of a FIFO queue; supported Regions; maximum; not adjustable.
  link: [up to 3,000 messages per second with batching](../facts/sqs.md#sqs-fifo-partition-throughput-3000-batched-300-single)
  link: [up to 300 messages per second](../facts/sqs.md#sqs-fifo-partition-throughput-3000-batched-300-single)
sqs-fifo-queue-name-suffix
  claim: The name of an SQS FIFO queue must end with the .fifo suffix, and the suffix counts towards the 80-character queue name quota.
  scope: per FIFO queue name.
  link: [must end with the .fifo suffix](../facts/sqs.md#sqs-fifo-queue-name-suffix)
  link: [counts towards the 80-character queue name quota](../facts/sqs.md#sqs-fifo-queue-name-suffix)
sqs-fifo-single-group-for-strict-order
  claim: To process all messages in a FIFO queue in strict order, use a single message group ID for every message in the queue.
  scope: SQS FIFO queue.
  link: [use a single message group ID](../facts/sqs.md#sqs-fifo-single-group-for-strict-order)
  link: [for all messages in the queue](../facts/sqs.md#sqs-fifo-single-group-for-strict-order)
sqs-horizontal-scaling-linear-gain
  claim: Scale SQS producers and consumers horizontally by adding more instances of each, and use action batching to send or receive multiple messages in a single request, reducing API call overhead. When you add more clients, you achieve essentially linear gains in queue throughput.
  scope: SQS queue.
  link: [Scale producers and consumers horizontally](../facts/sqs.md#sqs-horizontal-scaling-linear-gain)
  link: [essentially linear gains in queue throughput](../facts/sqs.md#sqs-horizontal-scaling-linear-gain)
sqs-idempotent-service-same-effect-as-single-request
  claim: An idempotent service promises that each request is processed exactly once, so that making multiple identical requests has the same effect as making a single request.
  scope: distributed systems, Well-Architected REL04-BP04.
  link: [multiple identical requests has the same effect](../facts/sqs.md#sqs-idempotent-service-same-effect-as-single-request)
  link: [as making a single request](../facts/sqs.md#sqs-idempotent-service-same-effect-as-single-request)
sqs-in-flight-fifo-limit
  claim: FIFO queues support a maximum of 120,000 in-flight messages (received by a consumer but not yet deleted); when the limit is reached, Amazon SQS does not return an error, but processing may be impacted.
  scope: per FIFO queue; maximum; adjustable; You can request an increase beyond this limit by contacting AWS Support..
  link: [120,000 in-flight messages](../facts/sqs.md#sqs-in-flight-fifo-limit)
  link: [does not return an error](../facts/sqs.md#sqs-in-flight-fifo-limit)
  say: one hundred twenty thousand in-flight messages
sqs-in-flight-limit-long-polling-no-error
  claim: When the in-flight message limit is reached while a consumer uses long polling, SQS does not return an error. It returns no new messages until the number of in-flight messages drops below the limit.
  scope: SQS queue, in-flight limit; long polling and in-flight limit reached.
  link: [does not return an error](../facts/sqs.md#sqs-in-flight-limit-long-polling-no-error)
  link: [will not return any new messages](../facts/sqs.md#sqs-in-flight-limit-long-polling-no-error)
sqs-in-flight-standard-limit
  claim: For most standard queues, there can be a maximum of approximately 120,000 in-flight messages (received by a consumer but not yet deleted), depending on queue traffic and message backlog.
  scope: per standard queue; maximum; adjustable; Depends on queue traffic and message backlog; to request a quota increase, submit a support request..
  link: [approximately 120,000 in flight messages](../facts/sqs.md#sqs-in-flight-standard-limit)
  link: [120,000](../facts/sqs.md#sqs-in-flight-standard-limit)
  say: about one hundred twenty thousand in-flight messages
sqs-in-flight-standard-limit-short-vs-long-polling
  claim: When a standard queue reaches its quota of in-flight messages (received by a consumer but not yet deleted), short polling returns the OverLimit error message, and long polling returns no error messages.
  scope: standard queues at the in-flight message quota.
  link: [returns the OverLimit error message](../facts/sqs.md#sqs-in-flight-standard-limit-short-vs-long-polling)
  link: [returns no error messages](../facts/sqs.md#sqs-in-flight-standard-limit-short-vs-long-polling)
sqs-kms-aws-managed-key-policy-not-modifiable
  claim: You cannot modify the key policy of the AWS managed KMS key for Amazon SQS.
  scope: AWS managed KMS key for Amazon SQS.
  link: [cannot modify the key policy](../facts/sqs.md#sqs-kms-aws-managed-key-policy-not-modifiable)
  link: [AWS managed KMS key for Amazon SQS](../facts/sqs.md#sqs-kms-aws-managed-key-policy-not-modifiable)
sqs-kms-aws-managed-key-unique-per-account-region
  claim: You can use the AWS managed KMS key for Amazon SQS, which is unique for each account and Region.
  scope: per account, per Region.
  link: [AWS managed KMS key for Amazon SQS](../facts/sqs.md#sqs-kms-aws-managed-key-unique-per-account-region)
  link: [unique for each account and region](../facts/sqs.md#sqs-kms-aws-managed-key-unique-per-account-region)
sqs-kms-consumer-needs-decrypt
  claim: A consumer must have the kms:Decrypt permission for any KMS key that encrypts the messages in the queue it reads.
  scope: SQS consumer, SSE-KMS queue.
  link: [the consumer must have the kms:Decrypt permission](../facts/sqs.md#sqs-kms-consumer-needs-decrypt)
  link: [encrypt the messages in the specified queue](../facts/sqs.md#sqs-kms-consumer-needs-decrypt)
sqs-kms-service-senders-need-customer-managed-key
  claim: Several AWS services act as event sources that can send events to SQS queues. To allow these event sources to work with encrypted queues, you must create a customer managed KMS key and add permissions in the key policy for the service to use the required AWS KMS API methods.
  scope: SQS queue with SSE-KMS, AWS service event sources.
  link: [create a customer managed KMS key](../facts/sqs.md#sqs-kms-service-senders-need-customer-managed-key)
  link: [permissions in the key policy](../facts/sqs.md#sqs-kms-service-senders-need-customer-managed-key)
sqs-lens-sqs-sns-eventbridge-roles-in-event-driven-design
  claim: The Serverless Applications Lens says to use messaging services like SQS for reliable and durable communication between microservices, SNS topics for fan out of events, and EventBridge when you need event filtering and routing.
  scope: Serverless Applications Lens, event-driven architectures.
  link: [reliable and durable communication between microservices](../facts/sqs.md#sqs-lens-sqs-sns-eventbridge-roles-in-event-driven-design)
  link: [you can utilize Amazon EventBridge](../facts/sqs.md#sqs-lens-sqs-sns-eventbridge-roles-in-event-driven-design)
sqs-locks-messages-multiple-producers-consumers
  claim: SQS locks messages during processing, so multiple producers can send and multiple consumers can receive messages at the same time.
  scope: SQS queue.
  link: [locks your messages during processing](../facts/sqs.md#sqs-locks-messages-multiple-producers-consumers)
  link: [multiple producers can send and multiple consumers](../facts/sqs.md#sqs-locks-messages-multiple-producers-consumers)
sqs-long-polling-http-timeout-longer-than-wait
  claim: To avoid HTTP errors, the HTTP response timeout for ReceiveMessage requests must be longer than the WaitTimeSeconds parameter.
  scope: SQS ReceiveMessage, long polling.
  link: [longer than the WaitTimeSeconds parameter](../facts/sqs.md#sqs-long-polling-http-timeout-longer-than-wait)
  link: [To avoid HTTP errors](../facts/sqs.md#sqs-long-polling-http-timeout-longer-than-wait)
sqs-long-polling-max-wait
  claim: When the wait time for the ReceiveMessage API action is greater than 0, long polling is in effect; the maximum long polling wait time is 20 seconds.
  scope: per ReceiveMessage request; maximum; not adjustable; Long polling is in effect when the wait time is greater than 0..
  link: [20 seconds](../facts/sqs.md#sqs-long-polling-max-wait)
  say: twenty seconds
sqs-long-polling-min-wait-1-second
  claim: If a 20-second ReceiveMessage wait time is too long for the application, a shorter ReceiveMessage wait time can be set, with a minimum of 1 second.
  scope: per ReceiveMessage request; long polling wait time; minimum; adjustable.
  link: [1 second minimum](../facts/sqs.md#sqs-long-polling-min-wait-1-second)
  say: one second
sqs-long-polling-queries-all-servers
  claim: With long polling, ReceiveMessage queries all servers and responds once at least one message is available. An empty response is sent only if the polling wait time expires.
  scope: SQS ReceiveMessage; long polling.
  link: [queries all servers for messages](../facts/sqs.md#sqs-long-polling-queries-all-servers)
  link: [sent only if the polling wait time expires](../facts/sqs.md#sqs-long-polling-queries-all-servers)
sqs-long-polling-reduces-empty-and-false-empty
  claim: Long polling helps reduce the cost of using SQS because it reduces the number of empty responses and of false empty responses (messages are available but not included in a response).
  scope: SQS ReceiveMessage; long polling.
  link: [reducing the number of empty responses](../facts/sqs.md#sqs-long-polling-reduces-empty-and-false-empty)
  link: [false empty responses](../facts/sqs.md#sqs-long-polling-reduces-empty-and-false-empty)
sqs-long-polling-wait-greater-than-zero
  claim: Long polling is in effect when the wait time for the ReceiveMessage API action is greater than 0.
  scope: per ReceiveMessage request.
  link: [greater than 0, long polling is in effect](../facts/sqs.md#sqs-long-polling-wait-greater-than-zero)
  link: [the wait time for the ReceiveMessage API action](../facts/sqs.md#sqs-long-polling-wait-greater-than-zero)
sqs-manual-delete-after-processing
  claim: Receiving a message does not delete it: the message remains in the queue but becomes temporarily invisible to other consumers. SQS offers two options for deleting messages after processing; with manual deletion, you explicitly delete messages with the DeleteMessage action.
  scope: SQS queue.
  link: [You explicitly delete messages](../facts/sqs.md#sqs-manual-delete-after-processing)
  link: [using the DeleteMessage action](../facts/sqs.md#sqs-manual-delete-after-processing)
sqs-message-attributes-count-toward-size
  claim: All components of an SQS message attribute are included in the 1 MiB message size restriction.
  scope: per message.
  link: [included in the 1 MiB message size restriction](../facts/sqs.md#sqs-message-attributes-count-toward-size)
  link: [All components of a message attribute](../facts/sqs.md#sqs-message-attributes-count-toward-size)
sqs-message-attributes-max
  claim: An SQS message can contain up to 10 metadata attributes.
  scope: per message; maximum; not adjustable.
  link: [10 metadata attributes](../facts/sqs.md#sqs-message-attributes-max)
  say: ten metadata attributes
sqs-message-retention-default
  claim: By default, an Amazon SQS queue keeps a message for 4 days.
  scope: per message in an SQS queue; default; adjustable; The retention period can be set between the minimum and the maximum..
  link: [4 days](../facts/sqs.md#sqs-message-retention-default)
  say: four days
sqs-message-retention-range
  claim: The SQS message retention period can be set from a minimum of 60 seconds (1 minute) to a maximum of 14 days (1,209,600 seconds).
  scope: per message in an SQS queue; the queue retention setting; maximum; adjustable; The default is 4 days..
  link: [60 seconds](../facts/sqs.md#sqs-message-retention-range)
  link: [14 days](../facts/sqs.md#sqs-message-retention-range)
  link: [1,209,600 seconds](../facts/sqs.md#sqs-message-retention-range)
  say: sixty seconds | fourteen days
sqs-message-size-range
  claim: An SQS message can be from a minimum of 1 byte (1 character) to a maximum of 1,048,576 bytes (1 MiB).
  scope: per message; maximum; not adjustable.
  link: [1 MiB](../facts/sqs.md#sqs-message-size-range)
  link: [1,048,576 bytes](../facts/sqs.md#sqs-message-size-range)
  link: [1 byte](../facts/sqs.md#sqs-message-size-range)
  say: one mebibyte | one byte
sqs-message-timer-initial-invisibility
  claim: A message timer sets an initial invisibility period for one message when it is added to a queue.
  scope: SQS message, per message.
  link: [initial invisibility period for a message](../facts/sqs.md#sqs-message-timer-initial-invisibility)
  link: [when it's added to a queue](../facts/sqs.md#sqs-message-timer-initial-invisibility)
sqs-message-timer-overrides-delay-queue
  claim: A message timer setting for an individual message overrides any DelaySeconds value on an SQS delay queue.
  scope: per message in a standard queue with a delay queue setting.
  link: [overrides any DelaySeconds value](../facts/sqs.md#sqs-message-timer-overrides-delay-queue)
  link: [A message timer setting for an individual message](../facts/sqs.md#sqs-message-timer-overrides-delay-queue)
sqs-message-timer-range
  claim: The delay for an individual SQS message (message timer) is 0 seconds by default, which is also the minimum, and the maximum is 15 minutes.
  scope: per message (message timer); maximum; not adjustable; The default and minimum delay is 0 seconds..
  link: [0 seconds](../facts/sqs.md#sqs-message-timer-range)
  link: [15 minutes](../facts/sqs.md#sqs-message-timer-range)
  say: zero seconds | fifteen minutes
sqs-metric-age-of-oldest-message-measures-lag
  claim: The ApproximateAgeOfOldestMessage metric reports, in seconds, the age of the oldest unprocessed message in the queue. It is reported if the queue contains at least one active message.
  scope: SQS queue CloudWatch metric.
  link: [ApproximateAgeOfOldestMessage](../facts/sqs.md#sqs-metric-age-of-oldest-message-measures-lag)
  link: [oldest unprocessed message in the queue](../facts/sqs.md#sqs-metric-age-of-oldest-message-measures-lag)
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
sqs-mq-resource-types-chart
  claim: In the resource-type chart of the SQS developer guide, Amazon MQ is a message broker, and Amazon SNS and Amazon SQS are not.
  scope: SQS developer guide overview (SQS, SNS and Amazon MQ); from the resource-type chart of the SQS developer guide.
  link: [Message brokers](../facts/sqs.md#sqs-mq-resource-types-chart)
  link: [Amazon MQ](../facts/sqs.md#sqs-mq-resource-types-chart)
sqs-no-receive-message-batch-action
  claim: There is no ReceiveMessageBatch action, because ReceiveMessage can process 10 messages at a time.
  scope: SQS ReceiveMessage action.
  link: [there is no ReceiveMessageBatch action](../facts/sqs.md#sqs-no-receive-message-batch-action)
  link: [can process 10 messages at a time](../facts/sqs.md#sqs-no-receive-message-batch-action)
sqs-policy-quota-bytes
  claim: The maximum size of an Amazon SQS policy is 8,192 bytes.
  scope: per SQS policy; maximum; not adjustable.
  link: [8,192 bytes](../facts/sqs.md#sqs-policy-quota-bytes)
sqs-policy-quota-conditions
  claim: An Amazon SQS queue policy can have a maximum of 10 conditions.
  scope: per queue policy; maximum; not adjustable.
  link: [10 conditions](../facts/sqs.md#sqs-policy-quota-conditions)
sqs-policy-quota-principals
  claim: An Amazon SQS queue policy can have a maximum of 50 principals.
  scope: per queue policy; maximum; not adjustable.
  link: [50 principals](../facts/sqs.md#sqs-policy-quota-principals)
sqs-policy-quota-statements
  claim: An Amazon SQS queue policy can have a maximum of 20 statements.
  scope: per queue policy; maximum; not adjustable.
  link: [20 statements](../facts/sqs.md#sqs-policy-quota-statements)
sqs-pricing-free-tier-1-million-requests
  claim: All customers can make 1 million Amazon SQS requests for free each month.
  scope: per month, all customers.
  link: [1 million Amazon SQS requests](../facts/sqs.md#sqs-pricing-free-tier-1-million-requests)
  link: [for free each month](../facts/sqs.md#sqs-pricing-free-tier-1-million-requests)
  say: one million requests
sqs-pricing-free-tier-no-rollover
  claim: Unused free tier usage for Amazon SQS does not roll over to the next month.
  scope: per month; free tier usage across all Regions except GovCloud.
  link: [does not roll over to the next month](../facts/sqs.md#sqs-pricing-free-tier-no-rollover)
  link: [Unused free usage](../facts/sqs.md#sqs-pricing-free-tier-no-rollover)
sqs-pricing-no-minimum-fee
  claim: With Amazon SQS you pay only for what you use and there is no minimum fee.
  scope: Amazon SQS account usage.
  link: [no minimum fee](../facts/sqs.md#sqs-pricing-no-minimum-fee)
  link: [you pay only for what you use](../facts/sqs.md#sqs-pricing-no-minimum-fee)
sqs-queue-backlog-unlimited
  claim: The number of messages that an Amazon SQS queue can store is unlimited.
  scope: per queue, messages waiting in the backlog; maximum; not adjustable.
  link: [is unlimited](../facts/sqs.md#sqs-queue-backlog-unlimited)
  link: [can store is unlimited](../facts/sqs.md#sqs-queue-backlog-unlimited)
sqs-queue-is-the-only-resource
  claim: In Amazon SQS, the queue is the only resource. A policy identifies it with an Amazon Resource Name (ARN).
  scope: SQS policies.
  link: [the only resource is the queue](../facts/sqs.md#sqs-queue-is-the-only-resource)
  link: [use an Amazon Resource Name (ARN)](../facts/sqs.md#sqs-queue-is-the-only-resource)
sqs-queue-name-max-length
  claim: An SQS queue name can have up to 80 characters; alphanumeric characters, hyphens and underscores are accepted. The name of a FIFO queue must end with the .fifo suffix, and the suffix counts towards the 80-character queue name quota.
  scope: per queue name; maximum; not adjustable; Queue names are case-sensitive..
  link: [80 characters](../facts/sqs.md#sqs-queue-name-max-length)
  say: eighty characters
sqs-receive-keeps-message-hidden
  claim: When a consumer receives a message, the message stays in the queue but becomes temporarily invisible to other consumers.
  scope: SQS queue.
  link: [it remains in the queue](../facts/sqs.md#sqs-receive-keeps-message-hidden)
  link: [temporarily invisible to other consumers](../facts/sqs.md#sqs-receive-keeps-message-hidden)
sqs-redrive-defaults-to-source-queue-same-type
  claim: By default, dead-letter queue redrive moves messages from the dead-letter queue to the source queue. You can choose any other queue as the redrive destination if both queues are the same type.
  scope: SQS dead-letter queue redrive; default; adjustable.
  link: [from a dead-letter queue to a source queue](../facts/sqs.md#sqs-redrive-defaults-to-source-queue-same-type)
  link: [if both queues are the same type](../facts/sqs.md#sqs-redrive-defaults-to-source-queue-same-type)
sqs-redrive-no-filter-or-modify
  claim: SQS does not support filtering and modifying messages while redriving them from the dead-letter queue.
  scope: SQS dead-letter queue redrive.
  link: [doesn't support filtering and modifying messages](../facts/sqs.md#sqs-redrive-no-filter-or-modify)
  link: [while redriving them from the dead-letter queue](../facts/sqs.md#sqs-redrive-no-filter-or-modify)
sqs-redrive-oldest-first-order
  claim: A dead-letter queue redrive moves messages in the order they were received, starting with the oldest message.
  scope: SQS dead-letter queue redrive.
  link: [in the order they are received](../facts/sqs.md#sqs-redrive-oldest-first-order)
  link: [starting with the oldest message](../facts/sqs.md#sqs-redrive-oldest-first-order)
sqs-redrive-resets-retention-and-assigns-new-id
  claim: A redrive task resets the retention period. All redriven messages are treated as new messages with a new message ID and enqueue time.
  scope: SQS dead-letter queue redrive.
  link: [redrive task resets the retention period](../facts/sqs.md#sqs-redrive-resets-retention-and-assigns-new-id)
  link: [considered new messages](../facts/sqs.md#sqs-redrive-resets-retention-and-assigns-new-id)
sqs-scales-transparently-for-spikes
  claim: SQS can process each buffered request independently and scales transparently to handle load increases or spikes without any provisioning instructions.
  scope: SQS.
  link: [scaling transparently to handle any load increases](../facts/sqs.md#sqs-scales-transparently-for-spikes)
  link: [without any provisioning instructions](../facts/sqs.md#sqs-scales-transparently-for-spikes)
sqs-send-stored-multi-az-before-ack
  claim: When you send a message, SQS stores it redundantly in multiple Availability Zones before acknowledging it, so no single computer, network or Availability Zone failure makes the message inaccessible.
  scope: SQS queue, SendMessage.
  link: [stores the message in multiple availability zones](../facts/sqs.md#sqs-send-stored-multi-az-before-ack)
  link: [no single computer, network, or AZ failure](../facts/sqs.md#sqs-send-stored-multi-az-before-ack)
sqs-short-polling-is-default-immediate-response
  claim: Short polling is the default. The ReceiveMessage request queries a subset of servers and sends an immediate response, even if no messages are found.
  scope: SQS ReceiveMessage; default; adjustable.
  link: [Short polling (default)](../facts/sqs.md#sqs-short-polling-is-default-immediate-response)
  link: [even if no messages are found](../facts/sqs.md#sqs-short-polling-is-default-immediate-response)
sqs-short-polling-request-may-miss-messages
  claim: With short polling, a particular ReceiveMessage request might not return all of your messages.
  scope: SQS ReceiveMessage, short polling.
  link: [might not return all of your messages](../facts/sqs.md#sqs-short-polling-request-may-miss-messages)
  link: [a particular ReceiveMessage request](../facts/sqs.md#sqs-short-polling-request-may-miss-messages)
sqs-short-polling-samples-subset-of-servers
  claim: With short polling, SQS samples a subset of its servers and returns messages from only those servers.
  scope: SQS ReceiveMessage, standard and FIFO queues; short polling.
  link: [samples a subset of its servers](../facts/sqs.md#sqs-short-polling-samples-subset-of-servers)
  link: [returns messages from only those servers](../facts/sqs.md#sqs-short-polling-samples-subset-of-servers)
sqs-sns-recommended-for-new-applications
  claim: SQS and SNS are recommended for new applications that can benefit from nearly unlimited scalability and simple APIs. They generally offer more cost-effective solutions for high-volume applications with their pay-as-you-go pricing.
  scope: SQS developer guide overview (SQS, SNS and Amazon MQ).
  link: [recommended for new applications](../facts/sqs.md#sqs-sns-recommended-for-new-applications)
  link: [nearly unlimited scalability and simple APIs](../facts/sqs.md#sqs-sns-recommended-for-new-applications)
sqs-sse-anonymous-requests-rejected
  claim: With SSE enabled, anonymous SendMessage and ReceiveMessage requests to the encrypted queue are rejected.
  scope: SQS queue with SSE.
  link: [anonymous SendMessage and ReceiveMessage requests](../facts/sqs.md#sqs-sse-anonymous-requests-rejected)
  link: [to the encrypted queue will be rejected](../facts/sqs.md#sqs-sse-anonymous-requests-rejected)
sqs-sse-backlogged-messages-not-encrypted
  claim: A message is encrypted only if it is sent after encryption of the queue is enabled. SQS does not encrypt messages that are already in the queue.
  scope: SQS queue when SSE is enabled.
  link: [encrypted only if it is sent after](../facts/sqs.md#sqs-sse-backlogged-messages-not-encrypted)
  link: [doesn't encrypt backlogged messages](../facts/sqs.md#sqs-sse-backlogged-messages-not-encrypted)
sqs-sse-default-key-no-cross-account-lambda
  claim: An encrypted queue that uses the default key (the AWS managed KMS key for Amazon SQS) cannot invoke a Lambda function in a different AWS account.
  scope: SQS queue encrypted with the AWS managed KMS key for Amazon SQS.
  link: [cannot invoke a Lambda function](../facts/sqs.md#sqs-sse-default-key-no-cross-account-lambda)
  link: [in a different AWS account](../facts/sqs.md#sqs-sse-default-key-no-cross-account-lambda)
sqs-sse-does-not-encrypt-metadata
  claim: SQS server-side encryption does not encrypt queue metadata (queue name and attributes), message metadata (message ID, timestamp, and attributes) or per-queue metrics.
  scope: SQS queue with SSE.
  link: [Queue metadata (queue name and attributes)](../facts/sqs.md#sqs-sse-does-not-encrypt-metadata)
  link: [Message metadata (message ID, timestamp, and attributes)](../facts/sqs.md#sqs-sse-does-not-encrypt-metadata)
  link: [Per-queue metrics](../facts/sqs.md#sqs-sse-does-not-encrypt-metadata)
sqs-sse-encrypts-message-body
  claim: SQS server-side encryption encrypts the body of a message in a queue.
  scope: SQS queue with SSE.
  link: [encrypts the body of a message](../facts/sqs.md#sqs-sse-encrypts-message-body)
sqs-sse-managed-encryption-on-by-default
  claim: Amazon SQS provides managed server-side encryption by default.
  scope: new SQS queue created in the console; default; adjustable.
  link: [managed server-side encryption by default](../facts/sqs.md#sqs-sse-managed-encryption-on-by-default)
  link: [Amazon SQS provides managed server-side encryption](../facts/sqs.md#sqs-sse-managed-encryption-on-by-default)
sqs-sse-requests-need-https-sigv4
  claim: All requests to queues with SSE enabled must use HTTPS and Signature Version 4.
  scope: SQS queue with SSE.
  link: [must use HTTPS and Signature Version 4](../facts/sqs.md#sqs-sse-requests-need-https-sigv4)
  link: [queues with SSE enabled](../facts/sqs.md#sqs-sse-requests-need-https-sigv4)
sqs-sse-two-key-types
  claim: SQS server-side encryption protects message contents with SQS-managed encryption keys (SSE-SQS) or with keys managed in AWS KMS (SSE-KMS).
  scope: SQS queue.
  link: [SQS-managed encryption keys (SSE-SQS)](../facts/sqs.md#sqs-sse-two-key-types)
  link: [AWS Key Management Service (SSE-KMS)](../facts/sqs.md#sqs-sse-two-key-types)
sqs-standard-at-least-once-duplicates
  claim: A standard queue ensures at-least-once delivery, so more than one copy of a message might be delivered, and messages may occasionally arrive out of order.
  scope: SQS standard queue.
  link: [at-least-once message delivery](../facts/sqs.md#sqs-standard-at-least-once-duplicates)
  link: [more than one copy of a message](../facts/sqs.md#sqs-standard-at-least-once-duplicates)
  link: [messages may occasionally arrive out of order](../facts/sqs.md#sqs-standard-at-least-once-duplicates)
sqs-standard-best-effort-ordering
  claim: A standard queue makes a best-effort attempt to keep the order in which messages are sent.
  scope: SQS standard queue.
  link: [best-effort attempt to maintain the order](../facts/sqs.md#sqs-standard-best-effort-ordering)
  link: [best-effort attempt](../facts/sqs.md#sqs-standard-best-effort-ordering)
sqs-standard-throughput-nearly-unlimited
  claim: SQS standard queues support a very high, nearly unlimited number of API calls per second for each action (SendMessage, ReceiveMessage, DeleteMessage).
  scope: per standard queue, per API action.
  link: [nearly unlimited number of API calls per second](../facts/sqs.md#sqs-standard-throughput-nearly-unlimited)
  link: [nearly unlimited](../facts/sqs.md#sqs-standard-throughput-nearly-unlimited)
sqs-temporary-queues-map-onto-one-queue
  claim: The Temporary Queue Client maps many application-managed temporary queues onto a single SQS queue, so the application makes fewer API calls and gets higher throughput when traffic to each temporary queue is low.
  scope: SQS Temporary Queue Client; low traffic to each temporary queue.
  link: [onto a single Amazon SQS queue automatically](../facts/sqs.md#sqs-temporary-queues-map-onto-one-queue)
  link: [fewer API calls and have a higher throughput](../facts/sqs.md#sqs-temporary-queues-map-onto-one-queue)
sqs-temporary-queues-request-response-use-case
  claim: The most common use case for temporary queues is the request-response messaging pattern, where a requester creates a temporary queue to receive each response message.
  scope: SQS Temporary Queue Client.
  link: [the request-response messaging pattern](../facts/sqs.md#sqs-temporary-queues-request-response-use-case)
  link: [temporary queue for receiving each response message](../facts/sqs.md#sqs-temporary-queues-request-response-use-case)
sqs-typically-single-subscriber-order-and-loss
  claim: SQS typically processes messages through a single subscriber, which is ideal for workflows where order and loss prevention are critical; to distribute wider, combine SQS with SNS for a fanout pattern.
  scope: SQS developer guide overview (SQS, SNS and Amazon MQ).
  link: [a single subscriber typically](../facts/sqs.md#sqs-typically-single-subscriber-order-and-loss)
  link: [fanout messaging pattern](../facts/sqs.md#sqs-typically-single-subscriber-order-and-loss)
sqs-undeleted-message-visible-again
  claim: If the consumer does not delete a message before the visibility timeout expires, the message becomes visible again in the queue and another consumer can retrieve it.
  scope: SQS queue; message not deleted before the visibility timeout expires.
  link: [becomes visible again in the queue](../facts/sqs.md#sqs-undeleted-message-visible-again)
  link: [retrieved by another consumer](../facts/sqs.md#sqs-undeleted-message-visible-again)
sqs-virtual-queues-incur-no-cost
  claim: Because a virtual queue makes no API calls to SQS, virtual queues incur no cost.
  scope: SQS virtual queue.
  link: [virtual queues incur no cost](../facts/sqs.md#sqs-virtual-queues-incur-no-cost)
  link: [makes no API calls to Amazon SQS](../facts/sqs.md#sqs-virtual-queues-incur-no-cost)
sqs-visibility-timeout-default
  claim: The default visibility timeout for an SQS message is 30 seconds.
  scope: per message; default; adjustable.
  link: [30 seconds](../facts/sqs.md#sqs-visibility-timeout-default)
  say: thirty seconds
sqs-visibility-timeout-extend-no-reset
  claim: The maximum visibility timeout of 12 hours is counted from the time Amazon SQS receives the ReceiveMessage request, and extending the visibility timeout does not reset that 12 hour maximum.
  scope: per message, counted from the ReceiveMessage request; maximum.
  link: [12 hours](../facts/sqs.md#sqs-visibility-timeout-extend-no-reset)
  link: [does not reset the 12 hour maximum](../facts/sqs.md#sqs-visibility-timeout-extend-no-reset)
  say: twelve hours
sqs-visibility-timeout-longer-than-sdk-read-timeout
  claim: For reliable processing, set the visibility timeout longer than the AWS SDK read timeout. This applies to ReceiveMessage with short polling and with long polling.
  scope: SQS ReceiveMessage.
  link: [longer than the AWS SDK read timeout](../facts/sqs.md#sqs-visibility-timeout-longer-than-sdk-read-timeout)
  link: [reducing the risk of duplicate processing](../facts/sqs.md#sqs-visibility-timeout-longer-than-sdk-read-timeout)
sqs-visibility-timeout-range
  claim: The SQS visibility timeout can be set from a minimum of 0 seconds to a maximum of 12 hours.
  scope: per message; maximum; adjustable; The default is 30 seconds..
  link: [0 seconds](../facts/sqs.md#sqs-visibility-timeout-range)
  link: [12 hours](../facts/sqs.md#sqs-visibility-timeout-range)
  say: zero seconds | twelve hours
sqs-visibility-timeout-too-long-delays-retry
  claim: A visibility timeout that is far longer than the processing time makes you wait a long time before a failed message can be processed again.
  scope: SQS queue; visibility timeout much longer than processing time.
  link: [wait for a relatively long time](../facts/sqs.md#sqs-visibility-timeout-too-long-delays-retry)
  link: [to attempt to process the message again](../facts/sqs.md#sqs-visibility-timeout-too-long-delays-retry)
sqs-visibility-timeout-too-short-gives-duplicate
  claim: If the visibility timeout is shorter than the time a consumer needs to process a message, another consumer receives a duplicate while the original consumer is still working on it.
  scope: SQS queue; visibility timeout shorter than processing time.
  link: [a duplicate message is received by another consumer](../facts/sqs.md#sqs-visibility-timeout-too-short-gives-duplicate)
  link: [original consumer is still working on the message](../facts/sqs.md#sqs-visibility-timeout-too-short-gives-duplicate)
sqs-vpc-endpoint-https-only
  claim: You can use Amazon VPC only with HTTPS Amazon SQS endpoints.
  scope: VPC to SQS.
  link: [only with HTTPS Amazon SQS endpoints](../facts/sqs.md#sqs-vpc-endpoint-https-only)
  link: [Amazon Virtual Private Cloud only](../facts/sqs.md#sqs-vpc-endpoint-https-only)
sqs-vpc-endpoint-keeps-traffic-off-public-internet
  claim: A connection between your VPC and SQS lets you send messages to your queues without crossing the public internet.
  scope: VPC to SQS; VPC endpoint for Amazon SQS.
  link: [without crossing the public internet](../facts/sqs.md#sqs-vpc-endpoint-keeps-traffic-off-public-internet)
  link: [send messages to your Amazon SQS queues](../facts/sqs.md#sqs-vpc-endpoint-keeps-traffic-off-public-internet)
sqs-vpc-interface-endpoint-no-gateway-or-nat
  claim: To connect a VPC to SQS you first define an interface VPC endpoint. The endpoint gives connectivity without requiring an internet gateway, a NAT instance or a VPN connection.
  scope: VPC to SQS.
  link: [you must first define an interface VPC endpoint](../facts/sqs.md#sqs-vpc-interface-endpoint-no-gateway-or-nat)
  link: [without requiring an internet gateway](../facts/sqs.md#sqs-vpc-interface-endpoint-no-gateway-or-nat)
sqs-vs-mq-new-apps-vs-broker-migration
  claim: AWS recommends Amazon MQ for migrating applications from existing message brokers that rely on APIs such as JMS or on protocols such as AMQP, MQTT, OpenWire and STOMP.
  scope: SQS developer guide overview (SQS, SNS and Amazon MQ).
  link: [We recommend Amazon MQ for migrating applications](../facts/sqs.md#sqs-vs-mq-new-apps-vs-broker-migration)
  link: [such as Advanced Message Queuing Protocol (AMQP)](../facts/sqs.md#sqs-vs-mq-new-apps-vs-broker-migration)
sqs-wa-back-pressure-slow-down-or-stop-incoming-data
  claim: Ignoring back pressure: a workload should have the ability to slow down or stop incoming data when a component cannot process it at the same rate.
  scope: Well-Architected reliability pillar, REL04-BP02.
  link: [Ignoring back pressure](../facts/sqs.md#sqs-wa-back-pressure-slow-down-or-stop-incoming-data)
  link: [slow down or stop incoming data](../facts/sqs.md#sqs-wa-back-pressure-slow-down-or-stop-incoming-data)
sqs-wa-idempotency-token-lets-client-retry
  claim: To make a request idempotent, clients can issue API requests with an idempotency token, which is used whenever the request is repeated; this makes it easier for a client to implement retries.
  scope: Well-Architected reliability pillar, REL04-BP04 idempotent operations.
  link: [an idempotency token](../facts/sqs.md#sqs-wa-idempotency-token-lets-client-retry)
  link: [implement retries without fear](../facts/sqs.md#sqs-wa-idempotency-token-lets-client-retry)
sqs-wa-loose-coupling-via-intermediate-durable-layer
  claim: To further improve resiliency through loose coupling, make component interactions asynchronous where possible: one component generates events and another consumes them, and the two components do not integrate through direct point-to-point interaction but usually through an intermediate durable storage layer, such as an SQS queue, a streaming data platform such as Kinesis, or Step Functions.
  scope: Well-Architected reliability pillar, REL04-BP02 loosely coupled dependencies.
  link: [an intermediate durable storage layer](../facts/sqs.md#sqs-wa-loose-coupling-via-intermediate-durable-layer)
  link: [such as an Amazon SQS queue](../facts/sqs.md#sqs-wa-loose-coupling-via-intermediate-durable-layer)
sqs-wa-make-component-interactions-asynchronous
  claim: To improve resiliency through loose coupling, make component interactions asynchronous where possible. This suits any interaction that does not need an immediate response and where an acknowledgment that the request was registered is enough.
  scope: Well-Architected reliability pillar, REL04-BP02 loosely coupled dependencies.
  link: [make component interactions asynchronous where possible](../facts/sqs.md#sqs-wa-make-component-interactions-asynchronous)
  link: [an acknowledgment that a request has been registered](../facts/sqs.md#sqs-wa-make-component-interactions-asynchronous)
sqs-wa-queue-or-stream-lets-you-burst-to-higher-throttle-rates
  claim: Where a system can tolerate asynchronous processing, you can put messages into a queue or stream to speed up responses to service clients, which allows you to burst to higher throttle rates.
  scope: Well-Architected reliability pillar, REL05-BP02 throttle requests.
  link: [put messages into a queue or stream](../facts/sqs.md#sqs-wa-queue-or-stream-lets-you-burst-to-higher-throttle-rates)
  link: [burst to higher throttle rates](../facts/sqs.md#sqs-wa-queue-or-stream-lets-you-burst-to-higher-throttle-rates)
sqs-wa-queues-in-hard-real-time-systems-stale-requests
  claim: In most hard real-time systems, requests older than a threshold time (often seconds) should be considered stale, because the client has given up, and not processed, even though queues offer several advantages.
  scope: Well-Architected reliability pillar, REL04-BP02 loosely coupled dependencies.
  link: [should be considered stale](../facts/sqs.md#sqs-wa-queues-in-hard-real-time-systems-stale-requests)
  link: [most hard real-time systems](../facts/sqs.md#sqs-wa-queues-in-hard-real-time-systems-stale-requests)
