# Platform critique of `tools/web/ARCHITECTURE.md` (version 1.0)

Reviewed against `_build/spec/ARTIFACT-RULES.md` and `_build/spec/existing/capabilities/*.d.ts` (claude, db, user, sample, downloads, permissions). Section numbers are those of the contract. The contract was not edited.

Counts: 1 blocker, 10 major, 15 minor.

What was checked and found correct (no change needed): page file without doctype/html/head/body and `<title>` first; fonts only from Google Fonts, no other external host; no print, dialogs, `<a download>`, iframes, service worker or device API; hash grammar (`[a-z0-9-]` tokens joined by `.`); the capability declaration shape; the db rule set (prefix rule `study` sets both `read` and `write`, `{self}` is the last segment, write level never below read level); path parity of every db path in 5.2 (documents 2 and 4 segments, collections 3); `update` only after an existence check; snapshots with `hasPendingWrites` ignored and never answered with a write; no timer writes to db; `sample.json` option names (`modelTier`, `signal`, `cache`), one new `AbortController` per call, no page-side timeout, turns that start and end on `user`; `downloads.save({filename, data})` with `.json`, `.txt`, `.pdf` and `.apkg` kept out; sticky header and fixed bar insets; token CSS in the three-block shape with light and dark values present for every colour of `PRODUCT.md` section 7 plus the additions of 4.1; `body` background from a token; static first frame present in the shell.

---

## Blocker

### 1. The build id is defined in a circle (2.4, 2.7)

**Place.** 2.4: "`build` is the first 10 hex characters of the SHA-256 over the sorted `path:hash` lines of all other emitted files". But `c/<slug>.json`, `d/<slug>.json` and the boot JSON of `index.html` each contain `"build"`. Chapter `hash` is the SHA-256 of `c/` plus `d/`, which also contain `build`.

**What is wrong.** The definition cannot be computed as written: the hash of a file depends on a value that depends on the hash of that file. Any way out that implementer A picks alone changes what the other four read. Also, even with a workaround, every `c/` and `d/` file changes whenever any file changes, so `publish-plan.json` marks all files `changed` on every publish and chapter `hash` is useless as a change signal.

**Change.**
- Remove `"build"` from `c/<slug>.json`, `d/<slug>.json`, `q/*.json`. Keep it only in `manifest.json` and the boot JSON.
- Define `hash` (chapter) as the first 8 hex of SHA-256 over the bytes of `c/<slug>.json` then `d/<slug>.json` (now free of `build`).
- Define `build` as the first 10 hex of SHA-256 over the sorted `path:sha256` lines of every emitted file except `manifest.json`, `index.html` and `publish-plan.json`, plus the SHA-256 of the concatenated CSS and JS text. `index.html` and `manifest.json` then carry it.
- Attempt and exam documents keep their `build` field (from `SAA.state.build`).

---

## Major

### 2. The search worker resolves `search/corpus.json` against the wrong base (6.6)

**Place.** 6.6: the worker starts from `assets/search-worker.js` and "loads `search/corpus.json`"; protocol `{t: "load", url|data}`.

**What is wrong.** Inside a worker a relative URL resolves against the worker script, so `fetch("search/corpus.json")` asks for `assets/search/corpus.json` and gets a 404. With a Blob URL worker a relative URL does not resolve at all. The contract's fallback ("if the worker cannot start, only jump-to is offered") does not cover this: the worker starts and then never becomes ready.

**Change.** One code path for both modes: the page loads the corpus through `Content.blob("search/corpus.json")` (or the inline entry) and posts `{t: "load", data: <text>}`. Delete the `url` form. Add: "if no `{t: "ready"}` arrives, or the worker posts `{t: "error"}`, only jump-to is offered". Change 9.6 "inside the worker" to "by the page, then posted to the worker".

### 3. After a republish the new shell can read old chapter files (3.7 step 3, 9.6)

**Place.** Only `Content.manifest()` uses `cache: "no-cache"`. `c/`, `d/`, `q/`, `glossary.json`, `plan.json`, `facts.json`, `qindex.json` use the default HTTP cache. Published paths are the same on every version.

**What is wrong.** The browser may serve a cached `c/vpc.json` from the previous version next to the new `manifest.json`. Section ids, fact ids and `keyRev` then disagree: links do not resolve, `qstats` records are dropped as "wrong `kr`", read stamps go to sections that no longer exist.

**Change.** In 3.2 `content.js`: "Every `fetch` of `Content` uses `cache: \"no-cache\"` (a conditional request; unchanged files cost a 304)." Do not add query strings. Add: "`Content.chapter(slug)` is refetched once when a manifest refresh shows a different `chapters[].hash` for a chapter in the memory cache."

### 4. The `--single` fallback, as written, publishes a different artifact and loses all progress (12, 2.7, 1.2)

**Place.** 12: "If multi-file fetch fails on the platform, publish the `--single` build; nothing else changes." `--single` writes `_build/site-single/index.html`.

**What is wrong.** A publish from another file path creates a new artifact unless the existing artifact URL is passed. A new artifact has a new origin (empty localStorage) and a new db (empty cloud progress). The same holds for any later publish from a moved build folder.

**Change.**
- 2.7: add `"url": <string|null>` to `publish-plan.json`, copied from `common.REPORTS / "site-published.json"` (the orchestrator stores the URL there after the first publish). `manifest.artifactUrl` takes the same value.
- 12: replace the sentence with "If multi-file fetch fails, publish `_build/site-single/index.html` **to the same artifact** (pass its `url`), with the same title and the same `capabilities`; remove the multi-file paths with `removed`. Never publish the book as a second artifact."
- 2.7: state "the first publish fixes the URL; every later publish passes it."

### 5. The republish path is never exercised, and the snapshot content is not defined (3.7, 5.4, 9.4)

**Place.** 9.4: "`window.claude.hot` is not stubbed." 5.4: `Store.snapshot()` returns "All documents". 5.4: `Store.init(hotStore)` "Loads each document from `hotStore`, else localStorage".

**What is wrong.**
- The one rule that protects a running mock on republish has no local test; its first run is in production.
- "All documents" does not say whether the attempts map, the outbox, `saa1:uid` and drafts are included. In `memory` status (storage throws) the outbox exists only in memory, so pending cloud writes are lost on a republish.
- The snapshot can be large (40 attempts with answers) and nothing requires it to be plain JSON.
- Preferring the hot copy over localStorage drops what another tab wrote.

**Change.**
- 5.4 `Store.snapshot()`: "returns `{v: 1, docs: {settings, progress, qstats, exam, speak}, outbox, uid}` plus `attempts` and `drafts` only when the status is `memory`. Plain JSON (`JSON.parse(JSON.stringify(x))` equals `x`), under 300 KB."
- 5.4 `Store.init(hotStore)`: "loads localStorage, then merges `hotStore.docs` into it with `Merge.doc` (not replace); ignores a `hotStore` whose `v` is unknown."
- 3.7 `App.snapshot()`: add `"v": 1`; views return plain JSON only.
- 9.4: add stub mode `hot`: `window.claude.hot = {snapshot(fn), ready(cb), data}`; `ready` calls `cb` asynchronously with `JSON.parse(sessionStorage.saaStubHot || "{}")`; `window.__saaRepublish()` stores `JSON.stringify(fn())` there and reloads.
- 9.2: add route `#t.hot` (owner C, with D): start mock 1, answer three questions, take `App.snapshot()`, round-trip it through JSON, call `Store.init` and `Exam` mount with it in a cleared localStorage, assert route, `cur`, `ans`, `activeMs` and the outbox are restored.

### 6. A new device can overwrite cloud settings and a running mock with defaults (5.2, 5.3, 5.5)

**Place.** 5.3: `root` and `exam` merge as "the whole document with the later `updatedAt`". 5.2: the `root` shape `{v, createdAt, lastSeenAt, settings}` has no `updatedAt`. 5.5 step 5 writes the root when `lastSeenAt` is old. 5.4 `Store.patch` "sets `updatedAt`".

**What is wrong.** On a first visit from a second browser, local defaults exist before `attach`. If defaults carry a current time (or the `lastSeenAt` write stamps `updatedAt`), the default settings win over the cloud document: `plan`, `planStart`, `examDate`, `routeBy`, `extraTime` are reset. The same race can replace a running `exam` document with `{none: 1}`.

**Change.**
- 5.2: `root` shape becomes `{v, createdAt, lastSeenAt, updatedAt, settings}`.
- 5.4 `Store.init`: "default documents have `updatedAt: 0`; `updatedAt` changes only in `Store.patch` and `Store.replace` (a user action)."
- 5.5 step 5: "the `lastSeenAt` write is `update({lastSeenAt})` (or `set` of the merged root when missing) and does not change `updatedAt`."
- 5.3: "a document with `updatedAt: 0` never wins over an existing remote document." Add this case to `test_merge.mjs`.

### 7. The first db call runs at load and may open a consent dialog before any click (3.7 step 4, 5.5)

**Place.** 3.7 step 4 calls `Store.attach(db, uid)` at boot; 5.5 step 3 does `get()` at once.

**What is wrong.** `permissions.d.ts`: "By default every capability asks the viewer lazily, at its first use." `claude.d.ts`: "a consent prompt ... arrives on the first call, never here [`use()`]". If db needs consent, the dialog appears over the first frame on every first visit, and the `get()` promises stay pending for as long as she takes to answer. The contract has no state for "waiting for consent" and no path back after a refusal.

**Change.**
- 3.7 step 4: also `claude.use("permissions")` (built in, not declared). Before `Store.attach`: `state("db")`. `granted`: attach now. `prompt`: do not attach; the status pill shows "Saved on this device only" with a button "Save online too"; the click calls `Store.attach` (the db call itself asks). `denied`: stay `local`; About offers "Open permissions" (`permissions.manage()`, on click only). `permissions` null: attach now (current behaviour).
- 5.5: "status stays `local` until step 3 resolves; the app never waits for `attach`."
- 5.6: add the row for `prompt`.
- 12: add "note whether db asks for consent on first use" to the functional pass.

### 8. The header does not fit a 400 px screen and sits outside the gutter wrapper (3.6, 4.2, 4.4)

**Place.** 3.6: `#saa-top` holds the Contents button, the brand "SAA-C03 Handbook", five nav links, the Search button and the sync pill ("Saved on this device only"). 4.2: "`.shell` is the one outer wrapper with `padding-inline: var(--gutter)`"; `.top` is a sibling of `.shell`. 4.4 has no header rule.

**What is wrong.** One row with that content is about 700 px wide: at 400 px it either overflows the page (sideways scroll of the body, forbidden) or is squeezed without a rule. `.top`, and the fixed exam bar, the toast and sheets, are outside `.shell`, so the "gutter of at least 16 px at every width" is not given to them by the contract.

**Change.**
- 4.2: "The gutter is `padding-inline: var(--gutter)` on `.shell` and on `.top`; fixed layers (`.ex-bar`, `.toast`, `.sheet`, phone `.pop`) use the same variable in their own padding."
- 4.4, new rule: "Header below 760 px: two rows, `flex-wrap: wrap`. Row 1: Contents button, brand (text `SAA-C03`; the full title stays in `aria-label`), Search button. Row 2: `#saa-nav`, five links with `flex: 1 1 0; min-width: 0`, `--fs-0`, each at least 44 px high. `#saa-sync` leaves the header: below 760 px it is a line under the header (`.sync` becomes a full-width strip in `#saa-main`), text wraps." Set `--top-h` to the two-row height in the phone block (a `static` token cannot change by width; make `top-h` a custom property set in `20-layout.css` and `90-phone.css`).
- 9.3: add the phone `home` shot to the contact sheet as the check for this.

### 9. Unbroken strings will widen the page on a phone, and no test looks for it (4.2, 9.2)

**Place.** 4.2: "`.tw`, `.code pre`, `.fig-s` are the only horizontal scroll containers." Nothing covers long tokens in running text. `web selftest` runs only at 1280x900.

**What is wrong.** The book is full of strings with no break point: inline code (`arn:aws:iam::123456789012:role/...`, `aws ec2 describe-...`), fact ids in mono, source URLs in the `sources` part and evidence cards, option text with ARNs. At 400 px one such string makes the body scroll sideways. Other likely places: `.chh-meta` ("Fast 20 min · Pass 65 min · Full 150 min"), `.rsw`, `.cells` (65 cells), `.q-nav`, `.bstrip`.

**Change.**
- 4.2: add "`.app { overflow-wrap: break-word }`; `p code`, `li code`, `td code`, `.evc-id`, `.evc-src a`, `a.ext`, `.opt`, `.q-stem`, `.srch-row` use `overflow-wrap: anywhere`. Rows of controls (`.chh-meta`, `.rsw`, `.q-nav`, `.fig-a`, `.td-min`) use `flex-wrap: wrap`. `.cells` is `grid-template-columns: repeat(auto-fill, minmax(44px, 1fr))`. Never `overflow-x: hidden` on `body` or `.app` to hide a fault."
- 9.2: "`web selftest` runs `#t.render-all` a second time at 400x860. After each part or question is mounted it asserts `document.documentElement.scrollWidth <= document.documentElement.clientWidth`, and that every element wider than the viewport is inside `.tw`, `.code pre`, `.fig-s` or `.zoom`. A failure names the chapter, part and the first offending element." Add `"phone": {"pass", "total"}` to the result JSON.

### 10. `content-visibility: auto` on `.sec` clips the hanging callout labels (9.6, 4.2)

**Place.** 9.6: "`.sec` and `.sub` use `content-visibility: auto`". 4.2: from 1100 px "`.co-l` positioned in the margin".

**What is wrong.** `content-visibility: auto` always applies paint containment, which clips everything outside the element's padding box. If `.sec` is the 66ch text column and the label hangs in the left margin, the label is cut off on desktop. Focus rings and the shadow edge of sticky table columns at the section edge are cut the same way.

**Change.** 4.2: "The hanging margin is inside the section: `.sec` and `.sub` span the main column and have `padding-inline-start: var(--margin)` from the margin breakpoint; `.sec-h`, `.sec-b` content is limited to `var(--measure)`; `.co-l` is positioned inside that padding. Sections also have `padding-inline-end: 4px` so focus rings are not clipped." 9.6: "`contain-intrinsic-size: auto 40rem`." If B finds this too costly, drop `content-visibility` (one part at a time is already in the DOM) and say so.

### 11. In `local` status the progress has one copy and no way back in (5.6, 8.3)

**Place.** 5.6 `local`: "offers ... 'Save my progress' (`downloads.save`, `saa-progress.json`)". No import exists anywhere.

**What is wrong.** `ARTIFACT-RULES.md`: browser storage is "never ... the only copy of state that matters". When db is null, not granted, or refused (finding 7), weeks of progress live only in localStorage, which a cleared browser or the phone app can empty. The export file cannot be loaded again, so it protects nothing.

**Change.** 5.4: add `Store.importAll(obj) -> {ok, counts}`: validates `v`, merges each document with `Merge.doc` and attempts with `Merge.attempts`, saves, queues the diff to the outbox, emits `store:change`. 8.5 `#about`: add "Restore progress": an `<input type="file" id="about-restore" accept=".json,application/json">` read with `FileReader`, plus a textarea "or paste the file's text" as the fallback when the file picker does not open in the frame; an inline result line ("Restored 212 answers and 3 attempts"). 5.6 `local` and `memory` rows: mention Restore. Add the round trip `exportAll` then `importAll` to `test_merge.mjs`. Owner D.

---

## Minor

### 12. Inline JSON and inline script text are not safely escaped as written (2.6, 2.5)

**Place.** 2.6: "(every `<` written as `<`)". The escape was lost in the text.

**Change.** "Every `<` in inline JSON (`#saa-boot`, `#saa-inline`) is written as `<`, and U+2028/U+2029 as ` `/` `. The worker source in `#saa-worker` and the concatenated page script must not contain `</script` or `<!--`: `web lint` rejects them in `js/*.js` (new code `WL09`). The sprite placed in `#saa-sprite` is the inner markup of `assets/icons.svg` without the XML declaration."

### 13. Boot does not survive an empty or failing hot start (3.7)

**Place.** `hot.ready(SAA.App.start)`; `App.start(data)` reads `data.store`.

**What is wrong.** If `ready` calls back with `undefined`, `data.store` throws and the app never starts. A throw in any view's `mount` during `Router.start()` also stops steps 3 and 4.

**Change.** "`App.start` begins with `data = data || {}` and runs once (a second call returns). Each of the four steps is in its own `try/catch`; a failure logs to the console and the next step still runs. If `Router.start()` throws, the static first frame stays and a line 'The page could not start. Reload to try again.' is added under it."

### 14. db subscriptions and budgets: missing error callbacks and a status that never recovers (5.5)

**What is wrong.** (a) `onSnapshot` is specified without the `error` argument; `db.d.ts` asks for it, and a dead-bridge `unavailable` ends the listener for good. (b) `resource_exhausted` (a rate budget, transient) is handled like `quota_exceeded` (permanent): status `local` with no return. (c) Each `merge` flush does `get()` then `update()`, doubling the call rate. (d) `transform_error` is not listed.

**Change.** (a) "Every `onSnapshot` passes an error callback: `unavailable` re-subscribes once after 5 s; any other code ends that listener and, for `revoked`/`not_granted`, cloud sync." (b) "`resource_exhausted`: keep the outbox, stay `cloud`, no flush for 30 s, then flush on the next user action; no toast. `quota_exceeded`: as now." (c) "`Store` keeps the set of paths known to exist (from step 3 and from successful writes); `merge` skips `get()` for them; an `update` that rejects `invalid_argument` on such a path is retried once as `get()` + `set`." (d) "`transform_error`: like `invalid_argument`."

### 15. Two tabs in one browser overwrite each other's localStorage documents (5.4)

**Change.** "`store.js` listens to the `storage` event for `saa1:*` keys: the changed document is merged into memory with `Merge.doc` and `store:change` (source `remote`) is emitted. Before each localStorage save, `Store` re-reads the key and merges." 

### 16. A different `uid` deletes local progress without a copy (5.5 step 2)

**Change.** "Move the local documents and outbox to `saa1:bak:<old uid>` (one backup, replaced each time) instead of deleting them; when `saa1:uid` later equals a backed-up id, merge the backup in." A null uid never triggers this (already so).

### 17. `sample` details (6.1, 6.2, 6.3)

- Ask uses the default cache, so "Quiz me" or "Give an analogy" pressed twice within five minutes replays the same answer. Change: "Ask calls pass `cache: false`; the Speak check keeps the default cache."
- `CAPS.promptBytes` is compared with a string length. Change: "measured as UTF-8 bytes (`new TextEncoder().encode(s).length`; in the pure module, a small byte counter)", limit stays 200000 (platform 262144).
- A turn with empty `content` rejects `invalid_request`. Change: "`AICore.askTurns` drops empty turns; the Send button is disabled for blank text."
- `images_unavailable`, `tools_unavailable`, `image_rejected` are in `SampleErrorCode` and not in the table. Change: add them to the `invalid_request` row (they cannot happen without images or tools; treat as a page bug).
- After `hide: true`, add to About, when `permissions` exists: "Claude features are off for this page. Open permissions" (`permissions.manage()` on click).

### 18. `downloads` codes (8.5)

**Change.** Add: "`unavailable`, `not_granted`, `capability_disabled`, `capability_removed`: hide every Save button for the visit and show the repo paths. `too_large`: 'This file is too large to save here. On your laptop it is at <repo path>.' `bad_request`, `transform_error`: 'The file could not be saved.' and `console.error`. A resolved `status` other than `\"saved\"` shows no notice." `Content.blob` must return a `Blob` (not text) and the row must refuse an empty blob.

### 19. Form control ids repeat on pages that list several questions (7.2, 7.3, 7.6)

**Place.** `opt-<i>` and `q-unsure` are fixed ids; results and review pages render many questions with `QView.review`, and the `return` mount can sit beside another question.

**Change.** "Ids are `q-<qid>-o-<option id>` and `q-<qid>-unsure`; the radio group `name` is `q-<qid>`. `QView.review` renders no inputs (marked list items with the words 'Correct answer' / 'Your pick')."

### 20. Token generation has no completeness check, and the third theme state is not shot (2.5, 4.1, 9.3)

**Change.** 2.5: "The build fails (`WB06`) when a `color` entry lacks `light` or `dark`, when an `alias` or `static` value holds a literal colour, or when a `var(--x)` in CSS, in `diagram css` or in an alias names a token that `tokens.json` does not define (allowed exception: `--dg-w`, `--dg-ground`, and variables set by script, listed in `tokens.json` `runtime`)." 9.3: "add `home.phone.forced-light.png`: `data-theme=\"light\"` with Chrome's dark scheme, to prove the `:not([data-theme=\"light\"])` guard." The `#fff` fallback inside `diagram css` (`var(--dg-ground, var(--surface, #fff))`) is outside `WL01`; define `--dg-ground` as an alias of `--surface` in `tokens.json` so the literal is never used.

### 21. Phone details that conflict with the rules or are left open (4.4)

- "Part tabs scroll sideways inside their own container": the rules allow that only for tables, code and diagrams. Change: "`.tabs` wraps (`flex-wrap: wrap`), no scroll."
- "`.pop` ... max 70% of the view height": implementers will write `70vh`. Change: "`max-height: 70%` of a `position: fixed; inset: 0` layer (`#saa-pop` parent), never a `vh` unit"; extend `WL02` to any `vh` unit except inside `@supports (height: 1dvh)`.
- `.sheet.full` and the phone drawer: "`position: fixed; inset: 0`, with `padding-top: env(safe-area-inset-top)` and `padding-bottom: env(safe-area-inset-bottom)` of their own (fixed layers do not get the `:root` padding)."
- Stacking: "`.toast` sits above `.ex-bar` (`bottom: calc(var(--ex-h, 0px) + 12px + env(safe-area-inset-bottom))`); order of layers: top bar, exam bar, drawer, pop, sheet, toast." 

### 22. Section jumps land under the sticky header; resume by `y` is unreliable (10, 9.6)

**Change.** "`.sec`, `.sub`, `.h3`, `.fig`, `.pr` have `scroll-margin-top: calc(var(--top-h) + env(safe-area-inset-top, 0px) + 12px)`. Resume stores `{slug, part, sid, off}` where `off` is the pixel offset inside the section `sid`; restore scrolls to the section, then adds `off`." (An absolute `y` is wrong when text size, route or `content-visibility` estimates differ.) The hot snapshot of the reader uses the same shape.

### 23. `caps` waits for the slowest of four promises (3.4, 3.7 step 4)

**What is wrong.** In a frame that never answers, each `use()` takes 10 s to resolve `null`; that is fine, but one slow capability also delays the others (Ask and Save buttons wait for db).

**Change.** "Each capability sets `SAA.state.caps.<name>` and emits `caps` when it settles (the event may fire up to four times; listeners are idempotent). `Store.attach` runs when both `user` and `db` have settled."

### 24. The first frame shows the contents list twice on wide screens (2.5, 3.6)

**Place.** `{{static}}` puts the contents list in `#saa-view`; `#saa-toc` also holds the "static contents list".

**Change.** "The build writes the list once into `#saa-toc`. `{{static}}` in `#saa-view` holds the title block, the `examFacts` strip and, with class `static-toc`, the same list; `20-layout.css` hides `.static-toc` from 760 px, and `90-phone.css` shows it (the drawer is closed on a phone)." State that the drawer is closed by CSS alone, without script.

### 25. Hash writes are not guarded (3.3)

**Change.** "`Router.go` updates its own state first, then writes the hash inside `try/catch` (`location.hash = ...`, or `history.replaceState` for `{replace}`); a failed write is ignored. `Router` ignores a `hashchange` for the route it is already showing." No `key=value` and no query string ever (already so).

### 26. Between 1100 and about 1280 px the text column is too narrow (4.2)

**Place.** Grid `17rem | main | 15rem` plus a left margin of 8.5rem: at 1100 px the text column is under 400 px, about 45 characters.

**Change.** "The hanging margin and `.co-l` in the margin apply from 1280 px. From 1100 to 1279 px the rail column stays and callout labels are tabs above the block." Add a 1100x800 `prose` shot to 9.3.
