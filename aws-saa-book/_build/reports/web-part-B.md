# Web version, part B: shell, CSS, router, content loader, reader, popovers, evidence, glossary

Implementer B, 2026-10-04. Contract: `tools/web/ARCHITECTURE.md` 1.1.

## Files written (all under `aws-saa-book/tools/web/`)

- `shell.html`, `shell.json`, `tokens.json`
- `css/10-base.css`, `css/20-layout.css`, `css/30-prose.css`, `css/40-components.css`, `css/90-phone.css`
- `js/util.js`, `js/content.js`, `js/router.js`, `js/popover.js`, `js/evidence.js`, `js/glossary.js`, `js/reader.js`, `js/boot.js`
- `tests/test_util.mjs`

## What was tested

Sandbox copy of the fixture book (`_build/tmp/web-b-book`, throwaway), with the other owners' files as they were at 23:00.

- `web lint`: 0 findings over 37 files.
- `node tools/web/tests/test_util.mjs`: 23/23 (esc, h, raw, join, set, norm, bytes, clock, bstrip, Router.parse and href round trip, Content.section, routeSections, progress, planned chapter).
- `build web --preview` and `--preview --single`: build without errors (token contrast `WB06` passes).
- `web selftest`: render 3153/3153, phone 3558/3558, sim 294/294, hot 24/24, all node tests ok.
- Screenshots looked at: chapter, prose, evidence, glossary, toc at 1280 px light and dark (`web shots`), and at a true 400 px light and dark through an iframe wrapper (see finding 1). Also looked at: tables (stacked and scrolling), figure with zoom sheet, sections sheet, Aa menu, Fast route (collapsed sections, "extra" tabs), skim mode, Do part, glossary page, sources.

Not exercised in a browser by hand: the Stop-and-answer gate (the fixture has no on-route subsection after a Stop prompt), `content:drop` reload, the hot restore of the reader position, keyboard focus trap of the sheet. They are code-complete and untested.

## Findings for the integrator (not my files)

1. **Phone screenshots of `web shots` and the phone run of `web selftest` are 500 px wide, not 400.** Headless Chrome (`--headless=new`) on macOS does not make a window narrower than 500 px; the PNG is the left 400 px of a 500 px layout (the fifth nav link and the Search button are cut off). A true 400 px check needs an iframe of 400 px inside a wider page (that is how I checked), or device emulation.
2. **A scrolled window gives a blank band at the top of a `--screenshot` PNG** (the sticky header shows in the middle of the image). The `prose`, `evidence` and `glossary` shot states therefore do not scroll: they move the view up with a negative top margin. Other owners' states that scroll the window will show the band.

## Deviations and additions (smallest reading where the contract was silent)

Shell
- Slots: `{{fonts}}` is the whole `<link>` element; `{{css}}` and `{{js}}` are text inside the `<style>` and `<script>` of `shell.html`; `{{boot}}` is JSON text inside `<script type="application/json" id="saa-boot">` of `shell.html` (boot.js also survives a whole element being substituted, it parses from the first `{` to the last `}`); `{{inline}}` is the whole element. This matches what `site.py` does today.
- `#saa-toc`, `#saa-pop` and `#saa-sheet` have `tabindex="-1"` (focus targets). Nav links carry `data-nav`.

Tokens
- Added themed token `scrim` (backdrop of sheet and phone popover). `runtime` also lists `col` (the column width set by `30-prose.css`).
- The text column is `min(var(--measure), 37rem)`: `66ch` of IBM Plex Sans is about 80 characters, 37rem keeps lines near 68.

CSS
- `content-visibility: auto` on `.sec` is dropped (9.6 allows it): it made scroll restore and scroll-spy unreliable; one part is in the DOM at a time.
- Sticky contents and rail columns with their own scroll exist only inside `@supports (height: 1dvh)`.
- The rail column exists only while `#saa-rail` is not hidden (`.shell:has(> .rail:not([hidden]))`), so other views get the full width.
- Element resets use `:where(.app)` (zero specificity) so component rules of every owner win.
- Extra classes: `.sheet-p`, `.sheet-b`, `.sheet-t`, `.pop-h`, `.pop-b`, `.pop-x`, `.fold-n` / `.offr` / `.gate-n` (collapsed notes), `.read-m`, `.skim-all`, `.sen`, `.syn`, `.pn`, `.aa`, `.page`, `.notice-page`, `.linkbtn`, `.fig-desc`, `.zoom-bar`, `.tab-x`, `.srcs`.
- The three route times are shown inside the route switch ("Fast 16 min"), not as a separate line.
- Zoom uses the CSS `zoom` property with `--zoom`.

JavaScript (additions; nothing of the contract was renamed)
- `U.join(list, sep)`, `U.select(el)`, `U.isSafe(v)`. `U.on` returns a remove function and calls `fn(event, matchedElement)`. `U.bstrip` also accepts `opts.gate` and `pct` keys `d1`..`d4`.
- `Content.manifest(true)` refreshes; a chapter whose hash changed is announced with the new bus event `content:drop {slugs}`. `Content.sections(slug, part?)`, `Content.section(slug, "part.sid")`. `Content.sprite() -> Promise<boolean>` fills `#saa-sprite` once. boot refreshes the manifest when the tab becomes visible after 10 minutes.
- `Router.act(name, fn)` (B's `data-act` registry; B's extra names start with `rd-`, plus `retry-load`, `pop-close`, `sheet-close`, `ev-report`), `Router.view(name)`, `Router.reload()`, `Router.loadError(el)`. A view definition may have `update(args) -> boolean` so that a route inside the mounted view (reader section, glossary term) does not remount. `Router.go` also takes `{view, args}`.
- `Pop.sheet` returns the body element (`.sheet-b`); `Pop.isOpen()`, `Pop.sheetOpen()`. Navigation closes popover and sheet.
- `Evidence.card(fact, id?)` (the fact card shape has no id; ids are remembered by `Evidence.register`), `Evidence.get(id)`.
- `Reader.hasMount(name)`. Synthetic parts get an `<h2>` with the part title (the chapter `h1` stays the only `h1`).
- `App.attach()`, `App.textSize(n)`. `App.caps` is `SAA.state.caps`.
- `labs.<task>.cleaned` is written with `Store.patch` as a time or `0` (it is not in the stamp list of 5.2).
- Tab "extra" rule: Fast marks every part except `fast` and `sources`; Pass marks a Markdown part without a Pass section; `sources` is never marked.
- Saved position is not restored when it is the first section with an offset under 200 px (the chapter header stays visible).
- The gate closes only the next subsection, and "read" for the gate is what was read when the part opened.
- Read delay (8 s) and the 12 hour route restore are constants in `reader.js` and `router.js`.
- The literal `"#fact"` is avoided in JavaScript (a naive `WL01` pattern would read `#fac` as a colour); `Router.href("fact", id)` is used.
