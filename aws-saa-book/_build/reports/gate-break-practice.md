# Gate break report: practice gates

Written by `tools/helpers/break_practice.py` (gate breaker, 2026-10-05). Nothing in the tool was changed.

## Method

- Every attempt runs in a fresh copy of the fixture book at `_build/tmp/breaker-practice/`, through `--book-dir`. No real data was touched.
- One change to the fixture `SPEC.json` in the sandbox: `questions.stem_key_overlap_margin_max` is 0.25 (the value of the real `SPEC.json`; the fixture has 1.0, which switches Q113 off). The mock attempts add the same `mock` template and chapters 50 and 51 that `tests/test_qbank.py` uses.
- 'Got through' means: the gate command ended with exit 0 (or 2, warnings only) and stored or accepted the bad input. Controls are bad inputs that the gate is known to reject; they show that the attempt reached the rule.
- A step line reads: command, exit code, first findings or the JSON result (cut at 300 characters).
- Run it again with `python3 aws-saa-book/tools/helpers/break_practice.py` (add `--no-uv` to skip the one attempt that needs `uv` and the package index; `--only=N,N` prints single attempts).

## Totals

- Attempts: 61
- Got through: 47
- Partly through: 2
- Held (controls included): 12
- Not run: 0

## Attempts

### 1. Control: two correct options on a single-answer question

- Gate: `q add`
- Did: sample-q004 copy; option b also marked correct.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 1: Q102 2 correct options, select is 1
- Result: **held**
- Note: Q102 holds.

### 2. Control: multiple-response question with one key

- Gate: `q add`
- Did: sample-q003 copy (Select TWO); option b set to wrong.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 1: Q102 1 correct options, select is 2
- Result: **held**
- Note: Q102 holds.

### 3. Two options with the same text, one marked correct and one marked wrong

- Gate: `q add`
- Did: sample-q004 copy; option c gets the exact text of the key (option a). The question now has two correct answers in fact, and only one is keyed.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: No rule compares option texts; Q102 checks only that option ids are unique.

### 4. Key leaked through option length (short options)

- Gate: `q add`
- Did: sample-q004 copy; key has 17 words, the three wrong options 4, 3 and 4 words. Mean is 7 words, so Q104 (applies from a mean of 10 words) never runs.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: Q104 is switched off below a mean of 10 words; Q202 (key is longest) is a chapter warning and needs 10 questions.

### 5. Key is the longest option, just inside the 30% spread

- Gate: `q add`
- Did: sample-q004 copy; key has 15 words, every wrong option 11. Each option is within 30% of the mean (12), but the key is 36% longer than each distractor.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity low)
- Note: Q104 measures the distance to the mean, and the long key pulls the mean up. Only Q202 looks at 'key is longest', as a bank share.

### 6. Key leaked through word overlap with the stem (long stem dilutes the Jaccard value)

- Gate: `q add`
- Did: Key = 'A crate to send the partner the widgets next week from the shelf.' (6 of its 7 content words come from the stem); wrong options share no word with the stem. Step 1 with the short fixture stem (control), step 2 with one more story sentence of 26 words in the stem. SPEC margin set to the real value 0.25.
- Gate answer:
  - `q add --chapter 99 --file <q-short.json> --by breaker` -> exit 1: Q113 the stem repeats the words of the key (overlap 0.38, best wrong option 0.00)
  - `q add --chapter 99 --file <q-long.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: The short-stem control is rejected by Q113. Jaccard divides by the union, so a longer stem lowers the key overlap below the margin while the key still consists of stem words only.

### 7. Explanation names options by position and letter without the word 'Option'

- Gate: `q add`
- Did: Step 1 control: 'Option B' in the explanation. Step 2: 'The second option is wrong, and (C) is wrong too; B is the usual trap.'
- Gate answer:
  - `q add --chapter 99 --file <q-c.json> --by breaker` -> exit 1: Q105 explanation names an option letter ('Option B')
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity medium)
- Note: letter_reference_regex needs the word Option, Answer or Choice before the letter. Options print without letters and the app can shuffle them, so these references point at the wrong option.

### 8. Exact copy of an existing question under a new id

- Gate: `q add / q lint / gate questions`
- Did: sample-q001 copied without id, concept renamed. Then q lint 99, the questions gate, and q lint --all.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
  - `q lint 99` -> exit 0: {"chapter": "99", "ok": true, "errors": []}
  - `gate 99 --gate questions` -> exit 0: {"result": "PASS", "chapter": "99", "gates": [{"gate": "questions", "ok": true, "errors": 0, "warnings": 0, "record": "_build/ledger/gates/99.questions.json"}], "errors": []}
  - `q lint --all` -> exit 1: Q302 near-duplicate of sample-q001 (similarity 1.0) \| Q302 near-duplicate of sample-q002 (similarity 1.0)
  - `q dedupe` -> exit 1: {"pairs": [{"a": "sample-q001", "b": "sample-q005", "similarity": 1.0, "kind": "duplicate"}, {"a": "sample-q002", "b": "sample-q005", "similarity": 1.0, "kind": "duplicate"}]}
- Result: **GOT THROUGH** (severity high)
- Note: q add and the questions gate accept the copy; only q lint --all (exit 1) and q dedupe (exit 1) see it, and no ledger stage runs them for a chapter.

### 9. Near-duplicate with reordered words

- Gate: `q dedupe / q lint --all`
- Did: sample-q001 with the clauses of every sentence reordered (same facts, same options, same key). Then q dedupe, q lint --all and the questions gate.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
  - `q dedupe` -> exit 0: {"pairs": []}
  - `q lint --all` -> exit 0: {"chapter": "all", "ok": true, "errors": []}
  - `gate 99 --gate questions` -> exit 0: {"result": "PASS", "chapter": "99", "gates": [{"gate": "questions", "ok": true, "errors": 0, "warnings": 0, "record": "_build/ledger/gates/99.questions.json"}], "errors": []}
- Result: **GOT THROUGH** (severity high)
- Note: 3-word shingle similarity of the two stems is 0.29 (threshold 0.6). Options are never compared.

### 10. Negative stem written in lowercase

- Gate: `q add`
- Did: Last sentence changed to 'Which Amazon Widget Store resource is not a way to send the 40 widgets?'
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity low)
- Note: negative_stem_regex matches only NOT and EXCEPT in capitals. The lowercase form is the harder one for this reader.

### 11. 'None of these options.' as an option

- Gate: `q add`
- Did: Option d text set to 'None of these options.' (banned list holds 'none of the above').
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity low)
- Note: banned_in_options is a list of four literal phrases.

### 12. Control: status ready and a passed verification smuggled in the input file

- Gate: `q add`
- Did: Input item carries status ready and verification.status pass.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
  - `stored state` -> exit -: ('candidate', 'candidate', 0)
- Result: **held**
- Note: q add resets status and verification.

### 13. Control: a pack holds no key, why or explanation

- Gate: `q pack`
- Did: All four questions set to candidate; q pack --lens closed; searched the file for correct, why, explanation, trap, facts.
- Gate answer:
  - `q pack --chapter 99 --lens closed --out pack-closed.json` -> exit 0: wrote aws-saa-book/_build/tmp/breaker-practice/pack-closed.json (109 lines)
  - `search the pack` -> exit -: leaking keys found: []
- Result: **held**
- Note: Pack items hold only id, type, select, stem, options (label, text).

### 14. Stored option order recovered from a pack (the shuffle is reversible)

- Gate: `q pack`
- Did: A solver reads data/book.json (mock_seed), recomputes random.Random(sha256('<seed>|<id>|<lens>|<round>')) on the positions 0..n-1 and maps each label back to the stored position. Then it answers 'the option stored first'.
- Gate answer:
  - `q pack --chapter 99 --lens closed --out pack-closed.json` -> exit 0: wrote aws-saa-book/_build/tmp/breaker-practice/pack-closed.json (109 lines)
  - `unshuffle with the public seed` -> exit -: stored order recovered for 4 of 4 questions; 'first stored options' equals the key in 3 of 4
- Result: **PARTLY THROUGH** (severity medium)
- Note: The seed is in data/book.json and the other inputs are in the pack, so the shuffle hides nothing from a solver that can read the book folder. It leaks the key as far as writers store the key first (fixture: 3 of 4). Q202 limits the position share only from 10 questions and only as a chapter warning.

### 15. Control: only two answer files (one solver missing)

- Gate: `q adjudicate`
- Did: Answer files of the closed and open lens only.
- Gate answer:
  - `q adjudicate --answers closed open` -> exit 3: error: q adjudicate needs --answers F1 F2 F3 or --select
- Result: **held**
- Note: Exit 3.

### 16. Control: one lens has no answer for one question

- Gate: `q adjudicate`
- Did: The ambiguity file leaves out sample-q004.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003"], "needs_edit": [{"id": "sample-q004", "reasons": ["ambiguity missing"]}], "rejected": [], "below_min": false}
- Result: **held**
- Note: The question goes to needs_edit ('ambiguity missing').

### 17. Answer files without a solver field

- Gate: `q adjudicate`
- Did: Three answer files with no 'solver' key at all.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": false}
  - `stored solvers` -> exit -: ['unknown', 'unknown', 'unknown']
- Result: **GOT THROUGH** (severity medium)
- Note: A missing solver is stored as 'unknown' and the question passes.

### 18. One solver (the question's author) signs all three lenses

- Gate: `q adjudicate`
- Did: Three answer files, all with solver 'breaker', the label that wrote the questions with q add --by breaker.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": false}
- Result: **GOT THROUGH** (severity high)
- Note: Nothing requires three different solvers, and questions store no author, so the writer can be all three solvers (facts vote refuses the author; q adjudicate does not).

### 19. Closed lens without stem_only, ambiguity lens without a case

- Gate: `q adjudicate`
- Did: stem_only null in the closed file; case null in the ambiguity file.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": false}
- Result: **GOT THROUGH** (severity medium)
- Note: The fields that make the lenses different are optional, so three identical 'pick the labels' runs count as three lenses.

### 20. Open-book citations: one unrelated fact id, or the one-word quote 'the', for every label

- Gate: `q adjudicate`
- Did: Step 1: every label cites the fact widget-shelf-max-widgets (unrelated to most options). Step 2: every label cites {source_id, quote: 'the'}.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": false}
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": false}
  - `stored citations_ok` -> exit -: True
- Result: **GOT THROUGH** (severity high)
- Note: A citation only has to exist: any verified fact, or any substring of any snapshot (no minimum length, no link to the option or to the question's facts).

### 21. Two rows for one question in one answer file (first agrees, second disagrees and flags)

- Gate: `q adjudicate`
- Did: The ambiguity file holds sample-q004 twice: first the key, then a wrong answer with a flag.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": false}
- Result: **GOT THROUGH** (severity low)
- Note: Only the first row of an id is read; the flag in the second row is dropped silently.

### 22. Old answer files applied to a question that was replaced after the packs went out

- Gate: `q adjudicate`
- Did: Honest answer files built for the fixture questions. Then q add --replace swaps sample-q004 for the length-leak version (new option texts, same key id) while it is still a round-0 candidate. Then q adjudicate with the old files.
- Gate answer:
  - `q add --chapter 99 --file <q.json> --by breaker --replace` -> exit 0: {"added": [], "replaced": ["sample-q004"], "rejected": []}
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": false}
  - `state of sample-q004` -> exit -: ('verified', 'pass', 0)
- Result: **GOT THROUGH** (severity high)
- Note: Answer files carry no rev, keyRev or content hash, and a round-0 replace keeps rev. The stored text was never seen by a solver, yet it is 'verified, pass'.

### 23. More than one edit after a failed round

- Gate: `q add --replace`
- Did: Round 0 fails for sample-q004 (closed disagrees). Then q add --replace twice with different takeaways.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003"], "needs_edit": [{"id": "sample-q004", "reasons": ["closed disagrees"]}], "rejected": [], "below_min": false}
  - `q add --chapter 99 --file <e1.json> --by breaker --replace` -> exit 0: {"added": [], "replaced": ["sample-q004"], "rejected": []}
  - `q add --chapter 99 --file <e2.json> --by breaker --replace` -> exit 0: {"added": [], "replaced": ["sample-q004"], "rejected": []}
  - `state of sample-q004` -> exit -: rev=3 round=1 status=candidate
- Result: **GOT THROUGH** (severity medium)
- Note: RULINGS: 'unanimous or one edit then reject'. The tool counts no edits in round 1; rev just goes up.

### 24. A rejected question comes back under a new id

- Gate: `q add`
- Did: sample-q004 fails round 0 and round 1 and is rejected. The same content is then added again without an id.
- Gate answer:
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 0: {"pass": ["sample-q001", "sample-q002", "sample-q003"], "needs_edit": [{"id": "sample-q004", "reasons": ["closed disagrees"]}], "rejected": [], "below_min": false}
  - `q adjudicate --chapter 99 --answers closed open ambiguity` -> exit 1: {"pass": [], "needs_edit": [], "rejected": ["sample-q004"], "below_min": true}
  - `state of sample-q004` -> exit -: ('rejected', 'rejected', 1)
  - `q add --chapter 99 --file <q.json> --by breaker` -> exit 0: {"added": ["sample-q005"], "replaced": [], "rejected": []}
  - `q lint --all` -> exit 0: {"chapter": "all", "ok": true, "errors": []}
- Result: **GOT THROUGH** (severity high)
- Note: q add does not look at rejected items or at _build/qbank/rejected.jsonl, and q dedupe skips rejected questions, so the copy is a fresh round-0 candidate.

### 25. Mark a never-verified candidate as verified

- Gate: `q set-status`
- Did: All questions candidate; q set-status --status verified sample-q004.
- Gate answer:
  - `q set-status --chapter 99 --status verified sample-q004 --by breaker` -> exit 0: {"set": ["sample-q004"], "refused": []}
  - `state of sample-q004` -> exit -: ('verified', 'candidate', 0)
  - `q lint 99` -> exit 0: {"chapter": "99", "ok": true, "errors": []}
- Result: **PARTLY THROUGH** (severity low)
- Note: Status 'verified' is set without any solver (only 'ready' is checked). Downstream --select, mocks and Q206 read verification.status, so the damage is a wrong count in q lint and q list.

### 26. Control: a mock question with the exact stem of a chapter question

- Gate: `mocks check`
- Did: Assemble mock 50, then give one chosen single-answer question the exact stem of sample-q004.
- Gate answer:
  - `mocks assemble --mock 50` -> exit 0: {"mock": "50", "ok": true, "seed": 20261054, "spares": 4}
  - `mocks check --mock 50` -> exit 1: K04 near-duplicate of sample-q004 (similarity 1.0)
- Result: **held**
- Note: K04 holds for a verbatim stem.

### 27. A mock built from chapter questions under new ids (one padding sentence in front of the stem)

- Gate: `mocks assemble / mocks check`
- Did: Every mock question is sample-q004 or sample-q003 with a new id and one extra first sentence of 18 new words; options, key, why and explanation are the chapter question's. This is also what the tool's own mock tests use as their pool. Second step: only 12 padding words.
- Gate answer:
  - `mocks assemble --mock 50` -> exit 0: {"mock": "50", "ok": true, "seed": 20261054, "spares": 4}
  - `mocks check --mock 50` -> exit 0: {"mocks": [{"mock": "50", "ok": true, "errors": [], "warnings": [], "counts": {"domains": {"1": 1, "2": 3, "3": 1, "4": 1}, "tasks": {"1.1": 1, "2.1": 2, "2.2": 1, "3.1": 1, "4.1": 1}, "multi": 1, "difficulty": {"1": 6}, "services": {"widget": 6}}}]}
  - `mocks assemble --mock 50` -> exit 0: {"mock": "50", "ok": true, "seed": 20261054, "spares": 4}
  - `mocks check --mock 50 (12 padding words)` -> exit 0: {"mocks": [{"mock": "50", "ok": true, "errors": [], "warnings": [], "counts": {"domains": {"1": 1, "2": 3, "3": 1, "4": 1}, "tasks": {"1.1": 1, "2.1": 2, "2.2": 1, "3.1": 1, "4.1": 1}, "multi": 1, "difficulty": {"1": 6}, "services": {"widget": 6}}}]}
- Result: **GOT THROUGH** (severity high)
- Note: Stem similarity to the chapter question is 0.50 with 18 padding words and 0.59 with 12 (threshold 0.6). K04 compares stems only, never options or explanations.

### 28. Two questions of one mock with the same stem

- Gate: `mocks check`
- Did: After assemble, one chosen single-answer question gets the stem of another chosen single-answer question of the same mock.
- Gate answer:
  - `mocks assemble --mock 50` -> exit 0: {"mock": "50", "ok": true, "seed": 20261054, "spares": 4}
  - `mocks check --mock 50` -> exit 0: {"mocks": [{"mock": "50", "ok": true, "errors": [], "warnings": [], "counts": {"domains": {"1": 1, "2": 3, "3": 1, "4": 1}, "tasks": {"1.1": 1, "2.1": 2, "2.2": 1, "3.1": 1, "4.1": 1}, "multi": 1, "difficulty": {"1": 6}, "services": {"widget": 6}}}]}
  - `q lint --all` -> exit 1: Q302 near-duplicate of mock-exam-1-q002 (similarity 1.0)
- Result: **GOT THROUGH** (severity medium)
- Note: K04 looks only at the other mock and at pool 'chapter'. q lint --all would report Q302 (exit 1), but mocks check and the ledger gates do not run it.

### 29. A mock question that copies a drill-pool question

- Gate: `mocks check`
- Did: sample-q004 is moved to pool drill in chapter 99; one mock question gets its exact stem.
- Gate answer:
  - `mocks assemble --mock 50` -> exit 0: {"mock": "50", "ok": true, "seed": 20261054, "spares": 4}
  - `mocks check --mock 50` -> exit 0: {"mocks": [{"mock": "50", "ok": true, "errors": [], "warnings": [], "counts": {"domains": {"1": 1, "2": 3, "3": 1, "4": 1}, "tasks": {"1.1": 1, "2.1": 2, "2.2": 1, "3.1": 1, "4.1": 1}, "multi": 1, "difficulty": {"1": 6}, "services": {"widget": 6}}}]}
- Result: **GOT THROUGH** (severity medium)
- Note: K04 tests pool == 'chapter' only, so a drill question can be reused in a mock.

### 30. Manifest edited by hand: minutes and counts changed

- Gate: `mocks check`
- Did: After assemble, mock.json gets minutes 9999 and an invented counts object.
- Gate answer:
  - `mocks assemble --mock 50` -> exit 0: {"mock": "50", "ok": true, "seed": 20261054, "spares": 4}
  - `mocks check --mock 50` -> exit 0: {"mocks": [{"mock": "50", "ok": true, "errors": [], "warnings": [], "counts": {"domains": {"1": 1, "2": 3, "3": 1, "4": 1}, "tasks": {"1.1": 1, "2.1": 2, "2.2": 1, "3.1": 1, "4.1": 1}, "multi": 1, "difficulty": {"1": 6}, "services": {"widget": 6}}}]}
- Result: **GOT THROUGH** (severity low)
- Note: mocks check recomputes the split from the questions and ignores the stored minutes, seed and counts; the web app reads minutes from this file.

### 31. Control: list answer with semicolons

- Gate: `cards add`
- Did: Back 'A shelf; a crate; a quota.'
- Gate answer:
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 1: C105 list answer: one fact per card
- Result: **held**
- Note: C105 holds.

### 32. List answer written with one comma and 'and', or with slashes

- Gate: `cards add`
- Did: Step 1: back 'A shelf, a crate and a quota.' Step 2: back 'shelf / crate / quota / Region'.
- Gate answer:
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 0: {"added": ["sample-c004"], "replaced": [], "rejected": []}
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 0: {"added": ["sample-c005"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: C105 looks for a line break, a semicolon or two commas. A three-item list in plain English has one comma.

### 33. Control: back of 14 words

- Gate: `cards add`
- Did: Back with 14 separate words.
- Gate answer:
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 1: C102 back has 14 words; at most 12
- Result: **held**
- Note: C102 holds.

### 34. Back far over the word limit, joined with hyphens

- Gate: `cards add`
- Did: Back 'No. Copy-the-shelf-to-the-other-Region-then-check-the-copy-then-delete-the-first-shelf-and-tell-the-team.' (20 words, counted as 2).
- Gate answer:
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 0: {"added": ["sample-c004"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity medium)
- Note: lint.word_count splits on whitespace only. The same trick works for every word limit (speak scripts, step texts, options).

### 35. Wrong number written as a word

- Gate: `cards add`
- Did: Back 'A crate. It holds ninety widgets.' with facts [widget-crate-capacity] (the fact says 50 widgets).
- Gate answer:
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 0: {"added": ["sample-c004"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: C109 sees digits only (lint.number_with_unit does not match number words), so a number in words needs no fact and can be wrong.

### 36. Card whose answer contradicts its own fact

- Gate: `cards add`
- Did: cannot card: front 'In Amazon Widget Store, is a new shelf readable by every user in the account?', back 'Yes. Every user reads it.', facts [widget-shelf-default-private].
- Gate answer:
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 0: {"added": ["sample-c004"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: front and back are not strict text: no fact link, no absolute-word rule, and cards have no blind check. 'extra' can be null, so the card carries no grounded sentence at all.

### 37. Near-duplicate front with three filler words

- Gate: `cards add`
- Did: Front of sample-c002 plus ' Think first, please.'
- Gate answer:
  - `cards add --chapter 99 --file <card.json> --by breaker` -> exit 0: {"added": ["sample-c004"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity low)
- Note: C106 needs a token Jaccard of 0.8; short fronts drop below it with two or three added words.

### 38. Control: a 60-second answer of 300 words

- Gate: `speak add`
- Did: Twelve lines of 25 plain words each.
- Gate answer:
  - `speak add --chapter 99 --file <speak.json> --by breaker` -> exit 1: P102 sixty_second has 245 words; allowed 60 to 145 \| P102 a sentence of sixty_second[1] has 22 words; at most 16 \| P102 a sentence of sixty_second[2] has 22 words; at most 16
- Result: **held**
- Note: P102 holds for plain words.

### 39. A 60-second answer of about 300 words, with words joined by hyphens

- Gate: `speak add`
- Did: The eight fixture lines, each with one more 'sentence' of 28 words joined by hyphens. The tool counts 8 more words; a speaker says 224 more.
- Gate answer:
  - `words a speaker says` -> exit -: 315
  - `speak add --chapter 99 --file <speak.json> --by breaker` -> exit 0: {"added": ["sample-s02"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity medium)
- Note: Same cause as the card attempt: word_count splits on whitespace.

### 40. 300 words outside the script: follow-up answer and key point

- Gate: `speak add`
- Did: follow_ups[0].answer and key_points[0].point each get 300 words.
- Gate answer:
  - `speak add --chapter 99 --file <speak.json> --by breaker` -> exit 0: {"added": ["sample-s02"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity medium)
- Note: Only ten_second, sixty_second and the cues have word limits. 4-say.md prints the follow-up answers, and the app grades against key points.

### 41. Ungrounded absolute claims in the script

- Gate: `speak add`
- Did: Line 3 replaced by 'A shelf is always global and never private.' (contradicts widget-shelf-scope and widget-shelf-default-private).
- Gate answer:
  - `speak add --chapter 99 --file <speak.json> --by breaker` -> exit 0: {"added": ["sample-s02"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: Scripts are checked for digits, number words with a unit, avoid words and banned words. There is no absolute-word rule and no tie between a script sentence and a fact (RULINGS hard rule 1).

### 42. Spoken numbers that P109 does not see

- Gate: `speak add`
- Did: Step 1 control: 'One shelf holds up to six hundred widgets.' Step 2: 'One shelf holds up to nine hundred of your widgets.' Step 3: 'One shelf holds up to nineteen widgets.'
- Gate answer:
  - `speak add --chapter 99 --file <speak.json> --by breaker` -> exit 1: P109 'six hundred widgets' in sixty_second[4] is not a spoken form of a fact in facts
  - `speak add --chapter 99 --file <speak.json> --by breaker` -> exit 0: {"added": ["sample-s02"], "replaced": [], "rejected": []}
  - `speak add --chapter 99 --file <speak.json> --by breaker` -> exit 0: {"added": ["sample-s02"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: number_word_regex has no one, seventeen, eighteen, nineteen, dozen, half or double; and the unit must follow the number word directly, so two words between number and noun switch P109 off.

### 43. Control: a Try without cleanup

- Gate: `tasks add`
- Did: sample-t02 copy with cleanup [].
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 1: T103 a try needs cleanup steps \| T107 no cleanup command undoes `create-shelf` (create command 1 of 2) \| T107 no cleanup command undoes `copy-shelf` (create command 2 of 2)
- Result: **held**
- Note: T103 holds.

### 44. A task that creates resources and deletes nothing (create verbs outside the list)

- Gate: `tasks add`
- Did: Steps 'aws widget put-shelf --name saa-breaker-shelf' and 'aws widget import-shelf ...'; cleanup is 'aws widget list-shelves'. No tag anywhere.
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: T103 wants a non-empty cleanup list, T106 and T107 act only on create|copy|run|allocate|launch. Any other creating verb needs no tag and no undo, and the cleanup can be a list command.

### 45. Cleanup deletes a different resource, or only pretends (--dry-run)

- Gate: `tasks add`
- Did: sample-t02 copy (create-shelf, copy-shelf); cleanup 'aws widget delete-shelf --name saa-some-other-shelf --dry-run' twice.
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: T107 pairs verbs and nouns only. It does not compare the resource name or id, and it does not know --dry-run or --generate-cli-skeleton.

### 46. run-instances undone by stop-instances

- Gate: `tasks add`
- Did: Step 'aws ec2 run-instances ... --tag-specifications ...'; cleanup 'aws ec2 stop-instances --instance-ids <INSTANCE_ID>'.
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity medium)
- Note: lab.UNDO accepts stop and delete for run, although cleanup_pairs maps run-instances to terminate-instances. A stopped instance keeps its EBS volume and its bill.

### 47. Security group opened to the world: ::/0 written in full, prefix list, split ranges, rules in a file, other operations

- Gate: `tasks add (T105)`
- Did: One tasks add per command. Controls first (must be rejected), then the variants.
- Gate answer:
  - `tasks add [c1 port 22 ::/0] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,Ipv6Ranges=[{CidrIpv6=::/0}]` -> exit 1: T105 steps[0]: matches the banned pattern authorize-security-group-ingress.*FromPort=(22\|3389)\b \| T105 steps[0]: opens SSH or RDP (port 22 or 3389) to the world (0.0.0.0/0 or ::/0)
  - `tasks add [c2 range 20-25 ::/0] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,Ipv6Ranges=[{CidrIpv6=::/0}]` -> exit 1: T105 steps[0]: opens SSH or RDP (port 22 or 3389) to the world (0.0.0.0/0 or ::/0)
  - `tasks add [c3 all protocols ::/0] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions IpProtocol=-1,Ipv6Ranges=[{CidrIpv6=::/0}]` -> exit 1: T105 steps[0]: opens SSH or RDP (port 22 or 3389) to the world (0.0.0.0/0 or ::/0)
  - `tasks add [c4 --port=22 --cidr=0.0.0.0/0] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --protocol=tcp --port=22 --cidr=0.0.0.0/0` -> exit 1: T105 steps[0]: opens SSH or RDP (port 22 or 3389) to the world (0.0.0.0/0 or ::/0)
  - `tasks add [v1 ::/0 written in full] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,Ipv6Ranges=[{CidrIpv6=0:0:0:0:0:0:0:` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v2 prefix list] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,PrefixListIds=[{PrefixListId=pl-0123` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v3 two halves of the internet] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,IpRanges=[{CidrIp=0.0.0.0/1},{CidrIp` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v4 modify-security-group-rules] aws ec2 modify-security-group-rules --group-id <SG_ID> --security-group-rules SecurityGroupRuleId=sgr-0123,SecurityGroupRule={IpProtocol=tcp,FromPort=` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v5 rules in a file] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions file://rules.json` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v6 --cli-input-json] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --cli-input-json file://open-ssh.json` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v7 port 443 to the world with --cidr=] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --protocol tcp --port 443 --cidr=0.0.0.0/0` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v8 all TCP ports, IPv4 range form] aws ec2 authorize-security-group-ingress --group-id <SG_ID> --ip-permissions IpProtocol=tcp,FromPort=0,ToPort=65535,IpRanges=[{CidrIp=0.0.0.0/0}]` -> exit 1: T105 steps[0]: opens SSH or RDP (port 22 or 3389) to the world (0.0.0.0/0 or ::/0)
  - `tasks add [v9 network ACL entry] aws ec2 replace-network-acl-entry --network-acl-id <SG_ID> --ingress --rule-number 100 --protocol 6 --port-range From=22,To=22 --cidr-block 0.0.0.0/0 ` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: Got through: ['v1 ::/0 written in full', 'v2 prefix list', 'v3 two halves of the internet', 'v4 modify-security-group-rules', 'v5 rules in a file', 'v6 --cli-input-json', 'v7 port 443 to the world with --cidr=', 'v9 network ACL entry']. Held: ['c1 port 22 ::/0', 'c2 range 20-25 ::/0', 'c3 all protocols ::/0', 'c4 --port=22 --cidr=0.0.0.0/0', 'v8 all TCP ports, IPv4 range form']. The world check is tied to the operation name authorize-security-group-ingress and to the literal strings 0.0.0.0/0 and ::/0.

### 48. Public exposure by other commands

- Gate: `tasks add (T105)`
- Did: One tasks add per command.
- Gate answer:
  - `tasks add [c1 public-read ACL] aws s3api put-bucket-acl --bucket saa-b --acl public-read` -> exit 1: T105 steps[0]: matches the banned pattern --acl public-read \| T105 steps[0]: sets a public ACL
  - `tasks add [c2 BlockPublicAcls=false] aws s3api put-public-access-block --bucket saa-b --public-access-block-configuration BlockPublicAcls=false,IgnorePublicAcls=true,BlockPublicPolicy=tru` -> exit 1: T105 steps[0]: matches the banned pattern BlockPublicAcls=false \| T105 steps[0]: turns a public access block setting off
  - `tasks add [v1 bucket policy Principal *] aws s3api put-bucket-policy --bucket saa-b --policy '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":"*","Action":"s3:GetObject","R` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v2 RDS publicly accessible] aws rds modify-db-instance --db-instance-identifier saa-db --publicly-accessible --apply-immediately` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v3 public EBS snapshot] aws ec2 modify-snapshot-attribute --snapshot-id snap-0123 --attribute createVolumePermission --operation-type add --group-names all` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v4 Lambda permission for everyone] aws lambda add-permission --function-name saa-fn --statement-id open --action lambda:InvokeFunction --principal '*'` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v5 function URL without auth] aws lambda put-function-url-config --function-name saa-fn --auth-type NONE` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v6 account-level public access block off] aws s3control delete-public-access-block --account-id 111122223333` -> exit 1: T105 steps[0]: removes the public access block
  - `tasks add [v7 public AMI] aws ec2 modify-image-attribute --image-id ami-0123 --launch-permission Add=[{Group=all}]` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: Got through: ['v1 bucket policy Principal *', 'v2 RDS publicly accessible', 'v3 public EBS snapshot', 'v4 Lambda permission for everyone', 'v5 function URL without auth', 'v7 public AMI']. Held: ['c1 public-read ACL', 'c2 BlockPublicAcls=false', 'v6 account-level public access block off']. T105 is a list of literal patterns for S3 ACLs and the public access block; a bucket policy and the public switches of other services are not in it.

### 49. Credentials and non-read-only helper commands

- Gate: `tasks add (T104, T105)`
- Did: One tasks add per command.
- Gate answer:
  - `tasks add [c1 create-access-key] aws iam create-access-key --user-name saa-user` -> exit 1: T105 steps[0]: matches the banned pattern create-access-key \| T106 steps[0]: `create-access-key` lacks the tag book=saa and task=sample-t03 \| T107 no cleanup command undoes `create-access-key` (create command 1 of 1)
  - `tasks add [c2 curl -X POST] curl -X POST https://api.example.com/create` -> exit 1: T104 steps[0]: curl is read-only here: -X is not allowed
  - `tasks add [v1 export-credentials] aws configure export-credentials --format env` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v2 role credentials from instance metadata] curl http://169.254.169.254/latest/meta-data/iam/security-credentials/saa-role` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v3 curl --json (a POST)] curl --json '{"k":"v"}' https://api.example.com/create` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v4 get-session-token] aws sts get-session-token --duration-seconds 129600` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: Got through: ['v1 export-credentials', 'v2 role credentials from instance metadata', 'v3 curl --json (a POST)', 'v4 get-session-token']. Held: ['c1 create-access-key', 'c2 curl -X POST']. 'aws configure' is banned only for set, sso, import and the bare form; curl is checked against a list of flags, not for a GET of a public URL.

### 50. More than one command, redirects and uncaptured variables

- Gate: `tasks add (T104, T115)`
- Did: One tasks add per command.
- Gate answer:
  - `tasks add [c1 pipe] aws s3 ls \| head` -> exit 1: T104 steps[0]: more than one command (shell operator \|)
  - `tasks add [c2 uncaptured $VPC_ID] aws ec2 describe-vpcs --vpc-ids $VPC_ID` -> exit 1: T115 steps[0]: $VPC_ID is used, but no earlier step captures it
  - `tasks add [v1 two commands on two lines] aws s3 ls\naws iam list-users` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v2 process substitution] aws s3 cp <(curl -s https://example.com/payload) s3://saa-b/payload` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v3 redirect into a file] aws sts get-caller-identity > /home/cloudshell-user/.aws/config` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v4 uncaptured ${VPC_ID}] aws ec2 describe-vpcs --vpc-ids ${VPC_ID}` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v5 uncaptured lowercase $vpc_id] aws ec2 describe-vpcs --vpc-ids $vpc_id` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks add [v6 input redirect] aws s3api put-object --bucket saa-b --key k --body /dev/stdin < /etc/passwd` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: Got through: ['v1 two commands on two lines', 'v2 process substitution', 'v3 redirect into a file', 'v4 uncaptured ${VPC_ID}', 'v5 uncaptured lowercase $vpc_id', 'v6 input redirect']. Held: ['c1 pipe', 'c2 uncaptured $VPC_ID']. T104 flags a token only when it holds ; | or &; a line break, < > and <( ) pass. T115 knows $NAME in capitals only.

### 51. Tag text anywhere in the command instead of a tag

- Gate: `tasks add (T106, T108)`
- Did: create-shelf and copy-shelf carry --description "book=saa task=sample-t03" and no --tags; verify is 'aws widget list-shelves --name book=saa'.
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity medium)
- Note: tag_patterns, tag_task_patterns and verify_tag_patterns are searched in the whole command string, not in the value of a tag option or filter.

### 52. Cost hidden behind '$0'

- Gate: `tasks add (T109)`
- Did: cost '$0 (the NAT gateway bills about 4.50 USD for each hour)'; cost_if_forgotten '$0, plus about 108 USD for each day'. No cost fact.
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: T103 and T109 read only amounts written with a $ sign. A price as '4.50 USD', 'USD 4.50', '5 dollars' or 'a few cents' needs no fact and is not held against cost_usd_max or T119.

### 53. A Look task that deletes

- Gate: `tasks add (T103)`
- Did: sample-t01 copy as sample-t03; step 2 command 'aws widget delete-shelf --name saa-prod-shelf'.
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
- Result: **GOT THROUGH** (severity high)
- Note: A Look is 'read-only' only in the sense that its operation does not match create_command_regex.

### 54. Untaggable create with no tag and no saa- name

- Gate: `tasks add (T106, T116)`
- Did: Steps 'aws s3api create-bucket --bucket company-data-2026'; cleanup 'aws s3api delete-bucket --bucket company-data-2026'. No tagging step.
- Gate answer:
  - `tasks add --chapter 99 --file <task.json> --by breaker` -> exit 0: {"added": ["sample-t03"], "replaced": [], "rejected": []}
  - `tasks lint 99` -> exit 2: {"chapter": "99", "ok": true, "errors": []}
  - `warnings of tasks lint 99` -> exit -: ['T116', 'T201', 'T201', 'T113']
- Result: **GOT THROUGH** (severity medium)
- Note: untaggable_rule says the next step tags the resource or the name starts with saa-. Neither is enforced: T116 is a warning, and nothing looks for the tagging step. The verify-by-tag step then finds nothing and reports a clean account.

### 55. Misspelled options that the CLI model does not see

- Gate: `tasks check-cli`
- Did: tasks.json replaced by one Look. Run A (control): 'aws ec2 describe-instances --instance-id i-0123456789abcdef0' (the option is --instance-ids). Run B: a single-dash option, a bare word in place of an option, misspelled shorthand keys, a misspelled --output value, an unknown --query path.
- Gate answer:
  - `tasks check-cli 99 (run A, control)` -> exit 1: {"chapter": "99", "awscli": "1.46.1", "checked": "2026-10-05", "commands_sha256": "26c3f90326ef815b331f82139f95b89c515d959c0408035861ee78bd0078be9e", "ok": false}
  - `tasks check-cli 99 (run B, five misspelled commands)` -> exit 0: {"chapter": "99", "awscli": "1.46.1", "checked": "2026-10-05", "commands_sha256": "c5f35f55218f7ecd781654d464b26a5c59f6bc1c2f375ac2f08c4859d08eadaa", "ok": true}
  - `commands reported ok in run B` -> exit -: ['aws ec2 describe-instances -filters Name=tag:book,Values=saa', 'aws ec2 describe-instances filters Name=tag:book,Values=saa', 'aws ec2 describe-instances --filters Nmae=tag:book,Vaules=saa', 'aws ec2 describe-instances --output jsno', 'aws ec2 describe-instances --query Resrevations[].Instnaces[].InstanceId']
- Result: **GOT THROUGH** (severity high)
- Note: Control exit 1. 5 of 5 misspelled commands are reported ok. cli_model.py skips every token that does not start with '--', and it checks option names only: never shorthand keys, enum values or JMESPath.

### 56. A CLI report written by hand

- Gate: `tasks lint --ship (T113)`
- Did: No check-cli run. _build/reports/cli/99.json written by hand with ok true and the SHA-256 of the fixture's invented 'aws widget' commands. Then tasks lint 99 --ship.
- Gate answer:
  - `tasks lint 99 --ship (before)` -> exit 1: T113 no CLI check report; run `tasks check-cli 99`
  - `tasks lint 99 --ship (after the hand-written report)` -> exit 0: {"chapter": "99", "ok": true, "errors": []}
- Result: **GOT THROUGH** (severity medium)
- Note: T113 trusts any file with the right hash and ok true. The report has no list check (commands is empty here) and no trace of a tool run. The fixture's invented 'aws widget' commands then ship.

### 57. Control: the clean arch spec, then two nodes in one cell

- Gate: `diagram lint`
- Did: Step 1: the base spec (must pass). Step 2: node app2 moved to cell A3, where app1 is.
- Gate answer:
  - `diagram lint --file diagrams/src/breaker-arch.json` -> exit 0: ok   breaker-arch  316x366  nodes 6  edges 5  crossings 0
  - `diagram lint --file diagrams/src/breaker-arch.json` -> exit 1: FAIL breaker-arch  316x366  nodes 6  edges 5  crossings 0 \|      error node-overlap: nodes 'app1' and 'app2' overlap \|      error label-overlap: label of node 'app1' overlaps label of node 'app2'
- Result: **held**
- Note: Base spec exit 0; the overlapping nodes are rejected.

### 58. Raw diagram with two labels on top of each other

- Gate: `diagram lint`
- Did: kind raw; the SVG holds two <text class="dg-nl"> elements at the same x and y, plus a third text that starts 2 units to the right.
- Gate answer:
  - `diagram lint --file diagrams/src/breaker-raw.json` -> exit 0: ok   breaker-raw  340x132  nodes 4  edges 0  crossings 0
- Result: **GOT THROUGH** (severity high)
- Note: The raw kind has no geometry lint at all (TOOLS-diagram.md says so: 'overlap and text width are yours to check'). Three labels in one place pass with exit 0, and so would text wider than its box.

### 59. Node label that states an ungrounded limit

- Gate: `diagram lint`
- Did: Base arch spec; node db1 label 'Max 999 TB' (the number is in neither claim nor say).
- Gate answer:
  - `diagram lint --file diagrams/src/breaker-arch.json` -> exit 0: ok   breaker-arch  316x366  nodes 6  edges 5  crossings 0
- Result: **GOT THROUGH** (severity medium)
- Note: TOOLS-rules.md R2 asks the diagram module for this check ('a label with a number with a unit must repeat a value that stands in claim or say'). It is not implemented, so a hard fact can enter the book inside a figure without a fact.

### 60. Claim of two sentences with absolute words

- Gate: `diagram lint`
- Did: claim 'A request passes through three tiers. it always uses 9 hops and never fails.' (second sentence starts in lowercase).
- Gate answer:
  - `diagram lint --file diagrams/src/breaker-arch.json` -> exit 0: ok   breaker-arch  316x366  nodes 6  edges 5  crossings 0
- Result: **GOT THROUGH** (severity low)
- Note: The one-sentence test looks for '. ' followed by a capital letter. (The chapter lint L702 and L705 check the caption again where the figure is embedded.)

### 61. SVG that does not belong to its spec

- Gate: `gate diagrams`
- Did: The fixture has diagrams/svg/sample-hero.svg and no spec. A valid but different spec is written as diagrams/src/sample-hero.json; diagram build is not run. Then gate 99 --gate diagrams.
- Gate answer:
  - `gate 99 --gate diagrams (fixture, no spec)` -> exit 1: D01 diagram sample-hero has no spec in diagrams/src
  - `gate 99 --gate diagrams (new spec, old SVG)` -> exit 0: {"result": "PASS", "chapter": "99", "gates": [{"gate": "diagrams", "ok": true, "errors": 0, "warnings": 0, "record": "_build/ledger/gates/99.diagrams.json"}], "errors": []}
  - `SVG file` -> exit -: unchanged old file
- Result: **GOT THROUGH** (severity high)
- Note: The gate checks that the spec lints and that an SVG file exists. It never renders the spec and compares, so the reader can see a picture that no spec describes (stale, or drawn by hand with overlaps).

## HOLES (bad inputs that passed)

Ordered by severity, then by attempt number. Each line: attempt, gate, what passed, smallest reproduction.

- **H03** [high] `q add`: Two options with the same text, one marked correct and one marked wrong.
  - Reproduce: q add a single-answer question where options[0].text == options[2].text, options[0].correct true, options[2].correct false.
- **H04** [high] `q add`: Key leaked through option length (short options).
  - Reproduce: q add a difficulty-1 single question with option word counts 17 (key), 4, 3, 4.
- **H06** [high] `q add`: Key leaked through word overlap with the stem (long stem dilutes the Jaccard value).
  - Reproduce: q add a question whose key is built from stem words, whose distractors share none, and whose stem has about 30 content words (every real stem: the real minimum is 60 words).
- **H08** [high] `q add / q lint / gate questions`: Exact copy of an existing question under a new id.
  - Reproduce: q add a copy of a stored question without its id and with another concept; run gate 99 --gate questions.
- **H09** [high] `q dedupe / q lint --all`: Near-duplicate with reordered words.
  - Reproduce: q add sample-q001 (no id, other concept) with the stem 'On one shelf in the us-east-1 Region of Amazon Widget Store, a company keeps 400 widgets. Next month the company expects to add 300 more widgets. All widgets must stay in us-east-1, a compliance rule states. With the LEAST operational overhead, which solution will meet these requirements?'; run q dedupe.
- **H18** [high] `q adjudicate`: One solver (the question's author) signs all three lenses.
  - Reproduce: q adjudicate with three answer files whose solver is the same label for all lenses.
- **H20** [high] `q adjudicate`: Open-book citations: one unrelated fact id, or the one-word quote 'the', for every label.
  - Reproduce: open answer file with citations {A: [{source_id: 'docs/fixture/widget-store/limits', quote: 'the'}], B: same, ...}.
- **H22** [high] `q adjudicate`: Old answer files applied to a question that was replaced after the packs went out.
  - Reproduce: q pack; solvers answer; q add --replace <same id, new stem or options, same key id>; q adjudicate with the old answer files.
- **H24** [high] `q add`: A rejected question comes back under a new id.
  - Reproduce: let a question be rejected in round 1; q add the same JSON without its id.
- **H27** [high] `mocks assemble / mocks check`: A mock built from chapter questions under new ids (one padding sentence in front of the stem).
  - Reproduce: copy a chapter question into data/50-.../questions.json with a new id, pool mock, and one unrelated first sentence of about 12 content words; mocks assemble; mocks check.
- **H32** [high] `cards add`: List answer written with one comma and 'and', or with slashes.
  - Reproduce: cards add a decide card with back 'A shelf, a crate and a quota.'
- **H35** [high] `cards add`: Wrong number written as a word.
  - Reproduce: cards add with back 'A crate. It holds ninety widgets.'
- **H36** [high] `cards add`: Card whose answer contradicts its own fact.
  - Reproduce: cards add a cannot card with a back that states the opposite of the fact in facts.
- **H41** [high] `speak add`: Ungrounded absolute claims in the script.
  - Reproduce: speak add with a sixty_second line 'A shelf is always global and never private.'
- **H42** [high] `speak add`: Spoken numbers that P109 does not see.
  - Reproduce: speak add with the line 'One shelf holds up to nineteen widgets.' or '... nine hundred of your widgets.'
- **H44** [high] `tasks add`: A task that creates resources and deletes nothing (create verbs outside the list).
  - Reproduce: tasks add a Try whose creating steps use put-*, import-*, start-*, register-*, restore-*, request-* or 'aws s3 mb', with a cleanup list of one read-only command.
- **H45** [high] `tasks add`: Cleanup deletes a different resource, or only pretends (--dry-run).
  - Reproduce: tasks add where each create has a delete-<noun> cleanup command that names another resource or carries --dry-run.
- **H47** [high] `tasks add (T105)`: Security group opened to the world: ::/0 written in full, prefix list, split ranges, rules in a file, other operations.
  - Reproduce: tasks add with a step 'aws ec2 modify-security-group-rules --group-id <SG_ID> --security-group-rules SecurityGroupRuleId=sgr-0123,SecurityGroupRule={IpProtocol=tcp,FromPort=22,ToPort=22,CidrIpv4=0.0.0.0/0}' (or any 'got through' line of this entry).
- **H48** [high] `tasks add (T105)`: Public exposure by other commands.
  - Reproduce: tasks add with a step 'aws s3api put-bucket-policy --bucket saa-b --policy <a policy with "Principal":"*">' (or any 'got through' line of this entry).
- **H49** [high] `tasks add (T104, T105)`: Credentials and non-read-only helper commands.
  - Reproduce: tasks add with a step 'aws configure export-credentials --format env'.
- **H50** [high] `tasks add (T104, T115)`: More than one command, redirects and uncaptured variables.
  - Reproduce: tasks add with a step command 'aws s3 ls\naws iam list-users' (a line break inside the JSON string).
- **H52** [high] `tasks add (T109)`: Cost hidden behind '$0'.
  - Reproduce: tasks add with cost '$0 (about 4.50 USD for each hour)' and cost_facts [].
- **H53** [high] `tasks add (T103)`: A Look task that deletes.
  - Reproduce: tasks add a look whose step command is a delete-*, terminate-*, put-* or modify-* operation.
- **H55** [high] `tasks check-cli`: Misspelled options that the CLI model does not see.
  - Reproduce: tasks check-cli on 'aws ec2 describe-instances -filters Name=tag:book,Values=saa' or 'aws ec2 describe-instances --filters Nmae=tag:book,Vaules=saa'.
- **H58** [high] `diagram lint`: Raw diagram with two labels on top of each other.
  - Reproduce: diagrams/src/<id>.json with kind raw and an SVG that has two <text> elements at the same position; diagram lint --file.
- **H61** [high] `gate diagrams`: SVG that does not belong to its spec.
  - Reproduce: change diagrams/src/<id>.json (or hand-edit diagrams/svg/<id>.svg) without running diagram build; gate <ch> --gate diagrams.
- **H07** [medium] `q add`: Explanation names options by position and letter without the word 'Option'.
  - Reproduce: q add with explanation text 'The second option is wrong, and (C) is wrong too; B is the usual trap.'
- **H14** [medium] (partly) `q pack`: Stored option order recovered from a pack (the shuffle is reversible).
  - Reproduce: python: order = qbank.permutation(book['book']['mock_seed'], item['id'], pack['lens'], pack['round'], range(len(item['options']))); the label at order.index(0) is the option stored first.
- **H17** [medium] `q adjudicate`: Answer files without a solver field.
  - Reproduce: q adjudicate with three answer files that have pack, lens, answers and no solver.
- **H19** [medium] `q adjudicate`: Closed lens without stem_only, ambiguity lens without a case.
  - Reproduce: q adjudicate with stem_only null and case null in every row.
- **H23** [medium] `q add --replace`: More than one edit after a failed round.
  - Reproduce: after a round-0 failure run q add --replace on the same id twice.
- **H28** [medium] `mocks check`: Two questions of one mock with the same stem.
  - Reproduce: give two questions of one mock the same stem; mocks check.
- **H29** [medium] `mocks check`: A mock question that copies a drill-pool question.
  - Reproduce: copy the stem of a pool-drill question into a mock question; mocks check.
- **H34** [medium] `cards add`: Back far over the word limit, joined with hyphens.
  - Reproduce: cards add with a back whose words are joined by hyphens (or slashes).
- **H39** [medium] `speak add`: A 60-second answer of about 300 words, with words joined by hyphens.
  - Reproduce: speak add with lines such as 'The short answer is: a shelf keeps your widgets in one Region. The-team-keeps-the-widgets-on-the-shelf-...'
- **H40** [medium] `speak add`: 300 words outside the script: follow-up answer and key point.
  - Reproduce: speak add with a follow_ups[].answer of 300 words.
- **H46** [medium] `tasks add`: run-instances undone by stop-instances.
  - Reproduce: tasks add with run-instances and a cleanup of stop-instances.
- **H51** [medium] `tasks add (T106, T108)`: Tag text anywhere in the command instead of a tag.
  - Reproduce: tasks add with 'aws widget create-shelf --name saa-x --description "book=saa task=<id>"' and no tag option.
- **H54** [medium] `tasks add (T106, T116)`: Untaggable create with no tag and no saa- name.
  - Reproduce: tasks add with create-bucket on a name without the saa- prefix and no put-bucket-tagging step.
- **H56** [medium] `tasks lint --ship (T113)`: A CLI report written by hand.
  - Reproduce: write _build/reports/cli/<id>.json = {chapter, ok: true, commands_sha256: sha256 of the commands joined with newlines}; tasks lint <id> --ship.
- **H59** [medium] `diagram lint`: Node label that states an ungrounded limit.
  - Reproduce: arch spec with a node label 'Max 999 TB' that the claim and the say lines do not hold.
- **H05** [low] `q add`: Key is the longest option, just inside the 30% spread.
  - Reproduce: q add a single question with option word counts 15 (key), 11, 11, 11.
- **H10** [low] `q add`: Negative stem written in lowercase.
  - Reproduce: q add with a stem that asks 'which ... is not ...' in lowercase.
- **H11** [low] `q add`: 'None of these options.' as an option.
  - Reproduce: q add with an option text 'None of these options.'
- **H21** [low] `q adjudicate`: Two rows for one question in one answer file (first agrees, second disagrees and flags).
  - Reproduce: answer file with two rows of the same id; the first row is the key.
- **H25** [low] (partly) `q set-status`: Mark a never-verified candidate as verified.
  - Reproduce: q set-status --chapter 99 --status verified <candidate id>
- **H30** [low] `mocks check`: Manifest edited by hand: minutes and counts changed.
  - Reproduce: edit data/50-.../mock.json: minutes 9999, counts {}; mocks check.
- **H37** [low] `cards add`: Near-duplicate front with three filler words.
  - Reproduce: cards add a card whose front is an existing front plus three new words.
- **H60** [low] `diagram lint`: Claim of two sentences with absolute words.
  - Reproduce: arch spec with claim 'One thing is true. another thing always holds.'

## Root causes (for the owner of the fix)

1. **Word counting splits on whitespace only** (`lint.word_count`). Hyphen- or slash-joined words defeat every word limit: card back, spoken scripts, step texts, options (attempts 34, 39).
2. **Similarity is measured on the stem only, and as a Jaccard value.** `q dedupe` and K04 never compare options, keys or explanations; reordering clauses or adding one sentence drops the value below 0.6 (9, 27). Q113 has the same weakness: a long stem dilutes the overlap of a key that is made of stem words (6).
3. **Duplicate checks are not part of any chapter gate.** `q add`, `q lint CH` and the `questions` gate do not run `q dedupe`; only `q lint --all` does (8). `mocks check` ignores duplicates inside one mock and copies of drill questions (28, 29). A rejected question can be added again (24).
4. **Adjudication trusts the answer files.** No solver identity or independence (17, 18), no required lens evidence (19), no relevance or minimum length for citations (20), no schema for rows (21), and no binding of an answer to the question revision or text (22). Round 1 allows any number of edits (23).
5. **Length and position leaks are checked only as bank shares.** Q104 is off below a mean of 10 words and measures against a mean that the key itself raises (4, 5); Q202 needs 10 questions and is a warning. The pack shuffle uses a public seed (14).
6. **Literal lists instead of rules.** Option letters (7), negative stems (10), banned option phrases (11), list answers (32), number words (35, 42), create verbs (44), banned commands (47, 48, 49), shell operators (50), dollar amounts (52).
7. **Cards and spoken scripts are not tied to their facts.** Only digits with a unit are checked; a sentence can contradict the fact it lists, or state 'always' and 'never' with no fact (36, 41). Follow-up answers and key points have no length limit (40).
8. **Task cleanup is paired by verb and noun, not by resource.** Another name, `--dry-run`, or `stop` for `run` satisfy T107 (45, 46); tag patterns match anywhere in the command (51); untaggable creates need neither tag nor prefix (54); a Look can delete (53).
9. **Reports and pictures are not bound to a tool run.** A hand-written CLI report satisfies T113 (56); the `diagrams` gate accepts any SVG file next to a spec that lints (61); the `raw` kind has no geometry check (58); node labels with numbers are not held against claim or say (59).
10. **The CLI model checks option names that start with `--` and nothing else** (55): single-dash typos, bare words, shorthand keys, enum values and JMESPath are not checked.

## Limits of this report

- The fixture service is invented, so 'bad' here means bad by the written rules (RULINGS, TOOLS, SPEC), not bad AWS facts.
- Attempts 14, 56 and 61 need write or read access to files under the book folder. Every agent of the build has that access.
- The fixture `SPEC.json` sets `key_position_share_max`, `key_is_longest_share_max` and `stem_key_overlap_margin_max` to 1.0, so the tool's own tests of Q113 and Q202 patch the values. Attempts here use 0.25 for Q113 and leave Q202 alone (it needs 10 questions).
- Not tried: `tasks emulate`, `drills build`, `cards build`, the web app, and the chapter lint of hand-written Markdown (another breaker has that part).
