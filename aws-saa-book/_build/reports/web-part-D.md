# Web version, part D: store, Today, plan, dashboard, files, stub

Date: 2026-10-04. Contract: `tools/web/ARCHITECTURE.md` 1.1, sections 5, 8, 9.4.

## Files written

| File | Content |
|---|---|
| `tools/web/js/merge.js` | `Merge.deep`, `stamps`, `doc`, `attempts`, `diff` (pure), plus `same`, `isObj` |
| `tools/web/js/store.js` | `Store` of 5.4 to 5.6: local-first, outbox, attach, flush, status line |
| `tools/web/js/today.js` | view `home`; shot state `home` |
| `tools/web/js/plan.js` | view `plan`, mount `plan`, helper namespace `SAA.Plan`; shot state `plan` |
| `tools/web/js/dash.js` | view `progress`; shot state `progress` |
| `tools/web/js/files.js` | views `files`, `about`; `SAA.Files.saveProgress`; shot states `files`, `about` |
| `tools/web/css/60-today.css` | the classes of 4.3 row "Today, plan, dashboard", tokens only |
| `tools/web/stubs/claude-stub.js` | fake `window.claude` with modes `ok`, `none`, `errors`, `hot`, `consent` |
| `tools/web/tests/test_merge.mjs` | 13 tests (uses `harness.mjs`) |
| `tools/web/tests/test_store.mjs` | 15 tests of `store.js` together with the real stub, in node, with virtual timers |

Throwaway (not part of the product): `_build/tmp/web-d-book/` (sandbox copy of the fixture book), `_build/tmp/web-d-shots/` (`make.py`, `shoot.py`, pages and PNGs), `_build/tmp/shots-d` (a stray one-line output file).

## What was tested, and how

- `node aws-saa-book/tools/web/tests/test_merge.mjs`: 13/13.
- `node aws-saa-book/tools/web/tests/test_store.mjs`: 15/15. Covers: db = null; browser storage throwing (status `memory`); both together; export then import; cloud attach and flush (paths under `study/<uid>`, `update` against `set`, exam written at once, flags, coalesced qstats write after 2 s); memory plus cloud ("saved online only"); a new device does not overwrite cloud settings or a running mock; remote snapshot merged without a write; `errors` mode (unavailable, one retry, revoked, sync stops, outbox kept); another uid on the same browser (backup and merge back); hot snapshot round trip; `replace("exam", null)` in the same second as a patch; two tabs (re-read before save, `storage` event); the 40-attempt trim; `consent` mode; every stub capability and mode.
- `python3 aws-saa-book/tools/saa.py web lint`: 0 findings.
- Looked at screenshots (desktop and true 400 px phone, light and dark) of Today, Plan, Progress, Get files, About, and of the degraded states: About in `consent` mode (line plus "Save online too"), About and Today with storage blocked and no db, Get files with no capability. Made from a `--preview --single` build of the fixture book.

Not tested: a Save click on a real `manifest.exports` row (the fixture has no exports and a single build never has any); the file picker of Restore progress; the `plan` mount inside a chapter (the fixture has no `calendar.md`); the "Drills from Claude" card with a real `Quiz.start`; `#t.hot` and `#t.exam-sim` (they need `selftest.js`).

## Deviations and interpretations (for the integrator)

1. **Extra `Store` functions.** `Store.save(name)` (local save of the live document without a cloud write or a new `updatedAt`; `exam.js` already calls it for the timer), `Store.coach()`, `Store.refreshCoach() -> Promise` (the coach needs `qindex`, which is async, so `exportAll` and `summaryText` use the last computed coach), `Store.info() -> {status, memory, consent, cloud, stopped, pending}`, `Store.get("coach")`, `Store.get("root")`. `Store.load` also takes `coach` and `drills`.
2. **`Store.status()` in memory mode.** It returns `cloud` when cloud sync is on, even if browser storage is broken. `Store.info().memory` tells the two apart. The line then reads "Saved online only".
3. **Extra namespaces.** `SAA.Plan` (date helpers, `model`, `paint`, `taskList`, `bind`, `label`) and `SAA.Files` (`saveProgress`). The module table lists no namespace for `plan.js` and `files.js`.
4. **`Merge.doc("qstats", l, r, opts)`.** "keyRev mismatch ignored" is implemented twice: with different `kr` on the two sides the higher `kr` wins whatever `t` says; with `opts.kr` (`{id: keyRev}` from qindex) records of another revision are dropped. `Store` does not pass `opts.kr` (qindex is async); `Scoring` already ignores stale records when it reads.
5. **Merge ties.** Stamps with the same absolute value: the negative one wins (so the merge is the same from both sides). `exam` with the same `updatedAt`: the copy with the larger `activeMs` wins (the timer saves without a patch). `Merge.attempts` returns a map, accepts maps or arrays, and prefers a copy that still has `answers`.
6. **`Store.replace` sets `updatedAt` to `max(now, previous + 1)`** and saves without the re-read merge. Otherwise a mock finished in the same second as its last patch came back as "running".
7. **`Store.patch("exam", p)` on a `{none: 1}` document adds `none: 0`** (a merge cannot delete a key).
8. **Outbox before attach.** Patches are recorded as the contract says. At attach, the entries of the five state documents are replaced by `Merge.diff(remote, merged)`, and local attempts that the db lacks are queued. Without cloud sync the outbox keeps only the newest 40 attempt entries, so it cannot grow without limit.
9. **Root creation.** `createdAt` is set on the first settings patch or on the first attach. Defaults have `createdAt: 0`, and the merge ignores 0 when it takes the smaller value.
10. **One backup.** The uid of the current backup is kept in `saa1:bakid`, because `U.ls` cannot list keys. `Store.reset()` clears keys with `U.ls.set(key, null)`.
11. **`Store.draft(id)` returns `""`** for a missing draft.
12. **`store:change` details.** `doc` can also be `"attempts"`, `"drills"`, `"ui"` and `"*"` (after attach, import, load, reset). Today, plan and dashboard ignore `"ui"`.
13. **Listeners in `store.js`** use `addEventListener` directly (`storage`, `pagehide`, `visibilitychange`, and one document click for the "Save online too" button), not `U.on`.
14. **After a failed attach** with a transient code the "Save online too" button stays and a later click tries again; after a terminal code (`not_granted`, `revoked`, ...) the store stops for the visit and `attach` resolves `false`.
15. **Current day (8.1 against 8.2).** By 8.1 the current day is the first day with an open task, so "Left from Day 3" of 8.2 could never show. Today's card shows the calendar day and lists open tasks of earlier days under "Left from Day n" (the last three such days). The plan view marks the calendar day `is-today` and marks earlier days that still have open tasks with the words "Open tasks". `Plan.model` returns both `today` and `current`.
16. **Today.** The speak minimum is not a checkbox (Speak is its only writer): it is a "Done" or "Not yet" pill with a link to `#speak`. The domain strip shows only when at least one answer exists. On the very first visit "New since your last visit" marks everything seen and shows nothing. The Daily mix and Drills cards show only when `SAA.Quiz` exists. Drills call `Quiz.start({kind: "drill", ref, ids: <the items of the drill>, title})`.
17. **Dashboard.** "Questions seen of the bank" counts qindex rows outside pool `mock`, not `manifest.counts.questions` (in the fixture the manifest number was smaller than the number of answered questions). Coverage uses `settings.routeBy[slug]`, else `settings.route`.
18. **Get files.** After a successful save the row says "Saved." (the contract only says what not to show for other statuses).
19. **Stub extras.** `localStorage.saaStubUid` (another user id), `localStorage.saaStubCaps` (comma list of capabilities that resolve null in any mode), `sessionStorage.saaStubNoLs = "1"` (every `saa1:` key throws, for the `memory` status), `__stub.setMode(m)`, `__stub.breakStorage(on)`, `__stub.sampleCalls`. `use()` resolves on a zero timer, never synchronously. A write fires the listener twice: once with `hasPendingWrites: true`, then confirmed.

## Things the integrator should know

- **Phone screenshots.** Headless Chrome did not go under 500 px of window width in `diagram shot` and `web shots`: the 400 px images were cropped on the right (the fifth nav link and the right edge of cards were cut). The layout itself is right: a 400 px iframe shows it. If `web shots` gives cropped phone images, it needs device metrics or a frame, not a CSS fix.
- `#t.shot.<name>` showed "Not built yet" when I ran `web shots` (no `selftest.js` yet), so my five shot states were run through throwaway pages instead. They return a promise.
- The shot states set `SAA.Test.clock` to 2026-10-07 (home, plan) and 2026-10-20 (progress) and never clear it.
- `test_store.mjs` does not use `harness.mjs` (it needs async tests and a fake `window`); it prints the same `ok` / `FAIL` / `PASSED n/n` lines and sets the exit code.
