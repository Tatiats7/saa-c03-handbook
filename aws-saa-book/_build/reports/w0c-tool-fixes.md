# W0c tool fixes: the follow-ups left open by the W0 integration

Date: 2026-10-09. Input: `w0-integration.md` ("What still does not work", items 3 and 4), `gate-break-fixes.md` (H13) and
`w0-result.json` (`modules.ledger.problems[0]`). Method for every item: the regression test first (it failed before the
fix), then the fix, then the full suite and `selftest`. No change to `common.py` or `saa.py`. `data/book.json`, the
ledger, the work folders and `data/facts/` were not touched (no real `data/facts/*.jsonl` exists yet, so no real fact
sheet changes shape from item 2).

## Result in one view

| Check | Result |
|---|---|
| `python3 aws-saa-book/tools/tests/run.py` | 788 tests, 0 failures, 0 errors (778 before; 10 regression tests added) |
| `python3 aws-saa-book/tools/saa.py selftest` | ok: every required module has a must-fail test (facts 59, qbank 113, ledger 22) |
| `python3 aws-saa-book/tools/helpers/smoke.py run` | `SMOKE OK`; the sandbox sheet `facts/vpc.md` now prints `... | 5 | Yes` for the adopted table row instead of the console link |

## 1. One number-boundary rule everywhere (W0 item 3, H13)

`lint.holds_display(text, display)` stays the one implementation: a substring test where a display that starts or ends
with a digit must not touch another digit of a longer number (`5 Gbps` in `45 Gbps`, `500 widgets` in `2 500 widgets`,
`1,000` in `11,000`). It is now used in the three places that still had a plain substring test.

| Where | Before | Now |
|---|---|---|
| `facts._check_rest`, M7 (a display is in the claim or a quote) | `display in text` | `facts._holds(text, display)` |
| `facts._rederive_verdict` (audit re-derivation, the branch for a display without a scannable number) | `d in answer or d in quote` | `_holds(answer, d) or _holds(quote, d)` |
| `qbank._Ctx.numbers_outside_displays` (C109 on card front and back, P109 on key points, must-not-say and follow-up answers) | `number_with_unit in display` | `_holds(display, number_with_unit)` (the existing `qbank._holds`, which already resolves to `lint.holds_display`) |

`facts._holds` is a guarded import of `saalib.lint` at call time (the same shape as `qbank._holds`); without the lint
module, which never happens in the book, it falls back to the plain substring test. The import is lazy, so the lazy
import of `facts` inside `lint._load_facts` stays free of a cycle.

Why M7 mattered although M5 compares numbers by value: M5 is soft when the fact has a `derivation`, and M5 does not
see a thousands group written with a space (`2 500` scans as `2` and `500`). The CLI regression test adds a fact whose
claim and quote say `2 500 widgets` with the display `500 widgets`; before the fix it was accepted.

Open rest, not changed: the spoken-form check of P109 (`phrase in spoken`) compares number words, where a shorter
phrase inside a longer one (`two hundred widgets` inside `five thousand two hundred widgets`) is still a substring hit.
The technical red team lens on `4-say.md` must catch it (same catch as practice holes 36 and 41).

Tests added: `test_facts_holes.py` `DisplayBoundaries` (`test_must_fail_m7_display_inside_a_longer_number_in_process`
with the three examples, `test_must_fail_m7_display_inside_a_thousands_group_through_facts_add`,
`test_must_fail_rederive_answer_holds_the_display_inside_a_longer_token`); `test_qbank_holes.py`
`test_must_fail_number_that_sits_inside_the_display_number` (`0 widgets` against `50 widgets`, C109 back),
`test_must_fail_number_in_the_front_that_sits_inside_the_display_number` (C109 front),
`test_must_fail_key_point_number_that_sits_inside_the_display_number` and
`test_must_fail_follow_up_number_that_sits_inside_the_display_number` (P109).

## 2. The fact sheet prints link text only (W0 item 4)

`facts.render_sheet` passes every quote through the new `facts._link_text`: Markdown images become their alt text and
links their link text (nested up to three levels, same regexes as `_plain`). It applies to sentence quotes and to
table-row quotes before the cells are split, so `| Shelves per Region | 20 | [Yes](https://console.aws.amazon.com/...) |`
prints as `"Shelves per Region | 20 | Yes" (columns: ...)`. Only the rendered sheet changes; the stored quote in
`data/facts/<service>.jsonl` and every mechanical check read the quote as before. The evidence line under each quote
(`> — [title](url)`) is unchanged: its host passed M2.

Test added: `test_facts_holes.py` `SheetLinks.test_sheet_prints_the_link_text_of_a_quote_only` (a table row with a
console link, a sentence with a docs link, a sentence with an image; no `](` in any quote line; the stored quotes are
unchanged).

## 3. A failed finalize puts the front matter status back (W0 ledger problem 1)

`ledger.stage_end` reads the `status:` value of every hand file (`ledger._front_status`, new) before it writes the
stage's status (`draft`, `reviewed`, `ready`), and writes the previous values back when the gates end in FAIL or
UNAVAILABLE. `_write_front_status` accepts a dict of relative path to value for that; its one-value form and its return
value are unchanged. A PASS still leaves the new status in place; `--fail` returns before the write, as before; the
`gate` command never wrote the front matter and still does not.

Tests added: `test_ledger.py` `test_must_fail_failed_finalize_puts_the_front_matter_status_back` (finalize with a
failing lint fake: both hand files are byte-for-byte as before) and
`test_failed_fix_stage_keeps_the_previous_status_and_a_passed_one_writes_it` (a failed `fix` keeps `drafted`; a passed
`fix` writes `reviewed`).

## Notes for the contract documents

- `TOOLS.md` 3.3 says the front matter status is written before the gates run; add: "and put back when the stage does
  not pass".
- `TOOLS.md` rule M7 and the C109/P109 rows: "in" means the `holds_display` comparison of `SPEC.json fact_links.comparison`.
- The fact sheet row of `TOOLS.md` section 5: a quote prints with its link and image text only.
