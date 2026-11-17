# Test fixtures

Everything here is invented for tool tests. "Amazon Widget Store" is not an AWS service, and no fixture URL was ever fetched.

## What is here

| Path | Content | Used by |
|---|---|---|
| `book/` | A complete miniature book: one deep chapter (`99-sample`), its data, its facts, its snapshots and its build state | every module |
| `book/99-sample/1-fast.md`, `2-deep.md` | hand-written chapter files that follow `CONVENTIONS.md` | lint, sync |
| `book/data/book.json` | the registry in its built form (tasks, bullets, sources, `service_map`, `exam_guide`) | all |
| `book/data/99-sample/*.json` | 4 questions, 3 cards, 1 speak item, 2 tasks | qbank, lab, sync |
| `book/data/facts/widget.jsonl` | 7 verified facts | facts, lint |
| `book/data/terms.json` | a few terms | lint, sync |
| `book/_build/style/SPEC.json` | the content contract with small counts and word limits; same structure as the real one | all (read through `common.STYLE_DIR`) |
| `book/_build/corpus/snap/docs/fixture/widget-store/limits.*` | the page the facts quote | facts |
| `book/_build/corpus/snap/aws/fixture/case-studies/tallis-freight.*` | a case-study page | facts |
| `book/_build/corpus/snap/aws/fixture/certification/certified-widget-specialist.*` | an invented certification page whose exam overview states each value as a heading and a short value line (`### Exam duration`, then `130 minutes`); no fixture fact cites it | facts (heading-scoped quotes, `test_facts_holes.HeadingScopedQuotes`) |
| `book/_build/corpus/snap/docs/fixture/exam-guide/*` and `corpus/index/fixture-exam-guide.json` | a 7-page exam guide in the markup of the real one (4 domains, 5 task statements, 13 bullets, 3 in-scope entries of which 2 are unique, 1 out-of-scope) | registry |
| `book/_build/registry/exam-guide.json`, `services.json` | the expected result of `registry build --offline` on those pages | registry (expected output), qbank, coverage |
| `book/_build/facts/votes/widget.jsonl` | the votes that make the 7 facts verified | facts |
| `book/_build/facts/requests.jsonl` | one open and one unfillable fact request | facts, ledger |
| `book/_build/ledger/chapters/99.json`, `gates/99.facts-final.json`, `events.jsonl` | a ledger: four stages passed, `brief` failed twice | ledger |
| `book/_build/work/99-sample/brief.v0.json` | the plan-stage demand list | ledger |
| `book/diagrams/svg/sample-hero.svg` | the hero figure (it has no spec in `diagrams/src/`, so the `diagrams` gate fails on the fixture with D01) | lint, ledger |
| `diagram/`, `feeds/` | fixtures owned by the diagram and feeds modules | those modules |

Things to know since contract fix 1 (2026-10-04):

- The startup is Callvale (`STARTUP.md`); the fixture uses that name.
- The twin pair `sample-q001` / `sample-q002` turns on a number with a change date. It is not volatile only because the fixture `SPEC.json` has `questions.volatile_window_months` 6. Tests of Q112 set the window back to 24. Real chapters never copy this choice.
- `sample-q001` is the wrong-path think-aloud (`worked.wrong_path: true`); the fixture counts ask for one.
- `sample-t02` shows both tag syntaxes (`book=saa,task=...` and `Key=book,Value=saa Key=task,Value=...`), a break-it step with `explain`, and `pass_route: true`.
- The cards are hand types only (`number`, `cannot`, `decide`); generated card types come from `cards build`.
- `2-deep.md` holds the `needs-fact` marker of the open request `fr-0001` (a warning in draft mode, W307).
- Known failures of the unchanged fixture: the `diagrams` gate (D01), the `counts` gate (B09), `tasks lint --ship` (T113).
- `python3 aws-saa-book/tools/tests/doc_sizes.py` prints the hash of `widget.jsonl` for `gates/99.facts-final.json`, and the word counts of the contract documents.

Things the fixture leaves out on purpose:

- No schema folder. `saalib.schemas.load()` falls back to the real `_build/schemas/`.
- No `.raw` snapshot files. In the fixture, `sha256` in a snapshot meta is the hash of the `.txt` file.
- The fixture snapshot ids (`docs/fixture/...`) are not what `corpus.source_id_for(url)` would return for their URLs. Code that asks "is this URL in the corpus" must also accept a snapshot whose meta has that `url` (TOOLS.md section 0, rule 11).
- Stages in the fixture ledger have `inputs_hash: null`. `stage begin` on a passed fixture stage therefore answers GO with reason `inputs-changed`. A test of SKIP must pass the stage through the tool first.
- No generated files (`3-do.md`, `4-say.md`, `5-quiz.md`, `sources.md`, `facts/widget.md`, `glossary.md`). Run `sync` in the sandbox to make them; `sync --check` on a fresh sandbox reports them missing.

## How a test uses the fixture

Never run a test against the real book, and never edit the fixture from a test. Copy it into a sandbox under `aws-saa-book/_build/tmp/` and point the tool at the copy. `tools/tests/sandbox.py` does this:

```python
import unittest
import sandbox                      # tests/ is on sys.path when run.py runs the tests
from saalib import common

class FactsGate(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("facts-" + self.id().split(".")[-1])   # aws-saa-book/_build/tmp/facts-<test>
    def tearDown(self):
        sandbox.remove(self.book)

    def test_fixture_facts_pass(self):
        code, result, err = sandbox.run_json(self.book, "facts", "verify", "--service", "widget")
        self.assertEqual(code, 0, err)

    def test_must_fail_wrong_number(self):
        def change(rows):
            rows[0]["values"][0]["display"] = "5,000 widgets"
        sandbox.edit_jsonl(self.book / "data" / "facts" / "widget.jsonl", change)
        code, result, err = sandbox.run_json(self.book, "facts", "verify", "--service", "widget")
        self.assertEqual(code, 1)
        self.assertIn("M5", [f["code"] for f in result["failed"][0]["errors"]])
```

- `sandbox.make(name)` deletes any old sandbox of that name and copies `fixtures/book/` to `aws-saa-book/_build/tmp/<name>`. Use one sandbox per test (the test name in the sandbox name), so tests can run in any order.
- `sandbox.run(book, *args)` runs `python3 aws-saa-book/tools/saa.py --book-dir <book> <args>` in a new process and returns `(exit code, stdout, stderr)`. `sandbox.run_json` adds `--json` and parses the output.
- `sandbox.paths(book)` is a context manager for in-process tests: it points `common.BOOK`, `common.DATA`, `common.BUILD`, `common.CORPUS` and the other path attributes at the sandbox, then restores them. This works only because modules read `common.X` at call time; a module that does `from saalib.common import DATA` breaks it.
- `sandbox.edit_json`, `sandbox.edit_jsonl` and `sandbox.replace_text` make the one change of a must-fail test.

By hand, the same thing is one plain command:

```
python3 aws-saa-book/tools/saa.py --book-dir aws-saa-book/_build/tmp/my-sandbox lint 99
```

`--book-dir` must be inside `aws-saa-book/`; the tool refuses anything else with exit code 4.

## Rules for tests

1. Offline. No test makes a network request. Patch `corpus._transport` (see `TOOLS-corpus.md`) or the helper runner (`lab._run_helper`).
2. Every gate has at least one test named `test_must_fail_<what>`: one bad input that the gate must reject, with an assertion on the exit code and on the finding code.
3. A must-fail test changes exactly one thing in the sandbox, so the finding proves the rule.
4. If a rule of `TOOLS.md` fails on the unchanged fixture, report it; do not change the fixture or the rule silently.
5. Run one module's tests with `python3 aws-saa-book/tools/tests/run.py <module>`. `run.py contract` also runs `test_contract_tools.py`, which checks the schemas of `TOOLS.md` against this fixture.

## Changing the fixture

The fixture is shared. A change needs the same change in whatever depends on it:

- `book/data/facts/widget.jsonl` changed: update the `sha256` in `book/_build/ledger/gates/99.facts-final.json`.
- A snapshot `.txt` changed: update `sha256` in its `.meta.json`, in every fact evidence that cites it, and (for exam guide pages) in `book/_build/registry/exam-guide.json`, with the line numbers.
- `book/_build/style/SPEC.json` must keep the structure of the real `SPEC.json` (`test_contract.py` checks it).
