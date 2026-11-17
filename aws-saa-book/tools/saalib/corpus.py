"""corpus: the only network path for evidence, plus bounded readers over the saved pages.

Subcommands: fetch, guide, search, show, tables.   Documentation: _build/style/TOOLS-corpus.md

Layout under common.CORPUS:
  snap/<source_id>.raw|.txt|.meta.json   page snapshots (the evidence base)
  full/<guide-id>.md|.meta.json          whole-guide Markdown, for search only (cite page snapshots)
  index/<guide-id>.json                  page list of a guide, with history and quota pointers
  history/<source_id>.<date>.<sha8>.txt  text of a snapshot that a revalidation replaced
  robots/<host>.json                     cached robots.txt (24 hours)
  rate.json (+ rate.json.lock)           last request slot and the daily request counter
  fetch.log.jsonl                        one line per HTTP request

Python API for other modules: source_id_for, snapshot_paths, load_text, load_meta, fetch,
build_guide, load_index, parse_tables, tables_for, search_corpus, resolve_source, html_to_text.
Standard library only.
"""
from __future__ import annotations

import collections
import gzip
import hashlib
import http.client
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

from . import common

USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
BASE_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/markdown,text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip",
}
MIN_INTERVAL = 1.0                 # seconds between request starts, across all processes
DAILY_CAP = int(os.environ.get("SAA_FETCH_DAILY_CAP", "6000"))
MAX_ATTEMPTS = 4                   # per URL, for 429 / 5xx / network errors
BACKOFF = (2.0, 6.0, 15.0)         # seconds before attempts 2, 3 and 4
TIMEOUT = 60
MAX_REDIRECTS = 5
MAX_BYTES = 80 * 1024 * 1024
ROBOTS_TTL = 24 * 3600
KEEP_NAMES = ("full.md", "llms.txt", "llms-full.txt")   # docs files that are not page twins
SEARCH_SCOPES = ("full", "snap", "faq", "changes", "cases", "all")
SEARCH_MAX_LIMIT = 200
SHOW_MAX_CHARS = 12000
SHOW_MAX_LINES = 400

_sleep = time.sleep                # patched by tests
_ROBOTS_MEMO: dict = {}

Response = collections.namedtuple("Response", "status headers body fetched_url final_url chain")


# ---------------------------------------------------------------- errors

class CorpusError(Exception):
    exit_code = common.EXIT_FAIL


class PolicyError(CorpusError):
    """Host outside the allow-list, robots.txt refusal, bad path, or the daily cap."""
    exit_code = common.EXIT_POLICY


class CapError(PolicyError):
    """The daily request cap is used up."""


class TransientError(CorpusError):
    """429, 5xx or a network error that survived every retry. Safe to retry later."""
    exit_code = common.EXIT_TRANSIENT


class FetchError(CorpusError):
    """A final non-200 answer (for example 404). Nothing is stored."""

    def __init__(self, message, status=None, final_url=None):
        super().__init__(message)
        self.status = status
        self.final_url = final_url


class MissingSource(CorpusError):
    """The source is not saved in the corpus yet."""
    exit_code = common.EXIT_PRECONDITION


# ---------------------------------------------------------------- URLs and ids

def _clean_url(url: str) -> str:
    """Validate against the allow-list and return the https URL without a fragment."""
    url = (url or "").strip()
    try:
        u = urllib.parse.urlsplit(url)
        host = (u.hostname or "").lower()
        port = u.port
    except ValueError:
        raise PolicyError(f"not a valid URL: {url[:200]!r}")
    if u.scheme not in ("http", "https") or not host:
        raise PolicyError(f"not an http(s) URL: {url[:200]!r}")
    if host not in common.ALLOWED_HOSTS:
        raise PolicyError(f"host {host!r} is not in the allow-list ({', '.join(common.ALLOWED_HOSTS)})")
    if u.username or u.password or port not in (None, 443, 80):
        raise PolicyError(f"credentials or a custom port are not allowed: {url[:200]!r}")
    return urllib.parse.urlunsplit(("https", host, u.path or "/", u.query, ""))


def _is_docs_page(u) -> bool:
    name = u.path.rsplit("/", 1)[-1]
    return u.hostname == "docs.aws.amazon.com" and name not in KEEP_NAMES and name.endswith((".html", ".md"))


def _canonical(url: str) -> str:
    """The human URL to cite: https, no fragment, and .html for a docs page."""
    u = urllib.parse.urlsplit(_clean_url(url))
    path = u.path
    if _is_docs_page(u) and path.endswith(".md"):
        path = path[:-3] + ".html"
    return urllib.parse.urlunsplit((u.scheme, u.netloc, path, u.query, ""))


def _md_twin(url: str):
    """The .md twin of a docs .html page URL, or None."""
    u = urllib.parse.urlsplit(url)
    if _is_docs_page(u) and u.path.endswith(".html") and not u.query:
        return urllib.parse.urlunsplit((u.scheme, u.netloc, u.path[:-5] + ".md", "", ""))
    return None


_RE_UNSAFE = re.compile(r"[^A-Za-z0-9._~-]")
_PREFIX = {"docs.aws.amazon.com": "docs", "aws.amazon.com": "www", "d1.awsstatic.com": "static",
           "repost.aws": "repost", "pricing.us-east-1.amazonaws.com": "pricing"}


def source_id_for(url: str) -> str:
    """Stable id made from the URL (see the corpus layout). Raises PolicyError for a foreign host."""
    u = urllib.parse.urlsplit(_clean_url(url))
    host = u.hostname
    path = urllib.parse.unquote(u.path)
    qhash = hashlib.sha1(u.query.encode("utf-8")).hexdigest()[:8] if u.query else ""
    if host == "aws.amazon.com" and path.startswith("/api/"):
        params = urllib.parse.parse_qs(u.query)
        name = (params.get("item.directoryId") or [""])[0] or "-".join(s for s in path[5:].split("/") if s)
        name = _RE_UNSAFE.sub("_", name) or "api"
        return f"api/{name}" + (f"-{qhash}" if qhash else "")
    segs = []
    for seg in path.split("/"):
        if not seg:
            continue
        seg = _RE_UNSAFE.sub("_", seg)
        segs.append("_" if seg in (".", "..") else seg)
    if not segs:
        segs = ["index"]
    last = segs[-1]
    if last.endswith((".html", ".htm")):
        last = last.rsplit(".", 1)[0]
    elif host == "docs.aws.amazon.com" and last.endswith(".md") and last not in KEEP_NAMES:
        last = last[:-3]
    segs[-1] = (last or "index") + (f"~q{qhash}" if qhash else "")
    return _PREFIX.get(host, "other") + "/" + "/".join(segs)


def _check_source_id(source_id: str) -> str:
    sid = (source_id or "").strip()
    parts = sid.split("/")
    if (not sid or sid.startswith("/") or len(parts) < 2
            or any(p in ("", ".", "..") or _RE_UNSAFE.search(p) for p in parts)):
        raise PolicyError(f"bad source_id {source_id!r}")
    return sid


def snapshot_paths(source_id: str) -> dict:
    base = str(common.CORPUS / "snap" / _check_source_id(source_id))
    return {"raw": Path(base + ".raw"), "txt": Path(base + ".txt"), "meta": Path(base + ".meta.json")}


def load_meta(source_id: str):
    try:
        return common.read_json(snapshot_paths(source_id)["meta"])
    except (PolicyError, ValueError):
        return None


def load_text(source_id: str):
    try:
        path = snapshot_paths(source_id)["txt"]
    except PolicyError:
        return None
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------- politeness: rate, cap, log

def _log(**row) -> None:
    common.append_jsonl(common.CORPUS / "fetch.log.jsonl", {"ts": common.now_iso(), **row})


def _throttle(interval=None) -> None:
    """Reserve the next request slot (one per MIN_INTERVAL across all processes) and count it."""
    interval = MIN_INTERVAL if interval is None else interval
    state_path = common.CORPUS / "rate.json"
    with common.file_lock(state_path):
        try:
            state = common.read_json(state_path, {}) or {}
        except ValueError:
            state = {}
        now = time.time()
        day = common.today()
        if state.get("day") != day:
            state = {"day": day, "count": 0, "last": state.get("last", 0)}
        if int(state.get("count", 0)) >= DAILY_CAP:
            raise CapError(f"daily request cap reached ({DAILY_CAP} on {day}); try again tomorrow (UTC)")
        last = float(state.get("last", 0) or 0)
        if last > now + 600:        # a broken clock must not block the build
            last = now
        slot = max(now, last + interval)
        state["last"] = slot
        state["count"] = int(state.get("count", 0)) + 1
        common.write_json(state_path, state)
    if slot > now:
        _sleep(slot - now)


def requests_today() -> int:
    state = common.read_json(common.CORPUS / "rate.json", {}) or {}
    return int(state.get("count", 0)) if state.get("day") == common.today() else 0


# ---------------------------------------------------------------- transport

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None             # redirects are followed by _request, hop by hop, under the allow-list


def _transport(url: str, headers: dict, timeout: float):
    """One GET without redirect following. Returns (status, lower-cased headers, body bytes).

    Tests replace this function; nothing else in the module opens a socket.
    """
    opener = urllib.request.build_opener(_NoRedirect)
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        response = opener.open(request, timeout=timeout)
    except urllib.error.HTTPError as err:      # 3xx (not followed), 304, 4xx and 5xx land here
        response = err
    with response:
        status = getattr(response, "status", None) or response.getcode()
        hdrs = {k.lower(): v for k, v in response.headers.items()}
        body = response.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise FetchError(f"response larger than {MAX_BYTES} bytes: {url}", status=status)
    if hdrs.get("content-encoding", "").lower() == "gzip" and body:
        body = gzip.decompress(body)
    return status, hdrs, body


def _attempts(url: str, cond, sid, interval=None):
    headers = dict(BASE_HEADERS)
    headers.update(cond or {})
    for attempt in range(1, MAX_ATTEMPTS + 1):
        _throttle(interval)
        started = time.time()
        error = None
        try:
            status, hdrs, body = _transport(url, headers, TIMEOUT)
        except CorpusError:
            raise
        except (urllib.error.URLError, http.client.HTTPException, OSError, EOFError) as exc:
            status, hdrs, body, error = None, {}, b"", repr(exc)[:200]
        row = {"url": url, "status": status, "bytes": len(body), "ms": int((time.time() - started) * 1000),
               "attempt": attempt, "source_id": sid}
        if error:
            row["error"] = error
        _log(**row)
        if status is not None and status != 429 and status < 500:
            return status, hdrs, body
        if attempt < MAX_ATTEMPTS:
            delay = BACKOFF[min(attempt - 1, len(BACKOFF) - 1)]
            retry_after = hdrs.get("retry-after", "")
            if retry_after.isdigit():
                delay = min(max(delay, float(retry_after)), 120.0)
            _sleep(delay)
    raise TransientError(f"{url}: still failing after {MAX_ATTEMPTS} attempts (last status {status}, {error or 'no network error'})")


def _request(url: str, cond=None, sid=None, robots=True) -> Response:
    """GET with allow-list, robots.txt, rate limit, retries and in-allow-list redirects."""
    first = _clean_url(url)
    current = first
    chain = []
    for _hop in range(MAX_REDIRECTS + 1):
        interval = None
        if robots:
            interval = _robots_check(current)
        status, hdrs, body = _attempts(current, cond, sid, interval)
        if status in (301, 302, 303, 307, 308) and hdrs.get("location"):
            target = urllib.parse.urljoin(current, hdrs["location"])
            try:
                target = _clean_url(target)
            except PolicyError as exc:
                _log(url=current, status=status, source_id=sid, refused_redirect=target[:300])
                raise PolicyError(f"redirect from {current} refused: {exc}")
            chain.append(current)
            current = target
            continue
        return Response(status, hdrs, body, first, current, chain)
    raise FetchError(f"too many redirects starting at {first}", final_url=current)


# ---------------------------------------------------------------- robots.txt (RFC 9309 matching)

def _parse_robots(text: str, agent: str = "*"):
    """Return (rules, crawl_delay) of the groups that name `agent`. rules = [(allow, pattern)]."""
    groups, current, last_was_agent = [], None, False
    for raw in (text or "").splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            if not last_was_agent:
                current = {"agents": [], "rules": [], "delay": 0.0}
                groups.append(current)
            current["agents"].append(value.lower())
            last_was_agent = True
        elif key in ("allow", "disallow"):
            last_was_agent = False
            if current is not None and value:
                current["rules"].append((key == "allow", value))
        elif key == "crawl-delay":
            last_was_agent = False
            if current is not None:
                try:
                    current["delay"] = float(value)
                except ValueError:
                    pass
    rules, delay = [], 0.0
    for group in groups:
        if agent in group["agents"]:
            rules.extend(group["rules"])
            delay = max(delay, group["delay"])
    return rules, delay


def _robots_match(pattern: str, target: str) -> bool:
    anchored = pattern.endswith("$")
    if anchored:
        pattern = pattern[:-1]
    rx = "".join(".*" if ch == "*" else re.escape(ch) for ch in pattern)
    return re.match(rx + ("$" if anchored else ""), target) is not None


def _robots_allowed(rules, target: str) -> bool:
    """Longest matching pattern wins; Allow wins a tie; no match means allowed."""
    best_len, best_allow = -1, True
    for allow, pattern in rules:
        if _robots_match(pattern, target):
            if len(pattern) > best_len or (len(pattern) == best_len and allow):
                best_len, best_allow = len(pattern), allow
    return best_allow


def _robots_for(host: str):
    path = common.CORPUS / "robots" / f"{host}.json"
    key = str(path)
    memo = _ROBOTS_MEMO.get(key)
    now = time.time()
    if memo and now - memo[0] < ROBOTS_TTL:
        return memo[1], memo[2]
    cached = None
    try:
        cached = common.read_json(path)
    except ValueError:
        cached = None
    if not cached or now - float(cached.get("fetched_epoch", 0)) >= ROBOTS_TTL:
        resp = _request(f"https://{host}/robots.txt", sid=f"robots/{host}", robots=False)
        if resp.status == 200:
            text = resp.body.decode("utf-8", errors="replace")
        elif 400 <= resp.status < 500:
            text = ""           # RFC 9309: an unavailable robots.txt (4xx) means no restrictions
        else:
            raise TransientError(f"robots.txt for {host} answered {resp.status}; refusing to fetch until it is readable")
        cached = {"host": host, "status": resp.status, "fetched_epoch": now, "fetched_at": common.now_iso(), "text": text}
        common.write_json(path, cached)
    rules, delay = _parse_robots(cached.get("text", ""))
    _ROBOTS_MEMO[key] = (float(cached.get("fetched_epoch", now)), rules, delay)
    return rules, delay


def _robots_check(url: str):
    """Raise PolicyError when robots.txt disallows the URL. Returns the request interval to use."""
    u = urllib.parse.urlsplit(url)
    if u.path == "/robots.txt":
        return None
    rules, delay = _robots_for(u.hostname)
    target = (u.path or "/") + (f"?{u.query}" if u.query else "")
    if not _robots_allowed(rules, target):
        _log(url=url, status=None, refused="robots.txt")
        raise PolicyError(f"robots.txt of {u.hostname} disallows {target[:200]}")
    if delay and MIN_INTERVAL > 0:
        return max(MIN_INTERVAL, min(delay, 10.0))
    return None


# ---------------------------------------------------------------- HTML to visible text

_SKIP_TAGS = frozenset("script style nav header footer noscript template svg iframe".split())
_SKIP_MINIMAL = frozenset("script style noscript template svg".split())
_HEADINGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}
_BLOCK_TAGS = frozenset(("p div section article main aside ul ol dl dt dd thead tbody tfoot blockquote "
                         "figure figcaption details summary address hr form fieldset caption").split())
_RE_SPACE = re.compile(r"\s+")


class _VisibleText(HTMLParser):
    """Visible text with headings (# prefix), list items (- prefix) and table rows (| a | b |) on their own lines."""

    def __init__(self, skip=_SKIP_TAGS):
        super().__init__(convert_charrefs=True)
        self.skip = skip
        self.skip_depth = 0
        self.lines = []
        self.buf = []
        self.prefix = ""
        self.pre = 0
        self.in_title = False
        self.title_parts = []
        self.title_done = False
        self.row = None          # list of finished cells while inside <tr>
        self.cell = None         # list of text pieces while inside <td>/<th>
        self.row_has_th = False
        self.table_rows = 0
        self.table_stack = []

    # -- line handling
    def _flush(self, raw=False):
        text = "".join(self.buf)
        self.buf = []
        text = text.rstrip() if raw else _RE_SPACE.sub(" ", text).strip()
        if text.strip():
            self.lines.append(self.prefix + text)
            self.prefix = ""

    def _break(self):
        if self.cell is not None:
            self.cell.append(" ")
        elif self.row is None:
            self._flush()

    def _close_cell(self):
        if self.cell is not None:
            text = _RE_SPACE.sub(" ", "".join(self.cell)).strip().replace("|", "\\|")
            self.row.append(text)
            self.cell = None

    def _close_row(self):
        if self.row is None:
            return
        self._close_cell()
        cells, self.row = self.row, None
        if any(cells):
            self.lines.append("| " + " | ".join(cells) + " |")
            if self.row_has_th and self.table_rows == 0:
                self.lines.append("| " + " | ".join("---" for _ in cells) + " |")
            self.table_rows += 1
        self.row_has_th = False

    # -- parser events
    def handle_starttag(self, tag, attrs):
        if tag in self.skip:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "title" and not self.title_done:
            self.in_title = True
        elif tag in _HEADINGS:
            self._break()
            if self.cell is None and self.row is None:
                self.prefix = "#" * _HEADINGS[tag] + " "
        elif tag == "li":
            self._break()
            if self.cell is None and self.row is None:
                self.prefix = "- "
        elif tag == "br":
            if self.pre and self.cell is None:
                self._flush(raw=True)
            else:
                self._break()
        elif tag == "table":
            self._flush()
            self.table_stack.append((self.row, self.cell, self.row_has_th, self.table_rows))
            self.row, self.cell, self.row_has_th, self.table_rows = None, None, False, 0
        elif tag == "tr":
            self._close_row()
            if self.cell is None:
                self._flush()
            self.row = []
        elif tag in ("td", "th"):
            if self.row is None:
                self._flush()
                self.row = []
            self._close_cell()
            self.cell = []
            if tag == "th":
                self.row_has_th = True
        elif tag == "pre":
            self._break()
            self.pre += 1
        elif tag in _BLOCK_TAGS:
            self._break()

    def handle_endtag(self, tag):
        if tag in self.skip:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "title":
            if self.in_title:
                self.title_done = True
            self.in_title = False
        elif tag in _HEADINGS or tag == "li":
            self._break()
            if self.cell is None and self.row is None:
                self.prefix = ""
        elif tag in ("td", "th"):
            self._close_cell()
        elif tag == "tr":
            self._close_row()
        elif tag == "table":
            self._close_row()
            if self.table_stack:
                self.row, self.cell, self.row_has_th, self.table_rows = self.table_stack.pop()
        elif tag == "pre":
            if self.cell is None and self.row is None:
                self._flush(raw=True)
            self.pre = max(0, self.pre - 1)
        elif tag in _BLOCK_TAGS:
            self._break()

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.in_title:
            self.title_parts.append(data)
            return
        if self.cell is not None:
            self.cell.append(data)
        elif self.row is not None:
            return                      # whitespace between cells
        elif self.pre:
            pieces = data.split("\n")
            for i, piece in enumerate(pieces):
                self.buf.append(piece)
                if i < len(pieces) - 1:
                    self._flush(raw=True)
        else:
            self.buf.append(data)

    def result(self):
        self._close_row()
        self._flush()
        title = _RE_SPACE.sub(" ", "".join(self.title_parts)).strip()
        return "\n".join(self.lines) + ("\n" if self.lines else ""), title


def html_to_text(html_text: str):
    """Return (visible text, title). Script, style, nav, header and footer content is dropped."""
    parser = _VisibleText()
    parser.feed(html_text)
    parser.close()
    text, title = parser.result()
    if len(text) < 200 and len(html_text) > 5000:
        # An unclosed <header> or <nav> can swallow the page; retry while skipping only non-visible tags.
        fallback = _VisibleText(skip=_SKIP_MINIMAL)
        fallback.feed(html_text)
        fallback.close()
        text2, title2 = fallback.result()
        if len(text2) > len(text):
            text, title = text2, title or title2
    return text, title


# ---------------------------------------------------------------- snapshots

_RE_MD_ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>~])")
_RE_MD_H1 = re.compile(r"(?m)^#\s+(.+?)\s*$")
_RE_MD_ANCHOR = re.compile(r"<a\s+(?:name|id)=[^>]*>\s*</a>")


def _unescape_md(text: str) -> str:
    return _RE_MD_ESCAPE.sub(r"\1", text)


def _decode(body: bytes, content_type: str) -> str:
    match = re.search(r"charset=([\w.-]+)", content_type or "", re.I)
    charset = match.group(1) if match else "utf-8"
    try:
        text = body.decode(charset, errors="replace")
    except LookupError:
        text = body.decode("utf-8", errors="replace")
    return text.lstrip("﻿")


def _kind_of(url: str, content_type: str, body: bytes) -> str:
    ctype = (content_type or "").split(";")[0].strip().lower()
    path = urllib.parse.urlsplit(url).path.lower()
    head = body[:400].lstrip().lower()
    if ctype in ("text/html", "application/xhtml+xml") or head.startswith((b"<!doctype html", b"<html")):
        return "html"
    if "json" in ctype or (path.endswith(".json") and head[:1] in (b"{", b"[")):
        return "json"
    if ctype == "text/markdown" or path.endswith(".md"):
        return "markdown"
    if ctype.startswith("text/") or ctype in ("application/xml", "application/rss+xml") or path.endswith(".txt"):
        return "text"
    return "binary"


def _extract(kind: str, body: bytes, content_type: str):
    """Return (text, title) for a response body."""
    if kind == "binary":
        return "", ""
    text = _decode(body, content_type)
    if kind == "html":
        return html_to_text(text)
    title = ""
    if kind == "markdown":
        match = _RE_MD_H1.search(text)
        if match:
            title = _unescape_md(_RE_MD_ANCHOR.sub("", match.group(1))).strip()
    return text, title


def _write_bytes(path: Path, data: bytes) -> None:
    path = Path(path)
    common.ensure_dir(path.parent)
    tmp = path.with_name(path.name + f".tmp{os.getpid()}")
    tmp.write_bytes(data)
    os.replace(tmp, path)


def _lock_for(name: str) -> Path:
    return common.CORPUS / "locks" / hashlib.sha1(name.encode("utf-8")).hexdigest()[:20]


def _cond_headers(meta) -> dict:
    cond = {}
    if meta and meta.get("etag"):
        cond["If-None-Match"] = meta["etag"]
    if meta and meta.get("last_modified"):
        cond["If-Modified-Since"] = meta["last_modified"]
    return cond


def _twin_ok(resp: Response) -> bool:
    ctype = resp.headers.get("content-type", "").lower()
    head = resp.body[:200].lstrip().lower()
    return (resp.status == 200 and urllib.parse.urlsplit(resp.final_url).path.endswith(".md")
            and "html" not in ctype and not head.startswith((b"<!doctype", b"<html")) and bool(resp.body.strip()))


def _cached(source_id: str):
    paths = snapshot_paths(source_id)
    if paths["meta"].exists() and paths["raw"].exists() and paths["txt"].exists():
        try:
            return common.read_json(paths["meta"])
        except ValueError:
            return None
    return None


def fetch(url: str, revalidate: bool = False, source_id: str = None) -> dict:
    """Return the snapshot meta for a URL, fetching it once if it is not in the corpus.

    The returned dict is the stored meta plus `state`: cached, fetched, not-modified, unchanged or
    changed. Raises PolicyError (allow-list, robots.txt, daily cap), TransientError (429 / 5xx /
    network after retries) or FetchError (final non-200, see .status).
    `source_id` overrides the id made from the URL (use it to name API responses, "api/<name>").
    """
    clean = _clean_url(url)
    sid = _check_source_id(source_id) if source_id else source_id_for(clean)
    meta = _cached(sid)
    if meta and not revalidate:
        return dict(meta, state="cached")
    with common.file_lock(_lock_for(sid), timeout=900):
        meta = _cached(sid)
        if meta and not revalidate:
            return dict(meta, state="cached")
        return _fetch_locked(clean, sid, meta)


def _fetch_locked(clean: str, sid: str, old) -> dict:
    canonical = _canonical(clean)
    paths = snapshot_paths(sid)
    cond = _cond_headers(old)
    if old and old.get("fetched_url"):
        candidates = [old["fetched_url"]]          # revalidate exactly what was stored
    else:
        twin = _md_twin(canonical)
        candidates = [twin, canonical] if twin else [clean]
    resp = None
    for i, candidate in enumerate(candidates):
        is_twin_try = len(candidates) == 2 and i == 0
        resp = _request(candidate, cond=cond, sid=sid)
        if resp.status == 304 and old:
            old = dict(old, revalidated_at=common.now_iso())
            common.write_json(paths["meta"], old)
            return dict(old, state="not-modified")
        if is_twin_try and not _twin_ok(resp):
            continue                                # no .md twin: fall back to the HTML page
        break
    if resp.status != 200:
        raise FetchError(f"{resp.fetched_url}: HTTP {resp.status}" + (f" (final URL {resp.final_url})" if resp.chain else ""),
                         status=resp.status, final_url=resp.final_url)
    content_type = resp.headers.get("content-type", "")
    kind = _kind_of(resp.final_url, content_type, resp.body)
    text, title = _extract(kind, resp.body, content_type)
    sha = common.sha256_bytes(resp.body)
    meta = {
        "source_id": sid,
        "url": canonical,
        "fetched_url": resp.fetched_url,
        "final_url": resp.final_url,
        "status": resp.status,
        "content_type": content_type,
        "etag": resp.headers.get("etag", ""),
        "last_modified": resp.headers.get("last-modified", ""),
        "sha256": sha,
        "text_sha256": common.sha256_bytes(text.encode("utf-8")),
        "fetched_at": common.now_iso(),
        "title": title[:300],
        "bytes": len(resp.body),
        "kind": kind,
    }
    state = "fetched"
    if old:
        if old.get("sha256") == sha:
            state = "unchanged"
        else:
            state = "changed"
            meta["previous_sha256"] = old.get("sha256", "")
            meta["previous_fetched_at"] = old.get("fetched_at", "")
            if paths["txt"].exists():
                stamp = (old.get("fetched_at") or "unknown")[:10]
                keep = common.CORPUS / "history" / f"{sid}.{stamp}.{(old.get('sha256') or 'x')[:8]}.txt"
                _write_bytes(keep, paths["txt"].read_bytes())
    _write_bytes(paths["raw"], resp.body)
    _write_bytes(paths["txt"], text.encode("utf-8"))
    common.write_json(paths["meta"], meta)          # written last: the meta file commits the snapshot
    return dict(meta, state=state)


def reextract(source_id: str) -> dict:
    """Rebuild the .txt of a snapshot from its .raw without any request (after an extractor fix)."""
    meta = _cached(source_id)
    if not meta:
        raise CorpusError(f"{source_id} is not in the corpus")
    paths = snapshot_paths(source_id)
    with common.file_lock(_lock_for(source_id), timeout=900):
        body = paths["raw"].read_bytes()
        kind = _kind_of(meta.get("final_url", ""), meta.get("content_type", ""), body)
        text, title = _extract(kind, body, meta.get("content_type", ""))
        meta.update(kind=kind, title=title[:300], text_sha256=common.sha256_bytes(text.encode("utf-8")))
        _write_bytes(paths["txt"], text.encode("utf-8"))
        common.write_json(paths["meta"], meta)
    return dict(meta, state="re-extracted")


def fetch_file(url: str, dest: Path, revalidate: bool = False, source_id: str = None) -> dict:
    """Download a URL to `dest` as it is (with <dest>.meta.json beside it). Used for full.md and binaries."""
    clean = _clean_url(url)
    dest = Path(dest)
    meta_path = Path(str(dest) + ".meta.json")
    sid = source_id or f"file/{dest.name}"

    def cached():
        if dest.exists() and meta_path.exists():
            try:
                return common.read_json(meta_path)
            except ValueError:
                return None
        return None

    old = cached()
    if old and old.get("url") == clean and not revalidate:
        return dict(old, state="cached")
    with common.file_lock(_lock_for(str(dest)), timeout=900):
        old = cached()
        if old and old.get("url") != clean:
            old = None
        if old and not revalidate:
            return dict(old, state="cached")
        resp = _request(clean, cond=_cond_headers(old), sid=sid)
        if resp.status == 304 and old:
            old = dict(old, revalidated_at=common.now_iso())
            common.write_json(meta_path, old)
            return dict(old, state="not-modified")
        if resp.status != 200:
            raise FetchError(f"{clean}: HTTP {resp.status}", status=resp.status, final_url=resp.final_url)
        sha = common.sha256_bytes(resp.body)
        meta = {"url": clean, "final_url": resp.final_url, "status": resp.status,
                "content_type": resp.headers.get("content-type", ""), "etag": resp.headers.get("etag", ""),
                "last_modified": resp.headers.get("last-modified", ""), "sha256": sha,
                "fetched_at": common.now_iso(), "bytes": len(resp.body), "path": common.rel(dest)}
        state = "fetched" if not old else ("unchanged" if old.get("sha256") == sha else "changed")
        _write_bytes(dest, resp.body)
        common.write_json(meta_path, meta)
        return dict(meta, state=state)


# ---------------------------------------------------------------- guide index

_RE_MD_LINK = re.compile(r"\[([^\]]+)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_HISTORY_NAME = re.compile(r"(?i)^(whatsnew|documenthistory|document-history|doc-history|dochistory|history)$")
_HISTORY_NAME2 = re.compile(r"(?i)(release-notes|releasenotes|-releases$|^releases$|doc-?history|document-?history)")
_HISTORY_TITLE = re.compile(r"(?i)\b(document|doc|documentation)\s+history\b")
_HISTORY_TITLE2 = re.compile(r"(?i)\brelease notes\b|\breleases\b|what'?s new")
_QUOTA_NAME = re.compile(r"(?i)(^|[-_])(limits|quotas|quota|limit)$")
_QUOTA_NAME2 = re.compile(r"(?i)limits|quotas")
_QUOTA_TITLE = re.compile(r"(?i)\bquotas\b")
_QUOTA_TITLE2 = re.compile(r"(?i)\bquota\b|\blimits\b|\brestrictions\b")


def guide_root(root: str) -> str:
    """Normalise a guide root URL: https, ends with '/', without llms.txt or a page name."""
    u = urllib.parse.urlsplit(_clean_url(root))
    path = u.path
    if not path.endswith("/"):
        head, _, last = path.rpartition("/")
        path = (head + "/") if "." in last else (path + "/")
    return urllib.parse.urlunsplit((u.scheme, u.netloc, path, "", ""))


def guide_id_for(root: str) -> str:
    """vpc/latest/userguide -> vpc-userguide; AmazonS3/latest/userguide -> amazons3-userguide."""
    path = urllib.parse.urlsplit(guide_root(root)).path
    segs = [s for s in path.split("/") if s and s.lower() != "latest"]
    return common.slugify("-".join(segs)) or "guide"


def _score_history(title: str, name: str) -> int:
    score = 0
    if _HISTORY_TITLE.search(title):
        score += 10
    elif _HISTORY_TITLE2.search(title):
        score += 4
    if _HISTORY_NAME.match(name):
        score += 8
    elif _HISTORY_NAME2.search(name):
        score += 5
    return score


def _score_quotas(title: str, name: str) -> int:
    score = 0
    if _QUOTA_TITLE.search(title):
        score += 6
    elif _QUOTA_TITLE2.search(title):
        score += 3
    if _QUOTA_NAME.search(name):
        score += 6
    elif _QUOTA_NAME2.search(name):
        score += 3
    return score


def _best(pages, scorer, minimum):
    scored = []
    for order, page in enumerate(pages):
        name = page["url"].rsplit("/", 1)[-1].rsplit(".", 1)[0]
        score = scorer(page["title"], name)
        if score >= minimum:
            scored.append((-score, len(page["title"]), order, page))
    scored.sort(key=lambda item: item[:3])
    ranked = [dict(item[3], score=-item[0]) for item in scored]
    return (ranked[0] if ranked else None), ranked[:5]


def parse_llms(text: str, root: str) -> dict:
    """Parse a guide's llms.txt into title, pages (inside the guide) and the full.md link."""
    root = guide_root(root)
    title_match = _RE_MD_H1.search(text)
    title = _unescape_md(title_match.group(1)).strip() if title_match else ""
    pages, seen, full_url, outside = [], set(), None, 0
    for match in _RE_MD_LINK.finditer(text):
        link_title = _RE_SPACE.sub(" ", _unescape_md(match.group(1))).strip()
        target = urllib.parse.urljoin(root + "llms.txt", match.group(2))
        try:
            target = _clean_url(target)
        except PolicyError:
            outside += 1
            continue
        name = urllib.parse.urlsplit(target).path.rsplit("/", 1)[-1]
        if name in ("full.md", "llms-full.txt") and target.startswith(root):
            full_url = full_url or target
            continue
        if not target.startswith(root) or not name.endswith((".md", ".html")):
            outside += 1
            continue
        url = _canonical(target)
        sid = source_id_for(url)
        if sid in seen:
            continue
        seen.add(sid)
        pages.append({"title": link_title, "url": url, "md_url": url[:-5] + ".md" if url.endswith(".html") else url,
                      "source_id": sid})
    return {"title": title, "pages": pages, "full_url": full_url, "links_outside_guide": outside}


def build_guide(root: str, guide_id: str = None, revalidate: bool = False) -> dict:
    """Fetch <root>/llms.txt and <root>/full.md and write index/<guide-id>.json. Returns the index."""
    root = guide_root(root)
    gid = common.slugify(guide_id) if guide_id else guide_id_for(root)
    llms_meta = fetch(root + "llms.txt", revalidate=revalidate)
    parsed = parse_llms(load_text(llms_meta["source_id"]) or "", root)
    if not parsed["pages"]:
        raise CorpusError(f"{root}llms.txt lists no pages inside the guide (kind {llms_meta.get('kind')}, final URL {llms_meta.get('final_url')})")
    warnings = []
    full = None
    full_url = parsed["full_url"] or (root + "full.md")
    try:
        full_meta = fetch_file(full_url, common.CORPUS / "full" / f"{gid}.md", revalidate=revalidate, source_id=f"full/{gid}")
        full = {k: full_meta.get(k) for k in ("url", "path", "bytes", "sha256", "etag", "last_modified", "fetched_at", "state")}
    except FetchError as exc:
        warnings.append(f"full.md not stored: {exc}")
    history, history_candidates = _best(parsed["pages"], _score_history, 5)
    quotas, quota_candidates = _best(parsed["pages"], _score_quotas, 6)
    if not history:
        warnings.append("no document-history page found by link text or page name")
    if not quotas:
        warnings.append("no quotas or limits page found by link text or page name")
    index = {
        "guide_id": gid, "root": root, "title": parsed["title"],
        "llms_url": root + "llms.txt", "llms_source_id": llms_meta["source_id"],
        "full_md": full, "built_at": common.now_iso(),
        "page_count": len(parsed["pages"]), "links_outside_guide": parsed["links_outside_guide"],
        "history": history, "quotas": quotas,
        "history_candidates": history_candidates, "quotas_candidates": quota_candidates,
        "warnings": warnings, "pages": parsed["pages"],
    }
    common.write_json(common.CORPUS / "index" / f"{gid}.json", index)
    return index


def load_index(guide_id: str):
    return common.read_json(common.CORPUS / "index" / f"{common.slugify(guide_id)}.json")


# ---------------------------------------------------------------- reading: resolve, search, show, tables

_RE_HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.*\S)\s*$")
_RE_FENCE = re.compile(r"^\s{0,3}(```|~~~)")
_TEXT_SUFFIXES = (".txt", ".md", ".jsonl", ".json")


def resolve_source(spec: str):
    """SOURCE -> (label, path, meta). SOURCE is a source_id, a URL, full:<guide-id>, or <scope>:<file>."""
    spec = (spec or "").strip()
    if spec.startswith(("http://", "https://")):
        spec = source_id_for(spec)
    match = re.match(r"^(full|faq|changes|cases):(.+)$", spec)
    if match:
        scope, name = match.group(1), match.group(2)
        if scope == "full" and not name.endswith(".md"):
            name += ".md"
        base = (common.CORPUS / scope).resolve()
        path = (base / name).resolve()
        try:
            path.relative_to(base)
        except ValueError:
            raise PolicyError(f"bad source {spec!r}")
        meta = None
        if scope == "full":
            meta = common.read_json(Path(str(path) + ".meta.json"))
        return f"{scope}:{name[:-3] if scope == 'full' else name}", path, meta
    sid = _check_source_id(spec)
    return sid, snapshot_paths(sid)["txt"], load_meta(sid)


def _clean_heading(text: str) -> str:
    return _unescape_md(_RE_MD_ANCHOR.sub("", text)).strip()[:120]


def _context(line: str, start: int, end: int, width: int = 200) -> str:
    if len(line) <= width:
        return line.strip()
    half = max(0, (width - (end - start)) // 2)
    a = max(0, start - half)
    b = min(len(line), a + width)
    a = max(0, b - width)
    return ("..." if a > 0 else "") + line[a:b].strip() + ("..." if b < len(line) else "")


def _search_files(scope: str, guide: str = None):
    """Yield (label, path) pairs for a scope, in a stable order."""
    corpus = common.CORPUS
    scopes = ("full", "snap", "faq", "changes", "cases") if scope == "all" else (scope,)
    index = load_index(guide) if guide else None
    gid = common.slugify(guide) if guide else None
    for sc in scopes:
        base = corpus / sc
        if not base.is_dir():
            continue
        if sc == "full":
            for path in sorted(base.glob("*.md")):
                if gid is None or path.stem == gid:
                    yield f"full:{path.stem}", path
        elif sc == "snap":
            if guide:
                if not index:
                    continue
                for page in index.get("pages", []):
                    path = snapshot_paths(page["source_id"])["txt"]
                    if path.exists():
                        yield page["source_id"], path
            else:
                for path in sorted(base.rglob("*.txt")):
                    yield str(path.relative_to(base))[:-4], path
        elif not guide:
            for path in sorted(base.rglob("*")):
                if path.is_file() and path.suffix in _TEXT_SUFFIXES and not path.name.endswith(".meta.json"):
                    yield f"{sc}:{path.relative_to(base)}", path


def search_corpus(pattern: str, scope: str = "all", guide: str = None, regex: bool = False,
                  limit: int = 20, per_file: int = 5) -> dict:
    """Bounded search over saved text. Matching ignores case and Markdown backslash escapes."""
    if scope not in SEARCH_SCOPES:
        raise CorpusError(f"unknown scope {scope!r}")
    limit = max(1, min(int(limit), SEARCH_MAX_LIMIT))
    if regex:
        try:
            rx = re.compile(pattern, re.IGNORECASE)
        except re.error as exc:
            raise CorpusError(f"bad regular expression: {exc}")
    else:
        needle = _RE_SPACE.sub(" ", _unescape_md(pattern)).strip().lower()
        if not needle:
            raise CorpusError("empty search pattern")
        rx = re.compile(r"\s+".join(re.escape(part) for part in needle.split(" ")), re.IGNORECASE)
    hits, total, files, files_hit = [], 0, 0, 0
    for label, path in _search_files(scope, guide):
        files += 1
        in_file, heading, fence = 0, "", False
        try:
            handle = open(path, encoding="utf-8", errors="replace")
        except OSError:
            continue
        with handle:
            for number, raw in enumerate(handle, 1):
                if _RE_FENCE.match(raw):
                    fence = not fence
                elif not fence:
                    h = _RE_HEADING.match(raw)
                    if h:
                        heading = _clean_heading(h.group(2))
                line = _unescape_md(raw.rstrip("\n"))
                match = rx.search(line)
                if not match:
                    continue
                total += 1
                in_file += 1
                if in_file == 1:
                    files_hit += 1
                if len(hits) < limit and (not per_file or in_file <= per_file):
                    hits.append({"source": label, "line": number, "heading": heading,
                                 "context": _context(line, match.start(), match.end())})
    return {"pattern": pattern, "scope": scope, "guide": guide, "regex": bool(regex), "limit": limit,
            "files_searched": files, "files_with_hits": files_hit, "total_hits": total,
            "shown": len(hits), "hits": hits}


def _split_row(line: str) -> list:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", s)]


_RE_RULE_ROW = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")


def _header_key(cell: str) -> str:
    key = _unescape_md(cell).replace("**", "").replace("`", "")
    key = re.sub(r"<[^>]{0,200}>", " ", key)
    return _RE_SPACE.sub(" ", key).strip()


def parse_tables(text: str) -> list:
    """Parse Markdown pipe tables. Each table: index, line, heading, header_text, headers, rows.

    A row is {"line": n, "text": <the row as written>, "cells": {header: cell}}. Cell text is
    verbatim (only trimmed), so "<row text>" or a cell can be used as a quote.
    """
    lines = text.splitlines()
    tables, heading, fence, i = [], "", False, 0
    while i < len(lines):
        line = lines[i]
        if _RE_FENCE.match(line):
            fence = not fence
            i += 1
            continue
        if fence:
            i += 1
            continue
        h = _RE_HEADING.match(line)
        if h:
            heading = _clean_heading(h.group(2))
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if "|" in line and "-" in nxt and ("|" in nxt or line.strip().startswith("|")) and _RE_RULE_ROW.match(nxt) \
                and not _RE_RULE_ROW.match(line):
            raw_headers = _split_row(line)
            headers, used = [], {}
            for pos, cell in enumerate(raw_headers, 1):
                key = _header_key(cell) or f"col{pos}"
                used[key] = used.get(key, 0) + 1
                headers.append(key if used[key] == 1 else f"{key} ({used[key]})")
            rows, j = [], i + 2
            while j < len(lines) and lines[j].strip() and "|" in lines[j]:
                cells = _split_row(lines[j])
                if len(cells) > len(headers):
                    cells = cells[:len(headers) - 1] + [" | ".join(cells[len(headers) - 1:])]
                cells += [""] * (len(headers) - len(cells))
                rows.append({"line": j + 1, "text": lines[j].strip(), "cells": dict(zip(headers, cells))})
                j += 1
            tables.append({"index": len(tables), "line": i + 1, "heading": heading,
                           "header_text": line.strip(), "headers": headers, "rows": rows})
            i = j
            continue
        i += 1
    return tables


def tables_for(source: str) -> list:
    """Tables of a snapshot (source_id, URL or full:<guide-id>). Raises CorpusError if it is not saved."""
    label, path, _meta = resolve_source(source)
    if not path.exists():
        raise MissingSource(f"{label} is not in the corpus; run: saa.py fetch <url>")
    return parse_tables(path.read_text(encoding="utf-8", errors="replace"))


def excerpt(source: str, around: str = None, lines: str = None, chars: int = 2000, occurrence: int = 1) -> dict:
    """A bounded excerpt of a saved text. Returns label, url, start_line, end_line, total_lines, text."""
    label, path, meta = resolve_source(source)
    if not path.exists():
        raise MissingSource(f"{label} is not in the corpus; run: saa.py fetch <url>")
    chars = max(200, min(int(chars or 2000), SHOW_MAX_CHARS))
    all_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    total = len(all_lines)
    truncated = False
    match_line = None
    if lines:
        single = re.match(r"^\s*(\d+)\s*$", lines)
        m = re.match(r"^\s*(\d*)\s*[:\-,]\s*(\d*)\s*$", lines)
        if single:
            a = b = int(single.group(1))
        elif m:
            a = int(m.group(1)) if m.group(1) else 1
            b = int(m.group(2)) if m.group(2) else total
        else:
            raise CorpusError(f"--lines needs A:B, got {lines!r}")
        a = max(1, a)
        b = min(total, b, a + SHOW_MAX_LINES - 1)
        if a > total:
            raise CorpusError(f"{label} has only {total} lines")
        start, end = a, b
        budget = SHOW_MAX_CHARS
    elif around:
        needle = _RE_SPACE.sub(" ", _unescape_md(around)).strip().lower()
        rx = re.compile(r"\s+".join(re.escape(p) for p in needle.split(" ")), re.IGNORECASE) if needle else None
        norm = common.normalize_text(around)
        found, pos = 0, None
        for number, raw in enumerate(all_lines, 1):
            m = rx.search(_unescape_md(raw)) if rx else None
            if m or (norm and norm in common.normalize_text(raw)):
                found += 1
                if found == max(1, int(occurrence or 1)):
                    match_line, pos = number, (m.start() if m else 0)
                    break
        if match_line is None:
            raise CorpusError(f"text not found in {label}: {around[:80]!r}" + (f" (occurrence {occurrence})" if found else ""))
        start = end = match_line
        size = len(all_lines[match_line - 1])
        grow = True
        while grow and size < chars:
            grow = False
            if start > 1 and size + len(all_lines[start - 2]) + 1 <= chars:
                start -= 1
                size += len(all_lines[start - 1]) + 1
                grow = True
            if end < total and size + len(all_lines[end]) + 1 <= chars:
                end += 1
                size += len(all_lines[end - 1]) + 1
                grow = True
        budget = chars
        if start == end and size > chars:
            line = _unescape_md(all_lines[match_line - 1])
            return {"source": label, "url": (meta or {}).get("url", ""), "fetched_at": (meta or {}).get("fetched_at", ""),
                    "start_line": start, "end_line": end, "total_lines": total, "match_line": match_line,
                    "truncated": True, "text": _context(line, pos, pos + len(needle), chars)}
    else:
        start, end, size = 1, 0, 0
        while end < total and end < SHOW_MAX_LINES and (end == 0 or size + len(all_lines[end]) + 1 <= chars):
            size += len(all_lines[end]) + 1
            end += 1
        end = max(end, min(1, total))
        budget = chars
    text = "\n".join(all_lines[start - 1:end])
    if len(text) > budget:
        text, truncated = text[:budget], True
    return {"source": label, "url": (meta or {}).get("url", ""), "fetched_at": (meta or {}).get("fetched_at", ""),
            "start_line": start, "end_line": end, "total_lines": total, "match_line": match_line,
            "truncated": truncated, "text": text}


# ---------------------------------------------------------------- CLI

def _row(meta: dict) -> dict:
    """What `fetch` prints for one snapshot: ids, numbers and paths. Never the body."""
    paths = snapshot_paths(meta["source_id"])
    return {"source_id": meta["source_id"], "state": meta.get("state", ""), "status": meta.get("status"),
            "kind": meta.get("kind", ""), "bytes": meta.get("bytes"), "title": (meta.get("title") or "")[:100],
            "url": meta.get("url", ""), "final_url": meta.get("final_url", ""),
            "fetched_at": meta.get("fetched_at", ""),
            "raw": common.rel(paths["raw"]), "txt": common.rel(paths["txt"]), "meta": common.rel(paths["meta"])}


def _worst(codes) -> int:
    for code in (common.EXIT_POLICY, common.EXIT_FAIL, common.EXIT_PRECONDITION, common.EXIT_TRANSIENT, common.EXIT_WARN):
        if code in codes:
            return code
    return common.EXIT_OK


def cmd_fetch(args) -> int:
    urls = list(args.urls or [])
    if args.batch:
        batch = Path(args.batch)
        if not batch.is_absolute():
            batch = common.REPO / batch
        if not batch.exists():
            return common.fail(f"batch file not found: {args.batch}", common.EXIT_PRECONDITION)
        for line in batch.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line.split()[0])
    if not urls:
        return common.fail("fetch needs at least one URL or --batch FILE", common.EXIT_PRECONDITION)

    if args.binary_to:
        if len(urls) != 1:
            return common.fail("--binary-to takes exactly one URL", common.EXIT_PRECONDITION)
        dest = Path(args.binary_to)
        if not dest.is_absolute():
            dest = common.REPO / dest
        if not common.inside_book(dest):
            return common.fail(f"--binary-to must be a path inside {common.REAL_BOOK}", common.EXIT_POLICY)
        try:
            meta = fetch_file(urls[0], dest, revalidate=args.revalidate, source_id=f"binary/{dest.name}")
        except CorpusError as exc:
            return common.fail(str(exc), exc.exit_code)
        result = {"state": meta["state"], "status": meta["status"], "bytes": meta["bytes"], "sha256": meta["sha256"],
                  "content_type": meta["content_type"], "url": meta["url"], "final_url": meta["final_url"],
                  "path": common.rel(dest), "meta": common.rel(Path(str(dest) + ".meta.json"))}
        if args.json:
            common.emit(result, args)
        else:
            common.emit(f"{result['state']} binary status={result['status']} bytes={result['bytes']} "
                        f"sha256={result['sha256'][:16]}\n  path={result['path']}", args)
        return common.EXIT_OK

    rows, codes, text = [], set(), []
    for url in urls:
        try:
            if args.reextract:
                meta = reextract(source_id_for(url) if "://" in url else url)
            else:
                meta = fetch(url, revalidate=args.revalidate)
            row = _row(meta)
            rows.append(row)
            text.append(f"{row['state']} {row['source_id']} status={row['status']} kind={row['kind']} bytes={row['bytes']}"
                        f" title={row['title']!r}\n  txt={row['txt']}\n  meta={row['meta']}")
        except CorpusError as exc:
            codes.add(exc.exit_code)
            row = {"url": url[:300], "state": "error", "exit": exc.exit_code, "error": str(exc)[:300],
                   "status": getattr(exc, "status", None)}
            rows.append(row)
            text.append(f"error exit={exc.exit_code} {url[:300]}\n  {row['error']}")
            if isinstance(exc, CapError):
                break
    summary = collections.Counter(r["state"] for r in rows)
    if args.json:
        common.emit({"results": rows, "summary": dict(summary), "requests_today": requests_today()}, args)
    else:
        if len(rows) > 1:
            text.append("summary: " + ", ".join(f"{k}={v}" for k, v in sorted(summary.items())))
        common.emit("\n".join(text), args)
    return _worst(codes)


def cmd_guide(args) -> int:
    try:
        index = build_guide(args.root, guide_id=args.id, revalidate=args.revalidate)
    except CorpusError as exc:
        return common.fail(str(exc), exc.exit_code)
    index_path = common.rel(common.CORPUS / "index" / f"{index['guide_id']}.json")
    if args.json:
        short = {k: v for k, v in index.items() if k != "pages"}
        short["index_path"] = index_path
        common.emit(short, args)
    else:
        def pointer(item):
            return f"{item['title']!r} {item['source_id']} (score {item['score']})" if item else "not found"
        full = index["full_md"]
        out = [f"guide {index['guide_id']}: {index['title']!r}, {index['page_count']} pages",
               f"  index={index_path}",
               f"  full={full['path']} bytes={full['bytes']} {full['state']}" if full else "  full=missing",
               f"  history: {pointer(index['history'])}",
               f"  quotas:  {pointer(index['quotas'])}"]
        out += [f"  warning: {w}" for w in index["warnings"]]
        common.emit("\n".join(out), args)
    return common.EXIT_WARN if index["warnings"] else common.EXIT_OK


def cmd_search(args) -> int:
    try:
        result = search_corpus(args.pattern, scope=args.scope, guide=args.guide, regex=args.regex,
                               limit=args.limit, per_file=args.per_file)
    except CorpusError as exc:
        return common.fail(str(exc), exc.exit_code)
    if args.json:
        common.emit(result, args)
    else:
        out = []
        for hit in result["hits"]:
            head = f" [{hit['heading']}]" if hit["heading"] else ""
            out.append(f"{hit['source']}:{hit['line']}{head}  {hit['context']}")
        out.append(f"{result['shown']} of {result['total_hits']} hits shown; {result['files_with_hits']} of "
                   f"{result['files_searched']} files matched (scope {result['scope']}, limit {result['limit']})")
        common.emit("\n".join(out), args)
    return common.EXIT_OK if result["total_hits"] else common.EXIT_FAIL


def cmd_show(args) -> int:
    try:
        result = excerpt(args.source, around=args.around, lines=args.lines, chars=args.chars, occurrence=args.occurrence)
    except CorpusError as exc:
        return common.fail(str(exc), exc.exit_code)
    if args.json:
        common.emit(result, args)
    else:
        head = (f"[{result['source']}] lines {result['start_line']}-{result['end_line']} of {result['total_lines']}"
                + (f" | match at line {result['match_line']}" if result["match_line"] else "")
                + (f" | {result['url']}" if result["url"] else "")
                + (f" | fetched {result['fetched_at']}" if result["fetched_at"] else "")
                + (" | truncated" if result["truncated"] else ""))
        common.emit(head + "\n" + result["text"], args)
    return common.EXIT_OK


def cmd_tables(args) -> int:
    try:
        label, _path, meta = resolve_source(args.source)
        tables = tables_for(args.source)
    except CorpusError as exc:
        return common.fail(str(exc), exc.exit_code)
    if args.index is not None:
        if not 0 <= args.index < len(tables):
            return common.fail(f"{label} has {len(tables)} tables; --index {args.index} does not exist", common.EXIT_FAIL)
        chosen = [tables[args.index]]
    else:
        chosen = tables
    full = args.index is not None or args.all
    if args.json:
        payload = chosen if full else [dict({k: v for k, v in t.items() if k != "rows"}, row_count=len(t["rows"])) for t in chosen]
        common.emit({"source": label, "url": (meta or {}).get("url", ""), "table_count": len(tables), "tables": payload}, args)
    else:
        out = [f"[{label}] {len(tables)} tables" + (f" | {(meta or {}).get('url', '')}" if meta else "")]
        for t in chosen:
            out.append(f"table {t['index']} at line {t['line']}, {len(t['rows'])} rows, under heading {t['heading']!r}")
            out.append(f"  header: {t['header_text'][:400]}")
            if full:
                out += [f"  L{r['line']}: {r['text'][:600]}" for r in t["rows"]]
        if not tables:
            out.append("no Markdown tables found")
        common.emit("\n".join(out), args)
    return common.EXIT_OK if tables else common.EXIT_WARN


def register(subparsers) -> None:
    p = subparsers.add_parser("fetch", help="cached, polite fetch of AWS pages into the corpus (the only network path)")
    p.add_argument("urls", nargs="*", metavar="URL")
    p.add_argument("--batch", metavar="FILE", help="file with one URL per line (# starts a comment)")
    p.add_argument("--revalidate", action="store_true", help="ask the server again with If-None-Match / If-Modified-Since")
    p.add_argument("--binary-to", metavar="PATH", help="save one binary download to this path inside the book")
    p.add_argument("--reextract", action="store_true", help="rebuild .txt from the saved .raw; no request is made")
    common.add_common_args(p)
    p.set_defaults(func=cmd_fetch)

    p = subparsers.add_parser("guide", help="fetch a guide's llms.txt and full.md and build its page index")
    p.add_argument("root", metavar="ROOT", help="guide root URL, for example https://docs.aws.amazon.com/vpc/latest/userguide/")
    p.add_argument("--id", help="guide id to use instead of the one made from the URL")
    p.add_argument("--revalidate", action="store_true")
    common.add_common_args(p)
    p.set_defaults(func=cmd_guide)

    p = subparsers.add_parser("search", help="bounded search over the saved corpus text")
    p.add_argument("pattern", metavar="PATTERN")
    p.add_argument("--scope", choices=SEARCH_SCOPES, default="all")
    p.add_argument("--guide", metavar="ID", help="only this guide (its full.md and its saved pages)")
    p.add_argument("--regex", action="store_true", help="PATTERN is a regular expression (case-insensitive)")
    p.add_argument("--limit", type=int, default=20, help=f"hits to show (default 20, at most {SEARCH_MAX_LIMIT})")
    p.add_argument("--per-file", type=int, default=5, help="hits to show per file (default 5, 0 = no per-file limit)")
    common.add_common_args(p)
    p.set_defaults(func=cmd_search)

    p = subparsers.add_parser("show", help="bounded excerpt of a saved page")
    p.add_argument("source", metavar="SOURCE", help="source_id, URL, or full:<guide-id>")
    p.add_argument("--around", metavar="TEXT", help="centre the excerpt on this text")
    p.add_argument("--occurrence", type=int, default=1, help="which match of --around (default 1)")
    p.add_argument("--lines", metavar="A:B", help="line range, 1-based and inclusive")
    p.add_argument("--chars", type=int, default=2000, help=f"size of the excerpt (default 2000, at most {SHOW_MAX_CHARS})")
    common.add_common_args(p)
    p.set_defaults(func=cmd_show)

    p = subparsers.add_parser("tables", help="parse the Markdown tables of a saved page into header-keyed rows")
    p.add_argument("source", metavar="SOURCE", help="source_id, URL, or full:<guide-id>")
    p.add_argument("--index", type=int, help="print the rows of table N (0-based)")
    p.add_argument("--all", action="store_true", help="print the rows of every table")
    common.add_common_args(p)
    p.set_defaults(func=cmd_tables)
