# spot-11: Opus spot check of chapter 11 (Connecting VPCs) entail votes

Date: 2026-10-14. Checker: spot-11 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round (`11-entail-001` to `11-entail-007`), before adjudication.

## Sample

Pool: 509 facts with home_chapter 11 and status mech-pass in `data/facts/vpc-peering.jsonl`, `transit-gateway.jsonl`, `vpc-endpoints.jsonl` and `privatelink.jsonl` (32 more are superseded). Ids sorted, `random.Random(20261013 + 11).sample(pool, 30)`. Ids in `spot-11.sample.json`.

Each fact was judged from its claim, values, qualifiers, quotes, packet context and headings (`facts show` and the `11-entail-*` packets), and where needed with `search` and `show` on the saved pages, under the strict rule of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 26. Not positive (partial): 4.
- The first-round voters had already marked 3 of the 4 partial.
- Voter misses (voter support, spot-11 partial): 1 of 30 (`transit-gateway-wp-traffic-stays-on-backbone`). Under three: **no flag** for chapter 11.
- Every sampled fact had a first-round entail vote.

## Non-positive verdicts

| Fact | First-round vote | spot-11 | Reason |
|---|---|---|---|
| transit-gateway-wp-cloud-wan-replaces-tgw-peering-vpn | partial | partial | "Centralizes network and security posture constructs in a single place" stands only in later sentences of the paragraph. |
| privatelink-consumer-endpoint-only-in-service-azs | partial | partial | The quote says the consumer "can create" endpoints in the service's AZs; the "only" of the claim is not in it. |
| privatelink-vs-lattice-wp-application-networking | partial | partial | Service network and auth policies stand only in the component list below the quote. |
| transit-gateway-wp-traffic-stays-on-backbone | support | partial | Wrong scope: the whitepaper sentence directly follows "Transit Gateways can be peered ... between different AWS Regions", and the What's New item states the same sentence for "Transit Gateway Inter-region Peering". The claim applied it to all transit gateway traffic. |

## Amended (each once, `--by spot-11`, all mech-pass after; no dependents in any of the four)

Patch files: `_build/work/11-vpc-connectivity/spot-11/<id>.json`. Every quote is verbatim from a saved AWS page.

1. **transit-gateway-wp-traffic-stays-on-backbone** (rev 2): claim scoped to inter-Region peering; whitepaper quote extended to start at the peering sentence (same line); added the verbatim What's New quote "Traffic using AWS Transit Gateway Inter-region Peering always stays on the AWS global network and never traverses the public internet, ..." (`api/whats-new-v2-aws-transit-gateway-s1000-p0`); question and qualifiers (scope, condition) updated.
2. **transit-gateway-wp-cloud-wan-replaces-tgw-peering-vpn** (rev 3): added a second quote from the same page, "You would have your network and security posture constructs defined in one place, and your networks in another. Cloud WAN allows you to centralize all of these constructs in a single place."; claim follows both quotes. (One 88-word single quote was refused by M4; two quotes were used instead.)
3. **privatelink-consumer-endpoint-only-in-service-azs** (rev 3): "only" removed from the claim; kind changed from restriction to behavior. No saved page has a quote that states the restriction outright (searched the PrivateLink guide and whitepapers).
4. **privatelink-vs-lattice-wp-application-networking** (rev 2): claim trimmed to what the quote carries (fully managed application networking service; connect, monitor and secure services across accounts and VPCs).

No batch was cut and nothing was finalized. The adjudicator sends these four to a fresh independent vote. No fact judged positive was touched.

## Positive (26)

privatelink-wp-unidirectional-overlapping-ips, vpc-endpoints-policy-does-not-override-identity-or-resource-policies, privatelink-faq-path-stays-within-aws, transit-gateway-encryption-support-enforces-in-transit, vpc-endpoints-faq-horizontally-scalable-highly-available, transit-gateway-appliance-mode-same-az-for-flow, transit-gateway-quota-vpc-attachment-bandwidth, vpc-peering-faq-inter-region-encrypted, vpc-endpoints-resource-endpoint-private-access, privatelink-faq-endpoint-bandwidth-default-10-gbps-per-az, vpc-endpoints-pricing-hourly-per-az-while-provisioned, vpc-endpoints-faq-resource-endpoint, transit-gateway-unique-asn-per-gateway, privatelink-guide-private-connect-no-igw-nat, transit-gateway-faq-multicast-attachment-types, vpc-peering-faq-no-single-point-of-failure, transit-gateway-quota-gateways-per-vpc, vpc-peering-faq-bandwidth-same-as-vpc, vpc-peering-scenario-active-directory-central-vpc, vpc-endpoints-faq-interface-endpoint-privatelink-services, transit-gateway-quota-dx-gateways-per-gateway, vpc-peering-one-to-one-relationship, transit-gateway-faq-onprem-routes-bgp, transit-gateway-metric-bytesin-sum, vpc-endpoints-quota-interface-gwlb-per-vpc, privatelink-wp-security-groups-manage-endpoint-access.

## Observations for the adjudicator (not entail verdicts)

- `transit-gateway-quota-vpc-attachment-bandwidth`: claim is supported. The qualifiers say `adjustable: false` and `default_or_max: max`, while the row sits under the "Default" column and its Adjustable cell says "Contact your Solutions Architect (SA) or Technical Account Manager (TAM)", not "No". The condition carries this; writers should not call it "not adjustable".
- `privatelink-faq-endpoint-bandwidth-default-10-gbps-per-az`: supported, but the claim and condition omit the quote's ceiling ("added automatically up to 100 Gbps"). Consider adding a display for the 100 Gbps ceiling so writers do not imply unlimited scaling.
