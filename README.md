# SAA-C03 Handbook

A study book for the AWS Certified Solutions Architect - Associate exam, written chapter by chapter by Claude agents. Every number and every can-or-cannot claim in it is checked against a saved AWS page. This repository holds the book, the tools that build it and the full build state, so the work can continue on any laptop.

## Where things stand on 2026-11-16

| Measure | Value |
|---|---|
| Chapters finished | 26 of 53 |
| All work, weighted by pipeline stage | 56% |
| Fact bases verified | 35 of 44 |
| Verified facts | 18,290 |
| Words written | 165,594 |

[STATUS.md](STATUS.md) has the table of all 53 chapters and the list of downloaded AWS pages. Regenerate it at any time:

```
python3 aws-saa-book/_build/ledger/workflows/status_report.py > STATUS.md
```

The published handbook is a claude.ai page tied to your Claude account, so it opens on any laptop where you are signed in: https://claude.ai/artifact/BkvPfVTzRqizdPAd2zV1Ka

## What is in this repository

| Path | What it holds |
|---|---|
| `aws-saa-book/00-*` to `52-*` | the chapters |
| `aws-saa-book/data/` | facts, questions, cards, tasks, spoken answers, glossary |
| `aws-saa-book/facts/` | the fact sheets the chapters link to |
| `aws-saa-book/_build/corpus/` | the 6,393 AWS pages already downloaded, about 1.4 GB |
| `aws-saa-book/_build/ledger/` | the stage record of every chapter, the runbook, the handoff guide and the workflow scripts |
| `aws-saa-book/_build/spec/` | the plan, the rulings and your diagnostic study plan |
| `aws-saa-book/_build/style/` | the writing contract and the tool manuals |
| `aws-saa-book/tools/` | the `saa.py` tool and its tests |
| `CLAUDE.md` | instructions that Claude Code reads by itself in this folder |

Left out on purpose: build outputs, which one command rebuilds; scratch files; Claude's chat history from the old laptop, because the runbook and the handoff guide hold everything that matters from it; and the other files in `2026-plans`.

## Step 1, on the old laptop: put it on GitHub

Keep the repository private. It holds copies of AWS documentation and your reader profile.

```
cd ~/Desktop/tatia/saa-c03-handbook
gh auth login
gh repo create saa-c03-handbook --private --source . --remote origin --push
```

If you prefer the website, create an empty private repository named `saa-c03-handbook` on github.com, then run:

```
cd ~/Desktop/tatia/saa-c03-handbook
git remote add origin https://github.com/Tatiats7/saa-c03-handbook.git
git push -u origin main
```

The first push is large and can take several minutes. If it fails with "RPC failed" or "HTTP 400", run `git config http.postBuffer 524288000` and push again.

## Step 2, on the new laptop: set up

You need:

- macOS or Linux. On Windows, install WSL with Ubuntu and do everything inside it.
- Git, Python 3.11 or newer, and Node 18 or newer.
- Google Chrome, for diagram previews.
- VS Code with the Claude Code extension, signed in to the same Claude account.

Then clone and check:

```
git clone https://github.com/Tatiats7/saa-c03-handbook.git
cd saa-c03-handbook
python3 aws-saa-book/tools/tests/run.py
python3 aws-saa-book/tools/saa.py status
```

The test run must end with OK, and the status must list 53 chapters.

## Step 3: continue the build

1. Open the `saa-c03-handbook` folder in VS Code and start a new Claude conversation.
2. Type `/model opus`.
3. Paste the prompt below and send it.
4. When a usage limit stops the work, type `continue the book` after the limit resets.

```
Continue building the SAA-C03 Handbook in this repository. Read aws-saa-book/_build/ledger/HANDOFF.md first, then the last three sections of aws-saa-book/_build/ledger/RUNBOOK.md, then aws-saa-book/_build/spec/RULINGS.md. Resume from the ledger with make_args.py as HANDOFF.md says. Run the chapter factory as workflows; I opt in to multi-agent workflows. You run on Opus 5.5. Every subagent runs on Opus 5.5 or Sonnet 5.5 as HANDOFF.md says, never Fable. Keep the light process: one writing run and one facts run at a time, two chapters each. Do not pause to ask me for approval. Tell me once per finished chapter and after each publish. Keep the runbook up to date. Commit after each finished chapter and after each publish, and push to origin.
```

## Rules for two laptops

- Only one laptop runs the build at a time. Two would put two agents on the same chapter.
- Before you start on a laptop, run `git pull`. When you stop, check that the last finished chapter is committed and pushed.
- The old copy in `2026-plans/aws-saa-book` is a frozen backup. Do not continue there.

## If something goes wrong

| Problem | Fix |
|---|---|
| Chrome is not found | Run `export SAA_CHROME="/path/to/chrome"` before starting Claude. |
| Thousands of facts fail check M2 after cloning | Line endings were converted. Run `git config --global core.autocrlf false`, delete the folder and clone again. |
| A tool fails with "No module named fcntl" | You are on Windows outside WSL. |
| The new thread says it cannot run workflows | Send the prompt again with the word `ultracode` in front. |
| A push is rejected because the remote has newer commits | Run `git pull`, then push again. |
