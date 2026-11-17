# Web version: review before the first publish

Date: 2026-10-04. Reviewer pass over a fresh preview of the fixture book.

**Verdict: not ready. 2 blocking defects.** Both are small fixes. Everything else can ship.

## What I ran and looked at

| Step | Result |
|---|---|
| `build web --preview` on a fresh sandbox copy of the fixture | ok, 0 errors, 5 expected warnings (1 `WB04`, 4 `WB10`) |
| `web selftest` | ok: render 3153/3153, phone 3558/3558, sim 294/294, hot 24/24, node 6/6 |
| `web shots` and `web shots --extra tools/web/tests/fixtures/extra-shots.json` | 141 PNG files. I looked at every one. |
| A second sandbox with two real diagram specs (`pilot-vpc-two-az`, `pilot-rds-multi-az-vs-replica`) and my own extra list | 96 PNG files. I looked at 49: every figure shot, and at least one phone and one desktop shot of every other state, covering both themes. |

Screenshot folders (names are `<name>.<desktop|phone>.<light|dark>.png`):

- **S1** = `aws-saa-book/_build/tmp/web-review/_build/shots/` (the standard set and the integrator's extra set)
- **S2** = `aws-saa-book/_build/tmp/web-review2/_build/shots/` (my set, names start with `y-`; list in `aws-saa-book/_build/tmp/web-review-extra.json`)

The fixture figure has no diagram spec, so the standard shots never show an inline, themed diagram. S2 exists to close that gap.

## Blocking defects

### B1. On the phone, wide tables hide columns and show no sign of it

- **Seen in:** S1 `x-table.phone.light.png`, `x-table.phone.dark.png` (the compare table "Shelf or crate" shows Question and Shelf; the Crate column is gone). S2 `y-mock-intro.phone.light.png`, `y-mock-intro.phone.dark.png` (the mock intro table shows Exam domain and Exam weight; "Questions here" is gone).
- **Why it blocks:** the cut falls exactly on a column edge, and a touch screen shows no scrollbar. The table looks complete. This reader trusts the gist of one glance, and the compare table is the "X or Y" decision of every chapter. She reads one option and never sees the other.
- **Cause:** `tools/web/css/90-phone.css` line 78 gives every table that is not stacked `min-width: 34rem` (544 px), also a three-column table that fits at 368 px. `.tw` in `30-prose.css` line 162 has no cue for scrolling. The comment says "first column fixed", and the shot shows no fixed column.
- **Fix (any one is enough):** remove the minimum width for tables of three columns or fewer; or stack `compare` and `plain` tables like the others; or keep the scroll and add a visible cue (an edge shadow while more content is to the right, plus a line such as "Scroll sideways: 1 more column").
- **Also:** add a phone assert to the selftest. Today it accepts any wide element inside `.tw`, so it cannot catch this.

### B2. "Practice" leads to an empty mistakes log, and the mocks and drills have no entry point

- **Seen in:** S2 `y-mistakes-empty.phone.light.png` (first tap on Practice: "Your mistakes log is empty", with an active primary button "Retry these"). S1 `home.desktop.light.png`, `plan.desktop.light.png` (the tasks "Retry your mistakes", "Take the preview mock" and "Answer the core questions" have no link; only reading tasks do). S2 `y-mock-intro.*` could only be reached by typing the route.
- **Why it blocks:** the practice features all work, and she cannot find them. Practice in `shell.html` points to `#mistakes`. No view links to `#mock.<n>` except the Quiz tab of a mock chapter, three taps deep in the contents. `#drill.d1` to `#drill.d4` are linked from nowhere. A reader who acts before she reads taps Practice on day one and meets a dead end.
- **Fix:** make Practice a short hub above the log: Daily mix, Retry my mistakes (off when the log is empty), the four domain drills, each mock with its state (Start, Resume, last score), then the mistakes log. Every route exists already. Give the empty log a next step ("Start with the quiz of the chapter you are reading").
- **Second part, can follow the first publish:** let a plan task carry a route (`mix`, `retry`, `mock.1`, `quiz.<slug>`), so every task on Today has a link.

## Not blocking

| # | Defect | Screenshot |
|---|---|---|
| N1 | **Exam facts are missing.** The four fact ids of `shell.json` (`exam-question-count`, `exam-duration`, `exam-passing-score`, `exam-esl-accommodation`) are not verified facts, and the real book has no `data/facts/` yet. The first frame has no exam strip, the results page has no pass line, and the ESL checkbox names no minutes. `ARTIFACT-RULES.md` names exam facts as part of the first frame. The orchestrator should add the four facts before the publish; the page works without them. | build warnings `WB10`; S2 `y-mock-intro.desktop.light.png`; S1 `mock-results.desktop.light.png` |
| N2 | The static first frame says "1 chapters: 0 ready, 1 in draft." Fix the plural. The first frame itself is right: title, counts and the contents list are in the HTML before any script. | `_build/tmp/web-selftest/index.html`, element `#saa-view` |
| N3 | The blueprint strip shows only D1 to D4. A reader who forgets terms cannot tell which domain is red. Add the short names (Secure, Resilient, Performing, Cost), at least from 760 px. The strip also stops at about 340 px and leaves the column half empty. | S1 `home.phone.light.png`, `chapter.desktop.light.png` |
| N4 | The results page shows the domain numbers twice (strip, then bars). Keep the bars. "Send the numbers to Claude" comes before the review of her answers; the review is what she needs first. | S1 `mock-results.desktop.light.png`; S2 `y-results-review.desktop.light.png` |
| N5 | A quiz prints "Question 1 of 4" twice. | S1 `quiz-open.desktop.light.png` |
| N6 | The draft banner says "Practice questions appear when the chapter is ready" while the Quiz tab is there and works (preview only, but it is what she will see for the pilot chapter). | S1 `chapter.phone.light.png`; S2 `y-quizpart.phone.light.png` |
| N7 | A link to the Do part shows the file name: "See 3-do.md". The build should replace the text of links to `3-do.md`, `4-say.md` and `5-quiz.md` when it equals the file name, or lint should reject it. | S1 `prose.desktop.light.png` |
| N8 | Fallback figure (no spec): a white card on the dark page, and no title in the figure header. Legible. Real diagrams are fine (see below). Treat `WB04` as an error for a ready chapter. | S1 `x-figure-open.phone.dark.png`, `x-figure-zoom.phone.dark.png` |
| N9 | On the phone a time or link wraps alone under its task ("52 min" under "Open Amazon Widget Store"). Put the minutes on the first line. | S1 `home.phone.light.png`, `plan.phone.light.png` |
| N10 | "Next" is on the left and "Previous part" on the right at the end of a part. On desktop, put Previous left and Next right. | S2 `y-deep-faq.desktop.light.png` |
| N11 | The tab line is 672 px wide on parts with a rail and 944 px on Do, Say it, Quiz and Sources. Keep one width. | S1 `x-do.desktop.light.png` against `chapter.desktop.light.png` |
| N12 | The reveal marker is a triangle on desktop and "+" on the phone. Use one. | S1 `speak-self.desktop.light.png`, `speak-self.phone.light.png` |
| N13 | Copy: "Speak and let your keyboard's microphone type, or type." Write "Use the microphone key of your keyboard, or type." In mock mode on the phone, hide "Keys: A to D pick an option." | S1 `speak-self.phone.light.png`, `mock-run.phone.light.png` |
| N14 | About says "The owner of this page, and Claude in the owner's session, can read study progress" also when progress is saved on this device only. And "save a file" appears without a Save button when `downloads` is absent (known to the integrator). | S1 `d-none-about.desktop.light.png` |
| N15 | Changed recently: the status "examinable" has almost no pill shape, and the values end with a stray full stop ("200 widgets."). | S2 `y-changed.phone.light.png` |
| N16 | The auto-link marks "Widget" inside the product name "Amazon Widget Store". With real terms, do not link a short term inside a longer AWS name. | S1 `chapter.desktop.light.png` |
| N17 | The text sent to Ask joins the heading and the first sentence without a break ("Look first Find one shelf"). | S1 `ask.phone.light.png` |
| N18 | Get files shows a laptop path and nothing else until exports exist. Fine for now; she should not open this page from the first publish note. | S1 `files.phone.light.png` |
| N19 | Not web: `aws-saa-book/data/harken.json` still exists. `RULINGS.md` says the name Harken must not appear anywhere in the book. The web build does not read it. | file listing |

## What is good (judged as the reader)

- **Reading.** Body text is 17 to 18 px with a line of about 60 to 65 characters on desktop and 35 to 40 on the phone, with calm spacing. Headings with a time box, hanging callout labels (Key fact, Exam signal, Say it, Startup example), the Deciding question block and the stacked tables on the phone all give a correct gist. S1 `prose.*`, `x-words.phone.*`, `x-numbers.phone.*`; S2 `y-traps.*`.
- **Routes.** Fast, Pass and Full sit under the title with minutes, the progress line names the route, and off-route sections collapse to "Not on the Pass route" with Open. S1 `chapter.*`, `x-numbers.desktop.light.png`.
- **Phone.** No sideways page scroll in any shot (also asserted 3558 times). Controls are large and reachable; the mock bar is one row; sheets replace popovers. Only B1 fails here.
- **Dark theme.** Every text, border, chip, pill and state colour is legible in every dark shot. Inline diagrams are themed correctly, with readable labels, icons and step numbers on desktop and at 400 px, and the compare diagram stacks its panels. S2 `y-fig-inline.*`, `y-fig-compare.*`, `y-fig-zoom.phone.dark.png`.
- **Practice.** Answering, the not-sure mark, per-option explanations with "Your pick" and "Correct answer" in words, cause buttons, think-aloud steps, stem-first mode, mock with answer sheet, submit confirmation, resume (hot test 24/24), domain breakdown and mistakes log all work. S1 `quiz-checked.*`, `mock-run.*`, `x-mock-submit.*`, `mock-results.*`, `mistakes.*`; S2 `y-quiz-cause.*`.
- **Design.** It continues her diagnostic artifact (Archivo wide headings, IBM Plex Sans and Mono, cool paper, indigo). No emoji, no gradient, no centred hero. Cards are used by role (prompts, figures, tasks), not on every block.
- **Platform.** `web lint` has 0 findings: no print, no dialogs, no page-started download, no `vh`, no literal colour, plain hash routes. Degraded modes say what is saved and where. S1 `d-*.png`.

## Fix pass (2026-10-04, after the review)

**Both blocking defects are fixed.** Tests after the fixes: `web selftest` ok (render 3153/3153, phone 3558/3558, sim 294/294, hot all pass, node 6/6); `tools/web/tests/test_site.py` 52/52; `tools/tests/run.py` 763 tests, OK. Shots looked at (sandbox `_build/tmp/web-review/_build/shots/`, names `z-*` from `_build/tmp/web-fix-extra.json`, plus `home`, `chapter`, `mistakes`, `quiz-open`).

| # | Status | What changed | Files |
|---|---|---|---|
| B1 | fixed | On the phone the 34rem minimum width applies only to tables with four or more columns; tables of up to three columns fit the screen (compare table and mock intro table show all columns). `.tw` now shades its right edge while columns are hidden (two token backgrounds, no script). The phone selftest fails when a table of fewer than four columns scrolls, or when a scrolling table has no shade. | `css/90-phone.css`, `css/30-prose.css`, `js/selftest.js` |
| B2 | fixed (first part) | `#mistakes` is now the Practice hub: Daily mix (with "Done today"), Retry my mistakes and Ten stem-first questions (disabled buttons with a reason when the log is empty), the domain drills, each mock with its state (Not started, In progress n of m with Resume, Last result with link), then the Mistakes log. The empty log names a next step with a link to the quiz of the chapter she last read (else the first chapter with questions). The short mount in chapter 00 hides its buttons while the log is empty. View title and `h1` are "Practice"; the log heading is an `h2`. | `js/mistakes.js`, `css/50-practice.css` |
| N2 | fixed | "1 chapter" / "n chapters". | `saalib/site.py` (one line) |
| N3 | fixed | The strip carries `data-n` (Secure, Resilient, Performing, Cost), drawn by CSS from 760 px; the strip is up to 37rem wide there and full width on the phone. | `js/util.js`, `css/40-components.css` |
| N4 | fixed | Results: the strip is gone (bars stay); Review comes before "Send the numbers to Claude". | `js/exam.js` |
| N5 | fixed | The quiz progress line says "Answered n of m" (updated on Check); "Question n of m" appears once. | `js/quiz.js` |
| N6 | fixed | A draft chapter that has questions says "The practice questions can still change." | `js/reader.js` |
| N7 | fixed | A link to `3-do.md`, `4-say.md`, `5-quiz.md` or `sources.md` whose text is the file name reads "the Do part", "the Say it part", "the quiz", "the sources". | `helpers/site_md.py`, both copies of `test_site.py` |
| N9 | fixed | On the phone the minutes stay on the first line of a task; the link goes below. | `css/60-today.css` |
| N10 | fixed | From 760 px Previous is left and Next is right (on the phone Next stays first). | `css/40-components.css` |
| N11 | fixed | The tab line is at most 42rem in every part. | `css/40-components.css` |
| N12 | fixed | Reveals use "+" and "−" at every width. | `css/30-prose.css`, `css/90-phone.css` |
| N13 | fixed | New microphone sentence; the "Keys" line is hidden on the phone. | `js/speak.js`, `css/50-practice.css` |
| N14 | fixed | About: "Who can read your progress" follows the save status; "save a file" appears only with a Save button. | `js/files.js` |
| N15 | fixed | The status pill has a border and surface; no full stop after a value that is one fact chip. | `css/30-prose.css`, `helpers/site_md.py`, both copies of `test_site.py` |

**Left open**

- B2, second part: a plan task cannot carry a practice route yet (needs a field in `data/plan.json` and its schema). "Retry your mistakes" and "Take the mock" on Today still have no link; Practice is one tap away.
- N1 (the four exam facts) and N19 (`data/harken.json`): for the orchestrator, not web code.
- N8 (fallback figure is a white card in dark; `WB04` as an error for a ready chapter), N16 (auto-link inside a longer AWS name), N17 (Ask text joins heading and first sentence), N18 (Get files before exports exist): not done.
- Not seen: the edge shade on a real table of four or more columns on the phone (the fixture has none that scrolls); the hub with a mock in progress or with a last result (the code paths are simple, the shots show "Not started" only).
- The hub is drawn on mount and does not listen to store changes; it is correct on every visit.

**Notes for other owners**

- Outside `tools/web/` I changed one line of `saalib/site.py` (N2), two places of `helpers/site_md.py` (N7, N15) and the two matching asserts in `tools/tests/test_site.py` (the integrator's copy of the web test), so that the main suite keeps passing.
- `ARCHITECTURE.md` still describes `#mistakes` as "Mistakes log" only (3.3, 7.6, 9.3) and the results page with the strip (7.5); the text was not updated.

## Not seen here

A real `sample` call, a real `downloads.save`, the file picker of Restore progress, the `plan` mount inside a chapter, the Stop-and-answer gate, and a real phone (safe areas, dictation). These belong to the functional pass after the first publish. One S2 shot (`y-changed.desktop.dark.png`) rendered with the fallback fonts because Google Fonts did not answer; the layout held.
