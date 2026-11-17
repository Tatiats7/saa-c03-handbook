# TOOLS: the command-line and data contract of `saa.py` (version 1.0)

This is the contract for the modules `ledger`, `registry`, `facts`, `lint`, `qbank` and `lab`. `RULINGS.md` overrides it. Content rules are in `CONVENTIONS.md` and `SPEC.json`; this contract says which tool rule enforces which `SPEC.json` key.

| You implement | Read |
|---|---|
| any module | sections 0, 1, 2 here |
| `saalib/ledger.py` | section 3 |
| `saalib/registry.py` | section 4 |
| `saalib/facts.py` | section 5; the mechanical checks are `TOOLS-rules.md` R8 |
| `saalib/lint.py` | section 6.1 here; section 6.2 (`sync`) in `TOOLS-items.md` |
| `saalib/qbank.py` | section 7 in `TOOLS-items.md` |
| `saalib/lab.py` | section 8 in `TOOLS-items.md`; the task rules are `TOOLS-rules.md` R9 |

`TOOLS-items.md` is part 2 of this file and `TOOLS-rules.md` is part 3, both with the same authority. Part 3 (contract fix 1) holds the gate table, the shared `lint` functions, the exact matching rules, the count keys, the new rule codes and the item status commands; every implementer reads it. `corpus`, `feeds` and `diagram` have their own documents (`TOOLS-corpus.md`, `TOOLS-feeds.md`, `TOOLS-diagram.md`); this contract only calls their Python API.

Paths are relative to `aws-saa-book/`. `CH` is a chapter id (`10`), a slug (`vpc`) or `10-vpc`; resolve it with `common.chapter()`. `<dir>` means `<NN>-<slug>`.

## 0. Rules for every subcommand

1. **Run form:** `python3 aws-saa-book/tools/saa.py <subcommand> ...` from the repo root. Every parser calls `common.add_common_args` (`--out`, `--max-lines`, `--json`) and prints through `common.emit`.
2. **Output.** With `--json`, print exactly the JSON object shown in this contract. Without it, print a one-line summary first, then at most 40 lines (errors first). Never print a whole file.
3. **Exit codes:** `common.EXIT_*`. 0 pass; 1 blocking failure; 2 warnings only; 3 precondition missing or stale; 4 policy refusal; 5 transient.
4. **Writes.** Every read-modify-write of a shared file runs inside `common.file_lock(<that file>)` and writes with `common.write_json` or `common.write_jsonl`. When two locks are needed, take them in path order.
5. **Input files** (`--file`) must be inside the book folder (`common.inside_book`), else exit 4. They hold one JSON object or an array of objects.
6. **Schemas.** Validate with `saalib.schemas.validate(obj, "<name>")` (already written; it supports the keyword subset in `SPEC.json` `data_files.schema_keywords_used`). A schema error is a blocking finding: `X01` for a file wrapper, a ledger file or a gate record; the item's schema rule (`Q101`, `C101`, `P101`, `T101`) for an item.
7. **Finding.** Every check reports findings of one shape: `{"code": "L303", "file": "10-vpc/2-deep.md", "line": 88, "item": null, "msg": "link text holds no value of vpc-natgw-bandwidth"}`. Text form: `file:line: CODE message` (or `item: CODE message`).
8. **Gate function.** A module exposes `gate_<name>(ch_id, quick=False, **options) -> dict` with the keys of `gate.schema.json` except `ts`, `run`, `tool_version`. `inputs` lists every book file the gate read (not corpus files), with its SHA-256. The table in `TOOLS-rules.md` R1 maps each gate name to its module, function and exact call.
9. **Who made a write:** writing commands take `--by LABEL` (default: environment variable `SAA_AGENT`, else `unknown`).
10. **Tests:** `tools/tests/test_<module>.py`, with a sandbox as in `tools/tests/fixtures/README.md`. A must-fail test is named `test_must_fail_<what>`; `selftest` counts them.
11. **"In the corpus"**: a URL is in the corpus when `corpus.load_meta(corpus.source_id_for(url))` is not None, or when any `corpus/snap/**/*.meta.json` has that `url`.
12. **SPEC values.** Read every limit from `common.STYLE_DIR / "SPEC.json"` at call time. A number in this contract (for example "24 words") only illustrates the key named beside it; the fixture book has its own, smaller values.
13. **The fixture is expected to pass** every rule unless a must-fail test changes it. If the unchanged fixture breaks a rule, name the rule and the fixture line in your result; do not weaken the rule or edit the fixture silently. Known exceptions of the unchanged fixture: the `diagrams` gate (D01, no spec), the `counts` gate (B09, open request `fr-0001`), `tasks lint --ship` (T113, invented commands), the `needs-fact` warning W307 and three W901 warnings (terms used before their bold definition).

## 1. Data locations

| Path | Content | Writer |
|---|---|---|
| `data/book.json` | registry (`book.schema.json`) | `registry build`, `registry set` |
| `data/facts/<service>.jsonl` | fact canon (`fact.schema.json`), sorted by id | `facts` |
| `data/<dir>/{questions,cards,speak,tasks}.json` | chapter items | `q add`, `cards add`, `speak add`, `tasks add`, `q adjudicate`, `facts amend` |
| `data/<dir>/mock.json` | mock manifest (`mock.schema.json`), chapters 50 and 51 | `mocks assemble` |
| `data/drills.json` | four domain drills (`drills.schema.json`) | `drills build` |
| `data/terms.json`, `data/exam-english.json` | vocabulary | the orchestrator |
| `data/plan.json` | study plans (`plan.schema.json`) | the writer of chapter 00 |
| `data/cards-terms.json`, `data/01-how-the-exam-asks/cards.json`, `data/49-speaking-pack/cards.json` | generated cards | `cards build` |
| `data/startup.json` | the startup's fact sheet as data (`STARTUP.md`) | the orchestrator |
| `<dir>/1-fast.md`, `2-deep.md`, ... | hand-written prose | writers |
| `<dir>/3-do.md`, `4-say.md`, `5-quiz.md`, `sources.md`; `facts/<service>.md`; `glossary.md` | generated reader files | `sync`, `facts render` |
| `_build/registry/exam-guide.json`, `services.json` | parsed exam guide | `registry build` |
| `_build/facts/votes/<service>.jsonl` | vote log, append-only (`vote.schema.json`) | `facts vote` |
| `_build/facts/requests.jsonl` | fact request queue (`fact-request.schema.json`) | `facts request` |
| `_build/facts/conflicts.jsonl`, `rejected.jsonl`, `batches/` | conflict queue, rejected inputs, verification batches | `facts` |
| `_build/work/<dir>/` | `brief.v0.json`, `brief.json`, `findings/<lens>.json` | chapter agents |
| `_build/qbank/rejected.jsonl` | rejected questions | `q adjudicate` |
| `_build/qbank/packs.jsonl` | hashes of what each solver was shown | `q pack` |
| `_build/ledger/chapters/<id>.json`, `gates/<id>.<gate>.json`, `events.jsonl` | ledger (`ledger-chapter.schema.json`, `gate.schema.json`) | `ledger` |
| `_build/reports/` | `lint/<id>.json`, `coverage.json`, `coverage.md`, `wave-<W>.json`, `audit/`, `cli/`, `emulate/`, `freshen-<date>.json`, `changelog.jsonl` | the command named |

`data/glossary.json` (named in RULINGS) is not used: `glossary.md` is generated from `data/terms.json` (the orchestrator is asked to correct the RULINGS line). The feed files `_build/corpus/changes/<service>.jsonl` and `cases/index.jsonl` are described by `change-item.schema.json` and `case-item.schema.json`.

## 2. Functions other modules call

| Module | Function | Returns |
|---|---|---|
| `facts` | `load(service=None)` | dict id to fact (all services when None) |
| | `displays(fact)` | list of `common.normalize_text(display)` |
| | `is_volatile(fact)` | True when `changed.date` is within `questions.volatile_window_months` before `book.snapshot_date`, or `volatility` is `frequently-changing`, or `kind` is `price` |
| | `mech_check(fact)` | findings (M codes) |
| | `gate_mech(ch)`, `gate_final(ch)`, `render_sheet(service)` | gate dicts (`gate_final` also runs F04 and, unless `quick`, the M checks); Markdown text |
| `registry` | `exam_guide()`, `services()`, `service_keys_in_scope()` | parsed JSON; set of keys |
| `lint` | `check_strict_text(text, where, stem=None)` | findings L301 to L305 and L801 for one JSON text field; numbers that stand in `stem` are scenario data and exempt |
| | `sections(ch)` | `{file: {section id: {"heading", "anchor", "role", "route", "minutes", "level", "parent", "line", "planned"}}}`; keys are anchor-form section ids (`headings.section_id`), H3 subsections included; sections that only `brief.json` names so far have `planned: true` |
| | `traps()` | dict trap id to chapter id, from the traps lists and `Exam trap` callouts of every hand file, plus the `traps` of every `brief.json` whose trap is not yet in a hand file; `trap-ref` comments are skipped |
| | `a_list_facts(ch)` | fact ids linked in column 1 of the `### A-list` table |
| | `template(ch)`, `word_count(text)`, `anchor(heading)`, `section_id(heading)` | the resolved template (`resolution.template`); the shared helpers that every module uses (import `lint` inside the function) |
| | `holds_display(text, display)`, `link_text_extra(text, displays)` | the number-boundary comparison of `fact_links.comparison`, and what a link text holds beside the displays (`TOOLS-rules.md` R1) |
| | `gate_lint(ch, quick=False, draft=False)`, `gate_sync(ch)` | gate dicts |
| `qbank` | `items(ch, kind)` | list (`kind`: `questions`, `cards`, `speak`) |
| | `gate_questions(ch)`, `gate_questions_verified(ch)`, `gate_cards(ch, ship=False)`, `gate_speak(ch, ship=False)` | gate dicts (the `counts` gate passes `ship=True`) |
| `lab` | `gate_tasks(ch, ship=False)` | gate dict (the `counts` gate passes `ship=True`) |
| `ledger` | `mark_stale(ch, reason, stages=None, item_stages=None)` | sets the named stages (default: `edit` and every later stage that passed, plus each stage in `item_stages`, a subset of `questions`, `cards`, `speak`, `tasks`, whose items the caller reset) and their passed dependents, direct or indirect, to `stale`; appends `reason` to the chapter's `stale` list; logs an event |
| `diagram` | `pipeline.check_id(id)`, `pipeline.spec_path(id)`, `pipeline.svg_path(id)`, `pipeline.caption(spec)` | see `TOOLS-diagram.md` |

## 3. Ledger (`saalib/ledger.py`): `stage`, `gate`, `status`, `report`, `selftest`

### 3.1 Stages

The per-chapter pipeline of PIPELINE section 10, adapted: no render stage (Markdown is the source), `tasks` replaces "lab", `speak` and `diagrams` are stages of their own.

| # | Stage | Prerequisites | Gates run by `stage end` | Not applicable when |
|---|---|---|---|---|
| 1 | `plan` | none | `plan` | |
| 2 | `mine` | plan | `facts-mech` | |
| 3 | `register` | mine | `facts-mech` | |
| 4 | `verify-facts` | register | `facts-final` | |
| 5 | `brief` | verify-facts | `brief` | |
| 6 | `prose` | brief | `lint` (draft mode) | |
| 7 | `questions` | brief | `questions` | template `counts.questions.shipped` is 0 |
| 8 | `tasks` | brief | `tasks` | every `counts.tasks.*.max` is 0 |
| 9 | `cards` | brief | `cards` | every card count is 0 |
| 10 | `speak` | brief | `speak` | `counts.speak.count` is 0 |
| 11 | `diagrams` | brief | `diagrams` | |
| 12 | `edit` | prose, questions, tasks, cards, speak, diagrams | `lint`, `sync` | |
| 13 | `review` | edit, verify-questions | `findings` | |
| 14 | `fix` | review | `findings-closed`, `lint`, `sync` | |
| 15 | `verify-questions` | questions | `questions-verified` | as `questions` |
| 16 | `finalize` | fix, verify-questions | `facts-final`, `lint`, `sync`, `questions-verified`, `cards`, `speak`, `tasks`, `diagrams`, `findings-closed`, `counts` | |

A not-applicable stage gets status `na` and counts as passed; its gate is skipped in `finalize`. The stage numbers are labels: `verify-questions` runs after `questions` and before `review`, so that the reviewers read a `5-quiz.md` with its questions. Stages 6 to 11 run in parallel: trap ids, section headings and diagram texts come from `brief.json`, and the item rules resolve them against the brief until the prose exists (`TOOLS-rules.md` R4).

Gates owned by `ledger`:

- `plan`: `_build/work/<dir>/brief.v0.json` exists (B01) with `{"chapter", "sources_fetched", "fetch_failures": [], "demand": [{"id", "bullet", "question", "status", "facts"}]}`; every bullet of the registry entry has a demand item (B02); every URL in the entry's `sources` lists `pages`, `faq`, `history`, `quotas`, `pricing` is in the corpus or in `fetch_failures` (B03).
- `brief`: `_build/work/<dir>/brief.json` exists (B01) with `{"chapter", "sections": [{"file", "section", "heading", "bullets": [], "facts": []}], "traps": [{"id", "belief", "truth", "facts": []}], "question_slots": [{"bullet", "concept", "difficulty", "type", "layer", "exam_english": []}], "terms": [], "tasks": [], "diagrams": [{"id", "kind", "claim", "alt", "say": []}]}`; `section` is the anchor-form section id and `heading` the exact heading text without the time box; every bullet maps to a section and, when the `questions` stage applies, to a question slot (B02); every fact id named is `verified` (B04); every entry of `terms` is a term of `data/terms.json` (B11); a hard fact of kind `behavior`, `capability`, `restriction` or `default` that the brief names has at least two displays (B12, warning).
- `findings`: `_build/work/<dir>/findings/<lens>.json` exists for the lenses `claims` (unsupported-claim hunter plus technical red team), `reader` and `exam` (`exam` only for deep, medium and pattern templates) (B05). The file is `{"lens", "chapter", "findings": [{"id", "file", "section", "quote", "type", "severity", "evidence", "status", "resolution"}]}`; `severity` is `blocking`, `should` or `note`; `status` is `open`, `fixed`, `removed` or `rejected`. A finding without `file`, `type` or `evidence` is B06.
- `findings-closed`: no finding has `severity: blocking` and `status: open` (B07).
- `diagrams`: for each diagram id embedded in the hand files: the spec exists (D01), the SVG exists (D02), `diagram.pipeline.check_id(id)` reports no error (D03), the SVG file equals the output of its spec (D04).
- `counts`: the modules' `--ship` count rules pass (Q201, C201, C204, P201, T201, T113; the calls are in `TOOLS-rules.md` R1); the tool could write front matter `status: ready` into every hand file (B08: a hand file without a `status` line); no open fact request for the chapter (B09); a stage other than `finalize` is still `stale` (B10).

**Front matter status.** `stage end` writes the `status` line of every hand file of the chapter, before the gates of that stage run: `draft` on `prose`, `reviewed` on `fix`, `ready` on `finalize`, and puts the previous values back when those gates do not pass. It is a one-line rewrite; a writer never changes `status`. The web manifest maps ledger status `ready` to `ready`, `drafted` and `reviewed` to `draft`, everything else to `planned`.

### 3.2 `stage begin CH STAGE [--run ID]`

`inputs_hash` = SHA-256 of `json.dumps({"stage": S, "style": <SPEC.json version>, "entry": <registry entry of CH>, "prereqs": {<prerequisite>: <its pass_seq>}}, sort_keys=True)`. Rules, first match wins:

1. Unknown chapter or stage: exit 3.
2. Stage not applicable: status `na`; print `SKIP` (reason `not-applicable`).
3. A prerequisite is not `pass` or `na`: print `BLOCKED` (reason `prereq:<stage>`). No attempt is used.
4. Status `pass` and the stored `inputs_hash` equals the current one: `SKIP` (reason `already-passed`).
5. Status is not `pass` and `attempts` is 3: `BLOCKED` (reason `attempts`); the chapter becomes `blocked`.
6. Otherwise `GO`: `attempts` + 1 (reset to 1 when the status was `pass` or `stale`), status `running`, store `inputs_hash`, `started`, `run`. Reason: `first`, `retry` (status was `fail` or `running`), `stale`, or `inputs-changed`.

Text: `GO 10 prose attempt=1 reason=first`. JSON: `{"decision": "GO", "chapter": "10", "stage": "prose", "attempt": 1, "reason": "first"}`. Exit 0 for GO and SKIP, 3 for BLOCKED. Agents act on the first word.

### 3.3 `stage end CH STAGE [--counts k=v ...] [--note TEXT] [--fail REASON]`

- The stage must be `running`, else exit 3.
- `--fail REASON` records a failure without running gates.
- Otherwise run every gate of the stage (all of them, not only up to the first failure), add `ts`, `run`, `tool_version`, and write `_build/ledger/gates/<id>.<gate>.json`.
- **Unavailable** (a gate's module or function is missing: `X03`, exit 3): no record is written, the stage stays `running`, the attempt is given back.
- **Pass** (no gate has errors): status `pass`, `attempts` 0, `pass_seq` + 1, `ended`, `counts` from `--counts`. Gate warnings replace that gate's entries in the chapter's `warnings` (each entry is the string `<gate>: <code> <msg>`). Every stage that depends on this one, directly or indirectly, and has status `pass` becomes `stale`. On `finalize`: `rev` + 1, `style_version` set, `stale` emptied.
- **Fail:** status `fail`, `reason` = the first error. When `attempts` is 3: chapter `blocked` = `{"stage", "reason", "since"}`.
- Chapter status, recomputed each time: `blocked` if `blocked` is set; else `ready` (finalize is `pass`), `reviewed` (fix), `drafted` (edit), `facts-verified` (verify-facts), else `planned`.
- Every begin, end, block, stale mark and status change appends `{"ts", "chapter", "stage", "event", "detail", "run"}` to `events.jsonl`.

JSON: `{"result": "PASS", "chapter": "10", "stage": "edit", "status": "drafted", "gates": [{"gate": "lint", "ok": true, "errors": 0, "warnings": 3, "record": "_build/ledger/gates/10.lint.json"}], "errors": []}` (`errors`: the first 20 findings). Exit 0 pass, 2 pass with warnings, 1 fail, 3 unavailable.

`stage reset CH STAGE|--all --reason TEXT` (orchestrator only): `attempts` 0, a `pass` becomes `stale`, `blocked` cleared. `stage show CH` prints the ledger file.

### 3.4 `gate`, `status`, `report`, `selftest`

- `gate CH [--gate NAME]`: runs the gates of `finalize` (or one), writes the records, changes no stage. Exit 0, 2 or 1.
- `gate --all [--quick]`: every chapter with status `drafted`, `reviewed` or `ready`. With `--quick` no gate function runs except `sync`; a stored record is `stale` when an input hash differs. JSON: `{"chapters": [{"id", "status", "result": "ok|stale|fail|no-record", "stale_gates": [], "failed_gates": [], "missing_gates": [], "unavailable_gates": []}]}`. Exit 1 if any `fail`, else 3 if any `stale` or `no-record`, else 0.
- `status [--wave W]`: one header line with totals per status, then one line per chapter: `10 vpc deep W2 drafted next=review facts=221/233 q=17/18 warn=2 stale=0`. JSON: `{"totals": {"planned": 50, "ready": 3}, "chapters": [{"id", "slug", "tier", "wave", "status", "next_stage", "blocked", "facts": {"verified", "total"}, "questions": {"ready", "target"}, "warnings", "stale"}]}`. A chapter without a ledger file is `planned`.
- `report wave W`: writes `_build/reports/wave-<W>.json` = `{"wave", "ready": [ids], "blocked": [{"id", "stage", "reason"}], "in_progress": [{"id", "status", "next_stage"}], "counts": {"facts", "questions", "cards", "speak", "tasks"}, "warnings": n, "open_requests": n, "report": path}` and prints at most 50 lines.
- `selftest`: runs `tests/test_*.py` in-process and prints `{"tests", "failures", "errors", "must_fail": {"<module>": n}}`. Exit 0 only when nothing fails and each of `ledger`, `registry`, `facts`, `lint`, `qbank`, `lab`, `corpus`, `feeds`, `diagram`, `contract` has at least one `test_must_fail_*`.

**Must-fail tests:** begin with an unmet prerequisite is BLOCKED; a fourth begin after three failed ends is BLOCKED and the chapter is `blocked`; end on a stage that is not running exits 3; end `verify-facts` fails when one fixture fact is set to `disputed`; `gate --all --quick` reports `stale` after one byte of an input changes; a begin after a prerequisite passed again answers GO, not SKIP. (The fixture ledger has `inputs_hash: null`, so a begin on its passed stages answers GO with `inputs-changed`.)

## 4. Registry (`saalib/registry.py`): `registry`, `coverage`

### 4.1 `registry build [--offline] [--accept-changes]`

1. **Book.** Read `_build/registry/book.seed.json`. If `data/book.json` does not exist, start from the seed. If it exists, overwrite `parts`, the `book` keys of the seed and the seed-owned keys of each chapter (`id`, `slug`, `title`, `part`, `tier`, `kind`, `xl`, `wave`, `services`) from the seed, and keep the tool-owned keys. Without a seed, `data/book.json` stays as it is; exit 3 only when both are missing. Give every chapter that lacks them `tasks: []`, `bullets: []` and `sources` with the eight empty lists of `book.schema.json`. Add `book.fact_namespaces` (default `{"exam": "01"}`), `book.style_version` (SPEC version) and `service_map` (default `{}`). Add `book.exam_guide` when it is missing: root `https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/`, guide id `aws-certification-solutions-architect-associate-03`.
2. **Pages.** Read `corpus/index/<guide_id>.json` (made by `saa.py guide <root>`; missing: exit 3). For each page, `corpus.fetch(url)` (cached) unless `--offline`; a missing snapshot is exit 3.
3. **Parse** each page `.txt` line by line. The first `# ` line decides the role.
   - `# Content Domain N: <title>`: a domain page. `## Task N.M: <title>` starts a task. A line that is exactly `Knowledge of:` or `Skills in:` starts a list; each following line that starts with `+ `, `- ` or `* ` is one bullet, until a blank line or a heading. Ids count in page order per list: `N.M.K1`, `N.M.K2`, `N.M.S1`. `text` is the line without the marker, with the surrounding white space stripped.
   - `# In-Scope AWS Services` and `# Out-of-Scope AWS Services`: each `## <category>` heading, then one entry per list line. `short_name` is the text in a final pair of parentheses. Entries with the same `official_name` are merged (`categories` joined, first `line` kept).
   - Any page: text that matches `Content Domain N: <title> \((\d+)% of scored content\)` gives a domain weight; another page with a weight has the role `overview`, else `other`.
   - Other lists (for example under `**Topics**`) and `<a name=...>` lines are skipped.
4. **Service keys.** For each in-scope entry: `keys` = `service_map[official_name]` when present; else the automatic match: the slug of the name without a leading `Amazon ` or `AWS ` and without the parentheses, or the same for `short_name`, when that slug is a `services` key of a chapter. `home_chapter` is the chapter of the first key; `level` is its tier.
5. **Checks.** Exactly 4 domains whose weights add up to 100, else exit 1. If an earlier `exam-guide.json` exists and the text of a bullet id changed or an id disappeared: exit 1 and write nothing, unless `--accept-changes`.
6. **Write** `exam-guide.json`, `services.json` and `data/book.json` (with `book.exam_guide_counts`, `book.built_at`).

JSON: `{"chapters": 53, "domains": 4, "tasks": 14, "bullets": 189, "in_scope": 119, "in_scope_unique": 118, "out_of_scope": 41, "unmapped": ["Amazon Kinesis"], "changed_bullets": []}` (the numbers are what the script counts; do not hard-code them). Exit 2 when `unmapped` is not empty.

### 4.2 `registry set CH [--file PATCH.json] [--bullets ID,ID] [--map "Official name=key1,key2"] [--cards KEY,KEY] [--replace KEY ...]`

Under the lock of `data/book.json`. The patch is `{"sources": {"faq": ["https://..."]}, "tasks": [], "bullets": [], "service_map": {}, "cards": [], "notes": ""}`.

- Lists are merged: existing items first, new items appended, duplicates dropped. `--replace sources.faq` (or `bullets`, `tasks`, `cards`) replaces that list.
- `tasks` always also receives the task of every bullet.
- `cards` (also `--cards`): the recognise-only keys (`TOOLS-rules.md` R5); replaces the list. `notes`: one string of at most 2,000 characters, a planning note for the chapter agents (the frequency note), marked as third-party research, never evidence; replaces the old note, an empty string removes it.
- A seed-owned key in the patch: exit 1. A URL whose host is not in `common.ALLOWED_HOSTS`: exit 4. A bullet id that is not in `exam-guide.json`, or a mapped key that no chapter has: exit 1.
- After a `--map` or `service_map` change, the `keys` of `services.json` are recomputed.

JSON: `{"chapter": "10", "added": {"sources.faq": 1, "bullets": 4}, "tasks": ["1.2", "2.2"]}`.

### 4.3 `registry check [--urls] [--fetch]`, `registry show CH`, `registry wave-args WAVE`

`registry check` findings (blocking unless marked):

- **R01** `book.json`, `exam-guide.json`, `services.json` are valid against their schemas.
- **R02** Chapter ids, slugs and service keys are unique across chapters; `part` exists; `tier` or `kind` resolves to a `SPEC.json` template; front and synthesis chapters have a `chapter_overrides` entry.
- **R03** Every bullet is in the `bullets` of at least one chapter; every task statement is in at least one chapter.
- **R04** Every in-scope entry has at least one key with a home chapter.
- **R05** No chapter service key is the automatic match of an out-of-scope entry.
- **R06** Every source URL is on an allowed host. With `--urls`: it is in the corpus (`--fetch` fetches missing ones first). A guide root in `sources.guides` has no snapshot: it is in the corpus when its `saa.py guide` index exists (`--fetch` builds it).
- **R07** Each `fact_namespaces` value is a chapter id; no namespace equals a service key.
- **R11** (warning) a chapter service key that maps to no in-scope entry.
- **R12** (warning) a deep or medium chapter with empty `sources.guides` and `sources.pages`.
- **R16** (warning, with `--urls`) a snapshot whose `final_url` has another path than its `url`.

JSON: `{"ok": false, "errors": [findings], "warnings": [findings], "counts": {"chapters", "bullets_unassigned", "services_unmapped"}}`. Text form: `data/book.json: R03 ... [1.1.K1]` (the item in brackets).

`registry show CH` prints the entry, its bullets with text, and its in-scope services.

`registry wave-args WAVE` prints one compact object for a workflow:

```json
{"wave": "W3", "chapters": [{"id": "04", "slug": "organizations", "dir": "04-organizations", "title": "Organizations, SCPs, Control Tower and RAM",
  "tier": "medium", "template": "medium", "xl": false, "services": ["organizations", "control-tower", "ram"], "tasks": ["1.1"], "bullets": 6,
  "mine_lenses": 3, "counts": {"questions_write": 12, "questions_ship": 10, "speak": 2, "cards": 12, "tasks_max": 3},
  "status": "planned", "next_stage": "plan"}],
 "skipped": [{"id": "09", "reason": "ready"}]}
```

`mine_lenses` is 5, 3 or 2 for the deep, medium and other templates. Chapters with status `ready` and an empty `stale` list go to `skipped`. An unknown wave: exit 3.

### 4.4 `coverage [--release]`

Reads the registry files, every `questions.json`, `cards.json` and `mock.json`, the facts and the ledger. Writes `_build/reports/coverage.json` (`{"bullets": [], "services": [], "tasks": [], "errors": [], "warnings": []}`) and `coverage.md`.

- Bullet row: `{"id", "chapters": [ids], "ready_chapters": n, "questions": n, "mock_questions": n}`. `questions` counts items with status `ready` and pool `chapter` or `drill` whose `bullets` hold the id.
- Service row: `{"id", "keys", "home_chapter", "level", "facts": n, "cards": n, "questions": n}`. Facts count when `verified`; an item counts when its `services` hold one of the keys.
- Task row: `{"id", "questions": n, "mock": {"50": n, "51": n}}`.

Blocking with `--release`: a bullet with `ready_chapters` 0 or `questions` 0 (V01); an in-scope service without a home chapter (V02); a deep-level service with 0 facts or 0 questions (V03); a task statement absent from a mock (V04). Warnings: a bullet with fewer than 2 questions (V11); a deep-level service with fewer than 5 questions (V12); a service with 0 cards (V13). Without `--release` everything is a warning. Exit 0, 2 or 1.

**Must-fail tests:** a bullet removed from the fixture chapter makes `registry check` fail with R03; a removed `service_map` entry makes R04; `registry set` with a seed-owned key exits 1, and with `https://example.com/` exits 4; `registry build --offline` with a changed bullet text exits 1 without `--accept-changes`; an overview page whose weights add up to 99 exits 1. `registry build --offline` on the fixture must produce exactly `fixtures/book/_build/registry/exam-guide.json` and `services.json` (ignoring `built_at`).

## 5. Facts (`saalib/facts.py`): `facts`, `audit`, `freshen`

### 5.1 Lifecycle

| Status | Meaning | Set by |
|---|---|---|
| `candidate` | stored; the mechanical checks have not passed for this `rev` | `verify`, `freshen` |
| `mech-pass` | the blocking mechanical checks pass | `add`, `adopt`, `amend`, `verify` |
| `verified` | every required vote is positive | `finalize` |
| `disputed` | a vote is not positive, or an open conflict | `finalize` |
| `rejected` | cannot be grounded; never rendered, never linked | `finalize`, `amend --reject`, `conflicts` |
| `superseded` | replaced by `superseded_by` | `amend --supersede` |

Only `verified` facts can be linked from the book. A fact id is never reused.

### 5.2 Mechanical checks (blocking, except M12)

The rules M1 to M13 are in `TOOLS-rules.md` R8 (moved there on 2026-10-09 with the gate-break changes; `facts.mech_check` implements them). M4 also accepts a short value line: with `heading` set, the quote is one whole line of 1 to 80 words within the 5 non-empty lines under that heading, its nearest heading above.

### 5.3 Subcommands

| Command | Behaviour |
|---|---|
| `facts add --file F [--by L]` | For each fact: set `rev` 1, `retrieved` (today), `author`, empty `votes`; fill the evidence fields; run the mechanical checks. Pass: store as `mech-pass`. Fail: do not store; append the input and its findings to `rejected.jsonl`. JSON `{"added": [ids], "rejected": [{"id", "errors": [findings]}], "conflicts": [ids]}`. Exit 1 if any was rejected. |
| `facts adopt --source SOURCE_ID (--table N --row M \| --sentence TEXT \| --heading H [--line N]) --file F` | Builds the evidence by script, then acts as `add`. With `--table` and `--row` (indexes as printed by `saa.py tables`): quote = the row text, `table_header` = the header text. With `--sentence`: the quote is the sentence that contains TEXT: the snapshot line that holds TEXT, cut at the `lint.sentence.split` boundaries (exit 1 when it is not found, or found twice). With `--heading`: quote = the N-th non-empty line under heading H (default 1), `heading` = its text. F holds the other fields, without `evidence`. |
| `facts verify [ID ... \| --service S \| --chapter CH \| --all]` | Re-runs M1 to M12, and F04 on a `verified` fact (R8). A `candidate` that passes becomes `mech-pass`. A `mech-pass`, `verified` or `disputed` fact that fails becomes `candidate` with `stale` set, and `ledger.mark_stale` is called for every chapter that uses it. `verify` writes the fact file only when a status changes; `match` and `mech` are filled by `add`, `adopt` and `amend`. JSON `{"checked": 7, "ok": 7, "failed": [{"id", "errors": [findings]}]}`. |
| `facts batch --chapter CH --lens entail\|currency\|derive [--size 30]` | Puts every `mech-pass` fact of the chapter that needs the lens (5.4) and has no vote for its current `rev` into batches `_build/facts/batches/<chapter id>-<lens>-<nnn>.json` = `{"id", "chapter", "lens", "facts": [ids], "created"}`. Prints the batch ids. |
| `facts packet BATCH --out FILE` | The verifier's only input (5.5). |
| `facts vote --file F --by L` | Appends votes (`vote.schema.json`; the tool sets `ts`, `voter` and `content`, the content hash of R8). Refused (exit 1, nothing appended): unknown fact; `rev` not current; a verdict not allowed for the lens; the author or an amender as voter; a second vote by one voter on one fact, rev and lens; a `quote` that `find_quote` does not find in `source_id`. `facts add`, `adopt`, `vote` and a rev-changing `amend` exit 3 when the label resolves to `unknown`. |
| `facts finalize [--chapter CH \| --service S \| ID ...]` | Computes status from votes (5.4); the M checks run again first (a failure: `candidate`, pending `mech`). JSON `{"verified": [], "disputed": [], "rejected": [], "pending": [{"id", "missing": ["currency"]}]}`. Exit 1 if any `disputed`, else 2 if any `pending`, else 0. |
| `facts card [ID ... \| --chapter CH \| --service S] [--all]` | Writer cards, verified facts only (`--all` adds the others, marked `NOT VERIFIED`): id, claim, scope line, one ready-made link per value `[<display>](../facts/<service>.md#<id>)`, spoken forms, the changed note. |
| `facts request ...` | The request queue (5.6). |
| `facts amend ID --file PATCH --reason TEXT [--by L] [--dry-run]`, `--reject`, `--supersede NEW_ID [--relink]` | 5.7; `--by` is required for a patch that changes `rev`. |
| `facts conflicts [--list] [--resolve CF --keep ID [--both] --reason TEXT]` | `--keep` rejects the other fact; with `--both` the conflict is closed and both stay (different scope; the reason is stored). |
| `facts render [--service S \| --all]` | Writes `facts/<service>.md` (5.8). |
| `facts list [--service] [--chapter] [--status] [--kind] [--hard]`, `facts show ID` | One line per fact (`id status rev kind first-display`); the whole fact with its votes and dependents. |

### 5.4 Votes and `finalize`

Required lenses of a fact:

- `entail` always (every fact; gate-break fix H1, RULINGS 2026-10-09; `hard` still decides M13 and the audit sample);
- `currency` when the fact is touched by a change item: `changed` is set, or `change_items` is not empty, or `volatility` is not `stable`;
- `derive` when `derivation` is set.

Verdicts per lens: `entail`: `support`, `partial`, `not-supported`, `unsure`; `derive`: `support`, `not-supported`, `unsure`; `currency`: `current`, `outdated`, `unsure`; `rederive`: `match`, `mismatch`, `not-found`. Positive: `support`, `current`, `match`. Rules, in order:

1. Only `mech-pass` and `disputed` facts are considered. A vote counts when its `rev` and `content` are current and its voter is neither the author nor an amender; every counting vote counts (one vote per voter, fact, rev and lens; R8).
2. A fact in an open conflict: `disputed`.
3. Any counting vote that is not positive (`partial` and `unsure` included): `disputed`; if the fact already has `repairs` 1: `rejected`.
4. A required lens without a counting vote: the fact stays `mech-pass` (pending).
5. Otherwise `verified`. No fact is verified on `mech-pass` alone: the `entail` vote is always required.

`finalize` writes the counting votes into `fact.votes` as `{"lens", "verdict", "voter", "rev"}`. A `rederive` vote comes from an audit (5.9); `facts vote` applies a `mismatch` or `not-found` at once: the `verified` fact becomes `disputed` and `ledger.mark_stale` is called for its chapters.

An adjudicator repairs a `disputed` fact once with `facts amend` (`repairs` becomes 1, `rev` + 1; `repairs` is raised only when the fact was `disputed`). Old votes stop counting; the fact needs fresh votes.

### 5.5 Packet

`{"batch", "lens", "instructions", "facts": [...]}`.

- For `entail` and `derive`, per fact: `id`, `rev`, `kind`, `claim`, `values`, `qualifiers`, `derivation`, and per evidence item `url`, `title`, `quote`, `table_header`, `context` (the snapshot lines that hold the match, with 5 lines before and after, at most 1,500 characters) and `headings` (the headings above the match).
- For `currency`, add `change_items`: the rows of `feeds.changes_for(service, since=book.change_window_start)` that are named in the fact's `change_items` or share at least two tokens of more than 3 letters with the claim; at most 8; each with `date`, `title`, `summary`, `url`, `quote`. A change item's key is its `id` (What's New) or `<history_source_id>#<line>` (history).
- For `rederive`: only `id`, `rev`, `service` and `question`.
- A packet never holds `author`, `status`, `votes`, `exam_relevance` or `note`.

### 5.6 Request queue

- `facts request --chapter CH --service S --question TEXT --where WHERE [--bullet ID]` appends an `open` request with id `fr-<4 digits>`. If an `open` or `filled` request of the same service has the same normalised question, nothing is added and that request is printed with `"duplicate_of"` (no duplicate is ever stored). `WHERE` is `<file>#<section id>` or an item id.
- `facts request --chapter CH --service S --fact ID --display TEXT --where WHERE` asks for one more display of an existing fact (`fact` = ID, `display` = TEXT, `question` = `display: TEXT`). The registrar adds the display with `facts amend` when M7 passes, then closes the request with `--close ID --fact ID`.
- `facts request --list [--status S] [--chapter CH]`.
- `facts request --close ID --fact FACT_ID` (the fact must be `verified`; status `filled`), or `--close ID --unfillable --note TEXT` (the note says where the search looked).

A sentence whose request is `unfillable` is never written. `report wave` counts open requests; the `counts` gate blocks on them (B09).

### 5.7 `amend` and dependents

The patch can change `claim`, `values`, `qualifiers`, `evidence`, `changed`, `change_items`, `kind`, `question`, `derivation`, `exam_relevance`, `tier0`, `note`, `volatility`, `source_tier`, `bullets` and `hard` (M11 still applies). The tool sets `rev` + 1, empties `votes`, stores the `--by` label in `amended_by` (an amender cannot vote on the fact), then runs the mechanical checks (pass: the fact is stored as `mech-pass`; fail: the amend is refused, exit 1, nothing is stored). A change of only `exam_relevance`, `tier0`, `question` or `note` keeps `rev`, status and votes.

Dependents are found by scanning:

- every hand `.md` of every chapter for links to `../facts/<service>.md#<id>`;
- every item of every `questions.json`, `cards.json`, `speak.json` and `tasks.json` whose `facts`, `cost_facts`, `key_points[].facts`, `follow_ups[].facts` or `must_not_say[].fact` hold the id, or whose text holds the link;
- `data/terms.json` (`facts`).

Effects when a `display` changed or was removed (none with `--dry-run`):

1. In hand Markdown and in JSON text fields, inside the text of links to this fact, the old display string is replaced by the new display of the same `key`. Link texts that then hold no display are listed as `broken_links`.
2. Each dependent question gets `status: candidate` and `verification: {"status": "candidate", "round": 0, "solvers": []}`. Each dependent card, speak item and task gets `status: candidate`.
3. `ledger.mark_stale(chapter, "fact <id> amended", item_stages=[...])` for every chapter with a dependent; `item_stages` names the item stages whose items step 2 reset, so that those stages run again and return the items to `ready`.
4. One line is appended to `_build/reports/changelog.jsonl`: `{"date", "fact", "reason", "was": [displays], "now": [displays], "chapters": [ids]}`.

`--reject` sets `rejected` and does steps 2 to 4 (every remaining link is lint error L302). `--supersede NEW_ID` sets `superseded` and `superseded_by`, rewrites the links to the new id with `--relink`, and does steps 2 to 4.

JSON: `{"fact", "rev", "status", "dependents": {"markdown": [{"file", "line"}], "questions": [], "cards": [], "speak": [], "tasks": []}, "replaced": 4, "broken_links": []}`.

### 5.8 Fact sheet `facts/<service>.md`

One file per service with at least one `verified` or `superseded` fact; facts sorted by id. The H3 text is the fact id, so the GitHub anchor equals the id: one anchor per fact.

```markdown
<!-- generated by saa.py; do not edit -->
# Amazon Widget Store: facts

7 facts, each with the exact sentence from AWS. Last checked 2026-10-04.

### widget-shelf-max-widgets

**Claim.** A shelf holds up to 500 widgets. Before November 19, 2025 the maximum was 200 widgets.

**Write it as.** `500 widgets` · `200 widgets`

**Scope.** per shelf; maximum; not adjustable.

> "Each shelf can hold up to 500 widgets."
> — [Amazon Widget Store limits](https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html)

**Checked.** 2026-10-04.

**Changed.** 2025-11-19: was 200 widgets.
```

- Title: the `official_name` of the first in-scope entry whose `keys` hold the service, else the service key. "Last checked" is the newest `retrieved`.
- One quote block per evidence item; links and images inside a quote print as their text. A table-row quote prints as `> "<cells joined with ' | '>" (columns: <header cells joined with ' | '>)`.
- `Scope.` joins `scope`, `default_or_max` (as `default`, `maximum`, `minimum`, `fixed`), `adjustable` or `not adjustable` (only for `limit`, `quota`, `default`) and `condition`; the line is left out when all are empty. `Changed.` only when `changed` is set.
- A superseded fact prints `### <old-id>` and `Replaced by [<new-id>](#<new-id>).`, so old links resolve.

### 5.9 `audit` and `freshen`

- `audit sample --n N --seed S [--chapter CH] [--revalidate]`: the population is the `verified` facts with `hard` true, sorted by id. With `--chapter`, the `tier0` facts of the chapter are taken first. The rest is `random.Random(S).sample`. The mechanical checks are re-run on the sample (`--revalidate` first calls `corpus.fetch(url, revalidate=True)` for each page). Writes `_build/reports/audit/s<S>-n<N>.json` = `{"id", "seed", "n", "created", "facts": [{"id", "rev", "claim", "quote", "url", "mech_ok"}]}` and prints the claim and quote pairs. Exit 1 when a mechanical check fails.
- `audit packet AUDIT --out FILE`: the `rederive` packet. A verifier returns votes with `answer`, `source_id` and `quote`. `facts vote` computes the verdict: `match` when the quote is found in the snapshot and every number of every `display` is in the answer or the quote (for a fact without numbers: a normalised `display` is held by the answer or the quote, `holds_display`); `not-found` when `answer` is null; else `mismatch`.
- `audit result AUDIT`: `{"sample": 20, "match": 19, "failed": [ids], "expand": [chapter ids]}`. With two or more failures, `expand` lists the home chapters of the failed facts (every hard fact there must be re-derived) and the exit code is 1.
- `freshen [--service S | --chapter CH] [--offline] [--limit N]`: for each snapshot cited by a non-rejected fact, `corpus.fetch(url, revalidate=True)` (skipped with `--offline`), then M2 and M3 against the current text. Quote still found: `evidence.sha256` and `retrieved` are updated and the status stays. Quote not found: the fact becomes `candidate` with `stale: "quote-missing"`, with the effects of 5.7 steps 2 and 3. Writes `_build/reports/freshen-<date>.json` = `{"pages": n, "not_modified": n, "changed": [source_ids], "facts_ok": n, "facts_broken": [ids], "errors": [{"url", "error"}]}`. Exit 1 when a fact broke, else 5 when a page could not be fetched, else 0. Because `retrieved` is printed in `sources.md` and in the fact sheets, `freshen` ends with `sync --only sources,facts` for the chapters it touched.

**Must-fail tests:** `add` rejects a paraphrased quote (M3); a display `5,000 widgets` against a quote with 500 (M5); `500 TiB` against a quote with `500 TB` (M5); a limit without scope (M6); a display that is in neither claim nor quote (M7); a 5-word quote that is not a complete sentence (M4); a hard fact without `question` (M13); a table row without `table_header` (M4); a host outside the allow-list (M2); a changed snapshot hash (M2); `hard: false` on a limit (M11). `vote` refuses the author and an amender as voter, a second vote by one voter on one fact, rev and lens, and a stale `rev`. `finalize` gives `disputed` for one `partial` vote, keeps any fact without an entail vote pending (hard or not), and keeps the changed fixture fact pending without a `currency` vote. `amend` of `500 widgets` to another value resets the fixture questions that use it and marks the chapter stale. The seven fixture facts pass `facts verify`, and `facts finalize` on the fixture votes changes nothing.

## 6. Lint and sync (`saalib/lint.py`): `lint`, `sync`

### 6.1 `lint CH [--file NAME] [--draft] [--strict]`, `lint --all`

Checks the hand-written files of a chapter (`source: hand` in the resolved template; template resolution as in `SPEC.json` `resolution`). JSON items are checked by `q lint`, `cards lint`, `speak lint` and `tasks lint`, which call `lint.check_strict_text`. Generated files are checked only for existence, first line and freshness (`sync --check`, section 6.2 in `TOOLS-items.md`).

- `--draft`: rules marked (d) become warnings. The `prose` stage uses it.
- `--strict`: treat the front matter `status` as `ready`.
- Writes `_build/reports/lint/<id>.json` = `{"chapter", "ok", "errors": [findings], "warnings": [findings], "counts": {"words": {"1-fast.md": 1650}, "sentence_average": 14.2, "fact_links": 61, "callouts": 5}}`. Exit 1 with errors, else 2 with warnings, else 0.

Parsing is line-based with the standard library. Blocks are separated by blank lines. A sentence is split as `lint.sentence.split` says; a table cell and a list item are each at least one sentence. Before the text rules run, normalise the text (R2), then remove front matter, HTML comments (after the markers `no-fact`, `needs-fact`, `needs-display`, `needs-term`, `xref`, `trap`, `trap-ref`, `gist-trap`, `task` and `twins` are read), fenced code, command-like inline code (R2) and generated regions. Image alt text is checked by L801 and L901 only. The exact matching rules (number with a unit, absolute word, banned word, prompt, bold field, callout label, quote block), the count keys of L106 and the codes added by contract fix 1 (L108, L308, L705, L905, W105, W308, W601, W903) are in `TOOLS-rules.md` R2 and R3; they are part of this section.

**Blocking rules**

| Code | Rule | SPEC.json keys |
|---|---|---|
| L101 | Every required file of the template exists; a generated file starts with the marker line (d); a Markdown file that the template does not list (d; chapter 00: `calendar-preview.md`) | `templates.*.files`, `chapter_overrides`, `generated_regions.generated_file_first_line` |
| L102 | Front matter parses and has the required keys; `id`, `slug`, `title`, `tier`, `services`, `kind`, `xl` equal the registry; `tasks` are among the registry entry's `tasks` when that list is not empty; `file` and `status` values | `front_matter.*`, `statuses.chapter` |
| L103 | One H1, equal to `title`; no heading below H3; H2 and H3 text matches the heading regex | `headings.*` |
| L104 | H2 sections: exact heading text, spec order, required ones present, no other H2 (`sections_mode: repeat`: one section per service, or the stated number) | `templates.*.files[].sections` |
| L105 | The section flag is on the next line and matches the regex; role and route equal the spec; `minutes` equals the heading time box; the fast time boxes add up to `minutes.fast`; the H3 time boxes add up to the `how` time box; a time box where one is required | `section_flag.*`, `headings.time_box_required_on` |
| L106 | Section counts: prompts, gist traps, rows, traps, compare tables, entries, subsections, one Stop and answer at the end of each subsection, fixed H3 names, assertion heading length | `sections[].counts`, `headings.fixed_h3`, `headings.assertion_heading_words` |
| L107 | Devices: a prompt label is allowed in the role and has the answer that its label needs; prompts end with `?`; reveal summaries and blank lines; bold fields present and in order; a Changed recently entry has the date and the four labelled lines, with a valid `Status` | `prompts.*`, `details.*`, `bold_fields.*`, `callouts.changed_recently` |
| L201 | The word count of a file is outside its `min` and `max` (`xl_max`, `by_tier`) | `files[].words`, `resolution.word_count`, `lint.file_word_limit_severity` |
| L202 | A Go deeper block, a callout, a table cell or a service-card field over its word limit; a sentence over `error_over_words`; a paragraph over `error_over_words` | `details.go_deeper_words_max`, `callouts.words_max`, `tables.cell_words_max`, `lint.sentence`, `lint.paragraph` |
| L301 | A fact link does not resolve: the href matches the regex, the fact exists and its `service` equals the file stem | `fact_links.href_regex`, `service_must_equal_file_stem` |
| L302 | The linked fact is not `verified` | `fact_links.fact_status_required` |
| L303 | The link text, normalised, holds no `display` of the fact (`holds_display`), or holds another number or a negation beside them | `fact_links.text_must_contain_a_display_value`, `comparison` |
| L304 | Strict text: a sentence or cell that has a number with a unit (the number regex followed by a unit or a count noun, with the extensions of R2; any currency amount) or an absolute word (R2, with the synonyms of `lint.EXTRA_ABSOLUTE`), and no fact link in the same sentence or cell; also a number with a unit outside the sentence's fact link | `roles`, `grounding.*`, `lint.absolute_words`, `lint.number_with_unit` |
| L305 | Heuristic text that has a number with a unit and no fact link | `grounding.heuristic`, `heuristic_blocks` |
| L306 | AWS quote block: the last line does not start with `— [`; the host is not allowed; the quote, without `> ` and its outer straight double quotes, is not found (`find_quote`) inside an evidence quote of a `verified` fact with the same URL, or does not hold whole sentences of it (R2); a case-study quote (its fact has kind `case-study`) is over 25 words | `fact_links.aws_quote` |
| L307 | A `needs-fact`, `needs-display` or `needs-term` marker in a file with status `reviewed` or `ready` | `fact_links.needs_fact_severity`, `marker_severity` |
| L401 | A callout label outside the list, or a generated-only label in a hand file | `callouts.labels` |
| L402 | More callouts than `callouts_max` (`callouts.not_counted_toward_callouts_max` are not counted); a `Try it` without a task comment, or with an unknown task id (d); a Try or Lab without exactly one `Try it` in its `section` (d) | `files[].callouts_max`, `callouts.not_counted_toward_callouts_max`, `devices.try_it` |
| L501 | A table without a kind comment on the line before the header, or with an unknown kind | `tables.kind_comment`, `tables.kinds` |
| L502 | Headers or column count wrong for the kind; more columns than the file allows; more rows in one table than the `rows_max` of its kind (default `tables.rows_max`) | `tables.kinds.*`, `files[].table_columns_max`, `tables.rows_max` |
| L503 | Kind rules: `signals` column 1 is quoted and no "But not if" cell is empty; `words`: cell 1 is a term of `data/terms.json` (d) and cell 2 has one bold span; `numbers` column 1 is a fact link; `compare` is followed by `**Deciding question:**` (in role `atlas`: `**Rule.**`) | `tables.kinds.*`, `devices.words_table` |
| L601 | A relative link to a missing file or anchor (the Markdown anchor of the full heading); a link to a generated file with an anchor; a fact link whose sheet `facts/<service>.md` or whose entry does not exist (d: run `sync`). A link to a file of another chapter that has no ledger status `drafted` or later is (d): the writer should have used an `xref` marker | `links.*`, `headings.markdown_anchor` |
| L602 | An external link outside an AWS quote block or a `Source.` field, or to a host outside the list; a bare URL | `links.external_allowed_in`, `lint.external_link_hosts` |
| L603 | A glossary link to a term id that is not in `data/terms.json` | `links.glossary` |
| L604 | A trap id that does not match the pattern, does not start with the slug, or is defined twice; a `trap-ref` whose id is not a trap of another chapter (a `trap-ref` is exempt from the slug and uniqueness tests); a task region whose id is not a `look` task of the chapter (d) | `ids.trap`, `generated_regions` |
| L701 | A diagram image that does not match the regex, is not alone in its paragraph, has an id that does not start with the slug, or has no SVG file (the missing SVG is (d)) | `diagram_embed.*` |
| L702 | The caption is missing, has more than one sentence or more than 24 words, or (when the spec exists) differs from the spec `claim`; the alt text differs from the spec `alt` | `diagram_embed.caption_*`, `equals_spec` |
| L703 | The spec (when `diagrams/src/<id>.json` exists) has numbered steps, and the ordered list after the caption has another number of items, or a step sentence differs from the spec `say` | `diagram_embed.step_list`, `equals_spec` |
| L704 | The hero diagram is missing (d), is not inside "Show the picture" after "Predict the picture.", or its spec is not of a kind in `hero_kinds` | `diagram_embed.hero_*` |
| L801 | A banned word or phrase (`lint.word_match`, exceptions honoured), outside AWS quotes; a customer word inside one of its allowed places is not a finding | `lint.banned_words`, `word_match`, `banned_word_exceptions`, `banned_words_scope` |
| L802 | A former service name (also `former_name_regexes`), except once per file directly after `formerly ` or `**Formerly.** `; not checked in a service-card heading or an AWS quote | `lint.former_names`, `former_name_allowed_once_after` |
| L803 | Raw HTML outside the allowed tags; emoji; italic emphasis; a contraction in prose; an image without alt text | `lint.raw_html_allowed`, `emoji`, `emphasis_italic`, `contractions_in_prose`, `images_need_alt` |
| L804 | Code: no language, an unknown language, more than 12 lines, a banned pattern | `code.*` |
| L901 | A banned variant of a term (`banned`, `banned_case` and `former_names` in `data/terms.json`; never `avoid`), unless it is part of a longer term or official name at that place | `lint.banned_term_match` |
| L902 | A customer word outside its allowed places | `lint.customer_words`, `customer_words_allowed_in` |
| L903 | Orphan rule: a "How it works" subsection that is the `section` of no question, card, speak item or task (d) | `lint.orphan_rule` |
| L904 | A required text of a file is missing | `files[].required_text` |

**Warnings**

| Code | Rule | SPEC.json keys |
|---|---|---|
| W201 | A section or subsection outside its word range | `sections[].words`, `lint.section_word_limit_severity` |
| W202 | A sentence over `warn_over_words`; the average sentence length over `average_words_max`; a paragraph with more than 4 sentences or over `warn_over_words`; more than 3 new bold terms in a paragraph | `lint.sentence`, `lint.paragraph` |
| W203 | More than 400 words of "How it works" text between two Stop and answer prompts | `lint.stop_and_answer_interval_words` |
| W307 | A `needs-fact` marker in a `draft` file | `fact_links.needs_fact_severity` |
| W801 | A warn word; an em dash in prose (not in a quote attribution) | `lint.warn_words`, `em_dash_in_prose` |
| W802 | A short form of `data/terms.json` (`short`) used before its full term in the file | `lint.abbreviation_spell_out_first_use_per_file` |
| W901 | The first occurrence of a term in the chapter is not bold, or lacks its respelling; a words-table row whose cell 1 is the term defines it, wherever that table first names it (1.0 rule: R11) | `lint.term_rules` |
| W902 | More than `story_max_words_per_chapter` words in the `Startup example` callouts of the chapter; the former working name of the startup. (The `startup.cast` name check is not implemented; review: R11.) | `startup.*` |

**Role exemptions of L304** and the list of what is not counted as a number: `TOOLS-rules.md` R2.

**Must-fail tests:** the list is in `TOOLS-rules.md` R3. The unchanged fixture chapter has no blocking finding in draft mode.

### 6.2 `sync`, 7 question bank, 8 tasks

See `TOOLS-items.md`.

## 9. Reserved subcommands

Top-level names of this contract: `stage`, `gate`, `status`, `report`, `selftest`, `registry`, `coverage`, `facts`, `audit`, `freshen`, `lint`, `sync`, `q`, `cards`, `speak`, `mocks`, `drills`, `tasks`. Taken by other modules: `ping`, `fetch`, `guide`, `search`, `show`, `tables`, `faq`, `changes`, `cases`, `diagram`. Reserved for later: `build` with `web` (`saalib/site.py`, options `--only-ready`, `--single`, `--preview`) and `anki`, `pdf`, `readme` (`saalib/exports.py`). PRODUCT's `lint.py`, `sync_md.py` and `diagram.py` scripts are the subcommands `lint`, `sync` and `diagram`.

## 10. Decisions taken here

Moved to `TOOLS-rules.md` R7, with the decisions of contract fix 1.
