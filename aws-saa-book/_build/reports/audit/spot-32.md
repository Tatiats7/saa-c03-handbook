# spot-32: Opus spot check of chapter 32 (Step Functions, Amazon MQ and AppFlow) entail votes

Date: 2026-10-14. Checker: spot-32 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round, before adjudication.

## Sample

Pool: 502 facts with home_chapter 32 and status mech-pass in `data/facts/{step-functions,mq,appflow}.jsonl`. Ids sorted, `random.Random(20261013 + 32).sample(pool, 30)` (seed 20261045). Ids in `spot-32.sample.json`.

I judged each fact from its claim, values, qualifiers, quotes, the packet context and the headings (`facts show`, packets `32-entail-001` to `007`). Where the context mattered, I also used `show <source>`. The rule was the strict one in TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 23. Not positive (partial): 7.
- The first-round voters had already marked 3 of the 7 as partial: task-states, human-in-the-loop and task-credentials.
- Voter misses (the voter said support, spot-32 says partial): 4 of 30: `step-functions-faq-vs-swf-new-applications`, `step-functions-sdk-integrations-no-sync`, `appflow-quota-concurrent-flow-runs` and `mq-activemq-network-of-brokers`. That is three or more, so **chapter 32 is flagged** (RULINGS 2026-10-13 flag rule).
- Every sampled fact had a first-round entail vote.

## Non-positive verdicts

| Fact | First-round vote | spot-32 | Reason |
|---|---|---|---|
| step-functions-faq-vs-swf-new-applications | support | partial | Universal claim with a nearby exception. The quote says "consider Step Functions for all your new applications". The very next sentence says to consider Amazon SWF when external signals must intervene or when child processes return a result to a parent. |
| step-functions-sdk-integrations-no-sync | support | partial | The subject "AWS SDK integrations" stands only in the bold label above the table. Neither the row ("Over two hundred services") nor the table header nor the headings name it. |
| appflow-quota-concurrent-flow-runs | support | partial | Qualifier `adjustable: true` has no support, and the fact's own condition admits that the page does not mark this quota. The per-account scope ("Your AWS account has the following quotas") and the "default" stand only in the surrounding lines. |
| mq-activemq-network-of-brokers | support | partial | The ActiveMQ scope stands only in the line above the quote: "Amazon MQ supports ActiveMQ's network of brokers feature." The claim's first clause is that line. |
| step-functions-task-states-unit-of-work-other-service | partial | partial | Exception nearby: the note says workers that run outside Step Functions (activities) can also perform tasks. |
| step-functions-use-case-human-in-the-loop | partial | partial | The scope qualifier "Standard workflows with a callback task token" is not in the quote. The callback sentence comes after the quote, and "Standard" appears nowhere. |
| step-functions-task-credentials-target-role | partial | partial | The field name `Credentials` and "Optional" stand only in the bold label above the quote. |

## Amended (each once, `--by spot-32`; all mech-pass afterwards, `facts verify` 7 of 7 ok; no dependents)

Patch files: `_build/work/32-step-functions/spot-32/<id>.json`. Every quote is verbatim from a saved AWS page.

1. **step-functions-faq-vs-swf-new-applications** (now rev 2): the quote now covers both FAQ sentences, including the SWF exception. The claim and the condition now carry the exception. The displays did not change.
2. **step-functions-sdk-integrations-no-sync** (now rev 2): kept the table row and added a second quote from `integrate-services`: "Using AWS SDK integrations, your state machines can call over nine thousand API actions for over two hundred AWS services." This ties "Over two hundred services" to AWS SDK integrations. The claim did not change. The bold label could not be quoted (M4: not a sentence).
3. **step-functions-task-states-unit-of-work-other-service** (now rev 3; register-32 had made rev 2): added the note "(Note: You can also use workers that run outside of Step Functions to perform tasks. For more info, see Activities.)" as a second quote. The claim now adds that activities can also perform tasks.
4. **appflow-quota-concurrent-flow-runs** (now rev 2): added two quotes, the lead-in "Your AWS account has the following quotas related to Amazon AppFlow." and the opening paragraph on default quotas (Region-specific; some can be increased, some cannot). `adjustable` is now false, which matches the convention of `mq-limit-activemq-connections-micro` for an unmarked quota. The scope now says "per AWS account". The claim says the page does not mark whether this quota can be increased.
5. **mq-activemq-network-of-brokers** (now rev 2): added "Amazon MQ supports ActiveMQ's network of brokers feature." as the first quote. The claim did not change.
6. **step-functions-use-case-human-in-the-loop** (now rev 3): the scope is now "Step Functions workflows (example use case)". Added the callback and task token sentence as evidence. The claim adds the AWS example: wait until a person confirms, then continue.
7. **step-functions-task-credentials-target-role** (now rev 2): added two sentences from the same field block, "For examples of using this field in the Task state, see Task state's Credentials field examples." and "This field is supported by the Task types that use Lambda functions and a supported AWS service." The claim no longer says "optional". It names the field through these quotes and states the supported Task types.

No batch was cut and nothing was finalized. The adjudicator sends these seven to a fresh independent vote. No fact judged positive was touched. One page was fetched that was not yet in the corpus: `docs/step-functions/latest/dg/concepts-access-cross-acct-resources`. I read it while looking for a Credentials sentence and did not use it as evidence.

## Positive (23)

step-functions-iam-no-resource-based-policies, mq-limit-activemq-connections-micro, mq-faq-activemq-upgrade-manual-major-minor-patch-auto-minor, step-functions-catchers-not-for-top-level-failures, appflow-salesforce-bulk-no-compound-fields, step-functions-retry-backoffrate-default, step-functions-faq-lambda-serverless-event-driven-compute, appflow-change-2023-05-salesforce-jwt, appflow-quota-connector-profiles, step-functions-faq-map-state-inline-and-distributed, step-functions-sync-express-callers, mq-rabbitmq-enforced-ha-policy-overrides-custom, step-functions-async-express-returns-confirmation, mq-faq-network-of-brokers-active-standby-or-single-instance, mq-rabbitmq-configurable-storage-5gb-multiple, mq-faq-custom-configurations-new-and-existing, appflow-encrypts-data-at-rest-and-in-transit, mq-rabbitmq-cluster-maintenance-one-node-at-a-time, mq-change-2025-02-activemq-instance-eos, mq-faq-charged-for-instance-storage-and-data-transfer, mq-rabbitmq-m7g-recommended, step-functions-bp-activity-pollers-at-least-100, step-functions-faq-console-shows-realtime-status-and-history.

## Observations for the adjudicator (not entail verdicts)

- The same pattern probably affects other facts in this chapter: `appflow-quota-flows-per-account` and `appflow-quota-flow-runs-per-month` also have `adjustable: true` while their condition says the page does not mark them. They were not in the sample and I did not touch them.
- `mq-rabbitmq-enforced-ha-policy-overrides-custom`: support on entailment. The quote comes from the migration guide and is about classic mirrored queues. The currency vote should check how it relates to RabbitMQ 4.x and quorum queues before a writer states it in general terms.
- `step-functions-retry-backoffrate-default`: support. The definition sentence has no subject, but the second sentence in the quote names `BackoffRate`.
- `step-functions-bp-activity-pollers-at-least-100`: support. The claim names `GetActivityTask`, which is in the context, not in the quote. The heading ("polling for activity tasks") carries the meaning.
- Chapter pattern: bold field or term labels (`**Credentials** (Optional)`, `**AWS SDK integrations in Step Functions**`) are not headings for the tool. A quote under such a label does not carry the subject the label names.
