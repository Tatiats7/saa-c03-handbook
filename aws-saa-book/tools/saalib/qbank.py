"""Question bank, flashcards, spoken answers, mock exams and domain drills.

Subcommands: q, cards, speak, mocks, drills (TOOLS-items.md section 7, TOOLS-rules.md R5).
Python API for other modules: items(ch, kind), gate_questions(ch), gate_questions_verified(ch),
gate_cards(ch), gate_speak(ch).

Standard library only. Paths are read as common.X at call time. The modules lint, facts, registry,
corpus and ledger are imported inside functions; when one of them (or one function) is missing,
a local fallback with the same contract is used, so this module always loads.
"""
from __future__ import annotations

import collections
import copy
import hashlib
import importlib
import json
import random
import re
from pathlib import Path

from saalib import common, schemas

KINDS = {"questions": ("question", "question", "q", 3), "cards": ("card", "card", "c", 3), "speak": ("speak", "speak", "s", 2)}
LABELS = "ABCDEF"
LENSES = ("closed", "open", "ambiguity")
PASSED = ("pass", "edited-pass")
PACK_ITEM_KEYS = {"id", "type", "select", "stem", "options"}
PACK_OPTION_KEYS = {"label", "text"}
STOP_WORDS = frozenset("""
a about after all also an and any are as at be because been before being between both but by can company could
did do does each for from had has have how if in into is it its more most must need needs new no not of on one
or other our out over same should so some such than that the their them then there these they this those through
to under until up use uses using want wants was were what when where which while who will with would you your
solution solutions meet meets requirement requirements
""".split())
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
_ARTICLES = frozenset("a an the of in to on for with between and or its your".split())
# gate-break fixes: rules in place of literal lists (H07, H10, H11)
_RE_META_OPTION = re.compile(r"(?<![A-Za-z])(?:(?:none|all|both|neither|either|any|each) of (?:the |these |those )?"
                             r"(?:above|options?|answers?|choices?|other options?|following)|(?:both|neither) [A-F] (?:and|nor) [A-F]"
                             r"|the (?:above|other) (?:options?|answers?|choices?))(?![A-Za-z])", re.I)
_RE_NEGATIVE_ASK = re.compile(r"(?<![A-Za-z])(?:which|what|who|where|when|how)(?![A-Za-z])[^?.]*(?<![A-Za-z])"
                              r"(?:(?:is|are|does|do|will|would) not|not (?:a|an|the|true|correct|valid|possible|required|meet)"
                              r"|except|incorrect|least likely)(?![A-Za-z])", re.I)
_RE_POSITION_REF = re.compile(r"\((?:[A-Fa-f])\)|(?<![A-Za-z])(?:first|second|third|fourth|fifth|sixth|last|next|previous) "
                              r"(?:option|answer|choice)(?![A-Za-z])|(?:^|[.;:,!?] )(?-i:[B-F]) (?:is|are|and|or|was|fails|works)(?![A-Za-z])"
                              r"|(?<![A-Za-z])(?:options?|answers?|choices?) (?:(?-i:[A-F])|[1-6])(?![A-Za-z0-9])", re.I)
INSTRUCTIONS = {
    "closed": "Closed book. For each item: read the stem only and write your solution in stem_only before you read the "
              "options. Then choose the answer labels. Use no sources. Set flag to one sentence when you see a second "
              "defensible answer or a missing constraint, else null.",
    "open": "Open book. Answer each item from the saved AWS pages and the fact canon only. Give citations for every "
            "label: why the key is right and why each other option is wrong. A citation is a fact id or "
            "{source_id, quote} with a verbatim quote. Set flag when a second answer is defensible, else null.",
    "ambiguity": "Ambiguity hunt. Choose the answer labels, then argue the strongest case for one wrong option in "
                 "case {label, text}. Set flag to one sentence when that case is defensible or a constraint is "
                 "missing, else null.",
}


# ---------------------------------------------------------------- small helpers

def _f(code, msg, item=None, file=None, line=None):
    return {"code": code, "file": file, "line": line, "item": item, "msg": msg}


def _fmt(f):
    where = f.get("item") or (f"{f.get('file')}:{f.get('line')}" if f.get("line") else f.get("file")) or "-"
    return f"{where}: {f['code']} {f['msg']}"


def _mod(name):
    import os
    if os.environ.get("SAA_QBANK_STANDALONE"):      # tests: force the local fallbacks
        return None
    try:
        return importlib.import_module(f"saalib.{name}")
    except Exception:
        return None


def _fn(module, name):
    mod = _mod(module)
    fn = getattr(mod, name, None) if mod is not None else None
    return fn if callable(fn) else None


def _holds(text, display):
    """lint.holds_display (a display must not sit inside a longer number); plain substring without lint."""
    fn = _fn("lint", "holds_display")
    return fn(text, display) if fn else bool(display) and display in text


def _strip_targets(text):
    return _LINK.sub(r"\1", text or "")


def _fb_word_count(text):
    return sum(1 for tok in _strip_targets(text).split() if re.search(r"[A-Za-z0-9]", tok))


def _wc(text):
    fn = _fn("lint", "word_count")
    if fn:
        try:
            return fn(text or "")
        except Exception:
            pass
    return _fb_word_count(text)


def _tokens(text):
    return [w for w in re.findall(r"[a-z]+", (text or "").lower()) if len(w) >= 3 and w not in STOP_WORDS]


def _jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a and b else 0.0


def _shingles(text, n=3):
    toks = _tokens(text)
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def _word_re(phrase, flags=re.I):
    return re.compile(r"(?<![A-Za-z0-9-])" + re.escape(phrase) + r"(?![A-Za-z0-9-])", flags)


def _rng(value):
    """A SPEC count: a number (exact) or {min, max}."""
    if isinstance(value, dict):
        return value.get("min", 0), value.get("max", 10 ** 9)
    if value is None:
        return 0, 10 ** 9
    return value, value


def _in(value, n):
    lo, hi = _rng(value)
    return lo <= n <= hi


def _sentences(text):
    return [s for s in re.split(r"(?<=[.?!:])\s+(?=[A-Z0-9\"'\x01])", text or "") if s.strip()]


def _spoken_sentences(text):
    return [s for s in re.split(r"(?<=[.?!])\s+", text or "") if s.strip()]


def _section_id(heading, spec):
    heading = re.sub(spec["headings"].get("time_box_regex", r" \(([0-9]{1,3}) min\)$"), "", heading.strip())
    return re.sub(r"[^a-z0-9 -]", "", heading.lower()).replace(" ", "-")


def _months_after(date, months):
    y, m, d = (int(x) for x in date[:10].split("-"))
    m += months
    y, m = y + (m - 1) // 12, (m - 1) % 12 + 1
    return f"{y:04d}-{m:02d}-{d:02d}"


def _label(args):
    import os
    return getattr(args, "by", None) or os.environ.get("SAA_AGENT") or "unknown"


def _emit(args, result, summary, findings=()):
    if getattr(args, "json", False):
        common.emit(result, args)
    else:
        common.emit("\n".join([summary] + [_fmt(f) for f in list(findings)[:40]]), args)


def _exit(errors, warnings):
    return common.EXIT_FAIL if errors else (common.EXIT_WARN if warnings else common.EXIT_OK)


def _read_input(path_text):
    """--file F: one object or an array, inside the book folder. Returns (items, exit code or None)."""
    path = Path(path_text)
    if not path.is_absolute():
        path = common.REPO / path
    if not common.inside_book(path):
        return None, common.fail(f"--file must be inside {common.REAL_BOOK}", common.EXIT_POLICY)
    if not path.exists():
        return None, common.fail(f"no file {path}", common.EXIT_PRECONDITION)
    try:
        obj = common.read_json(path)
    except ValueError as exc:
        return None, common.fail(f"{path}: not JSON ({exc})", common.EXIT_FAIL)
    return (obj if isinstance(obj, list) else [obj]), None


# ---------------------------------------------------------------- context (one per command; caches what it reads)

class Ctx:
    def __init__(self):
        self.spec = common.read_json(common.STYLE_DIR / "SPEC.json")
        if self.spec is None:
            raise SystemExit(common.fail("no SPEC.json", common.EXIT_PRECONDITION))
        self.inputs = {}
        self._c = {}
        self.note(common.STYLE_DIR / "SPEC.json")

    def note(self, path):
        path = Path(path)
        if path.is_file():
            try:
                relp = str(path.resolve().relative_to(common.BOOK.resolve()))
            except ValueError:
                return
            self.inputs[relp] = common.sha256_file(path)

    def gate_inputs(self):
        return [{"path": p, "sha256": s} for p, s in sorted(self.inputs.items())]

    def _get(self, key, make):
        if key not in self._c:
            self._c[key] = make()
        return self._c[key]

    # ---- registry
    @property
    def book(self):
        def make():
            self.note(common.DATA / "book.json")
            return common.load_book()
        return self._get("book", make)

    def chapters(self):
        return self.book["chapters"]

    def chapter(self, ch_id):
        ch_id = str(ch_id)
        for ch in self.chapters():
            if ch_id in (ch["id"], ch["slug"], f"{ch['id']}-{ch['slug']}"):
                return ch
        raise SystemExit(common.fail(f"unknown chapter {ch_id!r}", common.EXIT_PRECONDITION))

    def dirname(self, ch):
        return f"{ch['id']}-{ch['slug']}"

    def data_path(self, ch, kind):
        return common.DATA / self.dirname(ch) / f"{kind}.json"

    def data_rel(self, ch, kind):
        return f"data/{self.dirname(ch)}/{kind}.json"

    def doc(self, ch, kind):
        path = self.data_path(ch, kind)
        self.note(path)
        doc = common.read_json(path)
        if not isinstance(doc, dict) or not isinstance(doc.get("items"), list):
            return {"v": 1, "chapter": ch["slug"], "items": []} if doc is None else doc
        return doc

    def template(self, ch):
        def make():
            fn = _fn("lint", "template")
            if fn:
                try:
                    return fn(ch["id"])
                except Exception:
                    pass
            spec = self.spec
            key = ch.get("kind") or ch.get("tier")
            override = (spec.get("chapter_overrides") or {}).get(ch["id"]) or {}
            if override.get("template"):
                key = override["template"]
            base = copy.deepcopy((spec.get("templates") or {}).get(key) or {})

            def merge(a, b):
                for k, v in b.items():
                    if isinstance(v, dict) and isinstance(a.get(k), dict):
                        merge(a[k], v)
                    else:
                        a[k] = copy.deepcopy(v)
            merge(base, {k: v for k, v in override.items() if k != "template"})
            base["key"] = key
            return base
        return self._get(("tpl", ch["id"]), make)

    def counts(self, ch, kind):
        return ((self.template(ch).get("counts") or {}).get(kind)) or {}

    def is_mock(self, ch):
        return self.template(ch).get("key") == "mock" or ch.get("tier") == "mock" or ch.get("kind") == "mock"

    def mock_chapters(self):
        return [ch for ch in self.chapters() if self.is_mock(ch)]

    @property
    def guide(self):
        def make():
            path = common.REGISTRY / "exam-guide.json"
            self.note(path)
            fn = _fn("registry", "exam_guide")
            if fn:
                try:
                    return fn()
                except BaseException:
                    pass
            return common.read_json(path)
        return self._get("guide", make)

    @property
    def services_doc(self):
        def make():
            path = common.REGISTRY / "services.json"
            self.note(path)
            return common.read_json(path) or {}
        return self._get("services", make)

    @property
    def service_keys(self):
        def make():
            fn = _fn("registry", "service_keys_in_scope")
            if fn:
                try:
                    return set(fn())
                except BaseException:
                    pass
            if not self.services_doc:
                return None
            return {k for e in self.services_doc.get("in_scope", []) for k in e.get("keys", [])}
        return self._get("service_keys", make)

    @property
    def official_names(self):
        return [e["official_name"] for e in self.services_doc.get("in_scope", []) if e.get("official_name")]

    @property
    def terms(self):
        def make():
            self.note(common.DATA / "terms.json")
            return (common.read_json(common.DATA / "terms.json") or {}).get("terms", [])
        return self._get("terms", make)

    @property
    def exam_english(self):
        def make():
            self.note(common.DATA / "exam-english.json")
            doc = common.read_json(common.DATA / "exam-english.json") or {}
            return {w["id"]: w for g in doc.get("groups", []) for w in g.get("items", [])}
        return self._get("ee", make)

    # ---- facts
    @property
    def facts(self):
        def make():
            if common.FACTS_DIR.is_dir():
                for p in sorted(common.FACTS_DIR.glob("*.jsonl")):
                    self.note(p)
            fn = _fn("facts", "load")
            if fn:
                try:
                    return fn()
                except BaseException:
                    pass
            out = {}
            if common.FACTS_DIR.is_dir():
                for p in sorted(common.FACTS_DIR.glob("*.jsonl")):
                    for row in common.read_jsonl(p):
                        out[row["id"]] = row
            return out
        return self._get("facts", make)

    def verified(self, fid):
        fact = self.facts.get(fid)
        return bool(fact) and fact.get("status") == "verified"

    def displays(self, fid):
        fact = self.facts.get(fid)
        if not fact:
            return []
        fn = _fn("facts", "displays")
        if fn:
            try:
                return list(fn(fact))
            except Exception:
                pass
        return [common.normalize_text(v.get("display", "")) for v in fact.get("values", []) if v.get("display")]

    def spoken(self, fid):
        fact = self.facts.get(fid) or {}
        return [common.normalize_text(v["spoken"]) for v in fact.get("values", []) if v.get("spoken")]

    def is_volatile(self, fid):
        fact = self.facts.get(fid)
        if not fact:
            return False
        fn = _fn("facts", "is_volatile")
        if fn:
            try:
                return bool(fn(fact))
            except Exception:
                pass
        if fact.get("volatility") == "frequently-changing" or fact.get("kind") == "price":
            return True
        date = (fact.get("changed") or {}).get("date")
        snap = (self.book.get("book") or {}).get("snapshot_date") or common.today()
        months = self.spec["questions"].get("volatile_window_months", 24)
        return bool(date) and _months_after(date if len(date) >= 10 else date + "-01", months) >= snap

    def fact_ids_in(self, text):
        rx = re.compile(self.spec["fact_links"]["href_regex"])
        out = []
        for _, href in _LINK.findall(text or ""):
            m = rx.match(href)
            if m:
                out.append(m.group(2))
        return out

    def question_volatile(self, item):
        texts = [item.get("explanation", "")] + [o.get("why", "") for o in item.get("options", []) if o.get("correct")]
        return any(self.is_volatile(fid) for t in texts for fid in self.fact_ids_in(t))

    # ---- hand files: sections, traps, A-list
    def _hand_files(self, ch):
        d = common.BOOK / self.dirname(ch)
        marker = self.spec["generated_regions"]["generated_file_first_line"]
        out = []
        if d.is_dir():
            for p in sorted(d.glob("*.md")):
                text = p.read_text(encoding="utf-8")
                self.note(p)
                if not text.startswith(marker):
                    out.append((p, text))
        return out

    def _brief(self, ch):
        path = common.BUILD / "work" / self.dirname(ch) / "brief.json"
        self.note(path)
        return common.read_json(path) or {}

    def sections(self, ch):
        def make():
            hand = self._hand_files(ch)   # also records the inputs
            self._brief(ch)
            fn = _fn("lint", "sections")
            if fn:
                try:
                    return fn(ch["id"])
                except Exception:
                    pass
            out = {}
            for p, text in hand:
                secs, code = {}, False
                for n, line in enumerate(text.splitlines(), 1):
                    if line.startswith("```"):
                        code = not code
                    m = None if code else re.match(r"^(#{2,3}) (.+?)\s*$", line)
                    if m:
                        secs[_section_id(m.group(2), self.spec)] = {"heading": m.group(2), "level": len(m.group(1)), "line": n, "planned": False}
                out[p.name] = secs
            for s in self._brief(ch).get("sections", []) or []:
                if s.get("file") and s.get("section"):
                    out.setdefault(s["file"], {}).setdefault(s["section"], {"heading": s.get("heading"), "planned": True})
            return out
        return self._get(("sections", ch["id"]), make)

    def section_ok(self, ch, section, need_prefix=False, null_ok=False):
        if section is None:
            return null_ok
        m = re.match(r"^(?:([0-9]{2}-[a-z0-9-]+)/)?([a-z0-9-]+\.md)#([a-z0-9-]+)$", section)
        if not m:
            return False
        if m.group(1):
            target = next((c for c in self.chapters() if self.dirname(c) == m.group(1)), None)
            if target is None:
                return False
        elif need_prefix:
            return False
        else:
            target = ch
        return m.group(3) in (self.sections(target).get(m.group(2)) or {})

    @property
    def traps(self):
        def make():
            for ch in self.chapters():
                self._hand_files(ch)
                self._brief(ch)
            fn = _fn("lint", "traps")
            if fn:
                try:
                    return dict(fn())
                except Exception:
                    pass
            out = {}
            for ch in self.chapters():
                for _, text in self._hand_files(ch):
                    for tid in re.findall(r"<!--\s*trap:\s*([a-z0-9-]+)\s*-->", text):
                        out.setdefault(tid, ch["id"])
                for t in self._brief(ch).get("traps", []) or []:
                    if t.get("id"):
                        out.setdefault(t["id"], ch["id"])
            return out
        return self._get("traps", make)

    def a_list(self, ch):
        def make():
            hand = self._hand_files(ch)
            fn = _fn("lint", "a_list_facts")
            if fn:
                try:
                    return list(fn(ch["id"]))
                except Exception:
                    pass
            out = []
            for _, text in hand:
                inside = False
                for line in text.splitlines():
                    if line.startswith("#"):
                        inside = bool(re.match(r"^###\s+A-list\b", line))
                    elif inside and line.startswith("|"):
                        cells = [c.strip() for c in line.strip().strip("|").split("|")]
                        for fid in self.fact_ids_in(cells[0] if cells else ""):
                            if fid not in out:
                                out.append(fid)
            return out
        return self._get(("alist", ch["id"]), make)

    # ---- corpus
    def url_in_corpus(self, url):
        corpus = _mod("corpus")
        if corpus is not None:
            try:
                if corpus.load_meta(corpus.source_id_for(url)) is not None:
                    return True
            except Exception:
                pass

        def make():
            urls = set()
            snap = common.CORPUS / "snap"
            if snap.is_dir():
                for p in snap.rglob("*.meta.json"):
                    try:
                        urls.add((common.read_json(p) or {}).get("url"))
                    except ValueError:
                        pass
            return urls
        return url in self._get("corpus_urls", make)

    def corpus_text(self, source_id):
        corpus = _mod("corpus")
        if corpus is not None:
            try:
                text = corpus.load_text(source_id)
                if text is not None:
                    return text
            except Exception:
                pass
        if not re.match(r"^[A-Za-z0-9._/-]+$", source_id or "") or ".." in source_id:
            return None
        path = common.CORPUS / "snap" / (source_id + ".txt")
        return path.read_text(encoding="utf-8") if path.is_file() else None

    # ---- text rules
    def nwu(self, singular=False):
        def make():
            n = self.spec["lint"]["number_with_unit"]
            units = set(n["units"])
            nouns = set(n["count_nouns"])
            if singular:
                for x in list(nouns):
                    if x.endswith("ves"):
                        nouns.add(x[:-3] + "f")
                    if x.endswith("ies"):
                        nouns.add(x[:-3] + "y")
                    elif x.endswith("s"):
                        nouns.add(x[:-1])
            u = "|".join(re.escape(x) for x in sorted(units, key=len, reverse=True))
            c = "|".join(re.escape(x) for x in sorted(nouns, key=len, reverse=True))
            unit = r"(?:[ -]?(?:" + u + r")|[ -]?(?i:" + c + r"))(?![A-Za-z])"
            num = r"[0-9][0-9,]*(?:\.[0-9]+)?"
            full = re.compile(r"(?<![A-Za-z0-9.,])(?<![a-z]-)(?:\$" + num + r"|(" + num + r")" + unit + r")")
            return full, re.compile(r"^" + unit)
        return self._get(("nwu", singular), make)

    def absolute(self):
        def make():
            words = sorted(self.spec["lint"]["absolute_words"], key=len, reverse=True)
            return re.compile(r"(?<![A-Za-z0-9-])(?:" + "|".join(re.escape(w) for w in words) + r")(?![A-Za-z0-9-])", re.I)
        return self._get("abs", make)

    def banned_hits(self, text):
        def make():
            out = []
            for w in self.spec["lint"].get("banned_words", {}):
                out.append((w, _word_re(w, 0 if w == "may" else re.I)))
            return out
        text = _strip_targets(text)
        return [w for w, rx in self._get("banned", make) if rx.search(text)]

    def link_findings(self, text):
        """L301 to L303 for the links of one text field (local form)."""
        out = []
        rx = re.compile(self.spec["fact_links"]["href_regex"])
        for label, href in _LINK.findall(text or ""):
            m = rx.match(href)
            if not m:
                out.append(_f("L301", f"link {href} is not a fact link"))
                continue
            fact = self.facts.get(m.group(2))
            if not fact or fact.get("service") != m.group(1):
                out.append(_f("L301", f"fact {m.group(2)} does not resolve"))
            elif fact.get("status") != "verified":
                out.append(_f("L302", f"fact {m.group(2)} is {fact.get('status')}, not verified"))
            elif not any(_holds(common.normalize_text(label), d) for d in self.displays(m.group(2))):
                out.append(_f("L303", f"link text holds no value of {m.group(2)}"))
        return out

    def strict(self, text, where, stem=None):
        """lint.check_strict_text, or the local form of L301 to L305."""
        fn = _fn("lint", "check_strict_text")
        if fn:
            try:
                return list(fn(text, where, stem=stem))
            except Exception:
                pass
        out = self.link_findings(text)
        stem_numbers = {n.replace(",", "") for n in re.findall(r"[0-9][0-9,]*(?:\.[0-9]+)?", stem or "")}
        full, _ = self.nwu()
        marked = _LINK.sub(lambda m: "\x01" + m.group(1) + "\x02", text or "")
        for sent in _sentences(marked):
            if "\x01" in sent or sent.rstrip().endswith("?"):
                continue
            hit = None
            for m in full.finditer(sent):
                if m.group(1) is None or m.group(1).replace(",", "").rstrip(".") not in stem_numbers:
                    hit = m.group(0)
                    break
            if hit is None:
                m = self.absolute().search(sent)
                hit = m.group(0) if m else None
            if hit is not None:
                out.append(_f("L304", f"'{hit}' in a sentence without a fact link"))
        return out

    def numbers_outside_displays(self, text, fact_ids):
        full, _ = self.nwu()
        displays = [d for fid in fact_ids for d in self.displays(fid)]
        bad = []
        for m in full.finditer(_strip_targets(text)):
            # lint.holds_display: `0 widgets` is a substring of the display `50 widgets` but not the same number
            if not any(_holds(d, common.normalize_text(m.group(0))) for d in displays):
                bad.append(m.group(0))
        # gate-break H35: a number in words before a unit (`ninety widgets`) is a number too; it stands in a
        # display or in a spoken form of a fact of the item
        said = displays + [s for fid in fact_ids for s in self.spoken(fid)]
        for sent in _spoken_sentences(_strip_targets(text)):
            for phrase in spoken_numbers(self, sent):
                first = re.split(r"[ -]", phrase)
                small = first[0] in _SMALL_NUMBER_WORDS and (len(first) < 2 or first[1] not in _BIG_NUMBER_WORDS)
                if not small and not any(phrase in d for d in said):     # a small count in words is story text (R2)
                    bad.append(phrase)
        return bad

    # ---- the whole bank
    def bank(self):
        def make():
            out = []
            for ch in self.chapters():
                if self.data_path(ch, "questions").exists():
                    for it in self.doc(ch, "questions").get("items", []):
                        if isinstance(it, dict):
                            out.append((ch, it))
            return out
        return self._get("bank", make)


def _active(items):
    return [i for i in items if isinstance(i, dict) and i.get("status") not in ("rejected", "retired")]


# ---------------------------------------------------------------- question item rules (Q101 to Q116)

def _text_fields(item):
    """(name, text) of every text field outside stem and option text."""
    out = [("explanation", item.get("explanation")), ("takeaway", item.get("takeaway")), ("twin", item.get("twin")), ("say", item.get("say"))]
    for o in item.get("options", []):
        out.append((f"options[{o.get('id')}].why", o.get("why")))
        out.append((f"options[{o.get('id')}].misconception", o.get("misconception")))
    for i, step in enumerate((item.get("worked") or {}).get("steps", []), 1):
        out.append((f"worked.steps[{i}]", step))
    return [(n, t) for n, t in out if isinstance(t, str) and t]


def q_item_rules(ctx, ch, item, siblings, pos):
    """Findings of the blocking item rules. `siblings` is the file order; `pos` the item's index in it."""
    Q = ctx.spec["questions"]
    out = []
    qid = item.get("id") if isinstance(item, dict) else None
    rel = ctx.data_rel(ch, "questions")

    def add(code, msg):
        out.append(_f(code, msg, item=qid, file=rel))

    errs = schemas.validate(item, "question", "question")
    if errs:
        for e in errs[:8]:
            add("Q101", "schema: " + e)
        return out
    slug = ch["slug"]
    if not item["id"].startswith(slug + "-q") or item["chapter"] != slug:
        add("Q101", f"id and chapter must use the slug {slug}")
    if (item["pool"] == "mock") != ctx.is_mock(ch):
        add("Q101", "pool is mock exactly in mock chapters")

    stem = item["stem"]
    opts = item["options"]
    correct = [o for o in opts if o["correct"]]
    wrong = [o for o in opts if not o["correct"]]
    typ, sel, diff = item["type"], item["select"], item["difficulty"]

    # Q102
    want = Q["options"].get("single") if typ == "single" else Q["options"].get(f"multi_select_{sel}")
    if sel not in Q["select_allowed"] or (typ == "single") != (sel == 1):
        add("Q102", f"type {typ} with select {sel}")
    if want is None or len(opts) != want:
        add("Q102", f"{len(opts)} options; a {typ} question with select {sel} has {want}")
    if len(correct) != sel:
        add("Q102", f"{len(correct)} correct options, select is {sel}")
    if len({o["id"] for o in opts}) != len(opts):
        add("Q102", "option ids are not unique")
    texts = [common.normalize_text(o["text"]).rstrip(". ") for o in opts]
    for n, text in enumerate(texts):        # gate-break H03: the same text twice is a second correct answer
        if text in texts[:n]:
            add("Q102", f"option {opts[n]['id']} has the same text as option {opts[texts.index(text)]['id']}")
    instr = Q["multi_instruction"]
    if typ == "multi":
        if not stem.rstrip().endswith(instr.get(str(sel), "\x00")):
            add("Q102", f"a multi stem with select {sel} ends with {instr.get(str(sel))}")
    elif any(i in stem for i in instr.values()) or re.search(r"\(Select [A-Z]+\.\)", stem):
        add("Q102", "a single stem holds a select instruction")

    # Q103
    def words(name, text, key):
        n = _wc(text)
        if not _in(Q[key], n):
            lo, hi = _rng(Q[key])
            add("Q103", f"{name} has {n} words; allowed {lo} to {hi}")
        return n
    words("stem", stem, "stem_words")
    opt_key = "option_words_difficulty_1" if diff == 1 and "option_words_difficulty_1" in Q else "option_words"
    lengths = [words(f"option {o['id']}", o["text"], opt_key) for o in opts]
    total = words("explanation", item["explanation"], "explanation_words")
    for o in opts:
        total += words(f"why of option {o['id']}", o["why"], "why_words")
    words("takeaway", item["takeaway"], "takeaway_words")
    total += words("twin", item["twin"], "twin_words")
    if not _in(Q["explanation_total_words"], total):
        lo, hi = _rng(Q["explanation_total_words"])
        add("Q103", f"explanation total has {total} words; allowed {lo} to {hi}")

    # Q104
    mean = sum(lengths) / len(lengths)
    if mean >= Q["option_length_spread_applies_from_mean_words"]:
        for o, n in zip(opts, lengths):
            if abs(n - mean) / mean > Q["option_length_spread_max"]:
                add("Q104", f"option {o['id']} has {n} words; the mean is {mean:.1f}")
    # gate-break H04, H05: the key must not stand out by its length alone, at any mean (the mean hides it: the
    # long key pulls the mean up, and short options are below the mean rule)
    if correct and wrong:
        klen = [n for o, n in zip(opts, lengths) if o["correct"]]
        wlen = [n for o, n in zip(opts, lengths) if not o["correct"]]
        spread = Q["option_length_spread_max"]
        if min(klen) - max(wlen) >= 3 and (min(klen) - max(wlen)) / max(wlen) > spread:
            add("Q104", f"the key ({min(klen)} words) is longer than every wrong option (at most {max(wlen)} words)")
        elif min(wlen) - max(klen) >= 3 and (min(wlen) - max(klen)) / max(max(klen), 1) > spread:
            add("Q104", f"the key ({max(klen)} words) is shorter than every wrong option (at least {min(wlen)} words)")

    # Q105
    for o in opts:
        for phrase in Q["banned_in_options"]:
            if _word_re(phrase).search(o["text"]):
                add("Q105", f"'{phrase}' in option {o['id']}")
        m = _RE_META_OPTION.search(o["text"])       # gate-break H11: `None of these options.`
        if m:
            add("Q105", f"'{m.group(0)}' in option {o['id']}: an option does not point at other options")
    ask = _sentences(stem)[-2:] if typ == "multi" else _sentences(stem)[-1:]
    if (re.search(Q["negative_stem_regex"], stem) or any(_RE_NEGATIVE_ASK.search(s) for s in ask)) \
            and not ctx.template(ch).get("allow_negative_stems"):
        add("Q105", "negative stem")                # gate-break H10: also `which ... is not ...` in lowercase
    letter = re.compile(Q["letter_reference_regex"])
    for name, text in [("stem", stem)] + [(f"options[{o['id']}].text", o["text"]) for o in opts] + _text_fields(item):
        m = letter.search(text)
        if m:
            add("Q105", f"{name} names an option letter ('{m.group(0)}')")
    for name, text in _text_fields(item):           # gate-break H07: `the second option`, `(C)`, `B is the usual trap`
        m = _RE_POSITION_REF.search(text)
        if m:
            add("Q105", f"{name} names an option by its position or letter ('{m.group(0).strip()}'); options have no "
                        "fixed order")

    # Q106
    qual = item["qualifier"]
    qwords = Q["qualifier_words"]
    caps = re.findall(r"\b(?:" + "|".join(qwords) + r")\b", stem)
    if len(caps) > Q["qualifiers_per_stem"]["max"]:
        add("Q106", f"{len(caps)} qualifier words in the stem")
    none = Q.get("no_qualifier_value", "none")
    if qual == none:
        if diff != Q["no_qualifier_only_at_difficulty"]:
            add("Q106", f"qualifier none at difficulty {diff}")
    else:
        if qual not in stem:
            add("Q106", "the qualifier does not stand verbatim in the stem")
        if not qual.split() or qual.split()[0] not in qwords:
            add("Q106", "the qualifier does not start with a qualifier word")

    # Q107
    kw = Q["keywords"]
    if not kw["min"] <= len(item["keywords"]) <= kw["max"]:
        add("Q107", f"{len(item['keywords'])} keywords")
    for k in item["keywords"]:
        if k not in stem:
            add("Q107", f"keyword '{k}' is not in the stem")

    # Q108
    for o in wrong:
        if not (o["trap"] or o["misconception"]) or not o["distractor_type"]:
            add("Q108", f"wrong option {o['id']} needs a trap or a misconception, and a distractor_type")
    for o in correct:
        if o["trap"] or o["misconception"] or o["distractor_type"]:
            add("Q108", f"correct option {o['id']} has a trap, misconception or distractor_type")
    impossible = [o for o in wrong if o["distractor_type"] == "impossible-feature"]
    if len(impossible) > Q["impossible_feature_max_per_question"]:
        add("Q108", f"{len(impossible)} impossible-feature options")
    if Q.get("impossible_feature_needs_fact"):
        for o in impossible:
            if not ctx.fact_ids_in(o["why"]):
                add("Q108", f"the why of impossible-feature option {o['id']} links no fact")
    violates = [o for o in wrong if o["distractor_type"] == "violates-qualifier"]
    if qual == none and violates:
        add("Q108", "a question without a qualifier has a violates-qualifier option")
    if qual != none and diff >= Q["violates_qualifier_min_from_difficulty"] and not violates:
        add("Q108", f"difficulty {diff} needs a violates-qualifier option")

    # Q109
    for o in opts:
        if o["trap"] and o["trap"] not in ctx.traps:
            add("Q109", f"unknown trap id {o['trap']}")

    # Q110
    for fid in item["facts"]:
        if fid not in ctx.facts:
            add("Q110", f"fact {fid} does not resolve")
        elif not ctx.verified(fid):
            add("Q110", f"fact {fid} is {ctx.facts[fid].get('status')}, not verified")
    strict = [("explanation", item["explanation"]), ("takeaway", item["takeaway"]), ("twin", item["twin"])]
    strict += [(f"options[{o['id']}].why", o["why"]) for o in opts]
    linked = set()
    for name, text in strict:
        linked.update(ctx.fact_ids_in(text))
        if name == "twin" and Q.get("twin_quoted_phrase_exempt") and text.startswith(Q["twin_prefix"]):
            text = Q["twin_prefix"] + re.sub(r'^"[^"]*"', "", text[len(Q["twin_prefix"]):])
        for f in ctx.strict(text, f"{qid}.{name}", stem=stem if Q.get("stem_numbers_exempt_in_strict_fields") else None):
            if f.get("code") != "L801":
                add("Q110", f"{name}: {f.get('code')} {f.get('msg')}")
    for step in (item.get("worked") or {}).get("steps", []):
        linked.update(ctx.fact_ids_in(step))
        for f in ctx.link_findings(step):
            add("Q110", f"worked.steps: {f['code']} {f['msg']}")
    if not ctx.fact_ids_in(item["explanation"]):
        add("Q110", "the explanation holds no fact link")
    for fid in sorted(linked - set(item["facts"])):
        add("Q110", f"linked fact {fid} is not in facts")
    nolink = [("stem", stem), ("say", item.get("say") or "")] + [(f"options[{o['id']}].text", o["text"]) for o in opts] + [("keywords", k) for k in item["keywords"]]
    for name, text in nolink:
        if re.search(r"\]\(|https?://", text):
            add("Q110", f"{name} holds a link")

    # Q111
    guide = ctx.guide or {}
    tasks = {t["id"]: t for t in guide.get("tasks", [])}
    bullets = {b["id"]: b for b in guide.get("bullets", [])}
    if item["task"] not in tasks or not item["task"].startswith(f"{item['domain']}."):
        add("Q111", f"task {item['task']} is not a task statement of domain {item['domain']}")
    for b in item["bullets"]:
        if b not in bullets or bullets[b].get("task") != item["task"]:
            add("Q111", f"bullet {b} does not belong to task {item['task']}")
    keys = ctx.service_keys
    if keys is not None:
        for s in item["services"]:
            if s not in keys:
                add("Q111", f"service {s} is not an in-scope key")
    for t in item["topics"]:
        if t not in Q["topics"]:
            add("Q111", f"unknown topic {t}")
    if not ctx.section_ok(ch, item["section"], need_prefix=item["pool"] in ("mock", "drill")):
        add("Q111", f"section {item['section']} does not resolve" + (" (pool mock and drill need '<NN-slug>/<file>#<section id>')" if item["pool"] != "chapter" else ""))
    evidence = {e.get("url") for fid in item["facts"] for e in (ctx.facts.get(fid) or {}).get("evidence", [])}
    for s in item["sources"]:
        if s["url"] not in evidence and not ctx.url_in_corpus(s["url"]):
            add("Q111", f"source {s['url']} is not in the corpus")
    for eid in item.get("exam_english", []):
        word = ctx.exam_english.get(eid)
        if not word or not any(_word_re(w).search(stem) for w in [word["word"]] + list(word.get("also", []))):
            add("Q111", f"exam-English word {eid} is not in the stem")

    # Q112
    if item["volatile"] or ctx.question_volatile(item):
        add("Q112", "the key depends on a volatile fact")

    # Q113
    if correct and wrong:
        st = _tokens(stem)
        key_overlap = _jac(st, _tokens(" ".join(o["text"] for o in correct)))
        wrong_overlap = max(_jac(st, _tokens(o["text"])) for o in wrong)
        if key_overlap - wrong_overlap > Q["stem_key_overlap_margin_max"]:
            add("Q113", f"the stem repeats the words of the key (overlap {key_overlap:.2f}, best wrong option {wrong_overlap:.2f})")
        else:
            # gate-break H06: a long stem dilutes the Jaccard value. Also measure the share of the key's own
            # words that stand in the stem, which does not depend on the length of the stem.
            def cover(text):
                toks = set(_tokens(text))
                return len(toks & set(st)) / len(toks) if len(toks) >= 4 else 0.0
            key_cover = cover(" ".join(o["text"] for o in correct))
            wrong_cover = max(cover(o["text"]) for o in wrong)
            if key_cover >= 0.7 and key_cover - wrong_cover > max(Q["stem_key_overlap_margin_max"], 0.4):
                add("Q113", f"the key is made of stem words ({key_cover:.2f} of its words; best wrong option {wrong_cover:.2f})")

    # Q114
    if not item["twin"].startswith(Q["twin_prefix"]):
        add("Q114", f"twin does not start with '{Q['twin_prefix']}'")
    if item["twin_of"]:
        idx = next((i for i, s in enumerate(siblings[:pos]) if isinstance(s, dict) and s.get("id") == item["twin_of"]), None)
        if idx is None:
            add("Q114", f"twin_of {item['twin_of']} is not an earlier question of the chapter")
        else:
            other = siblings[idx]
            if other.get("twin_of"):
                add("Q114", "the earlier question of a twin pair has twin_of null")
            if other.get("layer") != item["layer"]:
                add("Q114", "twins have the same layer")
            if {o.get("text") for o in other.get("options", []) if o.get("correct")} == {o["text"] for o in correct}:
                add("Q114", "twins have different correct options")
            if pos - idx - 1 < Q.get("twin_min_questions_between", 0):
                add("Q114", f"{pos - idx - 1} questions between the twins; at least {Q['twin_min_questions_between']}")
    worked = item.get("worked")
    if worked:
        steps = worked["steps"]
        starters = Q["worked_step_starters"]
        if len(steps) != Q["worked_steps"]:
            add("Q114", f"{len(steps)} worked steps")
        for i, (step, start) in enumerate(zip(steps, starters), 1):
            if not step.startswith(start):
                add("Q114", f"worked step {i} does not start with '{start}'")
        n = sum(_wc(s) for s in steps)
        if not _in(Q["worked_words"], n):
            add("Q114", f"the think-aloud has {n} words")
        marker = Q["worked_wrong_path_marker"]
        in5 = len(steps) >= 5 and marker in steps[4]
        elsewhere = any(marker in s for i, s in enumerate(steps) if i != 4)
        if in5 != bool(worked["wrong_path"]) or elsewhere:
            add("Q114", "the wrong-path marker stands in step 5 exactly when wrong_path is true")

    # Q115
    for name, text in _text_fields(item):
        for w in ctx.banned_hits(text):
            add("Q115", f"banned word '{w}' in {name}")

    # Q116
    if item["pool"] in ("chapter", "drill") and not item["bullets"]:
        add("Q116", "a question of pool chapter or drill lists at least one bullet")
    return out


def _verification_passed(item):
    return (item.get("verification") or {}).get("status") in PASSED


def _twin_pairs(items):
    ids = {i.get("id") for i in items}
    return [(i["twin_of"], i["id"]) for i in items if i.get("twin_of") in ids]


def _q202(ctx, items):
    Q = ctx.spec["questions"]
    out = []
    singles = [i for i in items if i.get("type") == "single" and any(o.get("correct") for o in i.get("options", []))]
    if len(items) >= 10 and singles:
        pos = collections.Counter(next(n for n, o in enumerate(i["options"]) if o.get("correct")) for i in singles)
        n, top = pos.most_common(1)[0][1], pos.most_common(1)[0][0]
        if n / len(singles) > Q["key_position_share_max"]:
            out.append(f"position {top + 1} holds the key in {n} of {len(singles)} questions")
        longest = 0
        for i in singles:
            key = max(_wc(o["text"]) for o in i["options"] if o.get("correct"))
            if key > max(_wc(o["text"]) for o in i["options"] if not o.get("correct")):
                longest += 1
        if longest / len(singles) > Q["key_is_longest_share_max"]:
            out.append(f"the key is the longest option in {longest} of {len(singles)} questions")
    return out


def q_chapter_rules(ctx, ch, items, ship=False, verified=False):
    """(errors, warnings) of Q201 to Q206 for the items of one chapter."""
    Q = ctx.spec["questions"]
    rel = ctx.data_rel(ch, "questions")
    errors, warnings = [], []

    def soft(code, msg):
        (errors if ship else warnings).append(_f(code, msg, file=rel))

    live = [i for i in _active(items) if i.get("pool") != "drill"]
    counts = ctx.counts(ch, "questions")
    shipped = counts.get("shipped", 0)
    if not ship:
        if len(live) < shipped:
            soft("Q201", f"{len(live)} questions; the chapter ships {shipped}")
    else:
        ready = [i for i in live if i.get("status") == "ready"]
        checks = [("ready", len(ready), shipped),
                  ("core", sum(1 for i in ready if i.get("layer") == "core"), counts.get("core")),
                  ("extended", sum(1 for i in ready if i.get("layer") == "extended"), counts.get("extended")),
                  ("twin pairs", len(_twin_pairs(ready)), {"min": counts.get("twin_pairs_min", 0)}),
                  ("multi", sum(1 for i in ready if i.get("type") == "multi"), counts.get("multi")),
                  ("worked", sum(1 for i in ready if i.get("worked")), counts.get("worked")),
                  ("worked wrong-path", sum(1 for i in ready if (i.get("worked") or {}).get("wrong_path")), counts.get("worked_wrong_path"))]
        for name, n, want in checks:
            if want is not None and not _in(want, n):
                lo, hi = _rng(want)
                soft("Q201", f"{name}: {n}; needed {lo}" + ("" if lo == hi else (" or more" if hi >= 10 ** 9 else f" to {hi}")))
    for msg in _q202(ctx, live):
        soft("Q202", msg)
    by_concept = collections.defaultdict(list)
    for i in live:
        by_concept[i.get("concept")].append(i)
    for concept, group in sorted(by_concept.items(), key=lambda kv: str(kv[0])):
        if len(group) > Q["questions_per_concept_max"]:
            soft("Q203", f"{len(group)} questions on concept {concept}")
        if Q.get("unique_concept_trap_pair"):
            for a in range(len(group)):
                for b in range(a + 1, len(group)):
                    x, y = group[a], group[b]
                    if x.get("twin_of") == y.get("id") or y.get("twin_of") == x.get("id"):
                        continue
                    tx = {o.get("trap") for o in x.get("options", []) if o.get("trap")}
                    ty = {o.get("trap") for o in y.get("options", []) if o.get("trap")}
                    if tx == ty:
                        soft("Q203", f"{x.get('id')} and {y.get('id')} have the same concept and the same traps")
    if live:
        none = sum(1 for i in live if i.get("qualifier") == Q.get("no_qualifier_value", "none"))
        if none / len(live) > Q["no_qualifier_share_max"]:
            errors.append(_f("Q204", f"{none} of {len(live)} questions have no qualifier", file=rel))
        tol = Q.get("difficulty_mix_tolerance", 0.1)
        for d, share in sorted(Q.get("difficulty_mix", {}).items()):
            have = sum(1 for i in live if str(i.get("difficulty")) == d) / len(live)
            if abs(have - share) > tol + 1e-9:
                warnings.append(_f("Q204", f"difficulty {d}: share {have:.2f}, target {share:.2f}", file=rel))
        wrong = [o for i in live for o in i.get("options", []) if not o.get("correct")]
        if wrong and sum(1 for o in wrong if o.get("trap")) / len(wrong) < Q["trap_share_min"]:
            soft("Q205", f"{sum(1 for o in wrong if o.get('trap'))} of {len(wrong)} wrong options carry a trap id")
    if verified:
        for i in items:
            if i.get("status") == "ready" and not _verification_passed(i):
                errors.append(_f("Q206", "ready without a passed verification", item=i.get("id"), file=rel))
    return errors, warnings


def _wrapper_findings(ctx, ch, kind, doc):
    rel = ctx.data_rel(ch, kind)
    out = []
    if not isinstance(doc, dict) or doc.get("v") != 1 or not isinstance(doc.get("items"), list) or doc.get("chapter") != ch["slug"]:
        out.append(_f("X01", f"wrapper must be {{v: 1, chapter: {ch['slug']}, items: []}}", file=rel))
    elif set(doc) - {"v", "chapter", "items"}:
        out.append(_f("X01", "unknown key in the wrapper", file=rel))
    return out


def _items_of(doc):
    return [i for i in (doc.get("items") if isinstance(doc, dict) else None) or [] if isinstance(i, dict)]


def _status_counts(items, extra):
    c = {"total": len(items)}
    for s in ("candidate", "verified", "ready", "rejected"):
        c[s] = sum(1 for i in items if i.get("status") == s)
    c.update(extra)
    return c


def rejected_duplicate(ctx, ch, item, threshold=0.6):
    """The id of a rejected question that `item` repeats, or None (gate-break H24): a rejected question does not
    come back under a new id. Reads the rejected items of the chapter file and _build/qbank/rejected.jsonl."""
    mine = _print(item)
    old = [q for _c, q in ctx.bank() if q.get("status") == "rejected"]
    try:
        old += [q for q in common.read_jsonl(common.BUILD / "qbank" / "rejected.jsonl") if isinstance(q, dict)]
    except ValueError:
        pass
    for q in old:
        if q.get("id") != item.get("id") and similarity(mine, _print(q), threshold)[1]:
            return q.get("id")
    return None


def q_lint(ctx, ch, ship=False, verified=False, dupes=True):
    doc = ctx.doc(ch, "questions")
    errors = _wrapper_findings(ctx, ch, "questions", doc) if ctx.data_path(ch, "questions").exists() else []
    items = _items_of(doc)
    warnings = []
    seen = set()
    for pos, item in enumerate(items):
        if item.get("id") in seen:
            errors.append(_f("Q301", "duplicate id", item=item.get("id"), file=ctx.data_rel(ch, "questions")))
        seen.add(item.get("id"))
        if item.get("status") in ("rejected", "retired"):
            continue
        errors += q_item_rules(ctx, ch, item, items, pos)
    e, w = q_chapter_rules(ctx, ch, items, ship=ship, verified=verified)
    errors += e
    warnings += w
    if dupes:       # gate-break H08: the chapter lint and the questions gate see a copy, not only `q lint --all`
        mine = {i.get("id") for i in _active(items)}
        for p in dedupe_pairs(ctx, only=mine):
            if p["kind"] == "duplicate":
                first, second = (p["a"], p["b"]) if p["b"] in mine else (p["b"], p["a"])
                errors.append(_f("Q302", f"near-duplicate of {first} (similarity {p['similarity']})", item=second,
                                 file=ctx.data_rel(ch, "questions")))
    counts = _status_counts(items, {"multi": sum(1 for i in _active(items) if i.get("type") == "multi"), "twin_pairs": len(_twin_pairs(_active(items)))})
    return {"chapter": ch["id"], "ok": not errors, "errors": errors, "warnings": warnings, "counts": counts}


# ---------------------------------------------------------------- dedupe, exam-English words, bank rules

BAG_DUPLICATE = 0.85        # share of common words of stem plus options (order does not matter)
OPTIONS_SAME = 0.8          # share of common words of the options


def _print(item):
    """What the duplicate test reads of one question: (stem shingles, words of the options, words of stem and options)."""
    stem = item.get("stem", "") if isinstance(item.get("stem"), str) else ""
    opts = " ".join(o.get("text", "") for o in item.get("options", []) if isinstance(o, dict) and isinstance(o.get("text"), str))
    return _shingles(stem), set(_tokens(opts)), set(_tokens(stem)) | set(_tokens(opts))


def similarity(a, b, threshold=0.6):
    """(value, duplicate?) for two results of _print (gate-break H09, H27).

    Duplicate: the stems share `threshold` of their 3-word shingles; or stem and options share BAG_DUPLICATE of
    their words in any order (reordered clauses); or the options are the same and one stem holds `threshold` of
    the shingles of the other (a copied question with one more sentence).
    """
    jac = _jac(a[0], b[0]) if a[0] and b[0] else 0.0
    bag = _jac(a[2], b[2]) if a[2] and b[2] else 0.0
    inside = len(a[0] & b[0]) / min(len(a[0]), len(b[0])) if a[0] and b[0] else 0.0
    same_options = bool(a[1] and b[1]) and _jac(a[1], b[1]) >= OPTIONS_SAME
    value = max(jac, bag if bag >= BAG_DUPLICATE else 0.0, inside if same_options else 0.0)
    return value, jac >= threshold or bag >= BAG_DUPLICATE or (same_options and inside >= threshold)


def dedupe_pairs(ctx, threshold=0.6, only=None):
    """Pairs of live questions that are duplicates or have the same signature. `only`: a set of ids; then only
    pairs that hold one of them are compared (the chapter gate and `q add`)."""
    qs = [(ch, it) for ch, it in ctx.bank() if it.get("status") not in ("rejected", "retired") and it.get("id")]
    sh = [_print(it) for _, it in qs]
    sig = [(it.get("concept"), frozenset(o.get("trap") for o in it.get("options", []) if o.get("trap")),
            frozenset(o.get("concept") for o in it.get("options", []) if o.get("correct"))) for _, it in qs]
    pairs = []
    for a in range(len(qs)):
        for b in range(a + 1, len(qs)):
            ia, ib = qs[a][1], qs[b][1]
            if only is not None and ia["id"] not in only and ib["id"] not in only:
                continue
            sim, dup = similarity(sh[a], sh[b], threshold)
            twins = ia.get("twin_of") == ib["id"] or ib.get("twin_of") == ia["id"]
            if dup and not twins:
                pairs.append({"a": ia["id"], "b": ib["id"], "similarity": round(sim, 2), "kind": "duplicate"})
            elif qs[a][0]["id"] != qs[b][0]["id"] and sig[a] == sig[b]:
                pairs.append({"a": ia["id"], "b": ib["id"], "similarity": round(sim, 2), "kind": "same-signature"})
    return pairs


def word_stems(ctx):
    rows = []
    stems = [it.get("stem", "") for _, it in ctx.bank() if it.get("status") != "rejected"]
    for eid, word in ctx.exam_english.items():
        rxs = [_word_re(w) for w in [word["word"]] + list(word.get("also", []))]
        rows.append({"id": eid, "word": word["word"], "stems": sum(1 for s in stems if any(rx.search(s) for rx in rxs))})
    return rows


def q_bank_rules(ctx):
    Q = ctx.spec["questions"]
    errors, warnings = [], []
    seen = {}
    for ch, it in ctx.bank():
        if it.get("id") in seen:
            errors.append(_f("Q301", f"duplicate id (also in chapter {seen[it.get('id')]})", item=it.get("id"), file=ctx.data_rel(ch, "questions")))
        seen.setdefault(it.get("id"), ch["id"])
    for p in dedupe_pairs(ctx):
        if p["kind"] == "duplicate":
            errors.append(_f("Q302", f"near-duplicate of {p['a']} (similarity {p['similarity']})", item=p["b"]))
    need = Q.get("exam_english_word_min_stems", 0)
    for row in word_stems(ctx):
        if row["stems"] < need:
            warnings.append(_f("Q303", f"exam-English word '{row['word']}' ({row['id']}) is in {row['stems']} stems; needed {need}"))
    live = [it for _, it in ctx.bank() if it.get("status") not in ("rejected", "retired")]
    if live:
        share = sum(1 for i in live if i.get("type") == "multi") / len(live)
        if abs(share - Q["multi_share_of_bank"]) > 0.05 + 1e-9:
            warnings.append(_f("Q304", f"multi share of the bank is {share:.2f}; target {Q['multi_share_of_bank']:.2f}"))
    return errors, warnings


# ---------------------------------------------------------------- card rules (C101 to C204)

def card_item_rules(ctx, ch, item, siblings, pos):
    C = ctx.spec["cards"]
    out = []
    cid = item.get("id") if isinstance(item, dict) else None
    rel = ctx.data_rel(ch, "cards") if ch else "data/cards-terms.json"

    def add(code, msg):
        out.append(_f(code, msg, item=cid, file=rel))

    errs = schemas.validate(item, "card", "card")
    if errs:
        for e in errs[:8]:
            add("C101", "schema: " + e)
        return out
    slug = ch["slug"] if ch else "glossary"
    if not item["id"].startswith(slug + "-c") or item["chapter"] != slug:
        add("C101", f"id and chapter must use the slug {slug}")
    typ = item["type"]
    generated = bool(item.get("generated"))
    if generated != (typ in C["generated_types"]):
        add("C110", f"type {typ} with generated {generated}")
    # C103
    for fid in item["facts"]:
        if not ctx.verified(fid):
            add("C103", f"fact {fid} does not resolve to a verified fact")
    if typ in C["types_that_need_facts"] and not item["facts"]:
        add("C103", f"a {typ} card needs facts")
    if typ in C["types_that_need_term"] and item.get("term") not in {t["id"] for t in ctx.terms}:
        add("C103", f"term {item.get('term')} is not in data/terms.json")
    if typ == C["type_that_needs_word"] and item.get("word") not in ctx.exam_english:
        add("C103", f"word {item.get('word')} is not in data/exam-english.json")
    if typ == C["type_that_needs_speak"]:
        pool = [s for c in ctx.chapters() for s in _items_of(ctx.doc(c, "speak"))] if generated else (_items_of(ctx.doc(ch, "speak")) if ch else [])
        if item.get("speak") not in {s.get("id") for s in pool}:
            add("C103", f"speak item {item.get('speak')} does not exist")
    if generated:
        return out
    # C102
    back_max = C["back_words_max_say"] if typ == "say" else C["back_words_max"]
    if _wc(item["back"]) > back_max:
        add("C102", f"back has {_wc(item['back'])} words; at most {back_max}")
    if _wc(item["front"]) > C["front_words_max"]:
        add("C102", f"front has {_wc(item['front'])} words; at most {C['front_words_max']}")
    # C104
    if typ == "number":
        cloze = re.findall(C["number_cloze_regex"], item["front"])
        if len(cloze) != 1:
            add("C104", "a number card holds exactly one cloze {{c1::value}}")
        else:
            inner = common.normalize_text(re.sub(r"^\{\{c1::|\}\}$", "", cloze[0]))
            if not any(_holds(inner, d) for fid in item["facts"] for d in ctx.displays(fid)):
                add("C104", "the cloze holds no display value of its fact")
        if ch and not set(item["facts"]) & set(ctx.a_list(ch)):
            add("C104", "the fact of a number card is not in the A-list")
    # C105
    for start in C["banned_front_starts"]:
        if item["front"].startswith(start):
            add("C105", f"front starts with '{start}'")
    if not C.get("list_answers") and typ not in C.get("list_answer_exempt_types", []):
        back = item["back"]
        # gate-break H32: also `a shelf, a crate and a quota` (one comma) and `shelf / crate / quota`
        if "\n" in back or ";" in back or back.count(",") > 1 or re.search(r",[^,.;]*\b(?:and|or)\b", back) \
                or len(re.findall(r"\s/\s|(?<=[A-Za-z])/(?=[A-Za-z])", back)) >= 2:
            add("C105", "list answer: one fact per card")
    # C106
    if C.get("near_duplicates_need_pair_tag"):
        mine = _tokens(item["front"])
        for other in siblings[:pos]:
            if not isinstance(other, dict) or other.get("status") in ("rejected", "retired") or other.get("generated"):
                continue
            paired = item.get("pair") == other.get("id") or other.get("pair") == item["id"] or (item.get("pair") and item.get("pair") == other.get("pair"))
            theirs = _tokens(other.get("front", ""))
            # gate-break H37: a short front plus a few filler words is still the same front
            inside = len(set(mine) & set(theirs)) / min(len(set(mine)), len(set(theirs))) if mine and theirs else 0.0
            if not paired and (_jac(mine, theirs) >= 0.8 or (inside >= 0.95 and min(len(set(mine)), len(set(theirs))) >= 4)):
                add("C106", f"front is a near-duplicate of {other.get('id')} without a pair value")
    # C107
    if item.get("extra"):
        for f in ctx.strict(item["extra"], f"{cid}.extra"):
            if f.get("code") != "L801":
                add("C107", f"extra: {f.get('code')} {f.get('msg')}")
        for fid in ctx.fact_ids_in(item["extra"]):
            if fid not in item["facts"]:
                add("C107", f"linked fact {fid} is not in facts")
    for name in ("front", "back", "extra"):
        for w in ctx.banned_hits(item.get(name) or ""):
            add("C107", f"banned word '{w}' in {name}")
    # C108
    if ch and not ctx.section_ok(ch, item["section"]):
        add("C108", f"section {item['section']} does not resolve")
    if item.get("trap") and item["trap"] not in ctx.traps:
        add("C108", f"unknown trap id {item['trap']}")
    # C109
    for name in ("front", "back"):
        text = re.sub(r"\{\{c1::([^}]+)\}\}", r"\1", item[name])
        for bad in ctx.numbers_outside_displays(text, item["facts"]):
            add("C109", f"'{bad}' in {name} is not inside a display of a fact in facts")
    return out


def card_chapter_rules(ctx, ch, items, ship=False):
    C = ctx.spec["cards"]
    rel = ctx.data_rel(ch, "cards")
    errors, warnings = [], []

    def soft(code, msg, item=None):
        (errors if ship else warnings).append(_f(code, msg, item=item, file=rel))

    hand = [i for i in _active(items) if i.get("type") in C["hand_types"] and not i.get("generated")]
    pool = [i for i in hand if i.get("status") == "ready"] if ship else hand
    for deck, want in sorted(ctx.counts(ch, "cards").items()):
        if deck not in C["decks"]:
            continue
        n = sum(1 for i in pool if i.get("deck") == deck)
        lo, hi = _rng(want)
        if n < lo or (ship and n > hi):
            soft("C201", f"deck {deck}: {n} {'ready ' if ship else ''}cards; needed {lo}" + ("" if lo == hi else f" to {hi}"))
    numbered = {fid for i in hand if i.get("type") == "number" for fid in i.get("facts", [])}
    for fid in ctx.a_list(ch):
        if fid not in numbered:
            soft("C204", f"A-list fact {fid} has no number card")
    names = [t["term"] for t in ctx.terms] + ctx.official_names + [w for w in re.findall(r"[A-Za-z0-9]+", ch.get("title", "")) if len(w) >= 4 and w.lower() not in STOP_WORDS]
    for i in hand:
        front = i.get("front", "")
        if not any(_word_re(n).search(front) for n in names if n):
            warnings.append(_f("C203", "the front names no term, no service and no word of the chapter title", item=i.get("id"), file=rel))
    return errors, warnings


def cards_lint(ctx, ch, ship=False):
    doc = ctx.doc(ch, "cards")
    errors = _wrapper_findings(ctx, ch, "cards", doc) if ctx.data_path(ch, "cards").exists() else []
    items = _items_of(doc)
    seen = set()
    for pos, item in enumerate(items):
        if item.get("id") in seen:
            errors.append(_f("C101", "duplicate id", item=item.get("id"), file=ctx.data_rel(ch, "cards")))
        seen.add(item.get("id"))
        if item.get("status") not in ("rejected", "retired"):
            errors += card_item_rules(ctx, ch, item, items, pos)
    e, warnings = card_chapter_rules(ctx, ch, items, ship=ship)
    errors += e
    counts = _status_counts(items, {"generated": sum(1 for i in items if i.get("generated"))})
    return {"chapter": ch["id"], "ok": not errors, "errors": errors, "warnings": warnings, "counts": counts}


# ---------------------------------------------------------------- speak rules (P101 to P202)

def speak_item_rules(ctx, ch, item):
    S = ctx.spec["speak"]
    out = []
    sid = item.get("id") if isinstance(item, dict) else None
    rel = ctx.data_rel(ch, "speak")

    def add(code, msg):
        out.append(_f(code, msg, item=sid, file=rel))

    errs = schemas.validate(item, "speak", "speak")
    if errs:
        for e in errs[:8]:
            add("P101", "schema: " + e)
        return out
    slug = ch["slug"]
    if not item["id"].startswith(slug + "-s") or item["chapter"] != slug:
        add("P101", f"id and chapter must use the slug {slug}")
    ten, lines = item["ten_second"], item["sixty_second"]
    scripts = [("ten_second", ten)] + [(f"sixty_second[{n}]", line) for n, line in enumerate(lines, 1)]
    # P102
    if _wc(ten) > S["ten_second_words_max"]:
        add("P102", f"ten_second has {_wc(ten)} words; at most {S['ten_second_words_max']}")
    total = sum(_wc(line) for line in lines)
    if not _in(S["sixty_second_words"], total):
        lo, hi = _rng(S["sixty_second_words"])
        add("P102", f"sixty_second has {total} words; allowed {lo} to {hi}")
    if not _in(S["sixty_second_lines"], len(lines)):
        lo, hi = _rng(S["sixty_second_lines"])
        add("P102", f"sixty_second has {len(lines)} lines; allowed {lo} to {hi}")
    for name, text in scripts:
        for sent in _spoken_sentences(text):
            if _wc(sent) > S["sentence_words_max"]:
                add("P102", f"a sentence of {name} has {_wc(sent)} words; at most {S['sentence_words_max']}")
    # P103
    joined = "\n".join(lines)
    starters = list(S["starters_in_order"])
    if item["kind"] == "compare" and joined.startswith(S.get("compare_first_sentence_may_start", "Both ")):
        starters = starters[1:]
    at = 0
    for start in starters:
        m = re.compile(r"(?:^|(?<=[.?!:]\s))" + re.escape(start), re.M).search(joined, at)
        if not m:
            add("P103", f"the starter '{start}' is missing or out of order")
            break
        at = m.end()
    if not lines[-1].rstrip().endswith(S["last_line_ends_with"]):
        add("P103", f"the last line does not end with {S['last_line_ends_with']}")
    # P104
    if len(item["skeleton"]) != S["skeleton_cues"]:
        add("P104", f"{len(item['skeleton'])} skeleton cues; needed {S['skeleton_cues']}")
    for cue in item["skeleton"]:
        if _wc(cue) > S["skeleton_cue_words_max"]:
            add("P104", f"cue '{cue}' has more than {S['skeleton_cue_words_max']} words")
    # P105
    must = [k for k in item["key_points"] if k["kind"] == "must"]
    nice = [k for k in item["key_points"] if k["kind"] == "nice"]
    if not _in(S["must_points"], len(must)):
        add("P105", f"{len(must)} must points")
    if not _in(S["nice_points"], len(nice)):
        add("P105", f"{len(nice)} nice points")
    for k in must:
        if S.get("every_must_point_needs_fact") and not k["facts"]:
            add("P105", f"must point {k['id']} has no fact")
    refs = [(f"key point {k['id']}", fid) for k in item["key_points"] for fid in k["facts"]]
    refs += [("must_not_say", m["fact"]) for m in item["must_not_say"] if m.get("fact")]
    refs += [("follow_ups", fid) for fu in item["follow_ups"] for fid in fu.get("facts", [])]
    refs += [("facts", fid) for fid in item["facts"]]
    for name, fid in refs:
        if not ctx.verified(fid):
            add("P105", f"{name}: fact {fid} does not resolve to a verified fact")
    if not _in(S["must_not_say"], len(item["must_not_say"])):
        add("P105", f"{len(item['must_not_say'])} must_not_say entries")
    if len(item["follow_ups"]) != S["follow_ups"]:
        add("P105", f"{len(item['follow_ups'])} follow-ups")
    # P106
    names = [x for t in ctx.terms for x in (t.get("term"), t.get("short")) if x] + ctx.official_names
    for name, text in scripts:
        probe = re.sub(S["digits_allowed_inside_names_regex"], " ", text)
        for n in names:
            probe = re.sub(re.escape(n) + r"(?:\s*[0-9]+)?", " ", probe)
        if not S.get("digits_allowed") and re.search(r"[0-9]", probe):
            add("P106", f"a digit in {name}")
        if not S.get("brackets_allowed") and re.search(r"[()\[\]{}]", text):
            add("P106", f"a bracket in {name}")
        if not S.get("links_allowed") and re.search(r"\]\(|https?://", text):
            add("P106", f"a link in {name}")
    # P107
    avoid = [a for t in item["terms"] for a in t.get("avoid", [])]
    for name, text in scripts:
        for a in avoid:
            if _word_re(a).search(text):
                add("P107", f"avoid word '{a}' in {name}")
        for w in ctx.banned_hits(text):
            add("P107", f"banned word '{w}' in {name}")
    # P108
    if not ctx.section_ok(ch, item["section"]):
        add("P108", f"section {item['section']} does not resolve")
    # P109
    spoken = [s for fid in item["facts"] for s in ctx.spoken(fid)]
    for name, text in scripts:
        for sent in _spoken_sentences(text):
            for phrase in spoken_numbers(ctx, sent):
                if not any(phrase in s for s in spoken):
                    add("P109", f"'{phrase}' in {name} is not a spoken form of a fact in facts")
    # gate-break H40: the texts outside the two scripts have word limits too (4-say.md prints them)
    for label, text, limit in ([(f"key point {k['id']}", k["point"], S.get("key_point_words_max", 30)) for k in item["key_points"]]
                               + [("a follow-up answer", fu["answer"], S.get("follow_up_answer_words_max", 60)) for fu in item["follow_ups"]]
                               + [("a must_not_say entry", m.get("correct") or "", S.get("must_not_say_words_max", 40))
                                  for m in item["must_not_say"]]):
        if _wc(text) > limit:
            add("P102", f"{label} has {_wc(text)} words; at most {limit}")
    checks = [(f"key point {k['id']}", k["point"], item["facts"]) for k in item["key_points"]]
    checks += [("must_not_say", m["correct"], item["facts"]) for m in item["must_not_say"]]
    checks += [("follow-up answer", fu["answer"], fu.get("facts", [])) for fu in item["follow_ups"]]
    for name, text, fids in checks:
        for bad in ctx.numbers_outside_displays(text, fids):
            add("P109", f"'{bad}' in {name} is not inside a display of its facts")
    return out


_RE_NUMBER_WORD_EXTRA = r"\b(?:seventeen|eighteen|nineteen|dozen)\b"
_RE_NUMBER_WORD_DEFAULT = (r"\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|twenty"
                           r"|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)\b")
_SMALL_NUMBER_WORDS = frozenset("two three four five six seven eight nine ten eleven twelve".split())
_BIG_NUMBER_WORDS = frozenset("hundred thousand million billion dozen".split())
_SPOKEN_GAP_STOP = frozenset("and or to in per for than the is are a an at on by with from as that it they you".split())


def spoken_numbers(ctx, sent) -> list:
    """The spoken numbers of one sentence, each as the normalised phrase `<number words> <unit>` (gate-break H35,
    H42). The number words are those of speak.number_word_regex plus seventeen, eighteen, nineteen and dozen; the
    unit or count noun follows directly or after one or two words (`nine hundred of your widgets`)."""
    _, unit_after = ctx.nwu(singular=True)
    number = re.compile("(?:" + (ctx.spec.get("speak") or {}).get("number_word_regex", _RE_NUMBER_WORD_DEFAULT) + ")|"
                        + _RE_NUMBER_WORD_EXTRA, re.I)
    hits, out, i = list(number.finditer(sent)), [], 0
    while i < len(hits):
        j = i
        while j + 1 < len(hits) and re.fullmatch(r"(?:[ -]|\s+and\s+)", sent[hits[j].end():hits[j + 1].start()]):
            j += 1
        rest = sent[hits[j].end():]
        m = unit_after.match(rest)
        words = sent[hits[i].start():hits[j].end()]
        if m:
            out.append(common.normalize_text(words + m.group(0)))
        else:
            pos = 0
            for _ in range(2):
                gap = re.match(r" ([A-Za-z][A-Za-z'-]*)(?= )", rest[pos:])
                if not gap or gap.group(1).lower() in _SPOKEN_GAP_STOP or number.fullmatch(gap.group(1)):
                    break
                pos += gap.end()
                m = unit_after.match(rest[pos:])
                if m and m.group(0)[:1] in " -":
                    out.append(common.normalize_text(words + " " + m.group(0).strip(" -")))
                    break
        i = j + 1
    return out


def speak_lint(ctx, ch, ship=False):
    doc = ctx.doc(ch, "speak")
    rel = ctx.data_rel(ch, "speak")
    errors = _wrapper_findings(ctx, ch, "speak", doc) if ctx.data_path(ch, "speak").exists() else []
    items = _items_of(doc)
    warnings = []
    seen = set()
    for item in items:
        if item.get("id") in seen:
            errors.append(_f("P101", "duplicate id", item=item.get("id"), file=rel))
        seen.add(item.get("id"))
        if item.get("status") not in ("rejected", "retired"):
            errors += speak_item_rules(ctx, ch, item)
    counts = ctx.counts(ch, "speak")
    live = _active(items)
    pool = [i for i in live if i.get("status") == "ready"] if ship else live
    for name, n, want in (("items", len(pool), counts.get("count")), ("pass_route items", sum(1 for i in pool if i.get("pass_route")), counts.get("pass_route"))):
        if want is not None and (n != want if ship else n < want):
            (errors if ship else warnings).append(_f("P201", f"{name}: {n}; needed {want}", file=rel))
    out_counts = _status_counts(items, {"pack": sum(1 for i in live if i.get("pack"))})
    return {"chapter": ch["id"], "ok": not errors, "errors": errors, "warnings": warnings, "counts": out_counts}


# ---------------------------------------------------------------- public API

def items(ch, kind):
    """The items of data/<dir>/<kind>.json (kind: questions, cards, speak)."""
    if kind not in KINDS:
        raise ValueError(f"unknown kind {kind!r}")
    doc = common.read_json(common.chapter_data_dir(ch) / f"{kind}.json") or {}
    return list(doc.get("items", [])) if isinstance(doc, dict) else []


def _gate(name, ch_id, result_fn):
    ctx = Ctx()
    ch = ctx.chapter(ch_id)
    result = result_fn(ctx, ch)
    return {"gate": name, "chapter": ch["id"], "ok": not result["errors"], "exit": _exit(result["errors"], result["warnings"]),
            "errors": result["errors"], "warnings": result["warnings"], "counts": result["counts"], "inputs": ctx.gate_inputs()}


def gate_questions(ch_id, quick=False, **options):
    return _gate("questions", ch_id, lambda ctx, ch: q_lint(ctx, ch))


def gate_questions_verified(ch_id, quick=False, **options):
    return _gate("questions-verified", ch_id, lambda ctx, ch: q_lint(ctx, ch, ship=True, verified=True))


def gate_cards(ch_id, quick=False, **options):
    return _gate("cards", ch_id, lambda ctx, ch: cards_lint(ctx, ch))


def gate_speak(ch_id, quick=False, **options):
    return _gate("speak", ch_id, lambda ctx, ch: speak_lint(ctx, ch))


# ---------------------------------------------------------------- add, set-status

def _next_id(slug, letter, digits, taken):
    n = 1
    while f"{slug}-{letter}{n:0{digits}d}" in taken:
        n += 1
    return f"{slug}-{letter}{n:0{digits}d}"


def _mark_stale(ch, reason, stage):
    fn = _fn("ledger", "mark_stale")
    if fn:
        try:
            fn(ch["id"], reason, item_stages=[stage])
        except BaseException:
            pass


def _item_rules(ctx, ch, kind, item, siblings, pos):
    if kind == "questions":
        return q_item_rules(ctx, ch, item, siblings, pos)
    if kind == "cards":
        return card_item_rules(ctx, ch, item, siblings, pos)
    return speak_item_rules(ctx, ch, item)


def _need_guide(ctx):
    if ctx.guide is None:
        return common.fail("no _build/registry/exam-guide.json; run registry build", common.EXIT_PRECONDITION)
    return None


def cmd_add(args, kind):
    ctx = Ctx()
    ch = ctx.chapter(args.chapter)
    if kind == "questions" and _need_guide(ctx):
        return common.EXIT_PRECONDITION
    incoming, code = _read_input(args.file)
    if code is not None:
        return code
    _, _, letter, digits = KINDS[kind]
    code_dup = {"questions": "Q301", "cards": "C101", "speak": "P101"}[kind]
    path = ctx.data_path(ch, kind)
    added, replaced, rejected, stale = [], [], [], False
    with common.file_lock(path):
        doc = common.read_json(path) or {"v": 1, "chapter": ch["slug"], "items": []}
        stored = doc["items"]
        for index, raw in enumerate(incoming):
            def reject(findings, raw=raw, index=index):
                rejected.append({"index": index, "id": raw.get("id") if isinstance(raw, dict) else None, "errors": findings})
            if not isinstance(raw, dict):
                reject([_f("X01", "an item must be a JSON object")])
                continue
            item = copy.deepcopy(raw)
            taken = {i.get("id") for i in stored}
            old_pos = next((n for n, i in enumerate(stored) if i.get("id") == item.get("id")), None) if item.get("id") else None
            if args.replace:
                if old_pos is None:
                    reject([_f(code_dup, "--replace: the id does not exist", item=item.get("id"))])
                    continue
                old = stored[old_pos]
                if old.get("status") in ("rejected", "retired"):
                    reject([_f(code_dup, f"--replace: the stored item is {old.get('status')}", item=item.get("id"))])
                    continue
            elif old_pos is not None:
                reject([_f(code_dup, "the id exists; use --replace", item=item.get("id"))])
                continue
            else:
                old = None
            if not item.get("id"):
                item["id"] = _next_id(ch["slug"], letter, digits, taken)
            item["chapter"] = ch["slug"]
            item["status"] = "candidate"
            item["rev"] = 1
            was_passed = False
            if kind == "questions":
                item["keyRev"] = 1
                item["verification"] = {"status": "candidate", "round": 0, "solvers": []}
                item.setdefault("pool", "mock" if ctx.is_mock(ch) else "chapter")
                item["volatile"] = ctx.question_volatile(item) if isinstance(item.get("options"), list) else False
                if old is not None:
                    ver = old.get("verification") or {}
                    key = lambda q: {(o.get("id"), o.get("text")) for o in q.get("options", []) if isinstance(o, dict) and o.get("correct")}
                    item["keyRev"] = old.get("keyRev", 1) + (1 if isinstance(item.get("options"), list) and key(old) != key(item) else 0)
                    item["rev"] = old.get("rev", 1)
                    if ver.get("status") in PASSED:
                        item["rev"] += 1
                        was_passed = True
                    elif ver.get("round") == 1:
                        if ver.get("edits", 0) >= 1:    # gate-break H23: unanimous, or one edit, then reject
                            reject([_f("Q207", "the question had its one edit after the failed round; run `q pack --round 1` "
                                               "and `q adjudicate`, which passes or rejects it", item=item.get("id"))])
                            continue
                        item["rev"] += 1
                        item["verification"] = {"status": "candidate", "round": 1, "solvers": [], "note": ver.get("note"), "edits": 1}
                # gate-break H18: who wrote the text; none of these labels can be a solver of the question
                item["authors"] = sorted(set((old or {}).get("authors") or []) | {_label(args)})
            else:
                if kind == "cards":
                    C = ctx.spec["cards"]
                    if item.get("type") in C["generated_types"] or item.get("generated"):
                        reject([_f("C110", f"`cards add` refuses the generated type {item.get('type')}; `cards build` writes it", item=item.get("id"))])
                        continue
                if old is not None:
                    item["rev"] = old.get("rev", 1) + 1
                    was_passed = old.get("status") == "ready"
                    if kind == "speak":
                        item["pack"] = bool(old.get("pack"))
            siblings = list(stored)
            if old_pos is None:
                siblings.append(item)
                pos = len(siblings) - 1
            else:
                siblings[old_pos] = item
                pos = old_pos
            findings = _item_rules(ctx, ch, kind, item, siblings, pos)
            if not findings and kind == "questions":
                # gate-break H08, H24: a copy of a live question, or of a rejected one, is not stored
                mine = _print(item)
                for other in siblings + [q for c, q in ctx.bank() if c["id"] != ch["id"]]:
                    if other is item or other.get("id") == item["id"] or other.get("status") in ("rejected", "retired") \
                            or item.get("twin_of") == other.get("id") or other.get("twin_of") == item["id"]:
                        continue
                    value, dup = similarity(mine, _print(other))
                    if dup:
                        findings.append(_f("Q302", f"near-duplicate of {other.get('id')} (similarity {value:.2f})", item=item["id"]))
                        break
                again = None if findings else rejected_duplicate(ctx, ch, item)
                if again:
                    findings.append(_f("Q302", f"repeats the rejected question {again}; a rejected question does not come back",
                                       item=item["id"]))
            if findings:
                reject(findings)
                continue
            doc["items"] = stored = siblings
            (replaced if old_pos is not None else added).append(item["id"])
            stale = stale or was_passed
        if added or replaced:
            common.write_json(path, doc)
    if stale:
        _mark_stale(ch, f"{kind} item replaced", "questions" if kind == "questions" else kind)
    result = {"added": added, "replaced": replaced, "rejected": rejected}
    findings = [f for r in rejected for f in r["errors"]]
    _emit(args, result, f"{kind} add {ch['id']}: added={len(added)} replaced={len(replaced)} rejected={len(rejected)}", findings)
    return common.EXIT_FAIL if rejected else common.EXIT_OK


def cmd_set_status(args, kind):
    ctx = Ctx()
    ch = ctx.chapter(args.chapter)
    if args.status in ("retired", "rejected") and not args.reason:
        return common.fail(f"--status {args.status} needs --reason", common.EXIT_FAIL)
    path = ctx.data_path(ch, kind)
    done, refused = [], []
    with common.file_lock(path):
        doc = common.read_json(path) or {"v": 1, "chapter": ch["slug"], "items": []}
        stored = doc["items"]
        for iid in args.ids:
            pos = next((n for n, i in enumerate(stored) if i.get("id") == iid), None)
            if pos is None:
                refused.append({"id": iid, "errors": [_f("X01", "no such item", item=iid)]})
                continue
            item = stored[pos]
            findings = []
            if args.status == "ready":
                findings = _item_rules(ctx, ch, kind, item, stored, pos)
                if kind == "questions" and not _verification_passed(item):
                    findings.append(_f("Q206", "verification has not passed", item=iid, file=ctx.data_rel(ch, kind)))
            elif args.status == "verified" and kind == "questions" and not _verification_passed(item):
                # gate-break H25: `verified` is the result of `q adjudicate`, never a label set by hand
                findings.append(_f("Q206", "verification has not passed; only `q adjudicate` makes a question verified",
                                   item=iid, file=ctx.data_rel(ch, kind)))
            if findings:
                refused.append({"id": iid, "errors": findings})
                continue
            item["status"] = args.status
            if kind == "questions" and args.status == "rejected":
                item["verification"]["status"] = "rejected"
            if kind == "questions" and args.reason:
                item["verification"]["note"] = args.reason
            done.append(iid)
        if done:
            common.write_json(path, doc)
    for iid in done:
        common.append_jsonl(common.BUILD / "qbank" / "status.jsonl", {"ts": common.now_iso(), "kind": kind, "id": iid, "status": args.status, "by": _label(args), "reason": args.reason})
    result = {"set": done, "refused": refused}
    _emit(args, result, f"{kind} set-status {args.status}: set={len(done)} refused={len(refused)}", [f for r in refused for f in r["errors"]])
    return common.EXIT_FAIL if refused else common.EXIT_OK


# ---------------------------------------------------------------- lint commands

def _chapters_with(ctx, kind):
    return [ch for ch in ctx.chapters() if ctx.data_path(ch, kind).exists()]


def cmd_lint(args, kind):
    ctx = Ctx()
    if kind == "questions" and _need_guide(ctx):
        return common.EXIT_PRECONDITION
    lint_one = {"questions": q_lint, "cards": cards_lint, "speak": speak_lint}[kind]
    if args.all:
        errors, warnings, counts = [], [], collections.Counter()
        chapters = _chapters_with(ctx, kind)
        for ch in chapters:
            r = q_lint(ctx, ch, ship=args.ship, dupes=False) if kind == "questions" else lint_one(ctx, ch, ship=args.ship)
            errors += r["errors"]
            warnings += r["warnings"]
            counts.update(r["counts"])
        if kind == "questions":
            e, w = q_bank_rules(ctx)
        elif kind == "cards":
            e, w = _cards_bank_rules(ctx)
        else:
            e, w = [], []
            total = sum(1 for ch in chapters for i in _active(_items_of(ctx.doc(ch, "speak"))) if i.get("pack"))
            if total != ctx.spec["speak"].get("pack_total", 0):
                e.append(_f("P202", f"{total} speak items have pack true; needed {ctx.spec['speak'].get('pack_total', 0)}"))
        errors += e
        warnings += w
        result = {"chapter": "all", "ok": not errors, "errors": errors, "warnings": warnings, "counts": dict(counts)}
    else:
        if not args.chapter:
            return common.fail("give a chapter or --all", common.EXIT_PRECONDITION)
        result = lint_one(ctx, ctx.chapter(args.chapter), ship=args.ship)
    name = {"questions": "q", "cards": "cards", "speak": "speak"}[kind]
    summary = f"{name} lint {result['chapter']}: {'ok' if result['ok'] else 'FAIL'} errors={len(result['errors'])} warnings={len(result['warnings'])} " + " ".join(f"{k}={v}" for k, v in result["counts"].items())
    _emit(args, result, summary, result["errors"] + result["warnings"])
    return _exit(result["errors"], result["warnings"])


# ---------------------------------------------------------------- blind packs and adjudication

def permutation(seed, qid, lens, rnd, option_ids):
    """The option ids in the order one solver sees them; position n carries the label LABELS[n]."""
    ids = list(option_ids)
    random.Random(hashlib.sha256(f"{seed}|{qid}|{lens}|{rnd}".encode("utf-8")).hexdigest()).shuffle(ids)
    return ids


def _seed(ctx):
    return (ctx.book.get("book") or {}).get("mock_seed", 0)


def build_pack(ctx, ch, lens, rnd=0, ids=None):
    out = []
    for q in _items_of(ctx.doc(ch, "questions")):
        ver = q.get("verification") or {}
        if ver.get("status") != "candidate" or ver.get("round") != rnd or q.get("status") in ("rejected", "retired"):
            continue
        if ids and q["id"] not in ids:
            continue
        by_id = {o["id"]: o for o in q["options"]}
        order = permutation(_seed(ctx), q["id"], lens, rnd, [o["id"] for o in q["options"]])
        out.append({"id": q["id"], "type": q["type"], "select": q["select"], "stem": q["stem"],
                    "options": [{"label": LABELS[n], "text": by_id[oid]["text"]} for n, oid in enumerate(order)]})
    return {"pack": f"{ch['slug']}-r{rnd}-{lens}", "chapter": ch["id"], "lens": lens, "round": rnd, "instructions": INSTRUCTIONS[lens], "items": out}


def pack_findings(pack):
    """Q401: a blind pack holds nothing of a question but id, type, select, stem and the option labels and texts."""
    out = []
    for item in pack.get("items", []) if isinstance(pack, dict) else []:
        extra = set(item) - PACK_ITEM_KEYS
        for o in item.get("options", []):
            extra |= set(o) - PACK_OPTION_KEYS
        if extra or set(item) != PACK_ITEM_KEYS:
            out.append(_f("Q401", f"a pack item holds exactly id, type, select, stem, options; found {sorted(extra) or sorted(item)}", item=item.get("id")))
    return out


def cmd_pack(args):
    ctx = Ctx()
    ch = ctx.chapter(args.chapter)
    if not args.out:
        return common.fail("q pack needs --out FILE", common.EXIT_PRECONDITION)
    pack = build_pack(ctx, ch, args.lens, args.round, set(args.ids or []))
    bad = pack_findings(pack)
    if bad:
        _emit(args, {"pack": pack["pack"], "errors": bad}, f"q pack {pack['pack']}: FAIL", bad)
        return common.EXIT_FAIL
    if not pack["items"]:
        return common.fail(f"no candidate question in round {args.round}", common.EXIT_PRECONDITION)
    # gate-break H22: remember what each solver was shown; `q adjudicate` refuses answers for another text
    by_id = {q["id"]: q for q in _items_of(ctx.doc(ch, "questions")) if q.get("id")}
    common.append_jsonl(common.BUILD / "qbank" / "packs.jsonl", {
        "ts": common.now_iso(), "pack": pack["pack"], "chapter": ch["id"], "lens": args.lens, "round": args.round,
        "items": {item["id"]: solver_view_hash(by_id[item["id"]]) for item in pack["items"]}})
    common.emit(pack, args)
    return common.EXIT_OK


def solver_view_hash(q) -> str:
    """SHA-256 of what a solver sees and what the answer is checked against: stem, option texts, and the key."""
    body = {"stem": q.get("stem"), "type": q.get("type"), "select": q.get("select"),
            "options": sorted([o.get("id"), o.get("text"), bool(o.get("correct"))] for o in q.get("options", []))}
    return common.sha256_bytes(json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8"))


def _shown(ctx, ch, lens, rnd) -> dict:
    """question id -> hash of the text in the newest pack of this chapter, lens and round."""
    shown = {}
    for row in common.read_jsonl(common.BUILD / "qbank" / "packs.jsonl"):
        if row.get("chapter") == ch["id"] and row.get("lens") == lens and row.get("round") == rnd:
            shown.update(row.get("items") or {})
    return shown


def _solver_key(label) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(label or "").lower())


def _answer_file_problems(ctx, ch, files, rnd, by_id) -> list:
    """Why the three answer files cannot be adjudicated (gate-break H17 to H22). Empty when they can."""
    out = []
    keys = {}
    for lens in LENSES:
        doc = files[lens]
        label = doc.get("solver")
        if not isinstance(label, str) or len(_solver_key(label)) < 2 or _solver_key(label) == "unknown":
            out.append(f"{lens}: the answer file names no solver")
            continue
        keys[lens] = _solver_key(label)
    if len(set(keys.values())) != len(keys):
        out.append("the three lenses need three different solvers; one label signs more than one answer file")
    for lens in LENSES:
        seen = set()
        shown = _shown(ctx, ch, lens, rnd)
        for row in files[lens]["answers"]:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                out.append(f"{lens}: an answer row is not an object with an id")
                continue
            qid = row["id"]
            if qid in seen:
                out.append(f"{lens}: two rows for {qid}")
            seen.add(qid)
            q = by_id.get(qid)
            if q is None:
                continue
            if lens in keys and keys[lens] in {_solver_key(a) for a in q.get("authors") or []}:
                out.append(f"{lens}: solver {files[lens]['solver']!r} is an author of {qid}")
            if shown.get(qid) is None:
                out.append(f"{lens}: {qid} was in no pack of round {rnd}; run `q pack --lens {lens} --round {rnd}`")
            elif shown[qid] != solver_view_hash(q):
                out.append(f"{lens}: {qid} changed after the pack went out; make the packs again and solve again")
            if lens == "closed" and _fb_word_count(row.get("stem_only") if isinstance(row.get("stem_only"), str) else "") < 3:
                out.append(f"closed: {qid} has no stem_only (the solution stated before the options were read)")
            if lens == "ambiguity":
                case = row.get("case") if isinstance(row.get("case"), dict) else {}
                if case.get("label") not in list(LABELS[:len(q.get("options", []))]) or \
                        _fb_word_count(case.get("text") if isinstance(case.get("text"), str) else "") < 3:
                    out.append(f"ambiguity: {qid} has no case (the label of a wrong option and the strongest argument for it)")
    return out


CITATION_QUOTE_WORDS_MIN = 6


def _citations(ctx, answer, labels, q=None):
    """(ok, stored list) for the open lens.

    gate-break H20: a quote citation has at least CITATION_QUOTE_WORDS_MIN words; the labels do not all carry
    one and the same citation; and at least one citation is a fact of the question or a quote from a page that
    is evidence of one (the solver found what the question is built on).
    """
    cites = answer.get("citations")
    ok = isinstance(cites, dict)
    stored = set()
    per_label, facts, sources = [], set(), set()
    for label in labels:
        entries = (cites or {}).get(label) if isinstance(cites, dict) else None
        if not isinstance(entries, list) or not entries:
            ok = False
            continue
        mine = set()
        for c in entries:
            if isinstance(c, str):
                stored.add(c)
                mine.add(c)
                facts.add(c)
                ok = ok and ctx.verified(c)
            elif isinstance(c, dict) and isinstance(c.get("quote"), str) and isinstance(c.get("source_id"), str):
                stored.add(f"{c['source_id']}#{c['quote'][:40]}")
                mine.add(f"{c['source_id']}#{common.normalize_text(c['quote'])}")
                sources.add(c["source_id"])
                text = ctx.corpus_text(c["source_id"])
                ok = ok and text is not None and common.find_quote(c["quote"], text) is not None \
                    and len(common.normalize_text(c["quote"]).split()) >= CITATION_QUOTE_WORDS_MIN
            else:
                ok = False
        per_label.append(frozenset(mine))
    if len(per_label) >= 3 and len(set(per_label)) == 1:
        ok = False
    if q is not None and ok:
        own = set(q.get("facts") or [])
        own_sources = {e.get("source_id") for fid in own for e in (ctx.facts.get(fid) or {}).get("evidence", []) if isinstance(e, dict)}
        ok = bool(facts & own) or bool(sources & own_sources)
    return ok, sorted(stored)


def _live_count(ctx, ch, doc):
    return sum(1 for i in _items_of(doc) if i.get("pool") != "drill" and i.get("status") in ("ready", "verified", "candidate"))


def cmd_adjudicate(args):
    ctx = Ctx()
    ch = ctx.chapter(args.chapter)
    if args.select:
        return _select(ctx, ch, args)
    if not args.answers or len(args.answers) != 3:
        return common.fail("q adjudicate needs --answers F1 F2 F3 or --select", common.EXIT_PRECONDITION)
    files = {}
    rounds = set()
    for name in args.answers:
        rows, code = _read_input(name)
        if code is not None:
            return code
        doc = rows[0] if rows and isinstance(rows[0], dict) else {}
        m = re.search(r"-r([0-9])-", str(doc.get("pack", "")))
        if doc.get("lens") not in LENSES or not m or not isinstance(doc.get("answers"), list):
            return common.fail(f"{name}: not an answer file", common.EXIT_PRECONDITION)
        rounds.add(int(m.group(1)))
        files[doc["lens"]] = doc
    if len(files) != 3 or len(rounds) != 1:
        return common.fail("the three answer files must have three different lenses and the same round", common.EXIT_PRECONDITION)
    rnd = rounds.pop()
    path = ctx.data_path(ch, "questions")
    passed, needs_edit, rejected = [], [], []
    with common.file_lock(path):
        doc = common.read_json(path) or {"v": 1, "chapter": ch["slug"], "items": []}
        by_id = {q["id"]: q for q in doc["items"]}
        qids = sorted({a.get("id") for f in files.values() for a in f["answers"] if isinstance(a, dict)}, key=str)
        for qid in qids:
            q = by_id.get(qid)
            ver = (q or {}).get("verification") or {}
            if q is None or ver.get("status") != "candidate" or ver.get("round") != rnd:
                return common.fail(f"{qid}: not a candidate question of round {rnd}", common.EXIT_PRECONDITION)
        problems = _answer_file_problems(ctx, ch, files, rnd, by_id)
        if problems:
            return common.fail("the answer files are refused, nothing was stored: " + "; ".join(problems[:8])
                               + (f"; and {len(problems) - 8} more" if len(problems) > 8 else ""), common.EXIT_PRECONDITION)
        for qid in qids:
            q = by_id[qid]
            key = {o["id"] for o in q["options"] if o["correct"]}
            reasons, solvers = [], []
            for lens in LENSES:
                order = permutation(_seed(ctx), qid, lens, rnd, [o["id"] for o in q["options"]])
                label_to_id = {LABELS[n]: oid for n, oid in enumerate(order)}
                answer = next((a for a in files[lens]["answers"] if isinstance(a, dict) and a.get("id") == qid), None)
                if answer is None:
                    reasons.append(f"{lens} missing")
                    solvers.append({"lens": lens, "answer": [], "agree": False, "flag": None, "solver": str(files[lens].get("solver", "unknown"))})
                    continue
                given = answer.get("answer") if isinstance(answer.get("answer"), list) else []
                mapped = sorted({label_to_id[x] for x in given if x in label_to_id})
                agree = len(mapped) == len(given) and set(mapped) == key
                flag = answer.get("flag") or None
                entry = {"lens": lens, "answer": mapped, "agree": agree, "flag": flag, "solver": str(files[lens].get("solver", "unknown"))}
                if not agree:
                    reasons.append(f"{lens} disagrees")
                if flag:
                    reasons.append(f"{lens} flag")
                if lens == "closed":
                    entry["stem_only"] = answer.get("stem_only")
                if lens == "ambiguity":
                    entry["case_option"] = label_to_id.get((answer.get("case") or {}).get("label")) if isinstance(answer.get("case"), dict) else None
                if lens == "open":
                    ok, stored = _citations(ctx, answer, list(label_to_id), q)
                    entry["citations"], entry["citations_ok"] = stored, ok
                    if not ok:
                        reasons.append("open citations")
                solvers.append(entry)
            ver = q["verification"]
            ver["solvers"] = solvers
            ver["checked"] = common.today()
            if not reasons:
                ver["status"] = "pass" if rnd == 0 else "edited-pass"
                ver["note"] = None
                q["status"] = "verified"
                passed.append(qid)
            elif rnd == 0:
                ver["round"] = 1
                ver["note"] = "; ".join(reasons)
                needs_edit.append({"id": qid, "reasons": reasons})
            else:
                ver["status"] = "rejected"
                ver["note"] = "; ".join(reasons)
                q["status"] = "rejected"
                rejected.append(qid)
        common.write_json(path, doc)
        for qid in rejected:
            common.append_jsonl(common.BUILD / "qbank" / "rejected.jsonl", by_id[qid])
        below = _live_count(ctx, ch, doc) < ctx.counts(ch, "questions").get("shipped", 0)
    result = {"pass": passed, "needs_edit": needs_edit, "rejected": rejected, "below_min": below}
    lines = [f"{e['id']}: needs edit ({', '.join(e['reasons'])})" for e in needs_edit] + [f"{q}: rejected" for q in rejected]
    if getattr(args, "json", False):
        common.emit(result, args)
    else:
        common.emit("\n".join([f"q adjudicate {ch['id']} round {rnd}: pass={len(passed)} needs_edit={len(needs_edit)} rejected={len(rejected)} below_min={below}"] + lines[:40]), args)
    return common.EXIT_FAIL if below else common.EXIT_OK


def _select(ctx, ch, args):
    counts = ctx.counts(ch, "questions")
    path = ctx.data_path(ch, "questions")
    with common.file_lock(path):
        doc = common.read_json(path) or {"v": 1, "chapter": ch["slug"], "items": []}
        cands = [q for q in doc["items"] if q.get("status") in ("verified", "ready") and _verification_passed(q) and q.get("pool") != "drill"]
        by_id = {q["id"]: q for q in cands}
        need = {"core": counts.get("core", 0), "extended": counts.get("extended", 0)}
        multi_lo, multi_hi = _rng(counts.get("multi"))
        worked_n, wrong_n = counts.get("worked", 0), counts.get("worked_wrong_path", 0)
        chosen = []

        def n(pred):
            return sum(1 for q in chosen if pred(q))

        def fits(qs):
            trial = chosen + qs
            return (all(sum(1 for q in trial if q["layer"] == layer) <= need[layer] for layer in need)
                    and sum(1 for q in trial if q["type"] == "multi") <= multi_hi
                    and sum(1 for q in trial if q.get("worked")) <= worked_n
                    and sum(1 for q in trial if (q.get("worked") or {}).get("wrong_path")) <= wrong_n)

        def pref(q):
            have = {b for c in chosen for b in c.get("bullets", [])}
            return (0 if q["verification"]["status"] == "pass" else 1, 0 if set(q.get("bullets", [])) - have else 1, q["id"])

        def free(q):
            return q not in chosen

        pairs = [(by_id[q["twin_of"]], q) for q in cands if q.get("twin_of") in by_id]
        while n(lambda q: q.get("twin_of") and by_id.get(q["twin_of"]) in chosen) < counts.get("twin_pairs_min", 0):
            options = sorted((p for p in pairs if free(p[0]) and free(p[1]) and fits(list(p))), key=lambda p: max(pref(p[0]), pref(p[1])))
            if not options:
                break
            chosen += list(options[0])
        for want_wrong in (True, False):
            while True:
                if want_wrong and n(lambda q: (q.get("worked") or {}).get("wrong_path")) >= wrong_n:
                    break
                if n(lambda q: q.get("worked")) >= worked_n:
                    break
                options = sorted((q for q in cands if free(q) and q.get("worked") and bool(q["worked"].get("wrong_path")) == want_wrong and not q.get("twin_of") and fits([q])), key=pref)
                if not options:
                    break
                chosen.append(options[0])
        for layer in ("core", "extended"):
            while n(lambda q: q["layer"] == layer) < need[layer]:
                options = sorted((q for q in cands if free(q) and q["layer"] == layer and fits([q])), key=pref)
                if not options:
                    break
                chosen.append(options[0])
        while n(lambda q: q["type"] == "multi") < multi_lo:
            swap = None
            for old in reversed(chosen):
                paired = old.get("twin_of") or any(c.get("twin_of") == old["id"] for c in chosen)
                if old["type"] != "single" or old.get("worked") or paired:
                    continue
                new = sorted((q for q in cands if free(q) and q["type"] == "multi" and q["layer"] == old["layer"] and not q.get("worked")), key=pref)
                if new:
                    swap = (old, new[0])
                    break
            if not swap:
                break
            chosen[chosen.index(swap[0])] = swap[1]
        ready = [q for q in chosen]
        have = {"shipped": len(ready), "core": n(lambda q: q["layer"] == "core"), "extended": n(lambda q: q["layer"] == "extended"),
                "twin_pairs": len(_twin_pairs(ready)), "multi": n(lambda q: q["type"] == "multi"),
                "worked": n(lambda q: q.get("worked")), "worked_wrong_path": n(lambda q: (q.get("worked") or {}).get("wrong_path"))}
        ok = (have["shipped"] == counts.get("shipped", 0) and have["core"] == need["core"] and have["extended"] == need["extended"]
              and have["twin_pairs"] >= counts.get("twin_pairs_min", 0) and multi_lo <= have["multi"] <= multi_hi
              and have["worked"] == worked_n and have["worked_wrong_path"] == wrong_n)
        if not ok:
            result = {"ok": False, "have": have, "need": {k: counts.get(k) for k in ("shipped", "core", "extended", "twin_pairs_min", "multi", "worked", "worked_wrong_path")}}
            _emit(args, result, f"q adjudicate --select {ch['id']}: FAIL the counts cannot be met ({have})")
            return common.EXIT_FAIL
        ids = {q["id"] for q in chosen}
        for q in cands:
            q["status"] = "ready" if q["id"] in ids else "verified"
        common.write_json(path, doc)
    result = {"ok": True, "ready": sorted(ids), "verified": sorted(q["id"] for q in cands if q["id"] not in ids), "counts": have}
    _emit(args, result, f"q adjudicate --select {ch['id']}: ready={len(ids)} verified={len(result['verified'])}")
    return common.EXIT_OK


def cmd_dedupe(args):
    ctx = Ctx()
    pairs = dedupe_pairs(ctx, args.threshold)
    dup = [p for p in pairs if p["kind"] == "duplicate"]
    lines = [f"{p['a']} {p['b']} {p['similarity']:.2f} {p['kind']}" for p in pairs[:40]]
    if getattr(args, "json", False):
        common.emit({"pairs": pairs}, args)
    else:
        common.emit("\n".join([f"q dedupe: duplicates={len(dup)} same-signature={len(pairs) - len(dup)}"] + lines), args)
    return common.EXIT_FAIL if dup else (common.EXIT_WARN if pairs else common.EXIT_OK)


def cmd_list(args):
    ctx = Ctx()
    rows = []
    for ch, q in ctx.bank():
        if args.chapter and ch["id"] != ctx.chapter(args.chapter)["id"]:
            continue
        if (args.status and q.get("status") != args.status) or (args.pool and q.get("pool") != args.pool) or (args.task and q.get("task") != args.task):
            continue
        rows.append({"id": q.get("id"), "status": q.get("status"), "verification": (q.get("verification") or {}).get("status"),
                     "difficulty": q.get("difficulty"), "type": q.get("type"), "task": q.get("task"), "concept": q.get("concept")})
    if getattr(args, "json", False):
        common.emit({"questions": rows}, args)
    else:
        common.emit("\n".join([f"q list: {len(rows)} questions"] + [" ".join(str(v) for v in r.values()) for r in rows]), args)
    return common.EXIT_OK


def cmd_words(args):
    ctx = Ctx()
    need = ctx.spec["questions"].get("exam_english_word_min_stems", 0)
    rows = [r for r in word_stems(ctx) if not args.need or r["stems"] < need]
    if getattr(args, "json", False):
        common.emit({"min": need, "words": rows}, args)
    else:
        common.emit("\n".join([f"q words: {len(rows)} words (minimum {need} stems)"] + [f"{r['id']} {r['stems']} {r['word']}" for r in rows]), args)
    return common.EXIT_OK


# ---------------------------------------------------------------- cards build, speak set-pack

def _partner(term, collocation):
    term_tokens = {t.lower() for t in re.findall(r"[A-Za-z0-9-]+", term)}
    for m in re.finditer(r"[A-Za-z0-9-]+", collocation):
        w = m.group(0)
        if w.lower() not in term_tokens and w.lower() not in _ARTICLES and w.lower().rstrip("s") not in term_tokens:
            return collocation[:m.start()] + "___" + collocation[m.end():], w
    return None, None


def _generated_sets(ctx):
    """{path: (chapter slug, kind tag, [card without id])} for the three generated homes."""
    out = {}
    cards = []
    for t in ctx.terms:
        base = {"deck": "core", "facts": [], "term": t["id"], "word": None, "speak": None, "trap": None, "section": None, "pair": None, "tags": [], "generated": True, "status": "ready", "rev": 1}
        cards.append(dict(base, type="term", front=f"Which term means: {t['meaning']}", back=t["term"], extra=t.get("respelling")))
        cards.append(dict(base, type="meaning", front=f"What does \"{t['term']}\" mean?", back=t["meaning"], extra=None))
        for col in t.get("collocations", []):
            front, word = _partner(t["term"], col)
            if front:
                cards.append(dict(base, type="partner", front=front, back=word, extra=col))
    out["terms"] = (common.DATA / "cards-terms.json", "glossary", ("term", "meaning", "partner"), cards)
    ch01 = next((c for c in ctx.chapters() if c["id"] == "01"), None)
    if ch01 is not None:
        cards = []
        for eid, w in ctx.exam_english.items():
            front = re.sub(re.escape(w["word"]), "___", w["stem"], count=1, flags=re.I)
            cards.append({"type": "word", "deck": "exam-english", "front": front, "back": w["word"], "extra": f"{w['meaning']} {w['signals']}", "facts": [], "term": None,
                          "word": eid, "speak": None, "trap": None, "section": None, "pair": None, "tags": [], "generated": True, "status": "ready", "rev": 1})
        out["words"] = (ctx.data_path(ch01, "cards"), ch01["slug"], ("word",), cards)
    ch49 = next((c for c in ctx.chapters() if c["id"] == "49"), None)
    if ch49 is not None:
        cards = []
        for ch in ctx.chapters():
            for s in _active(_items_of(ctx.doc(ch, "speak"))):
                if s.get("pack"):
                    cards.append({"type": "say", "deck": "core", "front": s["prompt"], "back": s["ten_second"], "extra": " / ".join(s.get("skeleton", [])), "facts": [], "term": None,
                                  "word": None, "speak": s["id"], "trap": None, "section": None, "pair": None, "tags": [], "generated": True, "status": "ready", "rev": 1})
        out["say"] = (ctx.data_path(ch49, "cards"), ch49["slug"], ("say",), cards)
    return out


def _card_ref(card):
    return (card.get("type"), card.get("term"), card.get("word"), card.get("speak"), card.get("extra") if card.get("type") == "partner" else None)


def _built_doc(path, slug, types, cards):
    old = common.read_json(path) or {"v": 1, "chapter": slug, "items": []}
    keep = [i for i in old.get("items", []) if i.get("type") not in types]
    ids = {}
    for i in old.get("items", []):
        if i.get("type") in types:
            ids.setdefault(_card_ref(i), i["id"])
    taken = {i["id"] for i in old.get("items", [])}
    items = []
    for c in cards:
        cid = ids.get(_card_ref(c))
        if cid is None or cid in {i["id"] for i in items}:
            cid = _next_id(slug, "c", 3, taken)
            taken.add(cid)
        item = {"id": cid, "chapter": slug}
        item.update(c)
        items.append(item)
    return old, {"v": 1, "chapter": slug, "items": keep + items}


def cmd_cards_build(args):
    ctx = Ctx()
    sets = _generated_sets(ctx)
    written, stale, unchanged = [], [], 0
    for name, (path, slug, types, cards) in sets.items():
        if args.only and name != args.only:
            continue
        if not cards and not path.exists():
            continue
        with common.file_lock(path):
            old, new = _built_doc(path, slug, types, cards)
            if old == new and path.exists():
                unchanged += 1
            elif args.check:
                stale.append(common.rel(path))
            else:
                common.write_json(path, new)
                written.append(common.rel(path))
    if args.check:
        _emit(args, {"stale": stale, "unchanged": unchanged}, f"cards build --check: stale={len(stale)} unchanged={unchanged}" + "".join(f"\n{p}" for p in stale))
        return common.EXIT_FAIL if stale else common.EXIT_OK
    _emit(args, {"written": written, "unchanged": unchanged}, f"cards build: written={len(written)} unchanged={unchanged}" + "".join(f"\n{p}" for p in written))
    return common.EXIT_OK


def _cards_bank_rules(ctx):
    errors, warnings = [], []
    want = ctx.spec["cards"].get("exam_english_cards", 0)
    path = common.DATA / "01-how-the-exam-asks" / "cards.json"
    ctx.note(path)
    doc = common.read_json(path) or {}
    words = [i.get("word") for i in doc.get("items", []) if i.get("type") == "word" and i.get("generated")]
    if want or words:
        if len(words) != want or len(set(words)) != len(words) or set(words) != set(ctx.exam_english):
            errors.append(_f("C202", f"{len(words)} generated word cards; needed {want}, one per word of data/exam-english.json", file="data/01-how-the-exam-asks/cards.json"))
    path = common.DATA / "cards-terms.json"
    if path.exists():
        ctx.note(path)
        doc = common.read_json(path) or {}
        siblings = _items_of(doc)
        for pos, item in enumerate(siblings):
            errors += card_item_rules(ctx, None, item, siblings, pos)
    return errors, warnings


def cmd_set_pack(args):
    ctx = Ctx()
    ch = ctx.chapter(args.chapter)
    path = ctx.data_path(ch, "speak")
    done, missing = [], []
    with common.file_lock(path):
        doc = common.read_json(path) or {"v": 1, "chapter": ch["slug"], "items": []}
        by_id = {i.get("id"): i for i in doc["items"]}
        for sid in args.ids:
            if sid in by_id:
                by_id[sid]["pack"] = not args.off
                done.append(sid)
            else:
                missing.append(sid)
        if done:
            common.write_json(path, doc)
    _emit(args, {"set": done, "pack": not args.off, "missing": missing}, f"speak set-pack: set={len(done)} missing={len(missing)}")
    return common.EXIT_FAIL if missing else common.EXIT_OK


# ---------------------------------------------------------------- mocks

def _mock_cfg(ctx, ch):
    tpl = ctx.template(ch)
    cfg = tpl.get("mock") or {}
    split = cfg.get("domain_split") or (ctx.book.get("book") or {}).get("domain_split") or [0, 0, 0, 0]
    return {"split": list(split), "max_service": cfg.get("max_questions_per_service", 10 ** 9), "minutes": cfg.get("minutes", 130),
            "multi": _rng(ctx.counts(ch, "questions").get("multi"))}


def _mock_counts(questions):
    c = lambda key: dict(sorted(collections.Counter(str(key(q)) for q in questions).items()))
    return {"domains": c(lambda q: q["domain"]), "tasks": c(lambda q: q["task"]), "multi": sum(1 for q in questions if q["type"] == "multi"),
            "difficulty": c(lambda q: q["difficulty"]), "services": c(lambda q: q["services"][0])}


def assemble(ctx, ch, seed=None):
    """(ok, result, manifest or None). Pure: writes nothing."""
    cfg = _mock_cfg(ctx, ch)
    if seed is None:
        seed = _seed(ctx) + int(ch["id"])
    items_ = _items_of(ctx.doc(ch, "questions"))
    cands = sorted((q for q in items_ if q.get("status") in ("verified", "ready") and _verification_passed(q) and q.get("pool") == "mock"
                    and not q.get("volatile") and not ctx.question_volatile(q)), key=lambda q: q["id"])
    rng = random.Random(seed)
    chosen, step1 = [], set()
    used = set()
    svc = collections.Counter()
    order = collections.defaultdict(list)

    def take(q):
        chosen.append(q)
        used.add(q["id"])
        svc[q["services"][0]] += 1
        order[q["domain"]].append(q)

    missing = []
    for task in sorted(t["id"] for t in (ctx.guide or {}).get("tasks", [])):
        pool = [q for q in cands if q["task"] == task and q["id"] not in used]
        if not pool:
            missing.append(task)
            continue
        q = rng.choice(pool)
        take(q)
        step1.add(q["id"])
    multi_lo, multi_hi = cfg["multi"]
    short = []
    for d in (1, 2, 3, 4):
        rest = [q for q in cands if q["domain"] == d and q["id"] not in used]
        rng.shuffle(rest)
        for q in rest:
            if len(order[d]) >= cfg["split"][d - 1]:
                break
            if svc[q["services"][0]] >= cfg["max_service"]:
                continue
            if q["type"] == "multi" and sum(1 for c in chosen if c["type"] == "multi") + 1 > multi_hi:
                continue
            take(q)
        if len(order[d]) != cfg["split"][d - 1]:
            short.append({"domain": d, "need": cfg["split"][d - 1], "have": len(order[d])})
    while not short and sum(1 for c in chosen if c["type"] == "multi") < multi_lo:
        swapped = False
        for d in (1, 2, 3, 4):
            old = next((q for q in reversed(order[d]) if q["type"] == "single" and q["id"] not in step1), None)
            if old is None:
                continue
            for new in (q for q in cands if q["domain"] == d and q["id"] not in used and q["type"] == "multi"):
                if svc[new["services"][0]] - (1 if old["services"][0] == new["services"][0] else 0) < cfg["max_service"]:
                    chosen[chosen.index(old)] = new
                    order[d][order[d].index(old)] = new
                    used.discard(old["id"])
                    used.add(new["id"])
                    svc[old["services"][0]] -= 1
                    svc[new["services"][0]] += 1
                    swapped = True
                    break
            if swapped:
                break
        if not swapped:
            short.append({"domain": None, "need": multi_lo, "have": sum(1 for c in chosen if c["type"] == "multi"), "what": "multi"})
    if short or missing:
        return False, {"mock": ch["id"], "ok": False, "short": short, "missing_tasks": missing}, None
    ids = [q["id"] for q in chosen]
    rng.shuffle(ids)
    spares = [q["id"] for q in cands if q["id"] not in used]
    counts = _mock_counts(chosen)
    manifest = {"v": 1, "mock": ch["slug"], "chapter": ch["id"], "seed": seed, "assembled": common.today(), "minutes": cfg["minutes"],
                "domain_split": cfg["split"], "questions": ids, "spares": spares, "counts": counts}
    return True, {"mock": ch["id"], "ok": True, "seed": seed, "counts": counts, "spares": len(spares)}, manifest


def _mock_targets(ctx, which):
    mocks = ctx.mock_chapters()
    if which in (None, "all"):
        return mocks
    ch = ctx.chapter(which)
    if ch not in mocks:
        raise SystemExit(common.fail(f"chapter {which} is not a mock", common.EXIT_PRECONDITION))
    return [ch]


def cmd_mocks_assemble(args):
    ctx = Ctx()
    if _need_guide(ctx):
        return common.EXIT_PRECONDITION
    results, code = [], common.EXIT_OK
    for ch in _mock_targets(ctx, args.mock):
        mpath, qpath = common.DATA / ctx.dirname(ch) / "mock.json", ctx.data_path(ch, "questions")
        with common.file_lock(mpath), common.file_lock(qpath):
            ctx._c.pop(("doc",), None)
            ok, result, manifest = assemble(ctx, ch, args.seed)
            if ok:
                doc = common.read_json(qpath)
                chosen = set(manifest["questions"])
                spare = set(manifest["spares"])
                for q in doc["items"]:
                    if q.get("id") in chosen:
                        q["status"] = "ready"
                    elif q.get("id") in spare:
                        q["status"] = "verified"
                common.write_json(mpath, manifest)
                common.write_json(qpath, doc)
            else:
                code = common.EXIT_FAIL
        results.append(result)
    if not results:
        return common.fail("no mock chapter in the registry", common.EXIT_PRECONDITION)
    out = results[0] if len(results) == 1 else {"mocks": results}
    _emit(args, out, "mocks assemble: " + "; ".join(f"{r['mock']} {'ok seed=' + str(r['seed']) if r['ok'] else 'FAIL short=' + str(r['short']) + ' missing_tasks=' + str(r['missing_tasks'])}" for r in results))
    return code


def mock_check(ctx, ch, manifests, dupes):
    cfg = _mock_cfg(ctx, ch)
    rel = f"data/{ctx.dirname(ch)}/mock.json"
    errors, warnings = [], []

    def add(code, msg, item=None):
        errors.append(_f(code, msg, item=item, file=rel))

    manifest = manifests.get(ch["id"])
    if manifest is None:
        add("K01", "no mock.json; run mocks assemble")
        return {"mock": ch["id"], "ok": False, "errors": errors, "warnings": warnings, "counts": {}}
    for e in schemas.validate(manifest, "mock")[:8]:
        add("K01", "schema: " + e)
    ids = [i for i in manifest.get("questions", []) if isinstance(i, str)] if isinstance(manifest.get("questions"), list) else []
    if len(set(ids)) != sum(cfg["split"]) or len(ids) != len(set(ids)):
        add("K01", f"{len(set(ids))} unique ids; needed {sum(cfg['split'])}")
    own = {q["id"]: q for q in _items_of(ctx.doc(ch, "questions")) if q.get("id")}
    bank = {q.get("id"): (c, q) for c, q in ctx.bank()}
    other = {i for cid, m in manifests.items() if cid != ch["id"] and m for i in m.get("questions", [])}
    qs = []
    for i in ids:
        q = own.get(i)
        if q is None or q.get("pool") != "mock":
            add("K01", "not a pool-mock question of this mock's file", item=i)
        else:
            qs.append(q)
        if i in other:
            add("K04", "also in the other mock", item=i)
        if i in bank and bank[i][1].get("pool") in ("chapter", "drill"):
            add("K04", f"reuses a {bank[i][1].get('pool')} question", item=i)
    idset = set(ids)
    for p in dupes:
        if p["kind"] != "duplicate":
            continue
        for n, (mine, theirs) in enumerate(((p["a"], p["b"]), (p["b"], p["a"]))):
            # gate-break H28, H29: also a copy inside this mock, and a copy of a drill question
            if mine in idset and (theirs in other or (theirs in idset and n == 1)
                                  or (theirs in bank and bank[theirs][1].get("pool") in ("chapter", "drill"))):
                add("K04", f"near-duplicate of {theirs} (similarity {p['similarity']})", item=mine)
    # gate-break H30: the web app reads minutes from this file; the stored numbers are the computed ones
    if manifest.get("minutes") != cfg["minutes"]:
        add("K01", f"minutes is {manifest.get('minutes')}; the template says {cfg['minutes']}")
    if manifest.get("domain_split") != cfg["split"]:
        add("K01", f"domain_split is {manifest.get('domain_split')}; the template says {cfg['split']}")
    for d in (1, 2, 3, 4):
        n = sum(1 for q in qs if q.get("domain") == d)
        if n != cfg["split"][d - 1]:
            add("K02", f"domain {d}: {n} questions; needed {cfg['split'][d - 1]}")
    have_tasks = {q.get("task") for q in qs}
    for t in sorted(t["id"] for t in (ctx.guide or {}).get("tasks", [])):
        if t not in have_tasks:
            add("K03", f"task statement {t} is missing")
    svc = collections.Counter()
    for q in qs:
        if q.get("volatile") or ctx.question_volatile(q):
            add("K05", "volatile question", item=q["id"])
        if q.get("status") != "ready" or not _verification_passed(q):
            add("K08", "not ready with a passed verification", item=q["id"])
        if q.get("services"):
            svc[q["services"][0]] += 1
    for s, n in sorted(svc.items()):
        if n > cfg["max_service"]:
            add("K06", f"focus service {s} has {n} questions; at most {cfg['max_service']}")
    multi = sum(1 for q in qs if q.get("type") == "multi")
    if not cfg["multi"][0] <= multi <= cfg["multi"][1]:
        add("K07", f"{multi} multi questions; allowed {cfg['multi'][0]} to {cfg['multi'][1]}")
    for msg in _q202(ctx, qs):
        add("K09", msg)
    counts = _mock_counts([q for q in qs if q.get("services") and "domain" in q and "task" in q and "difficulty" in q and "type" in q])
    if manifest.get("counts") != counts:
        add("K01", "the counts in mock.json are not the counts of its questions; run mocks assemble")
    return {"mock": ch["id"], "ok": not errors, "errors": errors, "warnings": warnings, "counts": counts}


def cmd_mocks_check(args):
    ctx = Ctx()
    if _need_guide(ctx):
        return common.EXIT_PRECONDITION
    targets = _mock_targets(ctx, args.mock)
    if not targets:
        return common.fail("no mock chapter in the registry", common.EXIT_PRECONDITION)
    manifests = {ch["id"]: common.read_json(common.DATA / ctx.dirname(ch) / "mock.json") for ch in ctx.mock_chapters()}
    dupes = dedupe_pairs(ctx)
    results = [mock_check(ctx, ch, manifests, dupes) for ch in targets]
    done = [r for r in results if r["counts"]]
    for a in range(len(done)):
        for b in range(a + 1, len(done)):
            for d in ("1", "2", "3"):
                sa = done[a]["counts"]["difficulty"].get(d, 0) / max(1, sum(done[a]["counts"]["difficulty"].values()))
                sb = done[b]["counts"]["difficulty"].get(d, 0) / max(1, sum(done[b]["counts"]["difficulty"].values()))
                if abs(sa - sb) > 0.05 + 1e-9:
                    done[b]["warnings"].append(_f("K10", f"difficulty {d}: share {sb:.2f} here, {sa:.2f} in mock {done[a]['mock']}"))
    errors = [f for r in results for f in r["errors"]]
    warnings = [f for r in results for f in r["warnings"]]
    _emit(args, {"mocks": results}, "mocks check: " + " ".join(f"{r['mock']}={'ok' if r['ok'] else 'FAIL'}" for r in results) + f" errors={len(errors)} warnings={len(warnings)}", errors + warnings)
    return _exit(errors, warnings)


# ---------------------------------------------------------------- drills

def cmd_drills_build(args):
    ctx = Ctx()
    if _need_guide(ctx):
        return common.EXIT_PRECONDITION
    seed = args.seed if args.seed is not None else _seed(ctx)
    cands = sorted(((ch, q) for ch, q in ctx.bank() if q.get("status") == "ready" and _verification_passed(q)
                    and (q.get("pool") == "drill" or (q.get("pool") == "chapter" and q.get("layer") == "extended"))), key=lambda cq: cq[1]["id"])
    drills, shorts = [], []
    for d in (1, 2, 3, 4):
        rng = random.Random(seed + d)
        pool = [(ch, q) for ch, q in cands if q.get("domain") == d]
        per_chapter = collections.Counter()
        picked = []

        def take(ch, q):
            picked.append(q["id"])
            per_chapter[ch["id"]] += 1

        for task in sorted(t["id"] for t in ctx.guide.get("tasks", []) if t.get("domain") == d):
            options = [(ch, q) for ch, q in pool if q.get("task") == task and q["id"] not in picked and per_chapter[ch["id"]] < 2]
            if options and len(picked) < args.size:
                take(*rng.choice(options))
        rest = [(ch, q) for ch, q in pool if q["id"] not in picked]
        rng.shuffle(rest)
        for ch, q in rest:
            if len(picked) >= args.size:
                break
            if per_chapter[ch["id"]] < 2:
                take(ch, q)
        if len(picked) < args.size:
            shorts.append(_f("K21", f"drill-d{d} has {len(picked)} questions; wanted {args.size}", file="data/drills.json"))
        drills.append({"id": f"drill-d{d}", "domain": d, "title": f"Domain {d} drill", "questions": picked})
    path = common.DATA / "drills.json"
    with common.file_lock(path):
        common.write_json(path, {"v": 1, "seed": seed, "drills": drills})
    result = {"written": common.rel(path), "seed": seed, "drills": {d["id"]: len(d["questions"]) for d in drills}, "warnings": shorts}
    _emit(args, result, f"drills build: seed={seed} " + " ".join(f"{d['id']}={len(d['questions'])}" for d in drills), shorts)
    return common.EXIT_WARN if shorts else common.EXIT_OK


def cmd_drills_check(args):
    ctx = Ctx()
    path = common.DATA / "drills.json"
    doc = common.read_json(path)
    if doc is None:
        return common.fail("no data/drills.json; run drills build", common.EXIT_PRECONDITION)
    errors = [_f("K20", "schema: " + e, file="data/drills.json") for e in schemas.validate(doc, "drills")[:8]]
    bank = {q.get("id"): q for _, q in ctx.bank()}
    in_mock = {i for ch in ctx.mock_chapters() for i in (common.read_json(common.DATA / ctx.dirname(ch) / "mock.json") or {}).get("questions", [])}
    for drill in doc.get("drills", []) if isinstance(doc.get("drills"), list) else []:
        for qid in drill.get("questions", []):
            q = bank.get(qid)
            if q is None:
                errors.append(_f("K22", "no such question", item=qid, file="data/drills.json"))
            elif q.get("status") != "ready":
                errors.append(_f("K22", f"status {q.get('status')}, not ready", item=qid, file="data/drills.json"))
            elif q.get("domain") != drill.get("domain"):
                errors.append(_f("K22", f"belongs to domain {q.get('domain')}, not {drill.get('domain')}", item=qid, file="data/drills.json"))
            elif qid in in_mock or q.get("pool") == "mock":
                errors.append(_f("K22", "is a mock question", item=qid, file="data/drills.json"))
    result = {"ok": not errors, "errors": errors, "drills": {d.get("id"): len(d.get("questions", [])) for d in doc.get("drills", []) if isinstance(d, dict)}}
    _emit(args, result, f"drills check: {'ok' if not errors else 'FAIL'} errors={len(errors)}", errors)
    return common.EXIT_FAIL if errors else common.EXIT_OK


# ---------------------------------------------------------------- command line

def _leaf(sub, name, help_text, func):
    p = sub.add_parser(name, help=help_text)
    common.add_common_args(p)
    p.set_defaults(func=func)
    return p


def _group(subparsers, name, help_text):
    p = subparsers.add_parser(name, help=help_text)
    p.set_defaults(func=lambda a, p=p: (p.print_help(), common.EXIT_PRECONDITION)[1])
    return p.add_subparsers(dest=f"{name}_cmd")


def _add_parsers(sub, kind):
    p = _leaf(sub, "add", "add or replace items from a JSON file", lambda a: cmd_add(a, kind))
    p.add_argument("--chapter", required=True)
    p.add_argument("--file", required=True)
    p.add_argument("--replace", action="store_true")
    p.add_argument("--by")
    p = _leaf(sub, "lint", "check the items of a chapter, or of the whole bank", lambda a: cmd_lint(a, kind))
    p.add_argument("chapter", nargs="?")
    p.add_argument("--all", action="store_true")
    p.add_argument("--ship", action="store_true")
    p = _leaf(sub, "set-status", "set the status of items", lambda a: cmd_set_status(a, kind))
    p.add_argument("--chapter", required=True)
    p.add_argument("--status", required=True, choices=["ready", "verified", "retired", "rejected"])
    p.add_argument("ids", nargs="+", metavar="ID")
    p.add_argument("--by")
    p.add_argument("--reason")


def register(subparsers):
    q = _group(subparsers, "q", "question bank: add, lint, pack, adjudicate, dedupe, list, set-status, words")
    _add_parsers(q, "questions")
    p = _leaf(q, "pack", "write a blind pack for one solver lens", cmd_pack)
    p.add_argument("--chapter", required=True)
    p.add_argument("--lens", required=True, choices=LENSES)
    p.add_argument("--round", type=int, default=0)
    p.add_argument("--ids", nargs="+")
    p = _leaf(q, "adjudicate", "apply three solver answer files, or choose the shipped set", cmd_adjudicate)
    p.add_argument("--chapter", required=True)
    p.add_argument("--answers", nargs="+")
    p.add_argument("--select", action="store_true")
    p = _leaf(q, "dedupe", "find near-duplicate stems in the whole bank", cmd_dedupe)
    p.add_argument("--threshold", type=float, default=0.6)
    p = _leaf(q, "list", "list questions", cmd_list)
    p.add_argument("--chapter")
    p.add_argument("--status")
    p.add_argument("--pool")
    p.add_argument("--task")
    p = _leaf(q, "words", "exam-English words and the stems that use them", cmd_words)
    p.add_argument("--need", action="store_true")

    cards = _group(subparsers, "cards", "flashcards: add, lint, set-status, build")
    _add_parsers(cards, "cards")
    p = _leaf(cards, "build", "write the generated cards", cmd_cards_build)
    p.add_argument("--only", choices=["terms", "words", "say"])
    p.add_argument("--check", action="store_true")

    speak = _group(subparsers, "speak", "spoken answers: add, lint, set-status, set-pack")
    _add_parsers(speak, "speak")
    p = _leaf(speak, "set-pack", "set the pack flag of speak items", cmd_set_pack)
    p.add_argument("--chapter", required=True)
    p.add_argument("ids", nargs="+", metavar="ID")
    p.add_argument("--off", action="store_true")

    mocks = _group(subparsers, "mocks", "mock exams: assemble, check")
    p = _leaf(mocks, "assemble", "choose the questions of a mock", cmd_mocks_assemble)
    p.add_argument("--mock", default="all")
    p.add_argument("--seed", type=int)
    p = _leaf(mocks, "check", "verify a mock manifest", cmd_mocks_check)
    p.add_argument("--mock", default="all")

    drills = _group(subparsers, "drills", "domain drills: build, check")
    p = _leaf(drills, "build", "write data/drills.json", cmd_drills_build)
    p.add_argument("--seed", type=int)
    p.add_argument("--size", type=int, default=20)
    _leaf(drills, "check", "verify data/drills.json", cmd_drills_check)
