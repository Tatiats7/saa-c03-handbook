# W0c docs catch-up: the contract documents follow the code

Date: 2026-10-09. Input: `gate-break-fixes.md` (the 8 items of "Changes that the contract documents must take over", and the Notes), `w0-integration.md` (fixes 1 to 4), `_build/tmp/reg-16-30/result.json` (`tool_changes`), `w0-result.json` (every `deviations` list of the module builders) and `w0c-tool-fixes.md`. Every behaviour was confirmed in the code before the document changed (function read; `lint 99 --draft` run on a sandbox copy of the fixture, `_build/tmp/docs-check`). No code changed. `RULINGS.md` and `STYLE.md` were not touched.

**Word budgets.** `test_contract` caps `TOOLS.md` at 7,400 words, `TOOLS-items.md` at 4,800 and `CONVENTIONS.md` at 4,900, and all three stood at their caps. Raising a cap is a code change, so the detail went where contract fix 1 put its additions: three new sections in `TOOLS-rules.md` (R8 facts: mechanical checks and votes, moved from `TOOLS.md` 5.2; R9 task rules T101 to T201, moved from `TOOLS-items.md` 8.1; R10 question bank additions) and one in `CONVENTIONS-2.md` (F2 fact links: what the lint matches). The budgeted files keep short corrected sentences with pointers. Sizes after: TOOLS.md 7,326, TOOLS-items.md 4,389, CONVENTIONS.md 4,895 (`tools/tests/doc_sizes.py`). `python3 aws-saa-book/tools/tests/run.py` ran 788 tests, all pass; `saa.py selftest` is ok.

## Items documented (document, section, what changed)

Gate-break fixes, "Changes that the contract documents must take over":

1. Every fact needs an entail vote: `TOOLS.md` 5.4 required lenses and rule 5 (`entail` always; no fact is verified on `mech-pass` alone), 5.3 must-fail tests; `TOOLS-rules.md` R7 decision 9 marked superseded, R8 "Votes".
2. `facts amend --by` for a rev-changing patch: `TOOLS.md` 5.3 amend row, 5.7, vote row (exit 3 on `unknown`); `TOOLS-rules.md` R8 "Votes" (`amended_by`, an amender cannot vote).
3. Vote `content` hash and `tests/stamp_fixture_votes.py`: `TOOLS.md` 5.3 vote row, 5.4 rule 1; `TOOLS-rules.md` R8 "Votes" (what the hash covers) and "Fixture votes" (fixture only, nothing to migrate).
4. `q adjudicate` preconditions (pack of the same lens and round, three different solvers, `stem_only`, `case`): `TOOLS-items.md` 7.4; `TOOLS-rules.md` R10 "`q adjudicate`" (the full list, citations with 6 words and one own-fact citation).
5. `q add` stores `authors`; `question.schema.json` has `authors` and `verification.edits`: `TOOLS-items.md` 7.1; `TOOLS-rules.md` R5 `--replace` table (edits, Q207), R10 "`q add`"; `CONVENTIONS-2.md` J1 table, J2 "Copies" and "Blind solving".
6. `sync CH` writes and checks fact sheets: `TOOLS-items.md` 6.2 (chapter services plus every linked service; `--all --check` reports a sheet that no verified fact produces); `TOOLS.md` 6.1 L601 row (a missing sheet or entry, d).
7. `SPEC.json` `lint.number_with_unit`: the real file already held the longer `units` and `count_nouns` lists; its `number_words` sentence was wrong and now says which number words L304 matches (above twelve or compound).
8. Chapter 00 `calendar-preview.md` is L101: `TOOLS.md` 6.1 L101 row (a file the template does not list, d); `CONVENTIONS-2.md` S1.

Gate-break Notes (M4 refuses a quote across a multi-line link; a table cell is quoted as its row): `TOOLS-rules.md` R8 M4.

Gate-break grounding and practice tables (behaviours that the old sentences contradicted): `TOOLS-rules.md` R8 M2 (provenance, fixture snapshots), M3 (hidden text), M4 (sentence boundaries, placement), M5 (compare by value, `50K`, number words, a unit after one or two words, claim and `changed.was`), M7 (`holds_display`), M8 (heading crossing, more boilerplate); `TOOLS.md` 6.1 L303, L304, L306 rows and the parsing paragraph; `TOOLS-rules.md` R2 (number with a unit, absolute words with `EXTRA_ABSOLUTE`, what L304 reads, one link per number with a unit, whole sentences in AWS quote blocks), R3 (new-code table F04, Q207, Q302, Q401, D04, X03); `TOOLS-items.md` 7.2 Q102, Q104, Q105, Q113 rows, 7.3 (Q401, `packs.jsonl`), 7.5 (`qbank.similarity`), 7.6 C105, C106, P102, P109; `TOOLS-rules.md` R9 T103 to T109, T113 and R10; `TOOLS.md` 3.1 diagrams gate (D04); `TOOLS-diagram.md` (D04 note); `TOOLS.md` section 1 (`_build/qbank/packs.jsonl`); `CONVENTIONS.md` F and D12 (pointers), `CONVENTIONS-2.md` F2 (the matching rules in writer's terms), J3 (spoken limits), J5 (commands, tags, cleanup, cost line).

W0 integration fixes 1 to 4:

- Fix 1 `holds_display`: `TOOLS.md` section 2 (`lint.holds_display`, `link_text_extra`), 6.1 L303; `TOOLS-rules.md` R1; `TOOLS-items.md` C104, C109, P109; `CONVENTIONS-2.md` F2. (`SPEC.json` `fact_links.comparison` already said it.)
- Fix 2 `selftest` must-fail names: `TOOLS.md` 0.10 already said `test_must_fail_<what>`; nothing to change.
- Fix 3 sandbox diagrams read the real `icons.json`: `TOOLS-diagram.md` "Icons" line.
- Fix 4 `registry check` text form with the item in brackets: `TOOLS.md` 4.3.

Registry `tool_changes` (reg-16-30): `TOOLS.md` 4.3 R06 (a guide root is in the corpus when its `saa.py guide` index exists; `--fetch` builds it); 4.2 (patch keys `cards` and `notes`, `--cards`, `--replace cards`); `TOOLS-rules.md` R5 "Registry".

w0-result deviations:

- ledger: `TOOLS.md` 3.3 (UNAVAILABLE, X03, the attempt is given back; transitive staleness), 3.1 counts gate (B10 only while a stage other than `finalize` is still `stale`; the four `--ship` calls, in R1), section 2 `mark_stale` (dependents), 3.4 `gate --all` JSON (`missing_gates`, `unavailable_gates`).
- facts: `TOOLS.md` 5.3 verify and finalize rows, section 2 (`gate_final` runs F04 and the M checks); `TOOLS-rules.md` R8 (F04; M5 on the claim and `changed.was`; unit equivalences; R1 `facts-final` row).
- registry: `TOOLS.md` 4.1 step 1 (missing seed; `book` keys from the seed), step 3 (role `overview`, bullet text stripped).
- lint: `TOOLS.md` 6.1 W901 (a words-table row defines the term), W902 (the `startup.cast` check is not implemented); `TOOLS-rules.md` R1 `word_count` (HTML tags, hyphen chains). The sync generators living in `_sync.py` need no contract change (`sync` is still a `lint` subcommand).
- qbank: `TOOLS.md` 0.6 and `TOOLS-items.md` Q101 (an item's schema error is Q101, not X01), Q112 (recomputed), 7.3 Q401.
- lab: `TOOLS-items.md` 8.3 (`--endpoint-url` on every command, dead proxy) and `TOOLS-rules.md` R9 (T105 built-in patterns, T101 not X01, `check-cli` report keys `tag_options` and `warnings`).
- corpus and feeds: `TOOLS-corpus.md` and `TOOLS-feeds.md` already describe every deviation (meta keys, `fetch(source_id=)`, `--reextract`, `guide --id --revalidate`, `search --per-file`, `show --occurrence`, `tables --all`; tags from items, merged `cases/index.jsonl`, `cases tags`, the markdown FAQ parser, the extra row fields). Confirmed against `corpus.py` and `feeds.py`; nothing to change.
- diagram core and kinds: `TOOLS-diagram.md` already names the Helvetica stack, the dash patterns, `layout_sequence.py`, `asides`, the compare panel files and `dg-cmp`; added: group labels are regular weight, 11.5 units, ink colour ("How layout and routing behave").

w0c-tool-fixes notes: `TOOLS.md` 3.1 front matter status (put back when the stage's gates do not pass); `TOOLS-rules.md` R8 M7 and the C109/P109 rows (`holds_display`); `TOOLS.md` 5.8 and R8 "Fact sheet" (a quote prints with link and image text only).

Also corrected on the way: `TOOLS.md` 0.13 (the unchanged fixture gives three W901 warnings, seen in the sandbox run; W0 item 8); `CONVENTIONS-2.md` J5 said `aws configure export-credentials` is allowed, but T105 bans it as "prints credentials" (practice hole 49, RULINGS rule 9), so J5 now follows the code.

## Code-versus-document disagreements left (not changed in the documents)

1. **`qbank.gate_cards` and `gate_speak` drop the `ship` option.** `ledger.gate_counts` calls `gate_cards(ch, ship=True)` and `gate_speak(ch, ship=True)` (`ledger.py` 614), but both functions call `cards_lint(ctx, ch)` and `speak_lint(ctx, ch)` without `ship` (`qbank.py` 1573 to 1578), so C201, C204 and P201 never block in the `counts` gate (`lab.gate_tasks` passes `ship` on correctly). The documents keep the contract (R1: the counts gate uses the `--ship` forms). The fix is one line per function; `test_ledger` only tests the tasks path with a fake gate.
2. **W902 cast check.** `TOOLS.md` 6.1 promised a check of a capitalised name beside the startup name against `startup.cast`; `lint.py` does not implement it (the builder found the rule too vague). The row now says so; the orchestrator decides whether to specify it or drop it.
3. **P109 spoken forms** compare number words as substrings (`two hundred widgets` inside `five thousand two hundred widgets` passes), as `w0c-tool-fixes.md` reports; documented as an open rest in R10, caught by the technical red team lens.
4. **The unchanged fixture gives three W901 warnings** (`shelf`, `widget`, `Regional` not bold at first use), which the fixture README does not list (W0 item 8). `TOOLS.md` 0.13 now lists them as known; either the fixture or `tools/tests/fixtures/README.md` should change.
5. **Document budgets.** The caps in `test_contract.py` (7,400 / 4,800 / 4,900) leave no room for further in-place additions to `TOOLS.md` or `CONVENTIONS.md`; new detail must go to `TOOLS-rules.md` or `CONVENTIONS-2.md`, or the caps must be raised (code).
