# Sonnet entail votes, chapters 27 and 28: blind re-vote and seeded audit (2026-10-13)

**Question.** Fact voting moved from Opus to Sonnet today. Earlier, Opus voters marked 8 to 9 percent of facts not positive. On chapters 27 (Aurora) and 28 (DynamoDB), whose facts Sonnet also mined, Sonnet voters marked only 2.7 percent. Did the Sonnet voters miss real problems, or are these facts simply clean?

**Short answer.** They missed some problems, but none of them is a wrong fact. In a blind sample of 60 facts that Sonnet voted `support`, I would mark 4 `partial` (6.7 percent) and 0 `unsure`. All 4 belong to the class of problem that Opus voters flag most often. In each, a clause, a per-what scope, a condition or an exception comes from the text around the quote, or is left out, rather than being stated in the quote itself. None of the 4 has a wrong value. The tool's seeded audit matched 20 of 20. Under the decision rule, 4 non-positive verdicts with no materially wrong claim gives **recommendation (a): keep Sonnet for entail votes**. This is a close call; see the verdict section.

## 1. Method

- **Rules applied.** I used the packet's `entail` instruction: `support` only when the quotes alone state every part of the claim and of each value, with the same scope and qualifiers; read a quote together with its `heading`. I also used the heading-scoped and display rulings of 2026-10-11 (RULINGS.md) and TOOLS.md 5.4 and 5.5. To match the Opus standard, I followed the pattern of Opus non-positive votes in chapters 01 to 26:
  - a clause of the claim that appears only in unquoted context is `partial`;
  - a per-what scope that is in neither the quote nor its context is `partial`;
  - a universal claim whose exception is stated in the next sentences is `partial` (precedent: `iam-rcp-applies-to-outside-principals-and-root`);
  - text in the context may resolve "it" or "these", and may support a qualifier.
- **Sample.** I drew a blind sample with Python `random.Random(20261013)`.
  - Population: the `verified` facts in `data/facts/{aurora,aurora-serverless,dynamodb,dax}.jsonl` with `home_chapter` 27 (823 facts) or 28 (707 facts), ids sorted.
  - Draw: `rng.sample(ids27, 30)`, then `rng.sample(ids28, 30)` with the same rng.
  - Ids are in `sonnet-entail-20261013.sample.json`.
- **Per fact.** I ran `facts show <id>`; the outputs are saved in `sonnet-entail-20261013/<id>.json`. I read the packet context (±5 lines) that the voter saw. Where the quote alone was not enough, I also read the page with `show` or `search`.
- **Seeded audit.** The tool's audit (`audit sample` with seed 20261013, 10 hard facts per chapter, then `audit packet`) was re-derived by me as a single agent from the corpus. No votes were cast; verdicts were computed offline with the tool's own rule (`saalib.facts._rederive_verdict`).

## 2. The sample (60 facts; ✗ marks my non-positive verdicts)

**Chapter 27 (30):**
- aurora-replicas-offload-reads
- aurora-mysql-promote-replica-reboots-instances
- aurora-endpoint-abstracts-connections-no-hardcode
- aurora-quota-read-replicas-per-primary
- aurora-serverless-invalid-credentials-still-resume
- aurora-global-db-multiple-clusters-multiple-regions
- aurora-mysql-write-forwarding-version-support
- ✗ aurora-clone-copy-on-write-max-15
- aurora-io-counted-same-writer-reader
- aurora-reserved-instance-io-optimized-30-percent-more-units
- aurora-reserved-instance-billing-discount-not-physical
- aurora-serverless-mixed-configuration-cluster
- aurora-recovery-from-restart-near-instant
- aurora-best-practice-ram-working-set-in-memory
- aurora-serverless-platform-version-new-clusters-latest
- aurora-faq-failover-cname-within-30s
- aurora-reader-endpoint-may-point-to-new-primary-briefly
- aurora-change-default-encryption-cannot-disable
- aurora-autoscaling-needs-all-instances-available
- aurora-faq-cross-region-cluster-15-replicas-tens-of-ms
- aurora-serverless-overprovision-raises-cost
- ✗ aurora-serverless-provisioned-suited-to-steady-workloads
- aurora-quota-rds-proxies-per-region
- aurora-pricing-storage-billed-gb-month-both-configurations
- aurora-clone-needs-source-with-instance
- aurora-faq-io-optimized-fits-io-intensive-workloads
- aurora-replica-failover-priority-specify
- aurora-cmp-rds-promote-replica-minutes-reboot
- aurora-export-snapshot-to-s3-for-long-term
- aurora-mysql-migrate-from-rds-snapshot-under-an-hour

**Chapter 28 (30):**
- ✗ dynamodb-pricing-streams-getrecords-1mb
- dynamodb-conditional-write-succeeds-only-if-condition
- dax-production-three-nodes-three-azs
- dynamodb-change-pitr-configurable-period-2025-01
- dynamodb-wa-relational-storage-upper-bounds
- dynamodb-wcu-definition
- dynamodb-faq-global-tables-zero-rpo-mrsc
- dynamodb-encrypt-at-rest-default
- dynamodb-streams-vs-kds-duplicates
- dynamodb-table-throughput-quota-on-demand
- dynamodb-gsi-same-table-class-as-base
- dynamodb-lsi-item-size-400kb-limit
- dynamodb-multi-account-global-tables-replica-per-account
- dynamodb-gt-mrsc-no-ttl-lsi-transactions
- dynamodb-pitr-restores-to-new-table
- dynamodb-successful-write-http-200-durable
- dynamodb-sort-key-length
- ✗ dynamodb-pricing-gt-rwru-example-0625
- dynamodb-number-precision
- dynamodb-partitions-managed-by-dynamodb
- dynamodb-lsi-item-collection-max
- dynamodb-faq-privatelink-interface-endpoints
- dynamodb-gsi-back-pressure-definition
- dax-cluster-node-count
- dynamodb-cloudwatch-consumed-capacity-metrics
- dynamodb-zero-etl-opensearch-search-without-code
- dynamodb-must-choose-capacity-mode
- dynamodb-faq-multi-account-table-names
- dynamodb-aws-owned-key-not-viewable
- dynamodb-table-class-standard-ia-same-performance

All 60 are `verified` with a Sonnet `support` vote at the current rev. One of them, `dynamodb-wa-relational-storage-upper-bounds`, had been marked `partial` by a Sonnet voter at rev 1 and was repaired. That shows the Sonnet voters do apply the rule some of the time.

## 3. Non-positive verdicts

| Fact | My verdict | Reason (the words that disagree) | Sonnet voter (batch): reason given | Materially wrong? |
|---|---|---|---|---|
| aurora-clone-copy-on-write-max-15 | partial | Scope `per source Aurora DB cluster` on a hard limit. The quote ("You can create up to 15 clones with copy-on-write protocol. After you have 15 clones, the next clone that you create is a full copy.") and its context never say what the 15 counts against. | 27-entail-002: "Quote and its context state the claim with the same scope and qualifiers." | No. The scope is right according to another AWS sentence that is not quoted: "After more than 15 clones of a source volume are allocated, subsequent clones become full copies" (Aurora PostgreSQL major-version upgrade topic, in the full guide). Fix: add that quote. |
| aurora-serverless-provisioned-suited-to-steady-workloads | partial | The claim adds "where you choose a DB instance class with a predefined amount of memory, CPU power and I/O bandwidth". The only quote is "In contrast, *Aurora provisioned clusters* are suitable for steady workloads."; the added clause is the next, unquoted sentence. | 27-entail-010: "Quote, read in its context and under its headings, states every part of the claim with the same scope and conditions." | No. The clause is true per the next sentence. Fix: add it as a quote or cut the clause. |
| dynamodb-pricing-streams-getrecords-1mb | partial | The claim is universal: "DynamoDB Streams reads are charged in streams read request units. Each GetRecords API call is billed as one streams read request unit". The voter's own packet context then says "You are not charged for GetRecords API calls invoked through DynamoDB triggers on AWS Lambda … not charged for GetRecords API calls invoked by DynamoDB global tables." The exception is dropped and the condition does not carry it. The first sentence also comes from context, not the quote. | 28-entail-007: "The quote, read with its context and headings, states every part of the claim with the same scope and qualifiers." | No. The 1 MB value and the unit are exactly as AWS states them, and the verified siblings `dynamodb-pricing-streams-lambda-getrecords-not-charged` and `dynamodb-ttl-streams-lambda-no-getrecords-charge` carry the exception. Fix: add the exception to `condition`. |
| dynamodb-pricing-gt-rwru-example-0625 | partial | The stored condition says "same rate as single-Region write request units". The quote ("… 84.35 million replicated write request units x $0.6250 per million") does not say this, and the packet context does not either. | 28-entail-007: same text as above. The currency voter added: "consistent with the Nov 2024 price cut (replicated writes at single-Region rate)". | No. The same pricing example, about 15 lines earlier, bills single-Region writes at "0.6250 per million writes". Fix: quote that row or drop the clause. |

**Positive, with observations (not counted):**
- `aurora-recovery-from-restart-near-instant`: binary-log recovery slows restarts. The claim keeps AWS's "without the binary log", so it stays positive.
- `dynamodb-gsi-back-pressure-definition`: the name "GSI back-pressure" comes from the heading and the next sentence. Accepted under heading-scoped reading.
- `aurora-change-default-encryption-cannot-disable`: the condition "where no encryption configuration is provided" belongs to the default-encryption sentence, not to "cannot disable". This is a placement nit.
- `dax-production-three-nodes-three-azs`: the condition says "development or test only", while AWS says it does "not recommend" fewer than three nodes for production.
- `dynamodb-table-throughput-quota-on-demand`: "per Region" is redundant for a per-table quota.

## 4. Counts

| | Positive | Partial | Unsure | Not positive |
|---|---|---|---|---|
| Chapter 27 (30) | 28 | 2 | 0 | 6.7 % |
| Chapter 28 (30) | 28 | 2 | 0 | 6.7 % |
| **Total (60)** | **56** | **4** | **0** | **6.7 %** (Wilson 95 % interval about 2.6 % to 16 %) |

**Calibration against the earlier chapters** (entail votes in `_build/facts/votes/*.jsonl`):
- Chapters 01 to 26: 5.7 to 13.6 percent of entail votes are not positive. By a keyword count, between about a quarter and four fifths of those reasons (typically a third to a half) say the problem is in context only, or not in the quote.
- Chapter 27: 25 of 854 not positive (2.9 percent). Chapter 28: 17 of 724 (2.3 percent). Together: 2.7 percent.
- Estimate under the Opus standard: Sonnet's own 2.7 percent, plus about 6.7 percent of the facts it passed, comes to about 9 percent. That is the same rate the Opus voters produced.
- So these facts are **not** cleaner than earlier chapters. The Sonnet voters approve roughly 2 in 3 of the facts an Opus voter would mark `partial`. What they miss is evidence coverage: a clause, scope or exception not carried by the quote. In this sample they missed no wrong values, units, default-versus-maximum mix-ups or "up to"-versus-"exactly" errors.
- Weak signal: 96 percent of the chapter 27 `support` reasons (65 percent in chapter 28) are their batch's single most common, boilerplate reason, against 3 to 23 percent in most earlier chapters. Chapters 14 and 26 (about 70 percent) still flagged 5.7 and 7.3 percent, so boilerplate alone does not prove leniency.

## 5. The tool's seeded audit

**Commands** (`--chapter` accepts one chapter, so I ran two samples of 10):
- `audit sample --n 10 --seed 20261013 --chapter 27 --json --out …/s20261013-n10-ch27.json`, the same for chapter 28, then `audit packet s20261013-n10 --out …/s20261013-n10-ch2{7,8}.packet.json`.
- Re-derivations: `sonnet-entail-20261013.rederive.json`.

**Mechanical checks:** 20 of 20 pass.

**Re-derivation: 20 of 20 match** under the tool's rule. No failures, so no chapter to expand.
- Chapter 27:
  - aurora-faq-add-1-to-15-replicas-three-azs
  - aurora-faq-cannot-encrypt-existing-instance
  - aurora-faq-failover-cname-within-30s
  - aurora-faq-global-db-10-secondary-regions (re-derived from the user guide: "up to 10 secondary DB clusters")
  - aurora-faq-global-db-definition (user guide)
  - aurora-faq-global-db-no-code-change-writer-endpoint
  - aurora-faq-global-db-physical-lag-under-one-second (user guide: "latency typically under a second")
  - aurora-faq-replica-lag-tens-of-ms-same-region
  - aurora-faq-segments-six-copies
  - aurora-faq-standard-pay-per-io-vs-io-optimized-included
- Chapter 28:
  - dax-cluster-node-count
  - dax-cluster-up-to-11-nodes
  - dax-default-ttl-5-minutes-both-caches
  - dax-eventually-consistent-microsecond-latency
  - dax-faq-fully-managed-caching-microseconds
  - dax-faq-microsecond-cache-10x
  - dax-ideal-fastest-reads-hot-keys
  - dax-no-cache-invalidation-or-population-needed
  - dax-not-ideal-no-microsecond-need-or-repeated-reads
  - dax-not-ideal-strong-reads-write-heavy-few-repeats

**Independent cross-checks.** For 9 facts I also checked against a second source, the primary user or developer guide. All 9 agree in substance, so no wrong fact. But the tool's rule would score 8 of the 9 as `mismatch`, purely on wording, because a phrase display or a small number is missing from the second source. Examples:
- "can't convert an unencrypted DB cluster" against the display "not currently supported";
- "usually much less than 100 milliseconds" against "tens of milliseconds";
- "without requiring you to manage" against "without requiring developers to manage";
- "up to 15 Aurora Replicas", which lacks the "1" of "1 to 15".

This is the same match-rule strictness as in `s20261011-n20.review.md`. A blind re-deriver who lands on the user guide instead of the FAQ would produce false failures.

**Findings about the audit tool:**
- **The seed does nothing here.** With `--chapter`, `audit sample` takes the chapter's `tier0` hard facts first, up to `n`. Chapter 27 has 16 such facts and chapter 28 has 125, so each sample is just the first 10 tier0 ids in alphabetical order.
  - Chapter 27 got only Aurora FAQ-page facts (three FAQ pages).
  - Chapter 28 got only DAX facts; no `dynamodb-*` fact was sampled.
  - The audit therefore covers a narrow, FAQ-heavy slice. To get a random hard-fact sample, run it without `--chapter`, or use `n` larger than the tier0 count.
- **File-name collision.** The report file is `s<seed>-n<n>.json` whatever the chapter, so the second run overwrites the first. `s20261013-n10.json` now holds the chapter 27 sample; the `-ch27`/`-ch28` copies keep both.
- **Entail side-note on this audit sample** (outside the 60, not counted). Two more facts show the same miss class: `dax-ideal-fastest-reads-hot-keys` ("such as a hot key during a one-day sale" is not in either quote) and `dax-faq-microsecond-cache-10x` (its first sentence, "DAX is a fully managed, highly available caching service built for DynamoDB.", is not in its only quote). Both are true per the adjacent sentences.

## 6. Verdict and recommendation

The Sonnet entail voters on chapters 27 and 28 are reliable at the level that matters most. I found no wrong value, unit, per-what, default-versus-maximum or "up to"-versus-"exactly" error in 60 sampled facts, and the seeded audit matched 20 of 20. They are clearly more lenient than the Opus voters on evidence coverage:
- they accept claim clauses and conditions that come from the packet context instead of the quote;
- they accept per-what scopes no quote states;
- they accept universal claims whose exceptions follow in the next sentence.

I would mark 4 of 60 facts (6.7 percent) `partial`. That puts the combined rate near the Opus 8 to 9 percent, so the low 2.7 percent comes from voter leniency, not from cleaner mining. The decision rule says that with 3 or 4 non-positive verdicts, recommend (b) only if one is a materially wrong claim. None is: each of the 4 is true per the same page or a sibling fact, and each needs only a quote added or a clause trimmed. **Recommendation: (a) keep Sonnet for entail votes.**

This is close to the threshold: one more defensible partial would make it (b). The misses also touch the light-process rule that every claim must carry a verbatim quote. So pair (a) with two cheap measures:

1. Make the `entail` packet instruction explicit. Context may resolve "it" or "these" and may support a qualifier, but any clause of the claim, per-what scope or condition not in a quote is `partial`; so is an "each/all/always" claim whose exception appears in the context. Also ask for a per-fact reason, since chapter 27 reasons are 96 percent boilerplate.
2. Keep a per-chapter Opus spot check of about 30 entail verdicts, and move to (b) if it finds 3 or more.

The 4 facts above can go to the registrar for a one-step amend; I changed no fact and cast no vote.

## Files

- `aws-saa-book/_build/reports/audit/sonnet-entail-20261013.sample.json`: the 60-fact sample and how it was drawn
- `aws-saa-book/_build/reports/audit/sonnet-entail-20261013/<id>.json`: `facts show` output for each sampled fact
- `aws-saa-book/_build/reports/audit/s20261013-n10-ch27.json`, `…-ch28.json`, `…-ch27.packet.json`, `…-ch28.packet.json`, `s20261013-n10.json`: the tool's seeded audit samples and packets
- `aws-saa-book/_build/reports/audit/sonnet-entail-20261013.rederive.json`: single-agent re-derivations with cross-checks (not votes)
