# Web version: fact shards replace facts.json

Date: 2026-10-12. This pass finishes the change that an earlier agent started and could not complete (usage limit).

**Verdict: done.** The publishable build has 0 errors and emits no `facts.json`. The app loads one shard per fact namespace on demand. All tests pass, and the screenshots show both evidence paths working.

## The change in one table

| Before | After |
|---|---|
| `facts.json`: every verified fact in one file, 4 MB budget, 4.18 MB on 2026-10-12 (over budget) | `f/<service>.json`: one shard per fact namespace (`data/facts/<service>.jsonl`), warn 400 KB, cap 1.5 MB |
| | `facts-index.json` (4.6 KB, cap 60 KB): `{v, count, shards: {service: {path, bytes, sha256, count}}, stray: {id: service}}` |
| | `manifest.json` `factsIndex`: path, bytes, SHA-256, shard count and fact count of the index |
| `Content.facts()` | `Content.factsIndex()`, `Content.factService(id, index)` (pure), `Content.factShard(service)`, `Content.fact(id)` |
| `publish-plan.json` | lists every shard and the index (bytes, sha256, changed); `removed` lists `facts.json` |

How a fact id finds its shard (the same rule in `site.fact_shard` and `Content.factService`): use `stray[id]` when it names a shard. Otherwise take the longest shard key `k` such that the id starts with `k-`, so `s3-glacier-…` goes to `s3-glacier`, not `s3`. Otherwise there is no shard. The app fetches the index and each shard at most once per visit. A manifest refresh drops them only when the index hash changes. In `--single` they come from the inline map. Chapter, data and mock files still carry the cards of the facts they link, so reading a chapter loads no shard. A shard is fetched only for `#fact.<id>`, a fact found by search, or a chip whose card is not in the open file.

## Audit: what was already done, and what was unfinished

Already done by the earlier agent (checked by reading the code and by the tests below):

- `tools/saalib/site.py`: shard and index emission, the `factsIndex` row in the manifest, shard budgets, `RETIRED_PATHS = ("facts.json",)` in the plan's `removed`, and a `WB07` error for a namespace that is not a valid file name.
- `tools/web/js/content.js`: the lazy loader. `tools/web/js/evidence.js`: the popover and the `#fact.<id>` page read an unknown fact through `Content.fact`.
- `tools/web/js/selftest.js`: `#t.render-all` checks every shard against the index and finds every chapter fact again through `Content.fact`.
- `tools/web/tests/test_content.mjs` (new node test). `tools/tests/test_site.py`: the prefix rule, a must-fail test for a shard over its cap, a budget unit test, and the multi-file publish plan.

Unfinished or wrong, now done:

1. **ARCHITECTURE.md still described `facts.json`.** Updated: change note at the top, 1.2 data files table and budgets (with the reason for the 1.5 MB cap), 2.1 build JSON (`facts`, `preview`, `written`), 2.2 `load()` (the file stem is the namespace), 2.4 (`factsIndex`, shard and index shapes, the lookup rule, when shards load), 2.6 `--single`, 2.7 publish plan (shards, `removed`, retired paths), 3.2 Content and Evidence API, 3.3 `#fact.<id>`, 9.1 (`test_content.mjs`, the Python must-fail cases), 9.2 render-all, 9.6 load costs.
2. **Stale `_build/site/facts.json`.** It came from the last publishable build at 10:21, before the shard change at 11:01. The build now replaces the folder: `facts.json` is gone.
3. **Stale `_build/tmp/web-selftest`** (from 2026-10-04). Because of it, `node test_content.mjs` without an argument failed. `web shots` and `web selftest` rebuilt the folder; the test now passes.
4. **No test of the `--single` publish plan with shards.** Added to `test_only_ready_and_publish_plan`: one file in `content`; `removed` holds the shards, `facts-index.json`, `facts.json` and `manifest.json`, never `index.html`.
5. **Batch file count.** Each namespace adds one file to the content batch, whose limit is 255 files. New `WB01` warning above 230 files per batch, with a must-fail test (`test_must_fail_batch_file_count`).
6. Small fix found on the way: `DEFAULT_CFG` in `site.py` (used only when `shell.json` is missing) named the rejected fact id `exam-duration`; it now names `exam-duration-minutes`.

The two copies of the Python test, `tools/tests/test_site.py` and `tools/web/tests/test_site.py`, are identical.

## Shard sizes

Build `7e399e6b60` (`build web --only-ready`): 32 shards, 4,195 facts, 4,181,638 bytes in total.

| Shard | Facts | Bytes |
|---|---|---|
| f/s3.json | 597 | 600,096 (above the 400 KB warning level) |
| f/vpc.json | 511 | 500,963 (above the 400 KB warning level) |
| f/iam.json | 342 | 371,669 |
| f/kms.json | 245 | 221,928 |
| f/waf.json | 213 | 183,407 |
| f/organizations.json | 169 | 176,573 |
| f/acm.json | 161 | 150,905 |
| f/cognito.json | 158 | 150,813 |
| f/iam-identity-center.json | 144 | 150,231 |
| f/secrets-manager.json | 163 | 139,675 |
| f/global-infrastructure.json | 129 | 127,220 |
| f/guardduty.json | 123 | 122,929 |
| f/well-architected.json | 105 | 116,804 |
| f/directory-service.json | 107 | 115,277 |
| f/network-firewall.json | 107 | 115,011 |
| f/exam.json | 92 | 92,286 |
| f/control-tower.json | 84 | 87,590 |
| f/shield.json | 76 | 78,885 |
| f/security-hub.json | 68 | 73,948 |
| f/inspector.json | 70 | 66,053 |
| f/parameter-store.json | 64 | 65,379 |
| f/firewall-manager.json | 56 | 62,912 |
| f/config.json | 58 | 61,486 |
| f/management-console.json | 63 | 58,812 |
| f/ram.json | 52 | 57,018 |
| f/cloudhsm.json | 68 | 55,938 |
| f/sts.json | 42 | 54,016 |
| f/macie.json | 44 | 43,563 |
| f/detective.json | 31 | 29,679 |
| f/artifact.json | 29 | 26,519 |
| f/aws-cli.json | 16 | 16,809 |
| f/s3-glacier.json | 8 | 7,244 |

`stray` is empty: every fact id starts with its own namespace. Seven fact files (`ec2`, `ec2-auto-scaling`, `lambda`, `aws-auto-scaling`, `budgets`, `privatelink`, `vpc-peering`) have no verified facts yet, so they have no shard.

## Tests

| Run | Result |
|---|---|
| `python3 aws-saa-book/tools/tests/run.py site` | 56 tests, OK (none skipped) |
| `node <file>` for each of the 7 files in `tools/web/tests/` (default folder, and `_build/preview` as argument) | all pass: aicore 11/11, content 11/11, merge 13/13, scoring 23/23, search 5/5, store 15/15, util 23/23 |
| `python3 aws-saa-book/tools/saa.py web lint` | 37 files, 0 findings |
| `web selftest` on a sandbox copy of the fixture book (`_build/tmp/web-shards-selftest`) | ok: render 3163/3163, phone 3568/3568, sim 294/294, hot 24/24, node 7/7, 0 failures |
| `web selftest --only render` on the real book (extra check) | render 9285/9285, with the shard checks over all 32 shards. The command still exits 1 because of a build error that has nothing to do with the shards: see the open items. |

Section 9.2 of the architecture covers the evidence path: `#t.render-all` ends with the shard check, which finds every chapter fact through `Content.fact`.

## Builds

| Command | Result |
|---|---|
| `build web --only-ready` | ok, 48 files, 7,598,335 bytes, 0 errors, 3 warnings (`c/iam.json` 427 KB, `f/s3.json` 600 KB, `f/vpc.json` 501 KB: all above their warning levels, all below their caps). No `facts.json` in `_build/site/`. |
| `build web --only-ready --single` | ok, one `index.html` of 7,652,674 bytes (budget 15 MB), 0 errors, 0 warnings. The inline map holds the 32 shards and `facts-index.json`, and no `facts.json`. |

`_build/site/publish-plan.json`: `url` null, title "SAA-C03 Handbook", icon `book`. Batch `content` has 48 files: `assets/icons.svg`, `assets/search-worker.js`, `c/aws-map.json`, `c/how-the-exam-asks.json`, `c/iam.json`, `c/start-here.json`, `d/aws-map.json`, `d/how-the-exam-asks.json`, `d/iam.json`, the 32 `f/<service>.json` shards of the table above, `facts-index.json`, `glossary.json`, `index.html`, `manifest.json`, `plan.json`, `qindex.json`, `search/corpus.json`. Batch `exports` has 0 files. `removed`: `["facts.json"]`.

`_build/site-single/publish-plan.json`: `content` holds only `index.html`. `removed` holds 48 paths: every multi-file path, the shards, `facts-index.json` and `facts.json`.

## Screenshots

Folder: `aws-saa-book/_build/shots/facts-shards/`. The extra shot list is `aws-saa-book/_build/tmp/web-shards-extra.json`. The preview is of the real book, and IAM is a ready chapter.

- `shard-chip.desktop.light.png`, `.desktop.dark`, `.phone.light`, `.phone.dark`: route `#ch.iam.fast.in-one-breath`, then a click on the first fact chip. The evidence popover opens: `iam-eval-implicit-deny-by-default`, its claim, its scope, two verbatim AWS quotes with source links, "Checked 2026-10-11", and "Report a problem". On the phone it is a bottom sheet.
- `shard-fact-page.desktop.light.png`, `.phone.light`: a cold load of `#fact.sts-temporary-credentials-expire-not-stored`. No chapter file is open, so the card can only come from `facts-index.json` plus `f/sts.json`. The page shows the claim, the scope and the three quotes; they match `f/sts.json` word for word.

## Open items (not part of this change)

- **`q/mock-preview.json` is above its budget in a preview of the real book** (493 KB, cap 400 KB). This is the synthetic preview mock: it is never published, and it grows with the draft chapters. It makes `web selftest` on the real book exit 1 at the build step, while all render checks pass. Options: skip the `q/` budget for the synthetic mock, or keep fewer facts in it.
- **`--single` will outgrow 15 MB.** It inlines every verified fact (4.2 MB today, with 4 ready chapters) and every built chapter. At about three times today's facts, or with most chapters ready, it will pass the 15 MB budget. The build then fails with `WB01`. The fallback would need a smaller fact set (for example, only facts linked from built files, with search results for other facts showing the claim only).
- **Content batch near 255 files at full size.** About 118 other files plus about 120 to 130 shards when every in-scope service (118 in the registry) has facts. The new warning starts above 230. The remedy written in ARCHITECTURE.md 1.2 is a separate `facts` batch, published right after `content`; it is not built yet.
- `f/s3.json` and `f/vpc.json` are above the 400 KB warning level. They are far below the cap. A split is only needed near 1.5 MB.
