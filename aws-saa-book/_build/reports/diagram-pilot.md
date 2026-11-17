# Diagram pilot gate: visual judgment, round 2

Date: 2026-10-04. Judge: visual judge agent (second round, after the repair pass). All 16 specs rebuilt clean (`diagram build --all`, no errors, no warnings), then `diagram sheet` and `diagram shot <id>` for the 8 pilots. Every pilot was looked at in four panels (desktop and 368 px phone, light and dark) plus the standalone strip. The two densest figures (three-tier, hybrid) were also looked at as 2x standalone shots.

Limit of this judgment: the PNGs were read downscaled by the image viewer (the tall previews at about one third of capture size). Phone legibility was judged from those views plus the printed scale, not on a real phone.

## Verdict: PASS

- Average over all 40 scores: **4.53** (181 / 40). Rule: at least 4. Met.
- Every diagram scores at least 4 on layout and on phone legibility. Met. The lowest values are 4 (pilot-vpc-two-az on both; pilot-web-three-tier on layout).
- No overlap, no clipping and no edge through a node in any of the 8 diagrams, in light or in dark. No dark-only defect.
- The grid renderer is good enough to go on. No fallback to D2.

Round 1 was a narrow fail (4.38; pilot-vpc-two-az scored 3 on phone legibility at scale 0.75).

## Scores

L = correctness of layout, P = legibility at phone width, C = clarity of the single claim, S = consistency with the other diagrams, Q = professional look.

| Diagram | Kind | Size (units) | Phone scale | L | P | C | S | Q | Sum | Round 1 |
|---|---|---|---|---|---|---|---|---|---|---|
| pilot-elb-choose | ladder | 353 x 450 | 0.95 | 5 | 5 | 5 | 4 | 5 | 24 | 24 |
| pilot-hybrid-connectivity | arch | 332 x 616 | 1.00 | 5 | 5 | 4 | 4 | 5 | 23 | 22 |
| pilot-iam-cross-account-role | sequence | 305 x 376 | 1.00 | 5 | 5 | 5 | 4 | 4 | 23 | 21 |
| pilot-rds-multi-az-vs-replica | compare | 638 x 318 | 1.00 (stacked) | 5 | 5 | 5 | 4 | 5 | 24 | 24 |
| pilot-s3-lifecycle | timeline | 388 x 220 | 0.86 | 5 | 5 | 4 | 4 | 4 | 22 | 21 |
| pilot-s3-presigned-url | sequence | 328 x 400 | 1.00 | 5 | 5 | 5 | 4 | 4 | 23 | 23 |
| pilot-vpc-two-az | arch | 392 x 544 | 0.85 | 4 | 4 | 5 | 4 | 4 | 21 | 19 |
| pilot-web-three-tier | arch | 356 x 738 | 0.94 | 4 | 5 | 4 | 4 | 4 | 21 | 21 |

## What the repair pass fixed (confirmed in the screenshots)

- pilot-vpc-two-az: 444 to 392 units wide, phone scale 0.75 to 0.85. The route table nodes (and the icon with IP address text) are gone. The path now reads top to bottom. The gateway endpoint branch is gone, so the collinear step 3 and step 5 lines are gone.
- pilot-iam-cross-account-role: redrawn as a `sequence`. The two policy checks are two highlighted asides, which is exactly the claim. Steps follow the eye.
- pilot-hybrid-connectivity: steps renumbered 1 to 7, one badge per hop. Step 4 is one trunk with one badge that splits to the two VPCs.
- pilot-web-three-tier: step 3 is one trunk with one badge; step 4 merges into one arrowhead on the primary DB; the load balancer is highlighted again.
- pilot-s3-lifecycle: tick labels are words (Created, Later, Much later, Last day), the lane is "Usual access", and the Expiration line has a gap to the last span.

## Defects per diagram (what is left)

### pilot-elb-choose (24)
- No layout defect. Correct gist in five seconds.
- Spec, minor: no highlighted outcome, while the sample ladder highlights one. Decide one rule.

### pilot-hybrid-connectivity (23)
- Layout clean. Primary (blue, solid) against backup (grey, dashed) reads at once.
- Spec, minor: the claim sentence is long for a skim reader. Seven steps make a long list on the phone.
- Renderer, minor: the "primary" and "backup" labels sit above the badges, close to the group label band of the data center box.

### pilot-iam-cross-account-role (23)
- No layout defect.
- Spec, minor: the role itself is not drawn; the figure shows "User in account A", "AWS STS", "Bucket in account B". The claim speaks of "two policies on the role", so the reader must take from the caption that both asides belong to one role.
- Spec, minor: two highlighted asides and no highlighted message. Fine here, but it is a different use of highlight than in pilot-s3-presigned-url (one highlighted message).

### pilot-rds-multi-az-vs-replica (24)
- No layout defect. Same structure in both panels; the difference is the only change. Stacked phone form is clean.
- Spec, minor: "App server" and "Primary DB" here, "EC2 instance" and "Primary DB instance" in pilot-web-three-tier.
- Renderer, minor: on desktop the two panels stand far apart, with a wide empty band between them.

### pilot-s3-lifecycle (22)
- No layout defect.
- Spec: the ticks "Later" and "Much later" are vague. Acceptable while the fact canon has no day values; replace them with canon values when they exist.
- Renderer, minor: the "Transition" event labels sit directly above the lane label "Storage class"; the two rows of small text are close.

### pilot-s3-presigned-url (23)
- No layout defect. The aside "Browser has no AWS credentials" is well placed.
- Spec, minor: the actor that starts (Browser) stands in the middle, so message 1 runs right to left. Browser, Application, Amazon S3 would not work either (message 4 would cross a lifeline), so this is acceptable.
- Renderer, minor: the badge sits on the sender's lifeline with a short stub of line past it.

### pilot-vpc-two-az (21)
- Phone: scale 0.85. Node labels about 11 px, group labels about 10 px. Readable, the smallest text of the set.
- Layout, minor: the step 1 arrow enters each public subnet about 4 units to the right of the "Public subnet" label; on the phone the two almost touch. The "internet traffic" label starts close to the Availability Zone border.
- Spec: the private subnet is drawn above the public subnet and the internet is at the bottom. This keeps the outbound path top to bottom, but it is upside down against the usual AWS reference picture (internet and public subnet on top). A reader who knows the usual picture needs a second look. Decide one rule for outbound paths and write it in the style guide.

### pilot-web-three-tier (21)
- Renderer: the labels "Private subnets: data tier" and "Multi-AZ deployment" sit at the right end of their bands; every other group label is on the left. Looks unplanned.
- Renderer: two groups with the same cells (subnet plus Auto Scaling group; subnet plus Multi-AZ deployment) give double borders and two label bands. Busy, still correct.
- Renderer, minor: the step 3 trunk enters the instances from their inner sides (a horizontal bar between the two icons); the step 4 merge has a small kink just above the badge.
- Spec: no Availability Zone is drawn, so "Multi-AZ deployment" is told, not shown (a known limit: groups may not cross).

## Renderer defects, in order of impact

1. **Group label flips to the right end of its band** when an edge enters on the left (three-tier data tier). Mixed left and right labels in one figure. Prefer to shift the label a few units, or keep it left and route the edge past it.
2. **Two groups on the same cells** draw two borders and two label bands (three-tier). Consider one merged band ("Private subnets: app tier / Auto Scaling group") or a tighter inner inset.
3. **Side entry into nested groups.** A top-down trunk into a nested group ends on the inner sides of the nodes (three-tier step 3). A split above the nodes with entry from the top would keep the flow straight.
4. **Edge and edge label too close to a group label or border** (vpc step 1 next to "Public subnet"; "internet traffic" at the AZ border). Raise the minimum clearance to about 8 units, or let lint warn.
5. **Phone scale of two-column figures with three nested borders** is 0.85. Good enough; any wider label pushes it down again. Keep the lint warning at the `s` budget and watch this in chapter figures.
6. **Desktop card.** A small figure sits at the left of a wide card; compare panels stand far apart. Centre the figure or cap the card width (web app matter).
7. **Fan-in merge kink** (three-tier step 4): the joining line curves into the trunk just above the badge.
8. **Timeline event labels** sit close above the first lane label.
9. **Sequence badge stub**: a short piece of line shows past the badge on the sender's lifeline.
10. Still not supported and missed by a professional eye: an Auto Scaling group or Multi-AZ deployment across two AZ boxes; an internet gateway on the VPC border; group corner icons.

## Spec defects (authors), in order of impact

1. Set-wide naming: "App server" or "EC2 instance"; "Primary DB" or "Primary DB instance". Pick one per concept in the glossary.
2. Set-wide label case: sequence message labels start with a capital ("Ask for upload URL"); arch edge labels do not ("internet traffic", "replication"). Pick one rule.
3. Set-wide highlight rule: none in the ladder, a node in three-tier, edges in vpc and hybrid, asides in IAM, one message in presigned. State in the style guide what gets the highlight per kind.
4. pilot-vpc-two-az: private subnet above public subnet. Decide the rule for outbound paths.
5. pilot-s3-lifecycle: vague ticks until the canon has values.
6. pilot-hybrid-connectivity: long claim sentence.

None of these blocks the gate. Items 1 to 3 should be fixed in `TOOLS-diagram.md` before chapter diagrams are written, because they repeat in every figure.

## Files

- Contact sheet: `aws-saa-book/_build/tmp/diagram-preview/sheet.png`
- Previews: `aws-saa-book/_build/tmp/diagram-preview/pilot-*.png`
- 2x standalone shots: `aws-saa-book/_build/tmp/diagram-judge/r2-three-tier.png`, `aws-saa-book/_build/tmp/diagram-judge/r2-hybrid.png`
