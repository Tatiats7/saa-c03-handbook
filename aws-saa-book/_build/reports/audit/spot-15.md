# Spot check spot-15: chapter 15 (CloudFront and Global Accelerator)

Date: 2026-10-13. Checker: Opus spot check (RULINGS 2026-10-13, safeguard 2). Lens: ENTAIL, strict (TOOLS.md 5.4 plus the packet rule: a clause, scope, condition or exception that stands only in the surrounding text, or a universal claim with a nearby exception, is `partial`).

## Sample

- Population: 76 facts with `home_chapter` 15 and status `mech-pass` in `data/facts/cloudfront.jsonl` and `data/facts/global-accelerator.jsonl` (ids sorted).
- Seed 20261028 (20261013 + 15), `random.Random(seed).sample(ids, 30)`. Ids: `spot-15.sample.json`.
- Note: almost every fact in the sample is a fact the adjudicator already repaired after round 1 (repairs 1). Each one already had a round-2 Sonnet `entail` vote of `support` (batch 15-entail-012) when it was checked, and the votes were not yet finalized. So this spot check measures the round-2 votes.

## Result

30 checked, 27 positive, 3 partial (10%). This is at the flag threshold of 3 misses, so the chapter is logged as **flagged** (RULINGS: two flagged chapters in a row move entail votes back to Opus). All three misses are of the same kind: a nearby exception or scope limit that the claim leaves out. None of the three is wrong on its main value.

| Fact | Verdict | Reason |
| --- | --- | --- |
| global-accelerator-recovery-routing-about-30-seconds | partial | The next sentences say that established active connections are not moved and keep routing to the zero-weight Region; without that exception the claim reads as if all traffic returns in about 30 seconds. |
| global-accelerator-client-affinity-source-ip-uses-2-tuple | partial | Universal "same endpoint each time" claim; the paragraph that follows says client affinity is not guaranteed when traffic shifts to an edge location that prefers a different Region. |
| cloudfront-change-waf-blocked-requests-free-2024-10 | partial | "Never incur request fees or data transfer charges" reads as "blocked requests cost nothing", but the next sentence of the post says AWS WAF continues billing for evaluating and blocking these requests. The scope "pay-as-you-go" was not in the source either (the post says it applies to all CloudFront distributions using AWS WAF). |

The other 27 were judged `support`. Facts checked in context with `saa.py show`: global-accelerator-faq-no-dns-cache-dependency-seconds, global-accelerator-faq-custom-routing-deterministic-ec2-destination, cloudfront-quota-distributions-per-cache-policy (the row has no "Request a higher quota" link, unlike its neighbors, and the claim says "by default"), cloudfront-failover-lambda-edge-triggered-twice.

## Amended (each once, `--by spot-15`; the adjudicator sends them to a fresh vote)

1. **global-accelerator-recovery-routing-about-30-seconds** (rev 3 to 4): the claim now adds that established active connections are not moved and keep routing to the zero-weight Region until the connection is reset or the client makes a new connection. Two quotes from the same page were added ("However, note that established active connections are not moved." and "They continue to route to the zero weight Region until ...").
2. **global-accelerator-client-affinity-source-ip-uses-2-tuple** (rev 2 to 3): the claim now adds the exception: client affinity is not guaranteed when network maintenance or disruptions shift traffic to an edge location that prefers a different AWS Region. Two quotes from the same page were added.
3. **cloudfront-change-waf-blocked-requests-free-2024-10** (rev 2 to 3): the claim is narrowed to CloudFront request fees and data transfer charges, and it says that AWS WAF's own charges are out of scope. The scope qualifier was corrected (no "pay-as-you-go"). The AWS WAF billing sentence could not be attached. In the saved What's New JSON snapshot it does not sit on a sentence boundary (M4 refused it), and robots.txt disallows fetching the post page. The note records the sentence so that writers never say that blocked requests cost nothing at all.

Patches: `_build/work/15-cloudfront/spot/`.

## Pattern for the adjudicator and the next chapters

The round-2 voter returned the same generic reason ("The quotes under their headings state every part of the claim ...") for every fact in batch 15-entail-012. It checked whether the claim's clauses were covered, but it did not check for exceptions that stand after the quote. The safeguard-1 rule (a universal claim with a nearby exception is partial) was not applied in that batch.
