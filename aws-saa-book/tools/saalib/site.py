"""The web version: `build web`, `web lint`, `web selftest`, `web shots`.

Contract: tools/web/ARCHITECTURE.md section 2 (build), 9.2, 9.3, 9.5 (the three `web` commands live in
saalib/_site_web.py). Standard library only; Markdown is rendered by tools/helpers/site_md.py under uv.

Every path is read through `common.X` at call time. Nothing is written outside `common.BUILD`
(or the folder given with --out, which must be inside the book). The output is deterministic.
"""
from __future__ import annotations

import base64
import copy
import html
import json
import re
import shutil
import subprocess
from pathlib import Path

from saalib import common

TITLE = "SAA-C03 Handbook"
ICON = "book"
MARKER = ".saa-site"
FONTS_URL = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..800"
             "&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap")
PART_OF_FILE = {"1-fast.md": "fast", "2-deep.md": "deep", "2-services.md": "services", "calendar.md": "calendar",
                "mistakes.md": "mistakes", "exam-english.md": "words", "sheet.md": "sheet"}
GENERATED_PARTS = {"3-do.md": "do", "4-say.md": "say", "5-quiz.md": "quiz", "sources.md": "sources"}
PART_TITLES = {"fast": "Fast", "deep": "In depth", "services": "Services", "calendar": "Calendar",
               "mistakes": "Mistakes log", "words": "Exam English", "sheet": "Sheet", "do": "Do", "say": "Say it",
               "quiz": "Quiz", "sources": "Sources"}
JS_FILES = ["util.js", "content.js", "router.js", "merge.js", "store.js", "scoring.js", "popover.js", "evidence.js",
            "glossary.js", "reader.js", "qview.js", "quiz.js", "exam.js", "mistakes.js", "cards.js", "today.js",
            "plan.js", "dash.js", "files.js", "aicore.js", "ai.js", "speak.js", "ask.js", "search.js", "selftest.js",
            "boot.js"]
CSS_FILES = ["10-base.css", "20-layout.css", "30-prose.css", "40-components.css", "50-practice.css", "60-today.css",
             "70-ai.css", "90-phone.css"]
DEFAULT_CFG = {"examFacts": {"count": "exam-question-count", "minutes": "exam-duration-minutes", "pass": "exam-passing-score",
                             "esl": "exam-esl-accommodation"},
               "extraMinutes": 30, "previewMockMinutes": 130, "stemFirstCount": 100, "speakSeconds": 90,
               "wordsPerMinute": 130, "gate": {"strong": 80, "soft": 75, "domainMin": 65, "needed": 2},
               "minimums": [{"id": "pages", "label": "Read 10 pages"}, {"id": "words", "label": "Learn 5 words"},
                            {"id": "speak", "label": "One spoken rehearsal"}]}
CAPABILITIES = {"db": {"rules": [{"path": "", "read": "owner", "write": "owner"},
                                 {"path": "study", "read": "owner", "write": "owner"},
                                 {"path": "study/{self}", "read": "interact", "write": "interact"}]},
                "user": {}, "sample": {}, "downloads": True}
KB = 1000
MB = 1000 * 1000
# The facts of the book, one shard per fact namespace (data/facts/<service>.jsonl), section 2.4.
FACTS_INDEX = "facts-index.json"
SHARD_DIR = "f"
SHARD_WARN = 400 * KB        # the per-file warning level of the content files
SHARD_CAP = 1500 * KB        # the largest shard (s3, 597 facts) was 600 KB on 2026-10-12: room for about 1,490 facts
RE_SHARD = re.compile(r"^[a-z0-9][a-z0-9-]*$")
# Full-text search, one shard per chapter (search/<slug>.json) and search/index.json, section 2.4.
SEARCH_DIR = "search"
SEARCH_INDEX = "search/index.json"
SEARCH_BOOK = "book"          # the shard of the docs of no chapter: glossary terms, facts of a namespace no chapter lists
# files of an earlier layout: listed in publish-plan.json `removed` so a republish deletes them
RETIRED_PATHS = ("facts.json", "search/corpus.json")
BATCH_FILES = 255             # files in one publish call (platform limit)
BATCH_WARN_FILES = 230        # warning level: each fact namespace and each chapter adds a shard to the content batch (1.2)
# path pattern -> (warn, fail) in bytes; None = no warn level
BUDGETS = [(r"^index\.html$", 500 * KB, 700 * KB),(r"^manifest\.json$", 300 * KB, 500 * KB),
           (r"^qindex\.json$", 200 * KB, 300 * KB), (r"^c/", 400 * KB, 600 * KB), (r"^d/", None, 600 * KB),
           (r"^q/", None, 400 * KB), (r"^glossary\.json$", None, 300 * KB), (r"^plan\.json$", None, 60 * KB),
           (r"^facts-index\.json$", None, 60 * KB), (r"^f/", SHARD_WARN, SHARD_CAP),
           (r"^search/index\.json$", None, 200 * KB), (r"^search/", 400 * KB, 800 * KB),
           (r"^assets/icons\.svg$", None, 400 * KB), (r"^assets/search-worker\.js$", None, 60 * KB),
           (r"^exports/", None, 15 * MB)]
SINGLE_BUDGET = 15 * MB
EXPORT_TYPES = (".pdf", ".txt", ".zip")
OPT_WORDS = [("cost", ("cost", "cheap", "price")),
             ("ops", ("operational", "overhead", "effort", "management", "administrative")),
             ("perf", ("performance", "latency", "fast", "throughput", "scal", "speed", "quick")),
             ("resil", ("available", "availability", "resilient", "fault", "durable", "recovery", "downtime", "reliab",
                        "outage", "failure")),
             ("sec", ("secure", "security"))]
CARD_TYPES = ("decide", "differ", "number", "cannot", "word", "say")
QUALIFIED_KINDS = ("limit", "quota", "default")
ALIAS_CHAPTERS = {"numbers": "47", "traps": "46", "changed": "48"}
RE_EMBED = re.compile(r"!\[([^\]]*)\]\(\.\./diagrams/svg/([a-z0-9-]+)\.svg\)")
RE_FACT_LINK = re.compile(r"\]\(\.\./facts/[a-z0-9-]+\.md#([a-z0-9-]+)\)")
RE_DATA_FACT = re.compile(r'data-fact="([^"]+)"')
RE_COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|\brgba?\(|\bhsla?\(")
RE_VAR = re.compile(r"var\(\s*--([A-Za-z0-9-]+)")
FALLBACK_SHELL = """<title>SAA-C03 Handbook</title>
{{fonts}}
<style>{{css}}</style>
<div id="saa" class="app ts-1" lang="en">
  <a class="skip" href="#saa-main">Skip to content</a>
  <header id="saa-top" class="top">
    <button type="button" id="saa-menu" class="top-menu" data-act="toc" aria-controls="saa-toc" aria-expanded="false">Contents</button>
    <a class="brand" href="#home" aria-label="SAA-C03 Handbook"><span class="brand-s">SAA-C03</span><span class="brand-l"> Handbook</span></a>
    <nav id="saa-nav" class="nav" aria-label="Main"><a href="#home">Today</a> <a href="#plan">Plan</a> <a href="#mistakes">Practice</a> <a href="#speak">Speak</a> <a href="#progress">Progress</a></nav>
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
{{boot}}
{{inline}}
<script>{{js}}</script>
"""
FALLBACK_SKELETON = """<!doctype html>
<html lang="en"{{theme}}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;background:#FAFAF8}
img{max-width:100%}
[hidden]{display:none!important}
</style>
</head>
<body>
{{stub}}
{{page}}
</body>
</html>
"""


# ---------------------------------------------------------------- small helpers

def group(subparsers, name, help_text):
    parser = subparsers.choices.get(name) if getattr(subparsers, "choices", None) else None
    if parser is None:
        parser = subparsers.add_parser(name, help=help_text)
        parser._saa_actions = parser.add_subparsers(dest=name + "_cmd")
    return parser._saa_actions


def anchor(heading: str) -> str:
    """The Markdown (GitHub) anchor of a full heading text (SPEC.json headings.markdown_anchor)."""
    return "".join(c for c in heading.strip().lower() if c.isalnum() or c in " -").replace(" ", "-")


def section_id(heading: str) -> str:
    """The stable section id: the anchor of the heading without its time box (SPEC.json headings.section_id)."""
    return anchor(re.sub(r" \(([0-9]{1,3}) min\)$", "", heading.strip()))


def dumps(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


def script_json(obj) -> str:
    """JSON that is safe inside a <script> element (section 2.5)."""
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return text.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def finding(code, msg, file=None, line=0, item=None) -> dict:
    return {"code": code, "file": file, "line": line, "item": item, "msg": msg}


def _scalar(text: str):
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        return text[1:-1]
    if text in ("true", "false"):
        return text == "true"
    if re.fullmatch(r"-?[0-9]+", text):
        return int(text)
    return text


def _split_flow(text: str) -> list:
    parts, cur, quote = [], "", None
    for ch in text:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            cur += ch
        elif ch == ",":
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return parts


def front_matter(text: str) -> dict:
    """The restricted YAML block of CONVENTIONS.md section B."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    out = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, sep, value = line.partition(":")
        if not sep:
            continue
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            out[key.strip()] = [_scalar(p) for p in _split_flow(value[1:-1])]
        elif value.startswith("{") and value.endswith("}"):
            out[key.strip()] = {k.strip(): _scalar(v) for k, _, v in (p.partition(":") for p in _split_flow(value[1:-1]))}
        else:
            out[key.strip()] = _scalar(value)
    return out


def scan_sections(text: str) -> dict:
    """{markdown anchor: section id} of every H2 and H3 of one Markdown file."""
    out, fence = {}, False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        m = None if fence else re.match(r"^(#{2,3})\s+(.*?)\s*$", line)
        if m:
            out.setdefault(anchor(m.group(2)), section_id(m.group(2)))
    return out


def scope_line(fact: dict) -> str:
    """The Scope line of TOOLS.md 5.8."""
    q = fact.get("qualifiers") or {}
    parts = [str(q.get("scope") or "").strip(),
             {"default": "default", "max": "maximum", "min": "minimum", "fixed": "fixed"}.get(q.get("default_or_max"), "")]
    if fact.get("kind") in QUALIFIED_KINDS:
        parts.append("adjustable" if q.get("adjustable") else "not adjustable")
    parts.append(str(q.get("condition") or "").strip())
    parts = [p for p in parts if p]
    return "; ".join(parts) + "." if parts else ""


def fact_card(fact: dict) -> dict:
    changed = fact.get("changed")
    return {"service": fact.get("service"), "claim": fact.get("claim", ""),
            "values": [v.get("display") for v in fact.get("values", []) if v.get("display")],
            "scope": scope_line(fact),
            "quotes": [{"q": ev.get("quote", ""), "title": ev.get("title"), "url": ev.get("url"),
                        "header": ev.get("table_header")} for ev in fact.get("evidence", [])],
            "checked": fact.get("retrieved"),
            "changed": {"date": changed.get("date"), "was": changed.get("was")} if changed else None,
            "kind": fact.get("kind")}


def fact_shard(fact_id: str, services) -> str | None:
    """The shard the app reads first for a fact id: the longest service key k with the id starting "k-" (section 3.2).

    A fact whose shard is not this one is listed in `stray` of facts-index.json."""
    best = None
    for key in services:
        if fact_id.startswith(key + "-") and (best is None or len(key) > len(best)):
            best = key
    return best


def derive_opt(qualifier):
    if qualifier in (None, "", "none"):
        return "none"
    low = str(qualifier).lower()
    for key, words in OPT_WORDS:
        if any(w in low for w in words):
            return key
    return None


# ---------------------------------------------------------------- smaller sources (comments and indentation only)

_REGEX_AFTER = set("(,=:[!&|?{};+-*%<>~^")
_REGEX_WORDS = {"return", "typeof", "instanceof", "in", "of", "new", "delete", "void", "throw", "case", "do", "else",
                "yield", "await"}


def minify_js(src: str) -> str:
    """Drop comments, indentation and blank lines of a plain script. Nothing is renamed or joined.

    Strings, template literals and regular expressions are copied as they are; every line break
    that separates two statements stays. On anything unexpected the source is returned unchanged."""
    out = []
    i, n = 0, len(src)
    stack = [["code", 0]]           # frames: ["code", open braces] or ["tpl"]

    def tail() -> str:
        return "".join(out[-40:])

    def last_sig() -> str:
        for piece in reversed(out):
            stripped = piece.rstrip()
            if stripped:
                return stripped[-1]
        return ""

    def newline():
        while out and out[-1] in (" ", "\t"):
            out.pop()
        if out and out[-1] != "\n":
            out.append("\n")

    while i < n:
        c = src[i]
        if stack[-1][0] == "tpl":
            if c == "\\" and i + 1 < n:
                out.append(src[i:i + 2])
                i += 2
            elif c == "`":
                out.append(c)
                stack.pop()
                i += 1
            elif c == "$" and i + 1 < n and src[i + 1] == "{":
                out.append("${")
                stack.append(["code", 0])
                i += 2
            else:
                out.append(c)
                i += 1
            continue
        if c == "\n" or c == "\r":
            newline()
            i += 1
        elif c in " \t":
            if out and out[-1] not in ("\n", " "):
                out.append(" ")
            i += 1
        elif c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            i = n if j < 0 else j
        elif c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            if j < 0:
                return src
            if "\n" in src[i:j]:
                newline()
            elif out and out[-1] not in ("\n", " "):
                out.append(" ")
            i = j + 2
        elif c in "\"'":
            j = i + 1
            while j < n and src[j] != c:
                if src[j] == "\n":
                    return src
                j += 2 if src[j] == "\\" else 1
            if j >= n:
                return src
            out.append(src[i:j + 1])
            i = j + 1
        elif c == "`":
            out.append(c)
            stack.append(["tpl"])
            i += 1
        elif c == "/":
            prev = last_sig()
            word = re.search(r"([A-Za-z_$][\w$]*)\s*$", tail())
            is_regex = prev == "" or prev in _REGEX_AFTER or prev == "}" or (word is not None and word.group(1) in _REGEX_WORDS)
            end = None
            if is_regex:
                j, in_class = i + 1, False
                while j < n and src[j] != "\n":
                    ch = src[j]
                    if ch == "\\":
                        j += 2
                        continue
                    if ch == "[":
                        in_class = True
                    elif ch == "]":
                        in_class = False
                    elif ch == "/" and not in_class:
                        end = j
                        break
                    j += 1
            if end is None:
                out.append(c)
                i += 1
            else:
                j = end + 1
                while j < n and src[j].isalpha():
                    j += 1
                out.append(src[i:j])
                i = j
        else:
            if c == "{":
                stack[-1][1] += 1
            elif c == "}":
                if stack[-1][1] == 0 and len(stack) > 1:
                    stack.pop()
                    out.append(c)
                    i += 1
                    continue
                stack[-1][1] -= 1
            out.append(c)
            i += 1
    if len(stack) != 1:
        return src
    return "".join(out).strip("\n") + "\n"


def minify_css(src: str) -> str:
    """Drop comments, indentation and blank lines of a stylesheet. Strings are copied as they are."""
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if c == "/" and src.startswith("/*", i):
            j = src.find("*/", i + 2)
            if j < 0:
                return src
            i = j + 2
        elif c in "\"'":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            out.append(src[i:j + 1])
            i = j + 1
        else:
            out.append(c)
            i += 1
    lines = [ln.strip() for ln in "".join(out).split("\n")]
    return "\n".join(ln for ln in lines if ln) + "\n"


# ---------------------------------------------------------------- tokens

def _rgb(value: str):
    value = value.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", value)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) in (6, 8):
            return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        return None
    m = re.fullmatch(r"rgba?\(\s*([0-9.]+)[ ,]+([0-9.]+)[ ,]+([0-9.]+).*\)", value)
    if m:
        return tuple(float(m.group(i)) for i in (1, 2, 3))
    return None


def contrast(a, b) -> float:
    def lum(rgb):
        vals = []
        for c in rgb:
            c = c / 255
            vals.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
        return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def token_css(tokens: dict):
    """(css text, findings) from tokens.json (sections 2.5 and 4.1)."""
    findings = []
    themed = tokens.get("themed") or {}
    alias = tokens.get("alias") or {}
    static = tokens.get("static") or {}
    light, dark = [], []
    for name, value in themed.items():
        if not isinstance(value, dict) or "light" not in value or "dark" not in value:
            findings.append(finding("WB06", f"token {name} lacks a light or a dark value", "tools/web/tokens.json", item=name))
            continue
        light.append(f"--{name}:{value['light']}")
        dark.append(f"--{name}:{value['dark']}")
    rest = []
    for kind, table in (("alias", alias), ("static", static)):
        for name, value in table.items():
            if RE_COLOR.search(str(value)):
                findings.append(finding("WB06", f"{kind} token {name} holds a literal colour", "tools/web/tokens.json", item=name))
            rest.append(f"--{name}:{value}")

    def resolve(name, mode, depth=0):
        if name in themed and isinstance(themed[name], dict):
            return themed[name].get(mode)
        if name in alias and depth < 8:
            m = RE_VAR.search(str(alias[name]))
            return resolve(m.group(1), mode, depth + 1) if m else None
        return None

    for pair in tokens.get("pairs") or []:
        if not isinstance(pair, list) or len(pair) < 3:
            continue
        for mode in ("light", "dark"):
            a, b = resolve(pair[0], mode), resolve(pair[1], mode)
            ca, cb = (_rgb(a) if a else None), (_rgb(b) if b else None)
            if ca is None or cb is None:
                findings.append(finding("WB06", f"contrast pair {pair[0]} / {pair[1]} ({mode}) names a token without a colour value",
                                        "tools/web/tokens.json", item=pair[0]))
                continue
            ratio = contrast(ca, cb)
            if ratio + 1e-9 < float(pair[2]):
                findings.append(finding("WB06", f"contrast of {pair[0]} on {pair[1]} ({mode}) is {ratio:.2f}, below {pair[2]}",
                                        "tools/web/tokens.json", item=pair[0]))
    dark_block = ";".join(dark + ["color-scheme:dark"])
    css = (":root{" + ";".join(light + rest) + "}\n"
           "@media (prefers-color-scheme: dark){:root:not([data-theme=\"light\"]){" + dark_block + "}}\n"
           ":root[data-theme=\"dark\"]{" + dark_block + "}\n")
    return css, findings


def undefined_vars(tokens: dict, texts: dict) -> list:
    defined = set(tokens.get("themed") or {}) | set(tokens.get("alias") or {}) | set(tokens.get("static") or {})
    defined |= set(tokens.get("runtime") or [])
    out = []
    texts = dict(texts)
    texts["tools/web/tokens.json"] = " ".join(str(v) for v in (tokens.get("alias") or {}).values())
    for name, text in texts.items():
        for var in sorted(set(RE_VAR.findall(text))):
            if var not in defined:
                out.append(finding("WB06", f"var(--{var}) is not defined in tokens.json", name, item=var))
    return out


# ---------------------------------------------------------------- the build

class Stop(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


class Build:
    def __init__(self, only_ready=False, single=False, preview=False, out=None, minify=True):
        self.only_ready, self.single, self.preview, self.minify = only_ready, single, preview, minify
        name = ("preview" if preview else "site") + ("-single" if single else "")
        self.out = Path(out) if out else common.BUILD / name
        self.errors, self.warnings = [], []
        self.files = {}          # published path -> bytes (the multi-file layout)
        self.web = common.WEB_SRC

    # ---- findings

    def err(self, code, msg, file=None, line=0, item=None):
        self.errors.append(finding(code, msg, file, line, item))

    def warn(self, code, msg, file=None, line=0, item=None):
        self.warnings.append(finding(code, msg, file, line, item))

    def source(self, rel_path: str):
        """Text of a file of tools/web, or None with a WB02 finding (warning in a preview build)."""
        path = self.web / rel_path
        if path.is_file():
            return path.read_text(encoding="utf-8")
        (self.warn if self.preview else self.err)("WB02", f"source file tools/web/{rel_path} does not exist", f"tools/web/{rel_path}")
        return None

    # ---- step 1: load

    def load(self):
        self.book = common.load_book()
        self.meta = self.book.get("book") or {}
        self.fixture = bool(self.meta.get("fixture"))
        self.chapters = self.book.get("chapters") or []
        self.spec = common.read_json(common.STYLE_DIR / "SPEC.json") or \
            common.read_json(common.REAL_BOOK / "_build" / "style" / "SPEC.json") or {}
        self.terms = (common.read_json(common.DATA / "terms.json") or {}).get("terms", [])
        overlay = common.WEB_SRC / "tests" / "fixtures"
        self.plan = common.read_json(common.DATA / "plan.json")
        self.plan_file = "data/plan.json"
        if self.plan is None and self.fixture:
            self.plan, self.plan_file = common.read_json(overlay / "plan.json"), "tools/web/tests/fixtures/plan.json"
        self.drills = common.read_json(common.DATA / "drills.json")
        self.drills_file = "data/drills.json"
        if self.drills is None and self.fixture:
            self.drills, self.drills_file = common.read_json(overlay / "drills.json"), "tools/web/tests/fixtures/drills.json"
        self.guide = common.read_json(common.REGISTRY / "exam-guide.json") or {}
        self.all_facts, self.facts, self.fact_ns = {}, {}, {}
        if common.FACTS_DIR.is_dir():
            for path in sorted(common.FACTS_DIR.glob("*.jsonl")):
                for row in common.read_jsonl(path):
                    if row.get("id"):
                        self.all_facts[row["id"]] = row
                        if row.get("status") == "verified":
                            self.facts[row["id"]] = row
                            self.fact_ns[row["id"]] = path.stem      # the fact namespace names the shard
        cfg = None
        if (self.web / "shell.json").is_file():
            cfg = common.read_json(self.web / "shell.json")
        else:
            (self.warn if self.preview else self.err)("WB02", "source file tools/web/shell.json does not exist; built-in defaults are used",
                                                       "tools/web/shell.json")
        self.cfg = cfg if isinstance(cfg, dict) else copy.deepcopy(DEFAULT_CFG)
        self.by_id = {ch["id"]: ch for ch in self.chapters}
        self.dirs = {f"{ch['id']}-{ch['slug']}": ch["slug"] for ch in self.chapters}

    def dirname(self, ch) -> str:
        return f"{ch['id']}-{ch['slug']}"

    def items(self, ch, kind) -> list:
        doc = common.read_json(common.DATA / self.dirname(ch) / f"{kind}.json") or {}
        return [i for i in doc.get("items", []) if isinstance(i, dict)]

    def template(self, ch) -> dict:
        over = (self.spec.get("chapter_overrides") or {}).get(ch["id"]) or {}
        key = over.get("template") or ch.get("kind") or ch.get("tier")
        base = (self.spec.get("templates") or {}).get(key) or {}
        return {"key": key, "files": over.get("files") or base.get("files") or [],
                "minutes": {**(base.get("minutes") or {}), **(over.get("minutes") or {})}}

    # ---- step 2: status

    def status(self, ch) -> str:
        ledger = common.read_json(common.LEDGER / "chapters" / f"{ch['id']}.json") or {}
        if ledger.get("status") == "ready":
            return "ready"
        if (common.BOOK / self.dirname(ch) / "1-fast.md").is_file():
            return "planned" if self.only_ready else "draft"
        return "planned"

    def rev(self, ch) -> int:
        ledger = common.read_json(common.LEDGER / "chapters" / f"{ch['id']}.json") or {}
        return int(ledger.get("rev") or 0)

    # ---- step 3: validate

    def validate(self):
        try:
            from saalib import schemas
        except Exception as exc:       # the validator is another owner's module
            self.warn("WB07", f"schemas could not be loaded: {exc!r}")
            return

        def check(obj, name, file):
            if obj is None:
                return
            try:
                errors = schemas.validate(obj, name)
            except FileNotFoundError:
                return
            for e in errors[:5]:
                self.err("WB07", e, file)
            if len(errors) > 5:
                self.err("WB07", f"{len(errors) - 5} more schema errors", file)

        for ch in self.built:
            for kind, name in (("questions", "question"), ("cards", "card"), ("speak", "speak"), ("tasks", "task"), ("mock", "mock")):
                path = common.DATA / self.dirname(ch) / f"{kind}.json"
                if path.is_file():
                    check(common.read_json(path), name, f"data/{self.dirname(ch)}/{kind}.json")
        check(self.plan, "plan", self.plan_file)
        check(self.drills, "drills", self.drills_file)
        if (common.DATA / "terms.json").is_file():
            check(common.read_json(common.DATA / "terms.json"), "terms", "data/terms.json")

    # ---- chapters, parts, items

    def emit_ok(self, item, kind, draft) -> bool:
        allowed = ("verified", "ready") if (draft and self.preview) else ("ready",)
        if item.get("status") not in allowed:
            return False
        if kind == "questions":
            return (item.get("verification") or {}).get("status") in ("pass", "edited-pass")
        return True

    def prepare_chapters(self):
        self.state = {ch["slug"]: self.status(ch) for ch in self.chapters}
        self.built = [ch for ch in self.chapters if self.state[ch["slug"]] != "planned"]
        self.info = {}
        self.secidx = {}            # slug -> file -> {anchor: sid}
        for ch in self.built:
            folder = common.BOOK / self.dirname(ch)
            info = {"folder": folder, "md": [], "fm": {}, "texts": {}, "updated": []}
            for name, key in PART_OF_FILE.items():
                path = folder / name
                if path.is_file():
                    text = path.read_text(encoding="utf-8")
                    info["md"].append((key, name, path))
                    info["texts"][name] = text
                    fm = front_matter(text)
                    if name == "1-fast.md":
                        info["fm"] = fm
                    if fm.get("updated"):
                        info["updated"].append(str(fm["updated"]))
            self.secidx[ch["slug"]] = {name: scan_sections(text) for name, text in info["texts"].items()}
            draft = self.state[ch["slug"]] == "draft"
            info["items"] = {kind: [i for i in self.items(ch, kind) if self.emit_ok(i, kind, draft)]
                             for kind in ("questions", "cards", "speak", "tasks")}
            info["items"]["cards"] = [c for c in info["items"]["cards"] if c.get("type") in CARD_TYPES]
            self.info[ch["slug"]] = info

    def resolve_sec(self, section, home_slug):
        if not section or "#" not in section:
            return None
        target, _, sid = section.partition("#")
        slug = home_slug
        if "/" in target:
            folder, _, target = target.partition("/")
            slug = self.dirs.get(folder)
        part = PART_OF_FILE.get(target)
        if slug is None or part is None:
            return None
        if sid not in (self.secidx.get(slug, {}).get(target) or {}).values():
            return None
        return {"slug": slug, "part": part, "sid": sid}

    # ---- step 4: diagrams

    def diagrams(self):
        self.diagram_ctx, self.figure_info, self.icons_used = {}, {}, set()
        embeds = {}
        for slug, info in self.info.items():
            for name, text in info["texts"].items():
                for alt, ident in RE_EMBED.findall(text):
                    embeds.setdefault(ident, (alt, f"{info['folder'].name}/{name}"))
        pipeline = svg = icons_mod = None
        icons = {}
        try:
            from saalib.diagram import icons as icons_mod, pipeline, svg
            icons = icons_mod.load()
        except Exception as exc:
            if embeds:
                self.warn("WB04", f"the diagram modules could not be loaded ({exc!r}); every figure is embedded as an image")
        self.icons, self.icons_mod = icons, icons_mod
        for ident in sorted(embeds):
            alt, where = embeds[ident]
            entry = None
            if pipeline is not None and pipeline.spec_path(ident).is_file():
                try:
                    res = pipeline.check_id(ident)
                    if res.get("scene") is not None and not any(i.get("level") == "error" for i in res.get("issues", [])):
                        scene, spec = res["scene"], res["spec"]
                        cap = pipeline.caption(spec)
                        width = scene.get("phone_w") or scene.get("w") or 0
                        entry = {"html": svg.render_inline(scene, spec, icons), "kind": spec.get("kind", "arch"),
                                 "title": cap.get("title", ""), "claim": cap.get("claim", ""),
                                 "steps": [s[1] for s in cap.get("steps", [])]}
                        self.figure_info[ident] = {"title": cap.get("title", ""), "w": width}
                        self.icons_used.update(svg.used_icons(scene))
                    else:
                        self.warn("WB04", f"diagram {ident}: the spec has errors; the standalone SVG is embedded as an image", where, item=ident)
                except Exception as exc:
                    self.warn("WB04", f"diagram {ident}: the renderer failed ({exc!r}); the standalone SVG is embedded as an image", where, item=ident)
            if entry is None:
                path = common.DIAGRAM_SVG / f"{ident}.svg"
                if path.is_file():
                    data = path.read_bytes()
                    m = re.search(rb'<svg\b[^>]*?\bwidth="([0-9.]+)', data)
                    width = int(float(m.group(1))) if m else 0
                    src = "data:image/svg+xml;base64," + base64.b64encode(data).decode("ascii")
                    entry = {"html": f'<img class="fig-img" alt="{html.escape(alt, quote=True)}" style="--dg-w:{width}" src="{src}">',
                             "kind": "image", "title": "", "claim": "", "steps": []}
                    self.figure_info[ident] = {"title": "", "w": width}
                    if pipeline is None or not pipeline.spec_path(ident).is_file():
                        self.warn("WB04", f"diagram {ident} has no spec; the standalone SVG is embedded as an image", where, item=ident)
                else:
                    self.figure_info[ident] = {"title": "", "w": 0}
                    continue        # the helper reports the missing drawing
            self.diagram_ctx[ident] = entry

    # ---- step 5: render

    def render(self):
        inline = {}
        for slug, info in self.info.items():
            for q in info["items"]["questions"]:
                inline[f"q:{q['id']}:expl"] = q.get("explanation") or ""
                inline[f"q:{q['id']}:take"] = q.get("takeaway") or ""
                inline[f"q:{q['id']}:twin"] = q.get("twin") or ""
                for o in q.get("options", []):
                    inline[f"q:{q['id']}:why:{o.get('id')}"] = o.get("why") or ""
            for c in info["items"]["cards"]:
                inline[f"c:{c['id']}:extra"] = c.get("extra") or ""
            for t in info["items"]["tasks"]:
                for n, step in enumerate(t.get("steps", []), 1):
                    if step.get("explain"):
                        inline[f"t:{t['id']}:explain:{n}"] = step["explain"]
        self.inline_src = inline
        chapters = []
        for ch in self.built:
            info = self.info[ch["slug"]]
            has_quiz = any(q.get("pool") == "chapter" for q in info["items"]["questions"]) or ch.get("tier") == "mock"
            chapters.append({"slug": ch["slug"], "id": ch["id"], "dir": self.dirname(ch), "quiz": has_quiz,
                             "parts": [{"key": key, "path": str(path), "file": name} for key, name, path in info["md"]]})
        callouts = (self.spec.get("callouts") or {}).get("labels") or []
        prompts = list(((self.spec.get("prompts") or {}).get("labels") or {}).keys())
        bold = {k: v for k, v in (self.spec.get("bold_fields") or {}).items() if isinstance(v, list)}
        terms = []
        for t in self.terms:
            forms = [t.get("term")] + ([t["short"]] if t.get("short") else []) + list(t.get("aliases") or [])
            terms.append({"id": t["id"], "cs": t.get("kind") == "aws-name", "forms": [f for f in forms if f]})
        hosts = (self.spec.get("lint") or {}).get("external_link_hosts") or list(common.ALLOWED_HOSTS[:4])
        job = {"chapters": chapters, "inline": inline,
               "ctx": {"facts": {fid: {"service": f.get("service"),
                                       "displays": [v.get("display") for v in f.get("values", []) if v.get("display")]}
                                 for fid, f in self.facts.items()},
                       "unverified": sorted(set(self.all_facts) - set(self.facts)),
                       "terms": terms, "chapters": self.dirs, "part_of_file": PART_OF_FILE, "sections": self.secidx,
                       "diagrams": self.diagram_ctx, "callouts": callouts, "prompts": prompts, "bold_fields": bold,
                       "table_kinds": list(((self.spec.get("tables") or {}).get("kinds") or {}).keys()), "hosts": hosts}}
        self.rendered = run_helper(job)
        for key, part in self.rendered["parts"].items():
            slug, _, part_key = key.partition("/")
            file = next((f"{self.info[slug]['folder'].name}/{name}" for k, name, _ in self.info[slug]["md"] if k == part_key), key)
            for w in part.get("warnings", []):
                if w["code"] == "WB04":
                    if not any(x["code"] == "WB04" and x["file"] == file and x["msg"] == w["msg"] for x in self.warnings):
                        self.warn("WB04", w["msg"], file, w.get("line", 0))
                elif w.get("level") == "error" and w["code"] == "WB03":
                    self.err("WB03", w["msg"], file, w.get("line", 0))
                else:
                    self.warn(w["code"], w["msg"], file, w.get("line", 0))
        for w in self.rendered.get("inline_warnings", []):
            (self.err if w.get("level") == "error" and w["code"] == "WB03" else self.warn)(w["code"], w["msg"], item=w.get("key"))

    def h(self, key) -> str:
        return self.rendered["inline"].get(key, "")

    # ---- step 6: data

    def question(self, q, slug) -> dict:
        qid = q["id"]
        worked = q.get("worked")
        qual = q.get("qualifier")
        return {"id": qid, "ch": slug, "sec": self.resolve_sec(q.get("section"), slug), "pool": q.get("pool"),
                "layer": q.get("layer"), "d": q.get("domain"), "task": q.get("task"), "topics": q.get("topics") or [],
                "concept": q.get("concept"), "diff": q.get("difficulty"), "type": q.get("type"), "select": q.get("select"),
                "qual": None if qual in (None, "", "none") else qual, "opt": derive_opt(qual), "stem": q.get("stem", ""),
                "kw": q.get("keywords") or [],
                "options": [{"id": o.get("id"), "text": o.get("text", ""), "ok": bool(o.get("correct")),
                             "why_h": self.h(f"q:{qid}:why:{o.get('id')}"), "concept": o.get("concept"), "trap": o.get("trap")}
                            for o in q.get("options", [])],
                "expl_h": self.h(f"q:{qid}:expl"), "take_h": self.h(f"q:{qid}:take"), "twin_h": self.h(f"q:{qid}:twin"),
                "say": q.get("say"), "facts": q.get("facts") or [], "twinOf": q.get("twin_of"),
                "worked": {"steps": worked.get("steps") or [], "wrongPath": bool(worked.get("wrong_path"))} if worked else None,
                "keyRev": q.get("keyRev", 1)}

    def card(self, c, slug) -> dict:
        return {"id": c["id"], "type": c.get("type"), "deck": c.get("deck"), "front": c.get("front", ""),
                "back": c.get("back", ""), "extra_h": self.h(f"c:{c['id']}:extra"), "facts": c.get("facts") or [],
                "term": c.get("term"), "word": c.get("word"), "speak": c.get("speak"),
                "sec": self.resolve_sec(c.get("section"), slug), "trap": c.get("trap"), "changed": c.get("changed")}

    def speak(self, s, slug) -> dict:
        out = {k: v for k, v in s.items() if k not in ("status", "rev", "section")}
        out["sec"] = self.resolve_sec(s.get("section"), slug)
        return out

    def task(self, t, slug) -> dict:
        out = {k: v for k, v in t.items() if k not in ("status", "rev", "sources", "section", "steps")}
        steps = []
        for n, step in enumerate(t.get("steps", []), 1):
            row = {k: v for k, v in step.items() if k != "explain"}
            command = step.get("command")
            cap = step.get("capture")
            if command and cap:
                command = f"{cap['name']}=$({command} --query {cap['query']} --output text)"
            row["shown"] = command
            row["explain_h"] = self.h(f"t:{t['id']}:explain:{n}") if step.get("explain") else ""
            steps.append(row)
        out["steps"] = steps
        out["sec"] = self.resolve_sec(t.get("section"), slug)
        if t.get("type") in ("try", "lab"):
            out["careful"] = (self.spec.get("tasks") or {}).get("stop_rule", "")
        return out

    def facts_of(self, obj) -> set:
        """Fact ids named anywhere in an emitted item (lists named facts, cost_facts, fact, and _h links)."""
        found = set()

        def walk(value, key=None):
            if isinstance(value, dict):
                for k, v in value.items():
                    walk(v, k)
            elif isinstance(value, list):
                for v in value:
                    walk(v, key)
            elif isinstance(value, str):
                if key in ("facts", "cost_facts", "fact"):
                    found.add(value)
                elif key and key.endswith("_h"):
                    found.update(RE_DATA_FACT.findall(value))
        walk(obj)
        return {f for f in found if f in self.facts}

    def cards_for(self, ids) -> dict:
        return {fid: fact_card(self.facts[fid]) for fid in sorted(ids) if fid in self.facts}

    def data(self):
        self.manifest_chapters, self.qall, self.qindex = [], {}, {"v": 1, "q": {}, "wrong": {}, "s": {}}
        self.corpus = {}            # shard key (chapter slug or SEARCH_BOOK) -> docs of search/<key>.json
        totals = {"questions": 0, "coreCards": 0, "speak": 0}
        dates = []
        mock_numbers = {}
        for ch in self.chapters:
            if ch.get("tier") == "mock" or self.template(ch)["key"] == "mock":
                mock_numbers[ch["slug"]] = len(mock_numbers) + 1
        self.mocks = []
        pool_code = {"chapter": 0, "drill": 1, "mock": 2}
        for ch in self.chapters:
            slug = ch["slug"]
            state = self.state[slug]
            tpl = self.template(ch)
            if state == "planned":
                minutes = tpl["minutes"]
                self.manifest_chapters.append({
                    "slug": slug, "id": ch["id"], "title": ch.get("title", ""), "part": ch.get("part"),
                    "tier": ch.get("tier"), "template": tpl["key"], "status": "planned", "rev": self.rev(ch),
                    "domains": sorted({int(str(t)[0]) for t in ch.get("tasks", []) if str(t)[:1].isdigit()}),
                    "minutes": {"fast": minutes.get("fast", 0),
                                "pass": minutes.get("pass_xl" if ch.get("xl") else "pass", minutes.get("pass", 0)),
                                "full": minutes.get("full", 0)},
                    "files": [], "sections": [], "traps": {},
                    "counts": {"q": 0, "core": 0, "cards": 0, "speak": 0, "tasks": 0, "figures": 0}, "c": 0, "d": 0})
                continue
            info = self.info[slug]
            dates += info["updated"]
            fm = info["fm"]
            file_label = info["folder"].name
            is_mock = ch.get("tier") == "mock" or tpl["key"] == "mock"
            questions = [self.question(q, slug) for q in info["items"]["questions"]]
            cards = [self.card(c, slug) for c in info["items"]["cards"]]
            speak = [self.speak(s, slug) for s in info["items"]["speak"]]
            tasks = [self.task(t, slug) for t in info["items"]["tasks"]]
            chapter_q = [q for q in questions if q["pool"] == "chapter"]
            d_questions = [q for q in questions if q["pool"] in ("chapter", "drill")]
            for q in questions:
                self.qall[q["id"]] = q
            # parts
            parts, files, rows, traps, secs, text, figures = {}, [], [], {}, {}, {}, {}
            part_facts = set()
            for key, name, _path in info["md"]:
                got = self.rendered["parts"][f"{slug}/{key}"]
                title = got.get("title") or PART_TITLES.get(key, key)
                parts[key] = {"title": title, "html": got["html"]}
                files.append({"key": key, "title": PART_TITLES.get(key, key)})
                part_facts.update(got["facts"])
                for s in got["sections"]:
                    rows.append([s["sid"], key, s["kind"], s["route"], s["min"], s["title"], s["parent"], s["role"]])
                    if s["facts"] or s["terms"] or s["figures"]:
                        secs[s["sid"]] = {"facts": s["facts"], "terms": s["terms"], "figs": s["figures"]}
                for row in got["text"]:
                    if row["text"]:
                        text[row["sid"]] = row["text"]
                    if row.get("own"):
                        heading = next((s["title"] for s in got["sections"] if s["sid"] == row["sid"]), "")
                        self.corpus.setdefault(slug, []).append([f"ch.{slug}.{key}.{row['sid']}", ch.get("title", ""), heading,
                                                                 "s", row["own"]])
                for trap, sid in got["trapmap"].items():
                    traps.setdefault(trap, f"{key}.{sid}" if sid else key)
                for fid, meta in got["figmeta"].items():
                    extra = self.figure_info.get(fid, {"title": "", "w": 0})
                    desc = (meta.get("claim") or "").strip()
                    desc += "".join(f" {n}. {s}" for n, s in enumerate(meta.get("steps") or [], 1))
                    figures.setdefault(fid, {"n": meta["n"], "title": extra["title"], "alt": meta["alt"], "desc": desc.strip(),
                                             "w": extra["w"]})
            if any(t.get("type") in ("try", "lab") for t in tasks):
                files.append({"key": "do", "title": PART_TITLES["do"]})
            if speak:
                files.append({"key": "say", "title": PART_TITLES["say"]})
            if chapter_q or is_mock:
                files.append({"key": "quiz", "title": PART_TITLES["quiz"]})
            files.append({"key": "sources", "title": PART_TITLES["sources"]})
            have = {f["key"] for f in files}
            for fs in tpl["files"]:
                name = fs.get("name")
                want = PART_OF_FILE.get(name) or GENERATED_PARTS.get(name)
                if want == "do" and not fs.get("required"):
                    continue
                if fs.get("required") and want and want not in have:
                    msg = f"part {want} ({name}) is missing or has no shippable item"
                    (self.err if state == "ready" else self.warn)("WB05", msg, f"{file_label}/{name}")
            # facts of the items
            d_ids = set()
            for obj in d_questions + cards + speak + tasks:
                d_ids |= self.facts_of(obj)
            source_ids = set(part_facts) | d_ids
            pages = {}
            for fid in sorted(source_ids):
                fact = self.facts.get(fid)
                for ev in (fact or {}).get("evidence", []):
                    if not ev.get("url"):
                        continue
                    page = pages.setdefault(ev["url"], {"title": ev.get("title") or ev["url"], "url": ev["url"], "checked": "", "facts": []})
                    page["checked"] = max(page["checked"], str(fact.get("retrieved") or ""))
                    if fid not in page["facts"]:
                        page["facts"].append(fid)
            sources = sorted(pages.values(), key=lambda p: (p["title"].lower(), p["url"]))
            c_doc = {"v": 1, "slug": slug, "parts": parts, "facts": self.cards_for(source_ids & set(self.facts)),
                     "figures": figures, "sources": sources, "secs": secs, "text": text}
            c_bytes = dumps(c_doc)
            self.files[f"c/{slug}.json"] = c_bytes
            d_bytes = b""
            if d_questions or cards or speak or tasks:
                d_doc = {"v": 1, "slug": slug, "questions": d_questions, "cards": cards, "speak": speak, "tasks": tasks,
                         "facts": self.cards_for(d_ids)}
                d_bytes = dumps(d_doc)
                self.files[f"d/{slug}.json"] = d_bytes
            # indexes
            for q in questions:
                self.index_question(q, pool_code.get(q["pool"], 0))
            for q in chapter_q:
                self.corpus.setdefault(slug, []).append([f"quiz.{slug}", ch.get("title", ""), "Question", "q", q["stem"]])
            for s in speak:
                self.qindex["s"][s["id"]] = [slug, s.get("kind"), 1 if s.get("pass_route") else 0, 1 if s.get("pack") else 0,
                                             s.get("prompt", "")]
            totals["questions"] += len(chapter_q)
            totals["coreCards"] += sum(1 for c in cards if c.get("deck") == "core")
            totals["speak"] += len(speak)
            minutes = fm.get("minutes") if isinstance(fm.get("minutes"), dict) else {}
            domains = fm.get("domains") if isinstance(fm.get("domains"), list) else \
                sorted({int(str(t)[0]) for t in ch.get("tasks", []) if str(t)[:1].isdigit()})
            self.manifest_chapters.append({
                "slug": slug, "id": ch["id"], "title": ch.get("title", ""), "part": ch.get("part"), "tier": ch.get("tier"),
                "template": tpl["key"], "status": state, "rev": self.rev(ch),
                "hash": common.sha256_bytes(c_bytes + d_bytes)[:8], "domains": domains,
                "minutes": {k: int(minutes.get(k, tpl["minutes"].get(k, 0)) or 0) for k in ("fast", "pass", "full")},
                "files": files, "sections": rows, "traps": dict(sorted(traps.items())),
                "counts": {"q": len(chapter_q), "core": sum(1 for q in chapter_q if q["layer"] == "core"), "cards": len(cards),
                           "speak": len(speak), "tasks": len(tasks), "figures": len(figures)},
                "c": len(c_bytes), "d": len(d_bytes)})
            # the mock of a mock chapter
            if is_mock:
                mock_n = mock_numbers.get(slug, len(self.mocks) + 1)
                mock =common.read_json(common.DATA / self.dirname(ch) / "mock.json")
                valid = isinstance(mock, dict) and isinstance(mock.get("questions"), list)
                if valid:
                    try:
                        from saalib import schemas
                        valid = not schemas.validate(mock, "mock")
                    except Exception:
                        pass
                if not valid:
                    (self.err if state == "ready" else self.warn)("WB05", "mock.json is missing or does not validate; this mock is left out",
                                                                   f"data/{self.dirname(ch)}/mock.json")
                else:
                    by_id = {q["id"]: q for q in questions if q["pool"] == "mock"}
                    chosen = [by_id[i] for i in mock["questions"] if i in by_id]
                    if len(chosen) != len(mock["questions"]):
                        (self.err if state == "ready" else self.warn)(
                            "WB05", f"{len(mock['questions']) - len(chosen)} questions of mock.json are not shippable",
                            f"data/{self.dirname(ch)}/mock.json")
                    ids = set()
                    for q in chosen:
                        ids |= self.facts_of(q)
                    self.files[f"q/{slug}.json"] = dumps({"v": 1, "slug": slug, "minutes": mock.get("minutes"),
                                                          "split": mock.get("domain_split"), "questions": chosen,
                                                          "facts": self.cards_for(ids)})
                    self.mocks.append({"n": mock_n, "slug": slug, "title": ch.get("title", ""), "file": f"q/{slug}.json",
                                       "count": len(chosen), "minutes": mock.get("minutes"), "split": mock.get("domain_split"),
                                       "synthetic": False})
        if self.preview and not self.mocks:
            self.preview_mock()
        self.drill_files()
        self.totals = totals
        self.dates = dates

    def index_question(self, q, pool):
        self.qindex["q"][q["id"]] = [q["ch"], q["d"], 0 if q["layer"] == "core" else 1, pool, q["concept"], q["keyRev"],
                                     q["topics"]]
        wrong = {o["id"]: o["concept"] for o in q["options"] if not o["ok"]}
        if wrong:
            self.qindex["wrong"][q["id"]] = wrong

    def preview_mock(self):
        base = sorted((q for q in self.qall.values() if q["pool"] == "chapter"), key=lambda q: q["id"])
        if not base:
            return
        split = [20, 17, 15, 13]
        domains = [d for d, n in enumerate(split, 1) for _ in range(n)]
        questions, ids = [], set()
        for n in range(sum(split)):
            q = copy.deepcopy(base[n % len(base)])
            q.update({"id": f"preview-q{n + 1:03d}", "pool": "mock", "ch": "mock-preview", "d": domains[n], "twinOf": None})
            questions.append(q)
            ids |= self.facts_of(q)
            self.index_question(q, 2)
        minutes = self.cfg.get("previewMockMinutes", DEFAULT_CFG["previewMockMinutes"])
        self.files["q/mock-preview.json"] = dumps({"v": 1, "slug": "mock-preview", "minutes": minutes, "split": split,
                                                   "questions": questions, "facts": self.cards_for(ids)})
        self.mocks.append({"n": 1, "slug": "mock-preview", "title": "Preview mock", "file": "q/mock-preview.json",
                           "count": len(questions), "minutes": minutes, "split": split, "synthetic": True})

    def drill_files(self):
        self.drill_rows = []
        for drill in (self.drills or {}).get("drills", []) if isinstance(self.drills, dict) else []:
            chosen = [self.qall[i] for i in drill.get("questions", []) if i in self.qall and self.qall[i]["pool"] != "mock"]
            missing = len(drill.get("questions", [])) - len(chosen)
            if missing:
                self.warn("WB05", f"{missing} questions of {drill.get('id')} are not shippable in this build", self.drills_file,
                          item=drill.get("id"))
            ids = set()
            for q in chosen:
                ids |= self.facts_of(q)
            path = f"q/{drill['id']}.json"
            self.files[path] = dumps({"v": 1, "id": drill["id"], "domain": drill.get("domain"), "title": drill.get("title", ""),
                                      "questions": chosen, "facts": self.cards_for(ids)})
            self.drill_rows.append({"id": drill["id"], "domain": drill.get("domain"), "title": drill.get("title", ""),
                                    "file": path, "count": len(chosen)})

    def reference_files(self):
        glossary = {}
        aliases = {}
        for t in self.terms:
            glossary[t["id"]] = {"term": t.get("term"), "say": t.get("respelling"), "meaning": t.get("meaning", ""),
                                 "with": t.get("collocations") or [], "not": t.get("do_not_confuse") or [],
                                 "short": t.get("short"), "facts": [f for f in t.get("facts") or [] if f in self.facts]}
            self.corpus.setdefault(SEARCH_BOOK, []).append([f"glossary.{t['id']}", "Glossary", t.get("term", ""), "g",
                                                            " ".join([t.get("meaning", "")] + list(t.get("collocations") or []))])
            forms = ([t["short"]] if t.get("short") else []) + list(t.get("aliases") or [])
            if forms:
                aliases[t["id"]] = forms
        self.files["glossary.json"] = dumps({"v": 1, "terms": glossary})
        if isinstance(self.plan, dict):
            plan = copy.deepcopy(self.plan)
            for p in plan.get("plans", []):
                for day in p.get("days", []):
                    for task in day.get("tasks", []):
                        if task.get("chapter"):
                            task["chapter"] = (self.by_id.get(str(task["chapter"])) or {}).get("slug")
            self.files["plan.json"] = dumps(plan)
            self.plan_out = plan
        else:
            self.plan_out = None
            self.warn("WB05", "data/plan.json does not exist; the plan views stay empty", "data/plan.json")
        self.fact_shards()
        owner = {}                  # fact namespace -> the chapter that lists it in book.json `services`
        for ch in self.chapters:
            for service in ch.get("services") or []:
                owner.setdefault(service, ch["slug"])
        for fid in sorted(self.facts):
            ns = self.fact_ns.get(fid) or str(self.facts[fid].get("service") or "")
            self.corpus.setdefault(owner.get(ns, SEARCH_BOOK), []).append(
                [f"fact.{fid}", str(self.facts[fid].get("service") or ""), fid, "f", self.facts[fid].get("claim", "")])
        self.search_shards(aliases)
        self.files["qindex.json"] = dumps(self.qindex)
        if self.icons_mod is not None and self.icons_used:
            self.files["assets/icons.svg"] = self.icons_mod.sprite(self.icons, sorted(self.icons_used)).encode("utf-8")
        else:
            self.files["assets/icons.svg"] = b'<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true"></svg>\n'
        worker = self.source("js/search-worker.js")
        self.worker = worker or ""
        self.worker_src = worker
        if worker is not None:
            self.files["assets/search-worker.js"] = worker.encode("utf-8")
        self.exports = []
        if not self.single and common.EXPORTS.is_dir():
            for path in sorted(common.EXPORTS.iterdir()):
                if path.is_file() and path.suffix.lower() in EXPORT_TYPES:
                    data = path.read_bytes()
                    self.files[f"exports/{path.name}"] = data
                    self.exports.append({"name": path.name, "path": f"exports/{path.name}", "bytes": len(data),
                                         "repo": f"aws-saa-book/exports/{path.name}"})

    def fact_shards(self):
        """One f/<service>.json per fact namespace and the small facts-index.json (section 2.4)."""
        groups = {}
        for fid in sorted(self.facts):
            groups.setdefault(self.fact_ns.get(fid) or str(self.facts[fid].get("service") or ""), []).append(fid)
        shards = {}
        for service in sorted(groups):
            if not RE_SHARD.match(service):
                self.err("WB07", f"fact namespace {service!r} is not a valid shard name; its {len(groups[service])} facts are left out",
                         f"data/facts/{service}.jsonl")
                continue
            path = f"{SHARD_DIR}/{service}.json"
            data = dumps({"v": 1, "service": service, "facts": self.cards_for(groups[service])})
            self.files[path] = data
            shards[service] = {"path": path, "bytes": len(data), "sha256": common.sha256_bytes(data), "count": len(groups[service])}
        stray = {fid: service for service in shards for fid in groups[service] if fact_shard(fid, shards) != service}
        count = sum(row["count"] for row in shards.values())
        data = dumps({"v": 1, "count": count, "shards": shards, "stray": dict(sorted(stray.items()))})
        self.files[FACTS_INDEX] = data
        self.facts_index = {"path": FACTS_INDEX, "bytes": len(data), "sha256": common.sha256_bytes(data),
                            "shards": len(shards), "count": count}

    def search_shards(self, aliases: dict):
        """One search/<slug>.json per chapter that has docs, search/book.json for the rest, and search/index.json (2.4)."""
        rows = []
        for key in [ch["slug"] for ch in self.chapters] + [SEARCH_BOOK]:
            docs = self.corpus.get(key)
            if not docs:
                continue
            chapter = None if key == SEARCH_BOOK else key
            path = f"{SEARCH_DIR}/{key}.json"
            data = dumps({"v": 1, "chapter": chapter, "docs": docs})
            self.files[path] = data
            rows.append({"chapter": chapter, "path": path, "bytes": len(data), "count": len(docs)})
        data = dumps({"v": 1, "count": sum(r["count"] for r in rows), "aliases": aliases, "shards": rows})
        self.files[SEARCH_INDEX] = data
        self.search_index = {"path": SEARCH_INDEX, "bytes": len(data), "shards": len(rows), "count": sum(r["count"] for r in rows)}

    # ---- step 7: shell

    def assets(self):
        """The concatenated CSS and page script."""
        css_parts, css_texts = [], {}
        tokens = None
        if (self.web / "tokens.json").is_file():
            tokens = common.read_json(self.web / "tokens.json")
        else:
            (self.warn if self.preview else self.err)("WB02", "source file tools/web/tokens.json does not exist", "tools/web/tokens.json")
        if isinstance(tokens, dict):
            css, found = token_css(tokens)
            css_parts.append(css)
            self.errors += found
        try:
            from saalib.diagram import svg
            diagram_css = svg.inline_css()
        except Exception as exc:
            diagram_css = ""
            self.warn("WB02", f"the diagram stylesheet could not be loaded: {exc!r}")
        css_parts.append(diagram_css)
        css_texts["diagram css"] = diagram_css
        names = list(CSS_FILES)
        folder = self.web / "css"
        if folder.is_dir():
            names += [p.name for p in sorted(folder.glob("*.css")) if p.name not in names]
        for name in sorted(names):
            text = self.source(f"css/{name}")
            if text is not None:
                css_parts.append((minify_css(text) if self.minify else text).rstrip("\n") + "\n")
                css_texts[f"tools/web/css/{name}"] = text
        if isinstance(tokens, dict):
            self.errors += undefined_vars(tokens, css_texts)
        self.css = "".join(css_parts)
        sources = []
        for name in JS_FILES:
            if name == "selftest.js" and not self.preview:
                continue
            text = self.source(f"js/{name}")
            if text is not None:
                sources.append((name, text))

        def join(small: bool) -> str:
            return "".join(f"/* {name} */\n" + (minify_js(text) if small else text).rstrip("\n") + "\n;\n" for name, text in sources)

        self.js = join(False)
        node = shutil.which("node") if self.minify else None
        if node:                      # the smaller script is used only when node accepts its syntax
            small = join(True)
            check = common.ensure_dir(common.TMP / "site") / "page-script.js"
            check.write_text(small, encoding="utf-8")
            try:
                ok = subprocess.run([node, "--check", str(check)], capture_output=True, text=True, timeout=120).returncode == 0
            except (OSError, subprocess.TimeoutExpired):
                ok = False
            if ok:
                self.js = small
            else:
                self.warn("WB02", "the page script without comments failed the syntax check of node; the full text is used")
        if self.worker_src is not None and self.minify and node:
            small = minify_js(self.worker_src)
            check = common.TMP / "site" / "worker-script.js"
            check.write_text(small, encoding="utf-8")
            try:
                if subprocess.run([node, "--check", str(check)], capture_output=True, text=True, timeout=120).returncode == 0:
                    self.worker = small
                    self.files["assets/search-worker.js"] = small.encode("utf-8")
            except (OSError, subprocess.TimeoutExpired):
                pass

    def exam_facts(self) -> dict:
        out = {}
        for key, fid in (self.cfg.get("examFacts") or {}).items():
            fact = self.facts.get(fid)
            displays = [v.get("display") for v in (fact or {}).get("values", []) if v.get("display")]
            if not displays:
                self.warn("WB10", f"exam fact {key} ({fid}) is not a verified fact; the entry is left out", "tools/web/shell.json", item=fid)
                continue
            out[key] = {"id": fid, "text": displays[0]}
        return out

    def manifest(self):
        order = []
        if self.plan_out:
            plan_a = next((p for p in self.plan_out.get("plans", []) if p.get("id") == "a"), None)
            for day in (plan_a or {}).get("days", []):
                for task in day.get("tasks", []):
                    if task.get("chapter") and task["chapter"] not in order:
                        order.append(task["chapter"])
        order += [ch["slug"] for ch in self.chapters if ch["slug"] not in order]
        aliases = {}
        for name, ch_id in ALIAS_CHAPTERS.items():
            ch = self.by_id.get(ch_id)
            row = next((m for m in self.manifest_chapters if ch and m["slug"] == ch["slug"]), None)
            if row and any(f["key"] == "sheet" for f in row["files"]):
                aliases[name] = f"ch.{ch['slug']}.sheet"
        published = common.read_json(common.REPORTS / "site-published.json") or {}
        self.url = published.get("url") if isinstance(published, dict) else None
        self.published = published if isinstance(published, dict) else {}
        lines = [f"{path}:{common.sha256_bytes(data)}" for path, data in sorted(self.files.items())]
        lines += [f"css:{common.sha256_bytes(self.css.encode('utf-8'))}", f"js:{common.sha256_bytes(self.js.encode('utf-8'))}"]
        self.build_id = common.sha256_bytes("\n".join(lines).encode("utf-8"))[:10]
        self.manifest_doc = {
            "v": 1, "build": self.build_id, "title": TITLE,
            "date": max(self.dates) if self.dates else self.meta.get("snapshot_date"),
            "fixture": self.fixture, "artifactUrl": self.url,
            "domains": [{"id": d.get("id"), "title": d.get("title"), "weight": d.get("weight")} for d in self.guide.get("domains", [])],
            "parts": self.book.get("parts") or [], "chapters": self.manifest_chapters, "order": order,
            "mocks": self.mocks, "drills": self.drill_rows, "aliases": aliases,
            "terms": [[t["id"], t.get("term", "")] for t in self.terms], "examFacts": self.exam_facts(),
            "factsIndex": self.facts_index, "exports": self.exports, "counts": self.totals}
        self.files["manifest.json"] = dumps(self.manifest_doc)

    def toc_html(self) -> str:
        esc = html.escape
        words = {"planned": "Not written yet", "draft": "Draft", "ready": ""}
        by_part = {}
        for row in self.manifest_chapters:
            by_part.setdefault(row.get("part"), []).append(row)
        parts = list(self.book.get("parts") or [])
        known = {p.get("id") for p in parts}
        parts += [{"id": pid, "title": str(pid or "Other")} for pid in by_part if pid not in known]
        out = ['<ol class="toc-list">']
        for part in parts:
            rows = by_part.get(part.get("id")) or []
            if not rows:
                continue
            out.append(f'<li class="toc-part"><span class="toc-part-t">{esc(str(part.get("title", "")))}</span><ol>')
            for row in rows:
                word = words[row["status"]]
                status = f' <span class="toc-st">{word}</span>' if word else ""
                label = f'<span class="mono">{esc(row["id"])}</span> {esc(row["title"])}'
                if row["status"] == "planned":
                    out.append(f'<li class="toc-ch is-planned"><span class="toc-t">{label}</span>{status}</li>')
                else:
                    out.append(f'<li class="toc-ch is-{row["status"]}"><a href="#ch.{row["slug"]}">{label}</a>{status}</li>')
            out.append("</ol></li>")
        out.append("</ol>")
        refs = [("glossary", "Glossary")]
        refs += [(name, label) for name, label in (("numbers", "Numbers"), ("traps", "Traps"), ("changed", "Changed recently"))
                 if name in self.manifest_doc["aliases"]]
        refs += [("files", "Get files"), ("about", "About")]
        out.append('<div class="toc-ref"><p class="eyebrow">Reference</p><ul>'
                   + "".join(f'<li><a href="#{name}">{label}</a></li>' for name, label in refs) + "</ul></div>")
        return "".join(out)

    def static_html(self, toc: str) -> str:
        esc = html.escape
        facts = self.manifest_doc["examFacts"]
        strip = ""
        if facts:
            strip = '<p class="static-facts">' + " ".join(
                f'<span class="pill">{esc(facts[k]["text"])}</span>' for k in ("count", "minutes", "pass", "esl") if k in facts) + "</p>"
        ready = sum(1 for m in self.manifest_chapters if m["status"] == "ready")
        draft = sum(1 for m in self.manifest_chapters if m["status"] == "draft")
        total = len(self.manifest_chapters)
        line = f"{total} {'chapter' if total == 1 else 'chapters'}: {ready} ready, {draft} in draft."
        return ('<div class="static"><p class="eyebrow">Study handbook</p>'
                f'<h1 tabindex="-1">{esc(TITLE)}</h1><p class="lede">{esc(line)}</p>{strip}'
                f'<div class="static-toc">{toc}</div></div>')

    def page(self) -> str:
        shell = self.source("shell.html")
        if shell is None:
            shell = FALLBACK_SHELL
        toc = self.toc_html()
        boot = script_json({"build": self.build_id, "single": self.single, "preview": self.preview, "title": TITLE, "cfg": self.cfg})
        inline = ""
        if self.single:
            docs = {}
            for path, data in sorted(self.files.items()):
                if path.endswith(".json"):
                    docs[path] = json.loads(data.decode("utf-8"))
            inline = script_json(docs)
        fonts = f'<link rel="stylesheet" href="{FONTS_URL}">'
        if re.search(r'href="\{\{fonts\}\}"', shell):
            fonts = FONTS_URL
        css = self.css if re.search(r"<style[^>]*>\s*\{\{css\}\}", shell) else f"<style>{self.css}</style>"
        js = self.js if re.search(r"<script[^>]*>\s*\{\{js\}\}", shell) else f"<script>{self.js}</script>"
        if 'id="saa-boot"' not in shell:
            boot = f'<script type="application/json" id="saa-boot">{boot}</script>'
        worker = ""
        if self.single:
            if 'id="saa-inline"' not in shell:
                inline = f'<script type="application/json" id="saa-inline">{inline}</script>'
            worker = f'<script type="text/plain" id="saa-worker">{self.worker}</script>'
            if 'id="saa-worker"' in shell:
                shell = re.sub(r'(<script[^>]*id="saa-worker"[^>]*>)(</script>)', lambda m: m.group(1) + self.worker + m.group(2), shell, count=1)
                worker = ""
            sprite = self.files.get("assets/icons.svg", b"").decode("utf-8")
            sprite = re.sub(r"<\?xml[^>]*\?>", "", sprite)
            inner = re.sub(r"^\s*<svg\b[^>]*>|</svg>\s*$", "", sprite.strip())
            shell = re.sub(r'(<svg[^>]*id="saa-sprite"[^>]*>)\s*(</svg>)', lambda m: m.group(1) + inner + m.group(2), shell, count=1)
        slots = {"fonts": fonts, "css": css, "toc": toc, "static": self.static_html(toc), "boot": boot,
                 "inline": inline + worker, "js": js}
        return re.sub(r"\{\{(fonts|css|toc|static|boot|inline|js)\}\}", lambda m: slots[m.group(1)], shell)

    def wrap_preview(self, page: str) -> dict:
        skeleton = None
        path = self.web / "stubs" / "skeleton.html"
        if path.is_file():
            skeleton = path.read_text(encoding="utf-8")
        else:
            self.warn("WB02", "source file tools/web/stubs/skeleton.html does not exist; the built-in skeleton is used",
                      "tools/web/stubs/skeleton.html")
            skeleton = FALLBACK_SKELETON
        stub = self.source("stubs/claude-stub.js")
        stub_tag = f"<script>{stub}</script>" if stub is not None else ""
        out = {}
        for name, theme in (("index.html", ""), ("index-dark.html", ' data-theme="dark"'), ("index-forced-light.html", ' data-theme="light"')):
            slots = {"theme": theme, "stub": stub_tag, "page": page}
            out[name] = re.sub(r"\{\{(theme|stub|page)\}\}", lambda m: slots[m.group(1)], skeleton)
        return out

    # ---- step 8: budgets and the publish plan

    def budgets(self, final: dict):
        total = 0
        for path, data in sorted(final.items()):
            size = len(data)
            total += size
            if self.single:
                if size > SINGLE_BUDGET:
                    self.err("WB01", f"{path} is {size} bytes, above the budget of {SINGLE_BUDGET}", path)
                continue
            if self.preview and path.startswith("index"):
                continue            # the preview page carries the stub and the selftest; it is never published
            for pattern, warn, fail in BUDGETS:
                if re.search(pattern, path):
                    if size > fail:
                        self.err("WB01", f"{path} is {size} bytes, above the budget of {fail}", path)
                    elif warn is not None and size > warn:
                        self.warn("WB01", f"{path} is {size} bytes, above the warning level of {warn}", path)
                    break
            binary = path.endswith((".pdf", ".zip"))
            if size >= (15 * 1024 * 1024 if binary else 16 * 1024 * 1024):
                self.err("WB01", f"{path} is above the platform limit for one file", path)
        content = [p for p in final if not p.startswith("exports/")]
        exports = [p for p in final if p.startswith("exports/")]
        for name, paths in (("content", content), ("exports", exports)):
            size = sum(len(final[p]) for p in paths)
            if len(paths) > BATCH_FILES or size > 64 * 1024 * 1024:
                self.err("WB01", f"batch {name} has {len(paths)} files and {size} bytes (limit {BATCH_FILES} files, 64 MB)")
            elif len(paths) > BATCH_WARN_FILES:
                self.warn("WB01", f"batch {name} has {len(paths)} files, above the warning level of {BATCH_WARN_FILES} "
                                  f"(limit {BATCH_FILES}); every fact namespace adds one f/ shard, every chapter one search/ shard")
        if len(final) > 511 or total > 256 * 1024 * 1024:
            self.err("WB01", f"the site has {len(final)} files and {total} bytes (limit 511 files, 256 MB)")

    def publish_plan(self, final: dict) -> dict:
        old = self.published.get("hashes") or {}
        hashes = {path: common.sha256_bytes(data) for path, data in sorted(final.items())}

        def batch(name, paths):
            rows = [{"path": p, "bytes": len(final[p]), "sha256": hashes[p],
                     "changed": True if p in ("manifest.json", "index.html") else old.get(p) != hashes[p]} for p in paths]
            return {"name": name, "files": rows, "count": len(rows), "bytes": sum(r["bytes"] for r in rows)}

        content = [p for p in sorted(final) if not p.startswith("exports/")]
        exports = [p for p in sorted(final) if p.startswith("exports/")]
        removed = set(p for p in old if p not in final)
        removed |= {p for p in RETIRED_PATHS if p not in final}
        if self.single:
            removed |= {p for p in self.files if p != "index.html"}
        return {"build": self.build_id, "url": self.url, "title": TITLE, "icon": ICON, "capabilities": CAPABILITIES,
                "batches": [batch("content", content), batch("exports", exports)], "removed": sorted(removed),
                "hashes": hashes}

    # ---- the whole run

    def run(self) -> dict:
        from saalib import _site_web
        for f in _site_web.lint_sources():
            row = finding("WB02", f"{f['code']} {f['msg']}", f.get("file"), f.get("line", 0), f["code"])
            self.errors.append(row)
        self.load()
        self.prepare_chapters()
        self.validate()
        self.diagrams()
        self.render()
        self.data()
        self.reference_files()
        self.assets()
        self.manifest()
        page = self.page()
        if self.single:
            final = {"index.html": page.encode("utf-8")}
        else:
            final = dict(self.files)
            final["index.html"] = page.encode("utf-8")
        if self.preview:
            for name, text in self.wrap_preview(page).items():
                final[name] = text.encode("utf-8")
        self.budgets(final)
        plan = None
        write = self.preview or not self.errors
        if write:
            self.write(final)
            if not self.preview:
                plan = self.publish_plan(final)
                (self.out / "publish-plan.json").write_bytes((json.dumps(plan, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
        counts = {s: sum(1 for m in self.manifest_chapters if m["status"] == s) for s in ("ready", "draft", "planned")}
        largest = sorted(({"path": p, "bytes": len(d)} for p, d in final.items()), key=lambda r: (-r["bytes"], r["path"]))[:5]
        shard_rows = sorted(({"path": p, "bytes": len(d)} for p, d in self.files.items() if p.startswith(SHARD_DIR + "/")),
                            key=lambda r: (-r["bytes"], r["path"]))
        facts = {"count": self.facts_index["count"], "shards": self.facts_index["shards"], "largest": shard_rows[:3]}
        search_rows = sorted(({"path": p, "bytes": len(d)} for p, d in self.files.items()
                              if p.startswith(SEARCH_DIR + "/") and p != SEARCH_INDEX), key=lambda r: (-r["bytes"], r["path"]))
        search = dict(self.search_index, largest=search_rows[:3])
        return {"ok": not self.errors, "out": common.rel(self.out), "build": self.build_id,
                "mode": "single" if self.single else "multi", "preview": self.preview, "written": write,
                "chapters": counts, "files": len(final), "bytes": sum(len(d) for d in final.values()), "largest": largest,
                "facts": facts, "search": search, "errors": self.errors, "warnings": self.warnings,
                "plan": common.rel(self.out / "publish-plan.json") if plan is not None else None}

    def write(self, final: dict):
        out = self.out
        if out.exists():
            if any(out.iterdir()) and not (out / MARKER).is_file():
                raise Stop(common.EXIT_POLICY, f"refused: {common.rel(out)} is not empty and was not written by build web")
            shutil.rmtree(out)
        common.ensure_dir(out)
        for path, data in sorted(final.items()):
            target = out / path
            common.ensure_dir(target.parent)
            target.write_bytes(data)
        (out / MARKER).write_text("written by saa.py build web; this folder is replaced on every build\n", encoding="utf-8")


def run_helper(job: dict) -> dict:
    work = common.ensure_dir(common.TMP / "site")
    job_path, out_path = work / "job.json", work / "result.json"
    job_path.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
    if out_path.exists():
        out_path.unlink()
    helper = common.TOOLS / "helpers" / "site_md.py"
    try:
        proc = subprocess.run(["uv", "run", "--script", str(helper), "--job", str(job_path), "--out", str(out_path)],
                              capture_output=True, text=True, timeout=900, cwd=str(common.REPO))
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise Stop(common.EXIT_TRANSIENT, f"WB08 the Markdown helper could not run under uv: {exc}")
    if proc.returncode != 0 or not out_path.is_file():
        tail = "\n".join((proc.stderr or "").strip().splitlines()[-12:])
        raise Stop(common.EXIT_TRANSIENT, f"WB08 the Markdown helper failed (exit {proc.returncode}):\n{tail}")
    return json.loads(out_path.read_text(encoding="utf-8"))


def build_site(only_ready=False, single=False, preview=False, out=None, minify=True) -> dict:
    """Run one build. Raises Stop(code, message) on a refusal or a helper failure."""
    return Build(only_ready=only_ready, single=single, preview=preview, out=out, minify=minify).run()


def exit_code(result: dict) -> int:
    if result["errors"]:
        return common.EXIT_FAIL
    return common.EXIT_WARN if result["warnings"] else common.EXIT_OK


def text_report(result: dict) -> str:
    lines = [f"build web: {'ok' if result['ok'] else 'FAILED'}; {result['mode']}{' preview' if result.get('preview') else ''}; "
             f"build {result['build']}; {result['files']} files, {result['bytes']} bytes; "
             f"chapters ready {result['chapters']['ready']}, draft {result['chapters']['draft']}, planned {result['chapters']['planned']}; "
             f"{len(result['errors'])} errors, {len(result['warnings'])} warnings; out {result['out']}"]
    for kind, rows in (("error", result["errors"]), ("warning", result["warnings"])):
        for f in rows:
            where = f"{f['file']}:{f['line']}" if f.get("file") else (f.get("item") or "-")
            lines.append(f"{kind}: {where}: {f['code']} {f['msg']}")
    return "\n".join(lines[:41])


# ---------------------------------------------------------------- commands

def cmd_build(args) -> int:
    out = None
    if args.out_dir:
        out = Path(args.out_dir)
        if not out.is_absolute():
            out = common.REPO / out
        out = out.resolve()
        if not common.inside_book(out) or out == common.REAL_BOOK.resolve():
            return common.fail(f"refused: --out-dir must be a folder inside {common.REAL_BOOK}", common.EXIT_POLICY)
    try:
        result = build_site(only_ready=args.only_ready, single=args.single, preview=args.preview, out=out, minify=not args.no_minify)
    except Stop as stop:
        return common.fail(str(stop), stop.code)
    common.emit(result if args.json else text_report(result), args)
    return exit_code(result)


def cmd_lint(args) -> int:
    from saalib import _site_web
    return _site_web.cmd_lint(args)


def cmd_selftest(args) -> int:
    from saalib import _site_web
    return _site_web.cmd_selftest(args)


def cmd_shots(args) -> int:
    from saalib import _site_web
    return _site_web.cmd_shots(args)


def register(subparsers) -> None:
    build = group(subparsers, "build", "build the outputs of the book (web site, exports)")
    p = build.add_parser("web", help="build the web version into _build/site (see tools/web/ARCHITECTURE.md)")
    p.add_argument("--only-ready", action="store_true", help="treat draft chapters as planned")
    p.add_argument("--single", action="store_true", help="one index.html with every JSON file inlined")
    p.add_argument("--preview", action="store_true", help="local preview with the publish skeleton and the claude stub")
    p.add_argument("--out-dir", "--dir", dest="out_dir", help="output folder (inside aws-saa-book/) instead of the default")
    p.add_argument("--no-minify", action="store_true", help="keep comments and indentation of the page script and the CSS")
    common.add_common_args(p)
    p.set_defaults(func=cmd_build)

    web = group(subparsers, "web", "checks of the web version: lint, selftest, shots")
    p = web.add_parser("lint", help="source lint of tools/web (section 9.5)")
    common.add_common_args(p)
    p.set_defaults(func=cmd_lint)
    p = web.add_parser("selftest", help="build a preview, run the browser routes and the node tests")
    p.add_argument("--single", action="store_true")
    p.add_argument("--only", choices=["render", "phone", "sim", "hot", "node"])
    common.add_common_args(p)
    p.set_defaults(func=cmd_selftest)
    p = web.add_parser("shots", help="build a preview and write the screenshots of section 9.3")
    p.add_argument("--single", action="store_true")
    p.add_argument("--only", help="comma-separated shot names")
    p.add_argument("--shots-dir", dest="shots_dir", help="folder for the PNG files (inside aws-saa-book/)")
    p.add_argument("--extra", help="JSON file with extra shots: [{name, route, ls?, ss?, steps?, sizes?, themes?}] "
                                   "(steps: [[\"click\"|\"fill\"|\"scroll\"|\"wait\", selector or ms, text?]]); with --extra and "
                                   "without --only, only the extra shots are taken")
    common.add_common_args(p)
    p.set_defaults(func=cmd_shots)
