# W0c: heading-scoped evidence (M4)

Date: 2026-10-11. Scope: AWS pages that state a value as a heading and a short value line (`### Exam duration`, then `130 minutes`). Before this change such a value could not become a fact: M4 needs 8 words or a complete sentence, and a quote may not cross a heading.

## What changed

| File | Change |
|---|---|
| `_build/schemas/fact.schema.json` | Evidence items get an optional `heading` (string or null), next to `table_header`. |
| `tools/saalib/facts.py` | New `_heading_scope` (M4 for an evidence item with `heading`). `_check_evidence` uses it in place of the word and sentence rules when `heading` is set; all other checks (M2, M3, M5, M8 and the rest) still run on the quote. |
| `tools/saalib/facts.py` | `content_hash` adds `heading` only when it is set, so the hash of every existing fact and every stored vote is unchanged. A changed heading voids the votes. |
| `tools/saalib/facts.py` | `facts packet`: the evidence item has `heading` next to `quote` (only when set), and `context` is taken around the value line under that heading. The entail instruction has one more sentence: read a quote with a `heading` together with the heading. |
| `tools/saalib/facts.py` | `render_sheet` prints `> <heading>: "<quote>"`. `facts card` is unchanged. |
| `tools/saalib/facts.py` | `facts adopt --heading H [--line N]`: quote = the N-th non-empty line under the one heading line whose text is H (default 1), `heading` = the heading text as on the page. Exit 1 when H matches no heading or more than one, or the line does not exist before the next heading. |
| `tools/saalib/facts.py` | The M4 messages for a 2 to 7 word quote now say that a value line under a heading needs `heading` (`facts adopt --heading`). Text only. |
| `_build/style/TOOLS.md` | 5.2: one sentence on the heading-scoped quote. 5.3: the `adopt` row names `--heading H [--line N]`. TOOLS.md is at 7,378 of 7,400 words. |
| `_build/style/TOOLS-rules.md` | R8 M4: the full rule. R8 Votes: `heading` is in the content hash when set. R8 Fact sheet: the sheet and packet form. |
| `_build/schemas/vote.schema.json` | The `content` description names `heading`. |
| `tools/tests/fixtures/book/_build/corpus/snap/aws/fixture/certification/certified-widget-specialist.{txt,meta.json}` | New invented page (`fixture: true`) with the heading and value-line layout of the real certification page. No fixture fact cites it; `widget.jsonl` and the gate hash are unchanged. |
| `tools/tests/fixtures/README.md` | One row for the new page. |

## The rule (M4, evidence item with `heading`)

1. The quote is one whole line of the snapshot: equal to a `text` line of `ctx.layout` after `normalize_text` (not a heading or a table row), 1 to 80 words.
2. `heading` is the text of a heading line of the snapshot, and it is the nearest heading above that line.
3. The line is within the next 5 non-empty lines after the heading.
4. `table_header` is empty.

If one of these fails, M4 gives a message that says what to do. If the evidence item has no `heading`, nothing changes.

## Tests (`tools/tests/test_facts_holes.py`, class `HeadingScopedQuotes`, 10 tests)

- Must pass: `130 minutes` under `Exam duration` is added as `mech-pass`. It then goes through batch, packet (`heading` and context), vote, finalize (verified), the sheet line `> Exam duration: "130 minutes"`, and an unchanged card shape. The 5th line under a heading passes.
- Must fail (M4): a short quote without `heading`; a heading that is not the nearest one (`Category`); a quote that is not a whole line (`65 questions`); a heading not in the snapshot (`Exam length`); the 6th line under a heading; `heading` together with `table_header`; `adopt --heading` with an unknown heading (exit 1, nothing stored).
- Hash: a different heading gives a different content hash. `heading: null` gives the same hash as no heading.
- `adopt --heading` builds the evidence, also with `--line 5`.

Suite: `run.py facts` 99 tests OK (89 before). Full suite 798 tests OK. `saa.py selftest` ok (failures 0, errors 0, every module has a must-fail test).

## Real book

- Input `_build/work/01-how-the-exam-asks/fix-01-duration-heading.json`: the fact of `fix-01-duration.json` with the evidence `{"source_id": "www/certification/certified-solutions-architect-associate", "url": "https://aws.amazon.com/certification/certified-solutions-architect-associate/", "quote": "130 minutes", "heading": "Exam duration"}`. The stale note ("M4 rejects it") is replaced by a note on the heading-scoped quote. The original file is unchanged.
- `facts add --by fix-01-duration`: `exam-duration-minutes` added, status `mech-pass`, rev 1, home chapter 01, no conflict. `facts verify exam-duration-minutes`: ok. The packet shows `heading: Exam duration`, `quote: 130 minutes`, and the exam overview lines as context.
- Batches: `facts batch --chapter 01 --lens entail --size 40` made `01-entail-005` (1 fact: `exam-duration-minutes`). `--lens currency` made no batch (0 facts: the fact is `stable` with no change items, so it needs no currency vote).
- Nobody has voted. Nothing is finalized.

## Known limits (not changed)

- The schema keeps `quote` `minLength` 8, so a value line shorter than 8 characters (for example `720`) still cannot be quoted.
- `site.py` shows `table_header` for evidence but not `heading`, so the web app's evidence view shows `130 minutes` without its heading. The site owner should add it.
- RULINGS names `exam-duration` among the four facts the web shell reads. That id is rejected; the new id is `exam-duration-minutes`.
