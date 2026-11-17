# Gate break report: grounding gates

Date: 2026-10-04. Tool contract: `TOOLS.md` version 0.9. The tool was not changed.

All attempts ran in the sandbox `aws-saa-book/_build/tmp/breaker-grounding/` (a fresh copy of `tools/tests/fixtures/book/` before each attempt), with `--book-dir`. No real data was touched. Driver: `python3 aws-saa-book/tools/helpers/break_grounding.py` (raw results: `_build/reports/gate-break-grounding.json`).

## Summary

- Attempts: 66 (facts add, verify, vote, finalize: 25; amend: 4; lint: 32; sync: 5).
- Stopped by a gate: 17.
- Passed: 49; 48 of them are bad inputs (one, L27, is harmless).
- The 48 passing inputs come from 14 root holes, listed at the end.
- What held: a changed or invented quote (M3), a quote stitched from sentences that are not adjacent (M3), another number (M5), another unit directly after the number (M5), a stored fact after its snapshot changed (M2), a status set by hand without a vote line (F04), a patch that names `status`, `votes` or `rev`, an amend to a number that no quote has, a link text with the number in words (L303), a changed section role (L105), a hard claim in a reveal block, an absolute word alone in its sentence, a hand edit of a generated chapter file (`sync --check`).
- The default-against-maximum fact (F12) passes every mechanical check and is stopped only by the entail voter. With H7 the author is that voter.

## Attempts

`Passed: yes` means the bad input got through the gate named in the entry.

### A01: facts amend + finalize

- Did: Amend of a verified hard fact: new false claim plus `hard: false` (the displays stay, so no dependent is reset).
- Answer: facts amend -> exit 0: {"fact": "widget-shelf-scope", "rev": 2, "status": "mech-pass", "replaced": 0, "broken_links": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-shelf-scope"], "disputed": [], "rejected": [], "pending": []} [status verified]
- Answer: lint 99 --draft names the fact: False
- Passed: YES
- Note: The amend empties the votes, but `hard: false` removes the need for any vote, so finalize verifies the new claim at once. `facts amend` has no --by, so the change is not attributed.

### A02: facts amend

- Did: Patch that tries to set `status`, `votes` and `rev` directly.
- Answer: facts amend -> exit 1: error: a patch cannot change: status, votes, rev
- Passed: no
- Note: control

### A03: facts amend (M5)

- Did: Amend that changes the number of a verified fact (50 to 500) without new evidence.
- Answer: facts amend -> exit 1: M5 number 500 in claim appears in no quote; M5 number 500 in display '500 widgets' appears in no quote
- Passed: no
- Note: control

### A04: facts amend + finalize + lint

- Did: Amend of the verified limit `50 widgets`: kind behavior, hard false, claim and display `50 thousand widgets`. The tool then rewrites the link text in the chapter by itself.
- Answer: facts amend -> exit 0: {"fact": "widget-crate-capacity", "rev": 2, "status": "mech-pass", "replaced": 6, "broken_links": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-crate-capacity"], "disputed": [], "rejected": [], "pending": []} [status verified]
- Answer: 2-deep.md now holds `[50 thousand widgets](../facts/widget.md#widget-crate-capacity)`: True
- Answer: lint 99 --draft -> exit 2, errors that name the fact or the new value: 0
- Passed: YES
- Note: Combines F08 with A01. One command changes the canon and the prose; the chapter is marked stale and the items are reset, but every gate passes again when the stages rerun, with no vote on the new value.

### F01: facts add (M3)

- Did: Fabricated quote: the real sentence with 500 changed to 900.
- Answer: facts add -> exit 1: M3 evidence 0: the quote is not in the snapshot text (verbatim text only): 'Each shelf can hold up to 900 widgets.'
- Passed: no
- Note: control: must be rejected

### F02: facts add (M3)

- Did: Quote stitched from two real sentences that are not adjacent on the page (line 7 first half + line 8).
- Answer: facts add -> exit 1: M3 evidence 0: the quote is not in the snapshot text (verbatim text only): 'A shelf is a Regional resource. Each shelf can hold up to 500 widgets.'
- Passed: no

### F03: facts add (M4) + finalize

- Did: Real quote cut so that the first two words `You cannot` are dropped; claim says the opposite (`You can move a shelf`); kind behavior, hard false, no votes.
- Answer: facts add -> exit 0: {"added": ["widget-x-move"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-move"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: A quote of 8 or more words may start in the middle of a sentence. `can` is no absolute word, so M11 accepts hard=false, and a fact that is not hard is verified without any vote.

### F04: facts add (M5)

- Did: Real quote (50 widgets), claim and display carry another number (500 widgets).
- Answer: facts add -> exit 1: M5 number 500 in claim appears in no quote; M5 number 500 in display '500 widgets' appears in no quote
- Passed: no
- Note: control

### F05: facts add (M5)

- Did: Real quote (7 days), claim and display carry another unit (7 hours).
- Answer: facts add -> exit 1: M5 unit mismatch: no quote has 7 followed by hours (claim); M5 unit mismatch: no quote has 7 followed by hours (display '7 hours')
- Passed: no
- Note: control

### F06: facts add (M5, M11) + finalize

- Did: Same unit swap, with one adjective between number and unit (`7 full hours`), hard false, no votes.
- Answer: facts add -> exit 0: {"added": ["widget-x-unit2"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-unit2"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: M5 and M11 see a unit only directly after the number (one optional space or hyphen). `7 full hours` is a bare 7, which the quote has.

### F07: facts add (M5, M11) + finalize

- Did: Unit swap with two spaces between number and unit (`7  hours`), hard false, no votes.
- Answer: facts add -> exit 0: {"added": ["widget-x-unit3"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-unit3"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: The unit regex allows one space; a second space hides the unit.

### F08: facts add (M5, M11) + finalize

- Did: Magnitude word after the real number (`50 thousand widgets` against a quote with 50), hard false, no votes.
- Answer: facts add -> exit 0: {"added": ["widget-x-mag"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-mag"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: The digit string 50 is in the quote; `thousand` is neither unit nor count noun.

### F09: facts add (M5, M11) + finalize

- Did: Suffix on the number (`50K widgets` against a quote with 50), hard false, no votes.
- Answer: facts add -> exit 0: {"added": ["widget-x-k"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-k"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: The number regex has no check of the character after the digits.

### F10: facts add (M5, M11) + finalize

- Did: Number written in words (`nine hundred widgets`) against a quote with 500, hard false, no votes.
- Answer: facts add -> exit 0: {"added": ["widget-x-word"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-word"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: On the claim side a number word counts only directly before a unit or count noun, and only zero to twelve.

### F11: facts add (M7, M11) + finalize

- Did: False claim without a number or a listed absolute word, with an unrelated real quote; display taken from the claim; hard false, no votes.
- Answer: facts add -> exit 0: {"added": ["widget-x-false"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-false"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: M7 accepts a display that stands only in the claim. Nothing mechanical ties the claim to the quote, and a non-hard fact needs no vote.

### F12: facts add + finalize

- Did: Default against maximum: the quote states a maximum, the fact says default and adjustable (the quota table says No).
- Answer: facts add -> exit 0: {"added": ["widget-x-defmax"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 2: {"verified": [], "disputed": [], "rejected": [], "pending": [{"id": "widget-x-defmax", "missing": ["entail"]}]}
- Passed: no
- Note: The mechanical checks pass (status mech-pass); the fact stays pending for an entail vote. Stopped only by the voter.

### F13: facts vote + finalize

- Did: The author of F12 (label miner-a) votes `support` on the own fact under a second label (miner-b).
- Answer: facts vote --by miner-b (same agent, other label) -> exit 0: {"appended": 1, "refused": [], "disputed": [], "verdicts": [{"fact": "widget-x-defmax", "lens": "entail", "verdict": "support"}]}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-defmax"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: A label is free text. One agent with two labels is author and verifier.

### F14: facts vote

- Did: Author label `miner-a`, vote under `Miner-A` (case changed).
- Answer: facts vote --by Miner-A -> exit 0: {"appended": 1, "refused": [], "disputed": [], "verdicts": [{"fact": "widget-x-defmax", "lens": "entail", "verdict": "support"}]}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-defmax"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: The author test is an exact string comparison.

### F15: facts vote + finalize

- Did: A verifier disputes the fact; the attacker reuses the verifier's label for a later `support` vote on the same rev.
- Answer: honest vote not-supported --by verifier-b -> exit 0: {"appended": 1, "refused": [], "disputed": [], "verdicts": [{"fact": "widget-x-defmax", "lens": "entail", "verdict": "not-supported"}]}
- Answer: facts finalize -> exit 1: {"verified": [], "disputed": ["widget-x-defmax"], "rejected": [], "pending": []} [status disputed]
- Answer: second vote support, label verifier-b reused by the attacker -> exit 0: {"appended": 1, "refused": [], "disputed": [], "verdicts": [{"fact": "widget-x-defmax", "lens": "entail", "verdict": "support"}]}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-defmax"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: The last vote of a voter and lens counts, so a disputed fact becomes verified without an amend and without a new rev.

### F16: facts add (M4, M8)

- Did: Quote made of the table header and two table rows written without pipes (so no `table_header` is asked for); the claim pairs the 500 of one row with the name of another row.
- Answer: facts add -> exit 0: {"added": ["widget-x-table"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 2: {"verified": [], "disputed": [], "rejected": [], "pending": [{"id": "widget-x-table", "missing": ["entail"]}]}
- Passed: YES
- Note: normalize_text removes pipes and rule lines, so flattened table text is `verbatim`. The M4 table rules apply only when the quote starts with `|`. The fact is mech-pass and waits for an entail vote.

### F17: facts add (M3, M8)

- Did: Quote that runs across a section heading (`## Crates`) and starts and ends in the middle of sentences.
- Answer: facts add -> exit 0: {"added": ["widget-x-head"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-head"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: Heading text is joined to the body text by the normaliser; only a quote that is exactly one heading line is page furniture.

### F18: facts add (M3, M7) + finalize

- Did: Words smuggled into a real quote inside angle brackets. The stored `verbatim` quote reads `You <can now move a shelf, where before you> cannot move ...`; the display `can now move a shelf` is found in that quote.
- Answer: facts add -> exit 0: {"added": ["widget-x-tag"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-tag"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: normalize_text drops anything of the form <...> (up to 400 characters) on both sides, so M3 matches (the display is accepted because it stands in the claim). The stored quote, which the fact sheet prints and the verifier packet shows, is not the page text.

### F19: facts add (M2)

- Did: Snapshot written by hand into the corpus folder (a .txt and a three-key .meta.json with an allowed URL, never fetched), then a fact that quotes it and an honest entail vote.
- Answer: facts add -> exit 0: {"added": ["widget-x-fake"], "rejected": [], "conflicts": []}
- Answer: facts vote --by verifier-b -> exit 0: {"appended": 1, "refused": [], "disputed": [], "verdicts": [{"fact": "widget-x-fake", "lens": "entail", "verdict": "support"}]}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-fake"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: M2 asks only that the .txt exists and that the meta `url` equals the evidence URL. There is no check that the fetch tool made the snapshot (no fetch log entry, no raw file, no `sha256` in the meta). An honest verifier sees a matching quote and supports.

### F20: facts add (M8)

- Did: Quote taken from a navigation line of the page (breadcrumb and footer words), none of them in the BOILERPLATE list.
- Answer: facts add -> exit 0: {"added": ["widget-x-nav"], "rejected": [], "conflicts": []}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-nav"], "disputed": [], "rejected": [], "pending": []}
- Passed: YES
- Note: M8 knows ten fixed phrases. Navigation text without one of them is an accepted quote.

### F21: facts verify (M2)

- Did: One sentence added by hand to the snapshot .txt that the seven verified fixture facts cite; meta untouched.
- Answer: facts verify --service widget -> exit 1: M2 snapshot-changed: evidence 0: the text of docs/fixture/widget-store/limits has another SHA-256 now; M2 snapshot-changed: evidence 0: the text of docs/fixture/widget-store/limits has another SHA-256 now; M2 snapshot-changed: evidence 0: the text of docs/fixture/widget-store/limits has another SHA-256 now; M2 snapshot-changed: evidence 1: the text of docs/fixture/widget-store/limits has another SHA-256 now; M2 snaps...
- Passed: no
- Note: control: the stored evidence hash no longer matches

### F22: facts add (M2)

- Did: Same hand edit of the snapshot .txt, then a NEW fact that quotes the added sentence (the meta still holds the old sha256).
- Answer: facts add -> exit 0: {"added": ["widget-x-tamper"], "rejected": [], "conflicts": []}
- Answer: facts vote --by verifier-b -> exit 0: {"appended": 1, "refused": [], "disputed": [], "verdicts": [{"fact": "widget-x-tamper", "lens": "entail", "verdict": "support"}]}
- Answer: facts finalize -> exit 0: {"verified": ["widget-x-tamper"], "disputed": [], "rejected": [], "pending": []}
- Answer: facts verify widget-x-tamper -> exit 0: {"checked": 1, "ok": 1, "failed": []}
- Passed: YES
- Note: `facts add` fills evidence.sha256 from the current .txt and never compares the .txt with the `sha256` of its own meta file. Only facts stored before the edit notice it (F21).

### F23: facts-final gate (F04), facts verify

- Did: Facts file edited by hand: status set to verified and a `votes` summary written into the fact; the vote log untouched.
- Answer: gate 99 --gate facts-final -> exit 1: F04 status verified is not backed by the vote log at rev 1 (no counting vote for entail); the status was edited by hand
- Answer: facts verify widget-x-hand -> exit 1: F04 status verified is not backed by the vote log at rev 1 (no counting vote for entail); the status was edited by hand [status now candidate]
- Passed: no
- Note: control: F04 compares with the vote log

### F24: facts-final gate (F04), facts verify

- Did: As F23, plus one forged line appended by hand to the vote log `_build/facts/votes/widget.jsonl`.
- Answer: gate 99 --gate facts-final -> exit 0: {"result": "PASS", "chapter": "99", "gates": [{"gate": "facts-final", "ok": true, "errors": 0, "warnings": 0, "record": "_build/ledger/gates/99.facts-final.json"}], "errors": []} [does not name widget-x-hand]
- Answer: facts verify widget-x-hand -> exit 0: {"checked": 1, "ok": 1, "failed": []} [status verified]
- Passed: YES
- Note: The vote log is a plain file with no signature or chain; F04 trusts it.

### F25: facts verify, facts-final gate

- Did: Claim of a verified fact rewritten by hand to the opposite; rev, status, displays and votes untouched.
- Answer: facts verify widget-shelf-move -> exit 0: {"checked": 1, "ok": 1, "failed": []}
- Answer: gate 99 --gate facts-final -> exit 0: {"result": "PASS", "chapter": "99", "gates": [{"gate": "facts-final", "ok": true, "errors": 0, "warnings": 0, "record": "_build/ledger/gates/99.facts-final.json"}], "errors": []} [does not name the fact]
- Answer: facts render -> sheet holds the false claim: True
- Passed: YES
- Note: A vote is bound to (fact id, rev) only, not to a hash of claim, values and evidence. A hand edit that keeps `rev` keeps the votes.

### L01: lint (L303/L304/L306)

- Did: Control: `Each crate always holds 50 widgets.` added as a new paragraph in `2-deep.md`, section How it works (role how, strict).
- Answer: lint 99 -> exit 1; new errors against the unchanged fixture: 1; new warnings: 0
- Answer: new error L304 99-sample/2-deep.md: number with a unit `50 widgets`, absolute word `always` without a fact link: Each crate always holds 50 widgets.
- Passed: no
- Note: control

### L02: lint (L303/L304/L306)

- Did: Bare number with a non-breaking space: `A crate holds 9000\u00a0widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: The number regex allows a plain space or a hyphen only; the text unit is not normalised before matching.

### L03: lint (L303/L304/L306)

- Did: Bare number written as a word: `A crate holds nine thousand widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: Stated in TOOLS-rules R2 (number words are not matched). The reader still gets an ungrounded hard number.

### L04: lint (L303/L304/L306)

- Did: One adjective between number and count noun: `A crate holds 9000 small widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: Real cases of the same shape: `5 read replicas`, `1,000 concurrent executions`, `200 route tables`, `5 Elastic IP addresses`.

### L05: lint (L303/L304/L306)

- Did: Bold around the number or the noun: `A crate holds 9000 **widgets**.`
- Answer: lint 99 -> exit 1; new errors against the unchanged fixture: 1; new warnings: 0
- Answer: new error L304 99-sample/2-deep.md: number with a unit `9000 widgets` without a fact link: A crate holds 9000 widgets.
- Passed: no

### L06: lint (L303/L304/L306)

- Did: HTML entity for the space: `A crate holds 9000&nbsp;widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: Entities are not decoded before the number and absolute-word rules.

### L07: lint (L303/L304/L306)

- Did: HTML entity inside an absolute word: `A shelf is alw&#97;ys private.` (renders as `always`)
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES

### L08: lint (L303/L304/L306)

- Did: Zero-width space inside an absolute word: `A crate is on\u200bly for shipping, and it is ne\u200bver private.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES

### L09: lint (L303/L304/L306)

- Did: Absolute claims with words outside the list: `A crate is invariably public. No one except the owner is able to delete it, and nobody is able to move it.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: The list has nine entries. `no`, `not`, `all`, `every`, `any`, `none`, `maximum`, `minimum`, `at least`, `no more than`, `limited to`, `unlimited`, `required`, `does not support`, `is not possible`, `automatically`, `exclusively` are free.

### L10: lint (L303/L304/L306)

- Did: `can not` written as two words: `You can not copy a crate.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES

### L11: lint (L303/L304/L306)

- Did: Unit outside the list: `A crate weighs 9000 kg and takes 9000 TPS.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: The real SPEC list has no `bytes`, `TPS`, `RCU`, `WCU`, `AZs`, `Tbps`, `EB`, `volumes`, `snapshots`, `nodes`, `records`, `times`, `x`.

### L12: lint (L303/L304/L306)

- Did: Plus sign after the number: `A crate holds 9000+ widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES

### L13: lint (L303/L304/L306)

- Did: The claim in inline code: ``A crate holds `up to 9000 widgets`.``
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: Inline code is removed before the rules run (it is meant for commands), but it renders as readable text.

### L14: lint (L303/L304/L306)

- Did: The claim as a question: `Did you know that a crate always holds up to 9000 widgets?`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: Sentences that end with `?` are never read by L304 (R2).

### L15: lint (L303/L304/L306)

- Did: A `no-fact` marker on a factual sentence: `A crate must hold at most 9000 widgets. <!-- no-fact: requirement -->`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 1
- Answer: new warning W308 99-sample/2-deep.md: no-fact marker (requirement): A crate must hold at most 9000 widgets.
- Passed: YES
- Note: Passes with warning W308 by design; the gate result is exit 2 (pass). Only the claims reviewer can stop it.

### L16: lint (L303/L304/L306)

- Did: Absolute claim split over two sentences: `A crate stays public. Always.`
- Answer: lint 99 -> exit 1; new errors against the unchanged fixture: 1; new warnings: 0
- Answer: new error L304 99-sample/2-deep.md: absolute word `Always` without a fact link: Always.
- Passed: no
- Note: control

### L17: lint (L303/L304/L306)

- Did: Number and unit split over two sentences: `The limit of a crate is 9000. The unit is widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: A bare number without a unit is never a finding.

### L18: lint (L303/L304/L306)

- Did: Link text that hides the number in words: `A shelf holds [five hundred widgets](...#widget-shelf-max-widgets).`
- Answer: lint 99 -> exit 1; new errors against the unchanged fixture: 1; new warnings: 0
- Answer: new error L303 99-sample/2-deep.md: link text `five hundred widgets` holds no value of widget-shelf-max-widgets
- Passed: no
- Note: control

### L19: lint (L303/L304/L306)

- Did: Link text with the display inside a larger number written with a space: `[up to 2 500 widgets](...)`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: holds_display guards digits, commas and periods before the display, not a space-separated thousands group.

### L20: lint (L303/L304/L306)

- Did: Link text that holds the display and contradicts it: `[not 500 widgets but 9000 widgets](...)`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: L303 is a substring test, and the link then satisfies L304 for the whole sentence.

### L21: lint (L303/L304/L306)

- Did: Negated display: `A new shelf is [not private](...#widget-shelf-default-private) and can be read by all users.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES

### L22: lint (L303/L304/L306)

- Did: Piggyback: an ungrounded hard claim in a sentence that has a fact link to another fact: `A crate always holds 9000 widgets, more than the [500 widgets](...) of a shelf.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: One fact link satisfies L304 for its sentence (R2). Left to the claims reviewer by design.

### L23: lint (L303/L304/L306)

- Did: A real fact link on the wrong subject: `A crate holds [up to 500 widgets](...#widget-shelf-max-widgets).` (the fact is about shelves)
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: No mechanical check of the subject; left to the claims reviewer.

### L24: lint (L303/L304/L306)

- Did: Exempt role: the flag of How it works changed from role=how to role=example, plus the control sentence.
- Answer: lint 99 -> exit 1; new errors against the unchanged fixture: 2; new warnings: 0
- Answer: new error L105 99-sample/2-deep.md: flag role is example; the section has role how
- Answer: new error L304 99-sample/2-deep.md: number with a unit `9000 widgets`, absolute word `always` without a fact link: Each crate always holds 9000 widgets.
- Passed: no
- Note: control

### L25: lint (L303/L304/L306)

- Did: Hard claim placed in the section whose role is example (Decision record): `**Decision.** ... A crate always holds up to 9000 widgets, and a shelf can never be private.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: Sections with grounding `example` are not checked at all. W903 (story numbers) did not fire either: the fixture has no data/harken.json entry.

### L26: lint (L303/L304/L306)

- Did: Hard claim in a `Startup example` callout inside the strict section: `> **Startup example:** Callvale learned that a crate always holds up to 9000 widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: Callouts with grounding `example` are exempt (R2 exemption 3).

### L27: lint (L303/L304/L306)

- Did: Hard claim in an HTML comment: `<!-- A crate always holds 9000 widgets. -->`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES (harmless)
- Note: Passes, and is harmless for a Markdown reader (a comment is not rendered). Not counted as a hole.

### L28: lint (L303/L304/L306)

- Did: Hard claim inside the collapsed Go deeper block (details).
- Answer: lint 99 -> exit 1; new errors against the unchanged fixture: 1; new warnings: 0
- Answer: new error L304 99-sample/2-deep.md: number with a unit `9000 widgets`, absolute word `always` without a fact link: A crate always holds 9000 widgets.
- Passed: no
- Note: control

### L29: lint (L303/L304/L306)

- Did: Hard claim in the summary line of a details block: `<summary>Go deeper: a crate always holds 9000 widgets</summary>`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: The summary line is visible text, even when the block is closed.

### L30: lint (L303/L304/L306)

- Did: AWS quote block cut so that the negation is gone: `> "move a shelf to another Region."` under the real attribution line.
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: L306 accepts any substring of an evidence quote, also one that starts in the middle of a sentence.

### L31: lint (L303/L304/L306)

- Did: Full-width digits: `A crate holds ９０００ widgets.`
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES

### L32: lint (L303/L304/L306)

- Did: A hand-written file that the template does not list: `99-sample/6-extra.md` with two false hard claims.
- Answer: lint 99 -> exit 2; new errors against the unchanged fixture: 0; new warnings: 0
- Passed: YES
- Note: lint reads only the files of the resolved template. An extra .md in a chapter folder is reader-facing and unchecked.

### S01: sync --check

- Did: Generated `5-quiz.md` edited by hand (first `500 widgets` changed to `900 widgets`).
- Answer: baseline sync 99 --check -> exit 0: {"checked": 5, "stale": [], "missing": []}
- Answer: after the edit -> exit 1: {"checked": 5, "stale": ["99-sample/5-quiz.md"], "missing": []}
- Passed: no
- Note: control

### S02: sync --check, sync gate

- Did: Generated fact sheet `facts/widget.md` edited by hand: the AWS quote and the value changed from 500 to 900.
- Answer: sheet existed after sync --all: True
- Answer: sync 99 --check -> exit 0: {"checked": 5, "stale": [], "missing": []}
- Answer: gate 99 --gate sync -> exit 0: {"result": "PASS", "chapter": "99", "gates": [{"gate": "sync", "ok": true, "errors": 0, "warnings": 0, "record": "_build/ledger/gates/99.sync.json"}], "errors": []}
- Answer: sync --all --check -> exit 1: {"checked": 7, "stale": ["facts/widget.md"], "missing": []}
- Answer: sync 99 --only facts --check -> exit 1: {"checked": 2, "stale": ["facts/widget.md"], "missing": []}
- Passed: YES
- Note: The chapter form of `sync --check`, which is what the `sync` gate of `edit`, `fix` and `finalize` runs, does not build the fact sheets. Only `sync --all --check` or `--only facts` compares them.

### S03: sync --check, lint

- Did: Generated fact sheet `facts/widget.md` deleted (every fact link of the chapter points at it).
- Answer: sync 99 --check -> exit 0: {"checked": 5, "stale": [], "missing": []}
- Answer: lint 99 -> exit 2, L601 findings that name facts/: 0
- Passed: YES
- Note: Neither the sync gate nor the lint notices that the target of every fact link is missing.

### S04: sync --all --check

- Did: An orphan `facts/ghost.md` written by hand in the form of a generated fact sheet, for a service with no fact.
- Answer: sync --all --check -> exit 0: {"checked": 7, "stale": [], "missing": []}
- Passed: YES
- Note: sync compares only the files it would write; a file it would not write is never reported.

### S05: sync --check

- Did: One false sentence appended after the last line of generated `5-quiz.md`.
- Answer: sync 99 --check -> exit 1: {"checked": 5, "stale": ["99-sample/5-quiz.md"], "missing": []}
- Passed: no
- Note: control

## HOLES

Each hole lists the attempts that show it. The reproduction of an attempt is one or two plain commands in a sandbox.

### H1 (critical): A fact that is not `hard` is verified with zero votes, and M11 decides `hard` with nine words and a number-with-unit test

Attempts: F03, F11, F17, F20. Any false claim that avoids the nine absolute words and a number directly followed by a unit can be stored with `hard: false` and any real quote of 8 words. `facts finalize` verifies it at once. Smallest reproduction: F11.

- F03: facts add a fact with claim `You can move a shelf to another Region.`, display `move a shelf to another Region`, quote `move a shelf to another Region. To use another Region, copy the shelf.`, kind behavior, hard false; then facts finalize ID -> verified
- F11: claim `A shelf copies its widgets to every other Region automatically, and every user of the account reads it.`, display `copies its widgets to every other Region`, quote `A crate is a container for widgets that you ship between Regions.`, kind behavior, hard false; facts add, facts finalize -> verified
- F17: quote `copy the shelf. Crates A crate is a container for widgets` -> accepted
- F20: quote `AWS Documentation Amazon Widget Store User Guide Feedback Preferences Contact Us English Create an AWS Account` -> accepted

### H2 (critical): M5 and M11 lose the unit or the size of a number

Attempts: F06, F07, F08, F09, F10. An adjective or a second space between number and unit, a magnitude word (`50 thousand`), a suffix (`50K`), or a number in words. The claim then carries another value than the quote and still needs no vote. Smallest reproduction: F08.

- F06: claim `Widget Store deletes an empty crate after 7 full hours.`, display `7 full hours`, quote `Widget Store deletes an empty crate after 7 days.`, kind behavior, hard false; facts add, facts finalize -> verified with no vote
- F07: as F06 with claim and display `7  hours` (two spaces)
- F08: claim `A crate holds 50 thousand widgets.`, display `50 thousand widgets`, quote `A crate can hold up to 50 widgets.`, hard false; add, finalize -> verified
- F09: as F08 with `50K widgets`
- F10: claim `A shelf holds nine hundred widgets.`, display `nine hundred widgets`, quote `Each shelf can hold up to 500 widgets.`, hard false; add, finalize -> verified

### H3 (high): A quote may start and end in the middle of a sentence

Attempts: F03, F17, L30. Cutting `You cannot` off the front of a real sentence gives a `verbatim` quote with the opposite meaning, for M3/M4 and for the L306 quote block. Smallest reproduction: L30 (one line of Markdown) or F03.

- F03: facts add a fact with claim `You can move a shelf to another Region.`, display `move a shelf to another Region`, quote `move a shelf to another Region. To use another Region, copy the shelf.`, kind behavior, hard false; then facts finalize ID -> verified
- F17: quote `copy the shelf. Crates A crate is a container for widgets` -> accepted
- L30: replace the FAQ quote by `> "move a shelf to another Region."` -> no L306

### H4 (high): Text inside `<...>` is invisible to the quote match

Attempts: F18. Up to 400 characters can be added to a stored quote. The fact sheet and the verifier packet then show words that AWS never wrote. Reproduction: F18.

- F18: quote `You <can now move a shelf, where before you> cannot move a shelf to another Region. To use another Region, copy the shelf.` -> M3 passes

### H5 (critical): Nothing proves that a snapshot came from the fetch tool

Attempts: F19, F22. A .txt written or edited by hand under `_build/corpus/snap/` is accepted as evidence by `facts add`; an honest verifier then sees a matching quote. Smallest reproduction: F22.

- F19: write _build/corpus/snap/<any/id>.txt and .meta.json {source_id, url on an allowed host}; facts add a fact that quotes it -> mech-pass
- F22: append a sentence to a snapshot .txt; facts add a fact that quotes it -> mech-pass; one support vote -> verified

### H6 (medium): Page furniture and flattened table text pass M8 and M4

Attempts: F16, F20. Navigation words outside the ten BOILERPLATE phrases are a valid quote (F20). Table text written without pipes needs no `table_header` and can pair a number with the wrong row (F16; this one still waits for an entail vote).

- F16: quote `Resource Default Adjustable Shelves per Region 20 Yes Widgets per shelf 500 No`, claim `An account starts with 500 shelves in each Region.`, display `500 shelves`, kind quota -> mech-pass
- F20: quote `AWS Documentation Amazon Widget Store User Guide Feedback Preferences Contact Us English Create an AWS Account` -> accepted

### H7 (critical): A voter is a free-text label

Attempts: F13, F14, F15. The author votes on the own fact under a second label, or under the same label in another case. A later `support` under a disputing verifier's label turns a disputed fact into a verified one. Smallest reproduction: F14.

- F13: facts add --by miner-a; facts vote --by miner-b with verdict support; facts finalize -> verified
- F14: facts add --by miner-a; facts vote --by Miner-A; facts finalize -> verified
- F15: vote not-supported --by verifier-b; finalize (disputed); vote support --by verifier-b; finalize -> verified

### H8 (high): Votes are bound to the rev number, not to the content; the vote log is a plain file

Attempts: F24, F25. A hand edit of `claim` that keeps `rev` keeps all votes (F25). A hand edit of the status plus one appended vote line passes F04 (F24). Smallest reproduction: F25.

- F24: set status verified in data/facts/<s>.jsonl and append one vote line to _build/facts/votes/<s>.jsonl
- F25: edit `claim` of a verified fact in data/facts/<s>.jsonl without touching `rev`; facts verify -> ok; the fact sheet prints the new claim

### H9 (critical): `facts amend` can remove the need for votes, and then rewrites the prose itself

Attempts: A01, A04. A patch with `hard: false` (and a kind that M11 does not force) empties the votes and makes them unnecessary in one step. With a changed display the tool replaces the link texts in the chapter. `facts amend` takes no `--by`. Smallest reproduction: A01.

- A01: patch {"claim": "A shelf is a Regional resource that copies its widgets to each other AWS Region.", "hard": false}; facts amend widget-shelf-scope --file PATCH --reason wording; facts finalize widget-shelf-scope -> verified
- A04: patch {claim: `A crate holds 50 thousand widgets.`, kind: behavior, hard: false, values: [{key: max, display: `50 thousand widgets`}]}; facts amend widget-crate-capacity --file PATCH --reason unit; facts finalize widget-crate-capacity

### H10 (high): L304 misses a number with a unit

Attempts: L02, L03, L04, L06, L11, L12, L17, L31. Non-breaking space, `&nbsp;`, full-width digits, a number word, an adjective between number and noun, a unit outside the list, `9000+`, or number and unit in two sentences. Smallest reproduction: L04 (`A crate holds 9000 small widgets.`).

- L02: `A crate holds 9000<NBSP>widgets.` in a strict section -> no L304
- L03: `A crate holds nine thousand widgets.` -> no L304
- L04: `A crate holds 9000 small widgets.` -> no L304
- L06: `A crate holds 9000&nbsp;widgets.` -> no L304
- L11: `A crate takes 9000 TPS.` -> no L304
- L12: `9000+ widgets` -> no L304
- L17: `The limit of a crate is 9000. The unit is widgets.` -> no L304
- L31: `A crate holds <full-width 9000> widgets.` -> no L304

### H11 (high): L304 misses an absolute claim

Attempts: L07, L08, L09, L10. Words outside the nine-word list (`no one`, `nobody`, `invariably`, `every`, `all`), `can not` in two words, an entity or a zero-width space inside the word. Smallest reproduction: L10 (`You can not copy a crate.`).

- L07: `A shelf is alw&#97;ys private.` -> no L304
- L08: `on<ZWSP>ly`, `ne<ZWSP>ver` -> no L304
- L09: `A crate is invariably public. No one except the owner is able to delete it.` -> no L304
- L10: `You can not copy a crate.` -> no L304

### H12 (high): Places that L304 does not read but the reader does

Attempts: L13, L14, L15, L25, L26, L29, L32. Inline code, a sentence that ends with `?`, a `<summary>` line, any section or callout with grounding `example`, a sentence with a `no-fact` marker (warning W308 only), and a Markdown file that the template does not list. Smallest reproduction: L14.

- L13: ``A crate holds `up to 9000 widgets`.`` -> no L304
- L14: `Did you know that a crate always holds up to 9000 widgets?` -> no L304
- L15: any hard sentence + `<!-- no-fact: requirement -->` -> W308 only
- L25: add `A crate always holds up to 9000 widgets.` to a bold field of the Decision record -> clean
- L26: `> **Startup example:** Callvale learned that a crate always holds up to 9000 widgets.` -> no L304
- L29: `<summary>Go deeper: a crate always holds 9000 widgets</summary>` -> clean
- L32: create 99-sample/6-extra.md with any text -> lint 99 unchanged

### H13 (high): A fact link proves only that the display string is somewhere in the link text

Attempts: L19, L20, L21, L22, L23. `[not 500 widgets but 9000 widgets](...)`, `[not private](...)`, `[up to 2 500 widgets](...)`, a link on the wrong subject, and any other hard claim in a sentence that has one link. Smallest reproduction: L21.

- L19: `[up to 2 500 widgets](../facts/widget.md#widget-shelf-max-widgets)` -> no L303
- L20: `A shelf holds [not 500 widgets but 9000 widgets](../facts/widget.md#widget-shelf-max-widgets).` -> clean
- L21: `[not private](../facts/widget.md#widget-shelf-default-private)` -> clean
- L22: `A crate always holds 9000 widgets, more than the [500 widgets](LINK) of a shelf.` -> clean
- L23: `A crate holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets).` -> clean

### H14 (medium): The chapter form of `sync --check` (the `sync` gate) does not look at the fact sheets

Attempts: S02, S03, S04. `facts/<service>.md` can be edited or deleted, and a hand-made sheet for a service without facts can be added. Smallest reproduction: S02.

- S02: sync --all; edit facts/widget.md by hand; sync 99 --check -> ok; gate 99 --gate sync -> ok
- S03: delete facts/widget.md; sync 99 --check -> ok; lint 99 has no finding for the fact links
- S04: write facts/ghost.md by hand; sync --all --check -> ok

## Notes for the owners

- `common.normalize_text` is the source of H4 (it drops `<...>`) and of the flattened table text in H6. A change there is a change in `common.py`.
- H1, H2 and H9 share one cause: the tool lets the author decide `hard`, and checks that choice with the same narrow matcher that H10 and H11 defeat.
- H7 and H8 cannot be closed by the tool alone while every agent can write every file. They can be narrowed: compare labels case-insensitively, refuse a second vote of a voter on the same rev and lens, store a content hash (claim, values, evidence) in each vote and compare it in `_decide`.
- The fixture facts have no `author` field, so the author test never applies to them.
- During setup I changed two strings of my own driver script with a `python3 -c` one-liner instead of the Edit tool. Nothing else was edited that way.
