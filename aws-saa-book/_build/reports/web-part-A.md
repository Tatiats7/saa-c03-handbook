# Web version, part A: site build and tool commands

Date: 2026-10-04. Contract: `tools/web/ARCHITECTURE.md` version 1.1.

## Files

| File | Content |
|---|---|
| `tools/saalib/site.py` | `build web`; the build steps of section 2; token CSS and `WB06`; budgets; publish plan |
| `tools/saalib/_site_web.py` | `web lint` (`WL01` to `WL10`), `web selftest`, `web shots`, the in-process server. Loaded by `site.py`; `saa.py` skips it because of the `_` |
| `tools/helpers/site_md.py` | uv script (`markdown-it-py==3.0.0`, `pygments==2.19.1`): the mapping table of 2.3 |
| `tools/web/stubs/skeleton.html` | emulation of the publish skeleton, slots `{{theme}}`, `{{stub}}`, `{{page}}` |
| `tools/web/tests/test_site.py` | 52 tests: mapping (every device and callout), helpers, lint codes, fixture build |
| `tools/web/tests/fixtures/plan.json`, `drills.json` | overlay for the fixture book (three plans; four drills) |

## Commands

```
python3 aws-saa-book/tools/saa.py build web [--only-ready] [--single] [--preview] [--out-dir DIR] [--no-minify]
python3 aws-saa-book/tools/saa.py web lint
python3 aws-saa-book/tools/saa.py web selftest [--single] [--only render|phone|sim|hot|node]
python3 aws-saa-book/tools/saa.py web shots [--shots-dir DIR] [--only NAME,...] [--single]
python3 aws-saa-book/tools/web/tests/test_site.py
```

A shared sandbox of the fixture book is at `aws-saa-book/_build/tmp/web-fixture` (add `--book-dir aws-saa-book/_build/tmp/web-fixture`). Its preview is in `_build/preview` of that folder; `web selftest` and `web shots` build their own copy in `_build/tmp/web-selftest` and write PNG files to `_build/shots`.

## Tested alone (state at the end of this task)

- `test_site.py`: 52 of 52 pass.
- Fixture, `build web --preview`: 0 errors; warnings `WB04` (the fixture hero has no spec) and four `WB10` (the exam fact ids of `shell.json` are not in the fixture canon). Two runs give the same bytes.
- Fixture, `web selftest`: render 3153/3153, phone 3558/3558, sim 294/294, hot 23/23, node 6/6. With `--single`: the same, hot 24/24.
- Fixture, `web shots --only home,chapter,prose`: 14 PNG files and `sheet.png`; I looked at the sheet and at `prose.desktop.light.png`.
- Real book, `build web --preview`: 53 planned chapters, 0 errors.
- `web lint`: 36 files, 0 findings.

## Open problem for the integrator

**`index.html` is above its budget.** A build without `--preview` fails with `WB01`: 418,884 bytes against 400,000. The page script is about 391 KB of source in 25 files. The build already drops comments, indentation and blank lines (338 KB after that; see deviation 3). Either the budget of 1.2 goes up (the platform limit is 16 MB), or the modules get smaller. Until then `build web` writes no site and no `publish-plan.json`.

## Deviations and interpretations

1. **`--out DIR` is `--out-dir DIR` (alias `--dir`); `web shots --out DIR` is `--shots-dir DIR`.** `common.add_common_args` already defines `--out FILE` for the printed result, and the contract says that every command takes the common options.
2. **Output folder safety.** The build replaces its output folder. It refuses (exit 4) a folder that is not empty and does not hold the marker file `.saa-site`, which the build writes. The marker is not in any publish batch.
3. **Smaller sources.** `minify_js` and `minify_css` drop comments, indentation and blank lines; nothing is renamed or joined. The page script is used in that form only when `node --check` accepts it; without node, or on a failed check, the full text is used. `--no-minify` keeps the sources as written (useful for debugging line numbers). Not in the contract.
4. **A failed build.** With errors, a build without `--preview` writes nothing (`"written": false`, `"plan": null`). A preview build always writes, so the other parts can be tested while a check fails. A preview build writes no `publish-plan.json`.
5. **Result JSON** has two more keys: `preview` and `written`.
6. **Slots of `shell.html`.** The build accepts both forms: when the shell already holds `<script ... id="saa-boot">`, `<style>` or `<script>` around a slot, the slot gets the bare content; otherwise the build adds the element. `{{inline}}` gets `<script type="application/json" id="saa-inline">` plus `<script type="text/plain" id="saa-worker">` in a `--single` build and nothing otherwise. Without `shell.html` (preview only) a built-in shell with the DOM of 3.6 is used.
7. **Helper job and result.** Added to the job: `ctx.hosts`, `ctx.unverified`, `chapters[].quiz`, `parts[].file`, and `parts[].text` as an alternative to `path` (tests). Added to each part result: `title`, `figmeta`, `trapmap`, `tasks`, `generated`; each `text` row also has `own` (the text without the subsections). A warning is an object `{code, level, line, msg}`; `inline_warnings` lists those of the inline fields.
8. **Section text.** `c/<slug>.json` `text[sid]` of an H2 holds its whole text, subsections included (Ask needs it for "How it works"). The search corpus uses the text without the subsections, so no sentence is indexed twice. Sections without text are left out.
9. **`traps` map.** A `trap-ref` comment sets `data-trap` but is not entered in the manifest `traps` map (it points to a trap of another chapter).
10. **Figures.** A figure without spec and without SVG file renders `<p class="fig-missing">alt text</p>` inside `.fig-s`, with `WB04`. `data-kind` is `image` for an embedded SVG file. The `alt` of `.fig-img` is the Markdown alt text.
11. **Static first frame.** New class names, not in 4.3: `.static`, `.static-facts` (the exam facts as `.pill` elements), `.toc-list`, `.toc-part-t`, `.toc-t`, `.is-planned`, `.is-draft`, `.is-ready` on `.toc-ch`. The Reference list is `<div class="toc-ref">` with an `.eyebrow` and a list.
12. **Synthetic parts and `WB05`.** The check uses the `files` of the chapter's template in `SPEC.json`: a required file whose part is absent gives `WB05`; `3-do.md` only when it is required. A missing `data/plan.json` is a `WB05` warning and `plan.json` is not emitted.
13. **`c/<slug>.json` `facts`** hold the facts linked in the parts and the facts of the chapter's items, because the `sources` list names both and the Sources part draws chips from this file.
14. **`shell.json` missing** (preview only): the values of section 8.4 are built in as defaults, `previewMockMinutes` included.
15. **Mock number `n`** is the position among all mock chapters in book order, so `#mock.2` stays 2 when mock 1 is not written.
16. **`web lint`.** `WL06` also allows the host `www.w3.org` (the SVG namespace string). `WL01` checks named colours only in CSS. Comments are ignored except for `WL09`. `WL02` also catches `dvh`, `svh`, `lvh`.
17. **`web selftest`.** The count of skipped renderers is read from a line `<n> skipped` in `#saa-selftest`, when present. The JSON also has `build`.
18. **`web shots`.** All shots use scale 1. The forced-light shot uses Chrome's `--force-dark-mode`.
19. **Fixture overlay drills.** The fixture has only domain 2 questions, so the four drills reuse them; the selftest needs every drill to have questions.
20. **Term auto-links** match whole words only: `crates` does not link to `crate`. A term that is not an `aws-name` matches in any case.

## Notes for other owners

- C: a drill question is in `d/<slug>.json` and in its drill file by contract, so a test that reads every file sees the same id twice.
- B: the `prose` shots show an empty area above the header (the page is scrolled when Chrome takes the picture).
- Orchestrator: the four exam fact ids of `shell.json` are not verified facts yet (`WB10`), so `manifest.examFacts` is empty.
