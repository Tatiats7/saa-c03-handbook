"""feeds: convenience indexes built on top of the corpus (FAQ questions, change feeds, case studies).

Subcommands: faq, changes (harvest, history, for, tags), cases (harvest, for, tags).
Documentation: _build/style/TOOLS-feeds.md

Stores under common.CORPUS:
  faq/<name>.jsonl          one row per parsed question (+ faq/<name>.meta.json)
  changes/<service>.jsonl   What's New items and document-history rows of one service
  changes/_tags.json        the What's New tags seen so far (for mapping services to product tags)
  cases/index.jsonl         the customer-references directory (case studies), merged by id

These files are indexes for finding things. They are never evidence: a quote for the book always
comes from a page snapshot (snap/<source_id>.txt), checked with common.find_quote.
Every request goes through corpus.fetch, so the allow-list, robots.txt, the rate limit and the
cache all apply. Only the directory API is called for What's New and case studies; post pages are
never crawled here. Standard library only.
"""
from __future__ import annotations

import collections
import datetime
import html
import json
import re
import urllib.parse

from . import common, corpus

API_BASE = "https://aws.amazon.com/api/dirs/items/search"
API_MAX_SIZE = 1000                 # the API accepts a page size up to 1000
API_OFFSET_LIMIT = 10000            # paging stops at offset 10,000 (tested 2026-10-04)
DEFAULT_SINCE = "2022-07-01"        # just before SAA-C03 launched
WHATSNEW_DIR = "whats-new-v2"
WHATSNEW_SORT = "item.additionalFields.postDateTime"
WHATSNEW_PRODUCT_NS = "whats-new-v2#general-products"
CASES_DIR = "customer-references"
CASES_SORT = "item.additionalFields.sortDate"
CASES_PRODUCT_NS = "GLOBAL#product"
ANSWER_MAX_CHARS = 8000
SUMMARY_CHARS = 400

_RE_TAG_ARG = re.compile(r"^[a-z0-9][a-z0-9._-]{0,80}$")
_RE_WS = re.compile(r"\s+")


class FeedError(Exception):
    def __init__(self, message, exit_code=common.EXIT_FAIL):
        super().__init__(message)
        self.exit_code = exit_code


# ---------------------------------------------------------------- small helpers

def _one_line(text: str) -> str:
    return _RE_WS.sub(" ", text or "").strip()


def _html_text(fragment: str) -> str:
    """Visible text of an HTML fragment (same extractor as the page snapshots)."""
    if not fragment:
        return ""
    text, _title = corpus.html_to_text(fragment)
    return text.strip()


def _cut(text: str, limit: int) -> str:
    text = _one_line(text)
    if len(text) <= limit:
        return text
    head = text[:limit]
    stop = max(head.rfind(". "), head.rfind("? "))
    return (head[:stop + 1] if stop > limit // 2 else head.rstrip()) + " ..."


def _since(value):
    """Validate a YYYY-MM-DD option. Returns the string, or raises FeedError (exit 3)."""
    if not value:
        return ""
    try:
        return datetime.date.fromisoformat(value).isoformat()
    except ValueError:
        raise FeedError(f"bad date {value!r}; use YYYY-MM-DD", common.EXIT_PRECONDITION)


def _tag_arg(value: str, what: str = "tag") -> str:
    value = (value or "").strip().lower()
    if not _RE_TAG_ARG.match(value):
        raise FeedError(f"bad {what} {value!r}; use the short tag name, for example amazon-vpc", common.EXIT_PRECONDITION)
    return value


def _limit(args, default: int, maximum: int = 500) -> int:
    value = getattr(args, "limit", None)
    return max(1, min(int(value if value else default), maximum))


# ---------------------------------------------------------------- FAQ parsers

_RE_JSON_SCRIPT = re.compile(r"<script[^>]*type=[\"']application/json[\"'][^>]*>(.*?)</script>", re.S | re.I)
_RE_PAIR = re.compile(r'"itemHeading"\s*:\s*("(?:[^"\\]|\\.)*")\s*,\s*"itemLongLoc"\s*:\s*("(?:[^"\\]|\\.)*")')
_RE_HEAD = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
_RE_Q = re.compile(r"^(?:[-*+]\s+)?(?:#{1,6}\s+)?(?:\*\*|__)?Q\s?(?::\s*|\.\s+)(\S.*)$")
_RE_Q_ANY = re.compile(r"(?m)^\s*(?:[-*+]\s+)?(?:\*\*|__)?Q\s?(?::\s*|\.\s+)\S")
_RE_Q_SPLIT = re.compile(r"^(.{8,400}?\?)(?:\*\*|__)?\s+(\S.{20,})$")
_RE_MD_ANCHOR_LINE = re.compile(r"^\s*<a\s+(?:name|id)=[^>]*>\s*</a>\s*$")
_RE_MD_ANCHOR = re.compile(r"<a\s+(?:name|id)=[^>]*>\s*</a>")
_RE_FENCE = re.compile(r"^\s{0,3}(```|~~~)")


def _walk_items(node, out):
    if isinstance(node, dict):
        fields = node.get("fields") if isinstance(node.get("fields"), dict) else None
        holder = fields if fields and "itemHeading" in fields else (node if "itemHeading" in node else None)
        if holder is not None and isinstance(holder.get("itemLongLoc"), str) and isinstance(holder.get("itemHeading"), str):
            section = ""
            meta = node.get("metadata")
            if isinstance(meta, dict):
                for tag in meta.get("tags") or []:
                    if isinstance(tag, dict) and tag.get("name"):
                        section = str(tag["name"])
                        break
            out.append({"heading": holder["itemHeading"], "body": holder["itemLongLoc"], "section": section})
            return
        for value in node.values():
            _walk_items(value, out)
    elif isinstance(node, list):
        for value in node:
            _walk_items(value, out)


def embedded_items(raw_html: str) -> list:
    """Parser 1, step 1: the items embedded as JSON (itemHeading, itemLongLoc, first tag name)."""
    items = []
    for match in _RE_JSON_SCRIPT.finditer(raw_html):
        blob = match.group(1)
        if "itemHeading" not in blob:
            continue
        try:
            _walk_items(json.loads(blob), items)
        except ValueError:
            continue
    if not items and "itemHeading" in raw_html:
        # Fallback for a blob that is not valid JSON as a whole: read the two strings pair by pair.
        for match in _RE_PAIR.finditer(raw_html):
            try:
                items.append({"heading": json.loads(match.group(1)), "body": json.loads(match.group(2)), "section": ""})
            except ValueError:
                continue
    return items


def parse_legacy(text: str, base_section: str = "") -> list:
    """Parser 2: 'Q:' paragraphs in visible text. The answer runs to the next 'Q:' line or heading."""
    rows, heads, current = [], {}, None

    def close():
        nonlocal current
        if current is not None:
            current["answer"] = "\n".join(current.pop("lines")).strip()[:ANSWER_MAX_CHARS]
            rows.append(current)
        current = None

    for number, raw in enumerate((text or "").splitlines(), 1):
        line = raw.strip()
        q = _RE_Q.match(line)
        if q:
            close()
            question, first = q.group(1).strip(), ""
            split = _RE_Q_SPLIT.match(question)
            if split:
                question, first = split.group(1), split.group(2)
            question = question.replace("**", "").replace("__", "").strip()
            section = " / ".join(s for s in [base_section] + [heads[k] for k in sorted(heads)] if s)
            current = {"question": question, "section": section, "line": number, "lines": [first] if first else []}
            continue
        h = _RE_HEAD.match(line)
        if h:
            close()
            level = len(h.group(1))
            for deeper in [k for k in heads if k >= level]:
                del heads[deeper]
            if level >= 2:
                heads[level] = h.group(2).strip()
            continue
        if current is not None and line:
            current["lines"].append(raw.rstrip())
    close()
    return rows


def parse_markdown_faq(text: str) -> list:
    """Docs-guide FAQ pages (for example the Aurora FAQ): a heading that ends with '?' is a question."""
    rows, heads, current, fence, title = [], {}, None, False, ""

    def close():
        nonlocal current
        if current is not None:
            current["answer"] = "\n".join(current.pop("lines")).strip()[:ANSWER_MAX_CHARS]
            rows.append(current)
        current = None

    for number, raw in enumerate((text or "").splitlines(), 1):
        if _RE_FENCE.match(raw):
            fence = not fence
        h = None if fence else _RE_HEAD.match(raw.strip())
        if h:
            close()
            level = len(h.group(1))
            heading = _RE_MD_ANCHOR.sub("", h.group(2)).replace("\\", "").replace("**", "").strip()
            for deeper in [k for k in heads if k >= level]:
                del heads[deeper]
            q = _RE_Q.match(heading)
            if q:
                heading = q.group(1).strip()
            if level == 1:
                title = heading
            elif q or heading.endswith("?"):
                section = " / ".join(s for s in [heads[k] for k in sorted(heads)] if s) or title
                current = {"question": heading, "section": section, "line": number, "lines": []}
            else:
                heads[level] = heading
            continue
        if current is not None and not _RE_MD_ANCHOR_LINE.match(raw):
            current["lines"].append(raw.rstrip())
    close()
    return rows


def parse_faq_html(raw_html: str, visible_text: str) -> list:
    """Both HTML parsers together. Returns rows with question, answer, section, parser, line."""
    found, seen = [], set()

    def add(question, answer, section, parser):
        question = _one_line(html.unescape(question))
        if not question:
            return
        key = common.normalize_text(question) + "|" + common.normalize_text(answer)[:80]
        if key in seen:
            return
        seen.add(key)
        found.append({"question": question, "answer": answer, "section": section, "parser": parser, "line": None})

    for item in embedded_items(raw_html):
        heading = _one_line(_html_text(item["heading"]) or html.unescape(item["heading"]))
        body = _html_text(item["body"])
        if _RE_Q_ANY.search(body):
            # A legacy block stored inside one JSON item: many 'Q:' paragraphs under one heading.
            base = " / ".join(s for s in (item["section"], heading) if s)
            for row in parse_legacy(body, base):
                add(row["question"], row["answer"], row["section"], "legacy")
        else:
            q = _RE_Q.match(heading)
            add(q.group(1) if q else heading, body[:ANSWER_MAX_CHARS], item["section"], "json")
    for row in parse_legacy(visible_text):
        add(row["question"], row["answer"], row["section"], "legacy")

    # Put the rows in page order by finding each question as a line of the visible text.
    lines = collections.defaultdict(list)
    for number, raw in enumerate(visible_text.splitlines(), 1):
        norm = common.normalize_text(raw)
        if norm:
            lines[norm].append(number)
    for row in found:
        norm = common.normalize_text(row["question"])
        for key in (norm, "q: " + norm, "q. " + norm):
            if lines.get(key):
                row["line"] = lines[key].pop(0)
                break
    order = sorted(range(len(found)), key=lambda i: (found[i]["line"] is None, found[i]["line"] or 0, i))
    return [found[i] for i in order]


def faq_name_for(url: str) -> str:
    """https://aws.amazon.com/vpc/faqs/ -> vpc; /rds/aurora/faqs/ -> rds-aurora; a docs page -> its file name."""
    u = urllib.parse.urlsplit(url)
    segs = [s for s in u.path.split("/") if s]
    if u.hostname == "docs.aws.amazon.com":
        last = segs[-1].rsplit(".", 1)[0] if segs else "faq"
        return common.slugify(last) or "faq"
    segs = [s for s in segs if s.lower() not in ("faqs", "faq")]
    return common.slugify("-".join(segs)) or "faq"


def build_faq(url: str, name: str = None, revalidate: bool = False, follow: bool = False, max_pages: int = 15) -> dict:
    """Fetch a FAQ page through the corpus, parse it and write faq/<name>.jsonl. Returns the summary."""
    meta = corpus.fetch(url, revalidate=revalidate)
    name = common.slugify(name) if name else faq_name_for(meta["url"])
    if not name:
        raise FeedError("empty FAQ name", common.EXIT_PRECONDITION)
    final_url = meta.get("final_url") or meta["url"]
    final_host = urllib.parse.urlsplit(final_url).hostname or ""
    redirected = corpus.source_id_for(final_url) != corpus.source_id_for(meta["url"])
    warnings, pages = [], []

    def parse_snapshot(page_meta):
        sid = page_meta["source_id"]
        text = corpus.load_text(sid) or ""
        if page_meta.get("kind") == "html":
            raw = corpus.snapshot_paths(sid)["raw"].read_bytes().decode("utf-8", errors="replace")
            parsed = parse_faq_html(raw, text)
        else:
            parsed = [dict(r, parser="markdown") for r in parse_markdown_faq(text)]
            if not parsed:
                parsed = [dict(r, parser="legacy") for r in parse_legacy(text)]
        norm = common.normalize_text(text)
        for row in parsed:
            row["source_id"] = sid
            row["url"] = page_meta["url"]
            row["final_url"] = page_meta.get("final_url") or page_meta["url"]
            row["question_in_text"] = common.find_quote(row["question"], norm, already_normalized=True) is not None
            row["answer_in_text"] = bool(row["answer"]) and \
                common.find_quote(row["answer"], norm, already_normalized=True) is not None
        pages.append({"source_id": sid, "url": page_meta["url"], "final_url": page_meta.get("final_url", ""),
                      "kind": page_meta.get("kind", ""), "fetched_at": page_meta.get("fetched_at", ""),
                      "sha256": page_meta.get("sha256", ""), "questions": len(parsed)})
        return parsed

    rows = parse_snapshot(meta)
    more_pages = 0
    if final_host == "docs.aws.amazon.com" and follow:
        # A FAQ that moved into a docs guide is split over several pages; the guide's llms.txt lists them.
        root = final_url.rsplit("/", 1)[0] + "/"
        landing = corpus.source_id_for(final_url)
        llms = corpus.fetch(root + "llms.txt", revalidate=revalidate)
        listed = [p for p in corpus.parse_llms(corpus.load_text(llms["source_id"]) or "", root)["pages"]
                  if p["source_id"] != landing]
        # The FAQ pages share the landing page's name (aurora-faq, aurora-faq-security, ...).
        family = [p for p in listed if p["source_id"].startswith(landing + "-")]
        listed = family or listed
        more_pages = max(0, len(listed) - max_pages)
        for page in listed[:max_pages]:
            try:
                rows.extend(parse_snapshot(corpus.fetch(page["url"], revalidate=revalidate)))
            except corpus.PolicyError:
                raise
            except corpus.CorpusError as exc:
                warnings.append(f"{page['url']}: {exc}")
        if more_pages:
            warnings.append(f"{more_pages} more guide pages not read; raise --max-pages")
    elif final_host == "docs.aws.amazon.com" and redirected:
        warnings.append("this FAQ now lives in a docs guide; run again with --follow to read its other pages")

    out = []
    for position, row in enumerate(rows, 1):
        out.append({"id": f"{name}#{position}", "name": name, "position": position, "section": row["section"],
                    "question": row["question"], "answer": row["answer"], "parser": row["parser"],
                    "source_id": row["source_id"], "url": row["url"], "final_url": row["final_url"],
                    "line": row["line"], "question_in_text": row["question_in_text"],
                    "answer_in_text": row["answer_in_text"]})
    if not out:
        warnings.append("no questions parsed; read the snapshot text with `saa.py show` instead")
    path = common.CORPUS / "faq" / f"{name}.jsonl"
    summary = {
        "name": name, "url": meta["url"], "final_url": final_url, "redirected": bool(redirected),
        "source_id": meta["source_id"], "state": meta.get("state", ""), "built_at": common.now_iso(),
        "questions": len(out), "by_parser": dict(collections.Counter(r["parser"] for r in out)),
        "sections": len({r["section"] for r in out}),
        "empty_answers": sum(1 for r in out if not r["answer"]),
        "questions_not_in_text": sum(1 for r in out if not r["question_in_text"]),
        "answers_not_in_text": sum(1 for r in out if r["answer"] and not r["answer_in_text"]),
        "pages": pages, "warnings": warnings, "index": common.rel(path),
    }
    with common.file_lock(path):
        common.write_jsonl(path, out)
        common.write_json(common.CORPUS / "faq" / f"{name}.meta.json", summary)
    summary["rows"] = out
    return summary


# ---------------------------------------------------------------- the directory API (What's New, case studies)

def _api_url(directory: str, sort_by: str, size: int, page: int, tag_id: str = "") -> str:
    params = [("item.directoryId", directory), ("sort_by", sort_by), ("sort_order", "desc"),
              ("size", str(size)), ("item.locale", "en_US"), ("page", str(page))]
    if tag_id:
        params.append(("tags.id", tag_id))
    return API_BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


def api_harvest(directory: str, sort_by: str, label: str, tag_id: str = "", size: int = API_MAX_SIZE,
                max_pages: int = 10, refresh: bool = False, stop_before: str = "", date_of=None) -> dict:
    """Read pages of a directory, newest first. Stops at the end, at `stop_before` (a date), at
    max_pages, or at the API paging limit. Returns {items, total_hits, pages, stopped, truncated, source_ids}."""
    size = max(1, min(int(size), API_MAX_SIZE))
    items, sids, total, stopped, fetched_at = [], [], None, "max-pages", ""
    for page in range(max(1, int(max_pages))):
        if page * size >= API_OFFSET_LIMIT:
            stopped = "paging-limit"
            break
        sid = f"api/{directory}-{label}-s{size}-p{page}"
        try:
            meta = corpus.fetch(_api_url(directory, sort_by, size, page, tag_id), revalidate=refresh, source_id=sid)
        except corpus.FetchError as exc:
            if page == 0:
                raise
            stopped = f"http-{exc.status}"
            break
        try:
            data = json.loads(corpus.load_text(sid) or "")
            batch = data["items"]
            if not isinstance(batch, list):
                raise ValueError("items is not a list")
        except (ValueError, KeyError, TypeError) as exc:
            raise FeedError(f"{sid}: the API answer is not the expected JSON ({exc})")
        sids.append(sid)
        fetched_at = fetched_at or meta.get("fetched_at", "")
        if total is None:
            total = int((data.get("metadata") or {}).get("totalHits") or 0)
        items.extend(batch)
        if len(batch) < size or (total and len(items) >= total):
            stopped = "end"
            break
        if stop_before and date_of:
            last = date_of(batch[-1])
            if last and last < stop_before:
                stopped = "since"
                break
    truncated = stopped not in ("end", "since") and bool(total) and len(items) < total
    return {"items": items, "total_hits": total or 0, "pages": len(sids), "stopped": stopped,
            "truncated": truncated, "source_ids": sids, "fetched_at": fetched_at}


def _tag_slug(tag_id: str) -> str:
    return tag_id.rsplit("#", 1)[-1]


def _note_tags(raw_items, counts: bool = False) -> None:
    """Remember every What's New tag seen (changes/_tags.json). With counts=True, replace the sample counts."""
    path = common.CORPUS / "changes" / "_tags.json"
    seen, counter = {}, collections.Counter()
    for entry in raw_items:
        for tag in entry.get("tags") or []:
            if isinstance(tag, dict) and tag.get("id"):
                seen[tag["id"]] = tag
                counter[tag["id"]] += 1
    if not seen:
        return
    with common.file_lock(path):
        store = common.read_json(path, {}) or {}
        tags = store.get("tags", {})
        if counts:
            for record in tags.values():
                record["sample_count"] = 0
            store["sample_items"] = len(raw_items)
            store["sample_at"] = common.now_iso()
        for tag_id, tag in seen.items():
            record = tags.setdefault(tag_id, {"sample_count": 0})
            record.update(tag=_tag_slug(tag_id), namespace=tag.get("tagNamespaceId", ""), name=tag.get("name", ""),
                          description=tag.get("description", ""))
            if counts:
                record["sample_count"] = counter[tag_id]
        store["tags"] = tags
        store["updated_at"] = common.now_iso()
        common.write_json(path, store)


# ---------------------------------------------------------------- changes: What's New

def _whatsnew_date(entry) -> str:
    fields = (entry.get("item") or {}).get("additionalFields") or {}
    return str(fields.get("postDateTime") or (entry.get("item") or {}).get("dateCreated") or "")[:10]


def whatsnew_row(entry: dict, service: str, tag: str, api_sid: str = "") -> dict:
    item = entry.get("item") or {}
    fields = item.get("additionalFields") or {}
    text = _html_text(fields.get("postBody") or fields.get("postSummary") or "")
    path = (fields.get("headlineUrl") or "").strip()
    url = urllib.parse.urljoin("https://aws.amazon.com/", path) if path else ""
    products = sorted(_tag_slug(t["id"]) for t in entry.get("tags") or []
                      if isinstance(t, dict) and t.get("tagNamespaceId") == WHATSNEW_PRODUCT_NS and t.get("id"))
    return {"date": _whatsnew_date(entry), "title": _one_line(html.unescape(fields.get("headline") or "")),
            "summary": _cut(text, SUMMARY_CHARS), "url": url, "source": "whatsnew", "service": service,
            "id": item.get("id", ""), "tag": tag, "product_tags": products, "text": text, "api_source_id": api_sid}


def _merge_changes(service: str, new_rows: list, key_of) -> dict:
    """Merge rows into changes/<service>.jsonl under a lock. Rows with the same key are replaced."""
    path = common.CORPUS / "changes" / f"{service}.jsonl"
    with common.file_lock(path):
        merged = collections.OrderedDict()
        for row in common.read_jsonl(path):
            merged[_change_key(row)] = row
        before = len(merged)
        for row in new_rows:
            merged[key_of(row)] = row
        rows = sorted(merged.values(), key=lambda r: (r.get("date", ""), r.get("title", "")), reverse=True)
        common.write_jsonl(path, rows)
    return {"path": common.rel(path), "total": len(rows), "added": len(rows) - before}


def _change_key(row: dict) -> str:
    if row.get("source") == "history":
        return "history|" + "|".join(str(row.get(k, "")) for k in ("history_source_id", "date", "title"))
    return "whatsnew|" + (row.get("id") or row.get("url") or row.get("title", ""))


def harvest_whatsnew(tag: str, service: str, since: str = DEFAULT_SINCE, size: int = API_MAX_SIZE,
                     max_pages: int = 10, refresh: bool = False) -> dict:
    tag = _tag_arg(tag)
    service = common.slugify(service)
    if not service:
        raise FeedError("--service needs a name", common.EXIT_PRECONDITION)
    since = _since(since)
    result = api_harvest(WHATSNEW_DIR, WHATSNEW_SORT, tag, tag_id=f"{WHATSNEW_PRODUCT_NS}#{tag}", size=size,
                         max_pages=max_pages, refresh=refresh, stop_before=since, date_of=_whatsnew_date)
    raw = result["items"]
    if not raw:
        raise FeedError(f"the API has no What's New item for product tag {tag!r}; "
                        f"find the tag with: saa.py changes tags --find TEXT")
    _note_tags(raw)
    sid0 = result["source_ids"][0] if result["source_ids"] else ""
    rows, undated = [], 0
    for entry in raw:
        row = whatsnew_row(entry, service, tag, sid0)
        if not row["date"]:
            undated += 1
            continue
        if since and row["date"] < since:
            continue
        rows.append(row)
    stored = _merge_changes(service, rows, _change_key)
    oldest = min((_whatsnew_date(e) for e in raw if _whatsnew_date(e)), default="")
    warnings = []
    if result["truncated"] and (not since or oldest >= since):
        warnings.append(f"stopped at {result['stopped']} with {len(raw)} of {result['total_hits']} items; "
                        f"items older than {oldest} are not covered")
    if undated:
        warnings.append(f"{undated} items without a date were skipped")
    return {"service": service, "tag": tag, "since": since, "total_hits": result["total_hits"], "read": len(raw),
            "kept": len(rows), "oldest_read": oldest, "newest": max((r["date"] for r in rows), default=""),
            "pages": result["pages"], "stopped": result["stopped"], "api_source_ids": result["source_ids"],
            "warnings": warnings, **stored}


# ---------------------------------------------------------------- changes: document history

_MONTHS = {m: i for i, m in enumerate(
    "january february march april may june july august september october november december".split(), 1)}
_MONTHS.update({m[:3]: i for m, i in list(_MONTHS.items())})
_MONTHS["sept"] = 9
_RE_ISO = re.compile(r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b")
_RE_MDY = re.compile(r"\b([A-Za-z]{3,9})\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b")
_RE_DMY = re.compile(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]{3,9})\.?,?\s+(\d{4})\b")
_RE_MY = re.compile(r"\b([A-Za-z]{3,9})\.?,?\s+(\d{4})\b")
_RE_CELL_LINK = re.compile(r"\[([^\]]+)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_RE_CELL_TAG = re.compile(r"<[^>]{0,300}>")
_RE_CELL_ESC = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>~])")


def parse_date(text: str):
    """'November 21, 2025', '21 Nov 2025', '2025-11-21' or 'November 2025' -> (ISO date, precision) or None."""
    text = _one_line(_RE_CELL_ESC.sub(r"\1", text or "").replace("*", ""))

    def make(year, month, day, precision):
        try:
            return datetime.date(int(year), int(month), int(day)).isoformat(), precision
        except ValueError:
            return None

    m = _RE_ISO.search(text)
    if m:
        return make(m.group(1), m.group(2), m.group(3), "day")
    m = _RE_MDY.search(text)
    if m and m.group(1).lower() in _MONTHS:
        return make(m.group(3), _MONTHS[m.group(1).lower()], m.group(2), "day")
    m = _RE_DMY.search(text)
    if m and m.group(2).lower() in _MONTHS:
        return make(m.group(3), _MONTHS[m.group(2).lower()], m.group(1), "day")
    m = _RE_MY.search(text)
    if m and m.group(1).lower() in _MONTHS:
        return make(m.group(2), _MONTHS[m.group(1).lower()], 1, "month")
    return None


def _cell_text(cell: str) -> str:
    cell = _RE_CELL_LINK.sub(r"\1", cell or "")
    cell = _RE_CELL_TAG.sub(" ", cell)
    cell = _RE_CELL_ESC.sub(r"\1", cell).replace("**", "").replace("`", "")
    return _one_line(html.unescape(cell))


def parse_history(text: str) -> dict:
    """Dated rows of a document-history page (Markdown tables with a date column)."""
    rows, undated, tables_used = [], 0, 0
    for table in corpus.parse_tables(text or ""):
        headers = table["headers"]
        date_col = next((h for h in headers if "date" in h.lower()), None)
        if date_col is None:
            sample = table["rows"][:10]
            for h in headers:
                hits = sum(1 for r in sample if parse_date(r["cells"].get(h, "")))
                if sample and hits * 10 >= len(sample) * 6:
                    date_col = h
                    break
        if date_col is None:
            continue
        rest = [h for h in headers if h != date_col]
        title_col = next((h for h in rest if re.search(r"(?i)change|feature|update|release|what", h)), rest[0] if rest else None)
        others = [h for h in rest if h != title_col]
        desc_col = next((h for h in others if re.search(r"(?i)descri|detail|summary", h)), others[0] if others else None)
        used = False
        for row in table["rows"]:
            cells = row["cells"]
            parsed = parse_date(cells.get(date_col, ""))
            if not parsed:
                undated += 1
                continue
            title_cell = cells.get(title_col, "") if title_col else ""
            desc_cell = cells.get(desc_col, "") if desc_col else ""
            link = _RE_CELL_LINK.search(title_cell) or _RE_CELL_LINK.search(desc_cell)
            title = _cell_text(title_cell) or _cut(_cell_text(desc_cell), 120)
            rows.append({"date": parsed[0], "date_precision": parsed[1], "date_text": _cell_text(cells.get(date_col, "")),
                         "title": title, "summary": _cell_text(desc_cell), "link": link.group(2) if link else "",
                         "line": row["line"], "quote": row["text"], "table_header": table["header_text"]})
            used = True
        tables_used += 1 if used else 0
    return {"rows": rows, "undated": undated, "tables": tables_used}


def harvest_history(url: str, service: str, since: str = DEFAULT_SINCE, revalidate: bool = False) -> dict:
    service = common.slugify(service)
    if not service:
        raise FeedError("--service needs a name", common.EXIT_PRECONDITION)
    since = _since(since)
    meta = corpus.fetch(url, revalidate=revalidate)
    sid = meta["source_id"]
    parsed = parse_history(corpus.load_text(sid) or "")
    if not parsed["rows"]:
        raise FeedError(f"{sid}: no table with dated rows found; this is not a document-history table "
                        f"(final URL {meta.get('final_url', '')}). Look at it with: saa.py tables {sid}")
    rows = []
    for row in parsed["rows"]:
        if since and row["date"] < since:
            continue
        rows.append({"date": row["date"], "title": row["title"], "summary": row["summary"], "url": meta["url"],
                     "source": "history", "service": service, "link": row["link"], "date_text": row["date_text"],
                     "date_precision": row["date_precision"], "history_source_id": sid, "line": row["line"],
                     "quote": row["quote"], "table_header": row["table_header"]})
    stored = _merge_changes(service, rows, _change_key)
    dates = [r["date"] for r in parsed["rows"]]
    warnings = []
    if parsed["undated"]:
        warnings.append(f"{parsed['undated']} table rows without a readable date were skipped")
    return {"service": service, "source_id": sid, "url": meta["url"], "final_url": meta.get("final_url", ""),
            "since": since, "read": len(parsed["rows"]), "kept": len(rows), "newest": max(dates), "oldest": min(dates),
            "state": meta.get("state", ""), "warnings": warnings, **stored}


def changes_for(service: str, since: str = "", source: str = "", find: str = "") -> list:
    service = common.slugify(service)
    path = common.CORPUS / "changes" / f"{service}.jsonl"
    if not service or service.startswith("_") or not path.exists():
        raise FeedError(f"no change feed for {service!r}; run `saa.py changes harvest` or `changes history` first",
                        common.EXIT_PRECONDITION)
    since = _since(since)
    needle = _one_line(find).lower()
    rows = []
    for row in common.read_jsonl(path):
        if since and row.get("date", "") < since:
            continue
        if source and row.get("source") != source:
            continue
        if needle and needle not in " ".join(str(row.get(k, "")) for k in ("title", "summary", "text")).lower():
            continue
        rows.append(row)
    rows.sort(key=lambda r: (r.get("date", ""), r.get("title", "")), reverse=True)
    return rows


# ---------------------------------------------------------------- cases

def _case_date(entry) -> str:
    item = entry.get("item") or {}
    fields = item.get("additionalFields") or {}
    return str(fields.get("sortDate") or item.get("dateCreated") or "")[:10]


def case_row(entry: dict, api_sid: str = "") -> dict:
    item = entry.get("item") or {}
    fields = item.get("additionalFields") or {}
    by_ns = collections.defaultdict(list)
    for tag in entry.get("tags") or []:
        if isinstance(tag, dict) and tag.get("id"):
            by_ns[tag.get("tagNamespaceId", "")].append(tag)
    link = (fields.get("headlineUrl") or "").strip()
    url = ""
    if link:
        u = urllib.parse.urlsplit(urllib.parse.urljoin("https://aws.amazon.com/", link))
        url = urllib.parse.urlunsplit((u.scheme, u.netloc, u.path, "", ""))
    host = urllib.parse.urlsplit(url).hostname or ""
    languages = sorted(_tag_slug(t["id"]) for t in by_ns.get("GLOBAL#language", []))
    english = "english" in languages or (not languages and re.match(r"^/(solutions|partners|blogs)/", urllib.parse.urlsplit(url).path or "") is not None)
    return {
        "id": item.get("id", ""), "title": _one_line(html.unescape(fields.get("headline") or "")),
        "customer": _one_line(html.unescape(fields.get("customer-name") or "")), "url": url,
        "date": _case_date(entry), "tags": sorted(_tag_slug(t["id"]) for t in by_ns.get(CASES_PRODUCT_NS, [])),
        "summary": _one_line(_html_text(fields.get("descriptionSummary") or fields.get("description") or "")),
        "tag_names": {_tag_slug(t["id"]): t.get("name", "") for t in by_ns.get(CASES_PRODUCT_NS, [])},
        "segments": sorted({_tag_slug(t["id"]) for ns in ("GLOBAL#customer-segment", "customer-references#customer-segment")
                            for t in by_ns.get(ns, [])}),
        "industry": _one_line(html.unescape(fields.get("industry") or "")),
        "location": _one_line(html.unescape(fields.get("displayLocation") or "")),
        "content_type": fields.get("contentType", ""), "languages": languages, "english": bool(english),
        "fetchable": host in common.ALLOWED_HOSTS, "source": "customer-references", "api_source_id": api_sid,
    }


def _cases_path():
    return common.CORPUS / "cases" / "index.jsonl"


def harvest_cases(tag: str = "", size: int = API_MAX_SIZE, max_pages: int = 10, refresh: bool = False) -> dict:
    tag = _tag_arg(tag) if tag else ""
    result = api_harvest(CASES_DIR, CASES_SORT, tag or "all", tag_id=f"{CASES_PRODUCT_NS}#{tag}" if tag else "",
                         size=size, max_pages=max_pages, refresh=refresh)
    raw = result["items"]
    if not raw:
        raise FeedError(f"the API has no case study for product tag {tag!r}; "
                        f"find the tag with: saa.py cases tags --find TEXT" if tag else "the API returned no case study")
    sid0 = result["source_ids"][0] if result["source_ids"] else ""
    rows = [case_row(entry, sid0) for entry in raw]
    rows = [r for r in rows if r["id"]]
    path = _cases_path()
    with common.file_lock(path):
        merged = collections.OrderedDict((r["id"], r) for r in common.read_jsonl(path))
        before = len(merged)
        for row in rows:
            merged[row["id"]] = row
        ordered = sorted(merged.values(), key=lambda r: (r.get("date", ""), r.get("id", "")), reverse=True)
        common.write_jsonl(path, ordered)
    warnings = []
    if result["truncated"]:
        warnings.append(f"stopped at {result['stopped']} with {len(raw)} of {result['total_hits']} items; "
                        f"harvest by product tag to reach the rest")
    return {"tag": tag or "(all)", "total_hits": result["total_hits"], "read": len(raw), "added": len(ordered) - before,
            "total": len(ordered), "pages": result["pages"], "stopped": result["stopped"],
            "api_source_ids": result["source_ids"], "path": common.rel(path), "warnings": warnings}


def _load_cases() -> list:
    path = _cases_path()
    if not path.exists():
        raise FeedError("no case-study index yet; run `saa.py cases harvest [--tag TAG]` first", common.EXIT_PRECONDITION)
    return common.read_jsonl(path)


def cases_for(tag: str, find: str = "", segment: str = "", since: str = "", all_languages: bool = False) -> list:
    tag = _tag_arg(tag)
    since = _since(since)
    needle = _one_line(find).lower()
    segment = (segment or "").strip().lower()
    rows = []
    for row in _load_cases():
        if tag not in row.get("tags", []):
            continue
        if not all_languages and not row.get("english"):
            continue
        if since and row.get("date", "") < since:
            continue
        if segment and not any(segment in s for s in row.get("segments", [])):
            continue
        if needle and needle not in " ".join(str(row.get(k, "")) for k in ("title", "customer", "summary", "industry")).lower():
            continue
        rows.append(row)
    rows.sort(key=lambda r: (r.get("date", ""), r.get("id", "")), reverse=True)
    return rows


# ---------------------------------------------------------------- CLI

def _guard(func):
    """Turn the module's errors into exit codes."""
    def wrapped(args):
        try:
            return func(args)
        except FeedError as exc:
            return common.fail(str(exc), exc.exit_code)
        except corpus.CorpusError as exc:
            return common.fail(str(exc), exc.exit_code)
    wrapped.__name__ = func.__name__
    return wrapped


@_guard
def cmd_faq(args) -> int:
    summary = build_faq(args.url, name=args.name, revalidate=args.revalidate, follow=args.follow,
                        max_pages=max(1, min(args.max_pages, 60)))
    rows = summary.pop("rows")
    code = common.EXIT_OK if rows else common.EXIT_WARN
    if args.find:
        needle = _one_line(args.find).lower()
        norm = common.normalize_text(args.find)
        hits = [r for r in rows if needle in (r["question"] + " " + r["answer"]).lower()
                or (norm and norm in common.normalize_text(r["question"] + " " + r["answer"]))]
        limit = _limit(args, 5, 50)
        chars = max(100, min(args.chars, 4000))
        if args.json:
            common.emit({"name": summary["name"], "find": args.find, "matches": len(hits), "shown": min(len(hits), limit),
                         "rows": [dict(r, answer=r["answer"][:chars]) for r in hits[:limit]]}, args)
        else:
            out = []
            for r in hits[:limit]:
                answer = r["answer"] if len(r["answer"]) <= chars else r["answer"][:chars] + " ..."
                out.append(f"{r['id']} [{r['section']}] line {r['line']} of {r['source_id']}\nQ: {r['question']}\nA: {answer}\n")
            out.append(f"{min(len(hits), limit)} of {len(hits)} matches shown ({summary['questions']} questions in "
                       f"{summary['index']}). Quote from the snapshot, not from this index.")
            common.emit("\n".join(out), args)
        return common.EXIT_OK if hits else common.EXIT_FAIL
    if args.json:
        if args.list:
            limit = _limit(args, 60)
            summary["list"] = [{k: r[k] for k in ("position", "section", "question", "line", "parser")} for r in rows[:limit]]
        common.emit(summary, args)
        return code
    parsers = ", ".join(f"{k} {v}" for k, v in sorted(summary["by_parser"].items())) or "none"
    out = [f"faq {summary['name']}: {summary['questions']} questions ({parsers}) in {summary['sections']} sections",
           f"  url={summary['url']}",
           f"  final_url={summary['final_url']}" + ("  (redirected)" if summary["redirected"] else ""),
           f"  snapshot={summary['source_id']} ({summary['state']})  pages={len(summary['pages'])}",
           f"  index={summary['index']}",
           f"  not found in the snapshot text: {summary['questions_not_in_text']} questions, "
           f"{summary['answers_not_in_text']} answers; empty answers: {summary['empty_answers']}"]
    out += [f"  warning: {w}" for w in summary["warnings"]]
    if args.list:
        limit = _limit(args, 60)
        out += [f"{r['position']:>4}  [{r['section'][:40]}] {r['question'][:160]}" for r in rows[:limit]]
        if len(rows) > limit:
            out.append(f"... {len(rows) - limit} more (raise --limit, or use --find TEXT)")
    common.emit("\n".join(out), args)
    return code


def _harvest_text(kind: str, r: dict) -> str:
    out = [f"{kind}: read {r['read']}" + (f" of {r['total_hits']}" if "total_hits" in r else "")
           + (f", kept {r['kept']}" if "kept" in r else "") + f", added {r['added']}, file now has {r['total']} rows",
           f"  file={r['path']}"]
    for key in ("since", "newest", "oldest", "oldest_read", "stopped", "pages", "final_url"):
        if r.get(key) not in (None, ""):
            out.append(f"  {key}={r[key]}")
    out += [f"  warning: {w}" for w in r.get("warnings", [])]
    return "\n".join(out)


@_guard
def cmd_changes_harvest(args) -> int:
    result = harvest_whatsnew(args.tag, args.service, since=args.since, size=args.page_size,
                              max_pages=args.max_pages, refresh=args.refresh)
    common.emit(result if args.json else _harvest_text(f"whatsnew {result['tag']} -> {result['service']}", result), args)
    return common.EXIT_WARN if result["warnings"] else common.EXIT_OK


@_guard
def cmd_changes_history(args) -> int:
    result = harvest_history(args.url, args.service, since=args.since, revalidate=args.revalidate)
    common.emit(result if args.json else _harvest_text(f"history {result['source_id']} -> {result['service']}", result), args)
    return common.EXIT_WARN if result["warnings"] else common.EXIT_OK


@_guard
def cmd_changes_for(args) -> int:
    rows = changes_for(args.service, since=args.since, source=args.source or "", find=args.find or "")
    limit = _limit(args, 40)
    shown = rows[:limit]
    if args.json:
        keep = ("date", "source", "title", "summary", "url", "link", "id", "line", "history_source_id", "quote")
        common.emit({"service": common.slugify(args.service), "matches": len(rows), "shown": len(shown),
                     "rows": [{k: r[k] for k in keep if r.get(k) not in (None, "")} for r in shown]}, args)
    else:
        out = []
        for r in shown:
            out.append(f"{r.get('date', '')}  {r.get('source', ''):8}  {r.get('title', '')[:150]}")
            if args.verbose and r.get("summary"):
                out.append(f"    {r['summary'][:SUMMARY_CHARS]}")
            target = r.get("url", "") + (f"  (see {r['link']})" if r.get("link") else "")
            out.append(f"    {target}")
        out.append(f"{len(shown)} of {len(rows)} change items shown for {common.slugify(args.service)}"
                   + (f" since {args.since}" if args.since else "") + ". Dates and deltas only; current truth comes from the guides.")
        common.emit("\n".join(out), args)
    return common.EXIT_OK if rows else common.EXIT_FAIL


@_guard
def cmd_changes_tags(args) -> int:
    if args.refresh:
        pages = max(1, min(args.pages, API_OFFSET_LIMIT // API_MAX_SIZE))
        result = api_harvest(WHATSNEW_DIR, WHATSNEW_SORT, "all", size=args.page_size, max_pages=pages, refresh=True)
        _note_tags(result["items"], counts=True)
    store = common.read_json(common.CORPUS / "changes" / "_tags.json")
    if not store or not store.get("tags"):
        raise FeedError("no tag list yet; run `saa.py changes tags --refresh` (it reads the newest What's New items)",
                        common.EXIT_PRECONDITION)
    needle = _one_line(args.find or "").lower()
    rows = []
    for tag_id, record in store["tags"].items():
        if not args.all_namespaces and record.get("namespace") != WHATSNEW_PRODUCT_NS:
            continue
        if needle and needle not in f"{tag_id} {record.get('name', '')} {record.get('description', '')}".lower():
            continue
        rows.append({"tag": record.get("tag", _tag_slug(tag_id)), "id": tag_id, "namespace": record.get("namespace", ""),
                     "sample_count": record.get("sample_count", 0)})
    rows.sort(key=lambda r: (-r["sample_count"], r["tag"]))
    limit = _limit(args, 60, 2000)
    if args.json:
        common.emit({"matches": len(rows), "shown": min(len(rows), limit), "sample_items": store.get("sample_items", 0),
                     "sample_at": store.get("sample_at", ""), "tags": rows[:limit]}, args)
    else:
        out = [f"{r['tag']:55} {r['sample_count']:>6}" + (f"  {r['namespace']}" if args.all_namespaces else "") for r in rows[:limit]]
        out.append(f"{min(len(rows), limit)} of {len(rows)} tags shown. The number is the count in the newest "
                   f"{store.get('sample_items', 0)} What's New items (sample of {store.get('sample_at', 'never') or 'never'}).")
        common.emit("\n".join(out), args)
    return common.EXIT_OK if rows else common.EXIT_FAIL


@_guard
def cmd_cases_harvest(args) -> int:
    result = harvest_cases(args.tag or "", size=args.page_size, max_pages=args.max_pages, refresh=args.refresh)
    common.emit(result if args.json else _harvest_text(f"cases {result['tag']}", result), args)
    return common.EXIT_WARN if result["warnings"] else common.EXIT_OK


@_guard
def cmd_cases_for(args) -> int:
    rows = cases_for(args.tag, find=args.find or "", segment=args.segment or "", since=args.since or "",
                     all_languages=args.all_languages)
    limit = _limit(args, 20)
    shown = rows[:limit]
    if args.json:
        keep = ("id", "date", "customer", "title", "url", "tags", "segments", "industry", "location", "summary", "fetchable")
        common.emit({"tag": args.tag, "matches": len(rows), "shown": len(shown),
                     "rows": [{k: r.get(k) for k in keep} for r in shown]}, args)
    else:
        out = []
        for r in shown:
            out.append(f"{r.get('date', '')}  {r.get('customer', '')[:40]} | {r.get('title', '')[:130]}")
            out.append(f"    {r.get('url', '')}" + ("" if r.get("fetchable") else "  (host not in the allow-list)"))
            if args.verbose:
                out.append(f"    [{', '.join(r.get('segments', []))}] {r.get('industry', '')}; {r.get('location', '')}; "
                           f"tags: {', '.join(r.get('tags', [])[:12])}")
                out.append(f"    {r.get('summary', '')[:SUMMARY_CHARS]}")
        out.append(f"{len(shown)} of {len(rows)} case studies shown for tag {args.tag}. "
                   f"This index is for discovery; fetch the page and quote from its snapshot.")
        if not rows:
            out.append("No match: check the tag with `saa.py cases tags --find TEXT`, or harvest it with `cases harvest --tag TAG`.")
        common.emit("\n".join(out), args)
    return common.EXIT_OK if rows else common.EXIT_FAIL


@_guard
def cmd_cases_tags(args) -> int:
    needle = _one_line(args.find or "").lower()
    counter, names = collections.Counter(), {}
    for row in _load_cases():
        for tag in row.get("tags", []):
            counter[tag] += 1
            names[tag] = (row.get("tag_names") or {}).get(tag) or names.get(tag, "")
    rows = []
    for tag, count in counter.items():
        label = names.get(tag, "")
        if needle and needle not in f"{tag} {label}".lower():
            continue
        rows.append({"tag": tag, "count": count, "name": label})
    rows.sort(key=lambda r: (-r["count"], r["tag"]))
    limit = _limit(args, 60, 2000)
    if args.json:
        common.emit({"matches": len(rows), "shown": min(len(rows), limit), "tags": rows[:limit]}, args)
    else:
        out = [f"{r['tag']:45} {r['count']:>6}  {r['name']}" for r in rows[:limit]]
        out.append(f"{min(len(rows), limit)} of {len(rows)} product tags shown (count = case studies in the local index).")
        common.emit("\n".join(out), args)
    return common.EXIT_OK if rows else common.EXIT_FAIL


def _api_options(p, pages_default=10) -> None:
    p.add_argument("--page-size", type=int, default=API_MAX_SIZE, help=f"items per API request (at most {API_MAX_SIZE})")
    p.add_argument("--max-pages", type=int, default=pages_default, help="API requests at most (the API stops at offset 10,000)")
    p.add_argument("--refresh", action="store_true", help="ask the API again instead of using the saved answers")


def register(subparsers) -> None:
    p = subparsers.add_parser("faq", help="parse the questions of an AWS FAQ page into corpus/faq/<name>.jsonl")
    p.add_argument("url", metavar="URL")
    p.add_argument("--name", help="file name to use instead of the one made from the URL")
    p.add_argument("--list", action="store_true", help="list the questions (bounded by --limit)")
    p.add_argument("--find", metavar="TEXT", help="show the questions and answers that contain TEXT")
    p.add_argument("--limit", type=int, help="rows to print (default 60 for --list, 5 for --find)")
    p.add_argument("--chars", type=int, default=700, help="answer characters to print with --find (default 700)")
    p.add_argument("--follow", action="store_true", help="for a FAQ that moved into a docs guide: read the guide's other pages too")
    p.add_argument("--max-pages", type=int, default=15, help="guide pages to read with --follow (default 15)")
    p.add_argument("--revalidate", action="store_true", help="ask the server again for the page")
    common.add_common_args(p)
    p.set_defaults(func=cmd_faq)

    p = subparsers.add_parser("changes", help="change feed per service: What's New items and document-history rows")
    sub = p.add_subparsers(dest="changes_cmd", required=True)
    q = sub.add_parser("harvest", help="harvest What's New items of one product tag through the directory API")
    q.add_argument("--tag", required=True, metavar="PRODUCT_TAG", help="for example amazon-vpc (see: changes tags)")
    q.add_argument("--service", required=True, metavar="NAME", help="file name of the feed, for example vpc")
    q.add_argument("--since", default=DEFAULT_SINCE, help=f"keep items from this date on (default {DEFAULT_SINCE})")
    _api_options(q)
    common.add_common_args(q)
    q.set_defaults(func=cmd_changes_harvest)
    q = sub.add_parser("history", help="parse a guide's document-history page into dated rows")
    q.add_argument("url", metavar="URL")
    q.add_argument("--service", required=True, metavar="NAME")
    q.add_argument("--since", default=DEFAULT_SINCE, help=f"keep rows from this date on (default {DEFAULT_SINCE})")
    q.add_argument("--revalidate", action="store_true")
    common.add_common_args(q)
    q.set_defaults(func=cmd_changes_history)
    q = sub.add_parser("for", help="print a bounded list of the change items of a service")
    q.add_argument("service", metavar="SERVICE")
    q.add_argument("--since", default="", metavar="DATE")
    q.add_argument("--source", choices=("whatsnew", "history"))
    q.add_argument("--find", metavar="TEXT")
    q.add_argument("--limit", type=int, help="rows to print (default 40, at most 500)")
    q.add_argument("--verbose", action="store_true", help="add the summary of each item")
    common.add_common_args(q)
    q.set_defaults(func=cmd_changes_for)
    q = sub.add_parser("tags", help="list the What's New product tags seen so far")
    q.add_argument("--find", metavar="TEXT")
    q.add_argument("--refresh", action="store_true", help="read the newest What's New items again to collect tags")
    q.add_argument("--pages", type=int, default=3, help="API requests for --refresh (default 3, at most 10)")
    q.add_argument("--page-size", type=int, default=API_MAX_SIZE)
    q.add_argument("--all-namespaces", action="store_true", help="also list year and category tags")
    q.add_argument("--limit", type=int, help="rows to print (default 60)")
    common.add_common_args(q)
    q.set_defaults(func=cmd_changes_tags)

    p = subparsers.add_parser("cases", help="case-study discovery through the customer-references directory API")
    sub = p.add_subparsers(dest="cases_cmd", required=True)
    q = sub.add_parser("harvest", help="harvest the directory (all of it, or one product tag)")
    q.add_argument("--tag", metavar="TAG", help="product tag, for example dynamodb (see: cases tags)")
    _api_options(q)
    common.add_common_args(q)
    q.set_defaults(func=cmd_cases_harvest)
    q = sub.add_parser("for", help="print a bounded list of case studies with a product tag")
    q.add_argument("tag", metavar="TAG")
    q.add_argument("--find", metavar="TEXT")
    q.add_argument("--segment", metavar="NAME", help="customer segment, for example startup or enterprise")
    q.add_argument("--since", default="", metavar="DATE")
    q.add_argument("--all-languages", action="store_true", help="include case studies that are not in English")
    q.add_argument("--limit", type=int, help="rows to print (default 20, at most 500)")
    q.add_argument("--verbose", action="store_true", help="add segments, industry, tags and the summary")
    common.add_common_args(q)
    q.set_defaults(func=cmd_cases_for)
    q = sub.add_parser("tags", help="list the product tags in the local case-study index")
    q.add_argument("--find", metavar="TEXT")
    q.add_argument("--limit", type=int, help="rows to print (default 60)")
    common.add_common_args(q)
    q.set_defaults(func=cmd_cases_tags)
