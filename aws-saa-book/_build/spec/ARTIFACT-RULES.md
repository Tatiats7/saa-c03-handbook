# Artifact platform rules (authoritative for the web version)

The web version is published by the orchestrator as a claude.ai Artifact. These rules come from the Artifact tool's own contract. Design within them; do not try to detect or work around them.

## Page contract

- **One page file, `index.html`, authored WITHOUT `<!DOCTYPE>`, `<html>`, `<head>` or `<body>` tags.** At publish time it is wrapped in a skeleton whose head has only a charset, a viewport meta with `viewport-fit=cover`, and a small reset: light `color-scheme`, `:root` padded top and bottom by the phone's safe-area insets, zero body margin, a 14px system font on an off-white ground, `img{max-width:100%}`, `[hidden]{display:none!important}` (toggle visibility with `el.hidden`, not `style.display`). So the file starts with its own `<title>` and `<style>`.
- **Title:** a `<title>` within the first 8 KB. It is the artifact's name: `SAA-C03 Handbook`. Never change it between publishes.
- **Supporting files** (other HTML, CSS, JS, JSON, SVG, PDF, images) are published alongside and served at relative paths. `fetch()` of files published alongside the page works with relative URLs. Other HTML files are served raw (they would need their own doctype and get no skeleton).
- **Limits:** 16 MB per page and per text file; 15 MB per binary file; at most 255 files and 64 MB per publish; 511 files and 256 MB per version. Republishing the same file path updates the same URL in place; open viewers receive the update automatically.
- **CSP (enforced silently):** external scripts ONLY from `https://cdnjs.cloudflare.com` (preferred), `https://cdn.jsdelivr.net/npm/`, `https://unpkg.com`, `https://cdn.tailwindcss.com`, `https://code.jquery.com`; external stylesheets ONLY from `https://fonts.googleapis.com` (font files from `https://fonts.gstatic.com`). Everything else is blocked: other hosts, and on those CDNs anything but a script. No external images, no fetch/XHR/WebSocket to other hosts. Inline all other CSS and JS; embed assets as files published alongside or as `data:` URIs. Load a library as a pinned UMD build placed before the inline script that uses it. Prefer no library at all.
- **The frame blocks, for every viewer:** `window.print()` (never offer Print or Save as PDF); `alert()`, `confirm()`, `prompt()` (confirm returns false, prompt returns null); downloads started by the page (`<a download>`, blob or data links) except through the `downloads` capability; embedding other sites (`iframe`, `object`, `embed`); service workers; WebRTC; camera, microphone, location and similar device APIs. `mailto:` and `tel:` links are unreliable. Links to other sites must be real `<a href="https://...">` and open in a new tab. Web Workers work from published files or blob URLs.
- **Location:** only a plain `#anchor` made of letters, digits and `. _ ~ -` reaches `location.hash`. No `key=value` state, no query string.
- **Forms** work as page UI; handle `submit` with `preventDefault()`. Copy works with `navigator.clipboard.writeText` inside a click handler (catch rejection and fall back to selecting the text). Reading the clipboard never works.
- **Browser storage:** `localStorage`, `sessionStorage` and IndexedDB work per browser only; they survive republishes; they can be empty or throw (private window, cleared data, previews). Wrap every access in try/catch and render correctly without it. Use it for per-viewer conveniences and as a local cache, never as the only copy of state that matters.
- **Open viewers and updates:** register `window.claude?.hot?.snapshot(...)` and boot through `window.claude?.hot?.ready ? window.claude.hot.ready(start) : start(window.claude?.hot?.data ?? {})` so a republish keeps route, reading position and exam state. `hot` is absent outside a viewer, hence the `?.`.

## Responsive and theme rules

- Must work at about 400 px width. The page body never scrolls horizontally. Keep a side gutter of at least 16 px at every width, set once as side padding on one outer wrapper, with vertical padding given by `padding-block` (never a `padding` shorthand that zeroes the sides). Only tables, code blocks and diagrams may be wider than the screen, each inside its own `overflow-x: auto` container. Give flex and grid children that hold text `min-width: 0`.
- Keep the skeleton's `:root` safe-area padding. A sticky header uses `top: env(safe-area-inset-top, 0px)`; a fixed bar stays at `0` and adds the inset to its own padding. Never use `100vh`; size a one-screen view with `height: 100%` on `html` and `body`.
- **Theme has three states.** An explicit choice sets `data-theme="dark"` or `data-theme="light"` on the root; the default sets nothing and only `prefers-color-scheme` applies. Define every colour as a token in exactly this shape:

```css
:root { --bg: ...; --fg: ...; --accent: ... }                       /* every token, light values */
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg: ...; --fg: ...; --accent: ...; color-scheme: dark } }
:root[data-theme="dark"] { --bg: ...; --fg: ...; --accent: ...; color-scheme: dark }   /* same dark values */
body { background: var(--bg); color: var(--fg) }
```

  Every token has its first definition on bare `:root`. No component rule uses a literal colour. `body` sets an explicit background from a token. The two dark blocks carry identical values (generate them from one source).

## Design guidance

- Respect what exists: extend the design system of her existing artifacts (`_build/spec/existing/saa-c03-diagnostic.html`): Archivo (wide) for headings, IBM Plex Sans for body, IBM Plex Mono for ids and numbers, cool paper ground, indigo accent. Google Fonts is the only font host; declare real fallback stacks.
- A utilitarian, polished treatment for hours of reading: real typographic hierarchy, running text near 65 characters wide, a type scale that is kept, `text-wrap: balance` on headings, tabular numerals in tables, layout with flex or grid and `gap`.
- Avoid the generic AI looks: cream with a serif and terracotta; near-black with an acid accent; purple-to-blue gradient heroes; Inter or Space Grotesk; emoji as section markers; everything centred; the same rounded card with an accent rail on every block. Use card styling selectively, by role.
- Structure is information: numbering, labels and dividers must encode something true about the content.
- The page must be complete at rest: the first frame shows real content (title block, exam facts, contents list) without waiting for script or storage. Nothing readable waits at `opacity: 0`.
- Semantic colours (good, warning, bad) are separate from the accent. State is never shown by colour alone.
- Build cleanly: close every element, double-quote attributes, visible keyboard focus, respect `prefers-reduced-motion`, stable `id` on every form control, no overlapping elements, watch selector specificity.
- Copy: write from the reader's side, active voice, plain words, short sentences; errors say what went wrong and what to do. No mannered devices.
- Pre-publish verification allowed: one look at screenshots of a local build (desktop and phone width, light and dark), one pass of fixes, then publish. For a page with capabilities, one functional pass after the first publish.

## Runtime capabilities available to this user

Reached with `const x = await claude.use("name")`, which resolves the namespace or `null` (not served, not granted, or failed to load; indistinguishable by design; `null` after 10 s when no viewer answers). `window.claude` carries only `use`. Never block first paint on a capability; light features up when the promise resolves; design for absence. Authoritative type definitions: `_build/spec/existing/capabilities/*.d.ts` (read them before writing calls).

- `db` (with `user`): documents under access rules, live queries with `onSnapshot`, kept across republishes; Claude can later read and write the same data through a tool. Declared by the orchestrator at publish as `capabilities: {db: {rules: [...]}, user: {}, sample: {}, downloads: true}`. By default signed-in people read shared docs, contributors write, viewers never write. `data/users/<id>/` is private even from the owner, which is why this book uses an owner-readable prefix `study/<uid>/...` with per-path rules (see PRODUCT.md section 3). Even segment counts are documents, odd are collections. Subscribe once per query, never in render; one write at a time per document, only on change. Never hard-code seed data in the page.
- `user`: `id()` (opaque, stable within one owner's artifacts), `isOwner()`, `canEdit()`.
- `sample`: the page asks Claude. `await sample(input, opts)` returns `{text, truncated}`; `sample.json(input, opts)` returns parsed JSON. No memory between calls: send instructions, page data and the output format every time. Options: `onText` streaming, `signal` (a new AbortController per call), `modelTier` quick, default or complex, `cache`. The viewer's own usage is billed and the first call asks consent; call only on a click. Errors reject with `{code, message}`: hide on `not_granted`, back off on `rate_limited`, never loop.
- `downloads`: `await downloads.save({filename, data})` offers a generated or fetched file after the viewer confirms; only certain extensions are allowed (see `downloads.d.ts`; `.apkg` is not among them).
- `permissions` is built in (never declared): `state`, `request`, `manage`.

Only the orchestrator publishes. Agents build and test locally against a stub of `window.claude`.
