# Web version, part E: Claude features, speak practice, search

Date: 2026-10-04. Contract: `tools/web/ARCHITECTURE.md` 1.1, section 6.

## Files

| File | Content |
|---|---|
| `tools/web/js/aicore.js` | Pure. Prompt builders, validators, score, failure messages. |
| `tools/web/js/ai.js` | The only caller of `sample.json`. One call at a time, Stop, hide state. |
| `tools/web/js/speak.js` | View `speak`, mount `speak`, `Speak.render`, shot states `speak-self`, `speak-result`. |
| `tools/web/js/ask.js` | `Ask.open(slug, sid)`, the sheet, page-side quote check, marking in the reader, shot state `ask`. |
| `tools/web/js/search.js` | `Search.open`, `Search.jump`, the `/` key, worker start and fallback, shot state `search`. |
| `tools/web/js/search-worker.js` | The full-text worker (protocol of 6.6). |
| `tools/web/css/70-ai.css` | Classes of 4.3 row "Speak, Ask, search". |
| `tools/web/tests/test_aicore.mjs` | 11 tests. |
| `tools/web/tests/test_search.mjs` | 5 tests (worker in a `vm` context, `Search.jump`). Not in the contract table; added. |

Throwaway files (not part of the product): `_build/tmp/web-e/` (a sandbox copy of the fixture book, `mk.py`, scenario pages and PNGs).

## What was tested, and how

- `node tools/web/tests/test_aicore.mjs`: 11/11. `node tools/web/tests/test_search.mjs`: 5/5.
- `web lint`: 0 findings.
- `web selftest --book-dir _build/tmp/web-e`: render 3153/3153, phone 3558/3558, sim 294/294, hot 24/24, node 6/6. `Speak.render` is part of the render and phone runs.
- `web shots --only speak-self,speak-result,ask,search`: 16 PNGs written, looked at desktop and phone, light and dark.
- Scenario pages on the single preview (stub, and a fake `sample` put into `SAA.state.caps`), each looked at as a PNG:
  - Speak without `sample`: no Claude control, timer, five boxes, must-say checklist, model answer.
  - Speak check with the stub: band, score, moves, marked quotes, key points, "Not checked", clarity, repaired answer, follow-up.
  - `rate_limited`: the message, text kept. Validator `ok: false`: "The reply came back in a broken format. Try again." `not_granted`: the Claude controls disappear, the self-check stays.
  - Ask: grounded answer; `partly` with `grounded: "some"`; `answered` with `grounded: "none"` (muted block, "Answer more carefully"); `not_in_book` (links from `see`, "Search the book").
  - Ask quote link: closes the sheet and marks the sentence in the reader. Checked with a quote that crosses a fact link (three text nodes).
  - Search: jump-to rows; full text from the Blob worker (`--single`) and from `assets/search-worker.js` (served preview).

Not tested: a real `sample` call (only the stub and fakes); the Stop button during a slow call (the stub answers at once); Rehearsal with more than one prompt (the fixture has one prompt; the button is hidden below two prompts); `session_expired`, `refused`, `prompt_too_large` in the browser (covered by `AICore.message` in the node test only); a real phone. The exact phone width could not be judged from PNGs: headless Chrome on this machine lays out wider than 400 px, so every phone shot (also Today) is cut on the right. The selftest width asserts pass.

## Deviations and interpretations

Contract items I filled in or changed. None changes a name of the contract.

1. **`AICore.speakScore(data, item)` needs her answer and the speaking rate.** `validSpeak` puts the answer into `data.answer`; the rate comes from `SAA.state.cfg.wordsPerMinute` (an optional third argument overrides it). Without the rate, `seconds` is 0. No number is in the JavaScript (WL08).
2. **`validSpeak` and unknown ids.** A `covered` or `missing` entry with an unknown `kp` is dropped. An error with an unknown `fact` id keeps the error and loses the fact id (dropping the whole error would hide a real mistake). A `kp` that is both covered and missing stays covered only.
3. **Coverage counts the model's `covered` list**, also when the quote has `hit: false`; such a quote only loses its highlight (as 6.4 says).
4. **Extra functions in `AICore`:** `locate(quote, text)` (source offsets, for highlighting), `nmap`, `words`, `band`, `factIds`, `turnBytes`. `askContext` takes an optional sixth argument `{section: n}` (a smaller cap) and also returns `title` and `chapter`.
5. **`askTurns` history shape:** `[{q, a}]`. The assistant turn is a compact JSON string of the earlier reply (`status`, `answer`, `missing`, `see`), so earlier turns look like the format that is asked for.
6. **`askContext` text of an H2 with H3 children:** a child text is appended only when the H2 text does not already hold it (the build's H2 text already holds it today).
7. **`AI.call` results beyond the contract:** `retry` in every failure object; code `busy` when a second call arrives while one runs (no message); `not_granted` with `hide: true` when `sample` is null (nothing is switched off in that case).
8. **Extra `AI` functions:** `AI.hidden()` (true after a hide failure), `AI.busy()`, `AI.busyHtml()` (the "Checking…" line with Stop; callers handle `data-act="ai-stop"`).
9. **New bus event `ai:off`** (no detail), emitted once after a hide failure. `ai.js` also sets `hidden` on every `.sec-ask` and `.ai-only` element then. **For B:** `reader.js` line 199 shows `.sec-ask` from `caps.sample` alone, so a later part shows the Ask buttons again; `Ask.open` then only shows the toast "Claude features are off for this page." Using `SAA.AI.available()` there fixes it. `files.js` already uses `AI.available()`.
10. **`Speak.render` options:** `step` 3 or 4 opens the self-check at once (default: it opens with "Check myself"); extra options `text` (prefill, used by the hot snapshot and the shots) and `extra` (the "extra" pill).
11. **Speak storage.** Self-check save writes `t`, `tries`, `self`, `words`, `seconds`; the Claude result writes `t`, `score`, `band`, `missing`, `words`, `seconds`. `tries` grows once per attempt (the first save of the two), and again after Reset. Both saves stamp `daily.<day>.speak` and emit `speak:done`. The must-say ticks of the self-check are not stored (the document has no field for them).
12. **Ask draft key** is `ask-q` for every section (as 6.2 names it), so an unsent question follows her to the next section.
13. **Ask is not a view**, so it has no hot snapshot; unsent text survives a republish through `Store.draft`. Speak's view snapshot is `{text: {<textarea id>: value}}`.
14. **Ask support quotes.** Only quotes with `hit` are listed. A quote that is found in `#sec-<sid>` is a button that marks it; a quote from a fact, the glossary, a figure, the summary or a table row is shown as plain text with its source in words. `partly` with `grounded: "none"` is shown like `answered` with `none`.
15. **Search:** `Search.jump(text, manifest?)` takes the manifest as an optional second argument (for the node test). Rows are `{route, title, sub, kind}`; at most 12. Planned chapters are listed with "Not written yet".
16. **Worker ranking detail:** after matched terms, heading matches and kind order, ties go to the stronger match (exact, prefix, one edit), then book order. Prefix match needs two letters; one edit needs five letters and the same first letter.
17. **CSS specificity:** every selector of `70-ai.css` starts with `.app`, because `10-base.css` resets headings, lists and paragraphs as `.app h3`. Extra class names inside my components (for example `sp-q`, `sp-kps`, `ask-quote`, `srch-snip`) are local to this file.
18. **`.ai-only`** marks Claude controls outside the reader (hidden by `ai.js` on a hide failure).

## Notes for other owners

- **A:** `build web --out DIR` collides with the common `--out` option: `--out <folder>` is taken as the report file and fails with `IsADirectoryError` after the build ran.
- **A / C:** a headless screenshot of a scrolled page is shifted down (blank band on top). The `speak-result` shot state scrolls back to the top for that reason.
- **D (stub):** the canned ask reply quotes the first line of BOOK, which for an H2 starts with heading text ("Look first Find one shelf…"). That is a hit in the sent text and is not findable in the DOM, so the stub never produces a "Show in the text" button. A quote from the second sentence would.
- **Orchestrator, after the first publish:** one real `sample.json` call per tier (speak check on `default`, Ask on `quick`), and the Stop button during the speak check.
