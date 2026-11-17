# Web version, part C (practice): result and deviations

Date: 2026-10-04. Contract: `tools/web/ARCHITECTURE.md` 1.1, sections 7, 9.1 to 9.3, 11.

## Files written (all under `aws-saa-book/tools/web/`)

| File | Content |
|---|---|
| `js/scoring.js` | `SAA.Scoring` (pure): every function of 7.1 |
| `js/qview.js` | `SAA.QView.render`, `QView.review`, stem-first, cause buttons, report form |
| `js/quiz.js` | views `quiz`, `drill`, `retry`, `mix`; `Quiz.start`; mounts `quiz`, `return`; shots `quiz-open`, `quiz-stemfirst`, `quiz-checked` |
| `js/exam.js` | views `mock`, `attempt`; the timed mock (port of the diagnostic engine); shots `mock-run`, `mock-results` |
| `js/mistakes.js` | view `mistakes`; mount `mistakes`; shot `mistakes` |
| `js/cards.js` | view `cards`; `Cards.render`; shot `cards` |
| `js/selftest.js` | view `t`: `#t.render-all`, `#t.exam-sim`, `#t.hot`, `#t.shot.<name>` |
| `css/50-practice.css` | the classes of 4.3 rows Question, Exam, Mistakes and cards |
| `tests/harness.mjs` | `load`, `fixture`, `built`, `test`, `eq`, `ok` |
| `tests/test_scoring.mjs` | 23 tests |

## What was tested

- `node aws-saa-book/tools/web/tests/test_scoring.mjs`: 23/23, without a build (fixture book questions and a synthetic bank) and with a built preview folder as the first argument (79 built questions).
- `web lint`: 0 findings.
- `web selftest --book-dir <sandbox copy of the fixture book>`: `ok: true`. render 3153/3153, phone 3558/3558, sim 294/294, hot 23/23, all six node files pass.
- `web shots --only` my seven states: looked at desktop and phone, light and dark. They render as designed.

## Deviations and interpretations (for the integrator)

1. **`Store.save("exam")`.** The contract has no local-only save for the timer. `store.js` (D) provides `Store.save(name)`. `exam.js` adds the timer delta to the live `exam` document in place (`activeMs`, `ans.<id>.ms`) and calls `Store.save("exam")` every 10 ticks; `Store.patch("exam")` runs on answer, flag, navigation and `pagehide`, as 7.4 says. This is the one place where C writes into a `Store.get` object.
2. **`Quiz.start(spec)` navigates.** It keeps the spec and goes to the view of that kind (`#quiz.<ref>`, `#drill.<ref>`, `#retry.x`, `#mix`) with `force`, so the session has a route, a title and a hot snapshot. Extra spec fields: `sf` (force stem-first), `dq` (map of plain-text questions), `doc` (a drill document of 5.2; `Quiz.start({doc})` is the simplest call for "Drills from Claude"). `#drill.<id>` with an id other than `d1` to `d4` opens the drill document of that id from `Store.drills()`.
3. **`QView` options beyond 7.2:** `onNav(delta)`, `last` (button text "See the result"), `onCause(code)`, `focus`, `keys: false` (an inline question in prose takes no letter keys; used by the `return` mount). State fields beyond 7.2: `sfChip`, `sfWord`, `sfDone`, `cause`, `limit`. `stage` is `"sf"` or `"opts"`.
4. **Extra functions on my namespaces** (no new namespace): `Scoring.correctIds`, `pct`, `dayOf`, `validRec`, `routeRows`, `CAUSES`; `QView.bindReview`, `setCause`, `CAUSE`, `CAUSE_ORDER`, `fail`, `root`, `fmtDate`, `secHref`, `secTitle`, `chapterTitle`, `kwRanges`; `Exam.start`, `tick`, `go`, `submit`, `askSubmit`, `doc`, `running`, `summaryText` (the selftest drives the real exam through them).
5. **Key handling.** One `keydown` listener on `document`, installed once through `U.on(document, "keydown", null, …)`; it acts only while the interactive question is in the DOM. `exam.js` listens to `pagehide` on `globalThis` through `U.on` and removes it on unmount.
6. **Option markup.** `.opt` is a `div` that holds `label.opt-l` (input, bubble, text) and, after Check, `.opt-x` (tag and why), so links inside a "why" are not inside a label. Extra classes of mine: `.opt-l`, `.opt-t`, `.opt-x`, `.chip`, `.pv`, `.qz-*`, `.at-*`, `.ex-*`, `.mk-*`, `.fc-*`, `.drow-*`, `.selftest`.
7. **Stem words** are `<span class="q-w" role="button" tabindex="0">` (the contract names a span; role and tabindex make them usable from the keyboard).
8. **`Scoring.record`.** `d` is the local day number (`U.day` when `util.js` is loaded, else the same formula). A new wrong answer clears `c`; a correct answer keeps it. A record with another `keyRev` is replaced. `nextBox` has no upper limit.
9. **`Scoring.mistakes` field `last`** is the reason for the latest entry in the log: the newest wrong answer, else the newest not-sure mark.
10. **`Scoring.buildMix`.** Quotas 4/3/3 scale with `n`; shortfalls are filled round-robin from the three groups only, so the mix is empty when nothing is read and nothing is answered (the view says to read a section first). The day seeds only the order.
11. **`Scoring.gate`** also returns `counted` and `needed`. **`Scoring.buildCoach`**: accuracy uses the last answer per question; `weakTopics` needs 3 answers and accuracy under `cfg.gate.strong` (80 when `state.cfg` is absent); `missed` at most 20, `confusions` 10, `luckyGuesses` 30, `mocks` the last 6; `unreadPass` uses a private copy of the `Content.routeSections` rule because the module is pure.
12. **`Scoring.validQuestion`** rejects any key outside the DQ shape of 5.2 (so no `_h` and no `ch`). `quiz.js` copies a DQ field by field and marks it `dq: 1`; `QView` reads `_h` fields only when `dq` is absent. DQ answers are not written to `qstats`, and the attempt review cannot show them (they are not in `Content`).
13. **Mock intro** reads count, minutes and split from the manifest entry (the same numbers as the mock file); the file loads on Start. While another mock runs, Start is replaced by "Resume mock N" and a two-step "Discard it".
14. **Attempt page.** The pass note is plain text from `examFacts.pass.text` (no evidence link). Review uses the canonical option order, because the attempt document of 7.5 has no `oo`. "Retry the wrong ones" calls `Quiz.start({kind: "retry", ref: <attempt id>, …})`.
15. **Selftest output.** After the `SELFTEST PASS|FAIL` line and the failure lines, `selftest.js` may add `skipped <n>` and `note: …` lines (for example `note: no mock`). The stub-database assert of `#t.exam-sim` is skipped with a note when the store is not in status `cloud` after 0.5 s.
16. **`#t.hot`** reads the restored outbox directly after `Store.init(snap.store)`, because with the stub attached the outbox is flushed a moment later.

## Notes for other owners (nothing changed in their files)

- **A, `web shots`:** the phone PNGs are laid out wider than 400 px and cropped (headless Chrome's minimum window width); the right edge of every phone shot is cut, for all owners' views. The phone asserts of the selftest pass, so this looks like a screenshot artifact, not a layout fault, but the phone check of the contact sheet cannot be trusted until it is fixed (for example with device emulation instead of the window size).
- **A, `test_scoring.mjs`:** a question id can be in a `d/` file and in a drill file, so the test scores each built file on its own.
- **D:** `Quiz.start({doc: <drill document>})` is available for the "Drills from Claude" card.
- Not built (P2 or out of scope): nothing of part C was cut. The `return` mount is implemented but could not be seen with the fixture book (it needs three earlier chapters that are read).
