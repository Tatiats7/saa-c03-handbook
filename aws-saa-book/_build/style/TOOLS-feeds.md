# TOOLS: feeds (faq, changes, cases)

Module: `aws-saa-book/tools/saalib/feeds.py`. Tests: `python3 aws-saa-book/tools/tests/run.py feeds` (31 tests, offline).

These commands build **indexes for finding things**. They are never evidence.

- A quote for the book always comes from a page snapshot (`snap/<source_id>.txt`), checked with `common.find_quote`.
- Every request goes through `corpus.fetch`: allow-list, `robots.txt`, one request per second, cache.
- What's New and case studies are read only through the directory API. These commands never fetch a What's New post page (`robots.txt` disallows the posts of 2020 to 2024).

All subcommands take `--out FILE`, `--max-lines N` and `--json`. Lists are bounded by `--limit`.

```
python3 aws-saa-book/tools/saa.py faq URL [--list] [--find TEXT]
python3 aws-saa-book/tools/saa.py changes harvest --tag PRODUCT_TAG --service NAME [--since 2022-07-01]
python3 aws-saa-book/tools/saa.py changes history URL --service NAME [--since 2022-07-01]
python3 aws-saa-book/tools/saa.py changes for SERVICE [--since DATE]
python3 aws-saa-book/tools/saa.py changes tags [--find TEXT] [--refresh]
python3 aws-saa-book/tools/saa.py cases harvest [--tag TAG]
python3 aws-saa-book/tools/saa.py cases for TAG
python3 aws-saa-book/tools/saa.py cases tags [--find TEXT]
```

## Files written (under `_build/corpus/`)

| Path | Content |
|---|---|
| `faq/<name>.jsonl` | One row per parsed question |
| `faq/<name>.meta.json` | Summary of the last parse (counts, final URL, pages, warnings) |
| `changes/<service>.jsonl` | What's New items and document-history rows of one service, newest first |
| `changes/_tags.json` | Every What's New tag seen so far |
| `cases/index.jsonl` | Case studies from the customer-references directory, merged by id |
| `snap/api/<directory>-<tag or all>-s<size>-p<page>.*` | The saved API answers (raw JSON) |

`saa.py search --scope faq|changes|cases` searches these files.

## faq

```
saa.py faq URL [--name NAME] [--list] [--find TEXT] [--limit N] [--chars N] [--follow] [--max-pages N] [--revalidate]
```

```
python3 aws-saa-book/tools/saa.py faq https://aws.amazon.com/vpc/faqs/
python3 aws-saa-book/tools/saa.py faq https://aws.amazon.com/ec2/faqs/ --list --limit 20
python3 aws-saa-book/tools/saa.py faq https://aws.amazon.com/vpc/faqs/ --find "stateful" --limit 3
python3 aws-saa-book/tools/saa.py faq https://aws.amazon.com/rds/aurora/faqs/ --follow
```

Output:

```
faq ec2: 537 questions (json 1, legacy 536) in 50 sections
  url=https://aws.amazon.com/ec2/faqs/
  final_url=https://aws.amazon.com/ec2/faqs/
  snapshot=www/ec2/faqs (cached)  pages=1
  index=aws-saa-book/_build/corpus/faq/ec2.jsonl
  not found in the snapshot text: 0 questions, 0 answers; empty answers: 0
```

- The page is fetched once through the corpus (a second run uses the cache; `--revalidate` asks again). The file is rewritten on every run.
- `<name>` comes from the URL: `/vpc/faqs/` gives `vpc`, `/rds/aurora/faqs/` gives `rds-aurora`, `/efs/faq/` gives `efs`. `--name` sets another name.
- Three parsers, marked in the `parser` field:
  - `json`: items embedded in `<script type="application/json">` with `itemHeading` and `itemLongLoc`. The section is the item's first tag name.
  - `legacy`: `Q:` paragraphs. They are read inside the JSON items (EC2 keeps many `Q:` paragraphs in one item) and in the visible text. The answer runs to the next `Q:` line or heading. The section is the headings above, joined with ` / `.
  - `markdown`: docs guide pages. A heading that ends with `?` is a question; other headings are sections.
- Row fields: `id` (`<name>#<position>`), `name`, `position`, `section`, `question`, `answer`, `parser`, `source_id`, `url`, `final_url`, `line` (line of the question in the snapshot `.txt`, or null), `question_in_text`, `answer_in_text`.
- `question_in_text` and `answer_in_text` say whether `common.find_quote` finds the parsed text in the snapshot. When `answer_in_text` is false, read the snapshot with `saa.py show <source_id> --lines <line>:<line+20>`.
- **Aurora.** `https://aws.amazon.com/rds/aurora/faqs/` redirects to the docs guide `rds/latest/auroraextendedcontent/aurora-faq.html`. The snapshot stays under `www/rds/aurora/faqs`; `final_url` is recorded and the summary says `(redirected)`. The landing page has 7 questions. `--follow` reads the guide's `llms.txt` and parses the pages whose name starts with the landing page name (`aurora-faq-performance`, `aurora-faq-security`, ...; 10 pages, at most `--max-pages`, default 15). Each of those pages is a normal snapshot (`docs/rds/latest/auroraextendedcontent/aurora-faq-security`) and its rows carry that `source_id` and `url`.
- `--list` prints `position [section] question`, 60 rows by default. `--find TEXT` prints matching questions with the answer cut to `--chars` (default 700), 5 by default.
- Exit codes: 0 questions parsed; 2 no question parsed (the file is written empty); 1 page not found, or `--find` without a match; 4 host or `robots.txt` refusal; 5 transient.

## changes harvest (What's New)

```
saa.py changes harvest --tag PRODUCT_TAG --service NAME [--since 2022-07-01] [--page-size 1000] [--max-pages 10] [--refresh]
```

```
python3 aws-saa-book/tools/saa.py changes harvest --tag amazon-vpc --service vpc
```

```
whatsnew amazon-vpc -> vpc: read 200 of 298, kept 124, added 124, file now has 147 rows
  file=aws-saa-book/_build/corpus/changes/vpc.jsonl
  since=2022-07-01
  newest=2026-09-29
  oldest_read=2020-03-03
  stopped=since
```

- It calls `https://aws.amazon.com/api/dirs/items/search?item.directoryId=whats-new-v2&sort_by=item.additionalFields.postDateTime&sort_order=desc&size=N&item.locale=en_US&page=P&tags.id=whats-new-v2%23general-products%23<tag>`.
- The page size is at most 1000. Reading stops at the end of the list (`stopped=end`), when a page ends before `--since` (`since`), at `--max-pages` (`max-pages`), or at the API paging limit of offset 10,000 (`paging-limit`). The date filter is done in the script. A harvest that stops early without reaching `--since` gives a warning and exit 2.
- Run it once per tag. Several tags can feed one service file (for example `amazon-vpc` and `aws-privatelink` into `vpc`); rows are merged by item id, so a second run adds nothing.
- The API answers are cached like any snapshot. `--refresh` asks the API again.
- Row fields: `date` (from `postDateTime`), `title`, `summary` (first 400 characters of the post text), `url` (the post URL, for citing only), `source` = `whatsnew`, `service`, `id`, `tag`, `product_tags` (all product tags of the item), `text` (whole post text), `api_source_id`.
- Exit 1 when the tag has no item (find the tag with `changes tags`), exit 3 for a bad `--since` or tag.

## changes history (document history page)

```
saa.py changes history URL --service NAME [--since 2022-07-01] [--revalidate]
```

```
python3 aws-saa-book/tools/saa.py changes history https://docs.aws.amazon.com/vpc/latest/userguide/WhatsNew.html --service vpc
```

- Get the URL from the guide index (`saa.py guide ROOT` prints the `history` pointer; the page name differs per guide).
- The page is fetched as a normal docs snapshot. Every Markdown table with a date column is read (a header that contains "date", or a column where most cells are dates). Dates such as `November 21, 2025`, `21 Nov 2025`, `2025-11-21` and `March 2023` (stored as the first day, `date_precision` = `month`) are understood.
- Row fields: `date`, `title` (the "Change" cell without links), `summary` (the "Description" cell), `url` (the history page, `.html`), `source` = `history`, `service`, `link` (the first link in the row), `date_text`, `date_precision`, `history_source_id`, `line`, `quote` (the table row exactly as written, so `common.find_quote(row["quote"], page_text)` matches), `table_header`.
- Rows without a readable date are skipped and counted (warning, exit 2). A page without any dated table row: exit 1, nothing is stored.

## changes for

```
saa.py changes for SERVICE [--since DATE] [--source whatsnew|history] [--find TEXT] [--limit N] [--verbose]
```

```
python3 aws-saa-book/tools/saa.py changes for vpc --since 2025-11-01 --limit 6
```

```
2026-08-07  whatsnew  Amazon VPC IPAM now supports BGP route protection monitoring and delegated RPKI for BYOIP prefixes
    https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-vpc-ipam-bgp-rpki-byoip/
...
6 of 17 change items shown for vpc since 2025-11-01. Dates and deltas only; current truth comes from the guides.
```

- Newest first, 40 rows by default (at most 500). `--verbose` adds the summary. `--find` searches title, summary and post text. No request is made.
- Exit 3 when the service has no feed yet, exit 1 when nothing matches.
- Change items are Tier 3: they give dates and "what changed". The current value is always taken from a guide page.

## changes tags

```
saa.py changes tags [--find TEXT] [--refresh] [--pages N] [--all-namespaces] [--limit N]
```

```
python3 aws-saa-book/tools/saa.py changes tags --refresh
python3 aws-saa-book/tools/saa.py changes tags --find gateway
```

- The site's tag-list endpoint (`/api/dirs/tags/search`) is disallowed by `robots.txt`, so tags are collected from items. `--refresh` reads the newest What's New items without a tag filter (`--pages`, default 3 requests of 1000 items, at most 10) and stores every tag in `changes/_tags.json`. Every `changes harvest` also adds the tags it sees.
- Output: `tag  count`. The count is the number of items with that tag in the last `--refresh` sample (0 for a tag that was only seen in a harvest). One page of 1000 items gave 176 product tags on 2026-10-05. A rarely used tag may be missing; raise `--pages`, or try the name directly with `changes harvest` (an unknown tag exits 1).
- The default list has product tags only (`whats-new-v2#general-products#<tag>`). `--all-namespaces` adds year and category tags.
- Exit 3 before the first `--refresh` or harvest, exit 1 when nothing matches.

## cases harvest

```
saa.py cases harvest [--tag TAG] [--page-size 1000] [--max-pages 10] [--refresh]
```

```
python3 aws-saa-book/tools/saa.py cases harvest --tag dynamodb
python3 aws-saa-book/tools/saa.py cases harvest
```

- It calls the same API with `item.directoryId=customer-references`, sorted by `sortDate`, newest first. With `--tag` the filter is `tags.id=GLOBAL%23product%23<tag>` (for example `dynamodb`, `s3`, `ec2`, `lambda`). Without `--tag` it reads the whole directory (about 4,300 items, 5 requests).
- Rows are merged into `cases/index.jsonl` by id; a second harvest adds nothing.
- Row fields: `id`, `title`, `customer`, `url` (without tracking parameters), `date` (`sortDate`, else the creation date), `tags` (product tag names such as `dynamodb`), `tag_names`, `summary`, `segments` (for example `startup`, `enterprise`), `industry`, `location`, `content_type`, `languages`, `english`, `fetchable` (the page host is in the allow-list), `source`, `api_source_id`.
- Exit 1 when the tag has no item, exit 2 when the harvest stopped before the end.

## cases for, cases tags

```
saa.py cases for TAG [--find TEXT] [--segment NAME] [--since DATE] [--all-languages] [--limit N] [--verbose]
saa.py cases tags [--find TEXT] [--limit N]
```

```
python3 aws-saa-book/tools/saa.py cases for dynamodb --segment startup --limit 3 --verbose
python3 aws-saa-book/tools/saa.py cases tags --find s3
```

```
2023-12-17  Freecharge | Freecharge Transforms Its Digital Payment Platform on AWS to Improve Market Competitiveness
    https://aws.amazon.com/solutions/case-studies/freecharge-in/
    [startup] Financial Services; India; tags: dynamodb, ec2, eks
    Freecharge modernized its application stack using Amazon DynamoDB and Amazon EKS, ...
3 of 28 case studies shown for tag dynamodb. This index is for discovery; fetch the page and quote from its snapshot.
```

- `cases for` reads only the local index (no request). English case studies only, unless `--all-languages`. 20 rows by default.
- `cases tags` lists the product tags in the local index with the number of case studies and the product name.
- To use a case study in the book: `saa.py fetch <url>`, then quote from that snapshot. The `summary` here is directory text and is never quoted.
- Exit 3 when the index does not exist, exit 1 when nothing matches.

## Python API

```python
from saalib import common, corpus, feeds

summary = feeds.build_faq(url, name=None, revalidate=False, follow=False, max_pages=15)   # summary["rows"]
rows    = common.read_jsonl(common.CORPUS / "faq" / "vpc.jsonl")
result  = feeds.harvest_whatsnew("amazon-vpc", "vpc", since="2022-07-01")
result  = feeds.harvest_history(history_url, "vpc", since="2022-07-01")
rows    = feeds.changes_for("vpc", since="2025-01-01", source="", find="")
result  = feeds.harvest_cases("dynamodb")
rows    = feeds.cases_for("dynamodb", find="", segment="startup", since="", all_languages=False)
feeds.parse_date("November 21, 2025")      # ("2025-11-21", "day")
feeds.parse_history(markdown_text)         # {"rows": [...], "undated": n, "tables": n}
feeds.parse_legacy(visible_text)           # 'Q:' paragraphs
feeds.parse_markdown_faq(markdown_text)    # docs FAQ pages
feeds.parse_faq_html(raw_html, visible_text)
```

Errors: `feeds.FeedError` (has `.exit_code`) and the `corpus` error classes.

## Checked against the live sites (2026-10-05, 18 requests including robots.txt, sandbox `_build/tmp/feeds-live`)

| Check | Result |
|---|---|
| EC2 FAQ | 537 questions (536 `Q:` paragraphs, 1 JSON item); the visible text has 538 `Q:` lines; every parsed question and answer is found in the snapshot text |
| VPC FAQ | 169 questions from the embedded JSON, each with its section |
| Aurora FAQ | redirect recorded; 7 questions on the landing page; `--follow --max-pages 2` gave 27 questions from 3 pages (8 more pages listed) |
| VPC document history | 61 dated rows, 23 since 2022-07-01, newest 2025-11-21 |
| What's New, tag `amazon-vpc` | 298 hits; the first 200 already reach back to 2020, 124 kept since 2022-07-01 |
| Tag sample | 176 product tags in the newest 1000 items |
| Case studies, tag `dynamodb` | 405 of 405 read in two pages of 250 (the `page` parameter works); 28 English case studies with the `startup` segment |
| `/api/dirs/tags/search` | refused by `robots.txt` (exit 4, no request) |

The real corpus is still empty: nothing was harvested outside the sandbox.
