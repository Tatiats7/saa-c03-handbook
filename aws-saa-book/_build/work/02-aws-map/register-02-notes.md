# Registrar notes, chapter 02 (register-02, 2026-10-11)

Input: 325 mech-pass facts from three miners (behavior+decisions 139, numbers+changes 89, faq 63, plus 40 saved on 2026-10-09). Output: 305 live facts (146 hard), 20 superseded, 1 rejected, 0 open conflicts for this chapter.

## Duplicates merged (old -> kept)

- well-architected-six-pillars-named -> well-architected-six-pillars
- global-infrastructure-edge-locations-linked-to-regions-by-backbone -> global-infrastructure-edge-locations-connected-to-regions-by-backbone
- global-infrastructure-az-interconnect-low-latency-metro-fiber -> global-infrastructure-az-interconnect-metro-fiber
- global-infrastructure-az-sync-replication-single-digit-ms -> global-infrastructure-az-latency-single-digit-ms
- management-console-resources-shown-per-region -> management-console-missing-resources-check-region
- global-infrastructure-pop-isolated-from-each-other -> global-infrastructure-each-pop-isolated
- global-infrastructure-global-services-may-store-data-globally -> global-infrastructure-customer-content-stays-in-chosen-region
- well-architected-framework-provides-questions-to-evaluate-architecture -> well-architected-framework-definition-best-practices-and-questions
- management-console-cloudshell-storage-not-synced-across-regions -> management-console-cloudshell-faq-home-directory-persists-1-gb-per-region
- management-console-cloudshell-no-additional-cost -> management-console-cloudshell-faq-no-additional-charge
- global-infrastructure-opt-in-regions-after-2019-03-20 -> global-infrastructure-opt-in-regions-after-march-2019
- global-infrastructure-service-quotas-per-region-not-all-adjustable -> global-infrastructure-service-quota-default-per-region (the second half is global-infrastructure-service-quota-not-all-increasable)
- global-infrastructure-pop-network-hosts-cloudfront-route53-global-accelerator -> global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator
- management-console-console-private-access-limits-accounts-from-your-network -> management-console-private-access-limits-console-to-known-accounts-from-vpc
- global-infrastructure-quota-increase-not-immediate -> global-infrastructure-service-quota-increase-takes-days
- global-infrastructure-regions-not-shared-across-account-types -> global-infrastructure-account-type-cannot-reach-other-partition-regions
- well-architected-availability-definition-percentage-of-time -> well-architected-availability-definition
- global-infrastructure-az-id-same-in-every-account -> global-infrastructure-az-id-same-physical-location-every-account (the November 2025 mapping change stays in global-infrastructure-az-name-mapping-independent-per-account)
- global-infrastructure-az-is-one-or-more-data-centers -> global-infrastructure-az-definition-discrete-data-centers
- management-console-cloudshell-preauthenticated-with-console-credentials -> management-console-cloudshell-faq-browser-shell-pre-authenticated

Rejected: global-infrastructure-higher-cost-region-only-for-requirements (the COST07-BP02 best practice lives in well-architected-region-pricing-differs-choose-by-cost; the Region price fact is global-infrastructure-region-pricing-differs-local-market).

Kept on purpose, both sides, with distinct scope: the FAQ and user-guide pairs for CloudShell (1 GB, 120 days, 10 shells per user vs per account, inactivity timeout), the FAQ and framework pairs for the review timing and the workload definition, and the What's New change facts next to their docs facts (multi-session, Private Access).

## Qualifiers and questions

Scope added to 10 restriction facts without one (partitions, synchronous replication, Local Zone VPC features, Wavelength carrier gateway, CloudShell VPC environments, three "currently" FAQ restrictions, two Console Mobile App restrictions). Question of management-console-multi-session-announced rewritten: the claim states the session count, not the date.

## Conflicts

cf-0018 to cf-0033 closed with --both: all M12 false positives (availability table tiers, Region launch rows, and one superseded duplicate). The 15 conflicts still open belong to other chapters (Lambda, S3, EC2, Auto Scaling).

## Demand

124 items: 110 found, 11 partial, 3 not found. Added for d071: well-architected-review-risks-hri-and-mri-definitions (page fetched 2026-10-11). Not found and why: d095 (exam namespace, chapter 01), d107 (Nuix page gone; Vanguard and Burns & McDonnell stand in), d115 (Local Zones SLA FAQ answer holds only links). Partial items carry the miners' notes; the headline infrastructure counts (d002, d033) are not quotable as whole sentences on the saved pages, so writers must word them without numbers or request a fact.

## Namespaces

CloudShell facts stay under management-console (no cloudshell key). Six budgets facts mined by the numbers miner have home chapter 41 and are not part of this chapter.
