# spot-29: Opus spot check of chapter 29 (Amazon ElastiCache) entail votes

Date: 2026-10-14. Checker: spot-29 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round, before adjudication.

## Sample

Pool: 459 facts with home_chapter 29 and status mech-pass in `data/facts/elasticache.jsonl`. Ids sorted, `random.Random(20261013 + 29).sample(pool, 30)`. Ids in `spot-29.sample.json`.

Each fact was judged from its claim, values, qualifiers, quotes, packet context and headings (`facts show`, the `29-entail-*` packets) and, where the context mattered, `show <source>`, under the strict rule of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1. Unsupported qualifiers (scope, condition) count as partial, as in spot-12 and spot-23.

## Result

- Checked: 30. Positive (support): 26. Not positive (partial): 4.
- The first-round voter had already marked 1 of the 4 partial.
- Voter misses (voter support, spot-29 partial): 3 of 30: `elasticache-without-multi-az-new-primary-provisioned-longer-interruption`, `elasticache-reserved-nodes-partial-upfront-discount-52`, `elasticache-sizing-scale-when-traffic-minimum-test-first`. Three or more: **flag logged for chapter 29** under RULINGS 2026-10-13 safeguard 2. Only one is substantive (a nearby exception); the other two are unsupported qualifiers, with claims and quotes correct.
- Every sampled fact had a first-round entail vote.

## Non-positive verdicts

| Fact | First-round vote | spot-29 | Reason |
|---|---|---|---|
| elasticache-without-multi-az-new-primary-provisioned-longer-interruption | support | partial | Universal claim with a nearby exception: the Note right below says automatic failover can be enabled without Multi-AZ and then still promotes a replica to primary. |
| elasticache-reserved-nodes-partial-upfront-discount-52 | support | partial | Condition qualifier "depends on node type, Region and term" is in no quote and not in the quoted passage. |
| elasticache-sizing-scale-when-traffic-minimum-test-first | support | partial | Scope "node-based Valkey and Redis OSS clusters" not carried: the source is an ElastiCache (Redis OSS) whitepaper marked "for historical reference only" that never names Valkey. |
| elasticache-wa-caching-client-side-duplicates-and-inconsistency | partial | partial | The quote says "this approach"; that it is client-side caching stands only in the preceding paragraph (and a bold label, not a heading). |

## Amended (each once, `--by spot-29`, all mech-pass after; no dependents)

Patch files: `_build/work/29-elasticache/spot-29/<id>.json`. Every quote is verbatim from the saved AWS page.

1. **elasticache-without-multi-az-new-primary-provisioned-longer-interruption** (now rev 3): added the verbatim Note from the same page (`AutoFailover`): "While it is possible to have automatic failover enabled without Multi-AZ, replicas are not guaranteed to be in different Availability Zones in this configuration. Failover still promotes a replica to primary if one is available, but this does not protect against AZ-level failures." The claim now states this exception; condition qualifier says so too. Values unchanged.
2. **elasticache-reserved-nodes-partial-upfront-discount-52** (now rev 2): condition qualifier cleared. Claim, values and quote unchanged.
3. **elasticache-sizing-scale-when-traffic-minimum-test-first** (now rev 3): scope changed to "Amazon ElastiCache (Redis OSS) clusters, as described in an AWS whitepaper marked for historical reference only". Claim and quote unchanged.
4. **elasticache-wa-caching-client-side-duplicates-and-inconsistency** (now rev 2): added the verbatim preceding sentence from the same paragraph, "With client-side caching, each client (an application or service that queries the backend datastore) can store the results of their unique queries locally for a specified amount of time.", as the first evidence item. Claim unchanged.

The amends void these facts' earlier currency votes (rev changed). No batch was cut and nothing was finalized. The adjudicator sends these four to a fresh independent vote. No fact judged positive was touched.

## Positive (26)

elasticache-network-node-clusters-and-vpc-endpoint-caches-in-vpc, elasticache-serverless-minimum-metered-storage, elasticache-node-based-single-az-or-multi-az, elasticache-builders-library-emit-cache-hit-rate-metrics, elasticache-faq-failover-new-node-within-six-minutes, elasticache-faq-public-endpoint-security-groups-not-apply, elasticache-faq-durability-synchronous-writes, elasticache-engine-online-resharding-cluster-mode-enabled, elasticache-faq-global-datastore-no-sla-rpo-rto, elasticache-change-serverless-public-endpoints-2026-09, elasticache-builders-library-negative-cache-error-responses, elasticache-multi-az-needs-replica-in-other-az, elasticache-change-redis-oss-7-2022-11, elasticache-engine-use-most-recent-version, elasticache-wa-caching-hit-rate-goal-80-percent, elasticache-faq-reserved-nodes-size-flexibility, elasticache-new-replica-copies-all-data-then-async, elasticache-reserved-nodes-terms-and-payment-options, elasticache-auto-discovery-memcached-only, elasticache-at-rest-only-at-creation-no-toggle, elasticache-faq-data-tiering-how-lru-to-ssd, elasticache-backup-r6gd-restore-only-to-r6gd, elasticache-ttl-combines-lazy-loading-and-write-through, elasticache-replicas-scale-read-intensive-workloads, elasticache-serverless-storage-max-hit-evicts-ttl-data-then-oom, elasticache-faq-compliance-hipaa-baa.

## Observations for the adjudicator (not entail verdicts)

- `elasticache-faq-compliance-hipaa-baa`: support (the claim only says HIPAA is among the supported programs). The next sentence of the FAQ says that processing PHI requires an executed BAA with AWS; the id suggests the BAA was meant to be in the fact. Writers must not say "ElastiCache is HIPAA eligible" without the BAA condition; a separate fact or an amend that adds the BAA sentence would cover it.
- `elasticache-at-rest-only-at-creation-no-toggle`: support. The same page says enabling at-rest encryption on an existing node-based Valkey or Redis OSS cluster means backup, restore into a new replication group and deleting the old one; and that for Valkey `AtRestEncryptionEnabled` defaults to true. Neither is an exception to the claim, but the prose should mention the backup-and-restore path.
- `elasticache-faq-failover-new-node-within-six-minutes`: support. The same FAQ answer says Global Datastore cross-Region promotion can complete in under one minute; keep the two numbers apart in prose.
- Pattern in this chapter: mining or registering left some qualifiers (scope, condition) richer than the quotes; voters judged the claim text and passed the qualifiers. Other facts with filled `condition` or extended `scope` fields deserve a glance at adjudication.
