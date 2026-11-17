"""Shared helpers for every saa.py module. Standard library only (system Python 3.14).

Rules for module authors:
- Import paths and helpers from here; never hard-code directories.
- Every subcommand takes the common options added by add_common_args() and prints through emit().
- Return one of the EXIT_* codes from the subcommand function.
- All writes to shared stores (facts, registry, ledger, question bank) happen inside file_lock().
- normalize_text() is the ONLY normaliser used to compare a quote with a page snapshot.
"""
from __future__ import annotations

import contextlib
import fcntl
import hashlib
import html
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent      # aws-saa-book/tools
REAL_BOOK = TOOLS.parent                            # the real aws-saa-book folder
# `saa.py --book-dir DIR ...` (or SAA_BOOK_DIR) points every path below at a sandbox copy, so tests
# and gate-breaking experiments never touch real data. Reference paths as `common.X` at call time
# (never `from saalib.common import X`) so tests can also patch them.
BOOK = Path(os.environ["SAA_BOOK_DIR"]).resolve() if os.environ.get("SAA_BOOK_DIR") else REAL_BOOK
REPO = REAL_BOOK.parent
BUILD = BOOK / "_build"                             # ignored by git
DATA = BOOK / "data"                                # structured sources (tracked)
CORPUS = BUILD / "corpus"                           # saved AWS page snapshots
SPEC_DIR = BUILD / "spec"
STYLE_DIR = BUILD / "style"
SCHEMA_DIR = BUILD / "schemas"
REGISTRY = BUILD / "registry"
LEDGER = BUILD / "ledger"
REPORTS = BUILD / "reports"
TMP = BUILD / "tmp"
SITE = BUILD / "site"
FACTS_DIR = DATA / "facts"                          # data/facts/<service>.jsonl  (source of truth)
FACTSHEETS = BOOK / "facts"                         # facts/<service>.md          (generated, reader-facing)
DIAGRAM_SRC = BOOK / "diagrams" / "src"
DIAGRAM_SVG = BOOK / "diagrams" / "svg"
EXPORTS = BOOK / "exports"
WEB_SRC = TOOLS / "web"
TESTS = TOOLS / "tests"
FIXTURES = TESTS / "fixtures"

EXIT_OK = 0             # pass
EXIT_FAIL = 1           # blocking failure (a JSON report was written or printed)
EXIT_WARN = 2           # warnings only
EXIT_PRECONDITION = 3   # precondition missing or stale
EXIT_POLICY = 4         # policy refusal (host not allowed, robots.txt, path outside the book)
EXIT_TRANSIENT = 5      # transient problem, safe to retry

ALLOWED_HOSTS = (
    "docs.aws.amazon.com",
    "aws.amazon.com",
    "d1.awsstatic.com",
    "repost.aws",
    "pricing.us-east-1.amazonaws.com",
)

def _find_chrome() -> str:
    """Headless Chrome for diagram previews and the web self-test. SAA_CHROME overrides the search."""
    import shutil
    env = os.environ.get("SAA_CHROME")
    if env:
        return env
    for cand in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                 os.path.expanduser("~/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
                 "/Applications/Chromium.app/Contents/MacOS/Chromium",
                 shutil.which("google-chrome") or "", shutil.which("google-chrome-stable") or "",
                 shutil.which("chromium") or "", shutil.which("chromium-browser") or ""):
        if cand and os.path.exists(cand):
            return cand
    return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


CHROME = _find_chrome()


# ---------------------------------------------------------------- small utilities

def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def today() -> str:
    return time.strftime("%Y-%m-%d", time.gmtime())


def ensure_dir(path: Path) -> Path:
    Path(path).mkdir(parents=True, exist_ok=True)
    return Path(path)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def inside_book(path: Path) -> bool:
    """True when the path is inside the real book folder (a sandbox --book-dir must live there too)."""
    try:
        Path(path).resolve().relative_to(REAL_BOOK.resolve())
        return True
    except ValueError:
        return False


def rel(path: Path) -> str:
    """Repo-relative display form of a path."""
    try:
        return str(Path(path).resolve().relative_to(REPO.resolve()))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------- JSON / JSONL with locking

@contextlib.contextmanager
def file_lock(path: Path, timeout: float = 120.0):
    """Exclusive advisory lock on <path>.lock. Use around every read-modify-write of a shared file."""
    lock_path = Path(str(path) + ".lock")
    ensure_dir(lock_path.parent)
    start = time.time()
    with open(lock_path, "w") as lock_file:
        while True:
            try:
                fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.time() - start > timeout:
                    raise TimeoutError(f"could not lock {path} within {timeout}s")
                time.sleep(0.05)
        try:
            yield
        finally:
            fcntl.flock(lock_file, fcntl.LOCK_UN)


def read_json(path: Path, default=None):
    path = Path(path)
    if not path.exists():
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, obj) -> None:
    """Atomic write (temp file then rename)."""
    path = Path(path)
    ensure_dir(path.parent)
    tmp = path.with_name(path.name + f".tmp{os.getpid()}")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, path)


def read_jsonl(path: Path) -> list:
    path = Path(path)
    if not path.exists():
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    tmp = path.with_name(path.name + f".tmp{os.getpid()}")
    with open(tmp, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def append_jsonl(path: Path, row) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    with file_lock(path):
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- the one text normaliser

_QUOTES = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "―": "-", "−": "-",
    " ": " ", " ": " ", " ": " ", " ": " ", "​": "", "﻿": "",
    "…": "...",
}
_QUOTE_TABLE = str.maketrans(_QUOTES)
_RE_TAG = re.compile(r"<[^>\n]{0,400}>")
_RE_IMG = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_RE_LINK = re.compile(r"\[([^\]]+)\]\((?:[^()\s]|\([^()]*\))*(?:\s+\"[^\"]*\")?\)")
_RE_REFLINK = re.compile(r"\[([^\]]+)\]\[[^\]]*\]")
_RE_LINE_PREFIX = re.compile(r"(?m)^\s{0,8}(?:#{1,6}\s+|[+\-*]\s+|\d{1,3}[.)]\s+|>\s?)+")
_RE_TABLE_RULE = re.compile(r"(?m)^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
_RE_ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>~])")
_RE_WS = re.compile(r"\s+")


def normalize_text(text: str) -> str:
    """Canonical form used on BOTH sides of every quote check.

    HTML entities decoded, NFKC, typographic quotes and dashes unified, HTML tags and anchors
    dropped, Markdown links reduced to their text, list / heading / blockquote prefixes and
    table pipes removed, emphasis markers and backticks removed, whitespace collapsed, lowercased.
    """
    if not text:
        return ""
    t = html.unescape(text)
    t = unicodedata.normalize("NFKC", t).translate(_QUOTE_TABLE)
    t = _RE_TAG.sub(" ", t)
    t = _RE_IMG.sub(r"\1", t)
    for _ in range(3):  # nested or adjacent links
        t = _RE_LINK.sub(r"\1", t)
    t = _RE_REFLINK.sub(r"\1", t)
    t = _RE_TABLE_RULE.sub(" ", t)
    t = _RE_LINE_PREFIX.sub("", t)
    t = _RE_ESCAPE.sub(r"\1", t)
    t = t.replace("|", " ").replace("`", "").replace("*", "")
    t = _RE_WS.sub(" ", t).strip().lower()
    return t


def find_quote(quote: str, page_text: str, already_normalized: bool = False):
    """Return (start, end) of the normalised quote inside the normalised page text, or None."""
    q = normalize_text(quote)
    p = page_text if already_normalized else normalize_text(page_text)
    if not q:
        return None
    i = p.find(q)
    return (i, i + len(q)) if i >= 0 else None


# ---------------------------------------------------------------- output helpers

def add_common_args(parser) -> None:
    parser.add_argument("--out", help="write the result to this file instead of stdout (path inside aws-saa-book/)")
    parser.add_argument("--max-lines", type=int, default=0, help="print at most N lines (0 = no limit)")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")


def emit(result, args=None) -> None:
    """Print text or JSON, honouring --out and --max-lines."""
    text = result if isinstance(result, str) else json.dumps(result, ensure_ascii=False, indent=1)
    out = getattr(args, "out", None) if args is not None else None
    max_lines = getattr(args, "max_lines", 0) if args is not None else 0
    if out:
        out_path = Path(out)
        if not out_path.is_absolute():
            out_path = REPO / out_path
        if not inside_book(out_path):
            print(f"refused: --out must be inside {BOOK}", file=sys.stderr)
            raise SystemExit(EXIT_POLICY)
        ensure_dir(out_path.parent)
        out_path.write_text(text + ("" if text.endswith("\n") else "\n"), encoding="utf-8")
        print(f"wrote {rel(out_path)} ({len(text.splitlines())} lines)")
        return
    lines = text.splitlines()
    if max_lines and len(lines) > max_lines:
        print("\n".join(lines[:max_lines]))
        print(f"... ({len(lines) - max_lines} more lines; use --out FILE to save everything)")
    else:
        print(text)


def fail(message: str, code: int = EXIT_FAIL) -> int:
    print(f"error: {message}", file=sys.stderr)
    return code


# ---------------------------------------------------------------- book registry access

def load_book() -> dict:
    """The chapter registry: data/book.json once built, else the seed."""
    book = read_json(DATA / "book.json")
    if book is None:
        book = read_json(REGISTRY / "book.seed.json")
    if book is None:
        raise SystemExit(fail("no book registry found", EXIT_PRECONDITION))
    return book


def chapters() -> list:
    return load_book()["chapters"]


def chapter(ch_id: str) -> dict:
    ch_id = str(ch_id)
    for ch in chapters():
        if ch["id"] == ch_id or ch["slug"] == ch_id or f"{ch['id']}-{ch['slug']}" == ch_id:
            return ch
    raise SystemExit(fail(f"unknown chapter {ch_id!r}", EXIT_PRECONDITION))


def chapter_dir(ch_id: str) -> Path:
    ch = chapter(ch_id)
    return BOOK / f"{ch['id']}-{ch['slug']}"


def chapter_data_dir(ch_id: str) -> Path:
    ch = chapter(ch_id)
    return DATA / f"{ch['id']}-{ch['slug']}"
