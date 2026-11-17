# spot-19: Opus spot check of chapter 19 (ECS, EKS, Fargate and ECR) entail votes

Date: 2026-10-13. Checker: spot-19 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round, before adjudication.

## Sample

Pool: 697 facts with home_chapter 19 and status mech-pass in `data/facts/{ecs,eks,fargate,ecr,ecs-anywhere,eks-anywhere,eks-distro}.jsonl`. Ids sorted, `random.Random(20261013 + 19).sample(pool, 30)`. Ids in `spot-19.sample.json`.

I judged each fact from its claim, values, qualifiers, quotes, packet context and headings (`facts show` and the `19-entail-*` packets). Where the context mattered, I also read the page with `show <source>`. The rule is the strict one of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 24. Not positive: 6 (5 partial, 1 partial with a self-contradicting page).
- The first-round voters had already marked 5 of the 6 as not positive (4 partial, 1 unsure).
- Voter misses (voter support, spot-19 partial): 1 of 30 (`eks-anywhere-software-open-source`, a wrong scope qualifier only). This is under three, so chapter 19 gets **no flag** under RULINGS 2026-10-13 safeguard 2.

## Non-positive verdicts

| Fact | First-round vote | spot-19 | Reason |
|---|---|---|---|
| eks-access-entries-recommended-over-aws-auth | partial | partial | The claim's "instead of the legacy aws-auth ConfigMap" stands only in the next bullet; the page does not use the word "legacy". |
| ecs-interface-endpoints-incomplete-traffic-uses-public-endpoint | partial | partial | "Required Region-specific" endpoints stand only in the preceding list line, not in the quote. |
| ecs-predictive-scaling-historical-patterns | partial | partial | "Most useful", cyclical traffic and recurring on-and-off workloads stand only in the surrounding list. |
| ecs-pricing-no-charge-for-orchestration | partial | partial | A universal "pay only" claim, while the next section states a per-instance management fee for ECS Managed Instances. The scope qualifier "per account" was also wrong. |
| ecr-tag-immutability-prevent-overwrite | unsure | partial | The page sentence right after quote 1 says "Tag immutability affects all tags. You cannot make some tags immutable while others aren't." This contradicts the exclusion clause. The exclusion holds only in the console (and CLI) steps. |
| eks-anywhere-software-open-source | support | partial | Wrong scope qualifier: "per cluster" for a claim about the software license. Claim and quote are otherwise identical. |

## Amended (each once, `--by spot-19`; all mech-pass after the amend; no dependents; 0 open conflicts after)

Patch files: `_build/work/19-containers/spot-19/<id>.json`. Every added quote is verbatim from the same saved page.

1. **eks-access-entries-recommended-over-aws-auth** (now rev 2):
   - Added two verbatim sentences: the migrate recommendation ("... then we recommend that you migrate those entries to access entries.") and the "Adding entries to the `aws-auth` `ConfigMap` ** – ... then you must use this option." line.
   - The claim now names both cases and drops "legacy".
   - Added the display "migrate those entries to access entries" and updated the condition.
   - Set `hard` to true, because M11 requires it for "must".
2. **ecs-interface-endpoints-incomplete-traffic-uses-public-endpoint** (now rev 3):
   - Added the verbatim line "You must have the following Region-specific VPC endpoints:".
   - The claim now refers to the Regions in the condition ("Regions introduced starting on December 23, 2023"). M5 refuses a date in the claim that no quote holds; the date stands only in the section heading.
3. **ecs-predictive-scaling-historical-patterns** (now rev 2):
   - Added three verbatim quotes: "Predictive auto scaling is most useful in the following situations." and the "Cyclical traffic ‐ ..." and "Recurring on-and-off workload patterns ‐ ..." list items.
   - The claim is unchanged.
4. **ecs-pricing-no-charge-for-orchestration** (now rev 2):
   - Added the verbatim sentence "For ECS Managed Instances, there is an additional management fee per instance for the operational management provided by AWS."
   - The claim now carries this exception.
   - Added the display "additional management fee per instance". Scope set to "Amazon ECS pricing", with a condition.
5. **ecr-tag-immutability-prevent-overwrite** (now rev 3):
   - The exclusion clause is now scoped to the console Immutable setting that the quote describes.
   - The condition and note record the page's self-contradiction.
   - `adjustable` set to false (this is not a quota).
   - Observation for the adjudicator: the CLI section of the same page shows `IMMUTABLE_WITH_EXCLUSION` and `--image-tag-mutability-exclusion-filters`, so the overview sentence looks out of date. A currency vote may be worth asking for.
6. **eks-anywhere-software-open-source** (now rev 2): only the scope qualifier changed, to "Amazon EKS Anywhere software".

I cut no batch and finalized nothing. The adjudicator sends these six facts to a fresh independent vote. I did not touch any fact I judged positive.

## Positive (24)

ecs-faq-compute-autoscaling-fargate-and-ec2, ecs-app2container-modernizes-java-dotnet-into-containers, eks-zonal-shift-temporary-move-traffic-from-impaired-az, ecs-change-express-mode-launch-2025-11, eks-faq-hybrid-nodes-gateway-automates-pod-networking, fargate-retirement-service-tasks-replaced-automatically, ecr-images-per-repository-quota, fargate-no-placement-strategies-best-effort-az-spread, eks-change-extended-support-preview-2023-10, ecr-authorization-token-valid-12-hours, ecs-faq-mi-network-modes, fargate-whitepaper-own-kernel-for-ecs-and-eks, fargate-faq-arm-on-eks-not-supported, fargate-faq-multi-account-for-tens-of-thousands-of-cores, fargate-ondemand-vcpu-quota-eks-page, eks-faq-hybrid-three-options, eks-faq-extended-support-gets-security-patches, fargate-ephemeral-storage-max-200-gib, eks-fargate-not-on-outposts-wavelength-local-zones, eks-managed-node-group-no-extra-charge, eks-anywhere-subscription-flat-per-cluster, eks-cluster-autoscaler-uses-auto-scaling-groups, eks-faq-hybrid-nodes-vs-anywhere-connected-vs-air-gapped, ecs-case-study-smartsheet-fargate-independent-deployments.

## Observations for the adjudicator (not entail verdicts)

- `fargate-faq-arm-on-eks-not-supported`: entail is support, but the FAQ says "today". The fact is a candidate for a currency check against What's New.
- `eks-zonal-shift-temporary-move-traffic-from-impaired-az`: support. The page adds that "You can extend the zonal shift, if necessary". This is not an exception to the claim, but writers should not imply a fixed end.
