# SAA-C03 Handbook build

This repository holds a study book for the AWS Certified Solutions Architect - Associate exam (SAA-C03) and the tools and state that build it. The book lives in `aws-saa-book/`. The build is resumable: the ledger records every stage of every chapter.

## At the start of every session

1. Read `aws-saa-book/_build/ledger/HANDOFF.md`, then the last three sections of `aws-saa-book/_build/ledger/RUNBOOK.md`, then `aws-saa-book/_build/spec/RULINGS.md`.
2. Run `python3 aws-saa-book/tools/saa.py status`, or `python3 aws-saa-book/_build/ledger/workflows/status_report.py` for the full report.
3. Build the args of a run with `python3 aws-saa-book/_build/ledger/workflows/make_args.py <chapter ids>` (add `--facts` for a facts run) and launch `aws-saa-book/_build/ledger/workflows/saa-chapter-factory.v4-light.js` with the Workflow tool, passing the printed JSON object as `args`.

## Rules that do not change

- Models: the orchestrator thread runs on Opus 5.5. Every subagent runs on Opus 5.5 or Sonnet 5.5, set explicitly on every agent call. Never Fable. The table of which agent gets which model is in HANDOFF.md.
- Light process: one writing run and one facts run at a time, two chapters each.
- Grounding: every number, limit, default and can-or-cannot claim in the book is a verified fact with a verbatim quote from a saved AWS page. Every shipped question passed the three-solver blind panel.
- The corpus in `aws-saa-book/_build/corpus/` is evidence. Fetch only pages that are not in it yet. Never refresh a cached page: a refresh changes the snapshot hashes that verified facts check.
- One machine and one thread run the build at a time. Pull before you start. Commit after each finished chapter and after each publish; push when the user has asked for pushes.
- Tell the reader once per finished chapter and after each publish. Keep the runbook up to date. Do not stop to ask for approval.

## Machine notes

- macOS or Linux only: the tools use `fcntl`. On Windows, work inside WSL.
- Python 3.11 or newer, Node 18 or newer, and Google Chrome for diagram previews. If Chrome is not in the usual place, set `SAA_CHROME` to its executable.
- After any change to the tools or SPEC.json, `python3 aws-saa-book/tools/tests/run.py` must print OK.

## The reader

Write for the reader described in `aws-saa-book/_build/style/READER.md`: plain English, short sentences, depth in short layered pieces, English only. The reader skims, so headings, tables and captions must carry a correct gist on their own.
