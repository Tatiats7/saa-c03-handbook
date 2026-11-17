# How to resume the build

The book is built by Claude Code in the folder `2026-plans`. All finished work is saved in `aws-saa-book/`. If the build stops (usage limit, closed laptop, crash), nothing finished is lost.

## Case 1: the same Claude Code session is still open

Wait until the usage limit resets, then type:

```
continue the book
```

## Case 2: the session is gone (new window, restart, crash)

Open Claude Code in the folder `2026-plans` and paste this:

```
ultracode. Continue building the SAA-C03 Handbook in aws-saa-book/.
First read aws-saa-book/_build/ledger/RUNBOOK.md, then aws-saa-book/_build/spec/RULINGS.md,
then the approved plan at ~/.claude/plans/pasted-content-id-f907-i-need-curious-brook.md.
Resume from the state in the runbook. Do not redo finished work.
Do not pause to ask me for approval. Keep the runbook up to date.
```

The word `ultracode` at the start lets the new session run many agents at once, as this build needs.

## Before you walk away

- Mac plugged in, lid open.
- Leave the Claude Code window open.

## To check progress yourself

- Chapters appear as folders in `aws-saa-book/` (for example `03-iam/`).
- The current state is at the end of `aws-saa-book/_build/ledger/RUNBOOK.md`.
