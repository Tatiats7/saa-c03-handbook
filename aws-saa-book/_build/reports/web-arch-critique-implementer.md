# Web architecture contract: critique from the implementers' side

Reviewed: `tools/web/ARCHITECTURE.md` version 1.0 (2026-10-04), read as implementer A, B, C, D and E in turn.
Checked against: `RULINGS.md`, `ARTIFACT-RULES.md`, `CONVENTIONS.md`, `CONVENTIONS-2.md`, `SPEC.json`, the schemas, `PRODUCT.md` sections 2, 3 and 7, `LEARNING.md` 5.3 and 5.4, `TOOLS.md`, `TOOLS-items.md`, `TOOLS-diagram.md`, the capability type files, the fixture book, and the existing code in `saalib/common.py`, `saalib/diagram/` and `saalib/lint.py`.

Counts: 4 blockers, 16 majors, 23 minors.

Severity: **blocker** = two implementers will write code that does not fit together, or one cannot write a required part at all. **major** = a feature breaks, a build fails later, or data is lost. **minor** = an ambiguity with a cheap fix.

What I checked and found correct (no finding): every Python function the contract names exists with that name (`pipeline.check_id`, `pipeline.caption`, `svg.render_inline`, `svg.used_icons`, `svg.inline_css`, `preview._chrome` with the stated signature, `lint.section_id`, `lint.anchor`, `schemas.validate`, `common.BUILD`, `TMP`, `REPORTS`, `emit`, `load_book`); `saa.py` loads `saalib/site.py` by itself; the db paths have the right segment parity and the three rules are valid under `db.d.ts`; every `sample` error code of `sample.d.ts` has a row in 6.3; the eleven callout keys match `SPEC.json` `callouts.labels`; the thirteen table kinds match `SPEC.json` `tables.kinds`; the seven prompt keys match `prompts.labels`; no P0 feature of `PRODUCT.md` section 2 is missing except X1 (finding 20).

---

## Blockers

### 1. `U.h` and `U.raw` have no defined type, and the rule of 3.1 makes composition impossible

- **Place:** 3.1 (rule 4), 3.2 row 1 (`U.h`, `U.raw`), 3.2 rows 7, 8, 21 (`Pop.open(anchorEl, html)`, `Evidence.card(fact) -> html`, `AI.notice() -> html`), 9.5 `WL05`.
- **Wrong:** The contract does not say whether `U.h` returns a string or an object. Every implementer B to E uses it, and passes "html" to each other. If it returns a string, then `U.h` inside `U.h` escapes the inner result, because 3.1 allows `U.raw` only for `_h` fields and `parts[].html`. If it returns an object, `Pop.open` and `Reader.mountHtml` must know that. `WL05` also rejects `el.innerHTML = html` when `html` is a variable, and that is exactly what `Reader.mountHtml(el, html, facts)` and `Pop.open` must do.
- **Change:** In 3.2 row 1 write: "`U.h` returns a `SafeHtml` object (`{__safe: true, s: string}`, `toString()` gives `s`). An interpolated `SafeHtml`, or an array of `SafeHtml`, is inserted without escaping; every other value is escaped as text; `null`, `undefined` and `false` give an empty string. `U.raw(string) -> SafeHtml`. `U.set(el, safe)` is the only code that assigns `innerHTML`; it throws on a plain string." In 3.1 replace rule 4's last sentence by: "`U.raw` may wrap only `_h` fields, `parts[].html`, `figures` markup and the search worker's snippet. Every function of 3.2 that takes or returns `html` takes or returns `SafeHtml`." Replace the `innerHTML` clause of `WL05` by: "`innerHTML`, `outerHTML` or `insertAdjacentHTML` outside `util.js`".

### 2. The mount contract between the reader (B) and C, D, E is not defined

- **Place:** 2.3 (synthetic parts, the three `mount` rows), 3.2 row 10 (`Reader.registerMount(name, fn(el, id, ctx))`), 7.3 (mounts `quiz`, `return`), 10 ("Parts"), 11.
- **Wrong:** (a) `ctx` has no shape, so C, D and E do not know how to get the slug, the part, the chapter file or the `d/` file. (b) The mapping from a synthetic part key to a mount name is only implied (`do` to `task`, `say` to `speak`, `quiz` to `quiz`, `sources` to `sources`), and for `do` it is not said whether B calls `task` once per task or once for the part. (c) No row of the mapping table emits `data-mount="return"`, so nobody creates the element that C fills. (d) A mount has no way to stop its timers when the part is left (the speak timer). (e) There is no function to run a mount, which the selftest needs (finding 4).
- **Change:** Add to section 10: "`ctx` is `{slug, part, meta: Content.meta(slug), chapter: <c file>, data(): Promise<d file>, route: 'fast'|'pass'|'full', hot: object|null}`. `fn` may return a cleanup function; the reader calls it before the part leaves the DOM. Synthetic parts: the reader renders `<h1>` and then one `<div class="mount" data-mount="M" data-id="">` and runs the mount: `do` uses `tasks` (new mount, B: all Try and Lab tasks, each drawn with the same code as `task`), `say` uses `speak` (id = the speak id of the route, or empty for all), `quiz` uses `quiz`, `sources` uses `sources`. The reader adds `<div class="mount" data-mount="return"></div>` as the first child of the `fast` part of every chapter with tier deep, medium or light. A mount name that is not registered leaves the element empty and hidden." Add to 3.2 row 10: "`Reader.runMount(name, el, id, ctx) -> cleanup|undefined`".

### 3. "Sections on the route" has no single definition, and the default route hides the deep part

- **Place:** 2.3 (H2, H3 and "Other H3" rows; "Each `sections` entry"), 2.4 (`sections` rows), 8.3 (Coverage), 10 (Route switch, Read tracking, Contents).
- **Wrong:** Three parts compute "sections read of sections on the route": the reader header and the contents list (B) and the dashboard (D). The rule exists only as prose, and it has three holes.
  1. The manifest rows have `level` 2 or 3, so plain H3 headings (`Traps`, `A-list`, `B-list`, `Shelf or crate`) are rows too. Read tracking exists only on `.sec` and `.sub`, so those rows are never read and no chapter reaches 100%. If A leaves them out instead, `Content.section(slug, 'traps')` is null and the selftest check "every `a.xr` resolves" fails for a link or an item `section` that points to such a heading.
  2. Every H2 of `2-deep.md` has `route=full`. On the Pass route, which is the default, "How it works" is `.is-offroute` and "collapsed to its heading", and the Pass subsections inside it are collapsed with it. The reader then shows nothing of the deep part on the default route.
  3. It is not said whether a collapsed (`.is-offroute`, `.is-gated`) section can become read through its sentinel.
- **Change:** In 2.4 make the row `[sid, part, kind, route, minutes, title, parent, role]` with `kind` `2` (H2 section), `3` (tracked subsection) or `0` (plain H3: a link target only, never counted). Add to 3.2 row 2: "`Content.routeSections(slug, route) -> rows`: rows of kind 2 or 3 whose route is at or below `route`, minus every kind 2 row that has kind 3 children (the children are counted instead). `Content.progress(slug, route, progress) -> {read, total}`. B and D use only these two for every count." In section 10 add: "A `.sec` that holds at least one on-route `.sub` is never collapsed; only its off-route `.sub` children are. A collapsed section has no sentinel and cannot become read."

### 4. The selftest and the shot states call functions that no module provides

- **Place:** 9.1 (`harness.mjs`, `test_util.mjs`), 9.2 (`#t.render-all`, `#t.exam-sim`), 9.3 (shot states), 3.2 rows 1, 5, 10, 15, 22.
- **Wrong:**
  1. `#t.render-all` must render "every card, speak item and task", but `cards.js` and `speak.js` expose views only, and the task mount cannot be called (finding 2).
  2. `#t.exam-sim` runs the real `Exam` code "with an injected clock". No clock function exists; each module would call `Date.now()` itself. The unit of `now` in `Scoring.record(…, now, …)` is also not stated (seconds or milliseconds).
  3. A shot state "fills the stub store as needed", but `Store` has no function to load documents, and `WL06` forbids `localStorage` outside `util.js` and the stub. The selftest also needs an empty store on every run.
  4. `test_util.mjs` must "load `router.js` with a stub `location`", but `load(...files)` gives a context with "nothing of the DOM" and takes no globals.
  5. `Test.shots` is named in 3.2 and never described.
- **Change:** Add to 3.2: row 1 "`U.now()` (whole seconds) and `U.nowMs()`, both read `SAA.Test.clock` when it is set; no other module calls `Date.now()` or `new Date()` without an argument (new lint code `WL09`). `Test.states` is the map filled by `Test.register`; `Test.clock = null|function`." Row 5 "`Store.load(docs)` (preview only: replaces the documents in memory, clears the outbox, writes nothing) and `Store.reset()`." Row 15 "`Cards.render(el, card, {flipped})`". Row 22 "`Speak.render(el, item, {facts, step})`". In 9.1: "`load(files, globals?)`: `globals` are copied into the context before the files run." In 5.2 and 7.1 state: "every time is whole seconds from `U.now()`, except `ms`, `activeMs` (milliseconds)."

---

## Majors

### 5. The `root` document and the `settings` document are two shapes with one name

- **Place:** 5.2 (table row `root`; the `// settings` block), 5.3 (`Merge.doc("exam")` and `"root"`), 5.4 (`Store.get` names, `Store.patch("settings")`), 5.5 (outbox keys).
- **Wrong:** The db document is `root` = `{v, createdAt, lastSeenAt, settings}`, the localStorage key is `saa1:settings`, and the Store name is `settings`. `Merge.doc("root")` takes "the document with the later `updatedAt`", but `root` has no `updatedAt`. The outbox key of the root is the empty string, because keys are "relative to `study/<uid>`". `qstats` and `speak` also show no `updatedAt`, although `Store.patch` "sets `updatedAt`".
- **Change:** In 5.2: "`root` is `{v, createdAt, lastSeenAt, updatedAt, settings}`; `saa1:settings` stores the whole root; `Store.get('settings')` returns `root.settings`; `Store.patch('settings', p)` patches `root.settings` and sets `root.updatedAt`. Every state document has `updatedAt`." In 5.5: "the outbox key of the root is `.`".

### 6. Three owners write the localStorage key `saa1:ui` and its shape is not defined

- **Place:** 3.2 (text under the table: Router "stores the route in `saa1:ui`"), 3.3 (empty hash, `lastRoute`), 8.2 card 8 (`saa1:ui.seen`), 10 (Resume), 5.2 `progress.last`.
- **Wrong:** `U.ls.set(key, value)` replaces the whole value, so the router, the reader (both B) and Today (D) overwrite each other's fields. "`lastRoute` younger than 12 hours" can be read from `saa1:ui` or from `progress.last` (which has `t` but is written only on a section change). `saa1:uid` and `saa1:drafts` are also outside `Store`.
- **Change:** Add a local-only Store document: "`ui` (localStorage `saa1:ui`, never sent to db): `{route: hash, t: seconds, pos: {'<slug>.<part>': {sid, y}}, seen: {'<slug>': '<status>:<rev>'}, tab: {}}`. Written only through `Store.patch('ui', …)`. The empty hash restores `ui.route` when `U.now() - ui.t < 43200`. `progress.last` is for Today's 'Continue reading' card and for Claude only." List `ui` in `Store.get` names and in 5.4.

### 7. `build` is defined in a circle, and it makes every file change on every build

- **Place:** 2.4 (`build`, `hash`, `"build"` inside `c/`, `d/`), 2.5 (boot JSON), 2.7 (`changed`), 2.1 ("no timestamps anywhere").
- **Wrong:** `build` is the hash over "all other emitted files", but `c/<slug>.json`, `d/<slug>.json` and `index.html` contain `build`. If A resolves the circle by any order of computing, each `c/` and `d/` file still changes whenever any other chapter changes, so `publish-plan.json` marks every file `changed` and `chapters[].hash` changes for untouched chapters. `manifest.date` has no source; `common.today()` would break "the same inputs give the same bytes".
- **Change:** Remove `build` from `c/`, `d/` and `q/` files. "`build` = first 10 hex characters of SHA-256 over the sorted `path:sha256` lines of every emitted file except `manifest.json`, `index.html` and `publish-plan.json`; the inline script and CSS text are hashed as two extra lines `js:…`, `css:…`. `manifest.date` = the latest `updated` front-matter date of the built chapters, else `book.snapshot_date`."

### 8. The budgets of `manifest.json` and `qindex.json` fail on the full book

- **Place:** 1.2 (150 KB and 120 KB, "fail above").
- **Wrong:** A deep chapter has about 30 section rows of about 110 bytes (assertion headings have 5 to 14 words), chapter 45 has 24 H2 sections, and there are 53 chapters: the `sections` arrays alone are 120 to 170 KB, before chapter metadata (about 30 KB) and `terms` (about 20 KB). `qindex` has about 800 questions at about 70 bytes plus about 100 bytes of `wrong` each: about 135 KB. Both builds pass on the fixture and fail in a late wave.
- **Change:** `manifest.json` 500 KB (warn 300 KB); `qindex.json` 300 KB (warn 200 KB). If the manifest must stay small, move `sections` to `sections.json` loaded after first paint; then `Content.section` becomes async, which changes B, C, D and E, so decide it now.

### 9. `AICore.askContext` needs data that no emitted file holds

- **Place:** 6.1 (`askContext`), 2.3 (helper result), 2.4 (`c/<slug>.json`, manifest rows).
- **Wrong:** `[summary]` needs the sections "with role `breath`, `signals` and `recap`", but the manifest row has no role (the helper has it and A drops it). FACTS, GLOSSARY and `[figures]` need "the facts, terms and figures linked in the section", but the helper returns those lists per part, and `c/<slug>.json` has only chapter-wide maps. `aicore.js` is pure and cannot read the DOM.
- **Change:** The role goes into the manifest row (finding 3). Add to `c/<slug>.json`: `"secs": {"<sid>": {"facts": [ids], "terms": [ids], "figs": [ids]}}`, and make the helper return these lists per section (`sections[].facts`, `.terms`, `.figures`).

### 10. `#speak` cannot list the speaking pack or the prompts of all chapters

- **Place:** 2.4 (S: "without `status`, `rev`, `pack`"), 6.4 (last paragraph), 8.2 card 6.
- **Wrong:** The 30 pack items live in their own chapters with `pack: true`; chapter `speaking-pack` holds only its 6 cross-service items. The build strips `pack`, so E cannot find the pack. "Per chapter, the prompts with their last band" needs the speak items of every chapter, which means one `d/` fetch per chapter (about 50) because there is no speak index.
- **Change:** Keep `pack` in S. Add to `qindex.json`: `"s": {"<speak id>": [slug, kind, pass_route (0|1), pack (0|1), prompt]}` (about 100 prompts, under 20 KB), and `Content.sindex()`. 6.4: "`#speak` lists the entries with `pack` 1, then all entries by chapter in study order."

### 11. There is no route to the results of an earlier attempt

- **Place:** 3.3, 7.3 (results page), 7.4 ("Results of an earlier attempt open from the dashboard"; "`#mock.1` … decided by state"), 8.3 ("linking to results").
- **Wrong:** D must link each attempt "to results" and C must show them, but no hash addresses an attempt. After Submit the `exam` document is cleared, so it is also undefined whether `#mock.1` then shows the intro or the last results.
- **Change:** Add to 3.3: "`#attempt.<attempt id>` | Results and review of one attempt | C" (attempt ids match `[a-z0-9-]+`). 7.4: "After Submit the page goes to `#attempt.<id>` with `replace`. `#mock.<n>` without a running exam always shows the intro, with a line 'Last result: 72% on <date>' that links to the attempt. An attempt without `answers` (trimmed) shows the summary and 'The answers of this attempt are no longer stored on this device.'"

### 12. The generated Markdown parts do not fit the mapping table

- **Place:** 0 ("`sheet.md`, `exam-english.md` … are parsed like hand files"), 2.2 step 1, 2.3 (H1, H2, table rows).
- **Wrong:** `TOOLS-items.md` section 6: a generated file "has no front matter", its H2 headings have no section flag and no time box, and `exam-english.md` prints tables of kind `plain`, not `exam-english`. So `parts[].title` has no source (the H1 is dropped and reads "<title>: …"), and `data-role`, `data-route`, `data-min` are undefined for every `.sec` of the `sheet` and `words` parts. These rows also enter progress counts. `data/exam-english.json` is loaded in step 1 and no emitted file uses it.
- **Change:** Add to 2.3: "A generated Markdown file: part title = the H1 text after the last `: `, with the first letter in upper case, else the manifest `files[].title`. An H2 without a flag gives `data-role="sheet"`, `data-route` = `full`, `data-min="0"` and no `.tbox`; its row has kind `0` (not counted in progress). The line `<!-- generated by saa.py; do not edit -->` is dropped." Either remove `data/exam-english.json` from step 1, or state its use (the `words` part is then built from it and `exam-english.md` is not parsed; this is the simpler choice, because it also works before `sync` ran).

### 13. Mocks: missing input, missing fallback, and a selftest that fails on the real book

- **Place:** 0 ("Mocks"), 2.2 step 1, 2.4 (`mocks`), 7.4, 9.2 (`#t.exam-sim`).
- **Wrong:** (a) Step 1 does not load `data/<NN-slug>/mock.json`, and nothing says what happens when a mock chapter is not planned but `mock.json` does not exist yet. (b) The synthetic mock exists only when `book.fixture` is true. The real book has no mock until wave 13, so `web selftest` fails `sim` on the real book for most of the build. (c) The synthetic mock cycles 4 fixture questions "with domains in the split of `book.domain_split`", but a cycled question keeps its own `domain`; C's script ("all correct in domain 1, …") and its asserts depend on what A does. (d) "Half in domain 3" of 15 questions is 7 or 8.
- **Change:** 2.2: "A mock chapter enters `manifest.mocks` only when `mock.json` exists and validates; otherwise `WB05`. In a `--preview` build with an empty `mocks` list (fixture or not), synthesise `mock-preview`: 65 copies of ready chapter questions with ids `preview-q001` to `preview-q065`, `pool` `mock`, `ch` `mock-preview`, and `d` overwritten in order: the first 20 get 1, the next 17 get 2, the next 15 get 3, the last 13 get 4. Never in a build without `--preview`." 7.4: "`#mock.<n>` with no such entry shows 'Mock exam <n> is not written yet.'" 9.2: "half = the first `Math.floor(n / 2)` questions of the domain in exam order."

### 14. The severities of the `WB` codes are incomplete, and a link into an unbuilt chapter can fail the build

- **Place:** 2.1 (codes `WB01` to `WB10`), 2.3 (fact link, section link: "`WB03`"), 2.2 step 2 (`--only-ready`).
- **Wrong:** Only `WB04`, `WB05`, `WB09` and `WB10` state a severity. `WB03` is raised when a link "does not resolve"; with `--only-ready` every link from a ready chapter into a draft chapter does not resolve, and so does every link into a planned chapter. If A makes `WB03` an error, the first real publish fails; if a warning, real broken anchors pass.
- **Change:** 2.1: "Errors (exit 1): `WB01` above the fail budget, `WB02`, `WB06`, `WB07`, `WB03` when the target chapter is built in this run or the fact id does not exist. Warnings (exit 2): `WB01` above the warn budget, `WB03` when the target chapter is not built in this run (the link text stays, without a link) or the fact exists and is not verified, `WB04`, `WB05` for a draft chapter, `WB09`, `WB10`. `WB08` exits 5."

### 15. A draft chapter ships no practice, although the banner says it does

- **Place:** 2.2 ("Only items with `status: ready` are emitted"), 2.8 (draft banner: "questions may change").
- **Wrong:** Items become `ready` late (questions after `verify-questions`; mock questions in `mocks assemble`). A chapter that is `draft` in the ledger (statuses `facts-verified`, `drafted`, `reviewed`) usually has only `candidate` or `verified` items, so its `do`, `say` and `quiz` parts do not exist. The pilot chapter then cannot be tested in the app before `finalize`, and the banner text is false.
- **Change:** 2.2: "In a draft chapter of a `--preview` build, items with status `verified` or `ready` are emitted, and questions also need `verification.status` `pass` or `edited-pass`. In every other build only `ready` items are emitted." 2.8 draft banner: "Draft: not reviewed yet. Facts are linked to AWS sources. Practice questions appear when the chapter is ready."

### 16. Drills written by Claude: two shapes, and one of them would trust HTML from the database

- **Place:** 5.2 (drills: "`PRODUCT.md` section 3 (read only)"), 7.1 (`Scoring.validQuestion`: "has the Q shape"), 2.3 ("Every field with `_h` is safe HTML made by the build"), 8.2 card 9.
- **Wrong:** `PRODUCT.md` gives an inline drill item the source shape (`explanation`, options with source field names). `validQuestion` demands the Q shape, which has `expl_h`, `take_h`, `why_h`. If Claude writes Q-shape items, the page inserts database text as raw HTML, which breaks the `_h` rule. If Claude writes the PRODUCT shape, `QView` cannot render it.
- **Change:** 5.2: "A drill document is `{v, title, createdAt, by, why, items: [question id | DQ]}`. DQ is `{id: 'dr-…', type, select, stem, kw: [], d, options: [{id, text, ok, why}], expl, take, facts: [ids]}`: plain text only, no `_h` field. `Scoring.validQuestion(dq)` checks this shape and exactly `select` options with `ok`; an item that fails is skipped. `QView` shows `why`, `expl`, `take` as escaped text when the `_h` field is absent, and never reads an `_h` field of a question that did not come from `Content`." Drills are P2, but the shape must be fixed now because `QView` is P0.

### 17. The blueprint strip is drawn by three implementers with no shared function

- **Place:** 4.3 (`.bstrip`, owner B), 7.4 (results), 8.2 ("Above the cards"), 10 (chapter header).
- **Wrong:** B, C and D each build the markup of `.bstrip` with "widths from domain weights". Inline `style` widths, `flex-grow` or classes are all possible, and the accuracy colouring (D) and the "domains it feeds" marking (B) need different state classes.
- **Change:** Add to 3.2 row 1 (or a new `Reader.bstrip`): "`U.bstrip(domains, opts) -> SafeHtml`; `domains` is `manifest.domains`; `opts` is `{on: [domain ids]}` or `{pct: {1: 58, …}}`. Markup: `<div class="bstrip" role="img" aria-label="…">` with four `<span class="bstrip-s" style="flex-grow:<weight>" data-d="<n>">` holding `D1` and, with `pct`, the percent as text; state classes `is-on`, `is-good`, `is-warn`, `is-bad` (thresholds from `cfg.gate`)."

### 18. `Scoring` functions that D calls have undefined arguments and results

- **Place:** 7.1 (`buildMix`, `buildCoach`, `mistakes`, `scoreAttempt`), 5.2 (`coach`: "`PRODUCT.md` section 3, with `whyCounts` keyed K, C, W, T, D"), 11 (D may call `Scoring.buildCoach`, `gate`, `mistakes`, `buildMix`).
- **Wrong:** `buildMix(qindex, qstats, read, day, n)` must pick "from chapters she has read, in study order", but it gets no study order, and `read` has no shape. `buildCoach(state, qindex, manifest)`: `state` has no shape. The coach shape of `PRODUCT.md` uses things this contract removed: `examDate` at top level, `why: "confused"`, `unreadCore` (there is no `core` any more), `weakTopics[].topic` values such as `dataprot` that are not in `SPEC.json` `questions.topics`. `mistakes()` returns "rows" without a shape, and the mistakes view needs the stem, which is not in `qindex`. `scoreAttempt(…, meta)`: `meta` has no shape, and `first` needs the earlier attempts.
- **Change:** 7.1: "`buildMix(qindex, qstats, readSlugs, order, day, n = 10)`: `readSlugs` = slugs with at least one read stamp; `order` = `manifest.order`. `mistakes()` returns `[{id, slug, d, box, last: 'wrong'|'unsure', c, t}]`; the view loads stems with `Content.questions(ids)` for the visible page of 20 rows. `scoreAttempt(questions, answers, meta)` with `meta = {id, kind, ref, startedAt, submittedAt, activeSec, limitSec, build, over, first, order}`; the caller computes `first` from `Store.attempts()`. `buildCoach({settings, progress, qstats, speak, attempts}, qindex, manifest)`." Write the coach document in 5.2 in full: `{v, updatedAt, examDate, overall: {seen, bank, accuracy, sureAccuracy, mocks: [{ref, pct}]}, domains: {d1: {acc, n}}, weakTopics: [{topic, acc, n, chapters: [slugs]}], missed: [{id, wrong, lastPick, c}], confusions: [{a, b, n}], luckyGuesses: [ids], whyCounts: {K, C, W, T, D}, unreadPass: [slugs], speakWeak: [{id, missing}]}`.

### 19. Chapter files can be stale after a republish

- **Place:** 3.7 step 3 (only the manifest uses `cache: "no-cache"`), 2.4 (`hash`), 9.6 (performance).
- **Wrong:** `c/` and `d/` files are fetched with the default cache mode. After a republish the page reloads and gets a new manifest, but the browser can serve an old `c/vpc.json`. Then section ids, fact ids and question ids of the manifest and the chapter disagree. The manifest has `hash` per chapter, and nothing uses it.
- **Change:** 3.2 row 2: "Every `Content` fetch uses `cache: 'no-cache'` (a conditional request). `Content` keeps `{path: hash}` of what it holds in memory; on the `manifest` event it drops cached files whose chapter `hash` changed, and the reader reloads the open part when its chapter was dropped, keeping `{sid, y}`."

### 20. P0 feature X1 (the Anki deck) cannot reach her from the web app

- **Place:** 1.2 (`exports/*`: "`.pdf`, `.txt` only"), 8.5 ("the `.apkg` named as laptop-only").
- **Wrong:** `PRODUCT.md` lists X1 as P0 and "never cut", and English-only vocabulary cards are one of her five requests. `downloads.d.ts` does not allow `.apkg`, but it allows `.zip` (second list, next to `pdf`). The contract gives her no way to get the deck on a phone or on another computer.
- **Change:** 1.2: "`exports/*`: `.pdf`, `.txt`, `.zip`". 8.5: "The row of a `.zip` says 'Anki deck (zip): unzip it, then open the `.apkg` file with Anki.'" Ask the owner of `exports.py` to write `exports/SAA-C03-anki.zip` next to the `.apkg`. If the orchestrator rejects this, say so in section 0, so that it is a decision and not a gap.

---

## Minors

### 21. The glossary auto-link cannot apply its own case rule
- **Place:** 2.3 (job `ctx.terms: [{id, forms}]`; row "Glossary link").
- **Wrong:** "Case-sensitive for kind `aws-name`", but the job has no `kind`. It also does not say whether `former_names` are forms.
- **Change:** `"terms": [{"id", "cs": true|false, "forms": [term, short, aliases…]}]`; "former names are not forms".

### 22. Two emitters for `attempt`, two writers for the speak tick, and `caps` waits for the database
- **Place:** 3.4, 5.4 (`Store.addAttempt` "emits `attempt`"), 6.4 step 3, 8.2 card 2, 3.7 step 4.
- **Wrong:** The table says Quiz and Exam emit `attempt`; 5.4 says Store does. Speak stamps `daily.<day>.speak` and Today "sets" the same tick on `speak:done`. `caps` is emitted after `Store.attach`, which makes network reads, so the Claude controls wait for the database.
- **Change:** 3.4: "`attempt` is emitted by Store only." 8.2: "Today only redraws on `speak:done`; Speak writes the stamp." 3.7 step 4: "set `SAA.state.caps` and emit `caps` as soon as the four `use()` calls settle; then `user.id()` and `Store.attach` (not awaited)."

### 23. `Router.start`, `Router.current` and the hot snapshot do not connect
- **Place:** 3.2 row 3 and the text under the table, 3.7.
- **Wrong:** `Router.start()` takes no argument, but boot calls it "with `data.route`", and `ctx.hot` must come from `data.view`. `Router.current().hash` is used, but `SAA.state.route` is `{view, args}`. `Quiz.snapshot()`, `Exam.snapshot()` and `Reader.position()` duplicate the `snapshot()` of the view definition. `hot.ready(SAA.App.start)` can call `start` with `undefined`.
- **Change:** "`Router.start({hash?, view?})`; `view` is passed once as `ctx.hot` to the first mount whose view name equals the snapshot's. `Router.current() -> {view, args, hash}`. `App.snapshot()` reads only `def.snapshot()`; remove `Quiz.snapshot`, `Exam.snapshot`, `Reader.position` from 3.2. `App.start(data)` treats a missing `data` as `{}`."

### 24. Exam facts are found by position, and one exam rule is a constant
- **Place:** 8.4 (`examFacts` list, `extraMinutes: 30`), 7.4 ("the pass note from `examFacts` when present"), 0 (last row).
- **Wrong:** C must find the passing-score fact among `examFacts`, but the ids can be corrected by the orchestrator, so C cannot match by id. "Add 30 minutes (ESL accommodation)" shows an exam rule from `shell.json`, which the last row of section 0 forbids (`CONVENTIONS-2.md` S: the ESL accommodation is a fact of namespace `exam`).
- **Change:** `shell.json`: `"examFacts": {"count": id, "minutes": id, "pass": id, "esl": id}`; manifest `"examFacts": {"pass": {"id", "text"}, …}` with missing keys left out. 7.4: "The checkbox label is 'Add extra time (ESL accommodation): <examFacts.esl.text>'; without that fact the label has no number. `extraMinutes` stays the timer value."

### 25. The task card needs three things the T shape does not give
- **Place:** 2.4 (T), 10 ("the cost, cleanup and careful callouts").
- **Wrong:** The `Careful` callout is `SPEC.json` `tasks.stop_rule`, which is in no emitted file. A Lab prints `**Template.**` with a repo path; the web has no such file. T keeps the raw `section` string, while Q, C and S get a resolved `sec`.
- **Change:** T gets `"sec"` resolved as in Q, and `"careful"` = `tasks.stop_rule` for Try and Lab. 10: "A Lab shows 'Template on your laptop: <template path>'." C in 2.4: "`sec` resolved as in Q".

### 26. `data-trap`, `data-gist` and `data-twins` are emitted and nothing uses them
- **Place:** 2.3 (callout, traps, prompt and comments rows), 2.4 (Q option `trap`, C `trap`).
- **Wrong:** The helper returns `traps` per part, but no emitted file maps a trap id to a place, so the `trap` of an option cannot become a link. No behaviour is defined for `data-gist` or `data-twins`.
- **Change:** Add to the manifest chapter row `"traps": {"<trap id>": "<part>.<sid>"}`; 7.2: "an option with `trap` shows the link 'See the trap' to `#ch.<slug>.<part>.<sid>`". 2.3: "`data-gist`: the label reads 'Predict 1 · careful'. `data-twins`: the section ends with the link 'Practise this pair' to `#quiz.<slug>`." Or delete the three attributes.

### 27. The escape rule of `--single` is printed wrong
- **Place:** 2.6 ("every `<` written as `<`").
- **Change:** "every `<` written as `<`, and U+2028 and U+2029 as ` ` and ` `".

### 28. `data/cards-terms.json` has no place in the site
- **Place:** 2.4 (`d/<slug>.json` cards), 7.6.
- **Wrong:** The generated term, meaning and partner cards have chapter `glossary`, which is not a chapter, so `#cards.<slug>` never shows them. C drops `word`, `speak`, `pair`, `generated`.
- **Change:** State in 7.6: "Term cards are in the Anki deck only; the app shows hand cards, word cards (chapter 01) and say cards (chapter 49)." Keep `word` and `speak` in C.

### 29. Files, About, Glossary and the three sheets have no entry point
- **Place:** 3.6 (`#saa-nav`), 10 (Contents).
- **Change:** 10: "`#saa-toc` ends with a list 'Reference': Glossary, Numbers, Traps, Changed recently (only the aliases that exist), Get files, About. B sets `aria-current="page"` in `#saa-nav` and `#saa-toc` on the `route` event."

### 30. `QView.review` puts several questions in the DOM with the same ids
- **Place:** 7.2 ("ids `opt-<i>`", "`id="q-unsure"`", "One question is in the DOM at a time"), 7.3 (results list).
- **Change:** "`QView.review` renders no form control and no `id`. `QView.render` prefixes ids with the question id: `<qid>-opt-<i>`, `<qid>-unsure`."

### 31. The `opt` table misreads common qualifiers
- **Place:** 2.4 (Q `opt`).
- **Wrong:** "MOST scalable", "LEAST downtime", "MOST reliable", "MOST highly available" (matches), "LOWEST latency" (matches) : `scal`, `downtime`, `reliab` give `none`, so the stem-first step marks a right answer wrong. Case handling is not stated.
- **Change:** "Compare in lower case. `resil` also matches `downtime`, `reliab`, `outage`, `failure`; `perf` also matches `scal`, `speed`, `quick`. When the qualifier is not `none` and no word matches, `opt` is `null` and the stem-first step skips the chip question."

### 32. `order` is called "chapter ids" and shown as slugs
- **Place:** 2.4 (`order`).
- **Change:** "`order`: chapter slugs …". Also state the sources for a planned chapter: "`domains` = the first digits of the registry `tasks`; `minutes` = the template minutes of `SPEC.json`".

### 33. The `.pr` wrapper and the `.lede` rule have open cases
- **Place:** 2.3 (prompt row, paragraph row), 10 (Skim mode).
- **Wrong:** A Spot the bug prompt can have a code block between the question and the reveal; Predict prompts have no reveal. A section that starts with a prompt, a bold field, a callout or a mount has no first paragraph, so skim mode shows nothing of Predict, Decision record or FAQ.
- **Change:** "`.pr` holds the prompt paragraph, every block up to and including the next `details`, or only the paragraph when the next block is another prompt or a heading. `.lede` is the first plain paragraph that is a direct child of `.sec-b` or `.sub-b` and comes before any other block; else there is none. Skim mode also shows `.pr-q` and `.bf`."

### 34. The build has no rule for source files that do not exist yet
- **Place:** 1.1, 2.5, 11 ("A module must load … when a later module is missing").
- **Change:** 2.5: "A missing file of 3.2 or of the CSS list is skipped with a `WB02` warning in a `--preview` build and is an error otherwise."

### 35. The stub cannot test the republish path or start clean
- **Place:** 9.4 ("`window.claude.hot` is not stubbed"), 9.2 ("an empty store").
- **Change:** "Mode `hot`: `localStorage.saaStubHot` holds a JSON value; the stub defines `hot.ready(fn)` (calls `fn` with it) and `hot.snapshot(fn)` (keeps `fn` as `window.__saaSnapshot`). The stub exposes `window.claude.__stub = {mode, db, reset()}`; `selftest.js` calls `reset()` and `Store.reset()` first." Add a third selftest route `#t.hot` (C): snapshot a running mock, restart `App.start` with it, assert the route and `cur`.

### 36. The exam answer sheet has no column on desktop
- **Place:** 3.6 ("`#saa-rail` belongs to the reader (other views hide it)"), 7.4 ("in the right column on desktop").
- **Change:** 7.4: "The exam view builds its own two-column grid inside `#saa-view` (`.ex-grid`, in `50-practice.css`); it does not use `#saa-rail`." Add `.ex-grid` to 4.3.

### 37. Tokens: two values are not colours, and the diagram stylesheet has a literal fallback
- **Place:** 4.1 (`dg-show-light`, `dg-show-dark` under "Additions"; shape `color`), `TOOLS-diagram.md` line 621 (`var(--dg-ground, var(--surface, #fff))`).
- **Change:** `tokens.json`: rename `color` to `themed` ("any value with a light and a dark form"), and add the token `dg-ground` (light `var(--surface)`, dark `var(--surface)`) so the fallback is never used.

### 38. Link forms that the mapping table does not name
- **Place:** 2.3 (row "Link to a section").
- **Change:** Add: "`sources.md` gives `.sources`; `exam-english.md` gives `.words`; `sheet.md` gives `.sheet`; `calendar.md`, `mistakes.md`, `2-services.md` through `part_of_file`. A link to `../glossary.md` without an anchor gives `#glossary`. A link to `../facts/<service>.md` without an anchor is `WB03`."

### 39. `#toc` is a route with the behaviour of a button
- **Place:** 3.3 (`#toc`).
- **Wrong:** If the router mounts a view for `#toc`, it empties `#saa-view` and the page she was reading is gone.
- **Change:** "`#toc` is not a view: `Router` keeps the mounted view, opens the drawer (phone) or focuses `#saa-toc` (desktop), and does not store the route. With no mounted view it shows Today first."

### 40. Field names in the `speak` document collide with other meanings
- **Place:** 5.2 (`speak.items`: `n`, `sec`, `self`), 3.4 (`speak:done` `self: n`).
- **Wrong:** `sec` means a section reference everywhere else; here it is probably seconds. `n` is a counter, which 5.2 forbids ("no counters except `sf`").
- **Change:** `{t, tries, self: '10110', score, band, missing: [kp], words, seconds}`; "`tries` is merged with the item (later `t` wins)". `speak:done`: `{id, self: <count of yes>, score}`.

### 41. `Content` has no stated behaviour for errors and planned chapters
- **Place:** 3.2 row 2, 3.4 (`content:error`), 2.8.
- **Change:** "`Content.chapter(slug)` and `Content.data(slug)` resolve `null` for a planned chapter or a chapter without that file, and reject with `{path}` after emitting `content:error` on a network or parse error. A view then shows 'This page could not be loaded. Check your connection and try again.' with a Retry button." State also: "`Content.section(slug, sid)` returns the row as an object `{sid, part, kind, route, min, title, parent, role}`."

### 42. Zoom and the phone scale rule assume one `<svg>` per figure
- **Place:** 4.4 (`.fig-s svg`), 9.6 (Zoom), 2.3 (figure row).
- **Wrong:** A `compare` diagram renders as `<div class="dg-cmp">` with one `<svg>` per panel and `--dg-w` on the panel `div`; a figure without a spec is an `<img>` with no `--dg-w`.
- **Change:** 9.6: "Zoom clones the first child of `.fig-s` (an `svg`, a `.dg-cmp` or an `img`)." 2.3: "`.fig-img` gets `style="--dg-w:<figures.w>"`". 4.4: "the rule is `.fig-s > svg, .fig-s .dg-cmp-p > svg, .fig-s > img`."

### 43. Global click handling and `Reader.mountHtml` overlap
- **Place:** 3.3 (last paragraph: one click handler on `#saa`), 3.2 row 10 (`mountHtml` "wires chips, terms, reveals, copy, figures"), 7.2 (`why_h` holds `a.ev`), 11 (C and E may call both).
- **Wrong:** It is not clear whether C and E must call `Reader.mountHtml` for every `_h` fragment, or only `Evidence.register(facts)`. With the global handler, a click on `a.ev` would also navigate to `#fact.<id>`.
- **Change:** 3.3: "The `#saa` handler handles, in this order: `a.ev` (opens the evidence card, no navigation), `a.term` (opens the glossary popover), `[data-act]` controls of B (`copy`, `zoom`, `describe`, `toc`, `search`, `ask`), then other `a[href^='#']` (navigation). This works in every view. Other owners call only `Evidence.register(facts)` before they insert `_h` fields. `Reader.mountHtml` is for part HTML only (it also sets up read tracking, the rail and the mounts)."
