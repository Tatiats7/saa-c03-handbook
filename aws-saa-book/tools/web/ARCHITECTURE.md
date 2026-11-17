# Web version: architecture contract (version 1.1, 2026-10-04)

Version 1.1 applies the two reviews of version 1.0 (`_build/reports/web-arch-critique-platform.md`, `web-arch-critique-implementer.md`). One line per finding is in `_build/reports/web-arch-fix.md`.

Change of 2026-10-12 (fact shards): the single `facts.json`, which had grown past its 4 MB budget, is replaced by one `f/<service>.json` per fact namespace and a small `facts-index.json`, loaded lazily by `Content.fact`. Sections 1.2, 2.1, 2.2, 2.4, 2.6, 2.7, 3.2, 3.3, 9.1, 9.2 and 9.6 carry the change; the report is `_build/reports/web-facts-shards.md`.

Change of 2026-10-14 (search shards): the single `search/corpus.json` (4.6 MB with 19 ready chapters, about 12 MB expected at 53) is replaced by a small `search/index.json` and one `search/<slug>.json` per chapter, which the page posts to the worker one by one. Sections 1.2, 2.1, 2.4, 2.6, 2.7, 6.6, 9.1 and 9.6 carry the change; the report is `_build/reports/web-search-shards.md`.

This file is the contract for the five implementers of the web version of the SAA-C03 Handbook. `RULINGS.md` and `ARTIFACT-RULES.md` override it. `CONVENTIONS.md` overrides `PRODUCT.md` on Markdown syntax, file layout and section names; this file already applies that. Where this file is silent, `PRODUCT.md` decides. Do not ask questions: when something is not decided here, choose the simplest thing that keeps the interfaces of sections 3 and 10, and say so in your result.

Paths are relative to `aws-saa-book/`. "Slug" is the chapter slug of `data/book.json` (`vpc`); "sid" is a section id (the heading anchor without the time box). All ids match `[a-z0-9-]+`, so `.` separates route tokens.

## 0. Decisions that differ from PRODUCT.md

| Topic | Decision |
|---|---|
| Chapter content | One file `c/<slug>.json` per chapter with one entry per **part** (`fast`, `deep`, `services`, `do`, `say`, `quiz`, `sources`, and the special parts of front and synthesis chapters). The reader shows one part at a time. |
| Generated Markdown | `3-do.md`, `4-say.md`, `5-quiz.md` and `sources.md` are **never parsed**. The app renders those parts from JSON (`tasks`, `speak`, `questions`, `sources`). `sheet.md`, `exam-english.md`, `calendar.md` and `mistakes.md` are parsed like hand files, with the extra rules for generated files in 2.3. |
| Reading routes | `route=fast|pass|full` replaces `core|optional`. The route switch is a per-chapter setting with a global default of `pass`. |
| Callouts, tables, facts | The labels, table kinds and fact-link form of `CONVENTIONS.md` sections D to H. Fact ids are `<service>-<topic>`. |
| Cross-book pages | `#numbers`, `#traps` and `#changed` are aliases of the `sheet` part of chapters 47, 46 and 48. No `c/_*.json` files. |
| Mocks | Two (`mock-exam-1`, `mock-exam-2`). Their length and time come from `mock.json`, never from constants in JavaScript. Until they are written, a `--preview` build has one synthetic mock (2.2); a published build has none and `#mock.<n>` says so. |
| Anki deck | `downloads` does not allow `.apkg` and allows `.zip`. The app offers `exports/SAA-C03-anki.zip` (the `.apkg` inside a zip) when that file exists. Writing it is a request to the owner of `exports.py`; until then the deck is laptop-only and Get files says so. |
| Times | Every stored time is whole seconds from `U.now()`, except fields named `ms` or `activeMs` (milliseconds). |
| Mistake reasons | The five cause codes K, C, W, T, D of `SPEC.json` `lint.cause_codes`. |
| Plan | `data/plan.json`: plans `a`, `b`, `c`, days `d01` to `d19`. No dates in data; the reader sets the date of Day 1. |
| Glossary | Built from `data/terms.json` (there is no `data/glossary.json`). |
| DOM | One chapter part in the DOM at a time; fetched JSON is kept in a memory cache of five files. |
| Preview | `--preview` output works from `file://` only with `--single`. `web selftest` and `web shots` serve the preview from an in-process HTTP server, so the real `fetch` path is tested by one plain command. |
| Speak grading | The PRODUCT prompt, plus per-move scores from `LEARNING.md` 5.4. The page computes the score and the band. |
| Exam numbers in copy | Every exam rule shown by the app (number of questions, minutes, passing score) comes from a verified fact or from `mock.json`. No JavaScript or CSS file holds such a number. |

## 1. Files

### 1.1 Sources (`tools/`)

```
tools/saalib/site.py              A   commands: build web, web selftest, web shots, web lint
tools/helpers/site_md.py          A   uv script: Markdown to HTML (markdown-it-py, Pygments)
tools/web/ARCHITECTURE.md             this file
tools/web/shell.html              B   page template with {{slots}}
tools/web/shell.json              B   app constants that are not AWS facts (section 8.4)
tools/web/tokens.json             B   every colour token, light and dark; contrast pairs
tools/web/css/                    B   10-base.css 20-layout.css 30-prose.css 40-components.css
                                      50-practice.css (C) 60-today.css (D) 70-ai.css (E) 90-phone.css (B)
tools/web/js/                         the modules of section 3.2, concatenated in that order
tools/web/js/search-worker.js     E   published as assets/search-worker.js
tools/web/stubs/claude-stub.js    D   fake window.claude for the preview
tools/web/stubs/skeleton.html     A   emulation of the publish skeleton, slots {{theme}} {{stub}} {{page}}
tools/web/tests/                      harness.mjs (C), test_*.mjs (owner of the module), test_site.py (A),
                                      fixtures/plan.json, drills.json (A; overlay for the fixture book)
```

CSS files are concatenated in name order after the generated token block and the output of `diagram css`. A CSS file is owned by one implementer; nobody adds rules to another owner's file.

### 1.2 Published layout (`_build/site/`)

| Path | Content | Budget (fail above) |
|---|---|---|
| `index.html` | `<title>`, fonts link, `<style>`, static first frame, boot JSON, one inline `<script>`. No doctype, `html`, `head` or `body` tag. | 700 KB (warn 500 KB); raised by the integrator from 400 KB, because the page script alone is about 340 KB (the platform limit is 16 MB) |
| `manifest.json` | section 2.4 (holds the section rows of every chapter, so `Content.section` stays synchronous) | 500 KB (warn 300 KB) |
| `qindex.json` | question index and speak index | 300 KB (warn 200 KB) |
| `c/<slug>.json` | chapter content, one per chapter that is not `planned` | 600 KB each (warn 400 KB) |
| `d/<slug>.json` | questions, cards, speak items, tasks and their facts | 600 KB each |
| `q/<mock-slug>.json`, `q/drill-d<n>.json` | full questions of one mock or one domain drill | 400 KB each |
| `glossary.json`, `plan.json` | lazy reference data | 300 KB, 60 KB |
| `facts-index.json` | the index of the fact shards (2.4), read before the first shard | 60 KB |
| `f/<service>.json` | the verified facts of one fact namespace (`data/facts/<service>.jsonl`), loaded lazily (2.4) | 1.5 MB each (warn 400 KB) |
| `search/index.json` | the index of the search shards (2.4): the aliases and one row per shard, read before the first shard | 200 KB |
| `search/<slug>.json` | the search docs of one chapter (2.4); `search/book.json` holds the docs of no chapter | 800 KB each (warn 400 KB) |
| `assets/icons.svg` | sprite of the icons that the built diagrams use | 400 KB |
| `assets/search-worker.js` | the worker | 60 KB |
| `exports/*` | copied from `exports/` when present: `.pdf`, `.txt`, `.zip` only (never `.apkg`) | 15 MB each |
| `publish-plan.json` | not published (section 2.7) | |

Global limits, all blocking: every text file under 16 MB; every binary file under 15 MB; batch `content` (everything except `exports/`) at most 255 files and 64 MB; batch `exports` the same; the whole site at most 511 files and 256 MB. With 53 chapters the content batch has about 120 files, plus one shard per fact namespace (32 on 2026-10-12; about 120 to 130 when every in-scope service has verified facts). The build therefore warns (`WB01`) when a batch holds more than 230 files. The search shards add one file per chapter that has docs (28 on 2026-10-14, at most 54), so with every chapter built the content batch passes 255 files. Before that, the shards move to a batch of their own (`facts`, published right after `content`); that split is not built yet.

Fact shards: the warning level of 400 KB is the one of the content files; the cap of 1.5 MB is set from the largest shard, `f/s3.json` (597 facts, 600 KB on 2026-10-12), and leaves room for about 1,490 facts in one namespace. A namespace that reaches the cap is split into two namespaces (for example `s3` and `s3-storage-classes`); the prefix rule of 2.4 needs no other change. `facts.json` (one file of every fact, 4 MB) is retired: no build writes it and `publish-plan.json` lists it in `removed` (2.7).

Search shards: the levels are those of the content files with half the fact-shard cap (warn 400 KB, cap 800 KB); the largest shard, `search/route53.json`, was 272 KB on 2026-10-14 (most of it is the claims of its 785 facts). `search/corpus.json` (one file of every search doc) is retired like `facts.json`.

`--single` writes one file, `_build/site-single/index.html` (budget 15 MB), with every JSON file above inlined (section 2.6) and no `exports/`.

## 2. The build (`saalib/site.py`, implementer A)

### 2.1 Commands

`site.py` exposes `register(subparsers)`. The names `build` and `web` are command groups. Another module (`exports.py`) also adds to `build`, so both use this function, copied verbatim (do not edit `common.py`):

```python
def group(subparsers, name, help_text):
    parser = subparsers.choices.get(name) if getattr(subparsers, "choices", None) else None
    if parser is None:
        parser = subparsers.add_parser(name, help=help_text)
        parser._saa_actions = parser.add_subparsers(dest=name + "_cmd")
    return parser._saa_actions
```

| Command | Does |
|---|---|
| `build web [--only-ready] [--single] [--preview] [--out DIR]` | Builds the site. Default output `common.BUILD / "site"`; with `--single`, `site-single`; with `--preview`, `preview` (or `preview-single`). `--out` replaces the folder and must be inside the book (exit 4). Runs `web lint` first. |
| `web lint` | The source lint of section 9.5 over `tools/web/`. Exit 1 on a finding. |
| `web selftest [--single] [--only render|phone|sim|hot|node]` | Builds a preview of the current book into `common.TMP / "web-selftest"`, serves it, runs the routes of section 9.2 in headless Chrome, runs every `tools/web/tests/test_*.mjs` with `node`, prints one result object. |
| `web shots [--out DIR] [--only NAME,...] [--single]` | Builds the same preview and writes the screenshots of section 9.3 to `common.BUILD / "shots"` plus `sheet.png`. |

All take the common options and print through `common.emit`. Exit codes follow `TOOLS.md` section 0. JSON of `build web`:

```json
{"ok": true, "out": "aws-saa-book/_build/site", "build": "3fa9c1d2e0", "mode": "multi",
 "chapters": {"ready": 3, "draft": 1, "planned": 49}, "files": 118, "bytes": 5234567,
 "largest": [{"path": "c/vpc.json", "bytes": 381220}], "preview": false, "written": true,
 "facts": {"count": 4195, "shards": 32, "largest": [{"path": "f/s3.json", "bytes": 600096}]},
 "search": {"path": "search/index.json", "bytes": 3424, "shards": 28, "count": 14214,
            "largest": [{"path": "search/route53.json", "bytes": 271548}]}, "errors": [], "warnings": [],
 "plan": "aws-saa-book/_build/site/publish-plan.json"}
```

`facts` gives the number of facts, the number of shards and the three largest shards; `search` gives the size of `search/index.json`, the number of search shards and docs, and the three largest search shards. `written` is false when errors kept the build from writing its folder (a `--preview` build always writes).

Findings have the shape of `TOOLS.md` rule 7, with these codes: `WB01` budget; `WB02` source lint; `WB03` a link or section reference that does not resolve; `WB04` a diagram without a spec (warning; the standalone SVG is embedded as an image); `WB05` a generated or required part is missing (warning for a draft chapter, error for a ready one); `WB06` token contrast; `WB07` a data file fails its schema; `WB08` the helper failed (exit 5 when `uv` cannot run); `WB09` a construct that the mapping table does not know, rendered as plain Markdown (warning); `WB10` an exam fact of the shell is not verified (warning; that entry is left out).

Severities. **Errors** (exit 1): `WB01` above the fail budget; `WB02` (except a missing source file in a `--preview` build, 2.5); `WB06`; `WB07`; `WB03` when the target chapter is built in this run and the section does not exist, or when the fact id does not exist; `WB05` for a ready chapter. **Warnings** (exit 2): `WB01` above the warn budget; `WB03` when the target chapter is not built in this run (`planned`, or `draft` under `--only-ready`) or when the fact exists and is not verified (in both cases the link text stays, without a link); `WB04`; `WB05` for a draft chapter; `WB09`; `WB10`. `WB08` exits 5.

Read every path through `common.X` at call time. Never write outside `common.BUILD`. The build is deterministic: the same inputs give the same bytes; no timestamps anywhere.

### 2.2 Steps

1. `load()`: `common.load_book()`, `SPEC.json`, the ledger files, `data/terms.json`, `data/plan.json`, `data/drills.json`, `data/<NN-slug>/mock.json` of every chapter with tier `mock`, every `data/facts/*.jsonl` (status `verified` only; the file stem is the fact namespace, which names the shard of each fact, 2.4), `_build/registry/exam-guide.json`. (`data/exam-english.json` is not read; the `words` part comes from `exam-english.md`.) When `book.fixture` is true and `data/plan.json` or `data/drills.json` is missing, use the file of `tools/web/tests/fixtures/`.
   Mocks: a mock chapter enters `manifest.mocks` only when its `mock.json` exists and validates; otherwise `WB05` and no entry. In a `--preview` build whose `mocks` list is then empty (fixture or not), synthesise one mock with `n` 1, slug `mock-preview`, `synthetic: true`: 65 copies of ready chapter questions (cycled in id order) with ids `preview-q001` to `preview-q065`, `pool` `mock`, `ch` `mock-preview`, and `d` overwritten in order: the first 20 get 1, the next 17 get 2, the next 15 get 3, the last 13 get 4; `minutes` is `shell.json` `previewMockMinutes` (a preview value, not an exam fact) and `split` is `[20, 17, 15, 13]`. Never in a build without `--preview`.
2. `status(ch)`: `ready` when the ledger chapter status is `ready`; else `draft` when `<dir>/1-fast.md` exists; else `planned`. With `--only-ready`, `draft` becomes `planned`.
3. `validate()`: every data file of a non-planned chapter against its schema (`saalib.schemas.validate`).
4. `diagrams()`: for each diagram id embedded in a hand file: `diagram.pipeline.check_id(id)`; when a scene exists, `diagram.svg.render_inline(scene, spec, icons)` and `pipeline.caption(spec)`. Collect `diagram.svg.used_icons(scene)`.
5. `render()`: one call of the helper for the whole book (section 2.3).
6. `data()`: the files of section 2.4.
7. `shell()`: fill `shell.html` (section 2.5).
8. `budgets()`, then `publish_plan()` (section 2.7).

Only items with `status: ready` are emitted (questions also need `verification.status` `pass` or `edited-pass`), the rule of `sync`. One exception: in a draft chapter of a `--preview` build, items with status `verified` or `ready` are emitted (questions still need `verification.status` `pass` or `edited-pass`), so that a pilot chapter can be tested before `finalize`. Items with pool `mock` go only to `q/`, pool `drill` only to `d/` and the drill files.

Section ids: `site.py` has its own `section_id(heading)` and `anchor(heading)` with the rule of `SPEC.json` `headings`. `test_site.py` asserts that they equal `lint.section_id` and `lint.anchor` when `saalib.lint` can be imported.

### 2.3 The helper and the Markdown-to-HTML mapping

`tools/helpers/site_md.py` is a PEP 723 script (`requires-python = ">=3.12"`, `markdown-it-py` and `pygments` pinned to exact versions on first run). Call: `uv run --script aws-saa-book/tools/helpers/site_md.py --job FILE --out FILE`, both under `common.TMP / "site"`.

Job: `{"chapters": [{"slug", "id", "dir", "parts": [{"key", "path"}]}], "inline": {"<key>": "<text>"}, "ctx": {"facts": {id: {"service", "displays": []}}, "terms": [{"id", "cs": true|false, "forms": [term, short, aliases...]}], "chapters": {"<NN-slug>": "<slug>"}, "part_of_file": {"1-fast.md": "fast", ...}, "sections": {"<slug>": {"<file>": {"<anchor>": "<sid>"}}}, "diagrams": {id: {"html", "kind", "title", "claim", "steps": []}}, "callouts": SPEC callouts.labels, "prompts": [...], "bold_fields": [...], "table_kinds": [...]}}`.

Result: `{"parts": {"<slug>/<key>": {"html", "sections": [...], "facts": [ids], "terms": [ids], "figures": [ids], "traps": [ids], "text": [{"sid", "text"}], "warnings": []}}, "inline": {"<key>": "<html>"}}`.

Parser: `MarkdownIt("commonmark", {"html": True}).enable(["table", "strikethrough"])`. Front matter is cut before parsing. The component pass works on the token stream. Every text node is escaped by the renderer; raw HTML other than `details`, `summary`, `br`, `sub`, `sup`, `kbd` and comments is dropped with `WB09`.

Part keys by file: `1-fast.md` `fast`; `2-deep.md` `deep`; `2-services.md` `services`; `calendar.md` `calendar`; `mistakes.md` `mistakes`; `sheet.md` `sheet`; `exam-english.md` `words`.

Generated Markdown files (`sheet.md`, `exam-english.md`: no front matter, H2 headings without a section flag or time box). The line `<!-- generated by saa.py; do not edit -->` is dropped. The part title is the H1 text after the last `: ` with the first letter in upper case, else the manifest `files[].title`. An H2 without a flag gives `data-role="sheet"`, `data-route="full"`, `data-min="0"` and no `.tbox`; its section row has kind `0` (a link target, never counted in progress).

Synthetic parts (no Markdown): `do` when emitted tasks of type `try` or `lab` exist; `say` when emitted speak items exist; `quiz` when emitted questions of pool `chapter` exist (mock chapters: always, it opens the mock); `sources` always.

**Mapping table.** `…` is rendered inline content. Class names are final.

| Construct (CONVENTIONS) | HTML |
|---|---|
| H1 | Dropped. The part title is data (`parts[].title`). |
| H2 + section flag | `<section class="sec" id="sec-<sid>" data-sid="<sid>" data-role="<role>" data-route="<route>" data-min="<n>" [data-service]><header class="sec-h"><h2>Text without time box</h2><span class="tbox">4 min</span><button type="button" class="sec-ask" data-act="ask" hidden>Ask</button></header><div class="sec-b">…</div></section>`. The section ends at the next H2. |
| H3 in a `how` section, or an H3 with a time box | `<section class="sub" id="sec-<sid>" data-sid data-route="pass|full" data-min><header class="sub-h"><h3>…</h3><span class="tbox">3 min</span></header><div class="sub-b">…</div></section>`. `data-route` is `pass` when the H3 flag is present, else the route of its H2. |
| Other H3 (`Traps`, `A-list`, `Shelf or crate`) | `<h3 class="h3" id="sec-<sid>" data-sid>…</h3>` (no wrapper). Its section row has kind `0`: a link target only, never tracked or counted. |
| Paragraph; lede | `<p>…</p>`. `<p class="lede">…</p>` for the first plain paragraph that is a direct child of `.sec-b` or `.sub-b` and comes before any other block (prompt, bold field, callout, table, figure, mount); a section that starts with another block has no lede. |
| Callout `> **Label:** …` | `<aside class="co co-<key> hue-<hue>" data-label="<Label>"><p class="co-l">Label</p><div class="co-b">…</div></aside>`. Keys: `key` (Key fact), `signal`, `trap`, `heur`, `say`, `try`, `startup`, `cost`, `cleanup`, `careful`, `changed`. `hue` from `SPEC.json`. A trap comment adds `data-trap`; a task comment adds `data-task` and the link to `3-do.md` becomes `#ch.<slug>.do.<task id>`. |
| Changed recently | `<aside class="co co-changed hue-neutral" data-date="2025-11-19" data-status="examinable|not-yet"><p class="co-l">Changed recently <time>2025-11-19</time></p><p class="chg-what">…</p><dl class="chg"><dt>Old</dt><dd>…</dd><dt>Now</dt><dd>…</dd><dt>The exam probably expects</dt><dd>…</dd><dt>Status</dt><dd><span class="pill">examinable</span></dd></dl></aside>` |
| AWS quote block | `<figure class="awsq"><blockquote>"…"</blockquote><figcaption><a class="ext" href="https://…" target="_blank" rel="noopener">Title</a></figcaption></figure>` |
| Other blockquote | `<blockquote>…</blockquote>` and `WB09`. |
| Prompt paragraph | `<div class="pr pr-<key>" data-pid="<key>-<n>" [data-gist="1"]><p class="pr-q"><span class="pr-l">Check 1</span> …</p>` + the reveal that follows + `</div>`. Keys: `predict`, `check`, `recap`, `faq`, `stop`, `bug`, `pic`. `data-pid` for unnumbered prompts is `<key>-<index in the part>`. `.pr` holds the prompt paragraph and every block up to and including the next `details` (a Spot the bug prompt has a code block in between); it holds only the paragraph when the next block is another prompt or a heading, or when no `details` follows before them (Predict). With `data-gist`, the label reads "Predict 1 · careful". |
| Reveal `Answer` / `Show the picture` | `<details class="rv rv-answer|rv-picture"><summary>Answer</summary><div class="rv-b">…</div></details>` |
| Reveal `Go deeper: T` | `<details class="rv rv-deeper"><summary><span class="rv-l">Go deeper</span> T</summary><div class="rv-b">…</div></details>` |
| Bold field | `<p class="bf" data-f="<slug of label>"><span class="bf-l">Decision.</span> …</p>`. A list that follows `Options.`, `Stem signals.` or `If the question adds.` gets `class="bf-list"`. |
| Traps list item | `<li class="trap" data-trap="<id>"><p class="trap-w"><span class="bf-l">Wrong belief</span> …</p><p class="trap-t"><span class="bf-l">Truth</span> …</p></li>` inside `<ul class="traps">`. A `trap-ref` comment gives `data-trap` too. |
| Table with kind | `<div class="tw" role="region" tabindex="0" aria-label="Table: <first header>"><table class="tb tb-<kind> [tb-stack]"><thead>…</thead><tbody>…</tbody></table></div>`; every `td` has `data-th="<header text>"`. `tb-stack` on `signals`, `words`, `pairs`, `glance`, `breaks`, `numbers`, `log`, `plan`, `exam-english`. In a `words` table, cell 1 is `<th scope="row">` with the term link. |
| Deciding question, Rule | Bold field with `data-f="deciding-question"` or `rule`, class `bf bf-decide`. |
| Code fence | `<div class="code" data-lang="bash"><button type="button" class="code-copy" data-act="copy">Copy</button><pre tabindex="0"><code>…</code></pre></div>`. Pygments tokens map to four classes: `tok-kw` (Keyword, Name.Tag, Name.Builtin), `tok-str` (String), `tok-num` (Number), `tok-com` (Comment); others are plain text. |
| Inline code | `<code>…</code>` |
| Fact link | `<a class="ev" href="#fact.<fact id>" data-fact="<fact id>">link text</a>`; the id is added to the part's `facts`. Unknown or unverified fact: plain text and `WB03`. |
| Glossary link, and the first use of a term per H2 | `<a class="term" href="#glossary.<id>" data-term="<id>">text</a>`. Auto-link: match the `forms` of the job (`term`, `short` and `aliases`; former names are not forms), longest first, case-sensitive when `cs` is true (kind `aws-name`), never inside headings, links, code, labels or `summary`. |
| Link to a section | Same file `#a`, same chapter `2-deep.md#a`, other chapter `../10-vpc/1-fast.md#a`: `<a class="xr" href="#ch.<slug>.<part>.<sid>">`. Without anchor: `#ch.<slug>.<part>`. Links to `4-say.md`, `5-quiz.md`, `3-do.md`, `sources.md`: `#ch.<slug>.say`, `.quiz`, `.do`, `.sources` (an anchor on them is dropped). `exam-english.md`, `sheet.md`, `calendar.md`, `mistakes.md`, `2-services.md` resolve through `part_of_file` like any hand file. `../glossary.md` without an anchor: `#glossary`; with an anchor: the glossary link of the row above. `../facts/<service>.md` without an anchor: plain text and `WB03`. Unresolved: plain text and `WB03` (severity in 2.1). |
| External link | `<a class="ext" href target="_blank" rel="noopener">` (allowed hosts only). |
| Diagram embed + `**Figure.**` + step list | `<figure class="fig" data-fig="<id>" data-kind="<kind>"><div class="fig-h"><span class="fig-n">Figure <chapter id>.<n></span> <span class="fig-t">spec title</span></div><div class="fig-s" role="region" tabindex="0" aria-label="Figure: <alt>">inline SVG (one `<svg>`, or for a `compare` diagram `<div class="dg-cmp">` with one `<svg>` per `.dg-cmp-p` panel), or `<img class="fig-img" alt style="--dg-w:<width of the standalone SVG>" src="data:image/svg+xml;base64,…">` when there is no spec</div><figcaption class="fig-c">caption …</figcaption><ol class="fig-steps">…</ol><div class="fig-a"><button type="button" data-act="zoom">Zoom</button><button type="button" data-act="describe">Describe</button></div><p class="fig-alt" hidden>alt</p></figure>` |
| `<!-- task:start id=X -->` region | `<div class="mount" data-mount="task" data-id="X"></div>` |
| `<!-- plan:start id=a -->` region | `<div class="mount" data-mount="plan" data-id="a"></div>` (the app draws the live checklist) |
| `<!-- exam-english:start group=G -->` region | The generated table, emitted with kind `exam-english` whatever kind the generated Markdown prints (it prints `plain`). |
| `log` table of `mistakes.md` | `<div class="mount" data-mount="mistakes"></div>` after the example table. |
| Comments | `gist-trap` sets `data-gist` on the prompt (label "Predict 1 · careful"); `twins: a b` sets `data-twins="a b"` on the section, and the build appends `<p class="twins"><a class="xr" href="#quiz.<slug>">Practise this pair</a></p>` to the section body when the chapter has a `quiz` part; `trap`, `task` as above; all others (`no-fact`, `needs-*`, `xref`) are dropped. Every `data-trap` id is also recorded with its part and nearest sid for the manifest `traps` map (2.4). |
| `<br>`, `sub`, `sup`, `kbd`, lists, `strong` | Standard HTML. |

`inline` job entries (question `explanation`, `takeaway`, `twin`, option `why`; card `extra`; task step `explain`) are rendered as inline HTML with fact links only. In emitted JSON these fields carry the suffix `_h`. **Every field with `_h` is safe HTML made by the build; every other string is plain text that JavaScript must escape.**

Each `sections` entry: `{"sid", "title", "kind": 2|3|0, "role", "route", "min", "parent": sid|null, "service": key|null, "facts": [ids], "terms": [ids], "figures": [ids], "traps": [ids]}`. `kind` is `2` for an H2 section (`.sec`), `3` for a tracked subsection (`.sub`), `0` for a plain H3 or an unflagged H2 of a generated file. The lists hold what is linked or embedded inside that section (a kind 2 entry does not repeat what its kind 3 children hold; a kind 0 heading has empty lists, its content belongs to its parent). `text` is the plain text of each section for search and for "Ask about this section" (tables as `a | b | c` rows, reveals included, code excluded).

### 2.4 Emitted JSON

`manifest.json`:

```json
{"v": 1, "build": "3fa9c1d2e0", "title": "SAA-C03 Handbook", "date": "2026-10-04", "fixture": false,
 "artifactUrl": null,
 "domains": [{"id": 1, "title": "Design Secure Architectures", "weight": 30}],
 "parts": [{"id": "identity", "title": "Identity and governance"}],
 "chapters": [{"slug": "vpc", "id": "10", "title": "Amazon VPC", "part": "networking", "tier": "deep",
   "template": "deep", "status": "ready", "rev": 2, "hash": "a1b2c3d4", "domains": [1, 2, 3],
   "minutes": {"fast": 20, "pass": 65, "full": 150},
   "files": [{"key": "fast", "title": "Fast"}, {"key": "deep", "title": "In depth"}, {"key": "do", "title": "Do"},
             {"key": "say", "title": "Say it"}, {"key": "quiz", "title": "Quiz"}, {"key": "sources", "title": "Sources"}],
   "sections": [["predict", "fast", 2, "fast", 1, "Predict", null, "predict"]],
   "traps": {"vpc-trap-nat-az": "fast.signals-and-traps"},
   "counts": {"q": 18, "core": 9, "cards": 20, "speak": 4, "tasks": 3, "figures": 5},
   "c": 381220, "d": 96110}],
 "order": ["start-here", "how-the-exam-asks", "aws-map", "iam", "vpc"],
 "mocks": [{"n": 1, "slug": "mock-exam-1", "title": "Mock exam 1", "file": "q/mock-exam-1.json", "count": 65,
            "minutes": 130, "split": [20, 17, 15, 13], "synthetic": false}],
 "drills": [{"id": "drill-d1", "domain": 1, "title": "Domain 1 drill", "file": "q/drill-d1.json", "count": 20}],
 "aliases": {"numbers": "ch.numbers.sheet", "traps": "ch.signals-traps.sheet", "changed": "ch.changed-recently.sheet"},
 "terms": [["nat-gateway", "NAT gateway"]],
 "examFacts": {"count": {"id": "exam-question-count", "text": "65 questions"}, "minutes": {"id": "…", "text": "…"},
               "pass": {"id": "…", "text": "…"}, "esl": {"id": "…", "text": "…"}},
 "factsIndex": {"path": "facts-index.json", "bytes": 4611, "sha256": "e38f…", "shards": 32, "count": 4195},
 "exports": [{"name": "SAA-C03-final-week.pdf", "path": "exports/SAA-C03-final-week.pdf", "bytes": 912345, "repo": "aws-saa-book/exports/SAA-C03-final-week.pdf"}],
 "counts": {"questions": 640, "coreCards": 350, "speak": 96}}
```

- `sections` rows are `[sid, part, kind, route, minutes, title, parent, role]`, with `kind` as in 2.3: `2` an H2 section, `3` a tracked subsection, `0` a plain heading (a link target only). Rows are in document order. `Content.section` returns a row as an object (3.2). A planned chapter has `files: []`, `sections: []`, `traps: {}` and no `hash`; its `domains` are the first digits of the registry `tasks` and its `minutes` the template minutes of `SPEC.json`.
- `traps` maps each trap id found in the chapter's prose to `<part>.<sid>`, so that an option or a card with `trap` can link to `#ch.<slug>.<part>.<sid>`.
- `order` is the study order: chapter slugs in order of first appearance in plan `a` of `plan.json`, then the rest in book order.
- `status` values: `planned`, `draft`, `ready`. `rev` is the ledger `rev` (0 when absent). `hash` is the first 8 hex characters of the SHA-256 over the bytes of `c/<slug>.json` followed by the bytes of `d/<slug>.json` (an absent file counts as empty). Neither file holds `build`, so `hash` changes only when that chapter changes.
- `build` is the first 10 hex characters of the SHA-256 over the sorted `path:sha256` lines of every emitted file except `manifest.json`, `index.html` and `publish-plan.json`, plus two lines `css:<sha256 of the concatenated CSS text>` and `js:<sha256 of the concatenated page script>`. Only `manifest.json` and the boot JSON of `index.html` carry `build`; no `c/`, `d/` or `q/` file does. Attempt and exam documents take their `build` from `SAA.state.build`.
- `date` is the latest `updated` front-matter date of the built chapters, else `book.snapshot_date`. Never the clock.
- `artifactUrl` is the `url` of `common.REPORTS / "site-published.json"`, else `null` (2.7).
- `factsIndex` describes `facts-index.json`: path, bytes, SHA-256, number of shards, number of facts. `Content` finds the index through it; a manifest refresh with a new `sha256` drops the index and every loaded shard (3.2).
- `examFacts` come from the fact ids of `shell.json` `examFacts` (an object with the keys `count`, `minutes`, `pass`, `esl`); `text` is the first `display`. A key whose fact does not exist or is not verified is left out (`WB10`). Code finds an exam fact by key, never by position or id.

`c/<slug>.json`:

```json
{"v": 1, "slug": "vpc",
 "parts": {"fast": {"title": "Amazon VPC", "html": "<section class=\"sec\" …>"}, "deep": {"title": "…", "html": "…"}},
 "facts": {"vpc-natgw-bandwidth": {"service": "vpc", "claim": "…", "values": ["up to 100 Gbps"], "scope": "per NAT gateway; maximum",
   "quotes": [{"q": "…", "title": "NAT gateways", "url": "https://docs.aws.amazon.com/…", "header": null}],
   "checked": "2026-10-04", "changed": {"date": "2025-11-19", "was": "…"}, "kind": "limit"}},
 "figures": {"vpc-hero": {"n": "10.1", "title": "…", "alt": "…", "desc": "claim. 1. step one. 2. step two.", "w": 444}},
 "sources": [{"title": "NAT gateways", "url": "https://…", "checked": "2026-10-04", "facts": ["vpc-natgw-bandwidth"]}],
 "secs": {"<sid>": {"facts": ["vpc-natgw-bandwidth"], "terms": ["nat-gateway"], "figs": ["vpc-hero"]}},
 "text": {"<sid>": "plain text of the section"}}
```

The fact object is the **fact card shape** used everywhere (`c`, `d`, `q`, `f`). `scope` is the Scope line of `TOOLS.md` 5.8. `text` and `secs` (the per-section lists of the helper; sections with three empty lists are left out) are used by Ask and are not rendered. `figures[id].w` is the natural width in pixels.

`d/<slug>.json`: `{"v": 1, "slug", "questions": [Q], "cards": [C], "speak": [S], "tasks": [T], "facts": {id: fact card}}`.

- **Q**: `{"id", "ch": slug, "sec": {"slug", "part", "sid"}|null, "pool", "layer", "d": 1..4, "task", "topics": [], "concept", "diff", "type": "single"|"multi", "select", "qual": "LEAST operational overhead"|null, "opt": "cost"|"ops"|"perf"|"resil"|"sec"|"none"|null, "stem", "kw": [], "options": [{"id", "text", "ok": true|false, "why_h", "concept", "trap"}], "expl_h", "take_h", "twin_h", "say", "facts": [], "twinOf", "worked": {"steps": [], "wrongPath"}|null, "keyRev"}`. `opt` is derived from the qualifier, compared in lower case, by the first match in this table: `cost` (cost, cheap, price); `ops` (operational, overhead, effort, management, administrative); `perf` (performance, latency, fast, throughput, scal, speed, quick); `resil` (available, availability, resilient, fault, durable, recovery, downtime, reliab, outage, failure); `sec` (secure, security). A question without a qualifier has `none`. A qualifier that matches no word gives `null`, and the stem-first step then skips the chip question.
- **C**: `{"id", "type", "deck", "front", "back", "extra_h", "facts", "term", "word", "speak", "sec", "trap", "changed"}`, with `sec` resolved as in Q. Only hand cards, word cards and say cards are emitted (7.6).
- **S**: the speak item of `speak.schema.json` without `status`, `rev` (it keeps `pack`), plus `"sec"` resolved as in Q.
- **T**: the task of `task.schema.json` without `status`, `rev`, `sources`, with `steps[].explain_h`, `steps[].shown` (the command as `sync` prints it, with the capture wrapper), `"sec"` resolved as in Q, and for Try and Lab `"careful"`: the text of `SPEC.json` `tasks.stop_rule`. A Lab keeps its `template` path (shown as a laptop path, section 10).

`q/<mock-slug>.json`: `{"v": 1, "slug", "minutes": 130, "split": [20, 17, 15, 13], "questions": [Q in manifest order], "facts": {...}}`. `q/drill-d<n>.json`: `{"v": 1, "id", "domain", "title", "questions": [Q], "facts": {...}}`.

`qindex.json`: `{"v": 1, "q": {"<id>": [slug, domain, layer (0 core, 1 extended), pool (0 chapter, 1 drill, 2 mock), concept, keyRev, [topics]]}, "wrong": {"<id>": {"<option id>": concept}}, "s": {"<speak id>": [slug, kind, pass_route (0|1), pack (0|1), prompt]}}`. `wrong` lists the concept of every wrong option, for confusion pairs. `s` is the speak index of every emitted speak item (about 100 entries), so `#speak` needs no `d/` file to list them.

`glossary.json`: `{"v": 1, "terms": {"<id>": {"term", "say": respelling|null, "meaning", "with": [collocations], "not": [do_not_confuse], "short", "facts": []}}}`.

`plan.json`: `data/plan.json` as it is, with each task's `chapter` replaced by the slug.

`f/<service>.json` (a **fact shard**): `{"v": 1, "service": "s3", "facts": {id: fact card}}`, one file per fact namespace (the stem of `data/facts/<service>.jsonl`) with every verified fact of that namespace, ids in sorted order. A namespace that does not match `[a-z0-9][a-z0-9-]*` is a `WB07` error and its facts are left out.

`facts-index.json`: `{"v": 1, "count": 4195, "shards": {"s3": {"path": "f/s3.json", "bytes": 600096, "sha256": "…", "count": 597}}, "stray": {"<fact id>": "<service>"}}`. The shard of a fact id (the same rule in `site.fact_shard` and `Content.factService`): `stray[id]` when it is listed and names a shard; else the longest shard key `k` such that the id starts with `k-` (fact ids are `<service>-<topic>`, so `s3-glacier-vault-lock` goes to `s3-glacier`, not `s3`); else none. `stray` lists every fact whose namespace differs from what the prefix rule gives (an id that does not start with its namespace, or a fact `s3-glacier-x` kept in `s3.jsonl`); it was empty on 2026-10-12.

Shards are loaded only for a fact that no open file has registered: a deep link to `#fact.<id>`, a fact result of search (search itself reads the claim from the search shards), or a chip whose card is not in the open file. The `c/`, `d/` and `q/` files keep the cards of the facts they link, so reading a chapter or answering a quiz loads no shard. `facts.json` is retired (1.2).

Search docs: `[route, chapter title, heading, kind, text]`. One doc per section (`kind` `s`), per glossary term (`g`), per fact (`f`: claim; the chapter title is the fact's service) and per question stem of pool `chapter` (`q`). `route` is the hash without `#`.

`search/<slug>.json` (a **search shard**): `{"v": 1, "chapter": "vpc", "docs": [doc, ...]}`. The shard of a chapter holds the `s` and `q` docs of that chapter when it is built, and the `f` docs of every fact namespace that the chapter lists in `book.json` `services`. So a planned chapter has a shard when its services have verified facts (in a `--only-ready` build of 2026-10-14: 19 ready chapters and 8 planned ones), and its facts stay searchable. `search/book.json` (`"chapter": null`) holds the `g` docs and the `f` docs of a namespace that no chapter lists (today `exam`). A chapter without docs has no shard.

`search/index.json`: `{"v": 1, "count": 14214, "aliases": {"<term id>": ["form", ...]}, "shards": [{"chapter": "vpc" | null, "path": "search/vpc.json", "bytes": 120345, "count": 512}]}`. The shards are in book order, `search/book.json` last; `count` is the number of docs of all shards. `aliases` comes from `terms.json` (`short` and `aliases` of each term).

### 2.5 The shell

`shell.html` slots, filled by `site.py`: `{{fonts}}` (the Google Fonts link of the existing artifact, unchanged), `{{css}}`, `{{toc}}` (the contents list with one `<a href="#ch.<slug>">` per chapter and its status word, written into `#saa-toc`), `{{static}}` (the first frame in `#saa-view`: title block, the `examFacts` strip and, wrapped in `<div class="static-toc">`, the same list; `20-layout.css` hides `.static-toc` from 760px, where `#saa-toc` is a visible column, and below 760px the drawer is closed by CSS alone, without script, so the list shows once at every width), `{{boot}}` (JSON in `<script type="application/json" id="saa-boot">`: `{"build", "single", "preview", "title", "cfg"}`, where `cfg` is `shell.json`; JavaScript reads it as `SAA.state.cfg`), `{{inline}}` (empty unless `--single`), `{{js}}`. The file starts with `<title>SAA-C03 Handbook</title>`.

Token CSS is generated from `tokens.json`: one `:root{…}` block with every token, then the two dark blocks in the exact shape of `ARTIFACT-RULES.md`, both from the same `dark` values and each with `color-scheme: dark`. The build fails (`WB06`) when a pair in `tokens.json` `pairs` is below its ratio; when a `themed` entry lacks `light` or `dark`; when an `alias` or `static` value holds a literal colour; or when a `var(--x)` in a CSS file, in the output of `diagram css` or in an alias names a variable that `tokens.json` does not define (variables set by script or by a CSS file, such as `--dg-w`, `--top-h`, `--ex-h` and the zoom scale, are listed in `tokens.json` `runtime` and are allowed).

Source files: a file of 3.2 or of the CSS list of 1.1 that does not exist yet is skipped with a `WB02` warning in a `--preview` build and is an error in every other build.

Escaping: every `<` in inline JSON (`#saa-boot`, `#saa-inline`) is written as `<`, and U+2028 and U+2029 as ` ` and ` `. The page script and the worker source must not contain `</script` or `<!--` (`WL09`).

### 2.6 `--single` and `--preview`

- `--single`: `{{inline}}` becomes `<script type="application/json" id="saa-inline">{"manifest.json": {...}, "c/vpc.json": {...}, ...}</script>` (escaped as in 2.5), with every JSON file of the multi-file build, the shards `f/<service>.json`, `facts-index.json`, `search/index.json` and the search shards included; the inner markup of `assets/icons.svg`, without the XML declaration, is placed in `#saa-sprite`; the worker source is placed in `<script type="text/plain" id="saa-worker">`. `Content` then uses the inline backend and no network.
- `--preview`: the site is built, then `index.html` is replaced by `skeleton.html` with the page inside `<body>` and `claude-stub.js` in a `<script>` before it. The skeleton has `<!doctype html>`, charset, the viewport meta with `viewport-fit=cover`, and the reset of `ARTIFACT-RULES.md` (light `color-scheme`, safe-area padding on `:root`, zero body margin, 14px system font on an off-white ground, `img{max-width:100%}`, `[hidden]{display:none!important}`). `index-dark.html` is the same file with `<html data-theme="dark">`, and `index-forced-light.html` with `<html data-theme="light">`. `selftest.js` is part of the script only with `--preview`.
- A preview is never published. A person can serve it with `python3 -m http.server 8765 -d aws-saa-book/_build/preview`.

### 2.7 Publish plan

`publish-plan.json`: `{"build", "url": <string|null>, "title": "SAA-C03 Handbook", "icon": "book", "capabilities": {...section 5.1...}, "batches": [{"name": "content", "files": [{"path", "bytes", "sha256", "changed": true}], "count", "bytes"}, {"name": "exports", ...}], "removed": [paths], "hashes": {path: sha256}}`. `changed` compares with `common.REPORTS / "site-published.json"`; the orchestrator copies `publish-plan.json` there after a publish. `manifest.json` and `index.html` are in every content batch. The shards and `facts-index.json` are ordinary files of the content batch, each with `bytes`, `sha256` and `changed`, so an unchanged shard is not sent again. `removed` holds every path of `site-published.json` `hashes` that this build does not emit, plus each retired path of an earlier layout that the build does not emit (`site.RETIRED_PATHS`, today `facts.json` and `search/corpus.json`), so the first publish after each change deletes the old file from the artifact. The search shards and `search/index.json` are ordinary files of the content batch, like the fact shards.

`url` is copied from the `url` field of `site-published.json` (the orchestrator stores the artifact URL there after the first publish; `null` before it). The first publish fixes the URL; every later publish passes it, whatever folder the build came from (`site`, `site-single` or a moved folder). The book is never published as a second artifact: a new artifact has a new origin (empty localStorage) and a new database (no cloud progress). A `--single` build writes the same `publish-plan.json` shape with one file in `content` and every multi-file path in `removed` (the shards, `facts-index.json`, `facts.json`, the search files and `search/corpus.json` included).

### 2.8 Chapter status in the app

| Status | Contents list | Reader |
|---|---|---|
| `planned` | Title, muted, the words "Not written yet"; not a link target for Next and Previous | `#ch.<slug>` shows the title and "This chapter is not written yet." |
| `draft` | Normal, with the word "Draft" | A banner "Draft: not reviewed yet. Facts are linked to AWS sources. Practice questions appear when the chapter is ready." (In a preview build a draft chapter can already show verified items, 2.2.) |
| `ready` | Normal, with progress for the chosen route | Normal |

## 3. JavaScript

### 3.1 Rules

- Plain scripts, ES2020, no modules, no bundler, no library. One global: `window.SAA`. Each file is `(function (SAA) { "use strict"; … })(globalThis.SAA = globalThis.SAA || {});` and adds exactly the namespaces of the table.
- Files marked **pure** touch no `window`, `document` or storage at load or in any function, so the node harness can load them.
- No inline event attributes. All events go through delegation (`SAA.U.on`). Controls carry `data-act="<name>"`.
- HTML is built with `SAA.U.h`, a tagged template that returns a `SafeHtml` object (`{__safe: true, s: string}`; `toString()` gives `s`). An interpolated `SafeHtml`, or an array of `SafeHtml`, is inserted without escaping; every other value is escaped as text; `null`, `undefined` and `false` give an empty string. `U.raw(string) -> SafeHtml` may wrap only `_h` fields that came from `Content`, `parts[].html`, `figures` markup, the sprite, and the search worker's snippet. `U.set(el, safe)` is the only code that assigns `innerHTML`; it throws on a plain string. **Every function of this file that takes or returns `html` takes or returns `SafeHtml`.**
- Never `alert`, `confirm`, `prompt`, `window.print`, `<a download>`, a `vh` unit, `style.display`. Storage only through `SAA.U.ls`, and for the documents of 5.2 only through `Store`. Time only through `U.now()` and `U.nowMs()`.

### 3.2 Modules, in load order

| # | File | Owner | Namespace: public functions |
|---|---|---|---|
| 1 | `util.js` (pure except `on`, `ls`, `toast`, `announce`) | B | `U.esc(s)`, `U.raw(string) -> SafeHtml`, `U.h` (tag, returns `SafeHtml`), `U.set(el, safe)`, `U.now()` (whole seconds) and `U.nowMs()` (both call `SAA.Test.clock` when it is set; no other code calls `Date.now()` or `new Date()` without an argument, `WL10`), `U.bytes(s)` (UTF-8 length, pure), `U.bstrip(domains, opts) -> SafeHtml` (below the table), `U.debounce(fn, ms)`, `U.clone(o)`, `U.fmtClock(sec)`, `U.fmtMin(n)`, `U.day(ms?)` (local day number), `U.uid(prefix)`, `U.shuffle(arr, rng?)`, `U.rng(seed)`, `U.norm(s)` (lowercase, straight quotes, single spaces), `U.on(root, type, selector, fn)`, `U.ls.get(key)`, `U.ls.set(key, value)` (both JSON, try/catch, return `null` / `false` on failure), `U.toast(text)`, `U.announce(text)`, `U.copy(text) -> Promise<boolean>`; `bus.on(name, fn)`, `bus.off`, `bus.emit(name, detail)`; `Test.register(name, fn(el))`, `Test.states` (the map that `register` fills; `#t.shot.<name>` runs `Test.states[name]`), `Test.clock` (`null`, or a function that returns milliseconds) |
| 2 | `content.js` | B | `Content.manifest() -> Promise`, `Content.chapter(slug)`, `Content.data(slug)`, `Content.mock(slug)`, `Content.drill(id)`, `Content.glossary()`, `Content.plan()`, `Content.factsIndex()`, `Content.factService(id, index) -> service|null` (pure), `Content.factShard(service)`, `Content.fact(id) -> Promise<fact card|null>`, `Content.questions(ids) -> Promise<{q: {id: Q}, facts}>` (loads the needed `d/` and `q/` files through `qindex`), `Content.qindex()`, `Content.sindex()` (the `s` map of `qindex.json`), `Content.text(path) -> Promise<string>`, `Content.blob(path) -> Promise<Blob>`, `Content.prefetch(slug)`, `Content.meta(slug)` (manifest chapter object, sync after manifest), `Content.section(slug, sid)` (`{sid, part, kind, route, min, title, parent, role}` or null; sync), `Content.routeSections(slug, route) -> rows`, `Content.progress(slug, route, progress) -> {read, total}`, `Content.sprite()` (details below the table) |
| 3 | `router.js` | B | `Router.register(view, def)`, `Router.parse(hash) -> {view, args: []}`, `Router.href(view, ...args)`, `Router.go(hashOrRoute, {replace}?)`, `Router.start({hash?, view?}?)`, `Router.current() -> {view, args, hash}` |
| 4 | `merge.js` (pure) | D | `Merge.deep(a, b)`, `Merge.stamps(a, b)`, `Merge.doc(name, local, remote)`, `Merge.attempts(a, b)`, `Merge.diff(base, next)` |
| 5 | `store.js` | D | section 5.4 |
| 6 | `scoring.js` (pure) | C | section 7.1 |
| 7 | `popover.js` | B | (`html` is `SafeHtml`) `Pop.open(anchorEl, html, {label, wide}?)`, `Pop.close()`, `Pop.sheet(html, {label, full, onClose}) -> el`, `Pop.closeSheet()` |
| 8 | `evidence.js` | B | `Evidence.card(fact) -> SafeHtml`, `Evidence.show(anchorEl, id)`, `Evidence.register(factsMap)` (adds the facts that `a.ev` clicks can open; call it before inserting any `_h` field), `Evidence.get(id)`; `show` and the view `fact` load a fact that is not registered through `Content.fact(id)` and then register it |
| 9 | `glossary.js` | B | `Glossary.show(anchorEl, id)`; view `glossary` |
| 10 | `reader.js` | B | view `ch`; `Reader.mountHtml(el, html, facts, ctx)` (for part HTML only: inserts it, registers the facts, sets up read tracking, the rail, figures and the mounts inside `el`; returns a cleanup function), `Reader.registerMount(name, fn(el, id, ctx) -> cleanup?)`, `Reader.runMount(name, el, id, ctx) -> cleanup|undefined` (section 10) |
| 11 | `qview.js` | C | `QView.render(el, q, state, opts)`, `QView.review(el, q, answer, opts)` (section 7.2) |
| 12 | `quiz.js` | C | views `quiz`, `drill`, `retry`, `mix`; `Quiz.start(spec)` |
| 13 | `exam.js` | C | views `mock`, `attempt` |
| 14 | `mistakes.js` | C | view `mistakes`; mount `mistakes` |
| 15 | `cards.js` | C | view `cards`; `Cards.render(el, card, {flipped})` |
| 16 | `today.js` | D | view `home` |
| 17 | `plan.js` | D | view `plan`; mount `plan` |
| 18 | `dash.js` | D | view `progress` |
| 19 | `files.js` | D | views `files`, `about` |
| 20 | `aicore.js` (pure) | E | section 6 |
| 21 | `ai.js` | E | `AI.available() -> boolean`, `AI.call(input, {tier, cache, onState}) -> Promise<{ok, data}|{ok: false, code, message, hide}>`, `AI.stop()`, `AI.notice() -> SafeHtml` |
| 22 | `speak.js` | E | view `speak`; mount `speak` (the `say` part of a chapter); `Speak.render(el, item, {facts, step}) -> cleanup` (`step` 1 to 4 of 6.4) |
| 23 | `ask.js` | E | `Ask.open(slug, sid)` |
| 24 | `search.js` | E | `Search.open(prefill?)`, `Search.jump(text) -> rows` |
| 25 | `selftest.js` (preview only) | C | views `t` |
| 26 | `boot.js` | B | `App.start(data)`, `App.snapshot()`, `App.caps` |

A view definition: `{mount(el, args, ctx) -> void|Promise, unmount()?, title(args) -> string, snapshot()? -> object}`. `ctx` is `{hot: object|null}`: the `snapshot()` value of the same view from before a republish. `Router.start({hash, view})` (with `view` = `{name, data}`) passes `view.data` once, as `ctx.hot`, to the first mount whose view name equals `view.name`; every other mount gets `hot: null`. `snapshot()` returns plain JSON only (`JSON.parse(JSON.stringify(x))` equals `x`). `App.snapshot()` reads only `def.snapshot()` of the mounted view; modules expose no other snapshot function. `Router` calls `unmount` of the old view, empties `#saa-view`, sets `data-view`, calls `mount`, moves focus to the first `h1` (which every view renders, with `tabindex="-1"`), announces the title, and stores the route with `Store.patch("ui", {route, t})`.

Details of row 1 and row 2:

- `U.bstrip(domains, opts) -> SafeHtml` is the only code that draws the blueprint strip. `domains` is `manifest.domains`; `opts` is `{on: [domain ids]}` (reader: the domains a chapter feeds) or `{pct: {1: 58, …}}` (Today, results: accuracy). Markup: `<div class="bstrip" role="img" aria-label="…">` with four `<span class="bstrip-s" style="flex-grow:<weight>" data-d="<n>">` holding `D1` and, with `pct`, the percent as text. State classes: `is-on`; with `pct`, `is-good` at or above `cfg.gate.strong`, `is-warn` at or above `cfg.gate.domainMin`, else `is-bad`. The label lists the four domains with their state in words.
- `Content.routeSections(slug, route)`: the rows of kind 2 or 3 whose route is at or below `route` (`fast` < `pass` < `full`), minus every kind 2 row that has kind 3 children (the children are counted instead). `Content.progress(slug, route, progress)` counts those rows with a positive read stamp. **B and D use only these two functions for every "sections read" number.**
- Every `fetch` of `Content` uses `cache: "no-cache"` (a conditional request; an unchanged file costs a 304). No query strings. `Content` keeps the chapter `hash` of each `c/` and `d/` file in its memory cache; on a manifest refresh it drops the files of chapters whose `hash` changed, and the reader reloads the open part when its chapter was dropped, keeping `{sid, off}`.
- `Content.chapter(slug)` and `Content.data(slug)` resolve `null` for a planned chapter or a chapter without that file. On a network or parse error every `Content` function emits `content:error` and rejects with `{path}`; the view then shows "This page could not be loaded. Check your connection and try again." with a Retry button.
- `Content.blob` and `Content.text` work in both modes (in `--single`, from the inline entry).
- Facts (2.4): `Content.factsIndex()` resolves `facts-index.json` through `manifest.factsIndex.path`. `Content.fact(id)` finds the service with `Content.factService(id, index)`, loads that one shard with `Content.factShard(service)` and resolves the card, or `null` for an unknown service or an id that is not in its shard. The index and each shard are fetched at most once per visit (kept for the visit like `glossary.json`, not in the five-file cache of `c/`, `d/`, `q/`); a manifest refresh whose `factsIndex.sha256` changed forgets the index and every shard. In `--single` they come from the inline map. `Content.fact` is the only code that reads a shard; `Evidence` calls it for a fact that no open file registered.

### 3.3 Routes

| Hash | View | Owner |
|---|---|---|
| (empty), `#home` | Today. The empty hash restores `ui.route` when `U.now() - ui.t < 43200` (12 hours), else Today | D |
| `#toc` | Not a view: `Router` keeps the mounted view, opens the drawer (phone) or focuses `#saa-toc` (desktop), and does not store the route. With no mounted view it mounts Today first | B |
| `#ch.<slug>` | Reader at the part chosen by the route setting: `fast`, or the last part read | B |
| `#ch.<slug>.<part>` and `#ch.<slug>.<part>.<sid>` | Reader at a part, at a section. In part `do` the third token is a task id; in `say`, a speak id | B |
| `#quiz.<slug>`, `#quiz.<slug>.all` | Chapter quiz: core questions, or all | C |
| `#drill.d1` to `#drill.d4` | Domain drill | C |
| `#retry`, `#retry.w` | Retry my mistakes; ten stem-first questions (repair for cause W) | C |
| `#mix` | Daily mix | C |
| `#mock.1`, `#mock.2` | Mock exam: in progress when an `exam` document runs for that mock, else the intro (7.4) | C |
| `#attempt.<attempt id>` | Results and review of one attempt of any kind | C |
| `#mistakes` | Mistakes log | C |
| `#cards.<slug>` | Quick card review | C |
| `#speak`, `#speak.<slug>`, `#speak.<slug>.<id>` | Speak practice: pack list, chapter prompts, one prompt | E |
| `#glossary`, `#glossary.<term id>` | Glossary | B |
| `#fact.<fact id>` | Fact card as a page (fallback of the chip link); a fact that no open file registered is read from its shard through `Content.fact` | B |
| `#numbers`, `#traps`, `#changed` | Aliases from `manifest.aliases` | B |
| `#plan`, `#progress`, `#files`, `#about` | Plan, dashboard, Get files, About | D |
| `#t.render-all`, `#t.exam-sim`, `#t.hot`, `#t.shot.<name>` | Preview test routes | C |

An unknown route shows "This page does not exist" with a link to Today. Links are real `<a href="#…">`. `Router` also listens to `hashchange`, and ignores a `hashchange` for the route it already shows. `Router.go` updates its own state and mounts first, then writes the hash inside `try/catch` (`location.hash = …`, or `history.replaceState` for `{replace}`); a failed write is ignored, so navigation works when the host ignores hash writes. No `key=value` and no query string, ever.

One click handler on `#saa` (owner B, in `router.js`) serves every view. It handles, in this order, and stops at the first match: `a.ev` (opens the evidence card through `Evidence.show`, no navigation); `a.term` (opens the glossary popover); B's `[data-act]` controls `copy`, `zoom`, `describe`, `toc`, `search`, `ask`; then any other `a[href^="#"]` (`Router.go` and `preventDefault`). Other owners handle their own `data-act` names with `U.on` on their view element; they do not use B's six names. C, D and E call only `Evidence.register(facts)` before they insert `_h` fields; they never call `Reader.mountHtml` for a fragment.

### 3.4 Events (`SAA.bus`)

| Event | Detail | Emitted by |
|---|---|---|
| `route` | `{view, args, hash}` | Router, after mount |
| `manifest` | manifest | Content |
| `caps` | `SAA.state.caps` (each namespace, or null) | App, each time one capability settles (up to five times; listeners are idempotent) |
| `store:change` | `{doc, source: "local"|"remote"}` | Store |
| `store:status` | `{status: "cloud"|"local"|"memory", consent: "prompt"|"denied"|null}` | Store |
| `settings` | settings object | Store |
| `section:read` | `{slug, sid}` | Reader |
| `answer` | `{qid, ok, unsure, kind}` | Quiz, Exam (on submit, per question) |
| `attempt` | attempt document | Store only (`Store.addAttempt`) |
| `speak:done` | `{id, self: <count of yes, 0 to 5>, score: n|null}` | Speak (after it wrote the result and the daily stamp) |
| `content:error` | `{path}` | Content |

### 3.5 State

`SAA.state = {route: {view, args, hash}, manifest: null|object, build: string, cfg: object, caps: {user, db, sample, downloads, permissions} (each `undefined` until it settles, then the namespace or `null`), uid: null|string, status: "memory"|"local"|"cloud", single: boolean, preview: boolean}`. Only `boot.js`, `router.js`, `content.js` and `store.js` write it. Persistent state lives only in `Store`.

### 3.6 DOM contract (`shell.html`)

```html
<div id="saa" class="app ts-1" lang="en">
  <a class="skip" href="#saa-main">Skip to content</a>
  <header id="saa-top" class="top">
    <button type="button" id="saa-menu" class="top-menu" data-act="toc" aria-controls="saa-toc" aria-expanded="false">Contents</button>
    <a class="brand" href="#home" aria-label="SAA-C03 Handbook"><span class="brand-s">SAA-C03</span><span class="brand-l"> Handbook</span></a>
    <nav id="saa-nav" class="nav" aria-label="Main">Today · Plan · Practice (#mistakes) · Speak · Progress</nav>
    <button type="button" id="saa-search" data-act="search">Search</button>
  </header>
  <div class="shell">
    <nav id="saa-toc" class="toc" aria-label="Contents">{{toc}}</nav>
    <main id="saa-main" tabindex="-1">
      <p id="saa-sync" class="sync" hidden></p>
      <div id="saa-view" data-view="home">{{static}}</div>
    </main>
    <aside id="saa-rail" class="rail" aria-label="On this page" hidden></aside>
  </div>
  <div id="saa-live" class="vh" aria-live="polite"></div>
  <div id="saa-pop-layer" class="pop-layer" hidden><div id="saa-pop" class="pop" role="dialog"></div></div>
  <div id="saa-sheet" class="sheet" role="dialog" aria-modal="true" hidden></div>
  <div id="saa-toast" class="toast" role="status" hidden></div>
  <svg id="saa-sprite" width="0" height="0" aria-hidden="true"></svg>
</div>
```

`#saa-view` is the only mount for views. `#saa-rail` belongs to the reader (other views hide it and build their own columns inside `#saa-view`). `#saa-pop-layer`, `#saa-pop` and `#saa-sheet` belong to `Pop`. `Store` writes `#saa-sync` (a text line and at most one button; it sits at the top of the main column at every width, because the header has no room for it). The static first frame stays until `Router.start()` mounts the first view. B sets `aria-current="page"` on the matching link of `#saa-nav` and `#saa-toc` on the `route` event.

### 3.7 Boot (`boot.js`)

```js
var hot = window.claude && window.claude.hot;
try { if (hot && hot.snapshot) hot.snapshot(function () { return SAA.App.snapshot(); }); } catch (e) {}
if (hot && hot.ready) hot.ready(SAA.App.start); else SAA.App.start((hot && hot.data) || {});
```

`App.start(data)`:

`App.start` begins with `data = data || {}`, ignores a `data` whose `v` is not 1 (treated as `{}`), and runs once (a second call returns). Each of the four steps is in its own `try/catch`; a failure is logged with `console.error` and the next step still runs. If `Router.start()` throws, the static first frame stays and the line "The page could not start. Reload to try again." is added under it.

1. Read `#saa-boot` into `SAA.state`. `Store.init(data.store)` (sync: memory and localStorage). Apply the text size.
2. `Router.start({hash: data.route, view: data.view})`; a view that needs the manifest awaits `Content.manifest()` itself. Today renders from local state.
3. `Content.manifest()`; emit `manifest`; refresh the contents list (B replaces the content of `#saa-toc`).
4. `claude.use` for `user`, `db`, `sample`, `downloads` and `permissions` (built in, not declared) in parallel, each wrapped so that a missing `window.claude`, a rejection or `null` gives `null`. Each one sets `SAA.state.caps.<name>` and emits `caps` when it settles, so Ask and Save buttons do not wait for the database. When `user`, `db` and `permissions` have settled, without blocking anything else:
   - `uid = await user.id()` (null without `user`), kept in `SAA.state.uid`.
   - `db` or `uid` null: `Store.attach(null, null)` (stays `local`).
   - `permissions` null: `Store.attach(db, uid)` now.
   - else `await permissions.state("db")`: `granted`: `Store.attach(db, uid)` now. `prompt`: do not attach, call `Store.consent("prompt")`; the status line shows "Saved on this device only" with a button "Save online too", and the click calls `Store.attach(db, uid)` (the first db call itself asks). `denied`: `Store.consent("denied")`; About offers "Open permissions" (`permissions.manage()`, on click only; afterwards re-read the state). `unavailable`: stay `local`.
   No db call ever runs before a click unless the state is `granted` or `permissions` is absent, so no consent dialog covers the first frame. The app never waits for `attach`.

`App.snapshot()` returns `{v: 1, route: Router.current().hash, view: {name: <view name>, data: <snapshot() of the mounted view, or null>}, store: Store.snapshot()}`, plain JSON. `ctx.hot` is `view.data`. The reader's snapshot is `{slug, part, sid, off}` (`off`: pixels scrolled inside section `sid`); Quiz and Exam return their session; Speak and Ask return unsent text.

## 4. CSS

### 4.1 Tokens (`tokens.json`)

Shape: `{"themed": {"<name>": {"light": "#…", "dark": "#…"}}, "alias": {"<name>": "var(--…)"}, "static": {"<name>": "<value>"}, "runtime": ["dg-w", "top-h", "ex-h", "zoom"], "pairs": [["ink", "ground", 4.5]]}`. `themed` holds any value with a light and a dark form (colours, and the two `dg-show-*` display values). `runtime` lists variables that a CSS file or script sets (not generated). Alias `dg-ground` is `var(--surface)`, so the literal fallback inside `diagram css` is never used. Names and values are those of `PRODUCT.md` section 7 (light and dark tables), which keep the values of the existing artifact. Additions decided here: `code-bg` dark `#1B2230`, `code-ink` dark `#D5DBE7`, `on-accent` dark `#0F131B`, `mark` dark `#4A3F12`, `sunken` dark `#0B0E14`, `shadow` light `rgba(20,28,43,.16)` dark `rgba(0,0,0,.5)`, `dg-show-light` / `dg-show-dark` (`inline` / `none`, swapped in dark). Static: `font-display`, `font-body`, `font-mono`, `fs-0` 13px, `fs-1` 15px, `fs-2` 17px, `fs-3` 19px, `fs-4` 24px, `fs-5` 34px, `lh-body` 1.62, `measure` 66ch, `gutter` 16px, `radius` 4px, `rail` 15rem, `margin` 8.5rem. `--top-h` is not a token: `20-layout.css` sets it on `.app` (52px, one header row) and `90-phone.css` sets the two-row height. Text size: `.ts-0`, `.ts-1`, `.ts-2` on `#saa` set `--fs-2` to 16px, 17px, 19px.

No rule outside the generated blocks holds a literal colour. `body{background:var(--ground);color:var(--ink)}` is in `10-base.css`.

### 4.2 Layout

- `.app` fills the page; `.shell` is the outer wrapper of the content with `padding-inline: var(--gutter)` and `padding-block`. The same gutter is `padding-inline: var(--gutter)` on `.top`; fixed layers (`.ex-bar`, `.toast`, `.sheet`, the phone `.pop`) use the same variable in their own padding. Desktop (min-width 1100px): grid `toc 17rem | main minmax(0, 1fr) | rail var(--rail)`. Between 760px and 1099px: `toc | main`, no rail column (the rail is a sheet opened by a "Sections" button). Below 760px: one column; `.toc` is a drawer, closed by CSS alone (it opens with the class `is-open` that script sets).
- `.top` is sticky with `top: env(safe-area-inset-top, 0px)`. From 760px it is one row: Contents button (hidden while the contents column shows), brand, `#saa-nav`, Search. Below 760px it is two rows (4.4).
- Reader text: `.sec` and `.sub` span the main column; the content of `.sec-h`, `.sec-b`, `.sub-h`, `.sub-b` is limited to `max-width: var(--measure)`. From 1280px the hanging margin is **inside** the section: `.sec` has `padding-inline-start: var(--margin)` and `.co-l` is positioned inside that padding (a `.sub` adds no second margin). Below 1280px (so also from 1100px to 1279px, where the rail column already takes room) there is no hanging margin and `.co-l` is a small tab above the block. `.sec` and `.sub` always have `padding-inline-end: 4px`, so focus rings are not clipped. Nothing is positioned outside the padding box of a `.sec`.
- `.tw`, `.code pre`, `.fig-s` and `.zoom` are the only horizontal scroll containers. Every flex or grid child with text has `min-width: 0`.
- Long strings: `.app { overflow-wrap: break-word }`; `p code`, `li code`, `td code`, `.evc-id`, `.evc-src a`, `a.ext`, `.opt`, `.q-stem`, `.srch-row` use `overflow-wrap: anywhere`. Rows of controls (`.chh-meta`, `.rsw`, `.tabs`, `.q-nav`, `.fig-a`, `.td-min`, `.nav`) use `flex-wrap: wrap`. `.cells` is `grid-template-columns: repeat(auto-fill, minmax(44px, 1fr))`. Never `overflow-x: hidden` (or `clip`) on `body`, `.app` or `.shell` to hide a fault.
- Anchors: `.sec`, `.sub`, `.h3`, `.fig`, `.pr` have `scroll-margin-top: calc(var(--top-h) + env(safe-area-inset-top, 0px) + 12px)`.
- Layers, lowest first: `.top`, `.ex-bar`, the drawer, `.pop-layer`, `.sheet`, `.toast`. `.toast` sits above the exam bar: `bottom: calc(var(--ex-h, 0px) + 12px + env(safe-area-inset-bottom, 0px))` (`exam.js` sets `--ex-h` on `#saa` while the bar shows).

### 4.3 Component classes

| Component | Classes | Owner |
|---|---|---|
| Buttons, pills, eyebrow, mono | `.btn`, `.btn.primary`, `.btn.quiet`, `.pill`, `.pill.good|warn|bad|note`, `.eyebrow`, `.mono`, `.vh` | B |
| Sections | `.sec`, `.sec-h`, `.sec-b`, `.sub`, `.sub-h`, `.sub-b`, `.tbox`, `.h3`, `.lede`, state `.is-read`, `.is-offroute`, `.is-gated` | B |
| Callouts | `.co`, `.co-l`, `.co-b`, `.co-key`, `.co-signal`, `.co-trap`, `.co-heur`, `.co-say`, `.co-try`, `.co-startup`, `.co-cost`, `.co-cleanup`, `.co-careful`, `.co-changed`, `.chg`; hue `.hue-indigo|red|amber|teal|neutral` | B |
| Prompts and reveals | `.pr`, `.pr-l`, `.pr-q`, `.pr-predict|check|recap|faq|stop|bug|pic`, `.rv`, `.rv-answer`, `.rv-picture`, `.rv-deeper`, `.rv-b` | B |
| Fields, traps, quotes | `.bf`, `.bf-l`, `.bf-list`, `.bf-decide`, `.traps`, `.trap`, `.trap-w`, `.trap-t`, `.awsq` | B |
| Tables | `.tw`, `.tb`, `.tb-compare`, `.tb-signals`, `.tb-words`, `.tb-numbers`, `.tb-pairs`, `.tb-matrix`, `.tb-glance`, `.tb-services`, `.tb-breaks`, `.tb-log`, `.tb-plan`, `.tb-exam-english`, `.tb-plain`, `.tb-stack` | B |
| Code | `.code`, `.code-copy`, `.tok-kw`, `.tok-str`, `.tok-num`, `.tok-com` | B |
| Evidence chip and card | `.ev` (dotted accent underline and a small "src" mark from `::after`), `.evc`, `.evc-id`, `.evc-claim`, `.evc-q`, `.evc-src`, `.evc-chg` | B |
| Glossary | `.term`, `.glc`, `.glc-say`, `.glc-not` | B |
| Popover, sheet, toast | `.pop`, `.sheet`, `.sheet.full`, `.sheet-h`, `.sheet-x`, `.toast` | B |
| Figure card | `.fig`, `.fig-h`, `.fig-n`, `.fig-t`, `.fig-s`, `.fig-c`, `.fig-steps`, `.fig-a`, `.fig-img`, `.zoom` | B |
| Chapter header, route switch, part tabs | `.chh`, `.chh-meta`, `.rsw` (a `fieldset` of three radios: `.rsw-o`), `.tabs`, `.tab`, `.bstrip`, `.bstrip-s` with states `.is-on`, `.is-good`, `.is-warn`, `.is-bad` (blueprint strip; markup only from `U.bstrip`, 3.2) | B |
| Shell | `.top`, `.top-menu`, `.brand`, `.brand-s`, `.brand-l`, `.nav`, `.sync`, `.static-toc`, `.toc-ref` (the Reference list), `.pop-layer`, `.twins`, `.mount`, `.notice` (inline error or status line with a Retry button) | B |
| Section rail, contents | `.rail`, `.rail-i`, `.rail-i.is-cur`, `.rail-i.is-read`, `.toc`, `.toc-part`, `.toc-ch`, `.toc-st`, `.toc-bar` | B |
| Tasks | `.task`, `.task-step`, `.task-chk`, `.task-cmd`, `.task-warn` | B |
| Question | `.q`, `.q-meta`, `.q-stem`, `.q-w` (stem word), `.q-kw` (deciding phrase after checking), `.q-opts`, `.opt`, `.opt.sel`, `.opt.ok`, `.opt.no`, `.bubble`, `.opt-tag`, `.opt-why`, `.q-unsure`, `.q-sf` (stem-first panel), `.q-ex`, `.q-cause`, `.q-nav` | C |
| Exam | `.ex-grid` (the exam's own two-column grid inside `#saa-view`: question, answer sheet), `.ex-bar`, `.timer`, `.timer.over`, `.cells`, `.cell`, `.cell.ans`, `.cell.uns`, `.cell.cur`, `.ex-sheet`, `.score`, `.bigscore`, `.drow`, `.bar`, `.bar-f` | C |
| Mistakes, cards | `.mk`, `.mk-row`, `.mk-code`, `.fc`, `.fc-front`, `.fc-back`, `.fc.is-flipped` | C |
| Today, plan, dashboard | `.td`, `.td-card`, `.td-card.is-main`, `.td-min` (daily minimums), `.pl`, `.pl-day`, `.pl-day.is-today`, `.pl-task`, `.pl-gate`, `.ds`, `.ds-gate`, `.pbar`, `.pbar-f` (progress bar; a `<progress>` element is preferred where it fits), `.files`, `.files-row` | D |
| Speak, Ask, search | `.sp`, `.sp-timer`, `.sp-self`, `.sp-kp`, `.sp-kp.is-hit`, `.sp-res`, `.sp-band`, `.sp-err`, `.sp-improved`, `.mk-hit` (highlight in her text), `.ask`, `.ask-turn`, `.ask-src`, `.ai-note`, `.ai-busy`, `.srch`, `.srch-in`, `.srch-row`, `.srch-hit` | E |

Component treatment follows `PRODUCT.md` section 7 (callouts without accent rails, mono capital labels, hairline tables without zebra, a sticky first column in scrolled tables). Semantic states always carry a word ("Correct", "Your pick", "Read", "Draft"), never colour alone. Motion: one 120 ms fade on view change, inside `@media (prefers-reduced-motion: no-preference)`.

### 4.4 Phone rules (`90-phone.css`, max-width 759px)

- `.tb-stack` renders each row as a block; each cell shows `attr(data-th)` as a mono label above its text. Other tables scroll inside `.tw` with the first column sticky.
- Header: two rows with `flex-wrap: wrap`. Row 1: Contents button, brand (only `.brand-s`, the text "SAA-C03", shows; `.brand-l` is hidden and the full title stays in `aria-label`), Search button. Row 2: `#saa-nav` at full width, five links with `flex: 1 1 0; min-width: 0`, `--fs-0`, each at least 44px high. `--top-h` is set to the two-row height here. `.sync` is a full-width line in the main column whose text wraps.
- `.static-toc` is shown (the drawer is closed).
- `.pop` becomes a bottom sheet: `.pop-layer` is `position: fixed; inset: 0` and `.pop` sits at its bottom, full width, `max-height: 70%` of that layer (never a `vh` unit), bottom padding `env(safe-area-inset-bottom)`. `.sheet` is always full width.
- `.sheet.full` and the phone drawer are `position: fixed; inset: 0` with `padding-top: env(safe-area-inset-top)` and `padding-bottom: env(safe-area-inset-bottom)` of their own (fixed layers do not get the `:root` padding).
- `.fig-s > svg`, `.fig-s .dg-cmp-p > svg` and `.fig-s > img` have `min-width: calc(var(--dg-w) * 0.75px)`, so a figure never renders below scale 0.75; wider figures scroll.
- Targets are at least 44px high. The exam bar is a fixed bar at `bottom: 0` with the inset in its padding; the main column gets matching bottom padding.
- Part tabs wrap (`flex-wrap: wrap`); they do not scroll. Skim mode and text size sit in the chapter header's "Aa" menu.

## 5. State and storage (implementer D)

### 5.1 Capability declaration (in `publish-plan.json`)

```json
{"db": {"rules": [{"path": "", "read": "owner", "write": "owner"},
                  {"path": "study", "read": "owner", "write": "owner"},
                  {"path": "study/{self}", "read": "interact", "write": "interact"}]},
 "user": {}, "sample": {}, "downloads": true}
```

If the orchestrator reports that the rules were rejected, it publishes `db: {}`; the paths do not change.

### 5.2 Paths and documents

`<uid>` is the awaited `user.id()`. A null id means no cloud sync for the visit.

| Document name (Store) | db path | localStorage | Shape |
|---|---|---|---|
| `root` (read and patched through the Store name `settings`) | `study/<uid>` | `saa1:settings` (holds the whole root) | `{v, createdAt, lastSeenAt, updatedAt, settings}` |
| `progress` | `study/<uid>/state/progress` | `saa1:progress` | below |
| `qstats` | `study/<uid>/state/qstats` | `saa1:qstats` | below |
| `exam` | `study/<uid>/state/exam` | `saa1:exam` | section 7.4 |
| `speak` | `study/<uid>/state/speak` | `saa1:speak` | `{v, updatedAt, items: {"<speak id>": {t, tries, self: "10110", score, band, missing: [kp], words, seconds}}}` (`self` is five characters, one per yes/no box; `tries` travels with the item, the later `t` wins) |
| `coach` | `study/<uid>/state/coach` | none (derived) | below |
| `ui` | none (never sent to db) | `saa1:ui` | below |
| attempts | `study/<uid>/attempts/<id>` | `saa1:attempts` (map by id; the newest 40 keep `answers`, older ones are trimmed to the summary) | section 7.5 |
| drills | `study/<uid>/drills/<id>` | none | below (written by Claude; the page only reads) |
| flags | `study/<uid>/flags/<id>` | outbox only | `{v, id, at, kind: "question"|"section"|"fact", ref, build, note}` (`note` at most 500 characters) |

```json
// settings
{"textSize": 1, "route": "pass", "routeBy": {"vpc": "full"}, "plan": "a", "planStart": "2026-10-05",
 "examDate": null, "extraTime": 0, "stemFirst": "auto", "skim": 0}

// progress
{"v": 1, "updatedAt": 1790000000,
 "chapters": {"vpc": {"read": {"predict": 1790000000}, "last": "deep.nat-gateways", "skips": {"stop-2": 1790000300}}},
 "plan": {"a": {"d03": {"t1": 1790000000}}},
 "daily": {"20012": {"pages": 1790000000, "words": 0, "speak": 1790000900}},
 "labs": {"vpc-t02": {"steps": {"1": 1790000000}, "cleaned": 0}},
 "cards": {"vpc": 1790000000}, "terms": {"idempotent": 1790000000},
 "last": {"route": "ch.vpc.deep.nat-gateways", "t": 1790000300}}

// qstats
{"v": 1, "updatedAt": 1790000000, "sf": 37, "q": {"vpc-q012": {"h": "011", "u": "010", "t": 1790000000, "d": 20012, "box": 1,
  "pick": ["b"], "c": "W", "kr": 1}}}

// ui (this browser only)
{"route": "ch.vpc.deep", "t": 1790000300, "pos": {"vpc.deep": {"sid": "nat-gateways", "off": 240}},
 "seen": {"vpc": "ready:2"}, "tab": {}}

// coach (derived by Scoring.buildCoach; read by Claude)
{"v": 1, "updatedAt": 1790000000, "examDate": null,
 "overall": {"seen": 212, "bank": 640, "accuracy": 71, "sureAccuracy": 83, "mocks": [{"ref": "mock-exam-1", "pct": 72}]},
 "domains": {"d1": {"acc": 58, "n": 60}},
 "weakTopics": [{"topic": "identity", "acc": 50, "n": 12, "chapters": ["iam"]}],
 "missed": [{"id": "vpc-q012", "wrong": 2, "lastPick": ["b"], "c": "W"}],
 "confusions": [{"a": "nat-gateway", "b": "internet-gateway", "n": 3}],
 "luckyGuesses": ["s3-q004"], "whyCounts": {"K": 4, "C": 6, "W": 9, "T": 1, "D": 0},
 "unreadPass": ["kms"], "speakWeak": [{"id": "vpc-s01", "missing": ["kp2"]}]}

// drill document
{"v": 1, "title": "IAM policy evaluation", "createdAt": 1790000000, "by": "claude", "why": "…",
 "items": ["iam-q003", {"id": "dr-a1", "type": "single", "select": 1, "stem": "…", "kw": [], "d": 1,
   "options": [{"id": "a", "text": "…", "ok": true, "why": "…"}], "expl": "…", "take": "…", "facts": []}]}
```

- **Every state document (`root`, `progress`, `qstats`, `exam`, `speak`) has `updatedAt`.** `Store.get("settings")` returns `root.settings`; `Store.patch("settings", p)` patches `root.settings` and sets `root.updatedAt`.
- `ui` is local only and written only through `Store.patch("ui", …)`: the router writes `route` and `t`; the reader writes `pos`; Today writes `seen`; `tab` is free for per-view conveniences keyed by view name. `progress.last` is for Today's "Continue reading" card and for Claude, not for restoring the route. `saa1:uid`, `saa1:outbox`, `saa1:drafts` and `saa1:bak:*` are also read and written only by `Store` (`Store.draft`, 5.4).
- `weakTopics[].topic` is a value of `SPEC.json` `questions.topics`; `unreadPass` lists not-planned chapters with unread Pass-route sections (`Content.progress`); `accuracy` values are whole percents.
- A drill item is a question id of the book or a **DQ**: plain text only, no `_h` field. `Scoring.validQuestion(dq)` checks the DQ shape and exactly `select` options with `ok`; an item that fails, or an id that is not in `qindex`, is skipped. `QView` shows `why`, `expl`, `take` as escaped text when the `_h` field is absent, and never reads an `_h` field of a question that did not come from `Content`. Text from the database is never passed to `U.raw`.
- Every leaf under `read`, `plan`, `daily`, `labs.steps`, `cards`, `terms`, `skips` is a **stamp**: a time in seconds, positive for "done", negative for "undone". Maps are keyed by id; no arrays, no counters except `sf` (questions answered in stem-first mode; merged with `max`) and `speak.items.*.tries` (it belongs to its item and is merged with it).
- `h` is the result history, oldest first, at most 8 characters; `u` the matching "not sure" flags; `d` the day number of the last correct answer; `c` the cause code of the last wrong answer; `kr` the `keyRev` the record belongs to. A record whose `kr` differs from `qindex` is ignored and overwritten.

### 5.3 Merge (`merge.js`)

- `Merge.stamps(a, b)`: union of keys; for a key in both, the value with the larger absolute value wins. Applied recursively to every stamp map.
- `Merge.doc("progress", l, r)`: stamps as above; `chapters.*.last` and `last`: the side with the later `last.t` (for chapters: the later `updatedAt`).
- `Merge.doc("qstats", l, r)`: per question the record with the later `t`; `sf` the larger.
- `Merge.doc("exam", l, r)` and `"root"`: the whole document with the later `updatedAt` (settings are not merged field by field); for `root`, `createdAt` is the smaller and `lastSeenAt` the larger of the two. **A document with `updatedAt: 0` (untouched defaults) never wins over an existing document**, so a new device cannot overwrite cloud settings or a running mock.
- `Merge.doc("speak", l, r)`: per item the later `t`.
- Every `Merge.doc` result has `updatedAt` = the larger of the two. A missing side (`null`) gives the other side.
- `Merge.attempts(a, b)`: union by id; an attempt is immutable.
- `Merge.diff(base, next)`: the smallest patch `p` with `Merge.deep(base, p)` equal to `next` (objects recurse; other values replace).

### 5.4 `Store` API

| Function | Behaviour |
|---|---|
| `Store.init(hotStore?)` | Sync. Loads each document from localStorage, else defaults; then merges `hotStore.docs` into them with `Merge.doc` (merge, not replace, so what another tab wrote is kept), and takes `outbox`, `uid`, `attempts`, `drafts` of `hotStore` where the local value is missing. A `hotStore` whose `v` is not 1 is ignored. Default documents have `updatedAt: 0`. Sets status `local`, or `memory` when a test write to localStorage fails. |
| `Store.get(name)` | The live object (read only for callers). Names: `settings` (= `root.settings`), `progress`, `qstats`, `exam`, `speak`, `ui`. |
| `Store.patch(name, patch)` | Deep-merges into memory, sets `updatedAt` to `U.now()`, saves to localStorage (debounced 400 ms; `exam` at once), merges the patch into the outbox entry of the document, schedules a flush, emits `store:change`. `Store.patch("settings", p)` also emits `settings`. `ui` is saved to localStorage only (no outbox, no `updatedAt`). `updatedAt` changes only here and in `Store.replace`, that is, on a user action. |
| `Store.replace("exam", doc|null)` | Whole-document write (`set`); `null` writes `{v: 1, updatedAt, none: 1}`. |
| `Store.draft(id, text?)` | Reads (one argument) or saves (debounced) her unsent text in `saa1:drafts`; an empty string removes it. |
| `Store.consent(state)` | Records `"prompt"` or `"denied"` from boot (3.7) for the status line; emits `store:status`. |
| `Store.importAll(obj)` | `-> {ok, counts: {answers, attempts}, error?}`. Validates `v` and the shapes; merges each document with `Merge.doc` and the attempts with `Merge.attempts`; saves; puts the difference into the outbox; emits `store:change` (source `remote`). The way back in for a file of `exportAll`. |
| `Store.load(docs)`, `Store.reset()` | Preview only (used by shot states and the selftest): `load` replaces the named documents and `attempts` in memory, clears the outbox, writes nothing; `reset` returns every document to its default and clears the `saa1:*` keys. |
| `Store.stamp(name, pathArray, done)` | Convenience for one stamp. |
| `Store.addAttempt(a)` | Adds to the attempts map, queues `set` of `attempts/<id>`, recomputes and queues `coach` (`Scoring.buildCoach`), emits `attempt`. |
| `Store.attempts()` | Array, newest first. |
| `Store.drills()` | Array of valid drill documents (empty without db). |
| `Store.flag(kind, ref, note)` | Queues a flags document; toast "Report saved." |
| `Store.attach(db, uid)` | Section 5.5. Runs once (later calls return the same promise); it may be called late, from the "Save online too" click. |
| `Store.flush()` | Forces an outbox flush; called on `pagehide` and `visibilitychange` to hidden. |
| `Store.status()` | `"cloud"`, `"local"`, `"memory"`. |
| `Store.snapshot()` | For the hot snapshot: `{v: 1, docs: {root, progress, qstats, exam, speak}, outbox, uid}`, plus `attempts` and `drafts` only when the status is `memory` (otherwise they are in localStorage). Plain JSON, under 300 KB. |
| `Store.exportAll()` | `{v, build, exportedAt, root, progress, qstats, speak, attempts, coach}` for "Save my progress". |
| `Store.summaryText()` | The "Copy summary for Claude" text: overall, domains, weak topics, missed ids, cause counts. |

Two tabs: `store.js` listens to the `storage` event for `saa1:*` keys; the changed document is merged into memory with `Merge.doc` and `store:change` (source `remote`) is emitted. Before each localStorage save, `Store` re-reads the key and merges, so two tabs do not overwrite each other.

### 5.5 Cloud sync

`saa1:outbox` is `{"<db path relative to study/<uid>>": {"op": "merge"|"set", "data": {...}}}`. An entry for the same path is merged (`merge`) or replaced (`set`). The key of the root document is `.`; the others are `state/progress`, `attempts/<id>` and so on.

`Store.attach(db, uid)` (the status stays `local` until step 3 resolves; the app never waits for it):

1. If `db` or `uid` is null: stay `local`. Stop.
2. If `saa1:uid` holds another id: move the local documents, attempts and outbox to `saa1:bak:<old uid>` (one backup, replaced each time) and start from defaults (another person used this browser). If `saa1:bak:<uid>` exists for the new id, merge it in and remove it. If `saa1:uid` is empty, local progress is adopted (first signed-in visit). Save `saa1:uid`. A null uid never triggers this.
3. `get()` the four state documents and the root in parallel; `get()` the attempts collection (`orderBy("submittedAt", "desc").limit(200)`). Merge each with local (`Merge.doc`), save, emit `store:change` with source `remote`. Put `Merge.diff(remote, merged)` of each document into the outbox (nothing for a local document with `updatedAt: 0`). Remember which paths exist.
4. Subscribe once each to `state/progress`, `state/qstats`, `state/exam` and the `drills` collection. A snapshot with `hasPendingWrites` is ignored; any other is cloned, merged and saved, and never causes a write. Every `onSnapshot` passes an error callback: `unavailable` re-subscribes once after 5 s; any other code ends that listener, and `revoked` or `not_granted` also ends cloud sync.
5. When `lastSeenAt` is older than one day: queue `update({lastSeenAt})` on the root (`set` of the merged root when it is missing, with `createdAt`). This write never changes `updatedAt`. Set status `cloud`. Flush.

Flush: one write at a time over the whole outbox, in key order. `Store` keeps the set of paths known to exist (from step 3 and from successful writes). `merge` entry: for a known path, `update(data)` directly; an `update` that rejects `invalid_argument` on such a path is retried once as `get()` then `set(local document)`. For an unknown path: `get()`; when the document is missing, `set(local document)`; else `update(data)`. `set` entry: `set(data)`. On success remove the entry. Flushes are scheduled 2 s after the last patch (`qstats`, `progress`), at once for `exam` on answer or flag, and on `pagehide`. The timer never writes.

Errors: `unavailable` or an unknown code: one retry after 1 to 3 s, then wait for the next user action. `invalid_argument` (after the one retry above), `transform_error`, `not_granted`, `revoked`, `capability_disabled`, `capability_removed`: stop cloud sync for the visit, status `local`. `resource_exhausted` (a rate budget, transient): keep the outbox, stay `cloud`, no flush for 30 s, then flush on the next user action; no toast. `quota_exceeded` (permanent): keep the outbox, status `local`, toast "Online storage is full. Progress stays on this device."

### 5.6 Degraded modes and the status line (`#saa-sync`)

| Status | Line | Behaviour |
|---|---|---|
| `cloud` | hidden; "Saved" for 2 s after a flush | Full |
| `local` | "Saved on this device only" | Everything works. About explains that Claude cannot read the progress and offers "Copy summary for Claude", "Save my progress" (`downloads.save`, `saa-progress.json`) and "Restore progress" (8.5). |
| `local`, consent `prompt` | "Saved on this device only" and the button "Save online too" | The click calls `Store.attach(db, uid)`; the platform asks for consent on that first db call. A refusal (`not_granted`) leaves `local` and removes the button for the visit. |
| `local`, consent `denied` | "Saved on this device only" | About also offers "Open permissions" (`permissions.manage()` on click; on a rejection: "Open the Permissions menu of this page to allow saving."). |
| `memory` | "Progress is not being saved on this device" | Everything works until the tab closes; the cloud path still works when db is present (then the line says "Saved online only"). Without db, About offers "Save my progress" and "Restore progress" as the only way to keep it. |

Browser storage is never the only possible copy: in every status without cloud sync she can save a file and load it again (`Store.exportAll`, `Store.importAll`).

## 6. Claude features (implementer E)

### 6.1 `aicore.js` (pure)

| Function | Returns |
|---|---|
| `AICore.CAPS` | `{answer: 4000, question: 500, section: 12000, turns: 3, promptBytes: 200000}`. `promptBytes` is measured in UTF-8 bytes with `U.bytes` (the platform limit is 262144). |
| `AICore.speakPrompt(item, facts, answer)` | The prompt string of `PRODUCT.md` section 2 ("Check my explanation"), with these changes: key points come from `key_points` (`id | kind | point | accept: a; b`); "Common mistakes" lists `must_not_say` as `error -> correct`; "Model answer" is `sixty_second` joined by spaces; facts are `id | claim | "first quote"`; terms are `say | avoid a, b`. The JSON format adds `"moves": {"answer": 0-2, "how": 0-2, "watch": 0-2, "you": 0-2}`, `"heard_as": [{"said": "…", "meant": "…"}]` (at most 3) and `"follow_up": "one question from FOLLOW-UPS"`; a `FOLLOW-UPS` block lists the two follow-up questions. Two rules are added: "Grade facts strictly and English kindly. Never comment on accent or articles." and "moves: 0 missing, 1 partly, 2 clear, for: answer in the first sentence; how it works; one trade-off or limit; an example for the customer and a closing question." |
| `AICore.validSpeak(obj, item, answer)` | `{ok, data}`: checks types; drops entries with unknown `kp` or `fact` ids; clamps `moves` to 0..2; caps lists (`clarity` 3, `heard_as` 3); sets `hit: true|false` on every quote by `AICore.find(quote, answer)`. `ok` is false when `covered`, `missing`, `errors` or `improved` has the wrong type. |
| `AICore.speakScore(data, item)` | `{coverage: {hit, total}, score: 0-10, band, words, seconds, longest}`. `score` = sum of `moves` (0 to 8) + 2 when every must point is covered, + 1 when at least half are; capped at 5 when `errors` is not empty. Bands: 8 to 10 "Customer-ready", 6 to 7 "Correct but incomplete", 0 to 5 "Repair and repeat". `seconds` = words at `shell.json` `wordsPerMinute` (130). The model's `verdict` is not shown. |
| `AICore.askContext(chapter, slug, sid, manifest, glossary)` | `{first: string, sent: [strings]}`: the first turn of `PRODUCT.md` section 2 ("Ask about this section"). BOOK holds the section text (`c.text[sid]`, cut to `CAPS.section`), `[summary]` holds the text of the chapter's sections whose manifest row has role `breath`, `signals` or `recap` (cut to 6,000 characters), `[figures]` holds `figures[id].desc` for `chapter.secs[sid].figs`; FACTS holds `chapter.facts` for `secs[sid].facts`; GLOSSARY the glossary entries for `secs[sid].terms`; INDEX every chapter that is not planned. For a kind 2 section with kind 3 children, the lists of the children are added. The function reads no DOM. `sent` is the list of strings that quotes are checked against. |
| `AICore.askTurns(first, history, question)` | Turns for `sample.json`: the first turn, the last `CAPS.turns` pairs, the question (cut to `CAPS.question`). Turns with empty `content` are dropped; the list starts and ends on `user`. |
| `AICore.validAsk(obj, sent, manifest)` | `{ok, data}`: `status` in the three values; `answer` a string; each `support` gets `hit` by `AICore.find(quote, sent joined)`; `see` filtered to known slugs, at most 2. `data.grounded` is `"all"`, `"some"` or `"none"`. |
| `AICore.find(quote, text)` | Index of `U.norm(quote)` in `U.norm(text)`, or -1; quotes under 12 characters never match. |
| `AICore.message(code)` | `{text, hide: boolean, retry: boolean}` from the table of 6.3. |

### 6.2 Calls (`ai.js`)

- `AI.call` runs `sample.json(input, {modelTier, signal, cache})` only from a click. One call at a time: a second click while busy does nothing. A new `AbortController` per call; `AI.stop()` aborts it. No page-side timeout, no automatic retry.
- Speak check: `modelTier: "default"`, default cache. Ask: `modelTier: "quick", cache: false` (so "Quiz me" or "Give an analogy" pressed twice gives a new answer); "Answer more carefully" repeats the same turns with `modelTier: "default", cache: false`.
- Before the call, the prompt size in UTF-8 bytes is checked against `CAPS.promptBytes`; over it, the section text is cut further.
- Send and Check buttons are disabled while the text is blank.
- After a `hide: true` result, About shows (when `caps.permissions` exists) "Claude features are off for this page." with "Open permissions" (`permissions.manage()` on click).
- `AI.notice()` is the line shown next to every Claude button: "This uses your Claude usage. Claude asks for permission the first time."
- While a call runs: the button is replaced by "Checking…" and a Stop button (`.ai-busy`).
- Her text lives in a `textarea` with a stable id (`sp-answer-<speak id>`, `ask-q`) and is saved with `Store.draft(id, text)` on input (debounced), and restored on mount.

### 6.3 Failure states

| Condition | Behaviour |
|---|---|
| `SAA.state.caps.sample` is null | No Claude controls. Speak shows the self-check only. The Ask button stays `hidden`. |
| `not_granted`, `sampling_disabled`, `not_declared`, `capability_disabled`, `capability_removed` | `hide: true`: hide the Claude controls until reload. Never ask again. |
| `rate_limited` | "Claude is busy or your usage limit is reached. Your text is kept. Try again later." |
| `session_expired` | "Sign in to Claude again, then try again. Your text is kept." |
| `refused` | Clear any shown output. "Claude declined this text. Change it and try again." |
| `invalid_json`, `empty_completion`, or a validator result with `ok: false` | "The reply came back in a broken format. Try again." Manual button only. |
| `prompt_too_large` | "Your text is too long. Shorten it to under 600 words." |
| `cancelled` | Back to idle, no message. |
| `invalid_request`, `transform_error`, `queue_overflow`, `images_unavailable`, `tools_unavailable`, `image_rejected` | "This check cannot run right now." (a page bug; also `console.error`) |
| `upstream_error` or unknown | "Connection problem. Your text is kept. Try again." |

### 6.4 Speak practice (`speak.js`)

One prompt view (`#speak.<slug>.<id>`, and each prompt inside the `say` part) has four steps on one page:

1. **Prompt.** "A customer asks" with the persona, the prompt, the skeleton hidden behind "Show the four cues".
2. **Answer.** A 90-second count-up timer (`shell.json` `speakSeconds`) with Start and Stop, and the textarea (cap 4,000 characters, with a counter). Line under it: "Speak and let your keyboard's microphone type, or type."
3. **Self-check.** The five yes/no boxes of `LEARNING.md` 5.3 as real checkboxes, then the must-say points as a checklist (`.sp-kp`), then "Show the model answer" (10-second and 60-second versions, do-not-say list, follow-up questions). Saving the self-check writes `speak.items[id]` (`t`, `tries` + 1, `self`), stamps `daily.<day>.speak` and emits `speak:done`. Speak is the only writer of that stamp.
4. **Check my explanation** (only with `sample`): the result (`.sp-res`) shows the band and score, the key-point checklist with her quoted words highlighted in her text (`.mk-hit`, only quotes with `hit`), errors with the correction and an evidence chip for a known fact id, unverified statements under "Not checked", term swaps, "Heard as" hints, at most three clarity tips, the improved version with a Copy button, one thing to practise, and the follow-up question. The result is saved to `speak.items[id]` (`score`, `band`, `missing`).

`#speak` is drawn from `Content.sindex()` alone: first "Speaking pack", the entries with `pack` 1 (they live in their own chapters, plus the cross-service items of chapter `speaking-pack`), then all entries by chapter in study order, each with its last band from `speak.items`. A prompt's `d/` file loads when it is opened. `Speak.render` draws one prompt and returns a cleanup function that stops the timer; the `speak` mount uses it for each prompt of the `say` part (`id` empty: all prompts of the chapter, the `pass_route` one first and the others marked "extra" on the Fast and Pass routes). A "Rehearsal" button starts ten random prompts in sequence (interview mode, P2: implement last).

### 6.5 Ask about this section (`ask.js`)

The reader shows `.sec-ask` on every H2 when `caps.sample` is not null. `Ask.open(slug, sid)` opens a sheet: the section title, four fixed prompts as buttons ("Explain more simply", "Give an analogy", "What would the exam ask?", "Quiz me"), the text box (cap 500), the notice line. History is kept in memory per section (not saved).

Result rendering, from `validAsk`:

- `answered` or `partly` with `grounded: "all"`: heading "From this chapter", the answer, the support quotes as links that close the sheet, scroll to the sentence and mark it (`<mark class="mk-hit">`, found by text search inside `#sec-<sid>`). `partly` also shows `missing`.
- `grounded: "some"`: the same, with the line "Some of this could not be matched to the chapter."
- `answered` with `grounded: "none"`: heading "Not verified against the chapter", the answer in a muted block, and "Answer more carefully".
- `not_in_book`: "This section does not cover that.", links to the `see` chapters, and a "Search the book" button (`Search.open(question)`).

### 6.6 Search (`search.js`, `search-worker.js`)

- **Jump-to** (no worker): `Search.jump(text)` ranks chapter titles, section titles and glossary terms from the manifest (prefix match first, then substring). It answers as she types.
- **Full text**: on the first query of three or more characters the worker starts (`new Worker("assets/search-worker.js")`, or a Blob URL of `#saa-worker` in `--single`; `URL.createObjectURL` is allowed only here). The worker never fetches (a relative URL would resolve against `assets/`, and not at all from a Blob URL): the page loads `search/index.json` with `Content.text`, posts its aliases, then loads every shard of the index at once and posts each text in the order of the index (so doc ids, and ties in the rank, are the same on every visit). Nothing is cached in localStorage. Protocol: `{t: "aliases", aliases}` then `{t: "ready", n}`; `{t: "shard", data: <shard text>}` (or `{t: "shard", docs}`) then `{t: "added", n}` (`n`: docs so far) or `{t: "skipped", message}` for a text that is not a shard; `{t: "q", id, text}` then `{t: "r", id, rows: [{route, chapter, heading, kind, snippet}]}`, over the shards added so far, or `{t: "error", message}` before any `aliases` or `shard`. Each shard extends the index; nothing is rebuilt. Index: lowercase word tokens to doc ids. A query term matches a token exactly, by prefix, through `aliases`, or (terms of five or more letters) with one edit of distance. Rank: number of matched terms, then heading matches, then kind order `s`, `g`, `f`, `q`. At most 30 rows; the snippet is 140 characters around the first hit with the hit in `<mark>` (the worker escapes the text).
- While shards are still loading, the results answer over what is in, with the line "Indexing n of m chapters…" above them; each shard that comes in runs the open query again. A shard that cannot be loaded is left out (it counts as done). With 0 shards the search answers "No text matches."
- If the worker cannot start, posts `{t: "error"}`, or `search/index.json` cannot be loaded, only jump-to is offered, with the line "Full-text search is not available right now." The snippet is the only worker output that may be wrapped in `U.raw`.
- The search sheet opens with the Search button or the `/` key (not inside a text field).

## 7. Practice (implementer C)

### 7.1 `scoring.js` (pure)

| Function | Meaning |
|---|---|
| `Scoring.isCorrect(q, picked)` | True when the set of picked option ids equals the set of options with `ok`. |
| `Scoring.scoreAttempt(questions, answers, meta)` | The attempt document of 7.5. `answers` is `{qid: {p: [ids], u, ms}}`; a missing or empty answer is wrong. `meta` is `{id, kind, ref, startedAt, submittedAt, activeSec, limitSec, build, over, first, order}`, copied into the document; the caller computes `first` from `Store.attempts()`. |
| `Scoring.domainBreakdown(questions, answers)` | `{d1: {c, n}, …}`; the `n` values add up to the total. |
| `Scoring.nextBox(rec, ok, unsure, day)` | Wrong: box 0. Correct but unsure: `min(box, 1)`. Correct and sure: box + 1 only when `day` differs from `rec.d`. |
| `Scoring.record(rec, q, picked, ok, unsure, now, cause?)` | The new qstats record (history trimmed to 8). `now` is whole seconds (`U.now()`), passed in by the caller; the pure module reads no clock. |
| `Scoring.inMistakes(rec)` | The history has a `0`, or `u` has a `1`, and `box < 2`. |
| `Scoring.mistakes(qstats, qindex)` | Rows `[{id, slug, d, box, last: "wrong"|"unsure", c, t}]`, sorted: sure-but-wrong first (last result wrong and last flag 0), then box 0, then box 1, each oldest first. The rows hold no stem; a view loads stems with `Content.questions(ids)` for the visible page of 20 rows. |
| `Scoring.retryList(qstats, qindex, n = 20)` | Ids from `mistakes`, at most `n`. |
| `Scoring.buildMix(qindex, qstats, readSlugs, order, day, n = 10)` | `readSlugs`: the slugs with at least one positive read stamp; `order`: `manifest.order`. Ten ids: 4 new core questions (never answered) from chapters she has read, in study order; 3 older (answered correctly, largest age first); 3 from `mistakes`. Shortfalls are filled from the other groups; never pool `mock`. Seeded by `day`, so the mix is stable for the day. |
| `Scoring.returnQuestions(slug, order, qindex, qstats, n = 3)` | Core questions from the chapters 1, 3 and 6 places before `slug` in the study order. |
| `Scoring.confusions(qstats, qindex)` | `[{a, b, n}]`: for each last wrong pick, the pair (question concept, concept of the picked option). |
| `Scoring.gate(attempts, cfg)` | Section 8.3. |
| `Scoring.buildCoach(state, qindex, manifest, now)` | The coach document of 5.2. `state` is `{settings, progress, qstats, speak, attempts}`. |
| `Scoring.validQuestion(dq)` | True when a drill item written by Claude has the DQ shape of 5.2 (plain text, no `_h` field) and exactly `select` options with `ok`. |

### 7.2 The question component (`qview.js`)

`QView.render(el, q, state, opts)`: `state` is `{order: [option ids], picked: [], unsure: 0|1, checked: boolean, stage}`; `opts` is `{mode: "learn"|"exam", stemFirst: boolean, n, of, onChange(state), onCheck(), facts}`. One interactive question is in the DOM at a time.

- Options are real radio inputs (checkboxes for `multi`) inside a `fieldset`, with ids `q-<qid>-o-<option id>` and the group `name` `q-<qid>`, mono letter bubbles A to F in display order, and the `sel` state of the existing artifact. A `multi` question shows "Select TWO" (or THREE) and refuses a pick above `select` with the note "This question takes N answers. Untick one to change your selection."
- The "I am not sure about this one" checkbox (`id="q-<qid>-unsure"`) is on every question. It is the confidence mark and, in the mock, also the flag.
- Keys: A to F pick; left and right arrows move (exam, and learn mode after checking); Enter on the Check button.
- **Stem-first** (`opts.stemFirst`): the options and the unsure box are `hidden`. Panel `.q-sf` asks "What does the question optimize?" with six radio chips (Cost, Operational overhead, Performance, Resilience, Security, Nothing special; left out when `q.opt` is `null`) and "Tap the phrase that decides the answer": every word of the stem is a `<span class="q-w">`; a tap is right when the word lies inside one of `q.kw`. After both steps (right or wrong) the page shows the deciding phrases (`.q-kw`) and the right chip, then the options. "Show the options" skips the step at any time. Stem-first is on while `settings.stemFirst` is `"on"`, or `"auto"` and `qstats.sf < shell.json stemFirstCount` (100). It never applies in the mock, and always applies in `#retry.w`.
- **After Check** (learn mode): each option shows `.opt-tag` with the words "Correct answer" and/or "Your pick", its `why_h`, and for an option with `trap` that is in `Content.meta(q.ch).traps` the link "See the trap" to `#ch.<slug>.<part>.<sid>`; the stem shows the deciding phrases marked; then `expl_h`, `twin_h`, `take_h`, the think-aloud steps when `worked` (an ordered list under "Think aloud"), a "Review: <section title>" link to `q.sec`, and "Report a problem" (a small form: a textarea and Send, calling `Store.flag`).
- **After a wrong or unsure answer**: `.q-cause` asks "Why did you miss it?" with five buttons labelled from the cause codes: "Did not know" (K), "Confused two things" (C), "Missed a word" (W), "Ran out of time" (T), "Old limit in the question" (D). One tap stores `c`. Then a repair line: K links to `q.sec`; C links to the decision atlas chapter (`#ch.decision-atlas`) when it is not planned, else to `q.sec`; W links to `#retry.w`.

`QView.review(el, q, answer, opts)` renders the checked state read-only, for results pages, where many questions are in the DOM together: it renders no form control and no `id`; options are list items marked with the words "Correct answer" and "Your pick". `opts.cause: true` adds the cause buttons (plain buttons with `data-act` and `data-q`).

Before inserting any `_h` field, `QView` calls `Evidence.register(opts.facts)`. For a DQ (5.2) it shows `why`, `expl`, `take` as escaped text.

### 7.3 Quiz sessions (`quiz.js`)

`Quiz.start({kind, ref, ids, title})` runs a learn-mode session: one question at a time, Check, then Next; a progress line "Question 3 of 9"; at the end it writes an attempt (`kind` `chapter`, `drill`, `retry` or `mix`) with `Store.addAttempt` and goes to `#attempt.<id>` with `replace` (score, domain rows, the list of questions with `QView.review`, "Retry the wrong ones"). Each checked answer updates `qstats` at once (`Scoring.record`) and emits `answer`. A session in progress is kept in memory and in the hot snapshot only.

| Route | Ids |
|---|---|
| `#quiz.<slug>` | Ready questions of pool `chapter`: worked examples first, then core (route Fast or Pass), or all (route Full or `.all`). Option order is shuffled per session. |
| `#drill.d<n>` | `q/drill-d<n>.json` |
| `#retry` | `Scoring.retryList` |
| `#retry.w` | Ten questions from `mistakes` with cause W first, then other mistakes, stem-first forced |
| `#mix` | `Scoring.buildMix` |

The `quiz` part of a chapter (reader mount `quiz`, provided by C through `Reader.registerMount`) shows the counts, her last result, and the buttons "Core questions" and "All questions". At the top of the `fast` part, mount `return` (the reader creates the element, section 10) shows up to three return questions as a small inline quiz (P1; the mount stays empty and hidden when fewer than three earlier chapters are read).

### 7.4 The timed mock (`exam.js`)

Port of the engine of `saa-c03-diagnostic.html`. State document `exam`:

```json
{"v": 1, "id": "a-mgq3k2-x7", "kind": "mock", "ref": "mock-exam-1", "build": "3fa9c1d2e0", "phase": "run",
 "startedAt": 1790000000, "updatedAt": 1790000100, "limitSec": 7800, "activeMs": 61000, "cur": 3,
 "order": ["mock-exam-1-q017"], "oo": {"mock-exam-1-q017": ["c", "a", "d", "b"]},
 "ans": {"mock-exam-1-q017": {"p": ["c"], "u": 0, "ms": 84000}}}
```

- **No such mock**: `#mock.<n>` without an entry `n` in `manifest.mocks` shows "Mock exam <n> is not written yet." and a link to the domain drills.
- **Intro** (`#mock.<n>` without a running exam for that mock, always): the count, the time and the domain split from the mock file; when an earlier attempt of this mock exists, the line "Last result: 72% on <date>" linking to `#attempt.<id>`; a checkbox labelled "Add extra time (ESL accommodation): <examFacts.esl.text>" (without that fact the label ends after the bracket and holds no number) that sets `limitSec` to `(minutes + shell.json extraMinutes) * 60` and is remembered in `settings.extraTime`; the rules (answers are final after Submit; unanswered counts as wrong; the timer counts only while the page is open); "Start". If an `exam` document with `phase: "run"` exists for another mock, the intro offers "Resume mock N" and "Discard it".
- **In progress**: the exam bar (`.ex-bar`) with "Answered n/<count>", the timer, "Answer sheet", "Submit". Question order and option order are shuffled once at the start. No feedback before Submit. The answer sheet is the grid of numbered cells (answered, not sure, current) in the right column on desktop and a sheet on a phone. The exam view builds its own two-column grid inside `#saa-view` (`.ex-grid`, in `50-practice.css`); it does not use `#saa-rail`.
- **Timer**: counts active time only, as the existing artifact does: a 1 s interval adds the elapsed delta of `U.nowMs()` when it is under 90 s (the selftest drives it through `Test.clock` and calls the tick function directly). Local save every 10 ticks and on every answer; `Store.patch("exam")` (and so the cloud write) only on answer, flag, navigation to another question, and `pagehide`. `ms` per question is active time on that question. The timer announces at 30, 10 and 5 minutes left. At zero it shows "Time is up. The real exam ends here." and the display turns to "+m:ss over"; she can still submit; the attempt gets `over: 1`.
- **Submit**: an inline confirmation panel (not a dialog call) with the unanswered and not-sure counts. Then `Scoring.scoreAttempt`, `Store.addAttempt`, update `qstats` for every question of the mock, `Store.replace("exam", null)`, and `Router.go("#attempt.<id>", {replace: true})`.
- **Results** (view `attempt`, `#attempt.<id>`, for every kind of attempt; the mock adds the pass note and the timing): the big score in percent, the pass note `examFacts.pass.text` when present, time used, "Sure and correct", the four domain rows with bars and the blueprint strip, the save state line, "Copy summary", and Review with filters Wrong, Not sure, All. Each reviewed question shows the cause buttons. The blueprint strip is `U.bstrip(domains, {pct})`. The dashboard and Today link earlier attempts to `#attempt.<id>`. An unknown id shows "This result is not stored on this device." An attempt without `answers` (trimmed, 5.2) shows the summary and "The answers of this attempt are no longer stored on this device."
- **Resume**: `#mock.<n>` with a running `exam` document for that mock goes straight to the question at `cur`.

### 7.5 Attempt document

```json
{"v": 1, "id": "a-mgq3k2-x7", "kind": "mock|chapter|drill|retry|mix", "ref": "mock-exam-1", "first": 1, "over": 0,
 "startedAt": 1790000000, "submittedAt": 1790007800, "activeSec": 6120, "limitSec": 7800, "build": "3fa9c1d2e0",
 "total": 65, "correct": 47, "pct": 72, "sureCorrect": 39,
 "domains": {"d1": {"c": 13, "n": 20}}, "topics": {"identity": {"c": 4, "n": 6}},
 "order": ["mock-exam-1-q017"], "answers": {"mock-exam-1-q017": {"p": ["c"], "ok": 1, "u": 0, "ms": 84000}}}
```

`first` is 1 when no earlier attempt has the same `kind` and `ref`. `pct` is `Math.round(100 * correct / total)`.

### 7.6 Mistakes log and cards

- `#mistakes`: one row per question in the log: stem start (80 characters), chapter, the last result in words ("Wrong", "Right but not sure"), the cause code with its meaning, the box, and the date. Filters by cause code and by domain. Buttons: "Retry these" (`#retry`), "Ten stem-first questions" (`#retry.w`). Under it "Pairs you confuse" from `Scoring.confusions` (top 5, with the count). A row opens the question in review form with the cause buttons. The same table, short form, fills the `mistakes` mount in chapter 00.
- `#cards.<slug>`: quick review without scheduling. Cards of deck `core` first. A card shows the front (a `number` card shows the cloze as a blank); "Show answer" flips it; then "I knew it" and "Not yet"; "Not yet" cards return at the end of the round, once. `extra_h` and the review link show after the flip. The end stamps `progress.cards.<slug>`. A line says "For daily review with spacing, use the Anki deck (Get files)." The app shows hand cards, word cards (chapter 01) and say cards (chapter 49). The generated term, meaning and partner cards of `data/cards-terms.json` are in the Anki deck only; the glossary covers them in the app.

## 8. Today, plan, dashboard, files (implementer D)

### 8.1 Plan (`plan.js`)

- `settings.plan` (`a` by default) and `settings.planStart` (a local date, set by "Start Day 1 today" or a date input) define the calendar: Day n is `planStart + n - 1`. Without `planStart`, every view shows "Day 1" as the current day and the start button.
- `#plan`: a plan chooser (three radios with the plan titles and notes), then the days in order. Each day (`.pl-day`): "Day 4", its date when known, its minutes, and its tasks as checkboxes (`id="pl-<plan>-<day>-<task>"`). A task with `chapter` links to `#ch.<slug>`; opening that link also sets `settings.routeBy[slug]` to the task's `route`. A tick writes the stamp `progress.plan.<plan>.<day>.<task>`. Gates (`plan.gates`) render after their day as `.pl-gate` with their text.
- The current day is the first day, at or before today's day number, with an unticked task; when all earlier days are done, it is today's day. Days after the last day show "Plan finished".
- Mount `plan` (in `calendar.md`) renders the same day list for the plan id of the region, read-only except the ticks.

### 8.2 Today (`today.js`, view `home`)

Renders at once from local state; refreshes on `manifest`, `store:change` and `caps`. Cards, in order (a card with nothing to show is left out; at most five are visible, the rest behind "More"):

1. **Day card** (`.td-card.is-main`): "Day 4 of 19", plan title, minutes, the tasks of the current day as the same checkboxes, carry-over tasks of earlier days under "Left from Day 3", and a gate text when a gate falls on this day.
2. **Daily minimums** (`.td-min`): the three ticks of `shell.json` `minimums` ("Read 10 pages", "Learn 5 words", "One spoken rehearsal"), stamps under `progress.daily.<day>`. Speak writes the speak stamp (6.4); Today only redraws on `speak:done`.
3. **Continue reading**: the last reader route with the section title.
4. **Daily mix**: "10 questions, about 15 minutes" linking to `#mix`; shows "Done today" when a `mix` attempt exists for today.
5. **Mistakes**: the count in the log and a link to `#retry`.
6. **Say it**: the next speak prompt of the chapters of the current day that has no result yet.
7. **Not cleaned up**: tasks whose `labs.<task id>` has a ticked step and `cleaned` 0, with a link to the cleanup steps.
8. **New since your last visit**: chapters whose `status:rev` differs from `ui.seen[slug]` (`Store.get("ui")`); the list is marked seen with `Store.patch("ui", {seen})` when shown.
9. **Drills from Claude** (P2): documents of `Store.drills()`, each opening a quiz session.

Above the cards: the title block and the blueprint strip with her accuracy per domain, `U.bstrip(manifest.domains, {pct})` (the percent as text).

### 8.3 Dashboard (`dash.js`, view `progress`)

- **Readiness gate** (`.ds-gate`): `Scoring.gate(attempts, cfg)` with `cfg` from `shell.json` `gate` (`strong: 80`, `soft: 75`, `domainMin: 65`, `needed: 2`). It considers mock attempts with `first: 1` and `over: 0`, newest two. Result `{state: "go"|"go-soft"|"not-yet", strong: n, text}`: `go` when both are at or above `strong`; `go-soft` when both are at or above `soft` and no domain of either is under `domainMin`; else `not-yet`. Display: "1 of 2 mocks at 80%" and the state in words; under it the gate texts of the plan. These thresholds are her study rule, not AWS facts; the text says "your rule".
- **Domains**: four rows with accuracy bars over all answered questions, the count, and the exam weight.
- **Coverage**: per part of the book, chapters read on the chosen route (`Content.progress(slug, route, progress)` and nothing else), questions seen of the bank.
- **Mocks and attempts**: the list of attempts (date, kind, score, time), each linking to `#attempt.<id>`.
- **Speaking**: prompts with a band, by band.
- **Weak topics** and **cause counts** from the coach document.
- Buttons: "Copy summary for Claude", "Save my progress" (only with `downloads`).

Charts are `<progress>` elements or `.pbar` bars with a text value; no chart library.

### 8.4 `shell.json`

```json
{"examFacts": {"count": "exam-question-count", "minutes": "exam-duration", "pass": "exam-passing-score",
               "esl": "exam-esl-accommodation"},
 "extraMinutes": 30, "previewMockMinutes": 130, "stemFirstCount": 100, "speakSeconds": 90, "wordsPerMinute": 130,
 "gate": {"strong": 80, "soft": 75, "domainMin": 65, "needed": 2},
 "minimums": [{"id": "pages", "label": "Read 10 pages"}, {"id": "words", "label": "Learn 5 words"},
              {"id": "speak", "label": "One spoken rehearsal"}]}
```

The build copies it into the boot JSON as `cfg`. If the four exam fact ids do not exist in the canon, the orchestrator corrects the ids (the keys stay); the app works without them. `extraMinutes` is only the timer value of her mock setting; the number she reads in the label comes from the `esl` fact. `previewMockMinutes` is used only for the synthetic preview mock.

### 8.5 Get files and About (`files.js`)

- `#files`: one row per `manifest.exports` entry with its size and a Save button: `Content.blob(path)`, then `downloads.save({filename, data})`. `Content.blob` returns a `Blob`; the row refuses an empty blob ("The file could not be loaded."). The row of a `.zip` says "Anki deck (zip): unzip it, then open the `.apkg` file with Anki." Below: "On your laptop these files are in `aws-saa-book/exports/`"; when no `.zip` is in `manifest.exports`, the `.apkg` is named as laptop-only. Errors: `declined` no message; `rate_limited` "A save prompt is already open."; `extension_not_enabled` or `rejected_extension` "This file type cannot be saved here. On your laptop it is at <repo path>."; `too_large` "This file is too large to save here. On your laptop it is at <repo path>."; `unavailable`, `not_granted`, `capability_disabled`, `capability_removed` or an unknown code: hide every Save button for the visit and show the repo paths; `bad_request`, `transform_error`, `request_unknown`: "The file could not be saved." and `console.error`. A resolved `status` other than `"saved"` shows no notice. Without `downloads`, or in `--single`, the view lists the repo paths only. The page never offers Print.
- `#about`: the build id and date, the status of saving (section 5.6) with "Copy summary for Claude", "Save my progress" and "Restore progress", what Claude can read ("The owner of this page, and Claude in the owner's session, can read study progress."), text size, the permission links of 3.7 and 6.2, and "Report a problem".
- **Restore progress** (in every status): `<input type="file" id="about-restore" accept=".json,application/json">` read with `FileReader`, and under it a `textarea` (`id="about-restore-text"`) "or paste the file's text here" with a Restore button, as the fallback when the file picker does not open in the frame. Both call `Store.importAll(JSON.parse(text))`. An inline result line: "Restored 212 answers and 3 attempts." or "This is not a progress file of this book."

## 9. Tests and quality rules

### 9.1 Node tests (no dependencies)

`tests/harness.mjs` exports `load(files, globals?)`, which evaluates the named files of `js/` (an array, in the given order) in one `vm` context that has `globalThis.SAA = {}` and nothing of the DOM, and returns `SAA`; `globals` (an object, for example `{location: {hash: ""}}`) is copied into the context before the files run; `fixture(path)` reads a built JSON file from the folder given as the first command-line argument (default `aws-saa-book/_build/tmp/web-selftest`); and `test(name, fn)`, `eq`, `ok`, which print `ok` / `FAIL` lines and set the exit code. Run: `node aws-saa-book/tools/web/tests/test_scoring.mjs`.

| File | Owner | Must cover |
|---|---|---|
| `test_scoring.mjs` | C | For every question of every built `d/` and `q/` file: the correct set scores true; every single wrong pick scores false; for `multi`, every strict subset and every superset scores false; option order does not matter. All-correct gives 100 and the domain counts add up. `nextBox` rules, `inMistakes`, `retryList` order, `buildMix` composition and day stability, `gate` for go, go-soft, not-yet, and an `over` attempt ignored. |
| `test_merge.mjs` | D | Stamp union and the undo case; later-`t` question records; attempts union; `diff` then `deep` round trip; `keyRev` mismatch ignored; a default document with `updatedAt: 0` never wins over an existing `root` or `exam`; the round trip `exportAll` then `importAll` (through the pure merge functions that `importAll` uses). |
| `test_aicore.mjs` | E | Prompt builders hold every key point id and respect the caps; `validSpeak` drops unknown ids and marks quotes that are not in the answer; `speakScore` caps at 5 with an error; `validAsk` grounding `all`, `some`, `none`; `message` for every code of `sample.d.ts`. |
| `test_content.mjs` | B | The shard rule of `Content.factService` (longest key, the dash, `stray`, unknown ids); `Content.fact` loads only the shard of its service, the index and each shard once per visit, never `facts.json`; a manifest refresh keeps the shards unless the index hash changed; the inline backend of `--single`. With a built folder: `manifest.factsIndex` matches `facts-index.json` (bytes, hash, counts), every shard matches its index row and holds only ids that resolve to it, there is no `facts.json`, and every fact card of the `c/` files is found again through `Content.fact`. |
| `test_search.mjs` | E | The worker: `aliases`, `shard` (text or `docs`) and `skipped`; an index built from two shard messages finds a term of each, answers over the shards so far, and keeps the order of the shards; exact, prefix, one-edit and alias matches; escaped snippets; at most 30 rows. The page (`search.js` with a fake sheet and a `Worker` that runs the real file): "Indexing 1 of 2 chapters" while a shard is late, then results from both; 0 shards; no index. `Search.jump`. With a built folder: no `search/corpus.json`, every built chapter has a shard, every shard matches its index row and holds only its chapter's docs, and the worker indexes all of them. |
| `test_util.mjs` | B | `esc`; `h` escaping, with nested `h`, arrays of `SafeHtml`, `raw`, and `null`/`false`; `norm`; `bytes`; `now` with `Test.clock`; `bstrip` markup; `Router.parse` and `Router.href` round trip (`load(["util.js", "router.js"], {location: {hash: ""}})`; `router.js` touches `window` and `document` only inside `Router.start` and `Router.go`). |

`tools/tests/test_site.py` (A, Python; `python3 aws-saa-book/tools/tests/run.py site`) holds the tests of the build, with the must-fail cases of the shards: a shard above its cap (`WB01` error), a content batch above 255 files (`WB01` error; above 230 a warning), the search budgets (`search/index.json` above 200 KB, a search shard above 800 KB, a warning above 400 KB), and the publish plan of the shards in a multi-file and a `--single` build. `test_search_index_and_shards` checks the search index and shards of the fixture build.

### 9.2 Browser routes (`selftest.js`), read from the dumped DOM

`web selftest` starts `http.server.ThreadingHTTPServer` on `127.0.0.1` port 0 in a thread inside the tool process, serving the preview folder, and calls `saalib.diagram.preview._chrome(url, ["--dump-dom"], 1280, 900, 1, done, timeout=90)` with `done` true when the output holds `SELFTEST PASS` or `SELFTEST FAIL`. Each route writes its result into `<pre id="saa-selftest">` as the last step: `SELFTEST PASS <n>/<n> <name>` or `SELFTEST FAIL <ok>/<n> <name>` followed by one line per failure. The stub runs in mode `ok`; every route first calls `window.claude.__stub.reset()` and `Store.reset()`, so it starts with an empty store. The routes use no real timers longer than 50 ms (Chrome runs with a virtual time budget of 5 s); time moves only through `SAA.Test.clock`.

- `#t.render-all`: loads every chapter, mock and drill file. For every chapter part: mounts it with `Reader.mountHtml` (Markdown parts) or `Reader.runMount` (synthetic parts) and asserts that no text node holds `undefined`, `[object Object]`, `](` or `<!--`, that every `a.ev` has a fact in the file, every `a.xr` resolves through `Content.section` (or names a view route), and every `.mount` has a registered mount. For every question: renders it with `QView.render` and `QView.review` and asserts the option count, exactly `select` options with `ok`, non-empty `why_h` on every option, and no letter reference. For every card (`Cards.render`), speak item (`Speak.render`) and task (`Reader.runMount("task", …)`): renders it and asserts no empty required field. A renderer that is not written yet is counted as skipped, not failed. Last, it loads `facts-index.json` and every shard through `Content.factShard` and asserts that each shard holds the `count` of its index row and only ids that `Content.factService` sends to it, and that every fact card of the loaded `c/` and `d/` files is found again, with the same claim, through `Content.fact` (the path of `#fact.<id>`).
  `web selftest` runs this route twice: at 1280x900 and at 400x860. In the phone run, after each part or question is mounted it also asserts `document.documentElement.scrollWidth <= document.documentElement.clientWidth` and that every element wider than the viewport is inside `.tw`, `.code pre`, `.fig-s` or `.zoom`. A failure names the chapter, the part and the first offending element.
- `#t.exam-sim`: starts mock 1 through the real `Exam` code with `Test.clock` set, answers by a fixed script (all correct in domain 1, all wrong in domain 2, in domain 3 the first `Math.floor(n / 2)` questions in exam order correct and the rest wrong, unanswered in domain 4, five marked not sure), submits, and asserts the score, the domain breakdown, the attempt document in the stub db at `study/stub-user/attempts/<id>`, the `qstats` records, the cleared `exam` document, the coach document, the route `#attempt.<id>`, and that a second run has `first: 0`. The asserts are computed from the `d` values of the mock file, not from fixed numbers. Without any mock in the manifest the route reports `SELFTEST PASS 0/0` with the note "no mock".
- `#t.hot` (C, with D): starts mock 1, answers three questions, takes `App.snapshot()`, round-trips it through JSON, clears localStorage and the modules' memory (`Store.reset()`), then runs `Store.init(snap.store)` and `Router.start({hash: snap.route, view: snap.view})`, and asserts that the route, `cur`, `ans`, `activeMs` and the outbox are restored. It also runs the stub's `__saaRepublish` path once when the stub is in mode `hot`.

JSON of `web selftest`: `{"ok", "render": {"pass": n, "total": n, "skipped": n}, "phone": {"pass": n, "total": n}, "sim": {"pass": n, "total": n}, "hot": {"pass": n, "total": n}, "node": [{"file", "ok"}], "failures": [strings]}`. `--only` takes `render`, `phone`, `sim`, `hot` or `node`. Exit 1 on any failure, 3 when Chrome or node is missing, 5 when Chrome gives no result.

### 9.3 Screenshots

`web shots` captures each state at 1280x900 and 400x860, light (`index.html`) and dark (`index-dark.html`), by screenshotting `http://127.0.0.1:<port>/index.html#t.shot.<name>` through `preview._chrome` with `--screenshot`. File names: `<name>.<desktop|phone>.<light|dark>.png`. Then one `sheet.png` (an HTML grid of the phone-light and desktop-dark images, shot once). A shot state is a function registered with `SAA.Test.register(name, fn(el))` by the owner of the view; it calls `Store.reset()`, fills the store with `Store.load(docs)` as needed, sets `Test.clock` when the view shows a date or a timer, and mounts the real view. Three extra shots: `home.phone.forced-light.png` (`index-forced-light.html`: `<html data-theme="light">`, shot with Chrome's dark colour scheme, to prove the `:not([data-theme="light"])` guard); `prose.mid.light.png` at 1100x800 (the rail column without the hanging margin); and the phone `home` shot is on the contact sheet as the check of the two-row header.

| Name | State | Owner |
|---|---|---|
| `home` | Today on Day 3 with ticks, a mix done, two mistakes | D |
| `chapter` | Chapter top: header, route switch, tabs, first sections | B |
| `prose` | A deep part scrolled to a subsection with callout, table, code and figure | B |
| `evidence` | The same with an evidence popover open | B |
| `glossary` | A glossary popover open | B |
| `toc` | Contents drawer open (phone), contents column (desktop) | B |
| `quiz-open`, `quiz-stemfirst`, `quiz-checked` | A question before checking, in stem-first, and after a wrong answer with the cause buttons | C |
| `mock-run`, `mock-results` | Mock in progress with the answer sheet; results | C |
| `mistakes`, `cards` | Mistakes log; a flipped card | C |
| `plan`, `progress`, `files` | Plan, dashboard with a gate, Get files | D |
| `speak-self`, `speak-result` | Speak self-check; a Claude result from the stub | E |
| `ask`, `search` | Ask sheet with a grounded answer; search with results | E |

The implementer of a view looks at its PNGs with the Read tool before finishing. The contact sheet is the orchestrator's single pre-publish look.

### 9.4 The stub (`stubs/claude-stub.js`, implementer D)

Defines `window.claude = {use(name)}` only when `window.claude` is absent. Mode from `localStorage.saaStub` (`ok` by default; `none`; `errors`; `hot`; `consent`). It exposes `window.claude.__stub = {mode, db, reset()}`; `reset()` empties the stub db, `saaStubDb`, `saaStubHot` and `window.__saaDownloads`. The stub is the only file besides `util.js` that touches browser storage directly.

- `ok`: `user` (`id()` gives `"stub-user"`, `isOwner()` and `canEdit()` true, `can()` true); `db` with `doc`, `collection`, `get`, `set`, `update` (rejects `invalid_argument` on a missing document; deep merge with arrays replaced), `delete`, `onSnapshot` (fires soon after subscribe and after each write; `metadata` present), `orderBy`, `limit`, `where`, kept in memory and mirrored to `localStorage.saaStubDb`, with the path-parity check; `sample` and `sample.json` returning canned replies chosen by a marker in the prompt (a valid speak result built from the prompt's key point ids; a grounded ask result that quotes the first sentence of BOOK); `downloads.save` that records the call in `window.__saaDownloads` and resolves `{status: "saved"}`.
- `none`: every `use()` resolves `null`.
- `errors`: `db` writes reject `unavailable` then `revoked`; `sample.json` rejects with the code in `localStorage.saaStubCode` (default `rate_limited`); `downloads.save` rejects `declined`.
- `ok` also serves `permissions`: `state(name)` resolves `"granted"`, `manage()` resolves.
- `consent`: as `ok`, but `permissions.state("db")` resolves `"prompt"` until the first db call, then `"granted"`.
- `hot`: as `ok`, plus `window.claude.hot = {snapshot(fn), ready(cb), data}`. `snapshot` keeps `fn`; `ready` calls `cb` asynchronously with `JSON.parse(sessionStorage.saaStubHot || "{}")`; `window.__saaRepublish()` stores `JSON.stringify(fn())` in `sessionStorage.saaStubHot` and reloads the page. In the other modes `window.claude.hot` is absent, as outside a viewer.

### 9.5 Source lint (`web lint`, blocking, part of `build web`)

Over `tools/web/shell.html`, `css/*.css`, `js/*.js`, `stubs/claude-stub.js`:

| Code | Rejects |
|---|---|
| `WL01` | A literal colour in CSS or JS: `#` followed by 3, 4, 6 or 8 hex digits, `rgb(`, `rgba(`, `hsl(`, `hsla(`, or a named colour other than `transparent`, `currentColor`, `inherit`, `none` as the value of a colour property. `tokens.json` is the only place for colours. |
| `WL02` | Any `vh` unit (`100vh`, `70vh`, …), except inside `@supports (height: 1dvh)`. Also `overflow-x: hidden` or `clip` on `body`, `.app` or `.shell`. |
| `WL03` | `window.print`, `alert(`, `confirm(`, `prompt(` (as calls) |
| `WL04` | `<a download`, `.download =`, `URL.createObjectURL` outside `search.js` |
| `WL05` | `style.display`, `document.write`, `eval(`; `innerHTML`, `outerHTML` or `insertAdjacentHTML` outside `util.js` (everything goes through `U.set`) |
| `WL06` | A URL to a host other than `fonts.googleapis.com`; `localStorage` outside `util.js` and the stub; `navigator.serviceWorker`; `getUserMedia` |
| `WL07` | An `id="…"` used twice in `shell.html`; an attribute without double quotes |
| `WL08` | A digit string from the set `65`, `130`, `720` next to the word `question`, `minute` or `score` in a JS or CSS file (exam numbers belong to data) |
| `WL09` | `</script` or `<!--` in `js/*.js` (the files are inlined into a `<script>`; write `"<\/script"` if a string needs it) |
| `WL10` | `Date.now(` or `new Date()` without an argument outside `util.js` and the stub (time comes from `U.now`, `U.nowMs`) |

### 9.6 Accessibility and performance rules

- One `h1` per view; landmarks as in 3.6; focus moves to the `h1` on a route change with a polite announcement in `#saa-live`.
- Popovers and sheets: `role="dialog"` with a label, Escape closes, focus returns to the opener, focus is trapped in a sheet. On desktop a popover is anchored to its chip; it never covers the chip.
- Every scroll container is a focusable region with a label. Every figure has `role="img"` on the SVG (from the renderer), a label, and the Describe button, which shows `figures[id].desc`.
- Zoom opens the figure in a full sheet (`.sheet.full .zoom`) with a clone of the first child of `.fig-s` (an `svg`, a `.dg-cmp` or an `img`) at natural size inside a scroll container, plus "+" and "−" buttons that change a scale variable. No pinch code.
- Visible focus on every control; `prefers-reduced-motion` respected; state never by colour alone; form controls have stable ids and labels.
- First load is `index.html` plus `manifest.json`. A chapter costs one fetch (`c/`); its `d/` file loads when a quiz, the `do` or `say` part, or a task mount needs it. `Content.prefetch` loads the next chapter's `c/` file with `requestIdleCallback` (or a 2 s timeout). The icon sprite loads with the first part that has a figure. On the first full-text query the page loads `search/index.json`, then every search shard at once, and posts them to the worker in the order of the index. A fact that no open file holds costs `facts-index.json` and the shard of its service, each once per visit.
- `.sec` (not `.sub`) uses `content-visibility: auto` with `contain-intrinsic-size: auto 40rem`. This applies paint containment, which is why 4.2 keeps the hanging labels and focus rings inside the section's padding box. If B finds a clipped element that 4.2 cannot fix, B drops `content-visibility` (only one part is in the DOM at a time) and says so in the result.
- Resume and the reader's hot snapshot store `{sid, off}`, never an absolute scroll position: an absolute `y` is wrong when the text size, the route or the `content-visibility` estimates differ.
- The Describe and Zoom buttons, `.sec-ask`, Copy: handled by the `#saa` click handler of 3.3. localStorage writes are debounced; db writes are coalesced per document.

## 10. Reader behaviour (implementer B)

- **Chapter header** (`.chh`): the chapter number and title (`h1`), the domains it feeds on the blueprint strip (`U.bstrip(domains, {on: meta.domains})`), the three route times ("Fast 20 min · Pass 65 min · Full 150 min"), the route switch, the part tabs, and the "Aa" menu (text size, skim mode).
- **Route switch** (`.rsw`): radios Fast, Pass, Full. It writes `settings.routeBy[slug]`. Effect on the page: sections and subsections whose `data-route` is beyond the chosen route get `.is-offroute`: they are collapsed to their heading with the line "Not on the Pass route" and an "Open" button (never hidden). Fast: only the `fast` part is on the route. Pass: `fast`, the `pass` subsections of `deep`, the Try with `pass_route`, the speak item with `pass_route`, the core questions. Full: everything. The part tabs mark off-route parts with the word "extra". Chapter progress is `Content.progress(slug, route, progress)`: "sections read of sections on the route". A `.sec` that holds at least one on-route `.sub` is never collapsed; only its off-route `.sub` children are (so on the Pass route "How it works" stays open and shows its Pass subsections). A collapsed section (`.is-offroute` or `.is-gated`) has no sentinel and cannot become read until it is opened. Sections of kind `0` are never collapsed and never counted.
- **Parts**: Markdown parts are mounted with `Reader.mountHtml`. Synthetic parts are rendered by mounts: the reader renders the `<h1>` and then one `<div class="mount" data-mount="M" data-id="">` and runs the mount:

  | Part | Mount | Owner | `id` | Draws |
  |---|---|---|---|---|
  | `do` | `tasks` | B | empty, or the task id of the route's third token (scrolls to it) | every Try and Lab task, each drawn with the code of `task` |
  | (task region in prose) | `task` | B | the task id | one task: steps with real checkboxes that stamp `labs.<task id>.steps.<n>`, the command blocks with Copy, the cost and cleanup callouts, the careful callout from `T.careful`, for a Lab the line "Template on your laptop: <template path>", a "Cleaned up" checkbox that stamps `cleaned` |
  | `say` | `speak` | E | empty (all prompts), or a speak id | 6.4 |
  | `quiz` | `quiz` | C | empty | 7.3 |
  | `sources` | `sources` | B | empty | the list of `sources` with fact chips |
  | (first child of the `fast` part, added by the reader for chapters of tier deep, medium or light) | `return` | C | empty | 7.3 |
  | (regions in prose) | `plan` (D), `mistakes` (C) | | the plan id; empty | 8.1; 7.6 |

  The mount contract: `fn(el, id, ctx)` with `ctx = {slug, part, meta: Content.meta(slug), chapter: <the c file>, data(): Promise<the d file or null>, route: "fast"|"pass"|"full", hot: object|null}`. `fn` may return a cleanup function; the reader calls it before the part leaves the DOM (timers stop there). A mount name that is not registered leaves the element empty and `hidden`. `Reader.runMount(name, el, id, ctx)` runs one mount the same way (used by the selftest and by views that reuse a mount). `Reader.registerMount` is how C, D and E attach.
- **Stop and answer gate** (P1): in a `how` section, a subsection after an unopened Stop-and-answer reveal gets `.is-gated` (collapsed, with "Answer first, or skip"). Opening the reveal lifts the gate; "Skip" lifts it and stamps `chapters.<slug>.skips.<pid>`. No gate applies on a second visit to a read section.
- **Read tracking**: an `IntersectionObserver` on a sentinel at the end of every `.sec` and `.sub`; a section is read when its sentinel is seen at least 8 s after the part was opened. It stamps `chapters.<slug>.read.<sid>`, sets `.is-read`, and emits `section:read`. The rail and the contents list show it with a check mark and the word "Read" for screen readers.
- **Rail** (`#saa-rail`): the H2 and H3 list of the part with scroll-spy (`.is-cur`), time boxes, and read marks. On narrower screens a "Sections" button opens the same list in a sheet.
- **Resume**: the reader saves `ui.pos["<slug>.<part>"] = {sid, off}` with `Store.patch("ui", …)` on scroll (debounced; `off` is the pixel offset inside section `sid`) and restores it when the same part opens without a sid: scroll to the section, then add `off`; it writes `progress.chapters.<slug>.last` and `progress.last` on section change.
- **Previous and next**: at the end of a part, links to the next part on the route, then to the next chapter in study order that is not planned.
- **Evidence chip**: a click on `a.ev` opens the card: the fact id in mono, the claim, each quote with its source link (opens in a new tab), "Checked <date>", the Changed line, and "Report a problem". The link's own route `#fact.<id>` is the fallback.
- **Glossary popover**: the term, how to say it, the plain meaning, "Words that go with it", "Do not confuse with". It stamps `progress.terms.<id>`.
- **Skim mode** (P1): `.is-skim` on `#saa-view` shows, per section, only `.lede`, `.pr-q`, `.bf`, callouts, tables and figures, with a "Show all" button per section. Pure CSS plus one class toggle.
- **Code copy**: `U.copy`; on failure the code is selected and a toast says "Press copy on your keyboard."
- **Contents** (`#saa-toc`): parts and chapters from the manifest with status words and a thin progress bar per chapter for the chosen route (`Content.progress`); the current chapter is expanded to its parts. The list ends with "Reference" (`.toc-ref`): Glossary, Numbers, Traps, Changed recently (only the aliases that exist in `manifest.aliases`), Get files, About. The build writes the same Reference links into the static list.

## 11. Work split

Each implementer owns the listed files and nobody else's. Shared names (namespaces, events, classes, document shapes) are fixed by sections 2 to 9. Everybody registers shot states for their views, writes the node test of their pure module, runs `web lint`, and looks at their screenshots.

| | Owns | Must provide | May call |
|---|---|---|---|
| **A** Site build | `saalib/site.py`, `helpers/site_md.py`, `stubs/skeleton.html`, `tests/test_site.py`, `tests/fixtures/*` | `build web` with all options; the mapping table; every JSON file of 2.4; token CSS and contrast check; budgets; publish plan; `web lint`; `web selftest`; `web shots`; the in-process server; the fixture overlay and the synthetic preview mock; `publish-plan.json` with `url` | `common`, `schemas`, `diagram.pipeline`, `diagram.svg`, `diagram.icons`, `diagram.preview._chrome`; `lint.section_id` when present. Reads `shell.html`, `shell.json`, `tokens.json`, `css/`, `js/` as text. |
| **B** Shell and reader | `shell.html`, `shell.json`, `tokens.json`, `css/10-base.css`, `20-layout.css`, `30-prose.css`, `40-components.css`, `90-phone.css`, `js/util.js`, `content.js`, `router.js`, `popover.js`, `evidence.js`, `glossary.js`, `reader.js`, `boot.js`, `tests/test_util.mjs` | `U`, `bus`, `Test`, `Content`, `Router`, `Pop`, `Evidence`, `Glossary`, `Reader` (with `mountHtml`, `registerMount`, `runMount`), `App`; views `ch`, `glossary`, `fact`, aliases, the not-found view; the `#toc` action; the `#saa` click handler; mounts `task`, `tasks`, `sources`; section 10 | `Store.get`, `Store.patch`, `Store.stamp`, `Store.flag`, `Store.init`, `Store.attach`, `Store.consent`, `Store.snapshot`; `Ask.open` (only when `SAA.Ask` exists); `Search.open` |
| **C** Practice | `css/50-practice.css`, `js/scoring.js`, `qview.js`, `quiz.js`, `exam.js`, `mistakes.js`, `cards.js`, `selftest.js`, `tests/harness.mjs`, `tests/test_scoring.mjs` | `Scoring`, `QView`, `Quiz`, `Exam`, `Cards.render`; views `quiz`, `drill`, `retry`, `mix`, `mock`, `attempt`, `mistakes`, `cards`, `t`; mounts `quiz`, `return`, `mistakes`; section 7; the three selftest routes | `U`, `bus`, `Content`, `Router`, `Pop`, `Evidence.register`, `Reader.registerMount`, `Reader.runMount`, `Store.*`; in `selftest.js` only: `Reader.mountHtml`, `Speak.render`, `App.snapshot` |
| **D** State and planning | `css/60-today.css`, `js/merge.js`, `store.js`, `today.js`, `plan.js`, `dash.js`, `files.js`, `stubs/claude-stub.js`, `tests/test_merge.mjs` | `Merge`, `Store` (5.4), the stub (9.4); views `home`, `plan`, `progress`, `files`, `about`; mount `plan`; sections 5 and 8 | `U`, `bus`, `Content`, `Router`, `Reader.registerMount`, `Scoring.buildCoach`, `Scoring.gate`, `Scoring.mistakes`, `Scoring.buildMix`, `Quiz.start` |
| **E** Claude, speak, search | `css/70-ai.css`, `js/aicore.js`, `ai.js`, `speak.js`, `ask.js`, `search.js`, `search-worker.js`, `tests/test_aicore.mjs` | `AICore`, `AI`, `Speak`, `Ask`, `Search`; view `speak`; mount `speak`; section 6 | `U`, `bus`, `Content`, `Router`, `Pop`, `Evidence`, `Reader.registerMount`, `Store.get`, `Store.patch`, `Store.stamp`, `Store.draft` |

Rules for working in parallel:

- A module must load and the page must render when a later module is missing: guard calls to other owners' namespaces that are not yet written (`if (SAA.Quiz) …`). A view that is not registered shows "This part is not built yet."
- Until A's build exists, B to E develop against a hand-made preview: they may write throwaway files under `_build/tmp/` only.
- Nobody changes a shape, class or function name of this file. A needed change is reported in the result, not made.
- Order of work when time is short (cut from the end): P0 first (reader, contents, evidence, glossary, quiz, mock, mistakes, store, Today, plan, speak self-check, jump-to search), then speak check, dashboard, drills, mix, cards, stem-first, full-text search, Ask, skim mode, the Stop-and-answer gate, return questions, "New since", then P2 (drills from Claude, rehearsal mode).

## 12. After the first publish (orchestrator)

One functional pass, as `PRODUCT.md` section 8 lists: relative `fetch` of `.json`, `.svg`, `.pdf` and the worker; files not re-sent survive; the db rules are accepted and the data tool reads `study/<uid>/state/progress`; one `sample.json` call per tier; `downloads.save` of a `.txt` and a `.pdf`; a hash on the artifact link reaches the page; a republish restores the route and a running mock; the phone app (safe areas, bottom sheet, dictation, the two-row header, the file picker of Restore progress); note whether db asks for consent on first use and what `permissions.state("db")` answers before it. After the first publish the orchestrator writes the artifact `url` into `_build/reports/site-published.json`.

If multi-file fetch fails on the platform, publish `_build/site-single/index.html` **to the same artifact** (pass its `url`), with the same title and the same `capabilities`, and remove the multi-file paths listed in `removed`. Never publish the book as a second artifact: its origin and its database would be new, and her progress would be gone.
