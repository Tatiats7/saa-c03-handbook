# spot-33: Opus spot check of chapter 33 (Amazon API Gateway) entail votes

Date: 2026-10-14. Checker: spot-33 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round, before adjudication.

## Sample

Pool: 463 facts with home_chapter 33 and status mech-pass in `data/facts/api-gateway.jsonl`. Ids sorted, `random.Random(20261013 + 33).sample(pool, 30)`. Ids in `spot-33.sample.json`.

Each fact was judged from its claim, values, qualifiers, quotes, packet context and headings (`facts show`, the `33-entail-*` packets) and, where the context mattered, `show <source> --around`, under the strict rule of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 25. Not positive (partial): 5.
- The first-round voters had already marked 4 of the 5 partial.
- Voter misses (voter support, spot-33 partial): 1 of 30 (`api-gateway-change-response-streaming-2025`). Under three: **no flag** for chapter 33.
- Every sampled fact had a first-round entail vote.

## Non-positive verdicts

| Fact | First-round vote | spot-33 | Reason |
|---|---|---|---|
| api-gateway-change-response-streaming-2025 | support | partial | Quote 2 is a bare bullet ("Exceed API Gateway's 10 MB response payload limit."); the lead-in that makes it a statement about response streaming ("Use response streaming for the following use cases:") stands only in the preceding line. |
| api-gateway-rest-api-definition | partial | partial | The concept-page quote never names its subject; "API Gateway REST API" stands only in the bold term label above it (the HTTP API entry below has a near-identical body). |
| api-gateway-endpoint-header-names-edge-capitalized | partial | partial | Claim says private endpoints pass header names as-is; no quote carried the private-endpoint clause. |
| api-gateway-access-control-waf-not-authentication | partial | partial | The "not authentication" contrast depends on the authentication-and-authorization list, which stands only in the surrounding text. |
| api-gateway-mapping-template-vtl | partial | partial | The subject "Mapping template" stands only in the bold term label above the VTL definition. |

## Amended (each once, `--by spot-33`, all mech-pass after; no dependents; 0 open conflicts after)

Patch files: `_build/work/33-api-gateway/spot-33/<id>.json`. Every quote is verbatim from a saved AWS page.

1. **api-gateway-change-response-streaming-2025** (now rev 2): added the verbatim lead-in "Use response streaming for the following use cases:" from the same page (`response-transfer-mode`) as a third evidence item; claim unchanged. Its rev 1 currency vote is void at rev 2.
2. **api-gateway-rest-api-definition** (now rev 3): evidence replaced by "A REST API in API Gateway is a collection of resources and methods that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services." from `docs/apigateway/latest/developerguide/apigateway-rest-api` (fetched by spot-33 on 2026-10-14). Claim narrowed to that sentence (the "deploy in one or more stages" clause dropped); display v2 now "collection of resources and methods".
3. **api-gateway-endpoint-header-names-edge-capitalized** (now rev 2): added the verbatim "Private API endpoints pass all header names through as-is." from the same page (under "Private API endpoints"); claim unchanged.
4. **api-gateway-access-control-waf-not-authentication** (now rev 3): claim narrowed to "AWS lists AWS WAF among the mechanisms for performing other tasks related to access control of a REST API: AWS WAF can be used to protect your API Gateway API from common web exploits." Evidence unchanged (lead-in plus WAF bullet). The fact id still says "not-authentication"; ids are never reused, so the adjudicator may leave it.
5. **api-gateway-mapping-template-vtl** (now rev 3): evidence replaced by the two opening sentences of `docs/apigateway/latest/developerguide/models-mappings` (fetched by spot-33 on 2026-10-14), which name the subject; claim follows them (VTL script applied to a payload using JSONPath based on the Content-type header; a mapping template transformation uses it to modify the integration request or integration response); scope now "REST API integrations"; display v2 now "modify your integration request or integration response".

No batch was cut and nothing was finalized. The adjudicator sends these five to a fresh independent vote. No fact judged positive was touched.

## Positive (25)

api-gateway-private-api-direct-connect-no-internet, api-gateway-websocket-stateful-frontend-for-backends, api-gateway-table-resource-policies-rest-yes-http-no, api-gateway-custom-domain-wildcard-acm-validated, api-gateway-resource-policy-definition-and-principals, api-gateway-private-domain-provision-15-min, api-gateway-throttling-account-limit-increase-on-request, api-gateway-table-developer-portal-rest-yes-http-no, api-gateway-http-api-lower-latency-lower-cost, api-gateway-canary-promote-to-production, api-gateway-api-key-request-must-contain-key-else-403, api-gateway-table-xray-tracing-rest-yes-http-no, api-gateway-faq-lambda-authorizer-returns-iam-policy, api-gateway-ws-authorizer-result-size, api-gateway-faq-websocket-max-message-size-128kb, api-gateway-faq-backends-and-mock-static-content, api-gateway-choose-rest-or-http-guidance, api-gateway-change-private-custom-domains-2024, api-gateway-private-endpoint-vpc-only-interface-endpoint, api-gateway-faq-throttle-per-method-or-route, api-gateway-table-per-client-usage-throttling-rest-yes-http-no, api-gateway-usage-plan-limits-aggregate-across-stages, api-gateway-http-api-first-class-integration-needs-iam-role, api-gateway-usage-plans-per-api-key, api-gateway-ws-idle-timeout.

## Observations for the adjudicator (not entail verdicts)

- `api-gateway-faq-websocket-max-message-size-128kb`: support. The quota row's `**` footnote says a message larger than 32 KB must be split into frames of 32 KB or smaller; it does not change the 128 KB maximum, but writers should not state 128 KB without the frame rule nearby.
- `api-gateway-usage-plan-limits-aggregate-across-stages`: support. The next note on the page says usage plan throttling and quotas are not hard limits and are applied on a best-effort basis; that belongs in a separate fact, not in this one.
- Pattern in this chapter: definitions from the "Amazon API Gateway concepts" page (bold term label, then a body that never names the term) fail entailment. Other facts quoting that page the same way are likely to be voted partial too.
