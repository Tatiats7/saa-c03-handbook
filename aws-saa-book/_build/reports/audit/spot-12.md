# spot-12: Opus spot check of chapter 12 (Site-to-Site VPN, Direct Connect and Client VPN) entail votes

Date: 2026-10-14. Checker: spot-12 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round (`12-entail-001` to `12-entail-007`), before adjudication.

## Sample

Pool: 525 facts with home_chapter 12 and status mech-pass in `data/facts/site-to-site-vpn.jsonl`, `direct-connect.jsonl` and `client-vpn.jsonl` (90 more are superseded, 1 rejected). Ids sorted, `random.Random(20261013 + 12).sample(pool, 30)`. Ids in `spot-12.sample.json`.

Each fact was judged from its claim, values, qualifiers, quotes, packet context and headings (`facts show` and the `12-entail-*` packets), under the strict rule of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 26. Not positive (partial): 4.
- The first-round voters had already marked all 4 partial.
- Voter misses (voter support, spot-12 not positive): 0 of 30. **No flag** for chapter 12.
- Every sampled fact had a first-round entail vote.

## Non-positive verdicts

| Fact | First-round vote | spot-12 | Reason |
|---|---|---|---|
| site-to-site-vpn-change-modify-tunnel-bandwidth | partial | partial | The date May 6, 2026 stands only in the "Posted on" line, not in a quote. |
| site-to-site-vpn-faq-accelerated-same-protocols | partial | partial | The NAT-T exception ("Apart from NAT-T") stands only in the preceding FAQ sentence; the quote starts "Other that that". |
| client-vpn-internet-access-rule-0-0-0-0-and-default-route | partial | partial | Scope qualifier "with full tunnel" is in no quote and not on the page section. |
| site-to-site-vpn-psk-default-authentication | partial | partial | Condition "you can choose a certificate instead" stands only in the page's opening sentence. |

## Amended (each once, `--by spot-12`, all mech-pass after; no dependents in any of the four)

Patch files: `_build/work/12-hybrid-networking/spot-12/<id>.json`. Every quote is verbatim from a saved AWS page.

1. **site-to-site-vpn-change-modify-tunnel-bandwidth** (rev 2): added heading-scoped evidence "Posted on: May 6, 2026" under the What's New heading (R8 value line); the three existing quotes kept in order (`changed.was_evidence` 0 still points at the "Previously" quote). Claim unchanged.
2. **site-to-site-vpn-faq-accelerated-same-protocols** (rev 3): added the FAQ quote "NAT-T is required and is enabled by default for Accelerated Site-to-Site VPN connections."; claim now states that NAT-T is required and enabled by default for accelerated connections, then the sameness. `hard` set to true (M11: the claim now holds "by default").
3. **client-vpn-internet-access-rule-0-0-0-0-and-default-route** (rev 3): scope changed from "Client VPN endpoint with full tunnel" to "Client VPN endpoint; clients that cannot reach the internet (troubleshooting steps)". Claim and quotes unchanged.
4. **site-to-site-vpn-psk-default-authentication** (rev 3): added the quote "You can use pre-shared keys, or certificates to authenticate your Site-to-Site VPN tunnel endpoints." (same page, opening sentence); claim now names both options before the default.

No batch was cut and nothing was finalized. The adjudicator sends these four to a fresh independent vote. No fact judged positive was touched.

## Positive (26)

site-to-site-vpn-faq-tunnel-max-pps, direct-connect-limit-hosted-port-speeds, direct-connect-faq-resiliency-toolkit-wizard, site-to-site-vpn-limit-pps-large-tunnel, client-vpn-quota-endpoints-per-region, site-to-site-vpn-accelerated-why-consistent-experience, direct-connect-dxgw-global-resource-any-region-not-china, direct-connect-default-vifs-use-100-percent-capacity, direct-connect-vif-private-access-vpc-private-ips, site-to-site-vpn-limit-ipv6-same-as-ipv4, site-to-site-vpn-concept-customer-gateway-is-aws-resource, client-vpn-restriction-tgw-no-mixing-associations, site-to-site-vpn-accelerated-disabled-by-default, client-vpn-self-service-portal-download-client-and-config, site-to-site-vpn-restriction-concentrator-transit-gateway-only, client-vpn-faq-server-certificate-in-acm, client-vpn-no-traffic-initiated-toward-client-device, direct-connect-backup-lower-cost-vpn-primary-dx-with-vpn-backup, client-vpn-faq-authorization-rules-by-group, direct-connect-metric-connection-bps-ingress, site-to-site-vpn-faq-private-ip-mtu, direct-connect-lag-no-multi-chassis, site-to-site-vpn-sec09-use-ipsec-vpn-for-network-to-network, client-vpn-faq-openvpn-protocol, client-vpn-client-cidr-between-slash-22-and-slash-12, direct-connect-sitelink-separate-pricing-fee-off-by-default.

## Observations for the adjudicator (not entail verdicts)

- `site-to-site-vpn-faq-tunnel-max-pps`: entail support (the FAQ quote carries it), but the claim is unscoped: the quotas page gives up to 140,000 PPS per standard tunnel and up to 400,000 per large bandwidth tunnel. The first-round currency vote is `unsure` for this reason. Repair by scoping to standard tunnels.
- `direct-connect-backup-lower-cost-vpn-primary-dx-with-vpn-backup`: support as a "can" statement. The next paragraph says AWS does not recommend a VPN backup for Direct Connect connections faster than 1 Gbps (VPN on a virtual private gateway); that caveat is its own fact (`direct-connect-backup-vpn-bandwidth-limit-not-above-1-gbps`). Writers should cite both together.
- `direct-connect-limit-hosted-port-speeds`: support. The same paragraph says only qualifying partners may create hosted connections of 1 Gbps and above, and 25 Gbps only where 100 Gbps ports exist; the condition qualifier is empty, so writers should not imply every speed is available everywhere.
