# Gate break fixes

Date: 2026-10-05. Input: `gate-break-grounding.md` (14 root holes, H1 to H14) and `gate-break-practice.md` (49 holes, numbered by attempt).

Method for every hole: a regression test that repeats the breaker's input (it failed before the fix), then the fix, then the suite. No change to `common.py` or `saa.py`.

## Result in one view

- Grounding (14 root holes): 7 closed in full (H1, H2, H3, H4, H6, H9, H14). 7 closed for the reported inputs with a stated rest that a review step must catch (H5, H7, H8, H10, H11, H12, H13).
- Practice (49 holes): 43 closed, 3 narrowed with an open rest (20, 44, 56), 3 open (14, 36, 41). One sub-case, 47-v7, is no hole by the written rule and stays allowed.
- Suite: `python3 aws-saa-book/tools/tests/run.py` ran 744 tests, all pass (baseline before the work: 582). During the work another agent changed `saalib/diagram/route.py` and `saalib/diagram/lint.py` (edges of one step drawn as one trunk); two tests of `test_diagram.py` failed for some minutes for that reason and pass again.

New test files: `tests/test_facts_holes.py` (27), `test_lint_holes.py` (25), `test_qbank_holes.py` (36), `test_lab_holes.py` (14), `test_diagram_holes.py` (6). Helper: `tests/stamp_fixture_votes.py` (fixture only).

## Grounding holes

| Hole | Status | What changed | Where |
|---|---|---|---|
| H1 non-hard fact verified with no vote | closed | Every fact needs an entail vote. `hard` no longer switches the vote off; it still decides M13 and the audit sample. | `facts.required_lenses` |
| H2 unit or size of a number lost | closed | M5 sees a unit after one or two words (`7 full hours`), collapses spaces, reads `50 thousand` and `50K` as 50000, and reads compound number words (`nine hundred`). Numbers are compared by value. | `facts._scan_numbers`, `_gap_unit`, `_word_value`, `_value` |
| H3 quote starts or ends inside a sentence | closed | M4: a quote of 8 words or more starts at a sentence start and ends at a sentence end of the snapshot (or at a line start or end). L306: a quote block holds whole sentences of the evidence quote, or ends at the end of quoted speech. | `facts._placement`, `lint._whole_sentences` |
| H4 text in `<...>` invisible | closed | M3: a quote with a tag, a link target, a list or heading prefix, a zero-width character or a line break must stand literally on the page. Also closes a variant I found: a number hidden in a list prefix (`up to\n999) 50 widgets`). | `facts._hidden_text` |
| H5 snapshot not from the fetch tool | narrowed | M2: the meta file needs `sha256` and `text_sha256`, the `.txt` must have that hash, the `.raw` body must exist with its hash, and `fetch.log.jsonl` must name the source. A fixture snapshot (`fixture: true`) counts only in a sandbox. Closes F19 and F22 as reported. | `facts._provenance` |
| H6 page furniture, flattened table | closed for both inputs | M4 refuses table text that is not quoted as a row with `table_header`. M8 refuses a quote that runs across a heading, and five more navigation phrases. Other navigation text now waits for the entail vote (H1). | `facts._check_evidence`, `BOILERPLATE` |
| H7 voter is a free label | narrowed | Labels are compared without case, spaces and punctuation. A voter votes once per fact, rev and lens. Every counting vote counts, so a later positive line cannot cancel a negative vote. Agents that amended a fact cannot vote on it. Closes F14 and F15. | `facts.voter_key`, `_counting`, `cmd_vote` |
| H8 votes bound to rev only | closed for F25, narrowed for F24 | `facts vote` stores `content` = SHA-256 of claim, kind, hard, values, qualifiers, changed, change_items, derivation, volatility and the evidence quotes. A vote counts only while the fact has that hash. | `facts.content_hash`, `vote.schema.json` |
| H9 amend removes the need for votes | closed | Follows from H1. `facts amend` now needs `--by` for every patch that changes rev, and stores `amended_by`. | `facts.cmd_amend`, `fact.schema.json` |
| H10 L304 misses a number with a unit | closed for 7 of 8 inputs | Text is NFKC-normalised, entities decoded, zero-width characters removed. `9000+`, one or two adjectives before the unit, and number words above twelve or compound are matched. More units and count nouns in the real `SPEC.json`. | `lint._inline`, `Matcher` |
| H11 L304 misses an absolute claim | closed for all inputs | Same normalisation, plus 19 fixed synonyms and spellings (`can not`, `no more than`, `at least`, `invariably`, `no one`, `nobody`, `unlimited`, ...). | `lint.EXTRA_ABSOLUTE` |
| H12 places that L304 does not read | narrowed | Now read: inline code that is prose, a question that holds a number with a unit, `<summary>` lines. A Markdown file that the template does not list is L101. | `lint._code_text`, `_ground`, `_units`, `lint_chapter` |
| H13 fact link proves only a substring | closed for L19 to L22 | L303: the link text holds no other number and no negation beside the displays. `2 500 widgets` does not hold `500 widgets`. L304: a number with a unit outside the fact link still needs a link. | `lint.link_text_extra`, `holds_display`, `_ground` |
| H14 sync gate skips fact sheets | closed | `sync CH` builds and checks the sheets of the chapter's services and of every linked service. `sync --all --check` reports a sheet that no verified fact produces. Lint L601 reports a missing sheet or entry. | `_sync._outputs`, `_sync.run`, `lint._links_and_ids` |

### Open rest, and the step that must catch it

- **H5.** An agent that can write files can also write a `.raw`, both hashes and a log line. Catch: `saa.py freshen` (without `--offline`) and `audit sample --revalidate` fetch every cited page again and fail a quote that the real page does not hold. Run `freshen` for the chapter before `finalize`, and for the book in W14.
- **H7 (F13).** One agent with two labels. The tool cannot know who is behind a label. Catch: the orchestrator sets `SAA_AGENT` for each agent and never lets the miner agent run `facts vote`; the audit re-derivation (other agent, question only) is the second net.
- **H8 (F24).** A vote line written by hand with the right hash passes. Same catch as H7, plus the `facts-final` gate record lists the SHA-256 of the vote log, so a later hand edit makes the gate stale.
- **H10 (L11, L17).** A unit outside the SPEC list, and number and unit in two sentences. Catch: the unsupported-claim hunter lens of the chapter review.
- **H11.** A synonym outside the list. Same lens.
- **H12 (L15, L25, L26).** A `no-fact` marker (warning W308 by design) and sections or callouts with grounding `example` (exempt by ruling). Catch: the claims reviewer reads every W308 line and every decision record against "the story never teaches a fact".
- **H13 (L23).** A real fact link on the wrong subject. Catch: the technical red team lens.

## Practice holes

| Attempt | Status | What changed |
|---|---|---|
| 3 same option text twice | closed | Q102 compares normalised option texts. |
| 4, 5 key leaked by length | closed | Q104 also fails when the key is longer (or shorter) than every wrong option by 3 words and by more than the spread, at any mean. |
| 6 key made of stem words | closed | Q113 also measures the share of the key's words that stand in the stem. |
| 7 option named by position or letter | closed | Q105: `the second option`, `(C)`, `B is ...`, `option 2`. |
| 8 exact copy under a new id | closed | `q add` refuses a duplicate (Q302). `q lint CH` and the `questions` gate report duplicates of the chapter's questions. |
| 9, 27 reordered copy, padded copy | closed | New `qbank.similarity`: stem shingles, or 85% common words of stem plus options, or the same options with one stem inside the other. Used by `q dedupe`, Q302 and K04. |
| 10 negative stem in lowercase | closed | Q105 reads the question sentence for `which ... is not`, `except`, `incorrect`, `least likely`. |
| 11 `None of these options` | closed | Q105: an option does not point at other options. |
| 14 shuffle is reversible | open (partly) | The seed is public and every agent can read the book folder. Catch: Q202 (key position share) under `q lint --ship`, and the exam-validity lens. |
| 17, 18 no solver, one solver, author as solver | closed | `q adjudicate` exits 3: each file names a solver, the three are different, and none is in `authors` (set by `q add --by`). |
| 19 lens evidence missing | closed | Exit 3 without `stem_only` (closed) or `case` (ambiguity). |
| 20 citations without meaning | narrowed | A quote needs 6 words. All labels with one identical citation fail. One citation must be a fact of the question or a quote from a page that is evidence of one. Rest: a citation that is real but beside the point. Catch: exam-validity lens. |
| 21 two rows for one id | closed | Exit 3. |
| 22 old answers for a replaced question | closed | `q pack` records a hash of what the solver saw in `_build/qbank/packs.jsonl`. `q adjudicate` refuses answers for a question with no pack or another text. |
| 23 more than one edit | closed | Q207 on the second `--replace` in round 1 (`verification.edits`). |
| 24 rejected question returns | closed | `q add` compares with rejected items and `rejected.jsonl` (Q302). |
| 25 `set-status verified` by hand | closed | Q206. |
| 28, 29 copy inside a mock, copy of a drill question | closed | K04. |
| 30 manifest edited by hand | closed | K01 for `minutes`, `domain_split` and `counts`. |
| 32 list answer | closed | C105: one comma with `and` or `or`; two slashes. |
| 34, 39 words joined by hyphens | closed | `lint.word_count`: four or more joined parts count as their parts. |
| 35 wrong number as a word | closed | C109 and P109 read number words above twelve and compound ones before a unit. |
| 36 card contradicts its fact | open | No mechanical tie between a sentence and the meaning of a fact. Catch: the chapter review must read `cards.json` (technical red team lens); cards have no blind check today. |
| 37 near-duplicate front | closed | C106 also when one front holds 95% of the other. |
| 40 long follow-up answer and key point | closed | P102 limits: key point 30, follow-up answer 60, must_not_say 40 words (SPEC keys optional). |
| 41 absolute claims in a script | open | Same reason as 36. Catch: technical red team lens on `4-say.md`. |
| 42 spoken numbers | closed | P109: seventeen to nineteen, dozen, and a unit after one or two words. |
| 44 creating verbs outside the list | narrowed | Creating verbs now include import, register, restore, request, provision, purchase and `s3 mb`. `put-<noun>` needs `delete-<noun>` or the delete of its parent. T103: steps that change the account need a cleanup command that deletes. Rest: other verbs that make a resource (`start-...`, `enable-...`). Catch: `tasks emulate` and the technical red team. |
| 45 cleanup of another resource, `--dry-run` | closed | T107: the cleanup names the capture variable or the name of the created resource; `--dry-run` and `--generate-cli-skeleton` do not count. |
| 46 `stop-instances` for `run-instances` | closed | T107. |
| 47 security group open to the world | closed, except v7 | T105 for all rule operations, any IPv4 range shorter than /8 and IPv6 range shorter than /16 in any spelling, prefix lists on admin ports. T104 refuses `--cli-input-json` and `file://` for rule and policy options. v7 (port 443 to the world) is allowed by RULINGS rule 9 and stays allowed. |
| 48 public exposure by other commands | closed | T105: policy with principal `*` and Allow without a condition, `--publicly-accessible`, snapshot or image shared with `all`, `--principal *`, `--auth-type NONE`. |
| 49 credentials, curl | closed | T105: `configure export-credentials`, `get-session-token`, metadata credentials. T104: curl options are an allow-list. |
| 50 two commands, redirects, variables | closed | T104: line break, `>`, `<`, `<(`, `${NAME}`, `$name`. |
| 51 tag text anywhere | closed | T106 and T108 search only in the values of tag options (and filter options for verify). |
| 52 cost hidden behind `$0` | closed | T109 reads `4.50 USD`, `USD 4.50`, `5 dollars`, `20 cents`, and fails money words without an amount. |
| 53 a Look that deletes | closed | T103: a Look holds only read-only operations. |
| 54 untaggable create | closed | T106: the name starts with `saa-`, or a later step tags the resource. |
| 55 CLI model | closed | `helpers/cli_model.py`: stray words, single-dash options, shorthand keys, enum values, `--query` syntax and fields against the output shape. Tested with the real helper from the uv cache. |
| 56 hand-written CLI report | narrowed | T113 needs one ok row per command and the pinned awscli version. A file is still no proof of a run. Catch: the `finalize` step runs `tasks check-cli CH` itself before the `tasks` gate. |
| 58 raw diagram, labels in one place | closed | Raw kind: text boxes from the font table; `label-overlap` and `text-overflow`. |
| 59 number in a label | closed | `label-number` for every kind: a number with a unit in a label stands in the claim or a `say` sentence. |
| 60 claim of two sentences | closed | Any text after a sentence end. |
| 61 SVG not from its spec | closed | Gate `diagrams` D04: the SVG file equals the output of the spec. |

## Changes that the contract documents must take over

These change `TOOLS.md`, `TOOLS-items.md` or `TOOLS-rules.md`; I did not edit those files.

1. Every fact needs an entail vote (was: hard facts only). This is stricter than RULINGS "entailment vote on every hard fact"; it is the only mechanical closure of H1 and H9.
2. `facts amend --by LABEL` is required for a patch that changes rev.
3. Vote lines carry `content`; a fixture or migration needs `tests/stamp_fixture_votes.py` (fixture only). The real vote log does not exist yet, so nothing must be migrated.
4. `q adjudicate` needs a `q pack` of the same lens and round first, three different solvers, `stem_only` and `case`.
5. `q add` stores `authors`; `question.schema.json` has `authors` and `verification.edits`.
6. `sync CH` writes and checks fact sheets.
7. `SPEC.json` (real): more units and count nouns in `lint.number_with_unit`.
8. Chapter 00: `calendar-preview.md` is now L101 without `--draft` (a warning with `--draft`). This matches the ruling that the preview file is removed when chapter 00 is finalized.

## Notes

- New strictness can refuse honest input: a quote that crosses a multi-line Markdown link cannot be placed (M4), and a table cell must be quoted as its row. The message says what to do.
- `tools/helpers/break_grounding.py` and `break_practice.py` were not changed; run them again to confirm from the breaker's side.
