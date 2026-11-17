# TOOLS: corpus (fetch, guide, search, show, tables)

Module: `aws-saa-book/tools/saalib/corpus.py`. Tests: `python3 aws-saa-book/tools/tests/run.py corpus` (34 tests, offline).

This module is the only network path for evidence. Every command is one plain command from the repo root:

```
python3 aws-saa-book/tools/saa.py <subcommand> ...
```

All five subcommands take `--out FILE`, `--max-lines N` and `--json`. No command prints a whole page. `fetch` and `guide` never print page text at all.

## Where things are saved (under `_build/corpus/`)

| Path | Content |
|---|---|
| `snap/<source_id>.raw` | Bytes as fetched |
| `snap/<source_id>.txt` | The evidence text: the Markdown itself for docs pages, visible text for HTML pages, the body as it is for JSON and plain text |
| `snap/<source_id>.meta.json` | `source_id, url, fetched_url, final_url, status, content_type, etag, last_modified, sha256, text_sha256, fetched_at, title, bytes`, plus `kind` (markdown, html, json, text, binary) and, when present, `revalidated_at`, `previous_sha256`, `previous_fetched_at` |
| `full/<guide-id>.md` (+ `.md.meta.json`) | Whole-guide Markdown. For search only. Cite page snapshots, never `full.md` |
| `index/<guide-id>.json` | Page list of a guide with history and quota pointers |
| `history/<source_id>.<date>.<sha8>.txt` | Old text of a snapshot that a revalidation replaced |
| `robots/<host>.json` | Cached `robots.txt` (24 hours) |
| `rate.json`, `rate.json.lock` | Last request slot and the daily request counter |
| `fetch.log.jsonl` | One line per HTTP request: `ts, url, status, bytes, ms, attempt, source_id` (and `error`, `refused`) |

`source_id` rules: `docs.aws.amazon.com/<path>.html` (or its `.md` twin) gives `docs/<path>`; `aws.amazon.com/<path>/` gives `www/<path>`; `d1.awsstatic.com/<path>` gives `static/<path>`; `repost.aws/<path>` gives `repost/<path>`; `pricing.us-east-1.amazonaws.com/<path>` gives `pricing/<path>`; `aws.amazon.com/api/...?item.directoryId=X&...` gives `api/X-<8 hex of the query>`. Other URLs with a query get `~q<8 hex>` appended. `llms.txt` keeps its name (`docs/vpc/latest/userguide/llms.txt`).

## fetch

```
saa.py fetch URL... [--batch FILE] [--revalidate] [--binary-to PATH] [--reextract]
```

Examples:

```
python3 aws-saa-book/tools/saa.py fetch https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html
python3 aws-saa-book/tools/saa.py fetch https://aws.amazon.com/vpc/faqs/ --json
python3 aws-saa-book/tools/saa.py fetch --batch aws-saa-book/_build/tmp/urls.txt --out aws-saa-book/_build/reports/fetch-w2.txt
python3 aws-saa-book/tools/saa.py fetch https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html --revalidate
python3 aws-saa-book/tools/saa.py fetch https://d1.awsstatic.com/<path>/icons.zip --binary-to aws-saa-book/_build/tmp/icons/icons.zip
```

Output per URL (text mode):

```
fetched docs/vpc/latest/userguide/nat-gateway-basics status=200 kind=markdown bytes=5385 title='NAT gateway basics'
  txt=aws-saa-book/_build/corpus/snap/docs/vpc/latest/userguide/nat-gateway-basics.txt
  meta=aws-saa-book/_build/corpus/snap/docs/vpc/latest/userguide/nat-gateway-basics.meta.json
```

The first word is the state: `fetched` (new), `cached` (no request made), `not-modified` (304), `unchanged` (200 with the same bytes), `changed` (200 with new bytes; the old text is kept under `history/`), `re-extracted`, or `error`.

Behaviour:

- **Allow-list.** Only the hosts in `common.ALLOWED_HOSTS`, exact match, https, no credentials, no custom port. Anything else: exit 4, no request.
- **Redirects** are followed hop by hop (at most 5) and only inside the allow-list. `final_url` is recorded. `url` and `source_id` stay those of the URL you asked for. Compare `final_url` with `url` when a page may have moved (for example the Aurora FAQ, or a wrong CLI reference URL that redirects to an index page).
- **robots.txt** is fetched once per host per 24 hours and obeyed with RFC 9309 matching (group `*`, longest match, `*` and `$` wildcards, Allow wins a tie). A disallowed URL: exit 4. A 4xx answer for `robots.txt` means "no restrictions" (RFC 9309). A 5xx answer means nothing is fetched from that host (exit 5).
- **Rate.** One request start per second across all processes (a slot is reserved in `rate.json` under `rate.json.lock`). A `Crawl-delay` for `*` larger than 1 second is respected up to 10 seconds.
- **Daily cap.** 6,000 requests per UTC day (environment variable `SAA_FETCH_DAILY_CAP` changes it). When it is used up: exit 4 and the batch stops.
- **Retries.** 429, 5xx and network errors are tried 4 times with waits of 2, 6 and 15 seconds (or `Retry-After`, at most 120 seconds). Then exit 5.
- **Other final answers** (404, 403, ...): exit 1, nothing stored. In `--json` the row has `status`.
- **Docs pages.** For a `docs.aws.amazon.com/....html` URL the tool requests the `.md` twin and stores that Markdown as `.txt`. If the twin is missing (not 200, not Markdown, or a redirect away from `.md`), it fetches the HTML and stores its visible text. `url` in the meta is always the `.html` URL; `fetched_url` shows which one was stored; `kind` is `markdown` or `html`.
- **HTML pages.** Visible text through `html.parser`: `script`, `style`, `nav`, `header`, `footer`, `noscript`, `template`, `svg` and `iframe` are dropped. Headings become `# ...` lines, list items `- ...` lines, table rows `| a | b |` lines (with a `| --- |` rule after a header row, so `tables` also works on HTML snapshots). Link text is kept. `common.normalize_text` removes these prefixes, so quotes match either form.
- **JSON and plain text** are stored as they are.
- **Cache.** A saved snapshot is returned without a request. `--revalidate` sends `If-None-Match` and `If-Modified-Since` for the stored `fetched_url`; on 304 the snapshot is kept and only `revalidated_at` is added.
- **`--binary-to PATH`** takes exactly one URL and saves the bytes to PATH (inside `aws-saa-book/`, else exit 4) with `PATH.meta.json` beside it. It does not create a snapshot.
- **`--reextract`** rebuilds `.txt` from the saved `.raw` without a request (use after an extractor fix). It takes URLs or source_ids.
- **Batch exit code:** 4 if any policy refusal, else 1 if any hard failure, else 5 if any transient failure, else 0. Each URL has its own result line.

## guide

```
saa.py guide ROOT [--id ID] [--revalidate]
```

```
python3 aws-saa-book/tools/saa.py guide https://docs.aws.amazon.com/vpc/latest/userguide/
```

Output (checked live on 2026-10-05):

```
guide vpc-userguide: 'Amazon Virtual Private Cloud User Guide', 204 pages
  index=aws-saa-book/_build/corpus/index/vpc-userguide.json
  full=aws-saa-book/_build/corpus/full/vpc-userguide.md bytes=1232745 fetched
  history: 'Document history' docs/vpc/latest/userguide/WhatsNew (score 18)
  quotas:  'Quotas' docs/vpc/latest/userguide/amazon-vpc-limits (score 12)
```

- It makes two requests: `<root>llms.txt` (saved as a normal snapshot) and `<root>full.md` (saved under `full/`). It does not fetch the pages.
- The guide id is the URL path without `latest`, as a slug: `vpc-userguide`, `amazons3-userguide`, `autoscaling-ec2-userguide`, `elasticloadbalancing-application`. `--id` sets another id.
- Index keys: `guide_id, root, title, llms_url, llms_source_id, full_md, built_at, page_count, links_outside_guide, history, quotas, history_candidates, quotas_candidates, warnings, pages`. Each page is `{title, url, md_url, source_id}`. Only links inside the guide root are listed.
- `history` and `quotas` are best-effort pointers chosen by link text and page name (the names differ per guide). Each has a `score`; the top 5 candidates are also saved. A missing pointer or a missing `full.md` gives a warning and exit 2; the index is still written.
- A root without `llms.txt` (for example the CLI command reference): exit 1.

## search

```
saa.py search PATTERN [--scope full|snap|faq|changes|cases|all] [--guide ID] [--regex] [--limit N] [--per-file N]
```

```
python3 aws-saa-book/tools/saa.py search "scales up to 100 Gbps" --scope full
python3 aws-saa-book/tools/saa.py search "NAT gateways per Availability Zone" --scope snap --guide vpc-userguide
python3 aws-saa-book/tools/saa.py search "up to \d+ Gbps" --regex --limit 10
```

```
full:vpc-userguide:7843 [NAT gateway basics]  + A NAT gateway supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps. If you require more...
1 of 1 hits shown; 1 of 1 files matched (scope full, limit 20)
```

- A hit is `source:line [nearest heading]  context`, with about 200 characters of context around the match. `source` is a source_id for snapshots, `full:<guide-id>` for a whole-guide file, or `<scope>:<file>` for the faq, changes and cases stores.
- Matching ignores case, Markdown backslash escapes and the amount of white space. It works line by line.
- Default scope is `all`. Default `--limit` is 20 (at most 200). Default `--per-file` is 5 (0 removes the per-file limit).
- `--guide ID` limits the search to that guide's `full.md` and its saved pages (it needs the guide index).
- Exit 0 with hits, exit 1 with no hit or a bad regular expression.
- A hit in `full:<guide-id>` is a pointer, not evidence. Find the page in the guide index, `fetch` it, and quote from the page snapshot.

## show

```
saa.py show SOURCE [--around TEXT] [--occurrence N] [--lines A:B] [--chars N]
```

```
python3 aws-saa-book/tools/saa.py show docs/vpc/latest/userguide/nat-gateway-basics --around "scales up to 100 Gbps" --chars 500
python3 aws-saa-book/tools/saa.py show full:vpc-userguide --lines 7840:7850
python3 aws-saa-book/tools/saa.py show https://aws.amazon.com/vpc/faqs/ --around "What is Amazon Virtual Private Cloud"
```

- SOURCE is a source_id, a URL, `full:<guide-id>`, or a `<scope>:<file>` label printed by `search`.
- The first output line is a header: `[source] lines A-B of N | match at line M | url | fetched <time>`. The text follows exactly as saved (use it for verbatim quotes).
- Without options it prints the start of the file. `--chars` is the size of the excerpt (default 2,000, at most 12,000). `--lines` prints at most 400 lines and 12,000 characters. `--around` grows the excerpt by whole lines around the match; one very long line is cut around the match and marked `truncated`.
- Exit 3 when the source is not saved, exit 1 when `--around` text is not found.

## tables

```
saa.py tables SOURCE [--index N] [--all]
```

```
python3 aws-saa-book/tools/saa.py tables docs/vpc/latest/userguide/amazon-vpc-limits
python3 aws-saa-book/tools/saa.py tables docs/vpc/latest/userguide/amazon-vpc-limits --index 2 --json
```

```
[docs/vpc/latest/userguide/amazon-vpc-limits] 11 tables | https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html
table 2 at line 40, 5 rows, under heading 'Gateways'
  header: | Name | Default | Adjustable | Comments |
```

- Without `--index` it lists every table (index, line, row count, nearest heading above, header row). `--index N` (0-based) or `--all` adds the rows.
- JSON for a table: `{index, line, heading, header_text, headers, rows}`. A row is `{line, text, cells}` where `cells` maps each header cell to the cell text and `text` is the row as written. Cell text and `text` are verbatim (only trimmed), so `common.find_quote(row["text"], page_text)` matches. Quote a limit as the row plus `header_text`, so that "5" is known to sit under "Default".
- Empty header cells become `col1`, `col2`, ...; a repeated header gets ` (2)`. Tables inside code fences are ignored.
- Exit 2 when the page has no table, exit 3 when the source is not saved.

## Python API (for other modules)

```python
from saalib import common, corpus

sid   = corpus.source_id_for("https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html")
paths = corpus.snapshot_paths(sid)          # {"raw": Path, "txt": Path, "meta": Path}
text  = corpus.load_text(sid)               # str, or None when not saved
meta  = corpus.load_meta(sid)               # dict, or None
meta  = corpus.fetch(url, revalidate=False) # meta dict plus "state"; no request when cached
meta  = corpus.fetch(api_url, source_id="api/whats-new-vpc-p1")   # name an API response yourself
ok    = common.find_quote(quote, text) is not None
```

| Function | Returns |
|---|---|
| `fetch(url, revalidate=False, source_id=None)` | Meta dict plus `state`. Raises `PolicyError` (host, robots.txt, daily cap as `CapError`), `TransientError`, or `FetchError` (final non-200; `.status`, `.final_url`) |
| `fetch_file(url, dest, revalidate=False)` | Saves bytes to `dest` with `dest.meta.json`; same checks and errors |
| `reextract(source_id)` | Rebuilds `.txt` from `.raw` |
| `build_guide(root, guide_id=None, revalidate=False)`, `load_index(guide_id)`, `guide_id_for(root)` | The guide index dict |
| `search_corpus(pattern, scope="all", guide=None, regex=False, limit=20, per_file=5)` | `{total_hits, shown, hits: [{source, line, heading, context}], ...}` |
| `excerpt(source, around=None, lines=None, chars=2000, occurrence=1)` | `{source, url, fetched_at, start_line, end_line, total_lines, match_line, truncated, text}` |
| `parse_tables(text)`, `tables_for(source)` | List of tables (see above). `tables_for` raises `MissingSource` |
| `resolve_source(spec)` | `(label, path, meta)` |
| `html_to_text(html)` | `(visible text, title)` |
| `requests_today()` | Requests counted today |

Every error class has `.exit_code` (`PolicyError` 4, `TransientError` 5, `FetchError` 1, `MissingSource` 3). In tests, patch `corpus._transport` (signature `(url, headers, timeout) -> (status, lower-case headers dict, body bytes)`, no redirect following), `corpus._sleep`, `corpus.MIN_INTERVAL` and `common.CORPUS`; see `tools/tests/test_corpus.py`.

## Checked against the live sites (2026-10-05, 8 requests, in a sandbox)

- VPC guide: `llms.txt` lists 204 pages; `full.md` is 1.2 MB; history page `WhatsNew`, quotas page `amazon-vpc-limits`.
- `nat-gateway-basics.html`: the `.md` twin is served as Markdown; `--revalidate` returned 304.
- `amazon-vpc-limits`: 11 tables, each with the header `Name | Default | Adjustable | Comments`.
- `https://aws.amazon.com/vpc/faqs/`: 778 KB of HTML gives 518 lines of visible text; questions come out as `####` headings with the answers below them.
- The sandbox is `aws-saa-book/_build/tmp/corpus-live`. The real corpus is still empty.
