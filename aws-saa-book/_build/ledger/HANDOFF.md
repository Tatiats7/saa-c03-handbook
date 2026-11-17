# Handing the SAA-C03 Handbook build to a new thread or a new laptop

Updated 2026-11-16, when the build moved from `2026-plans/aws-saa-book` into its own Git repository, `saa-c03-handbook`. Read this first in any thread that takes over the build.

## Part 1. For Tatia

- Setting up a new laptop: follow `README.md` at the repository root (GitHub, requirements, clone, check).
- Starting a thread: `git pull`, open the repository folder in VS Code, start a new Claude conversation, type `/model opus`, paste the prompt from `README.md`. Never pick Fable for this work.
- Only one thread on one laptop runs the build at a time. Close the old thread first.
- After a usage-limit stop, type `continue the book` in the same thread once the limit resets.
- Optional: ask the thread to "set up the keeper" (see below). It checks every two hours and restarts the work after a limit resets, while the thread stays open, for up to 7 days. It has not been tried yet.

## Part 2. For the orchestrator thread

### Start-up checklist

1. `git pull` if the repository has a remote. Read this file, the last three sections of `RUNBOOK.md` and `RULINGS.md` (at least the sections added 2026-10-13 and 2026-10-22).
2. `python3 aws-saa-book/tools/saa.py status` lists every chapter with its state and next stage. `python3 aws-saa-book/_build/ledger/workflows/status_report.py` writes the full report.
3. A stage left `running` or `fail` by a dead thread is normal. The factory begins it again. After three failed attempts run `python3 aws-saa-book/tools/saa.py stage reset <ch> <stage> --reason "..." --by orchestrator`.
4. Launch one writing run with two chapters and one facts run with two chapters. Add a runbook line with the run ids.

### Launching the factory

- Build the args from the ledger:

  ```
  python3 aws-saa-book/_build/ledger/workflows/make_args.py 25 29            # writing run
  python3 aws-saa-book/_build/ledger/workflows/make_args.py 38 39 --facts    # facts run
  ```

  It prints a JSON object and saves it to `aws-saa-book/_build/tmp/run-<ids>.json`. Each chapter carries `passed` (the stages the ledger has passed, so the factory runs exactly the rest), `next_stage`, and an orchestrator note with the standard rules plus a resume line for unfinished stages.
- Resume aids: `--skip-writers ID=fast,deep,questions` when those files are already complete (the helper prints a hint when it sees them), `--skip-lenses ID=faq,...` for mining lenses already finished, `--note ID="text"` for anything else the chapter's agents must know.
- Call the Workflow tool with `scriptPath` = the absolute path of `aws-saa-book/_build/ledger/workflows/saa-chapter-factory.v4-light.js` on this laptop (`pwd` plus that relative path) and `args` = the printed JSON object, not a string.
- Mining lens keys: medium `numbers+changes`, `behavior+decisions`, `faq`; deep `numbers`, `behavior`, `decisions+changes`, `faq`; XL deep `numbers`, `behavior`, `decisions`, `faq`, `changes`; light and other `numbers+behavior+changes`, `decisions+faq`. A finished lens left `_build/work/<dir>/mine-<lens>.json`.
- Each run notifies when it completes and returns `ready` and `blocked` lists with gate errors. Do not poll.

### Models (never Fable)

| Model | Agents |
|---|---|
| Opus 5.5 | plan, register, fact adjudication, spot check, entail votes, brief, fast, deep, questions, tasks, cards and spoken answers, edit, closed-book solver, question adjudication, top-up, both reviewers, fix, ad-hoc repairs that change facts or chapter text |
| Sonnet 5.5 | miners, currency and derive votes, open-book and ambiguity solvers, terms, closer and repack, diagrams, fact requests, close-facts, finalize, ad-hoc mechanical work |

Every ad-hoc Agent call must pass `model: "opus"` or `model: "sonnet"` explicitly.

### Queue as of 2026-11-16

- Fact maintenance, first, in parallel with the first writing run: 55 facts in six finished chapters fail the facts gate (02: 20, 04: 15, 21: 12, 22: 4, 18: 3, 14: 1). Most were mined by later chapters into an earlier chapter's namespace after that chapter's fact check had passed, so nobody voted on them. About eight quote the storage decision guide, which was re-fetched on 2026-10-14. Run `saa-facts-repair.js` with the args in `aws-saa-book/_build/ledger/workflows/pending-fact-maintenance.json` (pass the JSON object). Then re-run the facts gate on those chapters: `python3 aws-saa-book/tools/saa.py gate <ch> --gate facts-final`. If an amended display touched chapter text, re-gate the stale stages and finalize, as the playbook says.
- Writing, first: 11 vpc-connectivity resumes at edit (its review files were written before edit and get overwritten), then reviews, fix, finalize. 24 backup resumes at prose: `1-fast.md` and `2-deep.md` and 12 questions exist, tasks and diagrams were begun and died. Check `lint 24 --draft` and `q lint 24`, then use `make_args.py 11 24 --skip-writers 24=fast,deep,questions`.
- Writing, next pairs: 25 hybrid storage + 29 ElastiCache; 32 Step Functions + 33 API Gateway; 34 streaming + 35 analytics; 37 monitoring with the next chapter whose facts close.
- Before writing 35: its spot check found 5 voter misses in 30 facts (all repaired). Consider a second 30-fact spot check with another seed, aimed at its change and pricing facts.
- Facts, in pairs: 38 deploy and operate + 39 migration; 40 HA and DR + 41 cost (deep pattern chapters); 42 security patterns + 43 decoupling and scaling; 20 more compute + 30 more databases; 36 AI, ML and media (light template).
- Then the synthesis wave W12 (44 to 49 and 52) and the mock exams W13 (50, 51). The factory has not run these templates yet. Read their templates in `SPEC.json` and `CONVENTIONS-2.md`, check what the factory prompts assume, and run one chapter as a pilot first. Each mock needs 65 questions: split the question writer into several parts and look at `saa.py mocks`.
- Then the W14 whole-book review: the backlog items are in the runbook (audit tool fixes, corpus snapshot versioning, web items, the IAM should-fix list).
- Publishing: chapter 12 finished after version 11. Publish with the next finished pair.

### Git

- Commit after each finished chapter and after each publish, with a short message such as `Chapter 25 hybrid-storage ready`. Push when the reader asked for pushes in the thread's prompt.
- `.gitignore` keeps build outputs, scratch files and lock files out. `.gitattributes` turns off line-ending conversion: never change that, because facts check SHA-256 hashes of the saved pages.
- Never rewrite history and never force-push.

### Publishing

1. `python3 aws-saa-book/tools/saa.py build web --only-ready` must report 0 errors.
2. Files map: every path in `aws-saa-book/_build/site/publish-plan.json` batches except `index.html`, each mapped to `aws-saa-book/_build/site/<path>`.
3. The Artifact is https://claude.ai/artifact/BkvPfVTzRqizdPAd2zV1Ka. A new thread must first list its files with the Artifact tool (`action: list`, `scope: files`, `url`). Check that the live version id matches the last one in the runbook (version 11 is `1792727364-0a14`). If it does not match, someone else published: read before overwriting. Then publish with `url`, `file_path: aws-saa-book/_build/site/index.html` and `files`. Leave out `capabilities` so they carry forward.
4. One publish call takes at most 255 files. Version 11 has 172. When the map passes about 250 files, publish in two calls to the same url; the second call adds to the first. A version holds up to 511 files.
5. A file the build no longer writes gets `null` in the map.
6. After publishing, add a runbook line with the version number and id.

### Blocker playbook

| Gate error | Fix |
|---|---|
| L307 needs-term marker at fix or finalize | Add the terms to `data/terms.json` with a Sonnet agent (copy the shape of the last entries; meanings carry no numbers), remove the markers, run `cards build`, re-gate fix, then finalize. The terms step after the brief prevents most cases. |
| T106 tag error on a CLI step that takes no tag option | Add the operation to `SPEC.json` `tasks.untaggable_operations`, run the test suite, then `stage begin <ch> tasks --run orchestrator` and `stage end <ch> tasks --counts tasks=<n>`. |
| F02 fact disputed or pending, B09 open fact request | Run `saa-facts-repair.js` with `{"chapters": [...], "facts": [{"id", "chapter", "issue"}]}`. For a fact the fix agent already amended, write "needs votes only" in `issue`. Then `facts request --close <fr> --fact <id>` and re-run finalize. |
| `q adjudicate --select` cannot meet the counts, usually twin pairs | Clear the orphan's `twin_of` in the questions file (metadata only, ruling 2026-10-13), then run `saa-twins-topup.js`. |
| A fact display was re-worded and reset questions, cards or spoken items | Set unchanged cards and spoken items ready (`cards set-status`, `speak set-status`), re-gate cards, speak and questions. Build packs with `q pack --round 0 --ids <ids>`, run `saa-requiz.js`, then re-gate edit, review and fix, then finalize. |
| M2 or M3: snapshot changed or quote missing | A page was re-fetched. Re-quote the facts from the current snapshot with `saa-facts-repair.js`. |
| Prose stage failed 3 attempts at the closer: L106 device count, L201 file over its word limit, L402 missing Try it callout | The Sonnet closer cannot do writing fixes. Fix the file yourself or with an Opus agent: device wording as CONVENTIONS shows it (a Spot the bug prompt ends "What is wrong?"), one `Try it` callout per Try task in the section the task names, trims that keep every fact link and avoid unlinked absolute words (L304). Then `stage reset <ch> prose`, `stage begin` and `stage end` prose, and pass questions the same way. |
| Stale edit, review or fix | `stage begin <ch> <stage> --run orchestrator`, then `stage end <ch> <stage>`. A callout that a display rewrite made too long (L202) needs a one-word trim. |
| SPOT CHECK FLAG in a facts run log | The Opus checker found 3 or more voter misses in 30 facts and repaired them. Two flagged chapters in a row is a reason to look at the voting again. |
| WB01 web budget | Budgets live in `tools/saalib/site.py` BUDGETS. Raise one only with a reason in the runbook. |
| "You've hit your session limit" or "weekly limit" | Write a STOP section in the runbook with each chapter's state. After the reset, relaunch with `make_args.py`. |

After any change to the tools or SPEC, `python3 aws-saa-book/tools/tests/run.py` must print OK.

### The keeper (only if Tatia asks for it)

Create a recurring CronCreate job, for example cron `17 */2 * * *`, with the prompt: "keeper: if a workflow you launched is still running, or the build is finished, reply in one line and do nothing; otherwise continue the book from the ledger as HANDOFF.md says." It lives only in this thread, fires only while the thread is open and idle, and expires after 7 days. Only one thread may hold a keeper.

### Where things are

- Ledger, runbook, this file and the workflow scripts: `aws-saa-book/_build/ledger/`. `workflows/` holds the factory, `make_args.py`, `status_report.py`, `saa-facts-repair.js`, `saa-twins-topup.js` and `saa-requiz.js`.
- Plan and rulings: `aws-saa-book/_build/spec/` (`PIPELINE.md` is the approved plan; `inputs/` holds the reader's diagnostic study plan). Contract: `aws-saa-book/_build/style/`.
- Reports: `aws-saa-book/_build/reports/`.
