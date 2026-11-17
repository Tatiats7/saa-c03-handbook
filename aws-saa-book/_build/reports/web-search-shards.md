# Web version: search shards replace search/corpus.json

Date: 2026-10-14.

**Verdict: done.** `build web --only-ready` has 0 errors and no longer writes `search/corpus.json`. The search loads a small index, then one shard per chapter. All tests pass.

## The change in one table

| Before | After |
|---|---|
| `search/corpus.json`: every search doc in one file. It was 4.6 MB with 19 ready chapters and would reach about 12 MB at 53. The budget was raised to warn 4 MB, fail 8 MB as a stopgap. | `search/<slug>.json`: one shard per chapter, `{v, chapter, docs}`. Budget: warn 400 KB, fail 800 KB. |
| | `search/index.json`: `{v, count, aliases, shards: [{chapter, path, bytes, count}]}`. Budget: fail 200 KB. |
| The page posted `{t:"load", data}` with the whole corpus. | The page posts `{t:"aliases"}`, then `{t:"shard", data}` once per shard. The worker adds each shard to its index. |
| Budget entry for `search/corpus.json` | Removed. `search/corpus.json` is in `RETIRED_PATHS`, so the next publish deletes it. |

The doc shape `[route, chapter title, heading, kind, text]` is unchanged.

## Design

**Which shard holds a doc.** The facts are 83% of the corpus (3.8 of 4.6 MB), and they do not belong to a chapter. A shard per ready chapter alone would not have shrunk the problem, so the rule is:

- `search/<slug>.json` holds the `s` (section) and `q` (question stem) docs of a built chapter.
- It also holds the `f` docs of every fact namespace that the chapter lists in `book.json` `services`. Every namespace except `exam` is listed by exactly one chapter.
- A planned chapter therefore gets a shard when its services have verified facts. Today that is 8 planned chapters: aurora, cloudfront, containers, dynamodb, efs-fsx, hybrid-networking, messaging and vpc-connectivity. Their facts stay searchable, as they were in `corpus.json`.
- `search/book.json` has `"chapter": null`. It holds the 195 glossary docs (`g`) and the facts of namespaces that no chapter lists (today `exam`, 92 facts).
- A chapter with no docs gets no shard.
- The index lists the shards in book order, with `book.json` last.

**Page (`search.js`).** On the first full-text query:

1. The page starts the worker, loads `search/index.json`, and posts the aliases. The worker answers `ready`, and queries work from then on.
2. The page fetches every shard at once (`Content.text`). It posts the texts in index order, so doc ids and rank ties are the same on every visit.
3. While shards are still loading, the results cover what is loaded so far, under the line "Indexing n of m chapters…". Each shard that arrives re-runs the open query.
4. A shard that fails to load is left out and counts as done.
5. With 0 shards the answer is "No text matches."
6. If there is no index, the line is "Full-text search is not available right now."

Nothing is cached in localStorage. In `--single` the search files come from the inline map, like every other JSON file. The screen-reader announcement fires once per query text and once more when the last shard is in, not on every refresh.

**Worker (`search-worker.js`), same `t` key as before:**

- `{t:"aliases", aliases}` replies `{t:"ready", n}`.
- `{t:"shard", data}` or `{t:"shard", docs}` replies `{t:"added", n}`, where `n` is the number of docs so far. A text that is not a shard gets `{t:"skipped", message}`.
- `{t:"q", id, text}` replies `{t:"r", id, rows}`. It replies `{t:"error"}` if it arrives before any `aliases` or `shard` message.
- The index grows by appending, and the vocabulary is kept up to date incrementally. Matching and ranking are unchanged.
- `{t:"load"}` is gone.
- Size: 9,557 bytes of source and 7,046 bytes as published (budget 60 KB). It is still published as `assets/search-worker.js`, or inlined as `#saa-worker` in `--single`.

## Files changed

- `tools/saalib/site.py`:
  - New constants: `SEARCH_DIR`, `SEARCH_INDEX`, `SEARCH_BOOK`.
  - `RETIRED_PATHS` now includes `search/corpus.json`.
  - `BUDGETS`: the corpus entry is removed, and `^search/index\.json$` (fail 200 KB) and `^search/` (warn 400 KB, fail 800 KB) are added.
  - `self.corpus` is now a dict of shard key to docs.
  - New `search_shards()`.
  - The build result has a `search` entry: index path, bytes, number of shards, number of docs, and the 3 largest shards.
  - The text of the batch warning now mentions the search shards.
  - No publish-plan change was needed: the plan lists the files themselves, not patterns.
- `tools/web/js/search.js`: the loader, the progress line and the announcement rule.
- `tools/web/js/search-worker.js`: the incremental protocol.
- `tools/tests/test_site.py`, and its identical copy `tools/web/tests/test_site.py`.
- `tools/web/tests/test_search.mjs`.
- `tools/web/ARCHITECTURE.md`: a change note, plus updates to 1.2, 2.1, 2.4, 2.6, 2.7, 6.6, 9.1 and 9.6.

## Tests

| Run | Result |
|---|---|
| `python3 aws-saa-book/tools/tests/run.py` (whole suite) | 811 tests, OK |
| `python3 aws-saa-book/tools/tests/run.py site` | 58 tests, OK (56 before) |
| `node` on each of the 7 files in `tools/web/tests/`, against the preview build and against `_build/site` | All pass: aicore 11/11, content 11/11, merge 13/13, scoring 23/23, search 9/9, store 15/15, util 23/23 |
| `saa.py web lint` | 37 files, 0 findings |
| `saa.py web selftest --only node` | node 7/7. The command still exits 1 because of the known, unrelated preview budget on `q/mock-preview.json` (597 KB, cap 400 KB; see the facts-shards report). |

New or changed tests:

- **Python**
  - `Helpers.test_must_fail_search_budgets` (new). Over-budget index and shard give errors, and a shard over 400 KB gives a warning. It also checks that the budget table has both new entries and no corpus entry, and that `search/corpus.json` is in `RETIRED_PATHS`.
  - `FixtureBuild.test_search_index_and_shards` (new). The index shape. Every built chapter is listed. Each shard parses, matches its row (bytes and count), and holds only its chapter's docs: `s` and `q` routes of the chapter, `f` docs of its services, `g` docs only in the book shard. The index count adds up. The build result has a `search` entry.
  - `test_files`: the search files exist, and `search/corpus.json` does not.
  - `test_build_is_deterministic_and_single_works`: `--single` inlines the search index and shards, and not the corpus.
  - `test_only_ready_and_publish_plan`:
    - The plan lists the search files with bytes, sha256 and changed.
    - `removed` is `["facts.json", "search/corpus.json"]`.
    - A planned chapter's shard holds only `f` docs.
    - The `--single` plan removes the search files.
- **Node** (`test_search.mjs`)
  - New: "aliases answer ready; each shard answers added …; a broken shard is skipped".
  - New: "the index builds from two shard messages and finds a term from each". This includes a query between the two shards and ties that follow shard order.
  - New: "page: answers over the shards so far, says 'Indexing n of m chapters', then the whole book". It runs `search.js` with a fake sheet, a `Worker` that runs the real worker file, and a late second shard. It also covers 0 shards and a missing index.
  - New, against a built folder: "built: the index lists every built chapter; each shard parses and holds only its chapter's docs" (also checks that there is no `corpus.json`).
  - New, against a built folder: "built: the worker indexes every shard in order and finds a heading of the first and of the last chapter".
  - The three older worker tests now load through `aliases` and `shard`.

## Build

`python3 aws-saa-book/tools/saa.py build web --only-ready`:

- Build `675c715e04`, 141 files, 27,835,693 bytes.
- 19 ready chapters, 34 planned.
- 0 errors and 15 warnings. All 15 are `c/` and `f/` files above 400 KB; none is a search file.
- No `search/corpus.json`. `publish-plan.json`: content batch has 141 files, and `removed` is `["facts.json", "search/corpus.json"]`.
- `index.html` is 446,417 bytes.

| | Bytes |
|---|---|
| `search/index.json` (28 shards, 14,214 docs, 30 alias entries) | 3,424 |
| Largest shard, `search/route53.json` (26 s, 18 q, 785 f) | 271,548 |
| Then `efs-fsx` (planned, 869 f), `s3`, `cloudfront` (planned), `aurora` (planned) | 244,838, 228,499, 225,669, 223,246 |
| `search/book.json` (195 g, 92 f) | 69,995 |
| All 28 shards together (same as the old corpus) | 4,622,860 |

**Checked in node over the built site.** The worker indexes all 28 shards in 146 ms. Queries take 0 to 6 ms:

- "NAT gateway" finds VPC sections.
- "DynamoDB global tables" finds facts of the planned dynamodb chapter.
- "least privilege" finds the glossary term first.
- "exam duration" finds `fact.exam-duration-minutes` from the book shard.

No browser was opened.

## Open items

- **Content batch at full size.** With 53 chapters there will be about 54 search shards, on top of about 240 other files including the fact shards. That passes the platform limit of 255 files per publish call. Today the batch has 141 files; `WB01` warns above 230. The batch split described in ARCHITECTURE 1.2 (a separate batch published after `content`) is still not built. It should be built before about 40 chapters are ready.
- **Browser checks not run.** On instruction, I ran no headless-Chrome checks: the `web selftest` routes (render, phone, sim, hot) and the `search` screenshot. `selftest.js` has no search check of its own; the node tests above cover the loader and the worker.
- **Re-queries during loading.** Each arriving shard re-runs the open query, so up to about 55 queries while loading. Each costs a few ms, so I added no throttle.
- **Reserved slug.** `book` is reserved as the name of the no-chapter shard; no chapter may use that slug.
- **Not changed.** The `--single` growth past 15 MB and the `q/mock-preview.json` preview budget, both from the facts-shards report, are unaffected by this change.
