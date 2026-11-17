# Corpus harvest: shared evidence pages (2026-10-11)

Scope: every FAQ page in the registry, the exam guide and certification policy pages (SOURCES.md Part 1), the grounding documents, decision guides and Well-Architected pages (registry and SOURCES.md Part 3), global infrastructure and shared responsibility, the service lifecycle lists named in FRESHNESS.md, plus every other `pages`, `history`, `quotas` and `pricing` URL in the registry.

All network access went through `saa.py fetch` / `saa.py faq`. Requests today after this run: 485 of the 6,000 cap (this harvest made 9 requests; everything else was already cached by earlier agents).

## Counts

| Group | URLs | Cached before | Fetched now | Empty text | Redirected |
|---|---|---|---|---|---|
| A. Exam, policy, global infrastructure, shared responsibility, lifecycle | 17 | 14 | 3 | 0 | 0 |
| B. Grounding docs, Well-Architected, whitepapers, decision guides (SOURCES.md Part 3 + FRESHNESS lifecycle) | 41 | 32 | 6 | 3 (see failures) | 4 |
| C. Registry pages on shared hosts (certification, whitepapers, wellarchitected, decision-guides, prescriptive-guidance) | 176 | 176 | 0 | 1 (see failures) | 3 |
| D. Remaining registry pages/history/quotas/pricing | 457 | 457 | 0 | 0 | 2 |
| F. Registry FAQ pages | 128 | 128 | 0 | 0 | 0 (9 Aurora docs FAQ pages record their `.md` twin as final_url, which is normal) |

Guide indexes present: 180 (including the exam guide `aws-certification-solutions-architect-associate-03`).

## FAQ parse (128 pages, 8,206 questions in total, every page parsed with at least 1 question)

Per-page counts are in `_build/corpus/faq/<name>.meta.json`; the index files `faq/<name>.jsonl` were rewritten from cache. The Aurora FAQ was parsed with `--follow` (landing page plus 9 sub-pages).

## Failures and things later agents should know

1. **`https://docs.aws.amazon.com/whitepapers/latest/guidelines-for-implementing-aws-waf/guidelines-for-implementing-aws-waf.html`** (registry chapter 08 `edge-protection`, `pages`): the whitepaper is gone. It redirects to `https://docs.aws.amazon.com/waf/latest/developerguide/` and the snapshot text is empty (0 characters, HTML fallback). Chapter 08 should cite the WAF Developer Guide pages instead; the registry entry is left for the chapter planner to replace with `registry set 08 --replace sources.pages`.
2. **Secure Content Delivery with CloudFront whitepaper** (chapter 15, two URLs: `.../secure-content-delivery-amazon-cloudfront.html` and `.../using-https.html`): both redirect to `https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecurityAndPrivateContent.html`. Text is present (it is the developer-guide page), but quotes must cite the CloudFront Developer Guide page, not the whitepaper URL.
3. **SOURCES.md Part 3 decision-guide shorthand** `analytics`, `cost-management`, `monitoring` are not real page names: `https://docs.aws.amazon.com/decision-guides/latest/decision-guides/{analytics,cost-management,monitoring}.html` redirect to the decision-guides index and give empty text. The real pages are `analytics-on-aws-how-to-choose`, `monitoring-on-aws-how-to-choose`, `cost-management-on-aws-how-to-choose` and `cloudtrail-or-cloudwatch`; the registry already uses those names and all four are cached with full text (53 KB, 39 KB, 29 KB, 21 KB). Do not cite the three empty snapshots.
4. **Redirects that are fine but change the citation URL:** `https://aws.amazon.com/getting-started/decision-guides/` -> `https://docs.aws.amazon.com/decision-guides/`; `https://aws.amazon.com/products/lifecycle/` (chapter 48) -> `https://docs.aws.amazon.com/general/latest/gr/service-lifecycle.html` (now cached directly too); `https://aws.amazon.com/dms/schema-conversion-tool/` (chapter 39) -> `https://aws.amazon.com/dms/features/`.
5. **Lifecycle lists** are cached as Markdown: `docs/general/latest/gr/service-lifecycle` (1.6 KB), `sunset_services` (5.3 KB), `full_shutdown_services` (3.3 KB), `maintenance_services` (already cached).
6. **Short but valid pages** (under 1,500 characters, usually an abstract or a quota stub): `saa-service-mentions` (1.1 KB), `saa-technologies-concepts` (0.6 KB), DR whitepaper landing page (1.0 KB, abstract only; the content is in `disaster-recovery-options-in-the-cloud`), `the-pillars-of-the-framework` (1.0 KB), and about 40 quota and pricing pages. Pricing pages on aws.amazon.com (CloudHSM, Batch, Auto Scaling, License Manager, Well-Architected Tool, Application Migration Service) hold only visible text; price tables are loaded by JavaScript and are not in the snapshot.
7. Not fetched on purpose: non-AWS hosts (pearsonvue, linkedin, skillbuilder, builder.aws.com, startups.aws.com, wellarchitectedlabs), PDFs and `llms.txt` / `full.md` files (those belong to `saa.py guide`).

Batch files used: `_build/tmp/harvest/missing-01.txt`; raw fetch output: `_build/reports/harvest-fetch-missing.txt`.
