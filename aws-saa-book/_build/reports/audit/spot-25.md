# spot-25: Opus spot check of chapter 25 (Storage Gateway, DataSync, Snow Family, Transfer Family) entail votes

Date: 2026-10-14. Checker: spot-25 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round, before adjudication.

## Sample

Pool: 731 facts with home_chapter 25 and status mech-pass in `data/facts/{storage-gateway,datasync,snow-family,transfer-family}.jsonl` (275 + 224 + 82 + 150). Ids pooled and sorted, `random.Random(20261013 + 25).sample(pool, 30)`. Ids in `spot-25.sample.json`.

I judged each fact from its claim, values, qualifiers, quotes, packet context and headings (the `25-entail-*` packets and `facts show`). Where the context mattered I also read the page with `show <source>`. The rule was the strict one of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1: the quote must carry every clause, scope, condition and qualifier on its own.

## Result

- Checked: 30. Positive (support): 24. Not positive (partial): 6.
- The first-round voters had already marked 4 of the 6 not positive (3 partial, 1 unsure).
- Voter misses (the voter said support but spot-25 said partial): 2 of 30. Both are `snow-family-change-storage-optimized-80tb-full-shutdown-2025-11` and `storage-gateway-quota-file-shares-per-bucket-gr`, and both have the same cause: a cross-reference to another fact was put in the `condition` qualifier. Two misses is under three, so chapter 25 is **not flagged**.

## Non-positive verdicts

| Fact | First-round vote | spot-25 | Reason |
|---|---|---|---|
| storage-gateway-faq-volume-snapshots-incremental | partial | partial | Its paragraph opens with "For cached volumes", and that scope stands outside the quote. The claim generalized to all Volume Gateway snapshots. |
| storage-gateway-faq-deploy-targets | partial | partial | The qualifier condition (the hardware appliance is no longer offered to new customers) is a cross-reference that is not in the quote. |
| storage-gateway-faq-ha-vmware-restart-60-seconds | partial | partial | The quote stands under the heading "How does Amazon FSx File Gateway provide high availability?", but the claim is about any Storage Gateway. The condition (vSphere with VMware HA) stands only in the next FAQ answer. |
| transfer-family-internet-facing-vpc-endpoint-sftp-and-ftps-only | unsure | partial | The claim is universal ("only SFTP and FTPS"), but the Transfer Family FAQ says AS2 server endpoints also use internet-facing, VPC-hosted endpoints. The guide note covers the SFTP/FTPS/FTP server procedure only. |
| snow-family-change-storage-optimized-80tb-full-shutdown-2025-11 | support | partial | The qualifier condition ("the current Storage Optimized device option is 210 TB") is a cross-reference to another fact. The full-shutdown table row does not carry it. |
| storage-gateway-quota-file-shares-per-bucket-gr | support | partial | The qualifier condition (what the S3 File Gateway quota page says) is a statement from another page. The General Reference row does not carry it. |

## Amended (each once, `--by spot-25`, all mech-pass after, no dependents)

The patch files are in `_build/work/25-hybrid-storage/spot-25/<id>.json`. Every quote is verbatim from a saved AWS page.

1. **storage-gateway-faq-volume-snapshots-incremental** (now rev 3): the quote now starts at "For cached volumes, where your volume data is already stored in Amazon S3, ..." and runs to the incremental sentence, on the same FAQ page. The claim and scope are narrowed to cached volumes. On the page, the stored-volumes paragraph does not state incremental storage.
2. **storage-gateway-faq-deploy-targets** (now rev 3): the condition is cleared and the hardware-appliance cross-reference moved into `note`. The evidence is unchanged.
3. **storage-gateway-faq-ha-vmware-restart-60-seconds** (now rev 2): the evidence is replaced by the same sentences under the general "High Availability on VMware / How does Storage Gateway provide high availability?" answer. The quote starts at "Storage Gateway achieves high availability ...", so it matches that answer and not the FSx one. The environment answer was added as a second quote ("Storage Gateway high availability can currently be enabled in clustered VMware vSphere environments that have VMware HA enabled and have shared volume storage available."). The claim, scope and condition were updated to match.
4. **transfer-family-internet-facing-vpc-endpoint-sftp-and-ftps-only** (now rev 2): the claim is now attributed to the guide page, and the FAQ quote on AS2 internet-facing, VPC-hosted endpoints was added. The displays are unchanged.
5. **snow-family-change-storage-optimized-80tb-full-shutdown-2025-11** (now rev 2): the condition is cleared and the 210 TB cross-reference moved into `note`.
6. **storage-gateway-quota-file-shares-per-bucket-gr** (now rev 2): the condition is cleared and the quota-page statement moved into `note`, which already flagged the conflict.

No batch was cut and nothing was finalized. The adjudicator sends these six to a fresh, independent vote. No fact I judged positive was touched.

## Positive (24)

snow-family-faq-job-must-complete-within-360-days, datasync-prepare-scans-both-locations-for-differences, datasync-quota-throughput-per-task-without-agent, datasync-change-enhanced-mode-hdfs-azure-object-hyper-v-2026-07, storage-gateway-faq-three-storage-interfaces, storage-gateway-s3-file-gateway-glacier-instant-retrieval-not-supported, snow-family-pricing-per-job-fee-includes-15-days-then-per-day, storage-gateway-faq-volume-gateway-restore-to-gateway-or-ebs, datasync-faq-s3-to-s3-copies-metadata-tags-not-acls-versions, datasync-faq-other-clouds-gcs-azure, storage-gateway-s3-file-gateway-nfs-versions-smb-versions, datasync-faq-no-vpn-required, transfer-family-managed-workflows-steps-move-decrypt-tag-lambda, transfer-family-ftps-tls-encrypts-control-and-data-channels, datasync-task-execution-prepare-transfer-verify, storage-gateway-tape-gateway-definition-virtual-tape-storage, storage-gateway-s3-file-gateway-supports-object-lock-buckets, transfer-family-server-protocols-identity-provider-endpoint-and-hostname, datasync-task-mode-basic-definition, transfer-family-custom-idp-lambda-authenticates-and-authorizes, storage-gateway-faq-billing-file-gateway-s3-requests-cache-saves, storage-gateway-faq-s3-file-gateway-file-share-maps-to-bucket-or-prefix, storage-gateway-gateway-upload-buffer-staging-area, transfer-family-change-web-apps-2024-12.

## Observations for the adjudicator (not entail verdicts)

- **Pattern in this chapter.** In 3 of the 6 non-positive facts, the `condition` qualifier holds a cross-reference to another fact or page (register-25 added some of these during registration, for example on deploy-targets). The voters caught one of these and missed two. Other chapter 25 facts whose `condition` names another fact id or "page says" are worth a sweep: such text belongs in `note`.
- `snow-family-pricing-per-job-fee-includes-15-days-then-per-day`: support. The scope "on-demand" comes from the page overview ("two ways to pay: on-demand and committed upfront pricing"), and the monthly plan says no per-day fees apply.
- `transfer-family-managed-workflows-steps-move-decrypt-tag-lambda`: support. The page says "might include" and the claim says "include". This is a list of examples, not a closed list.

## Re-run on the voted facts (2026-10-14, resume of verify-facts)

The orchestrator resumed verify-facts and asked for the spot check to run again on the voted facts. State found: no chapter 25 fact is mech-pass any more (717 verified, 1 disputed, 13 rejected, 69 superseded). The r2 votes of batches 25-entail-011 and 25-entail-012 are recorded (20:32 to 20:34 UTC) and the statuses are already set.

**Sample.** Pool = the 731 non-superseded voted facts, sorted, same seed (20261013 + 25). It draws the same 30 ids as the first run (checked by script; `spot-25.sample.json` records the re-run).

**State of the 30.** The 24 facts judged positive in the first run are unchanged since then (same rev, mech check before the spot-25 amendments). I re-read their claims, qualifiers and quotes and judge all 24 support again. The 6 facts amended by spot-25 each have a fresh r2 entail vote of support, and I re-judged their current revisions:

| Fact | rev | r2 entail vote | spot-25 now | Note |
|---|---|---|---|---|
| storage-gateway-faq-volume-snapshots-incremental | 3 | support | support | Quote now carries "For cached volumes"; claim narrowed to match. |
| storage-gateway-faq-deploy-targets | 3 | support | support | Entail is fine. Status `disputed` comes from the currency lens (r2 currency vote `unsure`: the FAQ says "Nutanix AVM", the user guides say "Nutanix AHV"). That is for the adjudicator, not an entail miss. |
| storage-gateway-faq-ha-vmware-restart-60-seconds | 2 | support | support | Both quotes carry the mechanism, the 60-second maximum and the vSphere HA condition. The claim drops "currently", which does not change the meaning. |
| transfer-family-internet-facing-vpc-endpoint-sftp-and-ftps-only | 2 | support | support | The claim names the page for each statement, so the universal "only" is no longer the book's own claim. |
| snow-family-change-storage-optimized-80tb-full-shutdown-2025-11 | 2 | support | support | Cross-reference moved to note; the row carries the claim. |
| storage-gateway-quota-file-shares-per-bucket-gr | 2 | support | support | Cross-reference moved to note; the row carries the claim. |

**Result of the re-run.** Checked 30. Not positive on the current revisions: 0. Amended in this run: 0 (nothing to repair; no batch cut, nothing finalized). The first-round voter misses stay as measured above: 2 of 30 (`snow-family-change-storage-optimized-80tb-full-shutdown-2025-11`, `storage-gateway-quota-file-shares-per-bucket-gr`), under three, so chapter 25 is **not flagged**.

**For the adjudicator.** `storage-gateway-faq-deploy-targets` is the one disputed fact in the chapter, and the reason is currency: the hypervisor name. A fix is to keep the FAQ quote and add the user guide quote "VM appliance running on VMware ESXi, KVM, Microsoft Hyper-V, or Nutanix AHV hypervisor" (docs/storagegateway/latest/tgw/WhatIsStorageGateway), or to note that AVM is the FAQ's spelling. Writers should say "Nutanix AHV".
