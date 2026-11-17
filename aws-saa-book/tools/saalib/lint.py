"""Chapter lint and sync (TOOLS.md 6.1, TOOLS-items.md 6.2, TOOLS-rules.md R1 to R4).

Subcommands: `lint CH [--file NAME] [--draft] [--strict]`, `lint --all`, `sync [CH | --all] [--check] [--only KIND ...]`.
Shared functions for other modules: template, word_count, anchor, section_id, sections, traps, a_list_facts,
check_strict_text, gate_lint, gate_sync. Every limit and heading comes from SPEC.json at call time.
Standard library only. The generators of `sync` live in saalib/_sync.py.
"""
from __future__ import annotations

import copy
import html
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

from saalib import common

LK, LM, LE = "", "", ""      # link marker: LK <index> LM <text> LE
NF, NE = "", ""                    # no-fact marker: NF <reason> NE
_RE_MARK = re.compile(LK + r"\d+" + LM + "|" + LE + "|" + NF + r"[^" + NE + r"]*" + NE)
_RE_LINKIDX = re.compile(LK + r"(\d+)" + LM)
_RE_NOFACT = re.compile(NF + r"([^" + NE + r"]*)" + NE)
_FACT_SPAN = re.compile(LK + r"(\d+)" + LM + "[^" + LE + "]*" + LE)
_RE_COMMENT = re.compile(r"<!--.*?-->", re.S)
_RE_ICODE = re.compile(r"`[^`\n]*`")
_RE_IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]*)\)")
_RE_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^()\s]*(?:\([^()]*\)[^()\s]*)*)\)")
_RE_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_RE_FENCE = re.compile(r"^\s*```\s*(\S*)\s*$")
_RE_LIST = re.compile(r"^\s{0,3}(?:([-*+])|(\d{1,3})[.)])\s+(.*)$")
_RE_MARKER = re.compile(r"<!--\s*(no-fact|needs-fact|needs-display|needs-term|xref|trap-ref|trap|gist-trap|task|twins|table)"
                        r"(?::\s*(.*?))?\s*-->", re.S)
_RE_REGION_START = re.compile(r"^<!--\s*([a-z][a-z-]*):start\b(.*?)-->$")
_RE_BOLD_START = re.compile(r"^\*\*([^*]+?)\*\*\s*")
_RE_ALNUM = re.compile(r"[^\W_]")
_RE_TAG = re.compile(r"</?([a-z][a-z0-9]*)(?:\s[^<>]*)?/?>")
_RE_EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿️]")
_RE_URL = re.compile(r"https?://[^\s)>\]]+")
_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
_RE_DATE = re.compile(r"\b\d{4}-\d{2}(?:-\d{2})?\b|\b(?:%s)\s+(?:\d{1,2},\s+)?\d{4}\b|\b\d{1,2}\s+(?:%s)\s+\d{4}\b" % (_MONTHS, _MONTHS))
_RE_SPLIT = re.compile(r"(?:(?<=[.?!:])|(?<=[.?!][\"')]))\s+(?=(?:" + LK + r"\d+" + LM + r")?[\"'A-Z0-9])")
_DRAFTED = ("drafted", "reviewed", "ready")
GEN_KINDS = {"3-do.md": "do", "4-say.md": "say", "5-quiz.md": "quiz", "sources.md": "sources",
             "exam-english.md": "exam-english", "sheet.md": "sheet"}


# ---------------------------------------------------------------- SPEC, template, small helpers

def spec() -> dict:
    sp = common.read_json(common.STYLE_DIR / "SPEC.json")
    if sp is None:
        raise SystemExit(common.fail(f"no SPEC.json in {common.STYLE_DIR}", common.EXIT_PRECONDITION))
    return sp


def _merge(base, over):
    if isinstance(base, dict) and isinstance(over, dict):
        out = dict(base)
        for key, value in over.items():
            out[key] = _merge(base[key], value) if key in base else copy.deepcopy(value)
        return out
    return copy.deepcopy(over)


def _entry(ch) -> dict:
    return ch if isinstance(ch, dict) else common.chapter(ch)


def template(ch) -> dict:
    """The resolved template of a chapter (SPEC.json resolution.template). Keys: key, files, counts, minutes."""
    entry, sp = _entry(ch), spec()
    over = sp.get("chapter_overrides", {}).get(entry["id"]) or {}
    key = over.get("template") or entry.get("kind") or entry.get("tier")
    base = sp.get("templates", {}).get(key)
    if base is None:
        raise SystemExit(common.fail(f"chapter {entry['id']}: no template {key!r} in SPEC.json", common.EXIT_PRECONDITION))
    out = _merge(base, {k: v for k, v in over.items() if k not in ("template", "note")})
    out["key"] = key
    for name, default in (("files", []), ("counts", {}), ("minutes", {})):
        out.setdefault(name, default)
    ref = None
    for fs in out["files"]:      # 2-services.md of deep, medium and pattern points at the light card sections
        if fs.get("sections_ref") and not fs.get("sections"):
            if ref is None:
                light = sp.get("templates", {}).get("light", {}).get("files", [])
                ref = next((f.get("sections", []) for f in light if f.get("name") == fs["name"]), [])
            fs["sections"] = copy.deepcopy(ref)
    return out


def _strip_for_count(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 3)
        if end >= 0:
            text = text[end + 4:]
    text = re.sub(r"<!--\s*([a-z][a-z-]*):start\b.*?<!--\s*\1:end\s*-->", " ", text, flags=re.S)
    text = re.sub(r"(?ms)^\s*```.*?^\s*```\s*$", " ", text)
    text = _RE_COMMENT.sub(" ", text)
    text = re.sub(r"\]\([^)\s]*\)", "] ", text)
    return _RE_TAG.sub(" ", text)


def word_count(text: str) -> int:
    """SPEC.json resolution.word_count: tokens that hold a letter or a digit."""
    if not text:
        return 0
    total = 0
    for tok in _RE_MARK.sub("", _strip_for_count(text)).split():
        if _RE_ALNUM.search(tok):
            # gate-break (practice 34, 39): four or more words joined by hyphens, slashes or underscores are counted
            # as their parts (`then-check-the-copy-then-delete`); `us-east-1` and `pay-as-you` stay one word
            parts = [p for p in re.split(r"[-/_–—]+", tok) if _RE_ALNUM.search(p)]
            total += len(parts) if len(parts) >= 4 else 1
    return total


def _time_box(sp, heading: str):
    m = re.search(sp["headings"]["time_box_regex"], heading)
    return (heading[:m.start()], int(m.group(1))) if m else (heading, None)


def anchor(heading: str) -> str:
    """The Markdown (GitHub) anchor of a full heading text."""
    return "".join(c for c in heading.strip().lower() if c.isalnum() or c in " -").replace(" ", "-")


def section_id(heading: str) -> str:
    """The stable section id: the anchor of the heading without its time box."""
    return anchor(_time_box(spec(), heading.strip())[0])


def _wm(phrase: str, flags=re.I):
    body = r"\s+".join(re.escape(p) for p in phrase.split())
    return re.compile(r"(?<![A-Za-z0-9-])" + body + r"(?![A-Za-z0-9-])", flags)


def _plain(marked: str) -> str:
    return _RE_MARK.sub("", marked).replace("**", "")


def _finding(code, file, line, msg, item=None) -> dict:
    return {"code": code, "file": file, "line": line, "item": item, "msg": msg}


def _load_facts() -> dict:
    try:
        from saalib import facts as facts_mod
        got = facts_mod.load()
        if isinstance(got, dict):
            return got
    except Exception:
        pass
    out = {}
    if common.FACTS_DIR.is_dir():
        for path in sorted(common.FACTS_DIR.glob("*.jsonl")):
            for row in common.read_jsonl(path):
                out[row.get("id")] = row
    return out


def _displays(fact) -> list:
    return [common.normalize_text(v.get("display", "")) for v in fact.get("values", []) if v.get("display")]


def holds_display(text: str, display: str) -> bool:
    """True when the normalised text holds the normalised display (L303, C104).

    It is a substring test with one guard: a display that starts or ends with a digit must not
    touch another digit of a longer number. `45 Gbps` and `1,500 widgets` do not hold the displays
    `5 Gbps` and `500 widgets`; `50` does not hold `5`.
    """
    if not display:
        return False
    start = text.find(display)
    while start >= 0:
        end = start + len(display)
        ok = True
        if display[0].isdigit() and start > 0:
            before = text[start - 1]
            if before.isdigit() or (before in "., " and start > 1 and text[start - 2].isdigit()):
                ok = False                  # also `2 500 widgets`: a thousands group written with a space
        if ok and display[-1].isdigit() and end < len(text):
            after = text[end]
            if after.isdigit() or (after in ".," and end + 1 < len(text) and text[end + 1].isdigit()):
                ok = False
        if ok:
            return True
        start = text.find(display, start + 1)
    return False


def link_text_extra(text: str, displays: list):
    """What a fact link text holds beside the displays of its fact and must not hold (gate-break H13):
    another number, or a word that negates the value (`not private`, `not 500 widgets but 9000 widgets`).
    Both arguments are normalised. Returns the offending text or None."""
    rest = text
    for display in sorted((d for d in displays if d), key=len, reverse=True):
        at = rest.find(display)
        while at >= 0:
            end = at + len(display)
            glued = (display[0].isdigit() and at > 0 and (rest[at - 1].isdigit() or rest[at - 1] in ".,")) or \
                    (display[-1].isdigit() and end < len(rest) and rest[end].isdigit())
            if glued:
                at = rest.find(display, at + 1)
                continue
            rest = rest[:at] + " | " + rest[end:]
            at = rest.find(display, at + 3)
    digit = re.search(r"\d[\d,.]*", rest)
    if digit:
        return digit.group(0)
    negation = _RE_NEGATION.search(rest)
    return negation.group(0) if negation else None


def _terms() -> list:
    return (common.read_json(common.DATA / "terms.json") or {}).get("terms", [])


def _official_names() -> list:
    data = common.read_json(common.REGISTRY / "services.json") or {}
    return [e for e in data.get("in_scope", []) + data.get("out_of_scope", []) if e.get("official_name")]


def _ledger_status(ch_id: str) -> str:
    return (common.read_json(common.LEDGER / "chapters" / f"{ch_id}.json") or {}).get("status", "planned")


def _items(entry, kind: str) -> list:
    doc = common.read_json(common.DATA / f"{entry['id']}-{entry['slug']}" / f"{kind}.json") or {}
    return [i for i in doc.get("items", []) if isinstance(i, dict)]


def _brief(entry):
    return common.read_json(common.BUILD / "work" / f"{entry['id']}-{entry['slug']}" / "brief.json")


def _in_range(n, want) -> bool:
    if isinstance(want, dict):
        return want.get("min", 0) <= n <= want.get("max", 10 ** 9)
    return n == want


def _range_text(want) -> str:
    return f"{want.get('min', 0)} to {want.get('max', 'any')}" if isinstance(want, dict) else str(want)


# ---------------------------------------------------------------- hard-fact matching (R2)

# gate-break H11: other spellings and exact synonyms of the absolute words of SPEC.json. They are always matched.
EXTRA_ABSOLUTE = ("can not", "no more than", "not more than", "at least", "not possible", "impossible", "does not support",
                  "do not support", "unsupported", "exclusively", "invariably", "no one", "nobody", "unlimited", "limited to",
                  "a maximum of", "a minimum of", "under no circumstances", "at all times")
_SMALL_WORD = "zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve"
_WORD_ALT = ("(?:" + _SMALL_WORD + "|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty"
             "|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)")
GAP_STOP = frozenset("of to and or in for the a an is are was per on at by with from as than that which after before within "
                     "every each when while if but not no its their it they you can will has have holds needs uses gets "
                     "creates adds keeps makes takes gives shows lists means".split())
_RE_NEGATION = re.compile(r"(?<![a-z])(?:not|never|without|except|but|instead of|rather than|no longer|n't)(?![a-z])")

class Matcher:
    """Number with a unit, absolute word, banned word and term matching, built from SPEC.json."""

    def __init__(self, sp, terms=None, names=None):
        self.sp, lint = sp, sp["lint"]
        nu = lint["number_with_unit"]
        units = "|".join(re.escape(u) for u in sorted(nu["units"], key=len, reverse=True))
        nouns = "|".join(r"\s+".join(re.escape(p) for p in n.split()) for n in sorted(nu["count_nouns"], key=len, reverse=True))
        tail = "(?:(?P<unit>" + units + ")" + ("|(?P<noun>(?i:" + nouns + "))" if nouns else "") + ")"
        self.num = re.compile(r"(?<![A-Za-z0-9$.])(?P<num>" + nu["number_regex"] + r")\+?[ \-]?" + tail + r"(?![A-Za-z])")
        # gate-break H10: one or two plain words between the number and its unit (`5 read replicas`), and a
        # number in words that is larger than twelve or compound (`nine thousand widgets`)
        gap = r"(?P<gap>(?: [A-Za-z][A-Za-z'-]*){1,2})"
        self.num_gap = re.compile(r"(?<![A-Za-z0-9$.])(?P<num>" + nu["number_regex"] + r")\+?" + gap + " " + tail + r"(?![A-Za-z])")
        self.num_word = re.compile(r"(?<![A-Za-z0-9-])(?P<num>" + _WORD_ALT + r"(?:[ -]" + _WORD_ALT + r")*)"
                                   + gap.replace("{1,2}", "{0,2}") + r"[ \-]" + tail + r"(?![A-Za-z])", re.I)
        self.unit_words = {u.lower() for u in nu["units"]} | {p.lower() for n in nu["count_nouns"] for p in [n, n.split()[0]]}
        self.cur = re.compile(r"\$[0-9][0-9,]*(?:\.[0-9]+)?")
        words = sorted(set(lint["absolute_words"]) | set(EXTRA_ABSOLUTE), key=len, reverse=True)
        self.abs = re.compile(r"(?<![A-Za-z0-9-])(?:" + "|".join(r"\s+".join(re.escape(p) for p in w.split()) for w in words)
                              + r")(?![A-Za-z0-9-])", re.I)
        self.banned = [(w, _wm(w, 0 if w == "may" else re.I), rep) for w, rep in lint.get("banned_words", {}).items()]
        self.ban_exc = [_wm(w) for w in lint.get("banned_word_exceptions", [])]
        self.warn = [(w, re.compile(_wm(w).pattern + (r"(?=\s*[0-9])" if w == "over" else ""), re.I), tip)
                     for w, tip in lint.get("warn_words", {}).items()]
        self.customer = [(w, _wm(w)) for w in lint.get("customer_words", [])]
        self.former = [(n, re.compile(r"(?<![A-Za-z0-9-])" + re.escape(n) + r"(?![A-Za-z0-9-])"), new)
                       for n, new in lint.get("former_names", {}).items()]
        self.former += [(rx, re.compile(rx), new) for rx, new in lint.get("former_name_regexes", {}).items()]
        self.contraction = re.compile(lint["contraction_regex"], re.I) if lint.get("contraction_regex") else None
        self.terms = terms if terms is not None else _terms()
        names = names if names is not None else _official_names()
        self.names = set()
        for t in self.terms:
            self.names.update(x for x in [t.get("term"), t.get("short")] + list(t.get("aliases", [])) if x)
        for e in names:
            self.names.update(x for x in (e.get("official_name"), e.get("short_name")) if x)
            self.names.add(re.sub(r"\s*\([^)]*\)\s*$", "", e["official_name"]))
        self.names_l = sorted({n.lower() for n in self.names}, key=len, reverse=True)
        self.digit_names = [re.compile(r"(?<![A-Za-z0-9])" + re.escape(n) + r"(?![A-Za-z0-9])", re.I)
                            for n in self.names if re.search(r"\d", n)]
        self.variants = []
        for t in self.terms:
            for v in t.get("banned", []):
                self.variants.append((v, _wm(v), t))
            for v in t.get("banned_case", []):
                self.variants.append((v, _wm(v, 0), t))
            for v in t.get("former_names", []):
                self.variants.append((v, _wm(v, 0), t))
        self.heur_units = set(sp["grounding"].get("heuristic_exempt_units", []))
        self.exam_words = [_wm(w) for w in sp["grounding"].get("exam_fact_words", [])]

    def numbers(self, text: str, stem_numbers=None) -> list:
        """Matches of a number with a unit: list of (matched text, unit or None)."""
        text = _RE_DATE.sub(lambda m: " " * len(m.group(0)), text)
        low, out, spans = text.lower(), [], []
        for rx in self.digit_names:
            spans += [m.span() for m in rx.finditer(text)]
        direct = list(self.num.finditer(text))
        taken = {m.start("num") for m in direct}
        extra = []
        for m in list(self.num_gap.finditer(text)) + list(self.num_word.finditer(text)):
            gap_words = [w.lower() for w in (m.group("gap") or "").split()]
            if m.start("num") in taken or any(w in GAP_STOP or w in self.unit_words for w in gap_words):
                continue
            if any(w.endswith("s") and not w.endswith(("ss", "ous")) for w in gap_words):
                continue                    # `Day 3 covers subnets`: a verb, not an adjective
            lead = low[:m.start("num")]
            if re.search(r"(?:step|day|chapter|version|phase|option|tier|table|figure|section|part|week|wave|lens) $", lead):
                continue
            if re.fullmatch(r"(?:19|20)\d\d", m.group("num")) and re.search(r"(?:in|since|by|until|before|after|from|of) $", lead):
                continue
            if m.re is self.num_word and re.fullmatch(_SMALL_WORD, m.group("num"), re.I):
                continue                    # a small story count in words is not matched (R2)
            taken.add(m.start("num"))
            extra.append(m)
        for m in direct + extra + list(self.cur.finditer(text)):
            start = m.start("num") if "num" in m.re.groupindex else m.start()
            digits = re.sub(r"[^0-9.]", "", m.group("num") if "num" in m.re.groupindex else m.group(0)).strip(".")
            if any(a <= start < b for a, b in spans):
                continue
            before = low[:start].rstrip()
            if before != low[:start] and any(before.endswith(n) and (len(before) == len(n) or not before[-len(n) - 1].isalnum())
                                             for n in self.names_l):
                continue
            if stem_numbers and digits in stem_numbers:
                continue
            unit = (m.groupdict().get("unit") or m.groupdict().get("noun")) if "num" in m.re.groupindex else "$"
            if (m.group(0), unit) not in out:
                out.append((m.group(0), unit))
        return out

    def absolutes(self, text: str) -> list:
        return [m.group(0) for m in self.abs.finditer(text)]

    def in_longer_name(self, text: str, start: int, end: int, variant: str) -> bool:
        low, v = text.lower(), variant.lower()
        for name in self.names_l:
            if len(name) > len(v) and v in name:
                at = low.find(name, max(0, start - len(name)))
                while 0 <= at <= start:
                    if at + len(name) >= end:
                        return True
                    at = low.find(name, at + 1)
        return False


def _split_sentences(marked: str) -> list:
    text = re.sub(r"([.!?:]?)\s*(" + NF + r"[^" + NE + r"]*" + NE + ")", r"\2\1", marked)
    return [s.strip() for s in _RE_SPLIT.split(text.replace("**", "")) if s.strip()]


def _is_question(sentence: str) -> bool:
    return _plain(sentence).rstrip(" \"')*").endswith("?")


_RE_ZERO_WIDTH = re.compile("[" + "".join(chr(c) for c in (0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF, 0xAD)) + "]")
_RE_PROSE_CODE = re.compile(r"[A-Za-z0-9 ,.'+%$-]+")
_CODE_WORDS = ("aws", "curl", "python3", "python", "saa.py", "git", "cd", "ls", "export", "echo", "jq", "sudo")


def _code_text(m) -> str:
    """Inline code is for commands and names, which the grounding rules skip. Code that reads as prose
    (`up to 9000 widgets`) is kept as text, so a hard claim cannot hide in it (gate-break H12)."""
    inner = m.group(0)[1:-1].strip()
    words = inner.split()
    if len(words) < 2 or not _RE_PROSE_CODE.fullmatch(inner) or "--" in inner or words[0] in _CODE_WORDS \
            or not re.search(r"[A-Za-z]{2}", inner):
        return " "
    return " " + inner + " "


def _inline(text: str):
    """Remove comments and command-like inline code, keep no-fact markers, encode links. Returns (marked text, links)."""
    # gate-break H10, H11: the rules read what the reader sees. Full-width digits and non-breaking spaces become
    # plain ones, zero-width characters go, and entities are decoded (after the comments are out).
    text = _RE_ZERO_WIDTH.sub("", unicodedata.normalize("NFKC", text))
    text = re.sub(r"<!--\s*no-fact:\s*(.*?)\s*-->", lambda m: NF + m.group(1) + NE, text)
    text = _RE_COMMENT.sub(" ", text)
    text = unicodedata.normalize("NFKC", html.unescape(text))
    text = _RE_ZERO_WIDTH.sub("", text)
    text = _RE_ICODE.sub(_code_text, text)
    text = _RE_IMG.sub(" ", text)
    links = []

    def repl(m):
        links.append((m.group(1), m.group(2)))
        return f"{LK}{len(links) - 1}{LM}{m.group(1)}{LE}"
    text = _RE_LINK.sub(repl, text)
    text = re.sub(r"</?(?:br|sub|sup|kbd)\s*/?>", " ", text)
    return text, links


def _ground(matcher, marked, links, grounding, where, findings, stem_numbers=None, warnings=None, stats=None):
    """L304 and L305 on one text unit; W308 for accepted no-fact markers."""
    sp = matcher.sp
    href_rx = re.compile(sp["fact_links"]["href_regex"])
    reasons = sp["grounding"].get("no_fact_reasons", [])
    exempt = set(sp["grounding"].get("exempt_sentences", []))
    for sent in _split_sentences(marked):
        plain = _plain(sent).strip()
        words = sum(1 for tok in plain.split() if _RE_ALNUM.search(tok))
        if stats is not None and words:
            stats.append((words, where))
        if grounding == "example" or not plain or plain in exempt:
            continue
        nums = matcher.numbers(plain, stem_numbers)
        if grounding == "heuristic":
            nums = [(t, u) for t, u in nums
                    if not (u in matcher.heur_units and not any(rx.search(plain) for rx in matcher.exam_words))]
            absolutes = []
        elif _is_question(sent):
            absolutes = []          # a question asks; but a number with a unit in it still tells (gate-break H12)
        else:
            absolutes = matcher.absolutes(plain)
        if not nums and not absolutes:
            continue
        if any(href_rx.match(links[int(i)][1]) for i in _RE_LINKIDX.findall(sent) if int(i) < len(links)):
            # gate-break H13: a fact link grounds the absolute words of its sentence and the numbers in its own
            # text; a number with a unit outside every fact link still needs a link
            outside = _FACT_SPAN.sub(lambda m: " " if int(m.group(1)) < len(links) and href_rx.match(links[int(m.group(1))][1])
                                     else m.group(0), sent)
            absolutes = []
            if grounding == "heuristic":
                nums = []
            else:
                nums = [n for n in matcher.numbers(_plain(outside).strip(), stem_numbers)]
            if not nums:
                continue
        marker = _RE_NOFACT.search(sent)
        what = ", ".join([f"number with a unit `{t}`" for t, _ in nums] + [f"absolute word `{a}`" for a in absolutes])
        if marker and marker.group(1) in reasons:
            if warnings is not None:
                warnings.append(_finding("W308", where.get("file"), where.get("line"),
                                         f"no-fact marker ({marker.group(1)}): {plain[:70]}", where.get("item")))
            continue
        if marker:
            what += f"; unknown no-fact reason `{marker.group(1)}`"
        code = "L305" if grounding == "heuristic" else "L304"
        findings.append(_finding(code, where.get("file"), where.get("line"), f"{what} without a fact link: {plain[:70]}", where.get("item")))


def _check_links(sp, facts, links, where, findings, stem_ok=True):
    """L301, L302, L303 for the links of one text unit. Returns the linked fact ids."""
    fl, ids = sp["fact_links"], []
    href_rx = re.compile(fl["href_regex"])
    for text, href in links:
        if "facts/" not in href or href.startswith("http"):
            continue
        m = href_rx.match(href)
        fact = facts.get(m.group(2)) if m else None
        if not m:
            findings.append(_finding("L301", where.get("file"), where.get("line"), f"fact link {href} does not match the pattern", where.get("item")))
        elif fact is None:
            findings.append(_finding("L301", where.get("file"), where.get("line"), f"fact link to unknown fact {m.group(2)}", where.get("item")))
        elif fact.get("service") != m.group(1):
            findings.append(_finding("L301", where.get("file"), where.get("line"),
                                     f"fact {m.group(2)} has service {fact.get('service')}, not {m.group(1)}", where.get("item")))
        else:
            ids.append(m.group(2))
            if fact.get("status") != fl.get("fact_status_required", "verified"):
                findings.append(_finding("L302", where.get("file"), where.get("line"),
                                         f"linked fact {m.group(2)} is {fact.get('status')}, not verified", where.get("item")))
            elif not any(holds_display(common.normalize_text(text), d) for d in _displays(fact)):
                findings.append(_finding("L303", where.get("file"), where.get("line"),
                                         f"link text `{text}` holds no value of {m.group(2)}", where.get("item")))
            else:
                extra = link_text_extra(common.normalize_text(text), _displays(fact))
                if extra:
                    findings.append(_finding("L303", where.get("file"), where.get("line"),
                                             f"link text `{text}` holds `{extra}` next to the value of {m.group(2)}; "
                                             "link only the value", where.get("item")))
    return ids


def _banned(matcher, plain, where, findings, skip_customer=False):
    """L801 on one plain text."""
    text = plain
    for rx in matcher.ban_exc:
        text = rx.sub(lambda m: " " * len(m.group(0)), text)
    customer = {w.lower() for w, _ in matcher.customer}
    for word, rx, rep in matcher.banned:
        if rx.search(text) and not (skip_customer and word.lower() in customer):
            findings.append(_finding("L801", where.get("file"), where.get("line"),
                                     f"banned word `{word}`" + (f": use `{rep}`" if rep else ""), where.get("item")))


def check_text(text: str, where, grounding: str = "strict", stem: str = None) -> list:
    """Findings L301 to L305 and L801 for one text. `where` is an item id or a dict with file, line, item."""
    where = where if isinstance(where, dict) else {"item": where}
    sp = spec()
    matcher, findings = Matcher(sp), []
    text = text or ""
    prefix = sp.get("questions", {}).get("twin_prefix")
    if prefix and text.startswith(prefix):      # the quoted phrase after the twin prefix is scenario text
        text = prefix + re.sub(r'^"[^"]*"', " ", text[len(prefix):], count=1)
    stem_numbers = None
    if stem:
        stem_numbers = {re.sub(r"[^0-9.]", "", n).strip(".") for n in re.findall(r"[0-9][0-9,]*(?:\.[0-9]+)?", stem)}
    marked, links = _inline(text)
    _check_links(sp, _load_facts(), links, where, findings)
    _ground(matcher, marked, links, grounding, where, findings, stem_numbers)
    _banned(matcher, _plain(marked), where, findings)
    return findings


def check_strict_text(text: str, where, stem: str = None) -> list:
    """TOOLS.md section 2: L301 to L305 and L801 for one JSON text field; numbers of `stem` are scenario data."""
    return check_text(text, where, "strict", stem)


# ---------------------------------------------------------------- Markdown parsing

class Block:
    __slots__ = ("kind", "line", "lines", "sec", "sub", "details", "open", "index", "extra")

    def __init__(self, kind, line, lines, **extra):
        self.kind, self.line, self.lines, self.extra = kind, line, lines, extra
        self.sec = self.sub = self.details = self.open = None
        self.index = -1

    @property
    def text(self):
        return "\n".join(self.lines)


def _fm_scalar(s: str):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    if s in ("true", "false"):
        return s == "true"
    return int(s) if re.fullmatch(r"-?\d+", s) else s


def _fm_value(s: str):
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        return [_fm_scalar(p) for p in s[1:-1].split(",") if p.strip()]
    if s.startswith("{") and s.endswith("}"):
        out = {}
        for part in s[1:-1].split(","):
            if ":" in part:
                k, v = part.split(":", 1)
                out[k.strip()] = _fm_scalar(v)
        return out
    return _fm_scalar(s)


class Doc:
    """One hand-written Markdown file, parsed line by line."""

    def __init__(self, name: str, text: str, sp: dict):
        self.name, self.raw, self.sp = name, text, sp
        self.lines = text.split("\n")
        self.fm, self.fm_errors, self.fm_lines, self.body_start = None, [], {}, 0
        self.blocks, self.headings, self.regions, self.markers, self.issues = [], [], [], [], []
        self._parse()

    def _front_matter(self):
        if not self.lines or self.lines[0].strip() != "---":
            return
        end = next((i for i in range(1, len(self.lines)) if self.lines[i].strip() == "---"), None)
        if end is None:
            self.fm_errors.append("front matter has no closing ---")
            return
        self.fm = {}
        for i in range(1, end):
            raw = self.lines[i]
            if not raw.strip():
                continue
            m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
            if not m:
                self.fm_errors.append(f"front matter line {i + 1} is not `key: value`")
                continue
            self.fm[m.group(1)] = _fm_value(m.group(2))
            self.fm_lines[m.group(1)] = i + 1
        self.body_start = end + 1

    def _add(self, block, h2, h3, details, opened):
        block.sec, block.sub, block.details, block.open = h2, h3, details, opened
        block.index = len(self.blocks)
        self.blocks.append(block)
        return block

    def _parse(self):
        sp, lines = self.sp, self.lines
        self._front_matter()
        region_kinds = set(sp["generated_regions"]["kinds"])
        i, n = self.body_start, len(lines)
        h2 = h3 = details = opened = None
        while i < n:
            line, s = lines[i], lines[i].strip()
            if not s:
                i += 1
                continue
            m = _RE_FENCE.match(line)
            if m:
                j = i + 1
                while j < n and not re.match(r"^\s*```\s*$", lines[j]):
                    j += 1
                self._add(Block("code", i + 1, lines[i + 1:j], lang=m.group(1)), h2, h3, details, opened)
                i = j + 1
                continue
            m = _RE_REGION_START.match(s)
            if m and m.group(1) in region_kinds:
                kind = m.group(1)
                j = i + 1
                while j < n and not re.match(r"^<!--\s*" + re.escape(kind) + r":end\s*-->$", lines[j].strip()):
                    j += 1
                attrs = dict(p.split("=", 1) for p in m.group(2).split() if "=" in p)
                if j >= n:
                    self.issues.append((i + 1, f"generated region {kind} has no end comment"))
                    j = i
                self.regions.append({"kind": kind, "attrs": attrs, "line": i + 1, "end": j + 1, "sec": h2, "sub": h3,
                                     "inner": lines[i + 1:j]})
                self._add(Block("region", i + 1, [], region=self.regions[-1]), h2, h3, details, opened)
                i = j + 1
                continue
            m = _RE_HEADING.match(line)
            if m:
                level, text = len(m.group(1)), m.group(2)
                title, minutes = _time_box(sp, text)
                head = {"level": level, "text": text, "title": title, "minutes": minutes, "line": i + 1,
                        "id": anchor(title), "anchor": anchor(text), "flag": None, "flag_raw": None, "pass": False,
                        "spec": None, "role": None, "parent": None, "end": n}
                if level == 2:
                    h2, h3 = head, None
                elif level == 3:
                    h3, head["parent"] = head, h2
                nxt = lines[i + 1].strip() if i + 1 < n else ""
                if nxt.startswith("<!-- section:"):
                    head["flag_raw"] = nxt
                    if level == 2:
                        fm = re.match(sp["section_flag"]["regex"], nxt)
                        if fm:
                            head["flag"] = {"role": fm.group(1), "route": fm.group(2), "minutes": int(fm.group(3)),
                                            "service": fm.group(5) if fm.re.groups >= 5 else None}
                            head["role"] = fm.group(1)
                    elif level == 3 and re.match(sp["section_flag"]["h3_regex"], nxt):
                        head["pass"] = True
                    i += 1
                self.headings.append(head)
                self._add(Block("heading", head["line"], [line], head=head), h2 if level >= 2 else None,
                          h3 if level == 3 else None, details, opened)
                i += 1
                continue
            if s.startswith("<!--"):
                j = i
                while j < n and "-->" not in lines[j]:
                    j += 1
                j = min(j, n - 1)
                raw = "\n".join(lines[i:j + 1])
                rest = _RE_COMMENT.sub("", raw).strip()
                if not rest:
                    block = self._add(Block("comment", i + 1, lines[i:j + 1]), h2, h3, details, opened)
                    self._markers(raw, i + 1, block)
                    i = j + 1
                    continue
            if s == "<details>":
                block = self._add(Block("details_open", i + 1, [line], summary=None), h2, h3, None, None)
                opened, details = block, ""
                i += 1
                continue
            m = re.match(r"^<summary>(.*)</summary>$", s)
            if m:
                details = m.group(1).strip()
                if opened is not None:
                    opened.extra["summary"] = details
                self._add(Block("summary", i + 1, [line]), h2, h3, details, opened)
                i += 1
                continue
            if s == "</details>":
                self._add(Block("details_close", i + 1, [line]), h2, h3, details, opened)
                details = opened = None
                i += 1
                continue
            if s.startswith("|"):
                j = i
                while j < n and lines[j].strip().startswith("|"):
                    j += 1
                prev = lines[i - 1].strip() if i > 0 else ""
                km = re.match(r"^<!--\s*table:\s*(\S+)\s*-->$", prev)
                block = self._add(Block("table", i + 1, lines[i:j], tkind=km.group(1) if km else None), h2, h3, details, opened)
                self._markers("\n".join(lines[i:j]), i + 1, block)
                i = j
                continue
            if s.startswith(">"):
                j = i
                while j < n and lines[j].strip().startswith(">"):
                    j += 1
                content = [re.sub(r"^\s*>\s?", "", x) for x in lines[i:j]]
                block = self._add(Block("quote", i + 1, lines[i:j], content=content), h2, h3, details, opened)
                self._markers("\n".join(lines[i:j]), i + 1, block)
                i = j
                continue
            if _RE_LIST.match(line):
                j, items = i, []
                while j < n and lines[j].strip():
                    lm = _RE_LIST.match(lines[j])
                    if lm:
                        items.append({"line": j + 1, "text": lm.group(3), "ordered": lm.group(2) is not None})
                    elif self._starts_block(lines[j]):
                        break
                    else:
                        items[-1]["text"] += " " + lines[j].strip()
                    j += 1
                block = self._add(Block("list", i + 1, lines[i:j], items=items), h2, h3, details, opened)
                for it in items:
                    self._markers(it["text"], it["line"], block)
                i = j
                continue
            j = i + 1
            while j < n and lines[j].strip() and not self._starts_block(lines[j]) and not re.match(r"^\s{0,3}[-*+]\s+", lines[j]):
                j += 1
            block = self._add(Block("para", i + 1, lines[i:j]), h2, h3, details, opened)
            self._markers("\n".join(lines[i:j]), i + 1, block)
            i = j
        for idx, head in enumerate(self.headings):
            later = [h for h in self.headings[idx + 1:] if h["level"] <= head["level"]]
            head["end"] = later[0]["line"] - 1 if later else n

    @staticmethod
    def _starts_block(line: str) -> bool:
        s = line.strip()
        return bool(_RE_HEADING.match(line) or _RE_FENCE.match(line) or s.startswith(("|", ">", "<details>", "</details>", "<summary>"))
                    or (s.startswith("<!--") and s.endswith("-->") and not _RE_COMMENT.sub("", s).strip()))

    def _markers(self, raw, line, block):
        for m in _RE_MARKER.finditer(raw):
            self.markers.append({"kind": m.group(1), "value": (m.group(2) or "").strip(),
                                 "line": line + raw[:m.start()].count("\n"), "block": block})

    def section_text(self, head) -> str:
        return "\n".join(self.lines[head["line"]:head["end"]])

    def h2(self) -> list:
        return [h for h in self.headings if h["level"] == 2]

    def h3(self, parent) -> list:
        return [h for h in self.headings if h["level"] == 3 and h["parent"] is parent]

    def inner(self, opened) -> list:
        return [b for b in self.blocks if b.open is opened and b.kind not in ("summary", "details_close")]


def _split_row(line: str) -> list:
    s = line.strip()
    s = s[1:] if s.startswith("|") else s
    s = s[:-1] if s.endswith("|") and not s.endswith("\\|") else s
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def _table(block):
    rows = [_split_row(x) for x in block.lines]
    body = rows[2:] if len(rows) > 1 and all(re.fullmatch(r":?-{2,}:?", c or "--") for c in rows[1]) else rows[1:]
    return rows[0], body


def _label(block):
    """The bold label at the start of a paragraph, or None."""
    m = _RE_BOLD_START.match(block.lines[0].strip()) if block.kind == "para" else None
    return m.group(1) if m else None


def _prompt_patterns(sp) -> list:
    out = []
    for label, cfg in sp["prompts"]["labels"].items():
        rx = re.compile("^" + r"(\d+)".join(re.escape(p) for p in label.split("<n>")) + "$")
        out.append((label, rx, cfg))
    return out


def _prompt_of(patterns, label):
    for name, rx, cfg in patterns:
        m = rx.match(label or "")
        if m:
            return name, cfg, (int(m.group(1)) if m.groups() else None)
    return None


def _callout(block):
    """(label, first-line text after the label) of a callout blockquote, else None."""
    m = re.match(r"^\*\*([^*:]+):\*\*\s*(.*)$", block.extra["content"][0].strip()) if block.kind == "quote" else None
    return (m.group(1), m.group(2)) if m else None


def _is_aws_quote(block) -> bool:
    return block.kind == "quote" and block.extra["content"][0].lstrip().startswith('"')


# ---------------------------------------------------------------- the chapter lint

class Ctx:
    def __init__(self, entry, draft=False, strict=False, strict_all=False):
        self.entry, self.draft, self.strict, self.strict_all = entry, draft, strict, strict_all
        self.sp = spec()
        self.tpl = template(entry)
        self.cid, self.slug = entry["id"], entry["slug"]
        self.dirname = f"{self.cid}-{self.slug}"
        self.dir = common.BOOK / self.dirname
        self.facts = _load_facts()
        self.terms = _terms()
        self.official = _official_names()
        self.matcher = Matcher(self.sp, self.terms, self.official)
        self.prompts = _prompt_patterns(self.sp)
        self.docs, self.errors, self.warnings = {}, [], []
        self.stats, self.inputs, self.callouts, self.embeds = [], set(), 0, []
        self.fact_links = 0
        self.other_docs, self.trap_ids, self.sheets = {}, {}, {}

    def add(self, code, name, line, msg, d=False, warn=False):
        f = _finding(code, f"{self.dirname}/{name}" if name else None, line, msg)
        (self.warnings if code.startswith("W") or warn or (d and self.draft) else self.errors).append(f)

    def where(self, doc, line):
        return {"file": f"{self.dirname}/{doc.name}", "line": line}

    def status(self, doc) -> str:
        return "ready" if self.strict else str((doc.fm or {}).get("status", "draft"))

    def grounding(self, role) -> str:
        return self.sp["roles"].get(role, {}).get("grounding", "strict")


def _hand_specs(ctx) -> list:
    out = []
    for fs in ctx.tpl["files"]:
        if fs.get("source") != "hand":
            continue
        required = bool(fs.get("required"))
        if fs.get("present_when"):
            required = bool(ctx.entry.get("cards"))
        out.append((fs, required))
    return out


def _words_limits(ctx, words) -> tuple:
    words = words or {}
    if "by_tier" in words:
        words = words["by_tier"].get(ctx.entry.get("tier"), {})
    hi = words.get("xl_max") if ctx.entry.get("xl") and "xl_max" in words else words.get("max")
    return words.get("min", 0), hi


def lint_chapter(ch, draft=False, strict=False, only_file=None, strict_all=False) -> dict:
    ctx = Ctx(_entry(ch), draft, strict, strict_all)
    sp = ctx.sp
    for path in (common.STYLE_DIR / "SPEC.json", common.DATA / "book.json", common.DATA / "terms.json"):
        ctx.inputs.add(path)
    words = {}
    # L101: files
    for fs, required in _hand_specs(ctx):
        path = ctx.dir / fs["name"]
        if not path.exists():
            if required:
                ctx.add("L101", fs["name"], None, f"required file {fs['name']} is missing")
            continue
        ctx.inputs.add(path)
        doc = Doc(fs["name"], path.read_text(encoding="utf-8"), sp)
        doc.fs = fs
        ctx.docs[fs["name"]] = doc
    marker_line = sp["generated_regions"]["generated_file_first_line"]
    # gate-break H12: every Markdown file in the chapter folder is reader-facing; one that the template does not
    # list is read by no rule
    listed = {fs["name"] for fs in ctx.tpl["files"]}
    if ctx.dir.is_dir():
        for path in sorted(ctx.dir.glob("*.md")):
            if path.name not in listed:
                ctx.add("L101", path.name, None, f"file {path.name} is not in the template of this chapter; no rule reads it", d=True)
    for fs in ctx.tpl["files"]:
        if fs.get("source") != "generated":
            continue
        path = ctx.dir / fs["name"]
        if not path.exists():
            needed = fs.get("required") or (fs["name"] == "3-do.md" and (common.DATA / ctx.dirname / "tasks.json").exists())
            if needed:
                ctx.add("L101", fs["name"], None, f"generated file {fs['name']} is missing: run sync", d=True)
        else:
            with open(path, encoding="utf-8") as f:
                first = f.readline().rstrip("\n")
            if first != marker_line:
                ctx.add("L101", fs["name"], 1, "generated file does not start with the marker line", d=True)
    for doc in ctx.docs.values():
        limited = bool(doc.fs.get("reader_editable")) and ctx.status(doc) == "ready"
        _front_matter(ctx, doc)
        _headings(ctx, doc)
        _tables(ctx, doc, headers_only=limited)
        if limited:
            continue
        _diagrams(ctx, doc)
        _devices(ctx, doc)
        _text_rules(ctx, doc)
        _links_and_ids(ctx, doc)
        _code(ctx, doc)
        _markers(ctx, doc)
        n = word_count(doc.raw)
        words[doc.name] = n
        lo, hi = _words_limits(ctx, doc.fs.get("words"))
        if n < lo or (hi is not None and n > hi):
            severity = sp["lint"].get("file_word_limit_severity", "error")
            ctx.add("L201" if severity == "error" else "W201", doc.name, None,
                    f"{n} words; the file allows {lo} to {hi}")
        for text in doc.fs.get("required_text", []):
            if text not in doc.raw:
                ctx.add("L904", doc.name, None, f"required text `{text}` is missing")
    minutes = _chapter_rules(ctx)
    total = sum(w for w, _ in ctx.stats)
    average = round(total / len(ctx.stats), 1) if ctx.stats else 0
    if ctx.stats and average > sp["lint"]["sentence"]["average_words_max"]:
        ctx.add("W202", None, None, f"average sentence length {average} is over {sp['lint']['sentence']['average_words_max']}")
    errors, warnings = ctx.errors, ctx.warnings
    if only_file:
        errors = [f for f in errors if f["file"] and f["file"].endswith("/" + only_file)]
        warnings = [f for f in warnings if f["file"] and f["file"].endswith("/" + only_file)]
    key = lambda f: (f["file"] or "", f["line"] or 0, f["code"])
    return {"chapter": ctx.cid, "ok": not errors, "errors": sorted(errors, key=key), "warnings": sorted(warnings, key=key),
            "counts": {"words": words, "sentence_average": average, "fact_links": ctx.fact_links, "callouts": ctx.callouts,
                       "minutes": minutes},
            "_inputs": ctx.inputs, "_embeds": ctx.embeds}


def _front_matter(ctx, doc):
    sp, fmr, entry = ctx.sp, ctx.sp["front_matter"], ctx.entry
    for msg in doc.fm_errors:
        ctx.add("L102", doc.name, 1, msg)
    if doc.fm is None:
        ctx.add("L102", doc.name, 1, "no front matter")
        doc.fm = {}
        return
    fm, chapter_file = doc.fm, doc.name == fmr["chapter_file"]
    keys = fmr["chapter_keys"] if chapter_file else fmr["other_keys"]
    for key in keys["required"]:
        if key not in fm:
            ctx.add("L102", doc.name, 1, f"front matter key `{key}` is missing")
    if chapter_file:
        for key in ("id", "slug", "title", "tier", "services", "kind", "xl"):
            if key in fm or key in entry:
                have, want = fm.get(key), entry.get(key)
                if key == "xl":
                    have, want = bool(have), bool(want)
                if have != want:
                    ctx.add("L102", doc.name, doc.fm_lines.get(key, 1), f"front matter `{key}` is {have!r}; the registry has {want!r}")
        allowed = [str(t) for t in entry.get("tasks", [])]
        for task in fm.get("tasks", []) if isinstance(fm.get("tasks"), list) else []:
            if allowed and str(task) not in allowed:
                ctx.add("L102", doc.name, doc.fm_lines.get("tasks", 1), f"task {task} is not a task of the registry entry")
        mins = fm.get("minutes")
        if "minutes" in fm and (not isinstance(mins, dict) or any(not isinstance(mins.get(k), int) for k in keys.get("minutes_keys", []))):
            ctx.add("L102", doc.name, doc.fm_lines.get("minutes", 1), "front matter `minutes` needs whole numbers for " + ", ".join(keys.get("minutes_keys", [])))
    elif "chapter" in fm and str(fm["chapter"]) != ctx.cid:
        ctx.add("L102", doc.name, doc.fm_lines.get("chapter", 1), f"front matter `chapter` is {fm['chapter']!r}, not {ctx.cid!r}")
    want_file = fmr["file_values"].get(doc.name)
    if "file" in fm and want_file and fm["file"] != want_file:
        ctx.add("L102", doc.name, doc.fm_lines.get("file", 1), f"front matter `file` must be {want_file}")
    if "status" in fm and fm["status"] not in sp["statuses"]["chapter"]:
        ctx.add("L102", doc.name, doc.fm_lines.get("status", 1), f"unknown status {fm['status']!r}")


def _card_keys(ctx) -> list:
    return list(ctx.entry.get("cards") or (ctx.entry.get("services", []) if ctx.tpl["key"] == "light" else []))


def _headings(ctx, doc):
    sp, hs, fs = ctx.sp, ctx.sp["headings"], doc.fs
    h1 = [h for h in doc.headings if h["level"] == 1]
    if len(h1) != 1:
        ctx.add("L103", doc.name, h1[1]["line"] if len(h1) > 1 else None, f"{len(h1)} H1 headings; exactly one is needed")
    elif hs.get("h1") and sp["front_matter"].get("h1_equals_title") and "title" in doc.fm and h1[0]["text"] != str(doc.fm["title"]):
        ctx.add("L103", doc.name, h1[0]["line"], "the H1 differs from the front matter title")
    rx = re.compile(hs["h2_h3_regex"])
    for h in doc.headings:
        if h["level"] > hs.get("max_level", 3):
            ctx.add("L103", doc.name, h["line"], f"heading below H{hs.get('max_level', 3)}")
        elif h["level"] in (2, 3) and not rx.match(h["text"]):
            ctx.add("L103", doc.name, h["line"], f"heading text `{h['text']}` has characters that a heading cannot hold")
    specs, h2s = fs.get("sections", []), doc.h2()
    repeat = fs.get("sections_mode") == "repeat" and specs
    if repeat:
        card = specs[0]
        for h in h2s:
            h["spec"] = card
        count = card.get("repeat")
        if isinstance(count, int):
            if len(h2s) != count:
                ctx.add("L104", doc.name, None, f"{len(h2s)} sections; the file needs {count}")
        else:
            keys, seen = _card_keys(ctx), {}
            names = {}
            for e in ctx.official:
                for k in e.get("keys", []):
                    names.setdefault(k, []).append(common.slugify(re.sub(r"\s*\([^)]*\)\s*$", "", e["official_name"])))
            for h in h2s:
                service = (h["flag"] or {}).get("service")
                if not service or service not in keys:
                    ctx.add("L104", doc.name, h["line"], f"service card `{h['title']}`: service={service} is not a card key of the chapter")
                    continue
                if service in seen:
                    ctx.add("L104", doc.name, h["line"], f"second service card for {service}")
                seen[service] = h
                if names.get(service) and common.slugify(h["title"]) not in names[service]:
                    ctx.add("L104", doc.name, h["line"], f"heading `{h['title']}` is not the official name of {service}")
            for k in keys:
                if k not in seen:
                    ctx.add("L104", doc.name, None, f"missing required section: the service card of {k}")
    elif specs:
        by_heading = {s["heading"]: (i, s) for i, s in enumerate(specs)}
        last, found = -1, set()
        for h in h2s:
            hit = by_heading.get(h["title"])
            if hit is None:
                ctx.add("L104", doc.name, h["line"], f"H2 `{h['title']}` is not a section of this file")
                continue
            idx, h["spec"] = hit
            if idx in found:
                ctx.add("L104", doc.name, h["line"], f"section `{h['title']}` appears twice")
            elif idx < last:
                ctx.add("L104", doc.name, h["line"], f"section `{h['title']}` is out of order")
            found.add(idx)
            last = max(last, idx)
        for i, s in enumerate(specs):
            if s.get("required") and i not in found:
                ctx.add("L104", doc.name, None, f"missing required section `{s['heading']}`")
    # L105: flags and time boxes
    flag = sp["section_flag"]
    for h in h2s:
        s = h["spec"] or {}
        if h["minutes"] is None:
            ctx.add("L105", doc.name, h["line"], f"H2 `{h['title']}` has no time box")
        if h["flag"] is None:
            ctx.add("L105", doc.name, h["line"] + 1, "the section flag is missing on the line after the H2, or does not match the pattern")
            h["role"] = s.get("role")
            continue
        if h["line"] + 1 < len(doc.lines) and doc.lines[h["line"] + 1].strip():
            ctx.add("L105", doc.name, h["line"] + 2, "a blank line must follow the section flag")
        if s.get("role") and h["flag"]["role"] != s["role"]:
            ctx.add("L105", doc.name, h["line"] + 1, f"flag role is {h['flag']['role']}; the section has role {s['role']}")
        if s.get("route") and h["flag"]["route"] != s["route"]:
            ctx.add("L105", doc.name, h["line"] + 1, f"flag route is {h['flag']['route']}; the section has route {s['route']}")
        if flag.get("minutes_must_equal_heading_time_box") and h["minutes"] is not None and h["flag"]["minutes"] != h["minutes"]:
            ctx.add("L105", doc.name, h["line"] + 1, f"flag minutes={h['flag']['minutes']} differs from the heading time box {h['minutes']}")
        h["role"] = s.get("role") or h["flag"]["role"]
        subs = doc.h3(h)
        needs_box = h["role"] == "how" or "subsections" in s.get("counts", {})
        for sub in subs:
            sub["role"] = h["role"]
            if sub["flag_raw"] and not sub["pass"]:
                ctx.add("L105", doc.name, sub["line"] + 1, "an H3 flag must be exactly " + flag["h3_syntax"])
            if needs_box and sub["minutes"] is None:
                ctx.add("L105", doc.name, sub["line"], f"H3 `{sub['title']}` has no time box")
        if needs_box and h["role"] == "how" and flag.get("how_minutes_equal_sum_of_h3_time_boxes") and subs \
                and all(x["minutes"] is not None for x in subs) and h["minutes"] is not None \
                and sum(x["minutes"] for x in subs) != h["minutes"]:
            ctx.add("L105", doc.name, h["line"], f"the H3 time boxes add up to {sum(x['minutes'] for x in subs)}, not {h['minutes']}")
    if doc.name == sp["front_matter"]["chapter_file"] and flag.get("fast_minutes_equal_sum_of_h2_time_boxes"):
        fast = (doc.fm.get("minutes") or {}).get("fast") if isinstance(doc.fm.get("minutes"), dict) else None
        total = sum(h["minutes"] or 0 for h in h2s)
        if isinstance(fast, int) and fast != total:
            ctx.add("L105", doc.name, doc.fm_lines.get("minutes", 1), f"the H2 time boxes add up to {total}; front matter minutes.fast is {fast}")


def _tables(ctx, doc, headers_only=False):
    sp, tb = ctx.sp, ctx.sp["tables"]
    for b in doc.blocks:
        if b.kind != "table":
            continue
        kind = b.extra["tkind"]
        if kind is None or kind not in tb["kinds"]:
            ctx.add("L501", doc.name, b.line, "table without a kind comment on the line before it" if kind is None else f"unknown table kind `{kind}`")
            continue
        ks = tb["kinds"][kind]
        header, body = _table(b)
        b.extra["header"], b.extra["body"] = header, body
        ok = True
        if ks.get("headers"):
            ok = header == ks["headers"]
        elif ks.get("allowed_headers"):
            ok = header in ks["allowed_headers"]
        elif ks.get("first_header"):
            ok = bool(header) and header[0] == ks["first_header"]
        if not ok:
            ctx.add("L502", doc.name, b.line, f"wrong headers for a `{kind}` table")
        cols = ks.get("columns", {})
        file_max = doc.fs.get("table_columns_max") or tb["columns_max"].get(doc.name, tb["columns_max"].get("other", 99))
        if not _in_range(len(header), cols) or len(header) > file_max:
            ctx.add("L502", doc.name, b.line, f"{len(header)} columns; a `{kind}` table in this file allows up to {min(file_max, cols.get('max', file_max))}")
        if headers_only:
            continue
        if len(body) > ks.get("rows_max", tb["rows_max"]):
            ctx.add("L502", doc.name, b.line, f"{len(body)} rows; one `{kind}` table allows {ks.get('rows_max', tb['rows_max'])}")
        cell_max = ks.get("cell_words_max", tb["cell_words_max"])
        for r, row in enumerate(body):
            line = b.line + 2 + r
            if len(row) != len(header):
                ctx.add("L502", doc.name, line, f"the row has {len(row)} cells; the header has {len(header)}")
            for cell in row:
                if word_count(cell) > cell_max:
                    ctx.add("L202", doc.name, line, f"table cell over {cell_max} words")
            if kind == "signals" and row:
                if ks.get("first_column_quoted") and not (row[0].startswith('"') and row[0].endswith('"') and len(row[0]) > 2):
                    ctx.add("L503", doc.name, line, "column 1 of a signals table is a stem phrase in straight double quotes")
                if len(row) > 3 and not row[3]:
                    ctx.add("L503", doc.name, line, "the `But not if` cell is empty")
            if kind == "words" and len(row) > 1:
                name = re.sub(r"\s+", " ", re.sub(r"\([^)]*\)", "", row[0])).strip().lower()
                if ks.get("terms_must_exist") and name not in {t["term"].lower() for t in ctx.terms}:
                    ctx.add("L503", doc.name, line, f"`{name}` is not a term of data/terms.json", d=True)
                col = ks.get("one_bold_span_in_column", 1)
                if len(row) > col and len(re.findall(r"\*\*[^*]+\*\*", row[col])) != 1:
                    ctx.add("L503", doc.name, line, "the collocation cell needs exactly one bold span")
            if kind == "numbers" and row and ks.get("first_column_is_fact_link"):
                links = _RE_LINK.findall(row[0])
                if not links or not re.match(sp["fact_links"]["href_regex"], links[0][1]):
                    ctx.add("L503", doc.name, line, "column 1 of a numbers table is a fact link")
        follow = (ks.get("followed_by_in_role") or {}).get((b.sec or {}).get("role")) or ks.get("followed_by")
        if follow:
            nxt = doc.blocks[b.index + 1] if b.index + 1 < len(doc.blocks) else None
            if nxt is None or nxt.kind != "para" or not nxt.lines[0].strip().startswith(follow):
                ctx.add("L503", doc.name, b.line, f"a `{kind}` table is followed by {follow}")


def _section_blocks(doc, head) -> list:
    key = "sub" if head["level"] == 3 else "sec"
    return [b for b in doc.blocks if getattr(b, key) is head and b.kind != "heading"]


def _count(ctx, doc, head, name, n, want):
    if not _in_range(n, want):
        ctx.add("L106", doc.name, head["line"], f"`{head['title']}`: {n} {name.replace('_', ' ')}; the section needs {_range_text(want)}")


def _devices(ctx, doc):
    """L106, L107, L202 (blocks), L401, L402 (count), W201, W203."""
    sp, pr, hs = ctx.sp, ctx.sp["prompts"], ctx.sp["headings"]
    labels = {c["label"]: c for c in sp["callouts"]["labels"]}
    qmark = pr.get("question_must_end_with", "?")
    callouts, go_deeper, spot = [], 0, 0
    # reveals
    for b in doc.blocks:
        if b.kind == "details_open":
            summary = b.extra.get("summary")
            nxt = doc.blocks[b.index + 1] if b.index + 1 < len(doc.blocks) else None
            det = sp["details"]
            if nxt is None or nxt.kind != "summary" or nxt.line != b.line + 1:
                ctx.add("L107", doc.name, b.line, "<details> is followed by a <summary> line")
                continue
            if summary not in det["allowed_summaries"] and not any(summary.startswith(p) and len(summary) > len(p) for p in det["allowed_summary_prefixes"]):
                ctx.add("L107", doc.name, nxt.line, f"reveal summary `{summary}` is not allowed")
            if det.get("blank_line_after_summary") and nxt.line < len(doc.lines) and doc.lines[nxt.line].strip():
                ctx.add("L107", doc.name, nxt.line, "a blank line must follow the <summary> line")
            if any(summary.startswith(p) for p in det["allowed_summary_prefixes"]):
                go_deeper += 1
                n = sum(word_count(x.text) for x in doc.inner(b))
                if n > det["go_deeper_words_max"]:
                    ctx.add("L202", doc.name, b.line, f"Go deeper block has {n} words; the limit is {det['go_deeper_words_max']}")
        elif b.kind == "details_close":
            if b.open is None:
                ctx.add("L107", doc.name, b.line, "</details> without <details>")
            elif sp["details"].get("blank_line_before_close") and doc.lines[b.line - 2].strip():
                ctx.add("L107", doc.name, b.line, "a blank line must stand before </details>")
        elif b.kind == "summary" and b.open is None:
            ctx.add("L107", doc.name, b.line, "<summary> outside <details>")
    if any(b.open is not None for b in doc.blocks[-1:]) and doc.blocks[-1].kind != "details_close":
        ctx.add("L107", doc.name, doc.blocks[-1].line, "<details> is not closed")
    # prompts
    prompts = []
    for b in doc.blocks:
        hit = _prompt_of(ctx.prompts, _label(b)) if b.kind == "para" else None
        if not hit:
            continue
        name, cfg, num = hit
        b.extra["prompt"] = (name, num)
        prompts.append(b)
        role = (b.sec or {}).get("role")
        if role not in cfg.get("in_roles", []):
            ctx.add("L107", doc.name, b.line, f"prompt `{_label(b)}` is not allowed in a section with role {role}")
        text = _RE_COMMENT.sub("", b.text).strip()
        if not text.endswith(qmark):
            ctx.add("L107", doc.name, b.line, f"prompt `{_label(b)}` does not end with {qmark}")
        nxt = doc.blocks[b.index + 1] if b.index + 1 < len(doc.blocks) else None
        if nxt is not None and nxt.kind == "code" and name == "Spot the bug.":
            nxt = doc.blocks[nxt.index + 1] if nxt.index + 1 < len(doc.blocks) else None
        answer = cfg.get("answer", "none")
        if answer.startswith("details:"):
            want = answer[len("details:"):].split(" with ")[0]
            if nxt is None or nxt.kind != "details_open" or nxt.extra.get("summary") != want:
                ctx.add("L107", doc.name, b.line, f"prompt `{_label(b)}` needs a reveal `{want}` directly after it")
            elif " with one AWS quote block" in answer and sum(1 for x in doc.inner(nxt) if _is_aws_quote(x)) != 1:
                ctx.add("L107", doc.name, b.line, f"the answer of `{_label(b)}` needs exactly one AWS quote block")
            b.extra["reveal"] = nxt if nxt is not None and nxt.kind == "details_open" else None
        elif nxt is not None and nxt.kind == "details_open":
            ctx.add("L107", doc.name, b.line, f"prompt `{_label(b)}` has no answer here")
        spot += name == "Spot the bug."
    # callouts
    say_max = sp["callouts"].get("say_it_words_max")
    for b in doc.blocks:
        if b.kind != "quote" or _is_aws_quote(b):
            continue
        co = _callout(b)
        if co is None or co[0] not in labels:
            ctx.add("L401", doc.name, b.line, f"unknown callout label `{co[0]}`" if co else "a blockquote is a callout with a label or an AWS quote block")
            continue
        label = co[0]
        b.extra["label"] = label
        callouts.append(b)
        if not labels[label].get("hand", True):
            ctx.add("L401", doc.name, b.line, f"callout `{label}` is generated only")
        n = word_count("\n".join(b.extra["content"])) - word_count(label)
        limit = say_max if label == "Say it" and say_max else sp["callouts"]["words_max"]
        if n > limit:
            ctx.add("L202", doc.name, b.line, f"`{label}` callout has {n} words; the limit is {limit}")
        if label == "Changed recently":
            _changed_entry(ctx, doc, b)
    counted = [b for b in callouts if b.extra["label"] not in sp["callouts"].get("not_counted_toward_callouts_max", [])]
    ctx.callouts += len(counted)
    if doc.fs.get("callouts_max") is not None and len(counted) > doc.fs["callouts_max"]:
        ctx.add("L402", doc.name, None, f"{len(counted)} callouts; the file allows {doc.fs['callouts_max']}")
    for key, n in (("spot_the_bug", spot), ("go_deeper", go_deeper)):
        want = doc.fs.get("counts", {}).get(key)
        if want is not None and want != {} and not _in_range(n, want):
            ctx.add("L106", doc.name, None, f"{n} {key.replace('_', ' ')} in the file; it needs {_range_text(want)}")
    # sections
    for h in doc.h2():
        s = h["spec"]
        if not s:
            continue
        blocks, counts, role = _section_blocks(doc, h), s.get("counts", {}), h["role"]
        own = [b for b in blocks if b.kind == "para" and "prompt" in b.extra]
        tables = [b for b in blocks if b.kind == "table" and "body" in b.extra]
        rows = lambda kind: sum(len(t.extra["body"]) for t in tables if t.extra["tkind"] == kind)
        quotes = [b for b in blocks if b.kind == "quote"]
        cl = lambda label: sum(1 for b in quotes if b.extra.get("label") == label)
        markers = [m for m in doc.markers if m["block"].sec is h]
        regions = [r for r in doc.regions if r["sec"] is h]
        subs = doc.h3(h)
        hero = [e for e in ctx.embeds if e["doc"] is doc and e["block"].sec is h and e["id"] == f"{ctx.slug}-hero"]
        for key, want in counts.items():
            if want == {}:
                continue
            if key == "prompts":
                mine = [b.extra["prompt"] for b in own if role in sp["prompts"]["labels"][b.extra["prompt"][0]].get("in_roles", [])
                        and b.extra["prompt"][1] is not None]
                nums = [n for _, n in mine]
                _count(ctx, doc, h, "prompts", len(nums), want)
                if nums != list(range(1, len(nums) + 1)):
                    ctx.add("L106", doc.name, h["line"], f"`{h['title']}`: prompts are not numbered 1 to {len(nums)} without a gap")
            elif key == "gist_traps":
                _count(ctx, doc, h, key, sum(1 for m in markers if m["kind"] == "gist-trap"), want)
            elif key == "task_regions":
                _count(ctx, doc, h, key, sum(1 for r in regions if r["kind"] == "task"), want)
            elif key == "plan_regions":
                _count(ctx, doc, h, key, sum(1 for r in regions if r["kind"] == "plan"), want)
            elif key == "exam_english_regions_per_subsection":
                for sub in subs:
                    _count(ctx, doc, sub, key, sum(1 for r in regions if r["kind"] == "exam-english" and r["sub"] is sub), want)
            elif key == "say_it":
                _count(ctx, doc, h, key, cl("Say it"), want)
            elif key == "startup_examples":
                _count(ctx, doc, h, key, cl("Startup example"), want)
            elif key == "hero_diagrams":
                pass        # L704, in _diagrams
            elif key == "hero_steps":
                if hero:
                    _count(ctx, doc, h, key, len(hero[0]["steps"]), want)
            elif key in ("rows", "signal_rows", "pairs_rows", "matrix_rows", "glance_rows", "services_rows"):
                kind = {"rows": "words", "signal_rows": "signals"}.get(key, key[:-5])
                _count(ctx, doc, h, key, rows(kind), want)
            elif key == "plan_rows":
                plan = next((p for p in (common.read_json(common.DATA / "plan.json") or {}).get("plans", []) if p.get("id") == s.get("plan")), None)
                if plan is not None:
                    _count(ctx, doc, h, key, len(plan.get("days", [])), want)
            elif key in ("a_list_rows", "b_list_rows"):
                name = "A-list" if key == "a_list_rows" else "B-list"
                has_h3 = any(x["title"] in ("A-list", "B-list") for x in subs)
                n = sum(len(t.extra["body"]) for t in tables if t.extra["tkind"] == "numbers"
                        and ((t.sub or {}).get("title") == name if has_h3 else name == "A-list"))
                _count(ctx, doc, h, key, n, want)
            elif key == "compare_tables":
                _count(ctx, doc, h, key, sum(1 for t in tables if t.extra["tkind"] == "compare"), want)
            elif key == "log_tables":
                _count(ctx, doc, h, key, sum(1 for t in tables if t.extra["tkind"] == "log"), want)
            elif key == "traps":
                _count(ctx, doc, h, key, sum(1 for m in markers if m["kind"] == "trap" and m["block"].kind == "list"), want)
            elif key == "trap_refs":
                _count(ctx, doc, h, key, sum(1 for m in markers if m["kind"] == "trap-ref"), want)
            elif key == "entries":
                n = cl("Changed recently")
                _count(ctx, doc, h, key, n, want)
                exempt = sp["grounding"].get("exempt_sentences", [])
                if n == 0 and exempt and not any(e in doc.section_text(h) for e in exempt):
                    ctx.add("L106", doc.name, h["line"], f"`{h['title']}` has no entry and needs the sentence: {exempt[0]}")
            elif key == "items":
                _count(ctx, doc, h, key, sum(1 for b in own if b.extra["prompt"][0] == "FAQ <n>."), want)
            elif key == "quotes":
                _count(ctx, doc, h, key, sum(1 for b in quotes if _is_aws_quote(b)), want)
            elif key == "options":
                n = 0
                for b in blocks:
                    if b.kind == "para" and _label(b) == "Options.":
                        nxt = doc.blocks[b.index + 1] if b.index + 1 < len(doc.blocks) else None
                        n = len(nxt.extra["items"]) if nxt is not None and nxt.kind == "list" else 0
                _count(ctx, doc, h, key, n, want)
            elif key == "cause_codes":
                bold = set(re.findall(r"\*\*([A-Z])\*\*", doc.section_text(h)))
                _count(ctx, doc, h, key, len(bold & set(sp["lint"].get("cause_codes", {}))), want)
            elif key == "subsections":
                _count(ctx, doc, h, key, len(subs), want)
            elif key == "stop_and_answer_per_subsection":
                for sub in subs:
                    sb = [b for b in _section_blocks(doc, sub) if b.kind != "comment"]
                    stops = [b for b in sb if b.kind == "para" and b.extra.get("prompt", ("",))[0] == "Stop and answer."]
                    _count(ctx, doc, sub, "Stop and answer prompts", len(stops), want)
                    if stops and sb and not (sb[-1].kind == "details_close" and sb[-1].open is stops[-1].extra.get("reveal")):
                        ctx.add("L106", doc.name, stops[-1].line, "Stop and answer and its reveal are the last blocks of the subsection")
        # fixed H3, heading lengths, pass-route marks
        for fixed in hs.get("fixed_h3", {}).get(s.get("key"), []):
            if fixed not in hs.get("fixed_h3_optional", []) and not any(x["title"] == fixed for x in subs):
                ctx.add("L106", doc.name, h["line"], f"`{h['title']}` needs the H3 `{fixed}`")
        if role == "how" or "subsection_heading_words" in s:
            want = s.get("subsection_heading_words") if s.get("assertion_headings") is False else hs.get("assertion_heading_words")
            for sub in subs:
                if want and not _in_range(len(sub["title"].split()), want):
                    ctx.add("L106", doc.name, sub["line"], f"H3 `{sub['title']}` has {len(sub['title'].split())} words; it needs {_range_text(want)}")
        if role == "how" and subs:
            want, n = sp["section_flag"].get("h3_pass_route_subsections"), sum(1 for x in subs if x["pass"])
            if want and not _in_range(n, want):
                ctx.add("L106", doc.name, h["line"], f"{n} subsections marked route=pass; the section needs {_range_text(want)}")
        # sentence limits of devices
        dv = sp.get("devices", {})
        plain_paras = [b for b in blocks if b.kind == "para" and b.details is None and "prompt" not in b.extra]
        if s.get("key") == "look" and dv.get("look_first_sentences_max"):
            n = sum(len(_split_sentences(_inline(b.text)[0])) for b in plain_paras)
            if n > dv["look_first_sentences_max"]:
                ctx.add("L106", doc.name, h["line"], f"`{h['title']}` has {n} sentences; the limit is {dv['look_first_sentences_max']}")
        if role == "realworld":
            first = plain_paras[0] if plain_paras else None
            rx = sp["bold_fields"].get("realworld_first_paragraph_regex")
            if first is None or (rx and not re.match(rx, first.lines[0].strip())):
                ctx.add("L107", doc.name, first.line if first else h["line"], "the case box starts with the company and the year in bold")
            elif dv.get("realworld_intro_sentences_max"):
                n = len(_split_sentences(_inline(_RE_BOLD_START.sub("", first.text.strip()))[0]))
                if n > dv["realworld_intro_sentences_max"]:
                    ctx.add("L106", doc.name, first.line, f"the case box intro has {n} sentences; the limit is {dv['realworld_intro_sentences_max']}")
            for b in quotes:
                if b.extra.get("label") == "Say it" and dv.get("realworld_say_it_sentences"):
                    n = len(_split_sentences(_inline(_callout(b)[1] + " " + " ".join(b.extra["content"][1:]))[0]))
                    if n != dv["realworld_say_it_sentences"]:
                        ctx.add("L106", doc.name, b.line, f"the Say it of a case box has {dv['realworld_say_it_sentences']} sentences")
        # bold fields, present and in order
        _bold_fields(ctx, doc, h, s, blocks, subs)
        # words
        lo, hi = _words_limits(ctx, s.get("words"))
        n = word_count(doc.section_text(h))
        if n < lo or (hi is not None and n > hi):
            severity = sp["lint"].get("section_word_limit_severity", "warn")
            ctx.add("W201" if severity != "error" else "L201", doc.name, h["line"], f"`{h['title']}` has {n} words; the section allows {lo} to {hi}")
        want = counts.get("subsection_words")
        interval = sp["lint"].get("stop_and_answer_interval_words", {}).get("max")
        for sub in subs:
            body = [b for b in _section_blocks(doc, sub) if b.details is None and "prompt" not in b.extra
                    and b.kind in ("para", "list", "table", "quote")]
            n = sum(word_count(b.text) for b in body)
            if want and not _in_range(n, want):
                ctx.add("W201", doc.name, sub["line"], f"`{sub['title']}` has {n} words; a subsection needs {_range_text(want)}")
            if role == "how" and interval and n > interval:
                ctx.add("W203", doc.name, sub["line"], f"{n} words before the Stop and answer; the limit is {interval}")
    # traps list items: Wrong belief then Truth
    wrong, truth = (ctx.sp["bold_fields"].get("traps") or ["Wrong belief:", "Truth:"])[:2]
    for m in doc.markers:
        if m["kind"] == "trap" and m["block"].kind == "list":
            item = next((it for it in m["block"].extra["items"] if it["line"] == m["line"]), None)
            if item and not re.search(re.escape(f"**{wrong}**") + r".+" + re.escape(f"**{truth}**"), item["text"]):
                ctx.add("L107", doc.name, m["line"], f"a trap is `**{wrong}** ... **{truth}** ...`")


def _bold_fields(ctx, doc, h, s, blocks, subs):
    bf, key, role = ctx.sp["bold_fields"], s.get("key"), h["role"]

    def check(scope_blocks, fields, required, where_line, name):
        found = [(_label(b), b.line) for b in scope_blocks if b.kind == "para" and _label(b) in fields]
        order = [fields.index(lbl) for lbl, _ in found]
        if order != sorted(order):
            ctx.add("L107", doc.name, found[0][1], f"`{name}`: the bold fields are out of order")
        for f in required:
            if f not in [lbl for lbl, _ in found]:
                ctx.add("L107", doc.name, where_line, f"`{name}`: the bold field `**{f}**` is missing")
    if key in ("breath", "decision", "realworld", "question") and isinstance(bf.get(key), list):
        check(blocks, bf[key], bf[key], h["line"], h["title"])
    if s.get("subsection_fields"):
        for sub in subs:
            check(_section_blocks(doc, sub), s["subsection_fields"], s["subsection_fields"], sub["line"], sub["title"])
    if s.get("fields"):
        fields = [f for f in s["fields"] if isinstance(f, dict) and f.get("label", "").endswith((".", ":"))]
        plain = [f for f in fields if not re.match(r"^(callout|table|comment|diagram)\b", f["label"])]
        check(blocks, [f["label"] for f in plain], [f["label"] for f in plain if f.get("required")], h["line"], h["title"])
        for f in plain:
            para = next((b for b in blocks if b.kind == "para" and _label(b) == f["label"]), None)
            if para is None:
                continue
            if f.get("sentences_max"):
                n = len(_split_sentences(_inline(_RE_BOLD_START.sub("", para.text.strip()))[0]))
                if n > f["sentences_max"]:
                    ctx.add("L106", doc.name, para.line, f"`{f['label']}` has {n} sentences; the limit is {f['sentences_max']}")
            if f.get("list_items"):
                nxt = doc.blocks[para.index + 1] if para.index + 1 < len(doc.blocks) else None
                n = len(nxt.extra["items"]) if nxt is not None and nxt.kind == "list" else 0
                if not _in_range(n, f["list_items"]):
                    ctx.add("L106", doc.name, para.line, f"`{f['label']}` has {n} list items; it needs {_range_text(f['list_items'])}")
            if word_count(para.text) > ctx.sp["lint"]["paragraph"]["error_over_words"]:
                ctx.add("L202", doc.name, para.line, f"field `{f['label']}` is too long")
        for f in s["fields"]:
            if isinstance(f, dict) and f.get("label", "").startswith("callout:") and f.get("required"):
                label = f["label"].split(":", 1)[1]
                if not any(b.kind == "quote" and b.extra.get("label") == label for b in blocks):
                    ctx.add("L107", doc.name, h["line"], f"`{h['title']}`: the `{label}` callout is missing")


def _changed_entry(ctx, doc, b):
    cr = ctx.sp["callouts"]["changed_recently"]
    content = [c.strip() for c in b.extra["content"]]
    first = _callout(b)[1]
    m = re.match(cr["date_regex"], first)
    if not m:
        ctx.add("L107", doc.name, b.line, "a Changed recently entry starts with a date in parentheses")
    labels = cr["line_labels"]
    if len(content) != len(labels) + 1 or any(not content[i + 1].startswith(f"**{lbl}**") for i, lbl in enumerate(labels) if i + 1 < len(content)):
        ctx.add("L107", doc.name, b.line, "a Changed recently entry has the lines " + ", ".join(labels) + " in this order")
        return
    br = cr.get("line_break", "<br>")
    for i in range(len(labels)):
        if not content[i].endswith(br):
            ctx.add("L107", doc.name, b.line + i, f"the line must end with {br}")
    status = content[-1][len(f"**{labels[-1]}**"):].strip().rstrip(".")
    if status not in cr["status_values"]:
        ctx.add("L107", doc.name, b.line + len(labels), f"Status `{status}` is not one of " + ", ".join(cr["status_values"]))
    if not m:
        return
    date = m.group(1)
    now = next((c for c in content if c.startswith("**Now:**")), "")
    for _, href in _RE_LINK.findall(now):
        fm = re.match(ctx.sp["fact_links"]["href_regex"], href)
        changed = (ctx.facts.get(fm.group(2)) or {}).get("changed") if fm else None
        if changed and changed.get("date") and not str(changed["date"]).startswith(date):
            ctx.add("L107", doc.name, b.line, f"entry date {date} differs from changed.date {changed['date']} of {fm.group(2)}")
    cutoff = (common.load_book().get("book") or {}).get("exam_eligibility_cutoff")
    if cutoff and date > cutoff[:len(date)] and status != cr["status_values"][-1]:
        ctx.add("L107", doc.name, b.line + len(labels), f"an entry dated after {cutoff} has Status `{cr['status_values'][-1]}`")


def _units(ctx, doc):
    """Yield the text units of a file: (raw text, line, grounding, kind, block)."""
    sp = ctx.sp
    labels = {c["label"]: c for c in sp["callouts"]["labels"]}
    tk = sp["tables"]["kinds"]
    bf = sp["bold_fields"]
    known = set()
    for v in bf.values():
        if isinstance(v, list):
            known.update(v)
    example_fields = {"how": {"Problem."}, "page": {"Requirement."}}
    expects = "**The exam probably expects:**"
    wrong, truth = (bf.get("traps") or ["Wrong belief:", "Truth:"])[:2]
    caption = sp["diagram_embed"]["caption_prefix"].strip()
    for b in doc.blocks:
        role = (b.sec or {}).get("role")
        base = ctx.grounding(role) if b.sec else "strict"
        if b.kind == "para":
            text = b.text.strip()
            if _RE_IMG.fullmatch(text) or text.startswith("!["):
                continue
            label, g = _label(b), base
            if label is not None:
                if "prompt" in b.extra:
                    g = "example"
                elif label in example_fields.get(role, ()) and (role != "how" or (b.sec.get("spec") or {}).get("subsection_fields")):
                    g = "example"
                if "prompt" in b.extra or label in known or text.startswith(caption) \
                        or (role == "realworld" and re.match(bf.get("realworld_first_paragraph_regex", "$^"), text)):
                    text = _RE_BOLD_START.sub("", text)
            yield text, b.line, g, "para", b
        elif b.kind == "summary":           # gate-break H12: the summary line is visible when the block is closed
            if b.details:
                yield b.details, b.line, base, "summary", b
        elif b.kind == "list":
            for it in b.extra["items"]:
                text = it["text"]
                m = re.match(r"^\s*\*\*" + re.escape(wrong) + r"\*\*(.*?)\*\*" + re.escape(truth) + r"\*\*(.*)$", text, re.S)
                if m:
                    yield m.group(1), it["line"], "example", "item", b
                    yield m.group(2), it["line"], base, "item", b
                else:
                    yield text, it["line"], base, "item", b
        elif b.kind == "table" and "body" in b.extra:
            ks = tk.get(b.extra["tkind"], {})
            for r, row in enumerate(b.extra["body"]):
                for c, cell in enumerate(row):
                    g = base
                    if base != "example":
                        if c in ks.get("example_columns", []) or b.extra["tkind"] in ("plan", "log"):
                            g = "example"
                        elif c in ks.get("heuristic_columns", []):
                            g = "heuristic"
                    if cell:
                        yield cell, b.line + 2 + r, g, "cell", b
        elif b.kind == "quote" and not _is_aws_quote(b):
            co = _callout(b)
            g = base
            if co and co[0] in labels and base != "example" and labels[co[0]].get("grounding") in ("example", "heuristic"):
                g = labels[co[0]]["grounding"]
            content = list(b.extra["content"])
            if co:
                content[0] = co[1]
                if co[0] == "Exam signal":
                    content[0] = re.sub(r'^\s*"[^"]*"', " ", content[0])
                if co[0] == "Changed recently":
                    content[0] = re.sub(sp["callouts"]["changed_recently"]["date_regex"], "", content[0])
                    for i, line in enumerate(content):
                        lg = "heuristic" if line.strip().startswith(expects) and g == "strict" else g
                        yield re.sub(r"^\s*\*\*[^*]+\*\*", "", line), b.line + i, lg, "callout", b
                    continue
            yield " ".join(content), b.line, g, "callout", b


def _text_rules(ctx, doc):
    sp, lint, m = ctx.sp, ctx.sp["lint"], ctx.matcher
    sen, par = lint["sentence"], lint["paragraph"]
    allowed_tags = set(lint.get("raw_html_allowed", []))
    term_names = {t["term"].lower() for t in ctx.terms if t.get("kind") in ("aws-name", "concept")}
    after = lint.get("former_name_allowed_once_after", [])
    former_used = set()
    bold_terms = {t["term"].lower() for t in ctx.terms}
    for text, line, g, kind, b in _units(ctx, doc):
        where = ctx.where(doc, line)
        marked, links = _inline(text)
        found, warns, stats = [], [], []
        ctx.fact_links += len(_check_links(sp, ctx.facts, links, where, found))
        _ground(m, marked, links, g, where, found, None, warns, stats)
        ctx.stats += stats
        plain = _plain(marked)
        sec_id = f"{ctx.dirname}/{doc.name}#{(b.sec or {}).get('id')}"
        allowed_place = sec_id in lint.get("customer_words_allowed_in", [])
        _banned(m, plain, where, found, skip_customer=allowed_place)
        ctx.errors += found
        ctx.warnings += warns
        for words, _ in stats:
            if words > sen["error_over_words"]:
                ctx.add("L202", doc.name, line, f"sentence of {words} words; the limit is {sen['error_over_words']}")
            elif words > sen["warn_over_words"]:
                ctx.add("W202", doc.name, line, f"sentence of {words} words; aim for {sen['warn_over_words']} or fewer")
        if kind == "para" and "prompt" not in b.extra:
            n = sum(w for w, _ in stats)
            if n > par["error_over_words"]:
                ctx.add("L202", doc.name, line, f"paragraph of {n} words; the limit is {par['error_over_words']}")
            elif n > par["warn_over_words"] or len(stats) > par["sentences_max"]:
                ctx.add("W202", doc.name, line, f"paragraph of {len(stats)} sentences and {n} words")
            bold = [x for x in re.findall(r"\*\*([^*]+)\*\*", text) if x.lower() in bold_terms]
            if len(bold) > par.get("new_bold_terms_max", 3):
                ctx.add("W202", doc.name, line, f"{len(bold)} new bold terms in one paragraph")
        for word, rx, tip in m.warn:
            if rx.search(plain):
                ctx.add("W801", doc.name, line, f"`{word}`: {tip}")
        if lint.get("em_dash_in_prose") and "—" in plain:
            ctx.add("W801" if lint["em_dash_in_prose"] == "warn" else "L801", doc.name, line, "em dash in prose")
        for word, rx in m.customer:
            if rx.search(plain) and not allowed_place and word.lower() not in term_names and word not in lint.get("banned_words", {}):
                ctx.add("L902", doc.name, line, f"customer word `{word}` outside its allowed places")
        # L802 and L901 on text that keeps bold markers, so that `**Formerly.** ` is visible
        flat = _RE_MARK.sub("", marked)
        for name, rx, new in m.former:
            for hit in rx.finditer(flat):
                before = flat[:hit.start()]
                if any(before.endswith(a) or before.lower().endswith(a.lower()) for a in after) and (name, doc.name) not in former_used:
                    former_used.add((name, doc.name))
                    continue
                ctx.add("L802", doc.name, line, f"former name `{hit.group(0)}`: use `{new}`")
        _variants(ctx, doc, line, flat, after, former_used)
        if not lint.get("contractions_in_prose", False) and m.contraction and m.contraction.search(plain.replace("’", "'")):
            ctx.add("L803", doc.name, line, "contraction in prose: " + m.contraction.search(plain.replace("’", "'")).group(0))
        if not lint.get("emphasis_italic", False):
            bare = marked.replace("**", "")
            if re.search(r"(?<![\w*])\*[^\s*][^*\n]*\*(?![\w*])", bare) or re.search(r"(?<![\w_])_[^\s_][^_\n]*_(?![\w_])", bare):
                ctx.add("L803", doc.name, line, "italic emphasis is not used")
    # raw scans: HTML, emoji, alt text
    in_fence = False
    for i in range(doc.body_start, len(doc.lines)):
        raw = doc.lines[i]
        if _RE_FENCE.match(raw) or (in_fence and raw.strip().startswith("```")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        clean = _RE_ICODE.sub(" ", _RE_COMMENT.sub(" ", raw))
        for tag in _RE_TAG.findall(clean):
            if tag not in allowed_tags and not clean.strip().startswith("<http"):
                ctx.add("L803", doc.name, i + 1, f"raw HTML tag <{tag}> is not allowed")
        if not lint.get("emoji", False) and _RE_EMOJI.search(clean):
            ctx.add("L803", doc.name, i + 1, "emoji")
        for alt, _ in _RE_IMG.findall(clean):
            where = ctx.where(doc, i + 1)
            if lint.get("images_need_alt") and not alt.strip():
                ctx.add("L803", doc.name, i + 1, "image without alt text")
            found = []
            _banned(m, alt, where, found)
            ctx.errors += found
            _variants(ctx, doc, i + 1, alt, [], set())


def _variants(ctx, doc, line, text, after, used):
    m = ctx.matcher
    for variant, rx, term in m.variants:
        for hit in rx.finditer(text):
            if m.in_longer_name(text, hit.start(), hit.end(), variant):
                continue
            before = text[:hit.start()]
            if any(before.lower().endswith(a.lower()) for a in after) and (variant, doc.name) not in used:
                used.add((variant, doc.name))
                continue
            ctx.add("L901", doc.name, line, f"banned variant `{hit.group(0)}`: the term is `{term['term']}`")


def _other_doc(ctx, dirname, name):
    key = (dirname, name)
    if key not in ctx.other_docs:
        path = common.BOOK / dirname / name
        ctx.other_docs[key] = Doc(name, path.read_text(encoding="utf-8"), ctx.sp) if path.exists() else None
    return ctx.other_docs[key]


def _links_and_ids(ctx, doc):
    sp, lint = ctx.sp, ctx.sp["lint"]
    hosts = set(lint.get("external_link_hosts", []))
    generated = {fs["name"] for fs in ctx.tpl["files"] if fs.get("source") == "generated"}
    term_ids = {t["id"] for t in ctx.terms}
    aq = sp["fact_links"]["aws_quote"]
    in_fence = False
    for b in doc.blocks:
        if b.kind in ("code", "heading", "region", "comment", "summary", "details_open", "details_close"):
            if b.kind == "heading" and _RE_LINK.search(b.text):
                ctx.add("L103", doc.name, b.line, "a heading cannot hold a link")
            continue
        quote = _is_aws_quote(b)
        source_field = b.kind == "para" and _label(b) == "Source."
        for off, raw in enumerate(b.lines):
            line = b.line + off
            clean = _RE_ICODE.sub(" ", _RE_COMMENT.sub(" ", raw))
            for text, href in _RE_LINK.findall(clean):
                if re.match(r"https?://", href):
                    host = urlparse(href).netloc.lower()
                    if host not in hosts:
                        ctx.add("L602", doc.name, line, f"external link to {host}: the host is not allowed")
                    elif not (quote or source_field):
                        ctx.add("L602", doc.name, line, "an external link stands only in an AWS quote block or a Source. field")
                    continue
                fm = re.fullmatch(r"\.\./facts/([a-z0-9-]+)\.md#([a-z0-9-]+)", href)
                if fm:                      # gate-break H14: the generated fact sheet is the target of the link
                    if fm.group(1) not in ctx.sheets:
                        path = common.FACTSHEETS / f"{fm.group(1)}.md"
                        ctx.sheets[fm.group(1)] = set(re.findall(r"(?m)^### (\S+)\s*$", path.read_text(encoding="utf-8"))) \
                            if path.exists() else None
                    anchors = ctx.sheets[fm.group(1)]
                    if anchors is None:
                        ctx.add("L601", doc.name, line, f"link to a missing file facts/{fm.group(1)}.md: run sync", d=True)
                    elif fm.group(2) not in anchors:
                        ctx.add("L601", doc.name, line, f"facts/{fm.group(1)}.md has no entry {fm.group(2)}: run sync", d=True)
                    continue
                if href.startswith("../facts/") or "/facts/" in href or href.startswith(("mailto:", "../diagrams/")):
                    continue
                target, _, frag = href.partition("#")
                if target == "../glossary.md":
                    if frag not in term_ids:
                        ctx.add("L603", doc.name, line, f"glossary link to unknown term `{frag}`")
                    continue
                if not target:
                    tdoc, tname, tdir = doc, doc.name, ctx.dirname
                else:
                    parts = target.split("/")
                    if len(parts) == 1:
                        tdir, tname = ctx.dirname, parts[0]
                    elif len(parts) == 3 and parts[0] == "..":
                        tdir, tname = parts[1], parts[2]
                    else:
                        tdir, tname = None, target
                    if tdir == ctx.dirname and tname in generated:
                        if frag:
                            ctx.add("L601", doc.name, line, f"a link to the generated file {tname} carries no anchor")
                        continue
                    if tdir is None:
                        if not (ctx.dir / target).resolve().exists():
                            ctx.add("L601", doc.name, line, f"link to a missing file {target}")
                        continue
                    tdoc = ctx.docs.get(tname) if tdir == ctx.dirname else _other_doc(ctx, tdir, tname)
                    other = tdir != ctx.dirname
                    if other and _ledger_status(tdir.split("-")[0]) not in _DRAFTED:
                        ctx.add("L601", doc.name, line, f"link to {tdir}, which is not drafted yet: use an xref marker", d=True)
                        continue
                    if tdoc is None:
                        if not (common.BOOK / tdir / tname).exists():
                            ctx.add("L601", doc.name, line, f"link to a missing file {target}")
                        elif frag:
                            ctx.add("L601", doc.name, line, f"link to the generated file {target} carries no anchor")
                        continue
                if frag and frag not in {h["anchor"] for h in tdoc.headings}:
                    ctx.add("L601", doc.name, line, f"link to a missing anchor #{frag} in {tname}")
            bare = _RE_LINK.sub(" ", _RE_IMG.sub(" ", clean))
            if not sp["links"].get("bare_urls", False) and _RE_URL.search(bare):
                ctx.add("L602", doc.name, line, "bare URL: " + _RE_URL.search(bare).group(0)[:60])
        if quote:
            _aws_quote(ctx, doc, b, aq, hosts)
    # trap ids
    trap_rx, seen = re.compile(sp["ids"]["trap"]), {}
    all_traps = None
    for mk in doc.markers:
        if mk["kind"] == "trap":
            tid = mk["value"]
            if not trap_rx.match(tid) or not tid.startswith(ctx.slug + "-"):
                ctx.add("L604", doc.name, mk["line"], f"trap id `{tid}` does not match `{ctx.slug}-trap-<belief>`")
            if tid in ctx.trap_ids:
                ctx.add("L604", doc.name, mk["line"], f"trap id `{tid}` is defined twice")
            ctx.trap_ids[tid] = (doc.name, mk["line"])
        elif mk["kind"] == "trap-ref":
            all_traps = traps() if all_traps is None else all_traps
            if all_traps.get(mk["value"]) in (None, ctx.cid):
                ctx.add("L604", doc.name, mk["line"], f"trap-ref `{mk['value']}` is not a trap of another chapter")
        elif mk["kind"] == "xref":
            ctx.add("L601" if ctx.strict_all else "W601", doc.name, mk["line"], f"xref marker: {mk['value']}")
    looks = {t["id"] for t in _items(ctx.entry, "tasks") if t.get("type") == "look"}
    for r in doc.regions:
        if r["kind"] == "task" and r["attrs"].get("id") not in looks:
            ctx.add("L604", doc.name, r["line"], f"task region id `{r['attrs'].get('id')}` is not a look task of the chapter", d=True)
    for line, msg in doc.issues:
        ctx.add("L604", doc.name, line, msg)


def _whole_sentences(quote: str, start: int, end: int) -> bool:
    """True when quote[start:end] starts at a sentence start and ends at a sentence end of the normalised evidence
    quote, or at the end of quoted speech (gate-break H3: `move a shelf ...` cut from `You cannot move a shelf ...`)."""
    before = quote[:start].rstrip().rstrip("\"'([")
    after = quote[end:]
    starts = not before or before[-1] in ".?!:"
    inner = quote[start:end].rstrip("\"')]")
    ends = not after.strip(" \"')]") or (inner[-1:] in ".?!" and after[:1] in (" ", '"', "'", ")")) \
        or re.match(r"[,.]?[\"']", after) is not None
    return starts and ends


def _aws_quote(ctx, doc, b, aq, hosts):
    content = [c.strip() for c in b.extra["content"]]
    last = content[-1]
    m = _RE_LINK.search(last)
    if len(content) < 2 or not last.startswith(aq["attribution_prefix"]) or not m:
        ctx.add("L306", doc.name, b.line + len(content) - 1, f"the last line of an AWS quote block starts with `{aq['attribution_prefix']}`")
        return
    url = m.group(2)
    if urlparse(url).netloc.lower() not in hosts:
        return        # L602 reports the host
    span = " ".join(content[:-1]).strip()
    span = span[1:] if span.startswith('"') else span
    cut = span.rfind('"')
    span = span[:cut] + span[cut + 1:] if cut >= 0 else span
    match, partial = None, False
    for fact in ctx.facts.values():
        if fact.get("status") != "verified":
            continue
        for ev in fact.get("evidence", []):
            hit = common.find_quote(span, ev.get("quote", "")) if ev.get("url") == url else None
            if hit and (ev.get("quote", "").lstrip().startswith("|") or _whole_sentences(common.normalize_text(ev["quote"]), *hit)):
                match = fact
                break
            partial = partial or bool(hit)
        if match:
            break
    if match is None and partial:
        ctx.add("L306", doc.name, b.line, "the quote block must hold whole sentences of the evidence quote "
                                          "(it starts or ends in the middle of a sentence)")
    elif match is None:
        ctx.add("L306", doc.name, b.line, "the quote is not found inside an evidence quote of a verified fact with this URL")
    elif match.get("kind") == "case-study" and word_count(span) > aq["case_study_quote_words_max"]:
        ctx.add("L306", doc.name, b.line, f"a case-study quote has at most {aq['case_study_quote_words_max']} words")


def _spec_caption(diagram_id):
    path = common.DIAGRAM_SRC / f"{diagram_id}.json"
    spec_data = common.read_json(path)
    if not isinstance(spec_data, dict):
        return None
    try:
        from saalib.diagram import pipeline
        cap = pipeline.caption(spec_data)
        steps = [say for _, say in cap.get("steps", [])]
        return {"claim": cap.get("claim", ""), "alt": cap.get("alt", ""), "steps": steps, "kind": spec_data.get("kind")}
    except Exception:
        steps = {}
        for edge in spec_data.get("edges", []) + spec_data.get("messages", []):
            if isinstance(edge, dict) and edge.get("say"):
                steps.setdefault(edge.get("step", len(steps) + 1), edge["say"])
        return {"claim": spec_data.get("claim", ""), "alt": spec_data.get("alt", ""),
                "steps": [steps[k] for k in sorted(steps)], "kind": spec_data.get("kind")}


def _diagrams(ctx, doc):
    sp, de, m = ctx.sp, ctx.sp["diagram_embed"], ctx.matcher
    img_rx = re.compile(de["image_regex"])
    norm = lambda t: common.normalize_text(_RE_LINK.sub(r"\1", t))
    href_rx = re.compile(sp["fact_links"]["href_regex"])
    has_fact = lambda t: any(href_rx.match(h) for _, h in _RE_LINK.findall(t))
    hard = lambda t: bool(m.numbers(t) or m.absolutes(t))
    hm = re.match(r"details:(.+?) after a (.+?) prompt", de.get("hero_inside", ""))
    for b in doc.blocks:
        if b.kind not in ("para", "list", "quote", "table") or "![" not in b.text:
            continue
        text = b.text.strip()
        im = img_rx.match(text) if b.kind == "para" and len(b.lines) == 1 else None
        if not im:
            ctx.add("L701", doc.name, b.line, "a diagram image is alone in its paragraph and matches the embed pattern (alt text of 20 characters or more)")
            continue
        did = im.group(1)
        alt = _RE_IMG.match(text).group(1)
        embed = {"doc": doc, "block": b, "id": did, "steps": []}
        ctx.embeds.append(embed)
        if de.get("id_must_start_with_slug") and not did.startswith(ctx.slug + "-"):
            ctx.add("L701", doc.name, b.line, f"diagram id `{did}` does not start with `{ctx.slug}-`")
        svg = common.DIAGRAM_SVG / f"{did}.svg"
        if not svg.exists():
            ctx.add("L701", doc.name, b.line, f"diagram file diagrams/svg/{did}.svg is missing", d=True)
        else:
            ctx.inputs.add(svg)
        cap = _spec_caption(did)
        if cap is not None:
            ctx.inputs.add(common.DIAGRAM_SRC / f"{did}.json")
        nxt = doc.blocks[b.index + 1] if b.index + 1 < len(doc.blocks) else None
        prefix = de["caption_prefix"]
        if nxt is None or nxt.kind != "para" or not nxt.text.strip().startswith(prefix.strip()):
            ctx.add("L702", doc.name, b.line, f"the caption `{prefix.strip()}` is missing after the image")
            continue
        caption = nxt.text.strip()[len(prefix.strip()):].strip()
        if len(_split_sentences(_inline(caption)[0])) != de.get("caption_sentences", 1):
            ctx.add("L702", doc.name, nxt.line, "the caption is one sentence")
        if word_count(caption) > de["caption_words_max"]:
            ctx.add("L702", doc.name, nxt.line, f"the caption has more than {de['caption_words_max']} words")
        lst = doc.blocks[nxt.index + 1] if nxt.index + 1 < len(doc.blocks) else None
        steps = [it["text"] for it in lst.extra["items"]] if lst is not None and lst.kind == "list" and lst.extra["items"][0]["ordered"] else []
        embed["steps"] = steps
        if cap is not None:
            if norm(caption) != norm(cap["claim"]):
                ctx.add("L702", doc.name, nxt.line, "the caption differs from the spec `claim`")
            if common.normalize_text(alt) != common.normalize_text(cap["alt"]):
                ctx.add("L702", doc.name, b.line, "the alt text differs from the spec `alt`")
            if cap["steps"]:
                if len(steps) != len(cap["steps"]):
                    ctx.add("L703", doc.name, nxt.line, f"{len(steps)} step sentences; the spec has {len(cap['steps'])} steps")
                else:
                    for k, (have, want) in enumerate(zip(steps, cap["steps"])):
                        if norm(have) != norm(want):
                            ctx.add("L703", doc.name, lst.extra["items"][k]["line"], f"step {k + 1} differs from the spec `say`")
            if hard(cap["claim"]) and not has_fact(caption):
                ctx.add("L705", doc.name, nxt.line, "the spec `claim` states a hard fact; the caption needs the fact link")
            for k, want in enumerate(cap["steps"][:len(steps)]):
                if hard(want) and not has_fact(steps[k]):
                    ctx.add("L705", doc.name, lst.extra["items"][k]["line"], f"step {k + 1} states a hard fact and needs the fact link")
        if did == f"{ctx.slug}-hero":
            opened = b.open
            before = doc.blocks[opened.index - 1] if opened is not None and opened.index > 0 else None
            inside = opened is not None and (not hm or (opened.extra.get("summary") == hm.group(1)
                                                         and before is not None and _label(before) == hm.group(2)))
            if not inside:
                ctx.add("L704", doc.name, b.line, f"the hero diagram sits inside {de.get('hero_inside')}")
            if cap is not None and cap.get("kind") not in de.get("hero_kinds", []):
                ctx.add("L704", doc.name, b.line, f"the hero diagram is of kind {cap.get('kind')}; allowed: " + ", ".join(de.get("hero_kinds", [])))
    for h in doc.h2():
        want = ((h["spec"] or {}).get("counts") or {}).get("hero_diagrams")
        if want not in (None, {}):
            n = sum(1 for e in ctx.embeds if e["doc"] is doc and e["block"].sec is h and e["id"] == f"{ctx.slug}-hero")
            if n == 0 and not _in_range(0, want):
                ctx.add("L704", doc.name, h["line"], f"the hero diagram `{ctx.slug}-hero` is missing in `{h['title']}`", d=True)
            elif not _in_range(n, want):
                ctx.add("L106", doc.name, h["line"], f"`{h['title']}`: {n} hero diagrams; the section needs {_range_text(want)}")


def _code(ctx, doc):
    cs = ctx.sp["code"]
    banned = [re.compile(p) for p in cs.get("banned_patterns", [])]
    for b in doc.blocks:
        if b.kind != "code":
            continue
        lang = b.extra["lang"]
        if cs.get("language_required") and not lang:
            ctx.add("L804", doc.name, b.line - 1, "code block without a language")
        elif lang and lang not in cs["languages"]:
            ctx.add("L804", doc.name, b.line - 1, f"unknown code language `{lang}`")
        if len(b.lines) > cs["lines_max"]:
            ctx.add("L804", doc.name, b.line - 1, f"code block of {len(b.lines)} lines; the limit is {cs['lines_max']}")
        for off, raw in enumerate(b.lines):
            for rx in banned:
                hit = rx.search(raw)
                if hit and not (lang == "json" and hit.group(0) in cs.get("allowed_account_ids", [])):
                    ctx.add("L804", doc.name, b.line + off, f"banned pattern in code: {hit.group(0)[:30]}")


def _markers(ctx, doc):
    fl = ctx.sp["fact_links"]
    severity = fl.get("needs_fact_severity", {}).get(ctx.status(doc), "warn")
    for mk in doc.markers:
        if mk["kind"] in ("needs-fact", "needs-display", "needs-term"):
            ctx.add("L307" if severity == "error" else "W307", doc.name, mk["line"], f"{mk['kind']} marker: {mk['value'][:70]}")
        elif mk["kind"] == "no-fact" and mk["value"] not in ctx.sp["grounding"].get("no_fact_reasons", []):
            ctx.add("L304", doc.name, mk["line"], f"unknown no-fact reason `{mk['value']}`")


def _chapter_rules(ctx) -> dict:
    """Rules over all hand files: L108, L308, L402 (tasks), L903, L905, L106 diagrams, W105, W802, W901, W902."""
    sp, lint, m = ctx.sp, ctx.sp["lint"], ctx.matcher
    href_rx = re.compile(sp["fact_links"]["href_regex"])
    seen = {}
    for doc in ctx.docs.values():
        for h in doc.headings:
            if h["level"] not in (2, 3):
                continue
            if h["id"] in seen:
                ctx.add("L108", doc.name, h["line"], f"section id `{h['id']}` is also used at {seen[h['id']]}")
            else:
                seen[h["id"]] = f"{doc.name}:{h['line']}"
            role = h["role"] or (h["parent"] or {}).get("role")
            if ctx.grounding(role) == "strict" and (m.numbers(h["title"]) or m.absolutes(h["title"])):
                body = doc.section_text(h)
                if not any(href_rx.match(href) for _, href in _RE_LINK.findall(body)):
                    ctx.add("L308", doc.name, h["line"], f"heading `{h['title']}` states a hard fact; its body has no fact link")
    # tasks and Try it callouts
    tasks = [t for t in _items(ctx.entry, "tasks") if t.get("status") not in ("rejected", "retired")]
    task_ids = {t["id"]: t for t in tasks}
    tries = {}
    for doc in ctx.docs.values():
        for b in doc.blocks:
            if b.kind == "quote" and b.extra.get("label") == "Try it":
                ids = [mk["value"] for mk in doc.markers if mk["block"] is b and mk["kind"] == "task"]
                if not ids:
                    ctx.add("L402", doc.name, b.line, "a Try it callout ends with a task comment", d=True)
                for tid in ids:
                    if tid not in task_ids:
                        ctx.add("L402", doc.name, b.line, f"Try it names the unknown task `{tid}`", d=True)
                    for h in (b.sub, b.sec):
                        if h:
                            tries.setdefault(tid, []).append(f"{doc.name}#{h['id']}")
    if ctx.docs:
        for t in tasks:
            if t.get("type") in ("try", "lab"):
                n = sum(1 for place in tries.get(t["id"], []) if place == t.get("section"))
                total = len({p for p in tries.get(t["id"], [])})
                if n != 1 or total > 2:
                    ctx.add("L402", None, None, f"task {t['id']} needs exactly one Try it callout in {t.get('section')}", d=True)
    # orphan rule
    used = set()
    for kind in ("questions", "cards", "speak", "tasks"):
        used.update(i.get("section") for i in _items(ctx.entry, kind) if i.get("section"))
    for doc in ctx.docs.values():
        for h in doc.headings:
            if h["level"] == 3 and (h["parent"] or {}).get("role") == "how" and f"{doc.name}#{h['id']}" not in used:
                ctx.add("L903", doc.name, h["line"], f"no question, card, speak item or task reviews `{h['title']}`", d=True)
    # brief
    brief = _brief(ctx.entry)
    if brief and not ctx.draft:
        ctx.inputs.add(common.BUILD / "work" / ctx.dirname / "brief.json")
        have_traps = set(ctx.trap_ids)
        for t in brief.get("traps", []):
            if t.get("id") not in have_traps:
                ctx.add("L905", None, None, f"brief trap `{t.get('id')}` is in no hand file")
        for s in brief.get("sections", []):
            doc = ctx.docs.get(s.get("file"))
            if doc is None or s.get("section") not in {h["id"] for h in doc.headings}:
                ctx.add("L905", s.get("file"), None, f"brief section `{s.get('section')}` is not in the file")
    want = ctx.tpl["counts"].get("diagrams")
    if want not in (None, {}) and ctx.docs and not _in_range(len(ctx.embeds), want):
        ctx.add("L106", None, None, f"{len(ctx.embeds)} diagram embeds in the chapter; it needs {_range_text(want)}", d=True)
    # W802, W901
    if lint.get("abbreviation_spell_out_first_use_per_file"):
        for doc in ctx.docs.values():
            body = _RE_COMMENT.sub(" ", "\n".join(l for l in doc.lines[doc.body_start:] if not l.startswith("# ")))
            for t in ctx.terms:
                if not t.get("short") or t.get("kind") == "aws-name":
                    continue
                full = body.lower().find(t["term"].lower())
                for hit in _wm(t["short"], 0).finditer(body):
                    if t["short"].lower() in t["term"].lower() and body.lower()[max(0, hit.start() - len(t["term"])):hit.end() + len(t["term"])].find(t["term"].lower()) >= 0:
                        continue
                    if full < 0 or hit.start() < full:
                        ctx.add("W802", doc.name, doc.body_start + body[:hit.start()].count("\n") + 1,
                                f"short form `{t['short']}` before the full term `{t['term']}`")
                    break
    first = {}
    for doc in ctx.docs.values():
        for b in doc.blocks:
            if b.kind in ("heading", "code", "region", "comment", "summary", "details_open", "details_close") or _is_aws_quote(b):
                continue
            words_table = b.kind == "table" and b.extra.get("tkind") == "words"
            text = _RE_ICODE.sub(" ", _RE_COMMENT.sub(" ", b.text))
            for t in ctx.terms:
                if t["id"] in first:
                    continue
                for form in [t["term"]] + list(t.get("aliases", [])):
                    hit = _wm(form).search(text)
                    if hit and not m.in_longer_name(text, hit.start(), hit.end(), form):
                        first[t["id"]] = True
                        bold = text[max(0, hit.start() - 2):hit.start()] == "**" and text[hit.end():hit.end() + 2] == "**"
                        tail = text[hit.end() + (2 if bold else 0):]
                        if words_table:      # the row whose cell 1 is the term defines it, wherever the table first names it
                            cells = [row[0] for row in b.extra.get("body", []) if row]
                            mine = [c for c in cells if re.sub(r"\s+", " ", re.sub(r"\([^)]*\)", "", c)).strip().lower() == t["term"].lower()]
                            words_row = bool(mine)
                            tail = mine[0][len(t["term"]):] if mine else tail
                        else:
                            words_row = False
                        if not (bold or words_row):
                            ctx.add("W901", doc.name, b.line, f"first use of the term `{t['term']}` is not bold")
                        elif t.get("respelling") and not re.match(r"\s*\(" + re.escape(t["respelling"]) + r"\)", tail):
                            ctx.add("W901", doc.name, b.line, f"first use of `{t['term']}` lacks its respelling ({t['respelling']})")
                        break
    # W902, W903
    st = sp.get("startup", {})
    story, numbers = 0, []
    for doc in ctx.docs.values():
        for b in doc.blocks:
            if b.kind == "quote" and b.extra.get("label") == "Startup example":
                text = " ".join(b.extra["content"])
                story += word_count(text) - 2
                numbers += [(doc, b.line, n) for n in re.findall(r"(?<![A-Za-z0-9.])[0-9][0-9,]*(?:\.[0-9]+)?", text)]
            elif ((b.sec or {}).get("spec") or {}).get("key") == "decision" and b.kind in ("para", "list"):
                numbers += [(doc, b.line, n) for n in re.findall(r"(?<![A-Za-z0-9.#-])[0-9][0-9,]*(?:\.[0-9]+)?(?![0-9]*\))", _RE_LINK.sub(" ", b.text))]
        if st.get("former_working_name") and _wm(st["former_working_name"]).search(_RE_COMMENT.sub(" ", "\n".join(doc.lines[doc.body_start:]))):
            ctx.add("W902", doc.name, None, f"the former working name {st['former_working_name']} must not appear")
    if st.get("story_max_words_per_chapter") is not None and story > st["story_max_words_per_chapter"]:
        ctx.add("W902", None, None, f"{story} words of story in Startup example callouts; the limit is {st['story_max_words_per_chapter']}")
    data = common.read_json(common.BOOK / st["data"]) if st.get("data") else None
    uses = ((data or {}).get("chapters") or {}).get(ctx.cid, {}).get("uses_numbers") if isinstance(data, dict) else None
    if isinstance(uses, list):
        allowed = set()

        def collect(v):
            if isinstance(v, dict):
                for x in v.values():
                    collect(x)
            elif isinstance(v, list):
                for x in v:
                    collect(x)
            elif isinstance(v, (int, float)) and not isinstance(v, bool):
                allowed.add(str(v).rstrip("0").rstrip(".") if isinstance(v, float) else str(v))
        for key in uses:
            collect((data.get("numbers") or {}).get(key, {}).get("value") if isinstance(key, str) else key)
        for doc, line, n in numbers:
            if n.replace(",", "") not in allowed:
                ctx.add("W903", doc.name, line, f"story number {n} is not in uses_numbers of the chapter")
    # W105
    mf = lint.get("minutes_formula", {})
    fast_doc = ctx.docs.get(sp["front_matter"]["chapter_file"])
    out = {}
    if fast_doc is not None and mf:
        counts = ctx.tpl["counts"]
        q, spk = counts.get("questions", {}), counts.get("speak", {})
        fast = sum(h["minutes"] or 0 for h in fast_doc.h2())
        others = [d for d in ctx.docs.values() if d is not fast_doc]
        h3_pass = sum(h["minutes"] or 0 for d in ctx.docs.values() for h in d.headings if h["level"] == 3 and h["pass"])
        deep = sum(h["minutes"] or 0 for d in others for h in d.h2())
        try_pass = sum(t.get("minutes", 0) for t in tasks if t.get("type") == "try" and t.get("pass_route"))
        hands = sum(t.get("minutes", 0) for t in tasks if t.get("type") in ("try", "lab"))
        per_q, per_s = mf.get("minutes_per_question", 0), mf.get("minutes_per_spoken_answer", 0)
        up = lambda x: int(x + 0.5)
        out = {"fast": fast,
               "pass": up(fast + h3_pass + try_pass + per_q * q.get("core", 0) + per_s * spk.get("pass_route", 0)),
               "full": up(fast + deep + hands + per_q * q.get("shipped", 0) + per_s * spk.get("count", 0))}
        have = fast_doc.fm.get("minutes") if isinstance(fast_doc.fm.get("minutes"), dict) else {}
        for key in ("pass", "full"):
            if isinstance(have.get(key), int) and abs(have[key] - out[key]) > mf.get("tolerance_minutes", 0):
                ctx.add("W105", fast_doc.name, fast_doc.fm_lines.get("minutes", 1), f"minutes.{key} is {have[key]}; the formula gives {out[key]}")
    return out


# ---------------------------------------------------------------- functions other modules call

def _hand_docs(entry) -> dict:
    sp, out = spec(), {}
    for fs in template(entry)["files"]:
        if fs.get("source") == "hand":
            path = common.BOOK / f"{entry['id']}-{entry['slug']}" / fs["name"]
            if path.exists():
                out[fs["name"]] = Doc(fs["name"], path.read_text(encoding="utf-8"), sp)
    return out


def sections(ch) -> dict:
    """{file: {section id: {heading, anchor, role, route, minutes, level, parent, line, planned}}} (TOOLS.md section 2)."""
    entry, out = _entry(ch), {}
    for name, doc in _hand_docs(entry).items():
        rows = out.setdefault(name, {})
        for h in doc.headings:
            if h["level"] not in (2, 3):
                continue
            parent = h["parent"] or {}
            flag = (h["flag"] or parent.get("flag") or {})
            rows.setdefault(h["id"], {
                "heading": h["title"], "anchor": h["anchor"], "role": flag.get("role"),
                "route": "pass" if h["level"] == 3 and h["pass"] else flag.get("route"),
                "minutes": h["minutes"], "level": h["level"], "parent": parent.get("id") if h["level"] == 3 else None,
                "line": h["line"], "planned": False})
    for s in (_brief(entry) or {}).get("sections", []):
        if not isinstance(s, dict) or not s.get("file") or not s.get("section"):
            continue
        rows = out.setdefault(s["file"], {})
        if s["section"] not in rows:
            rows[s["section"]] = {"heading": s.get("heading"), "anchor": None, "role": None, "route": None, "minutes": None,
                                  "level": None, "parent": None, "line": None, "planned": True}
    return out


def traps() -> dict:
    """Trap id to chapter id: hand files of every chapter, then brief traps that are in no hand file yet."""
    out, rx = {}, re.compile(r"<!--\s*trap:\s*([^\s>]+)\s*-->")
    chapters = common.chapters()
    for entry in chapters:
        folder = common.BOOK / f"{entry['id']}-{entry['slug']}"
        if not folder.is_dir():
            continue
        try:
            names = [fs["name"] for fs in template(entry)["files"] if fs.get("source") == "hand"]
        except SystemExit:
            names = [p.name for p in sorted(folder.glob("*.md"))]
        for name in names:
            path = folder / name
            if path.exists():
                for tid in rx.findall(path.read_text(encoding="utf-8")):
                    out.setdefault(tid, entry["id"])
    for entry in chapters:
        for t in (_brief(entry) or {}).get("traps", []):
            if isinstance(t, dict) and t.get("id"):
                out.setdefault(t["id"], entry["id"])
    return out


def a_list_facts(ch) -> list:
    """Fact ids linked in column 1 of the A-list numbers tables of the chapter."""
    entry, sp, out = _entry(ch), spec(), []
    href_rx = re.compile(sp["fact_links"]["href_regex"])
    for doc in _hand_docs(entry).values():
        for b in doc.blocks:
            if b.kind != "table" or b.extra.get("tkind") != "numbers":
                continue
            sub = (b.sub or {}).get("title")
            role = (b.sec or {}).get("role")
            if sub == "A-list" or (sub is None and role == "numbers"):
                for row in _table(b)[1]:
                    for _, href in _RE_LINK.findall(row[0] if row else ""):
                        m = href_rx.match(href)
                        if m and m.group(2) not in out:
                            out.append(m.group(2))
    return out


def _gate(name, entry, errors, warnings, counts, inputs) -> dict:
    rows = []
    for path in sorted({Path(p) for p in inputs}):
        if path.is_file():
            try:
                relp = str(path.resolve().relative_to(common.BOOK.resolve()))
            except ValueError:
                continue
            rows.append({"path": relp, "sha256": common.sha256_file(path)})
    return {"gate": name, "chapter": entry["id"], "ok": not errors,
            "exit": common.EXIT_FAIL if errors else (common.EXIT_WARN if warnings else common.EXIT_OK),
            "errors": errors, "warnings": warnings, "counts": counts, "inputs": rows}


def _item_inputs(entry) -> set:
    out = set()
    data = common.DATA / f"{entry['id']}-{entry['slug']}"
    for kind in ("questions", "cards", "speak", "tasks", "mock"):
        out.add(data / f"{kind}.json")
    if common.FACTS_DIR.is_dir():
        out.update(common.FACTS_DIR.glob("*.jsonl"))
    return out


def gate_lint(ch_id, quick=False, draft=False, **options) -> dict:
    entry = _entry(ch_id)
    report = lint_chapter(entry, draft=draft, strict=bool(options.get("strict")))
    return _gate("lint", entry, report["errors"], report["warnings"], report["counts"], report["_inputs"] | _item_inputs(entry))


def gate_sync(ch_id, quick=False, **options) -> dict:
    from saalib import _sync
    entry = _entry(ch_id)
    result = _sync.run(entry, check=True)
    errors = [_finding("X01", f, None, msg) for f, msg in result.get("invalid", [])]
    errors += [_finding("S01", f, None, "generated content is stale: run sync") for f in result["stale"]]
    errors += [_finding("S01", f, None, "generated file is missing: run sync") for f in result["missing"]]
    inputs = _item_inputs(entry) | {common.STYLE_DIR / "SPEC.json", common.DATA / "book.json", common.DATA / "terms.json"}
    inputs |= {common.BOOK / f for f in result.get("files", [])}
    return _gate("sync", entry, errors, [], {"checked": result["checked"], "stale": len(result["stale"]), "missing": len(result["missing"])}, inputs)


# ---------------------------------------------------------------- command line

def _text_report(report) -> str:
    lines = [f"lint {report['chapter']}: {'ok' if report['ok'] else 'FAIL'} errors={len(report['errors'])} warnings={len(report['warnings'])}"]
    for f in (report["errors"] + report["warnings"])[:40]:
        place = f"{f['file']}:{f['line']}" if f.get("file") and f.get("line") else (f.get("file") or f.get("item") or "chapter")
        lines.append(f"{place}: {f['code']} {f['msg']}")
    return "\n".join(lines)


def _public(report) -> dict:
    return {k: v for k, v in report.items() if not k.startswith("_")}


def cmd_lint(args) -> int:
    if args.all:
        rows, worst = [], common.EXIT_OK
        for entry in common.chapters():
            if not (common.BOOK / f"{entry['id']}-{entry['slug']}").is_dir():
                continue
            report = _public(lint_chapter(entry, draft=args.draft, strict=args.strict, strict_all=args.strict))
            common.write_json(common.REPORTS / "lint" / f"{entry['id']}.json", report)
            rows.append({"chapter": entry["id"], "ok": report["ok"], "errors": len(report["errors"]), "warnings": len(report["warnings"]),
                         "first": [f"{f['file']}:{f['line']}: {f['code']} {f['msg']}" for f in report["errors"][:3]]})
            code = common.EXIT_FAIL if report["errors"] else (common.EXIT_WARN if report["warnings"] else common.EXIT_OK)
            worst = common.EXIT_FAIL if common.EXIT_FAIL in (code, worst) else max(code, worst)
        result = {"ok": all(r["ok"] for r in rows), "chapters": rows}
        if args.json:
            common.emit(result, args)
        else:
            lines = [f"lint --all: {len(rows)} chapters, {sum(1 for r in rows if not r['ok'])} with errors"]
            lines += [f"{r['chapter']}: errors={r['errors']} warnings={r['warnings']}" + (f" | {r['first'][0]}" if r["first"] else "") for r in rows][:40]
            common.emit("\n".join(lines), args)
        return worst
    if not args.chapter:
        return common.fail("lint needs a chapter or --all", common.EXIT_PRECONDITION)
    report = _public(lint_chapter(args.chapter, draft=args.draft, strict=args.strict, only_file=args.file))
    if not args.file:
        common.write_json(common.REPORTS / "lint" / f"{report['chapter']}.json", report)
    common.emit(report if args.json else _text_report(report), args)
    return common.EXIT_FAIL if report["errors"] else (common.EXIT_WARN if report["warnings"] else common.EXIT_OK)


def cmd_sync(args) -> int:
    from saalib import _sync
    return _sync.cmd(args)


def register(subparsers) -> None:
    p = subparsers.add_parser("lint", help="check the hand-written files of a chapter against SPEC.json")
    p.add_argument("chapter", nargs="?", help="chapter id, slug or NN-slug")
    p.add_argument("--all", action="store_true", help="every chapter that has a folder")
    p.add_argument("--file", help="report only this file of the chapter, for example 2-deep.md")
    p.add_argument("--draft", action="store_true", help="rules marked (d) become warnings")
    p.add_argument("--strict", action="store_true", help="treat the front matter status as ready")
    common.add_common_args(p)
    p.set_defaults(func=cmd_lint)
    s = subparsers.add_parser("sync", help="generate the reader files and regions from the JSON items")
    s.add_argument("chapter", nargs="?", help="chapter id, slug or NN-slug")
    s.add_argument("--all", action="store_true", help="every chapter, the fact sheets and the glossary")
    s.add_argument("--check", action="store_true", help="write nothing; exit 1 when a file is stale or missing")
    s.add_argument("--only", nargs="+", default=None, metavar="KIND",
                   help="do, say, quiz, sources, tasks, plan, facts, glossary, exam-english, sheet")
    common.add_common_args(s)
    s.set_defaults(func=cmd_sync)
