# Fixes applied to `tools/web/ARCHITECTURE.md` (version 1.0 to 1.1)

Input: `web-arch-critique-platform.md` (P1 to P26: 1 blocker, 10 major, 15 minor) and `web-arch-critique-implementer.md` (I1 to I43: 4 blockers, 16 major, 23 minor).

Result: 69 findings, 69 fixed (6 of them with a variation, marked "fixed, changed"), 0 rejected, 0 deferred. Open points are at the end.

## Platform review

| # | Sev | Status | Where, and what |
|---|---|---|---|
| P1 | blocker | fixed | 2.4: `build` removed from `c/`, `d/`, `q/`; `hash` over `c/` + `d/` bytes; `build` over all files except manifest, index, plan, plus `css:` and `js:` lines. |
| P2 | major | fixed | 6.6, 9.6: the page loads the corpus (`Content.text`) and posts `{t: "load", data}`; `url` form deleted; `{t: "error"}` and the fallback line added. |
| P3 | major | fixed | 3.2 (details under the table): every `Content` fetch uses `cache: "no-cache"`; files of chapters whose `hash` changed are dropped and the open part reloads. |
| P4 | major | fixed | 2.7 (`url` in `publish-plan.json`, from `site-published.json`), 2.4 (`artifactUrl`), 12 (single build goes to the same artifact; never a second artifact). |
| P5 | major | fixed | 5.4 (`Store.snapshot` shape, `Store.init` merges the hot copy), 3.7 (`App.snapshot` with `v: 1`, plain JSON), 9.4 (stub mode `hot`, `__saaRepublish`), 9.2 (`#t.hot`). |
| P6 | major | fixed | 5.2 (`root.updatedAt`), 5.3 (a document with `updatedAt: 0` never wins), 5.4 (defaults have 0; only `patch`/`replace` change it), 5.5 step 5 (`lastSeenAt` write leaves `updatedAt`), 9.1 (test case). |
| P7 | major | fixed | 3.7 step 4 (`permissions.state("db")` decides: attach now, or wait for the "Save online too" click), 5.4 (`Store.consent`), 5.6 (rows for `prompt` and `denied`), 9.4 (stub mode `consent`), 12. |
| P8 | major | fixed, changed | 3.6, 4.2, 4.4: gutter on `.shell` and `.top`, fixed layers use the variable; two-row phone header with the short brand; `--top-h` set in CSS. Variation: `#saa-sync` moved to the top of the main column at every width (one place, simpler than two). Phone `home` shot on the contact sheet (9.3). |
| P9 | major | fixed | 4.2 (overflow-wrap rules, wrapping control rows, `.cells` grid, no `overflow-x: hidden`), 9.2 (second `render-all` run at 400x860 with the width asserts; `phone` in the result JSON), 9.5 (`WL02` extended). |
| P10 | major | fixed | 4.2 (hanging margin inside the padding box of `.sec`; end padding for focus rings), 9.6 (`content-visibility` on `.sec` only, `contain-intrinsic-size: auto 40rem`, with permission to drop it). |
| P11 | major | fixed | 5.4 (`Store.importAll`), 8.5 (Restore progress: file input and paste fallback), 5.6 (rows mention it), 9.1 (round-trip test). |
| P12 | minor | fixed | 2.5, 2.6: `<`, ` `, ` `; sprite inner markup; new lint code `WL09` for `</script` and `<!--`. |
| P13 | minor | fixed | 3.7: `data || {}`, runs once, each step in `try/catch`, the "could not start" line. |
| P14 | minor | fixed | 5.5: error callbacks on `onSnapshot`; `resource_exhausted` separated from `quota_exceeded`; known-path set skips `get()`; `transform_error` listed. |
| P15 | minor | fixed | 5.4: `storage` event and re-read before save. |
| P16 | minor | fixed | 5.5 step 2: backup to `saa1:bak:<old uid>` and merge back. |
| P17 | minor | fixed | 6.1 (`promptBytes` in UTF-8 bytes via `U.bytes`; empty turns dropped), 6.2 (Ask `cache: false`; blank text disables Send; About line after `hide`), 6.3 (three more codes). |
| P18 | minor | fixed | 8.5: all `downloads` codes, `status` other than `saved`, `Blob` and the empty-blob refusal. |
| P19 | minor | fixed | 7.2: ids `q-<qid>-o-<option id>`, `q-<qid>-unsure`, group name `q-<qid>`; `QView.review` renders no input and no id. |
| P20 | minor | fixed | 2.5 (`WB06` completeness and undefined-variable checks, `runtime` list), 4.1 (`dg-ground` alias), 9.3 (`home.phone.forced-light.png`), 2.6 (`index-forced-light.html`). |
| P21 | minor | fixed | 4.4 (tabs wrap; `.pop` 70% of a fixed layer `#saa-pop-layer`; own safe-area padding of full sheets and drawer), 4.2 (layer order, toast above the exam bar), 9.5 (`WL02` any `vh`). |
| P22 | minor | fixed | 4.2 (`scroll-margin-top`), 5.2 / 10 / 3.7 / 9.6 (resume and hot snapshot store `{sid, off}`). |
| P23 | minor | fixed | 3.4, 3.5, 3.7: each capability sets its slot and emits `caps` when it settles; attach waits only for `user`, `db`, `permissions`. |
| P24 | minor | fixed | 2.5, 3.6, 4.4: slot `{{toc}}` for `#saa-toc`; `.static-toc` in the first frame, hidden from 760px; drawer closed by CSS alone. |
| P25 | minor | fixed | 3.3: state first, hash write in `try/catch`, own `hashchange` ignored. |
| P26 | minor | fixed | 4.2 (hanging margin from 1280px; tabs above the block below it), 9.3 (`prose.mid.light.png` at 1100x800). |

## Implementer review

| # | Sev | Status | Where, and what |
|---|---|---|---|
| I1 | blocker | fixed | 3.1 (`SafeHtml`, `U.raw`, `U.set`; every `html` argument or result is `SafeHtml`), 3.2 rows 1, 7, 8, 21, 9.5 (`WL05`: no `innerHTML` outside `util.js`). |
| I2 | blocker | fixed | 10 (mount table and contract: `ctx` shape, cleanup, synthetic-part mapping, new mount `tasks`, who creates `return`, unregistered mount hidden), 3.2 row 10 (`Reader.runMount`). |
| I3 | blocker | fixed | 2.3 / 2.4 (row `[sid, part, kind, route, minutes, title, parent, role]`, kind 0 never counted), 3.2 (`Content.routeSections`, `Content.progress`, the only counters), 10 (a `.sec` with an on-route `.sub` is never collapsed; collapsed sections cannot become read). |
| I4 | blocker | fixed, changed | 3.2 (`U.now`, `U.nowMs`, `Test.clock`, `Test.states`, `Cards.render`, `Speak.render`), 5.4 (`Store.load`, `Store.reset`), 9.1 (`load(files, globals?)`), section 0 (time units). Variation: the lint code for `Date.now` is `WL10`, because `WL09` went to P12. |
| I5 | major | fixed | 5.2 (root shape with `updatedAt`; `saa1:settings` holds the root; `Store.get("settings")` is `root.settings`; every state document has `updatedAt`), 5.5 (outbox key `.`). |
| I6 | major | fixed, changed | 5.2 (local document `ui`: `route`, `t`, `pos`, `seen`, `tab`), 5.4, 3.2, 3.3, 8.2, 10. Variation: `pos` holds `{sid, off}`, not `{sid, y}` (P22). Drafts, uid and outbox also only through `Store` (`Store.draft`). |
| I7 | major | fixed | Same change as P1; `manifest.date` from the latest `updated` date, else `book.snapshot_date` (2.4). |
| I8 | major | fixed | 1.2: `manifest.json` 500 KB (warn 300), `qindex.json` 300 KB (warn 200). Sections stay in the manifest, so `Content.section` stays synchronous. |
| I9 | major | fixed | 2.3 (helper returns `facts`, `terms`, `figures` per section), 2.4 (`secs` in `c/<slug>.json`; role in the manifest row), 6.1 (`askContext` reads them). |
| I10 | major | fixed | 2.4 (S keeps `pack`; `qindex.json` gets the speak index `s`), 3.2 (`Content.sindex`), 6.4 (`#speak` drawn from it). |
| I11 | major | fixed | 3.3 (`#attempt.<id>`), 3.2 (view `attempt`, owner C), 7.3 and 7.4 (go there after the end; intro always for `#mock.<n>` without a running exam; trimmed and unknown attempts), 8.3. |
| I12 | major | fixed, changed | 2.3 (rules for generated Markdown: title, unflagged H2, dropped marker line; region tables forced to kind `exam-english`), 2.2 (`data/exam-english.json` no longer read). Variation: I kept parsing `exam-english.md` and did not switch the `words` part to JSON, to keep section 0 unchanged. |
| I13 | major | fixed, changed | 2.2 (`mock.json` loaded; `WB05` when missing; synthetic `mock-preview` in every `--preview` build without mocks, domains overwritten 20/17/15/13), 7.4 ("not written yet"), 9.2 (half = first `floor(n/2)`; asserts from data; "no mock" passes 0/0). Variation: its minutes come from new `shell.json` `previewMockMinutes`. |
| I14 | major | fixed | 2.1: severity of every `WB` code; `WB03` is a warning when the target chapter is not built in this run. |
| I15 | major | fixed | 2.2 (verified items of a draft chapter in a `--preview` build), 2.8 (banner text). |
| I16 | major | fixed | 5.2 (drill document and DQ shape, plain text only), 7.1 (`validQuestion(dq)`), 7.2 (`QView` never reads `_h` of a question that is not from `Content`). |
| I17 | major | fixed | 3.2 (`U.bstrip`, markup and state classes), 4.3, 7.4, 8.2, 10. |
| I18 | major | fixed | 7.1 (`buildMix`, `mistakes` rows, `scoreAttempt` meta, `buildCoach` state), 5.2 (the coach document in full). |
| I19 | major | fixed | Same change as P3 (3.2). |
| I20 | major | fixed, changed | 0, 1.2, 8.5: `.zip` allowed in `exports/`; the row text for the Anki zip. Depends on `exports.py` writing `exports/SAA-C03-anki.zip` (see open points); until then Get files names the deck as laptop-only. |
| I21 | minor | fixed | 2.3: job terms `{id, cs, forms}`; former names are not forms. |
| I22 | minor | fixed | 3.4 (`attempt` from Store only; `caps` per capability), 6.4 and 8.2 (Speak is the only writer of the speak stamp). |
| I23 | minor | fixed | 3.2 (`Router.start({hash, view})`, `Router.current()` with `hash`; `Quiz.snapshot`, `Exam.snapshot`, `Reader.position` removed), 3.5, 3.7. |
| I24 | minor | fixed | 8.4 / 2.4 (`examFacts` keyed `count`, `minutes`, `pass`, `esl`), 7.4 (label from the `esl` fact; `extraMinutes` is only the timer value). |
| I25 | minor | fixed | 2.4 (T gets `sec`, `careful`, keeps `template`; C gets resolved `sec`), 10 (Lab template line). |
| I26 | minor | fixed | 2.4 (manifest `traps` map), 7.2 ("See the trap"), 2.3 (`data-gist` label, `data-twins` link "Practise this pair"). |
| I27 | minor | fixed | Same change as P12. |
| I28 | minor | fixed | 7.6 (term cards are Anki-only), 2.4 (C keeps `word`, `speak`). |
| I29 | minor | fixed | 10 (Reference list in `#saa-toc`), 3.6 (`aria-current`). |
| I30 | minor | fixed | Same change as P19 (the id form of P19 was taken). |
| I31 | minor | fixed | 2.4 (lower case, more words, `opt: null`), 7.2 (chip question left out for `null`). |
| I32 | minor | fixed | 2.4: `order` holds slugs; sources of `domains` and `minutes` for a planned chapter. |
| I33 | minor | fixed | 2.3 (`.pr` extent, `.lede` rule), 10 (skim also shows `.pr-q`, `.bf`). |
| I34 | minor | fixed | 2.5: missing source file is a `WB02` warning in a preview build, an error otherwise. |
| I35 | minor | fixed | Same change as P5: stub mode `hot`, `__stub.reset()`, `#t.hot` (9.2, 9.4). The hot value is kept in `sessionStorage` (platform version). |
| I36 | minor | fixed | 7.4, 4.3, 3.6: `.ex-grid` inside `#saa-view`. |
| I37 | minor | fixed | 4.1: `color` renamed `themed`; `dg-ground` defined (as an alias of `--surface`). |
| I38 | minor | fixed | 2.3: link forms for `sources.md`, generated files, `../glossary.md`, `../facts/<service>.md`. |
| I39 | minor | fixed | 3.3, 11: `#toc` is an action, not a view. |
| I40 | minor | fixed | 5.2 (`tries`, `self` as a five-character string, `seconds`), 3.4 (`speak:done`). |
| I41 | minor | fixed | 3.2: `null` for planned or absent, reject with `{path}` after `content:error`, the retry line; `Content.section` returns an object. |
| I42 | minor | fixed | 2.3 (`.dg-cmp`, `--dg-w` on `.fig-img`), 4.4 (selector), 9.6 (zoom clones the first child). |
| I43 | minor | fixed | 3.3 (order of the `#saa` click handler; others call only `Evidence.register`), 3.2 row 10, 11 (C and E no longer call `Reader.mountHtml`, except `selftest.js`). |

## Open points (nothing blocks the implementers)

1. `exports.py` must write `exports/SAA-C03-anki.zip` (I20). It is outside this contract; the app works without it.
2. The fact id `exam-esl-accommodation` in `shell.json` `examFacts.esl` is a guess, like the other three ids; the orchestrator corrects ids, keys stay.
3. P8: `ARTIFACT-RULES.md` says the gutter is set once on one wrapper; the sticky header now also has `padding-inline: var(--gutter)`, as the platform reviewer asked. To be confirmed by the phone screenshot.
4. P7: what `permissions.state("db")` answers on the real platform is unknown until the first publish (section 12 asks the orchestrator to note it). Both answers are handled.
5. New names that implementers must know: slot `{{toc}}`, `#saa-pop-layer`, `Store.consent`, `Store.draft`, `Store.importAll`, `Store.load`, `Store.reset`, `Content.text`, `Content.sindex`, `Content.routeSections`, `Content.progress`, `U.set`, `U.now`, `U.nowMs`, `U.bytes`, `U.bstrip`, `Reader.runMount`, mount `tasks`, view `attempt`, lint codes `WL09`, `WL10`, `shell.json` `previewMockMinutes`, selftest groups `phone` and `hot`.
6. Not checked by any tool: the document was edited by hand and read for consistency with a search for the old names; no build or lint exists yet to run against it.
