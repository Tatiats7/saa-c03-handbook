"""Tests of the site build (part A of the web version).

Run:  python3 aws-saa-book/tools/web/tests/test_site.py

The Markdown-to-HTML mapping of tools/web/ARCHITECTURE.md section 2.3 is tested through the real helper
(tools/helpers/site_md.py under uv), with one job that holds one small Markdown text per device. The last
class builds the fixture book in a sandbox and checks the emitted files.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = next(p for p in HERE.parents if (p / "saa.py").is_file())   # works from tools/web/tests and from tools/tests
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "tests"))

from saalib import common, site, _site_web  # noqa: E402

FAST = """---
id: "99"
slug: sample
title: Amazon Widget Store
file: fast
---

# Amazon Widget Store

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

Guess before you read.

**Predict 1.** Does a shelf belong to every Region? <!-- gist-trap -->

**Predict 2.** Do 600 widgets fit on one shelf?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

<!-- task:start id=sample-t01 -->
Look

1. Old generated text that the app replaces.
<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Widget Store keeps widgets on a shelf in [one AWS Region](../facts/widget.md#widget-shelf-scope).

**The problem it solves.** A team counts widgets wrongly.

**Predict the picture.** Where does a shelf sit?

<details>
<summary>Show the picture</summary>

![A Region frame that contains one shelf, and a team outside](../diagrams/svg/sample-hero.svg)

**Figure.** A shelf sits inside [one AWS Region](../facts/widget.md#widget-shelf-scope).

1. The team creates a shelf.
2. The team puts widgets on the shelf.

</details>

> **Startup example:** Callvale keeps 300 demo widgets.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| shelf | **create** a shelf in a Region | The place that stores widgets | crate |
| crate (KRAYT) | **ship** a crate | A container | shelf |

## Choose it or not (2 min)
<!-- section: role=choose; route=fast; minutes=2 -->
<!-- twins: shelf-capacity crate -->

### Shelf or crate

<!-- table: compare -->
| Question | Shelf | Crate |
|---|---|---|
| How many widgets fit? | [500 widgets](../facts/widget.md#widget-shelf-max-widgets) | 50 widgets |

**Deciding question:** Do the widgets stay in one Region?

## Signals and traps (2 min)
<!-- section: role=signals; route=fast; minutes=2 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "widgets must stay on a shelf" | shelf | a shelf is Regional | more than one shelf |

### Traps

- **Wrong belief:** A shelf is global. **Truth:** A shelf stores widgets in [one AWS Region](../facts/widget.md#widget-shelf-scope). <!-- trap: sample-trap-shelf-global -->
- **Wrong belief:** A shelf grows without a limit. **Truth:** It does not. <!-- trap-ref: other-trap-limit -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-11-19) Maximum number of widgets on a shelf.<br>
> **Old:** [200 widgets](../facts/widget.md#widget-shelf-max-widgets).<br>
> **Now:** [500 widgets](../facts/widget.md#widget-shelf-max-widgets).<br>
> **The exam probably expects:** the new value.<br>
> **Status:** not examinable yet.

## Check (1 min)
<!-- section: role=check; route=fast; minutes=1 -->

**Check 1.** Does the Tokyo Region hold a copy?

<details>
<summary>Answer</summary>

No. A shelf is Regional.

</details>
"""

DEEP = """---
chapter: "99"
file: deep
title: Amazon Widget Store in depth
---

# Amazon Widget Store in depth

## How it works (6 min)
<!-- section: role=how; route=full; minutes=6 -->

### A shelf belongs to one Region for its whole life (3 min)
<!-- section: route=pass -->

A shelf is a [Regional resource](../facts/widget.md#widget-shelf-scope). A shelf is not a crate, and a shelf is a shelf.

See [Signals and traps](1-fast.md#signals-and-traps-2-min), [the fast file](1-fast.md), [this section](#how-it-works-6-min),
[the quiz](5-quiz.md), [the sources](sources.md#x), [VPC](../10-vpc/1-fast.md#predict-1-min), [missing](1-fast.md#no-such-anchor),
[the glossary](../glossary.md), [idempotent](../glossary.md#idempotent), [a sheet](../facts/widget.md),
[unknown fact](../facts/widget.md#widget-nope), [waiting fact](../facts/widget.md#widget-candidate),
[other](../11-iam/1-fast.md#predict-1-min).

> **Key fact:** A shelf stores widgets in one Region.

> **Exam signal:** "must stay in one Region" points to a shelf.

> **Exam trap:** A new shelf is not public. <!-- trap: sample-trap-deep -->

> **Exam heuristic:** The exam prefers the secure default.

> **Try it:** Create a shelf. See [3-do.md](3-do.md). <!-- task: sample-t02 -->

> **Cost:** $0.

> **Clean up:** Run these steps.

> **Careful:** Stop at twice the time.

> A plain quote that is no callout.

A description names its Region with `Region` in it, H<sub>2</sub>O, <kbd>Ctrl</kbd>, and <span>dropped</span> text. <!-- no-fact: stem --> <!-- xref: 04 scps -->

```json
{"Shelf": "saa-sample-shelf", "Widgets": 300}
```

```bash
# list the shelves
aws widget list-shelves --query "Shelves[].Name"
```

<details>
<summary>Go deeper: the shelf quota</summary>

The default quota is 20 shelves.

</details>

**Spot the bug.** Ben plans one shelf for 800 widgets. What is wrong?

```text
shelf: 800
```

<details>
<summary>Answer</summary>

A shelf holds less.

</details>

**Stop and answer.** What do you do with the shelf?

<details>
<summary>Answer</summary>

You copy the shelf.

</details>

### A new shelf is private until the owner changes it (3 min)

A new shelf starts closed.

**Stop and answer.** Can Ana read the shelf?

## Numbers that decide answers (1 min)
<!-- section: role=numbers; route=full; minutes=1 -->

### A-list

<!-- table: numbers -->
| Number | What it is |
|---|---|
| [500 widgets](../facts/widget.md#widget-shelf-max-widgets) | Maximum |

## Decision record (2 min)
<!-- section: role=example; route=full; minutes=2 -->

**Context.** Callvale stores 300 widgets.

**Options.**

- One shelf.
- Six crates.

**Decision.** One shelf.

**Rule.** Pick the shelf.

## FAQ quick-fire (2 min)
<!-- section: role=faq; route=full; minutes=2 -->

**FAQ 1.** Can you move a shelf?

<details>
<summary>Answer</summary>

No.

> "You cannot move a shelf to another Region."
> — [Amazon Widget Store limits](https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html)

</details>

See [a bad host](https://example.com/page) too.

## The patterns (2 min)
<!-- section: role=map; route=full; minutes=2 -->

### Two shelves (2 min)

**Problem.** A company keeps 600 widgets.

### Missing picture

![A drawing that does not exist anywhere in the book](../diagrams/svg/sample-missing.svg)

![A drawing that has a spec and renders as inline SVG](../diagrams/svg/sample-inline.svg)

**Figure.** The inline one.
"""

SERVICES = """---
chapter: "99"
file: services
title: Services
---

# Services

## Amazon Example Service (1 min)
<!-- section: role=card; route=full; minutes=1; service=example-service -->

**What it is.** One sentence.

**Stem signals.**

- "first stem phrase"

**Source.** [Page title](https://docs.aws.amazon.com/example/)
"""

CALENDAR = """---
chapter: "00"
file: calendar
title: Calendar
---

# Calendar

## Plan A (2 min)
<!-- section: role=plan; route=fast; minutes=2 -->

Plan A is the full plan.

<!-- plan:start id=a -->
<!-- table: plan -->
| Day | Minutes | Work |
|---|---|---|
| Day 1 | 60 | Read |
<!-- plan:end -->

## Log (1 min)
<!-- section: role=plan; route=fast; minutes=1 -->

<!-- table: log -->
| Date | Question | Cause | Sure | Fix |
|---|---|---|---|---|
| Day 3 | sample-q002 | W | yes | Read the last sentence first |

### Qualifiers (3 min)

<!-- exam-english:start group=qualifiers -->
<!-- table: plain -->
| Word | Meaning | It signals |
|---|---|---|
| MOST | the top one | a ranking |
<!-- exam-english:end -->

<!-- table: plain -->
| A | B |
|---|---|
| 1 | 2 |
"""

SHEET = """<!-- generated by saa.py; do not edit -->
# Signals and traps: sheet

## Amazon Widget Store

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "stay in one Region" | shelf | Regional | more widgets |

- **Wrong belief:** A shelf is global. **Truth:** It is Regional.
"""

INLINE_SVG = '<svg class="dg dg-arch" width="200" height="100" viewBox="0 0 200 100" role="img" style="--dg-w:200"></svg>'
CTX = {
    "facts": {"widget-shelf-scope": {"service": "widget", "displays": ["one AWS Region", "Regional resource"]},
              "widget-shelf-max-widgets": {"service": "widget", "displays": ["500 widgets", "200 widgets"]}},
    "unverified": ["widget-candidate"],
    "terms": [{"id": "shelf", "cs": True, "forms": ["shelf"]}, {"id": "crate", "cs": True, "forms": ["crate"]},
              {"id": "regional", "cs": False, "forms": ["Regional"]}, {"id": "idempotent", "cs": False, "forms": ["idempotent"]}],
    "chapters": {"99-sample": "sample", "10-vpc": "vpc", "11-iam": "iam"},
    "part_of_file": site.PART_OF_FILE,
    "sections": {"sample": {"1-fast.md": site.scan_sections(FAST), "2-deep.md": site.scan_sections(DEEP)},
                 "iam": {"1-fast.md": {"predict-1-min": "predict"}}},
    "diagrams": {"sample-hero": {"html": '<img class="fig-img" alt="" style="--dg-w:444" src="data:image/svg+xml;base64,AAAA">',
                                 "kind": "image", "title": "", "claim": "", "steps": []},
                 "sample-inline": {"html": INLINE_SVG, "kind": "arch", "title": "A shelf in a Region", "claim": "x", "steps": []}},
    "callouts": [{"label": "Key fact", "hue": "indigo"}, {"label": "Exam signal", "hue": "indigo"},
                 {"label": "Exam trap", "hue": "red"}, {"label": "Exam heuristic", "hue": "amber"},
                 {"label": "Changed recently", "hue": "neutral"}, {"label": "Say it", "hue": "teal"},
                 {"label": "Try it", "hue": "teal"}, {"label": "Startup example", "hue": "teal"},
                 {"label": "Cost", "hue": "amber"}, {"label": "Clean up", "hue": "amber"}, {"label": "Careful", "hue": "amber"}],
    "prompts": ["Predict <n>.", "Check <n>.", "Recap <n>.", "FAQ <n>.", "Stop and answer.", "Spot the bug.", "Predict the picture."],
    "bold_fields": {"breath": ["The problem it solves."], "decision": ["Context.", "Requirement.", "Options.", "Decision.", "Trade-off."],
                    "choose": ["Deciding question:"], "figure": ["Figure."], "atlas": ["Rule."],
                    "card": ["What it is.", "Stem signals.", "Source."], "pattern": ["Problem."]},
    "table_kinds": ["compare", "signals", "words", "numbers", "pairs", "matrix", "glance", "services", "breaks", "log", "plan",
                    "exam-english", "plain"],
    "hosts": ["docs.aws.amazon.com", "aws.amazon.com"],
}
JOB = {"chapters": [{"slug": "sample", "id": "99", "dir": "99-sample", "quiz": True,
                     "parts": [{"key": "fast", "file": "1-fast.md", "text": FAST}, {"key": "deep", "file": "2-deep.md", "text": DEEP},
                               {"key": "services", "file": "2-services.md", "text": SERVICES},
                               {"key": "calendar", "file": "calendar.md", "text": CALENDAR},
                               {"key": "sheet", "file": "sheet.md", "text": SHEET}]}],
       "inline": {"why": "A shelf holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets), **not** more. See [x](1-fast.md) & <b>y</b>.",
                  "empty": ""},
       "ctx": CTX}
RESULT = {}


def setUpModule():
    sandbox = common.REAL_BOOK / "_build" / "tmp" / "test-site-helper"
    if sandbox.exists():
        shutil.rmtree(sandbox)
    saved = common.TMP
    common.TMP = sandbox
    try:
        RESULT.update(site.run_helper(JOB))
    finally:
        common.TMP = saved
        shutil.rmtree(sandbox, ignore_errors=True)


def part(key):
    return RESULT["parts"][f"sample/{key}"]


class Mapping(unittest.TestCase):
    def has(self, key, text):
        self.assertIn(text, part(key)["html"])

    def lacks(self, key, text):
        self.assertNotIn(text, part(key)["html"])

    def codes(self, key):
        return [(w["code"], w["level"]) for w in part(key)["warnings"]]

    # ---- headings and sections

    def test_h1_is_dropped_and_title_is_data(self):
        self.lacks("fast", "<h1")
        self.assertEqual(part("fast")["title"], "Amazon Widget Store")
        self.assertEqual(part("deep")["title"], "Amazon Widget Store in depth")

    def test_h2_section(self):
        self.has("fast", '<section class="sec" id="sec-predict" data-sid="predict" data-role="predict" data-route="fast" data-min="1">'
                         '<header class="sec-h"><h2>Predict</h2><span class="tbox">1 min</span>'
                         '<button type="button" class="sec-ask" data-act="ask" hidden>Ask</button></header><div class="sec-b">')
        html = part("fast")["html"]
        self.assertEqual(html.count("<section"), html.count("</section>"))
        self.assertEqual(html.count("<div"), html.count("</div>"))
        self.lacks("fast", "section:")

    def test_service_card_section(self):
        self.has("services", 'data-role="card" data-route="full" data-min="1" data-service="example-service">')
        row = part("services")["sections"][0]
        self.assertEqual((row["service"], row["kind"]), ("example-service", 2))
        self.has("services", '<p class="bf" data-f="stem-signals"><span class="bf-l">Stem signals.</span> </p><ul class="bf-list">')
        self.has("services", '<a class="ext" href="https://docs.aws.amazon.com/example/" target="_blank" rel="noopener">Page title</a>')

    def test_h3_subsection_in_how(self):
        self.has("deep", '<section class="sub" id="sec-a-shelf-belongs-to-one-region-for-its-whole-life" '
                         'data-sid="a-shelf-belongs-to-one-region-for-its-whole-life" data-route="pass" data-min="3">'
                         '<header class="sub-h"><h3>A shelf belongs to one Region for its whole life</h3><span class="tbox">3 min</span></header>'
                         '<div class="sub-b">')
        self.has("deep", 'id="sec-a-new-shelf-is-private-until-the-owner-changes-it" '
                         'data-sid="a-new-shelf-is-private-until-the-owner-changes-it" data-route="full" data-min="3">')
        rows = {s["sid"]: s for s in part("deep")["sections"]}
        sub = rows["a-shelf-belongs-to-one-region-for-its-whole-life"]
        self.assertEqual((sub["kind"], sub["route"], sub["min"], sub["parent"], sub["role"]), (3, "pass", 3, "how-it-works", "how"))
        self.assertEqual(rows["how-it-works"]["kind"], 2)

    def test_h3_with_time_box_outside_how_is_tracked(self):
        rows = {s["sid"]: s for s in part("deep")["sections"]}
        self.assertEqual((rows["two-shelves"]["kind"], rows["two-shelves"]["min"]), (3, 2))
        self.has("deep", '<p class="bf" data-f="problem"><span class="bf-l">Problem.</span> A company keeps 600 widgets.</p>')

    def test_plain_h3(self):
        self.has("fast", '<h3 class="h3" id="sec-traps" data-sid="traps">Traps</h3>')
        rows = {s["sid"]: s for s in part("fast")["sections"]}
        self.assertEqual((rows["traps"]["kind"], rows["traps"]["parent"], rows["traps"]["facts"]), (0, "signals-and-traps", []))
        self.assertEqual(rows["shelf-or-crate"]["kind"], 0)

    def test_section_rows_and_lists(self):
        rows = {s["sid"]: s for s in part("fast")["sections"]}
        self.assertEqual([s["sid"] for s in part("fast")["sections"]][:3], ["predict", "look-first", "in-one-breath"])
        self.assertEqual(rows["in-one-breath"]["facts"], ["widget-shelf-scope"])
        self.assertEqual(rows["in-one-breath"]["figures"], ["sample-hero"])
        self.assertIn("shelf", rows["in-one-breath"]["terms"])
        self.assertEqual(rows["signals-and-traps"]["traps"], ["sample-trap-shelf-global", "other-trap-limit"])
        deep = {s["sid"]: s for s in part("deep")["sections"]}
        self.assertEqual(deep["how-it-works"]["facts"], [])          # the children hold them
        self.assertIn("widget-shelf-scope", deep["a-shelf-belongs-to-one-region-for-its-whole-life"]["facts"])

    def test_section_text(self):
        text = {t["sid"]: t for t in part("deep")["text"]}
        how = text["how-it-works"]
        self.assertIn("You copy the shelf.", how["text"])              # reveals are in, children are in
        self.assertNotIn("saa-sample-shelf", how["text"])              # code is out
        self.assertNotIn("You copy the shelf.", how["own"])
        fast = {t["sid"]: t["text"] for t in part("fast")["text"]}
        self.assertIn("shelf | create a shelf in a Region | The place that stores widgets | crate", fast["words-that-go-together"])
        self.assertNotIn("traps", fast)                                # kind 0 has no text of its own

    def test_lede(self):
        self.has("fast", '<div class="sec-b"><p class="lede">Guess before you read.</p>')
        self.has("deep", '<div class="sub-b"><p class="lede">A <a class="term"')
        self.assertEqual(part("fast")["html"].count('class="lede"'), 1)   # sections that start with another block have none
        self.has("calendar", '<p class="lede">Plan A is the full plan.</p>')

    # ---- prompts and reveals

    def test_predict_prompts(self):
        self.has("fast", '<div class="pr pr-predict" data-pid="predict-1" data-gist="1"><p class="pr-q">'
                         '<span class="pr-l">Predict 1 · careful</span> Does a <a class="term" href="#glossary.shelf" data-term="shelf">shelf</a>'
                         ' belong to every Region? </p></div>')
        self.has("fast", '<div class="pr pr-predict" data-pid="predict-2"><p class="pr-q"><span class="pr-l">Predict 2</span> ')
        self.lacks("fast", "gist-trap")

    def test_check_prompt_holds_its_reveal(self):
        self.has("fast", '<div class="pr pr-check" data-pid="check-1"><p class="pr-q"><span class="pr-l">Check 1</span> '
                         'Does the Tokyo Region hold a copy?</p><details class="rv rv-answer"><summary>Answer</summary>'
                         '<div class="rv-b"><p>No. A <a class="term" href="#glossary.shelf" data-term="shelf">shelf</a> is '
                         '<a class="term" href="#glossary.regional" data-term="regional">Regional</a>.</p></div></details></div>')

    def test_unnumbered_prompts_and_bug_with_code(self):
        self.has("deep", '<div class="pr pr-bug" data-pid="bug-1"><p class="pr-q"><span class="pr-l">Spot the bug</span> ')
        self.assertRegex(part("deep")["html"], r'data-pid="bug-1">.*?</p><div class="code" data-lang="text">.*?</div>'
                                               r'<details class="rv rv-answer">')
        self.has("deep", 'data-pid="stop-1"')
        self.has("deep", '<div class="pr pr-stop" data-pid="stop-2"><p class="pr-q"><span class="pr-l">Stop and answer</span> '
                         'Can Ana read the shelf?</p></div>')
        self.has("deep", '<div class="pr pr-faq" data-pid="faq-1">')

    def test_picture_reveal_and_deeper_reveal(self):
        self.has("fast", '<div class="pr pr-pic" data-pid="pic-1">')
        self.has("fast", '<details class="rv rv-picture"><summary>Show the picture</summary><div class="rv-b"><figure class="fig"')
        self.has("deep", '<details class="rv rv-deeper"><summary><span class="rv-l">Go deeper</span> the shelf quota</summary>'
                         '<div class="rv-b"><p>The default quota is 20 shelves.</p></div></details>')
        self.lacks("deep", "&lt;details")

    # ---- callouts

    def test_callouts(self):
        self.has("fast", '<aside class="co co-say hue-teal" data-label="Say it"><p class="co-l">Say it</p><div class="co-b"><p>Widget Store')
        self.has("fast", '<aside class="co co-startup hue-teal" data-label="Startup example">')
        for key, hue, label in (("key", "indigo", "Key fact"), ("signal", "indigo", "Exam signal"), ("heur", "amber", "Exam heuristic"),
                                ("cost", "amber", "Cost"), ("cleanup", "amber", "Clean up"), ("careful", "amber", "Careful")):
            self.has("deep", f'<aside class="co co-{key} hue-{hue}" data-label="{label}"><p class="co-l">{label}</p><div class="co-b"><p>')
        self.lacks("deep", "<strong>Key fact:</strong>")

    def test_trap_callout_and_try_callout(self):
        self.has("deep", '<aside class="co co-trap hue-red" data-label="Exam trap" data-trap="sample-trap-deep">')
        self.assertEqual(part("deep")["trapmap"]["sample-trap-deep"], "a-shelf-belongs-to-one-region-for-its-whole-life")
        self.has("deep", '<aside class="co co-try hue-teal" data-label="Try it" data-task="sample-t02">')
        self.has("deep", '<a class="xr" href="#ch.sample.do.sample-t02">the Do part</a>')
        self.assertEqual(part("deep")["tasks"], ["sample-t02"])

    def test_changed_recently(self):
        self.has("fast", '<aside class="co co-changed hue-neutral" data-date="2025-11-19" data-status="not-yet">'
                         '<p class="co-l">Changed recently <time>2025-11-19</time></p>'
                         '<p class="chg-what">Maximum number of widgets on a ')
        self.has("fast", '<dl class="chg"><dt>Old</dt><dd><a class="ev" href="#fact.widget-shelf-max-widgets" '
                         'data-fact="widget-shelf-max-widgets">200 widgets</a></dd><dt>Now</dt><dd>')
        self.has("fast", '<dt>The exam probably expects</dt><dd>the new value.</dd><dt>Status</dt><dd><span class="pill">not examinable yet</span></dd></dl></aside>')

    def test_aws_quote_and_other_blockquote(self):
        self.has("deep", '<figure class="awsq"><blockquote>"You cannot move a shelf to another Region."</blockquote><figcaption>'
                         '<a class="ext" href="https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html" target="_blank" '
                         'rel="noopener">Amazon Widget Store limits</a></figcaption></figure>')
        self.has("deep", "<blockquote><p>A plain quote that is no callout.</p></blockquote>")
        self.assertIn(("WB09", "warning"), self.codes("deep"))

    # ---- fields, traps, tables, code

    def test_bold_fields(self):
        self.has("fast", '<p class="bf" data-f="the-problem-it-solves"><span class="bf-l">The problem it solves.</span> A team counts')
        self.has("fast", '<p class="bf bf-decide" data-f="deciding-question"><span class="bf-l">Deciding question:</span> Do the widgets')
        self.has("deep", '<p class="bf bf-decide" data-f="rule"><span class="bf-l">Rule.</span> Pick the ')
        self.has("deep", '<p class="bf" data-f="options"><span class="bf-l">Options.</span> </p><ul class="bf-list"><li>One ')
        self.has("deep", '<p class="bf" data-f="decision"><span class="bf-l">Decision.</span> One ')

    def test_traps_list(self):
        self.has("fast", '<ul class="traps"><li class="trap" data-trap="sample-trap-shelf-global"><p class="trap-w">'
                         '<span class="bf-l">Wrong belief</span> A shelf is global.</p><p class="trap-t"><span class="bf-l">Truth</span> A ')
        self.has("fast", '<li class="trap" data-trap="other-trap-limit">')
        self.assertEqual(part("fast")["trapmap"], {"sample-trap-shelf-global": "signals-and-traps"})   # a trap-ref is no definition
        self.has("sheet", '<ul class="traps"><li class="trap"><p class="trap-w">')

    def test_tables(self):
        self.has("fast", '<div class="tw" role="region" tabindex="0" aria-label="Table: Term"><table class="tb tb-words tb-stack"><thead><tr>'
                         '<th scope="col">Term</th>')
        self.has("fast", '<tr><th scope="row" data-th="Term"><a class="term" href="#glossary.crate" data-term="crate">crate</a> (KRAYT)</th>'
                         '<td data-th="Words that go with it"><strong>ship</strong> a crate</td>')
        self.has("fast", '<table class="tb tb-compare"><thead>')
        self.has("fast", '<td data-th="Shelf"><a class="ev" href="#fact.widget-shelf-max-widgets" data-fact="widget-shelf-max-widgets">500 widgets</a></td>')
        self.has("fast", '<table class="tb tb-signals tb-stack">')
        self.has("fast", '<td data-th="The stem says">"widgets must stay on a shelf"</td>')     # no term link in a quoted stem phrase
        self.has("deep", '<table class="tb tb-numbers tb-stack">')
        self.lacks("fast", "table:")

    def test_generated_regions(self):
        self.has("fast", '<div class="mount" data-mount="task" data-id="sample-t01"></div>')
        self.lacks("fast", "Old generated text")
        self.has("calendar", '<div class="mount" data-mount="plan" data-id="a"></div>')
        self.lacks("calendar", "tb-plan")
        self.has("calendar", '<table class="tb tb-log tb-stack">')
        self.has("calendar", '</table></div><div class="mount" data-mount="mistakes"></div>')
        self.has("calendar", '<table class="tb tb-exam-english tb-stack">')
        self.has("calendar", '<table class="tb tb-plain">')

    def test_code(self):
        self.has("deep", '<div class="code" data-lang="json"><button type="button" class="code-copy" data-act="copy">Copy</button>'
                         '<pre tabindex="0"><code>')
        self.has("deep", '<span class="tok-kw">"Shelf"</span>')
        self.has("deep", '<span class="tok-str">"saa-sample-shelf"</span>')
        self.has("deep", '<span class="tok-num">300</span>')
        self.has("deep", '<span class="tok-com"># list the shelves</span>')
        self.has("deep", "with <code>Region</code> in it")
        classes = set(re.findall(r'class="(tok-[a-z]+)"', part("deep")["html"]))
        self.assertLessEqual(classes, {"tok-kw", "tok-str", "tok-num", "tok-com"})

    # ---- links

    def test_fact_links(self):
        self.has("deep", '<a class="ev" href="#fact.widget-shelf-scope" data-fact="widget-shelf-scope">Regional resource</a>')
        self.assertIn("widget-shelf-scope", part("deep")["facts"])
        self.lacks("deep", "widget-nope")
        self.has("deep", "unknown fact")
        msgs = {(w["level"], w["msg"]) for w in part("deep")["warnings"] if w["code"] == "WB03"}
        self.assertIn(("error", "fact widget-nope does not exist"), msgs)
        self.assertIn(("warning", "fact widget-candidate is not verified; the text stays without a link"), msgs)
        self.assertTrue(any(level == "warning" and "without a fact id" in msg for level, msg in msgs))

    def test_term_links_once_per_h2(self):
        html = part("deep")["html"]
        first = html.index('<section class="sub"')
        second = html.index('<section class="sub"', first + 1)
        self.assertEqual(html[first:second].count('data-term="shelf"'), 1)
        self.assertEqual(html[second:html.index('id="sec-numbers-that-decide-answers"')].count('data-term="shelf"'), 0)
        self.assertEqual(html.count('data-term="crate"'), 1)       # "crates" is another word
        self.assertEqual(html.count('data-term="shelf"'), 3)       # once in each H2 that uses the word
        self.has("deep", '<a class="term" href="#glossary.idempotent" data-term="idempotent">idempotent</a>')
        self.assertNotIn('class="term"', "".join(re.findall(r"<h[23][^>]*>.*?</h[23]>", html)))
        self.assertNotIn('class="term"', "".join(re.findall(r"<code>.*?</code>", html, re.S)))
        self.assertNotIn('class="term"', "".join(re.findall(r"<summary>.*?</summary>", html)))

    def test_section_links(self):
        self.has("deep", '<a class="xr" href="#ch.sample.fast.signals-and-traps">Signals and traps</a>')
        self.has("deep", '<a class="xr" href="#ch.sample.fast">the fast file</a>')
        self.has("deep", '<a class="xr" href="#ch.sample.deep.how-it-works">this section</a>')
        self.has("deep", '<a class="xr" href="#ch.sample.quiz">the quiz</a>')
        self.has("deep", '<a class="xr" href="#ch.sample.sources">the sources</a>')
        self.has("deep", '<a class="xr" href="#ch.iam.fast.predict">other</a>')
        self.has("deep", '<a class="xr" href="#glossary">the glossary</a>')
        self.lacks("deep", "no-such-anchor")
        self.lacks("deep", "ch.vpc")
        msgs = {(w["level"], w["msg"]) for w in part("deep")["warnings"] if w["code"] == "WB03"}
        self.assertIn(("error", "section 1-fast.md#no-such-anchor does not exist in chapter sample"), msgs)
        self.assertIn(("warning", "link to chapter vpc, which is not built in this run"), msgs)

    def test_external_links(self):
        self.lacks("deep", "example.com")
        self.has("deep", "See a bad host too.")

    def test_raw_html_and_comments(self):
        self.has("deep", "H<sub>2</sub>O, <kbd>Ctrl</kbd>, and dropped text.")
        self.lacks("deep", "<span>")
        self.lacks("deep", "<!--")
        self.lacks("fast", "<!--")
        self.lacks("deep", "no-fact")
        self.assertTrue(any(w["code"] == "WB09" and "raw HTML dropped" in w["msg"] for w in part("deep")["warnings"]))

    def test_twins(self):
        self.has("fast", 'id="sec-choose-it-or-not" data-sid="choose-it-or-not" data-twins="shelf-capacity crate" data-role="choose"')
        self.has("fast", '<p class="twins"><a class="xr" href="#quiz.sample">Practise this pair</a></p></div></section>')

    # ---- figures

    def test_figure(self):
        self.has("fast", '<figure class="fig" data-fig="sample-hero" data-kind="image"><div class="fig-h"><span class="fig-n">Figure 99.1</span> '
                         '<span class="fig-t"></span></div><div class="fig-s" role="region" tabindex="0" '
                         'aria-label="Figure: A Region frame that contains one shelf, and a team outside"><img class="fig-img"')
        self.has("fast", '<figcaption class="fig-c">A shelf sits inside <a class="ev"')
        self.has("fast", '<ol class="fig-steps"><li>The team creates a shelf.</li><li>The team puts widgets on the shelf.</li></ol>'
                         '<div class="fig-a"><button type="button" data-act="zoom">Zoom</button>'
                         '<button type="button" data-act="describe">Describe</button></div>'
                         '<p class="fig-alt" hidden>A Region frame that contains one shelf, and a team outside</p></figure>')
        meta = part("fast")["figmeta"]["sample-hero"]
        self.assertEqual((meta["n"], meta["claim"], len(meta["steps"])), ("99.1", "A shelf sits inside one AWS Region.", 2))

    def test_figure_numbers_run_through_the_chapter(self):
        self.has("deep", '<span class="fig-n">Figure 99.2</span>')
        self.has("deep", '<figure class="fig" data-fig="sample-inline" data-kind="arch"><div class="fig-h"><span class="fig-n">Figure 99.3</span> '
                         '<span class="fig-t">A shelf in a Region</span>')
        self.has("deep", INLINE_SVG)
        self.assertIn(("WB04", "warning"), self.codes("deep"))       # sample-missing has no drawing

    # ---- generated files and inline fields

    def test_generated_file(self):
        self.assertEqual(part("sheet")["title"], "Sheet")
        self.has("sheet", '<section class="sec" id="sec-amazon-widget-store" data-sid="amazon-widget-store" data-role="sheet" '
                          'data-route="full" data-min="0"><header class="sec-h"><h2>Amazon Widget Store</h2><button')
        self.lacks("sheet", "tbox")
        self.lacks("sheet", "generated by")
        self.assertEqual(part("sheet")["sections"][0]["kind"], 0)
        self.assertEqual(part("sheet")["warnings"], [])

    def test_inline_fields(self):
        self.assertEqual(RESULT["inline"]["why"],
                         'A shelf holds <a class="ev" href="#fact.widget-shelf-max-widgets" data-fact="widget-shelf-max-widgets">'
                         "up to 500 widgets</a>, <strong>not</strong> more. See x &amp; y.")
        self.assertEqual(RESULT["inline"]["empty"], "")

    def test_no_markdown_is_left(self):
        for key in ("fast", "deep", "services", "calendar", "sheet"):
            text = re.sub(r"<[^>]+>", " ", part(key)["html"])
            for mark in ("](", "**", "<!--", "{{"):
                self.assertNotIn(mark, text, f"{key}: {mark}")


class Helpers(unittest.TestCase):
    def test_section_id_equals_lint(self):
        try:
            from saalib import lint
        except Exception:
            self.skipTest("saalib.lint cannot be imported")
        for heading in ("Signals and traps (4 min)", "A subnet is public because of one route (3 min)", "Check (2 min)",
                        "A-list", "Amazon S3 Glacier Deep Archive (1 min)", "  Spaces  around (12 min)", "Über cafe 9"):
            self.assertEqual(site.section_id(heading), lint.section_id(heading), heading)
            self.assertEqual(site.anchor(heading), lint.anchor(heading), heading)
        self.assertEqual(site.section_id("Check (2 min)"), "check")
        self.assertEqual(site.anchor("Check (2 min)"), "check-2-min")

    def test_front_matter(self):
        fm = site.front_matter(FAST)
        self.assertEqual((fm["id"], fm["slug"], fm["title"]), ("99", "sample", "Amazon Widget Store"))
        fm = site.front_matter('---\ndomains: [1, 2]\ntasks: ["1.2", "2.2"]\nminutes: {fast: 20, pass: 65, full: 150}\nxl: true\n'
                               'updated: 2026-10-06\n---\n')
        self.assertEqual(fm, {"domains": [1, 2], "tasks": ["1.2", "2.2"], "minutes": {"fast": 20, "pass": 65, "full": 150},
                              "xl": True, "updated": "2026-10-06"})

    def test_opt(self):
        self.assertEqual(site.derive_opt("LEAST operational overhead"), "ops")
        self.assertEqual(site.derive_opt("MOST cost-effective"), "cost")
        self.assertEqual(site.derive_opt("LOWEST latency"), "perf")
        self.assertEqual(site.derive_opt("MOST highly available"), "resil")
        self.assertEqual(site.derive_opt("MOST secure"), "sec")
        self.assertEqual(site.derive_opt("none"), "none")
        self.assertEqual(site.derive_opt(None), "none")
        self.assertIsNone(site.derive_opt("BEST"))

    def test_script_json(self):
        text = site.script_json({"a": "</script><!--    "})
        self.assertNotIn("<", text)
        self.assertNotIn(" ", text)
        self.assertEqual(json.loads(text), {"a": "</script><!--    "})

    def test_minify_keeps_strings_regex_and_templates(self):
        src = ('(function (SAA) {\n  "use strict";   // a comment\n  /* block\n     comment */\n'
               '  var re = /https?:\\/\\//, s = "a // b  c", t = \'/* x */\';\n'
               '  var h = `<p>\n    two  spaces // kept ${ fn({a: 1}) /* gone */ } </p>`;\n'
               '  var d = a / b / c; // tail\n  return x ? /[/]"/.test(s) : 1;\n})(globalThis.SAA = globalThis.SAA || {});\n')
        out = site.minify_js(src)
        self.assertEqual(out, '(function (SAA) {\n"use strict";\nvar re = /https?:\\/\\//, s = "a // b  c", t = \'/* x */\';\n'
                              'var h = `<p>\n    two  spaces // kept ${ fn({a: 1}) } </p>`;\nvar d = a / b / c;\n'
                              'return x ? /[/]"/.test(s) : 1;\n})(globalThis.SAA = globalThis.SAA || {});\n')
        self.assertEqual(site.minify_js('var a = "open;\n'), 'var a = "open;\n')          # unexpected input comes back unchanged
        self.assertEqual(site.minify_css('/* c */\n.a {\n  color: var(--ink);  /* x */\n  content: "/* kept */";\n}\n\n'),
                         '.a {\ncolor: var(--ink);\ncontent: "/* kept */";\n}\n')

    def test_fact_shard_is_the_longest_service_prefix(self):
        keys = ["s3", "s3-glacier", "vpc", "vpc-peering"]
        self.assertEqual(site.fact_shard("s3-bucket-names", keys), "s3")
        self.assertEqual(site.fact_shard("s3-glacier-vault-lock", keys), "s3-glacier")
        self.assertEqual(site.fact_shard("vpc-peering-transitive", keys), "vpc-peering")
        self.assertIsNone(site.fact_shard("kms-key-rotation", keys))
        self.assertIsNone(site.fact_shard("s3", keys))                   # the key itself is not an id

    def test_must_fail_shard_budget(self):
        build = site.Build()
        build.budgets({"f/s3.json": b"x" * (site.SHARD_CAP + 1), "f/vpc.json": b"x" * (site.SHARD_WARN + 1),
                       "f/kms.json": b"x" * 10, "facts-index.json": b"x" * (60 * site.KB + 1)})
        self.assertEqual(sorted((f["code"], f["file"]) for f in build.errors), [("WB01", "f/s3.json"), ("WB01", "facts-index.json")])
        self.assertEqual([(f["code"], f["file"]) for f in build.warnings], [("WB01", "f/vpc.json")])
        self.assertEqual((site.SHARD_WARN, site.SHARD_CAP), (400 * site.KB, 1500 * site.KB))

    def test_must_fail_search_budgets(self):
        build = site.Build()                      # search/index.json and the search/ shards have their own budgets (1.2)
        build.budgets({"search/index.json": b"x" * (200 * site.KB + 1), "search/vpc.json": b"x" * (800 * site.KB + 1),
                       "search/s3.json": b"x" * (400 * site.KB + 1), "search/kms.json": b"x" * 10})
        self.assertEqual(sorted((f["code"], f["file"]) for f in build.errors), [("WB01", "search/index.json"), ("WB01", "search/vpc.json")])
        self.assertEqual([(f["code"], f["file"]) for f in build.warnings], [("WB01", "search/s3.json")])
        table = {pattern: (warn, fail) for pattern, warn, fail in site.BUDGETS}
        self.assertEqual(table[r"^search/index\.json$"], (None, 200 * site.KB))
        self.assertEqual(table[r"^search/"], (400 * site.KB, 800 * site.KB))
        self.assertFalse([p for p in table if "corpus" in p])                 # search/corpus.json is retired
        self.assertIn("search/corpus.json", site.RETIRED_PATHS)

    def test_must_fail_batch_file_count(self):
        build = site.Build()                      # one shard per fact namespace: the content batch warns before its limit
        build.budgets({f"f/s{i}.json": b"{}" for i in range(site.BATCH_WARN_FILES + 1)})
        self.assertEqual(([f["code"] for f in build.errors], [f["code"] for f in build.warnings]), ([], ["WB01"]))
        build = site.Build()
        build.budgets({f"f/s{i}.json": b"{}" for i in range(site.BATCH_FILES + 1)})
        self.assertEqual(([f["code"] for f in build.errors], build.warnings), (["WB01"], []))
        self.assertEqual((site.BATCH_WARN_FILES, site.BATCH_FILES), (230, 255))

    def test_scope_line(self):
        fact = {"kind": "limit", "qualifiers": {"scope": "per shelf", "default_or_max": "max", "adjustable": False, "condition": ""}}
        self.assertEqual(site.scope_line(fact), "per shelf; maximum; not adjustable.")

    def test_token_css(self):
        tokens = {"themed": {"ink": {"light": "#141C2B", "dark": "#E6EAF2"}, "ground": {"light": "#F2F4F8", "dark": "#0F131B"}},
                  "alias": {"dg-ground": "var(--ground)"}, "static": {"gutter": "16px"}, "runtime": ["dg-w"],
                  "pairs": [["ink", "ground", 4.5], ["ink", "dg-ground", 4.5]]}
        css, findings = site.token_css(tokens)
        self.assertEqual(findings, [])
        self.assertTrue(css.startswith(":root{--ink:#141C2B;--ground:#F2F4F8;--dg-ground:var(--ground);--gutter:16px}\n"))
        self.assertIn('@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ink:#E6EAF2;--ground:#0F131B;color-scheme:dark}}', css)
        self.assertIn(':root[data-theme="dark"]{--ink:#E6EAF2;--ground:#0F131B;color-scheme:dark}', css)
        self.assertEqual(site.undefined_vars(tokens, {"a.css": "p{color:var(--ink);width:calc(var(--dg-w)*1px)}"}), [])
        self.assertEqual([f["item"] for f in site.undefined_vars(tokens, {"a.css": "p{color:var(--nope)}"})], ["nope"])

    def test_must_fail_token_contrast_and_shape(self):
        tokens = {"themed": {"ink": {"light": "#777777", "dark": "#E6EAF2"}, "ground": {"light": "#888888", "dark": "#0F131B"},
                             "half": {"light": "#000000"}},
                  "alias": {"x": "#fff"}, "static": {"y": "rgb(0,0,0)"}, "pairs": [["ink", "ground", 4.5]]}
        _css, findings = site.token_css(tokens)
        self.assertEqual({f["code"] for f in findings}, {"WB06"})
        self.assertEqual(sorted(f["item"] for f in findings), ["half", "ink", "x", "y"])


class Lint(unittest.TestCase):
    def codes(self, name, kind, text):
        return sorted({f["code"] for f in _site_web.lint_text(name, kind, text)})

    def test_clean_sources_pass(self):
        self.assertEqual(self.codes("a.css", "css", ".x{color:var(--ink);height:100%;border:1px solid var(--line)}\n/* #fff 100vh */"), [])
        self.assertEqual(self.codes("js/x.js", "js", 'var a = "#home"; // alert( #fff\nU.set(el, U.h`<p>${t}</p>`);'), [])
        self.assertEqual(self.codes("shell.html", "html", '<div id="a" class="x"></div><link href="https://fonts.googleapis.com/css2">'), [])

    def test_must_fail_each_code(self):
        self.assertEqual(self.codes("a.css", "css", ".x{color:#fff}"), ["WL01"])
        self.assertEqual(self.codes("a.css", "css", ".x{background:rgba(0,0,0,.5)}"), ["WL01"])
        self.assertEqual(self.codes("a.css", "css", ".x{color:white}"), ["WL01"])
        self.assertEqual(self.codes("a.css", "css", ".x{height:100vh}"), ["WL02"])
        self.assertEqual(self.codes("a.css", "css", "@supports (height: 1dvh){.x{height:100dvh}}"), [])
        self.assertEqual(self.codes("a.css", "css", "body{overflow-x:hidden}"), ["WL02"])
        self.assertEqual(self.codes("a.css", "css", ".tw{overflow-x:auto}"), [])
        self.assertEqual(self.codes("js/x.js", "js", "if (confirm('x')) window.print();"), ["WL03"])
        self.assertEqual(self.codes("js/x.js", "js", "Store.consent('prompt'); AICore.speakPrompt(a);"), [])
        self.assertEqual(self.codes("js/x.js", "js", "a.download = 'x'; URL.createObjectURL(b);"), ["WL04"])
        self.assertEqual(self.codes("js/search.js", "js", "URL.createObjectURL(b);"), [])
        self.assertEqual(self.codes("js/x.js", "js", "el.innerHTML = s; el.style.display = 'none';"), ["WL05"])
        self.assertEqual(self.codes("js/util.js", "js", "el.innerHTML = s.s; localStorage.getItem(k); Date.now();"), [])
        self.assertEqual(self.codes("js/x.js", "js", "localStorage.getItem(k); fetch('https://example.com/a');"), ["WL06"])
        self.assertEqual(self.codes("shell.html", "html", '<div id="a"></div><p id="a" class=x></p>'), ["WL07"])
        self.assertEqual(self.codes("js/x.js", "js", 'var t = "65 questions in 130 minutes";'), ["WL08"])
        self.assertEqual(self.codes("js/x.js", "js", 'var t = "</script>";'), ["WL09"])
        self.assertEqual(self.codes("js/x.js", "js", "var t = Date.now(), d = new Date();"), ["WL10"])
        self.assertEqual(self.codes("stubs/claude-stub.js", "stub", "localStorage.x = Date.now();"), [])


def own_errors(result) -> list:
    """Errors that do not come from the web sources of the other implementers (lint, tokens, missing files, page size)."""
    return [f for f in result["errors"] if f["code"] not in ("WB02", "WB06") and not (f["code"] == "WB01" and f["file"] == "index.html")]


class FixtureBuild(unittest.TestCase):
    """The fixture book, built in a sandbox (preview, multi-file and single)."""

    @classmethod
    def setUpClass(cls):
        import sandbox
        cls.sandbox = sandbox
        cls.book = sandbox.make("test-site-build")
        cls.code, cls.result, cls.err = sandbox.run_json(cls.book, "build", "web", "--preview")
        cls.out = cls.book / "_build" / "preview"

    @classmethod
    def tearDownClass(cls):
        cls.sandbox.remove(cls.book)

    def load(self, path):
        return json.loads((self.out / path).read_text(encoding="utf-8"))

    def test_result(self):
        self.assertIsNotNone(self.result, self.err)
        self.assertEqual(own_errors(self.result), [])
        if not self.result["errors"]:
            self.assertIn(self.code, (0, 2))
        self.assertEqual(self.result["chapters"], {"ready": 0, "draft": 1, "planned": 0})
        self.assertEqual(self.result["mode"], "multi")
        self.assertIsNone(self.result["plan"])                       # a preview is never published
        self.assertIn("WB04", {w["code"] for w in self.result["warnings"]})   # the fixture hero has no spec

    def test_files(self):
        for path in ("index.html", "index-dark.html", "index-forced-light.html", "manifest.json", "qindex.json", "c/sample.json",
                     "d/sample.json", "q/mock-preview.json", "q/drill-d2.json", "glossary.json", "plan.json", "facts-index.json",
                     "f/widget.json", "search/index.json", "search/sample.json", "search/book.json", "assets/icons.svg"):
            self.assertTrue((self.out / path).is_file(), path)
        self.assertFalse((self.out / "facts.json").exists())                  # replaced by the shards (2.4)
        self.assertFalse((self.out / "search" / "corpus.json").exists())      # replaced by the search shards (2.4)
        page = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertTrue(page.startswith("<!doctype html>"))
        self.assertIn("<title>SAA-C03 Handbook</title>", page)
        self.assertIn('id="saa-boot"', page)
        self.assertNotIn("{{", re.sub(r"<script\b.*?</script>", "", page, flags=re.S))
        self.assertIn('<html lang="en" data-theme="dark">', (self.out / "index-dark.html").read_text(encoding="utf-8"))
        self.assertIn('href="#ch.sample"', page)

    def test_manifest(self):
        m = self.load("manifest.json")
        self.assertEqual((m["v"], m["title"], m["fixture"], m["date"], m["artifactUrl"]), (1, "SAA-C03 Handbook", True, "2026-10-04", None))
        self.assertEqual(m["build"], self.result["build"])
        self.assertEqual([d["weight"] for d in m["domains"]], [30, 26, 24, 20])
        ch = m["chapters"][0]
        self.assertEqual((ch["slug"], ch["id"], ch["status"], ch["tier"], ch["template"], ch["rev"]), ("sample", "99", "draft", "deep", "deep", 0))
        self.assertEqual(ch["minutes"], {"fast": 16, "pass": 38, "full": 52})
        self.assertEqual(ch["domains"], [2])
        self.assertEqual([f["key"] for f in ch["files"]], ["fast", "deep", "do", "say", "quiz", "sources"])
        self.assertEqual(ch["sections"][0], ["predict", "fast", 2, "fast", 1, "Predict", None, "predict"])
        sub = next(r for r in ch["sections"] if r[0] == "a-shelf-belongs-to-one-region-for-its-whole-life")
        self.assertEqual(sub[1:5] + sub[6:], ["deep", 3, "pass", 3, "how-it-works", "how"])
        self.assertEqual(ch["traps"]["sample-trap-shelf-move"], "fast.signals-and-traps")
        self.assertEqual(ch["counts"], {"q": 4, "core": 2, "cards": 3, "speak": 1, "tasks": 2, "figures": 1})
        self.assertEqual(m["order"], ["sample"])
        self.assertEqual(m["mocks"], [{"n": 1, "slug": "mock-preview", "title": "Preview mock", "file": "q/mock-preview.json",
                                       "count": 65, "minutes": m["mocks"][0]["minutes"], "split": [20, 17, 15, 13], "synthetic": True}])
        self.assertEqual([d["count"] for d in m["drills"]], [2, 4, 2, 2])
        self.assertEqual(m["counts"], {"questions": 4, "coreCards": 2, "speak": 1})
        self.assertIn(["shelf", "shelf"], m["terms"])
        c = (self.out / "c/sample.json").read_bytes()
        d = (self.out / "d/sample.json").read_bytes()
        self.assertEqual((ch["c"], ch["d"]), (len(c), len(d)))
        self.assertEqual(ch["hash"], common.sha256_bytes(c + d)[:8])
        index = (self.out / "facts-index.json").read_bytes()
        self.assertEqual(m["factsIndex"], {"path": "facts-index.json", "bytes": len(index), "sha256": common.sha256_bytes(index),
                                           "shards": 1, "count": 7})

    def test_chapter_files(self):
        c = self.load("c/sample.json")
        self.assertEqual(sorted(c["parts"]), ["deep", "fast"])
        self.assertEqual(c["parts"]["fast"]["title"], "Amazon Widget Store")
        self.assertNotIn("build", c)
        for fid in re.findall(r'data-fact="([^"]+)"', c["parts"]["fast"]["html"] + c["parts"]["deep"]["html"]):
            self.assertIn(fid, c["facts"])
        fact = c["facts"]["widget-shelf-max-widgets"]
        self.assertEqual(sorted(fact), ["changed", "checked", "claim", "kind", "quotes", "scope", "service", "values"])
        self.assertEqual((fact["scope"], fact["changed"], fact["values"]),
                         ("per shelf; maximum; not adjustable.", {"date": "2025-11-19", "was": "200 widgets"}, ["500 widgets", "200 widgets"]))
        self.assertEqual(c["figures"]["sample-hero"]["n"], "99.1")
        self.assertTrue(c["figures"]["sample-hero"]["desc"].startswith("A shelf sits inside one Region"))
        self.assertGreater(c["figures"]["sample-hero"]["w"], 0)
        self.assertIn("widget-shelf-scope", c["secs"]["in-one-breath"]["facts"])
        self.assertIn("predict", c["text"])
        self.assertTrue(all(s["facts"] and s["url"].startswith("https://") for s in c["sources"]))
        d = self.load("d/sample.json")
        q = d["questions"][0]
        self.assertEqual(sorted(q), sorted(["id", "ch", "sec", "pool", "layer", "d", "task", "topics", "concept", "diff", "type", "select",
                                            "qual", "opt", "stem", "kw", "options", "expl_h", "take_h", "twin_h", "say", "facts", "twinOf",
                                            "worked", "keyRev"]))
        self.assertEqual((q["sec"], q["opt"], q["qual"]),
                         ({"slug": "sample", "part": "deep", "sid": "a-shelf-belongs-to-one-region-for-its-whole-life"}, "ops",
                          "LEAST operational overhead"))
        self.assertEqual((d["questions"][2]["qual"], d["questions"][2]["opt"], d["questions"][2]["type"]), (None, "none", "multi"))
        self.assertIn('class="ev"', q["expl_h"])
        self.assertNotIn("](", json.dumps(d))
        self.assertTrue(all(o["why_h"] for x in d["questions"] for o in x["options"]))
        self.assertEqual(sum(1 for o in q["options"] if o["ok"]), q["select"])
        self.assertEqual(q["worked"]["wrongPath"], True)
        task = next(t for t in d["tasks"] if t["id"] == "sample-t02")
        self.assertEqual((task["careful"], task["sec"]["part"]), ("At twice the stated time, run the cleanup and move on.", "deep"))
        self.assertIn('class="ev"', task["steps"][1]["explain_h"])
        self.assertTrue(all("shown" in s and "explain" not in s for s in task["steps"]))
        self.assertNotIn("status", task)
        self.assertNotIn("careful", next(t for t in d["tasks"] if t["id"] == "sample-t01"))
        self.assertEqual((d["speak"][0]["sec"]["part"], d["speak"][0]["pack"]), ("deep", False))
        self.assertEqual(d["cards"][1]["extra_h"].count('class="ev"'), 1)
        for obj in d["questions"] + d["cards"] + d["speak"] + d["tasks"]:
            for fid in re.findall(r'data-fact="([^"]+)"', json.dumps(obj)) + list(obj.get("facts") or []):
                self.assertIn(fid.replace('\\', ''), d["facts"])

    def test_indexes_and_reference_files(self):
        qi = self.load("qindex.json")
        self.assertEqual(qi["q"]["sample-q001"], ["sample", 2, 0, 0, "shelf-capacity", 1, ["storage"]])
        self.assertEqual(qi["q"]["preview-q001"][3], 2)
        self.assertEqual(sorted(qi["wrong"]["sample-q001"]), ["b", "c", "d"])
        self.assertEqual(qi["s"]["sample-s01"][:4], ["sample", "explain", 1, 0])
        mock = self.load("q/mock-preview.json")
        self.assertEqual([sum(1 for q in mock["questions"] if q["d"] == d) for d in (1, 2, 3, 4)], [20, 17, 15, 13])
        self.assertEqual((mock["questions"][0]["id"], mock["questions"][64]["id"], mock["questions"][0]["pool"], mock["questions"][0]["ch"]),
                         ("preview-q001", "preview-q065", "mock", "mock-preview"))
        self.assertEqual(self.load("q/drill-d2.json")["questions"][0]["id"], "sample-q001")
        self.assertEqual(self.load("plan.json")["plans"][0]["days"][0]["tasks"][1]["chapter"], "sample")
        self.assertEqual(self.load("glossary.json")["terms"]["crate"]["say"], "KRAYT")
        index = self.load("facts-index.json")
        shard = (self.out / "f/widget.json").read_bytes()
        self.assertEqual(index, {"v": 1, "count": 7, "shards": {"widget": {"path": "f/widget.json", "bytes": len(shard),
                                 "sha256": common.sha256_bytes(shard), "count": 7}}, "stray": {}})
        widget = self.load("f/widget.json")
        self.assertEqual((widget["v"], widget["service"], len(widget["facts"])), (1, "widget", 7))
        c = self.load("c/sample.json")
        for fid, card in c["facts"].items():                          # the same fact card shape as the chapter files
            self.assertEqual(widget["facts"][fid], card, fid)

    def test_search_index_and_shards(self):
        index = self.load("search/index.json")
        self.assertEqual(sorted(index), ["aliases", "count", "shards", "v"])
        self.assertEqual(index["v"], 1)
        self.assertIsInstance(index["aliases"], dict)
        built = [ch["slug"] for ch in self.load("manifest.json")["chapters"] if ch["status"] != "planned"]
        listed = [row["chapter"] for row in index["shards"]]
        self.assertEqual(listed, ["sample", None])                            # every built chapter, then the book shard
        self.assertLessEqual(set(built), set(listed))
        owner = {"widget": "sample"}                                          # book.json `services` of the fixture
        kinds, total = set(), 0
        for row in index["shards"]:
            self.assertEqual(sorted(row), ["bytes", "chapter", "count", "path"])
            data = (self.out / row["path"]).read_bytes()
            shard = json.loads(data)
            self.assertEqual((row["bytes"], row["count"]), (len(data), len(shard["docs"])), row["path"])
            self.assertEqual((sorted(shard), shard["v"], shard["chapter"]), (["chapter", "docs", "v"], 1, row["chapter"]))
            self.assertEqual(row["path"], f"search/{row['chapter'] or 'book'}.json")
            for route, _title, _heading, kind, _text in shard["docs"]:
                kinds.add(kind)
                if kind == "s":
                    self.assertTrue(route.startswith(f"ch.{row['chapter']}."), route)
                elif kind == "q":
                    self.assertEqual(route, f"quiz.{row['chapter']}")
                elif kind == "g":
                    self.assertIsNone(row["chapter"], route)                   # glossary terms belong to no chapter
                else:
                    self.assertEqual(kind, "f")
                    self.assertEqual(owner.get(route.split(".", 1)[1].split("-", 1)[0]), row["chapter"], route)
            total += row["count"]
        self.assertEqual(kinds, {"s", "g", "f", "q"})
        self.assertEqual(index["count"], total)
        sample = self.load("search/sample.json")
        self.assertIn("ch.sample.fast.predict", [d[0] for d in sample["docs"]])
        self.assertEqual(sum(1 for d in sample["docs"] if d[3] == "f"), 7)    # the facts of the chapter's service
        self.assertEqual(self.result["search"]["shards"], 2)
        self.assertEqual(self.result["search"]["bytes"], (self.out / "search/index.json").stat().st_size)

    def test_build_is_deterministic_and_single_works(self):
        before = {p.relative_to(self.out).as_posix(): common.sha256_file(p) for p in self.out.rglob("*") if p.is_file()}
        code, again, err = self.sandbox.run_json(self.book, "build", "web", "--preview")
        self.assertEqual(again["build"], self.result["build"], err)
        after = {p.relative_to(self.out).as_posix(): common.sha256_file(p) for p in self.out.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        code, single, err = self.sandbox.run_json(self.book, "build", "web", "--preview", "--single")
        self.assertIsNotNone(single, err)
        self.assertEqual((single["mode"], own_errors(single)), ("single", []))
        folder = self.book / "_build" / "preview-single"
        self.assertEqual(sorted(p.name for p in folder.iterdir() if not p.name.startswith(".")),
                         ["index-dark.html", "index-forced-light.html", "index.html"])
        page = (folder / "index.html").read_text(encoding="utf-8")
        m = re.search(r'<script type="application/json" id="saa-inline">(.*?)</script>', page, re.S)
        self.assertIsNotNone(m)
        docs = json.loads(m.group(1))
        self.assertIn("c/sample.json", docs)
        self.assertEqual(len(docs["f/widget.json"]["facts"]), 7)               # every shard and the index are inlined (2.6)
        self.assertEqual(docs["facts-index.json"]["shards"]["widget"]["path"], "f/widget.json")
        self.assertNotIn("facts.json", docs)
        self.assertEqual([r["path"] for r in docs["search/index.json"]["shards"]], ["search/sample.json", "search/book.json"])
        self.assertEqual(docs["search/sample.json"]["chapter"], "sample")
        self.assertNotIn("search/corpus.json", docs)
        self.assertEqual(docs["manifest.json"]["chapters"][0]["slug"], "sample")
        self.assertEqual(docs["manifest.json"]["exports"], [])

    def test_must_fail_out_dir_outside_the_book(self):
        code, _out, err = self.sandbox.run(self.book, "build", "web", "--preview", "--out-dir", "/tmp/saa-site-outside")
        self.assertEqual(code, 4, err)

    def test_must_fail_broken_section_link(self):
        book = self.sandbox.make("test-site-broken-link")
        try:
            self.sandbox.replace_text(book / "99-sample" / "2-deep.md", "1-fast.md#signals-and-traps-2-min", "1-fast.md#no-such-section")
            code, result, err = self.sandbox.run_json(book, "build", "web", "--preview")
            self.assertEqual(code, 1, err)
            self.assertIn("WB03", {f["code"] for f in result["errors"]})
        finally:
            self.sandbox.remove(book)

    def test_must_fail_shard_over_its_cap(self):
        book = self.sandbox.make("test-site-big-shard")
        try:
            def grow(rows):
                big = json.loads(json.dumps(rows[0]))
                big["id"] = "widget-huge-quote"
                big["evidence"][0]["quote"] = "Each shelf can hold widgets. " * (site.SHARD_CAP // 29 + 10)
                rows.append(big)
            self.sandbox.edit_jsonl(book / "data" / "facts" / "widget.jsonl", grow)
            code, result, err = self.sandbox.run_json(book, "build", "web", "--preview")
            self.assertEqual(code, 1, err)
            self.assertIn(("WB01", "f/widget.json"), {(f["code"], f["file"]) for f in result["errors"]})
            self.assertEqual(result["facts"]["largest"][0]["path"], "f/widget.json")
        finally:
            self.sandbox.remove(book)

    def test_only_ready_and_publish_plan(self):
        book = self.sandbox.make("test-site-ready")
        try:
            code, result, err = self.sandbox.run_json(book, "build", "web", "--only-ready")
            self.assertIsNotNone(result, err)
            self.assertEqual(result["chapters"], {"ready": 0, "draft": 0, "planned": 1})
            self.assertEqual(own_errors(result), [])
            if result["errors"]:                      # sources of other implementers may still be missing or fail a check
                self.assertIsNone(result["plan"])
                self.assertFalse(result["written"])
                return
            out = book / "_build" / "site"
            manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual((manifest["chapters"][0]["status"], manifest["chapters"][0]["files"], manifest["mocks"]), ("planned", [], []))
            self.assertNotIn("hash", manifest["chapters"][0])
            self.assertEqual(manifest["chapters"][0]["domains"], [1, 2, 3, 4])
            plan = json.loads((out / "publish-plan.json").read_text(encoding="utf-8"))
            self.assertEqual((plan["title"], plan["icon"], plan["url"], plan["build"]), ("SAA-C03 Handbook", "book", None, result["build"]))
            self.assertEqual([b["name"] for b in plan["batches"]], ["content", "exports"])
            paths = [f["path"] for f in plan["batches"][0]["files"]]
            self.assertIn("index.html", paths)
            self.assertNotIn("publish-plan.json", paths)
            rows = {f["path"]: f for f in plan["batches"][0]["files"]}
            for path in ("facts-index.json", "f/widget.json", "search/index.json", "search/sample.json", "search/book.json"):
                data = (out / path).read_bytes()
                self.assertEqual((rows[path]["bytes"], rows[path]["sha256"], rows[path]["changed"], plan["hashes"][path]),
                                 (len(data), common.sha256_bytes(data), True, common.sha256_bytes(data)), path)
            self.assertNotIn("facts.json", paths)
            self.assertNotIn("search/corpus.json", paths)
            # a republish deletes the files of the old layouts
            self.assertEqual(plan["removed"], ["facts.json", "search/corpus.json"])
            # a planned chapter has no text, but its shard keeps the facts of its service searchable
            index = json.loads((out / "search/index.json").read_text(encoding="utf-8"))
            self.assertEqual([r["chapter"] for r in index["shards"]], ["sample", None])
            sample = json.loads((out / "search/sample.json").read_text(encoding="utf-8"))
            self.assertEqual({d[3] for d in sample["docs"]}, {"f"})
            # after a publish: unchanged shards are marked unchanged; a path that is gone is removed
            published = dict(plan, hashes=dict(plan["hashes"], **{"facts.json": "0" * 64, "f/old.json": "0" * 64}))
            (book / "_build" / "reports").mkdir(parents=True, exist_ok=True)
            (book / "_build" / "reports" / "site-published.json").write_text(json.dumps(published), encoding="utf-8")
            code, again, err = self.sandbox.run_json(book, "build", "web", "--only-ready")
            self.assertIsNotNone(again, err)
            plan2 = json.loads((out / "publish-plan.json").read_text(encoding="utf-8"))
            rows2 = {f["path"]: f["changed"] for f in plan2["batches"][0]["files"]}
            self.assertEqual((rows2["f/widget.json"], rows2["facts-index.json"], rows2["manifest.json"], rows2["index.html"]),
                             (False, False, True, True))
            self.assertEqual(plan2["removed"], ["f/old.json", "facts.json", "search/corpus.json"])
            self.assertFalse((out / "c").exists())
            page = (out / "index.html").read_text(encoding="utf-8")
            self.assertTrue(page.startswith("<title>SAA-C03 Handbook</title>"))
            import re as _re
            # whole tag names only: "<header" is not "<head"
            self.assertIsNone(_re.search(r"<!doctype|<(?:html|head|body)(?![a-z0-9-])", page.lower()))
            # --single: one file in the content batch; every multi-file path, the shards and the index included, is removed (2.7)
            code, single, err = self.sandbox.run_json(book, "build", "web", "--only-ready", "--single")
            self.assertIsNotNone(single, err)
            self.assertEqual(own_errors(single), [])
            if single["errors"]:
                return
            splan = json.loads((book / "_build" / "site-single" / "publish-plan.json").read_text(encoding="utf-8"))
            self.assertEqual(splan["build"], single["build"])
            self.assertEqual([f["path"] for f in splan["batches"][0]["files"]], ["index.html"])
            self.assertLessEqual({"f/widget.json", "facts-index.json", "facts.json", "manifest.json", "f/old.json", "search/index.json",
                                  "search/sample.json", "search/corpus.json"}, set(splan["removed"]))
            self.assertNotIn("index.html", splan["removed"])
        finally:
            self.sandbox.remove(book)


if __name__ == "__main__":
    unittest.main(verbosity=1)
