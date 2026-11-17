# Exemplar synthesis: contract 1.0 changes (2026-10-11)

Input: the five judge reports `exemplar-judge-{architect,designer,editor,exam,reader}.md`, the attempts `_build/tmp/exemplar-{a,b,c}/`. Result: winner a (Borda a 9, c 4, b 2; weighted means a 3.92, c 3.76, b 3.70; fatal defects in b and c). Output: `_build/style/exemplar/` (README lists what to imitate and the ten common failures), STYLE 1.0, SPEC 1.0, CONVENTIONS 1.0, CONVENTIONS-2 1.0. Sandbox for the tool checks: `_build/tmp/exemplar-final/` (a copy of `exemplar-a` with the final files in place).

## 1. Changed SPEC.json keys

| Key | Old | New | Reason (judge evidence) |
|---|---|---|---|
| `version` | `"0.9"` | `"1.0"` | Contract freeze after the panel (task instruction). |
| `callouts.not_counted_toward_callouts_max` | `["Changed recently"]` | `["Changed recently", "Say it"]` | All five judges asked for spoken rehearsal inside How it works (architect graft C1, designer graft 5, editor graft 5, exam must-fix 9, reader: "reading the chapter is rehearsing the job"). The device is one `Say it` per subsection. A deep chapter has 8 to 14 subsections, so with a limit of 12 counted callouts the Say it lines alone would fill the limit and push out the Exam signal, Exam trap and Try it devices the same judges asked for: a section that could not hold its devices. The limit still guards the warning-type callouts that the designer and editor called decoration (three Exam traps in a row). |
| `callouts.labels[Say it].use` | "a sentence to say aloud; the first one in In one breath is the one-breath definition" | adds "in How it works, one per subsection, directly before the Stop and answer, with the starters The short answer is and The thing to watch is" | Documents the new placement; the lint does not read `use`. |
| `callouts.changed_recently.placement` | absent | new documentation key: an examinable entry stands in the fast file; a `not examinable yet` entry stands in `2-deep.md` directly under the B-list | Designer must-fix 4 ("Remove the 'not examinable yet' quota box from the fast file, or move it to the deep file") and reader ("That is padding in the 15-minute file"). The other three judges asked only to fix its Old line; the move satisfies all five and keeps RULINGS rule 7 (the note still exists). The lint does not read the key; `_changed_entry` checks an entry wherever it stands. |
| `lint.banned_words` | (no entry) | `"has a say": "decides"`, `"have a say": "decide"`, `"safety net": ""` | Editor's idiom count: "each owner has a say" (attempt a), "as a safety net" (attempt c). Exact phrases, so no false positives in normal text. |

The same structural changes are in the fixture copy `tools/tests/fixtures/book/_build/style/SPEC.json` (`test_fixture_spec_has_the_same_structure` compares the key trees).

## 2. Values the judges discussed and that stay

| Key | Value | Why it stays |
|---|---|---|
| `templates.deep.files[1-fast.md].words.max` | 1800 | RULINGS fixes it. The reader proposed 1,600; the final fast file holds every graft at 1,788 words. Attempt c's note asked for 2,000, which RULINGS forbids. |
| `...how.counts.subsection_words.max` | 400 | Designer: "Cap each full subsection at about 400 words before Go deeper". All five exemplar subsections fit with trace, table, reason, signal and Say it (no W201; two of them needed trimming to get under the limit, which is the intended pressure). Attempt b's request for 450 is not supported by any judge. |
| `...faq.words.max` and `counts.items` | 450 and 10 | Attempt a's note called 10 items padding; no judge agreed, and the reader asked only to "trim each FAQ quote to the one sentence that answers". The exemplar holds 10 items within 450 words (no W201) with one-sentence quotes. |
| `...check.words.max`, `...recap.words.max` | 140, 160 | Attempts a and c ran over; the reader treated c's 154 words as "too long", so the limit is right. The exemplar fits both (no W201). |
| `questions.counts.twin_pairs_min` | 2 | Kept; the stricter rule (one strict pair with identical options) is a writing rule (CONVENTIONS-2 J2), because the lint cannot compare option sets yet. |
| `callouts_max` of deep `2-deep.md` | 12 | Not raised; the Say it exemption above solves the evidence. |

## 3. Convention changes (devices only)

- `CONVENTIONS.md` 1.0: D6 (a `not examinable yet` entry stands in `2-deep.md` under the B-list; `Old:` holds the old value), D8 (a `Say it` before the closing Stop and answer), E (Say it does not count toward the callout limit), revision line, and decisions 12, 17, 18, 20 and 26 shortened so that the file stays within its 4,900-word budget (now 4,899).
- `CONVENTIONS-2.md` 1.0: J2 strict twins and "state the side the twin does not test"; decisions 35 to 40 (house pattern, Say it, stem phrases as Exam signal, placement of not-examinable entries, strict twins, task verify).
- `STYLE.md` 1.0 (2,999 of 3,000 words): new section 11 (twelve rules from the panel, each with an example); bold step names and truth tables allowed in section 5; respell only words she can mispronounce; check every linked sentence before return. Removed because they proved wrong: the ungrounded spoken sample (section 6) and the ungrounded sample question (section 7), replaced by pointers to the grounded exemplar; the pronunciation starter list, which respelled common words and duplicated `data/terms.json`.

## 4. Fixture and test changes (`python3 aws-saa-book/tools/tests/run.py`: 798 tests, OK)

- `tools/tests/fixtures/book/_build/style/SPEC.json`: the five key changes of section 1.
- `tools/tests/fixtures/book/99-sample/2-deep.md`: one `Say it` before the Stop and answer of the first subsection, so the fixture shows the device.
- `tools/tests/fixtures/book/data/book.json` and `_build/ledger/chapters/99.json`: `style_version` 1.0.
- `tools/tests/test_contract.py` lines 149 and 150: the version pin changed from "0.9" to "1.0". This is the one change outside `fixtures/`: the test pins the SPEC version string, so no fixture change can make version 1.0 pass. No rule or tool behaviour changed.

## 5. Tool changes that are needed (not made)

1. **A slice mode for lint** (attempt b's note): `lint CH --draft` cannot be clean on an exemplar slice, because L201 (deep file below 3,500 words) and L106 (a "Planned:" stub without a Stop and answer; empty Numbers, Decision record and FAQ in the VPC slice) are not draft-softened. Proposal: `--slice` turns L201, L106 and L107 on subsections or sections whose body starts with "Planned:" or "Not part of this sample." into warnings.
2. **T108 and IAM verify steps.** All judges flagged that `iam-t02` verifies with the Resource Groups Tagging API, and no fact says that it lists IAM roles. Their fix (`aws iam get-role --role-name saa-iam-t02`, expect NoSuchEntity) fails T108, which requires a tag filter. Proposal: allow a read-only `get-*` or `describe-*` verify on a `saa-` name, with an expected not-found error, when the task's facts include one that the service has no tag filter API; or ground the tagging API support as a fact and keep the current form.
3. **W901 on prompts** (attempts a and c): the first use of a term inside a Predict prompt fires W901, because prompts come before the words table. Exempting prompt paragraphs would remove most of the 16 W901 warnings of the exemplar fast file.
4. **A strict-twin check** (Q114 extension): at least one twin pair per deep chapter with identical option texts.
5. **A Say it check** (L106 extension): one `Say it` per How-it-works subsection, directly before the Stop and answer.
6. `tasks check-cli 03` (T113) was not run: it installs the AWS CLI model through `uv`, and this agent installs nothing.

## 6. Data issues for the orchestrator

- `data/terms.json`: the core IAM terms are missing (trust policy, permissions policy, implicit deny, explicit deny, permissions boundary, instance profile); the deep file carries `needs-term` markers (W307). The respelling of `network ACL` is "NAK-ul (spoken short form)", so W901 asks for that whole string; it should be "NAK-ul".
- `data/book.json` `style_version` is still "0.9"; `registry build` writes it from SPEC. Changing SPEC may also change the inputs hash of stages that read SPEC; chapters 00 to 02 should be checked with `status`.
- No fact grounds "a custom network ACL denies all traffic until you add rules" (architect must-fix 12, for the VPC fast file). File the request when chapter 10 is briefed.
- The tool sets `checked` on tasks; the attempts carried 2026-10-12 (the UTC date of the run) against a build date of 2026-10-11. The exemplar uses 2026-10-11.

## 7. Tool checks of the exemplar (sandbox `_build/tmp/exemplar-final/`)

| Check | Result |
|---|---|
| `lint 03 --file 1-fast.md --draft` | 0 errors; warnings: W901 on terms first used in Predict prompts (item 3 above), one W601 xref marker |
| `lint 03 --draft` | errors only from the slice structure: L201 (3,059 of 3,500 words) and L106 on the ten "Planned:" stubs; no finding in any written block |
| `lint 10 --file 2-deep.md --draft` | errors only from the slice structure (2 subsections, empty Numbers, Decision record and FAQ); both written subsections within 400 words |
| `q lint 03` | 0 errors; warnings Q201 (6 of 18) and Q204 (difficulty mix of a 6-question sample) |
| `speak lint 03` | 0 errors; warning P201 (3 of 4) |
| `tasks lint 03` | 0 errors; warnings T201 (1 Try of 2 to 3) and T113 (no CLI report) |
| `diagram lint iam-hero` | ok, 390 by 440, no crossings |
| `tools/tests/run.py` | 798 tests, OK |
