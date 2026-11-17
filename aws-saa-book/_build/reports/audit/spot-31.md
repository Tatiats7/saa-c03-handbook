# spot-31: Opus spot check of chapter 31 (SQS, SNS and EventBridge) entail votes

Date: 2026-10-13. Checker: spot-31 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round, before adjudication.

## Sample

Pool: 557 facts with home_chapter 31 and status mech-pass in `data/facts/sqs.jsonl`, `data/facts/sns.jsonl` and `data/facts/eventbridge.jsonl`. Ids sorted, `random.Random(20261013 + 31).sample(pool, 30)`. Ids in `spot-31.sample.json`.

Each fact was judged from its claim, values, qualifiers, quotes, packet context and headings (`facts show`, the `31-entail-*` packets) and, where the context mattered, `show <source> --around`, under the strict rule of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 23. Not positive (partial): 7.
- The first-round voters had already marked 6 of the 7 partial.
- Voter misses (voter support, spot-31 partial): 1 of 30 (`sns-message-size-optin-1mib`). Under three: **no flag** for chapter 31 under RULINGS 2026-10-13 safeguard 2. (These entail votes ran on Opus; the measure agrees with that.)
- One sampled fact had no first-round entail vote: `sqs-fifo-queue-name-suffix` (spot-31: support). The adjudicator should check that its batch was voted.

## Non-positive verdicts

| Fact | First-round vote | spot-31 | Reason |
|---|---|---|---|
| sns-fifo-content-based-dedup-hash-of-body | partial | partial | Claim said "you do not set one" (quote: "don't need to"); the overriding published deduplication ID stands two sentences later. |
| sqs-in-flight-standard-limit-short-vs-long-polling | partial | partial | "this quota" (the in-flight quota of a standard queue) resolves only in the preceding sentence. |
| sns-pricing-standard-publish-64kb-chunk | partial | partial | The "Standard topics" scope stands only in the sibling section sentence, not in the quote or its "API Requests" heading. |
| sqs-failed-processing-message-not-lost | partial | partial | The failure causes and "becomes visible again" stand only in the preceding sentence. |
| sqs-manual-delete-after-processing | partial | partial | "after processing" stands only in the sentence that follows quote 1. |
| sns-sqs-envelope-contains-subject-message-metadata | partial | partial | The qualifier condition (raw message delivery disabled) had no quote, and the claim stated the JSON envelope without the raw-delivery exception. |
| sns-message-size-optin-1mib | support | partial | Universal "up to 1 MiB when configured"; the next sentence and the "Setting MaximumMessageSize" section restrict it to topics with 100 or fewer subscriptions, all Firehose, SQS or Lambda. |

## Amended (each once, `--by spot-31`, all now rev 2, mech-pass; no dependents; 0 open conflicts after)

Patch files: `_build/work/31-messaging/spot-31/<id>.json`. Every quote is verbatim from the same saved page except where noted.

1. **sns-fifo-content-based-dedup-hash-of-body**: claim now says "you don't need to set one" and that a published deduplication ID overrides the generated one; added that verbatim sentence (same page) and a display "the published deduplication ID overrides".
2. **sqs-in-flight-standard-limit-short-vs-long-polling**: quote extended to the whole bullet text from "For most standard queues ..." to "... returns no error messages." (same line); claim names the in-flight quota without a number, so no new conflict with the 120,000 fact.
3. **sns-pricing-standard-publish-64kb-chunk**: added the verbatim "Standard topic pricing is based on ..." sentence (same page); claim names Standard topic pricing and API requests.
4. **sqs-failed-processing-message-not-lost**: quote now holds the three sentences of "Handling failures" (with the page's em dashes); claim follows them and qualifiers.condition names the visibility-timeout condition.
5. **sqs-manual-delete-after-processing**: quote 1 now runs to the end of its line ("... deleting messages after processing:"); claim reordered to follow the quotes.
6. **sns-sqs-envelope-contains-subject-message-metadata**: added the verbatim raw-delivery sentence from `docs/sns/latest/dg/sns-large-payload-raw-message-delivery` (another saved AWS page; the SNS-to-SQS page has no raw-delivery text). The quote keeps the page's typo "for or Amazon SQS endpoints". Claim carries the exception; display "any Amazon SNS metadata is stripped" added.
7. **sns-message-size-optin-1mib**: added the verbatim "To set MaximumMessageSize above 256 KiB, the topic must have 100 or fewer total subscriptions ..." sentence (same page); claim and condition carry the restriction; display "100 or fewer total subscriptions" added. Note: `sns-message-size-optin-endpoints-and-100-subscriptions` states the same restriction separately; claim similarity was checked (below 0.4) and no conflict opened.

No batch was cut and nothing was finalized. The adjudicator sends these seven to a fresh independent vote (the currency vote of `sns-message-size-optin-1mib` and `sns-pricing-standard-publish-64kb-chunk` is also void at rev 2). No fact judged positive was touched.

## Positive (23)

eventbridge-quota-rules-per-bus, eventbridge-cross-account-events-not-forwarded-again, sqs-faq-long-polling-fewer-empty-receives-lower-cost, sns-dlq-queue-type-matches-topic-type, sqs-sse-two-key-types, eventbridge-target-needs-permission-to-access, eventbridge-putevents-partial-failure-caller-retries, eventbridge-pricing-schema-registry-free, sns-fifo-same-filtering-as-standard, sqs-fifo-queue-name-suffix, eventbridge-faq-pipes-sources-sqs-kinesis-dynamodb-kafka-mq, sqs-faq-jms-library-jms-1-1, sns-sqs-queue-needs-policy-allowing-topic, sns-fifo-topic-delivers-to-sqs-standard-and-fifo, sqs-faq-long-poll-timeout-min-1-second, eventbridge-decision-no-persistence-at-least-once, sqs-pricing-no-minimum-fee, sqs-faq-sse-producer-needs-generatedatakey-and-decrypt, sqs-message-attributes-max, eventbridge-scheduler-execution-role-assumed, eventbridge-pipe-single-source-single-target, eventbridge-scheduler-one-time-schedule-invokes-once, eventbridge-change-custom-event-bus-classic-rename-2026.

## Observations for the adjudicator (not entail verdicts)

- `eventbridge-decision-no-persistence-at-least-once`: the decision-guide quote carries the claim, so entail is support. But the claim "does not persist events" is contradicted by the new Custom Event Bus (retention 1 to 365 days, `eventbridge-change-custom-event-bus-classic-rename-2026`). Consider scoping it to Custom Event Bus - Classic and setting `volatility` so that it gets a currency vote.
- `sqs-faq-sse-producer-needs-generatedatakey-and-decrypt`: entail support; the open question about the July 2024 history row is a currency question and is stated in the condition.
- `eventbridge-target-needs-permission-to-access`: support; the page notes it describes Custom Event Bus - Classic rules, which matches the scope "EventBridge rule target".
