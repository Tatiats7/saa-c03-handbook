# W0 integration report

Date: 2026-10-04 local (the tool writes UTC dates, so files say 2026-10-05).

## Result in one view

| Item | Result |
|---|---|
| Test suite (`python3 aws-saa-book/tools/tests/run.py`) | 582 tests, 0 failures, 0 errors (579 before this work, all passing; 3 regression tests added) |
| `saa.py selftest` | ok: every one of the 10 required modules has a must-fail test (it failed before the fix below: `corpus` had 0) |
| End-to-end smoke test | `SMOKE OK`: 38 commands, 6 of them must-fail steps, 15 content checks |
| Real registry | built from the live exam guide: 53 chapters, 4 domains, 14 task statements, 189 bullets, 119 in-scope entries (118 unique), 41 out-of-scope |
| `saa.py status` (real book) | runs: `53 chapters: planned=53` |

## What I ran

1. `python3 aws-saa-book/tools/tests/run.py` (before and after the fixes).
2. `python3 aws-saa-book/tools/helpers/smoke.py run`. The transcript is `_build/reports/w0-smoke.log`. The sandbox is `_build/tmp/smoke`. Run it again at any time; it rebuilds the sandbox and keeps the two fetched pages, so a second run makes no request.
3. `saa.py guide https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/` in the real book (exit 2: an exam guide has no history page and no quotas page; that warning is expected).
4. `saa.py registry build --json` in the real book (exit 2: six unmapped service names, listed below).
5. `saa.py registry check` (saved to `_build/reports/w0-registry-check.txt`), `saa.py selftest`, `saa.py status`.

## The smoke test

Sandbox: a copy of the test fixture book (chapter `99-sample`, fixture `SPEC.json`) with the service key `vpc` added to chapter 99. The script patches the sandbox `data/book.json`, `_build/registry/services.json` and the front matter of `1-fast.md` for that. Inputs are in `tools/helpers/smoke/`.

Steps, all with real AWS text:

- **Corpus.** Fetched `nat-gateway-basics.html` (Markdown twin, 5,385 bytes) and `amazon-vpc-limits.html` (11 tables). `fetch https://example.com/` is refused with exit 4.
- **Facts.** Three facts added with verbatim quotes (`vpc-natgw-bandwidth`, `vpc-natgw-no-security-group`, `vpc-natgw-az-scope`). One fact adopted through the table path (`vpc-natgw-per-az-quota`, table 2 row 2, header `Name | Default | Adjustable | Comments`). A fact that claims 45 Gbps against a quote with 100 Gbps is rejected (M5). `facts verify`: 4 of 4 ok. Batch, packet (no author, status or votes in it), votes (the author's own vote is refused, V01), finalize: 4 verified. `facts render` wrote `facts/vpc.md`; `facts card` prints the ready-made links.
- **Chapter text.** One Go deeper block with five links to the four facts was inserted into `99-sample/2-deep.md`. `sync 99` wrote five files; `sources.md` lists both AWS pages. `lint 99`: 0 errors. With `up to 45 Gbps` as the link text, lint fails with L303. After the number is restored, lint passes again.
- **Questions.** Two original questions about NAT gateways added (Q101 to Q116 pass). Three blind packs (only `id`, `type`, `select`, `stem`, `options`; option order differs between lenses). `q adjudicate`: both pass, status `verified`.
- **Task.** One Look task added; `tasks lint 99` has no error (warnings T201 and T113, both expected). `tasks check-cli 99` ran through `uv`: the two real `aws ec2 describe-...` commands are ok, the fixture's seven invented `aws widget` commands fail as designed.
- **Diagram.** `diagram build sample-natgw-zones`: ok, 444 x 550, 6 nodes, 5 edges, 0 crossings.
- **Ledger.** `stage begin 99 verify-facts`: GO. `stage end`: PASS, gate `facts-final` ok, chapter status `facts-verified`. `stage begin 99 prose`: BLOCKED (`prereq:brief`), exit 3.
- **End state.** `sync 99 --check`: fresh. `gate 99 --gate lint`: PASS. `status`: `99 sample deep W0 facts-verified next=brief facts=11/11 q=4/4`.

## What I fixed

| # | Problem | Fix | Regression test |
|---|---|---|---|
| 1 | **Lint accepted a wrong number in a fact link.** L303 was a plain substring test, so the link text `up to 45 Gbps` passed because it holds the display `5 Gbps`. `150 widgets` passed against `50 widgets` in the same way. This is the rule that protects hard rule 1. | New `lint.holds_display(text, display)`: substring, but a display that starts or ends with a digit must not touch another digit of a longer number (`45`, `1,500`, `0.5`, `4430`). Used by L303 in `lint.py`, by the link check and the C104 cloze check in `qbank.py`, and by the fallback in `lab.py`. The `fact_links.comparison` sentence in `SPEC.json` (real and fixture) now says this. | `test_lint.py`: `test_must_fail_link_text_with_wrong_number_that_ends_like_the_value`, `test_holds_display_number_boundaries` |
| 2 | **`selftest` failed:** module `corpus` had no test named `test_must_fail_*` (its 12 must-fail tests were named `test_*_must_fail`). | Renamed the 12 tests in `test_corpus.py` to the contract's form. No test logic changed. | `selftest` itself (it now counts `corpus: must_fail=12`) |
| 3 | **Diagrams could not be built in any sandbox book.** `diagram build` under `--book-dir` reported every icon as unknown, because a sandbox has no `diagrams/icons.json`. The `diagrams` gate would fail in every sandbox test for the same reason. | `diagram/icons.py` `load()` reads the real book's `icons.json` when the sandbox has none (the same idea as the schema fallback). Writing still goes only to `common.BOOK`. | `test_diagram.py`: `test_sandbox_book_without_icons_reads_the_real_manifest` |
| 4 | **`registry check` text did not say which bullet.** It printed `data/book.json: R03 bullet is in the bullets of no chapter` 189 times. | `registry._finding_text` appends the item in brackets when a finding has a file and an item: `... no chapter [1.1.K1]`. JSON output is unchanged. | `test_registry.py`: added to `test_must_fail_bullet_in_no_chapter` |

New files: `tools/helpers/smoke.py`, `tools/helpers/smoke_steps.py`, `tools/helpers/smoke/` (inputs). `common.py` and `saa.py` were not changed and need no change.

## The real registry

Files written: `data/book.json`, `_build/registry/exam-guide.json`, `_build/registry/services.json`, and the 9 exam guide pages under `_build/corpus/snap/docs/aws-certification/latest/solutions-architect-associate-03/`.

- Domains: 4, weights 30 / 26 / 24 / 20 (sum 100).
- Task statements: 14.
- Knowledge and skill bullets: 189. Per task: 1.1: 11, 1.2: 10, 1.3: 11, 2.1: 23, 2.2: 20, 3.1: 5, 3.2: 10, 3.3: 13, 3.4: 8, 3.5: 14, 4.1: 21, 4.2: 15, 4.3: 14, 4.4: 14.
- In-scope services: 119 list lines, 118 unique names. Out-of-scope: 41.
- No chapter was mapped (as asked).

## What still does not work, or is not proven

1. **Six in-scope names have no service key yet:** Amazon Kinesis, Amazon OpenSearch Service, AWS Auto Scaling, AWS CLI, Amazon Managed Service for Prometheus, Amazon Route 53. The automatic match finds no chapter key for them. The mapping agent must add them with `registry set CH --map "Official name=key"`.
2. **`registry check` fails on the real book, as expected before mapping:** 209 errors (189 bullets and 14 task statements in no chapter, 6 services without a key) and 54 warnings. It must reach 0 errors after the mapping step.
3. **The substring weakness of fix 1 exists in three more places that I did not change:** M7 (a display is a substring of the claim or quote), `numbers_outside_displays` in `qbank.py` (C109, P109) and the re-derivation match in `facts.py`. They are less exposed, because M5 already checks every number of a display against the quote. They should use `lint.holds_display` too.
4. **A table-row quote prints raw Markdown in the fact sheet.** `facts/vpc.md` shows `[Yes](https://console.aws.amazon.com/servicequotas/...)` inside the quote. The reader file then holds a link to a host outside the allow-list. `facts.render_sheet` should print the link text only.
5. **The smoke chapter is the fixture chapter, not a chapter under the real `SPEC.json`.** The real templates need a full chapter, so the first proof of the real lint rules on real prose is the IAM pilot.
6. **Stages after `verify-facts` were not cycled in the smoke test** (the fixture has no `brief.json`). The unit tests cover them; no real chapter has gone through them.
7. **Independence is not proven by the smoke test.** One script wrote the facts, the votes and the solver answers (with different labels). The run proves the mechanics, including the refusal of an author's vote.
8. **The unchanged fixture gives three W901 warnings** (`shelf`, `widget`, `Regional` not bold on first use). The fixture README names only W307 as a known warning. Either the fixture or the README should change; nothing blocks.
9. **Not run:** `diagram shot` and `diagram sheet` (headless Chrome), `tasks emulate` (moto), `coverage`, `mocks`, `drills`, `audit`, `freshen`, `changes`, `faq`, `cases` against live data. Their unit tests pass.
10. **`status` in text form prints 40 chapter lines of 53** (the contract's line limit). Use `--json` or `--out` for all chapters.
